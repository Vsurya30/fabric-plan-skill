> v20: All reports use content-sized rich-text headers plus a small buffer and
> native row/column hierarchy icons `gmate`, independent of business use case.
> Read [report-presentation-defaults.md](report-presentation-defaults.md) and
> discover REPORT-PRESENTATION. Preserve intentional user overrides.

# Planning presentation defaults

This application default is explicitly required by the user: every Planning
application includes a rich Intelligence dashboard, with a text header, relevant
slicers and charts, then the embedded Planning workbench underneath. The normal
application builder provides one dashboard for each Planning owner. Keep the
standalone owner sheet available. A grid-only application is incomplete unless the
user explicitly requests a different presentation.

## Business request to executable path

| Request | Guide / command |
| --- | --- |
| Replace a generated field-list heading with a description | `present-planning`; native Planning TEXT canvas, HTML and complete geometry |
| Distinguish inputs, formulas and Power BI values | The same command classifies actual measure records and assignments, then writes scoped text colors |
| Create a planning app with an embedded dashboard | `plan.py build` or `provision`; both apply `application_defaults` |
| Confirm every owner has a dashboard | `check-application-presentation` on decoded raw parts; structural and offline |

```text
python plan.py present-planning --input presentation-request.json --out candidate.json
python plan.py check-application-presentation --input raw.json --out presentation-check.json
python plan.py build --model current-model.json --spec application.json --out draft
```

The presentation request contains `properties` (one current Planning owner),
`records` (its current typed measure records, including measureGuid/columnMeta),
`title`, `description`, and optional `palette` and `override_colors`. Candidate
output wraps the native object under `properties`; never save the whole wrapper.
The synthetic example under examples/planning-presentation.request.json is local
only. Use current catalogs and identities for real updates.

## Visible header, not an automatic field inventory

Every Planning sheet gets a distinct business title, description and matching
color legend. Explain what the planner reviews, what can be edited under the
existing rules, and what formulas produce. Describe only configured behavior.
The native default `DEFAULT_TITLE` element containing the `[fields]` mention is
the automatic comma-separated heading; changing a registry label does not replace
it. Do not leave that element as the visible description.

Use `visualState.chartCustomTitle.customTitle` with a real `TEXT` element: local
id, HTML content, numeric top/left, string width/height, and x/y/w/h/i/static grid
layout. The canvas carries elements, layout, layoutType CUSTOM, containerPosition
and numeric containerMeta width/height. Use the documented 64-column / 10px grid.
The writer preserves the existing text element ID and title siblings, explicitly
replaces the description canvas and sets showHeaderFooter true. It does not write
editor/clipboard state or substitute Lexical JSON for Matrix HTML.

Use Arial explicitly for title, description and legend runs. HTML-escape business
text. Calculate wrapped title/body/legend height from current text, font sizes and
width; add max(8px, ceil(8% of content height)), round up to 10px, and synchronize
customTitleHeight, containerMeta.height, element dimension.height and layout.h.
The shared helper has no large fixed minimum. Saved geometry does not prove fit
at every future viewport width. The writer is for an explicit header replacement, not a blind
rewrite of a custom image/chart header. Intelligence BI_TEXT uses the separate
Lexical constructor, with its own supported serialization.

## Consistent semantic measure colors

| Role | Foreground | Light tint for new ordinary measures |
| --- | --- | --- |
| Input / Forecast | Amber #8A5700 | #FFF4D6 |
| Formula | Purple #6B3FA0 | #F2EAFB |
| Power BI | Blue #1F5AA6 | #EAF2FC |
| From Sheets | Teal #176B62 | #E7F4F1 |

Use the same meanings in rich-text legends, grids and dashboard banners. Dark
banner variants use lighter foregrounds from the same color families for contrast.
Classification comes from Power BI/Visual assignments and native measure_type,
including nested VisualColumn Formula/DataInput; never infer kind from a label.
Unresolved types must be resolved before assigning a misleading role color.

The new Planning constructor applies this default palette. Existing reports use
text-only scoped measure operations by default, preserving period fills, locked
cell treatment, number formats and conditional variance indicators. Retain
explicit user colors unless recoloring is requested (`override_colors: true`).
Do not apply blanket fills to Forecast measures: open/closed and lock styles must
retain their meaning. Input color indicates the measure type; it never grants
edit permission. Linked measures are not editable source inputs in the consumer.
Do not change formulas, data values, source IDs, storage mapping, CF or grain.

## Required rich dashboard composition

The normal `plan.py build` and `provision` paths call application_defaults. They
retain explicit dashboard content and selected values, fill missing headers,
slicers and charts, and add a missing workspace for each owner. Controls use real
semantic dimensions; chart defaults use a source measure already requested in the
sheet or an explicitly supplied semantic KPI. Do not pick an arbitrary model
measure, synthesize data, or relabel actuals as plan values. If no supported chart
binding exists, resolve that dependency explicitly; do not claim the grid alone
satisfies the application requirement.

Python callers should use `build_application`; `construct.build` remains a
low-level component assembler for staged work. Run check_application before
claiming a complete application. The check requires a text visual, slicers, a
category chart (a CARD alone is insufficient), and an embed for every owner.
The layout reserves a top header, aligned selection controls and chart row(s),
then a full-width lower planning area. Preserve owner identities and use native
page-local reactiveVisualProperties for placement; never move the source grid.
For existing reports add these pages to a fresh complete baseline, preserving all
unrelated part bytes and stored input records.

Native deployment is staged hidden, then placed, then published. Required current
owner IDs and ETags are construction reads. `deploy_geometry(..., verify=False)`
and `visibility_native(..., verify=False)` support an explicit no-runtime-validation
request: submit using current identities and return receipts without post-save
validation. Default verification behavior is preserved for other callers.
Headers, calculation results, colors, slicer propagation and rendered fit remain
unverified until checked in the native application. API receipts establish saving.


## Required application baseline (v11)

Home is mandatory alongside rich Planning headers, measure colors and embedded
Intelligence dashboards. Read [application-defaults.md](application-defaults.md).
Use `check-application-defaults`; verify Home content, role metadata and workload
visibility separately. Do not silently downgrade a complete application to grids
or dashboards without its native landing page. Retain all source-binding fixes.
