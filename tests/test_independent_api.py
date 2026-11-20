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
from runtime.activation import select_saved_pivot
from runtime.codec import load, loads, pack, unpack
from runtime.home_api import decode_roles, deploy_home
from runtime.identity import Registry
from runtime.layout import audit, place_native, verify_unchanged
from runtime.pivots import compile_pivots
from runtime.session import resolve_planning
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
        sheet = self.raw['definition.json']['sheets'][0]
        owner = sheet['workloadItemEntityVisuals'][0]
        prefix = 'sheets/' + sheet['recordGuid'] + '/visuals/' + owner['visualId'] + '/'
        if url.endswith('/entity/'):
            payload = {'workloadEntities': [{'id': '201', 'displayName': sheet['displayName'], 'entityType': 10}]}
        elif '/datainput/column/' in url:
            columns = self.raw[prefix + 'dataInput.json']['columns']
            payload = {'resBody': columns, 'totalRecordCount': len(columns)}
        elif url.endswith('/properties/'):
            payload = {'etag': 'page-1', 'visuals': [{'id': '101', 'visualType': 80,
                'properties': {'etag': 'visual-1', 'properties': self.raw[prefix + 'properties.json']['properties']}}]}
        else:
            raise AssertionError('Unexpected mocked native route: ' + url)
        return {'status': 200, 'headers': {}, 'body': {'statusCode': 200, 'payload': copy.deepcopy(payload)}}


class IndependentApiTests(unittest.TestCase):
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

    def test_completed_native_actions_reconcile_without_second_write(self):
        actions = [
            ('pivot', PageAdapter(), lambda c: select_saved_pivot(c, '201', '101', '301', 'same-step')),
            ('place', PageAdapter(), lambda c: place_native(c, '201', '101',
                {'x': 30, 'y': 40, 'width': 200, 'height': 100}, 'same-step')),
            ('home', HomeAdapter(), lambda c: deploy_home(c, '__everyone__',
                {'items': [], 'rows': []}, 1, 'same-step'))]
        for name, adapter, action in actions:
            with self.subTest(action=name):
                client = self.client(name, adapter)
                action(client)
                result = action(client)
                self.assertEqual(result['write'], 'already-matched')
                self.assertEqual(adapter.writes, 1)

    def test_pivot_applied_before_response_loss_reconciles(self):
        adapter = PageAdapter(lose_response=True)
        client = self.client('lost-pivot', adapter)
        with self.assertRaisesRegex(RuntimeError, 'interrupted'):
            select_saved_pivot(client, '201', '101', '301', 'pivot')
        self.assertEqual(select_saved_pivot(client, '201', '101', '301', 'pivot')['write'], 'already-matched')
        self.assertEqual(adapter.writes, 1)

    def test_orphan_override_is_not_a_complete_inventory(self):
        page = native_page()
        page['payload']['properties']['properties']['reactiveVisualProperties'] = [
            {'visualId': '102', 'properties': rectangle()}]
        with self.assertRaisesRegex(ValueError, 'Orphan'):
            audit(page)

    def test_unrelated_page_property_drift_fails_readback(self):
        before = native_page()
        after = copy.deepcopy(before)
        after['payload']['properties']['properties']['pageFilter'] = 'unexpected change'
        with self.assertRaisesRegex(ValueError, 'Unrelated page'):
            verify_unchanged(before, after, '101', {'x': 20, 'y': 20, 'width': 200, 'height': 100})

    def test_duplicate_native_registrations_are_not_hidden_by_sets(self):
        raw = {'definition.json': {'sheets': [{'recordGuid': 'sheet-guid', 'displayName': 'Capacity',
            'sheetType': 'PLANNING', 'workloadItemEntityVisuals': [
                {'visualId': 'visual-guid', 'visualType': 'PLANNING', 'isEmbedded': False}]}]},
            'sheets/sheet-guid/visuals/visual-guid/properties.json': {'properties': {'pivotAssignments': []}},
            'sheets/sheet-guid/visuals/visual-guid/dataInput.json': {'columns': [{'measureGuid': '401'}]}}
        for duplicate in ('columns', 'registry'):
            with self.subTest(duplicate=duplicate):
                page = native_page()
                if duplicate == 'registry':
                    page['payload']['visuals'][0]['properties']['properties']['visualState']['manage_measures'] *= 2
                def adapter(method, url, headers, body):
                    if '/datainput/column/' in url:
                        records = [{'measureGuid': '401'}] * (2 if duplicate == 'columns' else 1)
                        payload = {'resBody': records, 'totalRecordCount': len(records)}
                    elif url.endswith('/entity/'):
                        payload = {'workloadEntities': [{'id': '201', 'displayName': 'Capacity', 'entityType': 10}]}
                    else:
                        return {'status': 200, 'headers': {}, 'body': page}
                    return {'status': 200, 'headers': {}, 'body': {'statusCode': 200, 'payload': payload}}
                with self.assertRaisesRegex(ValueError, 'Duplicate'):
                    resolve_planning(self.client(duplicate, adapter), raw)

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

    def test_native_verify_rejects_traversal_label_before_any_api(self):
        cli = runpy.run_path(str(ROOT / 'plan.py'), run_name='independent_cli_test')
        argv = ['plan.py', 'native', 'verify', '--config', 'unused', '--input', 'unused',
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
        def native(base, env, workspace, plan, journal, native_read_versions=None):
            yield Client('https://example.invalid/native', env, journal=journal,
                         adapter=server.native, sleep=lambda seconds: None)
        with patch('runtime.workflow.Client', client), patch('runtime.workflow.native_session', native):
            return provision(config, model, spec, directory)

    def test_dropped_conditional_edit_policy_fails_authored_readback(self):
        server = WorkflowServer(mutate_policy=True)
        with self.assertRaisesRegex(ValueError, 'allow_input'):
            self.run_workflow(server, self.directory / 'policy')
        self.assertFalse((self.directory / 'policy/acceptance.json').exists())

    def test_unknown_blank_server_initialization_fields_survive(self):
        server = WorkflowServer()
        self.run_workflow(server, self.directory / 'preserve')
        self.assertEqual(server.raw['definition.json']['serverUnknownInitialization'], {'retainMe': True})
        self.assertEqual(server.raw['planProperties.json']['properties']['serverUnknownDefault'], 'retain-me')

    def test_completed_create_resume_does_not_require_retained_operation(self):
        server = WorkflowServer(create_lro=True)
        directory = self.directory / 'create-expiry'
        self.run_workflow(server, directory)
        server.expired_create = True
        self.run_workflow(server, directory)
        self.assertEqual((server.creates, server.updates), (1, 1))

    def test_completed_update_resume_does_not_require_retained_operation(self):
        server = WorkflowServer(update_lro=True)
        directory = self.directory / 'update-expiry'
        self.run_workflow(server, directory)
        server.expired_update = True
        self.run_workflow(server, directory)
        self.assertEqual((server.creates, server.updates), (1, 1))

    def test_applied_update_with_lost_response_reconciles_without_resubmission(self):
        server = WorkflowServer(lose_update=True)
        directory = self.directory / 'lost-update'
        with self.assertRaisesRegex(RuntimeError, 'interrupted'):
            self.run_workflow(server, directory)
        result = self.run_workflow(server, directory)
        self.assertEqual((server.creates, server.updates), (1, 1))
        self.assertEqual(result['import'], 'reconciled-current-definition')
        self.assertEqual(load(directory / 'initial-update-result.json')['operationTerminalStatus'], 'unknown')

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
