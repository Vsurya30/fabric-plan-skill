"""Independent API regressions: mocks only, portable paths, synthetic data."""
import copy
import json
import os
from pathlib import Path
import runpy
import shutil
import socket
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime.codec import load, loads, pack, unpack
from runtime.home_api import decode_roles, deploy_home
from runtime.identity import Registry
from runtime.layout import audit
from runtime.pivots import compile_pivots
from runtime.transport import Client
from runtime.workflow import preflight, provision

TOKEN_ENV = 'FABRIC_PLAN_INDEPENDENT_TEST_TOKEN'


def rectangle(x=20, y=20, width=200, height=100):
    return {'position': {'x': x, 'y': y}, 'dimension': {'width': width, 'height': height}}


def native_page():
    state = {'pivot': {'configs': [{'id': '301', 'name': 'Summary', 'hidden': False}], 'active_id': None},
             'pivotExplorer': {'activePivot': None}, 'manage_measures': [{'id': '401'}]}
    props = {**rectangle(), 'visualState': state, 'pivotAssignments': []}
    return {'statusCode': 200, 'payload': {'etag': 'page-1',
        'properties': {'properties': {'canvasStyle': {'dimension': {
            'width': 600, 'height': 500, 'elementScalingUnit': 'pixel'}},
            'pageFilter': 'preserve', 'reactiveVisualProperties': []}},
        'visuals': [{'id': '101', 'visualType': 80,
                     'properties': {'etag': 'visual-1', 'properties': props}}]}}


class PageAdapter:
    def __init__(self, lose_response=False):
        self.state = native_page()
        self.writes = 0
        self.lose_response = lose_response

    def __call__(self, method, url, headers, body):
        if method == 'GET':
            return {'status': 200, 'headers': {}, 'body': copy.deepcopy(self.state)}
        incoming = loads(body.decode('utf-8'))
        self.writes += 1
        for vid, wrapped in incoming['visuals'].items():
            target = next(v for v in self.state['payload']['visuals'] if v['id'] == vid)
            target['properties'] = {**copy.deepcopy(wrapped), 'etag': 'visual-' + str(self.writes + 1)}
        for wrapped in incoming['workloadEntities'].values():
            self.state['payload']['properties'] = copy.deepcopy(wrapped)
        self.state['payload']['etag'] = 'page-' + str(self.writes + 1)
        if self.lose_response:
            self.lose_response = False
            raise OSError('Simulated response loss after write applied')
        return {'status': 200, 'headers': {}, 'body': {'statusCode': 200, 'payload': {}}}


class HomeAdapter:
    def __init__(self):
        self.data = self.etag = self.order = None
        self.writes = 0

    def __call__(self, method, url, headers, body):
        if url.endswith('/layout/'):
            payload = {'__everyone__': {'homeLayoutOrder': self.order, 'homeLayoutEnabled': True}}
        elif method == 'GET':
            payload = {'data': self.data, 'etag': self.etag}
        else:
            incoming = loads(body.decode('utf-8'))
            self.writes += 1
            self.data, self.order = incoming['data'], incoming['homeLayoutOrder']
            self.etag = 'home-' + str(self.writes)
            payload = {'etag': self.etag}
        return {'status': 200, 'headers': {}, 'body': {'statusCode': 200, 'payload': copy.deepcopy(payload)}}


class WorkflowServer:
    def __init__(self, mutate_policy=False, create_lro=False, update_lro=False, lose_update=False):
        self.raw = {'definition.json': {'sheets': [], 'serverUnknownInitialization': {'retainMe': True}},
                    'planProperties.json': {'properties': {'serverUnknownDefault': 'retain-me'}}}
        self.creates = self.updates = 0
        self.mutate_policy, self.create_lro = mutate_policy, create_lro
        self.update_lro, self.lose_update = update_lro, lose_update
        self.expired_create = self.expired_update = False

    def public(self, method, url, headers, body):
        if method == 'POST' and url.endswith('/plans'):
            self.creates += 1
            self.raw=unpack(loads(body.decode('utf-8')))
            if self.create_lro:
                return self.pending('create')
            payload = {'id': 'synthetic-plan'}
        elif '/operations/create' in url:
            if self.expired_create:
                return {'status': 410, 'headers': {}, 'body': {'error': 'Expired operation'}}
            payload = {'id': 'synthetic-plan'} if url.endswith('/result') else {'status': 'Succeeded'}
        elif '/operations/update' in url:
            if self.expired_update:
                return {'status': 410, 'headers': {}, 'body': {'error': 'Expired operation'}}
            payload = {} if url.endswith('/result') else {'status': 'Succeeded'}
        elif url.endswith('/getDefinition'):
            payload = pack(self.raw)
        elif url.endswith('/updateDefinition'):
            self.updates += 1
            self.raw = unpack({'definition': loads(body.decode('utf-8'))['definition']})
            if self.mutate_policy:
                path = next(p for p in self.raw if p.endswith('/dataInput.json'))
                record = next(c for c in self.raw[path]['columns'] if 'DataInput' in c['columnMeta']['measure_type'])
                record['columnMeta']['measure_type']['DataInput']['allow_input'] = 'Edit'
            if self.lose_update:
                self.lose_update = False
                raise OSError('Simulated response loss after update applied')
            if self.update_lro:
                return self.pending('update')
            payload = {}
        else:
            raise AssertionError('Unexpected mocked route: ' + url)
        return {'status': 201 if url.endswith('/plans') else 200, 'headers': {}, 'body': payload}

    @staticmethod
    def pending(operation):
        return {'status': 202, 'headers': {
            'location': 'https://example.invalid/v1/operations/' + operation, 'retry-after': '0'}, 'body': {}}

    def native(self, method, url, headers, body):
        raise AssertionError('Unexpected mocked native route: ' + url)


class IndependentApiTests(unittest.TestCase):
    def test_model_cli_discovers_tmdl_twice_without_recipe_or_native_flag(self):
        import base64
        from contextlib import redirect_stdout
        from io import StringIO

        api = 'https://example.invalid/v1'
        config = self.directory / 'destination.json'
        config.write_text(json.dumps({'apiBase': api, 'tokenEnvironment': TOKEN_ENV,
            'modelReference': {'semanticModelWorkspaceId': 'workspace', 'semanticModelId': 'model'}}))
        run = self.directory / 'discovery'
        model_route = api + '/workspaces/workspace/semanticModels/model'
        definition = model_route + '/getDefinition?format=TMDL'
        operations = []
        tmdl = "table 'Sales Data'\n\tcolumn Country\n\t\tdataType: string\n\tmeasure 'Gross Revenue' = 1\n\t\tformatString: #,0\n"
        envelope = {'definition': {'parts': [{'path': 'definition/tables/Sales Data.tmdl',
            'payloadType': 'InlineBase64', 'payload': base64.b64encode(tmdl.encode()).decode()}]}}

        def respond(client, method, url, headers, body):
            status, metadata = 200, {}
            if (method, url) == ('GET', model_route):
                payload = {'displayName': 'Sales model'}
            elif (method, url) == ('POST', definition):
                operations.append(api + '/operations/' + str(len(operations) + 1))
                status, metadata, payload = 202, {'location': operations[-1], 'retry-after': '0'}, {}
            elif method == 'GET' and url in operations:
                payload = {'status': 'Succeeded'}
            elif method == 'GET' and url == operations[-1] + '/result':
                payload = envelope
            else:
                self.fail(f'Unexpected discovery request: {method} {url}')
            return {'status': status, 'headers': metadata, 'body': payload}

        argv = ['plan.py', 'usecase', 'model', '--config', str(config), '--run', str(run)]
        with patch.object(sys, 'argv', argv), patch.object(Client, '_http', respond), redirect_stdout(StringIO()):
            for _ in range(2):
                runpy.run_path(str(ROOT / 'plan.py'), run_name='__main__')
        self.assertEqual(len(operations), 2)
        model = load(run / 'current-model.json')
        self.assertEqual(model['reference']['semanticModelName'], 'Sales model')
        self.assertEqual([(f['id'], f['dataType']) for f in model['fields']],
                         [('Sales Data[Country]', 'String'), ('Sales Data[Gross Revenue]', 'Double')])
        self.assertEqual(load(run / 'model-definition.json'), envelope)

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        (self.directory / 'temp').mkdir()
        env = patch.dict(os.environ, {TOKEN_ENV: 'synthetic-test-token',
            'TEMP': str(self.directory / 'temp'), 'TMP': str(self.directory / 'temp')})
        env.start()
        self.addCleanup(env.stop)
        self.network = patch.object(socket.socket, 'connect', side_effect=AssertionError('Network forbidden'))
        self.network.start()
        self.addCleanup(self.network.stop)

    def client(self, name, adapter):
        return Client('https://example.invalid/native', TOKEN_ENV, journal=self.directory / name,
                      adapter=adapter, sleep=lambda seconds: None)



    def test_orphan_override_is_not_a_complete_inventory(self):
        page = native_page()
        page['payload']['properties']['properties']['reactiveVisualProperties'] = [
            {'visualId': '102', 'properties': rectangle()}]
        with self.assertRaisesRegex(ValueError, 'Orphan'):
            audit(page)


    def test_false_string_does_not_enable_cross_axis_capability(self):
        sheet = {'sheetId': 'sheet', 'rows': ['Employee'], 'columns': ['Month'],
            'dimensions': {'Employee': '501', 'Month': '502'}, 'measures': {'Hours': '503'}}
        with self.assertRaisesRegex(ValueError, 'Boolean'):
            compile_pivots([{'name': 'Swap', 'rows': ['Month'], 'columns': ['Employee']}], sheet, Registry(),
                capabilities={'PlanningCrossPivot': 'false', 'PlanningColumnPivot': 'false'})

    def test_compressed_roles_preserve_unicode_and_u64(self):
        node = os.environ.get('FABRIC_PLAN_NODE') or shutil.which('node')
        if not node:
            self.skipTest('Optional Node runtime unavailable for LZUTF8 test')
        text = '{"__everyone__":{"title":"R\u00e9sum\u00e9 \u2013 \u6d4b\u8bd5","runtimeId":18446744073709551615}}'
        program = "const fs=require('node:fs');const lz=require(process.argv[1]);process.stdout.write(lz.compress(fs.readFileSync(0,'utf8'),{outputEncoding:'Base64'}));"
        compressed = subprocess.run([node, '-e', program, str(ROOT / 'vendor/lzutf8/lzutf8.js')],
            input=text.encode('utf-8'), capture_output=True, check=True, timeout=30).stdout.decode('ascii')
        self.assertEqual(decode_roles(compressed, node), json.loads(text))

    def test_native_home_rejects_traversal_label_before_any_api(self):
        cli = runpy.run_path(str(ROOT / 'plan.py'), run_name='independent_cli_test')
        argv = ['plan.py', 'native', 'home', '--config', 'unused', '--input', 'unused',
                '--run', str(self.directory / 'run'), '--label', '../escaped']
        with patch.object(sys, 'argv', argv), patch('runtime.session.native_session') as session:
            with self.assertRaisesRegex(ValueError, 'Unsafe operation label'):
                cli['main']()
            session.assert_not_called()


class WorkflowRegressionTests(unittest.TestCase):
    setUp = IndependentApiTests.setUp

    def inputs(self):
        model = load(ROOT / 'fixtures/model.json')
        spec = {'name': 'Synthetic Capacity', 'requiredCapabilities': [
            'planning.numeric', 'planning.native-measure', 'planning.conditional-edit-policy'],
            'sheets': [{'name': 'Capacity', 'rows': ['Employee[Employee]'], 'columns': ['Period[Month]'],
                'measures': [
                    {'key': 'allowed', 'kind': 'Native', 'source': 'Metrics[CanEdit]', 'label': 'CanEdit'},
                    {'key': 'hours', 'kind': 'DataInput', 'label': 'Available Hours',
                     'min_value': {'Static': 0}, 'allow_input': {'BasedOnFormula': '${allowed} > 0'}}]}]}
        config = {'apiBase': 'https://example.invalid/v1', 'powerbiApiBase': 'https://example.invalid',
            'workspaceId': 'workspace', 'name': spec['name'], 'tokenEnvironment': TOKEN_ENV, 'authorizedMutation': True}
        return config, model, spec

    def run_workflow(self, server, directory):
        config, model, spec = self.inputs()
        def client(base, env, allowed=None, journal=None):
            return Client(base, env, allowed, journal, server.public, sleep=lambda seconds: None)
        @contextmanager
        def native(base, env, workspace, plan, journal):
            yield Client('https://example.invalid/native', env, journal=journal,
                         adapter=server.native, sleep=lambda seconds: None)
        with patch('runtime.workflow.Client', client), patch('runtime.workflow.native_session', native):
            return provision(config, model, spec, directory)

    def test_native_calls_for_standard_provision_are_only_home(self):
        server = WorkflowServer()
        observed = []
        original = server.native
        def native(method, url, headers, body):
            observed.append((method, url))
            return original(method, url, headers, body)
        server.native = native
        result = self.run_workflow(server, self.directory / 'restricted')
        self.assertTrue(observed)
        self.assertTrue(all('/v1/access/roles/layout/' in url for method,url in observed))
        self.assertEqual(result['dashboards'][0]['geometrySource'],'public-create')
        self.assertEqual(result['visibilitySource'],'public-create')
    def test_successful_layout_and_home_complete_the_new_report(self):
        server = WorkflowServer()
        with patch('runtime.workflow.deploy_home',return_value={'write':'submitted'}) as home:
            result = self.run_workflow(server, self.directory / 'successful')
        home.assert_called_once()
        self.assertEqual((server.creates,server.updates),(1,0))
        self.assertTrue(result['originalScopeComplete'],result['phaseErrors'])
        self.assertEqual(result['mandatoryDefaults']['dashboardSaves'],1)
    def test_public_create_contains_visibility_and_complete_grid(self):
        server = WorkflowServer()
        self.run_workflow(server, self.directory / 'create')
        flags = {s['sheetType']:s['isHidden'] for s in server.raw['definition.json']['sheets']}
        self.assertEqual(flags, {'PLANNING':True, 'REPORTING':False})
        self.assertTrue(server.raw['planProperties.json']['properties']['homeLayout']['show'])
        records = next(v['columns'] for k,v in server.raw.items() if k.endswith('/dataInput.json'))
        rule = next(c['columnMeta']['measure_type']['DataInput'] for c in records
                    if 'DataInput' in c['columnMeta']['measure_type'])
        self.assertIsInstance(rule['allow_input'], dict)
        self.assertEqual((server.creates, server.updates), (1, 0))

    def test_completed_create_resume_does_not_recreate_or_publish(self):
        server = WorkflowServer(create_lro=True)
        directory = self.directory / 'create-expiry'
        self.run_workflow(server, directory)
        server.expired_create = True
        self.run_workflow(server, directory)
        self.assertEqual((server.creates, server.updates), (1, 0))



    def test_hidden_dashboard_is_rejected_before_create(self):
        from runtime.application_defaults import require_business_navigation
        raw = {'definition.json': {'sheets': [
            {'sheetType':'REPORTING','displayName':'Revenue','isHidden':True}]}}
        with self.assertRaisesRegex(ValueError,'public create'):
            require_business_navigation(raw)

    def test_invalid_home_controls_fail_preflight(self):
        for bad in ({'order': -1}, {'order': True}, {'show': 'false'}, {'roleId': ''}):
            with self.subTest(control=bad):
                _, _, spec = self.inputs()
                spec['requiredCapabilities'] += ['home.text', 'home.visibility']
                spec['home'] = {'blocks': [{'key': 'intro', 'type': 'text', 'title': 'Capacity'}],
                    'rows': [{'blocks': ['intro']}], **bad}
                with self.assertRaises(ValueError):
                    preflight(spec)


if __name__ == '__main__':
    unittest.main()
