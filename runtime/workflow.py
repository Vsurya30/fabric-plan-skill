"""Resumable API-only provisioning with explicit per-module fallbacks.

Unsupported requested features are recorded and isolated before compiling the
supported subset. They do not prevent independent application work.
"""
from pathlib import Path
import copy,uuid
from .codec import load,save,sha,dumps,unpack,pack
from .construct import build
from .transport import Client,plan_operation
from .validate import validate_plan,schema_report
from .session import native_session,resolve_planning
from .home_api import deploy_home,visibility_via_alm
from .surfaces import home_item,home_layout
from .home_fit import readable_home_layout
from .readback import verify_authored

SUPPORTED={'planning.anchor-measure','planning.conditional-formatting','planning.numeric','planning.formula','planning.native-measure','planning.forecast',
           'planning.pivots','planning.conditional-edit-policy','planning.dimension-id-mapping','planning.filter-context',
           'intelligence.slicers','intelligence.cards','intelligence.charts','intelligence.text','intelligence.embeds','home.text','home.cards','home.visibility'}

def preflight(spec):
    requested=spec.get('requiredCapabilities')
    if not isinstance(requested,list) or not requested: raise ValueError('Agent must enumerate requiredCapabilities from the complete business request')
    unknown=set(requested)-SUPPORTED
    if unknown: raise ValueError('API_CONSTRUCTION_GAP: '+', '.join(sorted(unknown)))
    allowed={'name','sheets','requiredCapabilities','home','dashboards'}
    if set(spec)-allowed: raise ValueError('Unconsumed spec modules: '+', '.join(sorted(set(spec)-allowed)))
    for s in spec['sheets']:
        known={'name','sheetId','visualId','rows','columns','measures','pivots','activePivot','capabilities','pivot',
               'row_expand_state_config','filterContextSettings','superFilterAssignments','header','comments','hidden',
               'dimensionKeyGroups','dimensionKeyOverrides','dimensionIdMappings','dimensionSkipSupport','lookupContextAssignments','context','columnTimeLevels','conditionalFormatting'}
        if set(s)-known: raise ValueError('Unconsumed/unsupported sheet modules: '+', '.join(sorted(set(s)-known)))
        for m in s['measures']:
            if m['kind'] not in ('Native','Formula','DataInput','Forecast') or m.get('inputKind','Number')!='Number':
                raise ValueError('API_CONSTRUCTION_GAP: complete selected input factory')
        if any(k in s for k in ('data_input_rules','measureModelConfig','advancedLookup','forecast')):
            raise ValueError('API_CONSTRUCTION_GAP: selected feature needs complete API factory')
    if spec.get('home'):
        h=spec['home'];order=h.get('order',1)
        if isinstance(order,bool) or not isinstance(order,int) or order<0: raise ValueError('Invalid Home priority')
        if not isinstance(h.get('show',True),bool): raise ValueError('Home visibility must be Boolean')
        if not isinstance(h.get('roleId','__everyone__'),str) or not h.get('roleId','__everyone__'): raise ValueError('Home role identity required')
        if any(b['type'] not in ('text','preview-cards') for b in spec['home']['blocks']):
            raise ValueError('API_CONSTRUCTION_GAP: Home uploaded assets/advanced nodes')
    return {'status':'passed-construction-subset','runtimeAcceptance':'separate'}

def compile_home(spec):
    items=[]; symbols={}
    for block in spec['blocks']:
        key=block['key']
        if key in symbols: raise ValueError('Duplicate Home block key')
        item=home_item(block['type'],block.get('title',''),block.get('description',''),columns=block.get('columns',4))
        items.append(item);symbols[key]=item['id']
    rows=[{'itemIds':[symbols[k] for k in r['blocks']],**{k:v for k,v in r.items() if k in ('height','widths')}} for r in spec['rows']]
    return readable_home_layout(items,rows,content_width_px=spec.get('contentWidthPx'))

def provision(config,model,spec,run):
    from .scope import prepare_scope
    run=Path(run);run.mkdir(parents=True,exist_ok=True)
    scope=prepare_scope(spec,SUPPORTED,model)
    save(run/'scope-coverage.json',scope)
    if not scope['completeOriginalScope']:
        # Scope analysis is a local diagnostic, never permission to deploy a
        # reduced reference-only substitute for the requested application.
        return {'planId':None,'completion':'Requested flow needs documented component phases; no reduced application deployed',
                'coverage':scope['coverage'],'originalScopeComplete':False,'mutation':'none'}
    spec=scope['spec']
    if not spec['sheets']:
        # No fake financial sheet is created from guessed fields or zero values.
        return {'planId':None,'completion':'No independent supported data sheet remains',
                'coverage':scope['coverage'],'originalScopeComplete':False,'mutation':'none'}
    from .planning_presentation import application_defaults,check_application,build_application
    spec=application_defaults(model,spec)
    preflight(spec)
    if config['name']!=spec['name']: raise ValueError('Creation name and authored Plan name differ')
    if not config.get('authorizedMutation'): raise ValueError('Current user authorization required')
    signature=sha(dumps({'model':model,'spec':spec,'target':{k:config[k] for k in ('apiBase','powerbiApiBase','workspaceId','name')}}))
    cp=run/'construction.json'
    if cp.exists():
        authored=load(cp)
        if authored['signature']!=signature: raise ValueError('Resume input drift; reconcile explicitly without recreating the Plan')
    else:
        authored=build_application(model,spec);validate_plan(authored['raw']);check_application(authored['raw'])
        authored.update(signature=signature,publicSchemas=schema_report(authored['raw']))
        save(cp,authored)
    from .application_defaults import check_application_defaults,require_delivery_phases
    # Resumed/cached constructions must satisfy the same mandatory baseline.
    check_application_defaults(authored['raw'],authored.get('home'))
    from .authoring_flow import require_authored_flow
    require_authored_flow(authored,spec)
    client=Client(config['apiBase'],config['tokenEnvironment'],config.get('allowedHosts'),run/'public-api')
    receipt=run/'created-plan.json'
    created=load(receipt) if receipt.exists() else plan_operation(client,config['workspaceId'],'create-blank',name=config['name'],label='create-blank')
    plan=created.get('body',{}).get('id')
    if not plan: raise ValueError('Creation result has no Plan ID; retain receipt and reconcile inventory, never repeat create')
    save(receipt,created)
    payload_path=run/'initial-update.json'
    if not payload_path.exists():
        fresh=plan_operation(client,config['workspaceId'],'export',plan,label='blank-export')['body']
        raw=unpack(fresh)
        if raw['definition.json'].get('sheets'): raise ValueError('Expected newly created empty Plan; no old template accepted')
        # Preserve server initialization fields while filling authored keys.
        def merge(a,b):
            out=copy.deepcopy(a)
            for k,v in b.items():
                out[k]=merge(out[k],v) if isinstance(v,dict) and isinstance(out.get(k),dict) else copy.deepcopy(v)
            return out
        for k,v in authored['raw'].items(): raw[k]=merge(raw[k],v) if k in raw else copy.deepcopy(v)
        save(payload_path,pack(raw))
    require_authored_flow(authored,spec,unpack(load(payload_path)))
    update_receipt=run/'initial-update-result.json'
    if update_receipt.exists():
        updated=load(update_receipt)
    else:
        prior_intent=(run/'public-api/initial-update.intent.json').exists()
        recovered=False
        if prior_intent:
            # A lost write response may have applied. Reconcile before any replay.
            current=plan_operation(client,config['workspaceId'],'export',plan,label='reconcile-update-'+uuid.uuid4().hex)['body']
            try: verify_authored(unpack(current),authored['raw'],[d['sheetGuid'] for d in authored.get('dashboardIdentities',[])]);recovered=True
            except ValueError: pass
        if recovered:
            updated={'status':'reconciled-current-definition','operationTerminalStatus':'unknown'}
        else:
            updated=plan_operation(client,config['workspaceId'],'update',plan,definition=load(payload_path),label='initial-update')
        save(update_receipt,updated)
    fresh=plan_operation(client,config['workspaceId'],'export',plan,label='verify-export-'+uuid.uuid4().hex)['body']
    raw=unpack(fresh);save(run/'deployed-definition.json',fresh);save(run/'deployed-decoded.json',raw)
    require_authored_flow(authored,spec,raw)
    persisted=verify_authored(raw,authored['raw'],[d['sheetGuid'] for d in authored.get('dashboardIdentities',[])]);save(run/'authored-readback.json',persisted)
    home=None;registration='not-verified';phase_errors=[];dashboards=[];mapping={}
    try:
        with native_session(config['powerbiApiBase'],config['tokenEnvironment'],config['workspaceId'],plan,run/'native-api',native_read_versions=config.get('nativeReadVersions')) as native:
            try:
                mapping=resolve_planning(native,authored['raw']);save(run/'runtime-identities.json',mapping);registration='passed'
            except (ValueError,KeyError,RuntimeError) as e:
                phase_errors.append({'phase':'native-registration','status':'not-verified','errorType':type(e).__name__})
            for dashboard in authored.get('dashboardIdentities',[]):
                try:
                    from .intelligence_api import deploy_geometry,visibility_native
                    verified=deploy_geometry(native,authored['raw'],dashboard,mapping,'dashboard-'+dashboard['sheetGuid'])
                    verified['sheetGuid']=dashboard['sheetGuid']
                    verified['visibility']={'nativeReadback':'pending'}
                    dashboards.append(verified);save(run/('dashboard-'+dashboard['sheetGuid']+'.json'),verified)
                except (ValueError,KeyError,RuntimeError) as e:
                    hidden='not-verified'
                    try:
                        from .intelligence_api import visibility_native
                        from .session import entities
                        candidates=[e for e in entities(native)['workloadEntities'] if e['displayName']==dashboard['name'] and e['entityType']==20]
                        if len(candidates)!=1:raise ValueError('Unresolved failed dashboard')
                        visibility_native(native,str(candidates[0]['id']),False,'hide-dashboard-'+dashboard['sheetGuid']+'-'+uuid.uuid4().hex)
                        hidden='hidden'
                    except (ValueError,KeyError,RuntimeError): pass
                    phase_errors.append({'phase':'dashboard','name':dashboard['name'],'status':'not-verified','visibility':hidden,'errorType':type(e).__name__})
            if dashboards:
                try:
                    from .navigation_publish import publish
                    requests={s['recordGuid']:False for s in authored['raw']['definition.json']['sheets'] if s['sheetType']=='PLANNING'}
                    requests.update({d['sheetGuid']:True for d in dashboards})
                    published=publish(client,native,config['workspaceId'],plan,authored['raw'],requests,'publish-business-navigation')
                    for d in dashboards:
                        d['visibility']=published[d['sheetGuid']]
                        save(run/('dashboard-'+d['sheetGuid']+'.json'),d)
                except (ValueError,KeyError,RuntimeError) as e:
                    phase_errors.append({'phase':'dashboard-publication','status':'not-verified','errorType':type(e).__name__})
            if spec.get('home'):
                try:
                    from .application_defaults import public_home_layout
                    h=spec['home'];home=deploy_home(native,h.get('roleId','__everyone__'),public_home_layout(authored['home'],mapping),h.get('order',1),'home-content')
                    home.update(visibility_via_alm(client,config['workspaceId'],plan,h.get('show',True),'home-visibility'))
                except (ValueError,KeyError,RuntimeError) as e:
                    phase_errors.append({'phase':'home','status':'not-verified','errorType':type(e).__name__})
    except (ValueError,KeyError,RuntimeError) as e:
        phase_errors.append({'phase':'native-session','status':'not-verified','errorType':type(e).__name__})
    required=None
    try:
        required=require_delivery_phases(authored,home_saved=home is not None,
            home_visible=bool(home and home.get('visibility')=='passed-persisted-workload-show'),
            dashboard_geometry=[d['sheetGuid'] for d in authored.get('dashboardIdentities',[]) if (run/('dashboard-'+d['sheetGuid']+'.json')).exists()],
            dashboard_visibility=[d['sheetGuid'] for d in dashboards if d.get('visibility',{}).get('nativeReadback')=='passed'])
    except ValueError as e:
        phase_errors.append({'phase':'mandatory-application-defaults','status':'incomplete','error':str(e)})
    evidence={'planId':plan,'construction':'passed','mandatoryDefaults':required,'import':updated.get('status'),'authoredReadback':persisted,'nativeRegistration':registration,
        'home':home,'dashboards':dashboards,'calculation':'not-tested','inputEdits':'not-tested','connectedPropagation':'not-tested','rendering':'not-tested',
        'completion':'Supported application saved; evaluate retained scope and runtime checks separately',
        'coverage':scope['coverage'],'originalScopeComplete':scope['completeOriginalScope'] and not phase_errors,'phaseErrors':phase_errors}
    save(run/'acceptance.json',evidence);return evidence
