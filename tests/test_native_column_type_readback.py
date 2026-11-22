"""Catalog alias compatibility, strict validation, and duplicate-safe resumes."""
import copy,json,os,tempfile,unittest
from unittest.mock import patch
from runtime.builder_api import column_matches,create_column
from runtime.native_profile import configure
from runtime.transport import Client


def payload():
    return {'measureGuid':'123','columnType':6,'name':'Linked estimate',
            'columnMeta':{'id':'123','data_type':'Number','name':'Linked estimate',
                          'measure_type':{'Native':{'measure_role':'ACMeasure'}}},
            'boundToFilterContext':10}


def saved_record(request,alias='dataInputType'):
    saved=copy.deepcopy(request)
    if alias=='dataInputType':saved['dataInputType']=saved.pop('columnType')
    elif alias=='both':saved['dataInputType']=saved['columnType']
    return saved


def ok(value):return {'status':200,'headers':{},'body':{'statusCode':200,'payload':value}}


class CatalogAdapter:
    def __init__(self,records=(),alias='dataInputType'):
        self.records=copy.deepcopy(list(records));self.alias=alias;self.posts=[];self.calls=[]
    def __call__(self,method,url,headers,body):
        self.calls.append((method,url,headers.get('x-target-visual')))
        if method=='GET':
            return ok({'resBody':self.records,'totalRecordCount':len(self.records)})
        if method!='POST':raise AssertionError('Unexpected method '+method)
        request=json.loads(body);self.posts.append(request)
        self.records.append(saved_record(request,self.alias))
        return ok({'measureGuid':request['measureGuid']})


class NativeColumnTypeReadback(unittest.TestCase):
    def setUp(self):self.request=payload()

    def test_sql_catalog_shape(self):column_matches(saved_record(self.request,'columnType'),self.request)

    def test_onelake_catalog_shape(self):column_matches(saved_record(self.request),self.request)

    def test_agreeing_aliases(self):column_matches(saved_record(self.request,'both'),self.request)

    def test_conflicting_aliases_are_rejected(self):
        saved=saved_record(self.request,'both');saved['dataInputType']=7
        with self.assertRaisesRegex(ValueError,'Conflicting'):column_matches(saved,self.request)

    def test_missing_wrong_null_and_string_types_are_rejected(self):
        for value in (None,7,'6'):
            for alias in ('columnType','dataInputType'):
                with self.subTest(value=value,alias=alias):
                    saved=saved_record(self.request,alias);saved[alias]=value
                    with self.assertRaisesRegex(ValueError,'columnType'):column_matches(saved,self.request)
        saved=copy.deepcopy(self.request);del saved['columnType']
        with self.assertRaisesRegex(ValueError,'columnType'):column_matches(saved,self.request)

    def test_identity_name_and_context_checks_remain_strict(self):
        for key,value in (('measureGuid','999'),('name','Wrong name'),('boundToFilterContext',20)):
            with self.subTest(key=key):
                saved=saved_record(self.request);saved[key]=value
                with self.assertRaisesRegex(ValueError,key):column_matches(saved,self.request)

    def test_metadata_checks_remain_strict(self):
        for key,value in (('id','999'),('data_type','Text'),('measure_type',{})):
            with self.subTest(key=key):
                saved=saved_record(self.request);saved['columnMeta'][key]=value
                with self.assertRaises((ValueError,KeyError)):column_matches(saved,self.request)


class NativeColumnResume(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        token=patch.dict(os.environ,{'COLUMN_ALIAS_TEST_TOKEN':'synthetic-credential'})
        token.start();self.addCleanup(token.stop)
        self.request=payload()

    def client(self,adapter,version='v2'):
        client=Client('https://example.invalid/CoreAPI','COLUMN_ALIAS_TEST_TOKEN',
            journal=self.tmp.name,adapter=adapter,sleep=lambda _:None,auth_scheme='MWCToken',
            context_headers={'x-ms-workload-resource-moniker':'synthetic-plan'})
        return configure(client,{'columns':version})

    def test_new_onelake_create_then_fresh_client_resume_posts_once(self):
        adapter=CatalogAdapter();first=create_column(self.client(adapter),'7',self.request,'create-linked')
        self.assertEqual(first['status'],'persisted-record-readback')
        self.assertNotIn('columnType',adapter.records[0])
        second=create_column(self.client(adapter),'7',self.request,'resume-linked')
        self.assertEqual(second['write'],'already-matched');self.assertEqual(adapter.posts,[self.request])
        self.assertNotIn('dataInputType',adapter.posts[0])
        self.assertEqual([m for m,u,v in adapter.calls],['GET','POST','GET','GET'])
        self.assertTrue(all('/v2/' in u and v=='7' for m,u,v in adapter.calls))

    def test_resume_previously_saved_onelake_column_sends_no_post(self):
        adapter=CatalogAdapter([saved_record(self.request)])
        result=create_column(self.client(adapter),'7',self.request,'resume-after-readback-failure')
        self.assertEqual(result['write'],'already-matched');self.assertEqual(adapter.posts,[])
        self.assertEqual(len(adapter.records),1)

    def test_sql_create_and_resume_still_work(self):
        adapter=CatalogAdapter(alias='columnType')
        create_column(self.client(adapter,'v1'),'7',self.request,'create-sql')
        result=create_column(self.client(adapter,'v1'),'7',self.request,'resume-sql')
        self.assertEqual(result['write'],'already-matched');self.assertEqual(adapter.posts,[self.request])
        self.assertTrue(all('/v1/' in u for m,u,v in adapter.calls))

    def test_invalid_existing_record_never_recreated(self):
        wrong=saved_record(self.request);wrong['dataInputType']=7
        conflict=saved_record(self.request,'both');conflict['dataInputType']=7
        context=saved_record(self.request);context['boundToFilterContext']=20
        metadata=saved_record(self.request);metadata['columnMeta']['id']='999'
        for record in (wrong,conflict,context,metadata):
            with self.subTest(record=record):
                adapter=CatalogAdapter([record])
                with self.assertRaises((ValueError,KeyError)):
                    create_column(self.client(adapter),'7',self.request,'invalid-resume')
                self.assertEqual(adapter.posts,[]);self.assertEqual(len(adapter.records),1)

    def test_duplicate_existing_id_is_rejected_without_post(self):
        record=saved_record(self.request);adapter=CatalogAdapter([record,record])
        with self.assertRaisesRegex(ValueError,'Duplicate native column'):
            create_column(self.client(adapter),'7',self.request,'duplicate-resume')
        self.assertEqual(adapter.posts,[])


if __name__=='__main__':unittest.main()
