> v39: Rows/Columns already define storage grain. External Context is only for additional stored selections, never ordinary page/global filtering. Connected Planning owners must match Context; query outputs must retain it. Read [storage-context.md](storage-context.md) for the bundled guards and build-time query evidence.

> v36: [OneLake storage-mode From Sheets and From Queries](onelake-linked-values.md). The bundled resolvers and native recipe phases accept OneLake catalogs without SQL id/sqlPk and retain the Fabric SQL profile. Use current owner/query metadata; no task-local repair.

> v18: [measure-display-defaults.md](measure-display-defaults.md) is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

> v17: New editable inputs explicitly default to ReadAndEdit. Business-dependent
> locking uses BasedOnFormula with a real, resolved expression. See
> [input-editability.md](input-editability.md); preserve intentional existing locks.

> v16: Read [adaptive-business-authoring.md](adaptive-business-authoring.md)
> before choosing features. Interpret business meaning, compose patterns and
> record parameters and dependencies with `plan-intent`. The five cases are examples;
> `usecase --recipe` accepts supported adaptations. Literal search does not choose
> the business design, and no example rate, date, currency or grain is a default.

# Reproduce the five business applications in a fresh session

## Reproducibility contract

Use this guide when a request matches sales targets, workforce merit, expense
budget, rolling forecast/quarterly review or connected currency/risk outlook.
The package contains each original functional prompt, complete symbolic business
spec, post-import dependency graph, styling/defaults and the orchestration that
was previously task-local. No chat history, old report export, local task folder,
source checkout or Codex-specific connector is required.

The intended repeatable output is the same sheets, measures, formulas, grain,
filters, controls, chart comparisons, colors, headers, Home and layout. It is not
byte-identical JSON: new Plan IDs, visual IDs, input IDs, ETags and timestamps must
be newly created/resolved. Current semantic-model data and the installed native
renderer determine values and final rendering. Do not promise pixel-identical
runtime behavior without checking that environment. User-added reference sheets,
manual input values and unrelated later edits are not part of these creation recipes.

The recipes incorporate v12-v14 corrections. Earlier unsupported decimal static
bounds are replaced with hidden formula bounds at the same fractional units;
AverageLeaf inputs default distribution on. The JSON `normalizationNotes` records
these intentional changes rather than reproducing obsolete defects.

## Business request -> complete recipe

| Business request | Case ID | Final structure | Features beyond the common baseline |
|---|---|---|---|
| Start monthly regional sales targets from prior-year sales and flag shortfalls | `01-sales-targets` | 1 Planning sheet, 1 dashboard, 2 comparison charts | Measure-based input default; actual minus target; negative-variance formatting |
| Plan employee merit from 0% to 15% and show salary cost impact | `02-workforce-merit` | 1 Planning sheet, 1 dashboard, 2 comparison charts | AverageLeaf/distribution; fractional percentage formatting; hidden 0.15 limit; salary times employee FX; proposed/base comparison |
| Budget expenses with 3% inflation, adjustments and monthly explanations | `03-expense-budget` | 1 Planning sheet, 1 dashboard, 2 comparison charts | Editable inflation, hidden fractional limit, budget and remaining-budget formulas; LongText explanation; overspend formatting |
| Roll monthly sales forecast into quarterly review and commentary | `04-rolling-review` | 2 Planning sheets, 2 dashboards, 4 comparison charts | Jan-Dec 2026 open period in UTC; `COLUMN.ADDMONTH(-1) * 1.1`; native Forecast; same/subset-grain From Sheets; quarterly variance and LongText commentary |
| Connect local estimates, risk/FX adjustments and a quarterly executive outlook | `05-currency-risk` | 3 Planning sheets, 3 dashboards, 6 comparison charts | Ordered multi-sheet links and dependent formulas; FX multiplier; risk/opportunity inputs; quarterly baseline comparison and commentary |

All five include visible native Home, rich Planning descriptions/legends,
source-role colors, semantic slicers, integrated variance charts, owner-preserving
Planning embeds, current source identities, leaf-ID storage, full grid formatting,
dynamic column expansion, saved hierarchy expansion, column-total handling,
layout sizing and native-measure filter cards.

## Fresh-session commands

Run from the installed `fabric-plan-skill` directory. Requirements are Python 3.11+ and
Node 24+ for the bundled compressed-payload/HTTPS adapters. Use `python` or your
platform's equivalent; set `FABRIC_PLAN_NODE` and, when needed on managed Windows,
`FABRIC_PLAN_HTTP_NODE` to your Node executable. These paths are local prerequisites,
not paths copied from the original author's computer. The HTTP adapter uses
system trusted roots; credentials are environment variables and never files.

```text
python plan.py discover "workforce merit salary cost"
python plan.py usecase list
python plan.py usecase show --case 02-workforce-merit
```

For an authorized destination, copy
`examples/five-usecases/destination.example.json` to `destination.json` and
replace every synthetic identity with current metadata.
It includes the explicit authorized environment/workspace/model/connection
identities used by the five reports, but no token or old Plan IDs. Check that it
is the user's intended destination. Set `FABRIC_TOKEN` securely in the process
environment. A config Boolean is not a substitute for the user's deployment request.
For another destination, resolve its actual endpoints, workspace, model URL and
PowerBIDatasets connection; do not change hostnames by string substitution.

```text
python plan.py usecase model --config destination.json --run runs/model
python plan.py usecase build --case 02-workforce-merit --model runs/model/current-model.json --run runs/merit

```

`model` reads metadata through the public semantic-model API, not model values.
Its selected parser supports normal tab-indented TMDL. These five recipes use
numeric measures; omitted measure return types are represented as Double. For
other return types or TMDL/TMSL branches, supply the complete current catalog in
the format described in runtime-guide.md. The actual connection identity is a
separate required input; it is not inferred from a model's source SQL connection.

`build` compiles the base application locally and records the remaining native
phases. `deploy` creates a new Plan and completes them. It can also compile directly
if build was not run. The default name is the business title plus Unix seconds;
`--name` chooses a different explicit name. Reuse the same run directory to resume.
The saved construction and identity registry must not be rebuilt mid-deployment.

To create all five, invoke deploy once per case with separate run directories:
`runs/sales`, `runs/merit`, `runs/expense`, `runs/rolling`, and `runs/currency`.
The original short prompts are in `examples/five-usecases/business-prompts.txt`.
Do not require a customer to paste a technical specification when these recipes
match the requested outcome. A changed requirement should be reflected in an
explicit adapted spec/graph using the same helpers, not hidden agent assumptions.

## Execution phases that must not be omitted

1. Resolve model fields, numeric units, keys and calendar grain. Compile the base
   definition with Planning owners, registered numeric inputs/formulas/Forecast,
   enabled Home and visible dashboard declarations.
2. Apply the recipe's Planning year filters, percentage formatting and base
   negative-variance rules. Forecast source retains 2025 and 2026 for the previous
   month's actual; the review and other cases select 2026.
3. Create/import once. Save receipts, wait for operation completion and resolve
   current runtime owner/column IDs. Never reuse IDs from another report.
4. Apply page-local embedded geometry, preserving direct owners.
5. Run quarterly or ordered links/formulas/commentary steps. A pending column job
   pauses dependent phases; do not invent a completion or fake chart data.
6. Apply rich headers, source-role colors and all five column-presentation defaults
   after the complete measure catalog exists.
7. Resolve each chart's current and baseline from that catalog. Native DAX measures
   keep PowerBI identity; only produced measures are From Sheets. Select integrated
   variance and reconcile filter cards. Keep business comparison direction.
8. Save native Home content. Dashboard visibility was set at creation.
   Home visibility is already in the imported workload properties.

`runtime.usecases` ships this order. Native mutation routes are application APIs,
not advertised public Fabric REST. Deploy performs required identity/ETag reads;
it does not open a UI, query/calculate values, or run post-save validation.
On uncertain write responses, changed ETags or unresolved job IDs, retain the run
and reconcile before continuing. Do not blindly replay a whole deployment.

## Feature-to-guide-to-command map

| Feature | Guide | Execution used by the recipe |
|---|---|---|
| Complete business flow | This guide | `usecase show/build/deploy`; `runtime.usecases` |
| Exact model and source binding | measure-source-bindings.md | `resolve-measure-binding`; `registered_measure` |
| Inputs, AverageLeaf and whole static bounds | numeric-input-constraints.md | Numeric/Forecast constructors, hidden bound formulas |
| Forecast and time-axis grain | forecast-authoring.md | `construct.planning`; native Forecast records |
| From Sheets, commentary, variance | forecast-review-execution.md | `quarterly_review`; `extend_sheet`; formula/input factories |
| Percentage and matrix styles | matrix-formatting.md | `format-matrix`; `compile_formatting` |
| Negative variance | forecast-review-execution.md | `apply_negative_variance` |
| Leaf identity storage | dimension-leaf-keys.md | `leaf-key-mapping`; constructor key groups |
| Home, headers, source colors and embeds | application-defaults.md; planning-presentation.md; context-intelligence.md | `build_application`; `apply_presentation`; public sheet geometry; Home writer |
| Visible columns and native measure cards | planning-column-presentation.md | `planning-column-presentation` |
| Integrated variance | integrated-variance.md | `comparison_chart`; `integrated-variance` |

## Evidence and completion

`recipe-contract.json` records symbolic dependency and output-shape checks;
`phase-ledger.json` distinguishes constructed base from completed native saves.
`completed.json` exists only after all prescribed save phases return. These are
construction/save records, not proof of rendered behavior or calculated values.
The five portable base builds and symbolic graphs were exercised offline in v15.
The refactored end-to-end runner has not been redeployed from a fresh machine or
independent Copilot session. Keep that limitation explicit.
