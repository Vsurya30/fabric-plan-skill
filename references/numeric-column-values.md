# Direct numeric columns in Values

Use this for direct column assignment, implicit measures, default Sum, missing
DAX measures, screenshot recreation or changing to a column-based semantic model.
Discover `NUMERIC-COLUMN-VALUES`. This is integrated into Planning, Intelligence
cards, charts, comparison charts and automatic dashboard construction.

## Construction rule

Resolve the requested metric against the current semantic model. Use an existing
explicit DAX measure when it is the intended source. When the intended source is
a numeric Column, assign it directly to Values and default its **source
aggregation to Sum**. Do not require or create a DAX wrapper just to use it.
Do not assign every numeric field: keys and codes remain dimensions/mappings
unless the user actually requests them as metrics.

New direct column bindings retain `sourceType: "PowerBI"`, `columnType: "Column"`,
`dataRoleType: "Measure"` and the exact current model field in `id`/`sourceId`.
They explicitly include `aggregationType: "sum"` and `customSource: true`.
Planning uses `bucketId: "ameasure"`; Intelligence uses its appropriate AC/PY
bucket. Presentation labels never replace physical table/column identity.

```json
{
  "id": "Facts[Amount]",
  "sourceId": "Facts[Amount]",
  "sourceType": "PowerBI",
  "columnType": "Column",
  "dataRoleType": "Measure",
  "dataType": "Double",
  "bucketId": "ameasure",
  "aggregationType": "sum",
  "customSource": true
}
```

This is a contract excerpt, not a full assignment. Use
`runtime.semantic_values.semantic_value` for complete catalog-based bindings.
Supported numeric types are Int64, Double and Decimal. Current source aggregations
are sum, average, min, max and count; input aliases Avg/Average normalize to
`average`. Honor explicit source aggregation choices. DAX measures retain
`columnType: "Measure"` and do not receive an implicit-column aggregation.

## Source aggregation and grid totals are separate

In a Planning Native measure spec, **`sourceAggregation`** controls the semantic
query. It defaults to `sum` for a numeric Column. **`aggregation`** and
**`columnAggregation`** control grid row and column totals. Never derive the
source aggregation or identity from those total settings.

```json
{
  "key": "rate",
  "kind": "Native",
  "source": "Facts[Rate]",
  "label": "Rate",
  "aggregation": "None",
  "columnAggregation": "None"
}
```

This assigns Sum at the source and suppresses both grid totals. To explicitly
average the source, add `"sourceAggregation": "average"`. Existing specs that
used a grid aggregation to imply a source choice must express it separately.
Do not change a user's saved Sum on rates or thresholds based only on the label.
Currency conversion grain, aggregation of rates, and mixed-currency totals still
need the business calculation contract; the assignment default does not settle
those calculation choices.

Intelligence card/chart specs use `aggregation` for their source value and
`comparisonAggregation` for a chart baseline. Both default to Sum for columns.
`resolve_measure` accepts the same source `aggregation`. The shared constructors
generate matching chart field filters using the actual source type and method.
Automatic dashboards can select an assigned numeric-column metric when no
explicit DAX metric is present.

## Preserve persisted identities

For new column bindings, the bundled identity registry uses the normalized
source aggregation and exact field key, such as `SUM__Facts[Amount]`. For an
existing report, resolve and retain the current registered `measureGuid`.
The observed UI changes `aggregationType` while retaining an existing identity
and formula references. Never rehash a persisted ID because its current
aggregation differs from the hash prefix that originally created it.
`registered_measure` preserves that current identity when reusing a Native
column in another visual. From Sheets and InfoBridge keep their own contracts;
this default does not reclassify their origins as Power BI.

## Evidence and portable example

A user-saved MSIT report was read on 2026-11-16 through the native page API and
full definition export. Five direct numeric columns had `aggregationType: "sum"`;
the source remained a Column assigned as Measure. FX grid totals remained None,
and threshold grid totals remained Min. Some existing measure identities and
filter configuration hints retained their previous aggregation history. Preserve
existing state; use consistent assignments and filters for fresh construction.
The package contains no report IDs, credentials, financial rows or old-report
dependency from that capture. Saved-definition evidence is not calculation proof.

Run `python examples/numeric-column-values/build.py <output-folder>` using the
extracted package alone. It builds a complete synthetic application without any
DAX measure, with independent grid totals, explicit Average override, comparison
charts, Home, Arial and complete Page Navigators. No live deployment is performed.
