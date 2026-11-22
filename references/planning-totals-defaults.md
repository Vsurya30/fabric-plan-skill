# Planning totals defaults

Use for every new Planning grid, including standalone and dashboard-embedded
owners, regardless of business case. A user can change these defaults. Preserve
explicit existing choices during unrelated repairs. These are Matrix properties;
do not copy them to chart or PowerTable state.

| Control | Default | Native `visualState.totals_config` property |
|---|---|---|
| Row Grand Total | ON, Top | `row_grand_total: "Top"` |
| Row Subtotal | ON, Top | `row_sub_total: "Top"` |
| Column Grand Total | ON, Left | `column_grand_total: "Left"` |
| Column Subtotal | OFF | `column_sub_total: null` |

These values were observed in the user-saved Treasury reference before applying
them to the roll-forward reports. OFF is JSON null, not false, zero or "Off".
Omitted positions invoke native behavior and are not a reliable authored default.
Allowed alternate row positions are Bottom (and Split for row subtotal); column
positions are Left/Right. Retain `freeze_total` and unrelated settings. New
construction keeps `freeze_total: false`; this is separate from total visibility.

The native totals updater is not a general sparse merge: omitted position fields
can clear positions. Merge against current state and submit the complete four
positions with preserved related settings through the existing supported adapter.
Do not overwrite intentionally configured views/bookmarks as an incidental repair.

## Local commands and overrides

```text
python plan.py planning-totals --input examples/planning-totals.request.json --out candidate.json
```

Input is `{"properties": <current Planning properties>, "reset": false}`.
`runtime.roll_forward.apply_totals_defaults` returns a copy, fills only absent
positions, validates native enum values, and preserves explicit null/positions.
`reset: true` replaces the four positions only when the user requests that reset.
`construct.planning` starts all new sheets with the four defaults; a partial
`totals_config` spec overrides only supplied positions. `columnPresentation:
"preserve"` preserves expansion but does not disable totals defaults for new grids.

An embed uses its Planning owner; update that owner once. Measures-in-Rows is a
separate roll-forward recommendation, not a universal grid-layout requirement.
Totals visibility does not determine their business math: opening balances use
First over time, closing balances Last, flows Sum, and percentages/diagnostics
need their explicit aggregation policy. See
[roll-forward-authoring.md](roll-forward-authoring.md).
