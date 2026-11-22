"""Package-only synthetic SQL/OneLake recovery; no network or prior report."""
import json,os,sys,tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from runtime.codec import save
from runtime.session import entities,columns
from runtime.native_profile import evidence
from runtime.transport import Client

def build(out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    env='FABRIC_PLAN_SYNTHETIC_PROFILE';previous=os.environ.get(env);os.environ[env]='synthetic-credential'
    results={}
    try:
        for backend in ('sql','onelake'):
            calls=[]
            def adapter(method,url,headers,body):
                assert method=='GET';calls.append(url)
                if backend=='onelake' and '/v1/' in url:
                    return {'status':500,'headers':{},'body':{'message':"Cannot read properties of undefined (reading 'findAll')"}}
                payload={'workloadEntities':[]} if '/workload/entity/' in url else {'resBody':[{'measureGuid':'123'}],'totalRecordCount':1}
                return {'status':200,'headers':{},'body':{'statusCode':200,'payload':payload}}
            with tempfile.TemporaryDirectory() as run:
                c=Client('https://example.invalid/CoreAPI',env,journal=run,adapter=adapter)
                entities(c);columns(c,'7');columns(c,'7')
                result=evidence(c);result['requestCount']=len(calls);result['liveReportWrites']=0
                expected='v1' if backend=='sql' else 'v2'
                assert result['selected']=={'entities':expected,'columns':expected}
                assert len(calls)==(3 if backend=='sql' else 5)
                results[backend]=result
        save(out/'profile-evidence.json',results)
    finally:
        if previous is None:os.environ.pop(env,None)
        else:os.environ[env]=previous
    return results

if __name__=='__main__':
    results=build(sys.argv[1]);print(json.dumps({'profiles':list(results),'liveReportWrites':0}))
