"""Native state adapters, distinct from Fabric ALM and its bearer context."""
import copy, urllib.parse
from .construct import guid
from .codec import save,load,dumps,pointer_get,pointer_set
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
def create_visual(client,page_id,product,visual_type,visual_guid,label,version='v1'):
    # Resolve product and enum from target metadata/verified capability profile.
    if not product or not isinstance(visual_type,int) or not visual_guid: raise ValueError('Creation metadata required')
    return client.request('POST',f'/{version}/workload/entity/{page_id}/visual/',{'product':product,'visualGuid':visual_guid,'visualType':visual_type},label=label)
def embed_sheet(client,page_id,source_sheet_id,label,version='v1'):
    return client.request('POST',f'/{version}/workload/entity/{page_id}/embed/sheet/',{'embedSheetsIds':[source_sheet_id]},label=label)
def scoped_reconcile(client,read_route,write_route,changes,label,content_type='application/json',etag_pointer=None):
    """Changes: pointer, expected, value. Full fresh direct record; never list projection."""
    before=client.request('GET',read_route)['body']; out=copy.deepcopy(before)
    for c in changes:
        if pointer_get(out,c['pointer'])!=c['expected']: raise ValueError('Native baseline drift at '+c['pointer'])
        pointer_set(out,c['pointer'],c['value'])
    if etag_pointer and not pointer_get(out,etag_pointer): raise ValueError('Missing ETag')
    body=dumps(out).encode() if content_type=='application/octet-stream' else out
    client.request('PATCH',write_route,body,label=label,content_type=content_type)
    after=client.request('GET',read_route)['body']
    for c in changes:
        if pointer_get(after,c['pointer'])!=c['value']: raise ValueError('Reconciliation did not persist')
    return after
def run_phases(client,phases,checkpoint):
    """Execute verified route descriptors with per-phase readback; resume by re-reading.
    No unknown endpoint defaults. Descriptors require verified API contracts;
    accepting a descriptor does not supply a missing construction contract.
    """
    from pathlib import Path
    p=Path(checkpoint); state=load(p) if p.exists() else {'phases':{}}
    for phase in phases:
        label=phase['id']; read=phase.get('readback')
        if not read or not phase.get('provenance'): raise ValueError('Phase needs verified route provenance and readback')
        actual=client.request('GET',read['route'])['body']
        if pointer_get(actual,read['pointer'])==read['expected']:
            state['phases'][label]='verified'; save(p,state); continue
        if state['phases'].get(label)=='verified': raise ValueError('Completed phase drifted; explicit reconciliation required')
        r=client.request(phase['method'],phase['route'],phase.get('body'),label=label,content_type=phase.get('contentType','application/json'))
        if r['status']==202: client.finish(r,label)
        actual=client.request('GET',read['route'])['body']
        if pointer_get(actual,read['pointer'])!=read['expected']: raise ValueError('Phase readback failed: '+label)
        state['phases'][label]='verified'; save(p,state)
    return state
