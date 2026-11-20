# Allow Input defaults and conditional editing

For **new editable Data Input and Forecast measures**, explicitly emit
`"allow_input": "ReadAndEdit"`, corresponding to **In both Read and Edit mode**.
This applies to **every Data Input type**: Number, Simulate, Text (short and long),
Checkbox, Person, List (single and multi select), and Date. It also applies to
commentary and supported visual-column placement of these inputs. Forecast uses
the same default in its edit configuration. Do not omit the property: the inspected native enum defaults to `Edit`
when omitted. That native default is a source fact, not the skill's authoring
default. Explicitly requested edit-only input may still use `"Edit"`.

When the business asks for conditional lock/unlock, approval/status gating,
eligibility or another expression-controlled edit rule, use **Allow Input based
on formula**, with a real expression:

```json
{"allow_input": {"BasedOnFormula": "${eligible} > 0"}}
```

`eligible` must resolve to an actual policy measure for the current cell grain.
If multiple conditions apply, resolve the business eligibility logic at that
grain and write the corresponding expression using supported formula functions.
The example above is a symbolic spec, not a deployed expression. Constructors resolve these
symbols to current native `M_<id>` references. Use the installed formula contract
for operators/types; never deploy placeholders, labels as IDs, copied old IDs or
an invented policy field. If a required business condition cannot be resolved,
keep it unresolved rather than replacing it with unrestricted ReadAndEdit. A
predicate states when input is permitted: true allows input, false prevents it.
The input rule does not grant access, override independent permissions or reopen
Forecast closed periods. Defaults, on-change actions and conditional formatting
serve different purposes and do not replace this gate.

## Correct property owner and construction route

| Owner | Native path | Authoring route |
|---|---|---|
| Ordinary input | `columnMeta.measure_type.DataInput.allow_input` | `construct.planning` numeric spec or `input_create(..., allow_input=...)` |
| Visual-column input | `columnMeta.measure_type.VisualColumn.DataInput.allow_input` | `input_create(..., visual_column=True, allow_input=...)` |
| Forecast | `columnMeta.measure_type.Forecast.edit_config.allow_input` | Forecast spec `allow_input`, resolved by `forecast_config` |

The reusable `runtime.input_policy.allow_input` enforces the union, nonempty
formula and resolvable symbolic/native references. Forecast eligibility symbols
also join the construction dependency graph. These offline checks do not compile
or evaluate the expression in the native engine.

For a new Forecast derived from a reference, do not inherit the reference's
incidental Edit mode. Set the requested policy explicitly, otherwise ReadAndEdit.
A reference with formula gating requires an explicit remapped policy; do not copy
its old IDs or silently erase the condition. For a repair of an existing report,
preserve its intentional mode/formula and other locks unless that change is
authorized. This default update is not a blanket unlock or data migration.

## Discover by business meaning

Requests such as "only let me edit an open period", "lock after submission",
"reopen when returned" or "allow eligible products only" route to **F30** and the
`conditional-input` intent in `plan-intent`. Resolve the target, condition, actual
expression and row/column/context scope. Read the F30 business guide for policy
and state dependencies. A full approval lifecycle may need additional modules;
do not infer that the allow-input formula implements those transitions.

```text
python plan.py discover --module F30
python plan.py plan-intent --input business-brief.json --out decision-plan.json
```

Keep the user-facing request functional. The agent selects this setting and writes
the expression; the user need not supply JSON or enum names. Honor explicit
validation instructions and distinguish a constructed/saved rule from proven
editing behavior.
