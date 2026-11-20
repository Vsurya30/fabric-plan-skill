"""API adapters for the user-supplied implementation contracts (not live-proven).

Caller selects the authenticated application/engine base. This module never
derives a new host or retries a mutation at another version/mount. Confirmed
metadata GET collections use the bounded SQL/OneLake read profile.
"""
import copy,base64,time,urllib.parse
from .transport import Client,HttpError
from .session import result_body,columns,page
from .readback import contains
from .codec import dumps
from .identity import native_id

def segment(value):
    if not isinstance(value,str) or not value:raise ValueError('Actual returned identity required')
    return urllib.parse.quote(value,safe='')

def job_ids(value):
    if not isinstance(value,list) or not value or any(not isinstance(x,str) or not x for x in value) or len(set(value))!=len(value):
        raise ValueError('Expected unique nonempty string job identities')
    return value

def column_matches(actual,expected):
    contains(actual['columnMeta'],expected['columnMeta'])
    # Writes use columnType; OneLake catalog records can expose dataInputType.
    # Resolve only this readback alias, without relaxing type or metadata checks.
    actual_type=actual.get('columnType',actual.get('dataInputType'))
    if 'columnType' in actual and 'dataInputType' in actual and actual['columnType']!=actual['dataInputType']:
        raise ValueError('Conflicting native column type aliases')
    if 'columnType' in expected and actual_type!=expected['columnType']:
        raise ValueError('Native column readback mismatch: columnType')
    # The enclosing native context flag is independent of the inner Boolean.
    for key in ('measureGuid','name','boundToFilterContext'):
        if key in expected and actual.get(key)!=expected[key]:raise ValueError('Native column readback mismatch: '+key)
def scoped(client,visual_id):
    if not isinstance(visual_id,str) or not visual_id.isdecimal():raise ValueError('Resolved numeric visual context required')
    from .native_profile import inherit
    return inherit(client,Client(client.base,client.token_env,client.allowed,client.journal,client.adapter,client.sleep,client.auth_scheme,
        {**client.context_headers,'x-target-visual':visual_id}))

def create_column(client,visual_id,payload,label,version=None):
    if version not in (None,'v1','v2'):raise ValueError('Selected native column API version required')
    required={'measureGuid','columnType','name','columnMeta'}
    if not required<=payload.keys():raise ValueError('Complete column create payload required')
    mid=native_id(payload['measureGuid'])
    if payload['columnMeta']['id']!=mid:raise ValueError('Column identity mismatch')
    c=scoped(client,visual_id)
    existing=[x for x in columns(client,visual_id,version=version) if x['measureGuid']==mid]
    from .native_profile import selected
    version=version or selected(client,'columns')
    if existing:
        if len(existing)!=1:raise ValueError('Duplicate native column')
        column_matches(existing[0],payload)
        return {'status':'persisted-record-readback','measureGuid':mid,'write':'already-matched','companions':'separate','execution':'not-tested'}
    response=result_body(c.request('POST',f'/{version}/visual/datainput/column/',dumps(payload).encode(),label=label,content_type='application/octet-stream'))
    if 'jobIds' in response:
        return {'status':'pending','jobIds':job_ids(response['jobIds']),'measureGuid':mid,'companions':'not-yet-registered',
                'requiredNext':'Use the selected column provisioning job contract; InfoBridge polling is not assumed interchangeable.'}
    if response.get('measureGuid')!=mid:raise ValueError('Selected response branch did not confirm the authored native identity')
    matches=[x for x in columns(client,visual_id,version=version) if x['measureGuid']==mid]
    if len(matches)!=1:raise ValueError('Created column missing/duplicated in current catalog')
    column_matches(matches[0],payload)
    return {'status':'persisted-record-readback','measureGuid':mid,'companions':'separate','execution':'not-tested'}

def register_column(client,entity_id,visual_id,payload,row_aggregation,column_aggregation,format_entries,label,visible=True):
    from .pivots import AGGREGATIONS
    if row_aggregation not in AGGREGATIONS or column_aggregation not in AGGREGATIONS:raise ValueError('Explicit per-axis aggregation required')
    if not isinstance(visible,bool) or not isinstance(format_entries,list) or not format_entries or any(not x.get('format') for x in format_entries):raise ValueError('Explicit formatting/visibility companions required')
    mid=native_id(payload['measureGuid']);records=[x for x in columns(client,visual_id) if x['measureGuid']==mid]
    if len(records)!=1:raise ValueError('Register only an actual persisted native column')
    column_matches(records[0],payload)
    before=page(client,entity_id);matches=[v for v in before['payload']['visuals'] if v['id']==visual_id and not v.get('isEmbedded')]
    if len(matches)!=1:raise ValueError('Direct owning visual required')
    v=matches[0];props=copy.deepcopy(v['properties']['properties']);state=props['visualState'];members=state['manage_measures']
    if len({x['id'] for x in members})!=len(members):raise ValueError('Duplicate measure registry')
    match=[x for x in members if x['id']==mid]
    if not match:members.append({'id':mid,'label':payload['name'],'order':max((x['order'] for x in members),default=-1)+1,'visible':visible})
    else:match[0].update(label=payload['name'],visible=visible)
    state['aggregation_config']['measure_aggregation'][mid]={'row':row_aggregation,'column':column_aggregation}
    state['formatConfig']['measure'][mid]=copy.deepcopy(format_entries)
    if payload['columnMeta'].get('data_type')=='Number':
        from .display_defaults import auto_number_formatting
        props['visualState']=auto_number_formatting(state,[mid])
    if props!=v['properties']['properties']:
        if not v['properties'].get('etag') or not before['payload'].get('etag'):raise ValueError('Current ETags required')
        b={'visuals':{visual_id:{'schema':'0.0.1','properties':props}},'workloadEntities':{},'workload':{},
           'etags':{'visuals':{visual_id:v['properties']['etag']},'workloadEntities':{str(entity_id):before['payload']['etag']}}}
        result_body(client.request('POST','/v1/workload/properties/batch/',b,label=label))
    after=page(client,entity_id);actual=next(x['properties']['properties'] for x in after['payload']['visuals'] if x['id']==visual_id)
    if actual!=props:raise ValueError('Companion readback mismatch or unrelated property drift')
    return {'registration':'persisted','calculation':'not-tested','inputSave':'not-tested'}

def create_rule(engine_client,payload,label,mount_verified=False):
    if mount_verified is not True:raise ValueError('Rule engine mount and authorization must be verified for this destination')
    if set(payload)!= {'ruleOperation'} or set(payload['ruleOperation'])!={'New'}:raise ValueError('Use the New rule constructor')
    r=result_body(engine_client.request('POST','/v1/rules',payload,label=label))
    return {'status':'submitted','response':r,'catalog':result_body(engine_client.request('GET','/v1/rules')),
            'execution':'not-tested','requiredNext':'Resolve generated persisted id separately from rule_id and verify selected rule fields.'}

def bridge_inventory(client,workload_id):return result_body(client.request('GET',f'/v2/workloaditem/{segment(workload_id)}/ib/source/'))
def bridge_query(client,query_id):
    q=segment(query_id)
    return {'metadata':result_body(client.request('GET',f'/v2/ib/query/{q}/meta/')),
            'transformations':result_body(client.request('GET',f'/v2/ib/queries/{q}/transformations/'))}
def reload_query(client,query_id,label):
    p=result_body(client.request('POST',f'/v2/ib/queries/{segment(query_id)}/reload-jobs/',label=label))
    ids=job_ids(p.get('jobIds'))
    return {'status':'queued','jobIds':ids,'queryId':query_id,'response':p}

def poll_bridge(client,workload_id,job_ids,*,event_id_fields,status_field,timestamp_field=None,query_id=None,
                target_visual_ids=(),aliases=None,max_polls=60,interval=2):
    if not isinstance(job_ids,list) or not job_ids or len(set(job_ids))!=len(job_ids) or any(not isinstance(x,str) for x in job_ids):raise ValueError('Expected unique returned job IDs')
    if not event_id_fields or not all(isinstance(x,str) and x for x in event_id_fields) or not status_field:raise ValueError('Resolved notification field mapping required')
    if not isinstance(max_polls,int) or isinstance(max_polls,bool) or not 1<=max_polls<=1800 or not 0<=interval<=30:raise ValueError('Bounded polling configuration required')
    requested=set(job_ids);mapping={x:x for x in job_ids};seen={};latest={}
    for record,execution in (aliases or {}).items():
        if record not in requested or not isinstance(execution,str) or not execution:raise ValueError('Alias must map returned record ID to actual returned execution ID')
        if execution in mapping and mapping[execution]!=record:raise ValueError('Ambiguous execution alias')
        mapping[execution]=record
    params={'feature':'infobridge','jobIds':','.join(job_ids)}
    if query_id is not None:params['queryId']=query_id
    if target_visual_ids:
        if any(not isinstance(x,str) or not x.isdecimal() for x in target_visual_ids):raise ValueError('Plain numeric target visual identities required')
        params['targetVisualIds']=','.join(target_visual_ids)
    route=f'/v2/workloaditem/{segment(workload_id)}/notifications/?'+urllib.parse.urlencode(params)
    for _ in range(max_polls):
        p=result_body(client.request('GET',route));events=p.get('events')
        if not isinstance(events,list):raise ValueError('Missing targeted notification events')
        grouped={}
        for event in events:
            ids={mapping[str(event[k])] for k in event_id_fields if k in event and str(event[k]) in mapping}
            if len(ids)>1:raise ValueError('Ambiguous job event ownership')
            if not ids:continue
            if status_field not in event:raise ValueError('Missing job status')
            key=next(iter(ids));grouped.setdefault(key,[]).append(event)
        for key,records in grouped.items():
            if len(records)>1:
                if not timestamp_field or any(timestamp_field not in e for e in records):raise ValueError('Multiple events require a verified timestamp ordering field')
                records.sort(key=lambda e:e[timestamp_field])
                if len({e[status_field] for e in records if e[timestamp_field]==records[-1][timestamp_field]})!=1:raise ValueError('Conflicting simultaneous job statuses')
            status=records[-1][status_field]
            if isinstance(status,bool) or status not in (100,210,200,211,400,499):raise ValueError('Unknown job status')
            if timestamp_field:
                stamp=records[-1].get(timestamp_field)
                if stamp is None:raise ValueError('Verified timestamp missing from job event')
                if key in latest:
                    if stamp<latest[key]:continue
                    if stamp==latest[key] and status!=seen[key]:raise ValueError('Conflicting job status at same timestamp')
                latest[key]=stamp
            elif seen.get(key)==200 and status in (100,210):
                continue  # Terminal completion cannot regress to a pending event.
            if status in (211,400,499):raise RuntimeError('Job '+key+' ended with non-success status '+str(status))
            seen[key]=status
        if all(seen.get(k)==200 for k in requested):return {'status':'all-expected-jobs-succeeded','jobs':seen,'consumerFreshness':'separate-verification'}
        if interval:client.wait(interval)
    raise TimeoutError('PENDING_JOBS: '+','.join(sorted(k for k in requested if seen.get(k)!=200)))

def source_parquet(client,source_id,skip=0,limit=None):
    if isinstance(skip,bool) or not isinstance(skip,int) or skip<0:raise ValueError('Nonnegative skip')
    if limit is not None and (isinstance(limit,bool) or not isinstance(limit,int) or limit<=0):raise ValueError('Positive limit')
    q={'skip':skip,'isCommentFile':'false'}
    if limit is not None:q['limit']=limit
    r=client.request('GET',f'/v2/ib/sources/{segment(source_id)}/stream/?'+urllib.parse.urlencode(q),accept='application/x-parquet;q=1.0')
    if r['status']==202:
        p=r['body'].get('payload',{})
        return {'status':'pending-user-output','jobIds':job_ids(p.get('jobIds')),'jobs':p.get('jobs'),
                'requiredNext':'Poll these jobs then retrieve the same scoped stream again'}
    if r['status']!=200 or not isinstance(r.get('body'),dict) or 'binaryBase64' not in r['body']:raise ValueError('Expected Parquet binary response')
    data=base64.b64decode(r['body']['binaryBase64'],validate=True)
    if len(data)<12 or data[:4]!=b'PAR1' or data[-4:]!=b'PAR1':raise ValueError('Not an unencrypted Parquet container')
    return {'status':'retrieved-binary','bytes':data,'schemaAndValues':'not-decoded-or-verified'}

def initialize_powertable(client,payload,label):
    if payload.get('creationMode')!=2:raise ValueError('Existing-table source only')
    p=result_body(client.request('POST','/v2/powertable/sources/',payload,label=label))
    if not isinstance(p.get('powerTableSource'),dict):raise ValueError('Missing returned PowerTable source object')
    return {'status':'source-created','source':p['powerTableSource'],'initializationJobs':'unverified',
            'requiredNext':'Resolve returned source/visual identities; read source details and table/schema before maintenance.'}
def powertable_schema(client,source_id):
    route='/v2/powertable/sources/'+segment(source_id)
    # These readers are independent. OneLake can return a valid physical schema
    # while its details adapter fails. Preserve each result and its exact status.
    out={'details':None,'schema':None,'readStatus':{},'errors':{}}
    for key,suffix in (('details','/details/'),('schema','/table/schema/')):
        try:
            value=result_body(client.request('GET',route+suffix))
            if key=='schema' and (not isinstance(value,list) or not value or
                any(not isinstance(c,dict) or not c.get('name') for c in value)):
                raise ValueError('Invalid physical PowerTable schema response')
            out[key]=value;out['readStatus'][key]='passed'
        except HttpError as e:
            if e.status in (401,403):raise
            out['readStatus'][key]='failed'
            out['errors'][key]={'status':e.status,'category':e.category}
    out['status']='complete' if not out['errors'] else 'partial' if any(x=='passed' for x in out['readStatus'].values()) else 'failed'
    out['writeback']='not-tested'
    return out

def read_bookmark(client,slug):
    value=result_body(client.request('GET','/v1/workload/bookmark/'+segment(slug)+'/'))
    if value.get('bookmarkSlug')!=slug or value.get('bookmarkMeta',{}).get('bookmarkSlug')!=slug:
        raise ValueError('Bookmark identity mismatch')
    if not isinstance(value.get('bookmarkVisualMeta'),dict):raise ValueError('Missing native bookmark snapshots')
    return value
def save_powertable(client,source_id,payload,label,*,version,route_shape):
    if version not in ('v3','v4') or route_shape not in ('source-qualified','context-only'):raise ValueError('Select the verified writer/validator route pair')
    if not client.context_headers.get('x-target-visual'):raise ValueError('Actual PowerTable visual context required')
    if not isinstance(payload.get('data'),str) or payload.get('actions') not in (['insert'],['update']):raise ValueError('Use the compressed row serializer')
    route=f'/{version}/powertable-source/'+(segment(source_id)+'/' if route_shape=='source-qualified' else '')+'data/save/'
    p=result_body(client.request('POST',route,dumps(payload).encode(),label=label,content_type='application/octet-stream'))
    return {'status':'submitted','response':p,'rowsSaved':'not-verified','requiredNext':'Poll the PowerTable job APIs and independently reread physical rows.'}

def upsert_bookmark(client,slug,capture,label):
    if not isinstance(capture,dict) or not {'name','bookmarkType','bookmarkMeta','bookmarkVisualMeta'}<=capture.keys():raise ValueError('Complete captured state required')
    if capture['bookmarkType']!=20 or not capture['bookmarkVisualMeta'] or capture['bookmarkMeta'].get('bookmarkSlug')!=slug:raise ValueError('Public capture/slug mismatch')
    if set(capture)-{'name','bookmarkType','bookmarkMeta','bookmarkVisualMeta','etag'}:raise ValueError('Do not send store callbacks/change sets')
    route='/v1/workload/bookmark/'+segment(slug)+'/'
    projection={k:v for k,v in capture.items() if k!='etag'}
    try:current=result_body(client.request('GET',route))
    except HttpError as e:
        if e.status!=404:raise
        current=None
    if current is not None:
        try:contains(current,projection);matched=True
        except ValueError:matched=False
        if matched:return {'status':'persisted-capture-readback','etag':current.get('etag'),'write':'already-matched','restore':'not-tested'}
        if current.get('bookmarkType')!=20 or not current.get('etag'):raise ValueError('Fresh public bookmark and ETag required for update')
        if capture.get('etag') and capture['etag']!=current['etag']:raise ValueError('Stale supplied bookmark ETag')
    if (client.journal/(label+'.intent.json')).exists():raise ValueError('Prior bookmark submission differs from current state; reconcile before a new write')
    candidate=copy.deepcopy(projection)
    if current is not None:candidate['etag']=current['etag']
    elif capture.get('etag'):raise ValueError('ETag supplied for absent bookmark')
    p=result_body(client.request('PUT','/v1/workload/bookmark/batch/',{slug:candidate},label=label))
    if not isinstance(p.get('etags'),dict) or slug not in p['etags']:raise ValueError('Missing bookmark ETag correspondence')
    saved=result_body(client.request('GET',route))
    contains(saved,projection)
    if saved.get('etag')!=p['etags'][slug]:raise ValueError('Bookmark ETag readback differs')
    return {'status':'persisted-capture-readback','etag':p['etags'][slug],'restore':'not-tested'}
