> v17: New editable inputs explicitly default to ReadAndEdit. Business-dependent
> locking uses BasedOnFormula with a real, resolved expression. See
> [input-editability.md](input-editability.md); preserve intentional existing locks.

# Numeric input and Forecast bounds and distribution

Use this guide when authoring numeric inputs, Forecast edit settings, percentage
assumptions, static limits, or parent input with Average Leaf aggregation. These
are the user's confirmed target-product constraints as of 2026-11-14; they take
precedence over earlier source snapshots that accepted arbitrary numeric bounds.

## Average Leaf and parent distribution

An editable Data Input or Forecast measure can use `AverageLeaf` aggregation and
`distribute_parent_value_to_children:true` together. Do not restrict distribution
to Sum or automatically turn it off for rates/percentages. In the business spec,
default distribution on when either aggregation axis is AverageLeaf, unless the
user explicitly asks to disable it. An explicit `distribute:false` stays false.

For Data Input, write `measure_type.DataInput.column_type.Number` (also underneath
VisualColumn when applicable). For Forecast, write
`measure_type.Forecast.edit_config.number_column_metadata`. Keep both aggregation
axes, input eligibility, locks, bound context and identities intact. Distribution
is not a weighted allocation rule or a guarantee of any tested spread result.
Low-level `input_create` has no aggregation context: pass the selected Boolean
explicitly there. `distribution_default` is available to higher-level callers.

## Static min/max values are whole numbers

Do not author fractional static minimum or maximum values, such as
`max_value:{"Static":0.15}`. Never round that value to 0 or 1, silently remove the
requested limit, or change the unit of an existing input. `static_bounds` rejects
fractional static limits in constructors and transport guards before submission.
This restriction applies to min/max only: decimal defaults, formulas, data values
and resolved measure-based bounds remain separate supported branches.

Choose a representation consistent with the business unit:

- For an existing fractional percentage input (0.03 means 3%), retain its IDs,
  stored data, percentage formatting and formulas. A hidden Formula measure
  returning `0.15` can supply `max_value:{"Measure":"<resolved native ID>"}`.
  Register that helper and its dependency; do not use its label as the ID.
- For a new input stored as percentage points, whole bounds 0 and 15 are possible.
  Formula consumers must divide by 100 and formatting must display 3 as 3%, not
  300%. Do not impose this representation on existing fractional stored values.

Example business spec fragments (actual IDs are resolved by the constructor):

```json
[
  {"key":"meritLimit","kind":"Formula","label":"Merit Maximum","formula":"0.15","visible":false,"aggregation":"Formula"},
  {"key":"merit","kind":"DataInput","label":"Merit Increase","aggregation":"AverageLeaf","distribute":true,"default_value":{"Static":0},"min_value":{"Static":0},"max_value":{"Measure":"meritLimit"}}
]
```

## Existing-report comparison

When the user says a report now works, cache its current native properties and
column catalog before any write. Keep a full definition backup and compare that
working state with the redeployment, separating business changes from generated
metadata, ETags and timestamps. Preserve already-hydrated display/time settings,
stable IDs and stored inputs on an in-place update. A successful save or JSON
comparison is not runtime validation. Do not assert which of several manual
changes fixed a mode-switch failure without isolation evidence.
