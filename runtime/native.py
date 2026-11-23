"""Home layout workload adapters, distinct from Fabric ALM and its bearer context."""
import copy, urllib.parse
from .construct import guid
from .transport import HttpError
def workload_token_request(workspace,plan):
    return {'type':'[Start] GetMWCTokenV2','workspaceObjectId':workspace,'workloadType':'Planning',
       'artifacts':[{'artifactType':'Planning','artifactObjectId':plan}],'asyncId':guid(),'iframeId':guid()}
def proxy_base(token_response,workspace,plan):
    host=token_response['TargetUriHost']; cap=token_response['CapacityObjectId']
    if any(c in host for c in '/:@?#'): raise ValueError('Expected metadata-returned target hostname')
    return f'https://{host}/webapi/capacities/{cap}/workloads/Planning/PlanningProxy/Automatic/workspaces/{workspace}/artifacts/{plan}/CoreAPI'
def save_home(client,role,layout,order,label,current_order=None,method='POST'):
    if method not in ('POST','PUT'):raise ValueError('Select verified Home provider method')
    from .home_fit import assert_home_fit
    fit=assert_home_fit(layout)
    from .session import result_body
    route='/v1/access/roles/layout/'+urllib.parse.quote(role,safe='')+'/'
    try:
        before=result_body(client.request('GET',route))
    except HttpError as e:
        if e.status!=404: raise
        before=None
    body={'homeLayoutOrder':order,'data':copy.deepcopy(layout)}
    # DXT V2 content reader returns 200 {data:null,etag:null} for an absent role.
    absent=before is None or (before.get('data','missing') is None and before.get('etag') is None)
    if not absent:
        if before.get('etag') is None: raise ValueError('Existing Home missing current ETag')
        body['etag']=before['etag']
    same=not absent and before.get('data')==layout and before.get('homeLayoutOrder',current_order)==order
    if not same: result_body(client.request(method,route,body,label=label))
    after=result_body(client.request('GET',route))
    if after.get('data')!=layout or not after.get('etag'): raise ValueError('Home readback mismatch')
    if 'homeLayoutOrder' in after and after['homeLayoutOrder']!=order: raise ValueError('Home priority readback mismatch')
    return {'status':'passed-persisted-home-content','etag':after['etag'],'write':'already-matched' if same else 'submitted',
        'priority':'verified' if 'homeLayoutOrder' in after else 'submitted-not-returned-by-content-reader',
        'visibility':'separate-workload-save','assetRendering':'not-run','layoutFit':fit}
def set_home_visibility(workload,show):
    if not isinstance(show,bool): raise ValueError('Home visibility must be Boolean')
    out=copy.deepcopy(workload)
    out.setdefault('properties',{}).setdefault('homeLayout',{})['show']=show
    return out
