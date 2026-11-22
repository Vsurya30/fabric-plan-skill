"""Workload-scoped Home multipart upload on an explicitly selected app base."""
from pathlib import Path
import hashlib,urllib.parse,base64
from .session import result_body

def multipart_image(path,workload_id):
    path=Path(path);data=path.read_bytes();name=path.name
    if not data or len(data)>5*1024*1024:raise ValueError('Home image must be nonempty and at most 5 MiB')
    if any(x in name for x in ('\r','\n','"')):raise ValueError('Unsafe multipart filename')
    ext=path.suffix.lower();types={'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.svg':'image/svg+xml'}
    if ext not in types:raise ValueError('Home accepts PNG/JPEG/SVG')
    if ext=='.png' and not data.startswith(b'\x89PNG\r\n\x1a\n'):raise ValueError('PNG signature')
    if ext in ('.jpg','.jpeg') and not data.startswith(b'\xff\xd8'):raise ValueError('JPEG signature')
    if ext=='.svg':
        import xml.etree.ElementTree as ET
        if b'<!DOCTYPE' in data.upper() or b'<!ENTITY' in data.upper():raise ValueError('External SVG document declarations not accepted')
        if ET.fromstring(data).tag.split('}')[-1]!='svg':raise ValueError('SVG root required')
    if not isinstance(workload_id,str) or any(c in workload_id for c in ('\r','\n')):raise ValueError('Workload identity')
    # Stable boundary makes retries reproduce the identical request-body hash.
    boundary='fabric-plan-'+hashlib.sha256(data+name.encode()+workload_id.encode()).hexdigest()[:40]
    if boundary.encode() in data:raise ValueError('Multipart boundary collision')
    chunks=[]
    for key,value in (('workloadId',workload_id),('feature','home-layout')):
        chunks.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n{value}\r\n'.encode())
    filename=urllib.parse.quote(name,safe='')
    chunks.append(f'--{boundary}\r\nContent-Disposition: form-data; name="file"; filename="{filename}"; filename*=UTF-8\'\'{filename}\r\nContent-Type: {types[ext]}\r\n\r\n'.encode())
    chunks+=[data,f'\r\n--{boundary}--\r\n'.encode()]
    return b''.join(chunks),'multipart/form-data; boundary='+boundary,types[ext],len(data)

def upload_home_image(client,path,workload_id,label):
    if client.auth_scheme!='MWCToken' or client.context_headers.get('x-ms-workload-resource-moniker')!=workload_id:
        raise ValueError('Workload-scoped application authentication required')
    body,typ,mime,size=multipart_image(path,workload_id)
    p=result_body(client.request('POST','/api/assets',body,label=label,content_type=typ))
    if not isinstance(p.get('fileId'),str) or not p['fileId']:raise ValueError('Upload returned no fileId')
    if p.get('workloadId')!=workload_id or p.get('feature')!='home-layout' or p.get('mimeType')!=mime or p.get('fileSize')!=size:
        raise ValueError('Upload scope/type/size readback mismatch')
    meta=result_body(client.request('GET','/api/assets/'+urllib.parse.quote(p['fileId'],safe='')))
    expected={'fileId':p['fileId'],'workloadId':workload_id,'feature':'home-layout','mimeType':mime,'fileSize':size}
    if any(meta.get(k)!=v for k,v in expected.items()):raise ValueError('Asset metadata readback mismatch')
    return {'fileId':p['fileId'],'imageConfig':{'source':p['fileId'],'sizingMode':'fit'},'metadata':'verified','layoutSaved':False,'rendered':'not-tested'}

def asset_content(client,file_id):
    r=client.request('GET','/api/assets/'+urllib.parse.quote(file_id,safe='')+'/content',accept='image/*')
    if r['status'] not in (200,206) or not isinstance(r.get('body'),dict) or 'binaryBase64' not in r['body']:raise ValueError('Expected binary asset content')
    return base64.b64decode(r['body']['binaryBase64'],validate=True),r['headers'].get('content-range')
