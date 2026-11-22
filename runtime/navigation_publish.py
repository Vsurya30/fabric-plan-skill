"""Publish current business-page visibility with verified SQL/OneLake writers."""
from .session import entities
from .native_profile import selected
from .intelligence_api import visibility_native

def publish(client,native,workspace,plan,authored,requests,label):
    # Retain the caller's explicit ALM context for API compatibility; visibility
    # itself uses the artifact-scoped native session, without an extra import.
    if not requests or any(not isinstance(v,bool) for v in requests.values()):
        raise ValueError('Explicit sheet visibility requests required')
    declared={s['recordGuid']:s for s in authored['definition.json']['sheets']}
    if not set(requests)<=declared.keys():raise ValueError('Unknown current authored sheet')
    catalog=entities(native)['workloadEntities'];profile=selected(native,'entities');resolved={}
    if profile not in ('v1','v2'):raise ValueError('Unverified entity writer profile')
    for sid in requests:
        matches=[e for e in catalog if e['displayName']==declared[sid]['displayName']]
        if len(matches)!=1:raise ValueError('Ambiguous native navigation identity')
        e=matches[0];expected={'PLANNING':10,'REPORTING':20,'POWERTABLE':30}[declared[sid]['sheetType']]
        if e['entityType']!=expected:raise ValueError('Native navigation type mismatch')
        resolved[sid]=e
    # No fallback after a failed/ambiguous mutation. The writer journals each
    # distinct entity request and verifies flags plus unchanged membership.
    return {sid:visibility_native(native,str(e['id']),requests[sid],label+'-'+str(e['id']),version=profile)
            for sid,e in resolved.items()}
