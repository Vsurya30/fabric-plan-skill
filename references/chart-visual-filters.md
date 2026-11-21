> v18: [measure-display-defaults.md](measure-display-defaults.md) is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

# Intelligence visual-level filter registration

Every dimension or measure assigned to an Intelligence chart needs its own ordinary visible field-filter registration. A chart assignment alone does not create the saved side-panel filter card. This applies to KPI cards as well as category/comparison charts.

The active property is **`properties.superFilterAssignments[]`**, alongside `properties.pivotAssignments`. It is not `visualState.embeddedSuperFilter`, page-level filters, global filters, external Context or a slicer. Those have separate purposes and must be preserved. New measure cards must have empty `filter: []` and null min/max/equal values: no restriction (the card displays All); an empty `superFilterAssignments: []` means no registered field cards.

## Construct from current assignments

Use `runtime.chart_filters.ensure_chart_filters(props)` after chart field construction, then `audit_chart_filters(props)`. `intelligence.card()` now calls the constructor automatically. The native dashboard placement phase also ensures and audits registrations for chart visuals. For other chart constructors, call the same helper after setting all categories and measures.

The factory is parameterized by current assignments; it contains no historical report, model, query or source IDs. It creates fresh filter IDs. In repair mode it adds missing ordinary cards without deleting existing filters, selected values, Context, hidden scope, formatting or geometry. If an existing registration is corrupt, inspect and repair that registration's identity explicitly while preserving its selection; do not clear the whole list to pass validation.

For each assigned field:

- Set `isDefault: true`, `position: "RIGHT"`, `filterLevel: "visual"`, and `configuration.hide: false`.
- Use the displayed field label (`customName`, then `name`, then `columnName`) for the configuration name.
- Copy the full current field assignment into the registration, including source/query identity, actual bucket, aggregation and type. Preserve large string IDs exactly.
- A numeric measure uses `isDefaultMeasure: true`, an advanced NUMERIC filter, `filterOperator: "between"`, and null min/max/equal defaults. `isDaxMeasure` is true for a PowerBI semantic Measure and false for an aggregated column or InfoBridge column.
- A grouping dimension has its own non-measure card. Text uses basic FACET configuration; a numeric dimension can use NUMERIC configuration while remaining `isDefaultMeasure: false`.
- Include the query ID in sort metadata for InfoBridge fields. The sort column ID must match the assignment ID.

A grouped measure filter contains the chart's grouping assignments followed by that one measure. These dimensions define its evaluation grain. Their presence inside a measure filter **does not** count as their own dimension filter cards, and does not authorize copying dimension selections into that measure filter. The inspected comparison-chart shape uses outer filter `bucketId: "AC"` for measure filters, while the nested measure retains its actual `AC` or comparison bucket such as `PY`. Grouping filters retain their own bucket such as `axis`.

Do not deduplicate only by field name or ID. The same field may be grouped and aggregated, or assigned in comparison buckets using different aggregations. Match source, query, field, bucket, role, column type and aggregation.

## Numeric measure shape

This compact excerpt illustrates the contract; use the complete constructor rather than sending the placeholder strings:

```json
{
  "id": "filter_<new-unique-id>",
  "pivotAssignments": ["<grouping assignments, if any>", "<full assigned measure>"],
  "isDefault": true,
  "isDefaultMeasure": true,
  "isDaxMeasure": false,
  "bucketId": "AC",
  "configuration": {
    "name": "Planned compensation",
    "hide": false,
    "filterMode": "advanced",
    "visualType": "NUMERIC",
    "filterOperator": "between",
    "alphaNumericValues": {"minValue": null, "maxValue": null, "equalValue": null}
  },
  "filter": [],
  "position": "RIGHT",
  "filterLevel": "visual"
}
```

The constructor also emits complete sort, Top N, search, scale, selection, aggregation and pane configuration.

## Import, identity repair and validation

When query identities are resolved after import, reconcile nested filter assignments and sort IDs along with the chart assignments. Do not add a correct filter while leaving a stale default registration for the same assigned field. Native numeric query IDs and portable ALM query GUIDs are different serializations; compare identities consistently within each representation.

The audit checks one ordinary visible filter per assignment, matching nested identities, role flags, type, bucket and evaluation grain. It detects a dimension that appears only inside a measure filter, hidden or duplicate registrations, and stale query/sort identities. Preserve extra intentionally authored filters rather than treating them as unwanted fields.

Some service versions can add `customSource:true` to a top-level semantic-measure
assignment while leaving its ordinary filter assignment without that flag. The
audit normalizes only this true-versus-absent case; explicit false, InfoBridge
flags, source IDs, buckets, types and evaluation grain remain significant.

Save using fresh ETags, reread native properties, and compare all unrelated visual/page properties for preservation. Export and audit the portable definition too. Persisted filter metadata does not prove that the pane renders, that changing a threshold works, or that an InfoBridge query has successfully refreshed. Do not attribute an InfoBridge query-not-found error solely to missing filter registration.

## Evidence boundary

Synthetic fixtures cover numeric InfoBridge filters, semantic measure filters,
and category/comparison examples. Offline tests verify the identity normalization;
native visual behavior remains a separate acceptance step.
