import copy,unittest
from unittest.mock import patch
from runtime.intelligence_api import visibility_native

class NativeVisibilityTests(unittest.TestCase):
    def entity(self,hidden):
        return {'id':'8','displayName':'Workforce','order':1,'entityType':20,
                'isHidden':hidden,'workloadItemId':'new-plan','workloadItemEntityVisuals':[]}
    def test_persist_and_preserve(self):
        writes=[]
        class Client:
            def request(self,*a,**kw):writes.append((a,kw));return {'status':200}
        with patch('runtime.intelligence_api.entities',side_effect=[{'workloadEntities':[self.entity(10)]},{'workloadEntities':[self.entity(20)]}]):
            self.assertEqual(visibility_native(Client(),'8',True,'publish',version='v1')['nativeReadback'],'passed')
        self.assertEqual(writes[0][0],('PUT','/v1/workload/entity/8/',{'isHidden':20}))
    def test_success_receipt_without_persistence_fails(self):
        class Client:
            def request(self,*a,**kw):return {'status':200}
        with patch('runtime.intelligence_api.entities',return_value={'workloadEntities':[self.entity(10)]}):
            with self.assertRaisesRegex(ValueError,'readback mismatch'):visibility_native(Client(),'8',True,'publish',version='v1')
    def test_unknown_target_never_mutates(self):
        class Client:
            def request(self,*a,**kw):raise AssertionError('Must not mutate')
        with patch('runtime.intelligence_api.entities',return_value={'workloadEntities':[]}):
            with self.assertRaisesRegex(ValueError,'Missing'):visibility_native(Client(),'8',True,'publish')

if __name__=='__main__':unittest.main()
