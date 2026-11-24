"""Bounded PowerTable column presentation constructors from verified SQL metadata.

Portable columnConfigs records, not row-save metadata or SQL DDL. No default
database, connection, table, lookup, access grant or existing record GUID.

Default column types follow the product's SQL-type map: text types are Text,
integer types are Number, decimal types are Decimal, ``date`` is Date, the
datetime family is Date time and ``bit`` is Checkbox. Single select (distinct
values) and database lookups are explicit opt-ins, never defaults. Every column,
including a primary key, is displayed unless the caller asks to hide it.
"""
import copy,re
from .construct import guid

# Native PowerTable column type codes (POWERTABLE_COLUMN_TYPE).
COLUMN_TYPE={'text':1,'text-options':2,'database-lookup':2,'date':4,'integer':6,'checkbox':11,'datetime':12,'decimal':13}
TEXT_TYPES=('varchar','nvarchar','char','nchar','text','ntext')
INTEGER_TYPES=('int','bigint','smallint','tinyint')
DECIMAL_TYPES=('decimal','numeric','money','smallmoney','float','real')
DATETIME_TYPES=('datetime','datetime2','smalldatetime')
COMPATIBLE={'text':set(TEXT_TYPES),'integer':{*INTEGER_TYPES,'bit'},'decimal':set(DECIMAL_TYPES),
            'date':{'date',*DATETIME_TYPES},'datetime':set(DATETIME_TYPES),'checkbox':{'bit'},
            'database-lookup':{*INTEGER_TYPES,'varchar','nvarchar','char','nchar'},
            'text-options':{'varchar','nvarchar','char','nchar'}}
DEFAULT_KIND={**{t:'text' for t in TEXT_TYPES},**{t:'integer' for t in INTEGER_TYPES},
              **{t:'decimal' for t in DECIMAL_TYPES},'date':'date',
              **{t:'datetime' for t in DATETIME_TYPES},'bit':'checkbox'}
TIME_ZONES=('timezone-independent','user-local')

def sql_base_type(value):
    """Lower-case SQL type without its size, e.g. ``NVARCHAR(MAX)`` -> ``nvarchar``."""
    if not isinstance(value,str) or not value.strip():raise ValueError('SQL type name required')
    return re.sub(r'\s*\(.*\)\s*$','',value.strip().lower())

def default_kind(sql_type):
    """Column kind the product assigns to a physical SQL type when a table is added."""
    base=sql_base_type(sql_type)
    if base not in DEFAULT_KIND:
        raise ValueError('No PowerTable default for SQL type '+base+'; choose a compatible kind explicitly')
    return DEFAULT_KIND[base]

def column_config(column, kind=None, *, lookup=None, lookup_catalog=None, decimals=2, allow_negative=True,
                  allow_edit=None, hide=False, time_zone=None, generated=False):
    """One columnConfigs record. ``kind=None`` uses the product default for the SQL type."""
    name=column['name'];db=copy.deepcopy(column['dbMeta'])
    required={'type','isIdentity','isNullable','isPrimaryKey','isUnique','isCompositeUnique'}
    if not isinstance(name,str) or not name or not required<=db.keys(): raise ValueError('Complete physical SQL metadata required')
    if any(not isinstance(db[k],bool) for k in required-{'type'}): raise ValueError('SQL metadata Boolean required')
    sqltype=sql_base_type(db['type']);identity=db['isIdentity'];pk=db['isPrimaryKey']
    if kind is None:kind=default_kind(sqltype)
    if kind not in COLUMN_TYPE: raise ValueError('Unimplemented column kind')
    for flag,label in ((hide,'hide'),(generated,'generated')):
        if not isinstance(flag,bool):raise ValueError(label+' must be Boolean')
    if allow_edit is not None and not isinstance(allow_edit,bool):raise ValueError('allow_edit must be Boolean')
    if identity and allow_edit is True:raise ValueError('Database identity columns must remain read-only')
    if generated and allow_edit is True:raise ValueError('Computed columns must remain read-only')
    if sqltype not in COMPATIBLE[kind]: raise ValueError('SQL type incompatible with selected presentation kind')
    if kind!='database-lookup' and (lookup is not None or lookup_catalog is not None): raise ValueError('Lookup supplied to nonlookup column')
    if kind!='datetime' and time_zone is not None:raise ValueError('time_zone applies only to Date time columns')
    readonly=identity or generated
    meta={'dbMeta':db,'defaultValue':'','defaultValueType':'NONE','isPrimaryKey':pk,
          'resetToDefaultOnRowModify':False,'updateValueOnRowModify':False}
    result={'allowEdit':0 if readonly or allow_edit is False else 1,'columnGuid':name,'columnName':name,
            'columnType':COLUMN_TYPE[kind],
            'visualColumnType':3 if kind in ('database-lookup','text-options') else 1,'description':'','displayName':name,
            'hideColumn':1 if hide else 0,'mandatory':0 if readonly or db['isNullable'] else 1,
            'recordGuid':guid(),'columnMeta':meta}
    if kind=='text':meta.update(maximumAllowedLength='',textFieldColumnType='Any Value')
    elif kind in ('integer','decimal'):
        if not isinstance(allow_negative,bool): raise ValueError('allow_negative must be Boolean')
        meta.update(allowNegative=allow_negative,largeNumberAbbrevation='',max='',min='',negativeValueFormat='-0',prefix='',suffix='',thousandSeparator='')
        if kind=='decimal':
            if isinstance(decimals,bool) or not isinstance(decimals,int) or not 0<=decimals<=15: raise ValueError('Invalid decimals')
            meta['noOfDecimals']=decimals
    elif kind=='date':meta.update(format='DEFAULT_LOCALE',min='',max='')
    elif kind=='datetime':
        zone='timezone-independent' if time_zone is None else time_zone
        if zone not in TIME_ZONES:raise ValueError('time_zone must be timezone-independent or user-local')
        meta.update(format='DEFAULT_LOCALE',min='',max='',timeZone=zone)
    elif kind=='checkbox':meta.update(checkedValue='1',unCheckedValue='0',checkboxFormatType='Checkbox')
    elif kind=='text-options':
        meta.update(allowAddingNewOptions=True,fcVisualIdColumnName=None,fcVisualLabelColumnName=None,
                    fcVisualName=None,isFilterBasedOnAnotherValue=False,optionLinking={},options=[],selectionMethod='DISTINCT_VALUES')
    else:
        if readonly or not isinstance(lookup,dict) or not isinstance(lookup_catalog,list): raise ValueError('Lookup specification and current SQL catalog required')
        if not {'schema','table','key','label'}<=lookup.keys() or set(lookup)-{'schema','table','key','label','chain'}:
            raise ValueError('Explicit lookup schema/table/key/label required; optional chain only')
        chain=lookup.get('chain',[])
        if not isinstance(chain,list):raise ValueError('Lookup chain must be an ordered list')
        hops=[{k:v for k,v in lookup.items() if k!='chain'},*chain]
        records=[];previous=None
        for order,hop in enumerate(hops):
            required={'schema','table','key','label'}|({'column'} if order else set())
            if not isinstance(hop,dict) or set(hop)!=required or any(not isinstance(hop[k],str) or not hop[k].strip() for k in required):
                raise ValueError('Incomplete lookup hop')
            local_name=name if order==0 else hop['column']
            if order and local_name not in previous:raise ValueError('Chained key absent from preceding lookup table')
            local_type=sqltype if order==0 else sql_base_type(previous[local_name]['type'])
            tables=[t for t in lookup_catalog if t['schema']==hop['schema'] and t['table']==hop['table']]
            if len(tables)!=1: raise ValueError('Missing/ambiguous lookup table')
            columns=tables[0]['columns'];names=[c['name'] for c in columns]
            if len(names)!=len(set(names)): raise ValueError('Ambiguous lookup column')
            by_name={c['name']:c for c in columns}
            if hop['key'] not in by_name or hop['label'] not in by_name: raise ValueError('Lookup key/label absent from SQL metadata')
            key=by_name[hop['key']]
            if sql_base_type(key['type'])!=local_type or not (key.get('isPrimaryKey') is True or key.get('isUnique') is True):
                raise ValueError('Lookup requires compatible unique remote key')
            records.append({'id':local_name,'label':hop['label'],'linkingColumn':hop['key'],
                            'order':order,'schema':hop['schema'],'table':hop['table']})
            previous=by_name
        result['displayName']=lookup['label']
        meta.update(optionLinking={'lookupConfig':records},options=[],selectionMethod='LOAD_FROM_DATABASE',
                    allowAddingNewOptions=False,isFilterBasedOnAnotherValue=False)
    return result

OVERRIDES={'kind','lookup','decimals','allow_negative','allow_edit','hide','time_zone','display_name','description'}

def table_column_configs(table, overrides=None, *, lookup_catalog=None):
    """Product-default columnConfigs for every physical column, in physical order.

    ``overrides`` maps a physical column name to explicit choices such as
    ``{"kind": "text-options"}``, ``{"kind": "database-lookup", "lookup": {...}}``,
    ``{"hide": true}`` or ``{"display_name": "Start date"}``. Unlisted columns get
    the product defaults. Computed columns (``generated``) stay read-only.
    """
    overrides={} if overrides is None else overrides
    if not isinstance(overrides,dict) or any(not isinstance(v,dict) for v in overrides.values()):
        raise ValueError('Column overrides must map physical column names to objects')
    physical=table.get('columns') if isinstance(table,dict) else None
    if not isinstance(physical,list) or not physical or any(not isinstance(c,dict) or not isinstance(c.get('dbMeta'),dict) for c in physical):
        raise ValueError('Physical column metadata required; columns must carry dbMeta')
    names=[c.get('name') for c in physical]
    if len(set(names))!=len(names):raise ValueError('Duplicate physical column name')
    unknown=set(overrides)-set(names)
    if unknown:raise ValueError('Override for unknown column: '+', '.join(sorted(map(str,unknown))))
    result=[]
    for c in physical:
        choice=dict(overrides.get(c['name'],{}))
        extra=set(choice)-OVERRIDES
        if extra:raise ValueError('Unsupported column override: '+', '.join(sorted(extra)))
        display=choice.pop('display_name',None);description=choice.pop('description',None)
        if 'lookup' in choice:choice['lookup_catalog']=lookup_catalog
        config=column_config({'name':c['name'],'dbMeta':c['dbMeta']},choice.pop('kind',None),
                             generated=c.get('generated') is True,**choice)
        for key,value in (('displayName',display),('description',description)):
            if value is not None:
                if not isinstance(value,str) or (key=='displayName' and not value.strip()):raise ValueError('Invalid '+key)
                config[key]=value.strip() if key=='displayName' else value
        result.append(config)
    return result

def apply_lookup(column,lookup,lookup_catalog):
    """Change lookup presentation only; preserve IDs, locks, dbMeta and row values."""
    generated=column_config({'name':column['columnName'],'dbMeta':column['columnMeta']['dbMeta']},
                            'database-lookup',lookup=lookup,lookup_catalog=lookup_catalog)
    result=copy.deepcopy(column)
    for key in ('columnType','visualColumnType','displayName'):result[key]=generated[key]
    for key in ('optionLinking','options','selectionMethod','allowAddingNewOptions','isFilterBasedOnAnotherValue'):
        result['columnMeta'][key]=copy.deepcopy(generated['columnMeta'][key])
    return result
