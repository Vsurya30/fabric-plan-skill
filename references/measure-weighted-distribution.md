# Planning distribution using another measure (v35)

Use this guide when a planner asks for a saved allocation/distribution rule whose
weights come from another measure. **The product supports this configuration.**
The bundled constructor supports the Column profile observed on 2026-11-16 and
the Row / CurrentYear profile saved in the Planning UI on 2026-11-17. Do not describe
all measure-weighted rules as unsupported, or substitute Equal, SelfWeight,
ManualInput, a formula, or the Number input's distribute-to-children toggle.

## Row distribution: current saved Planning example

The Planning sheet's `visualState.data_input_rules` contains
`rule_type.Distribute.operation.Row`, `apply_to_dimensions: "All"`, and:

```json
{"MeasureIdWithReference":{"measure":{"Measure":"<weight measure ID>"},"weights_from":{"Period":"CurrentYear"}}}
```

The selected target remains `measures.SelectedMeasures`. Outer `rows` and
`columns` are `"All"` in this capture. CurrentYear selects the **weight basis**;
it does not express the destination period, eligibility, locks or scenario.
Bind the rule to its Planning owner, not a chart or dashboard visual. An embedded
planning workbench uses that same owner and rule.

Use `measure_weighted_rule(..., axis="Row", weights_period="CurrentYear")`.
The lower-level constructor is `distribute_rows_by_measure(measure_id)`.
[The sanitized fixture](../fixtures/measure-weighted-row-rule.json) preserves
the actual Row structure and uses synthetic IDs. The reference had `forecast`
as the target and `Total Revenue` as the weights. Rebind to the new owner's
business measures; never copy its native IDs or audit identities.

## Column distribution: confirmed UI-to-JSON mapping

| UI choice | Persisted member |
|---|---|
| Rule Type: Distribution Rule | `rule_type.Distribute` |
| Apply Distribution Rule to: Columns | `operation.Column` |
| Apply to Dimensions: All Dimensions | `apply_to_dimensions: "All"` |
| Use Reference From: Measure | `reference.MeasureIdWithReference` |
| Choose Measure: the budget measure | `measure: {"Measure": "<current weight measure ID>"}` |
| Weights from Row: Use Self | No source-row member in this configuration |
| Apply to Measures: selected input measure | `measures.SelectedMeasures` with target IDs |
| Unrestricted outer row/column selectors | `rows: "All"`, `columns: "All"` |

`Use Self` here concerns the source **row**. It does not replace the selected
weighting measure with `SelfMeasure` or change the reference to `SelfWeight`.
No period, source-row or range-operation member was present. Preserve omission;
do not invent explicit null/default members. The screenshot had no assigned
column dimensions, but the persisted operation was still **Column**. Do not
rewrite the axis based on the visible layout or the word "allocation".

Sanitized saved shape: [fixture](../fixtures/measure-weighted-column-rule.json).
The original selected target was `datainputmeasure`; the weighting measure was
`Sum of BD LC Amt`. All user/account metadata and real native identities have
been replaced in the fixture. Its persisted `id` deliberately differs from its
logical `rule_id` to prevent treating those identities as interchangeable.

## Construct from the package

Run the offline example from any directory:

```powershell
python examples/measure-weighted-rules/build.py draft-rule
python plan.py construct-native weighted-rule --input draft-rule/weighted-rule.request.json --out draft-rule/cli.payload.json
```

For a real owner, replace the synthetic IDs using its current construction
identity registry or readback. `measure_ids` maps stable symbolic keys to exact
native IDs; it is not a label search. Resolve the target input and weighting
measure on the same owner, including proper source registration. Direct numeric
semantic Columns retain the existing default-Sum contract. Resolve weights at
the required business grain; no new DAX wrapper is required solely for this rule.

```python
from runtime.rule_factories import measure_weighted_rule
payload = measure_weighted_rule(
    logical_id=logical_rule_id, name="Allocate using budget weights",
    target_measures=["target"], weight_measure="budget", measure_ids=owner_ids,
    axis="Column", rows="All", columns="All")
```

The lower-level helper is `distribute_columns_by_measure(measure_id)`, accepted
by `new_rule` and the existing `construct-native rule` command. The new `weighted-rule`
command resolves symbolic references. Native IDs stay decimal strings, including
values beyond JavaScript's safe integer range. The request supplies logical
`rule_id`; it does not fabricate persisted `id`, timestamps or user audit fields.

## Persist and verify through the established flow

These are **Planning** input rules. Persist them on the actual type-80 owner;
an Intelligence page embeds that owner and must not receive an independent copy.

Two distinct routes are available:
1. The verified engine New route via \`builder-api rule-create\`, when its mount
   and authorization have actually been resolved. Do not guess an engine URL.
2. The saved Planning-state route through the existing full visual-properties
   batch writer. \`runtime.planning_rule_state.save_rule\` accepts the actual
   native entity/owner IDs, a validated New payload, and a fresh authored record
   ID. It writes a complete \`data_input_rules\` record, preserves other properties,
   uses fresh ETags, and checks exact saved state. Native page responses put
   \`visualType\` on the visual envelope, not inside its properties. The helper
   verifies that this is an owned Planning visual and rejects embedded proxies.

Example after resolving the current owner and symbolic measure IDs:

\`\`\`python
from runtime.planning_rule_state import save_rule
result = save_rule(native_client, entity_id, owner_visual_id, payload,
                   fresh_record_id, "save-planning-allocation")
\`\`\`

The second route was exercised on three newly constructed Planning owners:
salary by pay basis, expense by eligibility, and quantity by eligibility.
Each was saved and read back with its requested Row/Measure/CurrentYear rule.
This proves configuration persistence only. Record IDs in this route are fresh
authoring IDs; do not call them engine-issued, reuse reference IDs, or copy audit
users/timestamps. A New-operation envelope itself is not a saved record.

Keep the existing complete base import: supported inputs, formulas, Forecast and
CF together. Do not strip them and create reference-only sheets for this phase.
Do not add unconsumed `allocationRules` fields to a base spec and call that done.
Record each required rule in the execution ledger until it has been saved and
read back. A constructed payload alone is not a deployed allocation rule.

After saving, obtain the current native `visualState.data_input_rules` or the
unwrapped verified engine catalog. Use
`verify_saved_rule(payload, saved_rules)` to match the logical rule ID and compare
name, type/reference, target selectors, row/column selectors and enabled state.
The result separately returns the actual persisted ID. A mismatch or duplicate
logical ID fails the check; unrelated rules and server audit metadata are kept.

## Connected Planning acceptance boundaries

For a Connected Planning application, select monthly base salary
or the appropriate expense/quantity eligibility measure as required by the
business rule. Select Row for allocation across employees or other row members.
The captured CurrentYear weight period must match the intended weight basis;
do not claim it means each destination month's weights independently.

- Additional Row weight periods/ranges, selected-dimension Column branches,
  explicit source rows/periods and range operations need their own exact contracts.
  Their rejection in this narrow helper is a package boundary, not a product limitation.
- Existing resolved `Selected` outer row/column selectors are retained. A requested
  period/scenario scope must never silently become `All`; arbitrary period-range
  syntax is not implemented by this example.
- Validate actual redistribution, trigger behavior, period/scenario isolation,
  eligibility, locked-target handling, zero/missing/negative weights, rounding and
  total preservation at runtime. These are not established by saved JSON. The
  helper passes a measure identity; it does not apply the ManualInput branch's
  nonnegative-weight policy to source measure values.
- Restorable bookmarks are separate and optional. Do not add them to a task
  that does not request them or retain them after the user removes them.

Evidence: [capture comparison](measure-weighted-distribution-evidence.json).
The reference Plan was read only; no allocation was executed or live report changed.
