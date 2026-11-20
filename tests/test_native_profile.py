import copy,json,os,tempfile,unittest
from unittest.mock import patch
from runtime.native_profile import configure,evidence,probe,selected
from runtime.session import entities,page,columns
from runtime.builder_api import scoped,create_column
from runtime.input_factories import input_create
from runtime.transport import Client,HttpError

def ok(payload):return {'status':200,'headers':{},'body':{'statusCode':200,'payload':payload}}
def repo(member='findAll'):return {'status':500,'headers':{},'body':{'message':"Cannot read properties of undefined (reading '"+member+"')"}}
def catalog(records=()):return ok({'resBody':list(records),'totalRecordCount':len(records)})

class NativeProfileTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.env=patch.dict(os.environ,{'PROFILE_TEST_TOKEN':'synthetic-credential'});self.env.start();self.addCleanup(self.env.stop)
        self.calls=[]
    def client(self,adapter):
        def record(method,url,headers,body):
            self.calls.append((method,url,headers,body));return adapter(method,url,headers,body)
        return Client('https://example.invalid/CoreAPI','PROFILE_TEST_TOKEN',journal=self.tmp.name,adapter=record,
            sleep=lambda _:None,auth_scheme='MWCToken',context_headers={'x-ms-workload-resource-moniker':'synthetic-plan'})

    def test_sql_default_succeeds_without_alternate(self):
        c=self.client(lambda *a:ok({'workloadEntities':[]}))
        self.assertEqual(entities(c),{'workloadEntities':[]})
        self.assertEqual(len(self.calls),1);self.assertIn('/v1/',self.calls[0][1])
        self.assertEqual(evidence(c)['backendByCollection'],{'entities':'fabric-sql'})

    def test_onelake_read_fallback_and_cache(self):
        c=self.client(lambda m,u,h,b:repo() if '/v1/' in u else ok({'workloadEntities':[]}))
        entities(c);entities(c)
        self.assertEqual([u.split('/CoreAPI')[1] for m,u,h,b in self.calls],['/v1/workload/entity/','/v2/workload/entity/','/v2/workload/entity/'])
        self.assertEqual(evidence(c)['writeCapability'],'not-tested')

    def test_entity_and_column_routes_independent_and_headers_preserved(self):
        def adapter(m,u,h,b):
            if '/workload/entity/' in u:return repo() if '/v1/' in u else ok({'workloadEntities':[]})
            self.assertEqual(h['x-target-visual'],'7')
            self.assertEqual(h['x-ms-workload-resource-moniker'],'synthetic-plan')
            self.assertTrue(h['Authorization'].startswith('MWCToken '))
            return catalog()
        c=self.client(adapter);entities(c);columns(c,'7')
        self.assertEqual(evidence(c)['selected'],{'entities':'v2','columns':'v1'})

    def test_new_auth_or_generic_errors_never_trigger_alternate_version(self):
        for status in (400,401,403,500):
            with self.subTest(status=status):
                self.calls=[];c=self.client(lambda *a:{'status':status,'headers':{},'body':{'message':'unrelated failure'}})
                with self.assertRaises(HttpError):entities(c)
                # Transport may retry transient 500 on the same path; the backend resolver must not switch.
                self.assertTrue(all('/v1/' in u for m,u,h,b in self.calls))
                if status!=500:self.assertEqual(len(self.calls),1)

    def test_malformed_success_does_not_trigger_other_version(self):
        c=self.client(lambda *a:ok({'unexpected':[]}))
        with self.assertRaises(ValueError):entities(c)
        self.assertEqual(len(self.calls),1);self.assertEqual(evidence(c)['selected'],{})

    def test_catalog_404_can_fallback_but_missing_page_cannot(self):
        c=self.client(lambda m,u,h,b:ok({'workloadEntities':[]}) if '/v2/' in u else {'status':404,'headers':{},'body':{}})
        entities(c);self.assertEqual(selected(c,'entities'),'v2')
        self.calls=[];c=self.client(lambda *a:{'status':404,'headers':{},'body':{}})
        with self.assertRaises(HttpError):page(c,'9')
        self.assertEqual(len(self.calls),1)

    def test_both_repository_errors_bounded_and_read_only(self):
        c=self.client(lambda *a:repo('findPaginatedRows'))
        with self.assertRaises(HttpError):columns(c,'7')
        self.assertEqual(len(self.calls),2);self.assertEqual([m for m,u,h,b in self.calls],['GET','GET'])
        self.assertEqual(evidence(c)['selected'],{})

    def test_cached_profile_can_recover_after_migration(self):
        migrated=False
        def adapter(m,u,h,b):return repo() if migrated and '/v1/' in u else ok({'workloadEntities':[]})
        c=self.client(adapter);entities(c);migrated=True;entities(c)
        self.assertEqual(len(self.calls),3);self.assertEqual(selected(c,'entities'),'v2')

    def test_explicit_or_configured_version_is_strict(self):
        c=configure(self.client(lambda *a:repo()),{'entities':'v1','columns':'v2'})
        with self.assertRaises(HttpError):entities(c)
        with self.assertRaises(HttpError):columns(c,'7')
        self.assertEqual(len(self.calls),2)
        self.assertIn('/v1/workload/',self.calls[0][1]);self.assertIn('/v2/visual/',self.calls[1][1])
        with self.assertRaises(ValueError):configure(c,{'all':'v2'})

    def test_scoped_client_shares_profile_but_separate_artifact_does_not(self):
        c=self.client(lambda *a:catalog());configure(c,{'columns':'v2'})
        child=scoped(c,'7');columns(child,'7')
        self.assertEqual(selected(c,'columns'),'v2')
        self.assertEqual(evidence(self.client(lambda *a:catalog()))['selected'],{})

    def test_column_create_uses_checked_column_route_and_strict_readback(self):
        payload=input_create('123','Reason','LongText',{},'configuration');records=[]
        def adapter(m,u,h,b):
            if '/v1/' in u:return repo('findPaginatedRows')
            if m=='GET':return catalog(records)
            self.assertEqual(m,'POST');self.assertEqual(json.loads(b),payload)
            records.append(copy.deepcopy(payload));return ok({'measureGuid':'123'})
        c=self.client(adapter);result=create_column(c,'7',payload,'create-reason')
        self.assertEqual(result['status'],'persisted-record-readback')
        self.assertEqual([m for m,u,h,b in self.calls],['GET','GET','POST','GET'])
        self.assertIn('/v2/',self.calls[2][1])
        create_column(c,'7',payload,'create-again')
        self.assertEqual(sum(m=='POST' for m,u,h,b in self.calls),1)

    def test_failed_write_is_not_replayed_against_other_backend(self):
        payload=input_create('123','Reason','LongText',{},'configuration')
        def adapter(m,u,h,b):
            if m=='POST':return repo('findOne')
            return repo('findPaginatedRows') if '/v1/' in u else catalog()
        c=self.client(adapter)
        with self.assertRaises(HttpError):create_column(c,'7',payload,'create-reason')
        writes=[u for m,u,h,b in self.calls if m=='POST']
        self.assertEqual(len(writes),1);self.assertIn('/v2/',writes[0])

    def test_probe_reads_only_direct_planning_owners(self):
        def adapter(m,u,h,b):
            self.assertEqual(m,'GET')
            if '/v1/' in u:return repo()
            if '/properties/' in u:return ok({'visuals':[{'id':'7','visualType':80},{'id':'8','visualType':80,'isEmbedded':True}]})
            if '/workload/entity/' in u:return ok({'workloadEntities':[{'id':1,'entityType':10,'displayName':'Plan'},{'id':2,'entityType':20,'displayName':'Dashboard'}]})
            return catalog([{'measureGuid':'123'}])
        result=probe(self.client(adapter))
        self.assertEqual(result['owners'],[{'name':'Plan','entityId':'1','visualId':'7','columns':1,'measureIds':['123']}])
        self.assertEqual(result['liveReportWrites'],0)
        self.assertEqual(result['profile']['selected'],{'entities':'v2','columns':'v2'})

if __name__=='__main__':unittest.main()
