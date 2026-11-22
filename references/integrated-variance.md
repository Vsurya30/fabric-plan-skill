# Integrated variance comparisons in Intelligence dashboards

## Required default and business routing

When a business request compares a current/actual/planned measure with a baseline
in a bar or column chart, use native **integrated variance** by default. This is
part of the required Intelligence dashboard presentation, alongside the rich-text
header, useful slicers and embedded Planning sheet. Merely assigning AC/PY or
showing grouped bars does not implement this default. Honor an explicit request
for a different chart style; ordinary single-series bars remain ordinary bars.

Examples: sales actuals versus targets, forecast versus actuals, proposed salary
versus base salary, expense budget versus spend, and risk-adjusted outlook versus
baseline. Choose the comparison direction from the business meaning. AC and PY
are chart roles: PY need not mean previous year. Preserve meaningful business
captions, units, category grain, filters and source-specific field identities.
An increase in cost is not automatically favorable; preserve configured sign and
color polarity, or explicitly select it from the business requirement for new work.

## Saved native contract

The user-designated reference was read on 2026-11-14. The internally consistent
Category chart supplies this identity-free selected contract:

| Location | Saved selection |
|---|---|
| Visual declaration / native type | `ANALYTICS_PLUS` / `50` |
| `properties.chartType` | `COLUMN_INTEGRATED_VERTICAL` |
| `visualState.hiddenProperties_!!!_template` | JSON string; `id`, `previousId`, `lockedTemplateId` use `COLUMN_INTEGRATED_VERTICAL`; `actualChartType` is `integratedVariance`; renderer/chart type `columnChart`, orientation `vertical` |
| `visualState.hiddenProperties_!!!_measureConfig` | JSON string; visible AC entry uses `chart: integratedVariance`; relative ΔPY% pin is disabled in this reference |
| `visualState.hiddenProperties_!!!_chartsMode` | JSON string; `visualMode` and `prevVisualMode` are `CHART` |
| Assignments | Real category grouping, numeric AC current/comparison result, numeric PY baseline |

The reference's other chart had an integrated top-level chartType while retaining
a groupedBar template/config. Therefore align the top-level type, template and
measure configuration together. The baseline PY assignment remains necessary even
though the integrated renderer config has a visible AC entry instead of separate
AC and PY grouped bars. Do not remove PY or copy the reference's field IDs.

`fixtures/integrated-variance-column.json` contains only the reusable native
selection/template defaults and role configuration. It excludes tenant identities,
source assignments, filters, per-field styling, cached data and credentials.
Do not transplant a full reference visual into another report. Retain target
appearance, variance polarity, null handling, conditional formatting and layout.
The recorded contract is vertical; do not guess a horizontal enum. Use this
vertical integrated chart unless another orientation is explicitly required and
its supported contract has been resolved. More than one baseline, storyboard or
trellis-specific overrides require their own resolved configuration.

## Commands and constructors

For an existing resolved AC/PY chart, create a presentation-only candidate:

```text
python plan.py integrated-variance --input chart-properties.json --out chart-candidate.json
```

The input is the inner native properties object. `apply_integrated_variance`
requires type 50, one numeric AC and one numeric PY, and category grouping. It
preserves assignments, source IDs, measure GUIDs, filter cards, titles, geometry
and every unrelated property. It performs no network or data-column operations.
Its preconditions are construction guards, not runtime validation. Save the
candidate using a fresh visual/entity ETag through the existing properties batch
path. Do not overwrite unrelated Planning owners or user-added sheets.

For new semantic comparisons, `runtime.intelligence.column_chart` accepts the
existing chart spec plus `comparisonField` and optional `comparisonLabel`:

```json
{
  "category": "Region[Name]",
  "field": "Measures[Actual Sales]",
  "valueLabel": "Actual sales",
  "comparisonField": "Measures[Sales Target]",
  "comparisonLabel": "Sales target",
  "label": "Actual sales versus target by region"
}
```

Resolve those illustrative names from the current semantic model. This path
constructs both assignments and applies integrated variance automatically. For
From Sheets or query measures, first use the source-aware binding resolver, then
`runtime.forecast_review.comparison_chart(base, current_assignment, baseline_assignment)`.
That helper now chooses integrated variance by default and reconciles ordinary
filter cards when it changes assignments. `integrated=False` retains the older
base-chart configuration path only for an explicit alternative request; supply an
appropriate base chart, not an already-integrated candidate.

## Preservation and evidence boundary

Keep v13's five Planning column-presentation fixes, numeric input constraints,
Forecast/time-extension rules, native Home, rich headers, source-role colors,
source-aware bindings and leaf-key storage. This chart recipe does not write
inputs, formulas, registered columns or storage mappings. Reference capture and
successful API save receipts do not establish rendered or calculated behavior.
Honor the user's validation instruction and disclose when runtime checks are skipped.
