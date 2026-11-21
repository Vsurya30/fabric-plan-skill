> v30: [Measure-weighted distribution](measure-weighted-distribution.md) is now constructible for the captured Column / All dimensions / another Measure / source Row Use Self profile. Discover RULES or weights from another measure; use `construct-native weighted-rule`. Saved configuration is confirmed, not allocation execution. Other reference profiles and bookmark restore remain separate gaps. All prior fixes remain.

> v19: Every new Planning grid uses explicit row GT Top, row subtotal Top,
> column GT Left, column subtotal null/OFF. Preserve intentional overrides.
> Read [planning-totals-defaults.md](planning-totals-defaults.md). Measure-based
> roll-forwards recommend Measures in Rows + native Measure Model; discover
> ROLL-FORWARD and read [roll-forward-authoring.md](roll-forward-authoring.md)
> plus the complete supplied [formula reference](roll-forward-formula-patterns.md).

> 2026-11-14 numeric-input correction: [numeric-input-constraints.md](numeric-input-constraints.md) is authoritative for whole-number static min/max bounds and AverageLeaf parent distribution. Decimal defaults/formulas are separate; preserve existing percentage units and IDs.

> 2026-11-14 active formatting and identity update: read [matrix-formatting.md](matrix-formatting.md) and [dimension-leaf-keys.md](dimension-leaf-keys.md). Use `plan.py format-matrix` for selected typed formatting and `plan.py leaf-key-mapping` for stable leaf storage defaults. These newer, revision-qualified contracts supersede conflicting older general examples; original source documents remain intact. Formatting is offline-tested, not render-certified. The complete existing native CF seed is not claimed to be an exact copy of the newer source constants.

> Current selected-branch execution: [forecast-authoring.md](forecast-authoring.md) provides working-reference defaults; [forecast-review-execution.md](forecast-review-execution.md) provides runnable From Sheets, formatting and chart constructors. These supersede older missing-writer statements for these branches, not unrelated advanced contracts.

> Current construction supplement: `connected-construction.md` supplies executable ID/Skip descriptors, SQL lookup columns, additive append normalization, linked Native companions and embed references. Follow verified-authoring-flow.md for execution: preserve requested components, use documented phases, and continue independent supported work without automatically deploying a reduced substitute. Original detailed business and property explanations below remain preserved.

> Active Context/Intelligence construction addendum: read `references/context-intelligence.md`. External Context stays outside the grid and passes the selected scope into Planning; ordinary semantic slicers are separate. The executable constructor now covers Context, slicers, cards, text and page-local embedded geometry. Scenario rows and grid-only dashboards are not equivalent substitutes. Preserve feature-level omissions and separate saved-state checks from behavior verification.

> Standalone edition: read [runtime-guide.md](runtime-guide.md) for construction and deployment. Source checkout and historical task links below are optional provenance, not runtime prerequisites. Original feature explanations are preserved; the API-only runtime guide and gap inventory distinguish implemented APIs from blocked contracts. Historical UI steps are not execution instructions.

# Fabric Plan Supporting Feature Contracts

> Current module routing: use [module-routing.md](module-routing.md) or
> `python plan.py discover --module <ID>` for all F01-F30 and cross-cutting workflows.
> It connects business examples to real commands/callables and distinguishes base
> provisioning, separate phases and actual gaps. Preserve the latest targeted
> fixes; historical coverage statements below are release-scoped.

## Purpose and Status

Use [Fabric Plan Business Authoring](runtime-guide.md) as the primary create/update entrypoint for functional business requests. This document supplies reusable feature knowledge, verified property/ALM contracts, lifecycle operations, examples and investigation guidance for that workflow; ordinary users need not identify modules or provide JSON.

Use these internal contracts to investigate, construct, update and review the feature catalog below. Its verified knowledge is attributed to implementation owners, ALM writers/readers and public schemas. Explicitly supplied Fabric Plan definitions may additionally illustrate serialization and feature composition, with observed-example status rather than current-runtime certification. The contracts remain partial; this reference does not certify complete artifact generation or production registration.

> Generate only requested business features plus the mandatory presentation baseline from evidenced contracts. Never invent keys, nesting, types, enum literals, defaults, IDs, or serialization. Preserve unrelated siblings. A native state example is not an ALM part, and a valid JSON fragment is not a deployable artifact. Stop the affected feature when its persistence/export/import boundary is unresolved.

> **Design authority.** Derive a new Plan from the current user's functional request, the supplied semantic model and available data, verified platform/property contracts, and the shared presentation/validation standards. Do not inherit pages, measures, flows, rates, dates or resource identities from previous applications or unrelated conversation history. A reference Plan is not required and must not be used as a creation template.

> **Execution authority.** A business request to create a Plan enters the [business authoring workflow](runtime-guide.md), even when the user supplies only these two guiding documents. Partial catalog coverage, an unavailable AI schema adapter, or unexecuted runtime checks are not blanket creation blockers. Resolve the requested route through [contract-gap resolution and route fallback](#contract-gap-resolution-and-route-fallback), construct and save supported native content, then verify the actual saved outcome. Never substitute a blueprint or empty shell for the requested application.

For updates, inspect the user's specified current artifact and relevant dependencies to preserve its configuration and input identities. Keep that resource-specific baseline outside the reusable library; it is update context, not a template for another application. A model metadata read or name-collision check does not authorize searching other Plans for reusable designs.

This document is the supporting contract and evidence reference for the skill. Load relevant sections explicitly; this document's filename/location does not enable automatic skill discovery.

## Mandatory Presentation Baseline

For every artifact creation/update, follow the shared [Fabric Plan Presentation and Layout Standards](design-standards.md). It owns presentation requirements and separate definition/rendered checks; it does not prescribe a business domain, page list or calculation flow. Report unresolved settings rather than inventing native properties.

## When to Use

Use for Fabric Plan definition review, native feature-setting construction and source-backed changes involving the catalog below, Charts formatting or native calculated/input measures. Use Plan Item Lifecycle for documented item operations. Live calls require authorization and verified prerequisites. Do not use Power BI report definitions, copied application state or permissive property bags as Plan constructors. Determine a supplied file's actual format from its contents: a filename containing `report-definition` can still contain native Fabric Plan parts.

Use Intelligence Dashboard Patterns for request-specific overview design, visual selection, layout and interactions. Dashboard requests do not imply input planning, writeback or cross-domain integration.

## Business-to-Feature Composition

Start with the business decision, not source-code discovery. For each requested area, map **source -> editable driver -> formula -> connected result -> review**, using the current semantic model's fields and business meaning. The following are conceptual feature recipes, not native expressions, preset pages or defaults to inject into every application.

| Business intent | Compose the relevant features | Calculation and connection judgment |
| --- | --- | --- |
| Sales or revenue forecasting | Eligible product/customer/region/channel axes; source prices; quantity, price and discount inputs; calculated revenue; commercial review. | Gross revenue = quantity * price; discount amount = gross revenue * discount rate; net revenue = gross revenue - discount amount. Use the requested grain and units. Price/discount can be source-only when users do not need to change them. |
| Workforce budgeting | Stable employee keys and eligible effective-dated assignments; applicable salary source/default; requested pay and compensation inputs; employment-cost formulas. | Prorate applicable pay for employment/assignment dates, apply increases before the requested additional costs, and convert using the applicable currency/month. Split within-month changes when required; a monthly label is not proof of a full month of employment. |
| Supply or product costs | From Sheets/From Queries planned quantities; source standard costs; editable cost/inflation assumptions; calculated costs. | Cost = the connected sales quantity * adjusted unit cost. Keep one authoritative volume input; do not ask operations to re-enter sales quantities. Match product/region/channel/month/version keys. |
| Operating expenses | Eligible department/region/account intersections; monthly amount inputs; currency conversion; account-category summaries. | Separate expense types needed by the request and exclude contributions already supplied by workforce or product-cost plans. Do not infer eligible combinations solely from transactions. |
| Profitability or consolidated finance | Connected domain outputs; common dimensional grain; calculated income statement and ratios; account detail and executive visuals. | Normalize and aggregate contributions before combining them. Derive gross profit, EBITDA and operating income from the requested classification. Calculate margins from aggregated numerators/denominators, not summed leaf percentages. |
| Actuals with an open forecast | Native Forecast when suitable, or supported inputs/formulas with actual-source branches; window/version controls and bounded inputs. | Separate value display from edit permission. Retain saved closed-version forecasts and show recorded actuals where the request requires them; do not inherit a sample's dates or actuals-overwrite choice. |
| Maintaining planning members | PowerTable over authorized master/assignment/eligibility/version sources; validation and effective dates; refreshed eligible planning axes. | New eligible members must not require historical facts. Keep stable IDs separate from editable names and respect existing source keys/constraints. Maintenance is not authorization to provision forecast storage or grant access. |
| Business review and navigation | Request-specific Intelligence KPIs/charts, selections, clear introductions and roomy planning workbenches; optional supported maintenance and comparison surfaces. | Choose visuals for decisions: trends for timing, regional comparisons for differences, and connected sales/cost/headcount/expense views for cross-team review. Do not clone sample layouts or decorative page lists. |

Use only recipes relevant to the request. Set defaults and allowed ranges from the user's requirements and verified model semantics; clarify material ambiguity rather than adopting demonstration assumptions. Decide weighting, totals, blank/zero behavior and parent editing independently of leaf formulas.

### Functional Design and Planning Strategy

The supplied Functional Design Guidelines v2 adds a business-first design sequence: outcome -> sheet responsibilities/dependencies -> Rows/Columns/Values and context -> input/forecast behavior -> calculation chain/final outputs -> Pivot/connections -> layout, aggregation, formatting and input controls. This supplements the execution contract: a concise design is an intermediate artifact, not a blueprint-only substitute for an authorized working Plan. The guide's strategy-deck references are attributed evidence, not independent review of that deck or runtime acceptance.

#### Independent Planning Decisions

| Decision | Selection rule | Important distinction |
| --- | --- | --- |
| Sheet boundaries | Separate owners, planning grains or workflows when justified; name each final output and downstream consumer. | Alternate summaries of common data generally need Pivot views, not duplicate sheets or inputs. Separate sheets do not themselves enforce access isolation. |
| Base grain and entry grain | Define row dimensions, stable member identities, detailed period, measure and scenario/currency/filter context; separately specify a summarized entry view. | A field is not its member; employee names need stable identities. Hidden/filtered context still participates in the planning intersection. |
| Ordinary measure-based planning, Measure Model or Row Model | Start with measures evaluated for business entities. Add Measure Model for logical measure hierarchy authoring; use Row Model when the requirement authors business row members or their individual behavior. | Neither hierarchy editor is required for ordinary input, Forecast or formula measures. Measures in Rows is presentation, not conversion to a Row Model. Follow the [model-selection decision](#measure-based-planning-versus-row-authoring). |
| Ordinary input versus Forecast | Existing-period entry/override without a closed/open boundary can use ordinary input. Locked history plus open planning is sufficient reason for Forecast even when future periods already exist. | A business word such as forecast or a supplied ML measure does not imply trained prediction, native Forecast or time extension. |
| Default versus governed input versus output | A supported formula/measure default initializes an independently editable input; Driver-Based Planning governs an eligible Data Input target; a formula measure computes an output. | A calculated source can drive an input without becoming writable. Do not substitute On Change actions for ordinary formula dependencies. |
| Scope versus grouping | Context filtering defines eligible loaded scope; Pivot groups that scope for entry/review. | Neither grants access, reaches unloaded detail automatically, or chooses the distribution algorithm. |
| Cube versus Pivot | Cube makes an owned source assumption, target breakdown and reference-share basis explicit. Pivot offers alternate views over common base detail. | High-level entry alone does not establish a need for Cube; cross-fact enhancement examples do not establish shipped support. |
| Anchor versus allocation | Anchor places an assumption at its row/time decision level, retaining existing formulas, input capability and distribution. | Annual policy is not a January-only value; anchoring does not create allocation or make a source/formula measure editable. |
| Direct output versus lookup versus prepared data | From Sheets/Blend for compatible same/subset grain; Advanced Lookup for a keyed reference value; InfoBridge for mapping, joins, reshaping, append or reusable preparation. | Fewer dimensions means compatible subset grain, not merely fewer selected members. Coarse data cannot invent finer detail. |

For multiple submissions/versions, establish the actual scenario or series representation. The guide's explicit measure-per-series example needs additional corresponding measures as series increase; it is not the only permitted versioning architecture. In the Row Model example, Revenue 100/120 and Marketing 10/12 yield Revenue less marketing 90/108 across Actuals/Forecast, not total profit. In an ordinary measure-based example, Quantity 1,200 and Price 100 produce Revenue 120,000 without requiring the Measure Model editor; layout does not change those entities into account rows.

Use semantic-model fields on Rows/Columns wherever suitable and connected planning outputs in Values. Time assignments must follow a valid calendar: monthly Year/Quarter/Month or Year/Month; quarterly Year/Quarter; weekly Week Year/Week; fiscal year/period/week; daily Date. Calendar weeks can cross months, so Year/Quarter/Month/Week is not a valid universal hierarchy. Existing model periods, extended horizon, detailed input period and closed/open boundary are separate requirements. Model axes alone do not prove RLS enforcement through connected sources.

#### Measure-Based Planning Versus Row Authoring

The detailed Measure Planning versus Row Model functional guide clarifies the earlier broad use of Measure Model. **Ordinary measure-based planning is the starting workflow, not a separately named product mode.** The phrases measure model without hierarchy and measure model with hierarchy are explanatory shorthand, not commands or serialized mode values. Model -> Measure Model adds logical measure hierarchy authoring; Model -> Row Model authors business row members and their behavior. Measures in Rows independently chooses where measure labels appear.

Make the decision in this order:

1. Locate metric identity: are Quantity, Price, Hours, Revenue or Cost measures evaluated for entity/time intersections, or intended members of an authored account/KPI row hierarchy? Inspect the current model/owner when labels are ambiguous.
2. For measures, start with ordinary Number inputs, Forecast and explicit formula measures as needed. Keep a flat presentation when sufficient; add Measure Model when users need expandable logical groups. A formula calculates without a display hierarchy, and grouping does not supply a formula.
3. Use Row Model for requested child/sibling business rows, deeper authored account structures or independently configured row formulas/source/input/aggregation. Preserve existing source hierarchies when they already satisfy the request; do not convert objects solely to resemble a screenshot.

| Request or observed structure | Select / preserve | Discriminating check |
| --- | --- | --- |
| Revise quantity by Region/Product using a baseline | Ordinary Number input and any dependent formula measures | No new business row members; baseline resolves at the target entity/period. |
| Show actuals through October and edit November/December | Ordinary Forecast measure with appropriate closed/open behavior | The time horizon includes the periods; open-period defaults actually return future values. |
| Explain fifty existing metrics in expandable groups | Measure Model plus an eligible Measures in Rows view | Nodes remain registered measures; their definitions and input identities are preserved. |
| Display existing metrics vertically | Measures in Rows; Measure Model only if grouping is needed | A flat stack beneath Region/Product remains measures, not authored account members. |
| Review an existing GL/account hierarchy or complex DAX P&L | Preserve source rows and suitable measure calculations | Existing GL rows, financial terminology and source calculation complexity alone do not require Row Model. |
| Add Overtime Hours/Rate beneath Salaries or different formulas to individual account rows | Row Model | The new objects are row members with their own type/logic, not just displayed measure labels. |

Both approaches can express a P&L, have inputs/formulas and display expandable structures. Industry, row count, hierarchy depth, the word driver and the presence of a forecast do not choose the model. A product hierarchy identifies business members; a measure hierarchy groups metrics; an authored row hierarchy defines business row nodes. Driver-Based Planning is a separate eligible-input relationship, not another name for Measure Model or a requirement to use DriverRow.

For ordinary authoring, resolve Rows/entity grain, Columns/time and Values/source measures; use Insert Column -> Number with the period-repeating measure placement for an editable metric, not a one-off visual attribute. Choose supported static/measure/formula/blank defaults, preserving original actuals; ongoing calculated outputs belong in formula measures. Forecast adds period behavior, not missing future source values. Consult [input authoring](#input-and-formula-measure-authoring) and [Forecast](#rolling-forecast-authoring) for exact supported settings.

Treat entity subtotals as measure-specific calculations, not universally additive sums. Amounts, prices, hours, rates and balances need their own grain and total semantics. A measure parent does not sum mixed-unit descendants by virtue of their placement. A shared Quantity dependency can appear once under Revenue while COGS references it independently; the explanation tree need not reproduce the dependency graph. See [measure hierarchy](#measure-hierarchy-authoring) and [Row Model](#row-model-business-authoring) for the corresponding owner contracts.

A concise recommendation should state entity grain/time, metric identity, override/default/formula behavior, historical/open-period policy, optional hierarchy presentation and total semantics. Derive these from available context rather than forcing seven new questions. Then execute an authorized create/update under the existing execution contract; a recommendation is not a claim that the Plan was configured. Acceptance distinguishes source members, authored rows and measures, checks a representative edit and totals, retains signs/units and tests actual save/reopen and rendering separately.

#### Input and Strategy Patterns

- **Editable source override:** retain the original model measure as a dependency; create an eligible Number Visual measure with Default Value Measure for period-specific entry. Hide the baseline only when appropriate, then use a comparison rule to mark meaningful differences. A changed value versus baseline is not edit history; entering the original value leaves no difference. Copy from another series is a starting copy, not a live source-linked default.
- **Actuals plus forecast:** resolve closed-period source/formula, open mode and default independently. Only open Data Input supports direct override; Formula as its default differs from top-level read-only Formula mode. A source lacking values in the requested period cannot initialize those values, and same-period references do not automatically shift last year's actuals forward.
- **Commentary and dropdown placement:** use a Visual measure when the value repeats by planning period; a Visual column for one field per relevant row. One-time commentary is not one shared note for the whole sheet. Check type/placement-specific default and On Change limitations before creation.
- **Semantic-model single-select:** the guide recommends a stable option ID plus visible label and Arrow styling when appropriate; Chip/Plain remain alternatives. Option identity is distinct from the row's Dimension ID Mapping. Preserve a choice across a label rename only through the supported ID/refresh behavior, not by matching label text. Arrow-only activation is the guide's UI description, not a verified native event contract here.
- **Driver-Based Planning:** the strategy guidance describes one source, operation and operand determining an eligible Data Input target, with no inferred back-solving or arbitrary operation chain. A source can be native, calculated or input where supported; a formula output is not the writable target. Revenue 100 -> 120 with a 10% rule gives Marketing 10 -> 12. Verify target/type/period eligibility in the selected implementation; a business row named Driver need not use the Driver Input row type.
- **Annual anchor:** 4% at All Employees/Year applied once to annual salary 100,000 yields 104,000. It does not imply monthly compounding or a new copy-distribution rule. The supplied strategy leaves partial-Pivot write semantics unresolved; retain the [anchor contract](#anchor-assumption-authoring).
- **Scope-preserving Pivot:** with proportional allocation explicitly configured, North A/B 60/40 becomes 72/48 after a target of 120. South A/B remains 30/20. Restored authorized review shows region totals 120/50, product totals 102/68 and grand total 170. Reconciliation does not authorize writes outside loaded/eligible scope.
- **Owned Cube pool:** Marketing 12,000 allocated over eligible same-reference-fact SKU revenues 72,000/48,000 gives 7,200/4,800. Define denominator scope, period, zero/missing drivers, locks and rounding. A governed regional input and allocated SKU output have distinct roles; composing Driver-Based Planning with Cube requires verified target compatibility, not a presumed all-in-one wizard.

Follow the existing [input authoring](#input-and-formula-measure-authoring), [forecast](#rolling-forecast-authoring), [Pivot](#pivot-view-authoring), [Cube](#cube-planning-authoring), [lookup](#advanced-lookup-authoring) and [Row Model](#f11-row-model) contracts. These business patterns are not new native payloads or paste-ready formula syntax.

#### Use-Case Starting Grains

The guide's twenty examples are selection aids, not mandatory fields or prebuilt sheet sets. Resolve actual keys, source measures, time/calendar, units and eligible combinations from the current model. Each can use ordinary inputs, Forecast or a mixture according to period behavior.

| Use case | Candidate detailed row grain | Primary output / cadence |
| --- | --- | --- |
| FP&A | Entity, Cost Center, Account | Financial plan/latest estimate; month. |
| Workforce | Region, Department, Employee or Position | Loaded compensation; month. |
| SG&A | Entity, Department, Expense Account | Planned departmental expenditure; month. |
| Sales | Region, Product, Channel; Customer if needed | Final quantity and revenue; month. |
| Cash | Entity, Cash Flow Category, relevant Customer/Vendor group | Movements and closing cash; week or month. |
| Retail merchandise | Store, Category, SKU | Sales, receipts and ending inventory; fiscal week. |
| Trade promotions | Customer/Account, Product, Promotion | Incremental volume and promotion cost; month/fiscal week. |
| Production/COGS | Plant, Product, applicable Production Line | Production and cost; month/week. |
| Procurement | Purchasing Entity, Material, Supplier | Purchase quantity and spend; month. |
| Logistics | Origin, Destination, Mode, Carrier | Loads, freight and utilization; week/month. |
| Professional services | Practice, Project, Role or Consultant | Hours and service revenue; week/month. |
| Capital projects | Project, Work Package, Cost Category | Remaining cost and estimate at completion; month. |
| Healthcare | Facility, Service Line, Staff Category | Activity, staffing hours and cost; week/month. |
| Hospitality | Property, Room Type, Customer Segment | Sold nights and room revenue; date/month. |
| SaaS | Region, Product/Plan, Customer Cohort | Subscribers and recurring revenue; month. |
| Banking | Business Unit, Product, Customer Segment | Balances, income and cost; month. |
| Insurance | Legal Entity, Line of Business, Channel | Premium, claims and operating result; month. |
| Utilities | Territory, Customer Class, Service/Energy Product | Demand, revenue and supply cost; month/day. |
| Education | Campus, Program, Student Cohort | Enrollment, tuition and staffing; academic term/month. |
| Public/nonprofit | Fund/Grant, Program, Department, Expense Account | Spending and funding balance; fiscal period. |

#### Ordinary Measure-Based Planning Examples

The detailed comparison guide supplies twenty ordinary measure-based use cases, complementing the broader starting-grain catalog above. The following are candidate designs, not required pages or available source inventories. Use suitable source measures in Values and existing business dimensions on Rows; Year/Quarter/Month is illustrative, not mandatory for weekly, daily or fiscal processes. Verify actual keys, relationships, units, source availability and period context. Add Number inputs for overrides, Forecast for required historical/open-period behavior, and formula measures for outputs. The optional grouping column does not require opening Measure Model before authoring those measures.

| Industry / decision | Candidate entity grain | Metrics to source or plan | Optional measure grouping |
| --- | --- | --- | --- |
| Consumer goods demand | Region/Channel/Category/SKU | Quantity, selling price, revenue, unit cost | Revenue drivers; COGS drivers |
| Retail sales and margin | Country/Store/Department/SKU | Units, net sales, unit cost, margin | Margin -> Sales and COGS |
| B2B customer orders | Customer Segment/Sales Representative/Bill-to Customer/SKU | Order quantity, net price, revenue | Revenue -> Quantity and Price |
| Manufacturing conversion | Region/Plant/Product Family/SKU | Production units, materials/unit, labor hours/unit | Production Cost -> Materials, Labor, Freight |
| E-commerce contribution | Country/Marketplace/Category/SKU | Orders, units/order, net price, fulfillment cost | Contribution -> Sales, Returns, Fulfillment |
| SaaS subscriptions | Geography/Customer Segment/Product/Subscription Tier | Active/new accounts, churn, revenue/account | Subscription Revenue drivers |
| Telecom subscribers | Region/Sales Channel/Service/Tariff Plan | Subscribers, activations, disconnects, ARPU | Revenue -> Subscribers and ARPU |
| Hospitality rooms | Country/City/Hotel/Room Type | Sold/available room nights, daily rate | Room Revenue -> Sold Nights and Rate |
| Aviation passengers | Operating Region/Route/Cabin | Passengers, fare, ancillary revenue | Passenger Revenue components |
| Healthcare capacity | Region/Facility/Specialty/Service | Visits, revenue/visit, staff hours/visit | Service Result -> Revenue and Staffing |
| Logistics delivery | Region/Depot/Customer/Service Type | Shipments, rate/shipment, fuel, handling | Margin -> Freight Revenue and Delivery |
| Professional services | Region/Practice/Project/Role | Billable hours, billing rate, cost rate | Project Margin -> Fees and Delivery |
| Construction work | Region/Project/Work Package | Completed/remaining units, cost/unit, labor hours | Work Cost -> Materials, Labor, Subcontracting |
| Energy generation | Region/Site/Generation Technology | MWh, realized price/MWh, operating cost | Generation Result -> Revenue and Cost |
| Banking service operations | Region/Branch/Customer Segment/Service | Transactions, fee/transaction, processing hours | Service Contribution -> Fees and Processing |
| Workforce compensation | Region/Business Unit/Department/Job Family | Headcount, FTE, salary/FTE, benefits rate | Compensation -> Salary, Benefits, Other Costs |
| Higher education tuition | Campus/Faculty/Program/Student Type | Enrollment, tuition/student, aid/student | Net Tuition -> Gross Tuition and Aid |
| Nonprofit delivery | Region/Program/Funding Source | Donors, donation, participants, cost/participant | Funding sources and Program Cost drivers |
| Public-service resources | Agency/District/Service | Requests, hours/request, cost/hour | Service Cost driver chain |
| Commercial property rents | Region/Property/Unit Type | Leased area, rent/area, service charges | Rental Income components |

These are not twenty reasons to add Row Model. For example, Department/Job Family with FTE and Salary measures is ordinary measure-based planning; adding Regular Hours and Overtime Rate as authored children of an existing Salaries account is a different row-authoring request.

**Existing-period override:** at one Region/Channel/Month, SKU A/B actual quantities 1,000/500 and prices 10/20 yield source revenue 20,000. Create Reviewed Quantity with the applicable actual measure default; edit the new input to 1,200/600 and calculate Reviewed Revenue at SKU detail: 12,000 + 12,000 = 24,000. Source actual quantities remain 1,000/500. Neither hierarchy editor is needed. This example does not establish that actuals can default future periods or that all default changes overwrite saved input.

**Grain and totals counterexample:** original quantity totals 1,500 and revenue totals 20,000 imply quantity-weighted price 13.3333, not the simple mean 15. Total quantity * simple mean gives the incorrect 22,500. Configure detail calculation and higher-level aggregation deliberately; nesting Price under Revenue cannot repair this error, and an Average (Leaf) selection is not automatically quantity weighting.

**Forecast without hierarchy authoring:** at one Region/Product/year, January-October actual quantity totals 10,000. November/December budget defaults 1,200/1,300 give an initial latest estimate of 12,500. Open Data Input edits to 1,500/1,600 produce 13,100, an increase of 600; closed history stays 10,000. The target periods and budget defaults must exist. Test source selection, period boundary and rejected historical edits through the actual Forecast route; these are arithmetic expectations, not observed native execution.

#### Sheet Design Specification and Acceptance

For each selected sheet, record purpose/owner, base grain and ordered axes, detailed time/calendar, scenario/currency/filter context, model choice and KPI-versus-entity structure, version representation, source measures, input types/placement/defaults, closed/open policy, governed-target rules, formula dependencies/final outputs, aggregation on each axis, Pivot views/distribution, Cube source/target/reference policy if needed, anchors, lookups, upstream/downstream grain contracts, layout/measure placement, units/precision, conditional and input styles, access/input eligibility, and one representative edit with expected downstream results. Keep this concise and task-specific; do not make every optional feature a required section in the delivered app.

Use formula chains at their valid grain: Quantity 120 * Price 10 = gross 1,200; discount 5% gives net 1,140; unit cost 6 gives COGS 720; freight 0.50 gives 60; contribution is 360. Rates, headcount and closing balances need explicit aggregation semantics rather than automatic Sum. Recompute ratios from appropriate totals; never replace leaf quantity * price with total quantity * summed or unweighted prices.

For the guide's demand-to-cost request, choose an ordinary ML-baseline override and monthly text Visual measure if future periods exist and no history boundary is requested. Add a regional Pivot only with agreed distribution. The cost consumer can remove Channel from a compatible additive quantity grain. If the requirement changes to locked actuals through October and editable November onward, change the input behavior to Forecast without automatically redesigning unrelated sheets and links.

For presentation, retain the shared mandatory design standards and request-specific accessibility. The guide's Arial/Arrow preferences and Native-format starting suggestion are authoring choices, not product defaults. Native does not guarantee unscaled comma-separated output; inspect source format, precision and scope. Conditional formatting should express named business exceptions, tolerance and blank/zero meaning at detail/totals; color is not the only signal. Display formats do not convert currencies, and null-as-zero has the separately documented calculation effect. Do not erase established source/input/formula styling to imitate a guide's example palette.

Acceptance includes a permitted edit, unchanged excluded scope, save/reopen, connected refresh, correct ratios/units, restricted-user behavior and preserved identities. Bulk updates are outside this guide's configuration scope unless requested. Keep the design and arithmetic separate from native execution, runtime latency and ALM guarantees.

### Interpret the Prompt Before Choosing Modules

Business prompts mix outcomes, actions, constraints and presentation wishes. Extract those separately: who decides what, what they may change, at which grain and horizon, which result must respond, and what must remain unchanged or out of scope. An executive outcome such as "improve margin" needs model-grounded driver selection; a detailed workflow such as "adjust tomorrow's demand and review dispatch" supplies more of that chain. Neither requires the user to name modules. A regeneration request primarily asks for preservation plus specified changes, not fresh justification of every inherited feature.

For each material decision, keep a compact internal selection record: **request clause or stated assumption -> business action -> model source/grain -> selected feature -> simpler alternative and why insufficient -> deliberately omitted feature -> acceptance check**. Use `selected`, `not needed`, `explicitly excluded`, `preserved existing`, or `unresolved` for feature disposition. "Not observed in a sample" is evidence status, not a reason to exclude a feature. Summarize only material choices to the user; this record is not a new questionnaire or approval gate.

### Select Features by Business Distinction

These are conditional choices learned from the supplied business briefs, scope summaries and implemented examples, not mandatory modules. The prompt-to-feature evidence ledger separates reconstructed briefs, reported requests and observed implementations. Use the existing linked contracts for construction; this table does not add payload schemas.

| Business wording or distinction | Selection and reason | Do not infer or add automatically |
| --- | --- | --- |
| "Review actual performance" versus "change assumptions and see the impact" | Use Intelligence with verified source measures for read-only review; add Planning inputs and formulas when a user decision changes outcomes. Embed the workbench when editing and review belong together ([F27](#f27-embedding)). | An actuals dashboard does not show planner changes just because it has the same measure labels; a dashboard request alone does not require editable plans. |
| "Forecast" meaning driver-led planning versus statistical prediction | Use editable drivers, actual/forecast branches and bounded periods for a driver plan. Select [F09 Forecast](#f09-forecast) only for the required supported forecast behavior after resolving horizon, method and treatment of actuals. | Do not promise trained prediction, recursive inventory simulation or future accuracy from arithmetic assumptions or a sheet named Forecast. |
| "Use sales volume for costs" versus "combine several plans into an outlook" | Reuse the authoritative quantity locally if the decisions share one workbench; use [From Sheets/Blend](#f19-blend) for a compatible direct dependency. Use [F18 InfoBridge](#f18-infobridge) when normalization, mappings, append/join or a shared query result is needed. | Separate cost sheets and InfoBridge are not prerequisites for every dependent formula. Never introduce a second independent volume input merely to fill a domain template. |
| "Different teams/channels own assumptions" versus "one commercial workbench" | Separate working areas when ownership, drivers, grain or workflow differ; keep their output contracts compatible. Integrate price, demand and unit-cost drivers when the same decision can be made coherently in one plan. | Do not reproduce an enterprise application's domain/page count in a compact request. Separate sheets alone do not provide access isolation. |
| "Add products/employees before actuals exist" versus "inspect master context" | Select PowerTable maintenance only for authorized record changes; use source-only review otherwise. Connect stable member keys and effective-dated validity to eligible Planning intersections, including new members without transaction history. | An editable master table does not itself refresh the semantic model or planning eligibility. Maintenance does not authorize new databases, forecast destinations or integration writes. |
| "Enter a regional target" versus "allocate by seasonal/payroll weights" | Resolve parent entry/distribution behavior using [native input rules](#native-input-rules-and-distribution); select a weighting rule only when its business basis is required and verified. Check child eligibility, zero/blank weights and total conservation. | Parent distribution, native weighted allocation and [anchor visibility](#f20-anchor-measures) are different features. A prior temporary rule omission is not a universal ban, and historical sales are not always valid weights. |
| "Business owners maintain weights or limits" versus "use a fixed validated bound" | Use existing governed reference data, or authorized maintenance when requested, and resolve its grain through a supported source/query/lookup to the applicable input control. Keep the weight/limit computation separate from the rule consuming it. | Do not add a control table, SQL forecast-writeback loop or guessed fallback limit when a fixed bound suffices. The historical notes describe a metadata-driven limit design but explicitly do not establish its completed implementation. |
| "Compare an upside/downside" versus "save independent budget versions" | Pure what-if inputs/formulas can compare sensitivities without new source-model scenario records. Persisted versions need explicit scenario identity and [filter context](#f08-filter-context) through inputs, queries and consumers. | A model's simulation measure or a page called Scenarios does not prove a requested versioning workflow. Never present independent scenario storage or refresh isolation without the required context. |
| "Switch between region and employee detail" versus "show assumptions only at a hierarchy level" | Use [F06 pivots](#f06-pivot) and [F23 bookmarks](#f23-bookmark) for repeatable analytical views; consider F20 anchors for supported hierarchy-level visibility. Recheck aggregation and input grain for the selected view. | Do not create duplicate planning inputs for alternate review layouts. Visibility does not allocate values or change calculation semantics. |
| "Lock actual periods; plan eligible future combinations" | Separate source/display logic from [formula-based input eligibility](#f30-allow-input-based-on-formula), period rules and scenario context. Preserve historical/frozen values needed for comparison. | Visibility and filter scope are not edit permission or [F25 security](#f25-security). Future members need not have historical facts; labels do not establish valid combinations. |
| "Save and refresh consolidated results" versus "send results to an operational system" | Choose verified Plan persistence and connected refresh for internal planning. Select [F17 writeback](#f17-writeback) only for the requested destination integration and its authorization. | SQL-backed master maintenance does not require SQL forecast writeback. A dispatch recommendation is not an SAP submission; a connected result is not proof of instant propagation. |
| "Review before approval" versus "route approvals to named roles" | A review surface supports human inspection. Select [F13 Approval](#f13-approval) when the request actually needs workflow states, approvers and transitions; resolve those business rules. | The word "approval" in a narrative does not prove that native workflow was requested or configured. Never infer approvers or grant permissions. |

### Contrastive Business Examples

The following are sanitized practice prompts synthesized from the evidence, not verbatim recovered user messages or instructions to copy an existing Plan. Re-derive fields, defaults, pages, periods and identities for the actual request.

- **"Adjust daily demand, compare with stock and inbound, and review dispatch; do not send anything to the ERP."** Choose day-grain Planning, future-only adjustment eligibility and a compatible direct sheet dependency for the review. Exclude ERP/writeback actions. Require a real stock-flow model before claiming recursive inventory simulation. A short workbench and a long-horizon plan need an explicit shared-input or reconciliation design; matching labels do not synchronize their adjustments.
- **"Give sales one place to adjust volume, price and cost and review margin."** Start with one coherent Planning workbench and connected Intelligence review, not a mandatory separate supply plan. If a distinct operations owner must maintain costs at another grain, split that decision and connect the authoritative quantity. Consolidated margin must come from total profit divided by total revenue.
- **"Connect workforce, overhead and commercial plans into a P&L, and let us onboard valid new products."** Choose domain drivers, disjoint mapped financial contributions, normalization/consolidation and only the requested maintenance surfaces. Exclude compensation and product costs from manual overhead contributions to prevent double counting. Do not copy all administrative tables or assume authorization to provision a new model/database.
- **"Compare a downside to this plan without changing the saved budget."** A sensitivity calculation may be sufficient. Ask about independently editable/persisted versions only if that distinction cannot be resolved from context; add scenario storage and isolation when needed, not because the word "scenario" occurs.
- **"Explain how a category price change flows through margin and funding."** Choose an inspectable driver/formula chain and suitable hierarchy/review views; consider anchors only for the required assumption visibility. Verify rate aggregation, dependency behavior and the actual financial model. A demonstration's funding or tax proxy is not a formal cash-flow or statutory calculation, and its long formula chain is not a complexity target.
- **"Enter a parent target, but do not add allocation rules."** Respect the explicit rule exclusion while resolving whether ordinary parent distribution satisfies the requested entry. A later authorized requirement to use payroll or seasonal weights changes that selection; it does not retroactively describe the earlier build.

Use the selection record to test design adequacy: follow one permitted business edit through the intended calculation, save/refresh boundary and consuming review; verify an excluded action is absent and unrelated saved inputs are preserved. Where runtime checks cannot run, report that limitation rather than treating a plausible feature list as a working business application. Keep technical reliability lessons separate from evidence that the chosen features actually satisfy the prompt.

### Studying User-Supplied Plan JSON Examples

Inspect the part inventory first, then representative records for the features needed. Avoid exhaustive traversal, stored input-row inspection and broad repository reads when the existing guidance plus supplied examples cover construction. Preserve the distinction between these layers:

- **Packaging:** decoded examples can map part paths to objects; CreatePlan still requires the documented item-definition transport. A decoded map is not itself the REST body.
- **Composition:** input companions demonstrate `Native`, `DataInput`, `Formula` and `Forecast` tagged measure records. Source-linked defaults, `BasedOnFormula` editing and `M_<resolved-id>` dependencies show feature relationships, not permission to copy IDs or omit required metadata.
- **Connections:** `PLANNING`, `APPEND`, `EDITABLE`, `JOIN` and `SQL_SOURCE` in supplied ALM records are serialized source/query kinds. Keep these distinct from numeric runtime enums and use the target import contract. Inspect only the required source/consumer records and dimensional alignment.
- **Presentation:** sheet registries, visual properties, embedded placement and workload properties demonstrate separate layout/state boundaries. Preserve actual nesting and encoded boundaries; create fresh identities and a new request-specific layout.
- **Evidence:** cached counts, parquet versions, job status, native scenarios, connections, permissions and saved values belong to the example. Do not carry them into a candidate or claim runtime behavior from their presence.

The reviewed supplied examples contain native Plan `definition.json`, connected-planning parts, sheet/visual parts and measure companions despite their report-oriented filenames. They illustrate input/formula composition, forecast metadata, maintenance and connected-query features; they are not templates, proof of correctness, or a reason to fetch another live artifact.

When a selected serialization boundary remains ambiguous, an example conflicts with the target schema, or an actual validation/import fails, inspect only the responsible owner/writer/importer. Stop the investigation when that issue is resolved, construct the candidate, save through the supported route and verify its own result. Keep model metadata and relevant queries necessary for business correctness; avoiding code archaeology does not authorize guessing model fields.

## Required Reference Reads

Use this table as a section-level router, not an instruction to load the entire document. Start with the business authoring workflow and presentation standards, then read the selected feature sections and only their required shared dependencies. Read the applicable contract body, not just its title. Audit history, extraction procedures and source citations are not default creation reads.

### Contract Reuse and Source Investigation

Distinguish authoring authority from tool location. When the user clarifies that this bundle must supply the creation logic, use its business workflows, feature contracts and presentation rules as the authority; approved CLI tools and inspected technical serializers may execute them even when stored elsewhere. A helper's external path is not by itself a blocker. Do not inherit its business defaults, layout, identifiers or deployment journals. Preserve a genuinely explicit filesystem-only restriction when one is intended, rather than assuming either interpretation against the user's clarification.

Use the rules, examples and validation requirements already documented for the selected visual family, representation, route and recorded compatibility scope. A source citation supports those rules; it is not an instruction to reopen the implementation. Preserve native state, exported ALM and API-request distinctions and all stated evidence limits.

Inspect source only for a required contract that is missing or contradictory, a relevant known version/behavior change, or a validation failure that the documented guidance cannot resolve. Use available build/schema metadata and the recorded provenance to assess compatibility; a different repository revision alone does not require reauditing unrelated features. Unknown deployed compatibility must remain explicit and be checked through the selected route's validation, saved readback and authorized runtime checks, not silently treated as verified.

When a user points to an earlier successful creation, reconcile its recorded route, construction helpers and verification limits before describing a new blocker. Distinguish missing self-contained skill coverage from missing product capability or access. An earlier CLI-based create and readback do not require browser authentication to have occurred; browser checks remain a separate verification layer. A task-specific builder outside this bundle may explain prior success without establishing that its reusable implementation was packaged here. Inspecting its history to explain the difference does not authorize replaying its payload, reusing business defaults/identities or overriding a current skills-only constraint. Where permitted, reuse verified technical construction logic with fresh request/model inputs rather than rediscovering it; identify the exact packaging or compatibility gap that remains.

When investigation is needed, follow [contract-gap resolution](#contract-gap-resolution-and-route-fallback) for that boundary only and stop once it is resolved. Unavailable source links do not invalidate a self-contained evidenced contract, but neither do they permit guessing a missing field or declaring an unresolved route ready. Record reusable findings only when documentation maintenance is authorized.

### Request-Scoped Reading Map

| Request | Required contract |
| --- | --- |
| Any artifact creation or update | [Shared mandatory presentation/layout baseline](design-standards.md), including verified-property implementation and separate definition/rendered acceptance. |
| Functional use case or supplied decoded Plan examples | [Business-to-Feature Composition](#business-to-feature-composition): source values, editable drivers, formulas, connected results and review experience; inspect representative examples rather than every property. |
| Choose measure-based planning, logical measure grouping or authored business rows | [Model-selection decision](#measure-based-planning-versus-row-authoring), [ordinary examples](#ordinary-measure-based-planning-examples), then only the selected [measure hierarchy](#measure-hierarchy-authoring) or [row-authoring](#row-model-business-authoring) contract when needed. Neither editor is a prerequisite for ordinary inputs/formulas/Forecast. |
| Create/list/get/update/delete a Plan or retrieve/update its definition | [Plan Item Lifecycle](#plan-item-lifecycle), including action authorization, request shapes, pagination and LRO completion. |
| Intelligence/Reporting dashboard visuals or layout | [Intelligence Dashboard Patterns](#intelligence-dashboard-patterns), relevant visual/compiler contracts and current model field mappings. |
| Connected calculations, new members, stable inputs or refresh | [Model-Driven Design](#model-driven-design) and the selected F18/F19 source/consumer, import and refresh contracts when connected behavior is required. |
| Module selection, documented prerequisites or user-facing behavior | The relevant rows of [Plan Documentation Guidance](#plan-documentation-guidance), including documented/source discrepancies; then the selected feature's property and ALM contract. |
| Any exported-part construction or update | [Shared ALM Contract](#shared-alm-contract) and the selected feature's documented companion parts and restoration rules. |
| Charts number formatting or encoded hidden state | The Charts rules in [Source-Backed Contract Rules](#source-backed-contract-rules); F03 is Matrix-only. |
| Calculated/input measures, permissions or input kinds | [Native Measures and Inputs](#native-measures-and-inputs) and the applicable F05/F12/F29/F30 contract sections, not every input variant. |
| General construction, connected controls or acceptance planning | The applicable [Reusable Authoring Checks](#reusable-authoring-checks) and selected feature's property/schema contracts. These checks are not payload constructors. |
| Moving from local helpers to an imported, connected application | [Construction Readiness and Evidence](#construction-readiness-and-evidence), [Complete Records and Independent Checks](#complete-records-and-independent-checks), and [Failure Triage](#failure-triage). |
| Public-schema discrepancy or validation claim | [Published Packaging](#published-packaging), applicable current public schemas and [Verification Limits](#verification-limits). |
| A requested property not closed by these contracts | Check relevant supplied Plan examples for observed serialization first; if still unresolved or incompatible, inspect its current behavioral owner, save writer, ALM mapping and import reader. Do not copy another artifact's values or treat an observed shape as proof of behavior. |

## Plan Documentation Guidance

Use the product documentation at [docs.fabricplan.com](https://docs.fabricplan.com/), retrieved through the read-only [Plan documentation MCP](https://docs.fabricplan.com/~gitbook/mcp), for feature selection, user-facing prerequisites and acceptance checks. Retrieval date: 2026-11-06. Documentation guidance is not a native enum, persisted field, REST route or tested ALM recipe; reconcile it with the implementation and public definition for the selected version. UI examples and editor references must not be copied as native tokens, resource identities or business defaults.

[Advanced LOOKUP guidance](https://docs.fabricplan.com/planning-sheets/reference/formula-syntax/lookup-functions/lookup) requires an available source sheet/query and matching category grain. It documents positional matching with row values before column values, exact original value-field names rather than renamed display labels, and different behavior for omitted context arguments versus an explicit empty list. Preview is limited to 100 rows, so absence in preview is not proof of absence in the source. Creating a lookup alone does not load data; active formula use and the documented preview/sync workflow are separate checks. These are documented workflow claims, not a certified native LOOKUP signature, semantic-model lookup join or portable reference mapping.

[Home Layout guidance](https://docs.fabricplan.com/resources/create-and-manage-home-layouts) documents one layout per role, Item Baseline for users without a specific role, and highest-priority layout selection for users with multiple roles. Role Security takes precedence: a hidden sheet cannot be made accessible through a Home card. Preserve role security separately from presentation; do not create roles or grant access merely to complete a layout. F24's provider/ALM and F25's enforcement boundaries remain open.

### Documented Input and Model Constraints

[Input-column fundamentals](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/insert-manual-input-columns/insert-column-fundamentals) documents Insert As and Input type as creation-time choices that cannot be changed afterwards. Visual columns use static defaults; default-value controls are unavailable for Long Text, Multi Select and Person. On Change Formula is unavailable for Long Text. Resolve the requested role/type before allocation rather than promising an in-place type conversion. The documented UI default allows read/edit entry, while inspected native AllowInputType defaults to Edit; keep this discrepancy explicit instead of overwriting either claim. Formula-based editability does not replace security permissions.

[Row Model](https://docs.fabricplan.com/resources/plan-preview-frequently-asked-questions/row-model) distinguishes source-linked nodes, child rollups and expression-driven nodes, and distinguishes adding a child from adding a sibling. Build referenced nodes before dependent expressions. A tutorial's deletion of pre-existing rows is not a general prerequisite: updates must preserve unrelated rows and saved-input identities. Documented model node labels are not a replacement for F11's native tagged variants.

[Forecast editing](https://docs.fabricplan.com/planning-sheets/how-tos/forecast-data-to-predict-future-trends/edit-forecast-settings) separates open-range changes, reopening closed periods, total aggregation, actuals overwrite/retain and retaining blanks. Shortening an open range can remove periods; do not perform it as incidental cleanup. The documented actuals-overwrite workflow requires a Measure closed-period source. Map requested behavior to the selected native/ALM route rather than inferring it from a display label.

[Fiscal setup](https://docs.fabricplan.com/resources/fiscal-year-setup-in-plan) requires semantic-model fiscal fields, consistent numeric sort fields and historical/future coverage. Configure the fiscal start month and convention consistently with that model before forecasting/time extension. Plan does not generate or repair fiscal calendars. Obtain business calendar semantics; do not inherit the examples' start month or year labels.

### Catalog Documentation Coverage

All F01-F30 catalog modules were searched/accounted for. **Direct usage** means the retrieved page describes the requested product feature, not that its native or ALM contract is complete. **Related only** means a shared workflow or another visual family provides useful guidance without proving the exact module mapping. **No exact match** describes this search, not proof that documentation or functionality does not exist. Read the linked page's relevant sections and the corresponding F contract before acting; this is a bounded documentation pass, not an exhaustive crawl of the documentation repository.

| Module | Retrieved documentation | Coverage | Additional authoring/check guidance |
| --- | --- | --- | --- |
| F01 Layout | [Layouts](https://docs.fabricplan.com/planning-sheets/how-tos/format-and-display/layouts) | Direct usage | Separate table layout from measure placement. Loaded data/edit permission are prerequisites; Tree comparisons require resolved baseline/comparison measures. |
| F02 Aggregation Settings | [Manage aggregation](https://docs.fabricplan.com/planning-sheets/how-tos/adding-business-logic-and-formulae/manage-aggregation) | Direct usage | Resolve measure, row and hierarchy scope and both axis totals separately. Displaying/hiding a total is not choosing its calculation. |
| F03 Quick Format | [Format numbers](https://docs.fabricplan.com/planning-sheets/how-tos/basic-formatting/number-formatting) | Direct usage | Uniform, measure-level, per-cell Auto and source-native scaling have different presentation scope. Verify units/precision; do not confuse quick conditional formatting with numeric Quick Format. |
| F04 Insert Row | [Insert rows fundamentals](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/rows/insert-manual-input-rows) | Direct usage | Resolve selected parent/level and single versus templated insertion. Review cross-filter/RLS binding for referenced rows; UI binding alone does not prove server enforcement. |
| F05 Insert Column | [Input-column fundamentals](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/insert-manual-input-columns/insert-column-fundamentals) | Direct usage | Decide visual measure versus visual column before creation; use the type-specific control/default exceptions above. Do not generalize row-type switching to immutable column types. |
| F06 Pivot | [Pivot data](https://docs.fabricplan.com/planning-sheets/how-tos/adding-business-logic-and-formulae/pivot-data) | Direct usage | Named views reorder/show/hide row dimensions and affect aggregation/input grain. Distinguish this workflow from an InfoBridge Pivot Table transformation. |
| F07 Visual Filter | [Intelligence facet filters](https://docs.fabricplan.com/intelligence-sheets/how-tos/filter-data/create-a-filter-panel) | Related only | Category assignments and cascading selections inform interaction checks; they do not define Planning VisualFilters fields, scope or persistence. |
| F08 Filter Context | [Filter context awareness](https://docs.fabricplan.com/planning-sheets/how-tos/set-up-filter-context-awareness) | Direct usage | Verify inputs, comments, notes, locks, headers and writeback context across selections. Enabling context can prompt removal of existing elements; do not auto-confirm a destructive reset. |
| F09 Forecast | [Edit forecast settings](https://docs.fabricplan.com/planning-sheets/how-tos/forecast-data-to-predict-future-trends/edit-forecast-settings) | Direct usage | Treat open/closed ranges, aggregation, actuals replacement and blank retention as separate choices; preserve saved values unless the requested change permits replacement. |
| F10 Fiscal Year | [Fiscal setup](https://docs.fabricplan.com/resources/fiscal-year-setup-in-plan) | Direct usage | Match the model's start month, convention, fiscal hierarchy and numeric sorting; fiscal labels are not automatically native wire literals. |
| F11 Row Model | [Configure row properties](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/row-based-modeling/configure-row-properties-in-the-model) | Direct usage | Check open/closed configurations separately. Linked Row is documented for open periods; that UI label does not add a native CustomRowType variant. |
| F12 Measure Model | [Measure Model FAQ](https://docs.fabricplan.com/resources/plan-preview-frequently-asked-questions/measure-model) | Direct usage | Required native/DAX measures must already be in Values for the builder. Formula dependency readiness, field assignment and hierarchy placement are separate checks. |
| F13 Approval | [Approval workflow](https://docs.fabricplan.com/planning-sheets/concepts/planning-tools/approval-workflow) | Direct usage | Resolve sequential levels, approver selection, rejection/reset and notification intent. Interface-based workflows and On Change scripts are distinct supported usage paths, not interchangeable payloads. |
| F14 Formatting | [Cell/header/value formatting](https://docs.fabricplan.com/planning-sheets/how-tos/basic-formatting/cell-header-and-value-formatting) | Direct usage | Scope styling to cells, rows, columns or hierarchy levels. The documented Inforiver Sans UI default does not override this library's required configurable-text Arial baseline. |
| F15 Conditional Formatting | [Create rules](https://docs.fabricplan.com/planning-sheets/how-tos/format-and-display/conditional-formatting/create-rules-in-conditional-formatting) | Direct usage | Resolve target and values/totals/both scope before choosing IF conditions, color scale or classification. These UI families are not native discriminator strings. |
| F16 Column Style | [Header orientation and fit controls](https://docs.fabricplan.com/planning-sheets/how-tos/basic-formatting/cell-header-and-value-formatting) | Related only | Header wrapping, orientation, content fit and hierarchy-level formatting inform readability checks, not the exact ColumnStyle payload. |
| F17 Writeback | [Forecasting/writeback FAQ](https://docs.fabricplan.com/resources/plan-preview-frequently-asked-questions/forecasting-and-writeback) | Direct usage | Check writeback-specific permission, selected scenario/measures, filters, destination and logs. A sheet-row deletion does not imply SQL-row deletion; do not infer retry/idempotency across formats. |
| F18 Infobridge | [Connected Planning overview](https://docs.fabricplan.com/overview/infobridge-connected-planning) | Direct usage | Distinguish integration/transformation from destination writeback. A consolidated table is a documented best practice, not authorization to provision or combine destinations. |
| F19 Blend | [Blend with Infobridge](https://docs.fabricplan.com/planning-sheets/how-tos/infobridge/blend-measures-by-using-infobridge) | Direct usage | Direct sheet blending requires matching dimensions in the documented workflow. Queries provide a separate preparation route; reconcile required dimensions and measures before use. |
| F20 Anchor Measures | [Related measure-model concepts](https://docs.fabricplan.com/resources/plan-preview-frequently-asked-questions/measure-model) | No exact match | Search returned related measure-model/anchoring prose, not an AnchorConfig contract. Retain the source-backed dimension/hash/placement boundary; do not infer anchor settings from hierarchy position. |
| F21 Data Pane | [From Sheets and Queries](https://docs.fabricplan.com/planning-sheets/how-tos/infobridge/blend-measures-by-using-infobridge) | Related only | Confirm imported fields are available and assigned to Values. Data-source availability is not a contract for pane visibility flags or read/edit-mode persistence. |
| F22 Side Panel Filter | [Intelligence filter panel](https://docs.fabricplan.com/intelligence-sheets/how-tos/filter-data/create-a-filter-panel) | Related only | Review category-control choices and cascade behavior. Intelligence Super Filter configuration does not establish the native side-panel placement/visibility contract. |
| F23 Bookmark | [Bookmarks](https://docs.fabricplan.com/resources/bookmarks) | Direct usage | Public bookmarks are visible to users with sheet access; private bookmarks are creator-only. Updating or making a view default is separate from promoting its visibility. |
| F24 Home Layout | [Home Layouts](https://docs.fabricplan.com/resources/create-and-manage-home-layouts) | Direct usage | Review role fallback/priority and preview the layout. Preserve Security precedence and the distinct legacy/V2 storage/provider acceptance checks. |
| F25 Security | [Manage security](https://docs.fabricplan.com/planning-sheets/how-tos/manage-security-in-planning) | Direct usage | Review sheet visibility/read-only and feature permissions separately. Under Specific Sheets, unconfigured sheets are documented as defaulting to Read + Write; omission is not a deny policy. |
| F26 Themes | [Intelligence themes](https://docs.fabricplan.com/intelligence-sheets/how-tos/use-themes-for-consistent-color-schemes) | Related only | Canvas, chart and KPI theme scopes differ. Theme JSON import/export is a presentation workflow, not whole-Plan packaging or proof of native Matrix theme keys. |
| F27 Embedding | [Embedding/live measures](https://docs.fabricplan.com/planning-sheets/concepts/connected-planning/blend-measures) | Direct usage | Select an existing planning sheet; distinguish semantic-model baselines from live From Sheets fields. Documented real-time updates still require authorized runtime verification. |
| F28 Header Footer | [Intelligence Matrix pagination](https://docs.fabricplan.com/intelligence-sheets/how-tos/pagination-and-formatting-for-reports) | Related only | Check repeated headers/footers, selected filter labels, timestamps and page/export boundaries. Presets are optional UI aids, not required templates or a Planning ALM mapping. |
| F29 OnChangeFormula | [Input properties](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/insert-manual-input-columns/insert-column-fundamentals) | Direct usage | Change-triggered actions differ from a calculated value and from input eligibility. Verify intended effects and input-type availability; do not treat scripts as pure formulas. |
| F30 Allow Input Based on Formula | [Formula-based entry](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/insert-manual-input-columns/insert-column-fundamentals) | Direct usage | The formula is an entry condition, not a default-value formula or access grant. Review both eligible/ineligible intersections without weakening role security. |

### Native Helper Documentation Boundaries

The catalog mapping also supports calculated measures, dynamic rows, aggregation and pivot in the native-property inventory. The remaining helper topics have the following bounded documentation guidance:

| Native topic | Documentation contribution / limit |
| --- | --- |
| AdvanceLookup / SemanticModelLookup | Use the [Advanced LOOKUP](https://docs.fabricplan.com/planning-sheets/reference/formula-syntax/lookup-functions/lookup) checks above for documented source/grain/context behavior. No exact semantic-model lookup configuration was established; do not transfer function syntax or PowerTable relationships into native lookup predicates. |
| DataInputRules | [Allocation/input controls](https://docs.fabricplan.com/planning-sheets/concepts/planning-tools/allocation-rules-and-data-input-controls-in-planning-sheet) distinguishes equal/weighted distribution, min/max and locking with explicit target scope. Its hierarchy-update rejection claims do not prove native builder atomicity or validation beyond the inspected at-least-one-bound rule. |
| ColumnReorder | [Formatting/fit guidance](https://docs.fabricplan.com/planning-sheets/how-tos/basic-formatting/cell-header-and-value-formatting) is related presentation guidance only. No additional parent-child reorder mapping, ID allocation or import restoration was established. |
| CustomDateFormat / Date input | [Date-column controls](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/insert-manual-input-columns/insert-column-date) separates display format, allowed dates and defaults. It does not define native locale conversion or prove every runtime validator. |
| ExtendTime | [Time extension](https://docs.fabricplan.com/planning-sheets/how-tos/forecast-data-to-predict-future-trends/extend-planning-beyond-source-data-periods) documents at least one data-input measure and no forecasts already created for that standalone workflow. Do not delete existing forecasts to satisfy it or infer the native period encoding/inclusivity. |
| Cube request metadata | [Cube management](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/multidimensional-planning-and-forecasting/manage-cube-measures) separates whole-cube and individual-measure sync/breakdown operations. Deletion can remove linked measures across sheets; it is not incidental cleanup. UI operations do not close the request DTO/ALM mapping. |
| Native Formula | [Formula-column editor](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/insert-manual-input-columns/insert-calculated-columns) provides reference/function assistance. Suppressing displayed calculation errors is not repairing formula semantics; editor names and bracketed references do not establish native tokens, all signatures or formula-text restoration. |

### Documentation Discrepancies and Safe Use

The [date-column page](https://docs.fabricplan.com/planning-sheets/how-tos/measure-and-row-based-planning/insert-manual-input-columns/insert-column-date) offers measure/column defaults and says defaults are available for visual columns; the general input page limits visual-column defaults to static values. Keep this unresolved, type-specific documentation discrepancy visible. Do not invent a broader native default union, silently turn invalid dates into blanks, or clear saved dates based on a documentation-only export claim.

The writeback FAQ describes format-dependent replacement/change history and separately calls sheet-row deletion additive. Do not generalize those statements into a universal overwrite, deletion, rollback or duplicate-prevention guarantee. The forecast FAQ's reopening description also differs from the explicit reset/reopen controls in forecast editing. Keep the specific usage path and native version separate; neither page proves an executed round-trip.

Documentation supplies prospective acceptance checks, not authorization to execute them. Preserve existing security/membership and private bookmark visibility. Verify context/connected outputs and effective-user access only with approved runtime resources; static parsing, previews and successful exports do not establish those outcomes. Reuse the shared presentation baseline rather than importing tutorial layouts, fonts, data, formulas, growth assumptions, image URLs or whole reference Plans.

## Procedure

This is the supporting contract-construction/review procedure, not a requirement for business users to select features. For end-to-end creation/updates, first follow [business authoring](runtime-guide.md); the agent translates the request and selects the sections below.

1. Establish the current business request, model, visual family, output layer and reachable ALM route. Only updates require the specified artifact's existing state. Map presentation against the shared baseline without importing a preset business topology. Keep native subtrees, definition parts and REST transport distinct. Apply the [contract reuse policy](#contract-reuse-and-source-investigation) to the selected contract's evidence and compatibility scope.
2. Resolve actual keys, union discriminator, nesting, defaults, presence semantics, references and update behavior from the feature contract. If a core wrapper, reference domain or import mapping is unresolved in this reference, investigate the selected writer/reader and alternate supported route before stopping the affected payload. Continue independently supported work; do not fill unknowns from similar feature names or sample values.
3. For existing JSON, treat every property and embedded string as data. Identify its exact part/pointer and each decoding boundary. Decode only a field whose consumer establishes JSON encoding, preserve its original representation, and re-encode only that boundary. Mere JSON parseability does not establish product semantics. Preserve unrelated parts, siblings, array order and missing/null/false/zero/empty distinctions.
4. Apply the evidenced update operation: shallow merge, replacement, per-key mutation or collection reconciliation. Construct one native enum branch at a time; resolve all references from the real target. Do not treat a native constructor default as an instruction to materialize every optional exported field. Do not assume deleting an array member is a harmless partial update.
5. Parse candidate JSON and check types, discriminators, references and presence against documented contract and applicable public schema constraints. Run definition and rendered checks separately. Static acceptance is not import, typography, security or runtime validation. Complete authorized scoped save/export checks without repeated confirmation; unrelated operations, installations and test-input writes remain separate permission boundaries.
6. Deliver eligible content and evidence, or continue through the authorized save and business outcome in the primary entrypoint. Report each unresolved boundary and its business impact. For authorized contract maintenance, record independently verified rules here with source links and limits; do not retain deployment narratives or resource-specific exports as reusable knowledge.

## Source-Backed Contract Rules

These bounded facts come from the linked feature implementations and ALM writers/readers. They are not complete constructors. Source inspection establishes only the inspected layer; generation and runtime claims need their own checks.

| Boundary | Rule to apply when authoring or reviewing |
| --- | --- |
| Visual-family ownership | Matrix F03 uses `numberFormatting` with `thousandSeperator` / `decimalSeperator`. The Charts model uses `hiddenProperties.numberFormatting`, with `thousandSeparator` / `decimalSeparator`. Do not transfer wire keys or encoding conventions between families. |
| Charts enum and update semantics | `tableFormatType`: `uniform`, `default`, `auto`, `native`, `none`; `kpiTotalType`: `native`, `custom`; `displayScalingIn`: `title`, `breadcrumbs`, `both`. `scalingFactor` remains string-or-number, not an inferred finite enum. Ordinary update is shallow, custom-role update merges one role, reset replaces; theme/CARD/IBCS branches have separate effects. |
| Native measure discriminants | `Native`, `Formula`, `DataInput`, `Forecast`, `VisualColumn`, `AutoVariance`; payload variants use serde external tags. `VisualColumn` nests its own `Formula` or `DataInput`. Do not merge alternatives, omit AutoVariance from discovery, or assert its ALM support from the native declaration alone. |
| Native input kinds | `Number`, `ShortText`, `LongText`, `SingleSelect`, `MultiSelect`, `Date`, `Person`, `Checkbox`, `Simulation` are distinct implementation branches. Published/API type codes are a different layer, not extra native variants. |
| Input defaults and permissions | Native `allow_input` is `Edit`, `ReadAndEdit`, or `{"BasedOnFormula":"expression"}`; omitted defaults to `Edit`, not proven nullable. Omitted `bound_to_filter_context` defaults true. `disable_write_access` is skip_deserializing and `user_permission` skip_serializing in the inspected struct; neither is a portable permission-setting recipe. |
| Input metadata payloads | Number min/max/default use tagged values such as `{"Static":0}`, not an asserted bare-number schema. Select `options_source` is `Static(array)` or unit `Lookup`; its metadata-kind enum has a different Lookup payload. Person has no default_value field. Simulation references a real source measure. Preserve each branch's fields and omission semantics. |
| Native constraints versus UI assumptions | Text helper limits use UTF-8 byte length, with default maxima 255/25,000, not demonstrated character counts. Rollup wire delimiters are `,` / `|`, not display strings with spaces. These helpers alone do not prove all validation rules are enforced. |
| Planning V2 envelopes | Properties contain `$schema` plus transformed payload, not a manufactured `/visuals/{id}` map. Inputs use `/columns`, inserted rows `/rows`; emitters conditionally omit empty collections. Writeback settings are root-level and destinations conditionally present. Do not manufacture public-table-required fields to hide an emitter/schema conflict. |
| PowerTable envelopes and deletion | Source uses `/source`, configs `/columnConfigs`, settings `/sourceSettings`; not public-prose flat/array assumptions. Import reconciliation can delete existing configs absent from incoming GUIDs. Preserve the full intended collection; no partial import recipe is established by this wrapper evidence. |
| PowerTable lookup completeness | getColumnConfigDetails resolves each lookup source; a missing source logs a warning and skips that lookup. Successful export does not certify complete lookup configuration. Reconcile intended lookups with resolved source records and emitted configuration; do not copy a missing lookup from another artifact or silently declare it unnecessary. |
| PowerTable timestamp cleanup | Scoped sanitizers remove source-meta `lastRowCountUpdatedAt` and, in the visual-properties input, `properties.visualState.superFilter.*.columnMeta.createdAt/updatedAt`. They require object branches and do not parse strings or strip every date/timestamp. Apply only the selected writer's cleanup; preserve business dates and unrelated metadata instead of globally deleting similarly named fields. |
| Import restoration and rewiring | V2 normalizes root internal schema and reverses registered rewires, but full nested reachability remains open. Defined target notes/cell_lock/auditLog can overwrite imported counterparts when both visual-state containers exist. Export cleanup's `lock_state` is different; do not copy stale cleanup comments or generalize target restoration. |
| Schema conflicts and evidence | Preserve code, published schema and prose as separate version-bound claims. Exact schema casing/constants matter. Open property bags and schema acceptance do not certify meaningful nested support; schema rejection is not proof of product rejection. |

The Charts reader parses its setting with JSON.parse and returns an empty object on parse failure. That fallback does not establish the exported key/path, an encoding convention for other settings or a creation default. Resolve the applicable save/export adapter before emitting encoded fields.

### Charts Section Encoding and Patch Semantics

For the inspected Shell Charts adapter, buildPersistKey, readPersistedSection and deepMergePatch establish a concrete boundary: a section name becomes the literal key `hiddenProperties_!!!_<propertyName>`. The reader accepts a plain object or a JSON string containing a plain object. Missing/null, invalid JSON, arrays and scalar values fall back to `{}`; this is recovery behavior, not proof that malformed input is valid or safe to overwrite.

agentUpdateVisualStatesBatched accepts nonempty `updates`, each with a `visualId` and nonempty `sections` of `{ propertyName, patch }`. Each patch must be a plain object. It recursively merges plain objects, retains a value for an undefined patch, and replaces arrays/scalars/null wholesale. It serializes the merged section with `JSON.stringify`, updates local visual state and requests `PROPERTIES_SYNCED` refresh. This adapter is not the native HTTP BATCH contract, a property-schema validator, or evidence that the server saved the change.

Consolidate edits into one section patch per visual/property and one update per visual. The loop reads each section's base from the original visual snapshot, not an earlier patch in the same batch; repeated section entries can overwrite earlier changes. Visual updates run concurrently, and per-section failures are collected, so inspect `updatedCharts` and `failedCharts` rather than assuming atomic all-or-nothing success. Validate property names/types against their documented feature contracts before calling this permissive adapter; use scoped investigation for a required property whose contract remains missing or contradictory.

Synthetic encoding example, not a complete visual, HTTP request or ALM part:

```json
{"hiddenProperties_!!!_numberFormatting":"{\"enabled\":true,\"noOfDecimal\":2}"}
```

The field names/types above come from Charts numberFormatting; preserve other saved section members through the selected writer. The adapter's merge is different from that store's shallow reducer. Do not globally stringify object-valued properties in other visual families or globally parse all exported strings. Observed mixed string/object forms remain version/owner-specific evidence; full ALM import preservation and rendered formatting are separate checks.

#### KPI Control Selectors and Defaults

The IKPIControls types provide these runtime fields inside the `kpiControls` section. Its encoded state key on the inspected adapter is `hiddenProperties_!!!_kpiControls`; the enclosing ALM properties wrapper remains family/route-dependent.

| Runtime field | Declared values/type | Inspected factory value, not generation policy |
| --- | --- | --- |
| `layout`, `previousLayout` | Numeric EKPILayout: HIDE_KPI=0, KPI_ONLY=1, TOP=2, BOTTOM=3, LEFT=4, RIGHT=5, AUTO=6 | HIDE_KPI; do not copy this when a visible KPI is requested. |
| `kpiFitMode` | `Content`, `Best fit` | `Best fit` |
| `total.value.type` | `native`, `total`, `average`, `last`, `first`, `secondLast` | `total`; the measure still needs a resolved field binding. |
| `total.enabled`, `total.showBlankAsLabel`, `total.showCategoryLabel` | Booleans | true for each |
| `title.enabled`; `title.prefix` / `title.suffix` | Boolean; each affix has boolean `enabled`, string `value` | Enabled, with empty affix strings |
| `variance.varianceDisplay` | `valuePercentage`, `value`, `percentage` | `percentage`; `showVariance` is independently false. |
| `variance.showVariance`, `variance.value`, `variance.percentage`, `variance.treatZeroAsNeutral` | Booleans | false, true, true, false respectively |
| `minimalViewConfig` | `auto`, `minimal`, `actual` | `auto` |
| `responsiveFontSize` | Boolean | true |
| `bgImage.backgroundFill` | `cover`, `contain` | `contain`; background display is independently disabled. |
| Individual foreground image `source` / `foregroundFill` | `dataset` or `custom`; `cover`, `fill`, `contain` | No universal foreground-image default established here. |

Defaults are from kpiControlsInitialState, not the supplied report. The type also declares 19 EKPIPreset members, nested font/variance/icon/tooltip/layout records, per-group controls and image metadata; their complete dependencies, migrations, constraints and rendered precedence are not closed by this selector table. The factory uses null placeholders for some fields whose interfaces name concrete types; do not turn those placeholders into resolved identities/layouts or infer universal nullability.

Choose total selection from the business question and verified data ordering; a period-end balance and a sum of flows are not interchangeable. This declaration alone does not establish how `last` handles empty periods or how a preset combines with a layout. `IKPIControls` has no `numberFormatting` member: do not invent `kpiControls.numberFormatting.enabled` from a UI label or confuse its title suffix with a numeric scaling suffix. The supplied brief's KPI Number Format workaround remains an owner-specific investigation lead, not a global instruction to disable Charts/Matrix formatting. Native rendering and the requested override behavior remain unverified; the scoped owner clarification follows.

Scoped owner clarification from the current working tree: KPISettingsContainer.renderNumberFormatting reads the separate `numberFormatting` model and calls `updateFormat` for precision, scaling, prefix/suffix and sign placement. The Enable number format toggle reads `state.numberFormatting.enabled` and delegates changes through `updateShowNumberFormatting`. This identifies the owning section, not a `kpiControls` child or proof that disabling it achieves every KPI formatting requirement. Preserve the actual chart-mode handler and encoded section boundary; mode-specific behavior, saved readback and rendered results remain separate checks.

### Native Measures and Inputs

Read the native measure declaration and DataInputConfig before construction. Serde payload variants are externally tagged; VisualColumn has its own nested Formula/DataInput alternatives. The native AutoVariance branch does not by itself prove public ALM support.

The Number metadata has optional tagged min/max/default values and a distribution flag. Other kinds have separate metadata contracts; do not populate every kind with Number fields. Use the documented selected-kind rules and import conversion; investigate only a required branch not covered here under [contract reuse](#contract-reuse-and-source-investigation).

Native enum/default declarations do not close full column records, identity allocation, model/cube references, version-context storage, permission precedence or server enforcement. Keep those boundaries unverified until traced and tested. Do not prescribe input amounts, rate ranges, distribution or business defaults from a constructor or example.

Additional inspected input leaves: Person contains only defaulted `allow_entry_on_totals_or_subtotals: bool`, not a graph-object/default-value payload. Checkbox has optional `default_value: Static(bool) | Dimension(Id) | Measure(Id)` and optional `edit_on_total: bool`; the enum default Static(false) does not populate an omitted optional default. Simulation has defaulted `source_measure_id: Id`, slider/distribution booleans, `simulation_range: i32`, alignment/variance-style strings. A generated source-ID default is not a resolved simulation dependency.

#### Input and Formula Measure Authoring

Use editable measures for independent assumptions and formula measures for dependent outcomes. The supplied input/formula guide is historical saved-shape and troubleshooting evidence, not a complete universal column constructor. Reuse the native contracts above; capture a same-build native save only for an unresolved writer/registration boundary, not as a prerequisite for every ordinary authoring task.

**Must:** resolve the root sheet and owning visual, inspect the actual properties envelope, and maintain an explicit registry of measure identity, type, label, owner, aggregation, visibility and dependencies. Keep runtime visual/column IDs distinct from exported visual/measure identities. Preserve long decimal IDs as strings, retain identities on rename, and use the selected native allocation contract for new measures. Never derive linked/semantic identities from labels or convert already rounded IDs back to strings.

Create complete owning input/formula records, not just `columnMeta` fragments. Reconcile `manage_measures`, per-axis aggregation, optional model-tree membership, formatting, filter registrations and context binding. Validate references in formulas, measure-derived defaults/bounds, edit predicates and on-change expressions separately; reject unresolved references and calculation cycles. A source's measure identity is not automatically a local consumer formula identity. Reuse [native formula authoring](#native-formula-authoring) and [activation checks](#imported-measure-activation); a present `dataInput.json` record does not prove a displayed, editable or registered native measure.

**Example:** these are synthetic Number settings only, not a full measure or deployment payload. Preserve a measure-derived default when required instead of replacing every setting with Static.

```json
{
	"default_value": { "Static": 100 },
	"min_value": { "Static": 0 },
	"max_value": null,
	"distribute_parent_value_to_children": true
}
```

The guide reports a prior missing-measure defect corrected by tagged numeric wrappers. The native tagged contract supports retaining those wrappers; it does not prove every missing measure has the same cause. Preserve meaningful empty/null fields through the selected writer, including a native empty input-internal ID where required. Do not copy the guide's sample owner/measure IDs or generalize its outer numeric enums to unrelated record variants. The outer context enum and inner Boolean use the [separate binding contracts](#filter-context-binding-across-layers).

**Prefer:** explicit business formulas and a consistent percent/sign convention. For example, a discount stored as 5 is interpreted as five percent only when the expression divides by 100. Sum additive amounts/quantities; use the source-verified `AverageLeaf` variant when leaf averaging is requested, rather than reverting to the historical guide's unresolved enum note. Choose formula-total behavior from the expected business result: summing percentages is not a margin calculation. Parent distribution is a separate choice and does not establish a weighted allocation rule; see [native input rules](#native-input-rules-and-distribution).

**Avoid:** label substitution into persisted `M_<resolved-consumer-identity>` expressions, JavaScript assignment syntax, guessed version fields, blanket KPI-format changes or unconditional distribution/rate defaults. Preserve fresh concurrency fields using the selected writer; a historical `undefined` KPI suffix is not a universal reason to disable KPI formatting.

**Validation:** check unique registrations, complete records/tags, resolvable dependencies, intact IDs and the exact saved diff. On authorized test resources, verify appearance after reload, default/bound/editability behavior, parent-distribution conservation and rounding, rate/formula totals, locked periods, context isolation and target-local links. Record static checks separately from actual input save/reopen and calculation results.

### Filter Context Binding Across Layers

Do not treat outer `columns[*].boundToFilterContext` and nested `columnMeta.measure_type.DataInput.bound_to_filter_context` as spelling aliases. The request adapter maps native `true` to `BindFilterContext::Active = 10` and `false` to `Disabled = 20`. It applies to DataInput, Forecast and VisualColumn.DataInput; other measure branches return no binding value. The native omitted-field default remains true, as documented above.

The ALM export field list retains the outer `boundToFilterContext` separately from `columnMeta`. For a newly imported column, importDataInputColumnsV2 queues sidecar provisioning with `Number(columnRecord.boundToFilterContext ?? 0)`. Thus an omitted outer field becomes 0 on that path, not 10; a boolean becomes 1/0, not the native adapter's 10/20. Existing columns take the repository-update branch. Do not infer the meaning of 0, rewrite conflicting pairs or collapse these layers without the receiving contract. Full import/readback and context-isolated input retention remain untested here.

Business use: when scenario/version is filter context rather than a visible hierarchy level, verify both the selected binding representation and the saved input key. A numeric binding code alone does not establish scenario isolation, edit permission or downstream query context.

The audit's cached [Planning DataInput 1.0.0 schema](https://developer.microsoft.com/json-schemas/fabric/item/plan/definition/Planning/DataInput/1.0.0/schema.json), retrieved 2026-11-09, declares `DataInputMeasure.allow_input` as string enum `ReadAndEdit`/`ReadOnly`, closes that object without `bound_to_filter_context`, and declares `NumberColumnType.min_value`/`max_value` as number-or-null. This differs from the native Edit/ReadAndEdit/BasedOnFormula union, boolean binding and tagged bounds above, as well as the observed export. Do not silently flatten tags, rename permissions or remove the nested binding to satisfy that snapshot. Its `default_value` also allows an unconstrained object, which does not verify its operands. Source-level representation is established for the inspected checkout; deployed-version acceptance and a full schema/native reconciliation remain open.

## Additional Native Property Contracts

The AppProps owner registers `calc_measures`, `pivot`, `dynamic_rows`, `data_input_rules`, `aggregation_config` and `advance_lookup` as concrete members; `extend_time`, `custom_date_format`, `column_reorder` and `semantic_model_lookup` are optional members. Rust `Default` on AppProps is not a blanket serde default for every omitted root field. These native members are not asserted JSON Pointers into an ALM part. The parent module inventory also contains other features; their declarations alone do not certify their contracts.

### Native Identity and Measure Mutation

The shared Id implementation wraps `u64`, serializes a decimal string and deserializes through a string-only u64 visitor. JSON numbers are not an equivalent accepted representation. `generate()` and Default use random generation; `for_str`/`for_bytes` use deterministic xxh3 hashing; `from_u64` preserves an existing raw identity. These methods do not establish a global collision registry, nonzero guarantee, SQL identity allocation or permission to hash a display label into a new persistent binding.

CalculatedMeasureMember has defaulted `id: Id`, `label: String`, `measure_type: MeasureType`, `data_type: DataType`, optional description. Its request conversion generates an ID; native update changes only supplied label/type/description/data-type fields, preserving its ID. A supplied measure_type replaces that entire tagged payload; an absent description does not clear it. This is not full-record replacement or a complete public dataInput column constructor.

FormulaConfig/NativeConfig/AutoVarianceConfig add distinct payloads: Formula has defaulted string `formula` and optional omitted-if-None cube partition string; Native has optional defaulted `measure_role`; AutoVariance has defaulted formula and `Absolute(String)`/`Relative(String)` variance type, default `Absolute("")`. MeasureRole is `Measure` (enum default), `ACMeasure`, `PYMeasure`, `PLMeasure`, `FCMeasure`, `AnnotationMeasure`, `OtherMeasure`, or `ExtraMeasure(String)`. Optional Native role does not automatically become Some(Measure).

CalculatedMeasures and DynamicRows use concrete HTTP request adapters and return true from their backend-persistence decision; do not classify every module here as NoOp/native-mode-only. Their changed-member serialization and server-ID conversions require their own request/ALM tracing. A native simulation measure's creation inherits aggregation from its source; that side effect is not a universal default for other measure types.

### Native Lookup Contracts

- AdvanceLookup is a vector of members with defaulted string `id`/`name` and `assignments: Vec<PivotAssignmentMember>`. Its custom assignment decoder first accepts the native member, then tries `PivotAssignmentResponse` conversion; invalid response data propagates a deserialization error, not an empty-list success. Native update replaces the assignments of an existing lookup while preserving its other fields; a missing ID errors. Lookup IDs are strings, and the change-tracking `Id::for_str` conversion is not allocation of a new lookup identity.
- SemanticModelLookup holds `lookup: map<MeasureId, SemanticModelLookupConfig>`. Config fields are defaulted strings `primary_table`, `primary_key_id`, `label_id`; optional `join_tables: Vec<String>` and `predicates`; and `dimensions: PivotAssignments`. Each predicate has a tagged `visual_member_id: Dimension(Id) | Measure(MeasureId)` and string `lookup_member_id`. A generated default Dimension ID is not a binding to an actual field.
- Semantic lookup create inserts a full config, while update requires the property and keyed entry to exist. Both sort dimensions by predicate lookup-member order, then primary key, then remaining members; do not describe this as generic map patching. Its rebuild helper compares key/label and predicate lookup-member references, not every config field or visual reference. Read the actual query/build consumer before claiming join behavior, complete invalidation or security enforcement.

Both inspected lookup AppProperty implementations use NoOp HTTP request types and `is_native_mode()` for their backend-persistence decision. That decision is not proof they are absent from ALM exports. Complete assignment unions, lookup query execution, target reference rewiring and outer export/import remain separate boundaries.

#### Advanced Lookup Authoring

Use Advanced Lookup when a Planning formula needs a reference value from an available Sheet or Query, such as a forecast, exchange rate, unit cost or planning assumption. This functional guidance incorporates the supplied how-to, 24-slide Advanced Lookup versus InfoBridge presentation and its research notes. Syntax and UI behavior are documented by those materials, not newly verified against the implementation. The deck's two InfoBridge screenshots establish visible preparation controls and performed steps, not lookup execution or storage behavior. The how-to's screenshot placeholders and the deck's pricing dropdown schematic are not product screenshots. Keep these claims separate from the native contracts above and from SemanticModelLookup, PowerTable foreign-key lookups and Dimension ID Mapping.

##### Choose Lookup, InfoBridge or Both

| Business requirement | Appropriate starting point | Boundary |
| --- | --- | --- |
| Retrieve one scalar assumption or another sheet's forecast | Advanced Lookup over an available Sheet or Query at the intended reference grain | Confirm complete ordered keys, value-field identity, source aggregation and freshness. Retrieval is read-only; it does not write back or allocate inputs. |
| Combine facts, reshape, aggregate or deliver a flattened dataset | InfoBridge preparation and the final query consumed through From Queries | A lookup does not replace dataset transformation. Use the existing [InfoBridge graph contracts](#observed-portable-graph-and-consumer-records) for native construction. |
| Derive currency/classification keys, resolve tiers/effective dates or normalize source grain | Prepare a compact reference query, then use Advanced Lookup where appropriate | Range matching and dynamic projection are not established by the supplied LOOKUP guide. Resolve overlaps and ambiguities upstream. |
| Use business-maintained PowerTable assumptions | Resolve an actual supported Sheet/Query route to the maintained data | Direct PowerTable-to-Advanced-Lookup connectivity and its precise Query integration are not established here. Do not invent a connector or assume saves propagate automatically. |
| Let a dropdown/slicer choose a lookup key | Validate that control's real binding, or use a prepared query or explicit fixed keys for a fixed requirement | The proposed pricing interaction is conceptual. A fixed-key formula is not a substitute for a requested dynamic interaction without disclosing the limitation. |

Preserve reference data at its natural business grain where retrieval suffices, but do not claim it is always faster or uses less storage. A LEFT JOIN with unique reference keys preserves fact row count while logically repeating the matched attributes; duplicate keys can multiply rows. Repeated values do not prove physical duplication, and neither screenshots nor a separate lookup definition establish caching or materialization strategy. The deck's 5 regions * 200 products * 50 customers * 12 months * 3 scenarios = 1,800,000 potential combinations is a hypothetical dense space, not actual rows or a benchmark. Five annual regional rates still require explicit compatible Region/Year inputs; detail dimensions do not disappear automatically.

##### Configure and Reference a Lookup

1. Select the Planning visual in editing mode, with the feature enabled and the required source available. Open Fields (the pane control after Data) -> Advanced -> Lookup -> Add Lookup. Reading mode does not provide these configuration controls.
2. Expand From Sheets or Queries in the Data pane. Drag matching dimensions into Category in the required order, and the original source measure into Values. Configure at least one Category and a retrievable value; record the actual automatically assigned lookup name, such as Lookup 1.
3. Use the table-shaped Preview icon to inspect category labels, aggregation and a known combination. It is disabled without assigned fields and samples at most 100 rows, not all source data or all possible formula results. There is no separate save button on the lookup card; verify normal visual/Plan persistence independently.
4. Choose Insert Formula, give the calculated measure a meaningful Title, enter the expression, resolve validation messages and select Create (Update for an existing formula). The formula Title is not the LOOKUP value-field argument.
5. Verify the saved formula against known source values and after reopening. Add Lookup creates another independent definition. Before removing a lookup or a field, update dependent formulas; renamed/deleted source fields also require reconciliation.

The supplied guide documents two to four arguments, using straight quotes and list brackets:

```text
LOOKUP("Lookup name", "Value field", row_values, column_values)
```

Use the configured lookup's name and the exact original source name of its selected Values field, not a renamed display label or an Excel range/column number. Category values match positionally: row values first, then column values, with exact spelling, case and spacing. Omitted row/column arguments inherit the current context; an explicit `[]` contributes no values on that axis. Both the context and the Category order must identify the complete source combination. A shorter parent path does not automatically aggregate missing levels, and a no-category lookup does not supply a matching result.

**Example source:** a synthetic forecast Sheet, with lookup categories Region then Product and Values = Forecast:

| Region | Product | Forecast |
| --- | --- | --- |
| North | Bikes | 120000 |
| North | Accessories | 30000 |
| South | Bikes | 95000 |
| South | Accessories | 25000 |

At a North row and Bikes column, these documented syntax forms have the following conceptual expectations. The three-argument example specifically retains the current column:

| Formula | Expected Forecast |
| --- | --- |
| `LOOKUP("Lookup 1", "Forecast")` | 120000 |
| `LOOKUP("Lookup 1", "Forecast", ROW, COLUMN)` | 120000 |
| `LOOKUP("Lookup 1", "Forecast", ["North"])` | 120000 |
| `LOOKUP("Lookup 1", "Forecast", ["North"], ["Bikes"])` | 120000 |
| `LOOKUP("Lookup 1", "Forecast", ["South"], ["Accessories"])` | 25000 |
| `LOOKUP("Lookup 1", "Forecast", ["North", "Bikes"], [])` | 120000 |

For a separately configured lookup whose Category is Currency then Period and Values is Exchange Rate:

```text
LOOKUP("Lookup 2", "Exchange Rate", ["EUR", "2026-01"], [])
```

Here both keys are explicitly supplied in the first list; `[]` suppresses current column values. The equivalent coarse-grain Region/Year example is `LOOKUP("Lookup 3", "Rate", ["Europe", "2027"], [])` for those exact configured categories. These fixed examples do not establish dynamic extraction of selected dimensions, dropdown bindings or automatic removal of Product/Customer/Month/Scenario from a detailed visual. Resolve any missing currency, classification or period mapping through a supported source preparation path. Native formula tokens, assignment serialization and ALM bindings still require their existing contracts.

##### Business Patterns and Grain Checks

All amounts, rates and labels below are illustrative. Business arithmetic explains the calculation; it is not a complete executable Planning expression or a policy default. Verify source uniqueness and aggregation, especially for nonadditive rates and unit costs.

| Pattern | Complete reference grain | Illustrative calculation | Preparation or interpretation check |
| --- | --- | --- | --- |
| FX | Currency + Month + Rate Type | 100000 * 1.10 = 110000 | Rate quoted as USD per EUR means multiplication; inverse quotations require division. Prepare currency mapping when absent. |
| Employee benefits | Country + Employee Type + Year | 5000 * (1 + 0.22) = 6100 | Monthly base salary plus benefits; prepare classifications and eligibility rather than assuming them from employee labels. |
| Product margin | SKU + Year | 15000 - 200 * 40 = 7000 | Unit cost is nonadditive; BOM rollups, components and version selection may need preparation. |
| Pricing strategy | Strategy + Product Category | 100 * (1 + 0.05) = 105 | Fixed Base/category keys are illustrative; dynamic strategy-control binding remains unverified. |
| Freight | Origin Zone + Destination Zone + Shipping Mode | 1000 * 12 = 12000 | Consistent volume/rate units; warehouse-zone mapping, weight tiers and multi-leg routes need separate logic. |
| Commission | Sales Role + Product Category + Fiscal Year | 250000 * 0.08 = 20000 | Flat rate on eligible sales only; accelerators and cumulative thresholds are not LOOKUP features established here. |
| Shared-cost allocation | Business Unit + Cost Category + Year | 1000000 * 0.12 = 120000 | Apply 12%, 18% and 70% once to the same pool; never repeat the full pool per department. Retrieval is not the [distribution workflow](#input-rule-business-workflows). |
| Tax/tariff assumption | Country + Product Category + Effective Period | 50000 * 0.06 = 3000 | Fictional planning rate, not legal/tax guidance. Prepare exact period keys from date ranges, exemptions and overlapping rules. |
| Inflation | Region + Year | 10000 * (1 + 0.03) = 10300 | Annual uplift on a comparable prior-year month, not monthly compounding of the annual percentage. Prepare monthly curves separately. |
| Cross-sheet expense budget | Region + Product | 120000 * 0.04 = 4800 | Retrieve the shared forecast; monthly phasing or extra consumer dimensions require an explicit compatible mapping. |

##### Loading, Refresh and Acceptance

The guide describes saved formula references triggering lookup loading when the visual loads; preview is not a prerequisite. An unused lookup configuration does not trigger that formula-loading path. Preview remains a separate inspection route, and automatic loading is not continuous synchronization.

Confirm the source itself is current, then use footer Sync or Sheet-toolbar Refresh Data where available. Wait for completion and compare a known value; reopen the visual if it remains stale. A completed visual refresh does not prove upstream Query completion, every lookup value's freshness or cache invalidation. Do not rename the toolbar command Data Refresh, invent refresh ordering, or claim a preview refresh updates every saved consumer.

**Must:** validate complete ordered keys, unique intended matches, original value-field names, source aggregation/units and known results. Missing combinations or value fields may error; do not silently substitute zero. Duplicate precedence is unverified: inspect and correct unintended duplicates or define explicit upstream aggregation, rather than relying on first/last-match behavior. **Prefer:** the smallest supported lookup/preparation composition that preserves business grain. **Avoid:** converting illustrative choices into default rates, claiming arbitrary hierarchy totals, or treating scalar retrieval as a one-to-many join, allocation or writeback action.

Offline checks can validate example arithmetic and the intended ordered-key model, but cannot certify native parsing/evaluation. On authorized test resources check known matches, swapped category order, extra/missing dimensions, case/spacing, missing value fields, duplicates, rates/totals and source access. Verify a known result beyond the 100-row preview sample, saved reopen, a changed source value and each actual refresh boundary. For Unable to resolve table relationships, inspect assigned source fields/relationships and source readiness, not just formula labels. Record unresolved behavior and apply the existing native contract-gap procedure when an actual artifact request requires it. This documentation update authorizes no live source changes, query refreshes or Plan writes.

### Native Input Rules and Distribution

#### Input Rule Business Workflows

Use input rules to turn an entered target into detailed planning values, protect commitments and constrain adjustments. The supplied allocation discussion adds functional design examples, not freshly verified product behavior, a native rule constructor or evidence that its presentation was executed here. Explain Fabric Plan as a combined solution: PowerTable is part of Fabric Plan, not a separate substitute for it. Distinguish each component's responsibility without presenting custom business algorithms as native one-click features.

| Component | Responsibility and boundary |
| --- | --- |
| Fabric data | Historical/operational facts at known recipient, period, scenario and unit grain. |
| PowerTable in Fabric Plan | Business-maintained weights, mappings, assumptions and effective policies over authorized sources, with applicable governance. Optional when existing measures, plan mix or manual rule weights suffice. |
| Semantic model / DAX | Derive raw drivers, normalized shares, composite/proxy profiles or complete baseline amounts. DAX calculates values; it does not write planning transactions. |
| Planning sheets | Receive targets, distribute through configured rules, enforce applicable controls, and support review/adjustment against the baseline. Verify enforcement through the selected runtime. |

**Choose the workflow before configuring a rule:**

- **Distribute an entered target:** resolve a reference measure or supported manual/equal/self-weight basis, expose it to the planning visual, configure the axis and recipient scope, then enter/revise a subtotal or grand total. For proportional allocation, `recipient = editable pool * recipient weight / sum of eligible weights`. With protected commitments, the intended editable pool is the target less retained locked amounts; retain locked values in the grand total but exclude them from redistribution and its denominator. This is the functional acceptance rule, not proof of the engine's lock/distribution precedence.
- **Calculate a baseline, then initialize and review:** compute the pool and detailed allocations in the model, explicitly initialize/copy into editable planning values through a supported authorized operation, and retain the baseline separately for comparison. Where adjustments are separate, `final = baseline + adjustment`. Model recalculation is not input initialization; later refresh must not silently overwrite planner overrides. Decide whether totals must be conserved or an executive adjustment may intentionally change the target.

The supplied workflow distinguishes the cell's blue-menu **ad hoc distribution action** from a **recurring distribution rule** that supplies the basis for qualifying later entries/revisions. Do not equate an invoked action, the Number input distribution toggle, a recurring rule, or a model-calculated baseline. Equal spreading of the demonstrated initially blank input is not a universal default. The existing [frontend/native selector boundaries](#frontend-rule-discovery-and-selection) still apply, including the unresolved query-reference route.

**Must:** define target measure, row versus column axis, hierarchy/dimension level, eligible recipients, pool/target identity, source and destination periods, scenario, effective policy version and units. Resolve source measure availability and current policy/model freshness before calculation. Require unique effective approved policy matches and matching numerator/denominator scope; preserve intended business restrictions and security rather than clearing filters to make totals agree. PowerTable edits may require model refresh/access steps before measures reflect them. Source/model/table provisioning and test writes require separate authorization.

##### Allocation Examples

These are synthetic functional fixtures, not target schemas or product-runtime results. Each example exposes source data, the rule or maintained assumptions, calculation and final output. Use this self-contained pattern when explaining allocations; do not hide matching keys, denominators or exceptions in speaker notes. The historical deck's styling, file path, slide counts and claimed checks are not new artifact defaults or verification evidence.

**Regional target, native rule basis:** `RegionalSalesHistory` contains North 5,000,000, South 3,000,000 and West 2,000,000 currency units for one complete prior year. Match by RegionKey; the requested plan uses a single next-year Base scenario. No PowerTable is necessary: select the historical-sales measure as the recurring reference at region grain. The eligible denominator is 10,000,000; revising the same total recomputes the proportions.

| RegionKey | HistoricalSales | Target12000000 | Target15000000 |
| --- | --- | --- | --- |
| North | 5000000 | 6000000 | 7500000 |
| South | 3000000 | 3600000 | 4500000 |
| West | 2000000 | 2400000 | 3000000 |

North's first result is `12000000 * 5000000 / 10000000 = 6000000`. Both output columns must reconcile to their entered target; do not sum overlapping hierarchy totals with these recipients.

**Calculated demand baseline:** `DemandHistory` contains six complete monthly totals, each 100,000 units, for one product group; their sum is 600,000 and monthly average is 100,000. PowerTable `ChannelAllocationPolicy` maintains the following illustrative rows, keyed by product group, channel, scenario and effective version. All rows here share group Group-A, scenario Base and approved version V1; scope them to the intended destination month, not every scenario or version.

| ChannelKey | Share | BaselineUnits | AdjustmentUnits | ReviewedUnits |
| --- | --- | --- | --- | --- |
| Direct | 0.5 | 50000 | -5000 | 45000 |
| Partner | 0.3 | 30000 | 5000 | 35000 |
| Online | 0.2 | 20000 | 0 | 20000 |

Only ChannelKey/Share and the stated policy keys/status belong to the maintained policy; baseline, adjustment and reviewed columns illustrate separate calculated/planning outputs, not extra policy fields. Direct's baseline is `600000 / 6 * 0.5 = 50000`. Initialize deliberately, then record the review adjustment; both baseline and reviewed totals are 100,000. Define treatment of incomplete/missing months before choosing the average denominator.

**Proxy-derived new-product phasing:** PowerTable `LaunchProxyPolicy` stores target SKU, activity, gender, optional collection, scenario, effective version, approval status and optionally launch quantity. An illustrative approved Base/V1 row for Launch-A maps to Running/Unisex with collection explicitly defined as any collection and quantity 12,000. A second row for Launch-B maps to Walking/Unisex with any collection and quantity 8,000. These policies select comparable history; they do not change either SKU's actual master attributes or execute user-entered DAX text. Match each target to exactly one effective approved row, then filter `PeerDemandHistory` by that row's attributes in the agreed historical window.

| Month | PeerUnitsA | BaselineA | PeerUnitsB | BaselineB | CombinedUnits |
| --- | --- | --- | --- | --- | --- |
| April | 2000 | 2400 | 4000 | 3200 | 5600 |
| May | 3000 | 3600 | 4000 | 3200 | 6800 |
| June | 5000 | 6000 | 2000 | 1600 | 7600 |

Each peer cohort totals 10,000 units. Launch-A April is `12000 * 2000 / 10000 = 2400`; Launch-B April is `8000 * 4000 / 10000 = 3200`. Calculate per SKU and only then sum: combined output totals 20,000, not a single allocation using an arbitrarily selected proxy. Use monthly increments, not cumulative history. A planner may move 400 units from Launch-A May to April, yielding 2,800/3,200/6,000 with the same 12,000 total. Alternatively expose the profiles as reference measures and distribute separately entered launch targets.

Blank-as-wildcard is an explicit business policy, not a default for missing data. Duplicate approved matches must hold the affected target for resolution, never silently widen the cohort; independent valid targets can proceed when authorized. Missing history, zero denominators, invalid/negative weights and absent policies require a stated business outcome, not automatic equal allocation or zero-filled success.

**Locked commitments and bounds:** a 60,000-unit launch has April fixed at 12,000, with May/June editable using weights 3/5. Revising the total to 66,000 leaves an editable pool of 54,000. June has a 32,000-unit ceiling. The proportional proposal and explicit planner resolution are:

| Month | Weight | LockedUnits | ProposalUnits | ReviewedUnits |
| --- | --- | --- | --- | --- |
| April | 2 | 12000 | 12000 | 12000 |
| May | 3 | 0 | 20250 | 22000 |
| June | 5 | 0 | 33750 | 32000 |

May's proposal is `(66000 - 12000) * 3 / (3 + 5) = 20250`. June exceeds its ceiling by 1,750; the planner explicitly moves that amount to May. Both columns sum to 66,000 and April stays unchanged. `LockedUnits: 0` here means no locked amount, not a native lock-state encoding. Min-max validation is not an optimizer that automatically redistributes capped amounts. The source summary reports alerts while its referenced documentation also describes update prevention; verify the target build's interaction and saved result rather than promise one universal warning/rejection behavior.

##### Additional Allocation Patterns

| Business pattern | Selection and acceptance rule |
| --- | --- |
| Scenario policies / raw weights | Filter the effective scenario policy before normalizing. Weights 5/3/2 need not be entered as percentages; against 900,000 they yield 450,000/270,000/180,000. Never combine Base and Growth denominators. |
| Shared-service composite drivers | Normalize headcount and tickets separately, then blend their shares, for example 60%/40%; do not add unlike raw units. Shares 38%/38%/24% allocate 900,000 as 342,000/342,000/216,000. |
| Promotion / store maturity | Multiply demand by approved uplift to derive scores, or peer revenue by maturity to derive a pool. Scores 120/120/60 allocate 150,000 as 60,000/60,000/30,000. A 1,800,000 peer baseline at 80% maturity gives 1,440,000 before seasonal phasing. |
| Direct plus shared chargeback | Calculate each disjoint pool by its own basis, then add recipient results. Preserve pool identity and ensure no cost is allocated twice. |
| Multistage quotas | Allocate to parents, then use child shares conditional on each parent; reconcile both levels and do not normalize all child policies together. |
| Milestone cash flow | Match contract and approved milestone schedule/payment period; a 2,000,000 contract at 20%/50%/30% yields 400,000/1,000,000/600,000 in its selected months. Aggregate milestones sharing a month without duplicating the contract pool. |
| Whole positions | Use an explicit total-preserving integer policy, not decimal formatting. For 17 positions at 50%/30%/20%, largest remainder turns 8.5/5.1/3.4 into 9/5/3. Specify deterministic ties and eligible recipients; this is a configured calculation pattern, not a claimed native rounding option. |

**Prefer:** the simplest supported basis and controlled review. Preserve source, baseline, adjustment and final meanings; a selected business pattern is not permission to add SQL forecast writeback. **Avoid:** native-capability claims for arbitrary composite/proxy/integer algorithms, silent fallback cohorts, guessed rule precedence or automatic replacement of existing inputs.

**Validation:** check one recipient by hand, total conservation per pool/scenario/period, unique policy matching, row/column scope, complete source periods, units and rounding residuals. Test blank/zero/invalid drivers, ambiguous mappings, locks exceeding the target, all recipients locked with a target mismatch, infeasible bounds and overlapping rules without silently relaxing constraints. A target fully satisfied by locked amounts needs no residual distribution. On authorized resources verify the initial action, later target revisions, locked-value preservation, bound interaction, policy-to-model freshness, baseline initialization without overwrite, and save/reopen/connected results. Functional arithmetic checks do not certify native rule execution, enforcement, UI timing or ALM restoration; retain the exact contracts and gaps below.

#### Native Rule Serialization

DataInputRules is a vector of Rule records. `id` and `rule_id` are separate Id fields: creation generates the internal `id`, while update/delete/duplicate selection uses the logical `rule_id`. Records also contain defaulted name, selectors, disabled/updated flags and created/updated user/time metadata; do not invent audit identities or timestamps to simulate a persisted rule.

The selector and rule enums use default serde external tags:

| Native enum | Variants / default |
| --- | --- |
| SelectedColumns | Unit `All` (default), `PeriodRange(StringPeriodRange)`, `Selected(Vec<Id>)`. |
| SelectedRows | Unit `All` (default), `Selected(Vec<Id>)`, `Dimension(Id)`. The source describes Dimension selection for Lock/MinMax; the declaration alone is not a universal distribution scope. |
| SelectedMeasures | Unit `AllMeasures` (default), `SelectedMeasures(Vec<Id>)`, unit `AllVisualColumns`, `SelectedVisualColumns(Vec<Id>)`. |
| RuleType | `Lock { all_children: bool }` (default false), `Distribute { operation: ApplyDistributionTo }`, `MinMax { min: MinMaxConfig, max: MinMaxConfig }`. |
| MinMaxConfig | `Static { value: Option<f64>, is_exclusive: Option<bool> }`, `Measure { measure: Id, is_exclusive: Option<bool> }`, `Variable { value: f64, variable: String, is_exclusive: Option<bool> }`, each wrapped by its enum tag. |

The row/column distribution definitions distinguish `ApplyDistributionTo::Row` from `Column`. Row config has required `apply_to_dimensions` and `reference`; Column config has optional `apply_to_dimensions` and required `reference`. Selection is `All` or `SelectedDimensions(Vec<Id>)`. Their DistributionReference alternatives are unit `Equal`, unit `SelfWeight`, `MeasureIdWithReference` with axis-specific metadata, or `ManualInput { weights: map<Id, f64> }`.

Row reference metadata has `measure: SelfMeasure | Measure(Id)`, `weights_from: Period(TimeInterval) | Column(ColumnSelection)` and optional `operation: Average | ApplyAsRange`. Column reference metadata has the same measure selection, optional `weights_from_row: Id` and optional `weights_from_period`. TimeInterval variants are `CurrentYear`, `PreviousYear`, `PreviousQuarter`, `PreviousMonth`, `PreviousDay`, `Custom(StringPeriodRange)`. These declarations do not prove weight normalization, rounding or time-range execution.

The separate DistributionOperation has `Equal`, `ByWeight(ReferenceType)`, `ByTrend { percentage, dimension }` and `ByTrendValue { value, dimension }`. Its ReferenceType/ByWeightMeasureReference is not interchangeable with the RuleType Distribute row/column reference above; trace the owning request before choosing a payload.

New/duplicate rules run validate_min_max_bounds, which checks only that at least one bound is defined. Static None is undefined; Measure/Variable count as defined without value resolution. Updates apply supplied builder fields before this validation; do not assume failed validation is automatically atomic. Reordering swaps positions selected by rule IDs, so validate positions and the complete intended order before calling it. `supports_undo()` is false despite rollback helper implementations.

Synthetic **MinMaxConfig/RuleType fragment only**, not a complete Rule, request or ALM part:

```json
{"MinMax":{"min":{"Static":{"value":0,"is_exclusive":false}},"max":{"Static":{"value":null,"is_exclusive":null}}}}
```

**Gap:** referenced identity existence, range/user decoding, applicable rule precedence, overlapping scope, resolved bounds, distribution execution, failure rollback, native save and portable export/import remain unverified. Native Id string decoding is inspected above; a parseable rule fragment is not edit enforcement or an allocation result.

#### Frontend Rule Discovery and Selection

The frontend rule enums and Input Rules menu expose three rule kinds: `Lock`, `Distribute`, `MinMax`. Minimum and maximum are the two bounds of `MinMax`, not additional discriminators named `Minimum` and `Maximum`. All three creation menu entries are disabled outside edit mode; that UI gate is not proof of backend authorization. Conditional-formatting `rules` and number-column bounds remain different features.

| Frontend selector | Declared choices | Serialization boundary |
| --- | --- | --- |
| Measure scope | `AllMeasures`, `SelectedMeasures`, `AllVisualColumns`, `SelectedVisualColumns` | Resolve actual measure/visual-column IDs and the native tagged selector. |
| Row / column scope | Rows: `All`, `Custom`; columns: `All`, `Custom`, `PeriodRange` | UI `Custom` is not a native SelectedRows/SelectedColumns tag. |
| Distribution reference | `Measure`, `InfoBridgeQuery`, `ManualInput`, `Equal`, `SelfWeight` | The UI's `InfoBridgeQuery` choice is not a newly verified native RuleType or ALM field; the inspected helper does not implement query selection. |
| Distribution period / dimension | `All`, `Custom`, `SingleColumn`; `rows`, `columns` | Do not substitute these labels for the native TimeInterval/axis union. |
| Bound operand | `Static`, `Measure`, `Variable` | Map to the separate MinMaxConfig payload, not NumberDefaultValue. |
| Selection mode | `Selected`, `Filter` | Filter-mode construction and import remain partial. |

DataInputRulesUtils opens the editor with the chosen rule kind; its default builder delegates to `DataInputRulesHelper.createNewRule` and adds current-session metadata. Its locally chosen rule identifier is not permission to fabricate persisted native IDs or audit fields in a new ALM part. Use the native contracts above for known structures and the actual form/writer for missing conversion. The menu/type enumeration is complete for those inspected declarations only, not execution or feature closure.

The frontend factory starts Lock with `all_children: false`, MinMax with two `Static { value: null, is_exclusive: false }` bounds, and distribution on the row axis when row dimensions exist, otherwise on columns. Both empty bounds are an editor draft, not a valid native MinMax save under the at-least-one-bound validator. Conversion to distribution drops a dimension-level row selector in the inspected factory; preserve/validate intended scope instead of assuming rule-kind changes retain it.

Two concrete unresolved boundaries prevent generation from enum names alone:

- InfoBridge reference selection returns the cloned rule unchanged, and updateDistributionSelectedInfobridgeQuery returns its input unchanged. This path does not construct a query-weight rule. It is not proof every alternative product route lacks the capability.
- getDefaultCurrentTimeInterval can cast `CurrentHalfYear`, `CurrentQuarter`, `CurrentMonth`, `CurrentWeek` or `CurrentDay`, while the inspected native TimeInterval declares only CurrentYear, previous year/quarter/month/day and Custom. Reconcile deployed/generated-client versions and the receiving decoder before emitting those extra current-period literals; a TypeScript cast does not establish native support.

### Native Aggregation, Ordering and Dates

| Owner | Persisted native shape and update behavior |
| --- | --- |
| AggregationConfig | Four defaulted maps: `measure_aggregation: MeasureId -> RowColumnAggregation`; `row_measure_aggregation: MeasureId -> RowId -> RowColumnAggregation`; `row_member_measure_aggregation: MeasureId -> RowMemberId -> RowColumnAggregation`; `row_dimension_aggregation: DimensionId -> AggregationType`. RowColumnAggregation has optional `row`/`column`. An update replaces the addressed pair, not just its non-null axis; nested deletion removes an empty inner map. |
| Pivot | Defaulted `configs: Vec<PivotConfig>` and optional `active_id: Id`. Config has ID/name, optional row/column dimension lists and measures, defaulted hidden flag. PivotMeasure has ID and AggregationType; optional column aggregation/rollup are omitted when None. Update always assigns row/column dimension options, but retains measures when absent and name/hidden unless supplied. Do not send a sparse update expecting all omitted fields to survive. |
| ColumnReorder | `orders: map<ColumnId, Vec<ColumnId>>`. Create delegates to update, replacing the selected parent's entire `ordered_children`; other parents survive. Delete is unit `All` or tagged `ByParent(ColumnId)`. This is hierarchy-member ordering, not a replacement for managed-measure display order. |
| CustomDateFormat | Defaulted `enabled: bool`, `formats: map<ColumnId, DateFormatCategory>`. Creation inserts one column's format; an absent property is initialized enabled. Update uses `Toggle(bool)` or `BatchUpdate { formats }`, which replaces the complete formats map. Delete removes one column entry. Preserve unrelated formats in a BatchUpdate candidate. |
| ExtendTime | Defaulted NaiveDate `start_date`/`end_date`; update replaces the optional whole property. Create/delete explicitly return OperationNotSupported. This declaration does not establish range inclusivity, calendar expansion, ordering checks or model provisioning. |

AggregationType serializes canonical variants `Sum`, `Formula`, `Min`, `Max`, `Average`, `AverageLeaf`, `WeightedAverage(Id)`, `WeightedAverageRow(Id)`, `StandardDeviation`, `VisibleRounding`, `First`, `Last`, `None`, `Earliest`, `Latest`, `Median`, `Variance`, `DistinctCount`, `Count`, `Subtraction`, `Product`, `Division`, `AverageExclusiveZero`, `VisualSum`. Its lowercase/camel-case serde aliases are accepted inputs, not canonical emitted values. Weighted variants carry distinct measure/row reference domains. The base Planning constructor accepts every scalar variant and resolves `{"WeightedAverage":"symbolic-measure-key"}` to its native measure ID; `{"WeightedAverageRow":"native-row-id"}` remains an explicit row reference.

The default aggregation helper returns `Some(AggregationType::None)` on both axes for Native and `Some(Sum)` for other types, not absent Options. Upsert helpers currently seed Native defaults rather than resolving every measure's actual type. The inherited-aggregation helper uses Sum/Sum when the source pair is absent or both axes are absent; an explicit None sentinel is a different state. Measure and row-cell updates call simulation propagation, but this does not prove propagation for every other aggregation scope.

Pivot creation can auto-activate the first config; the active-ID setter validates existence. Visible-active selection scans cyclically from the active position, or chooses the first visible config if the active ID is absent. Reorder checks count and ID existence, but callers must also require a unique complete permutation; duplicate IDs are not a safe reorder. These native operations are not the UI pivot store's request schema.

DateFormatCategory is `DefaultLocale`, `AbbreviatedMonthPadded`, `AbbreviatedMonth`, `DayMonthYearDashes`, `FullMonthName`, `FullWeekdayMonth`, `MonthDayYearSlashes`, `MonthDayYearSlashesPadded`, `DayMonthYearSlashes`, `IsoFormat`, or `Custom(String)`. Its converter implements specific UI-token-to-chrono translation; it is not a general date-format validator or proof that locale/time-zone handling matches other date metadata. Inspect the converter before generating a Custom format.

These five property adapters use NoOp HTTP types and `is_native_mode()` for the inspected persistence decision. Preserve selected request versus whole native value distinctions; full range/field validation, reference rewiring, ALM placement and rendered outcomes remain separate checks.

### Native Cube Request Metadata

MultiDimensionSettings and companion records use `rename_all = "camelCase"`, unlike the snake_case ForecastConfig. Required vectors are `referenceMeasures`, `newPartitions`, `existingPartitions`; optional `visualMeasureIdMapping`, `sourceMeasureId`, `nativeMeasureMapping` and `cubeModel` are defaulted/omitted when absent. The current redesigned dynamic-Cube request emits `cubeModel:"DYNAMIC"`. Do not fill required vectors with empty arrays as a substitute for resolved partitions.

ReferenceMeasure requires string `id`, `label`, `type` (explicit rename), `aggregationType`, `dataType`, and boolean `isNative`. Partition requires name and `dataAssignment`; DataAssignment requires dimensions and timeDimensions. AssignedDimension requires id/label/type/dataType with optional distinctValueCount and optional `lookups`; each lookup requires id/label/type/dataType and can carry distinctValueCount. Lookups are same-table attributes fetched separately from the fact query, not PowerTable foreign keys or Planning dimension-ID mappings. AssignedTimeDimension requires id/label/type/dataType and does not accept lookup attributes. These identifiers are declared strings, not automatically JetStream Id or portable Fabric record GUIDs. The local PeriodRange explicitly documents UTC epoch milliseconds in signed `i64` start/end; this does not establish the unit of ForecastColumnRange's separate optional u64 fields.

**ALM boundary:** the inspected Planning V2 exporter reads stored properties and separate column/row records, normalizes visual and measure references, applies registered rewires/cleanup and adds `$schema` to emitted properties. It does not serialize AppProps unchanged. The [published definition](https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/definitions/plan-definition) has its own envelopes/type tables; no complete native-root-to-public mapping is established by this module scan.

## Native Formula Authoring

The formula parser uses oxc with `SourceType::cjs()` and regular-expression parsing enabled. It collects syntax diagnostics into FormulaParseError before calling the native Compiler. JavaScript syntax acceptance is therefore not native expression/function support, and neither establishes evaluation or ALM import success. Resolve this engine rather than substituting Excel, DAX, SQL or another JavaScript runtime.

The separate parse_and_compile_with_mock accepts a DataStore and FormulaTarget, performs another compiler pass when dynamic spans exist, and combines full-context requirements. "Mock" in this API name does not mean a syntax-only check or a complete visual/runtime test. Resolve actual target metadata and distinguish syntax, compilation/dependencies, evaluation, persisted formula text and portable reference restoration.

### Formula References and Target Context

FormulaTarget is Measure (default) or Row, not a user-facing column type or a portable property. CompilerOutput includes dependencies, dynamic/conditional spans, user-defined variables and requires_full_context; these are compiler/runtime objects, not serialized formula settings.

Dynamic reference helpers match exact uppercase `M_`, `C_`, `R_`, `D_` prefixes followed by native Id parsing, and `VR_` followed by a string variable identifier. Canonical cell references use `X_<row-id>_C_<column-id>`. The cell helper only checks four underscore-separated segments and parses positions 1/3; it does not validate both prefix segments. Use canonical tokens and resolved typed identities, not that permissiveness as a construction rule. Neither prefix parsing nor compilation establishes reference existence, target ownership or portable GUID support.

Identifier resolution tries dynamic references, static identifiers, then user-defined variables, otherwise returns InvalidReference. Static keywords and the named-function dispatcher use ASCII-uppercase matching; do not uppercase whole expressions, literal strings, variable names or dynamic references. Static COLUMN_PERIOD/CURRENT_PERIOD are aliases. `LEAVES` is the current row-member property for all leaves of the row; it is distinct from `MEMBERS`, `CHILDREN`, `DESCENDANTS`, `LEAF_INDEX` and a row-range. BLANK, NULL, TRUE and FALSE are distinct recognized identifiers, not evidence of equivalent business missing-value semantics.

### Formula Functions and Effect Boundaries

Use the actual dispatcher as the revision-bound named-function inventory, not an Excel function catalog or filenames alone. This revision has 171 registered name spellings, including aliases such as AVG/AVERAGE, ISBLANK/ISEMPTY, PERIOD/PERIOD_RANGE, STDEV/STDEVS, MODE/MODESNGL and RANK/RANKEQ. It first tries method-call compilation, then named functions, and errors on an unimplemented call. Registered families include arithmetic/rounding, aggregation/statistics, financial functions, text/conversion, date/period/fiscal windows, predicates/selection, lookup/context traversal and edit-triggered effects. Family membership does not certify every signature, coercion, calendar, lookup or runtime context; inspect the selected implementation and tests before composing it.

Signature checks are function-specific: IF requires exactly three arguments, resolves its condition as boolean, then evaluates the selected branch (None follows the false branch). SUM requires at least one argument and iterates all supplied arguments/array members, accumulating resolvable numeric values and skipping unresolved ones. Do not infer universal fixed arity, strict numeric rejection or Excel-compatible blank/text coercion from either example.

SETVALUE and NOTIFY_USER are registered, and OnchangeFormulaResult collects target positions and notification parts. The crate also includes assignment/variable-declaration compilers. Do not describe all formulas as pure/read-only, execute an edit-triggered expression merely to validate syntax, or export runtime result positions/notification objects into ALM. Availability in the dispatcher is not authorization or proof that effects run in every formula context; F29/F30 retain their permission, caller and save boundaries.

### Formula Evaluation and Persistence Limits

Program execution runs the compiled statements in order and returns the last result; an empty program yields Null. Do not silently treat multiple statements as one pure arithmetic expression or equate empty formula text with a missing setting. Unary compilation implements plus, negation and logical-not; numeric logical-not produces Number(0), booleans invert, and other primitive types error. Binary equality uses typed resolution and a separate XLOOKUP-predicate branch. ECMAScript parsing is not JavaScript runtime coercion or Excel/DAX parity.

FormulaDependency separates row/measure, dynamic-range/control, dynamic-row, static-cell-to-measure, dimension/column and self dependencies. The calculation-engine caller compiles with a target, maps dependencies to DataStore/node locations, and rejects a missing row dependency. Resolve graph ownership and open/closed Forecast row context; do not substitute a prefix scan for native dependency validation or assume compilation alone rules out cycles.

The ALM dispatcher selects OneLake V2 versus FabricSQL V1 with isOneLakeEnabled. In the inspected V2 column/row export, nonempty stored column/row lists pass through audit cleanup into separate columns/rows envelopes; columns also lose source sqlPk. The measure remapper maps selected property-reference fields using sqlPk-to-measureGuid metadata, not arbitrary formula text. Its presence does not prove M_/R_/cell tokens survive import into another environment. The [published FormulaMeasure](https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/definitions/plan-definition#formulameasure) specifies a string formula, not this engine's grammar or full token rewiring.

**Partial coverage:** parser/compiler ownership, reference helpers, selected operators/IF/SUM and one runtime dependency caller are inspected. Other named/method functions, assignment restrictions, namespaces, lookup/calendar/cube behavior, effective security, all reference existence/cycle checks and complete formula-text export/import restoration remain unresolved here. Full formula-bearing column/row/Forecast/on-change construction is not certified. Do not export compiled expressions, spans, execution-memory positions or dependency sets as new ALM fields.

### Formula Authoring Checks

Resolve the requested formula role, actual DataStore identifiers, target and required context; select only implemented syntax/functions with inspected signatures. Compile and evaluate against approved local fixtures separately, check dependencies and expected result types, then apply the verified native writer and route-specific ALM mappings. Preserve saved-input identities and unrelated formulas during updates. Stop the affected construction when function/context or portable reference restoration is unresolved. The [reference-free native example](#native-formula-fragment) remains a subtree, not a complete column.

Rejected native Formula subtree: valid JSON and ECMAScript syntax, but IF has only two arguments. The rejection follows the inspected compile-time signature; native execution was not performed in this pass.

```json
{"formula":"IF(1, 2)"}
```

## Must / Prefer / Avoid

**Must:** Read applicable references; preserve representation and presence; resolve real references; use exact branch/envelope/update semantics; expose conflicts and blocked core boundaries; incorporate new verified rules into this skill as well as detailed evidence.

**Prefer:** Request/model-derived creation, minimal verified updates to the specified current artifact, synthetic native-subtree examples and focused checks at the actual output layer.

**Avoid:** Copying another artifact as a template, synthesizing unknown keys/IDs/defaults, converting all JSON-looking strings, treating collection replacement as a patch or claiming generation/import support from inventory completeness.

## Synthetic Skill Examples

All examples in this document are synthetic, source-derived illustrations of the stated layer. They contain no real resource identity and are not reusable application templates, user requirements or proof of execution.

### Native Formula Fragment

Synthetic request: construct only a native Formula payload with no references. Read Native Measures and Inputs first. The fragment belongs under a resolved `measure_type.Formula` or `measure_type.VisualColumn.Formula`; it is not a full measure, column or deployable part.

```json
{"formula":"1 + 1"}
```

Check JSON syntax and source-declared shape. Do not claim expression execution or supply missing parent/ID/ALM fields by guessing.

### Preserve a Verified String Boundary During Update

Synthetic update request: change precision on the specified current visual. First verify its writer/consumer and encoding boundary. Change only the evidenced `noOfDecimal` member, preserve siblings and representation, and use the supported save route. Do not infer an exported key/path from a different visual or reset the complete setting. Unresolved adapters block the affected update.

### Decline an Unclosed Whole-Part Recipe

Synthetic request: create a Simulation input from its kind name alone. Explain the native source-measure dependency, but do not supply a runnable column when allocation, HTTP/native conversion or ALM import remains open. Resolve those boundaries from implementation and schema, not another Plan.

## Plan Item Lifecycle

### Scope, Attribution and Authorization

The [Plan Items index](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items) documents seven v1 operations. This section is the reusable lifecycle procedure for a future agent using these internal contracts; it does not run APIs, resolve tenant metadata or create a Plan merely because it is read. Public endpoint documentation can establish transport and prerequisites, not every feature's save/import behavior.

> **Telemetry - MANDATORY.** Every `api.fabric.microsoft.com` call must include `x-ms-fabric-skill` with the actual calling skill's literal name, including every pagination request, LRO poll, result retrieval and retry. For `az rest`, pass `--headers "x-ms-fabric-skill=$SkillName"` and `--resource "https://api.fabric.microsoft.com"`. Set `$SkillName` from the calling skill's actual `name` before running an example; it is not predefined. Do not send an empty name, placeholder, customer data or an invented production parent name. This manually loaded document does not assign production ownership/frontmatter. Follow COMMON-CLI.

Authenticate through approved existing Entra tooling. `az rest` acquires the bearer token for the explicit Fabric audience; do not print tokens or request passwords/secrets in chat. The pages support user, service-principal and managed identities; delegated scope requirements below describe user/delegated access and are not a substitute for tenant/service-principal configuration or resource permissions. Verify the signed-in identity, tenant, workspace access and approved authentication before a live call. Do not grant roles, change tenant settings, capacity or sensitivity labels implicitly.

On Windows, an unrecognized `az` command can be a PATH issue rather than a missing installation. Check the existing standard installation, such as `C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd`, before proposing an install; invoke a verified path with PowerShell's `&`. If sign-in is requested, run `az login` for the resolved tenant and let the user complete authentication directly. CLI authentication does not establish an authenticated browser or native workload session. For JSON requests through `az.cmd`, prefer a validated UTF-8 request file with `--body "@<request-file>"`; inline quoting can corrupt the body before the service evaluates the query. A successful file-based retry resolves that transport issue, not native definition or runtime readiness.

| Action | Authorization boundary |
| --- | --- |
| Generate/validate local JSON only | No live artifact write. Return exact layer, eligible content and blockers; no deployment implied. |
| List/Get metadata or retrieve a definition | Authorized resource read only; definition retrieval is a POST with stronger permissions. Store exports locally without echoing sensitive contents. |
| Create a new Plan | Requires explicit creation intent and resolved workspace/name/body. An empty shell does not fulfill a configured business application request; it must be separately requested, not silently substituted. |
| Update metadata/definition | Requires authorization for that existing Plan and exact proposed change; retrieve its current state and preserve unrelated content. Creation intent alone does not authorize overwriting a name collision. |
| Delete | Requires explicit deletion intent for the exact workspace/Plan; identify it and confirm destructive action when the target is ambiguous. Never automatically delete a partial creation or another Plan as cleanup. |

An explicit functional request to create/update a Plan authorizes the scoped creation/deployment and necessary permitted save/export verification; do not require a second confirmation solely because an API is involved. Resolve genuine target/scope ambiguity and enforce environment permissions. Runtime test-input writes and unrelated/destructive actions remain separate boundaries. Documentation-only requests authorize no live writes.

### Exact Operations and Permissions

Paths below are relative to `https://api.fabric.microsoft.com/v1`. All path IDs are real UUIDs resolved from the target, not example IDs. The linked operation page is authoritative for each row; do not infer permissions from the HTTP verb.

| Operation / documentation | Method and path | Request/query | Permissions and delegated scope | Success |
| --- | --- | --- | --- | --- |
| [Create Plan](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items/create-plan?tabs=HTTP) | `POST /workspaces/{workspaceId}/plans` | Required string `displayName`; optional string `description` (maximum 256 characters); optional `definition`. Omit definition to create an empty Plan. | Contributor workspace role; `Item.ReadWrite.All`. Workspace must be on supported Fabric capacity. | `201` Plan object or `202` LRO. |
| [Delete Plan](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items/delete-plan?tabs=HTTP) | `DELETE /workspaces/{workspaceId}/plans/{planId}` | No request body documented. | Write permission for Plan; `Item.ReadWrite.All`. | `200`, no result body documented. |
| [Get Plan](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items/get-plan?tabs=HTTP) | `GET /workspaces/{workspaceId}/plans/{planId}` | No request body documented. | Read permission; `Item.Read.All` or `Item.ReadWrite.All`. | `200` Plan object, not its definition. |
| [Get Plan Definition](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items/get-plan-definition?tabs=HTTP) | `POST /workspaces/{workspaceId}/plans/{planId}/getDefinition` | Optional query `format`; `PlanV1` is the currently documented definition format. No body documented. | Read and write permission; `Item.ReadWrite.All`. An encrypted sensitivity label requires sufficient usage rights to remove the label, per the page; do not remove it as a workaround. | `200` object containing `definition` or `202` LRO. |
| [List Plans](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items/list-plans?tabs=HTTP) | `GET /workspaces/{workspaceId}/plans` | Optional `recursive` boolean (default true), `rootFolderId` UUID, `continuationToken` string. Omitted root is workspace; false lists only direct children of selected folder. | Viewer workspace role; `Workspace.Read.All` or `Workspace.ReadWrite.All`. | `200`: `value` array plus optional continuation fields. |
| [Update Plan](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items/update-plan?tabs=HTTP) | `PATCH /workspaces/{workspaceId}/plans/{planId}` | `displayName` and/or `description` string, description maximum 256. Definition is not a documented metadata field. Null-clearing behavior not established; do not assume it. | Read and write permission; `Item.ReadWrite.All`. | `200` updated Plan object. |
| [Update Plan Definition](https://learn.microsoft.com/en-us/rest/api/fabric/plan/items/update-plan-definition?tabs=HTTP) | `POST /workspaces/{workspaceId}/plans/{planId}/updateDefinition` | Required `definition` object; no `updateMetadata` query switch documented on this Plan operation. Do not borrow switches from other item types. | Read and write permission; `Item.ReadWrite.All`. | `200`, no body documented, or `202` LRO. |

The returned Plan includes item metadata such as `id`, `type`, `displayName`, `description`, `workspaceId`, and potentially folder/defaultIdentity/logicalId/sensitivityLabel/tags. These response fields are not automatically accepted create/update fields. `type` is Plan; do not send a SemanticModel object or an item response back as a create request.

### Discovery and Pagination

If workspace ID is already supplied, verify that target directly; do not re-resolve by a similar name. If only a workspace name is supplied, list all permitted workspaces, follow pagination, then filter exact `displayName` using JMESPath as described in workspace/item discovery. Within the resolved workspace list Plans through the operation above, collect all `value` pages, then filter the exact Plan name. Zero, one and multiple matches are different outcomes; never choose `[0]` silently or overwrite a collision.

Use response `continuationUri` for the next GET, or an appropriately encoded `continuationToken` query while preserving folder/recursive selection. Stop only when continuation fields are absent/null; an empty page does not by itself prove completion. Verify continuation/LRO URLs are HTTPS on the expected Fabric API host before forwarding authorization. Detect repeated continuation tokens to avoid a loop. See [pagination](https://learn.microsoft.com/en-us/rest/api/fabric/articles/pagination). Carry attribution/authentication on every page.

### Definition Transport and Preservation

Create body and update-definition body both contain a `definition` object when publishing content. Get-definition returns `{ "definition": ... }`; use the inner object when building a request, not a second nested definition wrapper. `PlanDefinition` documents optional format selection and `parts`; the current format enum is `PlanV1`. Do not assume future formats or that the response always includes a format member.

Each part has string `path`, string Base64 `payload`, and `payloadType: InlineBase64`. Preserve exact forward-slash part identifiers and casing. Decode only the payload bytes to inspect a definition file; existing embedded JSON strings inside that file are a separate representation boundary. Do not put REST wrappers inside files, base64-encode an entire create request, send a decoded report-map as `definition`, or copy the Learn samples' truncated `...` payloads. Encoding the exact source bytes preserves content, including whitespace/BOM; parsing and reserializing is a content change and must not be presented as byte preservation.

For updates, retrieve the specified Plan's current definition, classify every part and modify a separate candidate within authorization. The Plan page does not establish sparse-part merge/deletion semantics; full resubmission can also reconcile collections or restore target state. Resolve those effects and `.platform`/model/connection mappings before publishing. Keep the baseline private to this update; never treat its part count or contents as a portable new-Plan constructor.

### Create a Configured Plan

Apply the [shared mandatory presentation workflow and acceptance checklists](design-standards.md#authoring-workflow) alongside these lifecycle steps. Presentation and business-contract gaps remain separate; no live publish or compliant-layout claim follows from a definition that merely parses.

1. Follow the [business authoring entrypoint](runtime-guide.md) to establish local definition generation, new live Plan or update intent. Resolve exact tenant/workspace, caller access, supported capacity, display name (and description length), collision behavior and the authorized action. If creation omits a destination workspace, resolve and use the workspace hosting the supplied semantic model; do not require a workspace ID unnecessarily or silently choose another workspace. For updates, export the latest definition and reuse its actual model/workspace unless the user requests a change. Reuse provided IDs only in their own domains.
2. Inspect the referenced semantic model's actual tables, columns/types, measure definitions, relationships, hierarchies, stable business keys, currencies, date grains and accessible connection/binding prerequisites, plus relevant permitted data, before designing the application. A Power BI model-view URL identifies a workspace/model, not its schema or a Plan definition. CreatePlanRequest has no documented top-level `semanticModelId`; a model binding belongs in its verified definition contract. Do not invent field names, relationships, connections or bindings from the model display name.
3. Build the request/model blueprint described in Model-Driven Design. Verify only requested domains, grains, eligibility, temporal/version rules, editable inputs and derived calculations. Connected outputs require resolved dependencies and shared context, not merely multiple sheets. Resolve mappings, formula dialect, validation, locking and import/writeback paths from source/schema; do not fetch a reference Plan to fill gaps.
4. Generate verified files and companion metadata with a complete identity/dependency map. Review JSON, schemas, source constraints and the publish body; reject placeholders and unresolved core envelopes. Use create-with-definition only when eligible. An empty Plan is a separate explicit lifecycle request, not a fallback for a blocked business application.
5. Submit the authorized create once, using Fabric authentication and attribution. Record request outcome and operation ID, then complete the LRO if returned. Do not report created at 202 or blindly re-POST after a timeout; reconcile operation status/exact target first to avoid duplicate creations.
6. Get the resulting Plan by the returned ID and retrieve its definition when permitted. Verify metadata, expected part set/content and reference mapping, distinguishing exact byte verification from semantic comparisons and expected service transformations. Do not claim operational success from HTTP acceptance alone.
7. Derive acceptance cases from the current request: calculations/totals, eligibility, actual-versus-planned periods, input validation/retention, version isolation, locking and connected propagation only where applicable. Exercise the actual save/refresh route and reconcile producer/consumer results without copying values. Record blocked or not-run checks; HTTP acceptance, screenshots and part counts do not substitute for business acceptance.

### Long-Running Operations and Errors

Create, GetDefinition and UpdateDefinition can return `202` with `Location`, `x-ms-operation-id`, and `Retry-After` seconds. `202` is accepted/in progress, not success; do not parse an absent result body as a Plan or definition. Follow [LRO handling](https://learn.microsoft.com/en-us/rest/api/fabric/articles/long-running-operation): authenticated attributed GET to the returned operation-state Location (or `/v1/operations/{operationId}`), honoring Retry-After with the approved runner's scheduling mechanism, until `Succeeded` or `Failed`. Do not add blocking sleep/poll loops to this agent's terminal workflow. Use bounded timeout/attempt budgets and stop on unexpected terminal states/errors instead of claiming completion.

On success, follow the operation-result Location or GET `/v1/operations/{operationId}/result` when that operation provides a result. Create needs the result Plan ID; getDefinition needs the definition response. Some completed operations have no result; do not invent a JSON response for UpdateDefinition. HTTP 200 on a state request alone is not proof that its `status` is Succeeded. Failed state/error means failure, not an empty valid definition.

Every page documents `429` with Retry-After seconds; respect it and documented `isRetriable` rather than repeatedly issuing requests. Capture status, errorCode, sanitized message/requestId and operation ID without secrets or sensitive payloads. Handle `ItemNotFound`, `ItemDisplayNameAlreadyInUse`, `CorruptedPayload`, `WorkspaceItemsLimitExceeded` or `InvalidItemType` as applicable to the operation, not automatic permission to alter names/resources or retry corrupt content. No assumed idempotency key, concurrency/ETag, rollback or selective merge behavior is established by these pages. After a timeout/unexpected write result reconcile state before any further write; surface permission/capacity/label blockers, do not work around them.

### Examples and Their Limits

**Synthetic empty-create illustration only**, no model binding or configured application:

```json
{"displayName":"Synthetic Plan","description":"Synthetic lifecycle example"}
```

**Synthetic metadata-update illustration only**, not a definition or planning-version update:

```json
{"displayName":"Synthetic Plan - Review","description":"Synthetic metadata example"}
```

The following synthetic transport illustration packages newly generated, validated files, not a reference export. Set `$ValidatedParts` to resolved `{Path, File}` mappings, `$PlanName`/`$PlanDescription` from the current request and `$CreateBodyPath` to a private task output. It preserves file bytes but does not construct features, prove import support or authorize publishing.

```powershell
$parts = @($ValidatedParts | ForEach-Object {
	@{ path = $_.Path; payload = [Convert]::ToBase64String([IO.File]::ReadAllBytes($_.File)); payloadType = 'InlineBase64' }
})
$definition = @{ format = 'PlanV1'; parts = $parts }
$createBody = @{ displayName = $PlanName; description = $PlanDescription; definition = $definition }
[IO.File]::WriteAllText($CreateBodyPath, ($createBody | ConvertTo-Json -Depth 100), [Text.UTF8Encoding]::new($false))
```

For updateDefinition use `{ definition = $definition }`, not the create body or the metadata PATCH body. Before running either, verify all required definition files/parent dependencies, path uniqueness and case, target references, decode/hash equality, JSON/source/schema validity and the change's impact. The documentation examples do not establish that an empty parts array, `{}`, or a single synthetic part is a valid configured Plan.

**Illustrative authorized CLI invocation** after setting actual `$WorkspaceId`, `$SkillName` and `$CreateBodyPath` and reviewing the exact body:

```powershell
az rest --method post --resource "https://api.fabric.microsoft.com" --url "https://api.fabric.microsoft.com/v1/workspaces/$WorkspaceId/plans" --headers "Content-Type=application/json" "x-ms-fabric-skill=$SkillName" --body "@$CreateBodyPath"
```

This demonstrates the initial request, not a complete LRO client: use a header-capable approved runner/helper to capture status/Location/Retry-After and follow the procedure above. Do not infer completion from stdout JSON or change the method for getDefinition. The operation table supplies exact methods/URLs for all remaining calls; include the same audience and attribution headers.

## Model-Driven Design

1. Extract the user's business goals, required working areas, decisions and acceptance outcomes. Do not select a preset domain/page list.
2. Inspect the supplied model's fields, types, measure definitions, relationships, stable keys, units, time/sort metadata and relevant permitted data. Resolve the hosting workspace when no creation destination is supplied. Do not assume a storage mode or connection from another model.
3. Map each requirement to real fields and verified capabilities. Separate eligible intersections, source/default values, editable inputs and derived results. Derive amounts/ranges/rates, temporal rules and allocation basis from the current request/model; clarify material ambiguity rather than inventing a default.
4. Resolve stable member/input identities and any scenario context, forecast window, actuals fallback, validation and locking contracts required by the request. Validate aggregations, blanks, zero denominators and units at the actual grain.
5. Add connected sources/queries only when needed. Verify source/query/output-field identities, transformation steps, consumer mappings, refresh order and error/status handling through the F18/F19 contracts and scoped checks. Do not infer an automatic cascade or private API.
6. Apply the shared presentation standards to this blueprint, construct eligible definitions and validate/save under the lifecycle workflow. For updates, preserve only the specified current artifact's relevant configuration and input identities.

Apply the following reusable checks to the selected features before construction and during acceptance. Do not add features merely to exercise the checklist.

## Reusable Authoring Checks

### Contract-Gap Resolution and Route Fallback

Enter this procedure only for a concrete missing or contradictory required contract, relevant known compatibility change, or unresolved validation failure under the [contract reuse policy](#contract-reuse-and-source-investigation). It applies during business authoring as well as authorized maintenance. A partial catalog entry alone does not require source investigation when the requested branch is covered. The creation supplement reviewed 2026-11-07 reinforces these responsibilities but supplies no new native schema or proof that its historical scripts work on the current build.

1. Identify the exact requested capability, target build/source family, required representation and missing boundary. Separate an unknown construction field from an unperformed runtime test or missing optional style control.
2. Inspect the relevant current behavioral owner, complete record writer, identifier resolver and selected export/import conversion. Reuse an inspected technical adapter where available; resolve its defaults, tagged settings, companions and environment mappings rather than copying a business application.
3. If the AI schema route lacks a compiler or reports a stub, inspect the documented Plan definition/ALM route and approved native application save provider. Conversely, a public-schema mismatch may require the current native writer; it does not authorize inventing a field. Verify each route's authentication and target context before use.
4. Use current schemas or independently authored, sanitized feature-level fixtures to check the selected representation. A fixture is optional technical evidence, never a requirement to discover/export another Plan or copy its pages, assumptions, identities or connections. Self-generated parse tests alone do not certify a writer.
5. Construct the exact resolved parts and reference graph, complete pre-save checks, and execute the authorized save when eligible. Do not demand import/readback or live propagation evidence before the first creation that produces the item being checked.
6. Retrieve the saved result and verify its definition, catalogs, computations and presentation through reachable authorized tools. Resolve observed defects through the actual owner, preserve the created item, and reconcile uncertain writes before retrying.
7. Declare a blocker only when a required construction/access prerequisite remains unavailable after applicable routes were investigated. Record capability, attempted route/owner, evidence/error, missing prerequisite, business impact and any independently saved outcome. Do not label the product unsupported unless that limitation was established.

| Situation | Required action | Save/completion consequence |
| --- | --- | --- |
| Catalog section marked partial | Use covered requested branches directly; investigate only a required gap or conflict. | Not a blanket prohibition or a requirement to certify the whole catalog. |
| AI schema adapter disabled or stubbed | Investigate direct item-definition/ALM and approved native writer routes. | Blocks that adapter, not the feature across every route. |
| Exact envelope, source identity or required dependency unknown | Resolve through the selected current writer/resolver/import mapping; keep the unresolved payload out of submission. | A genuine pre-save gate for the affected payload if no supported route resolves it. |
| Native provider needs different authentication/context | Resolve through approved application access; do not reuse an old report's workload token or assume Fabric bearer equivalence. | Access failure can block that provider; retain independently supported work. |
| Import/readback, renderer or test identity unavailable | Save a supported eligible definition, then report which follow-up checks are blocked/not-run. | Prevents the corresponding verified/compliant claim, not necessarily saving. |
| Required Home/Arial/group styling missing on one route | Inspect the surface's native writer and applicable alternative; disclose any remaining gap. | Does not justify guessed properties or abandoning supported business work; full presentation acceptance remains incomplete. |
| Core requested calculation or dependency cannot be constructed | Resolve the real missing construction contract; do not publish a decorative or disconnected substitute. | Blocks a working-application claim and an unusable substitute, not unrelated supported operations. |

Use the existing [readiness stages](#construction-readiness-and-evidence) to report what actually happened. Public API acceptance, saved-definition verification and business behavior are distinct outcomes; later verification failure must not erase a known successful creation or trigger duplicate creation.

These are general design and validation procedures, not additional verified wire contracts. Obtain exact fields, enums, formula syntax, defaults, supported source types and ALM mappings from the selected feature's documented contracts and applicable schema. Resolve concrete gaps under the contract reuse policy; runtime behavior still needs its separate checks. Do not consult another Plan as a creation template or import its settings to satisfy a check.

### Construction Readiness and Evidence

The user-supplied creation supplement, reviewed 2026-11-07, contributes implementation responsibilities and prospective acceptance checks, not newly verified native schemas. Its historical fixes and script inventories are not turnkey constructors. Reusable guidance is merged below; private project paths, resource identities, deployment narratives and continuation commands are not part of this library.

Label evidence as **public API contract**, **code/schema evidence**, **historical observation**, **illustrative design**, or **unresolved**. Record the applicable source/build and validation layer. A historical user-reported fix is a diagnostic hypothesis until reproduced for the target route; an internal registry or staging format must never be submitted as native Fabric JSON.

| Readiness stage | Required evidence | Does not establish |
| --- | --- | --- |
| Prepared | Current request/model blueprint and intended dependencies. | Complete native records or serialization. |
| Package checked | Exact part decoding/encoding, applicable schema/source checks and reference invariants, with coverage gaps. | Fabric acceptance or import completion. |
| API accepted | Immediate response or checkpointed operation identity. | Completion of an asynchronous import. |
| Import completed | Successful operation and retrievable resulting item. | Runtime catalogs, calculations or rendered visuals. |
| Saved-definition verified | Re-export/readback compared with the candidate, accounting for evidenced service transformations. | Query materialization, edit enforcement or propagation. |
| Runtime verified | Actual native source/query catalogs, output schemas and data results resolve. | All requested interactions or financial outcomes. |
| Behavior verified | Authorized edits, save/reopen, refresh, context, locks, navigation and applicable restricted-user tests. | Every future build or untested variant. |

Use the existing `passed-scoped`, `partial`, `blocked` and `not-run` statuses for individual checks. Block an affected output when its required envelope or reference mapping is unresolved; continue independently supported work. Do not turn an optional gap into a blanket claim that all Plan creation is impossible, or label an incomplete application fully compliant.

Treat these as responsibilities of the owning adapters/writers, not a requirement to create ten new modules or another harness:

For authoring, satisfy the responsibilities actually used by the chosen route through existing writers or a scoped adapter. The table is not a requirement to implement an entire framework, obtain all runtime completion evidence before saving, or certify unused feature families.

| Responsibility | Required implementation boundary | Completion evidence |
| --- | --- | --- |
| Target-build adapter | Version/route selection, envelopes, defaults, enums and encoded boundaries. | Independently authored records deserialize and round-trip on the selected route. |
| Native source resolver | Actual semantic/source registration and identifier grammar. | Assigned fields resolve in the target catalog, not only TMDL. |
| Identity registry | Owners and external, portable, persisted and runtime namespaces. | Unambiguous source/destination mappings and no unresolved typed references. |
| Input/formula writer | Complete records and aggregation, display, context and rule companions. | Imported measures exist and compute under the intended context. |
| Connected-query compiler | Sources, operator-specific transforms, grain, output schemas and dependencies. | Field availability, append compatibility and dependency checks pass. |
| Query importer/registrar | Destination remapping, dependency order and output registration. | Runtime query catalog and actual outputs resolve for consumers. |
| Filter/context writer | Assignments, filter registrations, selections and persistence context. | Standalone/embedded selectors agree and inputs remain isolated. |
| Maintenance adapter | Actual source/schema, keys, lookup settings and save semantics. | Authorized read/insert/update, generated-key and conflict checks pass. |
| Home/layout writer | Mode-authoritative role content/assets and owner/override geometry. | Ordinary-read navigation and rendered layout pass for intended roles. |
| Deployment verifier | Single submission, LRO/result recovery, saved readback and bounded checks. | Accurate stage-specific evidence, including failed/blocked phases. |

Where authorized test resources exist, first prove the requested connection mechanism on a small meaningful slice: one input, its source/query path, one dependent calculation and one consuming visual. Independently inspect native registrations and test an actual saved edit before expanding. This is a validation strategy, not permission to provision test data, publish a placeholder Plan, or replace the requested application with a smaller one.

### Complete Records and Independent Checks

An input/formula writer must resolve the owning visual, persisted and measure identities, selected native type, order/visibility, both axis aggregations, formatting, context and applicable rules through their actual writers. A valid inner configuration is not a complete column; copying a label and operation enum into an open property bag does not supply those companions.

For the source-verified Number metadata branch, a scalar such as `"default_value": 100` is not the tagged native setting. The following is an inner metadata fragment only, not a column or Plan part:

```json
{"default_value":{"Static":100},"min_value":{"Static":0},"max_value":null}
```

Preserve existing `Measure` defaults and already tagged objects; never double-wrap them. Select **option sources** use `Static(array)` or unit `Lookup`, while select **default values** use the separately defined Static option/Dimension/Measure union. Person and Simulation have different metadata. Planning ALM `/columns` and inserted-row `/rows` envelopes belong to their separate parts; do not append inserted rows to `dataInput.json`.

Parent-to-child numeric distribution is a business choice, not a universal creation default. Where requested and supported, verify the toggle independently from weighted rules. Resolve the actual Average (Leaf) serialization for rates/prices whose intended aggregation requires it; do not replace every formula, quantity or amount aggregation with Average (Leaf). Check row and column choices independently and retain explicit behavior for totals and locked descendants.

Audit formula, default, editability, lookup, min/max and distribution-driver dependencies together, including owner/source kind, missing nodes, cycles, null/zero behavior and alternate pivots. Preserve raw numeric tokens losslessly if the selected format uses them; preserve source-declared decimal strings as strings. TMDL names/lineage tags alone do not prove native registrations. A source-backed hash of a verified canonical source key is distinct from inventing an ID from a display name; use only the selected resolver's actual algorithm and input domain.

Compare against independently authored, approved, sanitized feature-level fixtures or the current writer/reader, not a self-generated object parsed by the same helper. Fixture inspection does not authorize discovering/exporting another Plan or copying its business design. Local helper consistency, native deserialization, saved-definition preservation and runtime behavior are separate checks.

### Grain, Eligibility and Workload

- Record each sheet's business question, row/column grain, field sources, inputs, calculations, context and outputs before generating it. Resolve field identity, type and relationships rather than matching labels alone.
- Keep intersection eligibility, source/default values and edit permission separate. Specify whether new members without historical facts are eligible; do not turn missing facts into zero or let helper values create unintended combinations.
- Choose aggregation from measure meaning and units. Additive quantities, rates, prices and calculated ratios can need different treatment; check leaf, subtotal and grand-total results instead of imposing one aggregation mode. Parent distribution is a separate decision.
- Verify chronological keys and label-to-sort-key consistency across multiple periods. Check the consumer's actual axis source/sort as well as model metadata.
- Estimate expanded workload from eligible leaf intersections, periods and displayed measures, including hierarchy/subtotal effects. Bound scope with request-appropriate selections and validate actual loading; pagination, a fixed historical cell limit or a preset regional filter is not a capacity guarantee.

### Identity and Dependency Registry

- Maintain a task-local registry separating external item/model/connection identities, sheet/visual identities, native or persisted input/measure identities, and query/output-field identities. Record each owner's scope, reference domain and verified import conversion.
- Preserve identifiers losslessly in the representation required by their decoder. Where the verified contract uses decimal strings, do not pass them through JavaScript `Number`, floating-point arithmetic or spreadsheet numeric coercion; distinct large IDs can round to the same value. Check identity equality across owned record/registry references without changing their types. A fixture-local random allocator is not a service allocation contract. Scope reference audits to the actual visual and typed reference fields: a text-prefix scan or recursive registry search alone cannot validate every formula dialect, default, forecast, semantic-model or connected-query binding.
- Resolve formula dependencies through that registry and the actual formula engine's syntax, not display names, a guessed prefix or a hash of a label. Check duplicates, cycles, dangling references and references owned by the wrong visual before packaging and after import.
- Keep display descriptions distinct from persistence keys. Verify mapping, pivot/context companions and allowed exclusions together; do not exclude a dimension merely because it is descriptive. Where rename or reassignment retention is requested, test that behavior explicitly.
- A connected consumer does not create its source/query or output schema. Generate all required companions through verified contracts, in dependency order, and check registered output identities. A measure hierarchy explains the design but is not the formula dependency graph.

#### Source-Kind Identity Reconciliation

Reconcile source assignment identity, destination native measure identity and persisted column identity separately. The supplied identity-repair code distinguishes semantic fields from From Sheets fields; its historical calculations are diagnostic evidence, not a universal allocator or proof of the current target's resolver.

Source snapshots and inspection limits for these library-derived checks are recorded in the ALM library corroboration ledger. They refine diagnostics, not the current generation-readiness status of the underlying feature contracts.

| Observed branch | Diagnostic comparison | Required boundary |
| --- | --- | --- |
| Row/column dimension | The dimension repair compares `visualState.rowDimensions` and `columnDimensions` IDs with unsigned decimal XXH3-64 of each exact `externalKey`. | Confirm the target dimension resolver and dependent references. Random authoring IDs are not substitutes for derived native dimension IDs; the historical repaired blend job still required runtime confirmation. |
| Semantic assignment | The verifier compares unsigned decimal XXH3-64 results for the assignment's exact `id`, with upper-cased aggregation plus `__` prefixed only when aggregation is present. | Confirm the selected resolver's canonical input and aggregation behavior; never hash a display label or apply this to every ID domain. |
| From Sheets assignment | The repair first maps the source's portable `measureGuid` to its actual runtime column `id`, then compares the aggregation-prefixed runtime key. | Read the authoritative source-column mapping for the actual owner. Do not predict a column ID from creation order, use a query ordinal, or hash the portable source GUID as if it were the runtime column ID. |
| From Queries consumer | The repair obtains the canonical destination measure binding from the actual exported consumer assignment. | Resolve query/output-field identity and destination measure identity independently; a query GUID or output-field ID is not a formula measure ID. |

The current native data parser sharpens the canonical-key rule: `ColumnType::Measure` keeps the exact assignment `id` regardless of aggregation; a non-Measure column prefixes the upper-cased aggregation plus `__` only for an explicitly present, non-`None` aggregation. The datastore then hashes that processed key through `Id::for_str`. Its separate `custom_source_measure_id` path uses a valid `measure_guid` directly only when the `planning_mock_custom_source` feature flag, `custom_source` marker and measure bucket all apply; otherwise it falls back to hashing. Do not copy a sample's custom-source override, assume that flight is enabled, or diagnose a hash mismatch without checking this branch and portable/runtime rewiring. Source inspection is not proof of deployed bindings.

For the observed Planning column route, compare the outer `measureGuid` with `columnMeta.id` and the owning assignment/measure registry, preserving each decoder's exact representation. Audit dependencies in defaults and editability as well as formulas. The supplied checker covers decimal `M_` tokens and string-valued `Measure` references within an owning column set; its pass is not coverage of every formula dialect, row/cell reference or external catalog.

If import changes an identity, build an explicit old-to-canonical map from the saved target, check collisions and owner domains, and update only affected typed references and keyed metadata. Reject stale references and cycles, and verify independent actual/forecast or context branches as applicable. Do not copy the historical scripts' recursive string replacement or whole-application clone workflow into a safe-update recipe. A local JavaScript evaluation of one formula remains an arithmetic expectation, not native parser, engine or persistence verification.

### Assignments, Filters and Context

> v18: [measure-display-defaults.md](measure-display-defaults.md) is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

Treat field assignment, filter registration and selected filter state as separate checks. Verify the correct visual/page/global/context scope, compatible field identities and selected values through the relevant writers; do not copy a field into every assignment list or manufacture opaque cache/hash values.

For the supplied helper's scoped `PLANNING`, `SUPER_FILTER` and `ANALYTICS_PLUS` cases, registrations live in `properties.superFilterAssignments`, not a newly invented `filterRegistrations` member. Check an existing registration's target through its sort/assignment metadata, not its label. The helper distinguishes grouping-field registration from measure registration, which retains grouping context and the selected measure; it does not certify every field type or visual family. Do not copy its sample-derived filter templates into a new Plan as defaults.

When synchronizing default registrations after an assignment change, require exactly one applicable non-context registration per intended assigned field. Preserve existing IDs, explicit/context entries, selections and configuration; update only the verified default registration's assignment/bucket metadata when necessary. Check that running synchronization twice produces the same result and that all non-filter properties and unaffected payload bytes remain unchanged. An empty `filter` array in these registrations is not proof of an explicit member selection or input-context isolation. Verify visible filter cards and interaction separately from saved-definition coverage.

When the requested design uses semantic master dimensions, retain those fields on axes and slicers and bind connected sheet/query measures to Values through the supported adapter. This strategy is not a proof of RLS or a prohibition on other source kinds supported by a verified contract. A single-select scenario context can replace a visible scenario row only when input keys, source/query grain, outputs and downstream matches still carry that context.

For scenario-aware planning, resolve the actual persistence-context contract and carry that context through sources, transforms and consumers. Test distinct values at the same intersection in two contexts, including save/reopen. A visible selector or saved bookmark alone does not establish input isolation. Check standalone and embedded interactions independently, including conflicting filters and source-filter effects on materialized results.

Distinguish a business version stored in model/control data, a native scenario simulation and a Forecast measure's period/version configuration. Select the mechanism from the requirement; neither a version number nor a business selector proves a native scenario lock. Where closed-version retention is required, separate the edit predicate from the displayed-value predicate: closing a version must not switch its retained planned values to actuals merely because editing is disabled. Verify the display rule and write restriction independently after the applicable control-data refresh.

### Business Controls, Lookups and Rules

Separate where control data lives, how it reaches the consumer, how its keys/grain match, and which default, calculation or rule uses it. Choose a supported direct-sheet, query, model or persistence route from the requirement and verified capabilities; neither SQL writeback nor a particular query pipeline is universally required.

- Keep master identity, validity/effective dates, suggested values, limits and distribution weights distinct. A descriptive lookup does not create a database constraint, and generated technical keys require both backend and native-save verification when relevant.
- For a database-generated maintenance key, inspect the actual database definition; hidden/read-only UI metadata does not create an identity/default constraint. On authorized test resources, omit that key when creating a valid row, then save/reopen and verify a generated unique key and preserved business fields. Do not enable deletion or drop/recreate an existing table to bypass a key-generation or migration gap.
- Do not allocate surrogate keys with `MAX(id)+1`. New-table identity/default design requires separate provisioning authority; an existing table may require a deliberate migration rather than a direct ALTER. Preserve referenced keys and verify effective-date overlap rules separately from uniqueness. Foreign-key lookups must store the actual ID while displaying the intended description, with compatible source/key types and nullability.
- Keep parent-to-child distribution, weighted allocation, min/max rules, lookup configuration and anchor/display settings separate. Verify each selected feature's applicability, scope and serialization; enabling one does not prove another is configured.
- For lookups, test missing, duplicate and ambiguous matches, null versus zero, inclusive/exclusive limits and the intended fallback. Do not silently substitute zero for an unresolved match or limit.
- For weighted distribution, establish units, applicable grouping/context, normalization and rounding from the request and engine contract. Test zero/negative/missing weights, locked/excluded cells and reconciliation of children to the entered parent value.
- Test rules/lookups at leaves, totals and alternate pivots. Verify the actual view state captured/restored by bookmarks; views must not duplicate data, invent scenarios or change input identity unintentionally.

### Connected Results and Freshness

Define common keys, units, period/context and aggregation grain before joining or appending outputs. Check unmatched keys, duplicate contributions, overlap between leaf/subtotal streams, conversion direction and sign conventions. Compute ratios from the intended aggregated numerator/denominator rather than summing displayed ratios.

For append inputs, compare the final projected names, aliases, field roles and primitive types with stored selected-field metadata and consumer bindings; check order where the engine combines fields positionally. Reducing grain requires an explicit aggregation, not merely removing a detailed dimension. Add typed non-contribution values only when the business rule establishes that meaning; do not convert an unknown or missing value to zero to make schemas agree.

**Bridge-query date placement:** date/period fields normally belong in Columns. When Year -> Quarter -> Month is already selected in Columns, do not also select `YearMonth` or the equivalent date field in Rows; this duplicates the same time grain in the pivot. Rows should contain the business dimensions needed for the contribution, such as region, scenario, financial group and account. Apply this consistently to all normalized contribution queries and the append/consolidation query, not only the workforce and operating-expense examples. An explicitly requested row-oriented date analysis is an exception, not the default.

Distinguish available output fields from selected pivot roles. Remove the redundant date from the **selected row dimensions**, preserving the existing column hierarchy, date helpers, field identities and unrelated selections. Keep the canonical period/date key in SQL projections, grouping, normalized append schemas and downstream bindings wherever required for monthly grain and alignment; clearing a pivot row is not authorization to drop the data column, aggregate across periods or alter SQL/sign logic. Use the actual query/pivot writer, inspect fresh query metadata before updating an existing Plan, and verify saved selections and period-level reconciliation after the change. Reject both duplicate row/column date selection and an append input that loses its required period key. Metadata checks do not establish refreshed-query totals or rendered acceptance.

The Pivot Table dialog constructs `sourceDimensions`, `sourceColumns`, `sourceMeasures` and a `removeColumns` list when selections change. Its Apply action creates a transformation, not necessarily a display-only override. Inspect the actual source catalog plus ordered rules and validate the resulting append schema before using this route; do not patch guessed source metadata or assume deselection leaves every output field intact. If a query has no period selected in Columns yet, resolve the supported date-column/hierarchy configuration first, rather than removing its only selected time field. For new construction, select the canonical period in Columns; preserve an already-resolved Year -> Quarter -> Month hierarchy instead of adding a second equivalent period selection.

**Native date-axis persistence:** source enrichment can rebuild `sourceMeta.selectedDimensions` and reintroduce a raw period in Rows even when the authored catalog excludes it. Read `GET /v2/ib/queries/{resolvedQueryId}/transformations/metadata/` and `GET /v2/ib/queries/{resolvedQueryId}/transformations/`, using the established CLI workload authentication/context. The metadata payload's `sourceMeta` is the base catalog; the second payload's `transformationRules`, ordered by `stepIndex`, determine subsequent selections. Inspect the rules actually used by the query, not just the initial catalog. Handle unknown later transforms explicitly; neither a base-catalog fix nor a saved step proves the final materialized schema.

The native pivot writer POSTs an array of `{type:50,value:{isValid:true,sourceDimensions:<resolved business Rows>,sourceColumns:<existing period Columns>,sourceMeasures:<existing Values>,removeColumns:[]}}` to `/v2/ib/queries/{resolvedQueryId}/transformations/`. The rule update writer PATCHes a single `{type,value}` to `/v2/ib/queries/{resolvedQueryId}/transformations/{resolvedRuleId}/rules/`. Both use UTF-8 JSON bytes and `application/octet-stream`, not guessed source-metadata fields or multipart upload; resolve the v1/v2 route from the actual target mode. In PowerShell, retain a typed `byte[]` with a direct encoding assignment rather than an `if` expression that can unwrap it into `Object[]`. Preserve IDs and all unaffected fields/rules, journal before a save, and reconcile a rejected/uncertain write through a fresh rules GET before retrying. Use PATCH for an existing owned rule rather than adding duplicate projections.

When correcting only redundant date placement, retain the existing native period columns and value definitions and request no explicit column removal. An empty `removeColumns` list does **not** certify that every post-transform field survives: refetch the saved rule, verify effective Rows/Columns through the ordered transformations, then validate materialized monthly keys, column names/order/types and reconciliation across all append inputs before claiming native financial acceptance. An authorized new-Plan run saved/refetched all five date-selection rules and retained six professional Arial header canvases; materialized append results and rendered appearance were not verified by those property checks.

Track the available field set after every transformation. Reject a field referenced before creation or after removal, and a projection that both selects and removes it. Inspect selections, filters, sort and date/hierarchy helpers when a field is missing. Derive a required field in the executed pipeline through a verified transformation; adding it only to metadata cannot create an output column. Validate the actual post-import output, not only declared schema equality.

Track source edits, persisted source values, last-refreshed query outputs and consumer results separately. Resolve the actual save/recalculation/refresh mechanism and dependency order; do not promise an automatic cascade or invent a refresh API. Verify that source filters and query scope match the reported total, and test access to materialized outputs under the relevant restricted identity. Correct semantic assignments alone do not prove end-to-end security.

Register source/query/output identities in dependency order and inspect the destination catalog, lineage, output schema and actual data before diagnosing an empty consumer as a chart problem. Transformation operator codes, Parquet versions and materialization metadata are route/build-specific; never fabricate file paths, success flags or row counts. Reject cycles, expose terminal failures and stale outputs, and coalesce redundant refreshes only through supported orchestration. On authorized temporary tests, restore the changed input through the same verified save path and confirm the restoration.

Treat business-version locks, period/intersection locks and optimistic concurrency as distinct controls. Test rejected writes at leaves and parents, including distribution into locked descendants; a hatch pattern is not enforcement. Use rowversion, ETag or revision checks only where the selected persistence endpoint supports them, preserve the current revision and follow its actual conflict response.

### Dependency Readiness and Safe Packaging

Creating a Plan does not provision its external data, semantic model or connections. Change those dependencies only when the current request authorizes it. Keep workspace/item, source-data, connection and runtime permissions separate; successful publication does not prove data access.

When authorized dependency changes are needed, verify source schema/data, endpoint visibility, model metadata and a representative query in order, using the actual connection/storage mode. An operation completing is not proof that a newly added field is queryable. Preserve the requested model and coordinate concurrent updates rather than replacing it with a sample model.

Keep readable candidate definitions and a private path/byte/hash manifest when appropriate. Preserve non-JSON content and unaffected payload bytes during updates, parse according to the actual response/encoding type, and round-trip the packaged bytes. Record operation outcomes for safe recovery; do not replay queued creates after an ambiguous result. Never put credentials, workload tokens or private deployment records into reusable skill content.

#### Saved Connection Omission and Bounded Repair

Evidence provenance for this section, the readback comparisons and the discarded-heading check is retained in the recorded-build review. These observations do not refresh the product-source revisions or certify a new construction route.

Treat an omitted dependency-bearing field as a separate failed preservation check, not an innocuous service normalization. In the supplied recorded build, root `definition.json.appDBconnection` was present in the submitted candidate but absent from the creation export and again after one targeted same-item update. The repair record reports `persisted: false` and native storage behavior unverified. This establishes a saved-definition gap for that run, not a universal unsupported field, a proven collaboration failure or a reason to provision a replacement connection. Keep application storage, semantic-model binding and writeback destinations distinct.

When a scoped repair is authorized and its writer is verified, base it on the saved destination export, preserve all unrelated parts, and prove that the candidate changes only the intended field. Re-export immediately before submitting and compare against that baseline; stop or rebase on drift rather than overwrite another edit. A clean pre-update comparison is not an atomic concurrency guarantee. Record submission intent, payload hash and operation identity, then inspect the final export of the same item. If the field is still absent, retain the unresolved result; do not loop identical repairs, recreate the Plan, invent a private connection endpoint or substitute another connection without resolving the actual persistence route and authority.

Keep the failed connection check visible even when all other definition checks pass or the reconciliation report has no unexpected differences. Establish effective collaboration storage and save/reopen input retention through authorized native checks before claiming them. Historical source values and repair code are evidence only, not connection defaults or an authoring template for a new application.

#### Evidence-Scoped Readback Reconciliation

Retain an exact raw comparison alongside a narrowly reconciled comparison and a separate list of unresolved requirements. A report's `unexpectedChanges: []` means no unclassified changes under its comparison policy; it does not mean every requested property persisted or every acceptance check passed. The supplied recorded build retained the failed connection check independently of its reconciled diff.

- For an observed GUID-casing change, compare only verified identity fields or GUID path segments case-insensitively, retaining the original spellings. Reject collisions before building a canonical-key map. Do not lowercase entire part paths, case-sensitive filenames, arbitrary strings or business keys; a JavaScript/Python map can otherwise hide duplicate entries.
- For a demonstrated identity-keyed visual-reference registry, reject duplicate identities in the owning scope and compare complete records by identity. Preserve sheet order and all positional arrays. Identity alignment must still detect changed `isEmbedded`, visual type, owner and other fields; it does not prove rendered stacking order.
- An observed empty writeback `destinations` array omitted on export may be classified only when the submitted list was actually empty and the saved field absent. Do not ignore a missing nonempty destination or make absent, null and empty universally equivalent. Likewise, record an added writeback version at its exact path/value rather than ignore all version metadata.
- For the observed PowerTable column `sourceId` addition, require that the candidate lacked the field and the saved value equals the actual owning source's `recordGuid`. Match columns through their verified record identities and compare every other field; do not rely on zipped array positions or apply this mapping to other source kinds.
- Compare platform metadata field by field with exact evidenced exceptions. Do not skip the whole `.platform` object, even when it contains destination-generated values. Semantic comparison and byte preservation are different results: a replay with serialization-only differences must not be reported as byte-identical.

#### Plan-Level Properties and Sheet Readback

The [public PlanProperties schema](https://developer.microsoft.com/json-schemas/fabric/item/plan/definition/PlanProperties/1.0.0/schema.json) defines `planProperties.json` with `properties.workloadModeConfig`, including complete EDIT and READ visibility records. The native initial mode configuration supplies pane defaults; visibility is not permission assignment or Home role-layout content. The importer reads this part, normalizes its schema and stores workload properties.

The inspected exporter returns before its sheet-property loop when workload properties are schema-only or empty. A created item without the root part subsequently exported its sheet registry and visuals but no `sheet.json` parts. This is a concrete readback gap consistent with that code path, not proof that the sheet settings were deleted. Include a legitimate, schema-validated Plan-level baseline in fresh construction; do not insert arbitrary placeholder properties to defeat the guard. For an existing item, use a fresh destination export, preserve every unrelated part and add/repair only the verified root settings, then re-export the same item. In the scoped follow-up, this additive same-item update restored all authored sheet-setting parts to the export, and their complete configuration passed preservation checks. Until each target's readback succeeds, retain its sheet-setting preservation as unresolved. This does not close native Home V2 authoring, layout rendering or input-retention acceptance.

### Layered Acceptance

Define a small auditable case from the current request with explicit expected values. Exercise applicable input/save/reopen, calculation, parent/leaf behavior, context isolation, source-to-consumer propagation, filters, views, rendering and restricted-user access. Local arithmetic is an expectation, not deployed execution evidence.

Report separate states for local preparation, syntax/schema checks, API outcome, saved-definition readback, native input/runtime checks, rendered checks, business reconciliation and security checks. Use passed-scoped, failed, blocked or not-run with concrete evidence. Symptoms such as missing inputs, blank grids, unresolved formulas or missing queries guide checks of the relevant boundary; historical fixes do not establish the cause of a new failure. Existing contract gaps remain open until independently verified.

### Failure Triage

These are first discriminating checks, not asserted root causes or universal repair recipes. Preserve the failing record, owner/context and sanitized operation/job evidence before changing it. Use the [presentation checks](design-standards.md#embedded-layout-and-navigation-checks) for geometry, titles and format-family issues.

| Symptom | First checks |
| --- | --- |
| Inputs/formulas absent | Complete owning record, selected type, tagged defaults/bounds and import registration. |
| Formula `#REF!` | Actual destination identity, owner/source kind and reference conversion. |
| Lookup `#N/A` | Source availability, key/grain compatibility, missing or duplicate matches and pivot/context scope. |
| Empty From Queries or query not found | Destination query catalog, GUID remapping, permissions and materialization, not JSON presence alone. |
| Empty or locked matrix | Eligibility/default-source results, context selection, stable key mapping and edit predicate. |
| Native source values absent | Resolved semantic source, model permissions/readiness, filters and actual measure evaluation. |
| Assigned field absent from filter pane | Family-specific filter registration and selected visual/page/context scope. |
| Incorrect period order | Year-inclusive semantic sort key, executed query ordering and visual sort state. |
| Wrong linked-sheet source | Destination visual ownership, compatible dimensions and typed source/measure remapping. |
| Inflated consolidated totals | Grain mismatch, duplicate leaf/subtotal contributions, overlapping domains and join cardinality. |
| Consumer unchanged after save | Persisted source value, dependency job/order, output freshness and consumer refresh state. |
| Accepted import but blank sheet | Completed import and saved parts, then native catalogs/data and actual rendering. |

#### Initialization and Native Request Failures

URL repair has a create-versus-update boundary. Do not retry a failed readback,
remove a binding or recreate the Plan automatically. Use only an approved
external service profile when a fresh property operation is required; if none is
available, obtain authorization for a supported create path. A saved definition
still requires independent acceptance.

Validate the semantic-model runtime handoff, not only model/workspace IDs. The shell callback returns stored/cached model details without filling a missing URL. FabricHost forwards `semanticModelDetails.url`, while native SemanticModelDetails requires a string `url` without a deserialization default. An undefined JavaScript value is omitted on JSON serialization; the WASM constructor parses the request and panics on a parse error before initialization/fetching. A generated Plan missing `semanticModelReference.url` is therefore a concrete startup-contract defect, even if its model IDs and public definition schema pass. Resolve the real model URL through approved metadata or authorized evidence for the same verified model/workspace; reject missing/null/invalid URLs before publishing, do not fabricate one or use an empty-string placeholder. A URL-only repair must preserve binding identities, connections and unrelated content. The observed omission and inspected failure path are not native-runtime recovery proof; verify the saved repair and actual affected visual afterward.

First establish whether the current load emits a data request. If none is emitted, do not require a nonexistent HTTP response or attribute the failure to earlier unrelated 400s. Capture the current Show Details message and the exception/stack logged as `FabricHost: Failed to initialize app instance`. The inspected host initialization handler covers engine initialization and later setup; the native orchestrator parses the property map before launching data and measure requests, and property parsing propagates errors. This identifies a pre-request investigation path, not proof of a particular malformed field, worker failure or current deployed code revision. Check the relevant frame/worker and capture interval before inferring absence; keep engine creation, property parsing, cached/new-visual paths, fetching and rendering distinct. Do not repair InfoBridge transformations merely because initialization failed before data loading.

For `Initialization Failed`, `unreachable`, or a native source-column request returning HTTP 400, retain the first failing request's method, sanitized response body, owning sheet/visual and selected field context. Reconcile exported assignments and companion records with the destination's actual runtime properties and column registrations. A successful item operation or unchanged export cannot establish that the native engine resolved those records; a truncated console URL alone cannot establish the rejected field or root cause.

`Unable to get mutable reference to target column array` can originate when a typed array accessor returns None: numeric formula updater requests Float64 storage, and the accessor accepts only that array variant, not BorrowedArray even when its logical type is Number. Check the owning node, declared logical type, actual storage variant and whether writes are permitted; the message alone does not establish a missing column, lock contention or the cause of a subsequent WebAssembly trap. Retrieve actual semantic-measure data types rather than assigning Double to every DAX measure: integer governance measures and floating-point amounts can coexist. Keep external assignment types distinct from the native Number logical type: Int64 and Double both map to Number, so correcting one to the other does not prove a storage-variant failure is fixed. A corrected declaration is a verified configuration change, not proof of runtime recovery until the affected visual loads and computes successfully.

Investigate formula diagnostics separately from data-source and asset-loading errors. The supplied repair script changes single-equals checks in selected native formula/editability fields and clears an inherited PowerTable assignment cache, but explicitly records the candidate as unverified. Do not copy its `= 1` to `> 0` replacement: equality and positivity are different business predicates. Validate the intended predicate with the selected native parser/compiler and retain DAX, SQL and native expression dialects separately. Clear or rebuild a cache only after proving its owner/reference mismatch; never erase all assignments to suppress an error.

Repeated icon registration, missing manifests, export timeouts and a WebAssembly streaming MIME warning can coexist with a native initialization failure. Establish whether the asset fallback completed and whether a later native request failed before attributing the failure to those warnings. Record preparation, import/readback, native loading and business verification independently; a repair remains a hypothesis until the same affected visual and request succeed, with intended calculations and context preserved.

##### Reference Comparison and Recovery Gates

When a user authorizes comparison with a named working Plan, export that reference and the failed target freshly into separate private evidence records. Inventory and hash every part, preserve exact native integers and case-distinct keys, and decode established nested JSON boundaries. Compare corresponding feature roles and actual source/query/consumer bindings; different page counts, identities or optional UI state are not defects by themselves. Never copy a reference connection, saved inputs, metadata caches or whole application into a replacement.

Use the following fail-safe sequence before a corrected deployment:

1. Reconcile the original generated candidate, any intervening repair and the fresh failed-target export. Confirm whether an alleged correction is already saved before repeating it. Preserve all prior journals; a newly named artifact requires a separate run and fresh authored identities, not reuse of an old create/export checkpoint.
2. Verify semantic assignments against current model field/measure metadata, including integer eligibility/window measures versus floating-point amounts. Reconcile companion identity, native kind, logical type and formula references separately. Int64 and Double both becoming native Number means an external-type repair does not prove a Float64 storage-write failure is resolved.
3. Apply the [Forecast gate](#forecast-pre-publication-gate) to forecast intent, including formula-driven designs, and verify both axes' aggregation for percentages/rates. A growth percentage must not be summed across periods; choose the appropriate business aggregation instead. Preserve declared formula semantics and context rather than replacing conditional expressions merely to suppress errors.
4. Compare effective defaults and supported owner/override geometry through the current readers. Missing optional UI sections are not an instruction to copy them; an explicitly partial nested object can replace defaults and requires its own contract check. Fractional rectangles alone do not prove a coordinate-scale bug, and matching outer bounds do not prove an initialized usable grid. Apply the [composition audit](design-standards.md#layout-generation-and-correction).
5. Add executable candidate checks where the selected builder supports them, with negative cases for empty/mixed forecast Columns, stale dimension state, incorrect external types, unresolved references, source/query field-role mismatches, summed rates and invalid placement. Prove that the relevant previous invalid configuration fails. Bind each required guard result and schema preflight to the exact submitted payload hash; a later payload edit invalidates both. Markdown instructions alone are not deterministic enforcement.
6. Track verified construction defects, suspected engine mechanisms and confirmed runtime causes as separate findings. The typed-array error requires evidence of the failing column, execution context and actual storage variant to establish causation; neither a reference diff nor a new successful import closes it. Do not label a candidate root-cause-fixed or professionally verified while native acceptance remains failed or not-run.
7. Respect an explicit CLI-only authentication constraint: reuse approved Azure CLI credentials and use `az login` when needed, without asking for a separate browser sign-in. A Kusto authorization denial is a telemetry-permission limit, not a reason to retry login, request browser credentials or infer that no failure occurred. Continue eligible CLI-supported work and disclose unavailable native/rendered checks; do not bypass access controls.

Evidence for the November 2026 follow-up: fresh definition comparison and current source inspection confirmed constructor-level date placement and rate-aggregation defects, while source measure declarations had already been corrected in the saved target. Scoped graph/reference checks passed, but the exact native initialization cause was not established. The CLI telemetry attempt was denied and no authenticated native render was performed. These limits must survive a later successful create/readback; they are not a generalized product defect or a promise that changing the hierarchy alone fixes initialization.

#### Dimension Lookup Descriptor Completeness

For every `dimension_id_mapping.mappings[displayColumn] = {ID: keyColumn}`, require both columns in `dimension_id_mapping.pivot`, including context-only dimensions. resolve_dimension_id_mapping_pairs finds both descriptors in that stored pivot and skips an incomplete pair. The mapping dictionary alone does not construct the lookup request. DimensionIdLookupTables::new can retain an absent lookup table; missing descriptors do not by themselves prove a panic or an initialization failure.

Derive missing descriptors from the destination's verified model metadata and existing dimension role/order. Preserve the full typed source descriptor, use the actual key-column data type, and keep lookup-only descriptors separate from displayed `pivotAssignments`. Do not copy another Plan's entire pivot, reorder its axes into the target, remove mappings to silence an error, or regenerate saved-input identities. An additive repair must preserve every existing descriptor and all unrelated properties; compare a fresh target export before submission and verify the saved additions afterward. Changes to key resolution may affect existing saved-input paths, so input save/reopen and downstream reconciliation remain required runtime checks.

When comparing a working reference, keep raw exhaustive differences separate from diagnostic alignment. Parse native integers losslessly, preserve case-distinct keys and positional arrays, distinguish missing/null/false/zero/empty, and recurse into object/array JSON strings. A missing reference UI section is not automatically required: FabricHost.getPropertyMap overlays saved state on defaults, although an explicitly present partial nested object can replace its default object. Resolve the actual reader before filling gaps. Missing telemetry permissions or an unauthenticated browser session is a verification blocker, not evidence that no runtime error exists.

#### Imported Measure Activation

Reconcile `dataInput.json.columns`, `properties.visualState.manage_measures`, native column responses and the displayed measure set by owner and identity, not counts alone. In the supplied before/after-save case, imported column records remained unchanged while the saved active-measure list retained only a native measure and a newly UI-created input. That is evidence of a configuration-versus-activation discrepancy, not proof of a GUID collision, formula error or particular backend defect. Do not repair it merely by adding more display entries or republishing identical columns.

Retain the before-import candidate, saved export, affected runtime properties/columns and sanitized failing responses. If authorized test resources permit a native create/save comparison, inspect the registration and hydration requests for an equivalent small measure through both routes; preserve existing inputs and obtain authority for any test write. Structural similarity to a working input does not establish equivalent activation. A native save that drops imported active measures requires investigation even when the column definitions still round-trip.

## Dimension ID Mapping

**Authoring default:** configure mappings for row dimensions only. Column dimensions and filter-context dimensions need no ID mapping by default; keep their assignments, selections and model sorting intact. An explicitly requested non-row mapping requires complete descriptors with the key on the display field's own axis, never a row-key fallback. This default is not permission to migrate populated coordinates during updates; assess existing mappings and preserve saved inputs through an approved strategy.

Use this feature when business descriptions should remain visible while planning input coordinates resolve through stable member keys. For example, an employee-name change should retain an input at the same employee, region, period, scenario and measure intersection. Excluding an organizational attribute from the key can permit regrouping without changing that coordinate, but only when the retained dimensions still uniquely identify the intended grain. These are acceptance goals, not guarantees established by a mapping entry.

### Evidence and Strategy Selection

The user-supplied technical guide describes a historical packaged implementation and scripts, not a newly verified live configuration. It establishes observed ID and Skip serialization and identifies stale ordering/context state in its own snapshot. The accompanying screenshot exposes **In key**, **ID Column**, **Label**, **Lookup**, **Id field** and **Parent key** controls; the shown rows select Label. It does not prove a saved ID mapping, explain every disabled control, or authorize changing that Plan. Resolve the current owning sheet/visual and its fresh saved state before interpreting a UI-versus-definition discrepancy.

| Business Need | Strategy / Boundary |
| --- | --- |
| Display descriptions but survive label changes | Choose ID Column backed by a stable, unambiguous key in the same semantic-model table. A numeric type alone is not evidence of a stable key. |
| Retain an established label-keyed populated sheet | Preserve its existing strategy unless a key change and any required migration are explicitly intended. Do not invent a `{Label: ...}` native union from the radio-button label. |
| Display an attribute without making it part of the coordinate | Use In key off / observed `{"Skip": {}}` only when permitted by the UI and the remaining dimensions preserve the business grain. Respect required/non-skippable dimensions. |
| Resolve a member through a parent lookup | Treat Lookup as a separate strategy. The ID/Skip sample does not close its UI eligibility, parent-order rules or save payload; obtain the current writer and compatible saved evidence before authoring it. |

### Must

1. Establish the business grain and whether inputs already exist. Load a lossless current definition and relevant native state where needed; record model binding, ownership, part hashes, measure identities, filters and context. Definition export is not a backup of persisted cell values.
2. Verify both description and key in the current semantic-model schema, with matching table membership, actual types and availability. Check null keys, key uniqueness and whether each displayed group resolves to exactly one key. Duplicate display labels can still combine members even when underlying IDs are unique. SQL column existence alone does not establish semantic-model availability. Schema/model refreshes and master-data changes require their own authorization; do not provision columns automatically.
3. Keep semantic-model master descriptions on the intended axes; keep From Sheets/InfoBridge measures in Values for this workflow. Preserve visible hierarchy order and Values identities. An attribute from the member's table is not interchangeable with a similarly named attribute from a separate dimension table.
4. Configure `properties.visualState.dimension_id_mapping` using the selected native writer. For every ID mapping, include complete descriptors for both display and key fields in its `pivot`, including context-only dimensions; follow [descriptor completeness](#dimension-lookup-descriptor-completeness). Key descriptors are lookup inputs, not extra visible ID levels. Preserve technical 64-bit field identities losslessly and distinguish them from business member keys, semantic field references, visual IDs and input/formula IDs.
5. Reconcile only affected dependent state: `rowDimensions`, `columnDimensions`, current assignment buckets, visual/embedded/page filters, filter-context properties and any persisted pivot, bookmark or consumer references. Respect each state's own shape; do not copy one array into every layer or add absent structures gratuitously. Preserve valid selections and scenario binding. A ScenarioID mapping does not create single-select filter context, and an empty context array does not prove it works.
6. Preserve the existing Plan and unrelated configuration for an ordinary authorized update. Save a separate candidate, verify its exact diff, complete the selected save/import operation, then read the current saved mapping and reopen the UI where possible. Do not follow a historical script's blanket context reset, arbitrary descriptor-template fallback, global ID replacement or automatic new-timestamped-Plan deployment.
7. Treat label-to-ID, ID-column, Skip and parent-lookup changes as coordinate-compatibility changes. Even completing previously missing descriptors can activate an ineffective mapping and change key resolution. Do not assume it migrates stored values; retain the old strategy or obtain an approved migration and rollback approach before changing populated coordinates. Preservation of measure IDs or definition bytes alone does not prove saved-cell retention.

### Prefer

- Stable business or surrogate keys whose uniqueness and lifecycle are verified, not whichever numeric column is easiest to select. Preserve an established code-based key instead of replacing it with a different ID merely to match an example.
- Display-only attributes excluded from the key only when the business explicitly wants regrouping to preserve inputs. Other changes, such as a move to a different retained region key, remain different coordinates.
- The native UI flow when available: Editing mode -> Data pane -> Semantic Model gear -> Dimension ID Mapping -> strategy/key selection -> Apply -> save -> reopen. A disabled control requires context/eligibility investigation, not a guessed payload bypass.

### Avoid

- Treating ID mapping as PowerTable foreign-key lookups, SQL auto-increment, time interpretation/sorting or security configuration. These are separate features and authorization boundaries.
- Copying historical row order or scenario-as-row state, assuming every descriptive attribute should be skipped, or claiming the screenshot proves the current artifact uses IDs.
- Renaming production master data or writing test inputs merely to demonstrate persistence without approved test resources. Do not claim rename safety from JSON checks alone.

### Example

Synthetic requirement: show personnel descriptions, retain inputs across personnel renames, and allow team regrouping while retaining the same person, region, period and scenario keys. The following illustrates the **mapping dictionary only**, assuming the fields and intended Skip behavior have been verified in the destination model:

```json
{
	"DimPerson[PersonName]": { "ID": "DimPerson[PersonID]" },
	"DimPerson[TeamName]": { "Skip": {} }
}
```

This is not a complete publishable properties part. Add the paired full native descriptors through the current writer, preserve any other required region/scenario mappings and their existing strategies, and keep lookup keys out of the visible axes. Do not emit Label or Lookup representations based on this ID/Skip example. Period ID mapping does not itself configure chronological sorting.

### Validation

Static checks must verify same-table field resolution/types, complete descriptor pairs, intended Skip behavior, current axis/context consistency, unchanged model/measure identities and lossless technical IDs. Inspect a fresh readback; public-schema or operation success does not prove coordinate behavior.

On explicitly authorized test resources, record the exact original intersection and distinctive value, then test save/reopen, a description-only rename with stable ID, regrouping of a skipped attribute, separate scenarios and periods, connected-query consumption without duplication, and the intended restricted-user context. Verify that changing a retained key is treated as a different intersection. Restore authorized test master-data changes afterward. Keep results separated as static, saved-definition and native persistence/refresh/security evidence; unperformed tests remain unverified.

## Intelligence Dashboard Patterns

Choose the overview, KPIs, charts, slicers and navigation from the current user's decisions and model semantics. No named report, page layout, chart type or business flow is a template.

- Resolve current visual type/state-schema registries and the selected compiler's field map; registry codes, native state and public ALM are distinct contracts.
- Keep canvas position/dimensions separate from chart axes, KPI internals and Planning row layout. Use the actual geometry type/writer and verify rendered fit.
- Resolve source fields, roles, grouping, sorting, units, null/zero formatting and interaction scope. A chart title or filename does not establish its active renderer or data meaning.
- Read the current Text/Shape/Navigator/Box compiler guides for their supported friendly schemas. Native field-map changes are not full exported visual constructors.
- Embedding requires verified owner/source identities, companion records, permissions and import restoration. Do not fabricate missing parts or copy a source from another application.
- Check view-specific rendering, navigation and filters separately from definition syntax. Keep requested business calculations and connected acceptance independent from visual appearance.

### Intelligence Dashboard Business Authoring

Before every visual addition or embed, run [CLI Visual Placement](#cli-visual-placement). This is a skill-level authoring sequence through existing APIs, not a backend/importer fix, a React callback or manual UI repair. Earlier importer-deployment guidance is superseded for this workflow. Preserve existing source sheets, saved inputs, filters, visual dimensions and page configuration.

#### CLI Visual Placement

**Source evidence:** observed in the product implementation. fetchVisuals delegates to getVisualsAndPageProperties. Read these contracts, not mounted store objects; the agent does not need to view the UI.

**Must:** fetch all visuals fresh, resolve the saved geometry and bounds, preserve the requested dimensions, include all visual families and reservations, calculate free space, create/embed and save that geometry, then refetch and check. **Prefer:** aligned edge candidates and the existing page's spacing in its native units. **Avoid:** cached inventories, filtering to charts only, missing-geometry guesses, arbitrary scaling, moving/shrinking old visuals, unchecked overflow, and the UI's overlapping no-fit fallback.

**1. Resolve transport and fetch the inventory.** Use the organization's
approved external service profile to resolve the current page inventory. The
profile supplies the trusted base URL, process-scoped credential name, required
headers and symbolic route templates outside this repository. Require a complete
page and visual inventory, and fetch it again before and after every mutation.
Never disclose route templates, derive hosts, request credentials in chat, or
forward credentials to redirects. If an approved profile is unavailable, stop
that service-specific phase and continue independent supported work.

**2. Extract complete occupied rectangles.** The user term `visualProperty.position` refers to parsed visual geometry, not a wire field named `visualProperty`. parseVisualResponse reads:

```text
page = response.payload.properties.properties
direct properties = visual.properties.properties ?? visual.properties
direct rectangle = direct properties.position {x,y}
									 + direct properties.dimension {width,height}
embedded rectangle = page.reactiveVisualProperties entry matching visual.id
										 .properties.position + .properties.dimension
units = page.canvasStyle.dimension.elementScalingUnit
```

For `visual.isEmbedded`, the loader uses page-local geometry instead of source-owner geometry. Include Planning/PowerTable embeds, slicers, filters, images, text, navigation and other visuals, including hidden/group members conservatively. Preserve every record's identity and unrelated fields. Missing or duplicate geometry is not free space: refetch/reconcile unsaved entries or report the unresolved rectangle. Do not manufacture the UI's default rectangle to certify placement. Non-visual filter/control panes must also be accounted for: use confirmed canvas exclusion or supply their measured rectangles as helper-only `reservedAreas`; their layout is not derivable from a position enum alone.

**3. Resolve bounds and units without a viewport.** ICanvasDimension defines `type`, `width`, `height`, `elementScalingUnit: 'pixel' | 'percentage'`. In pixel mode use the actual canvas interior dimensions in pixels and requested pixel size unchanged. In percentage mode position and dimension are fractions, with bounds `{width: 1, height: 1}`; `0.3` means 30%, not 0.3%. Use requested native fractions unchanged. If dimensions were requested in pixels on a fractional canvas, perform only the verified per-axis pixel-to-fraction conversion using actual canvas width/height, preserving rendered size; never multiply by 100 or use arbitrary coordinate scaling.

getDimensionByType uses saved `canvasStyle.dimension.width/height` for fixed/custom modes, but DOM wrapper/body dimensions for RESPONSIVE/NATIVE. Fractional bounds need no viewport, but pixel sizing, pane exclusions and rendered-size checks on dynamic canvases require an approved explicit layout-size input. Missing dynamic bounds cannot be replaced with a guessed screen size. Account for canvas borders through the same interior calculation; keep bounds in visual-local coordinates, not browser offsets. Do not change canvas units or auto-switch modes silently.

**4. Calculate free space.** getOptimizedElementPosition uses row-major scanning, axis-aligned rectangle intersection and spacing `5` pixels or `0.005` fractions. It calls `getOptimizedElementDimension` for defaults (which can depend on store/type) rather than preserving an explicit requested size. It also adds spacing after the collision check and falls back to top-left when full. Do not blindly invoke that method headlessly or copy those two unsafe behaviors.

Use the dependency-free visual-placement.cjs helper instead. Its pure `inventory(response)`, `findPlacement({bounds, dimension, occupied, gap, margin})` and `verifyPlacement(...)` functions need only JSON. It keeps the same coordinate schema and intersection rule, but uses deduplicated canvas/occupied-edge candidates instead of a dense pixel scan: consider edges after each rectangle plus spacing and before it minus the new size/spacing; sort Y then X; select the first full rectangle within bounds that clears every obstacle by the gap. This favors compact top-to-bottom, left-to-right alignment without resizing. Requested `dimension` is returned unchanged. The collision check includes the final margin/spacing; no unchecked offset follows it. Return `no-fit`, not the source fallback.

Helper input is a local envelope, **not an API request**:

```json
{
	"response": {"statusCode": 200, "payload": {"properties": {"properties": {"canvasStyle": {"dimension": {"type": "CUSTOM", "width": 200, "height": 100, "elementScalingUnit": "pixel"}}}}, "visuals": [{"id": "filter", "properties": {"properties": {"position": {"x": 5, "y": 5}, "dimension": {"width": 40, "height": 40}}}}]}},
	"bounds": {"width": 200, "height": 100},
	"dimension": {"width": 40, "height": 40},
	"gap": 5,
	"margin": 5,
	"reservedAreas": []
}
```

```powershell
Get-Content -Raw placement-input.json | node tools/visual-placement.cjs
# {"status":"placed","placement":{"position":{"x":50,"y":5},"dimension":{"width":40,"height":40}}}
node tools/visual-placement.cjs --self-test
```

Paths above are relative to `fabric-agentic-creation-skills`. `reservedAreas` contains local `{x,y,width,height}` rectangles in the same units, not new native fields. Use the existing page's documented spacing where present; defaults are the inspected layout search spacing, not a global design mandate. For multiple additions, append each chosen rectangle to `occupied` immediately, then reconcile it with the fresh saved response before placing the next. No helper mutates the fetched records.

**5. Handle no fit explicitly.** The inspected search has no safe automatic overflow mode; canvas base styles use `overflow: hidden`. Never put a visual outside those bounds and call it scrolling. The custom-dimension handler supports changing canvas width/height, with UI ranges of 100-8000 pixels. Within authorized layout scope, a CUSTOM pixel canvas can grow just enough for a new row: proposed height = maximum occupied bottom + gap + requested height + margin, keeping width and all old rectangles unchanged. Save the preserved `canvasStyle` with only the height change through the page batch writer, refetch actual bounds, and retry the helper; do not create before confirming space. These UI ranges are not a claim about every server version. No automatic expansion is authorized by this helper. Fractional expansion changes existing rendered sizes; do not silently rescale/rewrite existing visuals to enable it. If safe supported expansion is unavailable, stop the addition with `no-fit` and report the needed layout choice.

**6. Create/embed and persist the calculated geometry.** Use the approved
external profile's visual-create or sheet-embed operation with resolved
identities. Do not create another Planning owner. Resolve the returned visual
through a fresh inventory; if the result is ambiguous, stop without another
create.

Refetch current properties and ETags after creation, reconcile any concurrent
obstacles, and calculate again when necessary. Retain a known new identity but
do not treat it as verified geometry until the intended position has persisted.
For a direct visual, clone its current property object, preserve initialized
settings, then submit only position/dimension changes through the external
profile's `properties-batch` operation. For an embed, keep source settings
untouched and update only the page-local placement entry in the current page
object. The embedded entry includes:

```javascript
const embeddedEntry = {
	visualId: createdVisual.id,
	properties: {
		position: placement.position,
		dimension: placement.dimension,
		visualStyles: resolvedVisualStyles,
		visualInteractions: resolvedVisualInteractions,
		lockAspectRatio: resolvedLockAspectRatio,
		originEntityId: createdVisual.originEntityId
	}
};
```

Resolve the existing/default style and interaction values from the source's supported feature contract, not fabricated empty settings; preserve existing instance siblings. Include the fresh page ETag. preparePropertiesForSave supplies the `schema/properties` envelope; updateBulkVisualProperties strips client-only `visualEntityIds`, which must not appear in the HTTP body. Do not copy the GET response wrapper into POST. A 409 is a conflict, even if a client promise resolves: refetch, recompute against the latest inventory and merge the scoped property change; never use `force` to bypass it. Do not assume the two requests are atomic. If creation succeeded but save failed, retain the created identity and resume that save rather than duplicating creation.

Use the bundled transport only with an external profile supplied and approved by
the destination owner. Validate the HTTPS origin, never log credentials, and do
not persist route/authentication details in fixtures. Resolve operation-specific
response contracts; asynchronous acceptance is not completed persistence.

**7. Verify from a new GET.** Match the actual created ID, extract the authoritative direct or embedded geometry again, and compare all four values with intended placement (only a small floating-point tolerance, not relaxed layout tolerances). Check bounds and clearance against **every** current visual plus reserved areas; compare old rectangles and page/filter/source configuration with the baseline to detect unintended changes. The helper's `mode:'verify'` input accepts `{response, id, intended:{position,dimension}, bounds, gap, reservedAreas}` and reports only `passed-persisted-geometry`; include the same reserved areas used for placement. Report any pre-existing overlaps without relocating them. API success or local candidate output alone is not verification. Record requests without credentials and separate persisted geometry from native rendering, grid readability and functional/query acceptance, which are not certified by this offline skill update.

**Context while embedding:** adding a matching dashboard slicer must not clear a source Planning filter marked `isContextDimension`. The Planning Context card retains its explicit default independently of an ordinary display filter. Validate this after dashboard composition, not only in the standalone Planning constructor; a later embedding pass can otherwise erase a previously valid selection before submission.

**Explicit best-effort deployment:** the placement gate below governs verified layout acceptance; it need not prohibit an otherwise supported initial save when the user explicitly accepts deployment without runtime verification. Record the authorization, retain one hidden direct owner and its valid portable embedded reference, choose practical authored geometry, and disclose that unresolved runtime placement can fall back to the origin/default size. Do not estimate numeric identities, mark authored rectangles as effective runtime geometry, or claim professional layout acceptance. Inspect the created item's own readback for an available mapping and use only a supported target-local writer for subsequent activation; missing runtime IDs remain a follow-up limitation, not permission to copy another item's IDs. Keep substantive construction defects distinct from deferred runtime checks and report both honestly.

**Embedded geometry:** the page loader takes an embedded visual's position/dimension from page-local `reactiveVisualProperties`. Use the created/fetched visual identity and supported page save structure in [CLI Visual Placement](#cli-visual-placement). Preserve source-owner geometry and other dashboard instances. Do not use a default rectangle or local store state as proof of saved placement; no importer investigation or UI manipulation is required by this authoring contract.

The coordinate converter uses fractions for percentage mode: `0.95` means 95%, not 0.95%. Do not multiply by 100 to compensate for an unmatched placement. Test missing/mismatched IDs and effective fallback rectangles, not just authored bounds; retain separate owner versus embedded placement checks. Preserve a user's saved alignment as the new baseline, keep data/formulas/input identities unchanged, and verify the actual rendered result separately.

Do not replace a required hidden Planning source sheet and Intelligence embed with direct Reporting ownership merely to avoid a placement-mapping defect. The sheet importer accepts Planning and Reporting sheets and the visual importer requests DIRECT versus EMBED, but acceptance does not prove equivalent authoring, source-sheet discovery or connected workflows. A follow-up build passed schema/readback checks after this substitution, yet the user could no longer find the hidden Planning sheet and reported chart request failures. Preserve the required source-plus-embed composition and add a structural regression check. Keep those query failures separate: a populated source cache does not establish query materialization or a successful consumer request.

For an existing item, inspect the mapping writer before attempting an ownership repair. The inspected upsertArtifactVisual reuses the visual by recordGuid but writes mapping `type` only when creating a missing sheet/visual mapping; it does not switch an existing DIRECT mapping to EMBED. Adding a new hidden owner through this path could leave duplicate direct owners. Do not silently duplicate the visual, delete/recreate its sheet, risk saved inputs or claim that `updateDefinition` can perform this migration. Use a verified native ownership-migration route or obtain authorization for a separately constructed replacement, with the original retained and effective embedded placement resolved. Import support for a direct visual is not evidence that removing a required hidden source is safe.

Compose a dashboard around review and planning decisions, not a copied page or a collection of unrelated charts. The supplied Bookmarks/Intelligence guide separates source Planning sheets from the Intelligence canvas and uses bookmarks to expose summary, driver and review tasks over the same underlying plan. A dashboard can bring those tasks together without creating their calculations, source-write paths, scenarios or approval processes.

**Authoring workflow:**

1. Identify the audience, decision grain, periods/scenario, required source sheets, permitted edits and authoritative calculations. Resolve source/model compatibility and each user's access before presenting a combined view.
2. Create or open an Intelligence sheet. The [reporting setup documentation](https://community.fabricplan.com/docs/intelligence-sheets/how-tos/get-started-with-reporting/) requires Planning and PowerTable sheets used here to exist in the same Plan. Select Planning or PowerTable in the Visualizations pane and choose the intended existing sheet; do not copy another Plan as a shortcut.
3. Before adding each embed, KPI/chart or explanatory visual, execute [CLI Visual Placement](#cli-visual-placement) with a fresh full page inventory and the requested dimensions. Include newly placed visuals before the next addition; persist and refetch every intended rectangle. Keep scrolling, columns, navigation and active context legible; verify source and embedded experiences separately. Sample canvas dimensions or screenshots are not a layout template.
4. Prepare task-specific [bookmarks](#bookmark-business-authoring) and add a Bookmark Navigator for views and a Page Navigator for sheet destinations. Choose intentional order, included/excluded destinations and default behavior; test bookmarks captured on source sheets from the dashboard.
5. Add only needed context controls and create an explicit interaction map. Verify compatible fields, relationships, hierarchy levels and source semantics; a shared field name does not establish a working cross-visual filter.
6. Configure available Edit Interactions behavior for each intended target, including deliberately disabled interactions. Confirm what bookmarks restore versus preserve, especially current-page and data capture. Do not treat empty interaction maps as proof that no default interaction can occur.
7. Save/reopen and test as intended planner/reviewer personas. Exercise page changes, bookmarks, pending edits, source refresh, restricted fields, filtered totals and unaffected sibling visuals. Resolve update/removal references and changed source fields through the actual owner contracts rather than deleting/rebuilding a source.

| Control or action | Intended effect | Negative control / separate responsibility |
| --- | --- | --- |
| Entity slicer | Filter compatible revenue and workforce embeds | Global notes remain unchanged; authorization still applies independently. |
| Period selector | Resolve the intended period for period-based visuals | Annual classifications remain unaffected unless deliberately targeted. |
| Bookmark Navigator | Restore the saved visuals and included context | Uncaptured embeds retain their intended state; current-page capture may navigate away. |
| Page Navigator | Open the selected sheet | Does not itself write forecast values, change approval or synchronize sources. |
| PowerTable selection or save | Apply configured selection interactions or persist authorized reference changes | Source save, propagation/model refresh and downstream calculation are separate from bookmark navigation. |

The [Intelligence FAQ](https://community.fabricplan.com/docs/intelligence-sheets/intelligence-faq/) documents bookmarks, embedding and Edit Interactions choices including filter, highlight and disabled interactions. Determine which choices are supported for each selected family. It characterizes Intelligence as reporting, while the reporting setup page also describes Matrix/Table writeback ribbons: neither general statement establishes every embedded family's editing contract. Distinguish view navigation, authorized Planning input, and PowerTable/source save; use each owner's supported route, permissions and runtime checks instead of claiming the entire canvas is universally writable or read-only.

**Definition versus behavior:** the inspected package contains one Planning embed, two navigators, and no slicer or PowerTable embed. Workload/page filter assignments and explicit interaction maps are empty. Multi-embed, PowerTable and active-slicer designs are functional extensions supported by the guide/documentation, not saved settings in this sample. Verify active interactions, refresh latency and cross-sheet calculations independently. Co-location on a canvas does not connect measures or consolidate plans.

#### Bookmark Dashboard Business Examples

These fifteen guide-derived designs are illustrative acceptance cases. Create only the sheets, measures, context controls and connections required by the current request. A named exception/review view needs its actual filter/classification; hiding measures is never access control. Amounts and view names below are examples, not defaults or observed native results.

| Case and canvas/context | Task views and visible content | Worked decision and acceptance |
| --- | --- | --- |
| 1. FP&A: forecast plus governed assumptions; Entity/Year/Scenario | Executive summary shows Actual/Forecast/Variance; planner detail shows quantities/prices/overrides/comments; exceptions show unexplained changes. | 12,000,000 forecast less 11,400,000 baseline is 600,000. Summary/detail reconcile under the same slice; test whether Entity is restored or preserved. |
| 2. Retail: merchandise plus product attributes; Region/Season | Category review; SKU units/price/markdown; markdown impact/reason. | Trace an illustrative 250,000 shortfall to three SKUs rather than assuming a category-wide price issue. Reconcile category/detail and separately verify attribute saves; no bookmark creates a SKU. |
| 3. Manufacturing: demand and capacity plus optional assumptions; Plant/Period | Demand volume/backlog; capacity hours/overtime/utilization; material demand/shortages. | 10,000 units at two hours need 20,000 hours against 18,000 available, a 2,000 gap. Test capture/filter scope for each embed; a bookmark on one does not automatically configure the other. |
| 4. Workforce: workforce and hiring requests plus governed rates; Department/Year | Headcount movements; salary/benefits/cost; hiring dates/status/justification. | Ten hires at 120,000 give 1,200,000 annualized cost, not necessarily in-year spend. Verify start-date effects, headcount basis and actual compensation permissions. |
| 5. Capex: capital plan plus project metadata; Business Unit/Investment Year | Portfolio requested/approved amounts; project cash timing; pending owner/status/explanation. | Inspect a 4,000,000 equipment program within a 30,000,000 portfolio. Configure a real pending-status filter; selecting the view must not approve or reopen a project. |
| 6. Sales: forecast plus discount policy; Region/Channel/Quarter | Territory revenue/variance; customer volume/price/discount; exception threshold/review state. | 500,000 gross at 14% discount yields 430,000 net. Exceptions require a rule; check customer scope and hidden measures when restoring territory context. |
| 7. Procurement: procurement plus supplier terms; Category/Buyer | Savings baseline/planned spend; supplier quantities/prices/lead times; price exceptions/comments. | A 0.40 price increase on 100,000 units adds 40,000. Do not sum supplier rates; verify actual source-save propagation separately from navigation. |
| 8. Logistics: freight and service capacity plus optional carrier assumptions; Region/Week | Regional costs; route trips/distance/load/rate; service gaps/comments. | Forty trips at 750 add 30,000. Keep period/carrier scope consistent; expose intentionally restored filters and check that another embed's week is unaffected. |
| 9. SaaS: revenue and customer success; Segment/Region/Month | Opening/additions/churn/closing revenue; retention drivers/comments; at-risk classifications. | A 0.5 percentage-point churn increase on 4,000,000 implies 20,000 loss. Preserve meaningful rate aggregation; a risk view is neither a new rule nor a separate stored scenario. |
| 10. Healthcare: operating expense and aggregate staffing; Hospital/Service Line/Month | Budget/forecast/variance; staffed hours/rates/capacity; commentary/review state. | 200 hours at 60 add 12,000. Both intended embeds must resolve the same scope; switching views cannot grant a reviewer input rights. Retain clear hours/currency/percent units. |
| 11. Professional services: project finance and resources plus optional rates; Practice/Period | Revenue/cost/margin; role hours/utilization/rates; project risk/comments. | 160 hours at 100 add 16,000 cost with unchanged revenue. Verify the actual financial dependency and project-versus-role grain; a navigator does not establish weighted rates or cross-sheet reconciliation. |
| 12. Construction: projects and cash flow plus project attributes; Program/Project/Scenario | Program cost/revenue; monthly receipts/payments; change reasons/review fields. | A 250,000 cost/300,000 revenue change can improve total margin yet worsen cash timing. Keep scenario/period explicit; a view does not create a request/member or bypass input controls. |
| 13. Education: enrollment, tuition and faculty capacity; Campus/Program/Academic Term | Intake/retention/students; fee/net tuition; teaching load/staffing gaps. | Forty students at 5,000 give 200,000 for the illustrative term. Verify all consumers actually use enrollment and the same term; do not substitute a monthly horizon or assume filter preservation. |
| 14. Nonprofit: grant budget and delivery plus grant attributes; Grant/Funding Period/Program | Portfolio funding/spend/balance; permitted-category indicators; milestones/drivers/comments. | A 20,000 category transfer leaves the grant total unchanged. Restrictions and approvals need their own rules; public bookmarks must not broaden authorized data access. |
| 15. Enterprise hub: revenue, operating expense, workforce and policy/reference table; business-unit planning context | Unit financial summary; driver workshop; variance/ownership/review meeting, with pages for dedicated work areas. | 600,000 revenue uplift less 200,000 operating expense and 150,000 workforce adds 250,000 before other effects. Verify consistent definitions, dependencies and each embed's capture scope; the dashboard is not an automatic consolidation/approval engine. |

## Shared ALM Contract

The linked current exporters/importers establish bounded envelope and transformation facts. No historical export, report inventory or deployment handoff is a prerequisite. Read both writer and reader for the selected route; a native declaration does not establish complete ALM preservation.

### Route Selection

Resolve the documented target API from trusted current metadata before treating
`WorkspaceNotFound` as an authentication or permission failure. Never guess or
rewrite hosts, forward credentials to redirects, change permissions or request a
browser login. A metadata-route success does not establish runtime acceptance.

For a different semantic model, re-resolve tables, measures, expressions, periods, eligibility, OneLake source artifact and accessible connections before reusing a serializer. Historical helper names are not dependencies the new model must acquire: use explicit bindings to inspected existing measures only when their actuals/forecast, account, currency and grain semantics satisfy the request, preserving required source filters. Generic OAuth `FabricSql` connections and path-bound `SQL` connections are different branches; resolve their credential reader and explicit database-artifact target rather than copying an old database/connection or selecting the first name match. Read-only SQL schema access and a generated binding do not prove native maintenance write access; do not mutate master data to manufacture that evidence.

### PowerTable Eligibility and Physical Source Binding

**Scope: automatic model-first app creation only.** The following three gates apply when the user supplies only a semantic model and functional business prompt to create a planning app, and the agent chooses PowerTable maintenance tables automatically. They are an authoring-selection policy, not general PowerTable capability restrictions. PowerTable can target an explicitly requested source table outside the Plan's connected semantic model. For explicit source-table creation/connection requests, use the supported source-authoring route and validate source identity, supported object type, schema/keys, access and saved behavior; do not impose model membership, dimension classification or Direct Lake mode from this automatic policy. The model-dimension discovery helper belongs only to the automatic path. Do not infer arbitrary view writability or silently switch to an external source when automatic selection fails.

Within that automatic path, selection requires the intersection of the requested maintenance use case and **all three verified gates**, not the union of model tables and accessible SQL tables:

1. **Dimension in the connected model.** Use names such as `DimEmployee` to nominate candidates, then confirm the business entity grain, stable key, descriptive attributes and one-side relationship role. A name alone is insufficient. Exclude facts, transaction/control helpers, validity bridges and assignment tables that are not dimensions. Do not automatically choose a SQL object absent from the connected model from a general business requirement; an explicit source-table request instead follows the separate path above.
2. **Direct Lake table.** Inspect actual model table/partition metadata and the partition's source lineage. Reject Import, DirectQuery, calculated tables and unresolved/mixed partitions. A model-wide Direct Lake label or another table's partition does not prove this candidate's mode. Follow the candidate's real physical `entityName`, `schemaName` and referenced source expression; display names may differ from SQL names.
3. **Physical Fabric SQL base table.** Resolve the source workspace/artifact from the candidate's lineage, verify that artifact is a Fabric SQL database, and confirm its exact schema/table through `sys.tables`/`sys.objects` with base-table type `U`, plus keys and column metadata. The inspected read-only SQL schema helper joins `sys.tables` to `sys.columns`; its records prove only the inspected database/schema/table. Exclude views, indexed/materialized views, lakehouse/warehouse sources, missing objects and uncertain object types. Merely finding columns in `INFORMATION_SCHEMA.COLUMNS` is not base-table proof.

Build each eligible source from its own verified workspace, database artifact, supported connection, physical schema/table and current host/database; retain an eligibility decision and exclusion reason. Never select the first similarly named database/connection or silently fall back to the workspace's system database. Multiple source expressions/artifacts require per-table resolution; a serializer supporting only one expression must reject unsupported lineage rather than reuse that expression for every table. Automatic selection does not mean creating every eligible dimension: include only business-requested maintenance surfaces.

**Native SQL host format:** getMDEDestinationHelper maps source `dbHost` to settings `host`, and FabricSQL.setConnections passes it directly as the driver's `server`. A Fabric metadata connection-string value ending in `,1433` is not the native hostname: remove that verified default-port suffix when constructing `dbHost`; do not guess nondefault port support or strip arbitrary connection strings. Preserve the exact database name and artifact identity. Settings returned by the destination reader use `host`/`database`, not `dbHost`/`dbName`.

**Named-reference evidence:** an authorized saved-definition comparison observed a PowerTable with hostname-only `dbHost`, explicit `SQLDbNative` artifact/schema/table binding, and a source workspace different from the Plan's workspace. Live metadata classified both the reference and failing target connections as generic OAuth2 `FabricSql`/`ShareableCloud`; this is not evidence that the generic connection branch caused the failure. Resolve source identity independently of Plan placement, while retaining the three model-lineage eligibility gates for automatic maintenance creation. The reference's saved model flags did not declare Direct Lake, and its PowerTable table differed from its Planning writeback destination: neither a writeback-oriented name nor those exported flags establish current partition mode, physical-table eligibility or a source-to-writeback relationship. Its exported identity key was noneditable; do not transfer that key, table, connection, extra settings or business layout to another model. Definition export succeeded, but the native config reader returned HTTP 500, so source serialization is verified while runtime read/write behavior and recovery remain unverified.

**Existing-Plan recovery:** preserve current sheets, source/visual IDs, column settings and saved inputs. The new auto-creation restriction does not authorize deleting existing ineligible sheets. Retain fresh saved-source metadata before a supported, narrow source rebind; inspect its actual writer, preservation and concurrency semantics rather than inventing an ALM patch. Re-read the saved binding and execute the authorized native config/read route after saving. The inspected config reader loads the destination before resolving database access. Its DNS error is classified by dbConnectionErrorClassifier; a generic endpoint failure does not identify whether the workspace metadata connection or the PowerTable's own source failed. If source readback/export is unavailable, report the precise repair blocker and authored defect separately; never claim runtime recovery from corrected local construction. Do not replay credentials from a curl capture, change permissions/networking, recreate the Plan or mutate master data to test eligibility.

The inspected [public root schema](https://developer.microsoft.com/json-schemas/fabric/item/plan/definition/Definition/1.0.0/schema.json) requires a connection for its legacy semantic-model-reference alternative and lists only `POWERTABLE`, `PLANNING` and `INFO_BRIDGE` in visual declarations. These constraints differ from two scoped observations: ALMImportHandler accepts model identity plus source type without a connection, and importSemanticModel documents caller MWC-token access with connection binding skipped. Supplied exports also declare `BI_TEXT`, `SUPER_FILTER` and `ANALYTICS_PLUS` for Intelligence visuals. Missing connection does not mean automatic connection provisioning; an observed visual name does not certify target-import support. Preserve exact discrepancies in validation evidence, resolve the selected route, and verify saved bindings. Do not fabricate a connection ID, relabel every visual `PLANNING`, or disable an entire schema check to hide the conflict.

Resolve the artifact's current storage mode from current supported metadata
before selecting a SQL or OneLake representation. Never select a route merely
because a filename or version marker contains `V2`.

**Independent new-run evidence:** a separately authorized, independently built Daily run using the corrected hostname-only bindings returned HTTP/envelope 200 for all four eligible dimension PowerTable config readers. Fresh responses matched the intended SQL artifact/workspace, connection, database, hostname and physical schema/table, declared read access and supplied nonempty column metadata. Those first read-only checks ran while dashboard pages were still importing; native config success alone did not certify whole-Plan creation. Creation subsequently succeeded with 17 sheets, native completion verified five persisted embed placements, and the single final export succeeded with 182 parts. Scoped saved-definition checks passed model/default/identity/header/date/ownership requirements, and all four saved SQL source bindings matched the verified targets and successful native responses. These checks do not certify rendered grids, maintenance writes, financial/input propagation or an older Plan's recovery. No source or input data was written. Keep operation completion, native placement and final export/readback as separate gates.

**PowerTable render-state completeness:** successful source configuration, row/column counts and a ready session do not establish that the grid rendered. A user screenshot showed a blank grey grid despite those successes. The global style model defines font, row and header metrics, while the initial property handler uses batch dispatch and the batch subscription replaces supplied store slices. A font-only `visualState.globalStyles` can therefore lose required defaults when hydrated through that path; the ordinary style-update reducer's merge is not a guarantee about initial loading. Emit a complete source-verified style slice when overriding its font, preserving explicit current settings during repair. An actual-source offline probe reproduced missing font size/row height with the exported sparse state; the normalizer matches every product default and rejects invalid metrics. A narrow same-Plan Employee visual repair saved missing defaults through the supported batch writer with a fresh property-wrapper ETag, and exact native readback preserved unrelated settings. The user subsequently confirmed Employee Master works and supplied a populated-grid screenshot. That confirms this canary's rendered recovery, not rendering of other sheets or a new artifact. Gate construction and saved readback on complete style slices; reject font-only state, missing row height and invalid font metrics. Do not disable CSP, silence selector warnings, change SQL bindings, overwrite inputs or create another Plan without explicit authorization.

### Native Properties Load and Batch Save

Entity-property reads and property-batch saves are separate symbolic operations
under an external service profile. They are not public Fabric item-definition
endpoints, and this repository does not ship their route templates.

IPageSavePayload declares client `visualEntityIds: string[]`, required `visuals`, `workloadEntities` and `workload` maps (`Record<string, any>`), optional `etags` and optional boolean `force`. ETags contain optional `workload: string`, `workloadEntities: Record<string,string>` and `visuals: Record<string,string>`. Open map types do not define every accepted property, map-key namespace or patch/delete behavior; use the page-save constructor and feature owners before constructing a request.

updateBulkVisualProperties strips client-only `visualEntityIds` from the HTTP body. That list, the initiating entity and `workloadEntities` keys drive cache invalidation because a save can include other sheets, such as synchronized slicers. It invalidates affected property caches before and after the request and returns caught status 409 responses for caller handling. A resolved promise is therefore not necessarily a successful save. Preserve loaded ETags, inspect status/payload, reconcile conflicts and do not set `force` merely to bypass them. This client evidence does not establish server transactionality, force semantics, or a REST updateDefinition concurrency guarantee.

getVisualsAndPageProperties may return through the property-result cache or React Query (five-minute stale time in the inspected branch). Its `byPassQueryCache` option forces the applicable fresh-read path. For verification, use a supported fresh read and compare the affected owner properties, not merely the already-updated local store. Definition export, ordinary native load, rendered result and saved-input retention remain independent checks. Do not copy a captured authorization header, routing identity or another Plan's properties into the library.

#### Inspect a Captured Page Properties Response

A supplied page-properties JSON was parsed independently of the earlier prompt excerpts. It contains one visual and separate page/visual schema wrappers. For this observed response shape, use these inspection aliases, not a save payload or a universal index-selection rule:

```text
E = response.payload.properties.properties
V = response.payload.visuals[resolvedIndex].properties.properties
S = V.visualState
page appearance = E.canvasStyle
visual container appearance = V.visualStyles
grid appearance = S.globalStyles / S.gridStyles / S.themeColors
```

Resolve the intended visual by its actual identity and owner before editing; index zero merely identifies the only visual in this capture. Preserve the schema/ETag wrappers at their owning transport layer. Do not copy the whole response into Batch Save or a Fabric definition: statusCode, message, limit, response identities and captured ETags are not a portable property constructor. A recorded statusCode 200 is historical retrieval evidence, not a newly executed save/readback test.

| Observed setting | Interpretation and authoring boundary |
| --- | --- |
| `S.layout` and `S.totals_config` | Outline with measure_layout null; row grand total/subtotal Top, column grand/subtotal null, freeze_total false. Preserve null as Default placement or Off totals according to the particular owner, not one universal null rule. |
| `S.numberFormatting` | formatType custom, scalingFactor none, ibcsformat false, two decimals; null display blank and zero display zero. This demonstrates Native/source-format configuration, not all measures' resulting rendered strings. |
| `S.globalStyles` and sizes | Arial, string fontSize 14, headerFontSize 14px, and captured rowHeight 26. The extra rowHeight is observed state; current row-height control ownership remains row_height_config. Do not silently drop it, promote it to the native writer, or infer migration behavior solely from this snapshot. |
| `S.totalDisplayConfig` | subTotalHeight 1, grandTotalHeight 10. The captured 1 differs from the inspected Row Total control's 5-45 range; a UI constraint is not proof that loading this historical value rejects or clamps it. Preserve until the active reader/writer contract is resolved. |
| `S.globalStyles.columnStyle` | forecastOpen, custom and native each contain both read and edit records, six in total, with matching pairs in this sample. Their custom backgrounds coexist with presetType white. Matching values do not prove automatic synchronization or inheritance. Locked and forecastClosed overrides are absent, not explicit white/gray objects to synthesize. |
| `S.gridStyles` and `S.themeColors` | Horizontal minor lines Off despite a saved color; vertical minor lines solid; header lines true; rowAlternate with measureOnlyHighlight false; custom grid/odd/even colors. These remain separate from page/container backgrounds and do not override the property-specific style precedence. |
| `S.layoutSizes` | tableWidth 80, chartWidth 150, labelWidth 120, bulletWidth 300, maximumChartWidth 200, maximum-width limit false, isResponsive false, preferedWidthSelection measure. These are sample settings, not recommended dimensions or proof of final rendered widths. |
| Expansion and Tree sizes | Row and column expansion have separate saved state; showColumnExpandCollapse false can coexist with remembered expanded column levels. node_dimensions is Global with explicit null global/level members, not zero-size records. Preserve those distinctions and do not infer Tree is the active layout. |

The capture omits formatConfig, numberFormatUIConfig, gridLineCount, columnMeta, tree_config and ragged_hierarchy_config from S. That omission does not establish unsupported features or permission to write defaults over existing settings; consult the actual owner and fresh state. Do not use cached dimension/measure catalogs, audit logs, recent/frequent colors or migration markers as business design inputs. Scan the supplied file without fetching its live original, copying sample identities or treating a captured schema marker as ALM portability proof. Reuse [layout](#layout-and-measure-placement-authoring), [number format](#number-format-authoring), [grid appearance](#grid-appearance-authoring) and [Column Style](#column-style-authoring) contracts for changes, then verify the affected native result separately.

### Persisted State Is Not Exported State

getVisualPropertiesForExport reads visual metadata from cloud storage. `EntityNotFound` yields an empty object; other failures propagate. This retrieval is not evidence that any arbitrary UI property survives import.

OneLake Planning export normalizes visual/query IDs, rewrites measure references to GUIDs, removes prior schema markers, applies property rewires, cleans visual state, and adds event triggers before writing visual properties. It creates a visual folder under `sheets/{sheetRecordGuid}/visuals/{visualRecordGuid}`. Schema construction preserves the supplied type casing through getSchemaUrl.

The actual cleanupVisualStateForExport body deletes `properties.visualState.lock_state`. Its comment additionally mentions notes/icon cleanup not present in the inspected body. Follow executable behavior, not that stale comment, and do not infer other cleanup is absent elsewhere.

| Inspected OneLake output | Construction / presence rule | Consequence |
| --- | --- | --- |
| `properties.json` | Adds `$schema` from `Planning/Properties` and spreads the transformed properties payload. | Do not assume the public example's wrapper is the native store shape. |
| `modelTemplate.json` | Emits nonempty model-template data after `transformModelTemplateForExport`. | Do not copy model-editor state directly. |
| `writeback.json` | Emits nonempty settings; `destinations` appears only when a nonempty array. | Export can omit a field marked required in the public table; acceptance remains unverified. |
| `dataInput.json` | Emits only when columns exist; removes `sqlPk`, uses `columns`. | Public page marks this part required, but the inspected exporter can omit it. |
| `insertRows.json` | Emits only when rows exist, using `rows` and the audit-field cleanup helper. | Native inserted rows require record/reference conversion. |

Bundled synthetic fixtures establish the listed saved-shape relationships.
Exact import selection, rewire definitions, companion records and round-trip
behavior still require feature-specific validation against the current contract.

### Mixed-Visual Part Completeness

Validate parts against the owning declared sheet/visual, selected export route, family-specific writer and applicable schema, not a shared basename or the descriptive name of a decoded file. Planning and PowerTable both emit properties.json with different schema families and construction paths; do not flatten one family's wrappers to imitate another. Schema markers are evidence to reconcile, not proof of import compatibility.

The PowerTable factory selects export/import implementations from its useOneLake argument. The V2 checks below are not evidence of the supplied artifact's migration state or blanket V1 behavior; resolve the caller's decision before applying route-specific construction.

The inspected PowerTable V2 folder builder uses the sheet GUID map when available, otherwise falls back to the workload folder before adding visuals/<visual GUID>. Resolve every intended visual's sheet mapping before packaging; a successful upload through that fallback does not establish the published sheets/<sheet GUID>/visuals/<visual GUID> placement. Do not invent a sheet binding or promote the fallback layout into a supported public recipe.

Forms and automations emit only for nonempty returned collections. Compare intended features and resolved records with actual emitted parts; missing optional parts are neither universal unsupported-feature evidence nor an instruction to fabricate empty/default configurations. Preserve per-family companion requirements, and distinguish successful export from semantic completeness. These checks do not close reverse import, source/connection mapping or full PowerTable construction.

### Published Packaging

The public reference describes JSON definition files carried in REST `parts`, with `path`, Base64 `payload`, and `payloadType: InlineBase64`. Definition-file content does not contain its own REST wrapper. Use forward slashes in part paths. Resolve real sheet/visual/measure references; do not generate external resource IDs as substitutes for target metadata.

Recorded conflicts: public Planning schema examples often use lower-case URL segments while inspected exporter calls use `Planning/...`; equivalence has not been tested. Published `dataInput.json` and writeback `destinations` requiredness differ from the inspected conditional emitter. These are unresolved compatibility boundaries, not permission to silently choose either representation.

## Feature Catalog Conventions

F01-F30 are local routing identifiers, not application pages, business requirements or production folder identities. Every section is a **partial internal contract**. Native paths describe the linked store/Rust layer, not an asserted exported JSON Pointer. Resolve imported types and serialization before construction. All examples are synthetic native subtrees/settings, not full parts or JSON Patch documents. TypeScript requiredness is not ALM requiredness; unlisted fields are not necessarily unsupported.

| ID | Feature | Verified starting layer / remaining boundary |
| --- | --- | --- |
| F01 | [Layout](#f01-layout) | Store mutation and side effects; enum wire values and ALM path open. |
| F02 | [Aggregation Settings](#f02-aggregation-settings) | Global/row/cell stores; external enums and portable IDs open. |
| F03 | [Quick Format](#f03-quick-format) | Reducer defaults/merge behavior; save/import wrapper open. |
| F04 | [Insert Row](#f04-insert-row) | UI row interface and Rust distinction; requests/metadata/import open. |
| F05 | [Insert Column](#f05-insert-column) | UI measure interface; creation and backend conversions open. |
| F06 | [Pivot](#f06-pivot) | Preset type/presence constraint; preset-to-assignment conversion open. |
| F07 | [Visual Filter](#f07-visual-filter) | Variant reader and tagged-rule use; full recursive union open. |
| F08 | [Filter Context](#f08-filter-context) | Charts binding/defaults/reducer; saved/ALM mapping open. |
| F09 | [Forecast](#f09-forecast) | Form types/defaults/mutations; serde dates and dependencies open. |
| F10 | [Fiscal Year](#f10-fiscal-year) | Rust value/update/hydration; chrono wire type and ALM open. |
| F11 | [Row Model](#f11-row-model) | Nine native row variants/common members; metadata leaves open. |
| F12 | [Measure Model](#f12-measure-model) | Rust members/defaults/replacement; ID and ALM mapping open. |
| F13 | [Approval](#f13-approval) | UI/request shapes; backend rules and portable identities open. |
| F14 | [Formatting](#f14-formatting) | Scope maps/symbolic types; wire keys and nested styles open. |
| F15 | [Conditional Formatting](#f15-conditional-formatting) | Rule families/enums/interface; factories/native/ALM open. |
| F16 | [Column Style](#f16-column-style) | Controller/store distinction; complete style types/ALM open. |
| F17 | [Writeback](#f17-writeback) | OneLake extraction transformations; destination variants/import open. |
| F18 | [Infobridge](#f18-infobridge) | UI requests, worker dispatch, export root; route/step/import closure open. |
| F19 | [Blend](#f19-blend) | Runtime polling/events; dependency persistence/cascade contract open. |
| F20 | [Anchor Measures](#f20-anchor-measures) | Rust subtree/defaults; hash/ID conversion/ALM open. |
| F21 | [Data Pane](#f21-data-pane) | Props/mode visibility/defaults; assignments/save/ALM open. |
| F22 | [Side Panel Filter](#f22-side-panel-filter) | Page state/editor reader fallbacks; writer/variants/ALM open. |
| F23 | [Bookmark](#f23-bookmark) | Snapshot types/report-only export query; cloud/import mapping open. |
| F24 | [Home Layout](#f24-home-layout) | Legacy workload save, V2 role-content lifecycle and client layout boundaries; server/ALM/rich-text/asset portability remain partial. |
| F25 | [Security](#f25-security) | UI gates/forwarder; RLS implementation/persistence/ALM open. |
| F26 | [Themes](#f26-themes) | Definition/selection/reader distinctions; full theme leaves/save/ALM open. |
| F27 | [Embedding](#f27-embedding) | Linked implementation handles pagination; complete embedding contract open. |
| F28 | [Header Footer](#f28-header-footer) | Visibility and editor state; saved canvas/assets/ALM open. |
| F29 | [OnChangeFormula](#f29-onchangeformula) | Native option and UI value updates; formula/save/ALM closure open. |
| F30 | [Allow Input Based on Formula](#f30-allow-input-based-on-formula) | Native union and evaluation reader; caller/import/permission precedence open. |

## Matrix Authoring and Formatting

### F01 Layout

Intent: switch hierarchy/table/stepped/outline/drilldown layouts through the shared Toolbar. The layout store is the state owner, not the toolbar bridge.

| Native path / input | Contract |
| --- | --- |
| `inforiverProps.layout` | Imported `LayoutType`, re-exported as `Layout`; initial value `Layout.Hierarchy`. Wire literals are not established by those TypeScript symbols. |
| `layout.update(value)` | Returns prior state when there are no row dimensions; otherwise uses `value || state`. |
| Row expansion | Hierarchy/Table reset expansion; Stepped resets or expands to first level depending on layout mode/drilldown. |
| Drilldown | Disables search and ruler through separate dispatches. |
| Quick filter | Stepped/Table/Outline remove `row_label` rules; empty remaining rules become null. |

Do not treat a layout edit as a scalar-only update with no side effects. The store contains `undo: {}`; the `NO_UNDO` marker on dependent dispatches does not mean the whole feature has no undo. **ALM gap:** binding-to-cloud-property serialization, selected visual family, enum literals, and reverse restoration are not closed; no complete layout payload is provided.

#### Native Planning Layout Contract

The legacy store above is not the native Planning wire contract. LayoutConfig explicitly serializes `layout_type` as `Hierarchy`, `Table`, `Stepped`, `Outline`, `Drilldown` or `Tree`; its default is Hierarchy. `measure_layout` is optional, defaults to None/null, and accepts `Column` or `Rows`. Tree is not an alias for Drilldown. These source declarations close the native enum gap, not full item-definition restoration.

Workflow conversion maps `Rows(...)` to `Some(Rows)`, `Columns(...)` to `Some(Column)` and `None(...)` to None. Do not write the command spelling `Columns` as a saved enum or treat explicit Column as equivalent to Default/null. Layout and measure-placement commands carry different optional dependent updates for totals, grouping, expansion, filters, notes, ranking, number formats and ragged hierarchy; do not strip these dependencies when reproducing a supported UI action.

`LayoutConfig.update` changes only the chosen workflow branch; `patch_update` preserves an absent `layout_type` but directly assigns `measure_layout`, so omission can clear an existing placement. Backend persistence is native-mode-dependent and this AppProperty declares undo unsupported; that does not redefine legacy store/history behavior. Existing tests `test_update_layout_type_hierarchy`, `test_update_measure_layout_rows` and `test_layout_config_default_values` cover those native transitions/defaults; they have not been executed for this documentation update.

#### Layout and Measure Placement Authoring

**Business workflow:** choose the view that supports the decision, then configure measure placement, expansion and totals independently. For Category -> Sub Category against Year -> Quarter -> Month, a category manager can review Beverages, expand its product groups and edit an eligible Forecast input. The supplied rounded January Plan figures `34.60 + 17.28 + 4.03 = 55.91` million are an additive illustration, not a proof of native aggregation or stored precision. Changing presentation does not create transactions or new member identities; changing a [saved Pivot](#pivot-view-authoring) can change the grouped view and visible metadata without replacing base assignments.

| Layout choice | Presentation and return to detail | Source-confirmed switch effects |
| --- | --- | --- |
| Hierarchy | Compact hierarchy-label column; expand Beverages to see its groups beneath it. Mixed layouts can introduce more label columns. | Selects row subtotal Top, plus/minus-square icon and child-count Off. |
| Outline | Separate dimension columns with sparse own-level labels; repeat-level settings can repeat ancestors. Parents remain when subtotals are Off. | Selects row subtotal Top and freezes totals. |
| Stepped | Separate dimension columns; first-child-chain placement avoids repeating ancestor labels. Expanded subtotal rows suppress upper labels and may place subtotal text in the next label column. With subtotal Off, effective leaves remain. | Selects row subtotal Bottom and freezes totals; it is not merely Outline with a renamed subtotal. |
| Table | Repeats ancestor labels across dimension columns; non-grand-total labels have no expanded state. With subtotal Off, shows effective leaves, not underlying transaction records. Return to a hierarchical layout for normal branch navigation. | Clears row subtotals and row groups, expands the grid, freezes totals and removes the hierarchy icon. Grand totals are not universally removed; bottom subtotals can be enabled separately. |
| Tree | A separate tree-rendering surface for hierarchical/KPI relationships, not the grid Drilldown branch. Configure its primary/comparison measures and supported time context before use. | Selects row grand/subtotals Top, freeze Off, clears explicit measure placement and column grouping; invalid comparison measure becomes `none`. Scenario comparison bypasses this Tree render branch. |

These are UI-switch effects, not deserialization defaults. Financial-template switches additionally clear row grand totals for the four grid layouts. Evidence: label handlers, native layout filtering, layout controller, Tree render selection.

| Layout -> Measures | Native `layout.measure_layout` | Business-visible arrangement |
| --- | --- | --- |
| Default | null | Period hierarchy first, then adjacent Plan/Actuals/Forecast values inside each period. |
| In Rows | Rows | Managed visible measures, ordered by `order`, become rows within business categories; unmanaged eligible measures follow. A configured measure tree supplies ordering for eligible non-Table/non-Stepped layouts. |
| In Columns | Column | A synthetic Values level groups each measure above its Year/Quarter/Month series. Managed measure order takes precedence. |

For 12 months and 10 measures, fully expanded Default has `12 * 10 = 120` measure-value columns before totals. In Rows can retain 12 month-value columns and put the measures vertically; this trades width for rows, not a fixed-pixel-width guarantee. In Columns organizes the same fully expanded combinations and does not inherently reduce their count. A Forecast series and its time levels can be expanded/collapsed using enabled column controls; measure-prefixed column IDs keep series state separate. Do not copy those derived IDs into model field identities. Evidence: Default iteration, Rows ordering, Columns transformation.

**Availability:** the current Fabric menu hides all five layouts without row dimensions. Outline/Stepped require `PlanningSteppedAndOutlineLayout` and are disabled in a pivoted view. In Rows is disabled for Tree/mixed layout. Tree requires usable visible measures and valid measure state; no column dimensions is allowed, otherwise a time dimension must exist. Unconfigured entry opens Tree configuration. Do not import older menu restrictions into the current Fabric menu without matching its route. See Home builder and Tree availability.

##### Hierarchy and Tree Settings

Persisted native keys are `layout`, `totals_config`, `ragged_hierarchy_config`, `aggregation_config` and `tree_config`, not every Rust member's internal name; see property constants. Other frontend settings below remain under their named visual-state objects. Preserve mode/route-specific serializers and unrelated state.

| Owning setting | Supported controls, initialization and dependencies |
| --- | --- |
| `row_expand_state_config` | `rows` and `expand_till_descendant` ID maps start empty; `grid_state` starts `Grid(Expanded)`, or carries level states. States are Expanded/Collapsed/Nill. `max_level` is optional, not evidence that every consumer applies it. A grid update clears row/descendant overrides. Branch, descendant, level and whole-grid commands are distinct: Stepped does not universally collapse the whole grid. |
| `tableState.expandCollapseIcon`, `.columnExpandCollapseIcon` | PlusMinusSquare, PlusMinusSolid, PlusMinus, Arrow, Gmate, None; initial row/column choices PlusMinusSquare/Arrow. `gridStyles.showExpandCollapse` and `.showColumnExpandCollapse` govern control visibility separately from expansion state. The skill default for both is the exact saved lower-case `gmate`, regardless of use case; see [report presentation defaults](report-presentation-defaults.md#gmate-is-the-universal-row-and-column-icon-default). |
| `columnExpandCollapse`, `tableState.columnHierarchyLevel`, `expandColumnToLastLevel` | Per-column map starts empty; expand-to-last starts false. Per-ID state precedes level state outside column-break exceptions. Explicit Column placement uses measure-specific IDs. Preserve these states when appropriate, but use the owner's switch/reset behavior rather than replaying obsolete IDs. |
| `uiSettings.hideExpandLevel`, `.showRowDescendants`, `repeatLevelLabels` | Level visibility, child-count/descendant presentation and dimension-keyed repeated labels are separate controls. Hierarchy-only per-level hiding requires at least three row dimensions; expand-to-level excludes Table/Drilldown/summary. |
| `ragged_hierarchy_config` | Frontend initial `enabled=false`, `hide_blanks=ValueCategory`, `single_child=All`; `hide_blank_columns`, `hide_blank_dimension`, `hide_zeros`, `suppress_native_measures`, `suppress_di_measures`, `suppress_calculated_measures` false. HideBlanks choices VisibleValues/Value/Category/ValueCategory; SingleChild choices All/ParentOnly/ParentMultiLevel/SingleChild/SingleChildLevel. These filter display/eligible hierarchy paths, not permission grants. Ragged UI is hidden in Table/Drilldown, disabled in Rows; switching to Rows disables it. |
| Group and label sizing | Group requires eligible edit-mode selection. Current row-group predicate rejects Planning Sheet and additionally excludes non-Hierarchy, Rows/mixed, summary, row-break/smart-pagination and ranking combinations; do not promise it as a universally available Planning command. Column grouping excludes explicit Column and invalid selections. Indentation, label/column dimensions and responsive fitting remain separate from grouping and are covered under [appearance](#grid-appearance-authoring). |

Evidence: row expansion owner, column expansion reader, hierarchy controls, ragged initializer, group restrictions.

Tree has its own settings, not a renamed hierarchy grid. Frontend Tree initialization and native Tree defaults are separate layers:

| `tree_config` family | Frontend initial state and preservation rule |
| --- | --- |
| `visual_type`, `orientation`, `layout`, `margin`, `fit_mode` | null, LeftToRight, Normal, 0, BestFit. Null visual type does not instantiate the enum's default subtype. |
| `connector` | `lineType=curvedLine`, `lineWidth=1`, `lineStyle=solid`, `showArrow=false`, `arrowSize=15`; preserve the nested object when changing one control. |
| `legend.show`, `common_settings.show_tooltip` | Both true. |
| `node.node_view`, `.allow_customization`, `.node_components` | FullView, false; variance/variance_percentage/sparkline true and child_count false. Native component defaults are all false. |
| `node.conditional_format` | Frontend enabled with threshold/color rules; native disabled with empty rules. Treat the current rules as user configuration, not a universal business classification. |
| `colors` | `main_color`, `font_color`, `background`, `derived_nodes`, `composite_nodes`, `highlighted`, `connectors`; frontend supplies theme colors while native strings default empty. |
| `kpi_measure_ids`, `tree_view_measures`, `levels` | Empty KPI list; primary empty and secondary `none`; empty level map. Native secondary is empty string; an instantiated native level defaults its view to Global. |
| `simulation`, `active_top_node` | Frontend display Hover with empty simulating node; active node empty with root in available IDs. Native display Off and empty available IDs. These states do not establish Goal Seek or optimization permission. |
| `header_kpi`, `sparkline` | Header enabled, empty measure, theme background/font; sparkline display Default with separate color/varianceColor. Native color defaults differ. |

The Tree toolbar conditionally exposes subtype/time/baseline/KPI/scenario/display controls. Top-level updates are shallow; specialized nested handlers merge connector/legend state. Resolve the actual subtype and control before editing optional settings. Existing layout/subtotal, Rows-ordering and column-width fixtures are source evidence, not executed visual acceptance. Test the five layouts, each eligible measure placement, branch versus grid collapse, long labels, subtotal positions and save/reopen with actual filters and identities retained.

### F02 Aggregation Settings

Intent: select global aggregation, per-row overrides, or per-row/per-measure total-cell overrides. Evidence: aggregationType, rowAggregation, and rowTotalCellAggregation.

| Native path | Shape / update |
| --- | --- |
| `inforiverProps.aggregationType` | Imported `AggregationType`; initial `AggregationType.Sum`; falsy update retains prior value. |
| `inforiverProps.rowAggregation` | Map from row ID to `AggregationType`, initially `{}`. `update({ids,type})` assigns selected keys; `updateAll` shallow-merges. |
| `inforiverProps.rowTotalCellAggregation` | Map from row ID to a measure-ID/`AggregationType` map, initially `{}`. Selected-cell updates preserve other keys. |
| `reset()` | Clears the corresponding override map, not an instruction to delete every aggregation setting. |
| Lifecycle | The inspected effects trigger `UpdateType.AGGREATION_TYPE`. |

Use row and measure IDs from the target model. Do not copy the conditional-formatting module's separate `AggregationType` enum. **ALM gap:** external enum serialization, semantic-model restrictions, persisted wrappers, and portable-reference rewriting are unresolved.

#### Totals and Aggregation Authoring

Separate **where totals appear** from **how their values are calculated**. Row grand total spans applicable row members; row subtotals roll up Category or other intermediate row levels. Column grand total spans applicable columns; column subtotals roll up Quarter/Year in the supplied Year -> Quarter -> Month view. Month is a leaf here; a month subtotal requires lower members such as days. A Quarter subtotal is not the column grand total.

| Native `totals_config` member | Values and native default |
| --- | --- |
| `row_grand_total` | Top / Bottom / null; default Top. Split is rejected for grand total. |
| `row_sub_total` | Top / Bottom / Split / null; default Top. |
| `column_grand_total` | Left / Right / null; native default null; skill authoring default Left. |
| `column_sub_total` | Left / Right / null; skill authoring default null (OFF). |
| `freeze_total` | Boolean; default false. |

UI Off maps to null, not an `Off` enum. The native totals updater assigns position Options directly, so omitted positions can clear them; omitted freeze preserves its value. This is not a generic sparse patch. The supplied snapshot's Top/null/Bottom/null with freeze true is an observed state, not the default. The current totals gates disable Top for Table/Stepped, Bottom for Outline, column grand total for explicit Column placement, and limit Split to eligible hybrid mode. Freeze controls are currently hidden despite the persisted field. Dimensions, row breaks, pivots, sparklines and root-row type impose additional gates; a stored field does not imply its control is always offered.

**Monthly entry, quarterly review:** enable eligible column subtotals to review Q1 and row subtotals independently for categories. For additive Plan amounts, `78.42 + 80.51 + 90.38 = 249.31` million. Verify underlying values and filters: rounding displayed children first need not equal a normal total. Row Total opens title/height settings, not Manage Aggregation; its UI height range is 5-45. `totalDisplayConfig.totalCustomTitle`, `totalsDisplay`, `subTotalHeight` and `grandTotalHeight` govern presentation separately from native placement. See RowTotalsModal and command dispatch.

| Manage Aggregation choice | Calculation distinction and availability |
| --- | --- |
| Native | UI sends null, not literal `Native` or explicit `None`. Ordinary no-method processing can retain source values; reverting an override may restore a backup or refresh. Grouped Pivot/rollup paths may instead aggregate numeric native measures, so model-evaluated ratios are not universally preserved. |
| None | Explicit no-aggregation method, distinct from absent/null Native. |
| Sum / Minimum / Maximum | Sum / Min / Max over eligible values, with axis/context semantics from the calculation path. |
| Average Children / Average Leaf / Average Excluding Zero | Average / AverageLeaf / AverageExclusiveZero; choose the denominator deliberately, not merely a display label. |
| Std. Deviation / First / Last | StandardDeviation / First / Last; ordering and eligible populations matter. |
| Formula | Available for applicable formula measures; formula evaluation is not the sum of displayed ratios. |
| Visible Rounding | Feature-gated method with its own rounding behavior, not a general promise that every total sums rounded cells. |
| Weighted Average | Appended for already-weighted measures; hidden on the column axis and disables the applicable axis selector. A native implementation exists, but this is not a generally offered create-weighted-average option. |

The shared selector is used on both axes with axis/type restrictions: row selector needs row dimensions; column selector needs column dimensions and excludes hierarchy measures. Date offers None/Min/Max/Last. Native is removed for applicable data-input, formula, Pivot, breakdown and playground cases. Count/Median are not in this selector; the inspected native aggregators leave some enum variants uncomputed. Do not promote enum membership to selectable or production-ready functionality. Evidence: selector options, axis controls and Native mapping, native restore/recompute.

Native `aggregation_config` contains default-empty `measure_aggregation`, `row_measure_aggregation`, `row_member_measure_aggregation`, `row_dimension_aggregation` maps. The native declarations/helper distinguish absent axis overrides from an explicitly constructed None method. Do not treat empty maps as instructions to sum every native measure or infer a universal precedence from map names. In the inspected eligible rollup resolver, row metadata override precedes the measure's axis method, then Sum fallback, including numeric native measures; resolver. Keep row/member/dimension identities and selected axes intact when changing overrides.

**Non-additive example:** revenue 100/50 and profit 30/10 produce margins 30%/20%; combined revenue 150 and profit 40 give `40 / 150 = 26.6667%`, not 50% or 25%. A suitable model measure can return its own ratio at source totals, but a grouped view's fallback Sum does not preserve that semantics. Use a supported formula/aggregation design that recomputes from aggregate numerator and denominator; test both axes, Pivot grouping and grand/subtotals. Do not invent a weighted option or treat Number Formatting -> Percentage as aggregation. Native fixtures for axis precedence and weighted calculations were inspected, not run; save/reopen, effective selection and numerical behavior remain runtime checks.

##### Total Labels and Display Controls

The totalDisplayConfig initializer and effects additionally define the following frontend defaults, independently of native total placement and aggregation:

| Group | Fields and initial values |
| --- | --- |
| `totalCustomTitle` | grandTotalTitle `All`, columnGrandTotalTitle `Grand Total`, totalColumnSuffix `Total`, steppedSubTotalTitle `none`, steppedSubTotalText `Total ` (trailing space), splitTotalRowSuffix `Total`, columnSubTotalTitle `none`. |
| `totalsDisplay` | showColumnGTAsTable true, showSubTotalsAsTable false, showVarSubTotalsAsTable false, showTotalAsTable true, showVarTotalAsTable false, advancedSteppedLayout false, removeSingleChildren true. These are display/renderer settings, not replacement row/column aggregation methods. |
| Heights | subTotalHeight and grandTotalHeight both 10, separate from row_height_config and the row-height/header-height defaults. |

Row-subtotal Category Text offers prefix/suffix/none; Title Text supplies the string, while split rows use their own suffix. The Hierarchy settings contain a concrete visibility inconsistency: Category Text tests lowercase top/bottom while Title Text tests native Top/Bottom. Document the stored options without claiming that the Category Text control is always reachable. The menu values are not the total-placement enum.

Remove Single Children is described by its UI as hiding leaf nodes without siblings; it is separate from ragged_hierarchy_config.single_child. Enabling advancedSteppedLayout updates native display config, hides row expansion icons, resets expansion and clears row metadata; disabling restores plusMinusSquare and first-level expansion. It is not a harmless text-style toggle. Nested title/display updates merge their respective siblings before the controller call. The store binds this object to the older inforiverProps property name totalsDisplay while exposing totalDisplayConfig in state; resolve the actual host/export layer instead of renaming a saved object by analogy. Source defaults/actions do not certify every legacy presentation flag in the native renderer.

### F03 Quick Format

Intent: change number-format mode, precision, scaling, separators, and semantic formatting. numberFormatting binds to `inforiverProps.numberFormatting`, initially `{}`.

This section is Matrix-only. For Charts use the documented Charts rules in [Source-Backed Contract Rules](#source-backed-contract-rules). Resolve distinct field spelling, enums, mutations and encoding before emitting content; do not transfer Matrix state paths to Charts.

| Native setting | Evidenced behavior |
| --- | --- |
| `formatType` | Explicit reducer branches for `ibcs`, `default`, `flexible`, and `custom`. |
| `noOfDecimal` | Numeric precision; a format-type change injects 1 for `ibcs`, otherwise 2. |
| `ibcsformat` | True for `ibcs` or `default`; false otherwise when changing format type. |
| `showScalingUnit` | True for `flexible` when changing format type. |
| `scalingFactor` | `NONE` for custom, `AUTO_FIXED` for default/ibcs, `AUTO` otherwise; external wire values need resolution. |
| `thousandSeperator`, `decimalSeperator` | Preserve these exact spellings. Reducer splits the supplied separator command value at `@`. |
| `semanticFormatting` | Updated directly by the corresponding setting command; type/default beyond this reducer is not established here. |

`update` and `updateSingleProps` shallow-merge; `updateAllProps` replaces. Changing format type also clears scaling overrides in different scopes. Native **partial settings illustration**, not the complete reducer result (scaling omitted deliberately):

```json
{"formatType":"ibcs","noOfDecimal":1,"ibcsformat":true,"showScalingUnit":false}
```

**ALM gap:** native binding serialization and import preservation remain unresolved; do not insert this fragment into a guessed visual-state path.

#### Number Format Authoring

> v18: [measure-display-defaults.md](measure-display-defaults.md) is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

**Business workflow:** select the intended measures/cells, choose source/measure/uniform/cell-level formatting, then units, precision and optional sign/prefix/suffix settings. A plan amount of 78,420,000 can display as 78.42 with an explicit Millions unit; a fractional margin 0.125 can display as 12.5% under the applicable percentage/type guards. These are display examples, not changes to stored amounts or aggregation. Avoid applying amount scaling or currency prefixes to ratio measures unintentionally. Keep missing plan input visually distinct from genuine zero.

| Quick Format UI mode | `numberFormatting.formatType` | Confirmed transition behavior |
| --- | --- | --- |
| Measure Level | default | autoFixed scaling, two decimals; clears cell/row scaling overrides. |
| Uniform | ibcs | autoFixed scaling, one decimal; clears measure/cell/row scaling overrides. |
| Auto / Cell level | flexible | auto scaling, two decimals, scaling-unit display; clears measure scaling overrides. |
| Native / Source Format | custom | none scaling and two decimals; source formatting is a distinct path, not Uniform with a different label. |

There are four modes in the actual menu, even where screenshots emphasize three. Mode switching can erase scoped scaling overrides; use the controller, not a single scalar edit. Native source formatting can warn about semantic formatting and prefix/suffix alignment rather than universally disabling them; custom scaling labels are disabled on that route.

##### Number Format Property Inventory

The following are **frontend initialization values** from numberFormatting. Saved state, theme/template and host hydration can override them. Unset means absent in this initializer, not an asserted false, null or empty value. Native Rust derives false/zero/empty defaults with scaling-text Short, unlike this UI initialization; do not conflate the layers.

| Client keys | Initialized values, supported choices and dependencies |
| --- | --- |
| `formatType`, `enabled`, `ibcsformat`, `enablePrefixAsUnit` | default; true/true/true. `enableSuffixAsUnit` unset. |
| `scalingFactor`, `scalingTextType` | autoFixed, Full. Wires: none, auto, autoFixed, `1000`, `1000000`, `1000000000`, `1000000000000` as strings. Label choices Short/Medium/Full; display labels Thousands/Millions/Billions/Trillions are not those wire values. |
| `autoLocaleNumberFormat` | Optional Boolean. A new host visual sets it to true when the Planning auto-locale feature is enabled; an explicit saved value wins. Existing reports do not inherit true merely because the feature is available. It controls eligible viewer-locale grouping/decimal separators, not formula parsing, semantic separators or stored values. |
| `noOfDecimal`, `noOfDecimalPercent` | Both 2. Decrement stops at zero, increment obeys maximum precision; reset can write sentinel -1. This is separate from row heights or native input storage precision. |
| `thousandSeperator`, `decimalSeperator` | Comma and dot; preserve these spellings. Separator controls permit up to three characters. |
| `prefix`, `suffix` | Empty strings. `displayPrefixAsUnit`, `displaySuffixAsUnit`, `showDisplayUnit` unset; display-unit strings can also be computed per cell, not merely alignment flags. |
| `semanticFormatting`, `showNegativeSign`, `showScalingUnit`, `showPercentageSymbol`, `customizeScalingLabel` | All false initially; mode changes and scoped overrides can alter applicable behavior. Semantic selectors require semanticFormatting. showPercentageSymbol alone is not the Percentage format operation. |
| `positiveValueColor`, `negativeValueColor`, `neutralValueColor` | #82BA00 / #FF000A / #B3B3B3, separate from row highlighting and conditional formatting. |
| `positiveValueFormat`, `negativeValueFormat` | x / -x. Positive choices x, +x, x+; negative choices -x, x-, (x), x. |
| `thousands`, `millions`, `billions`, `trillion` | k / m / b / t. |
| `thousandsMediumText`, `millionsMediumText`, `billionsMediumText`, `trillionMediumText` | in k / in m / in b / in t. |
| `thousandsFullText`, `millionsFullText`, `billionsFullText`, `trillionFullText` | in Thousands / in Millions / in Billions / in Trillions. |
| `showNullAs`, `showZeroAs`, `customNullText`, `customZeroText` | blank / zero / empty / empty. Both selectors allow blank, zero, hyphen, custom. Zero-as-zero retains an already formatted zero; custom/blank/hyphen substitution is display behavior. |
| `enableNullAsZero`, `suppressCellErrors`, `customErrorText` | Initially unset. Null-as-zero disables the Null selector. Error suppression initializes customErrorText to #ERR, with a six-character control limit; the error code/message is retained even when its displayed text changes. |
| `showTooltipAsUnit`, `showTooltipDecimal`, `tooltipDecimal` | false / false / string `1`. Ordinary numeric tooltips and special-chart tooltip branches differ; the inspected General tooltip controls are commented out. Do not promise universal tooltip-unit/precision controls from these persisted fields. |
| Separate `numberFormatUIConfig` | `decimalPrecision=8` with UI range 8-17; `prefixNullWithUnit=true`, `suffixNullWithUnit=false`, `highLightInvertRows=false`, `highLightInvertCells=false`. Not additional leaves of the native NumberFormatting struct. |
| Separate `signDisplayOptions` | Boolean initialization: `show_category_sign=false`, `show_positive_sign=true`, `hide_result_sign=true`. These retain snake_case in the client state and are not aliases for positiveValueFormat/negativeValueFormat. |
| UI-only initialization extras | `showDataLabel=true`, `enableDataLabelFormatting=true`, `dlIBCSNoOfDecimal=0`, `dlFlexibleScalingFactor=auto`, `dlCustomScalingFactor=none`; migrationVersion unset. These extras are not fields of the inspected Rust NumberFormatting request/struct and must not be copied there. |

**Null-as-zero can change calculations:** unlike the showNullAs display substitution, enableNullAsZero is consumed as native enable_null_as_zero when constructing formula context. The inspected AVERAGE tests expect a null/10 input to yield 10 with the flag disabled and 5 with it enabled. Those tests were read, not executed here. Treat this as a calculation-policy choice and verify affected formulas, not merely a way to make empty cells display zero. It does not by itself establish that stored missing input records become persisted zeros.

The sign-display model merges one requested flag with existing flags, then calls the native client and refreshes pagination. The cell inversion reader uses show_category_sign under numeric, leaf, calculated-column and special-chart guards; it can multiply the displayed value by a category/inversion sign. This is not a universal plus-prefix operation or permission to rewrite stored inputs. Positive/result-sign behavior on every label/chart path remains consumer-specific.

Transport matters: jetModelsMap maps outer `number_formatting` to `numberFormatting`, not nested names. The native stored struct uses snake_case members such as `no_of_decimal` and `thousand_seperator`; its update request accepts camelCase within the number_formatting envelope. Native patch applies only Some fields, including explicit false/zero/empty string; it does not make an arbitrary partial stored object a valid full hydration payload. Resolve the writer/reader at the actual route before translating observed `visualState.numberFormatting`.

Example selected **client-state fragment after choosing Millions and two decimals**, not the complete controller mutation, Rust hydration object or ALM part:

```json
{"formatType":"ibcs","scalingFactor":"1000000","noOfDecimal":2,"showScalingUnit":true}
```

The Percentage command writes format property `10`; prefix/suffix are `8`/`9`, decimals `11`, scaling `13`. Applicable measure/row/column/cell operations in `formatConfig` are ordered by `order`, not a universal cell-over-row-over-measure hierarchy. Numeric display multiplies by 100 only under its actual percentage/type conditions. Keep scalar/percentage-point meanings distinct and inspect format operation ordering and percentage display.

Display precision is not a blanket input-parsing guarantee. InlineFormulaUtils strips whitespace/group separators, normalizes decimal separators, recognizes K/TH/M/B/T and rounds inline absolute/percentage changes to two decimals. Bulk entry accepts percent forms for Append By, setting isPercent, but rejects them for Set Value; it uses parser-default comma/dot rather than necessarily the display separators. Test these routes separately, especially when users enter fractional ratios or locale-formatted amounts.

Validation should distinguish stored value, formatted text, scope/order of overrides and entry parsing. Check 78,420,000 -> 78.42 Millions, 0.125 -> 12.5%, blank versus zero, negative/currency forms, reset sentinels, tooltip branches, all four mode transitions and overridden measures. Reopening/importing raw native/client representations, actual fonts/units, locale entry and bulk edits remain native-runtime checks, not conclusions from arithmetic or JSON parsing.

### F04 Insert Row

Intent: insert formula/static/template/forecast/contribution/aggregated rows and related variants. IDynamicRowConfig is a UI-facing contract; the Rust dynamic row contract is different.

| UI-facing path | Native distinction |
| --- | --- |
| `id`, `parentId`, `previousRowId` | String references in the UI interface; not proof of portable GUID domains. |
| `label`, `type`, `formula` | UI labels/type and formula; Rust uses `title` and `row_type` with externally tagged variants. |
| `disabled`, `deferredType` | Required by the inspected UI interface; verify the request/ALM layer separately before choosing presence semantics. |
| `includeToTotal`, `includeInChart`, `bindForCrossFilter` | Optional booleans in UI; require actual conversion to their Rust/backend equivalents. |
| `templatePosition` | Optional `first`, `last`, or `auto`. |
| `staticData` | Optional string-keyed map of string or number values. |
| `openPeriodConfig`, `closePeriodConfig` | Optional structured row-period configuration, not the measure forecast configuration. |

Rust variants are listed under F11. The inspected OneLake exporter emits `insertRows.json` with `rows` only when records exist. **Gap:** UI-to-request transformation, per-variant metadata, row-record conversion, import order/dependencies, and complete required companion context remain unresolved. No runnable row recipe is claimed.

#### Local Insert Rows Versus Business Members

Select by purpose, not by whether the requested object appears as a row. The supplied Inputs/Formatting/Workflows guide describes limited local row additions, substantial Row Model hierarchies and governed source-member creation as different workflows. Its video narration and new-member supplement are reported evidence; the packaged repeated-row definition was independently checked, but no standalone comparison-row definition or live master-data process was established.

| Business request | Starting choice | Required distinction |
| --- | --- | --- |
| One comparison subtotal or temporary local reporting line | Insert Formula Row or another supported local row type | Resolve source rows and period/context; choose Include in Total deliberately and position the row. |
| Small repeated contingency or adjustment | Templated Insert Row at the intended dimension level | Configure type, default units, scope, edit mode, scaling and total participation; repetition is not a new source member. |
| Substantial reusable KPI/account hierarchy | Row Model | Use the existing hierarchy/template contracts rather than accumulating unrelated one-off rows. |
| New product, category, supplier, department, cost center or project shared across reports | Governed source dimension, optionally maintained through PowerTable | Requires source save, stable keys, relationships and valid planning intersections; neither a visual row nor a free-form picklist creates them. |
| Another metric over existing products | Input/formula measure; optional Measure Model grouping | Adds a measure, not a row member or source schema field. |

**One-off comparison:** illustrative category amounts 900,000 and 300,000 produce a difference of 600,000. Exclude that diagnostic formula row from the original category total: the total remains 1,200,000, not 1,800,000. Resolve actual row-reference syntax, test period/filter/expansion behavior and retain existing member identities. The guide reports this video demonstration; it is not present as a standalone inserted-row definition in the packaged snapshot.

**Repeated adjustment:** the checked model-template part contains one row and one Append application with null condition. Its StaticRow default is the string `"100"`, include_in_total true, roll_up_aggregation Sum, scaling_factor null and row_edit_mode InEditModeOnly. The application dimension resolves to the intended Category field in that snapshot. Three eligible categories with one 100 adjustment each imply 300 contributions for the stated series/period, not a verified native total or a production default. Null scaling is not a universal wire spelling for UI No Scaling. The export uses properties.dynamicRowTemplates alongside properties.dynamic_row_template_dimensions_map; do not rename the earlier native snake_case definition contract or turn this snapshot into a create request.

**New shared member:** capture its stable key, label, parent, status and required attributes; validate uniqueness/parent/approval rules; save through the configured source-table process; verify the model exposes it with correct relationships; establish valid Product/Region/Channel combinations even without historical facts; then verify planning input retention and another authorized consumer. A proposed 10,000 units at 2.50 gives 25,000 revenue, but the arithmetic does not create the member. PowerTable form Apply and final database save are distinct steps where the documented workflow uses pending changes/Save to Database. Source/model synchronization, filters and storage mode determine availability; do not promise instantaneous propagation or provision/alter a source without authority.

The supplement's restriction of Insert Rows to editing is stated product direction, not a verified universal deployed permission. The saved InEditModeOnly row setting is narrower evidence. Distinguish availability of the insertion command, permission to edit an existing row and source-write authority. Preserve the existing [Row Model](#row-model-business-authoring), [identity mapping](#dimension-id-mapping) and [maintenance controls](#business-controls-lookups-and-rules) safeguards; specialized row types and deletion effects still need their own functional contracts.

### F05 Insert Column

Intent: create calculated columns/measures and data-input/forecast variants. ICalculatedColumn is not a minimal creation payload or backend record schema.

| UI-facing field | Type / caveat |
| --- | --- |
| `id`, `name`, `formula`, `desc` | Strings required by this interface. |
| `category`, `measures`, `depMeasures` | Required string arrays; dependencies need real target references. |
| `operation` | Imported `Operation`; serialized allowed values not closed. |
| `aggregation` | Imported JetStream `AggregationType`, distinct from similarly named CF enums. |
| `anchorConfig` | Optional or null; includes UI `is_enabled` not present in the Rust `AnchorConfig` struct. See F20. |
| `dataMap` | Optional string-keyed map of string/number values. |
| `filterContextDataMap` | Optional context-keyed map of those value maps. |

Do not build a column from only an ID, label and operation enum. Read [Native Measures and Inputs](#native-measures-and-inputs) and each selected branch's current metadata, validator and writer. **ALM gap:** creation workflow, remaining calculated-measure metadata, backend data-input records and reference conversion are partly traced. Public `dataInput.json` columns are a different layer; no whole-column example is asserted valid.

#### Input Type and Placement Workflows

Choose **business grain -> placement -> type -> default -> totals/context -> edit/event behavior**, rather than choosing a control solely from a label. Visual Measure repeats at applicable column-dimension intersections, not just months; Visual Column displays once per row context, not once for the whole report. Neither placement removes filter/scenario or permission requirements. A name containing Measure does not establish placement: the checked snapshot's date field is wrapped in VisualColumn.

| Input type | Business use and placement decision | Configuration and acceptance |
| --- | --- | --- |
| Number | Period quantity/rate/amount override or eligible one-time numeric attribute | Resolve units, source/static/formula/blank default, both aggregations, bounds, parent distribution and locked descendants. Unknown source values are not automatically zero. |
| Text / Long Text where supported | Period explanations versus one-time request description | Choose blank policy, validation/length and total-entry behavior. The saved example is ShortText; it does not prove Long Text has the same trigger/validation capabilities. |
| Checkbox | One assertion, such as a period reviewed | Decide default/null meaning and total entry. A checkbox is not a multi-stage approval process. |
| Person | Owner/reviewer, once per row or per period according to the requirement | Resolve identity and supported selection/default behavior; assignment does not confer authority. Discussed in the guide, absent from this export. |
| Single Select | One current status or classification | Choose manual versus semantic lookup, stable option identity, display style and whether users can add options. Use one state for mutually exclusive approvals. |
| Multi Select | Several concurrent reasons, risks or tags | Preserve option identities/order and permitted vocabulary. Multiple tags must not create multiple submissions or simultaneous contradictory approval states. |
| Date | One request completion date or period-specific delivery/milestone date | Separate manual entry from event-written dates; resolve accepted date representation and ownership. Being an event target does not establish support as an On Change trigger. |

**Placement examples:** monthly rationale/confirmation/delivery date are Visual Measures; an annual coordinator, overall request note or one completion date can be Visual Columns when that is the actual row-level grain. A row shared by multiple requests cannot hold their separate metadata merely by displaying a column once. Define the approval/request identity before choosing one-time status fields.

**Semantic picklist workflow:** select the actual source table, label and key fields, verify key uniqueness/nulls, choose supported appearance and option-creation policy, then save/reopen and test selection after a label change. The inspected snapshot uses options_source Lookup and Chip appearance, with label_id equal to primary_key_id; it does not demonstrate a distinct stable ID-column binding. Prefer a verified stable key when retention requires it, but do not silently migrate existing label-keyed selections. This option key is separate from Dimension ID Mapping for row coordinates.

**Manual picklist workflow:** define the controlled options with stable internal values, labels, order and appearance, configure permitted user additions, then use the selected internal representation through the supported formula writer. Preserve option identity on display-label changes. The example's approved/pending/rejected Multi Select demonstrates a control, not a sound mutually exclusive workflow status; choose Single Select for one current decision. Chip in this snapshot and Arrow in another guide are observations/preferences, not universal defaults.

**Observed saved-input boundaries:** the packaged dataInput part has eleven columns: two Native, eight DataInput records (including three nested in VisualColumn), and one Formula. The eight inputs comprise Number, two ShortText, two Checkbox, SingleSelect, Date and MultiSelect. Direct DataInput commentary/checkbox repeats with column intersections; nested VisualColumn ShortText/Checkbox/Date is one-time placement. All eight on_change_formula strings are empty. No Person or Simulation input is demonstrated. This inventory does not make the input feature exhaustive or establish a portable full-column constructor.

The Number default references the retained source measure; distribution is true and min/max are null in this snapshot. Do not invent configured bounds, assume a frozen baseline or overwrite existing overrides when the source refreshes. Validate source/default availability and actual override/refresh/reset behavior separately from a continuously calculated formula measure. Reuse [complete input records](#input-and-formula-measure-authoring), [context binding](#filter-context-binding-across-layers), [event workflows](#f29-onchangeformula) and [editability](#formula-based-editability-workflow), preserving actual IDs and type-specific settings.

### F06 Pivot

Intent: save alternative row/column/measure arrangements. IPivot requires `id: string`, `name: string`, optional `hidden: boolean`, and at least one of the fields below.

| Native member | Shape |
| --- | --- |
| `rowDimensions` | String array of dimension IDs. |
| `columnDimensions` | String array of dimension IDs. |
| `measures` | Array of imported `IMeasure` records; leaf contract not expanded here. |

The TypeScript `RequireAtLeastOne` constraint requires a member's presence, not a nonempty array. Do not equate saved pivot presets with public `pivotAssignments` records (`bucketId`, `sourceId`, etc.). **ALM gap:** preset persistence, active-pivot selection, conversion to assignments, and import/default behavior remain unresolved. Construct no guessed preset-to-ALM wrapper.

#### Pivot View Authoring

Use saved Pivots for detail planning and grouped review over the same base planning records. Base field assignments, saved view selection, current dimension metadata and expansion are different state. The supplied prompt reports an All view with Category/Sub Category and Year/Quarter/Month, and a Category view selecting Category with Year/Quarter; base assignments remain detailed in both snapshots. Preserve those assignments rather than deleting detail to construct the summary. A pivot can reorder selected dimensions within axes; conditional cross-axis support is described below, not inferred from the deck's examples.

1. Open Pivot, create a named view or duplicate an eligible existing view. Select/order the required row and column fields, and measures/rollups where enabled. Use actual dimension/measure IDs, not display names or source-array positions.
2. Save through the owning controller, reconcile temporary UI IDs with returned native IDs, then select the saved view or use Explorer. Keep All available as the source-detail route where supported; hidden views are not security rules.
3. Check grouped values against the detail under the same filters, input context and aggregation methods. Category/Q1 should reconcile to the illustrative additive `249.31` million, but a ratio requires [non-additive aggregation](#totals-and-aggregation-authoring).
4. If aggregated entry is required, verify that the measure, input rule, descendants, locks, permissions and current scope allow it. Link to [input-rule workflows](#input-rule-business-workflows); a Pivot alone does not grant editing, choose weights or promise redistribution.

| Native/host state | Exact semantics and lifecycle |
| --- | --- |
| `pivot.configs[]` | `id`, `name`, optional `row_dimensions`, `col_dimensions`, `measures`, and default-false `hidden`. Config collection initially empty. IDs remain lossless strings. |
| Axis null versus empty | `row_dimensions:null` / `col_dimensions:null` uses the corresponding source axis; `[]` is an explicit blank/Grand Total-only axis. The deck's empty column-selection UI says all columns; use that UI's serialization, not a blanket JSON `[]` rule. |
| `measures` | Null means source/all selection; explicit native `[]` is rejected. Each selected `PivotMeasure` has `id`, `aggregation_type`, optional `column_aggregation_type` and `rollup_type`. UI empty selection can normalize to null; this is not native empty-list equivalence. |
| `pivot.active_id` | Optional native active config ID. Controller maps All to native null; supplied exports can contain All's registered ID. Resolve the actual load/controller normalization, not equality of one snapshot alone. |
| `pivotExplorer` | `showPivotExplorer` initially false, `activePivot` initially null. UI state is separate from native active ID. Switching updates native selection, synchronizes store, clears expansion and refreshes pagination. Explorer hides hidden entries; disabling Explorer restores default visibility/selection. |
| Create/name/duplicate | UI temporary `pivot_...` IDs are not persisted identity allocation. Default All uses the native `Id::for_str("default_pivot")` convention. Inline rename trims and rejects blank/case-insensitive duplicates, excluding All; an older input path has weaker checks. Duplication preserves applicable source selections, including explicit measures. |
| Hide/delete/order | UI prevents all configurations being hidden and hides default delete. Native delete/visibility selection resolves a visible fallback. Bulk save separates create/update/delete/reorder/active phases; do not assume hidden active content or partial ordering has no effect. Native undo is unsupported. |
| Native update | `update_with` replaces row/column selections even when absent/null, but absent/null measures preserves the old measure list. A rename-only body can clear axes; `measures:null` is not a verified clear-explicit-list operation. Preserve full intended selections and check readback. |

Evidence: native Pivot schema/mutation, request validation, axis semantics, frontend normalization/synchronization, controller. Non-default creation rejects both axes null, not empty arrays; update validation differs. Do not manufacture a create request from a persisted object without its actual validator.

**Synthetic saved-config fragment**, with placeholder identities above the JavaScript safe-integer range, not a complete create request or reference to supplied sample members:

```json
{"id":"9007199254740993","name":"Category","row_dimensions":["9007199254740994"],"col_dimensions":["9007199254740995","9007199254740996"],"measures":null,"hidden":false}
```

**Conditional options:** `PlanningColumnPivot`, `PlanningCrossPivot` and `PlanningPivotNonNumeric` default false in the inspected Shell configuration; deployed overrides were not read. Without cross-Pivot, dimensions stay within source axes. Cross-axis movement requires the column/cross gates, known schema fields and removal from the opposite explicit axis. All selections are read-only. Source: flag defaults, axis adapter. Do not advertise unrestricted field movement or declare the gated feature absent from every deployment.

The non-numeric path offers numeric Sum/Min/Max/Average/AverageExclusiveZero/AverageLeaf/StandardDeviation/First/Last; defaults follow a supported source method, otherwise Sum. Formula/source-only aggregation may be displayed without being selectable. Text/Person/LongText offer Unique/Concat, Boolean AnyTrue/AllTrue, Date Earliest/Latest, SingleSelect Unique and MultiSelect Concat; the first listed rollup is the initial choice. These type-specific rollups are not proof that the similarly named generic aggregation enum is implemented on every path. See numeric options and rollup mapping.

The native pipeline applies the selected config after filtering/ranking and remaps grouped contributions to base rows. Legacy and flagged column-pivot paths differ. FabricHost restoration normalizes old All selections to null. Preserve filters, measure placement, formats and member identities while accepting the owner's expansion resets; do not restore obsolete metadata or fabricate a separate `groupBy` property. The bulk UI reorder branch assembles local requested order but sends existing-order IDs, so saved order requires explicit round-trip verification rather than a source-only success claim.

##### Pivot Business Reconciliation

The deck's examples are illustrative, not executed workflows. Pivots change grouped views of common loaded detail; filters constrain the intended edit scope, not security grants. A filtered Online target is not automatically a global target across excluded channels. Saved views/bookmarks and configured writeback are separate from base-input persistence and authorization. The deck's 12-million-cell statement is supplied product information, not an independently verified limit or latency guarantee.

- **Regional target:** for an explicitly configured proportional rule, store quantities 250/150/100 total 500; target 600 allocates 300/180/120. Reopening store/region views should reconcile, subject to eligibility, locks, actual allocation rules and refresh. Do not infer this weight choice from Pivot configuration.
- **Promotion:** Online quantities 100/200 become 120/240; prices 90/50 become 80/45 and unit costs remain 50/30. Online revenue rises 19,000 -> 20,400 while contribution falls 8,000 -> 7,200. Unchanged Stores contribute revenue 54,000 and contribution 27,000; combined revenue becomes 74,400 and contribution 34,200. Quantity-weighted rates and aggregate ratios are required. At the discounted prices, maintaining original contribution requires about 33.3% volume growth, not the assumed 20%; no automatic demand prediction is implied.
- **Overlapping decisions:** regional/SKU base quantities 300/200/250/250 become 360/240/250/250 after a regional increase, then 360/288/250/300 after increasing global SKU B. Total becomes 1,198; the earlier region targets change to 648/550. Views agree on latest detail, but prior targets are not automatically locked constraints. These overlapping row/column views must not be added together. At prices 120/200 and costs 80/150, revenue is 190,800 and contribution 53,800, about 28.2% margin. This is sequential reconciliation, not concurrent-edit, optimization or approval proof.

Validate null/empty axes and measures, default normalization, hidden/deleted active fallback, name rules, source-field membership, lossless IDs, both-axis totals and explicit rollups. On authorized runtime resources test switch/save/reopen, Explorer-off restoration, grouped editing and unaffected filtered detail, restricted users, ordering and concurrency. The owning native tests are not proof of deployed flags, backend query generation, ALM restoration or saved-input preservation.

### F07 Visual Filter

Intent: filter dimensions and measure values, including text, numeric, checkbox, select, boolean, and relative-date behavior. FilterUtils.getFilterHandler consumes variant-specific filter objects, not a universal flat `{field,operator,value}` record.

| Inspected reader path | Meaning |
| --- | --- |
| `ruleVariant.filter.Text` | Text-filter branch. |
| `ruleVariant.filter.Number` | Numeric-filter branch. |
| `ruleVariant.filter.Boolean` | Boolean-filter branch. |
| `ruleVariant.filter.VariableId` | Variable-backed branch; variable resolution remains open. |
| `parentOperator` | Relative-date `DatePeriods` takes a separate date-range path. |
| `quickFilter.rules[].Rule` | Used by the Layout cleanup reader; tagged node wrapping matters. |

The helper's loose `RuleType`/`RuleGroupType` interfaces are not proof of the imported JetStream `RuleRoot` serialization. String/list/null comparisons differ by operator. **ALM gap:** full recursive RuleNode union, wire operators, map to saved/exported filters, and import restoration. Reject a guessed flat rule recipe until that boundary is resolved.

### F09 Forecast

Intent: configure forecast measures, open/closed periods, reforecasting, source copying, and cube/multidimension settings. forecastConfig is a form/workflow state, not the serialized Forecast measure.

| Native UI path | Type / default distinction |
| --- | --- |
| `tempId` | Number in interface, but initial state uses null. Temporary workflow identity, not measure GUID. |
| `forecastColumnId`, `forecastTitle` | Strings; initial empty values. |
| `forecastPeriodRange.start/end` | Dayjs objects in interface, null in initial state; not automatically JSON timestamps. |
| `forecastSeriesConfiguration[]` | Period entries with optional copy method/source, source range, and file-import metadata. |
| `openPeriodConfig` | Initial DATA_INPUT / BLANK / empty value. |
| `closedPeriodConfig` | Initial LINK_TO_MEASURE / empty value. |
| `closePeriodTill` | String in interface; initially null. |
| `cubeData` | Optional cube breakdown/synchronization/multidimension payloads; nested contracts unresolved. |

`update` replaces when an existing config lacks a truthy `tempId`, otherwise appends. `openReforecast` replaces; `patchUpdate` shallow-merges only a matching truthy `tempId`. Forecast metadata types distinguish string date ranges from workflow Dayjs values. Do not serialize Dayjs/form state as `columnMeta.measure_type.Forecast`.

#### Cube Planning Authoring

Choose Cube when an assumption's input grain must be related to a configured analytical breakdown using a reference measure; choose [Pivot views](#pivot-view-authoring) when teams need grouped views of a common loaded base grain. Entry at a subtotal alone does not distinguish them. Input grain, reference-eligible target combinations, partition breakdown and displayed view grain are separate decisions. The supplied deck's standard relational design uses a native reference measure from the same fact as its connected hierarchy; its later cross-fact examples are explicitly enhancement designs, not confirmed shipped capability.

**Business setup:** establish the source pool and period/context, the actual reference measure and its coverage, and the target breakdown before creating the eligible input/forecast. In Enable Multi-Dimension Allocation -> Add Breakdown, choose the reference and semantic dimensions; Manage Breakdown later operates on existing/new partitions with different mutability. Enter the assumption at its natural grain, then review the resulting measure at the configured detail. The screenshot's reference label does not identify its business meaning by itself. A picker accepting a field does not prove a valid same-fact relationship or allocation denominator.

| UI/configuration area | Source-confirmed behavior and dependencies |
| --- | --- |
| Number input eligibility | Creation only; numeric non-hierarchy column, Sum on both axes, at least one Power BI row assignment and three Power BI column assignments. Calculated rows/Promote to measure block this path. The count predicate is not a requirement for literal Year/Quarter/Month names. |
| Reference measures | Creation/Shell management accept native Power BI catalog measures or non-NONE default aggregation; Matrix management uses a weaker truthy-aggregation predicate. No same-fact relationship check was found in these picker predicates. Resolve actual model/driver coverage. |
| Initial and additional breakdowns | Initial Breakdown 1 selects visual grouping dimensions and eligible native references unless restored/locked. Additional breakdowns start with visual column dimensions; creation protects the default breakdown from deletion. Hierarchy selections select descendant IDs, preferring columnId to id. They do not create model relationships. |
| Multiple breakdown validation | Requires a common row dimension; each chosen dimension must occur either once or in every breakdown. Columns become timeDimensions, other selections dimensions. Common Dimension is derived, not a new independent setting. |
| Single-reference discrepancy | Creation displays an exactly-one-reference error but omits that condition from `submitValidation().isValid`. Forecast receives the error string; standalone creation uses isValid. Do not claim uniform single-reference enforcement or exploit the discrepancy to invent supported multi-reference semantics. |
| Manage Breakdown | Existing reference selections/dimensions are read-only; only new breakdown dimensions are editable. Formula breakdown entry is blocked by the inspected Matrix/Shell entrypoints. Deleting a saved breakdown warns of Cube-measure deletion without undo; obtain destructive-change authorization. |
| Management differences | Shell protects the last breakdown and supports deletion-only submission; Matrix lacks that last-breakdown guard and deletion-only enablement branch. Shell's update predicate does not apply the dimension validator to every branch. Validate the actual route, not a single universal dialog contract. |
| Copy series / formulas | Cube copy series requires its feature switch and native Power BI source, and locks the reference to that source. Cube formula and separate closed/open reference options are feature-gated; declared bindings are not proof of universally available UI. |
| Forecast modes | Baseline breakdown supports closed Link to Measure and open Data Input, excluding formulas. The separate-period-measures switch can also allow open linked measures. Non-native period selections can disable/clear breakdowns, with the Data Input/Measure exception in the actual predicate. Preserve existing Data Input defaults unless the supported method transition resets them. |

Evidence: input eligibility/UI, eligibility predicate, CubeBreakDown creation/validation, Matrix management, Shell management, forecast gates.

##### Cube Configuration and Lifecycle

| Owner | Exact fields and distinction |
| --- | --- |
| Creation envelope | `label`, `measure_type`, `data_type`, optional `column_aggregation_type`, `row_aggregation_type`, `description`, `source_measure_id`, and required `multi_dimension_settings`. This is a workflow request, not the final saved measure object. |
| Creation `multi_dimension_settings` | Camel-case `referenceMeasures`, `newPartitions`, `existingPartitions` arrays; optional `visualMeasureIdMapping`, `sourceMeasureId`, `nativeMeasureMapping`, `cubeModel`. The dynamic redesigned dialog sends `cubeModel:"DYNAMIC"`. Reference record: `id,label,type,isNative,aggregationType,dataType`. Partition: `name,dataAssignment:{dimensions,timeDimensions}`. Dimension: `id,label,dataType,type,distinctValueCount?,lookups?`; each lookup is `id,label,dataType,type,distinctValueCount?`. Time dimensions omit count. New creation initializes existingPartitions empty; its declared element type is partition objects, not management's IDs. |
| Management request | `partitionMeasureId`, `referenceMeasures`, `newPartitions:[{name,dimensions,id?}]`, `existingPartitions:number[]`, `deletePartitions:number[]`. Not interchangeable with creation's nested dataAssignment. Resolve current time dimensions through the selected partition/visual route. |
| Saved measure binding | Returned `cube_partition_measure_id` binds DataInput/Forecast/Formula or nested VisualColumn.DataInput. Current DataInput and Forecast records can additionally carry `cube_model:"DYNAMIC"`; Formula has no corresponding cube_model member. The checked-in generated client schemas lag this Rust contract, so native readback is the acceptance boundary. Setup multi_dimension_settings is transient, not stored as that calculated measure's final member. Retain the actual owner's string-ID and permission-field semantics. |
| Number/forecast defaults | Native Number min/max/default remain optional tagged values, not zero; distribute-parent native default false. The Cube forecast creation path explicitly chooses version 1, Sum/Sum, ReadAndEdit, distribution true, bound-to-filter-context true and Forecast display retaining blanks. These are constructor choices, not universal measure defaults or authorization grants. |
| Operational outputs | Job codes observed: 100 Queued, 210 Running, 212 InProgress, 200 Success, 400 Failed. Job IDs, status/error text, synced counts and partition dimensions/time dimensions/cell counts are outputs, not authored settings or a complete lifecycle enum. Legacy management reports succeededPartitionIds/failedPartitions; newer flow reports status/jobIds. |

Sources: native creation request, settings DTO, Shell management DTO, creation controller, forecast constructor, job DTOs.

The native Cube create workflow transforms into the application's versioned visual/data-input API, potentially with Cube polling; it is not a public Fabric item-definition constructor. CubePartitionAPI separates get, manage-dimension, link-visual, resync, resync-measure and delete operations. OneLake forces v2; otherwise the relevant feature switch selects version. This adapter makes measure IDs strings in v2 and numbers in v1, not every nested partition ID. Never round a large ID to satisfy an older adapter; resolve its actual lossless contract. Complete success/polling/readback is required before claiming a created breakdown is usable.

Link-to-visual may return measure identity/aggregation or start polling. Successful resync refreshes the active embedded Matrix; switching sheets detects Cube bindings and requests refreshed values, with separate forecast-range synchronization gates. See link consumer, completion listener, sheet-switch refresh. This does not prove that every partition/view synchronizes instantly or that unsaved browser edits are shared. Internal parquet/jetds paths, contribution maps and NAPI `common_dimension_labels`/`reference_measure_name` arguments are execution details, not authorable Cube properties; see manage-breakdown binding.

##### Cube Business Examples and Boundaries

The following numerical fixtures express explicit allocation policies. They are not native execution results or automatic choices of driver, scope, zero handling or redistribution.

| Example | Input and driver | Expected reconciliation |
| --- | --- | --- |
| Regional training | Pool 120 thousand; eligible department FTE 50/30/20 within Region x Month | Allocations 60/36/24; total 120. Missing driver support needs an explicit policy, not invented employee rows. |
| Freight and handling | North pools 50/20, South pools 40/30; kg shares North 80/20 and South 20/80; order-line shares 20/80 in each center | Freight 40/10/8/32, handling 4/16/6/24; combined 44/26/14/56, total 140. Normalize each pool within its own center/month, not globally. |
| Cost-to-serve result | Revenue 200/200/150/250, direct cost 120/130/90/150, service cost 44/26/14/56 | Contribution 36/44/46/44, total 170 on revenue 800; aggregate margin 21.25%, not the average of displayed margins. |

For freight versus handling, separate drivers preserve operational differences even where revenues are equal. Each pool's identity, period, currency, eligibility and driver must remain traceable. Rates/ratios and reference refresh require their own semantics; do not repeat a coarse native amount across detailed combinations and sum the duplicates. Current UI reference eligibility alone does not certify relationships or an allocation policy.

**Cross-fact enhancement designs, not shipped acceptance:** the deck's airline example maps a fleet/month maintenance pool 400 to eligible operated flight legs by block hours 50/30, yielding route totals 250/150. Within each leg, passenger-km determines cabin shares; the simplified consistent 20/80 mix yields 50/200/30/120. With revenue 300/500/200/400 and fuel 40/160/24/96, contribution is 210/140/146/184, total 680. Raising maintenance to 480 produces 60/240/36/144 and total contribution 600. Preserve the leg-level normalization before route aggregation; do not allocate the original pool independently at both stages and double-count it.

The reverse-attribution design separately maps route revenue 800/600 by crew-duty shares 60/40 and 20/80 to East/West totals 600/800. This is alternative management attribution, not another cost deduction or revenue-recognition rule. Cloud chargeback, university program funding and warranty-reserve variants likewise require valid source-to-target keys, periods, scope, policy and reference coverage. Materializing columns into a wide file does not establish those semantics. No current-source finding here certifies end-to-end cross-fact enhancement availability.

Acceptance must cover compatible reference/model dimensions, common-row and per-breakdown constraints, missing/zero/negative drivers and new targets, type/aggregation/forecast eligibility, per-pool conservation, rounding, affected versus unaffected context and restricted-user access. On authorized resources verify creation/job completion, link/refresh, input change propagation, resync, failures and destructive deletion boundaries. Backend relationship enforcement, full setup-to-partition orchestration, cross-environment ID remapping, ALM restoration and saved-input retention remain unverified. Do not create or delete Cube resources merely to learn this deck.

#### Forecast period and time-extension authoring correction

For new native Forecast authoring, use the normalized ISO labels and epoch-second
UTC boundaries in [forecast-authoring.md](forecast-authoring.md#forecast-period-configuration-iso-labels-and-utc-boundaries).
The UI-saved contract supplies both optional UTC companions. Decoder optionality
below does not justify leaving them out of an authored forecast.

##### Time extension under Forecast

Date-axis before/after differences belong here. Derive one role per actual column
level; preserve Year-only, Year/Quarter and other supported chosen hierarchies. Do
not add levels to imitate the sample. Explicit `columnTimeLevels` maps custom
field names and destination-native units; see the dynamic-granularity section in
`forecast-authoring.md`. The metadata location is: `visualState.columnDimensions`
uses `isTimeDimension:true` and the matching `timeIntervalUnit` for each Year,
Quarter and Month level. Preserve real field identities and hierarchy order.
See [the time-extension contract](forecast-authoring.md#forecast---time-extension-date-axis-metadata).
These observed corrections do not, by themselves, prove grid rendering or calculation.

#### Native Forecast Decoder

The Rust ForecastConfig is a separate native contract, nested under the externally tagged `MeasureType::Forecast` variant. These declarations close native fields/variants, not a complete exported column or API request.

| Native member | Exact type / presence behavior |
| --- | --- |
| `forecast_version` | `f64`, serde default; not declared integer-only and not a lock flag. |
| `forecast_period` | Defaulted `ForecastColumnRange`: defaulted string `start`/`end`, optional `u64` `start_utc`/`end_utc`. No timestamp unit or time-zone conversion is defined in this struct. |
| `closed_period_till` | Defaulted optional string. |
| `auto_close_forecast_settings` | Defaulted optional object; members `auto_close_by`, `calendar_close_value`, `workday_close_value` are defaulted `u32`; `extend_range` is `Extended` or `None`, default `Extended`. Numeric control meanings require their consumers. |
| `forecast_value_display` | Defaulted optional enum: unit `Actual` or `Forecast { forecast_value_retain_blanks: bool }`. The enum's default `Actual` does not change an omitted Option into `Some(Actual)`. |
| `open_period_config`, `closed_period_config` | Defaulted optional `ForecastPeriodConfig`, whose defaulted `method` is an externally tagged `ForecastMethod`. |
| `forecast_allowed_user_permissions`, `disable_write_access` | Both `skip_deserializing`; defaults true and false respectively. Serialized flags are not portable instructions to grant/revoke access. |
| `edit_config`, `cube_partition_measure_id` | Defaulted optional edit object/string, omitted from serialization when None; edit-object members are described below. |
| `bound_to_filter_context` | Defaulted true, independently of the permission flags. |

ForecastEditConfig has defaulted optional `aggregate_total`, `allow_input: AllowInputType`, `on_change_formula: String`, `number_column_metadata: NumberColumnMetadata`. AggregateTotal is `AllPeriods` (enum default), `ClosedPeriods`, `OpenPeriods`; an omitted aggregate_total Option remains None. This is not the DataInputConfig envelope or proof of user permission.

ForecastMethod and defaults distinguish `Formula(String)`, `DataInput(DefaultValueType)` and `LinkToMeasure(Id)`; method default is `Formula("")`. The nested `DefaultValueType` is `Formula(String)`, `Measure(Id)`, `StaticValue(f64)`, unit `Blank` (enum default), or `Row(String)`. Do not substitute the Number input's `Static` tag for Forecast's `StaticValue`, or replace an optional period configuration with a guessed blank/default method.

ForecastCopyMethod separately declares `PeriodRange`, `SinglePeriod`, `AveragePeriodRange` (each carrying `SourcePeriodRange`) and unit `ImportFromFile`. Source ranges include a `StringPeriodRange` and `source_measure_id: Id`; target configuration contains optional copy method and target range. These copy variants are not additional ForecastMethod variants.

The current [published Forecast table](https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/definitions/plan-definition#forecastmeasure) declares required integer forecast_version, numeric period boundaries, and string display mode with a separate retain-blanks flag. The native decoder above instead permits f64, string boundaries with optional UTC companions, and a tagged Forecast display payload. Keep this discrepancy version-bound; do not coerce or flatten native fields to satisfy the public table without the actual route conversion.

**Remaining gap:** native enum/presence semantics and Id decoding above are inspected; full column/request construction, range/period conversion, cube/edit/auto-close consumers, public/native conflicts and route-specific export/import restoration still require closure. No formula, file-import or runtime forecast behavior is certified by these declarations.

For paired textual/numeric period boundaries, verify timestamp units, time zone, interval inclusivity and conversion through the actual writer/reader. Do not assume the representations are identical instants, silently repair a discrepancy or infer seconds versus milliseconds from an example; keep the affected construction blocked until the conversion is resolved.

#### Mandatory Forecast Date Hierarchy

**Functional prerequisite, not a layout recommendation:** every Planning sheet containing a native Forecast Measure must have a nonempty, valid date hierarchy in the **Columns bucket**, consisting exclusively of supported date levels. Even one non-date dimension mixed into Columns is invalid. Region, Product, Account, Department, Scenario and Version belong in appropriate Rows or supported filters/context, never alongside forecast date columns. A valid date hierarchy in Rows, a chronological label, or a chart date axis does not satisfy this Columns requirement. This is especially important when extending the Forecast Measure into future months, quarters or years: the engine needs recognized period identities and parent context, not merely sortable text.

**Mandatory default for forecasting intent:** detect forecasting, forecast planning, future-period projections and extension of the planning horizon from the user's request. Automatically assign **Year -> Quarter -> Month** to Columns on each forecast planning sheet, mapped to actual date-hierarchy fields in the supplied semantic model. Do not ask the user to choose a hierarchy for an ordinary forecast request. Use a different supported hierarchy only when the user explicitly requests that hierarchy or different date granularity; a weekly request is an explicit granularity choice. Do not evade this default by implementing a forecast as formulas/inputs instead of a native Forecast Measure. The native Forecast-specific gate also applies whenever that measure exists, regardless of the request's wording.

Resolve model fields, date relationships, types, label formats, chronological sorting and fiscal/calendar meaning before constructing assignments. Missing Year/Quarter/Month fields are not permission to invent bindings, silently use YearMonth as a substitute, or provision/change the semantic model. Resolve a supported date hierarchy through the authorized model/authoring route; if it is unavailable, report the exact missing prerequisite and withhold the affected forecast payload. This default does not choose the forecast horizon, forecast values, scenario or business grain.

| User request | Required default or explicit alternative |
| --- | --- |
| Create a sales forecasting sheet | Year -> Quarter -> Month |
| Forecast revenue for the next 12 months | Year -> Quarter -> Month |
| Build an expense forecasting model | Year -> Quarter -> Month |
| Extend my financial plan into 2028 | Year -> Quarter -> Month |
| Create a weekly demand forecast | Year -> Week, after validating model week/year semantics |
| Use Year and Month for this forecast | Year -> Month, explicitly requested and validated |

##### Supported Date Hierarchies and Labels

Authority: the user-supplied **RS Time Intelligence Date Hierarchy Guide**, reviewed 2026-11-10, particularly Supported Hierarchy Patterns, Supported Formats, Accepted Date Strings and Supported Composite Formats. The following in-library reference retains its supported combinations and recognition constraints so future authoring does not depend on a workstation Downloads path. The mandatory Forecast Columns/default policy above comes from the user's explicit requirement; the guide describes date recognition, not a new native assignment DTO or proof that a particular deployed Forecast extension was exercised.

| Supported hierarchy | Selection rule |
| --- | --- |
| Year | Explicit annual granularity |
| Year -> Half Year | Explicit half-year granularity |
| Year -> Quarter | Explicit quarterly granularity |
| Year -> Month | Explicit alternative monthly hierarchy |
| Year -> Week | Explicit weekly granularity |
| Year -> Half Year -> Quarter | Explicit documented alternative |
| Year -> Half Year -> Month | Explicit documented alternative |
| Year -> Half Year -> Week | Explicit documented alternative |
| Year -> Quarter -> Month | Mandatory default for forecasting intent |
| Year -> Quarter -> Week | Explicit documented alternative |
| Year -> Month -> Week | Explicit documented alternative; verify actual parent-period membership |
| Year -> Month -> Day | Explicit daily granularity |
| Year -> Week -> Day | Explicit daily granularity with week context |
| Year -> Quarter -> Month -> Day | Explicit daily granularity |
| Standalone full-date Day | Explicit daily granularity; each value identifies a full date |

Do not infer that every permutation or subset of the six levels is supported. In particular Quarter -> Year, Month -> Quarter, Day -> Month, Day -> Year and Week -> Month are invalid orderings. The guide notes that a Day directly under Quarter or Half Year is relative to that parent's start; that note is not a reason to invent an additional supported default. Prefer the documented daily hierarchies with Month before Day when daily granularity is requested.

Recognition precedence is explicit time-level/format configuration, then field-name keywords, then member values. Recognized field-name keywords include Year, Yr, Half Year, Half, Quarter, Qtr, Month, Week and Day. Numeric labels alone are ambiguous: `1` can describe several levels, and a numeric non-date business key is not a date level. Verify the resolved level and inherited parent context rather than accepting a name/type-only heuristic.

| Level | Accepted labels and ranges from the guide | Invalid examples |
| --- | --- | --- |
| Year | Two/four digits; FY prefix with/without a space, such as `25`, `2025`, `FY25`, `FY 2025`; two digits use the current century | `22-23`, `2025-2026`, `FY2A` |
| Half Year | `1`, `2`, `01`, `02`, `H1`, `H2` | `3`, `H3`, `First Half`, `Half 1` |
| Quarter | 1-4, zero-padded numbers, Q prefix, Qtr prefix with/without space, Quarter with space; accepted keywords also include `Qtr_1`, `Qtr-1`, `Quarter_1` through 4 | `Q0`, `Q5`, `Quarter 5` |
| Month | 1-12, zero-padded numbers, standard three-letter or full English month names; use `Sep` or `September` | `0`, `13`, `Sept` |
| Week | 1-53, zero-padded numbers, W prefix, Week plus space; accepted keywords also include `Week_1` through `Week_53` | `0`, `54`, `WK1` |
| Day | 1-31 with parent context, or `YYYY-MM-DD`, `YYYY-MM-DD 00:00:00`, `YYYY-MM-DDT00:00:00` | `0`, `32`, `01/02/2025`, `Feb 1, 2025`, `01-Feb-2025` |

Formats are case-insensitive, but members within one field must use a consistent format: do not mix `Jan` and `1`, or `Q1` and `Quarter 1`. Validate real calendar dates and the selected year's week rules as well as numeric ranges. Prefer four-digit years for unambiguous century selection. An FY label does not itself configure fiscal-year boundaries; retain the separate F10 contract.

Composite `Q1-FY24`/`Q1 FY 24` and full ISO dates are documented only with a matching label-format mapping, consistent structure and at most one value per level; ranges are invalid. Prefer separate date levels. A standalone `YearMonth` field or `2026-11` label is not established by this guide as a replacement for the mandatory default; verify an explicitly requested alternative through its documented mapping rather than assuming recognition.

| Candidate configuration | Validation result and correction |
| --- | --- |
| Columns Year -> Quarter -> Month; Region in Rows | Valid default when fields, labels and period coverage resolve |
| Columns Year -> Week for an explicit weekly forecast | Valid documented alternative when week/year context resolves |
| Columns Year -> Quarter -> Month -> Product | Invalid even though the date prefix is valid; move Product to Rows or appropriate filter/context |
| Columns Scenario -> Year -> Month | Invalid mixed date/business dimensions; keep Scenario in supported persistence context, not Columns |
| Date hierarchy only in Rows; Columns empty | Invalid for a Forecast Measure; assign the validated date hierarchy to Columns |
| Columns Quarter -> Year or Week -> Month | Invalid ordering; rebuild the requested supported broad-to-granular hierarchy |
| New forecast with unspecified granularity and no existing hierarchy | Default to Year -> Quarter -> Month; preserve an explicitly chosen or existing supported hierarchy |
| Columns Year -> Quarter -> Month with Q5, Sept or mixed month styles | Invalid members; correct through an authorized format/mapping route and revalidate |

##### Forecast Pre-Publication Gate

1. Detect forecasting intent and native Forecast Measures separately. Record the selected default or the user's explicit alternative; include the governing guide section and actual semantic-model field mappings.
2. Inspect every effective Columns assignment and expanded hierarchy level on each affected Planning owner, including saved pivots/bookmarks that can restore a different assignment. Reject empty Columns, any non-date dimension, unrecognized levels and invalid ordering. A collapsed display must not hide an invalid assignment from this check.
3. Validate the entire ordered hierarchy against the supported table, not just individual levels. For the default, require Year, Quarter and Month in that order. Check actual member labels, consistent formats, unique period meaning, chronological sorting and explicit mappings where necessary.
4. Validate the requested future horizon, parent-period identities, period boundaries and available or supported generated future members through the selected Forecast writer. Date recognition alone does not prove that future periods can be extended; do not fabricate model rows, timestamps or a forecast baseline. Retain the existing timezone, default-source and open/closed-period checks.
5. Correct invalid assignments before generation/publication: move business dimensions to the appropriate Rows/context, restore the documented ordering, resolve valid labels/mappings, then rebuild dependent assignments and re-run checks. For existing artifacts, preserve saved-input identities and context; a change in coordinate keys requires the existing migration safeguards, not a silent move/reset.
6. Withhold an affected forecast payload while any mandatory prerequisite is unresolved. Record the failed field/level, reason and corrective action; do not downgrade the rule to a warning or replace Forecast with a decorative/static substitute.
7. After an eligible save, verify the saved Columns mappings and, where native access permits, initialization, chronological expansion into the requested future periods, period calculations and open/closed editing behavior. Report unperformed runtime checks separately; JSON/API success is not functional acceptance. The supplied initialization-failure screenshot does not establish a date-hierarchy root cause by itself.

#### Rolling Forecast Authoring

Use a Forecast measure for a single series combining closed history and open forecast periods. The common actuals-to-date plus editable remaining-plan pattern is configured through Model -> Forecast rather than recreated with separate formulas and manual history locks. Select the historical source and open-period behavior deliberately; a rolling forecast is not inherently a statistical prediction, scheduled monthly rollover, snapshot or archived business submission.

The supplied rolling-forecast guide reports a successful November 10, 2026 definition export and five screenshots, with no interactive edit/refresh/save-reopen tests. Its embedded configuration is historical reported evidence, not a fresh export performed here. The separately linked evidence JSON and images were not supplied for independent inspection in this update. Its sample links both closed history and editable open defaults to a Plan measure, not to Actuals. Resource identities, sample dates, Sum/Sum aggregation and permission settings are not reusable defaults. Existing source-backed [native variants](#native-forecast-decoder) remain established at their inspected layer even where that single sample did not exercise them; resolve only a required construction gap rather than demanding a new live export for every already-covered variant.

##### Forecast Modes and Defaults

The selected Forecast Period establishes the open range. In an illustrative November-December range, January-October is closed history; the computer date alone does not choose or advance that boundary. Closed forecast cells display the configured link or formula and are unavailable for direct entry. This does not freeze the source ledger: corrected actuals may change the linked display after the applicable refresh.

The following mode matrix describes the supplied functional design. `true` means that the mode permits direct input, still subject to effective access, period eligibility and other restrictions; it is not an authorization grant:

| Period class | Mode | Data Input default | Direct entry eligible by mode |
| --- | --- | --- | --- |
| Closed | Link to Measure | Not applicable | false |
| Closed | Formula | Not applicable | false |
| Open | Data Input | Static | true |
| Open | Data Input | Measure | true |
| Open | Data Input | Formula | true |
| Open | Data Input | None | true |
| Open | Link to Measure | Not applicable | false |
| Open | Formula | Not applicable | false |

Data Input defaults provide a starting position: Static supplies a constant at each applicable intersection, Measure supplies the selected source's corresponding period/context value, Formula supplies a calculated default, and None starts blank. A per-intersection constant is not a department total. A blank source is not zero, and actuals ending in October cannot automatically supply November or shift last year's values into next year. Use an appropriate future-period source or a separately supported period-shift/prefill process.

Distinguish Data Input -> Measure from the top-level Link to Measure mode, and Data Input -> Formula from the top-level Formula mode. The former allow planner overrides; the latter display linked/calculated results without direct override of that forecast cell. For an entirely driver-led result, change the drivers rather than converting the calculated result into editable input unintentionally.

**Current authoring policy:** a business request for forecasting selects this native Forecast feature. Closed periods link to the relevant actuals measure, resolving its DAX meaning where available. Open periods use the requested source/formula; if unspecified, use Data Input -> None (`{"DataInput":"Blank"}`), not invented growth or zero. The user-confirmed formula `COLUMN.ADDMONTH(-1) * 1.1` takes the prior month: the first open month anchors to the preceding closed actual, and later months compound from their preceding forecast month. Missing anchor values are not zero. Saved settings and calculated runtime results remain separate evidence. The self-contained constructor, complete record companions and API acceptance sequence are in [forecast-authoring.md](forecast-authoring.md); no external repository or prior report is needed for this route.

##### Forecast Wizard and Authoring Sequence

1. In Editing mode, apply the [mandatory Forecast date hierarchy](#mandatory-forecast-date-hierarchy): default Columns to Year -> Quarter -> Month, or validate the user's explicit supported alternative, with no non-date Columns dimensions. Resolve the business grain and add the actual history and future-default sources needed for this request, checking their period/context coverage and units.
2. Open Model -> Forecast, set a meaningful measure name and the intended open range. The supplied guide covers a single forecast; the visible Multi Forecast control does not establish that feature's construction or behavior.
3. Configure Closed Periods using Link to Measure or Formula. For actuals-to-date, resolve the actual business Actuals source. A Plan source is valid when intended, but does not become actuals because a role or display enum says Actual.
4. Configure Open Periods. Choose Data Input plus its default for judgmental edits, or top-level Link to Measure/Formula for a read-only result. Check the actual future-period baseline rather than assuming carry-forward.
5. Save through the supported route and review historical and open cells alongside their sources. Identical starting numbers can have different editability. Preserve identity, source assignments, context, time metadata and existing inputs during updates; do not rebuild an unrelated measure or copy a sample configuration wholesale.
6. Verify saved settings, then native entry and source/override behavior on authorized test resources. The reported wizard says defaults fill when the range changes, but the guide does not establish existing override retention or precedence under range changes, source refresh and reforecast. Inspect those behaviors before automating a rollout; do not silently reseed user entries.

##### Reported Forecast Shape and Source Resolution

Locate the owning visual from the sheet/visual registry and select its `dataInput.json.columns[]` entry by exact identity, not array position or label alone. Verify `columnMeta.measure_type.Forecast` before reading a forecast method; the reported `dataInputType: 6` numeric code alone is not a sufficient discriminator. Branch on the actual method before accessing method-specific members.

| Reported saved field | Interpretation and required check |
| --- | --- |
| `columns[].measureGuid`, `columnMeta.id` | Reconcile the owning forecast identity and registration; retain decimal strings losslessly. |
| `closed_period_config.method.LinkToMeasure` | Resolve this identity to its source column and, for the observed native source, the owning `properties.pivotAssignments[].measureGuid` and semantic field. This establishes Plan versus Actuals, not the label alone. |
| `open_period_config.method.DataInput.Measure` | Editable measure-default strategy in the supplied sample; separate from a top-level LinkToMeasure method. |
| `edit_config.number_column_metadata.default_value` | Null in that sample despite its selected Measure default. Changing this metadata field is not equivalent to changing the open-period strategy. |
| `forecast_value_display: "Actual"`, source `measure_role: "ACMeasure"` | Both coexist with a business Plan source in the guide. Neither identifies the business content of the linked measure. |
| `closed_period_till: null` | No additional cutoff configured; does not remove history established by the start of the selected open range. |
| `auto_close_forecast_settings: null` | No configured rollover automation demonstrated by this sample. The word rolling does not establish a scheduler. |
| `edit_config.allow_input: "ReadAndEdit"` | Does not reopen closed periods or bypass actual permission checks. The native permission/write-disable fields retain the skip-deserialization limits documented above. |
| `manage_measures`, time dimensions and measure aggregation | Reconcile visibility/order, recognized time hierarchy and both aggregation axes. The observed forecast is not an extra native Power BI pivot assignment; do not invent one or a Cube partition merely to register it. |

Synthetic source identities below stand for already-resolved Actuals and Budget measures respectively. This illustrates only the two method subtrees, not a complete Forecast object, column or update payload:

```json
{
	"closed_period_config": {
		"method": { "LinkToMeasure": "9007199254740993" }
	},
	"open_period_config": {
		"method": { "DataInput": { "Measure": "9007199254740994" } }
	}
}
```

Preserve the distinction between Forecast's native `StaticValue`/`Blank` default variants and the Number input metadata union; a UI label None does not authorize emitting JSON null or omitting an arbitrary member. The exact route conversion still matters. The guide's reported numeric range values decode as Unix seconds at offsets different from the ISO midnight strings and are consistent with a daylight-saving-aware local-day interpretation. That observation does not establish the target report's time zone or the writer's universal convention. Preserve both representations for unchanged ranges; resolve units, zone, inclusivity and conversion before changing boundaries rather than deriving one directly from the other.

##### Forecast Business Examples

These are synthetic additive-currency examples in thousands, using two remaining open months. The closed totals are history, not editable future inputs. Rates and percentages require their own aggregation rather than inheriting Sum/Sum.

| Scenario | Closed history | Open month 1 | Open month 2 | Full-year estimate |
| --- | --- | --- | --- | --- |
| Revenue before adjustments | 1000 | 120 | 130 | 1250 |
| Revenue after adjustments | 1000 | 125 | 138 | 1263 |
| Expense before adjustments | 800 | 90 | 100 | 990 |
| Expense after adjustments | 800 | 85 | 80 | 965 |
| Payroll before adjustments | 5000 | 500 | 510 | 6010 |
| Payroll after adjustments | 5000 | 490 | 500 | 5990 |

- Revenue at Region x Product x Channel x Month: use Revenue Actuals for history and Data Input -> Revenue Budget for the future. The revised 1263 is 37 below a 1300 annual budget, without reopening history.
- Expense at Department x Expense Account x Region x Month: use posted actuals and budget defaults. Reducing the remaining months from 190 to 165 reduces the estimate by 25, to 965. Use None for genuinely blank submissions or Static only at a suitable recurring-input grain.
- Payroll at Department x Employee Group x Region x Month: a Data Input formula default uses planned headcounts 100 and 102 times loaded monthly cost 5, yielding 500 and 510. Hiring adjustments yield 490 and 500, for a 5990 full-year estimate. Employee-level proration and hire-date phasing need explicit sources/calculations. Choose top-level Formula instead when the result must remain entirely driver-controlled.

##### Forecast Acceptance and Troubleshooting

**Must:** distinguish saved configuration, source meaning, period eligibility and effective editing; retain unrelated properties and override identities. **Prefer:** the native Forecast composition for the basic closed-history/open-plan pattern. **Avoid:** extra manual locks solely to reproduce that boundary, invented predictive behavior, automatic rollover/snapshot claims, or treating the technical forecast version as evidence of an archived business revision. Additional approval, scenario and security controls remain separate where requested.

Static checks cover method variants, lossless identities and source resolution, actual future source coverage, period/time metadata, formula/default dependencies, registration and aggregation. Use the existing [Plan lifecycle](#plan-item-lifecycle) for definition retrieval, attribution and LRO handling rather than replaying credentials or private sample endpoints. On an authorized implementation, export/read back and test:

- Historical display against its actual selected source, and attempted entry into a closed period.
- An eligible Data Input cell's default, a distinctive override, save/reopen, blank-source and None-default behavior, and input-context isolation.
- Formula default versus top-level Formula, and Measure default versus top-level Link to Measure, including their different entry behavior.
- Source refresh and range advancement separately: linked display, newly eligible defaults, earlier overrides and newly closed values. Never infer precedence or overwrite retention from a successful export.
- Leaf/subtotal/grand-total aggregation, parent distribution into eligible versus closed/locked descendants, and restricted-user access.

If history displays budget, resolve its closed-source identity. If future values are read-only, inspect the open mode and effective restrictions. If defaults are blank, inspect the matching target period/context before adding a carry-forward rule. If numeric metadata edits have no effect, inspect the actual DataInput default branch. If a month does not close automatically, inspect real auto-close/reforecast configuration. Keep native results separate from local arithmetic; no live Plan/source writes or forecast execution are authorized merely by learning this guide.

### F14 Formatting

Intent: format cells, rows, columns, measures, dimensions, and groups. formatConfig binds to `inforiverProps.formatConfig`.

| Native container | Initial shape |
| --- | --- |
| `row`, `column`, `cell`, `measure` | Empty ID-keyed maps. |
| `columnDimension`, `rowDimension` | Empty dimension-keyed maps. |
| `labelCellGroup`, `rowGroup` | Empty group-keyed maps. |
| `rowMemberInDimension`, `columnMemberInDimension`, `columnHierarchy` | Empty maps; key grammar requires the producer. |
| `formatSize`, `__lastHouseKeepedSize` | Initial numeric counters 0; not automatically user-authored ALM properties. |

FORMAT_MAP associates symbolic keys with boolean font flags, numeric font size/indent/decimals, string colors/font family/prefix/suffix, and structured border/chart properties. The enum's actual string/numeric wire keys must be inspected before emitting them; friendly names like `backgroundColor` are not substitutes. Scenario-copy logic clones/rekeys selected entries. **ALM gap:** property-key serialization, ID grammar, every structured style member, and import preservation remain partial.

The inspected client FormatProperty declaration maps font family to `4`, background color to `5`, suffix to `9`, percentage to `10`, decimal places to `11`, and scaling factor to `13`. Supplied measure-format records illustrate an ID-keyed `measure` map whose values are ordered arrays of `{format, order}`; numeric property keys appear as JSON strings. This closes those selected key identities, not every formatting value or the enclosing import contract. Keep percentage-point inputs distinct from fractional calculated ratios, and unit assumptions distinct from additive amounts; choose percentage/scaling semantics from those units and verify the display rather than globally applying amount formatting.

#### Grid Appearance Authoring

**Business workflow:** keep a product group readable across twelve months using eligible alternate shading or hover, restrained period/header boundaries and meaningful forecast/locked-cell styling. Choose grid, container or page controls according to the intended scope. The supplied orange/blue row colors, gray grid and colored minor lines demonstrate configurability, not recommended defaults. A saved line color does not enable its line. Preserve actual [Column Style precedence](#column-style-authoring), not an assumption that alternate-row color always wins.

| Scope | Owner and persisted/client state | Does not mean |
| --- | --- | --- |
| Table cells and labels | Matrix `globalStyles`, `themeColors`, `gridStyles`, scoped `formatConfig` and row/dimension sizes | The Shell visual container background or the whole page. |
| Visual container | Selected visual `properties.visualStyles`: background, border, padding, shadow, corners, rotation and host tooltip | A number-format/Column Style object for grid cells. |
| Page/canvas and wallpaper | Owning entity `properties.canvasStyle`: page background, wallpaper, geometry and layout guides | Matrix major/minor gridlines or a semantic model property. |

The Matrix mapper changes only outer native names (`grid_styles`, `theme_colors`, `global_styles`) to client names; preserve leaf spellings and the actual host save representation. The host hydrator shallow-merges saved objects over defaults; template/theme changes and renderer fallbacks are separate. Do not copy UI initialization wholesale over a configured visual.

##### Typography, Dimensions and Direct Formatting

| Matrix owner/keys | Frontend initialization or supported scope |
| --- | --- |
| `globalStyles.fontFamily`, `fontSize`, `fontWeight`, `fontStyle`, `textColor` | Segoe UI fallback stack; string 14, normal, normal, #333333. Actual selected formatting can override them; do not confuse text-size strings with column-width numbers. |
| `hierarchyfontWeight`, `hierarchyFontStyle`, `columnHierarchyFontWeight`, `columnHierarchyFontStyle`, `subTotalFontWeight` | bold / normal / normal / normal / semiBold. Preserve the lowercase f in hierarchyfontWeight. |
| `headerFormat`, `headerHeight`, `headerFontSize`, `headerFontColor`, `headerLabelOrient` | false / 30 / string 14px / #333333 / initial. Orientation choices initial, bottomRight, top, topRight. |
| `isHeightUpdatedManually`, `showRowLabelEditor`, `variableColor` | false / false / #0078D4. Manual-sizing state is separate from row heights. |
| `blankRowLabel`, `blankColumnLabel`, `columnStyle` | Unset in the global initializer; absence does not materialize a preset style. |
| Other global presentation/meta | `varianceBarFont=12`, `kpiFontSize=45`, `chartScale=IntegratedChartsScale.UNIVERSAL`; migrationVersion unset. These belong to their own presentation consumers, not universal grid font settings. |
| `row_height_config` | `default_row_height=26`, `sub_total_row_height=26`, native root ID `16017913890930171270` in `custom_row_height` at 26, `row_level_height=[]`. The native request fields are unsigned 32-bit integers, so the formatter rejects fractional row/subtotal heights while preserving explicit existing maps. The inspected owner is not `globalStyles.rowHeight`; the bundled new-Planning constructor now emits this complete frontend seed instead of replacing the root map with `{}`. |
| Scoped `formatConfig` | Existing row/column/cell/measure/dimension/member/hierarchy maps hold ordered operations for bold, italics, underline, strike-through, font family/size/color/background, alignment/orientation/indent, numeric formats and borders/line decorations. Resolve actual enum wire keys and selection identity, not arbitrary CSS properties. Applicable operations are sorted by order; no blanket cell-over-row precedence is established. |

Sources: global initialization, row-height initialization, format type map, operation reader. Row/label/column dimensions, autosizing and per-level settings must follow their owning layout paths; number-format precision and a visual's responsive container do not imply fixed column widths.

`layoutSizes` is initialized to an empty object, not universal pixel sizes. Its typed fields are numeric tableWidth/chartWidth/labelWidth/bulletWidth, optional maximumChartWidth, optional isResponsive/isResizeAllowed/isMaximumChartWidthAllowed, and preferedWidthSelection with measure/column choices. Preserve that spelling. Width/responsive actions trigger column-resize lifecycle work; updateLayoutWidth merges fields, whereas update replaces the object when truthy. Common Measure Width selects measure versus column, applying resizing across a measure's columns; it is hidden for Table builds. See the width store. Runtime-computed widths and autosizing are not portable fixed defaults established by the empty initializer.

Tree `node_dimensions` is another owner, not table row height or label width. Native schema has scope Global/Level and nested node_dimensions with optional global and level maps; each dimension record contains string id and numeric width/height. Missing native record fields default to empty ID/zero sizes. The frontend initializer/resolver starts with Global and an empty nested object, then uses a 240-by-75 ordinary-Tree fallback (decomposition tree is separate). Nullish fallback preserves explicit zero. Frontend edits merge scoped metadata; native update replaces the whole object and reset restores the empty frontend state. Preserve other levels and distinguish these defaults from a valid rendered dimension.

`tree_data_label` is separate persisted presentation state. Its label-format
map has `category`, `value` and `percentage`; each entry has font
style/weight, optional font size/color, `position:top|bottom` and
`isFontSizeCustomized`. The flag prevents later global decomposition-tree font
updates from overwriting an explicitly sized part. Decomposition metadata holds
display `all|none`, selected label types, inline/separator configuration and child
count; variance separately controls display, `none|relative|absolute` and
semantic color, while KPI font fields remain their own object. Missing
font-size/color values intentionally fall back to tree/global typography rather
than representing `0` or an empty color. The skill preserves this state in
scoped repairs but does not claim a portable Tree visual authoring factory.

##### Row Highlight and Gridlines

| Matrix setting | Supported values, initial state and behavior |
| --- | --- |
| `themeColors.enableRowHover` | Initial rowAlternate; wires rowHover, rowAlternate, rowAlternateContrast, rowAlternateFlashy, off. This is a mode string, not a Boolean despite the name. |
| `rowHoverColor`, `rowHoverTextColor`, `rowOddColor`, `rowEvenColor` | #fafafa / #212121 / #F5F5F5 / #FFFFFF. Hover pickers are shown for rowHover; odd/even pickers and measure-only control for alternate modes. |
| `measureOnlyHighlight` | Initially false. True excludes label cells from alternating shading and restores their normal text-color path; it does not select only rows that contain measures. |
| Other `themeColors` fields | positiveColor #82BA00, negativeColor #FF000A, enableVarianceColor/invertVarianceColor false; chartTheme/themeType/previousThemeType trafficlights, tableThemeType false, valueColor/lineStyleRecentColor empty, migrationVersion unset. Preserve separately scoped chart/variance choices rather than treating them as alternate-row colors. |
| `gridStyles.majorGridLines`, `majorGridColor` | off initially; single/double/off; #A6A6A6. |
| `horizontalMinorGridLines`, `horizontalMinorGridColor` | solid initially; solid/dotted/off; #E6E6E6. |
| `verticalMinorGridLines`, `verticalMinorGridColor` | solid initially; solid/off; #E6E6E6. Do not invent a dashed vertical option from the border-style enum. |
| `headerGridLines` | Initially true, sharing horizontalMinorGridColor. Separate from Skip Lines. |
| `compactSplitLine`, `compactSplitLineColor` | true / #A6A6A6, separate compact-outline separator settings. |
| `gridBorderLineColor`, `gridBorderLineWidth`, `gridBorderLineStyle`, `gridBorderLinePosition` | #A6A6A6 / 0 / solid / null. Styles solid/dotted/dashed/none/solidDouble/solidThrice; numeric side values are distinct from styles. No positions means no explicit border. Missing width falls back to 1; explicit zero stays zero. |
| `chartSpacing`, `topSpace`, `bottomSpace`, `leftSpace`, `rightSpace`, `titleAndChartSpace`, `indentSpacing` | true; four outer spaces 0; title/chart space 4; indent 10. These are grid/content spacing, not Shell container padding. |
| `columnSpacing`, `columnSpacingValue` | off / 5; modes auto/on/off. Value control 0-20 appears for on, but zero/null updates retain the prior value. Auto appears only for IBCS in that settings control. |
| Other `gridStyles` | lineStyleColor #666666, lineStyleFormat solid; enableCategoryLabelColor false, categoryLabelColor #DDDDDD; showVAHighlight true, isLevelIndent false; showExpandCollapse true, showColumnExpandCollapse false; gridBackground #FFFFFF; direction ltr, with ltr/rtl choices; migrationVersion unset. |
| **Skip Lines: `chartSettings.gridLineCount`** | Separate binding, initial 1, numeric handler range 0-50. Reader uses sibling index modulo count, enables nonleaf rows and forces 1 for Excel. It is not columnSpacing, headerGridLines or a new gridStyles key. |

Sources: theme initialization, grid initialization, label highlight reader, Skip Lines binding, Skip Lines rendering, gridline modal. General settings hide Skip Lines for horizontal-Off/Excel, while its toolbar modal lacks those visibility gates. General header toggle is Default-template-only; vertical-line controls exclude Financial/IBCS in the inspected route. Keep stored settings, UI availability and rendering effects distinct.

##### Selection, Indicators and Ruler

The captured uiSettings object includes presentation controls and interaction state. The owner merges updates through the controller; do not replace the object with only a changed flag. Defaults below are the inspected initializer, not an instruction to reset the captured values.

| `uiSettings` field | Default, control and actual effect |
| --- | --- |
| `aggregateOption` | Boolean sum/avg/count true, min/max false. Status Panel Aggregation limits selection to three options and drives footer selection statistics, not totals_config or a measure's aggregation method. |
| `scrollThickness`, `customScroll` | Both false. Increase Scroll Thickness is hidden with custom scrolling; changing Custom Scroll writes scrollThickness false. Rendering uses separate thickness/custom-scrollbar CSS classes. |
| `dynamicRowIcon` | False initially, true in the capture. Indicate Inserted Row(s) also enables its read-view indicator. Rendering additionally checks row/subrow type and edit/read-view state; custom-model branches can bypass the flag. An icon does not confer edit access. |
| `selectionBorder` | True. False suppresses the header-selection border through a removeBorder class; selection itself remains available. |
| `storedColumnTooltip` | True. A reader still uses it for last-updated-cell tooltip text, but its inspected settings control is commented out. Reader support does not certify current UI authoring. |
| `showInfoRiverLogo` | True. Status-bar rendering also requires non-Fabric build and edit mode; a captured true does not promise a logo in Fabric. |
| `showChildCount`, `showRowDescendants` | False. Hierarchy controls require multiple category levels and no drilldown capability; descendants also requires child count. Reader supports applicable Hierarchy/Drilldown paths and appends child versus descendant counts. These settings do not expand rows. |
| `hideExpandLevel` | Empty dimension-keyed Boolean map. Toggle adds true or deletes the selected key; the reader hides that dimension's hierarchy icon, not its data rows. Preserve the layout/level availability rules. |
| `enable` | False initially, true in the capture. Selection-change code sets it as interaction bookkeeping; an independent general appearance toggle was not established. |

Sources: settings controls, footer aggregation, scroll classes, row-indicator reader, selection border, tooltip reader, logo gate, child-count controls, selection bookkeeping.

The ruler model separates enabled (default false; captured true) from disabled `{state:false,prevEnabledState:null}` restriction/restore bookkeeping. activeSummaryGroup is interaction focus, initially null; do not copy it as business layout. rulerMeta.width initially 20 is resize-authored, and showNumbers initially false has a Show Ruler Numbering control when enabled outside Stepped/Outline/Summary. The capture's loading field lacks an established active mapping in this trace. Likewise, persistConfigs.resetPlanningThemes is host bookkeeping: FabricHost can use it to reset themes after a feature-switch transition. Its captured true is not a style preset or a command to execute while learning the sample.

##### Visual Annotation Box Appearance

`S.annotationBox` styles the Matrix annotation panel, not Data Input cells, the visual container or page commentary. The capture contains a disabled box with preserved configuration. Enabling it alone does not establish annotations to render: the reader also needs annotation data and available space. Use Annotation Settings and its staged Save/Reset for supported style changes; enablement and resizing are separate actions.

| Annotation-box fields | Initial values, options and dependencies |
| --- | --- |
| `enabled`, `placement`, `size` | false, RIGHT, 200. Placement TOP/RIGHT/BOTTOM/LEFT; left/right size is width, top/bottom height. Drag resizing applies minimum 100 and maximum 600/available-space-minus-100 bounds; do not assume that drag logic clamps every loaded size. |
| `itemGap`, `fontSize`, `fontFamily`, `color` | 5, 12, Segoe UI, #333333. Gap control 0-50 is per-item bottom padding; body font 8-60. The capture uses the longer Segoe UI fallback stack, not a different field type. |
| `padding` | topPadding/rightPadding/bottomPadding/leftPadding all 5; isCustomPaddingSize false, isEnabled true. Controls 0-50. The reader applies a present padding object without checking these two flags; they are not reliable rendering-off switches. |
| `cornerRadius` | radiusTopLeft, radiusTopRight, radiusBottomLeft and radiusBottomRight all 0; isCustomCornerRadius false, isEnabled true. Controls 0-50; reader gates on isEnabled and then uses all four values. |
| `border` | color #D1D1D1, width 1, isEnabled true, side all. Width control 0-50; reader handles top/bottom/left/right, otherwise all, as solid borders. The position selector is commented out despite reader support. |
| `shadow` | color #E0E0E0, blur 8, isEnabled false, placement outer, side bottom, width 0, opacity 70, angle 135, distance 10. Controls expose inner/outer, side/direction and custom angle 0-360. Reader uses width, not distance, for offset; blur/width controls 0-50. Hex-color opacity is clamped 0-100 and used as alpha despite a Transparency UI label; RGB/RGBA strings pass through. Do not copy the container's white-overlay opacity semantics here. |
| `title` | enabled/showTitle/showValue/showVariance true; varianceType both (absolute/percentage/both), varianceIconType triangle (triangle/circle/circle-with-arrow); fontSize 12, fontFamily Segoe UI, color #333333; valueRenderRole and varianceRenderRole Responsive. Title font control 8-60. |

Sources: annotation schema/default factory, style controls, title controls, container-style reader, resize implementation, annotation rendering.

Title value roles include Responsive/AC/PY/PL/FC; variance choices use the owning paired variance-role constants and can include eligible measure IDs. Available choices depend on visible measures. Responsive values prioritize visible PY, then PL, FC, AC; missing eligible measures suppress values rather than inventing them. Title text comes from the row label and requires enabled title, showTitle and row data. Preserve role identities rather than serializing translated selector labels or copying a sample's measure IDs.

Page `E.commentary.notes.settings` and `E.commentary.annotation.settings` have separate Shell schemas, including borderAndCorner and padding top/right/bottom/left rather than the annotationBox padding names above. Do not substitute or synchronize the two objects by name. This appearance audit does not establish note CRUD, comment permissions or their full ALM construction.

The captured globalStyles.rowHeight remains legacy state in this bounded trace: no active reader or migration from that field was established. Current rendering reads row_height_config.default_row_height. Its native defaults use unsigned heights, ordinary/subtotal 26 and grand-total map entry 36, whereas the frontend root initializer and the bundled new-Planning seed use 26. Preserve the explicit layer-specific state; do not turn either value into an unqualified migration rule for existing reports.

##### Visual Container and Canvas Properties

The Shell container initializer and canvas initializer define separate objects. The following are their initialized states, not sample recommendations or complete import envelopes:

| Shell owner | Fields/defaults and reader distinctions |
| --- | --- |
| `visualStyles.background` | isEnabled true, backgroundColor #fff; optional type color/image, backgroundImageSrc, fillMode cover/contain/repeat/auto, opacity, fileName. Image fill falls back to cover; opacity is interpreted as white-overlay percentage `(opacity ?? 0)/100`, not page alpha. |
| `visualStyles.border` | Matrix container isEnabled false, color #ddd, side all, width 0. Side choices all/left/top/right/bottom; rendered solid, not Matrix grid-border-style enums. |
| `visualStyles.cornerRadius`, `.padding` | Enabled, custom flags false; four radiusTopLeft/TopRight/BottomLeft/BottomRight values 0; four leftPadding/rightPadding/topPadding/bottomPadding values 5. |
| `visualStyles.shadow`, `.rotation` | Shadow disabled, blur 12, color #000000, side bottom, placement outer, opacity 16, width 3, angle 0, distance 10. Rotation disabled, transform 0. |
| Host tooltip | isTooltipEnabled true, tooltipType default, tooltipPageId auto; tooltipStyle bold/italic/underline false, Segoe UI 12, label/value #252423, background #FFFFFF. Separate from Matrix numeric-tooltip units/precision. |
| `canvasStyle.background`, `.wallpaper` | Background type color, value/color #ffffff, imageUrl empty, enabled, cover, opacity 1; optional fileName. Wallpaper value is an object containing type/color/imageUrl, with its own enabled/fill/opacity fields. Canvas reader uses color/imageUrl and opacity 0-1; disabled/missing color returns white. |
| Canvas border/corners/shadow | Border enabled, #d0d0d0, all, width 0; enabled/custom-false corners all zero. Shadow follows the container baseline except angle 135. Preserve each object's separate state. |
| Canvas dimensions and guides | dimension type DEFAULT_16_9, width 1600, height 900, elementScalingUnit percentage; isLocked false; gridLineSettings showGridLines/snapToGrid false, gridRows/gridColumns null, gridLayoutType auto. showVisualGuide false, showSmartGuide true, verticalAlign top, scrollToZoom true, isAutoLayoutDisabled false; mobileCanvas has separate edit/runtime dimensions. |

See container style reader and canvas reader. Page gridLineSettings control authoring guides/snap, not table major/minor lines. Default viewport sizes are not a reason to copy a sample page geometry or bypass the shared presentation standards.

Validate field spelling, selector enum versus stored value, scoped IDs/operation order and separate background/opacity units. Native acceptance must check row-hover/alternate behavior, label exclusions, enabled versus merely colored lines, Skip Lines including zero, long labels, rotated headers, manual/responsive widths/heights, both application modes and save/reopen. Keep migrationVersion and transient editor flags distinct from user settings; no runtime/theme/ALM guarantee follows from an initializer.

### F16 Column Style

Intent: style headers/columns, set widths and numeric formatting, and remove calculated-column metadata. Shares F14 formatting but also has a JetStream columnMeta owner.

| Native setting / operation | Evidenced behavior |
| --- | --- |
| `inforiverProps.columnMeta` | Imported `ColumnMeta`, initially `{}`. Complete member schema not expanded. |
| `IColumnFormattingProps.id` | String identifying the target column. |
| `styles`, `numFormat` | Optional imported style/format structures, not arbitrary CSS objects. |
| `updateState(payload)` | Replaces the state with payload. |
| `updateColFormatting`, `updateNumberFormatting` | Build merged controller payloads, await `updateColumnMeta`, then replace local state. |
| `updateColumnWidth` | Accepts `{id,width,isResize?}[]`; inspected normalization rounds `width || 0`. |

Do not invent a `columnMeta.update({colId,alignment})` API or assume changing the local store alone persists a style. **ALM gap:** controller/native conversion, style wire keys, target column ID mapping, and restoration; no complete column-style part recipe.

#### Column Style Authoring

Format -> Column Style communicates cell state without granting input access. The preceding columnMeta contract is a separate per-column owner; this menu writes `globalStyles.columnStyle.<category>.<mode>`. Configure Reading View and Editing View independently when matching appearance is required. The inspected menu/modal has no copy/synchronize control between them; saving Editing does not update Reading. The application `isEditMode` chooses read/edit style, not which individual cell currently has keyboard focus.

| UI category | Saved key | Boundary |
| --- | --- | --- |
| Locked Cells | locked | Lock/driver and cell-state resolution matters; gray color is not the lock itself. |
| Data Input | custom | This is the Data Input category, not comments. Comment indicators have separate ownership. |
| Native Measures | native | Native/source measure appearance, not an authorization or aggregation setting. |
| Forecast - Open periods | forecastOpen | Styles the applicable forecast period state; does not make linked/formula periods directly editable. |
| Forecast - Closed periods | forecastClosed | Historical appearance is independent of underlying source refresh or permission. |

Source: Column Style menu, category reader. Both `read` and `edit` are valid mode keys. The global initializer does not populate this map; the menu shows gray for locked and white otherwise, while an unset reader can return null styles rather than a fully materialized white preset. Locked fallback CSS supplies its own background.

The category reader first returns a resolved adjustment-cell style when present. Otherwise, only a non-explicitly-locked cell is reclassified into forecastOpen (excluding driver-dependent rows) or forecastClosed; it retains the incoming category when those tests do not apply. Explicit visualMode and columnStyleConfig arguments can override the ordinary application-mode/map lookup for their caller. Notes/comments_col chart types bypass this category-style branch. Missing read styling does not inherit edit styling, and vice versa. These rules qualify the category table without turning Data Input into comment formatting.

| Style property | Supported values and preset/modal behavior |
| --- | --- |
| `presetType` | white = Default, gray = Dark, hatched = Hatched. Customize opens the editor; it is not a separate persisted custom preset enum. Custom field changes can coexist with presetType white. |
| `background`, `textColor`, `fillColor` | White preset: transparent/black/white; gray: #DDDDDD/black/white; hatch: white/black/#DDDDDD. Dark-theme hatch instead uses black/white/#A2A2A2. Direct white selection writes empty background, unlike the modal preset's transparent value. |
| `fillType` | none, singleSideHatched, doubleSideHatched; fill-color control appears for hatch. A fill-type action can reselect a preset and replace other fields, so inspect the complete resulting draft. |
| `fontSize` | Preset value 12; separate from global font size and scoped direct formatting. |
| `borderStyle`, `borderColor`, `borderWidth` | Modal presets use solid, #A6A6A6, 1. Selector choices none/solid/dotted/dashed/solidDouble/solidThrice; single/double/triple choices set width 1/2/3. Direct nonwhite preset selection omits borderWidth while modal Save includes it. |
| `borderSides` | Preset null; numeric line-side values INITIAL=1, top=2, bottom=3, double-top=4, double-bottom=5, top+bottom=6, double-solid-top=7, double-solid-bottom=8, left=9, right=10, all=11, around=12. Use the actual selection array, not CSS side-name strings. |
| Reset | Writes only the selected category/mode to null and closes the modal, retaining sibling categories/modes. Not a global style reset or whole-column deletion. |

Evidence: preset definitions, save/reset, fill/border controls, native client side enums.

**Forecast-entry example:** use an open-period Editing customization such as the supplied #78D3B9, then separately configure Reading if the same visual cue is intended there. Preserve the other nine categories/mode combinations and the full edited style record. In the example, presetType white with a custom background is not a contradiction to repair by inventing a Customize wire value. Check closed periods, source measures and locked cells alongside it. The color does not override period, input-rule or security restrictions.

**Precedence is property-specific:** background resolves conditional formatting, direct format, category-label color, then Column Style; alternate-row color is used only when none resolves. Text uses conditional/direct/semantic then Column Style/global; font size uses direct then Column Style/global. Explicit cell-highlight colors and CF hatch can apply in later passes, and locked-cell rendering can replace backgrounds/borders or remove alternate shading. Borders combine grid, Column Style, direct and CF processing independently. Hover injects row colors with important CSS; selection uses separate highlight/border classes and blending, without changing saved styles or application mode. See cell styling, color priority, locked-cell pass, border reader, hover.

Validate all five categories in both modes, unset/null versus explicit presets, custom field retention, selective Reset, hatch/border values and changing fill type. Test intersections with conditional/direct formats, alternating rows, locks, hover and selection rather than inferring precedence from one screenshot. Verify actual editability independently, then save/reopen. No native rendering or persistence was executed for this documentation update.

## Planning Controls and Native Serialization

### F10 Fiscal Year

Intent: configure fiscal start month and year naming. The FiscalConfig implementation owns serialization, partial update, and hydration.

| Native path | Exact inspected contract |
| --- | --- |
| `app_props.fiscal_config` | Optional FiscalConfig; absence is distinct from an explicitly configured default. |
| `month` | Transparent wrapper over `chrono::Month`; default January. Do not assume numeric 1-12 wire values without inspecting chrono serialization. |
| `year_convention` | String enum `Same` or `Prior`; default `Prior`. |
| Partial update | Present request members update existing config. If absent config is created, the other member is initialized to its own default. |
| Persistence / undo | `should_persist_to_backend()` returns `is_native_mode()`; `supports_undo()` is false. Hydrates as `Option<Self>`. |

Native partial value (not a whole part):

```json
{"year_convention":"Same"}
```

**ALM gap:** exact visual-state wrapper, chrono month wire representation, selected artifact route, and import acceptance/restoration are unresolved. Do not confuse toolbar `{kind,value}` commands with this native value.

### F11 Row Model

Intent: author row-model variants, hierarchy, totals, and model templates. CustomRowType / DynamicRowConfig establishes nine Rust variants: `CalculatedRow`, `StaticRow`, `DataSourceRow`, `ForecastRow`, `DriverRow`, `DistributionRow`, `OperationalInputRow`, `AggregationRow`, and `PercentContributionRow` (whose payload is an `Id`, not a metadata object). `LinkedRow` exists only in `CustomRowKind` and is not another `CustomRowType` variant.

| Native member | Type / omission distinction |
| --- | --- |
| `id`, `parent_id`, `previous_row_id` | JetStream `Id`, with the [native decimal-string decoder](#native-identity-and-measure-mutation); not UUID fields. Resolve the referenced row identities separately. |
| `row_type` | Externally tagged union; default constructor is CalculatedRow metadata. Variant payloads are not interchangeable. |
| `title`, `level`, `include_in_total`, `disabled` | String, unsigned integer, boolean, boolean with serde defaults. |
| `scaling_factor` | Optional `Auto`, `Thousands`, `Millions`, `Billions`, or `Trillions`. |
| `bind_for_cross_filter` | Optional boolean; not an arbitrary filter object. |
| `cross_filter_config` | Optional object with optional string `dimension_id`, `dimension_type`, `row_id`, `selection_type`. |
| `description` | Optional string. |
| `column_aggregation`, `roll_up_aggregation` | Optional native `AggregationType`. |

#### Native Row Metadata

The following defaulted members belong to the indicated row payload only. The serde declarations do not establish business defaults or allocation/calculation behavior.

| Row payload owner | Native metadata |
| --- | --- |
| CalculatedRow | Strings `formula`/`description`, booleans `include_in_chart`/`bind_for_cross_filter`, optional `deferred: DIColumns | CustomColumnsExcludeMeasures(Vec<String>)`. |
| StaticRow | Boolean `distribute_parent_value_to_child` (singular), optional `default_value: Row(Option<Id>) | Static(String) | Formula(String)`, optional `row_edit_mode: InEditModeOnly | BasedOnFormula(String)`. This is not Number metadata or AllowInputType. |
| DataSourceRow | Optional `source_ref_id: Id`, boolean `enable_dynamic_children`. |
| ForecastRow | `open_period_config` and `close_period_config` use ForecastRowMethod: `Formula(String)`, `DataSource(Option<Id>)`, `LinkedRow(Option<Id>)`, `DataInput(Option<ForecastDataInputType>)`, `Driver(DriverRowMetadata)`, `Distribution(DistributionRowMetadata)`. Method default is Formula empty string. ForecastDataInputType has `Static(String)`, `Row(Option<Id>)`, `Formula(String)`; it is not Forecast measure DefaultValueType. |
| DriverRow | Optional `driver_ref_id`, `operational_input_ref_id`, `driver_operation`, `driver_format_config`. DriverOperation has defaulted method, aggregation and distribution method; DriverMethods are Addition, Subtraction, Multiplication, Division, PercentageOf, GrowthByValue, GrowthByPercentage. DriverAggregationType is Sum, Average, First, Last, Min, Max, distinct from the broader AggregationType. |
| DistributionRow | Optional `distribution_method`, `operational_input_ref_id`, `distribution_format_config`. DistributionMethod is `Weights(Id)`, `SelfWeight(bool)`, `Equally(bool)`, `Copy(bool)`, `TrendValue(f64)`, `TrendPercentage(f64)`; enum default Equally(false) does not populate an omitted optional method. This is not a data-input rule's distribution union. |
| OperationalInputRow | `controller_ref_id: Id`, optional `min_max_config` with optional `min`/`max: i32`; not the rule MinMaxConfig's tagged bounds. |
| AggregationRow | Optional `aggregation_type`, optional `aggregation_distribution_type: AggregateDistributionType`, `aggregate_distribution_rows: Vec<Id>`. The imported distribution type still requires its owner. |

The separate LinkedRowMetadata has required `reference_row_id: Id`; it is not a tenth CustomRowType. Shared Driver/Distribution FormatConfig has optional decimal `u32`, min/max `i32`, prefix/suffix strings and ScalingFactor.

DynamicRowConfig.update applies supplied title/type/scale/totals/hierarchy/disabled/aggregation fields, but directly assigns `bind_for_cross_filter` and `description`, so absence can clear those. It retains cross_filter_config unless supplied; optional scale/aggregation updates set Some rather than clearing. This is not a uniform sparse merge or full replacement. DynamicRows declares defaulted `list` plus `map_for_internal_use: Id -> usize`; do not fabricate the internal index as a row-authoring shortcut.

Related UI contract: F04. The inspected exporter transforms model-template data before writing `modelTemplate.json`; that does not prove every model-editor structure is a supported template. **Remaining gap:** selected native metadata leaves and Id serialization above are inspected; imported distribution/data types, UI/model-editor conversions, full dynamic-row HTTP/ALM construction, template transformation and import ordering/hydration remain partial. No universal row-model JSON or runtime row behavior is certified.

#### Row Model Business Authoring

Use Row Model when the requirement authors or extends account/KPI/business-driver row members or their individually configured behavior against planning series. An existing account hierarchy or P&L label alone is insufficient reason; apply the [three-way model-selection decision](#measure-based-planning-versus-row-authoring). Reuse a template when the same hierarchy and logic should apply at a selected dimension level with context-specific values. Adding one line, adding a repeated structure, adding a comparison series and adding a source dimension are different requests; do not solve each by cloning a template or modifying the semantic model.

| Business request | Authoring decision |
| --- | --- |
| Add one cost line under a department | Add Child or Add Sibling relative to the intended row, then choose its value source/type and aggregation. Preserve existing identities. |
| Repeat an expense structure across departments | Create/update a reusable template; resolve the application dimension, conditions and Append/Replace before applying it. |
| Sum components or calculate selected branches | Aggregate for the specified child-combination rule; Formula for an explicit operand set or business calculation. A parent is not automatically Sum. |
| Add a margin, rate or operating diagnostic | Keep rates/counts distinct from monetary operands; choose appropriate column/time and row-context rollup semantics. |
| Compare another budget/forecast series | Add the appropriate series/context against the shared KPI hierarchy when that version design is intended; not another duplicate KPI hierarchy. |
| Add a source field such as Channel | Resolve the model/assignment requirement separately. An authored child adds hierarchy depth, not a new semantic-model column. |
| Protect history while planning future values | Combine row structure with supported ForecastRow/forecast-period configuration and input/security rules; editor availability is not cell editability. |

The supplied Global P&L guide describes five source row fields (Organization/Region/Branch/Department/Driver), a total above them, and time Year/Quarter/Month. Its screenshots reportedly show one Value series across three years. They do not prove Actuals/Budget/Forecast were assigned as three measures. Authored groups can deepen the displayed hierarchy without adding source fields. Business drivers such as Footfall or Conversion Rate can be source/formula rows; their names do not require the Driver Input type.

**Workflow:** inspect current axes, identity and series context; open Model -> Row Model; select the existing node; insert only needed child/sibling/template rows; configure each row's type, references and totals; review application scope and any actual period branches; save and verify representative instances. The guide's six UI choices are Data Source, Data Input, Formula, Aggregate, Driver Input and Distribution. The nine source-backed native variants above remain authoritative for their layer; a UI label is not a serialized discriminator, and a four-variant snapshot is not the complete feature surface.

##### Hierarchy Insertion and Templates

Bulk Insert is a newline outline, not a multi-column TSV table. The parser skips blank lines, uses leading tabs for depth, trims titles, requires the first nonblank row at depth zero and rejects depth increases greater than one. After parsing, configure row types and formulas explicitly; text indentation does not create business logic. Example with actual tabs:

```text
Operating Expenses
	Staff Costs
		Salaries
		Benefits
	Admin Costs
		Rent
		Supplies
	Depreciation
	Ratios and Metrics
		Staff Cost Share
```

Child/sibling UI creation passes a reference row and create_as_sibling to the owning workflow. Native placement also updates the following row's ordering link. A saved parent_id/previous_row_id is evidence of structure, not a universal create-request recipe or proof of which insertion command ran. Use the actual allocator/writer; parser depth identifiers and display labels are not native IDs.

Template level is relative to the template, starting at zero, not the ordinal of a source field such as Region. Multiple level-zero rows are supported by template construction. Root creation can generate a separate parent ID. Thus an external root parent is not necessarily a missing node or an actual source-member attachment; do not replace it with a dimension ID. Non-root parent links, levels and ordering must still be coherent within the intended template/owner.

| Native owner | Contract and operation boundary |
| --- | --- |
| `dynamic_row_templates` | Definitions containing id, title and rows; native decimal-string identities are not template names or public GUIDs. |
| `dynamic_row_template_dimensions_map` | Template ID maps to application records: dimension_id, required apply_type Append/Replace, optional condition_config Simple/Advanced. The definition and application are separate objects joined by identity. |
| Creation versus stored defaults | The creation workflow initializes Append with no condition. The serialized application record does not default an omitted required apply_type. |
| Condition update | Absent/null condition_config does not clear an existing condition in the inspected updater. Clearing requires is_reset_condition_data true through the owning request. |
| Unconditional application | No predicate selects the configured dimension level in the current data store; an unresolved dimension is skipped. Null predicate is not proof of no report filters or security restrictions. |
| Overlapping applications | The inspected member-classification consumer gives applicable Replace precedence over Append. This does not establish a winner between two Replace templates, first/last-wins order or deduplication. Never infer precedence from JSON object-key order. |

Sources: template definitions, application schema/updater, condition reset, creation defaults, applicability, member classification.

##### Row Value and Aggregation Decisions

Treat four controls separately: row_type determines the intersection's value; AggregationRow.aggregation_type combines that row's children; column_aggregation controls time/column aggregation; roll_up_aggregation controls higher row-context rollup. include_in_total is independent of all four and is not a formula operand list. Optional aggregation null/omission is no explicit value, while the string None is an actual enum member; the Sum enum default does not populate an omitted Option. Runtime fallback must be resolved at the selected consumer, not inferred from a UI displaying Sum.

For source-backed nodes, source_ref_id is distinct from the authored row ID, template ID, dimension ID and DAX measure identity. Contextual resolution uses the applicable row and original/current data-store/member/template maps. The DataSourceRow branch takes the first resolved ID; no result yields no reference. Repeated Salary labels must resolve within each department's actual context, not bind every instance to the first department's path. Missing dictionaries leave the exact source binding unresolved.

The guide reports a metrics group with AggregationRow None, column_aggregation None, roll_up_aggregation Sum and include_in_total true; all its reported rows have include_in_total true. Its financial root formulas explicitly select monetary components and omit metrics. Do not invent include_in_total false to explain their exclusion. A CalculatedRow may calculate its base intersection by formula yet use Sum at totals, whereas ratio rows use Formula for both aggregation axes in that reported design.

**Worked expense structure:** Staff Costs = Salaries + Benefits; Admin = Rent + Supplies; Opex explicitly adds Staff Costs + Admin + Depreciation, omitting a non-summing metrics branch. The guide's rounded displayed amounts reconcile as -82,876 -17,614 = -100,490; -23,827 -5,860 = -29,687; total with -10,364 is -140,541. Staff/Opex is approximately 71.50%, Benefits/Salary 21.25%, Rent/Admin 80.26%. These are checks of reported rounded numbers, not queries of underlying values or a template for a new business design.

**Three reusable business examples:**

- Shared P&L: Revenue 100/110/120 less positive Marketing 10/11/12 yields 90/99/108 across Actuals/Budget/Forecast. The limited result is Revenue less marketing, not total profit.
- Department expense template: five signed components (-80,-16,-20,-4,-5), (-50,-10,-8,-2,-3), and (-30,-6,-40,-4,-10) produce -125, -73 and -90 respectively. Reuse structure while preserving each department's context and input identities.
- Branch margin and diagnostics: Product/Service revenue 80,000/20,000; signed Material/Labor/Freight costs -40,000/-15,000/-5,000; Gross Margin = revenue + signed COGS = 40,000. Ratios are margin 40%, absolute COGS share 60%, service mix 20%; Orders 600 / Footfall 5,000 gives conversion 12%. Diagnostic counts do not contribute to monetary margin. Do not subtract already negative costs again.

For higher totals, Staff/Opex -100/-200 and -90/-100 combine to -190/-300 = 63.33%, not summed 140% or averaged 70%. Apply the same numerator/denominator discipline across time. Establish zero-denominator and blank behavior through the actual formula contract.

##### Authored Row Extension Examples

Use the detailed comparison guide's six patterns only when the requested drivers are authored business rows, not merely measures shown vertically:

| Existing account structure | Requested row extension | Independent row logic |
| --- | --- | --- |
| Gross Revenue / Discounts | Product Revenue with Quantity and Price children | Multiply drivers; combine monetary components; apply signed discount separately. |
| Salaries / Benefits | Regular Pay and Overtime Pay, each with Hours and Rate | Calculate pay branches, then apply the salary expense sign once. |
| Rent / Utilities | Area, Rent per Area, Consumption, Energy Tariff | Distinct units and formulas for each expense account. |
| Service Revenue | Visits, Fee per Visit, Reimbursement Adjustment, Net Service Revenue | Calculate service revenue and selected adjustment components. |
| Logistics Expense | Shipment Count, Base Cost per Shipment, Fuel Surcharge, Total Freight | Define the surcharge basis and combine only intended cost components. |
| Department Opex | Repeated Staff/Admin branches plus non-summing Ratios | Reuse the existing template/application contract with context-specific sources. |

**Revenue rows:** at one Department/Month/Forecast series, authored Product Quantity 1,000 and Product Price 100 produce Product Revenue 100,000. Gross Revenue combines Product Revenue and Service Revenue 30,000 to give 130,000; Net Revenue adds signed Discounts -5,000 to give 125,000. Quantity and Price are not additional monetary contributions. Select Aggregate only for the intended eligible monetary children; use an explicit formula where operands differ. This is row-level logic even though an alternative application could implement equivalent equations as measures.

**Salary rows:** at the same stated grain, Regular Hours 160 * Regular Rate 30 = Regular Pay 4,800; Overtime Hours 20 * Overtime Rate 45 = Overtime Pay 900; Salaries = -(Regular Pay + Overtime Pay) = -5,700. Do not sum hours, rates and their pay results, or negate already negative source expenses twice. If history must retain source Salaries while future values use drivers, resolve the supported row/series period settings separately; adding the rows does not establish that split. These conceptual equations do not introduce new native keys or resolved reference tokens.

##### Reported Model-Editor Mapping and Evidence Limits

The earlier Global P&L Markdown reports a companion model-editor response that the earlier update did not independently parse, with `etag` and `modelEditorTemplate.schema/properties`. Its properties contain dynamic_row_templates and dynamic_row_template_dimensions_map. Reported counts are six templates with 15/12/8/7/7/3 rows, totaling 52: 21 DataSourceRow, 17 CalculatedRow, 11 AggregationRow and three StaticRow. It reports 17 locally resolving formula expressions, six external root parent references and 21 opaque source references. At that earlier review, the companion JSON, evidence report, screenshots and strategy deck were unavailable at the named local paths. The later comparison package includes Row Model JSON/evidence and assets, but availability alone is not validation. Those earlier counts and UI associations remain guide-reported here; the four newly inspected comparison screenshots do not independently establish them or supply a Measure Model export.

| Reported example | Reusable interpretation, not copied identity |
| --- | --- |
| Gross Margin and Operating Expenses | Replace bindings at a shared dimension; Gross Margin has a member predicate, Opex has no explicit predicate. The Department label comes from guide/UI context, not a dimension-name dictionary in the reported response. Other financial/exploratory templates use Append. |
| `condition_config.Advanced.filter_rules` | Reported grouped RowFilter/Text Is predicates with And/Or combinators and not false. Keep structured predicates and resolved dimension identity; do not copy member names or infer source/security scope. |
| `CalculatedRow.formula` | Reported native R_<row ID> tokens, distinct from readable template/row paths. Retain the source-backed formula contract and verify every reference; no display-label-to-token string substitution recipe is established. |
| `StaticRow` | Reported default_value `{ "Static": "" }`, distribute_parent_value_to_child true and row_edit_mode null. Blank string is not zero or a measure/formula default. The distribution flag does not make the row a DistributionRow. |
| `DataSourceRow` | Reported source_ref_id and enable_dynamic_children false. A source-reference dictionary and runtime resolution are separate evidence. |
| Five null rollups | Guide reports null in five rows where screenshots show Sum. UI fallback versus capture drift is unresolved; retain null, not an invented explicit Sum. |
| Closed/open behavior | Reported payload has one row configuration per node, not period branches. Do not fabricate closed_period/open_period keys. This absence does not erase the existing source-backed ForecastRow open_period_config/close_period_config support. |
| Native versus export | modelEditorTemplate.properties.dynamic_row_templates is not automatically public modelTemplate.json properties.dynamicRowTemplates. Resolve the actual exporter/importer and ID rewrites; renaming keys is not deployment. |

The guide separately reports successful public definition retrievals with five parts and an empty sheets array. Those calls were not repeated, their cause is unresolved, and the reported model-editor response does not itself bind a sheet/visual or prove persistence. Do not access its live report, reuse captured ETags/credentials or treat a successful HTTP status as complete export coverage. Source-backed boundaries above are independent of that historical retrieval claim.

**Acceptance:** verify unique lossless IDs; definition/application joins; parent levels and ordering; referenced rows, dimensions and source dictionaries; condition/reset and overlapping-template behavior; row and time aggregation; signed arithmetic and excluded metrics; actual period/input/security restrictions; multiple instances with different source values; save/reopen and target-specific ALM restoration. A synthetic structural check cannot prove native formula execution, template propagation, source refresh or input retention. Preserve unrelated rows and never delete/recreate templates merely to force a desired hierarchy.

### F12 Measure Model

Intent: order/show/hide/manage measures and optional promoted/anchored measures. ManageMeasuresMember is serialized inside `ManageMeasures(Vec<ManageMeasuresMember>)`.

| Native member | Type / default |
| --- | --- |
| `id` | JetStream `Id`, serde default; domain is not established by this struct. |
| `visible` | Boolean; omitted deserialization default false, but `new(id,order)` explicitly sets true. Keep those claims separate. |
| `order` | Unsigned integer with serde default 0. |
| `width` | Optional unsigned integer, omitted from serialization when None. Units are not stated in this struct. |
| `source_measure_id` | Optional string, omitted when None; references a source measure for promoted measures. |
| `anchor_config` | Optional F20 structure, omitted when None. |

Update operation upserts the ID if needed and replaces the entire member with `updated_member`; reorder is a separate operation. Backend persistence depends on native mode; this property disables undo in the inspected implementation. Native **partial member illustration**, with target ID deliberately not supplied:

```json
{"visible":true,"order":0}
```

**ALM gap:** complete ID serialization, outer stored property envelope, promoted-reference remapping, and import/orphan behavior. Do not claim a shared definition interface alone proves ALM preservation.

#### Measure Hierarchy Authoring

Ordinary measure-based planning does not require this editor: source, input, Forecast and formula measures can operate over entity/time contexts with a flat list. Add Model -> Measure Model when logical measure grouping is needed, then select an eligible Measures in Rows view and verify expand/collapse. The guide focuses on that workflow, not a prohibition on other supported views such as Tree. Editor-supported measure creation is not evidence that all inputs must be authored there. Use the [model-selection decision](#measure-based-planning-versus-row-authoring) before choosing a hierarchy.

The preceding `manage_measures` registration contract is not the whole Measure Model feature. The supplied guide additionally observes `visualState.measure_tree` and `measure_tree_node_expand_state`: a business explanation hierarchy over existing measures, distinct from formula dependencies, semantic row dimensions, saved pivots, bookmarks and grand-total display. Nesting costs beneath profit does not define subtraction or addition. Shared formula drivers need not be duplicated to reproduce every dependency edge in the displayed tree.

**Must:** resolve every measure node against the current owner/consumer registry and preserve its string identity. Design the conceptual hierarchy first, then flatten it into preorder. For the supplied measure-node representation, the first node is level zero; levels are nonnegative integers and may rise by at most one; a parent is the nearest preceding node at the immediately shallower level. Multiple level-zero roots are valid. Use unique measure IDs for this authoring workflow; that is a chosen validation constraint, not proof of every product node variant. Preserve unknown metadata, required helper registrations and explicit node order.

**Example:** synthetic registered-measure IDs illustrate the historically observed shape, not an allocator or complete properties payload:

```json
{
	"measure_tree": [
		{ "id": "9007199254740993", "level": 0, "meta": { "hide_in": null, "node_type": { "Measure": { "aggregation": null } }, "rules": null } },
		{ "id": "9007199254740994", "level": 1, "meta": { "hide_in": null, "node_type": { "Measure": { "aggregation": null } }, "rules": null } },
		{ "id": "9007199254740995", "level": 1, "meta": { "hide_in": null, "node_type": { "Measure": { "aggregation": null } }, "rules": null } }
	],
	"measure_tree_node_expand_state": {
		"default_count": 1,
		"expanded": { "9007199254740993": true },
		"max_count": 3
	}
}
```

For example, show an outcome above its amount and rate drivers, but keep the actual calculation and per-axis aggregation independently configured. Null node aggregation does not remove aggregation elsewhere. Expansion keys must resolve to retained nodes; expansion counts in a sample are settings, not product capacity limits. Do not require every registered helper measure to be visible in the tree or assume a folder-node wire shape from the UI; obtain the selected folder writer/native example when needed.

**Prefer:** a concise initial explanation with expandable detail, meaningful labels matching the actual sheet dimensions, and existing source/input/formula formatting. A historical 10-15-line presentation target is not a universal requirement. **Avoid:** copying a sample P&L/sign convention, summing an already included subtotal with its components, treating hierarchy membership as formula registration, or changing KPI formatting based solely on a past issue.

**Workflow and validation:** use Model -> Measure Model where available; add existing measures, arrange roots/children/siblings, configure aggregation separately, set initial expansion, save and export. Verify registry membership, preorder/levels, unique measure-node IDs, expansion references and formula cycles independently. Native acceptance must check rendered indentation/order, expand/collapse after reload, leaf/parent/rate totals, scenario/period behavior, bookmark identities and embedded layout. A well-formed tree does not certify calculations or import preservation.

##### Measure Hierarchy Evidence and Worked Example

The detailed comparison guide and its four local screenshots were reviewed together. They distinguish an existing GL/account hierarchy with an Actuals measure, a flat measure list beneath geographic/product members, a rendered grouped measure hierarchy and the Measure Model editor. Visible labels and indentation are UI evidence, not exported identity mappings or proof of the current deployment. The package's Row Model companion response is not a Measure Model export.

| Editor observation | Reusable interpretation and limit |
| --- | --- |
| Sales Volume Number default 300, Sum; Average Selling Price Number default 150, WeightedAverage | Different metric definitions can coexist in one hierarchy. These values are sample settings, not defaults; the screenshot does not disclose the weighting basis. |
| Five adjustment inputs with Default Measure Value and Sum | Return, pricing, discount, markdown and allowance inputs can retain distinct source defaults. Their names alone do not prove units, writable source measures or formula operands. |
| Material Cost / Unit Number default 20, Average (Leaf) | A rate can use a different aggregation from an amount; leaf averaging is not proof of volume weighting. |
| Raw Material Cost, Total Labor Cost, Regular Labor Cost and Required Labor Hours formulas, each showing Sum | Visible expressions show negative material expense, negative combined pay, capacity-bounded regular pay and volume * labor-hours/unit. Do not impose Sum on every formula or reconstruct clipped Net Revenue/Total COGS expressions. |
| Gross Profit formula visibly includes Net Revenue + Total COGS + Total Expenses | Preserve the sample observation, but name a new result for the costs it actually includes. A familiar label does not establish the business definition of gross profit. |

The [Microsoft Learn Measure Model tutorial](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-4-measure-model), reviewed for this update, documents adding explicit formula measures, placing existing measures under parents, returning to Measures in Rows and viewing the hierarchy in Tree. It specifies Formula on both axes for its created formulas, whereas the supplied editor screenshot shows Sum on several formulas. These are scoped configurations, not interchangeable universal defaults. Select and test aggregation at the requested grain; neither grouping nor tutorial arithmetic guarantees correct totals for arbitrary data. Keep existing [aggregation restrictions](#totals-and-aggregation-authoring) and [Tree availability](#layout-and-measure-placement-authoring).

**Illustrative operational measure chain:** one Plant/Product/Month, USD, not a reconstruction of clipped screenshot content. All nodes below are measures. Inputs are volume 1,000 units, selling price 100/unit, material cost 20/unit, labor 1 hour/unit, regular capacity 900 hours, regular rate 30/hour and overtime rate 45/hour.

| Calculated measure | Conceptual calculation | Expected value |
| --- | --- | --- |
| Revenue | Volume * Selling Price | 100,000 |
| Raw Material Cost | -(Volume * Material Cost per Unit) | -20,000 |
| Required Labor Hours | Volume * Labor Hours per Unit | 1,000 hours |
| Regular Labor Cost | MIN(Required Hours, Capacity) * Regular Rate | 27,000 |
| Overtime Labor Cost | MAX(0, Required Hours - Capacity) * Overtime Rate | 4,500 |
| Total Labor Cost | -(Regular Labor Cost + Overtime Labor Cost) | -31,500 |
| Total COGS | Raw Material Cost + Total Labor Cost | -51,500 |
| Gross Profit | Revenue + Total COGS | 48,500 |

Other expenses are excluded here. The overtime rule is illustrative, not hidden screenshot text. An explanatory tree can place Revenue and Total COGS beneath Gross Profit, Volume/Price beneath Revenue, and Materials/Labor beneath COGS. Put each driver once in the display tree; formulas may reference drivers elsewhere. At volume 800 with other assumptions unchanged, required hours are 800, regular pay 24,000, overtime zero, materials -16,000 and gross profit 40,000. This lower-capacity case catches negative overtime and demonstrates why mixed units and nonlinear capacity rules need explicit formulas and grain-aware totals.

Validate the measure registry/dependency graph separately from the hierarchy preorder/expansion. Reorder or collapse a group without changing the configured formulas or input identities; verify actual values after save/reopen. The new screenshots supply no additional native Measure Model JSON contract and do not upgrade the existing historically observed tree fragment to a complete constructor.

### F13 Approval

Intent: define approval levels, approver selection, workflow actions, and approval columns. ApprovalFlow.types exposes distinct UI/request shapes.

| Input member | Shape |
| --- | --- |
| Approval level | Required string `id`, string `name`, `approverType`, boolean `allowEntryOnTotal`; optional string `approversColumnId` and accessing-user array `accessControl`. |
| `ApproversSelectionMode` | Exact string literals `EMAIL`, `COLUMN`. |
| `IWorkflow.condition` | String; `rules` is an array of set-value/mail rule variants. |
| `approval_meta.approval_columns[]` | `column_config: INewColumnConfig` plus native `user_permission: AccessControl`. |
| `approval_meta.approval_type` | Imported `ApprovalType[]`; wire members not inventoried. |
| `email_notification`, `should_reset_on_reject` | Imported notification type and required boolean; no default proven by this interface. |
| Update request | Adds required `deleted_column_ids: string[]`; create request does not. |

Do not conflate Planning approval columns with the public PowerTable `approvals.json` contract. User/graph references require target-domain resolution. **ALM gap:** exact exported shape, user mapping/drop rules, backend validation, notification variants, and importer behavior remain UNKNOWN. No tenant-remapping guarantee is made.

#### Approval Workflow Authoring

Use approvals when a business decision must certify a defined set of planning values, not merely display a review dashboard. The supplied 54-slide approvals/workflows deck contributes product screenshots, functional examples and speaker-note constraints. Screenshot-visible controls are historical UI evidence; its advanced processes and PowerTable policy tables are illustrative configurations, not newly executed workflows or universally available presets. The source contracts above remain authoritative for their inspected layer; no complete save/import constructor follows from the deck.

##### Choose and Configure the Workflow

Start with the preset Approval Workflow when its ordered stages fit. The supplied wizard shows named levels, approvers selected by email/user selection or a column, and an Allow entry on Totals/Subtotals control per level. Configure the participant binding and intended aggregate scope explicitly; a checked screenshot is not the correct default for every plan. Entra/Azure group use is reported in the supplied narrative, not established by these screenshots or the native payload table; resolve current support and membership semantics when requested.

The next wizard page exposes Reset on Rejection, submission notifications to approvers, and decision notifications to the submitter. The reset describes prior approval statuses returning to In Progress, not erasure of numeric plan values. Observed planner options are In Progress, Submitted and Reopened; reviewer options are Pending, Approved and Rejected. Treat these as the illustrated workflow's choices, not a closed enum for all custom status fields. Additional states or routes require intentional configuration.

| Business requirement | Starting point and distinct controls |
| --- | --- |
| Standard submitter/manager chain | Preset levels, participant bindings, notifications and a deliberate input rule. A preset state does not establish every requested numeric lock. |
| Values fixed during review | Combine planner/submission state with approval state in editability; blocking only Approved leaves Pending behavior unspecified. |
| Quality gates or threshold escalation | Custom readiness and guarded actions supplement appropriate preset stages; identify which parent total and submitted values the policy evaluates. |
| Parallel decisions | Require all configured reviewers to approve the same candidate revision; one completed stage is not final approval. |
| Shared ownership, versions or periods | Governed policy tables, model-evaluated flags and local workflow state; policy flags alone must not reopen submitted/approved inputs. |
| Release after approval | A separate authorized, replay-protected action writes a separate target from the approved value. Approval is not release or authorization for an external-system write. |

Keep five responsibilities separate: preset states route review; [Allow Input](#f30-allow-input-based-on-formula) controls contextual editing; [On Change](#f29-onchangeformula) performs configured writes; notifications prompt action; DAX evaluates model policy. Conditional formatting communicates status but does not enforce locks or permissions.

##### Approval Identity and Scope

**Must:** define the approval key from the actual business grain: entity/project or the required dimensions, scenario, business version, approval period/package, plan cycle and submitted candidate revision. A one-time visual status column can govern a row's intended multi-period package; a separate monthly decision requires month-scoped status identity. Filtering to February does not itself create a February approval record. Keep approval scope separate from all periods currently visible in the grid, and preserve [input filter context](#planning-input-context-authoring).

Locate the status-owning row and have descendants reference that package deliberately. Immediate parent is not always the business approval ancestor; resolve intermediate hierarchy levels instead of assuming ROW.PARENT means region/program. Readiness must include the canonical required descendants, including collapsed or visually filtered-out members within the authorized package. Do not bypass security to collect unavailable descendants; incomplete required scope is not a ready package.

Distinguish business VersionKey, candidate submission revision and persistence concurrency tokens. A new qualifying submission creates its next candidate revision once, not on every keystroke or view refresh. Invalidate decisions that certified prior values according to the agreed policy; a displayed Approved label without revision binding does not certify the new candidate. Retain prior decision history where required rather than overwriting it with a final current-state column.

##### PowerTable and Model Policy

PowerTable is Fabric Plan's optional business maintenance surface over governed policy data. Reuse an existing governed source when that suffices. The illustrated design uses three distinct policies; these names are conceptual, not mandatory product tables:

| Policy | Matching grain and outcome |
| --- | --- |
| PlanningAccess | Normalized signed-in identity plus region/account/scenario (and any additional required business scope); separate edit and review flags. |
| VersionPolicy | Scenario + business version; whether that version is editable. |
| PeriodPolicy | Scenario + business version + approval month; whether that period is open. |

For this design, require exactly one applicable policy row per key and a flag equal to 1; missing/blank/ambiguous/duplicate matches return 0. This is an explicit fail-closed example policy, not a universal product rule or a substitute for defining additive multi-role grants. DAX USERPRINCIPALNAME identifies the query user; normalize both stored and queried identities consistently. SELECTEDVALUE detects ambiguous keys but is not a leaf test: a filtered subtotal may have one value. Use the actual hierarchy scope, such as appropriate ISINSCOPE checks, or explicitly disable aggregate entry. If totals must be editable, evaluate every affected descendant's permission, state and period.

Define the combined PeriodOpen flag as version editable AND selected period open, with valid unique scope matches. A closed Prior version remains closed even when its month policy says open. DAX ALL over the illustrative disconnected mapping removes report filters, not model RLS. These flags complement product/column/persistence authorization; they are not security grants.

The supplied technical guide's sample policies omit Plan Cycle and assume that one cycle is already isolated. If policies vary by cycle, extend both storage coordinates and policy matching or explicitly isolate the cycle; adding it only to a displayed package label is insufficient. Its selected ApprovalPeriod month must identify the actual package. A rule repeated under monthly columns must resolve each column's month, not reuse one February flag across all periods. Extend access keys for version/period differences when required. The sample access DAX returns the stored flag for a unique match; validate the 0/1 domain and consume it with an explicit `== 1` test rather than claiming that MAXX itself normalizes invalid flags.

The data path is policy save -> actual destination table -> model visibility/refresh or requery -> planning-view reevaluation. A PowerTable seeded from a semantic model does not itself write changes back into that original model. Ensure the actual policy destination is included through the intended data path. OneLake/Direct Lake with configured updates is one illustrated architecture, not a zero-latency guarantee or a prerequisite for all workflows. DAX does not write statuses or read unsaved local planning edits; retain live workflow state in the planning rule rather than a stale model copy. Opening a period or changing the viewer must not itself stamp an edit, release values or send an approval notification.

##### Editability and Transition Guards

The following is conceptual logic for the illustrated single-reviewer workflow, not executable native formula text or permission assignment. Resolve native tokens, function support, selected input type and current writer through the existing contracts. In particular, do not generalize On Change support to Long Text from a short-comment example.

```text
InputAllowed = CanEditScope == 1 AND PeriodOpen == 1
			   AND PlannerStatus IN {In Progress, Reopened}
			   AND ManagerStatus != Approved
DecisionAllowed = CanReviewScope == 1 AND PeriodOpen == 1
				  AND PlannerStatus == Submitted AND ManagerStatus == Pending
SubmitAllowed = InputAllowed AND Ready AND valid new-submission transition
```

Synthetic truth-table fixtures, with both policy flags already evaluated at a valid leaf/package scope; Empty denotes an intentionally empty decision field, not a native serialization token:

| CanEditScope | CanReviewScope | PeriodOpen | PlannerStatus | ManagerStatus | InputAllowed | DecisionAllowed |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | In Progress | Empty | true | false |
| 1 | 0 | 1 | Submitted | Pending | false | false |
| 0 | 1 | 1 | Submitted | Pending | false | true |
| 1 | 0 | 1 | Reopened | Rejected | true | false |
| 1 | 0 | 1 | Reopened | Empty | true | false |
| 1 | 0 | 1 | Reopened | Approved | false | false |
| 1 | 0 | 0 | Reopened | Rejected | false | false |
| 0 | 1 | 0 | Submitted | Pending | false | false |
| 0 | 0 | 1 | In Progress | Pending | false | false |
| 0 | 1 | 1 | Submitted | Approved | false | false |

Readiness is a submission prerequisite, not necessarily an edit prerequisite: a missing comment must remain correctable by its authorized owner. Protect each decision/status field separately; the permission to edit an amount does not grant reviewer authority. The screenshot's simple rule `[Manager Status] != "Approved"` explains why Reopened plus Approved can still be locked. An intended reopening must address the relevant approval state through a controlled transition, not weaken the rule or assume a planner-label change resets everything.

The illustrated reviewer gate also requires an open version/period. A business process allowing decisions after closure needs a separately defined review policy; do not silently remove that guard. Boolean permission to edit a status cell does not validate every next list value: constrain the actor, prior/current state, requested next state and candidate revision independently.

For the guide's illustrative positive-baseline rule, an increase strictly above 15% requires an explanation. The following readiness results assume a valid numeric proposal and no other unmet quality checks; readiness is not approval:

| Baseline | Proposal | Explanation present | Ready |
| --- | --- | --- | --- |
| 100 | 130 | false | false |
| 100 | 125 | false | false |
| 100 | 125 | true | true |
| 100 | 115 | false | true |
| 100 | 110 | false | true |

Reducing 130 to 125 does not remove that explanation requirement. Define zero, negative, missing and newly created baselines before implementing percentage comparisons. If January Actual and February Forecast are different measures, bind Actual explicitly; moving Forecast back a month is not equivalent. Names such as ADD_MONTHS, ADD_QUARTER and ADD_YEAR do not establish signatures or the required time hierarchy.

| Transition | Required guard | Intended effects in the configured example |
| --- | --- | --- |
| Submit / resubmit | Authorized owner, open scope, ready package, allowed prior state and current revision | Record candidate revision once, set required reviews Pending, stamp submission/update fields, close inputs and notify configured reviewers. |
| Stage decision | Authorized reviewer, correct pending stage, open scope and current submitted revision | Record that stage and actor/time; route any required next stage. Stamp final approval only after all required decisions for this revision complete. |
| Reject for correction | Authorized pending reviewer; required reason supplied; current revision | Retain rejection/reason, reopen the intended package, invalidate applicable earlier decisions, stamp the return/update and notify the owner. Preserve numeric values. |
| Withdraw pending review | Authorized initiating owner, open scope, Submitted/Pending prior state | Reopen that package and clear its pending decision as configured; stamp update and notify the reviewer. Reject any stale decision arriving afterward. |
| Reopen approved package | Separate explicitly authorized reopening policy | Determine which decisions/revision must be invalidated and preserve history; neither pending rejection nor withdrawal automatically applies. |
| Release | Final current-revision approval plus releaser authority and first valid confirmation | Copy the resolved approved row/period value to a separate release field, stamp release, preserve approved inputs and prevent replay. |

Bind each On Change action to its initiating field and valid transition, not merely to a currently matching status. SETVALUE target row/column/measure and value must be resolved; illustrative labels, hard-coded amounts, candidate numbers and email addresses are not deployable references. Verify whether programmatic writes invoke downstream handlers before chaining them. A reviewer-caused Reopened write must not accidentally execute the owner's withdrawal branch. Revalidate state/revision at mutation time, guard repeated events and self-trigger cycles, and verify selected writer conflict/partial-failure behavior; neither atomic multi-field writes nor exactly-once delivery is established here.

| Initiating field | Scoped action binding |
| --- | --- |
| Forecast and Comment | Attach accepted-edit auditing to each intended input, not to view refresh or the calculated Ready field. |
| Planner Status | Separate guarded submission and pending-withdrawal branches; their targets and notifications differ. |
| Manager or other reviewer Status | Separate stage approval and rejection branches; a final-approval stamp requires completion of all required stages. |
| Quote Confirmed | Stamp verified evidence age only on the authorized confirmation event. |
| Release control | Write the separate release amount and release time once from the resolved approved source cell. |

Resolve target types as well as coordinates: a string email is not automatically a valid Person value, and date, checkbox and List inputs need their actual accepted representations. Paste, fill, clear, import and aggregate distribution may affect several cells; verify event scope/order, audit precision, partial failures and notification volume rather than assuming one event per user gesture or cell. These action excerpts are not complete deployment scripts or a general permission to execute them.

Use one intentional notification path per transition, preset or custom, to avoid duplicate notices. The screenshot shows actor, changed measure, row/column context, old/new values and View Report; it does not demonstrate an Approve button, recipient routing or guaranteed delivery. Opening that link changes view context only. Resolve recipients from the governed workflow, and validate target-build NOTIFY_USER support/channel behavior without sending test notifications under documentation-only authority.

Define conditional-formatting precedence so a generic Ready rule does not obscure Submitted or Approved. Target the actual protected scope and use a non-color indication of closure; formatting still does not enforce permission. In walkthroughs, retain the same explicit input/status/audit columns across successive states, identify the initiating edit and every written target, and show unchanged sibling packages. Do not compress operational state into one generic evidence column or mistake the illustrated grid for persisted history. Historical SENDMAIL imagery does not override the guide's later NOTIFY_USER examples or establish either function's current native contract.

##### Worked Functional Patterns

These are synthetic acceptance examples based on the deck, not business defaults or current-runtime results. Keep before/after fields, actors, guards, written targets and next recipients visible when explaining a process.

| Pattern | Worked result and acceptance distinction |
| --- | --- |
| Regional forecast quality gate | A 390 regional proposal exceeds a 360 cap. Adding the required variance comment resolves only the explanation gate. Reducing one leaf from 150 to 110 brings the package to 350, allowing submission. Close the selected month/package while leaving unrelated periods and packages unchanged. |
| Capital escalation and release | A confirmed new quote changes its age from 42 days to zero; editing an amount alone does not renew evidence. Project values 140 + 160 + 120 total 420; with another project's 180 the program is 600. Concentration 420/600 = 70% exceeds the illustrative 60% escalation threshold, so manager approval is not final. After director approval, a separate authorized release copies the approved 160 for the selected project/month only, not a hard-coded constant or a release of every sibling. |
| Parallel hiring review | Finance approves candidate 1 but HR returns it with a reason. Corrected values 10/12/12 total 34. Resubmission creates candidate 2 and requires fresh Finance and HR decisions on that candidate; candidate-1 approval must not carry forward silently. Final Approved By identifies the completing reviewer, not the complete decision history. |
| Identity/version/period control | Opening a Working month makes an otherwise eligible owner's In Progress input editable without changing its value. Submission closes it even while owner/period flags remain 1. The reviewer may change only the pending decision. Approval stays locked when the owner returns; rejection or pending withdrawal reopens only if ownership, business version and period still permit it. |

Date aging is evaluated through the configured refresh/action path; do not infer an unattended timer. Record a consistent business time zone and distinguish Last Edited, Submitted, Returned, Approved and Released fields. Current actor/time columns are convenience state, not an immutable event history. This deck example retains submission time during rework until the next valid submission; the Inputs/Workflows video's Working branch instead clears its submission date. Choose and document the intended policy, do not blend them, and preserve unrelated leaf audit fields when approving a parent package.

##### Approval Acceptance Checks

**Must:** maintain an explicit transition table and field-ownership map, resolve real participants/policies/source fields, preserve existing values and unrelated approval packages, and test the actual persistence route. **Prefer:** the smallest preset/custom composition that implements the business policy. **Avoid:** silently creating roles, granting permissions, adding policy tables or external writeback, copying historical identities/thresholds, or claiming model flags and formatting enforce backend security.

Static checks cover package keys, candidate/state references, rule/action dependencies, truth-table expectations, complete descendant scope and exact candidate diffs. On authorized test resources exercise owner versus reviewer, closed version/open month, missing and duplicate policies, subtotal contexts, readiness failures, submission, intermediate/final approval, rejection, withdrawal, resubmission and stale concurrent decisions. Verify no approval carries to another candidate, no unrelated amount changes, no repeated release/notification, and no audit write on viewing or policy refresh. Verify save/reopen, effective field/persistence permissions, notification routing and required history independently. No production notifications, approval decisions or policy edits are authorized merely by learning this deck.

### F15 Conditional Formatting

Intent: condition rules, target-value scales, classification/icons, URLs, color codes, and ranking. Exact rule enum literals are `rule`, `targetValue`, `classification`, `webUrl`, `colorCode`, `ranking`.

| Native setting family | Inspected members / types |
| --- | --- |
| Identity / target | `name`, `displayName`, `highlightedMeasure`, `highlightedMeasureName`: strings; `enabled`: boolean; member selections: imported option arrays. |
| Hierarchy | `ruleFor`, `columnRuleFor`: `parent`, `child`, `both`; total-exclusion flags are booleans. |
| Text / fill | Boolean `bold`, `italic`, `underline`, `applyTextColor`, `applyBackgroundColor`; string `color`, `background`, `underlineColor`. |
| Conditions | `conditionalOperator`: `or` or `and`; `conditions`: structured array whose complete leaf schema remains open. |
| Value comparison operators | `>`, `<`, `==`, `!=`, `>=`, `<=`, `<>`, `isBlank`, `isNotBlank`; these are one enum family, not a universal operator set for every filter. |
| Icons | `isIconPresent`, `isCustomIcon`: booleans; `icon`, `customIconBase64Value`, `customIconName`: strings. Position: `left`, `right`, `iconOnly`, `textOnly`. |
| Scales / ranking | `colorScheme`, `targetValues`, `ranking`, icon-group metadata, gradient numeric limits/colors; complete branch containers are not expanded. |

Evidence: IRule. This broad interface contains fields spanning multiple behaviors; do not emit every field for every variant. Type declarations do not establish factory defaults. **ALM gap:** concrete rule writers/default factories, native CF serialization, custom-icon assets, measure-reference rewiring, and importer behavior. No generic CF rule example is asserted complete.

#### Conditional Formatting Business Workflow

Use conditional formatting to explain a condition without changing values or enforcing permissions. Configure four independent choices: **target**, **condition/comparison source**, **scope**, and **appearance**. A condition on a commentary/helper field may format a different forecast amount. Specify detail/parent/column-total and member scope explicitly, then select supported text/background/icon/emphasis; a colored amount neither makes commentary mandatory nor approves a request.

For a simple condition, create a direct rule, choose the condition source and operator, review scope and preview the intended appearance. For reusable or compound Boolean logic, author a helper formula measure, test its output first, bind a rule to the helper's required result, and hide the helper through the supported Show Columns workflow if appropriate. Hiding is display only, not security. Save/reopen and verify the actual saved condition as well as the visible result.

**Comment-driven example:** the checked export contains an enabled rule targeting the numeric override while its condition references repeating commentary, with aggregationType and dynamicOperation both isNotBlank. It enables text color and an icon, with bold false. ruleFor is both and excludeRowTotal/excludeColumnTotal are false. These are sample settings, not a reason to style every input identically or proof of the engine's full total behavior. Native default/source-input colors and direct styles remain separate from this rule.

**Compound example:** conceptually, `IF(AND(Override != Baseline, Confirmed == true), 1, 0)` yields 1 only when both the value differs and confirmation is checked:

| Changed versus baseline | Confirmed | Helper |
| --- | --- | --- |
| No | No | 0 |
| Yes | No | 0 |
| No | Yes | 0 |
| Yes | Yes | 1 |

The packaged helper formula and hidden manage_measures entry were checked, but the saved custom rule still uses commentary, not the helper. A guide's demonstrated later UI action is not proof it persisted. The snapshot contains both cfProps.rules and jet_cfProps.rules; their coexistence does not mean two independent business rules should be created or that updating one copy is sufficient. Resolve the current writer and representation mapping.

Use tolerances appropriate to the business units when exact inequality is unsuitable; a changed-from-baseline flag is not an edit-history record. Decide whether total flags should recompute in total context or be excluded; summing leaf flags does not automatically mean a total needs approval. Test blank/zero/whitespace semantics, overlapping status/exception rules, member filters and alternate views. Keep a non-color cue and ensure a generic Ready rule does not obscure Submitted/Approved. Rule-family-specific scales, ranking, classification, URLs and complete precedence remain only partially covered; this guide closes simple cross-field/helper workflows, not every rule type.

### F17 Writeback

Intent: configure writeback metadata and destinations, independently of actually executing writes. getWritebackSettingsV2 is the inspected OneLake extraction owner.

| Persisted/exported member | Transformation |
| --- | --- |
| Settings metadata | Shallow-copied from the repository. Open metadata is not a discovered full field catalog. |
| `destinationIds` | Used to determine enabled destinations, then deleted; the toggle helper records portable selection separately. Exact helper marker remains unexpanded. |
| `updatedBy`, `updatedAt`, `createdBy`, `createdAt` | Deleted from settings metadata. |
| Destination repository | Selected by `isAlmWritebackDestinationV3Enabled(ctx)`; both addresses use the visual GUID. |
| `settings.databaseVariable` | Renamed to `settings.database` when truthy; variable-specific original key removed. |
| `connectionId`, `connectionIdVariable` | Deleted when falsy, not unconditionally stripped. Truthy presence does not establish a reusable credential or target authorization. |
| Destination `id`, `version` | Removed after audit cleanup. |
| Destination `visualId` | Replaced with portable `visualRecordGuid`; destination toggle helper applied. |

The caller emits `writeback.json` when settings are nonempty and omits empty `destinations` (Shared ALM Contract). The public table describes `writebackType`, `destinations`, auto-writeback and precision settings, but backend metadata is not closed by that table. **Gap:** destination variants, helper marker shape, full SQL-route parity, importer validation, variable resolution, debounce units/types, and target connectivity. No writes or credential handling were tested; no claim that credentials are always removed or destinations always reset.

### F20 Anchor Measures


**v43 current route:** [anchor-measures.md](anchor-measures.md) provides first-anchor
base construction and current-owner updates using the supplied native XXH3 hash
contract in [dimension-hashing.md](dimension-hashing.md). The temporary v42 note
is superseded. Read [anchor-business-cases.md](anchor-business-cases.md) for all ten
worked cases plus visibility-with-leaf-formulas examples. Source/UI design below
remains useful; it is not a claim of new native runtime acceptance.

Intent: anchor a managed measure to row/column dimensions. AnchorConfig belongs under `ManageMeasuresMember.anchor_config` (F12), not a newly invented top-level ALM key.

| Native member | Shape / default |
| --- | --- |
| `row_dimensions` | Array of JetStream `Id`, default empty. |
| `col_dimensions` | Array of JetStream `Id`, default empty. |
| `display_at_all_levels` | Boolean, default false. |
| `dimension_hash` | String, default empty. |

Native complete **AnchorConfig subtree only**, illustrating defaults and not enabling a useful target-specific anchor:

```json
{"row_dimensions":[],"col_dimensions":[],"display_at_all_levels":false,"dimension_hash":""}
```

Membership readers use `contains(dimension_id)`. The UI IAnchorConfig additionally has `is_enabled`; do not assume that UI flag belongs in this Rust subtree. **v41 evidence:** the inspected export uses decimal-string native dimension IDs resolved from rowDimensions/columnDimensions and omits UI is_enabled. **Remaining gaps:** general UI enable/disable conversion, hidden-node evaluation, cross-layout migration and import fallback. The supplied v43 snippet establishes the dimension-hash producer; first-anchor construction is implemented. No claim that ALM automatically validates or repairs stale anchors.

#### Anchor Assumption Authoring

Use anchors to maintain an assumption at the level where the business decides it and show reporting measures only where useful. This reduces repeated entry locations and clarifies ownership while retaining the model's existing calculations and distribution. The earlier guide describes generated configurations and a lab, not a completed native test matrix. The supplied reusable chat context adds later design corrections; those supersede older mockups for intended behavior, not source-backed serialization or unperformed runtime checks.

For customer-facing explanations, follow the supplied full-scope framing: data-input, formula and native Power BI measures, Manage Columns access, and Intelligence Sheet Matrix are included without narrating historical rollout phases. This is the requested presentation scope, not an independent production audit. Formula/native measures do not become editable, and a native measure's semantic-model definition and writeback rights must remain unchanged.

**Must:** resolve the existing owner, complete input/formula record, native internal dimension IDs and compatible layout hash before attaching `anchor_config` to that measure's `manage_measures` entry. Preserve measure identity and registration. Labels, semantic field references and internal dimension IDs are distinct. Never invent `dimension_hash`, transplant it from a different layout, or assume a retained hash remains valid after pivot changes. Use the supplied seed-zero XXH3-64 producer over every current ordered pivot dimension, not the selected anchor subset. Base specs accept per-measure anchor options; saved-owner updates use the same shared implementation. Reject stale saved hashes rather than silently rewriting other anchors.

Make the intended entry intersection visible. An annual assumption belongs at the Year subtotal, not January; an unused axis needs its appropriate All/Total intersection. The guide's `totals_config.column_grand_total` example addresses columns, not row-grand-total requirements. Configure total visibility through its own target-build contract and preserve unrelated layout.

**Prefer:** anchoring only where it matches the business assumption's grain, with appropriate nonadditive aggregation for prices/rates. **Avoid:** treating `display_at_all_levels` as permission to edit descendants or distribute values. Anchoring, dimension keys, filter context, lookup, bounds/locks and allocation rules are separate concerns. Do not turn the historical URL feature flag or generated case count into a permanent prerequisite, product limit or runtime-pass claim.

**Workflow and validation:** create/retain the measure, select supported row/time levels in the anchor UI, choose descendant display, expose the entry intersection, save and read back. On authorized test resources, verify entry at that intersection, descendant display versus editing, sibling isolation, annual/All-Total semantics, formula consumption, scenario isolation, mixed-grain totals, layout-change compatibility and save/reopen. Repeated display of one assumption must not become accidental double counting. Do not infer native correctness from a generated matrix of anchor combinations.

##### Anchor Grain and Entry Locations

Selected dimensions form one joint intersection. With anchoring enabled, at least one dimension across the two selectors is required by the latest supplied design; neither individual selector is mandatory. The empty native defaults above are not an enabled dimensionless constant. Quarter and Month identities without their required calendar parents remain unresolved; the examples use year-qualified periods.

| Row selection | Column selection | Enabled selection valid | Intended grain and entry |
| --- | --- | --- | --- |
| None | Year | true | One shared annual assumption at All rows x Year subtotal. |
| None | Year + Quarter | true | One shared year-qualified quarter at All rows x Quarter subtotal. |
| None | Year + Quarter + Month | true | One shared month at All rows x Month. |
| Region | None | true | One regional value across periods at Region x Total column. |
| Product | Year | true | One annual product value shared across regions, not one value per region-product pair. |
| Region | Year | true | One annual value per region. |
| Region | Year + Quarter | true | One quarterly value per region, not separate Year and Quarter anchors. |
| Region + Product | Year + Quarter | true | One value per region-product-year-quarter intersection. |
| None | None | false | Invalid enabled selection; no inferred Constant/Grand Total exception. |

For an input-capable measure, direct entry belongs only at its valid anchor intersection and remains subject to permissions and locks. Annual input belongs at Year subtotal, never January or the first visible month; quarterly input belongs at Quarter subtotal. A collapsed anchor is not replaced by a higher-level editable cell. Expand the relevant level or expose its subtotal to access it.

##### Display, Allocation and View Changes

Anchoring restricts direct entry and display; it does not create formulas, time intelligence or a dynamic lookup engine. Under the applicable existing Average (Leaf) and distribution settings, a rate/factor can copy unchanged into eligible leaves. Other aggregation/allocation settings retain their existing behavior: never force Average (Leaf) for every measure or copy an absolute pool as if it were a percentage. Underlying values must remain available to existing formulas even when repeated instances are hidden.

**Anchor-read-only is not locked.** A child denied direct entry solely by anchoring must remain eligible for otherwise authorized allocation from the anchor. Independent security restrictions and locked children remain protected. A blanket rule allowing allocation for every other reason for read-only status was not settled; verify the actual writer and allocation path rather than broadening permissions.

With Display measure across all levels on, non-anchor instances remain visible and read-only; copied values may be shown distinctly. With it off, omit whole non-anchor measure instances where the layout permits, preserving other measures:

| Layout | Intended hiding behavior |
| --- | --- |
| Measures on rows | Show a Region-anchored measure row under Region, not every Product; retain Product Revenue rows. |
| Measures inside time groups | Show a Quarter-anchored measure at Quarter subtotals; omit its monthly measure columns while retaining monthly Revenue. |
| Measure outside the time hierarchy | Restrict that measure's own time block to the anchor level, not every other measure's time detail. |

The updated deck illustrates surviving shared row/column cells as read-only: OFF hides repeated measure instances where supported, not necessarily every shared cell. Exact target-build gray-versus-blank rendering is not runtime-tested. Collapsing can remove all visible anchor instances without changing stored values; the exact empty-state experience remains open. Tooltips should distinguish where direct input is available from genuine locks and describe display-only measures without implying editability.

Actual removal of a configured source dimension has a different supplied design rule: discard/reset its anchoring and treat the measure as ordinary, preserving unrelated settings and data. Re-adding that dimension requires configuring anchoring again. Do not trigger this reset for collapse, a hidden subtotal, a visibility change or omission from a pivot view, and do not infer a native reset payload from the policy.

For pivots, evaluate the effective view: an empty axis selector may inherit all dimensions. The proposed conservative policy permits direct entry only at a complete anchor intersection, not merely wherever anchor fields are present. Missing non-anchor dimensions alone does not invalidate an otherwise complete intersection; totals above or detail below it are not the same location. However, partial-pivot writes, single-member-filter exceptions and deliberate allocation across multiple anchors were left unresolved. Do not turn the proposal into a confirmed blanket ban or permission. Changing the view must not silently change the configured anchor or rewrite stored values.

##### Anchor Configuration and Worked Examples

The supplied UI design uses Enable Anchor Measure, Row Dimension and Column Dimension multi-selects, and Display measure across all levels. The Manage Columns/Show Columns anchor-only popup identifies the measure and edits the same configuration with Apply/Cancel. The entry-point choice between a menu, direct icon and status column was not finalized. The discussion's misspelled `display_at_non_achored_level` is conceptual, not a substitute for the source-backed `display_at_all_levels`; keep UI `is_enabled` distinct from the native subtree.

These are illustrative arithmetic expectations, not native formula syntax, defaults or executed product tests. Rate/factor examples assume the applicable existing copy distribution. Worked business arithmetic remains illustrative, not executed native behavior.

| Business assumption | Anchor grain | Illustrative calculation |
| --- | --- | --- |
| Corporate salary increase | Year | 100000 * 1.04 = 104000 |
| Regional benefits | Region x Year | 8000 * 1.22 = 9760 |
| Hiring growth | Department x Year x Quarter | 100 * 1.05 = 105 |
| Monthly inflation | Year x Quarter x Month | 20000 * 1.003 = 20060 |
| Product price increase | Product x Year, shared across regions | 200 * 1.05 = 210 |
| Productivity | Region, across periods | 50000 * 1.10 = 55000 |
| Commission | Sales Role x Year | 125000 * 0.08 = 10000 |
| Expense reduction | Department x Year | 50000 * 0.92 = 46000 |
| Manufacturing scrap | Plant x Year x Quarter | ceil(10000 / 0.975) = 10257 |
| Seasonality uplift | Year x Quarter | 1000 * 1.15 = 1150 |

Annual salary increases do not compound monthly. Monthly inflation here is a period-specific uplift, not the annual-uplift lookup example. Hiring growth needs separate hire-date/phasing logic; commissions need eligibility rules; scrap rounds gross production up to whole units. A quarterly seasonality uplift may apply to a month in that quarter through existing calculations, not a new anchor lookup.

Combined monthly compensation applies one annual raise and the appropriate regional benefits, without copying example identities:

| Base monthly salary | Calculation | Monthly cost |
| --- | --- | --- |
| 8000 | 8000 * 1.04 * 1.22 | 10150.40 |
| 6000 | 6000 * 1.04 * 1.26 | 7862.40 |
| 5000 | 5000 * 1.04 * 1.18 | 6136.00 |

The total is 24148.80. Reporting examples can show native YTD Revenue at a useful total and formula Operating Margin at Quarter while preserving their existing calculation semantics; do not infer a both-axes-empty anchor or a new YTD formula from that presentation example.

Extend authorized native acceptance to all three layouts, shared Product-only assumptions, anchor-only read-only allocation versus locked children, collapse versus actual dimension removal, formula/native display, and effective pivot context. Test paste/import/bulk enforcement, new members, sparse combinations, filters and coarser anchors over unequal leaves. Preserve the unresolved policy/UX questions instead of marking them passed from synthetic examples or previous presentation validation.

### F28 Header Footer

**Required authoring default (v20):** use [content-based sizing with a buffer](report-presentation-defaults.md#content-determines-the-saved-header-height) for every rich-text report description. Synchronize the outer customTitleHeight and inner canvas/text/grid heights; do not use a large fixed minimum.

Intent: show/hide headers and footers and edit text/image/chart/KPI canvas content. showHeaderFooter binds `inforiverProps.showHeaderFooter`, defaults true, and replaces the boolean on update.

Native partial binding value:

```json
{"showHeaderFooter":false}
```

The separate headerFooterConfig is editor state: boolean `showEdit`, `showOverlay`, `showRuler`, `textSelection`; string `activeEditor`; selected-element/chart/config/copy references. It has no bind declaration in the inspected file. Setting `showEdit` false resets runtime options; other reducers merge or update overlay flags. Do not serialize selection/clipboard/editor state as the header layout.

Planning custom-title binding persists `chartCustomTitle` under `inforiverProps`, including `primaryTitle`, `formattedTitle`, `customTitle`, `customTitleHeight` and `customTitleWidth`. The title reader uses `customTitle` when its `elements` collection is non-empty; otherwise it builds the automatic field-list title. Setting only a registry name or `formattedTitle` does not establish this visible canvas override.

For a professional Planning description, follow [Planning Headers and Connected Steps](design-standards.md#planning-headers-and-connected-steps). The inspected canvas constructor represents text with `type: 'TEXT'`, HTML in `content`, a local element `id`, numeric `position.top/left`, string `dimension.width/height`, and grid `layout.x/y/w/h/i/static`. The canvas carries `elements`, `layout`, `layoutType: 'CUSTOM'` and `containerMeta.width/height`. Canvas constants define 64 horizontal grid units and a 10-pixel height unit; these are not Intelligence fractional canvas coordinates. Resolve container size and reserve enough title height without silently shrinking an existing workbench.

Author a meaningful bold title, concise business-description paragraphs and appropriate Source/Input/Formula legend using supported text HTML, with explicit Arial on title/body/emphasis/legend runs. Preserve native text/canvas formatting siblings and local identities; do not substitute a Lexical document, a React component, editor/clipboard state or guessed CSS/DTO properties. Visibility also depends on the separate header/title controls. Source-backed compiler tests cover six distinct descriptions and the native text/layout shape; native save/readback and actual rendered fit must still be checked for each deployment.

HeaderFooter.service imports sanitization, presets, layouts, and canvas helpers; imports alone do not prove ALM sanitization. **Gap:** full dynamic-content evaluation, image/chart/KPI canvas leaves, asset packaging, renderer sanitization call sites, and complete export/import treatment. No automatic HTML sanitization or silent-tag-drop guarantee is made.

### F29 OnChangeFormula

Intent: define behavior triggered by data-input edits, including value updates and notification-related processing. DataInputConfig uses `on_change_formula: Option<String>` with serde default; it is not the same as calculated-measure `formula` or allow-input permission evaluation.

Native partial DataInputConfig settings (not a complete column):

```json
{"on_change_formula":null,"allow_input":"Edit","bound_to_filter_context":true}
```

`disable_write_access` is `skip_deserializing`; `user_permission` is `skip_serializing`; `bound_to_filter_context` deserialization default is true. Do not turn these native serde annotations into guarantees about every HTTP/ALM layer.

OnChangeFormulaService checks UI `measure.onChangeFormula`, defines type-specific value conversion, and exposes `processAndUpdateValue`; it can update data, not merely notify. It distinguishes checkbox strings, options, multiselect arrays, dates, numeric conversion, and text validation. **Gap:** UI-to-Rust name conversion, complete allowed formula functions, execution ordering/error handling, actual save/export/import formula handling, and mail safety. Do not confuse this service with `AllowInputFormulaService`.

For approval actions, use the [transition guards](#editability-and-transition-guards): resolve initiating fields and targets, distinguish user from programmatic changes, prevent cyclic/repeated actions, and separate edit/submission/decision/release stamps. A viewer or model refresh is not itself an accepted input edit. Function names and illustrative editor snippets do not establish complete native action syntax or transactional execution.

#### On Change Workflow Authoring

Separate the responsibilities: **inputs capture; formulas calculate; conditional formatting explains; Allow Input gates; On Change writes deliberate event effects; notifications alert**. A calculated variance should remain a formula when it must track its dependencies. Use an event-written SubmittedVariance only when the business needs the value captured at a valid submission; identify the source/target intersection and submission revision. A source-volume refresh may change a live impact but must not silently recertify a captured decision.

Design each handler as **initiating field -> valid transition/condition -> target intersection -> accepted target value**, with field ownership, reset policy and failure behavior. Use the existing [approval guards](#editability-and-transition-guards) for actor eligibility, current revision, pending review and package boundaries. Resolve actual status internal values and supported native function syntax; Working/Under Review in this video and In Progress/Pending in the preset-style deck are different configured vocabularies, not interchangeable enums.

| Guide-reported event/condition | Intended target writes in that demonstration |
| --- | --- |
| Planner changes to Submitted | Manager becomes Under Review; Submitted Date receives DATE(NOW()). |
| Planner changes to Working | Submitted Date clears under the video's chosen current-state policy. |
| Manager changes to Approved | Approved Date receives DATE(NOW()). |
| Manager changes to Under Review | Approved Date clears for another review. |
| Manager changes to Rejected | Planner becomes Working; Approved Date clears. |

The locally inspected On Change screenshot shows the planner submission/status and submission-date branches in a different report from the saved input sample. It does not show all manager branches executing. The guide reports those additional branches; the supplied definition has eight empty on_change_formula strings, so none of these scripts is established as saved there. The visible Working row still has a submission date: the image alone cannot establish handler execution, chaining or clearing behavior.

Do not assume SETVALUE on Planner Status invokes that field's handler. If rejection must clear the submission date, specify and verify that effect explicitly instead of depending on unverified event chaining. Use a valid transition, not just status equality, to guard repeated selection, retries, loops and unwanted date rewrites. A date obtained from DATE(NOW()) is a current date marker, not a precise event timestamp or durable history. Define retention separately for submitted, returned and approved milestones; clearing workflow state must not erase the proposal amounts or explanation unless the requested policy explicitly requires it.

Validate completeness and eligibility before committing status/lock/notification effects through the supported route. Test partial failure and concurrency; the example does not prove atomic multi-target SETVALUE writes, automatic rollback or transactional review/versioning. Revalidate the submitted revision when deciding, and ensure a rejected/withdrawn request cannot also finish as approved through a stale event. Verify target-type conversion and whether this trigger type supports On Change; a Date/Person target does not prove equivalent trigger support.

**Notification design:** the guide narrates NOTIFY_USER with a recipient/message and Teams delivery, but neither a saved event script nor end-to-end notification delivery was verified in this package. Resolve supported function signatures and effective identity from the target engine rather than inventing user-function spellings. Use a governed recipient, clear organization/period/scenario/request/action context and one configured notification path per transition. Test authorization, correct recipients, duplicate/retry/unchanged-status handling and message delivery independently. A View Report link opens context; it is not an approval action. Documentation learning does not authorize sending messages.

**Functional handoff:** record grain and approval identity, each field's placement/type/default/owner, trigger, allowed prior/next states, source/target coordinates, calculated versus captured values, edit predicate, formatting condition/scope, recipient, resets and failure/replay handling. On approved test resources exercise edit -> submit -> review -> reject -> revise -> resubmit -> approve -> authorized reopen. Verify totals and detail, collapsed descendants, null/blank inputs, bulk/programmatic changes, save/reopen, unchanged periods/scenarios/siblings, and stale competing decisions. Source-member persistence is a separate acceptance path, not satisfied by an inserted row appearing on screen.

##### Cross-Industry Input and Workflow Cases

These twenty cases retain the guide's distinct business lessons as illustrative acceptance fixtures, not configured policies, native execution results or reusable customer payloads. Unless noted, resolve the scenario/version and current period as well as the row grain. Use the preceding event/editability contracts rather than inferring executable scripts from this table; numbers are worked examples, not defaults.

| Case and decision grain | Inputs and intended process | Discriminating acceptance check |
| --- | --- | --- |
| 1. FP&A: department/month forecast | Baseline 120,000, proposed 138,000, rationale and one review state; capture the 18,000 change on submission and lock that monthly request. | Reject, revise and resubmit without closing another month or carrying forward an earlier approval. |
| 2. Sales: customer/product/period discount | Discount rises from 8% to 14% on 500,000, an incremental 30,000 reduction; route the exception to the configured reviewer. | Test 9%, 10% and 14% with explicit threshold inclusivity. Do not equate 6 percentage points with a 6% relative increase. |
| 3. Workforce: team/role/start period | Request three positions at 8,000 each, a 24,000 monthly cost; keep justification, start date and Finance/HR decisions scoped to the submission. | Approval of two positions belongs in a separate approved quantity, not an overwrite of the requested three. Planning does not create employees. |
| 4. Capex: project/program | A 1,200,000 request crosses an illustrative 1,000,000 review threshold; use staged review and separately authorized release where required. | Compare a 900,000 control; a manager decision must not count as final if a further stage is required. |
| 5. Procurement: supplier/material/period | Price rises from 4.00 to 4.40 on 100,000 units, a 40,000 impact; retain price, volume, reason and the captured submission. | Source volume refresh changes a live calculation, not the already-approved snapshot; choose the policy explicitly. |
| 6. Manufacturing: plant/cost-center/month overtime | Requested 500 hours at 45 and a 1.5 premium gives 33,750; capture submitted cost and review. | Approved 400 hours is distinct from requested 500; preserve the proposal and test context and partial approval. |
| 7. Logistics: route/fleet/period fuel | Unit price 1.20 to 1.30 on 200,000 units adds 20,000; combine amount, confirmation and explanation. | Run all four confirmation/comment states. Confirm the chosen permission policy rather than trusting its UI description. |
| 8. Retail: store/category/campaign | Proposed uplift 75,000, multiple reason tags, one status and reviewer. | Several selected reasons still create one request, not duplicate submissions or concurrent Approved/Pending states. |
| 9. SaaS: segment/period churn | Churn rises from 2% to 2.5% on opening revenue 4,000,000, a 20,000 impact; capture the reviewed assumption. | Distinguish 0.5 percentage points from 0.5% relative change; blank revenue is not proved zero, and consolidated rates need appropriate weighting. |
| 10. Healthcare: hospital/service-line/month | Additional 200 staffed hours at 60 gives 12,000; include start date, operational reason and finance decision. | Test delayed start, partial approval and an unchanged sibling service line. Approval does not update a staffing/scheduling system. |
| 11. Professional services: project/role/month | Additional 160 hours at 100 gives 16,000 internal cost while billings stay unchanged; calculate margin and capture the proposed staffing impact. | Define whether rejection reopens one role/month or the whole project; an accidental total write is not package approval. |
| 12. Construction: existing project/work-package/period | Proposed 250,000 cost and 300,000 revenue, description, authorization date and review state; capture both values before locking. | Resubmission must not add the approved-plan delta twice. A new shared work package requires source master-data creation. |
| 13. Energy: site/asset-group/month | Move 180,000 maintenance spend from November to December, with confirmation/date/explanation. | Conserve the annual total, test both period targets and a closed period, and do not assume cross-period writes are atomic. |
| 14. Education: campus/program/term | Add 40 students at 5,000 net tuition, a 200,000 impact; capture enrollment and revenue for term review. | Fall approval must not close spring; avoid cross-listed enrollment double counting. Shared new programs require governed source members. |
| 15. Nonprofit: grant/category/period | Reallocate 20,000 from Travel to Field Services; readiness checks a balanced package before review. | 20,000 out but 19,000 in leaves a 1,000 imbalance. Check both targets and replay; approval alone does not establish grant compliance. |
| 16. Real estate: property/unit-type/month | Ten occupied units at 1,800 instead of 1,700 adds 1,000 monthly; capture rent, occupancy, date and rationale. | Six occupied units imply 600, not 1,000; do not sum rents as a portfolio rate. New shared properties belong in source master data. |
| 17. Corporate finance: business-unit/month certification | Review a 2,400,000 forecast with checkbox/comment/status and certification date; define which completion condition closes editing. | Run the permission truth table and authorized reopening while reviewer controls remain usable. This is not an accounting-system close or immutable audit history. |
| 18. Management reporting: existing category/period | Insert a local difference row: 900,000 less 300,000 equals 600,000; exclude it from the ordinary category total. | The original total remains 1,200,000, not 1,800,000; test expanded/collapsed and filtered views. |
| 19. Category planning: category/period adjustment | Append one limited local Number template at Category, with illustrative 100 default and intended total participation. | Three eligible category contributions total 300 for the specified scope; do not repeat at Sub Category or infer new database members. |
| 20. Enterprise master data: product and valid region/channel combinations | Govern a new SKU through its actual source table, then plan 10,000 units at 2.50 for 25,000 revenue. | Verify key uniqueness, parent, source save, no-history visibility, valid combinations, persistent input and another authorized consumer. |

The approvals-deck supplement adds regional readiness, capital concentration/release, parallel candidate-version review and policy-driven selective reopening. Reuse the existing [worked approval traces](#worked-functional-patterns) and [PowerTable/model policy](#powertable-and-model-policy) rather than creating duplicate scripts or inferring new saved approval settings from this guide.

### F30 Allow Input Based on Formula

Intent: gate editability for data-input measures and static-row conditions. Exact AllowInputType variants are unit strings `Edit`, `ReadAndEdit`, and externally tagged `BasedOnFormula(String)`; default is `Edit`.

Native partial setting with the formula text used in the service's illustrative comment; JSON syntax is checked, formula execution is not:

```json
{"allow_input":{"BasedOnFormula":"50 > 100"}}
```

AllowInputFormulaService compiles against the data-store schema, caches by measure/row position, and records reverse dependencies. In row/column batch evaluation, boolean conversion uses `unwrap_or(false)`: unresolvable boolean values are noneditable in these inspected paths, despite an earlier comment claiming true. Compilation errors propagate via `?`; that is a different failure path, not proof of an Edit fallback.

**Gap:** callers' error handling, cache invalidation lifecycle, permission/approval precedence, formula function availability, native-to-columnMeta mapping, and ALM import acceptance. Never promise that a broken formula makes a cell editable, and do not export compiled expressions or runtime lock caches.

For workflow use, combine model ownership/version/period flags with current local state as illustrated in [approval editability](#editability-and-transition-guards). Keep numeric/comment editability, submission readiness and reviewer decision permissions separate. A returned/reopened state cannot override a closed period or existing approved decision by itself; the conceptual truth table is not a substitute for native compilation and enforcement tests.

#### Formula-Based Editability Workflow

Treat the input expression as **May this user edit this intersection now?** True permits input and false prevents it within the input-rule evaluation; neither result grants report access or overrides independently enforced permissions. The supplied Inputs/Formatting/Workflows guide shows Edit Only, Read and Edit, and Based on Formula UI choices. These labels are not native enum literals to emit without the existing adapter contract.

The guide distinguishes narration from its recorded expression. In conceptual business notation, the recorded rule is `AND(Confirmed != true, ISBLANK(Comment))`: editable only while unconfirmed AND blank. That is different from the proposed policy `NOT(AND(Confirmed == true, NOT(ISBLANK(Comment))))`, which locks only when confirmed AND a comment exists. The latter is an alternative design, not an observed saved correction.

| Confirmed | Comment | Recorded rule allows input | Alternative both-complete policy allows input |
| --- | --- | --- | --- |
| False | Blank | Yes | Yes |
| False | Present | No | Yes |
| True | Blank | No | Yes |
| True | Present | No | No |

Choose the business policy explicitly before constructing the native expression. This four-case Boolean fixture does not establish native coercion of null checkboxes, empty strings or whitespace-only comments. Define meaningful commentary and test those cases using the actual engine; a visible blank and ISBLANK need not be equivalent. An invalid expression or failed permission evaluation must not be interpreted as a permission grant.

**Authoring workflow:** identify the editable field and row/column/scenario scope; resolve existing policy/status fields; write a positive permission predicate; test its truth table; apply through the field's Allow Input configuration; verify both permitted and rejected edits after save/reopen. For period-varying input, evaluate the actual cell period rather than applying a selected approval-package period indiscriminately to all visible months. Check leaves, totals, distribution into locked descendants, bulk entry and alternate Pivots separately instead of assuming one cell test covers every path.

Keep amount/comment and reviewer-decision predicates separate. Submission may close the amount while an authorized reviewer can still reject it; do not lock the control required to reopen the process. Rejection, withdrawal or reopening cannot bypass closed-period/version policy, nor can a planner state of Reopened override an unchanged Approved decision. Reuse the [approval guards](#editability-and-transition-guards) for owner/reviewer eligibility, stale-state checks and independent field protection.

**Acceptance example:** submit one department's November input, verify November is closed to the planner, leave unrelated December/scenario inputs unchanged, then reject as an authorized reviewer. Reopening succeeds only if owner, version, period and workflow conditions all permit it. Test all four confirmation/comment combinations and preserve the original values and control-field identities. These are prospective behavior checks, not a claim that the supplied sample exercised them.

## Shell, Charts, and Connected Planning

### F08 Filter Context

#### Planning Input Context Authoring

**Default selection is required:** every configured context dimension must have an explicit, nonempty selection from valid model members in the Planning **Context** panel's dimension card. Honor the requested member; otherwise choose a suitable verified member rather than leaving context unselected. For single-select context require exactly one selected member (for example, the radio option on the ScenarioName card) and validate its saved payload, not just the enabled flag or a dashboard slicer/page filter. Budget 2027 is the current application's requested scenario, not a universal scenario/year default. A screenshot demonstrates the visible selection on that card, not save/reopen persistence on every sheet.

Use Planning filter context to select a dimension such as scenario/version without keeping it on visible Rows, while context-bound inputs remain specific to that selection. An ordinary page filter restricts displayed data; it does not by itself establish input storage context or security. The supplied guide is historical multi-surface saved-state evidence, not a universal properties envelope or newly tested live report. The Charts contract below is a different family and must not replace Planning's settings.

**Must:** resolve the owner, current semantic field, valid selected member, existing input-coordinate strategy and fresh properties/column records. Inspect `.properties` versus `.properties.properties` rather than flattening every envelope. Reconcile all applicable surfaces:

| Planning Surface | Authoring Responsibility |
| --- | --- |
| `superFilterAssignments` | A complete native assignment with `isContextDimension: true`, matching semantic-field references, single selection and selected-member payload. Retain the filter ID unless creating a genuinely new filter instance. |
| `visualState.filterContextSettings` | Enable context using the native shape; set note/comment context only when the business requests that scope. |
| Input record | Retain separate outer numeric binding and nested `DataInput.bound_to_filter_context` Boolean; use [binding across layers](#filter-context-binding-across-layers), not spelling-based conversion. |
| Dimension mapping and axes | Preserve verified stable keys and required descriptors. Once context is established, remove only the intended visible row assignment and reconcile dependent row metadata/order. |
| Visual/embedded/page filters | Preserve valid selections and registrations; remove only identified conflicting restrictions when explicitly replacing them. Do not erase every page filter or create absent mirrored state blindly. |
| Native context properties/hash maps | Preserve opaque state through the current writer. Do not invent/transplant hashes or reset context caches to force a match. |
| Connected sources/consumers | Verify that scenario/version meaning and keys survive the actual query output, join/filter grain and consumer selection. Source context configuration alone does not establish propagation. |

An empty nested `filterContextDimensions` array or null hash in one exported object does not establish disabled context: the historical example has settings and context assignments on other surfaces. Conversely, an enabled flag or a ScenarioID mapping alone does not establish working input separation. Notes/comments are independent scope choices, not compulsory true defaults.

**Example:** for a request to switch between two planning versions while showing Region -> Team -> Person, establish a valid single-select version context, bind the requested inputs, and then remove Version from visible Rows. Keep region/person/period identities and unrelated filters unchanged. Verify that a distinctive input saved under version A is absent under B and returns when A is reselected; do not copy the guide's member names or context hashes.

**Prefer:** the supported native settings workflow, followed by save/reopen and a fresh export. For a populated sheet, retain its existing key semantics until an explicitly authorized test copy or migration/rollback plan demonstrates the change; creating a copy or test value is not implicit authorization from this documentation. **Avoid:** treating a historical workload proxy URL as a public write API, using another artifact's credentials/runtime entity ID, or always creating a timestamped replacement Plan.

**Validation:** check context selection survival, absent intended row dimension, retained filter cards, per-measure binding, and nonconflicting embedded/page selections. On authorized resources verify scenario isolation and return-to-context persistence, notes/comments when requested, connected grain and security independently. Investigate a blank grid using actual requests, selected members, conflicting filters, keys, source results and edit rules; distinguish it from a missing filter card. No cache-reset or equality-to-positivity rewrite is a generic context repair.

#### Charts Context Display Contract

Intent: configure which context-specific chart features are shown. filterContextSettings binds to `hiddenProperties.filterContextSetting` (singular), not an inferred ALM property named after the feature folder.

| Native path | Exact initial value / type |
| --- | --- |
| `filterContext`, `filterContextKey`, `hash` | Strings; initial `none`, empty, empty respectively. `none` is an observed default, not an exhaustive context enum. |
| `type` | `visual` or `measure`; initial `measure`. |
| `suppressFilterWarning`, `enableFilterContext` | Booleans, initially false. |
| `filterContextJson` | Map from string to string array, initially `{}`. Runtime keys require context production, not invented hashes. |
| `feature.showFilterContextCF`, `showFilterContextAnnotation`, `showFilterContextNotes`, `showTitle` | Initially true. These names are nested under `feature`. |
| `feature.showMeasureLabel`, `showFilterContextTextComponent`, `showAllContextComments` | Initially false. |

`updateSync` shallow-merges the payload. If `feature` exists but `showFilterContextNotes` is undefined, it sets notes from annotation visibility or true; it does not deep-merge every omitted feature member. Native complete **feature toggle subtree only**:

```json
{"showFilterContextCF":true,"showFilterContextAnnotation":true,"showFilterContextNotes":true,"showMeasureLabel":false,"showTitle":true,"showFilterContextTextComponent":false,"showAllContextComments":false}
```

**Gap:** actual hash/context producers, hidden-property encoding, visual-type applicability, saved metadata, and ALM import/export mapping. Do not equate this Charts feature with Planning data-input context storage merely because names overlap.

### F18 Infobridge

Intent: append/merge/join/query transformations with background processing and optional writeback. Native UI request shapes from infobridge.types are not the published Connected Planning definition.

| Native request / response | Shape |
| --- | --- |
| `IAppendQueryPayload` | String `name`; `queries: {id: string or number}[]`; `dateOptions: IDateColumnDetails[]`; `dateColumns: IColumnDetails[]`. |
| `IDateColumnDetails` | String `name`, string `alias`, boolean `isTimeInterval`. |
| `IMergeQueryPayload` | String `name`; `queries: IMergeSource[]`; date options/columns. `IMergeSource.sourceMeasures` is the declared object with string `id`, `alias`, `name`, `aggregationType`, not the separate selected-query array shape. |
| `ISelectedJoinQueries` | Numeric `sourceId`, string `sourceName`, string-array `joinColumnName`, optional boolean `isBaseQuery`. |
| `IQueryDetails` | String `name`, numeric `type`, numeric `linkedVisualId`, string `id`, string-array `jobId`; optional alternate job fields and boolean `sourceParquetExists`. |

AppendQuery.createAppendQuery calls `infoBridgeAPIService.appendDataSource(workloadId,payload)`, then stores job IDs and refreshes query/group data on allowed response codes. These runtime job fields are not definition fields.

The inspected InfoBridge worker dispatcher handles separate pre-process, source-load, visual-update, and Blend preparation events. V1/V2 handlers differ; `IB_LOAD_V2` uses query GUIDs and can resolve a visual identifier before dispatch. Dispatcher context/billing/telemetry caches are runtime data, not user-authored JSON.

#### Transformation Discovery Inventory

The frontend infoBridgeConstants step enum declares the following 26 numeric codes. This is a source-derived discovery inventory, not 26 closed payload contracts or evidence that every branch executes in the target service:

| Code | Declared transformation | Code | Declared transformation |
| --- | --- | --- | --- |
| 10 | LOAD_COLUMN | 20 | CALCULATE_SUBTOTAL |
| 30 | DISABLE_SUBTOTAL | 40 | UNPIVOT |
| 50 | PIVOT_TABLE | 60 | RENAME_COLUMN |
| 70 | DATE_COLUMN | 80 | GROUP_BY |
| 90 | PIVOT | 130 | ADD_MEASURE |
| 140 | APPEND_QUERY | 150 | MERGE_QUERY |
| 170 | ADD_DIMENSION | 180 | FILTER_ROWS |
| 190 | EXTRACT_COMMENTS | 200 | FIND_AND_REPLACE |
| 210 | SORT_BY | 220 | FORMAT |
| 230 | JOIN_QUERY | 240 | EXTRACT_COLUMN |
| 250 | SPLIT_COLUMN | 270 | CONDITIONAL_COLUMN |
| 280 | UNNEST_COLUMN | 290 | SPLIT_MEASURE |
| 300 | COLUMN_DATA_TYPE | 310 | REMOVE_COLUMN |

The nearby Constants enum declares 22 of these, omitting APPEND_QUERY, MERGE_QUERY, COLUMN_DATA_TYPE and REMOVE_COLUMN. Resolve the importing caller/dispatcher before selecting a registry; neither copy establishes the other four as unsupported. Inspect each selected transformation's constructor, validator and executor to resolve `meta.value`, output schema, source references and ALM restoration. The observed `transformationSteps[*].meta.type` placement does not license a top-level `type`/`stepType`, nor does an enum name establish an executable transformation.

Use the business operation to choose a candidate: normalize types/grain before append, join only with verified cardinality, and distinguish measure calculation from metadata renaming. Preserve ordered steps and validate actual output aliases. These discovery names do not authorize copying cached rows, counts or job state, and they do not prove downstream refresh. See the [portable graph](#observed-portable-graph-and-consumer-records) for separately observed records.

#### Detail-to-Reporting Contribution Normalization

Use this pattern when a detailed Planning query must contribute to a common reporting result, such as employee compensation appended with other financial contributions. Keep a reusable driver query at the detail needed by its consumers, and create a separate normalized reporting contribution. This is a business-to-transformation contract, not a mandatory P&L application, fixed account mapping or new native schema.

**Evidence boundary:** the supplied InfoBridge screenshot shows the source query, an initial pivot, added dimensions/measures, column removal and a final normalization pivot before append. The corresponding saved definition was inspected for all thirteen ordered transformation records and their operator values, without inspecting employee data rows. This establishes observed configuration, not successful execution: the screenshot is still loading, and neither its step labels nor saved `isValid` flags establish materialized output, reconciliation or refresh propagation.

##### Observed Workforce-to-Reporting Sequence

| Stage | Observed operation | Reusable contract |
| --- | --- | --- |
| 1 | Load a Planning source (`10`) | Resolve the actual owner, selected measure, scenario and period fields. Do not copy source/query/visual identities or an example's source selection. |
| 2 | Initial Pivot Table (`50`) | Select the required monetary measure with `sum`, retaining region, department, employee and scenario detail and the period in Columns. Exclude eligibility/editability flags, exchange-rate drivers and other measures not needed by this contribution. This first pivot still has employee-level grain; it is not the final reporting aggregation. |
| 3-4 | Add Dimension (`170`) | Create the reporting group and account fields through executed expressions or a verified mapping. The illustrated fields are `PNLGroup` and `AccountName`; a compensation classification is an example, not a universal account default. |
| 5-11 | Add Measure (`130`) | Map the contributed amount into its common reporting measure and create compatible, typed non-contribution measures only where zero is the established business meaning. Preserve currency, units, sign and unknown-value semantics. |
| 12 | Remove Columns (`310`) | Remove the original detail-value measure after its normalized replacement exists. In the inspected record this removes the original compensation measure; the caption "Keep only the common P and L outputs" does not by itself prove employee/department detail was removed. |
| 13 | Final Pivot Table (`50`) | Explicitly aggregate the common additive measures to the agreed reporting grain and remove employee/department dimensions that are no longer part of that grain. This step performs the grain reduction; hiding or dropping detail columns alone does not. |
| Downstream | Append normalized contributions | Append only after every input satisfies the same logical keys, measure meanings and compatible materialized schema. Appending does not repair mismatched grain, types or missing fields. |

For the illustrated logical reporting contract, Rows contain `RegionName`, `ScenarioName`, `PNLGroup` and `AccountName`; `YearMonth` remains the canonical period in Columns. The complete logical grain includes all five fields even though the period is not displayed in Rows. Adapt these fields to the actual request/model, retain stable keys where required for matching, and follow [Connected Results and Freshness](#connected-results-and-freshness) for date-axis and native persistence checks. If currency or another business context remains variable, convert through a verified rule before aggregation or retain that context in the agreed grain; do not silently combine unlike amounts.

The observed wide contribution has seven logical measures:

| Common output | Workforce contribution in the inspected configuration |
| --- | --- |
| `Plan Gross Revenue` | Typed structural zero |
| `Plan Net Revenue` | Typed structural zero |
| `Plan COGS` | Typed structural zero |
| `Plan Compensation` | Cast of the resolved compensation-in-reporting-currency measure |
| `Plan Other Opex` | Typed structural zero |
| `Plan Depreciation` | Typed structural zero |
| `Plan Units` | Typed structural zero, not employee headcount |

These are illustrative output aliases, not required names or seven mandatory measures for every Plan. The inspected expressions use `CAST(0.0 AS DOUBLE)` and a cast of the selected compensation measure to `DOUBLE`. Resolve the actual engine's expression validator, field quoting and required numeric type; financial precision requirements may require a different supported type. Never substitute zero for a missing lookup, unknown amount, conversion failure or absent required source. Do not negate expenses simply to match this example: reconcile the intended reporting sign convention and downstream formulas.

##### Operator and Ordering Rules

- Preserve the query's owning `sourceId`, its actual registered `queryId` and ordered `transformationSteps`. In the portable records the operator is `transformationSteps[*].meta.type`, with operator-specific `meta.value`; native transformation APIs have their own request envelopes. A UI step name/description is explanatory text, not an executable expression or schema declaration.
- The observed pivot value contains `sourceDimensions`, `sourceColumns`, `sourceMeasures`, `removeColumns` and `isValid`. Resolve selected field identities against the output of the immediately preceding step. The final pivot selects the four reporting dimensions, the canonical period in `sourceColumns`, and the seven common measures with `aggregationType: "sum"`; its `removeColumns` excludes employee and department. This is an observed branch, not permission to manufacture field descriptors or assume every pivot is display-only.
- Add Dimension/Add Measure records in this example use `columnName`, `formulaQuery` and `isValid`. A selected source measure must exist before its expression is evaluated; a normalized measure must exist before the old measure is removed. Additions must change the executed pipeline, not merely the field catalog.
- The inspected Remove Columns value uses `sourceColumns` to identify fields to remove. Distinguish that operator's field list from the pivot operator's `sourceColumns` period selection; identical property names do not imply identical semantics across operators.
- Keep independent contributions in a common schema without a detail-to-detail join. Append preserves contributing rows; do not use deduplication to hide duplicate inputs or introduce a join that multiplies employee/product rows. Aggregate the appended result at the required reporting grain where necessary. Never sum ratios, rates, flags, balances or distinct headcounts merely because additive monetary measures use `sum`.
- Where reporting classifications require several accounts or effective-dated mappings, resolve their cardinality and allocation before reducing away the necessary detail. A single constant group/account is valid only for a genuinely single-class contribution; it must not collapse distinct payroll components or create duplicate compensation.

##### Normalization and Append Acceptance

1. **Declare the contract first.** Record source and target logical grain, required keys/context, aliases, field roles, primitive types, currency/units, sign conventions, additive measures and structural-zero rules. Separate native pivot roles from the actual output representation; inspect period helpers/generated field names rather than assuming a logical period always materializes as one plain column.
2. **Track the schema after each step.** Reject references before creation or after removal, duplicate aliases, missing reporting keys, mixed numeric/string types and leftover detail fields that unintentionally preserve employee-level grain. Inspect the final ordered rules and materialized schema, not only initial source metadata or the final step caption.
3. **Prove the reduction.** For a contribution intended to be unique at the common key, assert no duplicate keys after normalization and reconcile additive totals before/after by region, scenario and period, with an explicit tolerance appropriate to the selected type. Two synthetic employees contributing 100 and 150 to the same reporting intersection must become one contribution of 250, not two indistinguishable projected rows or a doubled amount. Distinct months/scenarios must remain distinct.
4. **Validate every append input.** Compare final names/aliases, roles, types and applicable column order/date representation across all contributions. Resolve existing query identities and dependency edges separately from visual consumers. Reject accidental inclusion of the same contribution twice, incompatible currency/units, overlapping leaf/subtotal streams and a source that has not materialized. Two distinct streams may legitimately share reporting keys; do not discard either with a distinct-row workaround.
5. **Reconcile the consolidated output.** Each domain's designated contribution must equal its normalized source total at the same context, while its declared non-contribution measures remain structural zero. Test empty inputs and unknown values separately. Check final report aggregations and derived ratios against the intended financial definitions, not only row counts.
6. **Keep evidence layers separate.** A synthetic fixture can prove aggregation arithmetic and rejection cases; saved-definition readback can prove ordered settings. Neither proves native query execution. Where authorized, execute upstream queries, normalized contributions and append in dependency order, inspect actual output schemas/totals and verify consumer bindings and edit/save/refresh propagation. Otherwise report those runtime gates as not run; do not invent a refresh endpoint or mark a loading screenshot as successful.

#### Preprocessing Is Materialization, Not Definition Construction

The V2 preprocessing entrypoint declares its own GUID-native job payload, not an extension of the V1 job type. Its `queryId` and `sourceId` are strings; optional `visualId` is string/null. Job context, job IDs, tenant identity, visited visuals and transformation/impact flags are runtime inputs, not fields to add to `connectedPlanning/infobridge.json`.

`getSourceMetadataV2` reads the existing source through `ibSourceRepo(ctx,{sourceGUID})`; an absent source raises `PLN_IB_0014`. Its cast to `IIBSourceBlob` is not a recursive content validator or a recipe for creating that record. `loadSourceDataV2` delegates to `materializeSourceV2`, passing the existing blob, engine and optional editable-source handoff. Trace the concrete factory before claiming a source type's configuration or output support.

The worker initializes/reuses DuckDB, creates a job directory and derives a temporary database filename from the source identity. That hash is not a Plan/source/query identifier allocation mechanism. Its notification helper targets the visual carried by the V2 job; this does not prove the V1 linked-visual fan-out or a complete dependency refresh cascade.

#### Source Variants and Consumed Native Metadata

The local source enum and both factories use numeric dispatch: V1 loader selection, V2 materializer selection. These are the nine cases in this preprocessing stage, not an exhaustive catalog of query transformation steps or publicly supported sources.

| Native source type | Value | Preprocessing behavior / consumed configuration |
| --- | --- | --- |
| APPEND | 20 | V2 adapter requires nonempty `meta.queries`, an array of linked query identity strings. It resolves query-index entries and query blobs; every linked query needs an existing `filePath`. It reuses the V1 Append loader through a lookup override. |
| MERGE | 30 | V2 reader reads `meta.queries[]` with `id` and `sourceMeasures[]` carrying aliases. It matches linked query identities and selects measures by alias before aggregate construction; a missing matching metadata entry raises an error rather than silently selecting no measures. This worker shape is not the UI interface's singular `sourceMeasures` object. |
| JOIN | 80 | V2 reader keys `meta.queries[]` by `sourceId`, reads `joinColumnName` and `meta.joinType`, and uses linked query metadata for selected fields. Multiple legacy/GUID identity candidates are checked. The consumed query-reference key is not permission to substitute a source GUID or a display name. Join type validation/translation still needs its concrete query builder. |
| CSV | 40 | V1 reads `meta.source.file.downloadUrl` and chooses its CSV loader; V2 dispatches to a dedicated CSV adapter. File metadata is stored-source input, not the root public SourceMeta shorthand. |
| JSON | 50 | V1 reads the same download URL path but selects its JSON loader; format-specific parsing/settings require that reader, not CSV assumptions. |
| XLSX | 60 | V1 also reads `meta.source.file.sheetName`; workbook/sheet selection and settings require its concrete loader. |
| PARQUET | 70 | V1 selects the Parquet loader from the stored download URL; this is not an encrypted-file recipe. |
| EDITABLE | 220 | V2 finalizer requires `meta.source.editable.mdeVisualId` and an upstream `sourceParquetProcess` handoff. The optional `mdeSuperfilter` affects the existing visual-scoped parquet reference. It propagates upstream errors and requires `sourceMeta`; it performs no new transform/upload. The MDE visual ID remains numeric despite GUID-addressed source storage. |
| SQL / SQL_SOURCE | 230 | SQL over referenced InfoBridge query outputs through `meta.sql` and `meta.queries`; see [SQL expressions over query outputs](#sql-expressions-over-query-outputs). This route does not require provisioning or configuring a separate SQL database. The dispatch case alone does not establish refresh or deployed SQL-feature support. |

`PLANNING: 10` exists in the local enum but neither factory handles it here; this does not classify Planning sources as unsupported by the product. The [published InfoBridge contract](https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/definitions/plan-definition#infobridge-configuration-connectedplanninginfobridgejson) additionally lists `ENCRYPTED_PARQUET: 170`, absent from this enum/dispatch. Neither public string/int type acceptance nor an export's named type may be sent unchanged to the numeric worker switch. Resolve the applicable import/controller conversion and reachable worker route.

For normalization over existing connected results, the V2 SQL-source adapter requires `meta.sql` and linked query identities in `meta.queries`; the referenced query blobs must already have materialized file paths. Its documented placeholder syntax is `{{query_id:<identity>}}`, with GUID-capable matching in this V2 implementation, distinct from the digits-only V1 matcher described in that file. This can implement an explicit group/projection over upstream results without writing forecasts to a SQL database. It is not a recipe for a physical SQL connection, a guaranteed refresh cascade, or permission to fabricate parquet paths. Keep input-source catalogs separate from post-transform query catalogs. Execute authored projections against synthetic data to check output names/types, grouping, exclusions, signs and version separation; record the local engine version and do not equate that test with deployed source materialization or native edit propagation.

The APPEND adapter's linked-query resolver uses the query-index repository and actual query blobs, carrying distinct query, source and legacy identities into the loader. Sanitized SQL table names are local identifiers, not replacements for repository GUIDs. Successful identity resolution is not proof of compatible dimensions, context, units or complete query-output registration.

For Planning sources, inspect `meta.honorSourceFilter` independently from query dependencies and output status. The inspected semantic request generator adds source super-filters to an RLS InfoBridge build only when the resolved source-isolation policy allows them; it retains global and resolved consumer filters separately. The rollout behavior matrix distinguishes RLS, source isolation, filter-honoring rollout and the stored toggle. False is not a permission/RLS bypass, and true is not proof the deployed policy applied source filters. Compare intended source versus consumer scope, actual request/job evidence and row grain before changing it. Missing materialization metadata is not proof a query failed; empty serialized error arrays are not errors. Do not copy reference flags or cached row counts to manufacture success.

#### SQL Expressions Over Query Outputs

Treat an existing InfoBridge query's materialized output as a relational input to a new SQL-source query. Use `{{query_id:<resolved-query-identity>}}` in `FROM` or `JOIN`; the reader resolves it to a quoted local DuckDB table. This is SQL over InfoBridge results, not a physical SQL database connection or forecast writeback. A newly materialized SQL-source query can itself be referenced by later queries, forming an acyclic dependency graph.

**Observed native authoring evidence:** a freshly exported, explicitly authorized user-created filter sample has source and query type `SQL_SOURCE`, SQL in both source and query metadata, one base query step with `meta.type: 10`, and a linked edge from the upstream query to the SQL source. The UI's numeric placeholder is rewritten to an opaque portable query identifier in exported SQL and the linked edge, while `meta.queries` and the step's descriptive text retain the numeric identity. This is an observed representation boundary, not a ready-to-replay constructor or proof of a portable round-trip. Resolve the writer/importer's identity mapping; do not assume identifiers are always bare GUIDs, compare mixed identities as literal equals, execute descriptive text instead of `meta.sql`, or silently rewrite legacy dependency values. The SQL source's worker dispatch value `230` is a different enum domain from the observed base step `10`; never infer a step type from the source type. Cached materialization metadata and the user's preview support this filter example, not native certification of joins or all SQL syntax.

**Prefer** this route when a business transformation is clearer as relational SQL: explicit projections and aliases, filters, `CASE` expressions, casts, aggregation, compatible unions or multi-query joins. AI-generated SQL is a useful authoring mechanism, not a correctness guarantee. Keep a simple native transformation when it is clearer; do not replace an existing working query merely to use SQL. Validate CTEs, window functions and other advanced syntax against the selected deployed DuckDB route/version before relying on them; do not assume T-SQL or unrestricted database commands.

**Must:**

- Resolve each upstream query in the current Plan and inspect its actual output catalog, types, grain, scenario/period context and materialization. Query names, UI order, source IDs and query IDs are not interchangeable. The UI can display a numeric query token; exported definitions may use opaque portable identifiers or GUIDs. Use the identity required by the selected writer/import route, keeping SQL placeholders, source `meta.queries` and dependency registrations semantically consistent through its mapping. Never globally replace arbitrary numbers or reuse a reference Plan's identities.
- Store the statement in the SQL source's `meta.sql` and register its referenced queries in `meta.queries`; retain ordered query transformation records and explicit linked-source dependencies through the supported writer. Match every placeholder to a registered query, reject unresolved references and dependency cycles, and distinguish source ownership from downstream visual bindings. A repeated reference or self-join uses separate SQL aliases, not invented query identities.
- Define the output grain before writing joins. Join on all required stable business keys, including scenario/version and period where applicable. Check right-side uniqueness for many-to-one joins, audit unmatched keys, and deliberately choose `INNER JOIN` (drop unmatched) versus `LEFT JOIN` (retain unmatched). Pre-aggregate only when justified by the business grain; do not hide fan-out with `DISTINCT` or arbitrary deduplication.
- Use explicit projections and unique stable aliases for published outputs; quote field names and escape string literals correctly. Inspect null behavior, division-by-zero handling, numeric/date casts, units and currency. An exploratory `SELECT *` is useful, but a production join should not expose duplicate or drifting column names.
- Use a read-only result-producing statement. The inspected SQL loader loads upstream Parquet into temporary tables, rewrites placeholders and constructs a view; it rejects empty results schemas and more than 50 output columns in this revision. It also excludes some metadata-declared date/hierarchy columns and conditionally handles stored subtotals. Inspect the effective SQL input schema and leaf/parent grain rather than assuming every UI-preview column or total is available unchanged.
- Test SQL against small synthetic fixtures for matching, unmatched and duplicate keys, alternate scenarios/periods, nulls, aggregation totals and projected names/types. Then verify native materialization, the saved output catalog, downstream binding and refresh order on authorized resources. Offline execution is not deployed-version parity or proof of a refresh cascade.

**Avoid:** physical table-name guesses in place of query tokens; arbitrary external paths/functions, DDL/DML or provisioning; copied cached counts/files/status; source data or private identities in the reusable skill; and claims that one successful filter sample proves every SQL feature or join is supported.

**Examples:** the numeric tokens below are illustrative. Replace them with resolved current-Plan query identities through the chosen authoring route. Query `101` represents demand at RegionID/ScenarioID/MonthID/ProductID grain; query `202` represents one price per same key. These are synthetic schemas, not assumed columns in any user's Plan.

Filter and project an existing query:

```sql
SELECT "RegionID", "ScenarioID", "MonthID", "ProductID", "Quantity"
FROM {{query_id:101}}
WHERE "Quantity" > 0;
```

Calculate revenue with an inner join, deliberately excluding demand without a matching price:

```sql
SELECT demand."RegionID", demand."ScenarioID", demand."MonthID", demand."ProductID",
			 CAST(demand."Quantity" * prices."UnitPrice" AS DOUBLE) AS "PlannedRevenue"
FROM {{query_id:101}} AS demand
INNER JOIN {{query_id:202}} AS prices
	ON demand."RegionID" = prices."RegionID"
 AND demand."ScenarioID" = prices."ScenarioID"
 AND demand."MonthID" = prices."MonthID"
 AND demand."ProductID" = prices."ProductID";
```

For a business request such as combining forecast demand with scenario-specific prices, select this SQL-source route when both upstream outputs exist at compatible grain. Explain the join choice and unmatched-row policy, validate uniqueness and totals, then register the resulting query for downstream consumption. Do not introduce a second editable driver or write planning results to a database merely to implement the SQL calculation.

#### Materialized Output and Follow-On Jobs

The APPEND output builder merges object-valued existing metadata with derived dimensions, columns, measures, date options/columns, hierarchy columns and selected-field arrays. It enriches measure aggregation/data types and writes measured `recordCount`, `columnCount` and literal `parquetVersion: 'v1'`. Its count fallback uses `||`; the EDITABLE builder uses `??` with zero fallback. These are concrete output/presence behaviors, not business defaults or proof that a downstream reader enforces that version.

APPEND writes a combined DuckDB view to Parquet, counts rows/columns and uploads through the lease-aware source uploader. EDITABLE instead references an upstream-written file. Do not fabricate `filePath`, counts, job status or selected-field metadata to simulate materialization; inspect the actual source and query outputs.

buildSourceRecordV2 preserves source fields and supplies successful status, returned file path and metadata. processLinkedQueriesV2 finds query-index entries whose source value matches this source GUID and delegates those query keys to `bulkCreateIBQueryJobV2`. It does not route through the separate recursive linked-source reload worker. This establishes a follow-on job handoff, not full automatic propagation after every planner edit, cancellation/security guarantees or cross-domain reconciliation.

#### Export Conversion and Construction Eligibility

The inspected export source/query builders parse stored metadata, invoke query-identity rewrites using the remap flag, apply editable reference conversion and normalize measure references. They emit `sourceGuid`, named source types, visual record GUIDs and nested query records; query output has `queryId`, `sourceId`, transformed `meta` and separately built `transformationSteps`. These are this export implementation's emitted fields, not direct copies of the worker blob or proof of all route/import parity.

For construction, resolve actual source/query/output identities, the selected native metadata branch, complete transformation steps and the applicable export/import conversions before assembling the public part. The published root requires `$schema` and a nonempty `sources` array; its step table requires `stepIndex` and `meta`, with `meta.type`/`meta.name` and an open step-specific `value`. An open object does not close a transformation recipe. Do not use empty transformations, guessed output fields or runtime parquet references to stand in for the requested connected calculation.

For fresh queries with no configured writeback, omit optional `writebackSettings`; do not emit `{}` as a placeholder. The importer skips absent settings but requires `writebackSettingsGuid` whenever a settings object is present. A deployment reached this branch and failed with `ImportFailed` for the empty-object case despite passing the public schema. If writeback is requested, construct the actual settings identity, metadata and authorized destinations through their contract. Do not remove existing configured writeback during an update or invent an external destination to satisfy this guard; query materialization, saved Planning inputs and external writeback are separate concerns.

Distinguish source-data loading, reuse of a query's transformation steps and whole-item definition deployment. Importing a data file into a bridge is not installation of the InfoBridge definition part; successful step reuse does not prove source/consumer registration or item deployment.

Connected Planning export constructs `sources`, `linkedQueries`, and `queryGroups` plus `$schema`, then uploads using Connected Planning folder/file constants. The public part is `connectedPlanning/infobridge.json`; the public table alone does not close every source/step variant. Earlier source GUID and query GUID map builders prove separate identity domains.

#### Observed Portable Graph and Consumer Records

Representative metadata from three user-supplied decoded Fabric Plan definitions was inspected on 2026-11-08. This adds **illustrative serialization evidence** and scoped structural checks, not target-build import, runtime refresh or financial-correctness proof. No live originals were fetched. Retain only generic record relationships here, not the supplied applications' identities, layouts, business assumptions, saved values or local file paths.

| Layer | Observed exported record | Construction consequence |
| --- | --- | --- |
| Portable part | `connectedPlanning/infobridge.json` contains `$schema`, `sources`, `linkedQueries`, `queryGroups`. | A source/query definition and its dependency registry are separate collections. Empty example query groups are not a universal requirement. |
| Source | `sourceGuid`, `name`, named `type`, `visualId`, `meta`, nested `queries`. | Resolve the selected source branch and its producer visual where applicable. Observed Planning, editable, append, join and SQL-source names are not numeric worker dispatch values. |
| Query | `queryId`, owning `sourceId`, `name`, `type`, `visualId`, `meta`, ordered `transformationSteps`; writeback fields also occur. | Query `sourceId` matches its owning source's `sourceGuid`. Do not populate writeback or other branch-specific settings from an unrelated example. |
| Transformation step | `queryId`, `stepIndex`, `notes`, `meta`; observed meta has `type`, `name`, `description`, `value`. | Use operator-specific values and exact step order. Source selection, pivot/aggregation, filtering, added fields, column removal, append and join have different configurations. A step label or empty value is not a complete transformation. |
| Dependency edge | `linkedQueryGuid`, upstream `queryId`, dependent `sourceId`, `visualId`. | Here `sourceId` names the source consuming the upstream query, not necessarily that query's owning source. Keep the edge identity separate from source/query identities. The observed `visualId` refers to an associated upstream visual, not a destination field assignment. |
| Visual consumer | Exported `properties.pivotAssignments` entries with `sourceType: "InfoBridge"`, `queryId`, `id`, `sourceId`, field name/table/bucket metadata and applicable measure/aggregation fields. | Bind the actual consumer to registered output fields. Observed field references have the form `queryId[outputFieldKey]`; this is not permission to hash a label, reuse a sample key or invent an allocation algorithm. |

An observed append-query-to-join-source edge has `visualId: null`. It is not a dangling non-null visual reference: the upstream query and dependent source both resolve. Allow that distinction in structural checks, while verifying the target importer accepts the selected representation. Do not interpret every `linkedQueries` entry as a query-to-destination-visual link.

Representative transformations show a reusable composition: select source fields, aggregate/pivot to the needed grain, add derived fields or compatible contribution columns, remove unwanted detail, then append/join and calculate consolidated results. An added numeric column can carry a SQL expression such as `formulaQuery: "CAST(0.0 AS DOUBLE)"`; an added dimension can carry a string expression. These are InfoBridge transform expressions, not Planning formula tokens, proof of safe padding or a mandatory financial recipe. Derive columns, units, currency conversion, version context, join keys and calculations from the current request/model; confirm the operator's current validator before construction.

Metadata can contain field catalogs, selected dimensions/measures, time mappings, flags and cached materialization details. Decode only fields whose actual encoding requires it; do not assume every `meta` or nested value is a JSON string. Retain case-distinct keys when parsing supplied JSON (PowerShell: `ConvertFrom-Json -AsHashtable -Depth 100` with terminating errors). Inspect representative field metadata, not stored input rows or `flatData`; never copy cached counts, parquet references or validity/success state as construction evidence.

The current core API IIncludeItem and IMetaSchema declare `includeMeasures` and `includeScenarios` as optional arrays of `{id, name, alias?}`, not boolean switches. The V2 update service tests their lengths and merges supplied selections into metadata. A supplied export containing booleans does not supersede these declarations or prove successful materialization; correct that constructor defect rather than waive it as a schema conflict. Select the intended native measures/scenarios through the actual owner. Business-version dimensions and input filter context remain separate from this native scenario-selection list.

**Scoped structural checks:**

- Keep Planning axis roles aligned with InfoBridge source/query catalogs and transformation selections. Moving Year/Quarter/Month from Rows to Columns requires corresponding `columns`/`selectedColumns` and type-50 `sourceColumns`, not merely renaming entries in `dimensions`/`sourceDimensions`. Resolve context-only dimensions and generated date fields from the actual owner/source contract. A fresh export exposed a real constructor defect where the source correctly rebuilt its column catalog but the query still selected those IDs as row dimensions. Reject role-mismatched selections even when the IDs exist somewhere in the source; identity existence alone is insufficient. Repair a current destination from a fresh baseline, preserve unrelated parts and verify saved query selections afterward. This connected-query defect does not independently establish a native initialization root cause.
- Check unique source/query/edge identities within their actual scopes and resolve each query's owning source.
- Resolve every dependency's upstream query and dependent source. For append, compare `meta.queries` input identities with existing queries and the corresponding dependency edges. For joins, validate their own source/query-reference branch rather than applying the append string-array shape.
- Resolve non-null visual references to declared visual records/parts; do not flag null query-only dependencies as missing visuals. Check intended producer associations separately from destination consumers.
- Audit ordered step indices, selected input fields, output schema and transformation references. Exported source catalogs alone do not prove the final transformed output catalog or compatible append/join grain.
- Resolve each consumer's `queryId` and typed output-field references, including the applicable measure/aggregation metadata. Verify month/region/version/currency context, joins and units against the current business design.
- For query-backed KPI cards, verify selection under the **bound query**, not merely a same-named field in another expanded query. A populated Actual(s) bucket and a matching display label do not establish that the expected query's field is selected. Compare a fresh saved manual assignment with the baseline by visual identity, including `queryId`, `tableName`, `id`, `sourceId`, field type and aggregation. Separate a different source/query owner from an unresolved same-query field identity before diagnosing a missing green tick. Select the authoritative query from the card's business purpose: a domain workbench can consume its normalized contribution, while consolidated financial review can consume the append result; do not automatically bind every KPI to consolidation or retarget every card to a contribution. Resolve identities from the selected query's actual output catalog and supported assignment writer, never from labels or copied sample IDs. Preserve unrelated assignments and user saves; saved configuration and visible selection are separate from calculated-value/refresh verification.
- A query-bound quantity in a review visual does not prove a product-cost calculation consumes it or that a duplicate quantity input is absent. Trace the actual destination formula/source dependency and test the saved edit where authorized.

**Saved KPI reassignment evidence, 2026-11-11:** a user-reassigned domain KPI changed its query owner from the consolidated append to the domain contribution. Its `queryId`, `tableName` and query-qualified `id`/`sourceId` changed together; the output-field key, Actuals bucket, field type and Sum aggregation stayed the same. The user supplied the checked-field screenshot, and fresh export confirmed this one visual's assignment change. Thus the missing tick under the domain query did not demonstrate an unassigned measure or a defective output-field key: the prior card referenced a different query with the same-named field. The UI also changed the display name to an aggregation-prefixed label, cleared the assignment format string and added metadata; do not attribute the tick to those incidental changes or adopt them as universal defaults. Preserve separate numeric formatting and verify the exact bound query after save. Other cards and calculated/refresh behavior were not repaired or verified by this comparison.

Across the inspected examples, query identities were unique, query-to-owning-source and linked query/source references resolved, append inputs matched their dependency edges, and all non-null dependency visual references had matching properties parts. This is **passed-scoped structural evidence**, not full native schema validation, successful import, materialization, automatic refresh, shared-driver behavior or business acceptance. A complete new constructor still needs the selected current writer/import mapping; unfinished implementation is not a demonstrated product or authentication limitation.

**Remaining gap:** concrete source dispatch, selected metadata readers, output enrichment and the V2 follow-on job handoff are now inspected. HTTP/controller/queue matching, full query-transform validators/step metadata, source-exclusion rules, complete ALM reverse-import and route-specific rewiring, and edit-triggered refresh/security/cancellation still need closure. No full source/query constructor or exhaustive transformation catalog is claimed. Native UI IDs and materialized worker output must not be copied directly into portable queries.

#### Runtime Assignment Identity Gate

**Mandatory after import for affected query-bound visuals:** portable assignment consistency is not runtime catalog selection. The assignment reader can construct a fallback bucket item when catalog lookup fails, so a populated Actual(s) bucket does not prove a resolved field. The checked-state identity helper includes the field identity and source type; a matching label or output-field key alone is insufficient.

1. Retain the current destination's visual assignments, query ownership, buckets, aggregation, filters/context, geometry and unrelated settings before repair. Fetch fresh native state; never overwrite user additions with an earlier deployment export.
2. Load the destination's actual query and output-field catalog. When using an authorized browser, expand Queries and the intended query before concluding its fields are absent: catalog metadata was observed to load lazily. Use approved native readers for headless work; do not require browser authentication or MCP when prohibited.
3. Match each assignment by the intended query's stable identity plus its registered output-field identity and source kind, not name alone. Distinguish a wrong query owner from an unresolved same-query runtime ID. Compare the complete assignment identity required by the active reader with the canonical catalog entry, including applicable `id`, `sourceId`, `queryId` and source/table metadata. Preserve the writer's distinction between portable references and runtime fields such as `tableId`, `infoBridgeSourceId` and `infoBridgeSourceGuid`; their presence in catalog metadata does not make them universal required save fields.
4. If the assignment is stale, use the supported target-local assignment writer with canonical metadata. An explicitly authorized UI route can remove and reselect the exact catalog field as a scoped canary, immediately verifying the empty bucket and then its restored assignment. Never guess a numeric query ID, globally replace GUIDs, patch private React stores, copy another Plan's IDs or retarget to a different same-named query. Preserve bucket, aggregation, formatting, filters, geometry and unaffected assignments. Stop on ambiguous matches rather than clearing or duplicating fields.
5. Save through the supported route and verify through a fresh load, not only the already-mutated UI. Require the intended assignment count, exact catalog identity/source, unchanged bucket and aggregation, and the expected checked field under that exact query. Exercise all affected visuals, not only the canary. With authorized UI access, confirm the visible green tick after reopen; without it, report persisted identity reconciliation and rendered checked-state verification separately. Missing catalog/authentication access leaves the affected check blocked or not-run, never passed from export equality.
6. Where the selected builder has executable checks, reject a stale portable-qualified ID in native assignment state, a same-named field from another query, ambiguous catalog matches, duplicate assignments and changed bucket/aggregation. Do not reject valid portable IDs in the pre-import definition or hardcode any observed runtime number. Instructional guidance alone is not deterministic importer enforcement.

**Catalog selection versus execution identity:** resolve these separately. A catalog's runtime table-qualified `columnId` can differ from the stable query identity used by the active execution registry. A numeric catalog table ID is not permission to replace a GUID-native execution `queryId`. Match the catalog to the registered query through its stable source identity, then use each reader's actual identity; stop on ambiguity. A task-local reconciler now tests this separation, preservation, idempotence and eight rejection cases offline. That test does not establish native save behavior, visible checked state or successful query execution on a new artifact.

**Observed recovery, 2026-11-12:** seven Home visuals retained GUID-qualified field IDs while their same-query live catalog used runtime-qualified IDs with the same output keys. Supported UI reselection restored all seven checked fields without duplicates; a save and independent fresh reload verified the identities, source, Actuals buckets and Sum aggregation. The current sheet count and a user-added sheet were preserved. This establishes that scoped checkbox recovery, not a deployed importer fix or automatic remediation for future Plans. All affected visuals still reported `InfoBridge query not found`; query availability/materialization, successful values and financial propagation remain separate failed or unverified gates. Keep exact resource IDs and browser evidence private, and never turn the observed runtime IDs or page inventory into authoring defaults.

#### Runtime Query Reference Gate

**Mandatory after import for connected SQL/composite sources:** every `{{query_id:...}}` token and dependency in `meta.queries` must resolve to the intended query in the destination's current registry. Query order, labels, a catalog's numeric table ID and an imported SQL-row number are not substitutes for that registry's query identity. If the supported writer permits assigning sequential IDs, register those IDs first and use the exact returned mapping. A GUID-native registry requires its GUIDs; never renumber existing queries just to shorten SQL.

1. Read the actual destination source/query registry and resolve the intended upstream by stable source/query identity, not display order or name alone. Check SQL tokens, SQL-source dependencies and append/composite inputs, including repeated tokens and all applicable source/query metadata copies. Do not assume a valid portable graph survived import unchanged.
2. Before repair, retain fresh direct source and query records, transformation steps and the complete query inventory. A list endpoint can normalize metadata and omit stored field flags; use direct record reads as the preservation baseline rather than overwriting them with the list projection.
3. Limit a repair to the established dependency graph and reference tokens. Require the current SQL body to remain unchanged except for identity tokens; reject ambiguous owners, missing registered queries, changed dependency cardinality, a different valid query owner and unrelated SQL edits. Preserve user-corrected definitions, additional queries, output catalogs, formatting, filters and saved inputs. Inspect SQL-bearing transformation descriptions separately rather than assuming a source patch updates them.
4. Use the supported writer for each affected layer. The inspected query PATCH accepts JSON; the source PATCH accepts binary JSON. Their service writers read current ETags and preserve unrelated record fields. The broader SQL editor also replaces metadata, reconciles dependency mappings and schedules recomputation; do not treat these routes as interchangeable. Journal each request and verify readback before continuing; reconcile a rejected or ambiguous write instead of replaying successful changes.
5. Fresh-read all affected source/query definitions and require every dependency to resolve under the intended registry identity. Verify unchanged registered IDs, unrelated sources and transformation steps. Keep saved-reference correctness separate from visible editor validation, recomputation, materialized values and financial propagation.

**Observed scoped recovery, 2026-11-12:** the destination registry used GUIDs while three generated SQL sources and an append source still held numeric dependency references. One earlier SQL definition was already corrected and was preserved. Reference-only metadata PATCHes repaired the remaining four source/query pairs; fresh reads passed all five generated dependent definitions, unchanged registered identities, unchanged transformations and preservation of an additional user query. The first request was authoritatively rejected for content type without a write. After correcting that request, a source precheck stopped on list-versus-direct metadata differences; direct baselines preserved the stored flags and only the unwritten source phase resumed. Offline tests cover numeric and GUID registries, preserved metadata, paired source/query reconciliation, idempotence and rejection cases. This is native saved-reference evidence, not a deployed importer fix, query recomputation or visible editor/checkbox acceptance. Exact identities and request journals remain private.

#### Cross-Domain Contributions to P and L

An explicitly authorized fresh reference inspection in November 2026 showed separate workforce, operating-expense, revenue, supply-cost and revenue-discount contribution queries feeding an append-based P&L, with consumer visuals bound to the consolidated outputs. This is saved-definition evidence, not an independently exercised edit-to-P&L refresh. The inspected application's pages, business defaults, connections, IDs and saved inputs are not templates for new construction.

| Producer | Preparation before consolidation | Guard |
| --- | --- | --- |
| Workforce | Calculate compensation at the applicable employee grain, then aggregate to the required financial dimensions and period/context | Do not duplicate employee compensation in manual operating expenses; preserve currency and effective-dated membership |
| Operating expense | Select the intended non-payroll/non-product-cost expense categories, retain account classification, and aggregate away detail not needed downstream | Exclude compensation and COGS contributions already owned elsewhere; depreciation remains distinct when computing EBITDA |
| Revenue | Calculate quantity/price/discount results at the commercial grain, then prepare the required financial contribution | Derive cost from the authoritative quantity where that dependency is intended; a review-only quantity binding does not establish a cost formula dependency |
| Supply cost | Calculate product-grain quantities and costs before financial aggregation | Do not multiply a coarse quantity by an unweighted average unit cost |
| Discount, when separate | Add an explicitly signed discount contribution to the appropriate revenue/account classification | Reconcile gross revenue, discount and net revenue exactly once; do not append a second already-net revenue stream |
| Consolidation | Append compatible contribution outputs and calculate financial results from the aggregated components | Require matching field roles/types, grain, periods, scenario and currency; append is not a join or a substitute for aggregation |

The inspected saved sequence uses source selection/pivot preparation, category filtering where applicable, added classification fields, added numeric contribution measures, removal of intermediate measures, and an append source. Operator numbers are only observed metadata: type 50 prepares selected fields/pivoting, 170 adds classification columns, 180 supplies filter conditions, 130 adds numeric expressions, 310 removes intermediates and 140 marks the append step. Resolve the current operator writer/validator before authoring; a step name or `isValid` flag does not certify execution. Carry the time field through the actual dimension/column/date catalogs, not just `selectedDimensions`; inspecting one catalog can incorrectly suggest that the period was dropped.

For each contribution, trace the field set after every step. Explicitly aggregate finer grain, populate only business-justified non-contribution zeros, then remove intermediate measures after all dependent expressions are evaluated. Compare the final selected catalogs with the actual output and typed consumer bindings. Validate each append input against its registered upstream-query/dependent-source edge; check topological order, cycles, duplicate contributions, unmatched keys and source-filter scope. Trace destination formulas as well as chart bindings. An empty error-message field or a stored row count is not proof of fresh materialization.

**Synthetic reconciliation example:** gross revenue 1,200 and a separate -200 discount give net revenue 1,000. COGS 400 gives gross profit 600. Compensation 200 plus other operating expense 100 gives total operating expense 300; EBITDA is 300. Depreciation 50 gives operating income 250. A signed contribution total of `1000 - 400 - 200 - 100 - 50` also gives 250. Apply the request's actual account/sign/currency policy; these amounts are test fixtures, not defaults. Ratios must use the aggregated numerator and denominator, not summed percentages.

**End-to-end acceptance:** save an authorized producer edit, confirm its persisted value, refresh/materialize prerequisites and dependent queries through the supported route, then reconcile leaf and aggregate P&L results under the same period/scenario/currency. Restore any explicitly authorized temporary test edit through that same route. Definition topology can pass without this behavioral check; report propagation, freshness, input retention and security separately. Learning from a sample's extensive flow does not implicitly expand a requested revenue-only artifact into a cross-domain application.

### F19 Blend

#### Measures From Sheets Authoring

Use From Sheets/Blend for a supported direct measure dependency within the connected application; use From Queries/InfoBridge when outputs need normalization, SQL expressions, mapping, joins or append before consumption. For example, a cost sheet can consume an authoritative demand quantity rather than introduce a second editable quantity. SQL forecast writeback is not required merely to connect sheets; any external writeback fallback needs a demonstrated requirement and explicit authorization. Master-data PowerTables are a separate concern.

**Must:** inventory source and consumer grain, including dimension identity/type, period, scenario and units, before linking. Matching labels do not establish compatible grain. A coarse total cannot provide finer detail without an explicit allocation/lookup contract, and repeating a value across a missing dimension can inflate totals. Keep semantic master dimensions on the intended axes and linked measures in Values for this workflow; test security separately from field assignment.

Resolve the complete lineage: root sheet -> owner visual -> target runtime source visual/column -> consumer registration -> consumer formula token. Retain an internal identity manifest with each domain separately named; it is not native deployment JSON. Preserve decimal identities losslessly, resolve local formula references only after consumer registration, and validate both the visible linked value and a formula consuming it. Never assume a source ID, runtime numeric column ID, exported GUID or consumer `M_<id>` token is interchangeable.

**Workflow:** save the source; select its measure under From Sheets in the consumer's Data pane; assign it to Values; align semantic axes and context; save/reload and reconcile the linked value before adding dependent formulas. Capture the precise before/after native save/export changes for any unresolved persistence boundary. The supplied guide's runtime request fragment and workload routes demonstrate historical source selection, not a complete public creation API or portable From Sheets assignment. Its deployment archive used InfoBridge instead, so it does not close the direct persisted From Sheets constructor. Do not invent a Blend part or promote runtime request fields into ALM; use the target native writer or a verified InfoBridge alternative when appropriate.

**Prefer:** the simplest supported connection and a documented refresh order. For query-based flows, separate input save, source materialization, dependent calculation, consolidated output and dashboard refresh. For direct links, verify the product's actual invalidation behavior; dependency existence alone does not guarantee immediate propagation. If appending contributions instead, normalize dimensions/types/key meaning, period/scenario, account mapping, sign and currency, and exclude overlapping domains before stacking records.

**Avoid:** stale mappings from another report, linking by display name alone, inventing lookup/allocation behavior for mismatched grains, collapsing scenario context during refresh, or applying foreign report-scoped credentials. Preserve unrelated filters and target-local identities through the actual import mapper, not global replacement.

**Validation:** audit source existence, consumer registration, formula references, field/filter metadata and dependency cycles. On authorized test resources reconcile source/consumer leaf and aggregate values under identical region/period/scenario selections; verify one controlled edit through the actual refresh path, dependent formula calculation, rename/reload and scenario switching. A visible linked number plus formula `#REF!` points to consumer identity/registration checks, not proof that the link or formula is fully configured.

#### Connected Planning Design Examples

The functional guide adds two contrasting examples. These are business reconciliation fixtures, not a closed From Sheets constructor, automatically generated InfoBridge pipeline or measured refresh guarantee.

**Quantity to COGS, compatible subset grain:** source rows Region/Product/Channel with a shared Month/scenario produce Final Quantity; the destination uses Region/Product with the same period/context. For additive quantity, removing Channel can use supported direct Blend aggregation rather than requiring preparatory InfoBridge solely for that roll-up. Resolve dimension identities and aggregation semantics before linking.

| Product | Retail / Wholesale quantity | Consumed quantity | Unit cost | Product-grain COGS |
| --- | --- | --- | --- | --- |
| A | 1,000 / 500 | 1,500 | 2 | 3,000 |
| B | 600 / 400 | 1,000 | 3 | 3,000 |
| Total | 1,600 / 900 | 2,500 | Not summed or unweighted | 6,000 |

Keep semantic-model Region/Product/time on the destination axes, add Final Quantity from From Sheets to Values, and calculate the product-level result from the registered consumer measure and compatible Unit Cost. Aggregate resulting cost amounts for a Region/Month profitability consumer. Multiplying 2,500 by unweighted average cost 2.50 yields 6,250 and is wrong for this example. Removing a dimension from a rate measure is not equivalent to this additive quantity roll-up.

**Workforce to department, preparation required:** employee costs 6,100 and 7,320 in one cost center and 4,320 in another map to one department for the same agreed month/scenario/currency. Join an applicable many-to-one cost-center/department map without duplicating employees, then group Department/Month while retaining scenario and currency. The expected department cost is 17,740. Missing mappings, duplicate/effective-dated matches or incompatible units require explicit handling before consumption, not arbitrary first-match or silent row loss. Add the prepared measure from From Queries with compatible semantic-model department/time axes. If the source already exposes compatible Department/Month and only requires supported aggregation, use the simpler direct route instead.

For a compensation formula needing only a benefits rate, evaluate Advanced Lookup with resolved keys/context and missing/duplicate behavior rather than constructing a full preparation pipeline. A query is justified when the requirement is a reusable transformed dataset, not merely because the data originated on another sheet. In all three routes, validate one source change through save/materialization/consumer calculation and restricted-user context; source-change propagation claims do not supply a latency guarantee.

#### Runtime Refresh Contract

Intent: refresh dependent visual/query data after edits or column mutations. Blend.service defines runtime polling, not a saved `blend` ALM property.

| Runtime object | Exact observed members |
| --- | --- |
| Event type | `REFRESH_CATALOG_DATA`, `BLEND_QUERY_UPDATED_EVENT`, `CELL_EDIT`, `COLUMN_MUTATION`. |
| Event | Numeric `timestamp` and `status`, event enum, optional string/number `visualId`, string/number `queryId`, string `errorMessage`, string `jobId`. Fields are flat. |
| Polling request | String `workloadId`; `blendType` limited to `CELL_EDIT` or `COLUMN_MUTATION`; optional string-array `powerTableEditedColumnIds` and numeric `powerTableInitialTimeStamp`. |
| Service state | Timestamp, column-mutation/save-required/catalog-fetch flags; runtime ownership does not imply persistence. |
| Dispatch | `COLUMN_MUTATION` handled separately; other behavior depends on request event and RLS-aware polling gate. |

The backend worker paths in [F18](#f18-infobridge) show separate SQL/OneLake source preparation and a V2 source-to-linked-query job handoff. That handoff is not a complete edit-to-consumer refresh contract. **Gap:** dependency-graph persistence, exact API/queue match, refresh/cascade and RLS semantics, cancellation, and post-import rebuild. Do not add polling events or timestamps to `infobridge.json` or invent a standalone Blend part.

### F21 Data Pane

Intent: browse model/sheet/InfoBridge fields and collections, control visibility, and populate visual assignments. DataPane uses tabs `SEMANTIC_MODEL` and `COLLECTION`, incoming catalog collections, a collapse hook, and a resizable panel (initial width 200, minimum 150 in the inspected hook call).

| Setting layer | Inspected contract |
| --- | --- |
| Props | Loading booleans; filtered/pinned/collection arrays of imported catalog items; optional read-only/planning/reporting/personalize controls. These are not a persisted field catalog. |
| Pane interaction | `usePaneVisibilityControl('dataPane')`; resizing and refresh actions are distinct from selected-field assignments. |
| `workloadModeConfig.EDIT.showDataPane` | Boolean, initial true in the workload store. |
| `workloadModeConfig.READ.showDataPane` | Boolean, initial false. |
| Assigned fields | Owned by visual assignment workflows, not the pane's tab labels. |

Evidence: mode configuration and initial modes. The public `planProperties.json` describes mode visibility, but actual native-save/export/import mapping is not closed. **Gap:** collapse/width persistence, collection/pinned-item storage, field assignment reference conversion, and complete part requiredness. Do not serialize React props or assert that all pane-related state is runtime-only.

### F22 Side Panel Filter

Intent: configure page/workload filters independently of F07's Matrix rule engine. activePageStore has `pageLevelFilterAssignments: TSuperFilterAssignment[]`, optional string-array map `excludedFilterContextAssignments`, and entity-level variables. These scopes are not interchangeable with visual assignments.

| Local editor setting | Reader fallback in useFilterState |
| --- | --- |
| `singleSelect`, `selectAll`, `alphaNumericEnabled` | Boolean, false. |
| `regex` | String, `\d`. |
| `metrics` | Supplied pivot assignment or null. |
| `aggregationType` | Based on selected config or metric type: SUM for summation types, FIRST for String, EARLIEST otherwise. Imported wire enum still requires verification. |
| `showCount`, `highlightOnly`, `isSliderAndChartsEnabled` | Booleans, false. |
| `dateFormat`, `fiscalStartMonth` | String-or-null and number-or-null, fallback null. |
| `measureSearch` | Boolean, true. |
| `upperDimension` | String array, empty. |

Evidence: useFilterState. Local updates shallow-merge; changed selected filter/config synchronizes local state. UI defaults do not prove exporter-materialized defaults. Public page/workload/visual filter locations differ. **Gap:** apply/save writer, complete `TSuperFilterAssignment` variants and recursive filter leaves, selected scope's ALM rewires, variable IDs, and reverse import. No universal filter JSON is supplied.

### F23 Bookmark

Intent: save/restore report or personal view state, with configurable data/display/page capture. bookmarkStore separates saved snapshot properties from loading/slideshow/selection/persistence state.

| Snapshot member | Type / presence |
| --- | --- |
| `bookmarkSlug`, `activePageId`, `focusModeVisualId`, `spotlightId` | Optional strings; identity domains must be remapped, not guessed. |
| `bookmarkOrder` | Optional number; comment distinguishes workload/personal order signs. |
| `bookmarkConfig` | Optional booleans `includeData`, `includeDisplay`, `includeCurrentPage`; optional `accumulationType: all-visuals or selected-visuals`. |
| `pageLevelFilterAssignments`, `workloadLevelFilterAssignments` | Optional scoped assignment arrays. |
| `activeSelection` | Optional string array of selected visual references. |
| `entityLevelVariables`, `workloadLevelVariables`, `crossFilters` | Optional imported structured arrays, not arbitrary objects. |
| `bookmarkGroupId`, `bookmarkGroupLabel`, `isDefaultBookmark` | Optional strings and optional boolean. |

`updateBookmarkState` shallow-merges after stripping helper callbacks/undo flags; supplied bookmarks trigger undo recording unless suppressed. listBookmarks queries active **report** bookmarks and their active property records; personal export is not established by this path. Native partial capture-options subtree:

```json
{"includeData":true,"includeDisplay":true,"includeCurrentPage":false,"accumulationType":"selected-visuals"}
```

**Gap:** full cloud snapshot transformation/construction, export/import GUID conversion, group/slideshow handling, orphan-reference lifecycle and SQL/OneLake parity. The public snapshot placement below is observed, not a complete writer/import contract. A general bookmark store does not mean every bookmark kind is portable.

#### Bookmark Business Authoring

A bookmark is a named saved view of supported state, not a financial snapshot, scenario/version, approval decision or writeback. Its purpose is to let people return to a business task without manually rebuilding the presentation. Keep five independent concepts clear: Pivot selects grouping; Show Columns selects visible measures; Bookmark captures supported view state; Bookmark Navigator exposes those saved views; Page Navigator moves between sheets/pages.

**Authoring sequence from the supplied Bookmarks/Intelligence guide:**

1. Open the source Planning sheet and select the task's pivot, hierarchy expansion and layout.
2. Use Show Columns for the task's measures; configure applicable sorting, formatting and filters. Hiding a helper preserves its calculation and dependencies and does not provide access security.
3. Choose public versus personal scope and create a meaningfully named bookmark. Public means available to authorized sheet users, not anonymous internet access; personal sharing/export availability needs its own supported route.
4. Configure another task view and create its bookmark. Use Update to replace an existing bookmark's captured view; changing the live grid alone is not proof its saved state changed. Preserve bookmark identity when updating or renaming.
5. Deliberately choose default-view behavior, save the Plan, then apply each view and reopen as an intended consumer. Check rename/default/update behavior and stale navigator references after permitted removal; do not assume public and personal lifecycle/export paths are interchangeable.

| Business view | Candidate grouping and visible measures | Acceptance distinction |
| --- | --- | --- |
| Executive Review | Category/quarter; Actual, Forecast, Variance | Reconcile the same slice to detail; hide technical drivers without changing their calculations or access rights. |
| Driver Planning | Detailed row/month; Quantity, Price, Forecast, Assumption Comment | Restore intended editable drivers and preserve independent input rules, approved states and pending-edit behavior. |
| Variance Explanation | Suitable exception detail; Actual, Forecast, Variance, Commentary | An actual calculation/filter identifies exceptions; the bookmark name does not implement that rule. |
| Review Queue | Approval-package scope; Forecast, Planner Status, Reviewer Status, Submitted Date | Expose existing controls; selecting the view does not submit, approve or reopen anything. |

Define the restore policy before saving: a named North review may restore a fixed region, while Driver Detail may be intended to preserve the consumer's current region. Determine which configured capture settings and target-build behavior implement that policy; do not promise that slicers always survive or are always replaced. Test both a different current selection and a missing/deleted field/member. Preserve scenario/version identity visibly even when it is outside the grid axes.

Data/display/current-page capture and all-visuals/selected-visuals are separate choices. includeData is a view-capture flag, not proof of frozen financial amounts. Resolve the actual captured visual membership rather than treating all-visuals as every visual in every sheet. With includeCurrentPage enabled, inspect activePageId: a source-sheet bookmark invoked from an Intelligence canvas may restore that source page. Test the actual transition; visible navigator tabs do not prove the user remains on the dashboard.

For Show Columns, inspect each bookmark's captured measure state rather than only the current source visual. Different task bookmarks may intentionally show different measures, but the supplied guide reports identical visibility in its two examples despite different active pivots. A view named All does not imply all measures become visible, filters clear, hierarchy fully expands or pivot overrides become empty arrays. Keep null overrides, visibility, expansion and selected context distinct.

**Acceptance:** verify pivot and explorer selection, visible measures/order, layout, sorting, formatting and captured filters; public/personal audience, default behavior and display order; source versus embedded navigation, current-page capture and deliberately unaffected visuals; permitted input behavior and pending edits; save/reopen and source refresh. Compare totals only for identical slice, measure, units and period. An illustrative 12,000,000 forecast versus 11,400,000 baseline has a 600,000 variance in either summary or detail; navigation must not itself write those amounts. Runtime restore, pending-edit handling and effective security require separate checks from a valid exported bookmark record.

#### Observed Public Bookmark Snapshots

The supplied Bookmarks/Intelligence response was independently decoded locally: seventeen payloads match its manifest hashes; nine available decoded companions match byte-for-byte, while eight visual companion files are absent from this local package. Use the original response as evidence for those missing companions, not a fabricated replacement or another live export. The following are inspected snapshot relationships, not a minimal create/update payload.

| Meaning | Observed location / relationship | Preservation or verification rule |
| --- | --- | --- |
| Public record | planProperties.json properties.bookmarks, keyed by recordGuid | Two screenshot-identified public records have bookmarkType 20; do not infer every bookmark enum or personal export support. |
| Snapshot identity | bookmarkSlug and cloudMeta.bookmarkMeta.bookmarkSlug | Both agree; record identity, slug, page and visual are distinct domains. |
| Display order/default | cloudMeta.bookmarkMeta.bookmarkOrder / isDefaultBookmark | Array order is 2 then 1; display order uses metadata. Neither is default. Do not sort unrelated positional arrays. |
| Captured page/selection | cloudMeta.bookmarkMeta.activePageId / activeSelection | Both resolve to the source Planning sheet and its direct visual, not the dashboard page. |
| Capture options | cloudMeta.bookmarkMeta.bookmarkConfig | Data/display/current-page true, all-visuals scope in this sample; these are not universal defaults. |
| Visual snapshot | cloudMeta.bookmarkVisualMeta keyed by the source visual GUID | Resolve a real owner and inspect complete captured state; keys are not local placement indices. |
| Active view | Captured pivot.active_id and pivotExplorer.activePivot | Values agree and resolve through the direct source visual's properties.visualState.pivot.configs. Captured config copies omit IDs in this snapshot. |
| Visibility | Captured manage_measures versus direct source manage_measures | Both captured arrays have eleven entries, nine visible; Actuals and the helper are hidden. Captured entries use labels without IDs; source entries retain IDs. Do not interchange the shapes or assume arbitrary label-to-ID migration. |
| Additional supported state | Captured layout, sorting, row_expand_state_config, numberFormatting, cfProps, totals_config, data_filter | Presence is not proof of a configured rule or a complete portable restore path. Resolve meaningful contents rather than treating every property as enabled. |

The source All pivot has null row/column/measure overrides; Category explicitly selects one row dimension and two column dimensions, with null measure override. Resolve base assignments separately from the active view's dimension metadata. The two captured visual objects differ at exactly pivot.active_id, pivotExplorer.activePivot and page_config. Their manage_measures arrays are identical, so this snapshot does not demonstrate different visibility per bookmark; task-specific visibility is supported functional guidance, not an observed difference here. The page_config object-versus-empty-string difference is recorded, not normalized or adopted as a business requirement.

[Microsoft Learn bookmark management](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-add-bookmark), checked with this guide, documents Update, Make default, Promote to Public, Rename, Delete and Copy link. Use those permitted actions deliberately: promotion changes audience, a copied link does not grant sheet access, and removal requires checking dependent controls. Public/personal permission, lifecycle, group/slideshow and target-build restore behavior are separate from successful part parsing. See the [dashboard workflow](#intelligence-dashboard-business-authoring) and [embedded ownership checks](#observed-embedded-owner-and-placement-checks) when applying these records through navigators.

### F24 Home Layout

Intent: compose a role-targeted Home with text, images, a banner and navigable sheet cards. This is workload configuration, not a new Planning sheet or visual. Client construction/save facts below do not establish a complete Fabric item-definition recipe or backend validation contract.

**Select the actual storage mode first.** `PlanningHomeLayoutV2` controls the editor path; feature switches are environment gates, not content fields. Legacy saves role content through workload properties. V2 saves role content through the authenticated application's role-layout provider; changing workload properties alone cannot deploy that content. Do not assume automatic legacy migration or delete retained legacy layouts.

#### Home Storage and Save Boundaries

The workload serializer removes `previewMode` and `previewDraft`; removal of legacy `roles`/`layouting` in V2 is commented out. preparePropertiesForSave wraps properties with `schema: "0.0.1"`. In the client bulk-save body, Home is at `workload.properties.homeLayout`, not a visual's properties. Preserve unrelated workload properties. This is a client request envelope, not an asserted on-disk ALM part.

| Mode / operation | Client contract and mutation boundary |
| --- | --- |
| Legacy content | Merge the intended role entry into `homeLayout.roles[]`; each role's `layouting` holds shared `items`/`rows`. Top-level `layouting` is compatibility state, not an active role-page fallback. Resolve existing security roles; layout JSON does not create membership or permissions. |
| V2 metadata/content reads | Hydrate metadata and affected existing role content before mutation. A confirmed 404 means absent content; other load failures must not become empty content. Preserve returned ETags. |
| V2 content upsert | Role ID is supplied to the provider, not invented in content. Body is `{homeLayoutOrder, data, etag?, force?}`; `data` is only the shared layout, not the whole Home/role object. Normal save omits `force`; conflict overwrite needs an explicit decision. |
| V2 priority | The order provider wraps the intended role-order list as `{roles:[{roleId,homeLayoutOrder}]}`. Mirror the client's complete intended list; omitted-role server semantics are unverified. Priority changes are not content replacement. |
| Visibility | Merge `homeLayout.show` through workload properties in both modes. It is not a role API field, role deletion or access revocation. |

Evidence: V2 hydration and change selection, upserts/order/visibility, and RLS provider bodies. These are configured backend-provider operations, not Fabric public item REST methods. Use approved application authentication/context; do not invent a public deployment endpoint.

V2 executes deletes, upserts, order changes and visibility save as separate phases. Partial completion is possible; reconcile completed mutations and current ETags before recovery. Do not blindly replay all operations or force over another user's changes. No cross-phase transaction is established.

#### Shared Content Fields

The workload declarations describe optionality, not blanket nullability or server validation. Shared layout is legacy `roles[].layouting` or V2 `data`; preserve unknown existing compatibility fields without treating them as authorable capabilities.

| Native member | Shape |
| --- | --- |
| `homeLayout.show` | Optional boolean; hiding Home does not grant/revoke entity access or erase layouts. |
| Legacy `roles[]` | Numeric `order`, string `roleId` and `lastUpdated`; optional `layouting` and `etag`. Use resolved roles and deterministic positive priorities, not example identities. V2 timestamps/ETags come from the provider, not fabricated content. |
| Shared `items[]` | Required for an explicit layout; string local `id` and editor `instanceId`; exactly `text`, `image`, `preview-cards`, `header-image-text`. Optional `instanceState` and `imageConfig` depend on type. Item/editor IDs are not entity IDs. |
| Active `imageConfig` | Optional source string and `sizingMode: fit or fill`; normalizer defaults nullish sizing to `fill`. `instanceState.image` is passive compatibility state, not the active image source or an established migration path. |
| `instanceState.text.title`, `.description` | Separate serialized Lexical document strings, not plain business text or nested objects. Empty string is intentional empty content. Open text-record typing does not permit arbitrary style keys. |
| `instanceState.previewCards` | Optional numeric `columns: 3 or 4` (nullish read default 4); optional `unSelectedEntityIds: string[]` is an exclusion list, not a selected/inclusion list. Empty exclusions include eligible options, including newly eligible sheets. |
| `instanceState.cardDescriptions` | Map actual eligible entity IDs to serialized Lexical strings. Descriptions neither create sheets nor grant access. |
| Shared `rows[]` | Required for an explicit layout; string `id`, ordered `itemIds`, positionally aligned `(number or null)[] widths`, nullable numeric `height`, optional nullable numeric `defaultHeightRatio`, optional boolean `isHeightManual`. Row/item-reference order controls placement. |
| Transient state | Preview snapshots, undo/redo history, hydration/loading state, toolbar targets and browser blob URLs are not authored persisted content. |

The layout resolver/helpers default missing/empty items or rows to the complete default layout, remove invalid row references and align retained widths. All-invalid rows also default the layout. This repair is not validation of uniqueness, supported types or all geometry. Empty arrays do not construct an intentionally blank Home.

The draft reducer keeps history separately. `stripDerivedRowMetrics` affects dirty comparison, not the actual saved layout; do not assume measured heights disappear from persistence. updateHomeLayout shallow-merges top-level state; it does not recursively merge role arrays or layouts.

#### Construction and Acceptance

- Preserve local item/row/editor identities on edits; allocate collision-free, selector-safe identities for new or duplicated blocks, and update every row reference and corresponding width entry. Resolve sheet, role and asset identities separately.
- Use editor-equivalent layout restrictions from the specification and their current UI owners: banner/cards in standalone full-width rows and at most six text/image blocks horizontally. Validate finite positive explicit dimensions, positional widths and long-content fit. Null widths are flexible; numeric widths are pixels, not percentages or Intelligence grid units. Manual height and relative sizing hints are not interchangeable. For new prose/card rows default to flexible widths and content-driven heights, stacking prose when available space is unknown. Read [Home layout fit](home-layout-fit.md) and use its constructor/checks; schema validity alone does not prevent unreadable narrow columns or clipped text.
- Generate nonempty text through compatible Lexical/editor APIs and its registered nodes. The Home editor restores serialized content and exports editor state. Do not hand-write an unverified node tree, inject HTML or add item-level font/theme fields to satisfy Arial. Verify actual serialized formatting and rendered typography separately.
- Resolve images through the target workload's image/asset integration. Use actual returned references, not source-workload IDs or temporary blob URLs. Replacement cleanup is not proven rollback-safe or reference-counted; do not delete shared assets without ownership evidence and authorization.
- Resolve effective roles and entities through HomeLayoutService. Legacy chooses one matching priority layout, not a merge; its everyone fallback depends on user-record/membership state. V2 selection is backend-owned, so do not assume identical tie-breaking or fallback. Visibility and exclusions are presentation controls, not security boundaries.
- Re-read authoritative content, order, visibility and assets after save. Test ordinary read mode with relevant user roles, hidden/excluded sheets and real navigation. Unsaved preview does not prove persistence, navigation or security. Record partial V2 failures by phase.

**Synthetic visibility fragment**, to merge into existing Home state through its mode-appropriate workload save, not a replacement object or full Plan part:

```json
{"show":true}
```

**Remaining gaps:** backend authorization/schema validation and role-selection semantics; complete dependency-owned Lexical node/version schemas; asset ownership/portability/rollback; exact Fabric ALM part placement, migration, import restoration and cross-workspace role/reference remapping. No browser execution, backend mutation or full Plan deployment is established by this documentation. Preserve the existing specification; no duplicate feature skill or invented `HOME_LAYOUT` part is required.

#### Home Layout Authoring

Use Home Layout for audience-specific introductions, planning-cycle instructions, process images and navigation into existing authorized sheets. It is not a new sheet, a live KPI surface or an approval engine. A flowchart explains a process but does not create routing, tasks or interactive workflow steps. Choose content from the current business request; a sample's banner, sheet catalog, roles and business names are not application defaults. Static text and uploaded images must be appropriate for everyone who can see that layout; do not assume semantic-model RLS filters their contents.

The supplied Home Layout functional/JSON guide reports a November 10, 2026 role-layout request and two exports. Its embedded excerpts are reported capture evidence, not a request executed here. The four images attached to this learning request show the role-layout editor, Create Layout role selector, a separate Security view and an edited text section. The Security image has Item Baseline selected; it does not establish a custom role's restrictions. A disabled already-used role in the selector is consistent with the documented one-layout-per-role limit, not a complete role-selection test. The save-success toast demonstrates a visible UI acknowledgement, not independent readback or restricted-user acceptance. The guide's separately linked complete request, decoded exports, validation script and payload-matched image were not independently inspected in this update.

##### Choose and Configure the Home Experience

1. Resolve the intended existing role and audience, current layout storage mode and actual sheet identities. Use Home -> Home Layout in editing mode, then Create Layout or Add Layout. Item Baseline supplies the documented default audience experience; preserve the mode-specific fallback caveats above. Add new role in the UI is a separate security action, not authorization to create a role, grant sheets or assign people as a side effect of layout authoring.
2. Introduce the application with the Hero Banner and add ordinary text sections for decisions, assumptions, deadlines and next steps. Use supported rich-text formatting and lists, preserving the actual Lexical document structure. Authored numbers or KPI descriptions are static unless a separately supported feature provides live data.
3. Add images through the supported upload flow. A process diagram should remain readable: prefer Fit when all labels must remain visible and check Fill for cropping. Replace, move or resize only the intended block; preserve unrelated assets and content.
4. Configure Available Sheets using the supported three/four-column layout, Show Sheets and card descriptions. Match eligible sheets by stable identity as well as display name; duplicate names are possible. A sheet's root `isHidden` property, a card exclusion and a role's sheet permission are different controls. Home does not create the referenced sheet or grant its access.
5. Arrange sections and images in business order. The documentation permits one layout per role, at most one Hero Banner and one Available Sheets block per layout, plus ordinary text/image blocks. Deleting a special block makes its add command available again. Keep the existing standalone-row and horizontal-count restrictions above; duplicate blocks need new local identities and row placement, not reused IDs.
6. Set Show and role-layout priority deliberately. Show hides presentation while retaining configuration; Show Sheets removes a card, not Explorer access. Highest-priority visible matching layout is the documented experience, not a claim that the chosen role replaces other memberships. Verify actual mode-specific selection, baseline behavior and tie handling rather than inferring them from one screenshot.
7. Preview, close preview, save and reopen the saved layout. Undo/Redo and Preview are editor state, not new payload fields. Test Explorer -> Home, sheet navigation and first-open behavior in the intended reading/published experience; the captured request contains no default-landing-page field.

For example, an inventory audience might need stock-risk guidance, replenishment steps, an explanatory diagram and links to the actual inventory sheets. A demand audience might need forecast assumptions and consensus-review steps; executives might need a concise review introduction. These are selection examples, not required pages or sample sheet names to create. An inventory-plus-demand user may see one prioritized Home while retaining both roles' effective access. Review-only navigation must be paired with separately configured [Security permissions](#security-authoring), not inferred from card text or placement.

##### Application Illustration: Generate, Upload, Place and Verify

For every new Plan application, include one purpose-designed AI illustration in native Home unless the user opts out or supplies a preferred image. Choose a visual explanation of that application's actual planning decisions and connected outcomes, not a generic landscape or a copied application's artwork. This design default does not bypass image-tool consent, licensing, data-handling or upload permissions. For updates, preserve existing user-authored images unless their replacement is explicitly requested.

**New observed evidence:** an authorized fresh read of the specified application's Item Baseline role content returned five items and four rows after a user inserted, uploaded, resized and moved an image. The image remains an ordinary `type: "image"` item; it is referenced by the second row, directly below the existing hero and before the instruction text/cards. The screenshot and row order do not establish that the image is above the hero. Its active configuration has an opaque asset `source` and `sizingMode: "fill"`; its row has a finite positive `height` and `isHeightManual: true`. The public 125-part definition still exposes only `homeLayout.roles: []` and `show: true`, not the complete provider-owned layout or uploaded image bytes. These observations verify saved content/placement, not asset portability, image generation or independent reading-mode acceptance.

The Home image handler calls the configured asset service's `upload({file, feature: "home-layout", scope: EAssetScope.WORKLOAD})`, then stores its returned `fileId` in `imageConfig.source`. The asset-service provider supplies the current approved backend/token/workload context. This is a source-backed client contract, not a new public Fabric upload endpoint or a universal headless HTTP payload.

The inspected upload validation accepts PNG, JPEG and SVG MIME types, up to `5 * 1024 * 1024` bytes. Prefer an actual PNG from the image generator; validate its MIME/bytes and file size before upload rather than merely renaming an extension. Recheck target-build limits if they differ. The image resolver fetches opaque asset references through `getAssetUrl` and creates a revocable browser display URL; that temporary URL must not become the persisted source.

1. **Plan the illustration.** Derive a sanitized, non-sensitive visual brief from the business purpose: principal planning areas, their relationships and the outcome users review. Prefer a clean, wide composition with a restrained palette compatible with Home. Do not copy the example's mountain image, business names, dates, source IDs or artwork. Do not send confidential data, actual employee/customer records, private screenshots, model exports, credentials or sensitive business figures to an image-generation service.
2. **Generate one actual image.** Use an available, authorized AI image-generation tool and inspect the resulting file for relevance, misleading content and readable composition. Follow that tool's explicit-request/consent requirements; skill prose alone does not grant authorization or credits. Avoid embedded numbers, tiny text and fake live charts; keep the application title, explanation and essential meaning in accessible native text. Do not claim that drafting a prompt or drawing an unrelated placeholder completed image generation. If generation is unavailable, denied or fails, disclose the gap and retain independently supported Home work; do not silently substitute an unrelated stock image or automatically retry a cancelled/failed generation.
3. **Upload into the destination workload.** Validate format/size, then use its supported asset uploader with the Home feature and workload scope above. Record the returned reference before saving layout content. Do not construct a file ID by encoding a guessed path, reuse another workload's reference, persist a local filename or `blob:` URL, or embed the image generator's external link as if upload had succeeded. Resolve any CLI upload route from its actual asset provider rather than guessing an endpoint.
4. **Create and place the block.** Allocate a unique local image `id` and `instanceId`, set `imageConfig.source` to the returned `fileId`, and add a row referencing the item `id`. A good default is a full-width standalone image row near the top, directly below the hero and above instructions/navigation; use a different explicit position if requested. Move it by editing ordered `rows`/`itemIds`, not merely the `items` array. Preserve all unrelated identities, text, sheet-card settings, role content and priority.
5. **Size for the content.** Use `fit` when the entire illustration or diagram labels must remain visible; use `fill` only when crop is acceptable and the important subject survives. Resize through the row's supported numeric `height` and manual-height state, preserving aligned `widths` and optional fields. Keep source pixel dimensions, row height, relative ratio and image sizing mode distinct. Choose height from the actual image, viewport and navigation needs; do not copy the captured manual height as a default or push all useful Home content below an oversized image. If an alternative hero background is requested, inspect its separate cropping/text-contrast behavior rather than adding a second competing illustration.
6. **Save and verify the separate resources.** Upload and role-layout save are separate operations, not a proven transaction. Hydrate fresh content/ETags, save through the actual legacy/V2 contract, then independently read back the item, source, sizing, row order/height, role priority and Home visibility. Verify asset retrieval and ordinary reading-mode rendering, crop, scroll behavior and sheet-card access for the intended audience. An image is illustrative/static, not live model data, an access grant or proof of a functioning workflow. If alt text is required, resolve a supported native facility or retain a meaningful adjacent text description; do not invent an `alt` field.

Replacement in the inspected image handler can delete the previous asset after updating draft state; it is not established as transactional, rollback-safe or reference-counted. Do not replace/delete user assets merely to follow the new-application default. On partial upload/save failure, report the completed phase and orphan/recovery state; clean up only an owned, proven-unreferenced asset with appropriate authorization.

**Illustration acceptance:** distinguish brief prepared, image generated, target asset uploaded, layout persisted and image rendered. Require evidence for each completed stage. For cross-workspace deployment, upload/resolve destination assets and rewrite only the owned references through the verified portability contract; copying provider JSON or exporting `homeLayout` alone does not transfer pixels. A missing generation/upload/rendering capability is an explicit affected gap, not permission to fabricate success.

##### Reconcile Captured Requests With Existing Contracts

Keep item-definition export/import, role-layout service content and role security/assignment as three separate contracts. Both exports reported in the guide contain `properties.homeLayout.roles: []`, despite a populated role-layout request and configured UI. **An empty exported roles array does not prove that Home Layout is absent.** Resolve storage mode and supported role-layout reads before concluding there is no content. Do not fetch the guide's live example Plans or transplant their content as a template. The guide also reports that the public PlanProperties schema did not declare `homeLayout`; that absence supplies no conversion contract and does not invalidate the inspected client feature.

| Guide observation | Reusable interpretation | Existing knowledge or remaining boundary |
| --- | --- | --- |
| Baseline Home role operation | `__everyone__` is a reserved baseline role identity; role identity is an operation argument, not an added body field. | Resolve custom-role IDs from the approved external profile; do not use display names. This is not a public Fabric REST endpoint or permission to replay captured credentials. |
| Body contains `homeLayoutOrder`, `data.items`, `data.rows`, `etag` | Content uses the shared layout; the token is opaque, not a timestamp or identity to calculate. | Retain the [mode-specific save contracts](#home-storage-and-save-boundaries), including fresh ETags, separate order/visibility operations and explicit conflict decisions. A single order value does not prove ranking direction, tie behavior or omitted-role handling. |
| Empty exported roles array versus populated service body | Exported workload metadata is not necessarily a complete backup of service-owned Home content. | Do not insert the entire role-layout body into `roles[]`; legacy role layout and V2 data have distinct envelopes. Import restoration remains unverified. |
| Hero/text titles and descriptions contain encoded JSON | Parse the outer body, then the selected rich-text string; serialize the edited document back to a string. | Preserve paragraphs, formatting, node types/version fields and unrelated nodes. The guide's single-paragraph replacement function is fixture-only and must reject other shapes, not flatten real rich content. |
| `preview-cards` example has no state | A minimal block can coexist with rendered cards and search; the root sheet catalog is separate. | This capture does not establish card resolution or overrides. Existing source inspection establishes `instanceState.previewCards.columns`, `.unSelectedEntityIds` and `instanceState.cardDescriptions`; do not invent sibling `sheets`, `columns` or `hiddenSheetIds` fields. |
| Image `source` decodes from Base64 to a workload-scoped storage path | The observed source is an encoded asset reference, not image bytes or a public URL. | Do not assume every possible source string has this encoding. Preserve existing references for text-only edits; new target assets require supported upload and returned references, not copied source-item paths. |
| Only `fill` captured; hero has no explicit source | The default banner can render without a custom image reference. | Source-backed `fit`/`fill` support above remains established at that layer. The sample does not establish hero image replacement, asset portability or complete rendering acceptance. |
| No Show or card settings in the captured request | Absence from one operation is not feature absence. | Source inspection already places Show at workload `homeLayout.show` and card settings in their shared-content fields. Do not replace these known contracts with a universal request for another capture. |

The captured five-block/four-row composition illustrates content versus placement, not a mandatory template or full constructor:

| Row order | Block type | Block count |
| --- | --- | --- |
| 1 | header-image-text | 1 |
| 2 | text | 2 |
| 3 | preview-cards | 1 |
| 4 | image | 1 |

`items` owns content; ordered `rows` and their ordered `itemIds` own placement. Row references use item `id`, not editor `instanceId`. Reordering only `items` is not an established move operation. Reconcile deletion/duplication across records, row references and corresponding widths together. Preserve positional null widths, nullable height/ratio values, optional `isHeightManual` presence and numeric precision; the sample's manual card/image heights are not size defaults or proof of a rounding rule. Existing normalizer behavior can restore a default layout from empty/invalid rows, so clearing arrays is not a reliable blank-Home operation.

##### Home Layout Acceptance Checks

- Start an authorized update from the target's current role content and a lossless snapshot/hash, not the guide's source payload, ETag or asset references. Preserve existing local item, instance and row identities and unrelated properties. New-role/content construction must use the actual supported creation convention.
- Check item/instance/row uniqueness, every row reference, positional width counts, allowed block types, at-most-one hero/cards and supported geometry. Parse nonempty rich-text strings independently and verify intended edits without losing other nodes. Preserve the existing intentional-empty-string behavior; do not force every empty value through JSON parsing.
- Resolve role, sheet and asset identities independently. Check duplicate sheet names, correct exclusions versus selections, and assets that load under the intended user's permissions. Never treat a Base64 storage path as transferred pixels or an upload endpoint.
- Re-read content, order, Show and images after save; test restricted single-role, multi-role and baseline users in ordinary reading mode. Check newly eligible sheets, card hiding versus security hiding, real navigation and read-only behavior independently. The Security screenshot's broad baseline is an observed configuration, not a recommended default.
- Verify process-image labels, text wrapping, card descriptions and three/four-column layouts at intended viewport sizes. Check Fit/Fill cropping and first-open behavior separately from editor preview; no uploaded image is a live or automatically secured workflow.
- Exercise concurrent edits and partial V2 saves using approved test resources. Reconcile completed phases before retry, never silently force stale content. Verify any authorized export/import separately for layout, assets, role linkage and security; a successful layout-content save is not proof of portable deployment.

These are authoring and acceptance instructions, not new native authorization evidence. The supplied guide and screenshots authorize learning only: no role grants, membership changes, asset upload, Plan save or live reference retrieval follows from this update.

### F25 Security

Intent: invoke Planning/PowerTable security and RLS governance controls, not
author an ACL from presentation properties.

| Inspected state / branch | Consequence |
| --- | --- |
| `isEditMode`, current entity, active visual | Availability depends on mode/context; Planning can require pivot assignments. |
| `isPTManageAccessRLSEnabled`, `isPlanningSecurityRolesEnabled` | Separate PowerTable/Planning gates. |
| `isPlanningSecurityGovernanceEnabled` | Panel opens SECURITY_ACCESS tab when enabled, otherwise default open behavior. |
| `generalSettings.securityAccess` | Reads `currentUserRole`, `accessConfig`, `isArtifactOwner`; these are not an exported ACL schema. |
| `hasSecurityGovernanceAccess(...)` | Decides availability using current user and access configuration. |
| PowerTable unsaved changes | Can require confirmation/discard refresh before opening security. |
| Legacy Planning branch | Forwards `fabric_security.security` toolbar action rather than mutating an ACL here. |

**Gap:** concrete RLS store/services, role/filter/membership DTOs, backend validators and persistence, selected feature-gate semantics, target identity resolution, and ALM mapping. Do not claim security is excluded from ALM, runtime-only, or automatically portable based on this entry point. No security JSON recipe or fabricated user identifiers are supplied.

For [approval workflows](#approval-workflow-authoring), protect decision, policy, audit and release fields as well as amounts. Keep input formulas, field permissions, model RLS, persistence authorization and decision history distinct. A DAX flag does not grant access, and a user able to rewrite approval state can undermine a status-based input rule. Test effective-user enforcement separately from visual appearance and current-state timestamps.

#### Security Authoring

Use Security to translate business responsibilities into explicit sheet and planning-action permissions. This guidance incorporates the supplied Security Enterprise Guide v4: 56 slides, 56 speaker-note pages and five embedded documentation screenshots. Its October 22, 2026 review was not independently re-audited here. Screenshot settings are documentation examples, not the finished business profiles. The deck explicitly reports no backend or runtime verification. Its signed-in-user MWC identity and Power BI-equivalent Build/RLS behavior are forward-looking product direction, not proof that a target deployment uses that path.

##### Separate the Access Layers

| Layer | Business responsibility | Boundary to preserve |
| --- | --- | --- |
| SQL or OneLake source | Tables, folders, rows and columns available to the source connection | Resolve storage mode, supported engine and effective connection identity. A SQL policy is not automatically copied to files, mirrors or writeback destinations. |
| Semantic model | Static region/entity RLS or dynamic user-to-scope mapping; OLS for source tables/columns and metadata | Model roles are not Plan roles. Build alone does not bypass consumer RLS/OLS; source-model Write, including Contributor/Member/Admin in that model workspace, does not provide a restricted consumer test identity. |
| Fabric workspace/item | Open, reuse and author the appropriate item | Source model Read + Build and destination Plan authoring rights are separate. A Contributor in a separate Plan workspace need not become an editor of the source model. Plan input/formula authoring does not itself edit that model. |
| Plan session persona | Viewer consumes, Stakeholder contributes values/collaboration, Planner authors planning structures | Activity-based persona and tenant/capacity eligibility do not create workspace, model or custom-role grants. A custom role named Planner is not the Planner session persona. |
| Plan role | General sheet access plus Measures, Scenario, Writeback and Comments | Row scope still comes from the model. Plan Hidden is not model OLS or proof that sensitive values are withheld from every response. |
| Governance and Home | Who administers governed settings; how permitted sheets are presented | Home card visibility and layout priority are presentation, not security-role selection or permission revocation. |

For DirectQuery with supported SSO, source policies evaluate the delegated user; without SSO they evaluate stored connection credentials. Direct Lake similarly distinguishes user SSO from fixed identity, and OneLake versus SQL-endpoint paths have different enforcement/fallback behavior. Import applies source restrictions at refresh, not again for each viewer; model RLS/OLS governs subsequent consumer queries. Source-workspace editors can have broader rights than OneLake consumer roles. MWC determines the model query identity in the supplied product direction, not every downstream source or destination identity. Inspect actual configuration before promising end-to-end user delegation.

Use explicit model RLS assignments, including relationships for a dynamic identity-to-region mapping. Design views from permitted fields: referencing an OLS-denied column can produce an access error, not a clean blank. Do not solve that failure by granting model Write. See the deck's platform references for [model RLS](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security), [OLS](https://learn.microsoft.com/en-us/fabric/security/service-admin-object-level-security), [Build](https://learn.microsoft.com/en-us/power-bi/connect-data/service-datasets-build-permissions) and [Direct Lake security](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-security-integration); their presence here is not a fresh documentation or environment verification.

##### Configure Roles and Assignments

1. Establish the intended audience, existing Fabric/model access, eligible session persona, enabled security layout and authorized administrator. Opening Security requires eligible edit mode, sheet/data context and governance access. A learning request does not authorize role creation, assignments or grants.
2. In Security -> Roles -> Add Roles, create a nonblank trimmed name, case-insensitively unique, at most 255 characters, with an optional description of at most 1,000 characters. Reserve Item Baseline. Creating a name is separate from saving access configuration; do not rely on unverified new-role backend defaults.
3. Configure General for every relevant sheet, then Planning -> Measures, Scenario, Writeback and Comments. Save Changes on the valid access draft. In V1, scope is chosen separately for each permission family. Back to Sheet protects unsaved changes; Discard abandons them and Cancel retains the draft.
4. Open Users -> Assign Role; select at least one authorized person and one custom role, then Add. Entra groups and batch-save layouts are conditional. Update an existing user's Roles cell rather than adding a duplicate. Item Baseline cannot be assigned explicitly. The assignment list includes explicitly assigned users, not everyone who can access the item.
5. Present allowed sheets through the existing [Home contract](#f24-home-layout), then verify the affected restricted identity. Home Preview is not an effective-permission simulator; the supplied review found no security View as role feature. Do not invent impersonation, role cloning, reset, import/export or native JSON controls.

In the reported UI, Item Baseline is protected from rename/delete and its presence is configuration-dependent. Custom-role Update changes name/description; deleting a role removes that assignment from its users, not their Fabric access. Removing a user's last custom role is described by the UI as returning to baseline. Other direct/group roles and source permissions remain relevant. Signed-in-user permission refetch was reported, but timing for other open sessions was not established; refresh/reopen is an acceptance step, not a guarantee of immediate revocation.

##### Sheet and Feature Permissions

The following V1 states express configuration intent, not certified backend enforcement. General can list Planning, PowerTable and Intelligence sheets; do not extend Planning-specific conclusions to the other workloads.

| Visible | Read Only | Intended sheet state | Conditional V2 equivalent |
| --- | --- | --- | --- |
| On | Off | Editable subject to feature permissions | Read + Write |
| On | On | Review only | Read |
| Off | Off | Hidden | Hidden |

Visible Off clears and disables Read Only; Off/On is not a configurable V1 state. Missing sheet entries are reported to load as visible/editable; V2 unset sheet permissions default to Read + Write. Sheet Read Only versus a writable measure, direct access to hidden sheets, and hidden response data remain runtime/backend questions. For a reviewer, configure measure Read and writeback Off explicitly as well as sheet Read Only; these complement, rather than prove, independent server enforcement.

| Planning family | V1 controls and reported defaults | Required distinction |
| --- | --- | --- |
| Measures | All Sheets or Specific Sheets; Read + Write, Read, Hidden; default Read + Write | Includes data-input and forecast measures together, not model OLS. Eligible sheets need at least one such measure. Specific scope permits per-measure levels. Reported client restrictions also exclude protected measures from forecast batch, auto-forecast and insert-scenario choices; hidden-data withholding and backend write refusal remain unverified. |
| Scenario | All Sheets or Specific Sheets, then per-scenario View; default On; eligible sheets need a scenario | View does not establish create/edit/delete rights. Actual filtering was not traced in the supplied client review. |
| Writeback | All Sheets or Specific Sheets; On/Off; unset and newly selected Specific-sheet entries default On | Input editing is separate from invoking writeback. Client gating, restricted logs/destination controls and a fresh settings check were reported, not independent destination/backend authorization. Automatic writeback also needs access, licence and destination prerequisites. |
| Comments | All Sheets or Specific Sheets; View, Add, Lock/Unlock, Star; V1 defaults all On | View is required for the other three; turning it Off clears those permissions on save. This reported UI dependency qualifies the public description of independent checkboxes. Thread locking is not input-cell locking; additional role permissions for replies, mentions, attachments or ownership changes are not established. |

**Specific Sheets is not deny-by-omission.** The screenshot explicitly warns that unconfigured sheets default to Read + Write. The supplied V1 review reports denial-only storage for Specific Scenario/Writeback, so an absent entry loads as allowed. Select at least one eligible sheet for Specific scope and enumerate all applicable sheets/measures/scenarios, including explicit restrictive feature settings for sheets hidden by General. Do not combine All Sheets defaults and per-sheet overrides as if V1 were V2. Review every added sheet and newly applicable feature before rollout.

Conditional V2 uses Default Permissions plus per-sheet Exceptions for measures, scenarios, writeback and comments; detailed exceptions can select all or particular measures/scenarios. Deleting an exception removes the override. Measures default Read + Write and writeback defaults On. Scenario levels include Read + Write, Read and Hidden, but the operation meaning of Read remains unresolved. Comments without View mean No Access, with dependent actions cleared. V2 relayout and V1 use different reported stored shapes; the review found no client migration, which proves neither failed migration nor safe backend conversion. Confirm enabled flags and the supported transition. Create Snapshots and Manage were inactive in the reviewed Planning surface, not generally available controls. Copy From Sheet belongs to Reading View Customization, not Planning permission copying.

##### Baseline, Multiple Roles and Governance

Public documentation describes most-permissive access per feature across multiple Plan roles, but the supplied review did not inspect the backend merge. Public baseline wording (all users) and reviewed UI wording (unassigned users) differ. Choose an explicitly restrictive baseline, subject to authorization, rather than depending on a broad baseline being narrowed by a custom role. Interpret inverse controls such as Read Only by effective capability, not a naive Boolean union. Home's highest-priority visible layout does not select the winning security role. Adding a Plan role does not broaden model RLS or grant an OLS-denied column.

Security Access governance offers Yes, No and Specific Contributors only, with reported default Yes when unset. Admins, Members and the item owner retain governance access. Specific requires at least one selected person and excludes groups in that selector. Governance covers security and governed sheet operations, with related settings; do not promise every sheet create/delete or approval-management operation remains available to a blocked Contributor. The conditional OneLake Set up access link concerns writeback data and does not import source-model policies. Session upgrades remain subject to tenant/capacity rules, not a workaround for governance or access restrictions.

##### Security Business Patterns

For a review role, create and save the role, configure Sales Plan and Summary as Visible On/Read Only On (V2 Read), hide Workforce Plan, set allowed measures Read and hidden-sheet measures Hidden, turn writeback Off everywhere, permit only intended scenarios and optionally Comments View. Assign the actual approved reviewers only after configuration. For Sales Plan alone, also hide Summary. A set of permitted sheets is individual sheet configuration, not a separate sheet-group object. The deck screenshots retain broader documentation example settings; do not copy them as the completed review profile.

The following illustrative Sales Plan profiles separate measure ownership from source-row ownership. Every profile hides Executive Reserve. They are intended settings, not tested entitlements. In the complete example, Item Baseline hides Sales/Workforce and permits Summary Read, with scenarios/writeback/comments Off; Summary is read-only for custom roles, other hidden sheets receive restrictive feature settings. Set the actual baseline only with authorization.

| Responsibility | Sales Budget | Rolling Forecast | Finance Adjustment | Sales writeback | Sales comments |
| --- | --- | --- | --- | --- | --- |
| Regional planner | Read + Write | Read | Read | Off | View, Add |
| Forecaster | Read | Read + Write | Read | Off | View, Add |
| Controller | Read | Read | Read + Write | On | View, Add, Lock/Unlock, Star |
| Regional planner plus Controller | Read + Write | Read | Read + Write | On | View, Add, Lock/Unlock, Star |

The dual-role row is the documented most-permissive expectation to verify, not a resolved precedence algorithm. All three single-role examples use Base scenario only; a separate strategy role can be configured for Base and Downside, with actual filtering still to verify. HR receives Workforce inputs instead of Sales access. An executive receives Summary measures Read, writeback Off and optionally comment View, with source scope independently defined by its model role. Adding/moderating comments also requires the appropriate session eligibility. Removing Controller should remove its additional grants only if no remaining role, group or baseline supplies them.

Illustrative amounts, in thousands: source actuals `1200 + 800 + 1500 + 2500 + 1000 = 7000`; a supported fixed-identity source connection limited to the first four groups exposes `6000`, while the regional user's model RLS selects `1200 + 800 = 2000`. Denying a confidential source column through OLS leaves those permitted revenue amounts unchanged when the view avoids that field. These are separate source and model identities, not sequential filtering guaranteed for every storage mode. RLS-excluded rows are absent from the model result; diagram cells labelled Hidden are explanatory, not real placeholders.

Budget starts at `1320 + 880 = 2200`; the regional planner changes the first input to `1380`, giving `2260`. The forecaster separately changes forecast `2150` to `2180`; Finance Adjustment remains `50`, writable only by its permitted responsibility. A controller needs an appropriate saved/shared version available in its session, eligible persona/licence, writeback access and an independently authorized destination. Writeback On does not transfer unsaved edits, create approval/handoff, or carry source RLS to the destination. A simpler single-sheet fixture is budget `110 + 5 = 115`, visible to a measure-Read reviewer who cannot edit it under the intended configuration.

##### Security Acceptance Checks

- Record actual deployment, flags/layout, storage mode, source/model/destination identities and every access source before testing. Use approved restricted identities without source-model Write, not an administrator whose source permissions bypass consumer RLS/OLS. Resolve real identities; never fabricate membership identifiers from screenshot labels.
- Test authorized source rows and permitted fields, OLS-denied dependencies, visible/hidden sheets through Explorer and direct links/API responses, and hidden measure values in responses/exports. A disabled control or absent card is not proof of data withholding or server refusal.
- Exercise editable versus protected measures, bulk/forecast-related operations, sheet Read Only combined with writable measures, and allowed/denied manual and automatic writeback. Check backend/persistence rejection and separately authorized destinations, not only toolbar states.
- Verify scenario filtering and its actual operation rights; comments View dependency plus add/lock/star enforcement and role-to-runtime mapping. Check comment thread locks separately from cell locks and approval state.
- Test no role, one role, multiple roles, direct/group membership, removal of one/final role, new-role defaults, role deletion and other active sessions. Retain the unresolved baseline/merge questions until effective-user results resolve them; do not promise immediate cross-session revocation.
- Add a sheet or applicable feature and check every permission family for permissive omission. Verify conditional V2 defaults/exceptions and any supported transition separately; do not infer migration or PowerTable/Intelligence enforcement from Planning UI evidence.
- Verify save/reopen, authorized governance selection and role-specific Home in ordinary read mode. Keep evidence of expected versus actual results and failures. Learning/static checks, Home Preview, JSON validity and API save success do not certify authorization enforcement. Runtime tests and any access changes require separate authorization.

### F26 Themes

Intent: apply built-in/custom themes while respecting visual-specific overrides. IThemeConfig has optional string `id`, required string `label`, imported `themeType: EThemeType`, optional `clonedFromThemeType`, required structured `theme: ITheme`, optional boolean `deleted`.

| Native layer | Inspected behavior |
| --- | --- |
| Theme definition | `themeType` belongs to the definition interface; complete EThemeType literals and ITheme leaves are not inventoried. |
| Workload selection | updateThemeType replaces `state.theme` with `type`, `id`, and `appliedThemes`; do not rename selected-state `type` to `themeType`. |
| Reset planning themes | Preserves current selected-theme siblings while replacing `appliedThemes`. |
| Iframe visuals | ThemeService delegates to host `applyThemeChange` except on init/page-switch branches. |
| Shape visuals | Uses previous-theme comparisons through `applyUpdateOnlyIfUnchanged`, not unconditional replacement of every custom style. |

Typography/color readers access responsive font size, auto font color, font family, structural background and outline colors. Those reads are a subset, not a complete custom-theme schema. **Gap:** theme factories/enums, save/load effect, full custom-theme leaves, plan/visual precedence, schema/public-vs-native differences, and ALM import/export. Do not invent a `themeMeta` destination or promise that switching theme overwrites all overrides.

### F27 Embedding

For end-to-end business composition, use [Intelligence Dashboard Business Authoring](#intelligence-dashboard-business-authoring), [bookmark authoring](#bookmark-business-authoring) and the [fifteen dashboard cases](#bookmark-dashboard-business-examples). Those functional workflows complement, but do not complete, every embedding variant's native construction and lifecycle contract.

The linked implementation handles embedded PowerTable pagination UI, not the complete embedding/authentication/layout contract. EmbeddedPowerTablePagination reads `footerConfigStore.footerConfig` and active visual ID.

| Runtime member / action | Inspected behavior |
| --- | --- |
| `pageMetadata.hide_pagination` | Hides pagination controls when truthy. |
| `pageMetadata.page_number`, `total_pages` | Passed to pagination controls; not authored as artifact metadata here. |
| `onPageChange(action,page?)` | Action is `first`, `previous`, `next`, `last`, or `page`; page parameter is numeric. |
| No active visual | Returns without dispatch. |
| Host command | `onFooterInteraction` with Pagination tab/item, `toolbar_item`, stringified page value and click interaction. |

**Gap:** host-side pagination handler, actual persisted visual paging configuration, embedded/direct visual declarations, source/permission ownership, public definition wrappers, and import/export. Do not conclude that every embedding setting is runtime-only from this narrow anchor. No guessed `embeddedConfig` part is introduced.

#### Observed Embedded Owner and Placement Checks

The supplied dashboard constructor and readback verifier show a separate, bounded composition: a hidden direct Planning owner remains in `definition.json.sheets`, while a Reporting sheet lists an `isEmbedded` reference to that owner's portable `visualId`. Page placement is checked independently in the Reporting sheet's `properties.reactiveVisualProperties` against its runtime visual identity. Portable owner identity and runtime placement identity are separate mappings; do not generate a second Planning owner or assume the embedded declaration imports the owner's missing companion parts.

Check native identity-bearing fields inside a proposed new visual as well as its outer portable ID. A supplied build discarded a newly copied heading because it retained the original `preVisualId`; changing its registry GUID did not resolve that hidden identity. This is a collision risk observed in a discarded candidate, not an executed runtime failure or a universal uniqueness rule for all embedded references. Use the actual family allocator/writer, keep intentional references to existing owners intact, and do not invent or blanket-delete native numeric IDs. Removing that run's new heading is not permission to remove existing user visuals or omit a required introduction.

Check that every embedded source resolves to exactly one direct owner, that its family-specific properties and input companions survive import, and that page placement resolves to the intended embedded instance. Preserve measure IDs and metadata, not only page counts or frame geometry. The historical verifier checks those saved records but explicitly leaves Planning rendering and slicer interaction unverified; this does not close the full embedding, authorization or import contract above.

Slicer selection, visual filter registration and page/source filters are distinct. Inspect overlapping name/ID bindings and context at both owner and embedded page when results disagree. Do not copy the constructor's clearing of competing filters as a universal repair: it can remove intentional business restrictions. Require scoped approval for changed filter behavior and test standalone versus embedded results under the intended context and permissions.

#### Bookmark Dashboard Owner and Navigator Evidence

The independently parsed Bookmarks/Intelligence package has one PLANNING source sheet and one REPORTING dashboard. The source remains visible: the hidden-owner arrangement in the earlier example is not an embedding requirement. The dashboard references the same Planning visual GUID with isEmbedded true; its properties stay under the direct owner's visual directory, with no second Planning-properties part under the dashboard. The two direct dashboard-owned navigators have BI_RUNTIME_INPUT declarations and properties.visualType 203 in this snapshot. Preserve the existing [route/schema discrepancy](#route-selection); this observation is not permission to bypass schema validation or invent a new portable visual discriminator.

The dashboard's properties.reactiveVisualProperties contains one embedded placement keyed by a local visualId. Its string value is 1, matching the source preVisualId and originEntityId in this sample, not the portable GUID. Position and dimension are canvas placement; the sample canvas is 1600 by 900 with percentage element scaling. Resolve the real source-to-instance mapping and geometry writer; do not reuse that key, source IDs or geometry as creation defaults, duplicate the owner, or apply heading-collision cleanup to an intentional embedded reference.

Both navigator properties use visualState.navigatorState. Its type is PAGE_NAVIGATOR_TABS or BOOKMARK_TABS; the common visual code alone does not distinguish them. navigatorTabsState is horizontal, selects all bookmarks with an empty hiddenBookmarks list, has allowDeselection false and gap 5 in this snapshot. Bookmark-specific shared fields do not establish page-navigation behavior. navigatorButtonState contains actionType NONE and bookmarkId null: that unused single-button state is not evidence that a tab navigator needs repair or a hard-coded bookmark target.

No slicer visual, embedded PowerTable or second Planning embed is configured here. properties.syncSlicerConfig, workloadLevelFilterAssignments and dashboard pageLevelFilterAssignments are empty arrays; syncVisualsState and explicit embedded/navigator visualInteractions are empty objects. These locations guide inspection of a richer sample but are not an active interaction workflow or a complete slicer constructor. The screenshots establish visible source/dashboard presentations and navigator labels, not click outcomes, persisted edits, permission enforcement or multi-visual filter propagation. The visible collaboration-connection advisory is not a verified persistence configuration and does not authorize provisioning a connection.

## Construction and Update Procedure

Apply the [shared design baseline](design-standards.md) to all artifact updates, preserving compliant existing presentation and reporting unsupported settings. Its definition-level and rendered-layout checklists are distinct gates, not implied by JSON/schema acceptance.

1. Select the requested feature section, source revision, visual family, variant, and actual migration route.
2. Resolve target metadata and reference domains. Do not mix sheet IDs, visual database IDs, portable GUIDs, measure IDs, and measure GUIDs.
3. Use only evidenced native mutations and persisted paths. Apply exact discriminator casing and distinguish omitted, null, empty, zero, and false.
4. Preserve unrelated siblings and unknown existing fields unless a verified transformation removes them. UI dispatch names are not JSON property names or merge guarantees.
5. Apply the actual save/export transformations and required companion parts. If this section does not close that chain, follow [route fallback](#contract-gap-resolution-and-route-fallback), inspect the applicable owners and construct the resolved route. Return a named blocker only if a required prerequisite remains unavailable; never invent an ALM recipe.
6. Parse candidate JSON, validate the applicable schema and source constraints, and verify import/restoration where available. Report which of these checks actually ran.

## Validation and Maintenance

This reference records bounded implementation/ALM facts and published API contracts, not deployed-application evidence. Documentation maintenance authorizes no service writes, data changes, bootstrap or model-backed tests. Scope subsequent operations to the current request and the lifecycle authorization boundary.

During authorized maintenance, recheck affected sections for relevant changes to serialization types, feature gates, defaults, export/import mappings, schemas or handler registrations. Record the inspected revision and relevant local changes without promoting untouched contracts to newly verified status. Ordinary authoring follows [contract reuse](#contract-reuse-and-source-investigation), not a mandatory repository audit. No feature is generation-ready solely because its entry-point folder was found or its UI types were read. Every unresolved property/mapping remains `UNKNOWN` until supported by evidence.

### Self-Contained Construction Contracts

When extending a selected feature during authorized maintenance, make its construction guidance usable without reopening source. Before calling it a complete recipe, document:

- Applicable visual family, variant, representation, save route and known compatibility scope, with prerequisites and authorization boundaries.
- Exact persisted paths, types/discriminators, accepted values, defaults and absent/null/empty behavior for that variant.
- Required companion records, identity allocation/reference rules, dependency order and update-preservation semantics.
- A complete minimal feature example with explicit bindings and packaging requirements; distinguish illustrative placeholders from a submission-ready payload and never copy business/resource identities.
- Reproducible pre-save checks, saved-definition comparison and required native behavior checks, each with its actual result and limitations.

A property table or parseable example alone is not a complete construction recipe. Retain `partial` or `unverified` status for missing construction or execution evidence; this checklist does not upgrade existing sections or require every feature to be completed before using an already covered branch.

### Source Citation Portability

Existing relative implementation links assume sibling repository checkouts and may not resolve in a standalone package. They are provenance aids, not required runtime dependencies of the documented contract. For new or refreshed citations, record repository identity, inspected commit, repository-relative path and owning symbol, plus relevant local modifications; a line number alone is not stable provenance. Use a verified commit-pinned repository URL when available, or resolve the repository-relative path against the reader's local checkout root. Do not invent remote URLs or imply private sources are publicly accessible.

Consult the existing ledger for recorded provenance; do not assign its latest revision to every historical citation. Unresolved attribution remains an evidence gap. A broken source link is not permission to guess a payload, and recording this convention does not repair or revalidate all existing source links.

### Must / Prefer / Avoid

| Rule | Guidance |
| --- | --- |
| Must | Read the matching feature contract and required dependencies; use its documented rules within their recorded scope. Source citations are optional evidence reads unless the contract reuse policy triggers investigation. |
| Must | Treat partial as evidence coverage, not unsupported functionality. Use covered branches and resolve concrete required gaps through route fallback; keep unperformed runtime checks separate from pre-save gates. |
| Must | Distinguish native settings, runtime events, API requests, persisted records, exported files, and REST transport. |
| Prefer | For an update, use the specified current artifact's verified writer and preserve unrelated state and input identities. For creation, use request/model-derived construction contracts, not another artifact. |
| Prefer | Validate an isolated requested variant rather than combining every discovered option into one example. |
| Avoid | Guessing enums, scope wrappers, IDs, hidden-property encoding, default materialization, or target-user mapping. |
| Avoid | Copying stale comments, editor state, polling timestamps, compiled expressions, or lock caches into ALM. |

### Rejection Checklist

- Reject a complete-artifact claim when the chosen feature's core ALM envelope/import mapping is still UNKNOWN.
- Reject a flat untagged rule as a replacement for the unresolved JetStream rule-node union (F07).
- Reject `LinkedRow` as an invented tenth CustomRowType variant (F11).
- Reject a partial `feature` object update that assumes a deep merge of every Filter Context toggle (F08).
- Reject assumptions that constructor visibility and omitted-deserialization visibility are identical (F12).
- Reject blanket claims that all writeback connection fields are removed (F17).
- Reject personal-bookmark portability based on the inspected report-only export query (F23).
- Reject serialized editor/preview/clipboard history as an established header/home ALM configuration (F24/F28).
- Reject a permission/ACL JSON recipe based only on the Security toolbar gates (F25).
- Reject a claim that invalid allow-input boolean conversion defaults to editable in the inspected batch readers (F30).
- Reject a JSON/native example as a tested formula, schema-valid part, successful round trip, or live deployment unless that exact level was executed.

### Verification Limits

Use each fact within its recorded evidence and compatibility scope; consult the routing ledger when its provenance is needed. A source revision records an inspected checkout, not a deployed-build guarantee. Recheck source only under the contract reuse policy or authorized maintenance. The independently rechecked ALM/input/Charts and Text/Shape/theme owners support only their stated layer. Other feature sections retain bounded source anchors and named gaps; this cleanup is not exhaustive re-verification of every implementation branch or a complete new-Plan constructor.

| Validation layer | Status / limits |
| --- | --- |
| Source inspection | Partial: concrete owners/declarations and selected ALM readers/writers; no exhaustive property/branch closure. |
| Public documentation/schema | Published contract is distinct from local implementation. Resolve requiredness, discriminator, casing and type conflicts for the selected route; open bags do not certify support. |
| Syntax/links/transport | Focused checks can establish parseability, link validity and byte packaging, not feature semantics. |
| Native execution/import/runtime | Unverified until scope-matched execution, saved-definition and native acceptance checks are performed. |
| Complete construction | Input/row/cube identities, companion records, rewiring, model binding variants and import restoration remain partially unverified. |
| Connected behavior | Full transformation, source/consumer refresh, cancellation/status and materialized-result security contracts remain partially unverified. |
| Presentation | Home, font/group styling, full theme and embedding writer/import/render boundaries remain partially unverified. |

The catalog is a bounded routing aid, not an exhaustive coverage denominator. No feature becomes generation-ready because a link resolves, a schema accepts an open object or an older application works.

## 2026-11-13 filter, KPI, query-identity and connection correction

The self-contained [consumer repair contract](consumer-repair.md) supersedes sparse KPI-store examples, lowercase filter-pane positions and any assumption that native input-record row IDs are query output-column IDs. It also records semantic-model/workspace intake and generic FabricSql OAuth connection selection. Preserve the detailed business/use-case guidance above. API readback is not rendered or financial-propagation proof.
