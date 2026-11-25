# Fabric Plan authoring reference — opening balances, movements, and closing balances

Use this reference when a business request asks for a balance that changes from one planning period to the next. Examples include cash, inventory, receivables, headcount, and deferred revenue. Each case shows the source grain, editable fields, forecast series, formulas, and expected output.

The formulas below use readable measure labels and the Fabric Plan formula conventions supplied for this task. Resolve the references against the target sheet during artifact generation. Validate formulas in that sheet’s editor or parser and then test their results in the grid. The worked values are acceptance fixtures based on illustrative inputs.

## 1. Model the balance before writing formulas

| Role | What to create or bind | Examples |
|---|---|---|
| Native Power BI measure | Bind an existing semantic model measure at the required entity and period grain. Use sources that respect the sheet’s filters and dimensions. | Actual ending cash, on-hand snapshot, actual headcount, shipments, invoice sales |
| Data input measure | Create an editable field for a planner decision, assumption, or override. Use appropriate units, edit windows, and defaults. | Emergency cash draw, purchase receipt adjustment, attrition, credit adjustment |
| Forecast measure | Create the series whose closed periods take actuals and whose open periods carry a baseline, prefill, or planner forecast as needed. | Projected receipts, forecast demand, hiring forecast |
| Formula measure | Calculate the opening, signed movements, closing balance, and any threshold or reconciliation. | Opening Cash, Net Cash Movement, Closing Cash |

A forecast measure may combine a closed-period source and an open-period forecast. Set its prefill and allowed edits for the specific workflow. When open-period values are stored and editable, establish when the prefill runs and how repeat fills treat existing planner changes. An input of zero may represent a deliberate override. In the worked grids, optional movements without entries are zero by the input policy. [Microsoft Learn — Create forecasts using predictions and historical data](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-build-forecasts)

Use a continuous date axis ordered by the business calendar. Choose a leaf grain such as company × week or SKU × warehouse × month. Define the stock unit and sign convention. All cases below enter increases and decreases as positive magnitudes and subtract decreases in the formulas. Explicitly allow signed manual corrections when the business needs them.

### Opening and closing formula templates

The calculation is **opening in period t = closing in period t−1**. Closing is opening plus the current period net movement. The first opening is a governed seed, usually the actual closing balance immediately before the first forecast period. When the sheet starts at the first forecast bucket, bind `[Opening Seed]` to that prior actual. For these examples, the seed measure is available on the first forecast bucket.

**Opening Balance**

```text
IFNA([Closing Balance].RELATIVE(-1), [Opening Seed])
```

**Closing Balance**

```text
[Opening Balance] + [Net Movement]
```

Use this fallback form when the missing preceding period is the expected seed condition and the engine returns an NA for it. If an unexpected missing value could occur later, use an explicit first-forecast-period condition and flag missing prior closes for review. If the grid includes history, use the actual closing snapshot for closed periods and start the forecast from the last actual close. A forecast series such as `[Receipts Forecast]` can provide a closed-period flag via `[Receipts Forecast].CLOSEDPERIOD` when its period settings match the balance. Check that a newly closed period resets the downstream chain to the now-authoritative actual. [Microsoft Learn — Planning identifiers](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/identifiers)

For a mixed actual and forecast grid, the closing formula can branch like this when the forecast's closed-period flag is valid at the evaluated grain:

```text
IF([Movement Forecast].CLOSEDPERIOD, [Actual Closing Balance], [Opening Balance] + [Net Movement])
```

The first open period's relative read then picks up the last actual close. Define a separate first-visible seed if prior history may fall outside the evaluation axis.

The formula dependency is backward across periods, with `Closing(t-1) → Opening(t) → Closing(t)`. Create and resolve the two measure references together and test whether the target planner and artifact authoring path accept the dependency. A same-period dependency back to closing is a cycle. For example, a draw that goes into Closing Cash should be based on Cash Before Draw.

### Cumulative alternative for independent movements

If the authoring path rejects the cross-period dependency, calculate each close from a seeded cumulative range of independent movements. This version assumes a forecast-only grid, one seed at its first date, and a movement measure that can be computed without the closing balance.

**Closing Balance**

```text
var seed = SUM(SELECT.BYDATE([Opening Seed], MINDATE, MINDATE))
var movements = SUM(SELECT.BYDATE([Net Movement], MINDATE, COLUMN.CURRENT_PERIOD))
seed + movements
```

**Opening Balance**, when movements are additive and the closing has no nonlinear adjustment or recursive rounding

```text
[Closing Balance] - [Net Movement]
```

On a mixed history and forecast grid, use the explicit forecast start in both selections, with the seed bound to that forecast bucket, and branch closed-period values to actuals. Reconcile short periods, gaps, and horizon changes before choosing a date anchor. A direct cumulative sum is equivalent only when movements are independent of the opening or prior closing. If a cap, replenishment rule, or attrition rate feeds the next balance, keep the recurrence or calculate the state sequentially in a supported upstream process.

### Aggregation and reconciliation

- Sum compatible flows over time. For a time subtotal, use the beginning balance of the first included period and the ending balance of the last included period. Across entities, add balances only for the same date and comparable currency or units.
- Keep the calculation precise and apply display rounding at the end when feasible. When the policy rounds a movement, apply `ROUND` to that movement before it enters the balance. A rule that rounds each intermediate closing can change the next opening.
- Use a reconciliation measure such as `[Closing Balance] - [Opening Balance] - [Net Movement]`, with an expected result of zero at leaf grain. At time subtotals, use first opening, last closing, and total movement.
- Keep explicit modeling rules for blank seeds, missing mandatory forecast values, and optional inputs. `IFNA(expression, fallback)` handles NA. Check the target sheet’s blank behavior before relying on it to handle empty inputs. [Microsoft Learn — Conditional statements](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/conditional-statements)

## 2. Formula patterns for the skill

| Business question | Pattern | What to verify |
|---|---|---|
| What was this measure’s previous value? | `[Closing Cash].RELATIVE(-1)` | The previous leaf period is the one intended. A positive offset reads forward. The target accepts relative reference for this series. |
| What was the forecast for the next bucket? | `[Demand Forecast].RELATIVE(1)` | A rightward read at the last bucket has an explicit missing-value policy. A read alone does not schedule a receipt. |
| What is demand from the first position through the current leaf? | `SUM(SELECT.BYINDEX([Demand Forecast], 1, LEAF_INDEX))` | `LEAF_INDEX` is the current evaluating leaf index in the supplied convention. Confirm its spelling, start index, and selection scope in the target. A within-group position may restart at a year or quarter boundary. |
| What is the demand in the first three positions? | `SUM(SELECT.BYINDEX([Demand Forecast], 1, 3))` | The expected positions match the target selection axis. Use the applicable column count if the end should be dynamic. |
| What is demand for the first date in the grid? | `SUM(SELECT.BYDATE([Demand Forecast], MINDATE, MINDATE))` | Both boundaries are the same date. Confirm there is one intended period value per selected measure and row. |
| What is demand over the displayed date horizon? | `SUM(SELECT.BYDATE([Demand Forecast], MINDATE, MAXDATE))` | The first and last available column dates match the intended business horizon, especially after filtering. |
| What is demand from one month before through five months after this bucket? | `SUM(SELECT.BYDATE([Demand Forecast], ADDMONTHS(COLUMN.CURRENT_PERIOD, -1), ADDMONTHS(COLUMN.CURRENT_PERIOD, 5)))` | With a complete monthly axis and inclusive endpoints, this covers seven months. Check partial windows and fiscal periods. |
| What are the typical, lowest, or highest values in a window? | `AVERAGE(SELECT.BYDATE(...))`, `MIN(SELECT.BYDATE(...))`, or `MAX(SELECT.BYDATE(...))` | Choose the aggregation from the business question and define how to handle an empty selection. |
| What is the displayed column Grand Total value? | `CR_<grand-total-column-id>.M_<measure-id>` | Resolve both IDs from the target artifact. Read the configured total when subtotal logic matters. Use a range calculation when the business rule defines its own range. |
| What is the rounded amount or order multiple? | `ROUND(value, 2)` or `CEILING(units, packSize)` | `ROUND` sets decimal precision. `CEILING` applies an upward multiple. Validate pack size before using it. |

Use the [Microsoft Learn identifier reference](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/identifiers) for period dates and relative reads and the [rounding function reference](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/math-functions/rounding-formatting-functions) for precision and multiples. The dotted selectors, `LEAF_INDEX`, `ADDMONTHS`, and the column/measure ID pair follow the supplied target conventions. Confirm those tokens and their evaluation context in the target build. Examples from another formula surface can use different names for the same business operation.

**Declare a variable, keep the array, then filter it**

```text
var window = SELECT.BYINDEX([Demand Forecast], 1, LEAF_INDEX)
var positive = FILTERIF(window, ">0")
IF(COUNTIF(window, ">0") > 0, ROUND(AVERAGE(positive), 1), BLANK)
```

With 80, 0, and 100 in the range, the result at the third leaf is 90.0. The zero is excluded by policy in this diagnostic. In a stock movement or forecast total, a genuine zero may need to stay in scope. Test the empty result and whether the formula editor accepts an array in a local variable. [Microsoft Learn — Conditional statements](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/conditional-statements)

**Calculate a date boundary before selecting values**

```text
var fromDate = ADDMONTHS(COLUMN.CURRENT_PERIOD, -1)
var throughDate = ADDMONTHS(COLUMN.CURRENT_PERIOD, 5)
SUM(SELECT.BYDATE([Demand Forecast], fromDate, throughDate))
```

Choose offsets that match the calendar. For a four-week week-based plan, use the target’s supported week shift and date axis. A relative offset moves by position, so validate behavior with missing periods, hidden periods, reordered columns, and year boundaries.

**Conditional calculation and forecast fill**

Use an `IF` expression to choose a value at evaluation time, for example `IF([Closing Cash] < [Cash Floor], "Below floor", "OK")`. For forecast fill, set the source and open periods in the forecast configuration when the requirement is to initialize editable values. If a request specifically calls for a formula-language `FILL` statement, check the target editor or implementation for its signature and whether it evaluates values or writes inputs. Bind the confirmed operation only after identifying the destination, period scope, and overwrite behavior. The examples use forecast prefill or calculation formulas as appropriate. [Microsoft Learn — Forecast configuration](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-build-forecasts)
