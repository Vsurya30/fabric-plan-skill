# Forecast hierarchies, one-time columns and dynamic as-of controls

Use this guide for monthly forecasting, forecast time extension, one-time inputs,
quarterly commentary, annual notes, Formula Visual Columns, QTD/MTD/YTD,
as-of dates, interactive cutoff selection and SELECTEDVALUE-driven planning.
Discover `TIME-INTELLIGENCE`; use `FORMULA-SYNTAX` for comparison operators.
These rules apply across use cases, not only the report that exposed the issue.

## 1. Preserve a valid calendar hierarchy

Resolve actual model fields, calendar relationships, sort order, date formats and
fiscal definitions first. Prefer individual date attributes, in this order:

| Grain | Preferred Columns |
|---|---|
| Monthly | Year, Quarter, Month (MonthName is a valid field label) |
| Quarterly | Year, Quarter |
| Yearly | Year |
| Weekly | Year, Quarter, Month, Week only when those are valid parents |

For weeks crossing month/quarter boundaries, use the model's valid Year/Week
hierarchy; do not invent month parentage. A model without Quarter can use
Year/Month. Do not add synthetic calendar fields just to satisfy an example.
Custom fiscal names require explicit role mappings, not guesses from labels.

Avoid YearMonth, YearQuarter and YearWeek in Columns when equivalent separate
attributes exist. A composite is allowed when explicitly required or when no
suitable individual hierarchy exists; record the reason and establish the native
time role, member ordering and extension behavior. A YearMonth filter or slicer
may remain useful for a date window; the rule concerns the planning axis.

Forecasts extending into future periods require **only valid date hierarchy
attributes in Columns**. Move unrelated product/scenario dimensions only within
authorized scope; do not silently remove them. Calendar member completeness,
chronological sorting and the applicable time unit must be resolved separately.

`build` normalizes a recognized composite Forecast axis to available individual
fields. `calendarRoleFields` maps Year/Quarter/Month/Week to actual model field
keys. `weekParentageValidated:true` is an evidence assertion by the author, not a
check of the calendar's data. An intentional composite requires
`allowCompositeTimeAxis:true`, `compositeTimeAxisReason` and `columnTimeLevels`.
No suitable fields means resolve the model or deliberate exception; do not guess.

For existing reports, use `planning-time-axis` with properties, current model,
columns and optional `time_levels`. It prepares properties only. Preserve existing
date-window filters (including a removed composite's scope filter), measure IDs,
Forecast bounds, locks, input values and storage key mappings. A changed visible
calendar axis does not authorize a writeback key migration. Reconcile other
explicitly affected embedded views and reference the same owner, without cloning
input state. Use current exports and optimistic baseline hashes when publishing.

## 2. Choose the correct one-time column

When the request adds information beside a finer-grain planning grid, evaluate a
Visual Column first. Leave the existing Columns hierarchy intact.

| Request in the existing grid | Preferred additional column |
|---|---|
| Quarterly/annual management commentary beside monthly values | Visual Input Column, LongText |
| Monthly/quarterly notes beside weekly values | Visual Input Column, LongText |
| One-time forecast adjustment | Visual Input Column, Number |
| QTD, MTD, YTD or selected-date summary | Formula Visual Column |

Append once at the end of the grid, once per row context, not once under every
month. Visual input and visual formula are distinct native types:

```json
{"VisualColumn":{"DataInput":{"id":"<configuration-id>","title":"Commentary","column_type":{"LongText":"<resolved metadata>"},"allow_input":"ReadAndEdit","bound_to_filter_context":true}}}
```

```json
{"VisualColumn":{"Formula":{"formula":"<resolved native formula>"}}}
```

These illustrate the `measure_type` tags, not complete deployment payloads. Use
`runtime.input_factories.input_create(..., visual_column=True)` for typed text,
numeric and other supported native input metadata; use `formula_create` with the
same flag for a native formula request. Create and register against the actual
owner. Native `columnType` create requests and ALM `dataInputType` records are
different contracts. The regular builder accepts `visual_column:true` for its
numeric DataInput and Formula kinds. Forecast/Native are not VisualColumn tags.

One-time presentation does not imply one global saved comment. Resolve row,
quarter/year, scenario/version and filter context for persistence. If separate
comments for every quarter are needed, retain those distinct storage contexts or
use an appropriate period-grain commentary sheet. Do not overwrite one comment
while presenting it as multiple quarter-specific entries. Define subtotal entry
and roll-up explicitly. Do not create a new calendar axis merely for the comment.

## 3. Prefer a dashboard slicer for shared cutoff control

Always evaluate this route first for dynamic as-of calculations:

**Intelligence slicer → DAX SELECTEDVALUE measure → exposed Planning native
measure → Formula Visual Column → QTD/MTD/YTD result.**

Choose it when a date should influence multiple visuals/sheets/calculations in
the same dashboard, when the user requests a dashboard dropdown, or when a
suitable semantic slicer already exists. Reuse the existing selector where safe.
A visual-level parameter is appropriate for a cutoff exclusive to one sheet or
when a dashboard slicer cannot supply the required context. Record why.

1. Select an unambiguous date/month key and single selection. MonthName alone
   requires a year; YearMonth may be used in this slicer without becoming the
   planning axis. Decide an explicit no-selection/multi-selection policy.
2. Avoid filtering away the history needed by QTD/MTD/YTD. Prefer a disconnected
   as-of date table where a connected calendar slicer would prune that history.
3. Expose the selected scalar through a semantic measure, for example this DAX:

```dax
Selected As Of Date = SELECTEDVALUE('As Of Calendar'[Date])
```

4. Assign that measure to the Planning owner, resolve its actual native ID and
   supported date representation, then bind the Formula Visual Column cutoff to
   the exposed value. Conceptually:
   `SUM(QTD(M_<forecast-id>, 0, DATE(M_<selected-date-id>)))`.
   Choose any date conversion from the actual returned type; do not assume DAX
   date scalars and native formula values are interchangeable.
5. When runtime verification is in scope, change the slicer and trace the new
   selection, SELECTEDVALUE output, owner measure, formula result and every
   intended visual. Configure interactions explicitly. Saved metadata alone does
   not establish cross-visual propagation or correct recalculation.

The bundled as-of helper below constructs the captured **single-sheet parameter**
route. It does not automatically create a disconnected semantic table, DAX
measure or dashboard interactions. Use the semantic-model and Intelligence
authoring routes for those prerequisites; do not substitute a local parameter
silently for a requested shared dashboard control.

## 4. Native parameters and exact formula patterns

External control → selected value → optional transformation → cutoff date →
time-intelligence aggregation → one Formula Visual Column.

Parameter choice: Number for year/offset/numeric control; Text for a string;
Date for a date control; List/dropdown for constrained date/month choices. The
available UI can offer input box, slider, dropdown, tiles or radio for applicable
types. Confirm the target type/interface contract. A Date **input column** is not
a Date **parameter**. The shipped serializer covers the captured dataset-backed
date **List** parameter; it does not assert a complete generic Number/Text/Date
parameter creation API. Do not invent missing enum/property contracts.

For the captured date-list parameter, preserve all three linked representations:

| Location | Identity/value |
|---|---|
| sheet.properties.entityLevelVariables | `CALC_VARIABLE_<id>`, list/dataset, selectedDimension, scope entity, selected value |
| visualState.globalVariables | same ID, singleSelect, label/title, showVariable |
| visualState.calculatedVariables | same ID with selected date value |

Read the full emitted payload from `date_parameter_bundle` or the example. Use
actual Date dimension values and a unique stable ID; resolve the same field's
type and default membership. A native formula refers to it as
`VR_CALC_VARIABLE_<id>`, not its visible label.

Exact native date-list patterns (replace symbolic IDs with current IDs):

```text
SUM(QTD(M_<forecast-id>, 0, DATE(VR_CALC_VARIABLE_<id>)))
SUM(MTD(M_<forecast-id>, 0, DATE(VR_CALC_VARIABLE_<id>)))
SUM(YTD(M_<forecast-id>, 0, DATE(VR_CALC_VARIABLE_<id>)))
```

The first argument is the source measure, second is relative period offset
(normally zero, unless requested), and third is the cutoff. `SUM` is the native
aggregation wrapper. For an entire selected month, the captured native wrapper
is **one-argument** `EOMONTH(DATE(VR_CALC_VARIABLE_<id>))`. Do not copy DAX's
two-argument EOMONTH form into this language. Keep an exact daily cutoff when the
business asks for partial-month MTD/QTD; month-end rounding is a deliberate choice.

Month-name alternative: map January through December to 1 through 12 with SWITCH,
pair with an explicit selected year, construct the first day, and optionally
round to month end. A safe place to perform this transformation for the dashboard
route is DAX, whose syntax is separate from native Planning formulas:

```dax
Selected As Of Date =
VAR SelectedYear = SELECTEDVALUE('As Of Calendar'[Year])
VAR SelectedMonth = SELECTEDVALUE('As Of Calendar'[MonthName])
VAR MonthNo = SWITCH(SelectedMonth,
    "January",1,"February",2,"March",3,"April",4,
    "May",5,"June",6,"July",7,"August",8,
    "September",9,"October",10,"November",11,"December",12,BLANK())
RETURN IF(ISBLANK(SelectedYear) || ISBLANK(MonthNo), BLANK(),
    EOMONTH(DATE(SelectedYear,MonthNo,1),0))
```

For a sheet-only month-name parameter, use the equivalent supported native
SWITCH → DATE(selected year, month number, 1) → EOMONTH transformation only after
resolving those native function signatures; its serializer is not supplied by
`date_parameter_bundle`. Prefer a date-valued list to remove month/year ambiguity.
Never hardcode the example year into reusable logic. Missing/invalid choices must
have an explicit policy, not a silent current-date substitution.

## 5. Aggregation, missing values and safe scope

Keep the main monthly/weekly grain. Resolve time windows, loaded history and
future-month availability; a truncated visible interval can make a QTD/YTD total
incomplete. Keep missing distinct from zero. The helper can guard an aligned
missing-cell measure with the **same** period and cutoff:

```text
IF(SUM(QTD(M_<missing-id>, 0, <cutoff>)) > 0, BLANK, SUM(QTD(M_<forecast-id>, 0, <cutoff>)))
```

If checking zero, use `== 0`; see [formula-equality.md](formula-equality.md).
Choose row aggregation per business semantics. Sum only compatible additive
values; currencies must be converted at the correct leaf grain before summing.
Rates and mixed local currencies do not become additive just because a visual
column is appended. Preserve existing missing/FX guards and balance aggregation.
The helper defaults row aggregation to None and column aggregation to None.

Scoped repairs retain unrelated encoded parts, measure/configuration IDs,
formulas, input values, access rules, filters, InfoBridge bindings and storage
identity. Do not use a working reference's owner IDs, data or connections.
Reusing reference UTC bounds requires the identical horizon/timezone.

## 6. Portable commands and evidence boundary

```sh
python plan.py discover --module TIME-INTELLIGENCE
python examples/forecast-time-intelligence/build.py draft
python plan.py planning-time-column --baseline draft/baseline.json --input draft/time-column.request.json --out candidate
python plan.py repair-formula-equality --input draft/equality.request.json --out equality.json
```

The standalone example uses bundled synthetic fields and demonstrates new-sheet
hierarchy selection, date-list binding, a Formula Visual Column and a separate
LongText Visual Input create request. The two-stage native create/register path
for text is intentional; do not mistake that request for an imported ALM column.

`planning-time-axis --input axis-request.json --out properties.json` takes
`{"properties":<owner properties>,"model":<current field catalog>,"columns":[<actual field keys>],"time_levels":<optional role mapping>}`.
It is a property candidate, not a full report. `planning-time-column` takes the
request demonstrated in the example and emits a scoped definition and manifest.
It rejects duplicate IDs rather than silently overwriting existing parameters.

When authorized, publish candidates through the normal API writer and poll save
completion. Check definition readback separately from runtime tests: future
period navigation, input editability, cutoff switching, QTD/MTD/YTD numeric
results, comment persistence and writeback (only when configured). If the user
will validate, report exactly what was saved and what is unverified. See
[forecast-time-intelligence-evidence.json](forecast-time-intelligence-evidence.json)
for this release's evidence; package tests are not live UI acceptance.
