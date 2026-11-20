"""Mandatory page navigation is constructed and saved without a repair phase."""
import copy
import unittest
from pathlib import Path
from unittest.mock import patch
from runtime.codec import load
from runtime.planning_presentation import build_application
from runtime.application_defaults import check_application_defaults,require_delivery_phases
from runtime.intelligence_api import deploy_geometry
from runtime.layout import overlap
from runtime.navigator_defaults import require_complete_defaults

ROOT=Path(__file__).resolve().parents[1]

def build(explicit=False):
    model=load(ROOT/'fixtures/model.json');spec=load(ROOT/'fixtures/finance-spec.json')
    if explicit:
        owner=spec['sheets'][0]['name']
        spec['dashboards']=[{'name':'Executive review','owner':owner,'slicers':[],'cards':[]},
                            {'name':'Operational review','owner':owner,'slicers':[],'cards':[]}]
    return build_application(model,spec)

def navigator(b,d=None):
    d=d or b['dashboardIdentities'][0]
    sheet=next(s for s in b['raw']['definition.json']['sheets'] if s['recordGuid']==d['sheetGuid'])
    member=next(v for v in sheet['workloadItemEntityVisuals'] if v['visualType']=='BI_RUNTIME_INPUT')
    path=f'sheets/{d["sheetGuid"]}/visuals/{member["visualId"]}/properties.json'
    return sheet,member,b['raw'][path]['properties']

class MandatoryPageNavigationTests(unittest.TestCase):
    def test_every_automatic_and_explicit_dashboard_has_visible_portable_navigation(self):
        for explicit in (False,True):
            b=build(explicit)
            self.assertEqual(b['defaultsCheck']['dashboardsWithPageNavigator'],len(b['dashboardIdentities']))
            for d in b['dashboardIdentities']:
                sheet,member,p=navigator(b,d);nav=p['visualState']['navigatorState']
                self.assertEqual(p['visualType'],203)
                self.assertFalse(member['isEmbedded'])
                self.assertFalse(p['layerProperties']['layerProperties']['isHidden'])
                self.assertEqual(nav['type'],'PAGE_NAVIGATOR_TABS')
                self.assertNotIn('selectedPages',nav['navigatorTabsState'])
                self.assertEqual(nav['navigatorTabsState']['destinationType'],{'all':True,'hidden':False,'tooltip':False})
                self.assertTrue(require_complete_defaults(nav))
                self.assertEqual(nav['style']['DEFAULT']['shapeState']['text']['fontFamily'],'Arial')
                r=d['placements'][member['visualId']];grid=d['placements'][d['ownerGuid']]
                self.assertEqual(grid['y']-r['y']-r['height'],16)
                self.assertEqual(r['height'],48)
                self.assertEqual(r['width'],grid['width'])
                for other_id,other in d['placements'].items():
                    if other_id!=member['visualId']:self.assertFalse(overlap(r,other,15.999999))

    def test_missing_membership_or_wrong_kind_cannot_pass_even_with_all_save_receipts(self):
        for change in ('unlisted','button','bookmark','embedded','hidden','empty-targets','source-ids','hidden-only','wrong-host'):
            b=build();sheet,member,p=navigator(b);nav=p['visualState']['navigatorState']
            if change=='unlisted':sheet['workloadItemEntityVisuals'].remove(member) # orphan part remains
            elif change=='button':nav['type']='NAVIGATOR_BUTTON'
            elif change=='bookmark':nav['type']='BOOKMARK_TABS'
            elif change=='embedded':member['isEmbedded']=True
            elif change=='hidden':p['layerProperties']['layerProperties']['isHidden']=True
            elif change=='empty-targets':nav['navigatorTabsState']['selectedPages']=[]
            elif change=='source-ids':nav['navigatorTabsState']['selectedPages']=['123']
            elif change=='hidden-only':nav['navigatorTabsState']['destinationType']={'all':False,'hidden':True,'tooltip':False}
            else:member['visualType']='BI_TEXT'
            ids=[d['sheetGuid'] for d in b['dashboardIdentities']]
            with self.subTest(change=change),self.assertRaisesRegex(ValueError,'Required visible Page Navigator'):
                require_delivery_phases(b,home_saved=True,home_visible=True,dashboard_geometry=ids,dashboard_visibility=ids)

    def test_gate_rejects_off_canvas_and_overlapping_navigation(self):
        for change in ('off-canvas','overlap'):
            b=build();sheet,member,p=navigator(b)
            p['position']={'x':24,'y':10000 if change=='off-canvas' else 24}
            with self.subTest(change=change),self.assertRaisesRegex(ValueError,'Page Navigator'):
                check_application_defaults(b['raw'],b['home'])

    def test_required_native_geometry_phase_saves_full_navigation_state_with_fresh_etags(self):
        # Imported controls may have a host default state. Normal provisioning
        # must save authored tabs and padding before exposing the dashboard.
        from test_context_intelligence import GeometryTransaction
        for verify in (True,False):
            b,d,mapping,state,owner=GeometryTransaction().fixture()
            saved_nav=next(v for v in state['payload']['visuals'] if v['properties']['properties'].get('visualType')==203)
            intended=copy.deepcopy(saved_nav['properties']['properties']['visualState']['navigatorState'])
            saved_nav['properties']['properties']['visualState']={'navigatorState':{'type':'NAVIGATOR_BUTTON'},'hostSetting':'keep'}
            saved_nav['properties']['properties']['layerProperties']['layerProperties']['isHidden']=True
            saved_nav['properties']['etag']='navigator-current-etag'
            original=copy.deepcopy(state);owner_original=copy.deepcopy(owner);writes=[]
            class Client:
                def request(self,method,url,body,label):
                    writes.append(copy.deepcopy(body));state['payload']['properties']=body['workloadEntities']['20']
                    for v in state['payload']['visuals']:
                        if v['id'] in body['visuals']:v['properties']={**body['visuals'][v['id']],'etag':'v2'}
                    return {'body':{'statusCode':200}}
            with patch('runtime.intelligence_api.entities',return_value={'workloadEntities':[{'displayName':d['name'],'id':20}]}),patch('runtime.intelligence_api.page',side_effect=lambda c,e:copy.deepcopy(owner if e=='7' else state)):
                result=deploy_geometry(Client(),b['raw'],d,mapping,'normal-delivery',verify=verify)
                self.assertEqual(result['write'],'saved')
                self.assertEqual(len(writes),1)
                props=writes[0]['visuals'][saved_nav['id']]['properties']
                self.assertEqual(props['visualState']['navigatorState'],intended)
                self.assertEqual(props['visualState']['hostSetting'],'keep')
                self.assertFalse(props['layerProperties']['layerProperties']['isHidden'])
                self.assertEqual(writes[0]['etags']['visuals'][saved_nav['id']],'navigator-current-etag')
                self.assertEqual(owner,owner_original)
                for old in original['payload']['visuals']:
                    if old['id'] in (saved_nav['id'],'999'):continue
                    new=next(v for v in state['payload']['visuals'] if v['id']==old['id'])
                    self.assertEqual(old['properties']['properties'],new['properties']['properties'])
                self.assertEqual(deploy_geometry(Client(),b['raw'],d,mapping,'normal-delivery',verify=verify)['write'],'already-matched')
                self.assertEqual(len(writes),1)

if __name__=='__main__':unittest.main()
