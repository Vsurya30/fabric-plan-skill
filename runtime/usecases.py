"""Portable business recipes: discover, compile and create/resume without chat state.

Only explicit deploy performs writes. Source registrations and ETags are resolved
as prerequisites; no UI, calculation tests or post-save validation are performed.
"""
import copy,re,time,uuid
from pathlib import Path
from .codec import load,save,dumps,sha,parts,unpack,pack
from .construct import merge
from .identity import Registry
from .planning_presentation import build_application,apply_presentation
from .forecast_review import owner,find_column,save_properties,quarterly_review,comparison_chart,apply_negative_variance
from .measure_bindings import resolve_measure,registered_measure
from .input_factories import input_create,formula_create
from .session import native_session,entities,page,columns,result_body,resolve_planning
from .transport import Client,plan_operation

ROOT=Path(__file__).resolve().parents[1]
CASES=ROOT/'examples/five-usecases'

def catalog():return load(CASES/'index.json')

def recipe(key):
    if isinstance(key,dict):
        required={'id','title','prompt','spec','post','expected'}
        if not required<=key.keys():raise ValueError('Adapted recipe needs '+', '.join(sorted(required)))
        return copy.deepcopy(key)
    if key not in {x['id'] for x in catalog()}:raise ValueError('Unknown usecase; use usecase list')
    return load(CASES/(key+'.json'))

def current_model(config,run):
    """Read authorized model metadata. No data queries. TMDL selected schema branch."""
    c=Client(config['apiBase'],config['tokenEnvironment'],config.get('allowedHosts'),Path(run)/'model-api')
    ref=copy.deepcopy(config['modelReference']);w=ref['semanticModelWorkspaceId'];m=ref['semanticModelId']
    item=c.request('GET',f'/workspaces/{w}/semanticModels/{m}')['body']
    r=c.request('POST',f'/workspaces/{w}/semanticModels/{m}/getDefinition',{},label='model-'+uuid.uuid4().hex)
    definition=c.finish(r,'model-definition')['body'];save(Path(run)/'model-definition.json',definition)
    decoded=parts(definition);fields=[];q=r"(?:'((?:[^']|'')+)'|([^\s=]+))"
    types={'int64':'Int64','double':'Double','decimal':'Decimal','string':'String','dateTime':'DateTime','boolean':'Boolean'}
    for name,b in decoded.items():
        if not name.startswith('definition/tables/') or not name.endswith('.tmdl'):continue
        s=b.decode('utf-8-sig');t=re.search('^table '+q,s,re.M)
        if not t:raise ValueError('Unrecognized TMDL table declaration: '+name)
        tn=(t[1] or t[2]).replace("''", "'");matches=list(re.finditer(r'^\t(measure|column) '+q,s,re.M))
        for i,x in enumerate(matches):
            kind=x[1];cn=(x[2] or x[3]).replace("''", "'");body=s[x.end():matches[i+1].start() if i+1<len(matches) else len(s)]
            dt=re.search(r'^\t\tdataType: (\w+)',body,re.M);fmt=re.search(r'^\t\tformatString: (.+)',body,re.M)
            # These five recipes use numeric measures; TMDL commonly omits their
            # return type. Non-numeric measure authoring needs an explicit catalog.
            dtype=types.get(dt[1]) if dt else 'Double' if kind=='measure' else None
            if not dtype:continue
            fields.append({'id':tn+'['+cn+']','tableName':tn,'columnName':cn,'columnType':'Measure' if kind=='measure' else 'Column','dataType':dtype,'formatString':fmt[1] if fmt else ''})
    if not fields:raise ValueError('Selected TMDL branch unavailable; supply a current model catalog per runtime-guide.md')
    ref['semanticModelName']=item.get('displayName',ref.get('semanticModelName'))
    model={'reference':ref,'fields':fields};save(Path(run)/'current-model.json',model);return model

def field_requirements(case):
    keys=set()
    for s in case['spec']['sheets']:
        keys.update(s['rows']+s['columns']);keys.update(m['source'] for m in s['measures'] if m['kind']=='Native')
        for g in s.get('dimensionKeyGroups',[]):keys.update([g['leaf'],g['key'],*g['ancestors']])
    for d in case['spec']['dashboards']:
        keys.update(s['field'] for s in d['slicers'])
        for chart in d['charts']:keys.update([chart['field'],chart['category']])
    return sorted(keys)

def recipe_contract(case,model):
    """Offline completeness of symbolic dependencies, scope and chart bindings."""
    spec=case['spec'];post=case['post'];sheets={s['name']:s for s in spec['sheets']}
    if len(sheets)!=len(spec['sheets']):raise ValueError('Duplicate sheet name')
    missing=set(field_requirements(case))-{f['id'] for f in model['fields']}
    if missing:raise ValueError('Missing current model fields: '+', '.join(sorted(missing)))
    if set(post)-{'steps','quarterly','comparisons','negative','percent','periodFilters'}:raise ValueError('Unconsumed native phase')
    labels={n:{m['label']:m['kind'] for m in s['measures']} for n,s in sheets.items()}
    for n,s in sheets.items():
        if len(labels[n])!=len(s['measures']):raise ValueError('Ambiguous measure labels: '+n)
    def link(source,target,source_measure,label):
        src=sheets[source];dst=sheets[target]
        from .storage_context import require_same
        require_same(src,dst)
        if not set(dst['rows'])<=set(src['rows']) or dst['columns']!=src['columns'][:len(dst['columns'])]:raise ValueError('Incompatible From Sheets grain')
        if labels[source].get(source_measure) not in ('DataInput','Forecast','Formula'):raise ValueError('From Sheets needs a produced measure; native companions are not outputs')
        if label in labels[target]:raise ValueError('Destination caption collision: '+label)
        labels[target][label]='FromSheets'
    q=post.get('quarterly')
    if q:
        link(q['sourceSheet'],q['targetSheet'],q['sourceForecast'],q['forecastLabel'])
        if q['targetActuals'] not in labels[q['targetSheet']]:raise ValueError('Unresolved quarterly actuals')
        labels[q['targetSheet']][q['varianceLabel']]='Formula';labels[q['targetSheet']][q['commentaryLabel']]='DataInput'
    for step in post.get('steps',[]):
        n=step['sheet']
        for item in step.get('links',[]):link(item['sourceSheet'],n,item['sourceMeasure'],item['label'])
        for f in step.get('formulas',[]):
            if set(re.findall(r'\$\{([^}]+)\}',f['expression']))!=set(f['symbols']):raise ValueError('Formula symbols incomplete')
            if not set(f['symbols'].values())<=set(labels[n]):raise ValueError('Formula dependency order is incomplete')
            if f['label'] in labels[n]:raise ValueError('Formula caption collision')
            labels[n][f['label']]='Formula'
        if step.get('commentary'):labels[n][step['commentary']]='DataInput'
        if not set(step.get('negative',[]))<=set(labels[n]):raise ValueError('Unresolved conditional-format target')
    comparisons={c['owner']:c for c in post['comparisons']}
    if set(comparisons)!=set(sheets):raise ValueError('Every recipe owner requires its explicit comparison contract')
    for name,c in comparisons.items():
        if not {c['left'],c['right']}<=set(labels[name]):raise ValueError('Unresolved chart comparison')
    for kind in ('negative','percent'):
        for name,ls in post.get(kind,{}).items():
            if not set(ls)<=set(labels[name]):raise ValueError('Unresolved '+kind+' formatting')
    if set(post['periodFilters'])!=set(sheets):raise ValueError('Missing planning period selection')
    actual={'planningSheets':len(sheets),'dashboards':len(spec['dashboards']),'comparisonCharts':sum(len(d['charts']) for d in spec['dashboards']),'home':spec['home']['show']}
    if actual!=case['expected']:raise ValueError('Recipe shape differs from expected output')
    return {'shape':actual,'finalMeasures':labels,'dependencies':'resolved symbolically','runtimeValidation':'not run'}

def prepare(key,model,run,name=None):
    run=Path(run);case=recipe(key);p=run/'recipe.json'
    contract=recipe_contract(case,model)
    from .authoring_flow import require_authored_flow
    if p.exists():
        before=load(p)
        if before['case']!=case or before['modelHash']!=sha(dumps(model)) or (name and before['name']!=name):raise ValueError('Resume recipe/model/name drift; do not recreate an existing application')
        cached=load(run/'construction.json')
        require_authored_flow(cached,case['spec'])
        return cached,case,before['name']
    missing=set(field_requirements(case))-{f['id'] for f in model['fields']}
    if missing:raise ValueError('Resolve current model fields; missing: '+', '.join(sorted(missing)))
    name=name or case['title']+' '+str(int(time.time()));spec=copy.deepcopy(case['spec']);spec['name']=name
    b=build_application(model,spec)
    from .filters import selection,select_axis_filter
    from .matrix_formatting import compile_formatting
    for s,ident in zip(spec['sheets'],b['identities']):
        path=f"sheets/{ident['sheetId']}/visuals/{ident['visualId']}/properties.json";props=b['raw'][path]['properties']
        period=case['post']['periodFilters'][s['name']]
        select_axis_filter(props,period['field'],selection(model,period['field'],values=period['values']))
        ids={m['label']:m['id'] for m in props['visualState']['manage_measures']}
        for label in case['post'].get('negative',{}).get(s['name'],[]):props=apply_negative_variance(props,ids[label],label)
        ops=[{'key':'pct-'+ids[label],'scope':'measure','id':ids[label],'format':{'percentage':True,'decimals':1}} for label in case['post'].get('percent',{}).get(s['name'],[])]
        if ops:props['visualState']=compile_formatting(props['visualState'],{'operations':ops})['state']
        b['raw'][path]['properties']=props
    b['envelope']=pack(b['raw']);save(run/'construction.json',b);save(run/'spec.json',spec)
    require_authored_flow(b,spec)
    save(run/'recipe-contract.json',contract)
    save(p,{'case':case,'name':name,'modelHash':sha(dumps(model))})
    save(run/'phase-ledger.json',{'base':'constructed','modelFields':'resolved','expected':case['expected'],
      'pending':['create/import','native identities','embedding geometry','linked measures and dependent formulas','presentation and column defaults','integrated comparison charts','dashboard visibility','Home content'],
      'runtimeValidation':'not run','completeness':'Local base only; execute deploy to complete the native phases'})
    return b,case,name

def extend_sheet(client,step,run):
    """Ordered links -> dependent formula DAG -> typed commentary -> companions."""
    from .builder_api import create_column
    eid,vid,p=owner(client,step['sheet']);existing=columns(client,vid)
    labels=[x['name'] for x in existing]
    if len(labels)!=len(set(labels)):raise ValueError('Ambiguous native measure captions in '+step['sheet'])
    bylabel={x['name']:x['measureGuid'] for x in existing}
    f=Path(run)/('ids-'+vid+'.json');reg=Registry(load(f) if f.exists() else {})
    assignments=[];created=[]
    for link in step.get('links',[]):
        se,sv,sp=owner(client,link['sourceSheet']);cs=columns(client,sv);source=find_column(cs,link['sourceMeasure'])
        from .storage_context import require_same
        require_same(sp,p)
        for axis in ('rowDimensions','columnDimensions'):
            src=[x['externalKey'] for x in sp['visualState'][axis]];dst=[x['externalKey'] for x in p['visualState'][axis]]
            if not set(dst)<=set(src) or (axis=='columnDimensions' and dst!=src[:len(dst)]):raise ValueError('Current native source/target grain changed')
        a=resolve_measure({'sourceType':'Visual','visualId':sv,'sourceMeasureGuid':source['measureGuid'],'bucket':'ameasure','order':len(p['pivotAssignments'])+len(assignments),'label':link['label']},sheets=[{'visualId':sv,'name':link['sourceSheet'],'properties':sp,'columns':cs}])
        assignments.append(a);mid=a['measureGuid'];bylabel[link['label']]=mid
        created.append({'measureGuid':mid,'columnType':6,'name':link['label'],'columnMeta':{'id':mid,'label':link['label'],'data_type':'Number','measure_type':{'Native':{'measure_role':'FCMeasure'}}}})
    for formula in step.get('formulas',[]):
        mid=reg.custom(formula['label']);created.append(formula_create(mid,formula['label'],formula['expression'],{k:bylabel[v] for k,v in formula['symbols'].items()}));bylabel[formula['label']]=mid
    commentary=step.get('commentary')
    if commentary:
        mid=reg.custom(commentary);created.append(input_create(mid,commentary,'LongText',{},str(uuid.uuid5(uuid.NAMESPACE_URL,vid+commentary)),visual_column=False));bylabel[commentary]=mid
    save(f,reg.entries)
    for payload in created:
        result=create_column(client,vid,payload,'create-'+vid+'-'+payload['measureGuid'])
        save(Path(run)/('created-'+vid+'-'+payload['measureGuid']+'.json'),result)
        if result.get('status')=='pending':raise RuntimeError('Pending native column jobs; reconcile their completion before dependent writes')
    def register(prop):
        for a in assignments:prop['pivotAssignments']=[x for x in prop['pivotAssignments'] if x.get('measureGuid')!=a['measureGuid']]+[a]
        vs=prop['visualState'];ms=vs['manage_measures']
        for x in created:
            mid=x['measureGuid'];found=next((m for m in ms if m['id']==mid),None)
            if found:found.update(label=x['name'],visible=True)
            else:ms.append({'id':mid,'label':x['name'],'visible':True,'order':len(ms)})
            ag='None' if x['name']==commentary else 'Sum'
            vs['aggregation_config']['measure_aggregation'][mid]={'row':ag,'column':ag}
            vs['formatConfig']['measure'].setdefault(mid,[{'format':{'4':'Arial'},'order':len(ms)}])
        from .display_defaults import auto_number_formatting
        prop['visualState']=auto_number_formatting(vs,[x['measureGuid'] for x in created if x['columnMeta'].get('data_type')=='Number'])
        for label in step.get('negative',[]):prop=apply_negative_variance(prop,bylabel[label],label)
        return prop
    return save_properties(client,eid,vid,register,'extend-'+vid)

def finish_native(client,auth,case,model,run,*,alm_client=None,workspace=None,plan=None):
    from .intelligence_api import deploy_geometry,visibility_native
    from .column_presentation import apply_column_presentation
    from .application_defaults import check_application_defaults,require_delivery_phases
    check_application_defaults(auth['raw'],auth.get('home'))
    from .authoring_flow import require_authored_flow
    require_authored_flow(auth,case['spec'])
    run=Path(run)
    def phase(key,fn):
        file=run/(key+'.json')
        if file.exists():return load(file)
        result=fn();save(file,result);return result
    mapping=phase('native-identities',lambda:resolve_planning(client,auth['raw']))
    for dash in auth['dashboardIdentities']:
        phase('geometry-'+dash['sheetGuid'],lambda d=dash:deploy_geometry(client,auth['raw'],d,mapping,'geometry-'+d['sheetGuid'],verify=False))
    if case['post'].get('quarterly'):
        result=phase('quarterly',lambda:quarterly_review(client,case['post']['quarterly'],run/'quarterly-records'))
        if result.get('status')!='saved':raise RuntimeError('Quarterly dependencies remain incomplete')
    for i,step in enumerate(case['post'].get('steps',[])):phase('step-'+str(i),lambda s=step:extend_sheet(client,s,run/'extended'))
    owners=[]
    for sheet in case['spec']['sheets']:
        eid,vid,p=owner(client,sheet['name']);cs=columns(client,vid)
        owners.append({'name':sheet['name'],'entityId':eid,'visualId':vid,'properties':p,'columns':cs})
        def presentation(q,s=sheet,records=cs):
            return apply_column_presentation(apply_presentation(q,records,s['name'],s['header'],override_colors=True)['properties'])
        phase('presentation-'+vid,lambda e=eid,v=vid,fn=presentation:save_properties(client,e,v,fn,'presentation-'+v))
    es=entities(client)['workloadEntities']
    for comp in case['post']['comparisons']:
        src=next(o for o in owners if o['name']==comp['owner'])
        left,right=comparison_measures(client,src,comp,owners,model)
        targets=[d['name'] for d in case['spec']['dashboards'] if d['owner']==comp['owner']]
        for target in targets:
            matches=[e for e in es if e['displayName']==target]
            if len(matches)!=1:raise ValueError('Ambiguous comparison dashboard')
            eid=str(matches[0]['id']);p=page(client,eid)
            for v in p['payload']['visuals']:
                if v.get('isEmbedded') or v.get('visualType')!=50:continue
                if v['properties']['properties'].get('chartType')=='CARD':continue
                vid=str(v['id'])
                phase('comparison-'+vid,lambda e=eid,v=vid,a=left,b=right:save_properties(client,e,v,lambda q:comparison_chart(q,a,b),'comparison-'+v))
    from .application_typography import finish_native_typography
    save(run/'native-typography.json',finish_native_typography(client))
    from .navigation_publish import publish
    requests={s['recordGuid']:False for s in auth['raw']['definition.json']['sheets'] if s['sheetType']=='PLANNING'}
    requests.update({d['sheetGuid']:True for d in auth['dashboardIdentities']})
    published=publish(alm_client,client,workspace,plan,auth['raw'],requests,'publish-business-navigation')
    for dash in auth['dashboardIdentities']:save(run/('visible-'+dash['sheetGuid']+'.json'),published[dash['sheetGuid']])
    def home():
        h=case['spec']['home'];role=h['roleId'];before=result_body(client.request('GET','/v1/access/roles/layout/'+role+'/'))
        from .application_defaults import public_home_layout
        body={'homeLayoutOrder':h['order'],'data':public_home_layout(auth['home'],mapping)}
        if before.get('etag'):body['etag']=before['etag']
        return result_body(client.request('POST','/v1/access/roles/layout/'+role+'/',body,label='home-content'))
    phase('home-content',home)
    required=require_delivery_phases(auth,home_saved=True,
        home_visible=auth['raw']['planProperties.json']['properties']['homeLayout']['show'] is True,
        dashboard_geometry=[d['sheetGuid'] for d in auth['dashboardIdentities'] if (run/('geometry-'+d['sheetGuid']+'.json')).exists()],
        dashboard_visibility=[d['sheetGuid'] for d in auth['dashboardIdentities'] if (run/('visible-'+d['sheetGuid']+'.json')).exists()])
    return {'phases':'saved','mandatoryDefaults':required,'expected':case['expected'],'runtimeValidation':'not run','postSaveValidation':'not run'}

def comparison_measures(client,source,comparison,owners,model):
    """Read current query metadata only when a selected companion needs it.

    No SQL reader, reload or refresh is needed to resolve either binding route.
    """
    from .consumer_bindings import find_query
    from .builder_api import segment
    records=[find_column(source['columns'],comparison[side]) for side in ('left','right')]
    mids={r['measureGuid'] for r in records};queries=[]
    qids={a['queryId'] for a in source['properties'].get('pivotAssignments',[])
        if a.get('measureGuid') in mids and a.get('sourceType')=='InfoBridge'}
    for qid in sorted(qids):
        metadata=result_body(client.request('GET',f'/v2/ib/query/{segment(qid)}/meta/'))
        if not isinstance(metadata,list):raise ValueError('Expected current query metadata records')
        queries.append(find_query(metadata,qid))
    return tuple(registered_measure(source['properties'],r,source['visualId'],source['name'],
        model=model,bucket=bucket,sheets=owners,queries=queries) for r,bucket in zip(records,('AC','PY')))

def deploy(key,config,model,run,name=None):
    """Create a new application or resume this run; never overwrite by report name."""
    if not config.get('authorizedMutation'):raise ValueError('Deployment requires the current user-authorized destination')
    if config.get('planId'):raise ValueError('Usecase deploy creates/resumes a new Plan; existing-report changes need a scoped repair')
    run=Path(run);auth,case,name=prepare(key,model,run,name)
    from .application_defaults import check_application_defaults
    check_application_defaults(auth['raw'],auth.get('home'))
    target={k:config[k] for k in ('apiBase','powerbiApiBase','workspaceId')};target['modelReference']=model['reference']
    tp=run/'target.json'
    if tp.exists() and load(tp)!=target:raise ValueError('Resume destination drift')
    save(tp,target)
    done=run/'completed.json'
    if done.exists() and load(done).get('mandatoryDefaults',{}).get('mandatoryDefaults')=='passed':return load(done)
    c=Client(config['apiBase'],config['tokenEnvironment'],config.get('allowedHosts'),run/'public-api')
    cp=run/'created.json'
    created=load(cp) if cp.exists() else plan_operation(c,config['workspaceId'],'create-blank',name=name,label='create')
    save(cp,created);plan=created.get('body',{}).get('id')
    if not plan:raise ValueError('Create receipt missing Plan ID; reconcile, do not repeat create')
    candidate=run/'candidate.json'
    if not candidate.exists():
        baseline=plan_operation(c,config['workspaceId'],'export',plan,label='blank-export')['body'];save(run/'blank-definition.json',baseline)
        raw=unpack(baseline)
        if raw['definition.json'].get('sheets'):raise ValueError('Expected newly created blank Plan')
        for k,v in auth['raw'].items():raw[k]=merge(raw[k],v) if k in raw else copy.deepcopy(v)
        save(candidate,pack(raw))
    from .authoring_flow import require_authored_flow
    require_authored_flow(auth,case['spec'],unpack(load(candidate)))
    saved=run/'import.json'
    if not saved.exists():save(saved,plan_operation(c,config['workspaceId'],'update',plan,definition=load(candidate),label='import'))
    with native_session(config['powerbiApiBase'],config['tokenEnvironment'],config['workspaceId'],plan,run/'native-api',native_read_versions=config.get('nativeReadVersions')) as client:
        result=finish_native(client,auth,case,model,run/'native-phases',alm_client=c,workspace=config['workspaceId'],plan=plan)
    result.update(planId=plan,name=name,case=case['id']);save(done,result)
    save(run/'phase-ledger.json',{'base':'saved','nativePhases':'saved','expected':case['expected'],'pending':[],'runtimeValidation':'not run','postSaveValidation':'not run'})
    return result
