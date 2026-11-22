# Measure source identity and typed assignment

Use this guide when assigning measures to Planning, Intelligence, filter cards or
downstream calculations. The display caption never proves the measure's source.
Resolve the requested origin first, then its current catalog IDs and native types.
A DAX measure registered inside a Planning sheet remains a semantic-model measure;
its Native companion row ID does not make it a From Sheets output.

## Business request to source contract

| Intended source | Required identity and type | Constructor |
| --- | --- | --- |
| Original Power BI DAX measure | Current model plus exact table-qualified field ID; sourceType PowerBI, columnType Measure; matching sourceId, tableName, columnName, dataType and semantic measureGuid | semantic_measure / resolve-measure-binding |
| Direct numeric Power BI column | Exact current field; sourceType PowerBI, columnType Column, dataRoleType Measure; source aggregation defaults to sum | semantic_value / semantic_measure / resolve-measure-binding |
| Input, Forecast or formula produced by a sheet | Current owner visual ID + source measureGuid; external key is SQL column record id or, for OneLake without id, measureGuid; source record type DataInput, Forecast or Formula, including VisualColumn wrapper; match visualState.manage_measures | resolve-measure-binding / registered_measure |
| From Queries / InfoBridge output | Current query registry ID (SQL sqlPk or opaque OneLake id) and selected post-transform output ID, alias and data type; sourceType InfoBridge and query-qualified id/sourceId | resolve-measure-binding with consumer_bindings |

Power BI display folders (for example a business folder called Mid-Market
Estimate) are not physical table identities. Read the actual model catalog and
preserve the table-qualified measure ID. Do not create a new ID from folder or
caption text. AC/PY/ameasure identify destination roles, not the source namespace.

For a comparison, resolve both sides independently. An estimate Forecast may be
From Sheets while the current forecast comparator is a DAX measure. Do not send
both through the same linking helper because they appear on the same source grid.
Conversely, a calculated USD estimate/forecast created as a sheet Formula remains
a sheet output; it must not be replaced by an unrelated DAX amount with a similar
name. Honor currency, period and grain in addition to identity.

## Executable construction

```text
python plan.py resolve-measure-binding --input binding-request.json --out assignment.json
```

The input is an object with `request` and optional `model`, `sheets`, `queries`.
PowerBI request: `{ "sourceType":"PowerBI", "fieldId":"Finance[Current Forecast]", "bucket":"PY" }`.
Use the current model metadata as `model`, not an invented field dictionary.
When this field is a numeric Column, the binding defaults to `aggregationType:
"sum"`. Supply request `aggregation` only for an explicit source override. This
does not change an explicit DAX Measure. Read
[numeric-column-values.md](numeric-column-values.md) for separate grid total
settings and preservation of existing registered IDs after UI aggregation edits.

Visual request: sourceType `Visual`, string `visualId`, `sourceMeasureGuid`,
optional `columnId`, and destination `bucket`. `sheets` contains the matching
owner's `name`, `visualId`, current `properties` and current `columns` records.
The helper requires the selected column's native type and source measureGuid to
match its owner registration. The returned destination measureGuid is distinct
from the source measureGuid; use `sheet_column_id` for the external column key.
Fabric SQL uses the current row id; OneLake uses measureGuid when id is absent/null.
Current owner-scoped OneLake records may also omit visualId. When present, it
must agree. Runtime visual IDs remain distinct from ALM visual GUIDs. Read
[onelake-linked-values.md](onelake-linked-values.md) for both storage profiles.

InfoBridge request: sourceType `InfoBridge`, `queryId`, `outputId`, a typed
`assignment` from the current query metadata, and destination `bucket`. `queries`
contains the current native records and selected output metadata. Use sqlPk only
when returned; OneLake records without it use their opaque id. The bundled
`find_query` resolves this exact domain without requiring a SQL property.
It reuses the query resolver and numeric type family contract. Input row IDs,
source-record IDs, old query IDs and output ordinals cannot replace output IDs.
Unknown source types or missing metadata are explicit construction dependencies.

Python callers selecting a registered Planning measure use
`registered_measure(properties, record, visual_id, sheet_name, model=...)`.
It follows a Native companion's exact upstream pivot assignment. For a local
Formula/Input/Forecast it builds a sheet link from the current source records.
`from_sheet_assignment` now rejects Native companions instead of silently making
an invalid link. Never bypass this guard by changing a measure's label or tag.

These constructors preserve lossless string IDs. In an existing Planning
consumer, changing its internal measureGuid can break formulas, formatting or
stored inputs: preserve it or perform an explicitly scoped migration. Rebinding
a chart does not authorize changes to Planning formulas or stored values.

## Reconcile every registration together

When replacing a chart binding, update pivotAssignments and its ordinary
superFilterAssignments together: id, sourceId, sourceType, visualId/queryId,
columnType, dataRoleType, dataType, measureGuid, table/column metadata, isDaxMeasure
and sort references. `comparison_chart` calls `reconcile_chart_filters`: retain
exact surviving source/role cards and their selections; remove obsolete generated
cards and duplicates; add the corrected field cards. A same-caption field from
another namespace does not inherit selections by name. Custom/context filters
and existing hidden selections remain untouched. Reconcile those separately only
if they explicitly reference the changed field; never globally replace strings.

This is required construction logic, not a request for runtime validation.
Read current metadata and ETags needed to save. If the user skips validation,
do not query calculations, open the UI, perform post-save readback or run a test
suite. Return the API receipt and state that runtime behavior was not validated.
