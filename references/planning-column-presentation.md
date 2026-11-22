> v20: All reports use content-sized rich-text headers plus a small buffer and
> native row/column hierarchy icons `gmate`, independent of business use case.
> Read [report-presentation-defaults.md](report-presentation-defaults.md) and
> discover REPORT-PRESENTATION. Preserve intentional user overrides.

> v18: [measure-display-defaults.md](measure-display-defaults.md) is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

# Planning columns, expansion and default filter cards

Use for new Planning grids, disappearing columns on Reading/Editing transitions,
column hierarchy expansion, incomplete sizing, or missing native-measure cards.

## Evidence and scope

On 2026-11-14 the user confirmed recovery of Workforce Merit after ONLY these
changes: `columnExpandCollapse` became an empty per-member map with
`expandColumnToLastLevel:true`, and `tableState.columnHierarchyLevel` marked each
current bound column-dimension ID `{"collapsed":"Expanded"}`. This confirms that
repair for that report. It does not isolate which of the two settings mattered or
establish a universal runtime cause.

The user subsequently requested all five comparison items as an authoring recipe:
expansion-to-leaf, hierarchy-level expansion, default column-total handling,
complete sizing, and native-measure filter cards. The last three are additional
requested configuration improvements, not separately confirmed causes or fixes.

## Reusable authoring rules

1. Derive expanded levels from `visualState.columnDimensions[].id` of the target.
   A Year-only grid gets one level; Year/Quarter gets two; Year/Quarter/Month gets
   three. Other column dimensions use their own current IDs. Never copy another
   sheet's IDs or hard-code time grain. Preserve time metadata and date extension.
2. For the explicit expansion repair, set `columnExpandCollapse` to
   `{"columnExpandCollapse":{},"expandColumnToLastLevel":true}` and replace only
   `tableState.columnHierarchyLevel` with the target levels marked Expanded.
   Preserve other tableState entries. Clear the old member map as part of this
   chosen expansion policy; do not replay foreign runtime member IDs.
3. Use explicit authoring defaults for missing column positions: grand total
   `"Left"`, subtotal `null` (OFF). Preserve existing explicit null and non-null
   choices. This supersedes the earlier recipe that removed null overrides.
   New Planning construction also sets row grand total and subtotal to `"Top"`;
   see [planning-totals-defaults.md](planning-totals-defaults.md).
4. Fill missing layoutSizes fields from the observed Planning baseline: tableWidth
   80, chartWidth 150, labelWidth 120, isResponsive false, bulletWidth 300,
   maximumChartWidth 200, isMaximumChartWidthAllowed false,
   preferedWidthSelection "measure". Retain existing widths and responsive choices.
   These are selected presentation defaults, not mandatory schema values; the
   native initializer can be empty. Do not claim a missing width proves corruption.
5. Add an ordinary visible NUMERIC filter card for every supported assigned numeric
   Values field using its exact source/measure identities and grouping grain.
   Initialize it to All (`filter: []`, null numeric bounds); never copy a Year or
   other dimension selection into the measure card. This includes semantic,
   From Sheets and InfoBridge values without changing their source types.
   Planning cards keep the actual `ameasure`/Values bucket, not chart AC/PY roles.
   Preserve existing selections, Context, and cards. Do not label From Sheets or
   InfoBridge assignments as Power BI or invent cards for unassigned fields.

New Planning construction uses this recipe. `columnPresentation:"preserve"`
opts out; explicit tableState/columnExpandCollapse/saved pivots retain their
authored expansion, and explicit totals_config retains its chosen totals.
Updates require the requested scope: do not automatically expand deliberately
collapsed saved views or bookmarks. Row-only sheets have no column levels to seed.

Never alter input values, definitions, bounds, formulas, permission settings,
aggregation, source bindings, leaf-ID mappings, rich headers, semantic colors,
Home, dashboard ownership or embeds as a column-display repair. An embedded grid
uses its source owner; update the owner once, not a cloned embedded measure set.

## Commands

```text
python plan.py planning-column-presentation --input properties.json --out candidate.json
python plan.py planning-column-presentation --input properties.json --out candidate.json --expansion-only
```

Callables: `runtime.column_presentation.expand_columns(properties)` and
`apply_column_presentation(properties, expansion=True, sizing=True,
default_column_totals=True, native_measure_filters=True)` return a copy.
Publish using the existing native property-batch adapter with fresh owner ETags,
or a scoped ALM update. Cache the before/submitted states and save receipt.
Follow the user's validation instruction; a save receipt is not runtime testing.
