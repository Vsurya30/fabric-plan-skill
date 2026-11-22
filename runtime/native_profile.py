"""Bounded read-only negotiation for confirmed SQL/OneLake metadata collections.

This is not a general URL rewriter or a mutation retry mechanism. Entity and
column capabilities are checked independently, scoped to the artifact client.
"""
from .transport import HttpError

def configure(client,versions=None):
    versions=dict(versions or {})
    if set(versions)-{'entities','columns'} or any(v not in ('auto','v1','v2') for v in versions.values()):
        raise ValueError('nativeReadVersions accepts entities/columns: auto, v1 or v2')
    client.native_read_profile={'configured':versions,'selected':{},'attempts':[]}
    return client

def profile(client):
    if not hasattr(client,'native_read_profile'):configure(client)
    return client.native_read_profile

def inherit(parent,child):
    # Only callers retaining the same artifact-scoped authentication may use this.
    child.native_read_profile=profile(parent)
    return child

def read(client,resource,route,validate,*,version=None,allow_not_found=False):
    if resource not in ('entities','columns'):raise ValueError('Unrecognized metadata collection')
    p=profile(client);configured=p['configured'].get(resource,'auto')
    explicit=version if version is not None else configured
    if explicit not in ('auto','v1','v2'):raise ValueError('Metadata API version')
    first=p['selected'].get(resource,'v1') if explicit=='auto' else explicit
    choices=[first,('v2' if first=='v1' else 'v1')] if explicit=='auto' else [first]
    for index,selected in enumerate(choices):
        path=route(selected)
        try:
            response=client.request('GET',path)
        except HttpError as e:
            p['attempts'].append({'resource':resource,'version':selected,'route':path,
                'status':e.status,'category':e.category,'repositoryMember':e.repositoryMember})
            # An undefined repository can mean the wrong persistence adapter.
            # Authentication, transport failures and generic errors are not that signal.
            compatible=e.category=='native-repository-unavailable' or (allow_not_found and e.status==404)
            if index==0 and len(choices)==2 and compatible:continue
            raise
        value=validate(response)  # Do not accept malformed 200 responses as success.
        p['selected'][resource]=selected
        p['attempts'].append({'resource':resource,'version':selected,'route':path,'status':'validated-read'})
        return value

def selected(client,resource):
    value=profile(client)['selected'].get(resource)
    if value is None:raise ValueError('Verify the '+resource+' metadata route first')
    return value

def evidence(client):
    import copy
    result=copy.deepcopy(profile(client))
    result.update(writeCapability='not-tested',storageMigration='not-performed',
        backendByCollection={k:('onelake' if v=='v2' else 'fabric-sql') for k,v in result['selected'].items()})
    return result
