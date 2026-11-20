# Measure cards at All and Auto number formatting (v18)

Apply these defaults to new applications and new numeric measures in any business
case. They are independent of the wording of the prompt or the five case recipes.

## Assigned measure cards stay visible, with no preset restriction

Show assigned Values measures in the side filter panel. Initialize each ordinary
measure card with `filter: []`, no selected values/presets, and null numeric
min/max/equal bounds. The intended UI is **is (All)**. A range slider's available
extent or the editor's `between` operator alone does not mean a range is applied.
Do not hide/delete the card to achieve an unrestricted view. Preserve complete
typed field IDs and source, query, visual, aggregation and bucket identities.

This applies to semantic DAX and aggregated numeric columns, native query /
InfoBridge values, and supported From Sheets assignments. Custom inputs/formulas
are numeric measures too, but do not invent a source assignment just to create a
filter card: use their actual supported registration contract.

Dimension defaults may select an explicitly requested year, region or scenario.
Apply the selection only to that dimension's **own** card. A measure card can
contain Year/Region/etc. assignments as its evaluation grain: those are not the
card's selected field. Never match `any(pivotAssignment.id == year)` when applying
a dimension selection. `runtime.filters.select_axis_filter()` requires a single
Grouping assignment and excludes measure and Context cards.

Existing intentional measure restrictions remain during unrelated repairs. The
user may set them manually, or explicitly request a business threshold. No
measure restriction is introduced merely because a field is assigned to Values.
Use `clear_measure_filter_selections(properties)` only for an authorized reset to
All; it keeps the cards, dimension selections, hidden Context, formulas and values.

Default constructors: `ensure_chart_filters()` for charts/KPIs and
`ensure_assigned_measure_filters()` for Planning. Both create unrestricted cards;
they preserve existing selections. `ensure_native_measure_filters()` remains a
compatible alias. Registration and filtering are separate operations.

## Numeric Planning measures use per-measure Auto

The user-selected MSIT reference contains this operation for all four numeric
measures (two DAX, one input and one formula):

```json
{"format":{"13":"auto"},"order":8}
```

The owner is `properties.visualState.formatConfig.measure[resolvedMeasureId][]`.
Property `13` is scaling. **`auto` is different from `autoFixed`.** In that same
export, global `numberFormatting` remains `formatType: "default"` and
`scalingFactor: "autoFixed"`; the per-measure operations implement the selected
menu option. Do not change the global mode, use the display label `Auto` as a
wire value, or set a fixed `1000000` divisor by default.

Use `runtime.display_defaults.auto_number_formatting(state, numeric_ids)` after
numeric measure registration. It assigns monotonically increasing format orders,
is idempotent, and preserves colors, percentage flag `10`, decimal precision `11`,
currency prefixes/suffixes and every unrelated format property. Native source
types or custom `columnMeta.data_type: "Number"` identify numeric measures;
captions and source family do not. Text commentary, dates and checkboxes are
excluded. Never rescale stored values, inputs, bounds, formulas or aggregation.

New numeric Data Inputs, Simulation, Forecast, Formula, semantic, From Sheets and
query measures receive Auto. Explicit business formatting (for example fixed
millions or an intentionally unscaled FX rate) wins. Percentage formatting remains
percentage formatting; Auto does not turn a ratio into an amount. Default calls
preserve existing per-measure scaling; `overwrite=True` is an explicit scoped
reset. Existing cell/row/column overrides remain; inspect operation order if they
override the requested display. Do not clear all formatConfig or replace a full
globalStyles object with a fragment.

This observed wire shape is **Matrix/Planning-specific**. For a Charts/KPI numeric
display use its own `hiddenProperties_!!!_numberFormatting` contract in A02 of
`audit-contracts.md`, with Auto for amount roles and percentage for percentage
roles; preserve its encoding and full required state. Never copy Matrix property
13 into a Charts store or use the chart `percentage` scaling token in Matrix.

## Discoverable commands and scoped update

```text
python plan.py discover "show assigned measures as All and use Auto number formatting"
python plan.py reference measure-display-defaults.md
python plan.py planning-display-defaults --input display-request.json --out candidate.json
```

`examples/measure-display.request.json` is a complete synthetic local example of
that request. Replace it with the current target's properties/records for a real
repair; do not deploy the synthetic IDs.

The request contains actual current `properties` and `records` (native or ALM
DataInput columns), plus optional `overwrite_scaling` and
`clear_measure_selections` booleans. Both default false. Set them true only when
the user requested that reset. Numeric IDs are resolved from those typed records
and assignments. The command returns a local properties candidate; deployment
still uses the ordinary authorized writer, current ETags and preservation rules.

Business routing: F03 for Auto, F07/F22 for unrestricted visible measure cards,
F21/F18/F19 for source identity. The five-case builder uses the same helpers.
The export is evidence for persistence shape, not proof of new runtime behavior.
Respect the user's decision to perform UI/runtime validation themselves.
