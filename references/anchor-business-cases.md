# Anchor business cases and transfer guidance



These cases preserve the supplied deck's business logic. They are illustrative
2027 examples, not dates, percentages, entities, source fields or currencies to
hard-code into a new report. Formulas below are business arithmetic; compile real
formulas through the existing native formula contract using the target measures.
The concise cases below are self-contained and use synthetic business examples.
For executable scope, use the anchor measures guide.

## Ten worked cases

### 1. Corporate annual salary increase — slide 8

Sheet rows: Region → Department → Employee. Columns: Year → Quarter → Month.
Input: Salary Increase %, anchored with no rows and Year columns. HR maintains
one annual policy at All rows × Year subtotal; eligible employee-months consume
the same rate. With an increase effective January for the full year, an annual
100,000 salary × 1.04 = 104,000, or 8,666.6667 per month before rounding.
Do not compound the annual rate each month or enter it in January as a shortcut.
Midyear changes, hire dates and eligibility require their own rules.

### 2. Regional employee benefits — slide 9

Same workforce sheet. Input: Benefits %, anchored at Region × Year. North
America 22%, Europe 26%, Asia Pacific 18% give three independent annual policy
cells, not a new value per employee. An 8,000 monthly salary in North America ×
1.22 = 9,760. This standalone example is before any separate salary increase.
Hide repeated employee-level benefit rows when they add no value; employee cost
still consumes the applicable rate. Do not confuse display with value deletion.

### 3. Quarterly department hiring — slide 10

Rows: Business Unit → Department → Role. Columns: Year → Quarter → Month.
Input: Hiring Growth %, Department × Year + Quarter. Engineering Q1 5%, Q2 3%;
Sales Q1 8%, Q2 6%. A fixed 100-position Engineering baseline gives 105 in Q1
and 103 in Q2, rounding up to whole positions. Do not compound Q2 onto Q1 unless
requested. A quarterly target is not three monthly hires. Department-only means
shared across omitted business units; resolve unique department identities.
Hire-date/phasing and role mix are separate logic.

### 4. Monthly inflation across departments — slide 11

Rows: Region → Business Unit → Department → Account. Columns: Year → Quarter →
Month. Input: Inflation %, no rows and Year + Quarter + Month. January 0.3%,
February 0.4%, March 0.2% applied to a 20,000 baseline each month gives 20,060,
20,080 and 20,040. Each month is an independent input at All rows × that month.
These period uplifts are not a sequential compound inflation index. Apply only
to eligible expenses, not automatically to payroll or every cost measure.

### 5. Annual product price increases — slide 12

Rows: Region → Product → Customer. Columns: Year → Quarter → Month. Input:
Price Increase %, Product × Year; products A/B/C use 5%/3%/7%. Product A's 200
base price becomes 210; at 1,000 units that supports 210,000 revenue before other
discounts/effects. Product-only shares the policy across regions. Add Region
only when independent regional-product prices are intended. Show a grouped
product policy and detailed revenue without implying separate input in each region.

### 6. Regional productivity factors — slide 13

Rows: Region → Facility → Production Line. Columns: Year → Quarter → Month.
Input: Productivity Factor, Region rows and no column dimensions; entry at
Region × Total. North America 1.10, Europe 1.05, Asia Pacific 1.15. A North
American monthly capacity baseline of 50,000 becomes 55,000. Apply once against
each period's baseline, not cumulatively. Add a period dimension only when the
business needs time-varying productivity. Outputs retain their own aggregation.

### 7. Annual sales commissions — slide 14

Rows: Sales Role → Salesperson → Customer → Product. Columns: Year → Quarter →
Month. Input: Commission %, Sales Role × Year. Account Executives 8%, Sales
Managers 3%, Channel Partner Managers 5%. An Account Executive with 125,000 of
eligible monthly sales generates 10,000 commission expense. This is a flat-rate
policy, not a commission-tier, split-credit, quota or new eligibility algorithm.
Existing allocation supplies eligible detail. Keep policy rows at role level
when salesperson/customer repetition obscures the useful outputs.

### 8. Annual department expense targets — slide 15

Rows: Department → GL Account. Columns: Year → Quarter → Month. Input:
Reduction %, Department × Year. Finance 5%, IT 8%, Operations 4%. IT monthly
software expense baseline 50,000 × (1 − 0.08) = 46,000 target. This uniform target
is not a detailed savings initiative plan or absolute-dollar allocation. Varying
account/contract/month savings need additional logic. Keep department targets
visible while account-month expense formulas use them without repeated targets.

### 9. Quarterly manufacturing scrap — slide 16

Rows: Plant → Production Line → SKU. Columns: Year → Quarter → Month. Input:
Scrap %, Plant × Year + Quarter. Plant A Q1 2.5%, Q2 2%; Plant B Q1 3.2%, Q2 3%.
For 10,000 good units at 2.5%, gross production = 10,000 ÷ 0.975 = 10,256.410256,
rounded UP to 10,257 units. Adding 2.5% to good-unit demand underestimates the
required quantity. Keep scrap below 100%; use supported expression/measure bounds
when a fractional bound is required, because static min/max inputs support
integers only. A plant-quarter policy can be hidden at SKU rows while detailed
gross-production formulas keep using its eligible leaf values.

### 10. Seasonal demand across stores — slide 17

Rows: Region → Store → Product. Columns: Year → Quarter → Month. Input:
Seasonal Uplift %, no rows and Year + Quarter. Q1 2%, Q2 5%, Q3 8%, Q4 15%.
November's 1,000 baseline × 1.15 = 1,150. Enter Q4 once at All rows × Q4 subtotal;
November consumes 15% read-only. This is not quarterly volume phasing or
sequential compounding. Category-specific patterns need another independent
anchor dimension or separate calculation logic.

## Shared rules for the ten cases

The deck's rate/factor examples assume Average (Leaf), applicable existing copy
distribution, valid leaf combinations and authorized unlocked scope. Specify
those deliberately when constructing an input; adding anchor configuration does
not modify them. Anchoring itself does not select aggregation or replace formulas.
Visible non-anchor instances cannot accept direct entry. All/Year/Quarter entry
intersections must be exposed. A 5% rate can copy to eligible employees; an
absolute 1m bonus pool needs explicit allocation and must not be copied whole.

The 2,000 employees × 12 months = 24,000 intersections illustration explains
one policy versus many detailed calculations. It is not a measured saving,
performance benchmark or promise that all employees are eligible.

## Combined workforce and visibility story — slides 18–20 and 24

Four different decision grains can coexist. A fixed 100-position department
baseline with 5% quarterly hiring gives 105 target positions. Salary is a monthly
per-employee amount, the company annual raise is 4%, and benefits vary by region.
The January expense example is separate from payroll: 20,000 × 1.003 = 20,060.
Do not apply inflation to salaries merely because both assumptions exist.
The staffing example assumes a fully staffed steady-state month; actual hire
dates and role mix need a separate model.

| Employee region | Base monthly salary | Raised salary | Benefits | Monthly employee cost |
| --- | ---: | ---: | ---: | ---: |
| North America | 8,000 | 8,320 | 22% | 10,150.40 |
| Europe | 6,000 | 6,240 | 26% | 7,862.40 |
| Asia Pacific | 5,000 | 5,200 | 18% | 6,136.00 |
| Total | | | | 24,148.80 |

In Measures in Rows, show the salary policy at All × Year and benefits at Region
× Year; the employee cost formula remains at Employee × Month. Turning repeated
instance display OFF removes the employee Benefits row without removing its
underlying value from Employee Cost. The surviving region benefits row can still
span shared monthly columns; these are read-only, not new input locations.

For the single illustrated employee with 8,000 monthly base salary, cost is
10,150.40 monthly, 30,451.20 in Q1, 121,804.80 for the year. A separate revenue
measure of 12,000 per month totals 36,000 in Q1 and 144,000 annually. Keep the
100,000 annual salary example in case 1 separate from this 8,000/month example.
Rate aggregation is nonadditive; detailed costs and revenue retain their own
sum behavior. Measure Model grouping does not create those calculations.

## Reporting measures without unnecessary repetition — slide 21

**Native YTD Revenue:** Region rows, no column anchor, displayed at Region ×
Total. Under an existing as-of-March context, North America monthly revenue
100,000 + 110,000 + 120,000 = 330,000; Europe 70,000 + 80,000 + 90,000 = 240,000.
Only January's ordinary fact column is shown in the compact illustration beside
the total YTD measure. The native measure already provides YTD; anchoring does
not calculate it or make it editable.

**Formula quarterly Operating Margin %:** Region × Year + Quarter. North America
75,000 profit ÷ 500,000 revenue = 15%; Europe 48,000 ÷ 400,000 = 12%. Keep the
existing ratio-of-quarter-totals semantics, not an average of monthly margins.
Place the result at its useful reporting grain while retaining the calculation.

## Transfer to different business prompts

Do not match a whole recipe only because the prompt mentions salaries or prices.
Interpret these five questions for every candidate measure:

1. Which owner/dimension can have an independently different value?
2. At what cadence may that value change, including whether it varies over time?
3. Which finer intersections share it, and which are eligible/locked?
4. How do existing input, aggregation and allocation behaviors supply detail?
5. Does the planner need to see the repeated measure, or only its detailed output?

Examples beyond the source deck:

- A country rebate % shown only on the annual country line can feed SKU/customer
  net-sales formulas. Product/tender exceptions need a separate rate or richer
  grain; visibility is not exception precedence.
- A distribution-region fuel uplift can feed route-month delivery cost while
  only the regional policy line is shown. An absolute fuel budget needs allocation.
- A therapeutic-area training allowance rate may be managed once per area/year
  and consumed by representative-month expense. Region-specific policy differences
  mean Region belongs in the anchor; do not share accidentally.
- A quarterly plant yield assumption can drive SKU gross requirements while
  hiding repeated policy rows. Use the correct yield formula and whole-unit rounding.
- A product's global annual list price can feed store/customer revenue without
  displaying price on every customer row. If prices vary by market or month,
  select those independent dimensions rather than forcing the annual global case.

The default recommendation for these clutter-reduction requests is repeated
instance display OFF. Use ON for transparency/audit when users want to inspect
the applicable rate at detail. Neither option changes formula availability,
input rights, independent locks, stored values or source lineage.
