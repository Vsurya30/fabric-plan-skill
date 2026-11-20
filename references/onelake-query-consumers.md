> v39: Rows/Columns already define storage grain. External Context is only for additional stored selections, never ordinary page/global filtering. Connected Planning owners must match Context; query outputs must retain it. Read [storage-context.md](storage-context.md) for the bundled guards and build-time query evidence.

# Query Values in Fabric SQL and OneLake

For both direct From Sheets and From Queries on artifacts in **OneLake storage
mode**, start with [onelake-linked-values.md](onelake-linked-values.md). This guide
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

The opaque-query form was verified against saved native Planning properties and
current query metadata on 2026-11-16. The reference's computed output was a string
hash; its qualified assignment and separate `queryId` matched the registry exactly.
This establishes serialization, not every new artifact's runtime calculation.

No initial refresh is required for a correctly wired deployment. Validate source
ownership, selected output types, dependency edges and semantic dimension/context
mapping; report materialization and edit-to-P&L propagation separately. A metadata
read failure may use only documented bounded GET alternatives. Never replay
mutations across API versions or switch storage modes automatically.

The v36 source-aware `resolve_measure`, `registered_measure`, recipe comparison
phase and output-rebinding helper also use this domain. An opaque ID is not only
supported by the low-level constructor: callers must not pre-index sqlPk. Both
routes were compared with fresh saved native and ALM metadata on 2026-11-17.
