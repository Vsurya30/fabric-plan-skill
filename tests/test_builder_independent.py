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
from runtime.codec import loads
from runtime.home_api import decode_roles
from runtime.input_factories import input_create, metadata
from runtime.navigator_api import state as navigator_state
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









    def illustration(self):
        data = b'<svg xmlns="http://www.w3.org/2000/svg" width="20" height="10"><rect width="20" height="10" fill="#12303d"/></svg>'
        path = self.directory / 'provided-illustration.svg'
        path.write_bytes(data)
        return path, data

    def asset_client(self, name, adapter):
        return self.client(name, adapter, auth_scheme='MWCToken',
                           context_headers={'x-ms-workload-resource-moniker': 'workload-test'})




if __name__ == '__main__':
    unittest.main()
