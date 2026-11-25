# Query Values in Fabric SQL and OneLake

For both direct From Sheets and From Queries on artifacts in **OneLake storage
mode**, start with the onelake linked values guide. This guide
covers query outputs; no SQL row id is required for a direct OneLake sheet link.

Inspect the current artifact's query registry and selected output catalog.
For Fabric SQL, a returned numeric `sqlPk` qualifies output fields. For OneLake,
when that property is absent/null, the current `id` qualifies output fields.
The assignment's `queryId` is that same qualifier. `id` and `sourceId` both use
`queryId[outputFieldId]`; never use the source ID, a field ordinal, or an input
record key. Preserve opaque IDs verbatim, whether UUIDs or Q-prefixed strings.
A malformed explicit sqlPk is an error, not permission to silently change modes.

```json
{
  "id": "<current-query-id>[<current-output-id>]",
  "sourceId": "<current-query-id>[<current-output-id>]",
  "queryId": "<current-query-id>",
  "sourceType": "InfoBridge",
  "columnType": "Column",
  "dataType": "Double",
  "aggregationType": "sum"
}
```

This is a partial illustration. Use `runtime.consumer_bindings.output_catalog`
and `numeric_output_fields` for complete current catalog descriptors;
`resolve_assignment`/`assert_resolved` verify ownership, output ID and captions.
The default additive identity hashes the exact `SUM__queryId[outputFieldId]`
assignment key. Do not rehash existing persisted internal formula identities.
`execution_map` retains the current OneLake ID; SQL profiles use the returned pk.

Pass resolved numeric outputs in the build specification's `queryFields` list.
Planning Native Values can reference those exact keys; dashboards can use them
in cards and charts, including separately labeled comparison series. The builder
emits real Native companions, formula dependencies and teal linked-result
formatting. Semantic-model master fields stay in Rows, Columns and slicers.
Do not convert query outputs into pretend Power BI measures.

The opaque-query form matches saved Planning properties and query metadata: a
computed output can be a string hash, while its qualified assignment and separate
`queryId` match the registry exactly. That establishes serialization, not every
new artifact's runtime calculation. Query outputs must retain the storage Context
that connected owners use; the storage context guide holds the bundled guards.

No initial refresh is required for a correctly wired deployment. Validate source
ownership, selected output types, dependency edges and semantic dimension/context
mapping; report materialization and edit-to-P&L propagation separately. A metadata
read failure may use only documented bounded GET alternatives. Never replay
mutations across API versions or switch storage modes automatically.

The source-aware `resolve_measure`, `registered_measure`, recipe comparison phase
and output-rebinding helper also use this domain, so callers must not pre-index
sqlPk.
