"""Portable discovery and the executable command paths it exposes; no live APIs."""
import ast
from contextlib import contextmanager, redirect_stdout
import copy
from decimal import Decimal
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from runtime.discovery import catalog, discover, render
from runtime.codec import load
from runtime.construct import build
from runtime.scope import prepare_scope
from runtime.workflow import preflight, SUPPORTED

ROOT=Path(__file__).resolve().parents[1]


class DiscoveryTests(unittest.TestCase):
    def test_all_numbered_modules_and_related_routes_resolve(self):
        c=catalog(); ids=[m['id'] for m in c['modules']]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertEqual({i for i in ids if re.fullmatch(r'F\d\d',i)}, {f'F{i:02}' for i in range(1,31)})
        for m in c['modules']:
            self.assertTrue(m['businessRequests'])
            self.assertTrue(m['prerequisites'])
            self.assertTrue(m['limitations'])
            for other in m['related']:self.assertIn(other,ids)
            for op in m['operations']:self.assertIn(op,c['actions'])
            for g in m['guides']:
                text=(ROOT/'references'/g['file']).read_text(encoding='utf-8-sig')
                if g['heading']:
                    headings=[re.sub(r'^#+\s*','',line) for line in text.splitlines() if line.startswith('#')]
                    self.assertEqual(headings.count(g['heading']),1,(m['id'],g))

    def test_every_advertised_callable_exists(self):
        for op in catalog()['actions'].values():
            for symbol in op['symbols']:
                module,name=symbol.rsplit('.',1)
                tree=ast.parse((ROOT/Path(*module.split('.')).with_suffix('.py')).read_text(encoding='utf-8-sig'))
                self.assertTrue(any(isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name==name for n in tree.body),symbol)

    def test_advertised_cli_routes_are_accepted_by_parser(self):
        prefixes=set()
        for op in catalog()['actions'].values():
            if op['command']:
                parts=op['command'].split()[2:]
                if '--' in ' '.join(parts):parts=parts[:next(i for i,v in enumerate(parts) if v.startswith('--'))]
                prefixes.add(tuple(parts))
        for prefix in sorted(prefixes):
            result=subprocess.run([sys.executable,str(ROOT/'plan.py'),*prefix,'--help'],capture_output=True,text=True,cwd=ROOT)
            self.assertEqual(result.returncode,0,(prefix,result.stderr))

    def test_business_search_and_guide_only_limits(self):
        for query,expected in [('rolling forecast','F09'),('quarterly commentary','F05'),
                               ('from sheets','F19'),('negative variance','F15'),
                               ('employee master','POWERTABLE'),('time extension','F09')]:
            self.assertIn(expected,[m['id'] for m in discover(query)['modules']],query)
        approval=discover(module='f13')['modules'][0]
        self.assertEqual(approval['coverage'],'guide-only')
        self.assertEqual(approval['operations'],[])
        self.assertEqual(discover('zzzznotafeature')['count'],0)
        with self.assertRaises(ValueError):discover(module='F99')
        self.assertIn('No complete creation command',render(discover(module='F13')))

    def test_json_cli_is_read_only_and_portable(self):
        result=subprocess.run([sys.executable,str(ROOT/'plan.py'),'discover','--module','F19','--json'],capture_output=True,text=True,cwd=ROOT.parent)
        self.assertEqual(result.returncode,0,result.stderr)
        data=json.loads(result.stdout)
        self.assertEqual(data['modules'][0]['operations'][0]['id'],'forecast-review')

    def test_custom_time_axis_survives_scope_and_preflight(self):
        model=load(ROOT/'fixtures/model.json')
        for key,label in [('Calendar[FY]','FY'),('Calendar[FQ]','FQ')]:
            model['fields'].append(dict(id=key,tableName='Calendar',columnName=label,columnType='Column',dataType='Text'))
        spec=dict(name='Synthetic routed Forecast',requiredCapabilities=['planning.native-measure','planning.forecast'],sheets=[
            dict(name='Forecast',rows=['Employee[Employee]'],columns=['Calendar[FY]','Calendar[FQ]'],
                 columnTimeLevels={'Calendar[FY]':'Year','Calendar[FQ]':'Quarter'},
                 measures=[dict(key='actual',kind='Native',label='Actual',source='Metrics[BasePay]'),
                           dict(key='forecast',kind='Forecast',label='Forecast',actuals='actual',start='2026-01-01',end='2026-12-31')])])
        original=copy.deepcopy(spec)
        scope=prepare_scope(spec,SUPPORTED,model)
        preflight(scope['spec'])
        result=build(model,scope['spec'])
        props=next(v['properties'] for k,v in result['raw'].items() if k.endswith('/properties.json'))
        self.assertEqual([x['timeIntervalUnit'] for x in props['visualState']['columnDimensions']],['Year','Quarter'])
        self.assertEqual(spec,original)

    def test_forecast_review_cli_serializes_success_without_repeating_operation(self):
        import plan
        @contextmanager
        def session(*args,**kwargs):yield object()
        with tempfile.TemporaryDirectory() as directory:
            d=Path(directory)
            (d/'config.json').write_text(json.dumps(dict(authorizedMutation=True,powerbiApiBase='https://example.invalid',tokenEnvironment='UNSET_TEST_TOKEN',workspaceId='synthetic',planId='synthetic')))
            (d/'request.json').write_text('{}')
            stdout=io.StringIO()
            with patch.object(sys,'argv',['plan.py','forecast-review','--config',str(d/'config.json'),'--input',str(d/'request.json'),'--run',str(d/'run')]), \
                 patch('runtime.session.native_session',session), \
                 patch('runtime.forecast_review.quarterly_review',return_value={'status':'saved','value':Decimal('1.1')}) as review, \
                 redirect_stdout(stdout):
                plan.main()
            review.assert_called_once()
            self.assertEqual(json.loads(stdout.getvalue()),{'status':'saved','value':1.1})


if __name__=='__main__':unittest.main()
