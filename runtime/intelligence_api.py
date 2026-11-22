"""Resolve fresh runtime IDs and apply dashboard placement through property APIs.

No source-owner movement, numeric-ID guessing, UI step, or external template.
"""
import copy,uuid
from .session import entities,page
from .layout import audit,inventory
from .readback import contains

def visibility_native(client,entity_id,visible,label,*,verify=True,version=None):
    """Profile-specific entity writer; enum 20 is visible, 10 is hidden.

    V1 SQL and V2 OneLake writers are independently live-verified. Resolve the
    current entity collection before writing once; never replay across versions.
    ALM false flags can be acknowledged without exposing an existing page.
    """
    if not isinstance(visible,bool) or not str(entity_id).isdecimal():
        raise ValueError('Resolved numeric entity identity and Boolean visibility required')
    def current():
        matches=[e for e in entities(client)['workloadEntities'] if str(e['id'])==str(entity_id)]
        if len(matches)!=1:raise ValueError('Missing/ambiguous native entity')
        return matches[0]
    before=current();expected=20 if visible else 10
    from .native_profile import selected
    writer=version or selected(client,'entities')
    if writer not in ('v1','v2'):raise ValueError('Verified entity writer version required')
    if before.get('isHidden')==expected:return {'visible':visible,'write':'already-matched','nativeReadback':'passed'}
    client.request('PUT',f'/{writer}/workload/entity/{entity_id}/',{'isHidden':expected},label=label)
    if not verify:return {'visible':visible,'write':'saved','nativeReadback':'not-run'}
    after=current()
    if after.get('isHidden')!=expected:raise ValueError('Native visibility readback mismatch')
    for key in ('displayName','order','entityType','workloadItemId','workloadItemEntityVisuals','isFilterContextEnabled'):
        if after.get(key)!=before.get(key):raise ValueError('Unrelated entity metadata changed: '+key)
    return {'visible':visible,'write':'saved','nativeReadback':'passed'}

def visibility(client,workspace,plan,sheet_guid,visible,label):
    """Legacy ALM alternative. DXT existing-sheet flags require visibility_native.

    Keep explicit readback: an accepted import is not evidence of visibility.
    """
    from .codec import unpack,parts,patch,sha
    from .transport import plan_operation
    if not isinstance(visible,bool): raise ValueError('Visibility must be Boolean')
    current=plan_operation(client,workspace,'export',plan,label=label+'-export-'+uuid.uuid4().hex)['body']
    root=unpack(current)['definition.json'];matches=[s for s in root['sheets'] if s['recordGuid']==sheet_guid]
    if len(matches)!=1: raise ValueError('Missing or duplicate staged dashboard')
    if matches[0].get('isHidden') is (not visible): return {'visible':visible,'write':'already-matched'}
    matches[0]['isHidden']=not visible
    envelope=patch(current,{'definition.json':root},{'definition.json':sha(parts(current)['definition.json'])})
    plan_operation(client,workspace,'update',plan,definition=envelope,label=label)
    check=plan_operation(client,workspace,'export',plan,label=label+'-verify-'+uuid.uuid4().hex)['body']
    actual=next(s for s in unpack(check)['definition.json']['sheets'] if s['recordGuid']==sheet_guid)
    if actual.get('isHidden') is not (not visible): raise ValueError('Dashboard visibility readback mismatch')
    return {'visible':visible,'write':'saved'}

def signature(p):
    return (p.get('visualType'),p.get('layerProperties',{}).get('layerProperties',{}).get('name'),
            tuple(sorted((a['id'],a['bucketId']) for a in p.get('pivotAssignments',[]))))

def deploy_geometry(client, raw, dashboard, planning_map, label,*,verify=True):
    catalog=entities(client)['workloadEntities']
    candidates=[e for e in catalog if e['displayName']==dashboard['name'] and e.get('entityType',20)==20]
    if len(candidates)!=1: raise ValueError('Ambiguous dashboard entity')
    eid=str(candidates[0]['id']);before=page(client,eid);payload=before['payload'];records=payload['visuals']
    key=dashboard['ownerGuid']
    owner=planning_map.get(key)
    if owner is None:
        sheets=[s for s in raw['definition.json']['sheets'] if s['sheetType']=='PLANNING' and
                any(v['visualId']==key and not v.get('isEmbedded') for v in s['workloadItemEntityVisuals'])]
        if len(sheets)!=1: raise ValueError('Expected one authored source sheet for the embedded grid')
        source=[e for e in catalog if e.get('entityType')==10 and e['displayName']==sheets[0]['displayName']]
        if len(source)!=1: raise ValueError('Expected one source sheet in the dashboard catalog')
        source_id=str(source[0]['id'])
        owner_before=page(client,source_id)
        source_visuals={str(v['id']) for v in owner_before['payload']['visuals']
                        if not v.get('isEmbedded') and v['visualType']==80}
        embedded=[v for v in records if v.get('isEmbedded') and str(v['id']) in source_visuals]
        if len(embedded)!=1: raise ValueError('Expected one embedded grid belonging to the source sheet')
        owner={'sheetGuid':sheets[0]['recordGuid'],'entityId':source_id,'visualId':embedded[0]['id']}
    else:
        owner_before=page(client,owner['entityId']) if verify else None
    p=copy.deepcopy(payload['properties']['properties']);candidate=copy.deepcopy(before)
    authored_page=raw[f'sheets/{dashboard["sheetGuid"]}/sheet.json']['properties']
    if p['canvasStyle']['dimension']['elementScalingUnit']!='pixel': raise ValueError('Native canvas unit changed; explicitly convert all geometry before mutation')
    contains(p['canvasStyle']['dimension'],authored_page['canvasStyle']['dimension'],'canvas')
    batch={'visuals':{},'workloadEntities':{},'workload':{},'etags':{'visuals':{},'workloadEntities':{}}}
    if payload.get('etag') is None: raise ValueError('Fresh page ETag required')
    batch['etags']['workloadEntities'][eid]=payload['etag'];used=set();matches={}
    for portable,r in dashboard['placements'].items():
        embedded=portable==dashboard['ownerGuid']
        if embedded:
            found=[v for v in records if v.get('isEmbedded') and str(v['id'])==str(owner['visualId'])]
        else:
            desired=raw[f'sheets/{dashboard["sheetGuid"]}/visuals/{portable}/properties.json']['properties']
            found=[v for v in records if not v.get('isEmbedded') and signature(v['properties']['properties'])==signature(desired)]
        if len(found)!=1 or found[0]['id'] in used: raise ValueError('Ambiguous dashboard visual identity')
        v=found[0];vid=v['id'];used.add(vid);matches[portable]=vid
        pos={k:r[k] for k in ('x','y')};dim={k:r[k] for k in ('width','height')}
        if embedded:
            overrides=p.setdefault('reactiveVisualProperties',[]);found_override=[o for o in overrides if str(o['visualId'])==str(vid)]
            if len(found_override)>1: raise ValueError('Duplicate embedded override')
            override=found_override[0] if found_override else {'visualId':vid,'properties':{}}
            override['properties'].update(position=pos,dimension=dim,originEntityId=owner['entityId'],lockAspectRatio=False)
            if not found_override: overrides.append(override)
        else:
            props=copy.deepcopy(v['properties']['properties']);props.update(position=pos,dimension=dim)
            if desired.get('visualType')==203 and 'navigatorState' in desired.get('visualState',{}):
                from .navigator_defaults import require_complete_defaults
                nav=desired['visualState']['navigatorState'];require_complete_defaults(nav)
                # ALM registers the control. Save its full authored native state
                # in this required phase, alongside geometry and fresh ETags.
                props.setdefault('visualState',{})['navigatorState']=copy.deepcopy(nav)
                props.setdefault('layerProperties',{}).setdefault('layerProperties',{})['isHidden']=False
            if props.get('visualType')==50:
                from .chart_filters import ensure_chart_filters,audit_chart_filters
                ensure_chart_filters(props);audit_chart_filters(props)
            nested=v['properties'].get('etag');flat=v.get('etag')
            if nested is not None and flat is not None and nested!=flat: raise ValueError('Conflicting visual ETags')
            etag=nested if nested is not None else flat
            if etag is None: raise ValueError('Fresh visual ETag required')
            batch['visuals'][vid]={'schema':'0.0.1','properties':props};batch['etags']['visuals'][vid]=etag
            for c in candidate['payload']['visuals']:
                if c['id']==vid:c['properties']=batch['visuals'][vid]
    if len(used)!=len(records): raise ValueError('Unaccounted dashboard visuals; preserve and replan the complete inventory')
    batch['workloadEntities'][eid]={'schema':'0.0.1','properties':p};candidate['payload']['properties']=batch['workloadEntities'][eid]
    audit(candidate,gap=15.999999)
    # Existing labels reconcile intent through transport journaling; read current
    # state first on a resume. No repeated creation when a response is lost.
    unchanged=payload['properties']['properties']==p and all(
        next(v for v in records if v['id']==k)['properties']['properties']==val['properties'] for k,val in batch['visuals'].items())
    if not unchanged: client.request('POST','/v1/workload/properties/batch/',batch,label=label)
    if not verify:return {'name':dashboard['name'],'entityId':eid,'owner':owner,'visuals':matches,'write':'already-matched' if unchanged else 'saved','nativeReadback':'not-run','runtime':'not-run'}
    after=page(client,eid);inv=inventory(after)
    contains(inv['page'],p,'page')
    for portable,vid in matches.items():
        if inv['visuals'][vid]['rectangle']!=dashboard['placements'][portable]: raise ValueError('Dashboard rectangle readback mismatch')
        if vid in batch['visuals']: contains(inv['visuals'][vid]['properties'],batch['visuals'][vid]['properties'],'visual')
    owner_after=page(client,owner['entityId'])
    if owner_after['payload']['properties']!=owner_before['payload']['properties'] or owner_after['payload']['visuals']!=owner_before['payload']['visuals']:
        raise ValueError('Source owner changed during layout transaction; reconcile concurrent edits')
    return {'name':dashboard['name'],'entityId':eid,'owner':owner,'visuals':matches,**audit(after,gap=15.999999),
            'write':'already-matched' if unchanged else 'saved','slicerPropagation':'not-tested','contextInputIsolation':'not-tested'}
