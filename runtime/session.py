"""Workload session for role-specific Home layout. No browser or source repo.

The public environment base must be explicitly resolved by the invoking agent.
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
def native_session(powerbi_base,token_environment,workspace,plan,journal,adapter=None):
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
        yield Client(base,env,journal=journal,adapter=adapter,auth_scheme='MWCToken',
            context_headers={'x-ms-workload-resource-moniker':plan,'x-delegated-token':'DUMMY_TOKEN'})
    finally: os.environ.pop(env,None)

