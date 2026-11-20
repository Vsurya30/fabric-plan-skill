> v29 execution rule: follow [verified-authoring-flow.md](verified-authoring-flow.md). Import supported inputs, formulas, Forecast and CF together. Use documented native phases only; no reference-only staging shortcut or automatic reduced-scope deployment. The original request and import-contract checks remain authoritative. This supersedes older partial-deployment fallback wording.

> Direct numeric-column Values (v28): use [numeric-column-values.md](numeric-column-values.md). Planning, KPI cards and charts default semantic Columns to source Sum when no explicit aggregation is supplied. Planning `sourceAggregation` is independent of grid total settings; saved measure IDs are preserved.

> v27 mandatory navigation: every Intelligence dashboard includes a visible native Page Navigator, even when omitted from the prompt. The standard builder reserves space and the native geometry phase saves its complete state. The completion gate rejects missing controls. Read [the navigation contract](navigators.md#mandatory-dashboard-page-navigation-v27). All v26 padding and earlier fixes remain.

> v26 Navigator defaults: [current construction contract](navigators.md#current-construction-contract-v26). New dashboard Navigators include complete DEFAULT icon/text/shape padding even when icons are disabled. Both factories and the create adapter use the shared completion helper; the application-default gate rejects incomplete authored states. Partial state overrides and current/legacy corner profiles remain distinct.

> v19: Every new Planning grid uses explicit row GT Top, row subtotal Top,
> column GT Left, column subtotal null/OFF. Preserve intentional overrides.
> Read [planning-totals-defaults.md](planning-totals-defaults.md). Measure-based
> roll-forwards recommend Measures in Rows + native Measure Model; discover
> ROLL-FORWARD and read [roll-forward-authoring.md](roll-forward-authoring.md)
> plus the complete supplied [formula reference](roll-forward-formula-patterns.md).

> v18: [measure-display-defaults.md](measure-display-defaults.md) is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

> v17: New editable inputs explicitly default to ReadAndEdit. Business-dependent
> locking uses BasedOnFormula with a real, resolved expression. See
> [input-editability.md](input-editability.md); preserve intentional existing locks.

> v14 required default: use native integrated variance for bar/column baseline comparisons. Read [integrated-variance.md](integrated-variance.md) for exact selectors, source-preserving commands and business examples. Ordinary single-series bars are unchanged.

# Required application defaults

The v32 [business navigation contract](business-navigation.md) exposes Home,
Intelligence dashboards with embedded Planning workbenches, and PowerTables.
Underlying Planning sheets are hidden. Initial InfoBridge refresh is optional;
validate wiring and report untested materialization separately.

Arial, enabled native Home, Intelligence coverage for every Planning sheet,
and a visible native Page Navigator on every Intelligence dashboard
are **non-negotiable for every flow and every prompt context**. Screenshots,
reference JSON, a two-sheet request, omitted feature mentions and skipped runtime
validation never opt out. Keep source-role colors and rich headers as well.

Use Arial for all authored text, including effective Matrix per-measure/header
overrides, rich-text CSS, serialized chart text, slicers and native Home text.
Do not carry a different reference font into a newly authored flow.

These are user-required defaults for every new Fabric Plan application, not
optional enhancements that depend on the business prompt mentioning them:

1. Consistent measure role colors: amber Input/Forecast, purple Formula, blue
   Power BI, teal linked data. Resolve actual source types and preserve period,
   lock, conditional-format and edit-permission meaning.
2. A rich-text business description and matching legend for every Planning
   sheet. The generated [fields] list is not an acceptable header.
3. Intelligence dashboard coverage for every Planning owner: meaningful text
   header, real semantic-dimension slicers, relevant category/variance charts,
   and the embedded Planning grid below. Preserve standalone owner identity.
4. A visible native Home landing page with the application's purpose, clear
   instructions for starting the workflow, and available-sheet navigation cards.
5. A native Page Navigator on every Intelligence dashboard, including explicitly
   authored dashboards. Use complete render defaults and all visible normal
   pages, with reserved space above the grid. Buttons/bookmark tabs are different
   controls. Read [navigators.md](navigators.md#mandatory-dashboard-page-navigation-v27).

Do not silently omit any default or call an application complete if a required
phase failed. Native Home is not an ordinary sheet named Home and is not the same
thing as an Intelligence dashboard. Home content, role priority/audience and the
workload-level visibility switch are separate requirements.

## Construct and deploy

`plan.py build` / `build_application` produce these requirements with hidden
underlying Planning owners and dashboard access. The result
includes `home.json`, `homeSpec.json`, and `defaultsCheck.json` in addition to the
existing definition, dashboard and identity files. The generated Plan properties
include `homeLayout.show: true`. Home content is saved through the native Home
provider, not invented inside public definition roles. `provision` always executes
the Home content/visibility phase and records failures as incomplete delivery.

`home_defaults` preserves existing authored Home blocks, fills missing description
and preview-card content, and requires show=true. New baseline content uses the
native __everyone__ layout without changing security or granting access. Preserve
other role layouts, their ordering and audience rules. For an existing application,
use current role metadata/ETags and reuse existing populated content; fill gaps
without replacing unrelated content. A visible Home switch alone is insufficient.

Use flexible Home text widths and content-sized rows; numeric widths are pixels,
not percentages. Read the Home-fit instructions in runtime-guide.md. Do not create
fake images, temporary asset URLs or external links as substitutes for navigation.

```text
python plan.py check-application-defaults --input decoded.json --home home.json --out defaults-check.json
```

This command checks Arial plus all five requirements in the supplied definition/content.
It rejects non-Arial effective formatting overrides, not just the global font.
It also rejects absent or hidden Page Navigators, wrong native kinds, orphan
parts, restricted/empty targets and incomplete render defaults. The native
geometry phase saves the full authored Navigator state alongside its position.
`check-application-presentation` retains its narrower dashboard-coverage meaning.
Low-level `construct.build` is a component assembler; it is not the completion
path for an application. Its evidence explicitly sets `applicationComplete:false`.
Use the normal builder or compose every required phase.

`runtime.application_defaults.require_delivery_phases(authored, home_saved=...,
home_visible=..., dashboard_geometry=..., dashboard_visibility=...)` is the
completion gate. The two dashboard arguments contain the successful saved sheet
GUIDs; the Home arguments reflect successful content/visibility save phases.
Pass real receipts, never optimistic placeholders. The gate reruns the authored
baseline and rejects any missing required phase. Both `provision` and `usecase
deploy` call it; cached builds are checked too. A custom composed workflow must
use the same gate before writing a completed receipt or claiming full delivery.

No skip-Home, skip-dashboard or alternate-font opt-out is part of application
authoring. Keep construction/save status separate from runtime validation. A
scoped repair does not authorize unrelated report changes; report any unmet
application baseline instead of describing the whole flow as complete.

## Validate according to the user's current instruction

Construction guards always apply. When validation is requested:
- Run the relevant offline regressions for defaults, source identity and formatting.
- Read back saved Home content and role metadata, the effective user layout, and
  `planProperties.properties.homeLayout.show`. Verify both content and visibility.
- Check rich descriptions, source-role colors, dashboard component coverage,
  page-local embed geometry, and exact PowerBI/Visual/InfoBridge field identities.
- Check rendering/navigation in an authorized browser when available. Never work
  around a browser access policy. API/static success cannot certify rendered fit,
  formula results, edit behavior or slicer propagation; report that boundary.

When the user explicitly skips validation, preserve that preference: save the
authorized changes and report receipts without runtime/UI/post-save validation.
An earlier skip does not override a later explicit request to validate.
