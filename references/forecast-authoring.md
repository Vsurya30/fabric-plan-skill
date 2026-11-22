> v17: New editable inputs explicitly default to ReadAndEdit. Business-dependent

Current authoring rules: read [forecast-time-intelligence.md](forecast-time-intelligence.md)
for non-composite calendar axes, one-time Visual Columns and shared versus local
as-of controls. Read [formula-equality.md](formula-equality.md): native comparisons
use `==`; single `=` is reserved for variable declarations. These rules supersede
older comparison examples; original supplied documents remain preserved.

> locking uses BasedOnFormula with a real, resolved expression. See
> [input-editability.md](input-editability.md); preserve intentional existing locks.

> 2026-11-14 numeric-input correction: [numeric-input-constraints.md](numeric-input-constraints.md) is authoritative for whole-number static min/max bounds and AverageLeaf parent distribution. Decimal defaults/formulas are separate; preserve existing percentage units and IDs.

# Forecast intent and executable construction

Use the native **Forecast** feature for a forecasting request. Do not silently
replace it with an ordinary numeric input, calculated measure, or static series.
Preserve F09's detailed business guidance and native variants. This selected
constructor closes the ordinary actuals-history plus editable-open-default route;
advanced copy, cube and automatic closure variants retain their separate contracts.

## Business defaults

1. Resolve the relevant actuals measure, including its DAX definition when the model
   exposes several similarly named measures. Closed periods link to that actuals
   measure. A plan, budget, forecast or planning-eligibility helper is not an actuals
   source merely because its label includes sales or salary.
2. Assign Region/Product or other business detail to Rows. By default use the real
   Year, Quarter, Month fields in Columns, in that order. MonthName must be sorted
   by month number. Keep non-date dimensions out of Forecast Columns.
3. Use the user's forecast horizon. Closed history precedes the first open period.
   If the horizon cannot be inferred from the request, ask for it while continuing
   independent construction. Do not derive a business cutoff from the machine clock.
4. When the user supplies an open-period default formula or source measure, use it
   under editable Data Input defaults. For a vague forecast request with no open
   configuration, choose **None**, serialized as `{"DataInput":"Blank"}`. Do not
   invent growth rates, carry-forward values or zero baselines.
5. `COLUMN.ADDMONTH(-1) * 1.1` means previous month multiplied by 1.10. For a
   November start, the first open month uses October's closed actual; December
   uses November's forecast, so the growth compounds monthly. This is a requested
   assumption, not a statistical model. Do not replace it with a reference to a
   fixed October measure in every future month. Missing October actuals are not
   automatically zero. User-supplied syntax is preserved exactly; live calculation
   evidence remains separate from saved configuration.

## Working-reference default profile

Use `referenceForecast` to supply the selected `columnMeta.measure_type.Forecast`
settings from a working reference, and `referenceTimezone` only for an explicit
IANA zone. The constructor rebinds actuals to `actuals`, preserves the user's
`openDefault`, and copies same-horizon saved bounds. Do not pass unremapped edit
formulas or measure-dependent limits from a different owner.

The Correct Version save supplies the default profile: `closed_period_till:null`,
`auto_close_forecast_settings:null`, `forecast_allowed_user_permissions:true`,
`disable_write_access:false`, `forecast_value_display:"Actual"`, context bound true,
`edit_config.aggregate_total:null`, `allow_input:"ReadAndEdit"`, and
`on_change_formula:null`. Numeric min/max/default are null and
`distribute_parent_value_to_children:true`. Set `distribute:false` only for an
explicit different requirement. Row/column aggregation remains Sum/Sum.

The UI showed All Periods even though its native `aggregate_total` was null.
The earlier constructor emitted `AllPeriods`, an explicit previous-day
`closed_period_till`, omitted the permission/auto-close fields and disabled
distribution. These are observed configuration differences, not isolated proof
of a single runtime root cause. Reproduce the working profile; do not invent values.

For repair and quarterly From Sheets/variance/chart execution, use
[forecast-review-execution.md](forecast-review-execution.md). The report's existing
Forecast ID and consumers survive a repair. A designated reference does not
authorize overwriting unrelated security, existing input data or other measures.

## Composed spec

`runtime.construct.planning` calls `runtime.forecast.forecast_config` and allocates
the native Forecast record, manage-measure entry, Sum/Sum aggregation, formatting,
context binding and closed-actual dependency. The provisioner retains this module
as `planning.forecast`; it must not drop it as an unknown kind.

```json
{
  "key":"forecast", "kind":"Forecast", "label":"Sales forecast USD",
  "actuals":"actual", "start":"2026-11-01", "end":"2035-12-31",
  "timezone":"UTC",
  "openDefault":{"Formula":"COLUMN.ADDMONTH(-1) * 1.1"}
}
```

The `actual` symbolic key must be a preceding/resolved Native actuals measure in
the same sheet. Omit `openDefault`, or set it to `"None"`, for blank open defaults.
`{"Measure":"someResolvedKey"}` seeds from a resolved assigned measure.
The caller must verify the actuals meaning; a constructor cannot infer DAX semantics
from a symbolic key alone.

The native payload is under `columnMeta.measure_type.Forecast`, with
`closed_period_config.method.LinkToMeasure` containing the actual native measure ID
and `open_period_config.method.DataInput.Formula` containing the formula. This is
different from a read-only `method.Formula`. `forecast_value_display:"Actual"` is a
display choice and does not establish the closed-period source.

### Forecast-period configuration: ISO labels and UTC boundaries

Emit all four `forecast_period` fields: `start`/`end` as full nominal ISO labels
(`YYYY-MM-DDT00:00:00.000Z`), plus `start_utc`/`end_utc` as integer Unix **seconds**.
Resolve the authoring/report timezone from available context. The UTC start is
local midnight on the first open day; UTC end is one second before local midnight
after the final open day. Account for DST independently at each boundary. Nominal
ISO labels are not the instants from which to blindly derive the UTC companions.
Optional fields in the Rust decoder do not establish that renderer/time expansion
can omit them. This supersedes the older factory's omission rule.

Pass `timezone` as an IANA name in the Forecast spec (for example `America/Chicago`
when that is the resolved user/report context). Alternatively pass `periodUtc` with
both captured epoch-second values for the identical dates and timezone. Do not
reuse a sample timezone or timestamps across reports. If neither an explicit reference/report timezone nor same-horizon bounds
are available, default to UTC without prompting. Never infer the timezone from
the host clock, client locale or an offset alone.
The factory uses Python zoneinfo, falling back to Node ICU when Windows lacks IANA
data; no new package installation is required when the bundled Node prerequisite is met.

Observed UI-saved example for November 2026 through December 2035 in Chicago:
`start_utc:1793509200`, `end_utc:2082779999`. The date labels remain
`2026-11-01T00:00:00.000Z` and `2035-12-31T00:00:00.000Z`. These are example
boundaries, not reusable defaults.

### Forecast -> Time extension: date-axis metadata

The before/after date-axis comparison belongs to **time extension under Forecast**.
For `visualState.columnDimensions[]`, preserve the resolved field IDs/external keys
and mark each real calendar level `isTimeDimension:true`, with `timeIntervalUnit`
equal to `Year`, `Quarter` or `Month` respectively. A generic `isNative:true`
dimension descriptor alone does not carry the time-extension role. The constructor
calls `forecast_time_axis` automatically for sheets containing native Forecasts.
Keep the corresponding semantic `pivotAssignments` and Year -> Quarter -> Month
order; do not create fake calendar fields or reassign business dimensions.

The captured manual save added these axis roles for the whole visual, yet the
original forecast still stayed hidden in the user's screenshot. The original and
manual forecasts were both registered and `visible:true`; the old forecast alone
lacked normalized period boundaries. Thus these are two observed missing contracts,
with UTC boundaries the stronger visibility suspect. The comparison alone did not
isolate a causal fix or prove calculations. Preserve original measure IDs, actuals
links, formulas, inputs and unrelated settings during repairs.



#### Dynamic granularity: derive, do not copy the example

The axis roles are dynamic, one per actual assigned column dimension. The
Year/Quarter/Month before-and-after snapshot illustrates one report only:

| Actual column hierarchy | Time-extension roles emitted |
| --- | --- |
| Year | Year only |
| Year -> Quarter (including a resolved Qtr field) | Year, Quarter |
| Year -> Month | Year, Month |
| Year -> Quarter -> Month | Year, Quarter, Month |
| Other documented supported hierarchy | One matching native unit for each resolved level |

Preserve the user's chosen granularity and an existing valid hierarchy. Never
append Quarter or Month merely to match the sample, and never mark every field as
Month. The Year -> Quarter -> Month default applies to new requests with no chosen
or existing granularity. Names, field IDs and ordering come from the actual model.
For ambiguous or custom field names, resolve the level from explicit configuration,
then name keywords and actual member/format context; numeric data types alone do
not establish a date role. Fiscal-year and week semantics remain separate.

The sheet spec accepts `columnTimeLevels`, keyed by exact assigned column field:
`{"Calendar[FiscalYr]":"Year","Calendar[Qtr]":"Quarter"}`.
Recognized Year/Yr, Quarter/Qtr and Month/MonthName/MonthNumber names map directly.
For other supported levels, pass a descriptor with the resolved semantic `level`
and the destination's exact `timeIntervalUnit`, obtained from the applicable
native contract/metadata. Do not guess the Half Year enum or copy the uppercase
writeback enum. The resolver supports the complete documented hierarchy-pattern
table in F09, including annual, half-year, weekly and daily patterns, while requiring
the actual native unit for uncaptured levels. Standalone Day requires full-date
members. Invalid orderings and unsupported combinations remain invalid.

Time extension and open-period formula semantics are separate. Preserve an explicit
`COLUMN.ADDMONTH` formula as requested; do not silently rewrite it to an annual or
quarterly offset when column granularity changes. If the requested business rule
cannot be expressed at that grain, resolve that specific mismatch.

## Verification

Skip the following report checks when the user requests no validation; retain only
reads necessary for construction, current IDs/ETags and operation completion.

Check the saved native Forecast record, exact source measure ID, open/closed
methods, horizon, date column ordering and activation/aggregation registrations.
For dashboards check slicer bindings, each chart field's ordinary Visual level
filter, KPI default state and numeric-ID page-local embed rectangle. Keep chart
actuals clearly labelled when they show actuals rather than Forecast outputs.

When data access works, compare the first open month to preceding actual ×1.10,
the second to first ×1.10, and test future-month expansion, direct open edits,
closed edit restrictions and save/reopen. Model failover or unavailable source
data does not justify invented values or a claim that these tests passed. Continue
independent authorized definition deployment and state the runtime limitation.
