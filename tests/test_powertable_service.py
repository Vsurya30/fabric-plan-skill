import json
import os
import tempfile
import unittest
from unittest.mock import patch

from runtime.powertable_service import (
    PowerTableServiceClient,
    approval_payload,
    create_approval,
    create_form,
    form_payload,
    resolve_source,
    source_path,
)


class PowerTableServiceContracts(unittest.TestCase):
    def test_approval_payload_uses_exact_user_and_group_graph_ids(self):
        payload = approval_payload([
            {'graphId': 'user-guid', 'entityType': 'USER'},
            {'graphId': 'group-guid', 'entityType': 'GROUP'},
        ])
        self.assertEqual(payload, {
            'ruleType': 10,
            'defaultApprovers': {'addedApproverObjs': [
                {'graphId': 'user-guid', 'entityType': 10},
                {'graphId': 'group-guid', 'entityType': 20},
            ]},
            'multiLevelEnabled': 0,
            'approvalLevel': 1,
        })
        for bad in (
            [],
            [{'graphId': '', 'entityType': 'USER'}],
            [{'graphId': 'x', 'entityType': 'UNKNOWN'}],
            [{'graphId': 'x', 'entityType': 1}],
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                approval_payload(bad)

    def test_form_payload_requires_runtime_column_config_ids(self):
        payload = form_payload(
            'New employee',
            [{'columnConfigId': 'column-guid', 'mandatory': 1, 'defaultValue': ''}],
        )
        self.assertEqual(payload['formConfiguration']['title'], 'New employee')
        self.assertEqual(payload['fieldsConfiguration'][0]['columnConfigId'], 'column-guid')
        for fields in ([], [{'name': 'Employee'}], [{'columnConfigId': '', 'mandatory': 1}]):
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                form_payload('Bad form', fields)
        with self.assertRaises(ValueError):
            form_payload('Bad form', [{'columnConfigId': 'x', 'mandatory': 2}])

    def test_source_and_mutation_paths_are_fixed_and_canonical(self):
        self.assertEqual(
            source_path('dbo', 'Employee'),
            '/v2/powertable/sources/dbo/Employee/',
        )
        self.assertEqual(
            source_path('dbo', 'Employee', source_id='source-1', suffix='approvals'),
            '/v2/powertable/sources/source-1/approvals/',
        )
        for kwargs in ({'source_id': 'a/b'}, {'schema': '../dbo'}, {'table': 'a?b'}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                source_path(kwargs.get('schema', 'dbo'), kwargs.get('table', 'Employee'),
                            source_id=kwargs.get('source_id'))

    def test_external_profile_is_bounded_and_journals_exact_service_requests(self):
        calls = []

        def adapter(method, url, headers, raw):
            calls.append((method, url, headers, json.loads(raw) if raw else None))
            if '/approvals/' in url:
                return {'status': 200, 'body': {'payload': {'saved': True}}}
            if '/forms/' in url:
                return {'status': 200, 'body': {'payload': {'id': 9}}}
            return {'status': 200, 'body': {'payload': {
                'isConfigured': True, 'dataSourceId': 44, 'visualId': 88,
                'sheetName': 'Employees', 'columnConfig': [],
            }}}

        with tempfile.TemporaryDirectory() as run, patch.dict(os.environ, {'PT_SERVICE_TOKEN': 'token'}):
            client = PowerTableServiceClient(
                'https://service.example.invalid', 'PT_SERVICE_TOKEN',
                ['service.example.invalid'], run=run, adapter=adapter,
                authorized_mutation=True,
            )
            source = resolve_source(client, {
                'dbName': 'Demo', 'dbHost': 'sql.example.invalid',
                'schema': 'dbo', 'table': 'Employee',
            }, label='source')
            create_approval(client, source['sourceId'],
                approval_payload([{'graphId': 'user', 'entityType': 'USER'}]),
                label='approval')
            create_form(client, source['sourceId'],
                form_payload('Employee form', [{'columnConfigId': 7}]),
                label='form')
            self.assertEqual([c[0] for c in calls], ['GET', 'POST', 'POST'])
            self.assertTrue(calls[1][1].endswith('/v2/powertable/sources/44/approvals/'))
            self.assertTrue(calls[2][1].endswith('/v2/powertable/sources/44/forms/'))
            with self.assertRaises(ValueError):
                client.check_route('https://other.example/v2/powertable/sources/44/forms/')

            read_only = PowerTableServiceClient(
                'https://service.example.invalid', 'PT_SERVICE_TOKEN',
                ['service.example.invalid'], run=run + '-readonly', adapter=adapter,
            )
            with self.assertRaisesRegex(ValueError, 'authorizedMutation'):
                create_form(read_only, '44', form_payload(
                    'Blocked', [{'columnConfigId': 7}]), label='blocked')


if __name__ == '__main__':
    unittest.main()
