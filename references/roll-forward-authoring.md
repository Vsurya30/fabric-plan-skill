> v20: All reports use content-sized rich-text headers plus a small buffer and

Current authoring rules: read [forecast-time-intelligence.md](forecast-time-intelligence.md)
for non-composite calendar axes, one-time Visual Columns and shared versus local
as-of controls. Read [formula-equality.md](formula-equality.md): native comparisons
use `==`; single `=` is reserved for variable declarations. These rules supersede
older comparison examples; original supplied documents remain preserved.

> native row/column hierarchy icons `gmate`, independent of business use case.
> Read [report-presentation-defaults.md](report-presentation-defaults.md) and
> discover REPORT-PRESENTATION. Preserve intentional user overrides.

# Roll-forward authoring

Read this guide when a balance carries between periods, even if the prompt never
says "roll-forward". Then read the shared modeling/formula sections and the entire
matched case in [the complete supplied reference](roll-forward-formula-patterns.md).
That file is preserved byte-for-byte, including every formula, worked grid,
source link, assumption, caveat and validation scenario. This guide supplements
it with native presentation contracts and executable routing; it does not replace it.

## Discover by business outcome

```text
python plan.py discover "cash runway and funding shortfall"
python plan.py discover "stock depletion and replenishment"
python plan.py discover "invoice cohorts and collections timing"
python plan.py discover "staffing exits depend on opening headcount"
python plan.py discover "unearned revenue recognition and cancellations"
python plan.py discover --module ROLL-FORWARD
python plan.py reference roll-forward-formula-patterns.md --list
```

| Business meaning / alternate wording | Read entire source heading | Preserve this distinction |
|---|---|---|
| Liquidity, cash runway, bank funding, weekly cash bridge | 1. Treasury cash flow forecast | Company × bank account × week; reconciled prior close, funding gap before draw, internal transfers cancel |
| Stock depletion, supply coverage, reorder, inventory bridge | 2. Inventory and replenishment forecast | SKU × warehouse × month; negative projected net inventory carries shortage; future two-month suggestion is advisory |
| Debtors, invoice cohorts, collection lag, working capital | 3. Accounts receivable and collections forecast | Company × customer segment × month; previous invoice month's rate and sales cohort, plus prior closing balance |
| Staffing, hires/leavers, attrition, filled positions | 4. Headcount and hiring forecast | Department × location × month; exits depend on opening headcount, round movement at business grain |
| Unearned revenue, prepaid contracts, liability release | 5. Deferred revenue forecast | Legal entity × contract cohort × month; independent recognition schedule, cancellations and negative-cohort flags |

Forecast horizon extension alone routes to F09. A balance bridge routes here,
usually composed with F09 (closed/open forecast), F05 (inputs), FORMULAS/F02
(calculation and aggregation), F12 (Measure Model), F01 (layout/totals), and
INTELLIGENCE (dashboard). A new domain with the same opening + movements = closing
semantics reuses the pattern, not another case's entities, currency or dates.

`plan-intent` accepts `balance-roll-forward` alongside other business outcomes.
Record grain, calendar, unit, seedAuthority, movements, signConvention,
forecastCutoff, editableFields, dependencyStrategy and aggregation in its details.
Unresolved bindings stay unresolved; do not invent bank accounts, weekly calendars,
cohorts or source measures. Illustrative model additions require user authorization
and clear labels. The source's worked values are fixtures, not business defaults.

## Model and formula decision path

1. Establish entity grain, ordered continuous business calendar, scenario, stock
   unit, prior-actual seed authority and first visible/first open buckets. Weekly,
   monthly and fiscal periods need their own confirmed calendar operations. A
   relative offset is a position, not automatically a calendar month.
2. Bind actuals with exact current PowerBI identities; inputs represent decisions,
   Forecast series represent closed actuals plus editable open baselines, formulas
   calculate the bridge. From Sheets/InfoBridge must use their real typed output
   IDs. Keep semantic dimensions in Rows/Columns and preserve leaf storage IDs.
3. Define signs (subtract positive outflows; allow signed adjustments explicitly),
   zero/blank/missing-value policies, prefill timing and repeat-fill treatment of
   planner overrides. New data inputs and Forecast use ReadAndEdit unless an
   explicit policy or real BasedOnFormula lock applies. Static min/max bounds are
   integers; never silently round fractional limits or change percentage units.
4. Resolve all references against current identities. The source uses readable
   labels; convert to the target formula contract, with correctly quoted symbols
   and variables. Grand-total column and measure IDs are independently resolved.
   Do not copy example IDs or assume another formula surface accepts these tokens.
5. Choose recurrence or the independent cumulative alternative below. Keep forward
   suggestions separate from actions that write receipt, funding or hiring inputs.
6. Set entity/time aggregation independently. Flow Sum, opening First and closing
   Last over time; entity balances add only at the same date in compatible units.
   Reconciliation is closing - opening - net movement at leaf; time totals need
   first opening, last closing and summed movement. Do not sum every opening or
   closing; hierarchy nesting does not supply these calculations.

### Temporal dependency and construction limits

The intended chain is Closing(t-1) → Opening(t) → Closing(t). Resolve its measure
identities jointly, then use the supported target authoring/parser path. A draw
feeding current closing must use Cash Before Draw to avoid a same-period cycle.
IFNA seed fallback handles an expected missing predecessor, not every blank or an
unexpected later gap. Use explicit first-period logic where needed. Mixed history
uses authoritative actual closes in closed periods and resets the next opening
when a forecast period closes; a first-visible seed may be needed outside history.

The bundled generic `build` has a measure-level acyclic dependency guard. It does
not prove or accept a temporal recurrence merely because `.RELATIVE(-1)` appears.
Do not disable the guard, strip dependencies or substitute a fake seed to claim
success. For a target-supported recurrence, use the confirmed native joint/batch
reference path with all identities registered; create drafts only within the
authorized workflow, and do not leave placeholders in a finished artifact. If the
available path cannot author the recurrence, state that specific limit and choose
a supported equivalent only when business semantics permit it.

The source cumulative formula is equivalent only for independent additive
movements, one properly anchored seed, and no recursive rounding/nonlinear cap.
Cash with manual draws, inventory with independent receipts, AR without a cap,
and independent deferral schedules can qualify. Mixed history needs explicit
forecast-start selections and actual branches. Headcount attrition based on opening
does **not** qualify; use recurrence or a supported sequential upstream schedule.
Independent forecast exits are a changed business rule, requiring the user's choice.

## Formula-pattern index

All exact expressions and qualifications are in source section **2. Formula
patterns for the skill**, not inferred from these short labels:

| Need | Source pattern / caveat |
|---|---|
| Previous / next bucket | `.RELATIVE(-1)` / `.RELATIVE(1)`; end-of-horizon policy; reading future values does not schedule receipts |
| Cumulative / first N positions | `SELECT.BYINDEX`, `LEAF_INDEX`, applicable column count; confirm token, base index, group reset and hidden/reordered periods |
| First date / full displayed horizon | `SELECT.BYDATE`, MINDATE/MAXDATE; horizon filters change endpoints |
| Rolling calendar window | ADDMONTHS/COLUMN.CURRENT_PERIOD; -1 through +5 inclusive is seven months; do not use month shifts for weeks |
| Window statistics | AVERAGE/MIN/MAX over selections with empty-range policy |
| Stored Grand Total | `CR_<column-id>.M_<measure-id>`; read configured total vs explicit business range |
| Precision / pack multiples | ROUND and CEILING; positive pack size, movement rounding before balance only when required |
| Array variables / filtered diagnostics | SELECT array → FILTERIF → COUNTIF guard → rounded average; 80,0,100 yields 90.0 only under this zero-exclusion policy |
| Date variables | fromDate/throughDate before SELECT.BYDATE; keep target variable declaration/serialization rules |
| Conditional value / editable initialization | IF calculation vs Forecast prefill; no invented FILL signature or unscoped overwrite action |

## Measures in Rows and a logical Measure Model

**Recommend this whenever roll-forward metrics are separate measures.** Put time
on columns and measures on rows, ordered Opening → movements → Closing → decision
outputs → Reconciliation. Use the native Measure Model to nest drivers beneath
the measure they explain. Keep opening, key movements and closing visible together.
If the model already represents metrics as dimension members, or the user chooses
another layout, adapt rather than adding a redundant measure hierarchy.

Native properties:

```json
{
  "layout": {"layout_type":"Hierarchy", "measure_layout":"Rows"},
  "measure_tree": [
    {"id":"<resolved-parent-id>","level":0,"meta":{"hide_in":null,"node_type":{"Measure":{"aggregation":null}},"rules":null}},
    {"id":"<resolved-child-id>","level":1,"meta":{"hide_in":null,"node_type":{"Measure":{"aggregation":null}},"rules":null}}
  ]
}
```

`measure_tree`, not legacy `measureModelConfig`, stores this tree. Preorder starts
at level 0 and increases by at most one. Cover every visible measure once, preserve
hidden helpers and current node metadata, and resolve current IDs. Align
`manage_measures[].order`; expand parent nodes in `measure_tree_node_expand_state`.
Disable ragged hierarchy for Measures in Rows. Keep business formulas, actuals,
Forecast/input definitions, allow-input rules, source types, storage mappings,
filters, per-axis aggregation and source-role colors intact. Nested parent labels
are explanatory organization, not an instruction to sum children or double-count
a formula. Retain explicit summary arithmetic and aggregation. Emphasize summary
rows through the existing formatting helper when desired; choose width for content.

Adapt these arrangements to resolved measures; add actuals/other requested metrics
without hiding them merely to fit a template:

| Case | Parent → logical children; root sequence |
|---|---|
| Cash | Opening Cash → seed; Net Cash Movement → receipts, operating payments, capex, draw; Closing Cash; Funding Gap → floor, Cash Before Draw; Reconciliation |
| Inventory | Opening Inventory → seed; Net Inventory Movement → receipts, receipt adjustment, demand; Closing Inventory; Shortage; Coverage Buy → safety stock, pack size; Reconciliation |
| AR | Opening AR → seed; Net AR Movement → credit sales, Planned Collections → same-month rate and extra collections, writeoffs; Closing AR → actual closing AR; Reconciliation |
| Headcount | Opening Headcount → seed; Net Headcount Movement → starts, transfers in/out, Expected Exits → attrition rate; Closing Headcount; Reconciliation |
| Deferred revenue | Opening Deferred Revenue → seed; Net Deferral Movement → new deferrals, recognition, credits; Closing Deferred Revenue; Horizon Recognition; Reconciliation |

All new grids use [the four totals defaults](planning-totals-defaults.md), also in
their owner-preserving dashboard embed. Retain the established rich business
header/legend, measure colors, native Home, dimension slicers, integrated variance
for meaningful same-unit baseline comparisons, and numeric Auto formatting.
Assigned measure filter cards stay visible at All; requested dimension selections
belong only to their dimension cards.

### Executable presentation helpers

```text
python plan.py roll-forward-presentation --input examples/roll-forward-presentation.request.json --out candidate.json
python plan.py planning-totals --input examples/planning-totals.request.json --out totals-candidate.json
```

The first request contains current `properties` and `hierarchy: [{"id": "...",
"level": 0}, ...]`; optional `totals` (default true), `reset_totals` (false) and
`label_width`. Current IDs must be strings. No label guessing, source remapping,
arithmetic alteration or live write occurs. Hidden measures retain registration.
`reset_totals` is only for an explicitly requested reset, not an unrelated update.
In a new `build` sheet spec, use `measureHierarchy: [{"measure":"symbolicKey",
"level":0}, ...]`; the constructor resolves IDs before arranging the hierarchy.
This presentation option does not bypass formula dependency restrictions.

## Acceptance fixtures and honest validation boundaries

Read every worked grid and following paragraph in the complete source. Key
checkpoints help locate those detailed cases; they do not replace them:

| Case | Worked checkpoints and required variation |
|---|---|
| Cash | Closes 530,470,530; week 2 before draw 370, gap 80; remove draw → close 370 and next opening 370; transfers cancel at company |
| Inventory | Closes 80,10,-80; shortage 80; April two-month gap 100 rounds to buy 108 in packs of 12; incomplete later windows blank; approval writes arrival date without duplicate receipts |
| AR | Closes 225,243,211; June collections 64 current +108 previous +10 extra; July June-cohort remainder 96; previous cohort rate changes timing; missing lookback needs governed carry-in |
| Headcount | Closes 53,51,54; August exits ROUND(53×6%)=3; zero July starts → next opening 49 and exits use 49; FTE precision is a distinct policy |
| Deferred revenue | Closes 320,285,305; quarter opening 300, recognition 250, closing 305; negative cohorts and cancellation impact on remaining schedule |

Source section **4. Instructions to add to the authoring skill** supplies the full
validation scenarios: first seed, next two openings, edit propagation, actual/open
rollover, year boundary, endpoints, time subtotal, explicit zero, blank,
out-of-horizon read, repeat prefill preserving overrides, newly opened period and
saved/refreshed writeback when requested. Start with one entity and three periods,
then two entities and totals. Do not claim these checks ran from reading the source
or passing local presentation tests. Follow the current user instruction: when
runtime validation is skipped, save authorized changes and state that boundary.
