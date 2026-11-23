"""Resolve fresh runtime IDs and apply dashboard placement through property APIs.

No source-owner movement, numeric-ID guessing, UI step, or external template.
"""
import uuid

def visibility(client,workspace,plan,sheet_guid,visible,label):
    """Set dashboard visibility through the public Plan definition.

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

