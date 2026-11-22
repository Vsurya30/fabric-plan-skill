import copy,unittest
from types import SimpleNamespace
from unittest.mock import patch
from runtime.navigation_publish import publish

class NavigationPublishTests(unittest.TestCase):
 def setUp(self):
  self.raw={'definition.json':{'sheets':[{'recordGuid':'owner','displayName':'Owner','sheetType':'PLANNING','isHidden':True},{'recordGuid':'dashboard','displayName':'Dashboard','sheetType':'REPORTING','isHidden':True}]}}
  self.catalog=[{'id':'7','displayName':'Owner','entityType':10,'isHidden':20,'order':0,'workloadItemEntityVisuals':[{'visualId':19}]},{'id':'8','displayName':'Dashboard','entityType':20,'isHidden':10,'order':1,'workloadItemEntityVisuals':[{'visualId':20}]}]
  self.requests={'owner':False,'dashboard':True};self.calls=[];self.persist=True;self.fail=False
 def request(self,method,route,body,**kw):
  self.calls.append((method,route,body))
  if self.fail:raise RuntimeError('Write failed')
  if self.persist:next(e for e in self.catalog if e['id']==route.split('/')[-2])['isHidden']=body['isHidden']
  return {'status':200,'body':{}}
 def call(self,version='v2'):
  n=SimpleNamespace(native_read_profile={'configured':{},'selected':{'entities':version},'attempts':[]},request=self.request)
  def catalog(_):return {'workloadEntities':copy.deepcopy(self.catalog)}
  with patch('runtime.navigation_publish.entities',side_effect=catalog),patch('runtime.intelligence_api.entities',side_effect=catalog):
   return publish(None,n,None,None,self.raw,self.requests,'publish')
 def test_onelake_uses_native_v2_without_import(self):
  before=copy.deepcopy(self.catalog);result=self.call()
  self.assertEqual(self.calls,[('PUT','/v2/workload/entity/7/',{'isHidden':10}),('PUT','/v2/workload/entity/8/',{'isHidden':20})])
  self.assertTrue(all(r['nativeReadback']=='passed' for r in result.values()))
  self.assertEqual([e['workloadItemEntityVisuals'] for e in before],[e['workloadItemEntityVisuals'] for e in self.catalog])
 def test_sql_retains_v1(self):
  self.call('v1');self.assertTrue(all('/v1/' in r[1] for r in self.calls))
 def test_already_matched_does_not_write(self):
  self.catalog[0]['isHidden']=10;self.catalog[1]['isHidden']=20
  self.call();self.assertEqual(self.calls,[])
 def test_native_readback_required(self):
  self.persist=False
  with self.assertRaisesRegex(ValueError,'readback mismatch'):self.call()
 def test_ambiguous_identity_stops_before_mutation(self):
  self.catalog.append(copy.deepcopy(self.catalog[0]))
  with self.assertRaisesRegex(ValueError,'Ambiguous'):self.call()
  self.assertEqual(self.calls,[])
 def test_failed_writer_is_never_replayed_on_another_version(self):
  self.fail=True
  with self.assertRaises(RuntimeError):self.call()
  self.assertEqual(len(self.calls),1);self.assertIn('/v2/',self.calls[0][1])
 def test_unknown_authored_identity_is_rejected(self):
  self.requests['unknown']=True
  with self.assertRaisesRegex(ValueError,'Unknown'):self.call()
  self.assertEqual(self.calls,[])

if __name__=='__main__':unittest.main()
