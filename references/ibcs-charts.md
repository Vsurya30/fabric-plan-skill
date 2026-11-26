# IBCS charts and dashboards

Use this guide when a dashboard needs IBCS content:

- a named chart recipe (C01–C13), a stacked or 100% stacked chart, a waterfall, or an overlapped actual-versus-reference comparison;
- a Matrix table in place of the embedded Planning grid;
- a message title and footnotes;
- the IBCS Plan theme.

The builder writes chart templates, field bindings, the Matrix, story text and, when asked, the Plan theme. The IBCS styling of each chart is a separate concern; see [The IBCS look](#the-ibcs-look).

## Contents

- [Request shape](#request-shape)
- [Recipe catalog](#recipe-catalog)
- [Template rules the builder enforces](#template-rules-the-builder-enforces)
- [What the definition carries](#what-the-definition-carries)
- [IBCS dashboard page](#ibcs-dashboard-page)
- [Plan theme](#plan-theme)
- [The IBCS look](#the-ibcs-look)
- [Check and report](#check-and-report)

## Request shape

Add the chart to a dashboard's `charts` list. A chart that names `recipe` or `chartType` is built by `runtime/ibcs_charts.py`. Any other chart stays a plain column chart, or an integrated variance chart when it has `comparisonField`.

```json
{
  "label": "Sales by region",
  "recipe": "C01",
  "category": "Geo[Region]",
  "stack": "Product[Segment]",
  "measures": {
    "AC": "Facts[Sales]",
    "PL": {"field": "Facts[Plan]", "label": "Plan"},
    "FC": {"field": "Facts[Forecast]", "aggregation": "sum", "label": "Forecast"}
  }
}
```

- `category` is a model dimension and goes in the `axis` bucket. It is required.
- `stack` is a second dimension. Use it only where the template has a stack bucket.
- `measures` is keyed by bucket. **AC** holds the actual. **PY**, **PL** and **FC** hold the comparisons: prior year, plan and forecast.
- A measure value is a field ID, or an object with `field` plus optional `aggregation` and `label`. On LINE and AREA, AC also accepts a list of fields.
- Fields come from the current model or a registered query output. Never derive them from labels or from example names.
- `recipe` alone selects the recipe's default template. Give `chartType` as well only to pick one of the recipe's alternatives (C08 mixed uses AREA). `chartType` without `recipe` builds that template with its own rules.
- Unknown options are refused, including styling keys such as `theme`.

## Recipe catalog

| Code | Recipe | `chartType` | Required bindings |
|---|---|---|---|
| C01 | Stacked Column | `STACKED_COLUMN_VERTICAL` | axis, AC, PL, FC, stack |
| C02 | Stacked Bar | `STACKED_COLUMN_HORIZONTAL` | axis, AC, stack |
| C03 | Overlapped Column | `COLUMN_VERTICAL` | axis, AC, PY, FC |
| C04 | Overlapped Bar | `COLUMN_HORIZONTAL` | axis, AC, PL |
| C05 | Waterfall + Column | `COLUMN_WATERFALL_VERTICAL` | axis, AC, PY |
| C06 | Waterfall + Bar | `COLUMN_WATERFALL_HORIZONTAL` | axis, AC, PY |
| C07 | Line | `LINE` | axis, AC |
| C08 | Stacked Area | `STACKED_AREA`; mixed variant `AREA` | axis, AC, stack; mixed: axis, AC (one or more) |
| C09 | Scatter | `SCATTER_PLOT` | axis, AC (x), PY (y) |
| C10 | Bubble | `BUBBLE_PLOT` | axis, AC (x), PY (y), PL (size) |
| C12 | Side-by-Side Waterfall | `SIDE_BY_SIDE_WATERFALL` | one axis field, AC, PY |
| C13 | Overlapped Column, date/forecast | `COLUMN_VERTICAL` | axis, AC |

C07 and C13 assume a date axis. The builder does not check the axis data type, so choose the period field yourself.

The catalog has no C11. An unknown code is refused: find out which chart the user means instead of guessing an alias. `runtime.ibcs_charts.recipes()` returns this table, and `required_buckets(code, chartType)` returns the required bindings.

Bucket names are chart roles, not business periods. In C09 and C10, PY and PL hold the y coordinate and the bubble size, not a prior year or a plan. Bind the measures the user names for each role. If a required binding cannot be resolved from the model, name it and ask; do not substitute a similar field.

## Template rules the builder enforces

- The AC, PY, PL and FC buckets each take one field. The exception is AC on LINE and AREA, which takes up to 27.
- Scatter has only AC and PY, and both are required. Bubble has AC, PY and PL, and all three are required.
- Stacked and 100% stacked charts (column or bar) need either a stack dimension or measures in at least two buckets. With two or more measures and no stack, the chart stacks the measures. With one measure and no stack, the chart renders as a plain column or bar, so the builder refuses that combination. The native stacked area always needs a stack.
- Waterfalls and the side-by-side waterfall compare at least two measures in different buckets. The side-by-side waterfall takes a single axis field.
- The category and the stack must be different dimensions. A semantic measure cannot be a dimension. The same value cannot be bound to two buckets.
- Small multiples (row and column trellis), tooltip measures and text categories are not built here.

## What the definition carries

Each chart is an `ANALYTICS_PLUS` visual (type 50). It carries:

- the template in two places, top-level `chartType` and `visualState.chartType`, with the same value;
- pivot assignments with `bucketId` set to the bucket name: `axis`, `stack`, `AC`, `PY`, `PL` or `FC`;
- one ordinary visual-level filter card for each assigned field. Two parts of these cards are not yet confirmed from an export:
  - The stack's card follows the same rule as the category's.
  - A comparison measure's card registers under bucket `AC`, with the real bucket kept on its nested assignment. This was observed for PY and is applied to PL and FC as well.

Fabric saves the same template selectors and assignments when a chart is added. The chart then writes its own template state on first render. **Do not pre-write** template, measure configuration, column-field or comparison mappings. **Do not add title settings.** IBCS charts keep the title the chart produces, and an explicit title belongs to a separate, user-requested edit.

Fabric loads a chart with no saved `chartType` as `COLUMN_VERTICAL`. The plain column chart now names that template explicitly, which changes nothing at runtime but keeps its buckets checked against a known template. Each template has its own bucket names, and a field in a bucket the template lacks binds nothing. Charts from earlier builds of this package keep their category in the generic `category` bucket, so they show values without categories. To restore the category, move it to `axis` together with its filter cards.

## IBCS dashboard page

Two optional dashboard keys turn a workspace into an IBCS page. Both are built by `runtime/ibcs_report.py`.

```json
{
  "table": {"label": "Sales detail", "rows": ["Geo[Region]"], "columns": ["Period[Month]"],
            "measures": {"AC": "Facts[Sales]", "PL": {"field": "Facts[Plan]", "label": "Plan"}}},
  "ibcs": {"message": "Sales 5% above plan, driven by EMEA", "subtitle": "Sales in EUR m",
           "detail": "FY2026, AC vs PL", "footnotes": ["AC = actual, PL = plan"]}
}
```

**`table` adds a Matrix.** The Matrix is an `INFORIVER` visual (type 10), and it takes the grid slot in place of the embedded Planning grid.

- `rows` takes one or more dimensions. `columns` takes zero or more.
- AC goes in `ameasure`; it takes one or more measures. PY, PL and FC go in `pymeasure`, `plmeasure` and `fcmeasure`, and each takes one.
- The definition spells the type exactly `INFORIVER`. A misspelled type imports as a Planning visual.
- The Matrix reads model or registered query values. It does not show the Planning grid's input cells or unsaved values.
- When no other dashboard embeds the Planning owner, the owner's own Planning page stays visible, so users enter values there. The coverage check reports this case as `inputOnVisiblePlanningPage`.
- The note slot captions the Matrix with the table label, unless `note` or footnotes are given.
- The Matrix gets no visual-level filter cards. Slicer selections are not saved into its state either; that behavior has not been confirmed for a Matrix.

**`ibcs` adds the story.**

- `message` is required: the one statement the page should convey.
- On a Matrix page, the message title replaces the workspace banner. It follows Fabric's own IBCS report title: the message in bold 18px, then `subtitle` at 13px and `detail` at 11px. The text uses Arial, and its color is left to the theme.
- On a page that still embeds the Planning grid, the message heads the dark workspace banner instead. The banner keeps the role-color key, because the grid's input, Power BI, formula and From Sheets colors still need it.
- `footnotes` takes a list of lines. Each becomes an 11px paragraph in the note slot. In the left-rail and stacked layouts that slot moves to the bottom of the page and grows with the number of lines. A custom layout places the note rectangle itself.
- Footnotes and `note` share one slot, so give only one of them.
- Threaded comments, and notes anchored to data cells or chart points, cannot be authored through a definition. Report them as unavailable.

## Plan theme

`planProperties.json` `properties.theme.type` selects the Plan theme; type 5 is IBCS.

- **New Plan.** Add a top-level `"theme": "ibcs"` to the build spec. The provisioning capability is `plan.theme`; the Matrix capability is `intelligence.matrix`.
- **Existing Plan.** Call `runtime.ibcs_report.set_plan_theme(planProperties, "ibcs")` on the freshly exported part. It changes `type` and keeps every other member of the theme object.

The theme applies to the whole Plan. Set it only when the user explicitly asks for an IBCS Plan theme; asking for IBCS charts is not enough. Product code shows these effects:

- Matrix and Table visuals re-apply the Plan theme each time they load.
- Planning grids follow the Plan theme only when the tenant has Plan themes enabled for Planning.
- On load, a chart changes only the settings still at the previous theme's values. A sheet the Plan has not themed before has no previous value to compare against, and a chart whose theme was customized keeps its own. So a newly authored chart does not reliably become IBCS.

A readback of the definition proves only that the value was saved. It does not prove what any visual renders.

## The IBCS look

Each recipe pairs its template with styling: the IBCS theme, data labels, measure fill patterns, ranking, deviation callouts and number format. **The builder does not write that styling.**

- **Theme state.** When the chart's theme changes, the chart recomputes many saved settings at once. Writing the theme name alone would leave those settings at the previous theme's values, so the result is a mixed look rather than IBCS.
- **AI chart state.** The in-product AI chart state is applied by the running chart in the session that sets it. Fabric does not read it back from a saved definition.
- **Settings with no saved-definition route.** Measure styles, top-N ranking, deviation callouts, number format, forecast population, axis breaks, reference bands, bubble sizes, group colors, series labels, and line and sorting options have no saved-definition route in the current product.

Report these as **not applied**, and name them per chart. The user can apply them in the product. Or the user can export a Plan with a chart already styled in the product, so that its saved state can be reused as observed state for the same template.

## Check and report

1. Before the build, confirm that every required binding resolves to a current model or query field.
2. After building, `runtime.ibcs_charts.describe(properties)` lists the template, the matching recipes, the bucket bindings and whether the two template selectors agree. `runtime.chart_filters.audit_chart_filters(properties)` checks the filter cards.
3. After an authorized update, export the Plan and compare it with what was built:
   - each chart's two `chartType` values;
   - the assignments of each chart and Matrix, by field ID and bucket;
   - the Plan theme `type`.
4. Report outcomes separately:
   - templates, bindings, the Matrix, story text and the theme value as saved;
   - IBCS chart styling as not applied;
   - rendering as not tested.
