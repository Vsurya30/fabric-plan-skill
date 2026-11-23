import unittest,copy,os,tempfile,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from runtime.pivots import compile_pivots,select_pivot
from runtime.identity import Registry
from runtime.layout import inventory
from runtime.native import save_home,set_home_visibility
from runtime.session import native_session,result_body
from runtime.transport import plan_operation,Client
from runtime.codec import loads
from test_runtime import page

class PivotTests(unittest.TestCase):
    def setUp(self):
        self.s={'sheetId':'sheet','rows':['Region','Employee'],'columns':['Month'],
            'dimensions':{'Region':'101','Employee':'102','Month':'103'},'measures':{'Cost':'104'}}
    def test_default_null_and_summary_axis(self):
        r=compile_pivots([{'key':'region','name':'Region','rows':['Region'],'columns':None}],self.s,Registry(),active='region')
        self.assertEqual(r['pivot']['configs'][0],{'id':'5880676360701185739','name':'All','row_dimensions':None,'col_dimensions':None,'measures':None,'hidden':False})
        self.assertEqual(r['pivot']['configs'][1]['row_dimensions'],['101']);self.assertIsNone(r['pivot']['configs'][1]['col_dimensions'])
        self.assertEqual(r['pivot']['active_id'],r['pivotExplorer']['activePivot'])
    def test_dimension_cannot_be_on_both_axes(self):
        with self.assertRaises(ValueError): compile_pivots([{'name':'Bad','rows':['Month']}],self.s,Registry(),capabilities={'PlanningCrossPivot':True,'PlanningColumnPivot':True})
    def test_cross_axis_gate_and_unknown(self):
        for axis in [['Month'],['Missing']]:
            with self.assertRaises(ValueError): compile_pivots([{'name':'Bad','rows':axis}],self.s,Registry())
    def test_hidden_active_rejected(self):
        with self.assertRaises(ValueError): compile_pivots([{'key':'x','name':'X','rows':[],'hidden':True}],self.s,Registry(),active='x')
    def test_null_and_empty_differ(self):
        r=compile_pivots([{'name':'Totals','rows':[]}],self.s,Registry());self.assertEqual(r['pivot']['configs'][1]['row_dimensions'],[])
        with self.assertRaises(ValueError): compile_pivots([{'name':'X'}],self.s,Registry())
    def test_selection_preserves_input_state(self):
        r=compile_pivots([{'name':'Region','rows':['Region']}],self.s,Registry());r['manage_measures']=[{'id':'104'}]
        before=copy.deepcopy(r);after=select_pivot(r,r['ids']['Region']);self.assertEqual(r,before);self.assertEqual(after['manage_measures'],before['manage_measures'])

class NewNativeTests(unittest.TestCase):
    def test_absent_home_200_null(self):
        class Fake:
            def __init__(self): self.calls=[]
            def request(self,method,route,body=None,**kw):
                self.calls.append((method,body))
                if len(self.calls)==1: return {'body':{'payload':{'data':None,'etag':None}}}
                if method=='POST': return {'body':{'payload':{'etag':'e'}}}
                return {'body':{'payload':{'data':{'items':[]},'etag':'e'}}}
        c=Fake();r=save_home(c,'__everyone__',{'items':[]},1,'home')
        self.assertNotIn('etag',c.calls[1][1]);self.assertEqual(r['priority'],'submitted-not-returned-by-content-reader')
    def test_visibility_requires_bool(self):
        with self.assertRaises(ValueError): set_home_visibility({},'false')
    def test_native_application_error(self):
        with self.assertRaises(RuntimeError): result_body({'body':{'statusCode':400,'payload':{}}})
    def test_token_exchanged_scoped_and_removed(self):
        calls=[];env_before=set(os.environ);os.environ['TEST_API_TOKEN']='mock-public'
        def adapter(method,url,headers,body):
            calls.append((url,headers,loads(body.decode()) if body else None))
            return {'status':200,'headers':{},'body':{'Token':'mock-child','TargetUriHost':'a.analysis.windows.net','CapacityObjectId':'cap'}}
        with tempfile.TemporaryDirectory() as t:
            with native_session('https://api.example.invalid','TEST_API_TOKEN','workspace','plan',t,adapter) as c:
                self.assertEqual(c.auth_scheme,'MWCToken');self.assertEqual(os.environ[c.token_env],'mock-child');env=c.token_env
            self.assertNotIn(env,os.environ)
            self.assertTrue(all('mock-child' not in f.read_text() for f in Path(t).glob('*')))
        self.assertEqual(calls[0][2]['artifacts'][0]['artifactObjectId'],'plan')
    def test_blank_create_has_no_definition(self):
        class Fake:
            def request(self,m,r,b,**k): self.body=b;return {'status':201,'body':{'id':'new'}}
            def finish(self,r,l): return r
        c=Fake();plan_operation(c,'workspace','create-blank',name='New',label='new');self.assertEqual(c.body,{'displayName':'New'})

if __name__=='__main__': unittest.main()
