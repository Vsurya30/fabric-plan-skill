> v24 non-negotiable baseline: Arial, enabled native Home with saved overview/navigation, and Intelligence dashboard coverage for every Planning sheet apply regardless of prompt context. Read the application defaults guide; use the full application builder and completion gate. A component build or a successful definition save alone is incomplete.

> v19: Every new Planning grid uses explicit row GT Top, row subtotal Top,
> column GT Left, column subtotal null/OFF. Preserve intentional overrides.
> Read the planning totals defaults guide. Measure-based
> roll-forwards recommend Measures in Rows + native Measure Model; discover
> ROLL-FORWARD and read the roll forward authoring guide
> plus the complete supplied formula reference.

> v18: the measure display defaults guide is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

> v17: New editable inputs explicitly default to ReadAndEdit. Business-dependent
> locking uses BasedOnFormula with a real, resolved expression. See
> the input editability guide; preserve intentional existing locks.

# Author from business meaning, not a remembered example

Use this guide for every new application or materially changed request. The five
bundled cases are worked patterns, not an exhaustive menu. Different wording with
the same outcomes should lead to the same design decisions. Changed grain, source,
unit, horizon, calculation or control requirements must change those decisions.

## Interpret, decide, then execute

1. Retain the complete request and break it into business outcomes. Start with row
   grain, then time columns and values. Identify what people edit, what comes from
   the model, what is calculated, who consumes it and what constitutes completion.
2. Resolve the actual model fields and data sources. Business captions are not
   field identities. Establish units, calendar, aggregation and storage identity
   before selecting calculations. Use current metadata, not sample table names.
3. Choose features by the distinctions below. Compose patterns across cases when
   useful; do not choose one case and silently drop the rest of the request.
4. Record each clause's decision, selected guide/command, prerequisites and phase.
   Record where each business parameter came from: user clause, current model,
   documented product default, or an explicitly stated assumption. Unresolved
   source, unit, time-boundary or security semantics are not arbitrary defaults.
5. Execute the graph in dependency order. Resolve source measures before links,
   links before dependent formulas, then charts and formatting. Finish Home and
   dashboard save phases. A base definition alone is not the completed workflow.

Do this reasoning even when `discover` returns no match or the highest-ranked
result looks plausible. `discover` is a literal lookup aid. The authoring agent
interprets language; `plan-intent` records that interpretation and returns routes.
Neither command proves that the agent understood every clause or that an artifact
has been delivered. Compare the ledger with the full request before authoring.

## Defaults versus business parameters

Apply these established defaults unless the user explicitly changes them:

- Visible native Home with a business overview and navigation.
- Rich-text Planning descriptions and a readable source-role legend; distinct
  colors for editable inputs/Forecast, formulas, Power BI and linked measures.
- Intelligence dashboards with a text header, appropriate semantic slicers,
  charts and the original Planning owner embedded below them.
- Integrated variance for bar/column comparisons against a baseline, using real
  current and baseline bindings and an explicit business sign convention.
- Complete typed formatting, current source identities, all five column
  presentation defaults, and grain-derived time metadata.
- Stable leaf-key storage when uniqueness and ancestor dependency are established;
  AverageLeaf input distribution enabled unless disabled; whole-number static
  min/max bounds, using resolved measure bounds for fractional limits.

Do **not** carry over sample dates, growth rates, currency, salary limits, monthly
grain, field names, selected markets, assumptions or sheet counts. In particular,
Jan-Dec 2026, `COLUMN.ADDMONTH(-1) * 1.1`, 3% inflation, a 15% merit cap and USD belong
to particular requests. None is a universal default. Unspecified Forecast open
defaults remain the documented None; do not add 10% growth. A custom name or a
different dashboard count is not a reason to lose mandatory presentation defaults.

Resolve routine presentation choices autonomously. For missing business inputs,
consult the supplied model/context first; ask only for information that materially
changes correctness and cannot be inferred. Continue independent work. A disclosed
assumption is not a substitute for a necessary business or authorization decision.

## Business decision table

| Business distinction | Select | Do not substitute | Guide and execution route |
|---|---|---|---|
| Managers enter an amount, rate or assumption | Typed numeric Data Input; choose unit, default, aggregation and limits | Formula-only values for requested edits | the numeric input constraints guide; `input`, `column-create`, `column-register` |
| A value is derived from other values | Formula with resolved references and correct total behavior | A duplicate editable input or invented DAX | the formula equality guide, FORMULAS; `formula`, create/register phases; F02 |
| Historical periods follow actuals and future periods accept estimates | Native Forecast with requested closure/open policy | Ordinary numeric input merely labelled Forecast | the forecast authoring guide; F09, `forecast`, `forecast-review` |
| Reuse an original semantic-model measure in another view | Its original PowerBI source assignment | A Native companion misclassified as From Sheets | the measure source bindings guide; `resolve-measure-binding` |
| Reuse a produced input/Forecast/formula at the same or compatible coarser grain | Direct From Sheets, with source and target identity/grain resolved | Duplicate inputs or writeback/reimport just to link | no bundled guide here; `forecast-repair` covers a scoped update; F19, `quarterly_review`, `extend_sheet` |
| Join mappings, transform/append sources, or derive a different query output | InfoBridge and its actual query outputs | A direct link that cannot supply the required dimensionality | the infobridge construction guide; F18, bridge source/transform/query/reload/poll/consumer |
| Show performance against a baseline | Integrated variance; keep current/baseline semantics and units | Grouped bars with only comparison assignments | the integrated variance guide; F27, `comparison_chart` |
| Explain each period's number | Text measure at the requested time grain | An outside-axis column if commentary must repeat each period | no bundled guide here; typed LongText input |
| Keep one note alongside a row regardless of period | Supported visual text-column placement | A repeated period input chosen just from the word commentary | no bundled guide here, F05; resolve the placement branch |
| Maintain master records or driver-table rows | PowerTable with source, key and editable columns | A planning measure for record maintenance | the PowerTable modes guide; POWERTABLE |
| Allocate a pool using weights | Allocation rule with target grain and total/missing-weight policy | Numeric parent-to-children distribution toggle | the measure-weighted distribution guide; RULES |
| Explore a temporary what-if versus save separate versions | Sensitivity input versus persisted version Context | Assuming both are the native Scenario lifecycle | the context intelligence guide; SCENARIOS and F08 |
| Require approvals or enforce access | The actual supported workflow/security implementation | Slicers, colors, labels or a Home explanation | F13/F25 contracts; guide-only branches remain explicit gaps |

Check the directory for exact installed guide names and commands; the route output
contains authoritative paths. A route selects what to read and execute, not a
guarantee that every variant has a full constructor. Unsupported requirements stay
in the ledger with their affected downstream outputs. Never invent properties to
make an unsupported branch appear complete.

## Generalize the learning

| Alternative business wording | Reasoned design | What must not be copied from a sample |
|---|---|---|
| "Let managers propose pay rises and show the extra payroll burden." | Workforce inputs plus baseline/proposed/cost formulas and department comparisons | A 15% cap, monthly grain or USD unless supplied |
| "Lock finished periods to sales; let us revise the rest of the outlook." | Native Forecast, actuals-controlled closure and editable open periods | A 2026 horizon or 10% monthly compounding |
| "Use the branch plan in a quarter-end leadership view without rekeying it." | Produced measure From Sheets at compatible quarterly grain; downstream formulas use that link | Rebuilding an independent input or pretending a semantic measure is linked |
| "Show where spending exceeds the envelope and capture an explanation." | Budget/input and expense baseline, deliberate variance sign, unfavorable formatting and correctly placed text | Assuming positive differences are always favorable or always using monthly text |
| "Combine operating estimates with currency drivers and risk adjustments." | Multi-sheet dependency graph; direct links when compatible, InfoBridge when mapping/transformation is needed | Applying SUM indiscriminately to FX rates or using a single old FX value |
| "Plan units sold by quarter next year, rather than revenue by month." | Re-resolve quantity measures, quarterly grain, units and horizon; adapt compatible input/formula patterns | Currency formats, monthly formulas or old time-extension levels |

Mixed requests are normal. For example, a staffing plan with regional cost review
can combine workforce assumptions, connected calculations, quarterly reuse and
variance presentation. Choose each feature for the requirement it serves, not for
the industry name. Different words can express the same workflow; the same word
(forecast, scenario, note, variance) can express different workflows.

## Executable decision ledger

Create a brief using `examples/business-intent/merit-review.json` as the structure.
Its `intent` values are **the agent's semantic decisions**, not user-facing prompt
syntax. Preserve the original clauses and evidence; change all business details.

```text
python plan.py plan-intent --input business-brief.json --out decision-plan.json
```

Route each module id from `decision-plan.json` through the discovery step in the
skill instructions to obtain its guides and operations.

The local command retains every requirement, missing decisions and unknown
branches, checks dependency references/cycles, and returns bundled guides/actions
in dependency order. `readyForAuthoring` only means the selected route details are
present. It does not validate business meaning, data, units or API support. An
unknown intent must be resolved through the complete module directory. Update the
ledger when new evidence changes a decision and carry it through delivery.

For a variation using the shipped five-case pipeline, export an appropriate
recipe, adapt its `spec`, `post` graph and `expected` structure, then use:

```text
python plan.py usecase show --case 01-sales-targets --out adapted-recipe.json
python plan.py usecase build --recipe adapted-recipe.json --model current-model.json --run runs/adapted

```

`--recipe` and `--case` are alternatives. Only deploy writes externally and needs
the user's deployment authorization. This runner supports the base Planning,
Forecast, native linked/formula/commentary and comparison phases described in
the five usecase recipes guide; it is not a generic executor for every module. Its recipe
contract requires explicit comparison, period and complete-default structure for
each owner. Its comparison phase uses one current/baseline pair per owner across
that owner's charts. For different workflows or per-chart comparison pairs,
compose the selected module helpers separately
and preserve the same requirement/phase ledger. Do not force unrelated requirements
into this runner or drop them to pass its contract.

When adapting a recipe, reconcile **all** occurrences: row/column grain, native
sources, storage evidence, time formulas, period filters, slicers, formula symbols,
source/target owners, downstream links, comparison direction, labels, descriptions,
Home text and expected counts. Never reuse run directories or saved registries for
a changed application. Retain the same directory only when resuming the same plan.

`examples/business-intent/quarterly-targets.recipe.json` is a complete adaptation
example with Year/Quarter grain, 2027 selection and independently named owner and
dashboard. Its model fields, currency and horizon are explicit sample choices,
not defaults for other requests. The offline construction is recorded separately
in `adaptive-business-evidence.json`.

Keep delivery evidence precise: selected route, constructed definition, successful
save and rendered/calculated behavior are different claims. Respect a request to
skip runtime validation. The package's offline exercises do not prove fresh-agent
interpretation or native service behavior.
