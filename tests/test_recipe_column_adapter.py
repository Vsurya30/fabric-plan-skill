import tempfile,unittest
from unittest.mock import Mock,patch
from runtime.forecast_review import quarterly_review

class RecipeColumnAdapter(unittest.TestCase):
    def test_quarterly_create_delegates_and_stops_on_pending(self):
        state={'rowDimensions':[],'columnDimensions':[],
               'manage_measures':[{'id':'1001','label':'Forecast'}]}
        props={'visualState':state}
        source={'measureGuid':'1001','name':'Forecast','columnMeta':{
            'id':'1001','data_type':'Number','measure_type':{'Forecast':{}}}}
        actual={'measureGuid':'1002','name':'Actual','columnMeta':{
            'id':'1002','data_type':'Number','measure_type':{'Native':{}}}}
        client=Mock()
        with tempfile.TemporaryDirectory() as tmp, \
             patch('runtime.forecast_review.owner',side_effect=[('1','11',props),('2','22',props)]), \
             patch('runtime.forecast_review.columns',side_effect=[[source],[actual]]), \
             patch('runtime.builder_api.create_column',return_value={'status':'pending','jobIds':['job-1']}) as create, \
             patch('runtime.forecast_review.save_properties') as save:
            out=quarterly_review(client,{'sourceSheet':'Source','targetSheet':'Target',
                'sourceForecast':'Forecast','targetActuals':'Actual'},tmp)
        self.assertEqual(create.call_args.args[1],'22')
        self.assertEqual(out['status'],'pending-column-jobs')
        self.assertEqual(out['jobIds'],['job-1'])
        save.assert_not_called();client.request.assert_not_called()
