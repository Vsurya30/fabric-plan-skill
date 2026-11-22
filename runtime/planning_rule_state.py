"""Author captured Planning rule records in the owning visual's saved state.

Record IDs supplied here are fresh authoring IDs, not IDs claimed to have been
issued by the engine New API. Audit fields are omitted, never copied or forged.
Persistence checks do not certify allocation execution or lock enforcement.
"""
import copy
from .identity import native_id
from .rule_factories import new_rule,verify_saved_rule

def authored_record(payload,record_id):
    request=payload['ruleOperation']['New']
    checked=new_rule(request['rule_id'],request['name'],request['rule_type'],
        rows=request['rows'],columns=request['columns'],measures=request['measures'],
        disabled=request['is_disabled'])['ruleOperation']['New']
    record={'id':native_id(record_id),**copy.deepcopy(checked),'is_updated':False}
    return record

def append_record(properties,payload,record_id,*,visual_type=None):
    # Native page responses store the type on the visual envelope, whereas
    # authored ALM properties may also carry it. Never infer owner type from
    # the presence of manage_measures alone.
    owner_type=properties.get('visualType',visual_type)
    if owner_type!=80 or (visual_type is not None and visual_type!=80):
        raise ValueError('Rule must belong to a Planning visual')
    p=copy.deepcopy(properties);state=p['visualState'];record=authored_record(payload,record_id)
    known={m['id'] for m in state['manage_measures']}
    target=record['measures']
    if not isinstance(target,dict) or set(target)!={'SelectedMeasures'} or not set(target['SelectedMeasures'])<=known:
        raise ValueError('Resolve selected input measures on the current owner')
    operation=record['rule_type']['Distribute']['operation']
    config=next(iter(operation.values()))['reference']['MeasureIdWithReference']
    if config['measure']['Measure'] not in known:raise ValueError('Weight is absent from current owner')
    saved=state.setdefault('data_input_rules',[])
    existing=[x for x in saved if x['rule_id']==record['rule_id']]
    if existing:
        verify_saved_rule(payload,saved)
        if existing[0]['id']!=record['id']:raise ValueError('Existing record ID differs')
        return p
    if any(x['id']==record['id'] or x['name']==record['name'] for x in saved):raise ValueError('Rule record/name collision')
    saved.append(record)
    return p

def save_rule(client,entity_id,visual_id,payload,record_id,label):
    """Save only this owner's rule state, with fresh ETags and exact readback.

    This is configuration persistence through the captured properties batch
    route. It does not execute an allocation or certify native engine behavior.
    """
    from .session import page
    from .forecast_review import save_properties
    def owned(response):
        matches=[v for v in response['payload']['visuals'] if str(v['id'])==str(visual_id)]
        if len(matches)!=1 or matches[0].get('isEmbedded') or matches[0].get('visualType')!=80:
            raise ValueError('Resolve one actual Planning owner')
        return matches[0]
    before=owned(page(client,str(entity_id)))
    props=before['properties']['properties']
    intended=append_record(props,payload,record_id,visual_type=before['visualType'])
    def transform(current):
        if current!=props:raise ValueError('Planning owner changed; reread before saving')
        return intended
    result=save_properties(client,str(entity_id),str(visual_id),transform,label)
    after=owned(page(client,str(entity_id)))['properties']['properties']
    if after!=intended:raise ValueError('Saved Planning properties differ from intended state')
    check=verify_saved_rule(payload,after['visualState']['data_input_rules'])
    return {'save':result,'verification':check,'idOrigin':'fresh authored saved-state ID',
        'runtimeExecution':'not-tested'}
