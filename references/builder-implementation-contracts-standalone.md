> v30: [Measure-weighted distribution](measure-weighted-distribution.md) is now constructible for the captured Column / All dimensions / another Measure / source Row Use Self profile. Discover RULES or weights from another measure; use `construct-native weighted-rule`. Saved configuration is confirmed, not allocation execution. Other reference profiles and bookmark restore remain separate gaps. All prior fixes remain.

> 2026-11-14 numeric-input correction: [numeric-input-constraints.md](numeric-input-constraints.md) is authoritative for whole-number static min/max bounds and AverageLeaf parent distribution. Decimal defaults/formulas are separate; preserve existing percentage units and IDs.

> Standalone edition: read [runtime-guide.md](runtime-guide.md) for construction and deployment. Source checkout and historical task links below are optional provenance, not runtime prerequisites. Original feature explanations are preserved; the API-only runtime guide and gap inventory distinguish implemented APIs from blocked contracts. Historical UI steps are not execution instructions.

# Source-Derived Contracts for an End-to-End Planning Builder

## 1. What this document adds

This document turns the previously listed gaps into concrete construction and execution contracts extracted from the planning frontend, native calculation engine, backend APIs, ALM import logic and InfoBridge worker.

It covers:

- Typed input and formula factories.
- Allocation and validation rules.
- InfoBridge execution, polling and output retrieval.
- Existing-table PowerTable initialization and maintenance transport.
- Bookmark construction, portable conversion and restoration.
- Navigator state and visual construction.
- Home image upload, retrieval and layout persistence.

It is self-contained: the field names, operation paths and examples are included here rather than delegated to source-file references.

**Evidence level:** implementation inspection, not a live deployment test. These contracts materially reduce the documentation gaps, but they do not prove that a complete builder has been implemented or that every operation works in the destination environment. Unknowns and version conflicts are identified rather than filled with invented defaults.

Examples with descriptive identifiers must be populated with actual destination identities. Native measure, dimension and rule IDs require lossless unsigned decimal strings, not descriptive labels.

## 2. Transport, identity and compatibility rules

### 2.1 Separate API surfaces

The application backend routes in this document are not public Fabric item REST endpoints.

Use approved application authentication and destination context. Resolve the actual backend host from trusted environment configuration. Do not append application routes to the public Fabric base URL.

The native calculation engine also exposes a `CoreAPI/` route family. This is an engine request surface; do not assume every such route is directly mounted by the application backend.

### 2.2 Standard application response

Many backend handlers return this logical envelope:

```json
{
  "statusCode": 200,
  "message": "Operation-specific message",
  "payload": {},
  "limit": 0
}
```

`payload` and `limit` above are illustrative. The real payload is operation-specific, and the real limit comes from backend configuration. Some operations return raw binary content or explicit HTTP 202 responses instead.

Inspect both the HTTP status and the operation body. HTTP 200 for an enqueue operation is not job completion.

### 2.3 Identity domains

Keep these identities separate:

| Identity | Construction rule |
| --- | --- |
| Fabric item/workspace IDs | Resolve from destination metadata. |
| Portable sheet/visual/source GUIDs | Allocate once and persist in an identity registry. |
| Native calculated-measure IDs | Generate unsigned 64-bit values and serialize as canonical decimal strings. |
| Semantic-source measure IDs | Resolve from the exact canonical assignment key using the selected native resolver. |
| Query/source/job identifiers | Preserve the identifiers returned by the selected API branch. |
| Bookmark slugs | Treat separately from bookmark record GUIDs and native visual IDs. |
| Home asset IDs | Use the actual upload response; never manufacture them from paths. |

For the inspected native semantic resolver:

- A DAX measure uses its exact assignment ID without an aggregation prefix.
- A normal column with aggregation uses the upper-case aggregation name, two underscores and the exact assignment ID.
- The processed key is hashed with unsigned XXH3-64 and serialized as a decimal string.
- Do not apply this resolver blindly to From Sheets, InfoBridge or custom-source fields.

Native formula measure references use `M_` followed by the resolved native decimal ID. Hashing a display label or using a portable GUID in that token is not a valid substitute.

### 2.4 Version-sensitive filter-context encoding

There are distinct contracts:

| Layer | Encoding |
| --- | --- |
| Inner native input/forecast configuration | Boolean `bound_to_filter_context`; default true in the inspected native type. |
| Native calculated-column create payload | `boundToFilterContext: 10` for active; `20` for disabled. |
| Inspected older backend column validation | Legacy 0/1 convention. |

Choose the encoding for the actual writer/validator pair. Do not normalize every branch to one number. Verify save/reopen isolation between planning versions separately from this metadata flag.

## 3. Typed input factories

### 3.1 Complete native measure record

A calculated measure consists of:

| Field | Type and purpose |
| --- | --- |
| `id` | Native unsigned decimal ID string. |
| `label` | Display caption, not the persistence key. |
| `measure_type` | Exactly one supported externally tagged measure kind. |
| `data_type` | Native `Text`, `Number`, `Boolean` or `DateTime`. |
| `description` | Optional explanatory text. |

Supported measure kinds include `Native`, `Formula`, `DataInput`, `Forecast`, `VisualColumn` and `AutoVariance`. This guide specifies input/formula branches; listing another kind is not a complete factory for it.

A normal input is wrapped under `DataInput`. An applicable visual-column input uses a separate nested wrapper:

```json
{
  "VisualColumn": {
    "DataInput": {
      "id": "123",
      "title": "Input caption",
      "column_type": {
        "Person": {
          "allow_entry_on_totals_or_subtotals": false
        }
      },
      "allow_input": "ReadAndEdit",
      "bound_to_filter_context": true
    }
  }
}
```

Do not use the visual-column branch merely to hide an input or replace an ordinary measure. Placement and input type are separate choices.

### 3.2 Common DataInput configuration

| Field | Native contract |
| --- | --- |
| `id` | String identity carried by the input configuration. Preserve the selected factory's relationship to the outer measure ID. |
| `column_type` | One of the tagged type configurations below. |
| `title` | Input title. |
| `allow_input` | `"Edit"`, `"ReadAndEdit"` or `{"BasedOnFormula":"expression"}`. |
| `on_change_formula` | Optional expression. |
| `bound_to_filter_context` | Boolean, default true. |
| `cube_partition_measure_id` | Optional cube identity; only for an actually provisioned cube-backed branch. |
| `cube_model` | Optional saved DataInput/Forecast marker. Preserve `"DYNAMIC"` from the current dynamic-Cube response/request contract; Formula has no corresponding member. |
| `disable_write_access` | Native runtime-managed field; not a replacement for server-side authorization. |
| `user_permission` | Native runtime permission state; do not invent it as an unrestricted creation field. |

Use an explicit edit predicate for open-version/month restrictions. Keep that predicate separate from the rule determining whether retained planned values are displayed.

### 3.3 Number

```json
{
  "Number": {
    "min_value": {"Static": 0},
    "max_value": {"Static": 100},
    "distribute_parent_value_to_children": false,
    "default_value": {"Static": 5}
  }
}
```

`min_value`, `max_value` and `default_value` are nullable tagged settings:

- `{"Static": number}`
- `{"Measure": "native-decimal-id"}`

They are not bare scalar values. Use finite numbers and check default-versus-bound consistency.

The example is a 0-100 percentage-point field. Do not assume all rates use that unit; confirm the source and formulas. A percentage-point rate is divided by 100 in arithmetic.

### 3.4 ShortText and LongText

Both use:

| Field | Type |
| --- | --- |
| `default_value` | Optional `Static(string)`, `Dimension(native ID)` or `Measure(native ID)`. |
| `allow_entry_on_totals_or_subtotals` | Boolean. |
| `prevent_null` | Optional boolean. |
| `field_validation` | Validation union below. |
| `minimum_length`, `maximum_length` | Optional unsigned integers. |
| `roll_up_delimiter` | Optional comma or pipe, serialized as `","` or `"|"`. |

Validation values:

`AnyValue`, `Numeric`, `NonNumeric`, `AlphaNumeric`, `Email`, `Url`, or `{"Custom":"expression"}`.

The inspected default maximum lengths are 255 for ShortText and 25,000 for LongText. Enforce the appropriate type's limits instead of assigning one universal text limit.

### 3.5 SingleSelect and MultiSelect

Both use the same native metadata structure:

| Field | Type |
| --- | --- |
| `options` | Legacy option array; preserve/migrate through the actual factory. |
| `options_source` | `{"Static":[options]}` or unit string `"Lookup"`. |
| `option_style` | `Chip`, `Arrow` or `PlainText`. |
| `advanced` | Optional object with string/null `visual_identifier` and `columns`. The bundled select factory now validates and preserves it. |
| `default_value` | Optional `Static(option)`, `Dimension(native ID)` or `Measure(native ID)`. |
| `allow_user_to_add_new_option` | Boolean. |
| `allow_entry_on_totals_or_subtotals` | Boolean. |
| `prevent_null` | Optional boolean. |
| `icon_position` | Optional string. |

An option has the following fields:

```json
{
  "display_name": "Open",
  "value": "open",
  "color": "",
  "icon": "",
  "order": 0
}
```

Do not emit `options_source: {}` or a scalar string as a static option default. The default's `Static` variant holds an option object, including for the inspected MultiSelect metadata type.

Selecting `"Lookup"` does not configure the lookup source. That source and its matching/key behavior require their own supported configuration.

### 3.6 Date

| Field | Type |
| --- | --- |
| `format` | Native date-format enum. |
| `min_date`, `max_date` | Optional date strings. |
| `allow_entry_on_totals_or_subtotals` | Boolean. |
| `default_value` | Optional `Static(string)`, `Dimension(string)` or `Measure(native ID)`. |

Use `"DEFAULT_LOCALE"` for the inspected default native date-format branch, not the frontend spelling `"DefaultLocale"`.

Other inspected literals include `MONTH_DD_YYYY`, `DD_MONTH_YYYY`, `DD_FULLMONTH_YYYY`, `DD_MM_YYYY_SLASH`, `DD_MM_YYYY_HYPHEN`, `DD_MM_YY_SLASH`, `DD_MM_YY_HYPHEN`, `MM_DD_YYYY_SLASH`, `MM_DD_YYYY_HYPHEN`, `MM_DD_YY_SLASH`, `MM_DD_YY_HYPHEN` and `DDDD_MMMM_D_YYYY`.

Date strings and display formats are separate from numeric epoch values. Confirm parsing/timezone behavior before using a date field for employment or validity boundaries.

### 3.7 Person

```json
{
  "Person": {
    "allow_entry_on_totals_or_subtotals": false
  }
}
```

The inspected native Person metadata does not define a default-value field. Do not add a guessed person default or option list.

### 3.8 Checkbox

```json
{
  "Checkbox": {
    "default_value": {"Static": false},
    "edit_on_total": false
  }
}
```

The default also supports `Dimension(native ID)` and `Measure(native ID)`. `edit_on_total` is optional. Totals behavior must follow the business meaning, not a universal true default.

### 3.9 Simulation

Required native fields:

- `source_measure_id`: native ID.
- `simulation_slider`: boolean.
- `simulation_range`: signed integer.
- `distribute_parent_value_to_children`: boolean.
- `simulation_value_align`: string.
- `variance_formatting_style`: string.

The inspected frontend factory uses a visible slider, a fallback range of 100 and right alignment. The native type leaves the alignment and variance style as strings; it does not establish a closed enum. Do not invent valid style values from the field name.

### 3.10 Formula

```json
{
  "Formula": {
    "formula": "M_123 * 2"
  }
}
```

An applicable visual-column formula uses `{"VisualColumn":{"Formula":{...}}}`.

Formula configuration has an optional `cube_partition_measure_id`, but it must reference an actually created cube measure. Ordinary formulas do not need an input column-type configuration.

Check formula dependencies, cycles, owner scope, aggregation and missing-value behavior independently of JSON validity.

### 3.11 Forecast

Forecast is not an alias for an ordinary input. Its native configuration separates:

- `forecast_version`: number.
- `forecast_period`: start/end strings and optional unsigned `start_utc`/`end_utc`.
- `closed_period_till`: optional string.
- `open_period_config` and `closed_period_config`: optional method configurations.
- `edit_config`: optional edit/number metadata.
- `forecast_value_display`: optional display union.
- `auto_close_forecast_settings`: optional rollover configuration.
- Permission, runtime write restriction, `cube_partition_measure_id`,
  dynamic-Cube `cube_model:"DYNAMIC"` and filter-context settings.

A period configuration contains `method`, whose variants are:

- `{"Formula":"expression"}`
- `{"DataInput": default-value-type}`
- `{"LinkToMeasure":"native-decimal-id"}`

The forecast DataInput default-value type supports:

- `{"Formula":"expression"}`
- `{"Measure":"native-decimal-id"}`
- `{"StaticValue": number}`
- `"Blank"`
- `{"Row":"row-reference"}`

Display supports `"Actual"` or `{"Forecast":{"forecast_value_retain_blanks":boolean}}`.

Automatic range extension includes native `Extended` and `None` variants. This does not specify every rollover configuration field; automatic rollover remains a separately bounded factory.

For closed-version retention, disabling edits must not switch retained planned figures to actuals merely because the version status changed.

### 3.12 Outer column create transport

The native create request sends JSON bytes with `Content-Type: application/octet-stream`:

| Field | Purpose |
| --- | --- |
| `measureGuid` | Native calculated-measure ID. |
| `columnType` | Backend type code. |
| `name` | Label. |
| `columnMeta` | Complete native measure record. |
| `boundToFilterContext` | Version-appropriate encoding; applicable to input/forecast branches. |
| `multiDimensionSettings` | Current Cube request with `referenceMeasures`, `newPartitions`, `existingPartitions`, optional native mappings, and `cubeModel:"DYNAMIC"` for the redesigned path; dimensions can carry same-table `lookups`. It is not a generic dimension list. |
| `userPermission` | Only when required by the actual selected create/batch contract. |

Type codes observed: text 1, SingleSelect 2, MultiSelect 3, DateTime 4, Number 6, Person 7, Checkbox 11, Simulation 25 and LongText 101. Approval is a separate backend type; no complete native Approval factory was established in this scan.

The saved `cube_model:"DYNAMIC"` field is implemented in the current Rust
DataInput and Forecast contracts, but the checked-in generated client schema does
not yet list it. The native octet-stream create/readback contract must therefore
be checked at the Rust/actual-response boundary, not by treating that stale
generated interface as a closed rejection list.

The native request selects:

- `CoreAPI/v1/visual/datainput/column/`
- `CoreAPI/v2/visual/datainput/column/` when the OneLake API setting is enabled.

It adds `enableCubePolling=true` when multidimensional provisioning settings are supplied.

The application backend also exposes legacy create/update/batch column routes. Do not infer a direct backend V2 route solely from the native client's V2 constant.

The native response model accepts either:

- `payload.measureGuid` with optional `columnMeta`.
- `payload.jobIds` for asynchronous creation.

An older frontend workflow consumes `payload.id`. These responses belong to different adapters; do not interchange them.

### 3.13 Companion records

A usable column requires more than the input configuration:

- Owner and persisted registration.
- Order and visibility.
- Row and column aggregation.
- Number/date/text formatting.
- Input context and applicable rules.
- Supported defaults/lookups and their dependency references.
- Saved readback and execution evidence.

Rates and prices may require AverageLeaf; additive monetary amounts and quantities usually require summation. Derived margins should be calculated from aggregate numerator and denominator. Choose each axis explicitly rather than copying one setting to every measure.

## 4. Allocation and validation-rule factories

### 4.1 Rule transport

Native rule routes:

| Method | Engine route |
| --- | --- |
| POST | `CoreAPI/v1/rules` |
| GET | `CoreAPI/v1/rules` |
| PUT | `CoreAPI/v1/rules/{id}` |
| DELETE | `CoreAPI/v1/rules/{id}` |

The outer request uses camel-case `ruleOperation`; nested builder fields use snake_case.

```json
{
  "ruleOperation": {
    "New": {
      "rule_id": "123",
      "name": "Distribute monthly amount equally",
      "rule_type": {
        "Distribute": {
          "operation": {
            "Row": {
              "apply_to_dimensions": "All",
              "reference": "Equal"
            }
          }
        }
      },
      "columns": "All",
      "rows": "All",
      "measures": {"SelectedMeasures": ["456"]},
      "is_disabled": false
    }
  }
}
```

This is the explicit logical create shape, not evidence of a successful rule execution. The native create operation generates the persisted `id`; the caller supplies logical `rule_id`. Audit/user metadata follows the native builder's defaults and authenticated context.

Create operations include `New` and `Duplicate`. Update operations include `Update` and `Reorder`.

Do not blindly send these engine requests to a public Fabric endpoint. Rule-specific backend mounting and authorization were not established by this scan.

### 4.2 Scope selectors

| Scope | Supported native union |
| --- | --- |
| Columns | `All`, `PeriodRange(range)` or `Selected(native IDs)`. |
| Rows | `All`, `Selected(native IDs)` or `Dimension(native ID)`. |
| Measures | `AllMeasures`, `SelectedMeasures(native IDs)`, `AllVisualColumns` or `SelectedVisualColumns(native IDs)`. |

Payload-bearing enum variants are objects, not bare enum strings.

### 4.3 Rule kinds

- `Lock` with `all_children`.
- `Distribute` with a Row or Column operation.
- `MinMax` with separate minimum and maximum configurations.

The number input's parent-to-child distribution toggle is separate from a weighted distribution rule. One does not automatically create the other.

### 4.4 Distribution references

Supported references:

- `Equal`
- `SelfWeight`
- `MeasureIdWithReference(configuration)`
- `ManualInput` with a map from native IDs to numeric weights.

Example manual row weights:

```json
{
  "Distribute": {
    "operation": {
      "Row": {
        "apply_to_dimensions": {"SelectedDimensions": ["789"]},
        "reference": {
          "ManualInput": {
            "weights": {
              "1001": 0.6,
              "1002": 0.4
            }
          }
        }
      }
    }
  }
}
```

A row measure reference chooses `SelfMeasure` or `Measure(native ID)`, a period/column weight source, and optional `Average` or `ApplyAsRange` range operation.

A column measure reference chooses a measure and optional source row/period.

These unions do not define a generic `driver` field or `excluded_dimensions` property. Use the actual dimension applicability selection; do not invent parallel exclusions.

### 4.5 Min/max rules

Each bound supports:

- `Static`: optional numeric `value` and optional `is_exclusive`.
- `Measure`: native `measure` and optional `is_exclusive`.
- `Variable`: numeric `value`, variable string and optional `is_exclusive`.

Column metadata bounds and rule-level bounds are separate contracts.

### 4.6 Required behavioral checks

Verify parent/child conservation, rounding, zero/missing/negative weights, locked descendants, rule scope, alternate pivots and both axes. A serialized weight map does not demonstrate correct allocation.

## 5. InfoBridge execution and freshness

### 5.1 GUID-addressed application routes

| Method | Relative route | Meaning |
| --- | --- | --- |
| GET | `/v2/workloaditem/{workloadId}/ib/source/` | Source/query inventory. |
| GET | `/v2/ib/query/{queryGUID}/meta/` | Query metadata. |
| GET | `/v2/ib/queries/{queryGUID}/transformations/` | Ordered transformation records. |
| POST | `/v2/ib/queries/{queryGUID}/reload-jobs/` | Enqueue a query reload. |
| POST | `/v2/ib/sources/{sourceGUID}/reload-jobs/` | Reload source or linked source leaves. |
| GET | `/v2/workloaditem/{workloadId}/notifications/` | Targeted job polling. |
| GET | `/v2/workloaditem/{workloadId}/ib/jobs/logs/` | Paginated job list/history. |
| GET | `/v2/workloaditem/{workloadId}/ib/jobs/{jobGUID}/logs/` | One job's logs. |
| PATCH | `/v2/ib/query/job/{jobGUID}/cancel/` | Cancel a queued job. |
| GET | `/v2/ib/sources/{sourceGUID}/stream/` | Retrieve source Parquet data. |

### 5.2 Query reload

Query reload requires the query GUID and accepts no extra query parameters in the inspected validator. No application input payload is required by that validator.

The service:

1. Resolves query/source scope.
2. Rejects a missing query.
3. Rejects a query already queued or running.
4. Writes queued status using the current repository version.
5. Creates a LOAD_SOURCE job and dispatches the transformation worker.
6. Returns `payload.jobIds`.

```json
{
  "statusCode": 200,
  "payload": {
    "jobIds": ["returned-job-record-identifier"]
  }
}
```

The returned ID can be a numeric string or GUID depending on the storage/feature branch. The worker's execution `jobId` is a different identity; preserve both when returned.

### 5.3 Source reload and payload discrepancy

Source reload uses `application/octet-stream`. File sources can reparse a file reference, with optional base64 `sheet` selection. Non-file sources ignore file-specific metadata.

The service supports absent file-reparse data, but the inspected route validator requires a binary payload. Do not document a universally bodyless request. Select a caller-compatible binary body and verify it against the deployed validator.

Composite append/merge/join/SQL sources resolve linked leaf sources recursively. Source reload is not a guarantee that every consuming visual is refreshed.

### 5.4 Worker dispatch

Dispatch is mutually exclusive:

| Operation/source | Worker path |
| --- | --- |
| Editable base data | PowerTable integration. |
| Non-editable base data | InfoBridge preprocessing. |
| Query reload/transformation | InfoBridge transformation. |

The transformation worker loads materialized source data, applies ordered rules, generates Parquet output, publishes query metadata/file path and completes the job.

It marks the query running before replacing output, then marks the published query successful. Failures update job/query failure state and notify linked consumers.

The dependent blend cascade is conditional on measure-update context and feature settings. Ordinary query reload does not justify a claim that all dependent visuals are current. Verify the whole required graph explicitly.

### 5.5 Targeted polling

Use:

`GET /v2/workloaditem/{workloadId}/notifications/?feature=infobridge&jobIds=...`

Parameters:

- `feature=infobridge`: required for this polling branch.
- `jobIds`: nonempty comma-separated returned IDs.
- `queryId`: optional owning query GUID for a direct job-partition lookup.
- `targetVisualIds`: optional plain comma-separated numeric visual IDs, not base64.

The notification service matches both job record IDs and worker execution IDs. It returns `payload.events`, with event fields including timestamp, status, execution job ID, error message and numeric visual identity where resolvable.

An empty events array is not success; it may mean unresolved jobs. Apply a bounded deadline and preserve the outstanding IDs.

Job statuses:

| Number | Meaning |
| --- | --- |
| 100 | Queued |
| 210 | Running |
| 200 | Success |
| 211 | Partial success |
| 400 | Failed |
| 499 | Cancelled |

These are job statuses, not HTTP codes. Do not accept 211 as complete execution.

Job-list polling alone is insufficient: the job-list service hides records without `startTime`. Prefer targeted notifications for newly queued jobs.

### 5.6 Output retrieval

The stream route accepts:

- `skip`: nonnegative integer.
- `limit`: positive integer or null; omitted/null means the full source.
- `isCommentFile`: boolean, default false.

Request Parquet using `Accept: application/x-parquet;q=1.0`.

An RLS-aware request can return HTTP 202 with `payload.jobIds` and `payload.jobs` while per-user output is built. Poll those jobs, then request the stream again. Do not parse that JSON body as Parquet.

Use the scoped stream service rather than reconstructing blob paths. Preserve user-RLS and source-isolation behavior.

### 5.7 Financial acceptance

After all required jobs complete, verify:

- Output schema and stable keys.
- Common month, region, version and currency context.
- No duplicate contribution rows.
- Saved salary increases flow to compensation and reduce EBITDA/operating income by the same USD cost.
- Saved sales quantities feed both revenue and product costs.
- Margins derive from aggregate financial amounts.

Query metadata and transformation inventory checks remain separate from these execution checks.

## 6. PowerTable initialization

### 6.1 Bind an existing table

Use the existing-source route, not the new-database-table provisioning route:

`POST /v2/powertable/sources/`

```json
{
  "tableName": "PlanningEmployees",
  "schema": "dbo",
  "dbName": "DestinationDatabase",
  "dbHost": "verified-sql-host",
  "connectionId": "approved-connection-id",
  "creationMode": 2,
  "sqlTargetArtifact": {
    "workspaceId": "workspace-guid",
    "artifactId": "sql-item-guid",
    "artifactType": "SQLDbNative"
  }
}
```

`creationMode` values:

| Value | Meaning |
| --- | --- |
| 1 | Create from scratch |
| 2 | Existing table |
| 3 | Import file |
| 4 | Semantic model |
| 5 | Create from template |

Required source-create fields include `tableName`, `schema` and `creationMode`. Database/connection selection can instead use `connectionIdVariable` and `databaseVariable`.

When supplied, `sqlTargetArtifact` requires `workspaceId`, `artifactId` and `artifactType`. The inspected artifact types are `"Warehouse"` and `"SQLDbNative"`.

Creating a source and creating a physical SQL table are different operations and permissions.

### 6.2 Initialization outcome and readback

The service creates a PowerTable visual, establishes its identity in context and creates destination/source settings. The result includes a `powerTableSource` object. Do not guess that the return is just a scalar visual ID.

Reconcile the returned source with the target page's visual inventory and source details. Read the actual schema using:

`GET /v2/powertable/sources/{sourceId}/table/schema/`

This operation uses the authenticated target visual context. Also use source details:

`GET /v2/powertable/sources/{sourceId}/details/`

Verify physical columns, keys, nullability, precision, defaults and native column configuration before enabling maintenance.

### 6.3 ALM behavior

ALM import upserts source/configuration records, lookup settings and permissions. It then dispatches a separate connected-planning worker chain to generate PowerTable/InfoBridge/blend Parquet.

That dispatch is asynchronous and initiated separately from record import. Successful item import is not proof the data initialization workers completed.

### 6.4 Save transport

The native frontend provider constructs:

- `POST /v3/powertable-source/{sourceId}/data/save/`
- `POST /v4/powertable-source/{sourceId}/data/save/`

The inspected backend registers `/v3/powertable-source/data/save/` and `/v4/powertable-source/data/save/`, without the source-ID segment. No intervening rewrite was established. This is a concrete route-surface compatibility issue, not permission to guess the deployed URL.

Select the actual authorized destination route and its required visual/source context. V4 is selected by the native direct-writeback-response setting; it is not a universal replacement for V3.

The request is encoded JSON bytes with `Content-Type: application/octet-stream`, not an Arrow or MessagePack request. **The outer JSON's `data` field is an LZUTF8-compressed, Base64-encoded JSON string.**

The outer logical payload contains:

| Field | Contract |
| --- | --- |
| `metaData` | Array describing exported columns. |
| `data` | LZUTF8 Base64 string containing the operation-specific create/update/delete JSON object. |
| `relations` | Optional relation metadata. |
| `incomingRowCount` | Optional count. |
| `actions` | Optional operation actions. |
| `scdConfig` | Optional slowly changing dimension settings. |
| `requestedData` | Optional filter-specific data/configuration. |

Each metadata member has `id`, with optional `dataType`, `isPrimaryKey`, `isNullable`, `isEditable` and `isCustomColumn`.

Backend operation processing uses `createData`, `updateData` and `deleteData`; a universal top-level `inserted/updated/deleted` array is not the canonical verified body.

Update processing consumes row identity, old values, updated-column metadata and conditions. Preserve metadata-to-record order and actual key values.

### 6.5 Exact native row encoding

Create records are arrays ordered by the metadata export order, excluding non-editable primary keys. Update records are objects keyed by column name; their conditions identify the existing row by its primary key. Delete records contain primary-key values; associated deleted-row metadata carries full review/audit values.

Example insert operation object, **before compression**:

```json
{
  "createData": {
    "records": [["1250"]],
    "visualMeta": {
      "rowIds": [],
      "optionsMeta": {}
    }
  }
}
```

This assumes one editable `Amount` column and a genuinely database-generated key that is not exported as an insert value.

Example update operation object, **before compression**:

```json
{
  "updateData": {
    "records": [{"Amount": "1300"}],
    "conditions": [{"Id": "42"}],
    "visualMeta": {
      "rowIds": ["42"],
      "oldRecords": [],
      "updatedColumns": ["Amount"],
      "optionsMeta": {}
    }
  }
}
```

This illustrates an update to a row with key 42. Row IDs, old-record audit values and option metadata must come from the actual read/serializer state; empty arrays do not waive a configured approval/audit requirement.

The outer insert payload is:

```json
{
  "data": "<LZUTF8 Base64 encoding of the insert operation JSON>",
  "metaData": [
    {
      "id": "Amount",
      "dataType": "decimal",
      "isPrimaryKey": false,
      "isNullable": true,
      "isEditable": true
    }
  ],
  "relations": {},
  "incomingRowCount": 1,
  "actions": ["insert"],
  "scdConfig": null
}
```

The descriptive `data` string above must be replaced with an actual encoded value. It is not a literal that can be submitted.

Encoding/decoding order:

1. Serialize the create/update/delete operation object to JSON.
2. LZUTF8-compress it using Base64 output encoding.
3. Set the resulting string as outer `data`.
4. Serialize the complete outer payload and encode it to the native octet byte representation.
5. Send with `application/octet-stream`.
6. The backend decodes and parses the outer JSON, then Base64-decompresses and parses inner `data`.

Ordinary actions are `"insert"`, `"update"` and `"delete"`, not `"create"`. Other native action names include `"upsert"`, `"replaceAll"` and `"distribute"`; those require their separate supported operation semantics.

Lookup relation columns additionally use `isCustomColumn: true` and matching relation metadata with `tableName`, `identifierColumn` and `referenceColumn`.

### 6.6 Job verification

Use:

- `GET /v2/powertable-source/jobs/`
- `GET /v2/powertable-source/jobs/{id}/history/logs/`
- `GET /v2/powertable-source/jobs/{id}/error-details/`

A response saying writeback was initiated is not a saved-row result. Verify terminal job outcome and read the table again.

Source identity comes from the authenticated visual/destination context; do not invent a mandatory top-level `sourceId` field in the save body.

### 6.7 Maintenance safeguards

- Database-generated keys must actually be generated by the database.
- Non-generated keys need a supported explicit-entry workflow.
- Lookups store stable IDs while displaying names.
- Renaming an employee/department must not change the plan persistence key.
- Effective-date combinations require validation beyond primary-key uniqueness.
- New eligible members without facts must appear in the planning surface after the supported refresh.
- Deletion remains disabled unless authorized.

## 7. Bookmark construction and portable conversion

### 7.1 Application operations

| Method | Route |
| --- | --- |
| GET | `/v1/workload/bookmark/` |
| PUT | `/v1/workload/bookmark/batch/` |
| GET | `/v1/workload/bookmark/{bookmarkSlug}/` |
| GET | `/v1/workload/bookmark/defaultBookmark/` |
| DELETE | `/v1/workload/bookmark/{bookmarkSlug}/` |

Bookmark type 10 is personal/private; 20 is workload/public. Public does not mean anonymous access.

Batch upsert uses a JSON object keyed by bookmark slug:

```json
{
  "bookmark-slug": {
    "name": "Commercial review",
    "bookmarkType": 20,
    "bookmarkMeta": {
      "bookmarkSlug": "bookmark-slug",
      "activePageId": "destination-page-id"
    },
    "bookmarkVisualMeta": {},
    "etag": "fresh-bookmark-etag"
  }
}
```

This example shows the outer upsert shape only. It does not specify a complete snapshot or capture-options factory. An empty `bookmarkVisualMeta` is not a captured commercial review.

The batch result contains `payload.etags`; a single upsert result contains `payload.etag`. Preserve correspondence and independently read back the saved bookmark.

### 7.2 Capture versus persistence

The save projection retains bookmark slug, name, type, captured metadata, captured visual metadata and ETag. It strips store callbacks and update flags.

It distinguishes create/update/deletion sets, but the batch HTTP body is the slug-keyed upsert object, not that client change-set structure.

Construct the actual capture from selected visual/page state:

- Requested pivot, expansion and visible measures.
- Applicable formatting and filters.
- Selected visual scope.
- Page/workload variables and cross-filter state where supported.
- Include/exclude choices in capture options.

Persisting a caption and generic metadata object is not snapshot construction.

### 7.3 ALM import shape and mapping

The importer reads public bookmarks from workload plan properties. Each bookmark requires a nonempty `recordGuid`.

Portable records can contain:

- Bookmark fields including `bookmarkSlug`.
- `properties` entries with `property` and `value`.
- `cloudMeta` containing captured bookmark metadata and visual metadata.

Import:

1. Matches the bookmark by stable `recordGuid`.
2. Renames `bookmarkSlug` to persisted `slugId`.
3. Separates property records from the bookmark record.
4. Separately transforms and stores cloud snapshot metadata.
5. Reconciles bookmark property records.

Verified cloud mappings:

| Field | Destination conversion |
| --- | --- |
| `bookmarkMeta.activePageId` | Portable sheet/entity GUID to target numeric entity ID, serialized as string. |
| `bookmarkMeta.activeSelection[]` | Portable visual GUID to target numeric visual ID. |
| `bookmarkVisualMeta` object keys | Portable visual GUID to decimal target visual-ID string. |

Unmapped entries can be preserved by the importer. Preservation is not proof those references are valid. Validate every required destination target after import.

The importer can delete existing public bookmarks absent from the incoming set. Do not treat a partial bookmark list as an additive update.

Mapping of every possible nested reference, focus/spotlight state, groups and personal-bookmark portability is not established solely by these three mappings. Keep those branches explicitly bounded.

### 7.4 Restore acceptance

Change the live view, restore the bookmark and verify the selected state. Repeat after destination import. Confirm excluded capture options remain excluded and planned input values are unchanged.

A bookmark is not a planning version, approval or frozen financial submission.

## 8. Navigator construction

### 8.1 Navigator kinds and actions

Kinds:

- `NAVIGATOR_BUTTON`
- `BOOKMARK_TABS`
- `PAGE_NAVIGATOR_TABS`

For buttons, supported action names include `NONE`, `BACK`, `WEB_URL`, `PAGE_NAVIGATION`, `BOOKMARK_NAVIGATION`, `CLEAR_SLICER`, `APPLY_SLICER`, `DRILL_THROUGH` and `VARIABLE`.

Destination fields:

- Page action: `pageDestinationId`.
- Bookmark action: `bookmarkId` containing the bookmark slug.
- Web action: `webUrl`.
- Variable action: `variableId`.

Only use a destination that exists and is accessible to the audience.

### 8.2 Complete navigator base state

The base state includes:

- `type`
- `navigatorButtonState`
- `navigatorTabsState`
- `activeEditStyle`
- `style`
- `isNavigationBackForDrillThu`

Default tabs configuration:

```json
{
  "gap": 5,
  "layoutType": "horizontal",
  "scrollDirection": "vertical",
  "showScrollButtons": true,
  "hiddenBookmarks": [],
  "columns": 2,
  "rows": 2,
  "destinationType": {"all": true, "tooltip": false, "hidden": false},
  "collapsible": {
    "isEnabled": false,
    "isCollapsed": false,
    "collapsedWidth": 44,
    "identifierType": "number",
    "collapseAnimation": "instant",
    "collapseDirection": "start",
    "collapseTriggerIcon": {
      "backgroundColor": "#ffffff",
      "fillColor": "#000",
      "position": "start",
      "size": 12
    }
  },
  "tabsShortText": {},
  "hierarchy": {
    "isEnabled": false,
    "indentation": 10,
    "triggerColor": "#000",
    "fixedHeight": {"isEnabled": false, "value": 50}
  },
  "allowDeselection": false,
  "selectedBookmarkNavigatorOption": "all",
  "launchOnDeselection": "none",
  "isHideDeselectedBookmark": false
}
```

Supported layout types also include `vertical`, `grid` and `auto-grid`. Selected page arrays and hidden bookmark arrays are separate selectors.

For a page button, set `navigatorButtonState.actionType` to `PAGE_NAVIGATION` and its destination. For bookmark tabs, populate supported bookmark selectors rather than inventing a new list field.

### 8.3 Rectangle default style

`style.DEFAULT` uses `shapeType: "RECTANGLE"` and the following `shapeState`. This is a native constructor baseline, not a prescribed business palette:

```json
{
  "tooltip": {"content": "", "isEnabled": true},
  "rotation": {"all": 0, "shape": 0, "text": 0, "isEnabled": true, "type": "all"},
  "border": {"isEnabled": true, "color": "#d0d0d0", "side": "all", "width": 1, "style": "solid"},
  "cornerRadius": {"isEnabled": true, "isCustomCornerRadius": false, "topLeft": 0, "topRight": 0, "bottomRight": 0, "bottomLeft": 0},
  "padding": {"isEnabled": true, "isCustomPaddingSize": false, "bottomPadding": 5, "leftPadding": 5, "rightPadding": 5, "topPadding": 5},
  "shadow": {"isEnabled": false, "blur": 12, "color": "#000000", "side": "bottom", "placement": "outer", "opacity": 16, "width": 3, "distance": 10, "angle": 135},
  "glow": {"isEnabled": false, "blur": 10, "opacity": 100, "color": "#F7DE6E"},
  "fill": {"fillColor": "#e0e0e0", "isEnabled": true},
  "line": {"thickness": 1, "style": "solid", "edgeCap": "normal", "isEnabled": true},
  "arrow": {"direction": "right", "arrowheadSize": 50, "stemWidth": 25, "isEnabled": true},
  "chevronArrow": {"angle": 90, "isEnabled": true},
  "hexagon": {"slant": 25, "isEnabled": true},
  "octagon": {"snipSize": 33, "isEnabled": true},
  "parallelogram": {"slant": 33, "isEnabled": true},
  "speechBubble": {"chatBubbleHeight": 80, "tailPosition": "bottom-left", "tailAngle": 12.5, "isEnabled": true},
  "trapezoid": {"slant": 33, "isEnabled": true},
  "triangle": {"tipPosition": 50, "isEnabled": true},
  "snip": {"isEnabled": false, "verticalSnipPosition": "top", "horizontalSnipPosition": "right", "snipSize": 30},
  "text": {
    "value": "Button",
    "isEnabled": true,
    "fontFamily": "\"Segoe UI\", wf_segoe-ui_normal, helvetica, arial, sans-serif",
    "fontSize": 12,
    "fontColor": "#333333",
    "horizontalAlign": "center",
    "verticalAlign": "middle",
    "isBold": false,
    "isItalic": false,
    "isUnderline": false,
    "textRotation": 0,
    "padding": {"leftPadding": 0, "bottomPadding": 0, "rightPadding": 0, "topPadding": 0, "isCustomPaddingSize": false, "isEnabled": true}
  },
  "icon": {"isEnabled": false},
  "action": {"actionType": "NONE", "isEnabled": false, "pageDestinationId": null, "bookmarkId": null, "webUrl": null},
  "initialShapeType": {"isEnabled": true, "type": "RECTANGLE"},
  "accentBar": {"isEnabled": false, "value": {"color": "#252423", "side": "left", "width": 2}}
}
```

Keep the constructor's compatibility fields even when they do not affect the rectangle. Set actual captions and business typography deliberately.

Hover, pressed and active states are partial `shapeState` overrides:

- Hover: fill `#c0c0c0`, text `#000000`.
- Pressed: fill `#a0a0a0`, text `#ffffff`.
- Active: fill `#000000`, text/icon `#ffffff`.

Set `activeEditStyle: "DEFAULT"` for the constructor baseline. Do not replace the complete default style with an empty object.

### 8.4 Create the visual

Use:

`POST /v1/workload/entity/{entityId}/visual/`

```json
{
  "product": 203,
  "visualType": 203,
  "visualGuid": "<new-client-generated-guid>"
}
```

Both product and visualType use the numeric BI_RUNTIME_INPUT code 203. Do not send the enum label as a string.

The response payload is a visual record. Capture its persisted `id`; do not use the client GUID as the key in the properties batch.

### 8.5 Save the correctly nested property envelope

Use:

`POST /v1/workload/properties/batch/`

The required outer structure is:

```json
{
  "visuals": {
    "123": {
      "schema": "0.0.1",
      "properties": {
        "visualState": {
          "navigatorState": {}
        }
      }
    }
  },
  "workloadEntities": {},
  "workload": {},
  "etags": {
    "visuals": {
      "123": "<current-properties-etag>"
    }
  },
  "force": false
}
```

This is an envelope illustration, not a complete Navigator save: replace key 123 with the actual returned visual ID and **populate** `navigatorState` as follows:

1. Set `type` to the requested Navigator kind.
2. Set `navigatorButtonState` with the chosen `actionType`, actual `pageDestinationId` or bookmark slug, and unused `bookmarkId`/`webUrl`/page destination fields null as appropriate.
3. Set `navigatorTabsState` to the complete object in section 8.2, then apply the intended supported selectors/layout.
4. Set `activeEditStyle` to `"DEFAULT"`.
5. Set `style.DEFAULT` to an object with `shapeType: "RECTANGLE"` and `shapeState` equal to the complete literal object in section 8.3.
6. Set `style.HOVER.shapeState`, `style.PRESSED.shapeState` and `style.ACTIVE.shapeState` to the exact partial overrides listed in section 8.3.
7. Set `isNavigationBackForDrillThu` to false unless the specific drill-through workflow requires otherwise.

The nesting is **visual record -> schema/properties envelope -> visualState -> navigatorState**. A direct `visuals[id].navigatorState` field is not the serialized native property contract.

Read the page/entity properties to obtain the current visual properties ETag. The exact new-visual ETag response location must be matched to that deployed read branch; no dedicated new-visual ETag endpoint was established.

Preserve current owner/page properties and update placement through the supported page layout record. Creation alone does not position the Navigator.

Treat HTTP 409 as a conflict requiring reread/reconciliation, not automatic force overwrite.

### 8.6 Navigator acceptance

Read the saved visual envelope and verify all targets. Confirm page buttons, bookmark tabs, active state, hover state, tab overflow and layout placement behave correctly for the intended audience.

Property readback is an API persistence check. Clicking and rendering are separate acceptance checks and must not be reported as performed when they were not.

## 9. Home asset upload and layout

### 9.1 Upload transport

Use the configured application backend:

`POST /api/assets`

Headers:

- `Authorization: MWCToken <approved-application-token>`
- `X-Ms-Workload-Resource-Moniker: <destination-workload-object-id>`

Home uses multipart form data with:

| Field | Value |
| --- | --- |
| `file` | Actual image file bytes and filename. |
| `workloadId` | Destination workload object ID, when supplied by context. |
| `feature` | `home-layout` |

Do not add entity/visual scope fields to an ordinary workload-scoped Home upload. They are used for other asset scopes.

Let the multipart encoder generate the boundary and matching Content-Type. Sending a bare `multipart/form-data` header without its boundary is invalid.

### 9.2 Upload response

The response's `payload` contains:

- `fileId`
- `originalFileName`
- `mimeType`
- `fileSize`
- `category`
- `scope`
- `workloadId`
- `feature`
- Nullable scope-dependent `entityId` and `visualId`
- `url`
- `uploadedAt`
- `uploadedBy`

Home stores the returned `fileId` in `imageConfig.source`. It does not store the uploader URL, local path or temporary browser blob URL.

### 9.3 Retrieval and deletion

| Method | Relative route | Result |
| --- | --- | --- |
| GET | `/api/assets/{encodedFileId}` | Metadata envelope. |
| GET | `/api/assets/{encodedFileId}/content` | Binary image content; optional Range request. |
| DELETE | `/api/assets/{encodedFileId}` | Delete asset. |

Use the same approved workload authentication context. Content retrieval accepts HTTP 200 and 206. The inspected client treats deletion 404 as already absent; this is not permission to delete another user's asset.

### 9.4 Image validation and placement

The inspected Home validation accepts PNG, JPEG and SVG up to 5 MiB. Recheck limits for the actual destination build.

Generate an illustration only with explicit user authorization and a sanitized business brief. Generation and upload are separate operations.

Create a native image item with an actual returned asset source and place its item ID in the ordered row list. Row order controls placement; reordering the item catalog alone does not move the image.

Use `fit` where the complete image must remain visible. Use `fill` only when cropping is acceptable. Height, manual-height state, widths and source pixel dimensions are different settings.

### 9.5 V2 Home provider operations

| Method | Route | Purpose |
| --- | --- | --- |
| GET | `/v1/access/users/home-layout/` | Ordinary user's effective Home. |
| GET | `/v1/access/roles/layout/` | Role-layout inventory. |
| GET | `/v1/access/roles/layout/{roleId}/` | Role content and current version. |
| PUT | `/v1/access/roles/layout/{roleId}/` | Role-layout upsert. |
| PATCH | `/v1/access/roles/layout/order/` | Role priority update. |
| DELETE | `/v1/access/roles/layout/{roleId}/` | Role-layout deletion. |

Role content upsert carries `data` containing `items` and `rows`, with current `etag` when available. Preserve any role-order field required by the selected provider branch.

Normal save must not force overwrite. A `force` option exists for explicit conflict resolution, not silent recovery.

Role priority is updated separately:

```json
{
  "roles": [
    {"roleId": "resolved-role-id", "homeLayoutOrder": 0}
  ]
}
```

Home visibility is saved separately through workload properties; it is not a role-layout API field.

The inspected provider uses PUT for role content. An adapter using POST must be reconciled against the deployed route rather than treated as an equivalent method.

### 9.6 Failure recovery

Upload, role content, role priority and workload visibility are separate mutations. No cross-operation transaction was established.

If upload succeeds and layout save fails, record the owned asset ID and failed phase. Read destination content before retrying. Delete only assets proven to be unreferenced and authorized for cleanup.

Read back role content and ordinary-user effective Home. A frontend default-layout fallback is not evidence that the requested saved layout exists.

## 10. End-to-end construction order

1. Resolve destination workspace, item, model and approved authentication.
2. Select native/backend versions and storage branches.
3. Create the independent sheet/visual identity registry.
4. Build semantic-source assignments from actual model fields and stable keys.
5. Create typed inputs and formulas with visibility, order, aggregation and formatting companions.
6. Construct supported allocation/validation rules and verify their persistence.
7. Bind and initialize maintenance sources; read back physical/native schemas.
8. Build connected sources, ordered transformations and compatible reporting-grain outputs.
9. Execute the required graph and poll every expected job.
10. Bind consuming visuals to verified output fields and retrieve refreshed data.
11. Capture supported bookmark state and create navigation targets.
12. Create/save Navigator visuals with complete state and current ETags.
13. Generate/upload an authorized illustration; save Home content, priority and visibility.
14. Independently read all saved definitions/native registrations.
15. Test salary/volume propagation, version isolation, closed-version retention and new-member eligibility.

Do not publish an empty Plan to bypass unresolved core factories.

## 11. What remains before calling the builder complete

| Area | Newly established | Remaining implementation or verification boundary |
| --- | --- | --- |
| Typed inputs | Native per-type structures, defaults, unions, create transport and response variants. | Integrate every intended branch, reconcile route/context versions, provision companions and run native save/reopen tests. |
| Allocation | Native rule selectors, tagged distribution/min-max shapes and engine request wrapper. | Verify actual engine route accessibility/authorization and execute leaf/total/weighted allocation checks. |
| InfoBridge | Reload APIs, worker dispatch, targeted polling and Parquet stream/RLS behavior. | Complete source/transformation factories and prove the full consumer graph refreshes and reconciles. |
| PowerTable | Existing-table creation, schema readback, frontend insert/update/delete shapes, LZUTF8 Base64 inner encoding and job APIs. | Resolve source-qualified client versus unqualified backend save routes; verify native key/lookup behavior and database save/reopen. |
| Bookmarks | Save projection, upsert routes and concrete ALM identity mappings. | Complete requested capture branches, remaining nested-reference conversion and destination restore tests. |
| Navigators | Numeric visual/product creation codes, nested property batch/ETags, complete tab state and rectangle constructor defaults. | Resolve new-visual ETag readback, integrate page placement, resolve all targets and verify navigation/rendering. |
| Home | Actual multipart fields/authentication, file-ID mapping, retrieval/deletion and role-layout PUT. | Integrate generation consent, destination asset upload, priority/visibility phases and audience/render checks. |

These are no longer all equally unspecified. However, an extracted API contract is not an implemented adapter, and an implemented adapter is not runtime verification.

### 11.1 Explicit compatibility findings

| Finding | Required handling |
| --- | --- |
| Native filter-context enum 10/20 versus older backend 0/1. | Select and validate a compatible writer/validator pair. |
| Native V2 column route does not alone prove direct backend registration. | Resolve actual mounted route and response shape for the selected host. |
| Source reload's optional file-reparse comment versus required binary validator. | Verify the actual route payload rule; do not claim universal bodyless support. |
| Native PowerTable source-qualified save URL versus backend URL without source ID. | Resolve actual destination routing/context; do not invent a proxy rewrite. |
| Home role provider PUT versus adapter POST. | Align the adapter to the deployed method before claiming Home persistence. |
| ALM success versus separately dispatched PowerTable/InfoBridge workers. | Poll/read data initialization separately from import completion. |

## 12. Completion and failure policy

For API-only authoring:

- Do not substitute manual UI instructions for missing APIs.
- Do not fabricate values, assets, snapshots, job completion or successful initialization.
- Do not silently accept stale results, partial success or unmatched identity references.
- Record each completed phase and each unrun check.
- Recover uncertain submissions through readback before replaying.
- Preserve unrelated state and use current version checks.
- Keep rendering checks separate from API persistence/execution.
- Claim end-to-end success only after every requested business outcome is verified.

The correct conclusion after this inspection is: **substantial construction and execution contracts have been extracted; the complete end-to-end builder still requires adapter integration and runtime acceptance.**
