"""Executable From Sheets, quarterly commentary/variance, CF and chart composition.

Uses the bundled native session. No agent SDK, source checkout or old Plan needed.
These application routes are tenant/build-dependent, not public Fabric REST APIs.
Successful saves are not calculation/rendering certification.
"""
import copy,uuid
from pathlib import Path
from .codec import load,save,dumps
from .identity import xxh3,Registry,native_id
from .session import entities,page,columns,result_body
from .builder_api import scoped
from .input_factories import input_create,formula_create
from .chart_filters import ensure_chart_filters

def from_sheet_assignment(source,source_visual,source_name,label=None,bucket='ameasure',order=1):
    """source is a current /datainput/column/ record, NOT an ALM record.

    Fabric SQL uses the source row id; OneLake can use source measureGuid when
    the row id is absent. Runtime visual IDs differ from ALM visual GUIDs.
    This selected constructor supports numeric SUM at same/subset grain.
    """
    from .measure_bindings import record_kind,sheet_column_id
    if record_kind(source) not in ('DataInput','Formula','Forecast'):
        raise ValueError('Native companions are not From Sheets outputs; resolve the original source assignment')
    if source.get('visualId') is not None and str(source['visualId'])!=str(source_visual):
        raise ValueError('Source column belongs to a different visual')
    if isinstance(source_visual,bool) or not str(source_visual).isdecimal():
        raise ValueError('Resolve native source column and visual IDs before linking')
    native_id(str(source_visual));source_id=sheet_column_id(source)
    if source['columnMeta'].get('data_type')!='Number':raise ValueError('SUM requires numeric source')
    if bucket not in ('ameasure','AC','PY'):raise ValueError('Selected supported destination bucket required')
    mid=str(xxh3('SUM__'+source_id));label=label or source['name']
    return {'aggregationType':'sum','bucketId':bucket,'columnName':source['name'],
        'columnType':'Column','customName':label,'dataRoleType':'Measure','dataType':'Double',
        'formatString':'#,0.00','id':source_id,'sourceId':source_id,
        'measureGuid':mid,'sourceType':'Visual','tableName':source_name,'visualId':str(source_visual),
        'name':label,'order':order,'isFlatHierarchy':False,'isRenamed':True}

def negative_variance_rule(measure_id,label='Variance',rule_name=None):
    native_id(measure_id)
    from .matrix_formatting import conditional_rule
    return conditional_rule(_negative_request(measure_id,label,rule_name),
        {'measure':{measure_id},'labels':{measure_id:label},'rowDimensionOrder':[]})

def _negative_request(measure_id,label,rule_name=None):
    return {'id':rule_name or 'negative_variance_'+measure_id,'label':label+' below zero',
        'target':measure_id,'test':measure_id,'operator':'<','threshold':0,
        'rowScope':'both','columnScope':'both','excludeRowTotal':False,'excludeColumnTotal':False,
        'appearance':{'textColor':'#B42318','background':'#FEE4E2','bold':True}}

def apply_negative_variance(properties,measure_id,label='Variance'):
    from .matrix_formatting import compile_formatting
    out=copy.deepcopy(properties)
    out['visualState']=compile_formatting(out['visualState'],{'rules':[_negative_request(measure_id,label)]})['state']
    return out

def variance_config(*, integrated=True):
    if integrated:
        from .integrated_variance import integrated_variance_config
        return integrated_variance_config()
    def item(role,chart,typ,order,axis,visible):
        return {'role':role,'isVisible':visible,'chartIsVisible':visible,'enable':visible,
            'chart':chart,'type':typ,'order':order,'calcFormula':'','isWaterfallMeasure':False,
            'yAxis':axis,'isTrellis':False,'dimension':None,'legendMeasureInfoText':''}
    return {'instanceId':'DEFAULT_VISUAL_INSTANCE','config':[
        item('\u0394PY%','variancePin','RELATIVE_VARIANCE',0,'none',False),
        item('\u0394PY','varianceBar','ABSOLUTE_VARIANCE',1,'none',True),
        item('AC','groupedBar','ACTUAL',0,'yAxis1',True),item('PY','groupedBar','ACTUAL',1,'yAxis1',True)]}

def comparison_chart(properties,forecast_assignment,actuals_assignment, *, integrated=True):
    """Configure a type-50 comparison, integrated variance by default.

    AC and PY are chart comparison roles, independent of source namespace.
    Native AC-PY compares the supplied left and right measures. Keep their actual
    business captions and typed source IDs. Ordinary cards are reconciled to the
    surviving fields so an old binding cannot linger under the same caption.
    """
    out=copy.deepcopy(properties)
    if out.get('visualType')!=50:raise ValueError('Use an ANALYTICS_PLUS column chart')
    ac=copy.deepcopy(forecast_assignment);ac.update(bucketId='AC',order=0)
    py=copy.deepcopy(actuals_assignment);py.update(bucketId='PY',order=0)
    out['pivotAssignments']=[a for a in out['pivotAssignments'] if a.get('dataRoleType')!='Measure']+[ac,py]
    if integrated:
        from .integrated_variance import apply_integrated_variance
        out=apply_integrated_variance(out)
    else:
        out['visualState']['hiddenProperties_!!!_measureConfig']=dumps(variance_config(integrated=False)).strip()
    from .chart_filters import reconcile_chart_filters
    reconcile_chart_filters(out)
    return out

def owner(client,sheet_name):
    matches=[e for e in entities(client)['workloadEntities'] if e['displayName']==sheet_name]
    if len(matches)!=1:raise ValueError('Missing/ambiguous sheet '+sheet_name)
    eid=str(matches[0]['id']);p=page(client,eid)
    vs=[v for v in p['payload']['visuals'] if not v.get('isEmbedded') and v.get('visualType')==80]
    if len(vs)!=1:raise ValueError('Expected one owned Planning visual in '+sheet_name)
    return eid,str(vs[0]['id']),vs[0]['properties']['properties']

def find_column(catalog,name):
    xs=[c for c in catalog if c['name']==name or c['measureGuid']==name]
    if len(xs)!=1:raise ValueError('Missing/ambiguous measure '+name)
    return xs[0]

def save_properties(client,entity_id,visual_id,transform,label):
    before=page(client,str(entity_id));v=next(v for v in before['payload']['visuals'] if str(v['id'])==str(visual_id))
    props=transform(copy.deepcopy(v['properties']['properties']))
    if props==v['properties']['properties']:return {'status':'unchanged'}
    body={'visuals':{str(visual_id):{'schema':'0.0.1','properties':props}},'workloadEntities':{},'workload':{},
        'etags':{'visuals':{str(visual_id):v['properties']['etag']},'workloadEntities':{str(entity_id):before['payload']['etag']}}}
    return result_body(client.request('POST','/v1/workload/properties/batch/',body,label=label))

def quarterly_review(client,request,run):
    """Native post-import phase. No post-save reads or runtime tests.

    Reads only current identities, existing columns and mutation ETags. A returned
    asynchronous column job pauses dependents instead of pretending it completed.
    """
    run=Path(run);run.mkdir(parents=True,exist_ok=True)
    se,sv,sp=owner(client,request['sourceSheet']);te,tv,tp=owner(client,request['targetSheet'])
    if sv==tv:raise ValueError('Source and consumer must be distinct owners')
    from .storage_context import require_same
    require_same(sp,tp)
    ss=sp['visualState'];ts=tp['visualState']
    for key in ('rowDimensions','columnDimensions'):
        sk=[d['externalKey'] for d in ss[key]];tk=[d['externalKey'] for d in ts[key]]
        if not set(tk)<=set(sk):raise ValueError('From Sheets consumer must use same/subset dimensions')
        if key=='columnDimensions' and tk!=sk[:len(tk)]:raise ValueError('Use ordered coarser calendar levels')
    source=find_column(columns(client,sv),request['sourceForecast'])
    existing=columns(client,tv);actual=find_column(existing,request['targetActuals'])
    if 'Native' not in actual['columnMeta']['measure_type']:raise ValueError('Resolve native actuals')
    label=request.get('forecastLabel','Sales Forecast');assignment=from_sheet_assignment(source,sv,request['sourceSheet'],label)
    mid=assignment['measureGuid'];statefile=run/'review-identities.json'
    if statefile.exists():ids=load(statefile)
    else:
        reg=Registry();ids={'sourceVisual':sv,'targetVisual':tv,'linked':mid,'variance':reg.custom('variance'),
            'commentary':reg.custom('commentary'),'commentaryConfig':str(uuid.uuid4())};save(statefile,ids)
    if any(ids[k]!=v for k,v in [('sourceVisual',sv),('targetVisual',tv),('linked',mid)]):raise ValueError('Resume identity changed')
    commentary=request.get('commentaryLabel','Quarterly Commentary');variance=request.get('varianceLabel','Variance')
    created=[{'measureGuid':mid,'columnType':6,'name':label,'columnMeta':{'id':mid,'label':label,'data_type':'Number','measure_type':{'Native':{'measure_role':'FCMeasure'}}}},
        input_create(ids['commentary'],commentary,'LongText',{},ids['commentaryConfig'],visual_column=False),
        formula_create(ids['variance'],variance,'${forecast} - ${actual}',{'forecast':mid,'actual':actual['measureGuid']})]
    from .builder_api import create_column
    for payload in created:
        r=create_column(client,tv,payload,'create-'+payload['measureGuid'])
        save(run/('created-'+payload['measureGuid']+'.json'),r)
        if r.get('status')=='pending':return {'status':'pending-column-jobs','jobIds':r['jobIds'],'dependentsSaved':False}
    def register(p):
        p['pivotAssignments']=[a for a in p['pivotAssignments'] if a.get('measureGuid')!=mid]+[assignment]
        s=p['visualState'];members=s.setdefault('manage_measures',[])
        for n,c in enumerate(created):
            cid=c['measureGuid'];entry=next((m for m in members if m['id']==cid),None)
            if entry is None:members.append({'id':cid,'label':c['name'],'order':len(members),'visible':True})
            else:entry.update(label=c['name'],visible=True)
            ag='None' if cid==ids['commentary'] else 'Formula' if cid==ids['variance'] else 'Sum'
            s.setdefault('aggregation_config',{}).setdefault('measure_aggregation',{})[cid]={'row':ag,'column':ag}
            s.setdefault('formatConfig',{}).setdefault('measure',{}).setdefault(cid,[{'format':{'4':'Arial','5':'#FFF0C2' if cid==ids['commentary'] else '#DFF2E7'},'order':n}])
        from .display_defaults import auto_number_formatting
        p['visualState']=auto_number_formatting(s,[mid,ids['variance']])
        from .column_presentation import ensure_assigned_measure_filters
        ensure_assigned_measure_filters(p)
        return apply_negative_variance(p,ids['variance'],variance)
    save_properties(client,te,tv,register,'review-register-'+tv)
    for chart in request.get('charts',[]):
        # Resolve current visual by unique layer name within the named dashboard.
        es=[e for e in entities(client)['workloadEntities'] if e['displayName']==chart['sheet']]
        if len(es)!=1:raise ValueError('Ambiguous dashboard')
        eid=str(es[0]['id']);p=page(client,eid)
        vs=[v for v in p['payload']['visuals'] if not v.get('isEmbedded') and v['properties']['properties'].get('layerProperties',{}).get('layerProperties',{}).get('name')==chart['visualName']]
        if len(vs)!=1:raise ValueError('Ambiguous chart layer')
        vid=str(vs[0]['id']);props=vs[0]['properties']['properties']
        actuals=[a for a in props['pivotAssignments'] if a.get('dataRoleType')=='Measure' and a.get('id')==chart['actualsField']]
        if len(actuals)!=1:raise ValueError('Assign the resolved semantic actuals measure to the base chart first')
        py=copy.deepcopy(actuals[0]);py.update(name=chart.get('actualsLabel','Sales Actuals'),customName=chart.get('actualsLabel','Sales Actuals'))
        save_properties(client,eid,vid,lambda p:comparison_chart(p,assignment,py),'variance-chart-'+vid)
    result={'status':'saved','linkedMeasureGuid':mid,'ids':ids,'runtimeValidation':'not-run','postSaveReads':False}
    save(run/'result.json',result);return result
