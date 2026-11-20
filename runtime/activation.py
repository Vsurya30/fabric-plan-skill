"""API persistence actions on a freshly resolved Planning owner.

These are property mutations, not proof of a native engine calculation or an
interactive client controller firing. Evidence never promotes those stages.
"""
import copy
from .session import page,result_body
from .pivots import select_pivot

def select_saved_pivot(client,entity_id,visual_id,pivot_id,label):
    before=page(client,entity_id)
    matches=[v for v in before['payload']['visuals'] if v['id']==visual_id and not v.get('isEmbedded')]
    if len(matches)!=1 or matches[0]['visualType']!=80: raise ValueError('Expected resolved direct Planning owner')
    record=matches[0]; wrapped=record['properties']; props=copy.deepcopy(wrapped['properties'])
    if not wrapped.get('etag') or not before['payload'].get('etag'): raise ValueError('Current ETags required')
    props['visualState']=select_pivot(props['visualState'],pivot_id)
    body={'visuals':{visual_id:{'schema':'0.0.1','properties':props}},'workloadEntities':{},'workload':{},
        'etags':{'visuals':{visual_id:wrapped['etag']},'workloadEntities':{str(entity_id):before['payload']['etag']}}}
    same=props==wrapped['properties']
    if not same: result_body(client.request('POST','/v1/workload/properties/batch/',body,label=label))
    after=page(client,entity_id)
    actual=next(v['properties']['properties'] for v in after['payload']['visuals'] if v['id']==visual_id)
    if actual!=props: raise ValueError('Saved Pivot readback differs or unrelated property drifted')
    return {'status':'passed-persisted-active-pivot','pivotId':pivot_id,'write':'already-matched' if same else 'submitted','controllerExecution':'not-tested','calculation':'not-tested'}
