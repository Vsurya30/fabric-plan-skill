import copy,os,runpy,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
from runtime.codec import load,pack,save
from runtime.authoring_flow import require_import_contract,native_column_preflight
from runtime.planning_presentation import build_application
from runtime.transport import Client,HttpError
from runtime.builder_api import create_column
from runtime.input_factories import input_create
from runtime.session import entities
from runtime.workflow import provision

ROOT=Path(__file__).resolve().parents[1]

class AuthoringFlowTests(unittest.TestCase):
    def setUp(self):
        self.model=load(ROOT/'fixtures/model.json')
        self.spec=load(ROOT/'examples/conditional-formatting/application.json')
        self.b=build_application(self.model,self.spec)

    def test_complete_base_retains_inputs_formulas_and_cf(self):
        result=require_import_contract(self.spec,self.b)
        self.assertEqual(result['conditionalFormattingRules'],7)
        self.assertEqual(result['measures'],sum(len(s['measures']) for s in self.spec['sheets']))
        self.assertEqual(self.b['buildRequest'],self.spec)
        self.b['buildRequest']['name']='Changed copy'
        self.assertNotEqual(self.b['buildRequest']['name'],self.spec['name'])

    def test_reference_only_detour_fails_against_original_request(self):
        stripped=copy.deepcopy(self.spec)
        for sheet in stripped['sheets']:
            sheet['measures']=[m for m in sheet['measures'] if m['kind']=='Native']
            sheet['conditionalFormatting']=[]
        other=build_application(self.model,stripped)
        with self.assertRaisesRegex(ValueError,'IMPORT_CONTRACT'):require_import_contract(self.spec,other)
        # A business request that really is reference-only is not forbidden.
        self.assertEqual(require_import_contract(stripped,other)['status'],'passed')

    def test_removed_input_or_formula_and_cf_cannot_pass_candidate_gate(self):
        for remove in ('DataInput','Formula','CF','registry'):
            candidate=copy.deepcopy(self.b['raw']);identity=self.b['identities'][0]
            prefix=f"sheets/{identity['sheetId']}/visuals/{identity['visualId']}/"
            vs=candidate[prefix+'properties.json']['properties']['visualState']
            if remove=='CF':vs.pop('cfProps')
            elif remove=='registry':vs['manage_measures']=[]
            else:
                data=candidate[prefix+'dataInput.json']
                data['columns']=[r for r in data['columns'] if remove not in r['columnMeta']['measure_type']]
            with self.subTest(remove=remove),self.assertRaisesRegex(ValueError,'IMPORT_CONTRACT'):
                require_import_contract(self.spec,self.b,candidate)

    def test_formula_changed_to_zero_fails(self):
        candidate=copy.deepcopy(self.b);changed=False
        for path,data in candidate['raw'].items():
            if not path.endswith('/dataInput.json'):continue
            for record in data['columns']:
                kind=record['columnMeta']['measure_type']
                if 'Formula' in kind:kind['Formula']['formula']='0';changed=True
        self.assertTrue(changed)
        with self.assertRaisesRegex(ValueError,'changed formula'):require_import_contract(self.spec,candidate)

    def test_typed_metadata_does_not_silently_become_number(self):
        for metadata in ({'typed':{'kind':'LongText'}},{'inputKind':'LongText'}):
            spec=copy.deepcopy(self.spec)
            spec['sheets'][0]['measures'].append({'key':'comment','kind':'DataInput','label':'Reason',**metadata})
            with self.assertRaisesRegex(ValueError,'UNSUPPORTED_BASE_INPUT'):build_application(self.model,spec)

    def test_forecast_and_its_formula_stay_in_base_even_with_separate_commentary(self):
        sample=runpy.run_path(str(ROOT/'examples/forecast-time-intelligence/build.py'))['sample']
        model,spec,_,_,_,_,commentary=sample()
        built=build_application(model,spec)
        self.assertEqual(require_import_contract(spec,built)['measures'],3)
        self.assertEqual(commentary['columnMeta']['data_type'],'Text')
        i=built['identities'][0];path=f"sheets/{i['sheetId']}/visuals/{i['visualId']}/dataInput.json"
        built['raw'][path]['columns']=[r for r in built['raw'][path]['columns'] if 'Forecast' not in r['columnMeta']['measure_type']]
        with self.assertRaisesRegex(ValueError,'IMPORT_CONTRACT'):require_import_contract(spec,built)

    def test_discovery_prominently_routes_observed_failures_and_business_request(self):
        from runtime.discovery import discover
        for query in ('reference-only import','stripped inputs','findPaginatedRows','expected flow','native preflight'):
            self.assertIn('VERIFIED-AUTHORING-FLOW',[m['id'] for m in discover(query)['modules'][:3]],query)

    def test_incomplete_scope_has_no_live_create_or_reduced_import(self):
        spec=copy.deepcopy(self.spec)
        spec['sheets'][0]['measures'].append({'key':'comment','kind':'DataInput','inputKind':'LongText','label':'Reason'})
        with tempfile.TemporaryDirectory() as run,patch('runtime.workflow.Client') as client:
            result=provision({'name':spec['name']},self.model,spec,run)
            client.assert_not_called()
            self.assertEqual(result['mutation'],'none');self.assertFalse(result['originalScopeComplete'])
            self.assertTrue(Path(run,'scope-coverage.json').exists())

    def test_native_catalog_failure_checks_both_documented_reads_without_post(self):
        calls=[]
        def adapter(method,url,headers,body):
            calls.append((method,url))
            if '/v2/workload/entity/' in url:
                return {'status':200,'headers':{},'body':{'statusCode':200,'payload':{'workloadEntities':[]}}}
            return {'status':500,'headers':{},'body':{'message':"Cannot read properties of undefined (reading 'findPaginatedRows')"}}
        with tempfile.TemporaryDirectory() as run,patch.dict(os.environ,{'FLOW_TEST_TOKEN':'synthetic-credential'}):
            client=Client('https://example.invalid','FLOW_TEST_TOKEN',journal=run,adapter=adapter,sleep=lambda _:self.fail('Deterministic failure retried'))
            self.assertEqual(entities(client,'v2')['workloadEntities'],[])
            payload=input_create('123','Reason','LongText',{},'configuration')
            with self.assertRaises(HttpError) as error:create_column(client,'7',payload,'create-reason')
            self.assertEqual(error.exception.category,'native-repository-unavailable')
            self.assertEqual(error.exception.repositoryMember,'findPaginatedRows')
            self.assertEqual(len(calls),3);self.assertTrue(all(m=='GET' for m,u in calls))
            self.assertTrue(any('/v1/visual/' in u for m,u in calls))
            self.assertTrue(any('/v2/visual/' in u for m,u in calls))

    def test_auth_failure_is_not_repository_failure(self):
        for status in (401,403):
            error=HttpError(status,{'message':"Cannot read properties of undefined (reading 'findOne')"})
            self.assertEqual(error.category,'authentication');self.assertIsNone(error.repositoryMember)

    def test_repository_create_failure_is_not_replayed(self):
        calls=[]
        def adapter(*args):
            calls.append(args[0]);return {'status':400,'headers':{},'body':{'message':"Cannot read properties of undefined (reading 'findOne')"}}
        with tempfile.TemporaryDirectory() as run,patch.dict(os.environ,{'FLOW_TEST_TOKEN':'synthetic-credential'}):
            client=Client('https://example.invalid','FLOW_TEST_TOKEN',journal=run,adapter=adapter)
            for _ in range(2):
                with self.assertRaises(HttpError) as error:client.request('POST','/v1/visual/datainput/column/',{},label='same-request')
                self.assertEqual(error.exception.repositoryMember,'findOne')
            self.assertEqual(calls,['POST'])

    def test_readable_catalog_does_not_claim_write_capability(self):
        def adapter(*args):
            return {'status':200,'headers':{},'body':{'statusCode':200,'payload':{'resBody':[],'totalRecordCount':0}}}
        with tempfile.TemporaryDirectory() as run,patch.dict(os.environ,{'FLOW_TEST_TOKEN':'synthetic-credential'}):
            client=Client('https://example.invalid','FLOW_TEST_TOKEN',journal=run,adapter=adapter)
            result=native_column_preflight(client,'7')
            self.assertEqual(result['status'],'column-catalog-readable')
            self.assertEqual(result['writeCapability'],'not-tested')

if __name__=='__main__':unittest.main()
