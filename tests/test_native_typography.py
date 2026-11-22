import unittest,copy,json
from unittest.mock import patch
from runtime.application_typography import normalize_arial,font_issues,finish_native_typography

class NativeTypographyTests(unittest.TestCase):
    def test_expanded_boundaries_preserve_data(self):
        p={'formula':'{"fontFamily":"Consolas"}','pivotAssignments':[{'id':'field'}],
           'visualState':{'manage_measures':[], 'title':'{"style":"font-family: Calibri; color: red"}',
             'hiddenProperties_!!!_appearance':json.dumps({'charts':{'fontFamily':'Segoe UI'},'other':7}),
             'formatConfig':{'measure':{'m':[{'format':{'4':'Calibri','3':'red'},'order':1}]}},
             'formula':'["fontFamily"]', 'random':'{"fontFamily":"keep"}'}}
        before=copy.deepcopy(p);out=normalize_arial(p)
        self.assertEqual(p,before);self.assertEqual(out['formula'],p['formula'])
        self.assertEqual(out['pivotAssignments'],p['pivotAssignments'])
        self.assertEqual(out['visualState']['random'],p['visualState']['random'])
        self.assertEqual(out['visualState']['formatConfig']['measure']['m'][0]['format']['3'],'red')
        self.assertFalse(font_issues(out['visualState']))
        self.assertEqual(normalize_arial(out),out)

    def test_native_update_and_no_duplicate_write_on_resume(self):
        state={'payload':{'visuals':[{'id':3,'isEmbedded':False,'properties':{'properties':{'visualState':{'fontFamily':'Calibri'}}}},
                {'id':4,'isEmbedded':True,'properties':{'properties':{'visualState':{'fontFamily':'Calibri'}}}}]}}
        writes=[]
        def write(c,e,v,fn,label):
            writes.append(v);state['payload']['visuals'][0]['properties']['properties']=fn(state['payload']['visuals'][0]['properties']['properties'])
        with patch('runtime.session.entities',return_value={'workloadEntities':[{'id':1}]}),patch('runtime.session.page',side_effect=lambda *a:copy.deepcopy(state)),patch('runtime.forecast_review.save_properties',side_effect=write):
            finish_native_typography(None);finish_native_typography(None)
        self.assertEqual(writes,['3'])
        self.assertEqual(state['payload']['visuals'][1]['properties']['properties']['visualState']['fontFamily'],'Calibri')

    def test_readback_mismatch_fails(self):
        state={'payload':{'visuals':[{'id':3,'properties':{'properties':{'visualState':{'fontFamily':'Calibri'}}}}]}}
        with patch('runtime.session.entities',return_value={'workloadEntities':[{'id':1}]}),patch('runtime.session.page',return_value=state),patch('runtime.forecast_review.save_properties'):
            with self.assertRaisesRegex(ValueError,'readback'):finish_native_typography(None)
