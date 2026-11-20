"""Synthetic workforce extension contract tests. No network, UI, or old report."""
import base64
import copy
import os
from pathlib import Path
import shutil
import socket
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from runtime.assets_api import multipart_image, upload_home_image
from runtime.builder_api import create_column, create_rule, poll_bridge, reload_query, save_powertable, source_parquet
from runtime.codec import loads
from runtime.home_api import decode_roles
from runtime.input_factories import input_create, metadata
from runtime.navigator_api import create as create_navigator, state as navigator_state
from runtime.powertable_factory import row_save
from runtime.rule_factories import distribute_rows, min_max, new_rule
from runtime.transport import Client

TOKEN_ENV = 'FABRIC_PLAN_BUILDER_TEST_TOKEN'


def response(payload, status=200):
    return {'status': status, 'headers': {}, 'body': {'statusCode': 200, 'payload': payload}}


def comment_payload():
    return input_create('501', 'Manager Comment', 'LongText',
        {'maximum_length': 2000, 'allow_entry_on_totals_or_subtotals': False}, '',
        measures={'canEdit': '401'}, context_bound=False,
        allow_input={'BasedOnFormula': '${canEdit} > 0'})


class ColumnAdapter:
    def __init__(self, catalog=(), async_ids=None, corrupt_binding=False):
        self.catalog = copy.deepcopy(list(catalog))
        self.async_ids = async_ids
        self.corrupt_binding = corrupt_binding
        self.posts = 0

    def __call__(self, method, url, headers, body):
        if method == 'GET':
            return response({'resBody': self.catalog, 'totalRecordCount': len(self.catalog)})
        self.posts += 1
        if self.async_ids is not None:
            return response({'jobIds': self.async_ids})
        payload = loads(body.decode('utf-8'))
        if self.corrupt_binding:
            payload['boundToFilterContext'] = 10
        self.catalog.append(payload)
        return response({'measureGuid': payload['measureGuid']})


class Notifications:
    def __init__(self, batches):
        self.batches = iter(batches)
        self.routes = []

    def request(self, method, route, **kwargs):
        self.routes.append(route)
        return response({'events': next(self.batches, [])})

    def wait(self, seconds):
        pass


def native_page():
    return {'statusCode': 200, 'payload': {'etag': 'page-1',
        'properties': {'properties': {'canvasStyle': {'dimension': {
            'width': 1000, 'height': 800, 'elementScalingUnit': 'pixel'}},
            'reactiveVisualProperties': [], 'unrelatedPageState': {'keep': True}}},
        'visuals': [{'id': '101', 'visualType': 80, 'properties': {'etag': 'owner-1',
            'properties': {'position': {'x': 20, 'y': 180}, 'dimension': {'width': 560, 'height': 280},
                           'visualState': {'unrelatedInputState': 'keep'}}}}]}}


class NavigatorAdapter:
    def __init__(self):
        self.page = native_page()
        self.creates = self.saves = 0

    def __call__(self, method, url, headers, body):
        if method == 'GET':
            return {'status': 200, 'headers': {}, 'body': copy.deepcopy(self.page)}
        payload = loads(body.decode('utf-8'))
        if url.endswith('/visual/'):
            self.creates += 1
            self.page['payload']['visuals'].append({'id': '102', 'visualType': 203,
                'properties': {'etag': 'nav-1', 'properties': {'visualState': {},
                    'position': {'x': 0, 'y': 0}, 'dimension': {'width': 10, 'height': 10}}}})
            self.page['payload']['etag'] = 'page-2'
            return response({'id': '102'})
        self.saves += 1
        for visual_id, wrapped in payload['visuals'].items():
            target = next(v for v in self.page['payload']['visuals'] if v['id'] == visual_id)
            target['properties'] = {**copy.deepcopy(wrapped), 'etag': 'nav-2'}
        self.page['payload']['etag'] = 'page-3'
        return response({})


class AssetAdapter:
    def __init__(self, image_bytes, wrong_readback=False):
        self.image_bytes = image_bytes
        self.wrong_readback = wrong_readback
        self.uploads = 0
        self.last_body = None
        self.meta = {'fileId': 'synthetic-asset', 'workloadId': 'workload-test',
                     'feature': 'home-layout', 'mimeType': 'image/svg+xml', 'fileSize': len(image_bytes)}

    def __call__(self, method, url, headers, body):
        if method == 'POST':
            self.uploads += 1
            self.last_body = body
            return response(self.meta)
        meta = copy.deepcopy(self.meta)
        if self.wrong_readback:
            meta['feature'] = 'different-scope'
        return response(meta)


class IndependentBuilderTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name)
        (self.directory / 'temp').mkdir()
        env = patch.dict(os.environ, {TOKEN_ENV: 'synthetic-builder-token',
            'TEMP': str(self.directory / 'temp'), 'TMP': str(self.directory / 'temp')})
        env.start(); self.addCleanup(env.stop)
        network = patch.object(socket.socket, 'connect', side_effect=AssertionError('Network forbidden'))
        network.start(); self.addCleanup(network.stop)

    def client(self, name, adapter, **kwargs):
        return Client('https://example.invalid/application', TOKEN_ENV, journal=self.directory / name,
                      adapter=adapter, sleep=lambda seconds: None, **kwargs)

    def node(self):
        value = os.environ.get('FABRIC_PLAN_NODE') or shutil.which('node')
        if not value:
            self.skipTest('Optional Node runtime unavailable for LZUTF8')
        return value

    def salary_inputs(self):
        metadata_rows = [
            {'id': 'EmployeeId', 'dataType': 'int', 'isPrimaryKey': True, 'isNullable': False, 'isEditable': False},
            {'id': 'Salary', 'dataType': 'decimal', 'isNullable': False, 'isEditable': True},
            {'id': 'Department', 'dataType': 'nvarchar', 'isNullable': True, 'isEditable': True}]
        records = [{'Salary': '82000'}]
        conditions = [{'EmployeeId': '7'}]
        audit = {'rowIds': ['7'], 'oldRecords': [{'EmployeeId': '7', 'Salary': '80000', 'Department': 'Operations'}],
                 'updatedColumns': ['Salary'], 'optionsMeta': {}}
        return metadata_rows, records, conditions, audit

    def test_workforce_typed_inputs_keep_exact_native_contracts(self):
        comment = comment_payload()
        checkbox = input_create('502', 'Reviewed', 'Checkbox', {'default_value': {'Static': False}, 'edit_on_total': False}, '')
        option = {'display_name': 'Operations', 'value': 'D-OPS', 'color': '', 'icon': '', 'order': 0}
        settings = {'options_source': {'Static': [option]}, 'default_value': {'Static': option},
                    'allow_user_to_add_new_option': False, 'prevent_null': True}
        before = copy.deepcopy(settings)
        department = input_create('503', 'Department', 'SingleSelect', settings, '')
        self.assertEqual([p['columnType'] for p in (comment, checkbox, department)], [101, 11, 2])
        self.assertEqual(comment['boundToFilterContext'], 20)
        self.assertEqual(comment['columnMeta']['measure_type']['DataInput']['allow_input'], {'BasedOnFormula': 'M_401 > 0'})
        self.assertEqual(checkbox['columnMeta']['data_type'], 'Boolean')
        self.assertEqual(department['columnMeta']['measure_type']['DataInput']['column_type']['SingleSelect']['default_value'], {'Static': option})
        self.assertEqual(settings, before)

    def test_text_default_cannot_violate_minimum_length(self):
        with self.assertRaises(ValueError):
            metadata('LongText', {'minimum_length': 10, 'default_value': {'Static': 'x'}})

    def test_picklist_unknown_default_rejects(self):
        option = {'display_name': 'Operations', 'value': 'D-OPS', 'color': '', 'icon': '', 'order': 0}
        other = {**option, 'value': 'D-OTHER'}
        with self.assertRaises(ValueError):
            metadata('SingleSelect', {'options_source': {'Static': [option]}, 'default_value': {'Static': other}})

    def test_bounded_allocation_uses_separate_rules_and_preserves_inputs(self):
        weights = {'701': 0.6, '702': 0.4}
        allocation = new_rule('801', 'Allocate by team weights',
            distribute_rows('ManualInput', ['601'], weights), measures={'SelectedMeasures': ['401']})
        bounds = new_rule('802', 'Capacity bounds', min_max({'Static': {'value': 0}}, {'Static': {'value': 200}}),
                          measures={'SelectedMeasures': ['401']})
        self.assertEqual(allocation['ruleOperation']['New']['rule_type']['Distribute']['operation']['Row']['reference'], {'ManualInput': {'weights': weights}})
        self.assertEqual(bounds['ruleOperation']['New']['measures'], {'SelectedMeasures': ['401']})
        self.assertEqual(weights, {'701': 0.6, '702': 0.4})
        with self.assertRaises(ValueError): distribute_rows('ManualInput', weights={'701': 0})
        with self.assertRaises(ValueError): min_max({'Static': {'value': 200}}, {'Static': {'value': 0}})
        writes = []
        def adapter(method, url, headers, body):
            if method == 'POST':
                writes.append(loads(body.decode('utf-8')))
                return response({'id': '901'})
            return response({'rules': [{'id': '901', 'rule_id': '801'}]})
        client = self.client('rule', adapter)
        result = create_rule(client, allocation, 'allocation', mount_verified=True)
        create_rule(client, allocation, 'allocation', mount_verified=True)
        self.assertEqual(len(writes), 1)
        self.assertEqual(result['response']['id'], '901')
        self.assertNotEqual(result['response']['id'], allocation['ruleOperation']['New']['rule_id'])
        self.assertEqual(result['execution'], 'not-tested')

    def test_salary_update_encoding_preserves_key_and_unrelated_values(self):
        meta, records, conditions, visual_meta = self.salary_inputs()
        original = copy.deepcopy((meta, records, conditions, visual_meta))
        payload = row_save(meta, 'update', records, conditions=conditions, visual_meta=visual_meta, node=self.node())
        inner = decode_roles(payload['data'], self.node())['updateData']
        self.assertEqual(inner['records'], [{'Salary': '82000'}])
        self.assertEqual(inner['conditions'], [{'EmployeeId': '7'}])
        self.assertEqual(inner['visualMeta']['oldRecords'][0]['Department'], 'Operations')
        self.assertEqual((meta, records, conditions, visual_meta), original)
        self.assertEqual(payload['actions'], ['update'])
        calls = []
        def adapter(method, url, headers, body):
            calls.append((url, headers, loads(body.decode('utf-8'))))
            return response({'jobIds': ['salary-job']})
        client = self.client('salary', adapter, context_headers={'x-target-visual': '901'})
        result = save_powertable(client, 'salary-source', payload, 'salary-update',
                                version='v4', route_shape='source-qualified')
        save_powertable(client, 'salary-source', payload, 'salary-update',
                       version='v4', route_shape='source-qualified')
        self.assertEqual(len(calls), 1)
        self.assertTrue(calls[0][0].endswith('/v4/powertable-source/salary-source/data/save/'))
        self.assertEqual(calls[0][1]['Content-Type'], 'application/octet-stream')
        self.assertEqual(decode_roles(calls[0][2]['data'], self.node())['updateData']['conditions'], [{'EmployeeId': '7'}])
        self.assertEqual(result['rowsSaved'], 'not-verified')
        # The supplied section 6.5 explicitly documents these empty serializer
        # arrays. Their shape is valid when no selected audit profile requires more.
        example_meta = [
            {'id': 'Id', 'dataType': 'int', 'isPrimaryKey': True, 'isNullable': False, 'isEditable': False},
            {'id': 'Amount', 'dataType': 'decimal', 'isPrimaryKey': False, 'isNullable': True, 'isEditable': True}]
        insert = row_save(example_meta, 'insert', [['1250']], generated_keys=['Id'],
                          visual_meta={'rowIds': [], 'optionsMeta': {}}, node=self.node())
        self.assertEqual(decode_roles(insert['data'], self.node())['createData'],
                         {'records': [['1250']], 'visualMeta': {'rowIds': [], 'optionsMeta': {}}})
        update = row_save(example_meta, 'update', [{'Amount': '1300'}], conditions=[{'Id': '42'}],
            visual_meta={'rowIds': ['42'], 'oldRecords': [], 'updatedColumns': ['Amount'], 'optionsMeta': {}}, node=self.node())
        self.assertEqual(decode_roles(update['data'], self.node())['updateData']['visualMeta']['oldRecords'], [])

    def test_salary_update_rejects_invalid_known_key_and_audit_shapes(self):
        mutations = [
            ('rowIds string', lambda r, c, v: v.update(rowIds='7')),
            ('optionsMeta null', lambda r, c, v: v.update(optionsMeta=None)),
            ('oldRecords null', lambda r, c, v: v.update(oldRecords=None)),
            ('structured key', lambda r, c, v: c[0].update(EmployeeId={'not': None})),
            ('null nonnullable salary', lambda r, c, v: r[0].update(Salary=None))]
        for name, mutate in mutations:
            with self.subTest(case=name):
                meta, records, conditions, visual_meta = self.salary_inputs()
                mutate(records, conditions, visual_meta)
                with self.assertRaises(ValueError):
                    row_save(meta, 'update', records, conditions=conditions, visual_meta=visual_meta, node=self.node())

    def test_column_readback_checks_outer_context_on_existing_and_created_record(self):
        payload = comment_payload()
        for existing in (True, False):
            with self.subTest(existing=existing):
                wrong = copy.deepcopy(payload); wrong['boundToFilterContext'] = 10
                adapter = ColumnAdapter([wrong] if existing else [], corrupt_binding=not existing)
                with self.assertRaises(ValueError):
                    create_column(self.client('binding-' + str(existing), adapter), '101', payload, 'comment')

    def test_column_async_jobs_require_unique_string_list(self):
        for index, ids in enumerate(('job-a', ['job-a', 'job-a'], [None])):
            with self.subTest(ids=ids):
                with self.assertRaises(ValueError):
                    create_column(self.client('jobs-' + str(index), ColumnAdapter(async_ids=ids)), '101', comment_payload(), 'comment')
        result = create_column(self.client('jobs-valid', ColumnAdapter(async_ids=['job-a'])), '101', comment_payload(), 'comment')
        self.assertEqual(result['status'], 'pending')
        self.assertEqual(result['companions'], 'not-yet-registered')

    def test_column_replay_does_not_recreate_persisted_record(self):
        adapter = ColumnAdapter()
        client = self.client('column-replay', adapter)
        create_column(client, '101', comment_payload(), 'comment')
        again = create_column(client, '101', comment_payload(), 'comment')
        self.assertEqual(again['write'], 'already-matched')
        self.assertEqual(adapter.posts, 1)

    def poll(self, client, jobs, **kwargs):
        return poll_bridge(client, 'workload-test', jobs, event_id_fields=['jobId'], status_field='status',
                           timestamp_field='time', interval=0, max_polls=2, **kwargs)

    def test_bridge_stale_later_poll_cannot_regress_completed_job(self):
        events = Notifications([
            [{'jobId': 'a', 'status': 200, 'time': 20}, {'jobId': 'b', 'status': 210, 'time': 20}],
            [{'jobId': 'a', 'status': 100, 'time': 10}, {'jobId': 'b', 'status': 200, 'time': 30}]])
        self.assertEqual(self.poll(events, ['a', 'b'])['status'], 'all-expected-jobs-succeeded')

    def test_bridge_partial_failure_and_empty_notifications_are_not_success(self):
        with self.assertRaises(RuntimeError):
            self.poll(Notifications([[{'jobId': 'a', 'status': 211, 'time': 1}]]), ['a'])
        with self.assertRaises(TimeoutError): self.poll(Notifications([[], []]), ['a'])

    def test_rls_pending_stream_requires_valid_job_ids(self):
        class Fake:
            def request(self, *args, **kwargs): return response({'jobIds': 'not-a-job-array'}, status=202)
        with self.assertRaises(ValueError): source_parquet(Fake(), 'source-test')

    def test_page_navigator_replay_and_save_preserve_other_owner(self):
        adapter = NavigatorAdapter()
        original = copy.deepcopy(adapter.page['payload']['visuals'][0])
        client = self.client('navigator', adapter)
        state = navigator_state('PAGE_NAVIGATOR_TABS', selected_pages=['201'], caption='Workforce views')
        # A caller using the old sparse disabled-icon profile is completed before save.
        state['style']['DEFAULT']['shapeState']['icon'] = {'isEnabled': False}
        args = (client, '201', '00000000-0000-4000-8000-000000000001', state,
                {'x': 20, 'y': 20, 'width': 560, 'height': 60}, 'navigator')
        first = create_navigator(*args, pages=['201'], bookmarks=[])
        second = create_navigator(*args, pages=['201'], bookmarks=[])
        self.assertEqual(first['visualId'], '102'); self.assertEqual(second['visualId'], '102')
        self.assertEqual((adapter.creates, adapter.saves), (1, 1))
        self.assertEqual(adapter.page['payload']['visuals'][0], original)
        self.assertEqual(first['navigationAndRendering'], 'not-tested')
        saved = next(v for v in adapter.page['payload']['visuals'] if v['id'] == '102')
        icon = saved['properties']['properties']['visualState']['navigatorState']['style']['DEFAULT']['shapeState']['icon']
        self.assertEqual(icon['padding']['topPadding'], 4)
        self.assertFalse(icon['isEnabled'])
        self.assertEqual(state['style']['DEFAULT']['shapeState']['icon'], {'isEnabled': False})

    def illustration(self):
        data = b'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="10"><rect width="20" height="10" fill="#12303d"/></svg>'
        path = self.directory / 'provided-illustration.svg'
        path.write_bytes(data)
        return path, data

    def asset_client(self, name, adapter):
        return self.client(name, adapter, auth_scheme='MWCToken',
                           context_headers={'x-ms-workload-resource-moniker': 'workload-test'})

    def test_provided_home_illustration_upload_is_stable_and_scoped(self):
        path, data = self.illustration()
        adapter = AssetAdapter(data)
        client = self.asset_client('asset', adapter)
        first = upload_home_image(client, path, 'workload-test', 'illustration')
        second = upload_home_image(client, path, 'workload-test', 'illustration')
        self.assertEqual(first, second); self.assertEqual(adapter.uploads, 1)
        self.assertIn(data, adapter.last_body)
        self.assertEqual(first['imageConfig']['source'], 'synthetic-asset')
        self.assertFalse(first['layoutSaved'])
        self.assertEqual(multipart_image(path, 'workload-test'), multipart_image(path, 'workload-test'))

    def test_asset_metadata_readback_cannot_change_feature_scope(self):
        path, data = self.illustration()
        with self.assertRaises(ValueError):
            upload_home_image(self.asset_client('wrong-asset', AssetAdapter(data, wrong_readback=True)),
                              path, 'workload-test', 'illustration')


if __name__ == '__main__':
    unittest.main()
