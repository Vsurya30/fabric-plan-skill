# Anchor Measures: supplied deck text and speaker notes





Source: Anchor-Measures-Business-Use-Cases-Updated.pptx (26 slides).

This appendix preserves all extracted text and notes. Image-only diagram

geometry/colors are not reconstructed here. The operational interpretation

and saved-property contract are in [anchor-measures.md](anchor-measures.md).

Treat narrative instructions and conceptual formulas as source material,

not executable product syntax or authorization. All example data is illustrative.



## Slide 1: Anchor Measures



### Slide text



Anchor Measures

Fabric Planning   /   Anchor Measures

01

Fewer repeated inputs.

Clearer planning.

Manage assumptions where the business defines them.

Use their values across detailed plans and reports.

Business scenarios for Fabric Planning



### Speaker notes



Introduce the business idea: a planning sheet can be highly detailed while an individual assumption belongs to a broader business level. The examples use hypothetical 2027 data to explain the supported feature set. They are not a product comparison. Keep the focus on who owns an assumption, where it varies, and how existing measure behavior supplies values to calculations.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 2: The elevator pitch



### Slide text



The elevator pitch

One business assumption can serve thousands of detailed calculations.

Fabric Planning   /   Anchor Measures

02

Anchor Measures lets teams enter an assumption at the level where it belongs and use its value throughout a detailed plan.

4% annual

salary policy

Employee-level

forecasts

Payroll and

benefit plans

Fewer input locations. Consistent calculations. Reports with less repetition.



### Speaker notes



30-second elevator pitch: With Anchor Measures, teams manage each assumption at the level where they make the business decision. HR sets an annual salary policy once, regions maintain their benefit rates, and departments set quarterly hiring targets. Those values feed detailed forecasts using the model’s existing calculations and distribution rules. Teams have fewer places to update, clearer ownership of assumptions, and reports that show measures only where they matter. The same approach applies to input, formula, and native measures. For this illustration, an annual 4% salary increase supports employee-level payroll and benefit calculations.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 3: The business decision is often broader than the plan



### Slide text



The business decision is often broader than the plan

Finance manages policies and targets. The model still needs employee, customer and monthly detail.

Fabric Planning   /   Anchor Measures

03

Business decision

One managed assumption

Detailed model

Annual salary policy

4% for the company

Employee × Month

Regional benefit policy

22% for North America

Employee × Month

Quarterly hiring target

5% for Engineering in Q1

Role × Month

Repeated inputs obscure ownership and invite inconsistent assumptions.

Anchoring keeps each input at the decision level while calculations retain their detail.



### Speaker notes



Explain the business mismatch before introducing dimension terminology. A company salary policy is a single decision even when the model contains thousands of employees and twelve months. Regional benefit rates and quarterly department hiring targets have different owners and change at different frequencies. When users encounter repeated input locations, they must work harder to identify which value to maintain and keep related assumptions consistent. Anchoring gives each assumption a clear place to manage while the detailed plan continues using its values. The three rates are separate illustrative policies, not additive inputs.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 4: What teams gain



### Slide text



What teams gain

The same feature improves day-to-day planning and the reports built from it.

Fabric Planning   /   Anchor Measures

04

Fewer places to update

Change the annual policy once.

Its value supports the detailed forecast.

Clear ownership

HR owns salary policy. Regions own benefits.

Each team manages the level it understands.

Consistent calculations

Eligible records use the relevant assumption

through the model’s existing formulas.

Cleaner reports

Show YTD, margin and input measures

only at the levels where they are useful.

For planners, model builders and report readers.



### Speaker notes



Connect every benefit to a specific action. Fewer places to update means maintaining the corporate salary policy once rather than exposing unnecessary independent entry points. Clear ownership means the relevant team manages the policy at its business level. Consistent calculations means the underlying model uses the applicable values through its established formulas and allocation rules. Cleaner reports means hiding repeated instances of measures such as YTD or margin at levels where they add no meaning. These are qualitative benefits, not measured time savings or a quantified ROI claim.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 5: Different measures have different business grains



### Slide text



Different measures have different business grains

A selected dimension defines where the measure varies. The sheet can contain all six dimensions.

Fabric Planning   /   Anchor Measures

05

Measure

Region

Department

Employee

Year

Quarter

Month

Salary Increase %

●

Benefits %

●

●

Hiring Growth %

●

●

●

Inflation %

●

●

●

Productivity Factor

●

Forecast Employee Cost

●

●

●

●

●

●

Assumptions can live at a broader grain than the employee-month formula that consumes them.



### Speaker notes



Use this matrix as the central reference for the deck. Purple dots identify the dimensions that jointly define each assumption. Hiring includes Year and Quarter, not independently editable Year and Quarter cells. Forecast Employee Cost uses the full detailed row and calendar grain. Department-only anchoring manages one shared value for each department across omitted parent dimensions. This explains how independently managed assumptions coexist with detailed formula outputs.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 6: Row-only, column-only and combined anchors



### Slide text



Row-only, column-only and combined anchors

An empty axis means the measure does not vary by that axis’s dimensions.

Fabric Planning   /   Anchor Measures

06

Row-only

Rows: Region

Columns: None

Scope

Total

Jan

North America

1.10

1.10

  Sales

1.10

1.10

    Ana

1.10

1.10

Column-only

Rows: None

Columns: Year

Scope

FY2027

Jan

All rows

4%

4%

  North America

4%

4%

    Ana

4%

4%

Combined

Rows: Region

Columns: Year

Scope

FY2027

Jan

North America

22%

22%

  Sales

22%

22%

    Ana

22%

22%

At least one dimension is required when anchoring is enabled. A Year-only policy is not a dimensionless constant.



### Speaker notes



Read the three patterns from left to right. Region-only places the factor at Region × Total, with no time variation. Year-only places a corporate assumption at All rows × Year. Region × Year introduces independent annual assumptions per region. The three grids use different measures: productivity factor, salary increase, and benefit rate. Gray detail values can still support formulas. The current requirement disallows both selectors being empty. The parent-child rows are conceptual examples, not three alternative allocations of the same measure.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 7: How an input reaches detailed calculations



### Slide text



How an input reaches detailed calculations

The existing distribution updates eligible detail. Formulas consume those resulting values.

Fabric Planning   /   Anchor Measures

07

1

Enter 4%

at FY2027

2

Existing

distribution

3

Stored detail

values = 4%

4

Salary

formula

5

Forecast

output

Employee / Month

Monthly base

Stored raise %

Forecast Salary

Ana / Jan 2027

$8,000

4%

$8,320

Ben / Jan 2027

$6,000

4%

$6,240

Copy example: Average (Leaf) plus existing distribution. Other settings may distribute differently.

Read-only due to anchoring can receive allocation. Locked and unauthorized cells remain protected.



### Speaker notes



Distinguish the grid restriction from the allocation engine. Users cannot edit an individual copied rate directly when that location is not the anchor. An allowed parent allocation can still update those children. Locked cells and independent write restrictions remain protected. This diagram does not introduce a new dynamic lookup or override formula evaluation. Both sample outputs are base salary multiplied by 1.04. The existing formulas consume the applicable values after distribution.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 8: Corporate annual salary increase



### Slide text



Corporate annual salary increase

HR sets one 2027 salary policy for every eligible employee.

Fabric Planning   /   Anchor Measures

08

Rows: None (All rows)

Columns: Year

Salary Increase %

Scope

FY2027

Jan

Feb

Mar

All rows

4%

4%

4%

4%

  Ana / North America

4%

4%

4%

4%

  Ben / Europe

4%

4%

4%

4%

  Chen / Asia Pacific

4%

4%

4%

4%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Forecast Salary =

Base Salary ×

(1 + Salary Increase %)

$100,000 × 1.04

$104,000

forecast annual salary

The policy belongs to the year. Employee-month cells use the same 4% without separate input.

Annual policy applied once. Monthly salary is $104,000 ÷ 12, not a repeated 4% compounding increase.



### Speaker notes



Business scenario: HR sets one 2027 salary policy for every eligible employee.

Planning Sheet grain: Region × Department × Employee × Year × Quarter × Month.

Anchor configuration: Rows None (All rows); Columns Year.

Assume the increase is effective from January for the full year. The annual base salary is $100,000, so the forecast is $104,000. The unrounded monthly forecast is $8,666.6667. The corporate assumption is entered at All rows × FY2027. With Average (Leaf) and the existing copy distribution, eligible employee-month leaves carry 4%. The purple cell is the only entry location in this example.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: The policy belongs to the year. Employee-month cells use the same 4% without separate input.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 9: Regional employee benefits



### Slide text



Regional employee benefits

Finance maintains one annual benefits policy for each region.

Fabric Planning   /   Anchor Measures

09

Rows: Region

Columns: Year

Benefits %

Region / Employee

FY2027

Jan

Feb

Mar

North America

22%

22%

22%

22%

  Ana

22%

22%

22%

22%

Europe

26%

26%

26%

26%

Asia Pacific

18%

18%

18%

18%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Total Employee Cost =

Salary Expense ×

(1 + Benefits %)

$8,000 × 1.22

$9,760

monthly employee cost

Regional policy explains the variation. Each employee uses the assumption for their own region.

The reference assumption is Region × Year. The calculation occurs at Employee × Month.



### Speaker notes



Business scenario: Finance maintains one annual benefits policy for each region.

Planning Sheet grain: Region × Department × Employee × Year × Quarter × Month.

Anchor configuration: Rows Region; Columns Year.

North America has a 22% benefit assumption, Europe 26%, and Asia Pacific 18%. There are three independent annual entry cells, not a separate annual cell for each employee. For a North American employee with $8,000 monthly salary expense, the total is $8,000 × 1.22 = $9,760. This example uses salary expense before any separate raise assumption. Slide 19 combines raises and benefits explicitly.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: Regional policy explains the variation. Each employee uses the assumption for their own region.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 10: Quarterly department hiring



### Slide text



Quarterly department hiring

Department leaders set hiring growth at the quarterly planning cycle.

Fabric Planning   /   Anchor Measures

10

Rows: Department

Columns: Year + Quarter

Hiring Growth %

Department / Role

Q1 total

Jan

Feb

Q2 total

Engineering

5%

5%

5%

3%

  Software engineer

5%

5%

5%

3%

Sales

8%

8%

8%

6%

  Account executive

8%

8%

8%

6%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Target Headcount =

ROUND UP [Baseline ×

(1 + Hiring Growth %)]

100 positions × 1.05

105 positions

Engineering Q1 target

A department sets the target once per quarter. Role-level plans consume the quarterly assumption.

2027 shown. Hiring dates, role mix and monthly phasing require separate business logic.



### Speaker notes



Business scenario: Department leaders set hiring growth at the quarterly planning cycle.

Planning Sheet grain: Business Unit × Department × Role × Year × Quarter × Month.

Anchor configuration: Rows Department; Columns Year + Quarter.

The department anchor combines Department with Year and Quarter. Engineering has Q1 growth of 5% and Q2 growth of 3%. Sales has 8% and 6%. Use a fixed 100-position Engineering baseline for each example quarter: Q1 is 105 and Q2 would be 103. Do not compound Q2 onto the Q1 target unless that is a separately specified model. Round up to whole positions. The quarterly target is not three monthly hires. Show Department grouped across business units using unique department identities. The formula notation expresses the business calculation.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: A department sets the target once per quarter. Role-level plans consume the quarterly assumption.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 11: Monthly inflation across departments



### Slide text



Monthly inflation across departments

Finance publishes one monthly uplift for eligible expense forecasts.

Fabric Planning   /   Anchor Measures

11

Rows: None (All rows)

Columns: Year + Quarter + Month

Inflation %

Scope / Expense account

Jan 2027

Feb 2027

Mar 2027

All rows

0.3%

0.4%

0.2%

  Finance / Travel

0.3%

0.4%

0.2%

  IT / Services

0.3%

0.4%

0.2%

  Operations / Supplies

0.3%

0.4%

0.2%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Adjusted Expense =

Base Expense ×

(1 + Inflation %)

$20,000 × 1.003

$20,060

January adjusted expense

The assumption varies by month, while departments share the same monthly value.

One-period uplift against each month’s baseline. This example does not use a cumulative inflation index.



### Speaker notes



Business scenario: Finance publishes one monthly uplift for eligible expense forecasts.

Planning Sheet grain: Region × Business Unit × Department × Account × Year × Quarter × Month.

Anchor configuration: Rows None (All rows); Columns Year + Quarter + Month.

The monthly rates are January 0.3%, February 0.4%, and March 0.2%. Each rate is a separate business input at All rows × the month. With a $20,000 baseline in each month, outputs are $20,060, $20,080, and $20,040. These are period-specific uplifts; they are not compounded sequentially. Year and Quarter selections identify the calendar context. All departments and accounts in the eligible scope use the relevant monthly value.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: The assumption varies by month, while departments share the same monthly value.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 12: Annual product price increases



### Slide text



Annual product price increases

Pricing teams set one annual increase per product across customers and regions.

Fabric Planning   /   Anchor Measures

12

Rows: Product

Columns: Year

Price Increase %

Product / Customer scope

FY2027

Jan

Feb

Mar

Product A / all regions

5%

5%

5%

5%

  Customer 101 / NA

5%

5%

5%

5%

Product B / all regions

3%

3%

3%

3%

Product C / all regions

7%

7%

7%

7%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Planned Selling Price =

Base Selling Price ×

(1 + Price Increase %)

$200 × 1.05

$210

Product A selling price

Product × Year shares the policy across regions. Region × Product × Year would create different inputs.

One shared product policy supports customer and monthly calculations across every region.



### Speaker notes



Business scenario: Pricing teams set one annual increase per product across customers and regions.

Planning Sheet grain: Region × Product × Customer × Year × Quarter × Month.

Anchor configuration: Rows Product; Columns Year.

Product A, B, and C have annual increases of 5%, 3%, and 7%. Product A has a $200 base selling price and a planned price of $210. At 1,000 units this supports $210,000 planned revenue, assuming no other discounts or pricing effects. Product is grouped across regions in this illustration so there is one editable annual value per product. This shared product policy applies across all regions. A separate editable value for each region would represent Region × Product anchoring.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: Product × Year shares the policy across regions. Region × Product × Year would create different inputs.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 13: Regional productivity factors



### Slide text



Regional productivity factors

Operations applies a region-specific factor to facility capacity plans.

Fabric Planning   /   Anchor Measures

13

Rows: Region

Columns: None (Total column)

Productivity Multiplier

Region / Facility

Total

Jan

Feb

Mar

North America

1.10

1.10

1.10

1.10

  Dallas facility

1.10

1.10

1.10

1.10

Europe

1.05

1.05

1.05

1.05

Asia Pacific

1.15

1.15

1.15

1.15

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Adjusted Capacity =

Base Capacity ×

Productivity Multiplier

50,000 × 1.10

55,000 units

monthly adjusted capacity

The model treats productivity as region-specific with no period variation in the anchor.

Enter at Region × Total. The monthly 1.10 values remain read-only and support facility calculations.



### Speaker notes



Business scenario: Operations applies a region-specific factor to facility capacity plans.

Planning Sheet grain: Region × Facility × Production Line × Year × Quarter × Month.

Anchor configuration: Rows Region; Columns None (Total column).

North America uses 1.10, Europe 1.05, and Asia Pacific 1.15. With no column anchor, each region input belongs in the Total column. North American base capacity of 50,000 units per month becomes 55,000. The multiplier applies to the base monthly capacity; it is not multiplied again each month. If the business later requires time-varying productivity, a period dimension belongs in the anchor. Capacity outputs retain their own aggregation rules.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: The model treats productivity as region-specific with no period variation in the anchor.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 14: Annual sales commission policies



### Slide text



Annual sales commission policies

Sales operations maintains commission rates by sales role and planning year.

Fabric Planning   /   Anchor Measures

14

Rows: Sales Role

Columns: Year

Commission %

Sales Role / Salesperson

FY2027

Jan

Feb

Mar

Account Executive

8%

8%

8%

8%

  Maya

8%

8%

8%

8%

Sales Manager

3%

3%

3%

3%

Channel Partner Manager

5%

5%

5%

5%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Commission Expense =

Eligible Sales ×

Commission %

$125,000 × 8%

$10,000

monthly commission expense

The role and year define the policy. Customer and product detail consume that policy.

Eligible sales, crediting rules and any commission tiers remain separate business logic.



### Speaker notes



Business scenario: Sales operations maintains commission rates by sales role and planning year.

Planning Sheet grain: Sales Role × Salesperson × Customer × Product × Year × Quarter × Month.

Anchor configuration: Rows Sales Role; Columns Year.

Account Executives use 8%, Sales Managers 3%, and Channel Partner Managers 5% for 2027. Maya is an Account Executive with $125,000 eligible monthly sales, creating $10,000 commission expense. This is a simple flat-rate illustration. It does not imply new commission-tier, split-credit, quota, or eligibility logic. The annual role input distributes the rate to eligible detailed intersections using the existing copy behavior.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: The role and year define the policy. Customer and product detail consume that policy.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 15: Annual department expense targets



### Slide text



Annual department expense targets

Management gives each department an annual cost-reduction target.

Fabric Planning   /   Anchor Measures

15

Rows: Department

Columns: Year

Cost Reduction %

Department / GL account

FY2027

Jan

Feb

Mar

Finance

5%

5%

5%

5%

IT

8%

8%

8%

8%

  Software subscriptions

8%

8%

8%

8%

Operations

4%

4%

4%

4%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Target Expense =

Baseline Expense ×

(1 − Cost Reduction %)

$50,000 × 0.92

$46,000

IT monthly expense target

Department leaders own annual targets. Account-month calculations use the relevant target rate.

A uniform target formula does not decide which accounts deliver the actual savings.



### Speaker notes



Business scenario: Management gives each department an annual cost-reduction target.

Planning Sheet grain: Department × GL Account × Year × Quarter × Month.

Anchor configuration: Rows Department; Columns Year.

Finance targets 5%, IT 8%, and Operations 4%. An IT software-expense baseline of $50,000 per month yields a $46,000 target under the uniform 8% reduction model. This defines a target calculation, not a detailed savings plan or a new allocation algorithm for absolute savings dollars. Actual savings may differ by account, contract, or month and require additional planning logic.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: Department leaders own annual targets. Account-month calculations use the relevant target rate.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 16: Quarterly manufacturing scrap rates



### Slide text



Quarterly manufacturing scrap rates

Plant teams estimate quarterly scrap to size detailed production requirements.

Fabric Planning   /   Anchor Measures

16

Rows: Plant

Columns: Year + Quarter

Scrap Rate

Plant / SKU

Q1 total

Jan

Feb

Q2 total

Plant A

2.5%

2.5%

2.5%

2.0%

  SKU 104

2.5%

2.5%

2.5%

2.0%

Plant B

3.2%

3.2%

3.2%

3.0%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Gross Production =

ROUND UP [Good Units

÷ (1 − Scrap Rate)]

10,000 ÷ 0.975

10,257 units

required gross production

The plant owns its quarterly scrap assumption. SKU-month calculations use that same rate.

2027 shown. Round 10,256.4103 up to whole units to meet at least 10,000 good units.



### Speaker notes



Business scenario: Plant teams estimate quarterly scrap to size detailed production requirements.

Planning Sheet grain: Plant × Production Line × SKU × Year × Quarter × Month.

Anchor configuration: Rows Plant; Columns Year + Quarter.

Plant A uses a 2.5% scrap rate in Q1 and 2.0% in Q2. Plant B uses 3.2% in Q1; an illustrative 3.0% Q2 rate completes the table. Required gross production for 10,000 good units at 2.5% scrap is 10,000 / 0.975 = 10,256.410256, rounded up to 10,257 units. Dividing by yield is important; simply adding 2.5% to 10,000 does not fully account for scrap. The rounding notation is conceptual.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: The plant owns its quarterly scrap assumption. SKU-month calculations use that same rate.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 17: Seasonal demand across stores



### Slide text



Seasonal demand across stores

Merchandising sets a shared quarterly uplift for the illustrative retail model.

Fabric Planning   /   Anchor Measures

17

Rows: None (All rows)

Columns: Year + Quarter

Seasonal Demand Uplift %

Scope

Q1 total

Q2 total

Q3 total

Q4 total

Nov

All rows

2%

5%

8%

15%

15%

  New York / Product A

2%

5%

8%

15%

15%

  London / Product B

2%

5%

8%

15%

15%

Average (Leaf) with existing copy distribution. Gray cells are read-only.

CONCEPTUAL FORMULA

Adjusted Demand =

Baseline Demand ×

(1 + Seasonal Uplift %)

1,000 × 1.15

1,150 units

November demand forecast

The illustrative quarterly assumption is shared by all stores and products.

2027 shown. Category-specific seasonality needs additional dimensions or calculation rules.



### Speaker notes



Business scenario: Merchandising sets a shared quarterly uplift for the illustrative retail model.

Planning Sheet grain: Region × Store × Product × Year × Quarter × Month.

Anchor configuration: Rows None (All rows); Columns Year + Quarter.

The model uses Q1 2%, Q2 5%, Q3 8%, and Q4 15% uplift. A November baseline of 1,000 units becomes 1,150. All rows × Q4 subtotal is the input location for the Q4 value; November is a read-only consumer of 15%. This is an uplift against each applicable month baseline, not a quarterly-volume phasing distribution or sequential compounding. Different category patterns would need added anchor dimensions or business logic.

All purple cells mark the configured input locations. Displayed non-anchor values are gray and read-only. For the rate/factor examples, assume Average (Leaf) with the applicable existing copy distribution enabled, valid leaf combinations, and authorized unlocked input scope. Anchoring itself does not choose or replace aggregation. Formulas are conceptual business formulas, not product syntax.

Why this grain: The illustrative quarterly assumption is shared by all stores and products.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 18: Several business grains can coexist in one model



### Slide text



Several business grains can coexist in one model

Each assumption has an owner and a level. The calculation combines the applicable detailed values.

Fabric Planning   /   Anchor Measures

18

Salary increase 4%

Year

Benefits 22%

Region × Year

Hiring growth 5%

Department ×

Year × Quarter

Workforce model

North America / Engineering

Jan 2027

105 positions

$10,150.40 per employee

Inflation 0.3%

Year × Quarter × Month

Other expense

$20,060

Assumption inputs

Detailed calculations

Planning outputs



### Speaker notes



Walk through four assumptions with different grains. The illustrative January workforce model uses a 100-position baseline, 5% department quarterly hiring growth, $8,000 monthly salary per employee, a corporate 4% raise, and 22% regional benefits. This produces 105 target positions and $10,150.40 employee cost per month. A separate $20,000 operating-expense baseline uses January inflation of 0.3%, giving $20,060. The diagram keeps inflation on the other-expense formula instead of incorrectly applying it to salaries by default. A fully staffed steady-state month is assumed; actual hire dates and role mix need separate logic.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 19: Formula measures consume the applicable detailed values



### Slide text



Formula measures consume the applicable detailed values

Conceptual formula: Forecast Employee Cost = Base Monthly Salary × (1 + Raise %) × (1 + Benefits %)

Fabric Planning   /   Anchor Measures

19

Employee / Region

Base salary

Raise %

Raised salary

Benefits %

Employee cost

Ana / North America

$8,000

4%

$8,320

22%

$10,150.40

Ben / Europe

$6,000

4%

$6,240

26%

$7,862.40

Chen / Asia Pacific

$5,000

4%

$5,200

18%

$6,136.00

January total

$24,148.80

4% comes from the annual corporate policy.

22%, 26% and 18% come from regional policies.

Hiding the input measure rows does not remove the underlying values from these supported calculations.



### Speaker notes



Use January records to show the actual arithmetic. Ana: 8,000 × 1.04 = 8,320, then × 1.22 = 10,150.40. Ben: 6,000 × 1.04 = 6,240, then × 1.26 = 7,862.40. Chen: 5,000 × 1.04 = 5,200, then × 1.18 = 6,136.00. Sum employee costs to 24,148.80. The corporate raise is the same detailed value for all three employees. Benefits differ by region. No assumption is independently entered in this calculation grid, and gray rates are read-only. The formula uses the detailed values supplied through the existing input/distribution behavior. It does not query a new anchor lookup API.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 20: Visibility changes the grid, not the formula inputs



### Slide text



Visibility changes the grid, not the formula inputs

Example: Benefits % anchored at Region × Year in the measures-on-rows layout.

Fabric Planning   /   Anchor Measures

20

Display across all levels: ON

Display across all levels: OFF

Measure instance

FY2027

Jan

NA / Benefits %

22%

22%

  Ana / Benefits %

22%

22%

  Ana / Employee Cost

$121,804.80

$10,150.40

Measure instance

FY2027

Jan

NA / Benefits %

22%

22%

  Ana / Employee Cost

$121,804.80

$10,150.40

The extra Benefits % row stays visible,

but its cells cannot accept direct entry.

The non-anchor Benefits % row disappears.

Employee Cost keeps the same result.

Show gray detail for transparency, or hide repeated measure rows for a cleaner view.



### Speaker notes



The ON view shows a region-level annual benefit anchor and a repeated employee-level benefit row. Only the purple annual cell is editable. The OFF view removes the non-anchor employee benefit row while retaining the employee-cost formula. The region benefit row still spans monthly columns in this illustration because those columns are shared with other measures. The remaining shared cells are read-only and do not create additional input locations. In default layout, period-level measure columns can be omitted inside non-anchor blocks. In measures-on-columns layout, the measure block can retain only relevant period levels. No layout change deletes input values or changes formulas.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 21: Reporting measures can appear only where useful



### Slide text



Reporting measures can appear only where useful

Display anchoring can reduce repetition while preserving the existing calculation.

Fabric Planning   /   Anchor Measures

21

YTD Revenue (March 2027)

Native Power BI measure

Region

YTD at Total

Jan revenue

North America

$330,000

$100,000

Europe

$240,000

$70,000

Rows: Region. Columns: None.

YTD appears in Total, not each month block.

Quarterly Operating Margin %

Formula measure

2027 Q1

Revenue

Profit

Margin %

North America

$500,000

$75,000

15%

Europe

$400,000

$48,000

12%

Rows: Region. Columns: Year + Quarter.

The existing profit ÷ revenue formula stays intact.

Anchoring adds neither YTD logic nor edit rights. Both reporting measures remain calculated results.



### Speaker notes



These are two supported reporting examples. YTD Revenue is a native semantic-model measure whose existing calculation stays intact. For the illustrative as-of-March context, North America monthly revenues are 100,000, 110,000 and 120,000, giving YTD 330,000. Europe has 70,000, 80,000 and 90,000, giving 240,000. Only January fact columns are shown beside the Total YTD measure in the compact table. The Region anchor shows one YTD result per region in the Total column. The operating-margin example is the existing quarter profit divided by quarter revenue: 75,000 / 500,000 = 15%, and 48,000 / 400,000 = 12%. Anchoring does not average monthly percentages or create time intelligence. Formula-measure anchoring places the margin result at the relevant reporting level.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 22: Configuration in the measure panel



### Slide text



Configuration in the measure panel

The same controls apply to data input, formula and native measures.

Fabric Planning   /   Anchor Measures

22

1

Open a measure panel or Manage Columns

2

Turn on Enable Anchor Measure

3

Select Row Dimension, if it varies by rows

4

Select Column Dimension, if it varies by time

5

Choose Display measure across all levels

6

Apply the settings, then review the grid



### Speaker notes



The screenshot is the UI reference supplied by the user, not a newly captured production build. It shows the enable toggle, selected row chips, and the Year/Quarter/Month checkbox dropdown. Visibility control is specified in the feature requirements but is not visible in this crop of the provided UI. Either dimension selector may be empty, but at least one dimension is required with anchoring on. For newly created measures the action is Create; editing an existing measure uses the applicable save/apply workflow. Manage Columns provides access to anchor configuration for native measures and other existing measures. It uses the same anchor settings as the measure panel.

Sources and status: User-supplied screenshot codex-clipboard-8595e9d7-fe00-4514-98c6-160560582062.png; feature summary sections 3–4 and latest chat implementation updates.



## Slide 23: The grain follows the business decision



### Slide text



The grain follows the business decision

Choose the dimensions that explain independent changes in the assumption.

Fabric Planning   /   Anchor Measures

23

Business question

Example decision

Who owns an independently different value?

Region for benefits, Product for pricing

When can the assumption change?

Year for salary policy, Quarter for hiring

Which detail should share the same value?

All eligible employees within that scope

How should input reach the detail?

Copy rates with Average (Leaf). Review amount allocation.

Which calculation uses the resulting value?

Employee Cost, Target Headcount or Planned Price

A rate and an absolute pool need different distribution choices.

Example: a 5% bonus rate may copy to employees. A $1 million bonus pool needs an explicit allocation method.



### Speaker notes



Use this framework during solution design. Select a row dimension only if it identifies an independently managed value. Select the required time grain when the business can change the assumption at that cadence. Specify who and what belongs in the eligible scope, then choose the existing aggregation/allocation behavior. A percentage rate and an absolute amount are not interchangeable. A $1 million pool must not be copied to each employee as though it were a rate. At least one dimension defines the anchor when anchoring is enabled.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 24: One sheet, several business decisions



### Slide text



One sheet, several business decisions

Revenue, assumptions and employee cost coexist at the levels that fit each measure.

Fabric Planning   /   Anchor Measures

24

Hierarchy / Measure

FY2027

Q1 total

Jan

Feb

Mar

All / Salary Increase %

4%

4%

4%

4%

4%

North America / Benefits %

22%

22%

22%

22%

22%

  Sales / Ana / Revenue

$144,000

$36,000

$12,000

$12,000

$12,000

  Sales / Ana / Salary Increase %

4%

4%

4%

4%

4%

  Sales / Ana / Benefit Rate %

22%

22%

22%

22%

22%

  Sales / Ana / Forecast Employee Cost

$121,804.80

$30,451.20

$10,150.40

$10,150.40

$10,150.40

Revenue uses the detailed facts. Salary and benefits use broader input grains. Employee cost consumes both.

Purple: editable anchor

Gray: read-only value

Teal: formula

Green: calculated output



### Speaker notes



This is an illustrative measures-on-rows view with non-anchor instances displayed. The annual salary increase is editable only at All × FY2027. Benefits are editable only at North America × FY2027. Ana sits in Sales under North America. Revenue is a blue planning fact of $12,000 each month, giving Q1 $36,000 and annual $144,000. Ana has $8,000 monthly base salary, a 4% raise and 22% benefits. Employee cost is $8,000 × 1.04 × 1.22 = $10,150.40 each month, Q1 $30,451.20, and year $121,804.80. Rates remain gray at non-anchor instances. This salary base is a different illustrative employee from the $100,000 annual salary case on slide 8.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 25: Fewer assumption locations, clearer planning ownership



### Slide text



Fewer assumption locations, clearer planning ownership

The business manages the policy at its own level while detailed calculations keep their full grain.

Fabric Planning   /   Anchor Measures

25

1

annual corporate policy

24,000

eligible employee-month calculations

Planning benefit

What changes for the user

Clear ownership

HR maintains the annual salary policy once.

Consistent detail

Eligible calculations consume the same policy value.

Cleaner grids

Non-anchor measure instances can be hidden.

Maintainable models

Assumption management stays separate from formula outputs.



### Speaker notes



Return to the model-size illustration: a single annual policy can supply 2,000 employees across twelve months, assuming all intersections are eligible. This shows the relationship between the number of independently managed values and detailed calculations. It is not a measured reduction in effort or a benchmark against another product. The benefits are concrete: the policy has a clear owner, detailed formulas use consistent assumptions, the grid can omit repeated measure instances, and the model separates assumptions from outputs. Existing bulk-entry tools are not being compared or replaced.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.



## Slide 26: Anchor Measures



### Slide text



Anchor Measures

Fabric Planning   /   Anchor Measures

26

Enter assumptions

at the right grain.

Use their values throughout

your detailed planning model.

Annual policies. Regional rates. Quarterly targets. Detailed outcomes.



### Speaker notes



Close by repeating the business principle: assumptions belong at the level where the business defines and manages them. The detailed model can continue using the resulting values at its own grain. Invite the audience to name one assumption they currently maintain too many times and identify its true row and time dimensions. Invite them to choose the business owner, row level and time period for that assumption, then show how the detailed plan uses its value.

Sources and status: Supplied feature summary and team discussion. All business data is illustrative.


