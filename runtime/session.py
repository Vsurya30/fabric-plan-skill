"""API-only workload session and verified read routes. No browser or source repo.

The public environment base must be explicitly resolved by the invoking agent.
The DXT exchange and read routes were exercised 2026-11-13 UTC.
"""
import os,uuid,urllib.parse
from contextlib import contextmanager
from .transport import Client
from .native import workload_token_request,proxy_base

def result_body(response):
    b=response['body']
    if not isinstance(b,dict): raise ValueError('Expected API object response')
    if 'statusCode' in b and b['statusCode']!=200: raise RuntimeError('Native application status '+str(b['statusCode']))
    return b.get('payload',b)

@contextmanager
def native_session(powerbi_base,token_environment,workspace,plan,journal,adapter=None,native_read_versions=None):
    """Get a short-lived artifact-scoped token. Never serialize its credential.

    powerbi_base is explicit authorized environment metadata; no hostname replacement.
    """
    auth=Client(powerbi_base,token_environment,journal=journal,adapter=adapter,
        context_headers={'x-ms-fabric-skill':'fabric-plan-skill'})
    r=auth.request('POST','/metadata/v201606/generatemwctokenv2',workload_token_request(workspace,plan),label='mwc-'+str(uuid.uuid4()))
    d=r['body']; base=proxy_base(d,workspace,plan)
    host=urllib.parse.urlsplit(base).hostname
    if not host or not (host.endswith('.pbidedicated.windows.net') or host.endswith('.analysis.windows.net')):
        raise ValueError('Unexpected workload token target; require an explicitly audited environment profile')
    if not isinstance(d.get('Token'),str) or not d['Token']: raise ValueError('Missing workload token')
    env='FABRIC_PLAN_MWC_'+uuid.uuid4().hex.upper(); os.environ[env]=d['Token']
    try:
        from .native_profile import configure
        yield configure(Client(base,env,journal=journal,adapter=adapter,auth_scheme='MWCToken',
            context_headers={'x-ms-workload-resource-moniker':plan,'x-delegated-token':'DUMMY_TOKEN'}),native_read_versions)
    finally: os.environ.pop(env,None)

def entities(client,version=None):
    from .native_profile import read
    def validate(response):
        p=result_body(response)
        if not isinstance(p.get('workloadEntities'),list): raise ValueError('Missing entity catalog')
        ids=[str(e['id']) for e in p['workloadEntities']]
        if len(ids)!=len(set(ids)): raise ValueError('Duplicate runtime entity identity')
        return p
    return read(client,'entities',lambda v:f'/{v}/workload/entity/',validate,version=version,allow_not_found=True)

def page(client,entity_id,version=None):
    from .native_profile import read
    if not str(entity_id).isdigit(): raise ValueError('Use resolved numeric runtime entity identity')
    def validate(response):
        b=response['body']
        if b.get('statusCode')!=200 or not isinstance(b.get('payload',{}).get('visuals'),list): raise ValueError('Incomplete page response')
        return b
    return read(client,'entities',lambda v:f'/{v}/workload/entity/{entity_id}/properties/',validate,version=version)

def columns(client,visual_id,version=None):
    from .native_profile import read,inherit
    if not str(visual_id).isdigit(): raise ValueError('Use resolved native visual identity')
    scoped=Client(client.base,client.token_env,client.allowed,client.journal,client.adapter,client.sleep,
        client.auth_scheme,{**client.context_headers,'x-target-visual':str(visual_id)})
    inherit(client,scoped)
    def validate(response):
        r=result_body(response)
        if not isinstance(r.get('resBody'),list): raise ValueError('Missing column catalog')
        if r.get('totalRecordCount',len(r['resBody']))!=len(r['resBody']): raise ValueError('Incomplete column catalog')
        return r['resBody']
    return read(scoped,'columns',lambda v:f'/{v}/visual/datainput/column/?order=ASC&take=-1',validate,version=version,allow_not_found=True)
