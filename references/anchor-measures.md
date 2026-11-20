# Anchor measures: business grain, display and saved configuration



Use this guide when a policy belongs at a broader grain than the detailed plan,
or when a measure is needed by detailed formulas but should not repeat at every
hierarchy level. The user need not say **anchor**. First identify who maintains
independently different values and when those values can change.

## Find the right pattern

| Business request | Anchor decision | Detailed model keeps |
| --- | --- | --- |
| Enter one company-wide annual assumption | No row dimensions; Year | Employee/product/month detail and existing formulas |
| Maintain one regional policy per year | Region; Year | Independent region policies; detail uses its own region's policy |
| Share one product policy across regions | Product; Year | Region detail, without adding Region to the input grain |
| Change a department target quarterly | Department; Year + Quarter | Role/month detail; no implied monthly hiring schedule |
| Use a regional factor with no time variation | Region; no column dimensions | Period calculations; entry at Region × Total |
| Keep an assumption in leaf calculations, hide repeated assumption rows | Its real business grain; `display_at_all_levels: false` | Underlying values, formula dependencies and detailed output measures |
| Show an existing YTD measure once per region | Region; no column dimensions | Existing DAX/time intelligence; no input rights |
| Show a calculated quarterly margin only where meaningful | Region; Year + Quarter | Quarter profit ÷ quarter revenue; not average monthly margins |

An omitted axis means **All rows** or **Total column**. At least one dimension
must be selected across the axes. The dimensions form one joint intersection,
not a set of independent input levels. Product alone and Region × Product are
different decisions. Use unique identities when the same department/product label
appears under different parents. Do not add every parent merely to match the grid.

Recommend anchors when the measure's decision/display grain is coarser than the
sheet grain. Do not apply them to every measure. Keep an ordinary detailed input
when independent values really are required at each leaf. Use storage Context
for independent scenario/version coordinates outside the axes, From Sheets or
InfoBridge for cross-source reuse, and lookup for reference-table retrieval.
Anchoring is not a replacement for those capabilities or for a saved allocation
rule. Preserve explicit user choices.

Before authoring, record: measure identity and type; full sheet grain; independent
row dimensions; calendar cadence; eligible scope; existing aggregation and
distribution; consuming formulas; repeated-instance display preference; input
permissions/locks; and the visible entry intersection. Resolve only meaningful
ambiguities. Rates and amounts require different distribution decisions.

## Visibility without losing formula availability

This is a primary use case, not merely a cosmetic side effect. A region-level
assumption can be visible at Region while the employee/customer/SKU formula
continues to consume the applicable underlying value at its leaf grain. Use
`display_at_all_levels: false` to omit repeated non-anchor **measure instances**
where the layout permits. Do not remove the measure registration, hide the whole
measure via `visible: false`, delete inputs, replace formula references, or
zero/blank the data to achieve that appearance.

Functional examples (illustrative designs; not newly deployed examples):

| Scenario | Visible assumption | Detailed consumer and business reason |
| --- | --- | --- |
| Regional employee benefits | Region × Year: Benefits % | Each employee-month calculates raised salary × (1 + Benefits %). The employee cost remains visible; repeating Benefits % beneath every employee adds clutter. |
| Pharma market rebate policy | Market × Year: Standard Rebate % | Product/customer/month net revenue uses gross sales × (1 − applicable rebate). Keep policy on the market line, detailed revenue below. Tender-specific exceptions need separate business logic/grain. |
| Plant quality loss | Plant × Year × Quarter: Scrap % | SKU-month gross production = ceil(good-unit demand ÷ (1 − Scrap %)). Show the quarterly plant policy and detailed production, without repeated SKU assumption rows. |
| Regional freight uplift | Region × Year: Freight Uplift % | Route/customer/month freight cost uses its own baseline × (1 + regional uplift). Hide repeated policy rows, retain detailed costs. This is not allocation of an absolute freight pool. |
| Product standard price | Product × Year: Price | Store/customer/month revenue uses units × applicable price. Share across omitted Region only if pricing is truly global. Preserve product-specific annual input and detail revenue. |
| Department savings target | Department × Year: Reduction % | Account-month target expense uses baseline × (1 − reduction). Show the department target and account outcomes; detailed initiatives remain a separate plan. |

The policy rate may be copied into eligible leaves by established input behavior;
the anchor itself is not a new dynamic lookup, broadcast or calculation engine.
Existing detailed formulas continue to use those values. Hiding a row does not
prove that a not-yet-populated leaf has a value. Check the existing distribution
and formula path when requested; do not claim runtime propagation from JSON.

With display ON, repeated instances are visible but still read-only away from
the anchor. Display OFF does not guarantee every shared non-anchor **cell** is
blank. In Measures in Rows, a surviving region assumption row may still span
monthly columns shared with other measures. In default measures-inside-time
layout, omit that measure's columns in non-anchor time blocks. In Measures in
Columns, restrict that measure's own time block; retain other measures' detail.
Recommend Measures in Rows for a readable mixed-grain assumptions-and-outcomes
story; use Measure Model only when a logical hierarchy adds meaning. Grouping
does not change calculations, aggregation or input identity.

## Entry, totals and independent controls

Annual input is at the **Year subtotal**, not January or the first visible month.
Quarterly input is at the **Quarter subtotal**. No row dimension needs the All
row; no column dimension needs the Total column. Use year-qualified time levels
from the actual calendar. Do not invent Quarter/Month identities or add a
nonexistent Quarter when the actual axis is Year → Month.

Keep the universal defaults: Row GT ON, Row subtotal ON, Column GT ON, Column
subtotal OFF. An anchor needing an intermediate Year/Quarter entry is a scoped
exception: expose the required column subtotal on that sheet. The helper changes
only necessary hidden totals, preserving their existing visible placement.
Do not turn off the entry subtotal to hide repeated measure rows. Expansion and
subtotal/individual-node visibility are separate; ensure the intended intersection
is reachable without changing storage grain. The helper does not synthesize
unobserved per-node visibility or expansion properties.

Inputs and Forecast retain `ReadAndEdit` by default and any formula-based lock.
Anchoring narrows direct entry; display ON does not permit descendant entry.
An anchor-read-only descendant is distinct from an independently locked or
unauthorized cell. Applicable allocation from the anchor can reach eligible
children; independent locks and security remain effective.

For suitable rate/factor inputs, Average (Leaf) plus the existing
distribute-parent-to-children behavior can copy the rate. Do not silently change
aggregation or enable distribution on an existing measure while adding anchors.
Never copy an absolute $1m pool into every employee. Resolve an appropriate
allocation method for amounts. Formula/native measures remain calculated and
read-only; anchoring neither grants write rights nor supplies YTD logic.

## Saved JSON contract and executable scope

The supplied 26-slide deck and a fresh saved Plan definition were inspected on
2026-11-17. The definition has 21 `anchor_config` objects on managed measures,
including two native Power BI measures. They share one layout hash and have
`display_at_all_levels: false`. This is saved-configuration evidence, not a UI,
input-save or formula-execution test. `dataInputType: 6` alone does not distinguish
Native, Formula and DataInput; inspect the typed measure record and assignment.

Persist here, preserving the entire managed-measure member and its identity:

```text
properties.visualState.manage_measures[*].anchor_config
```

```json
{
  "row_dimensions": ["<current native dimension ID>"],
  "col_dimensions": ["<current native Year ID>"],
  "display_at_all_levels": false,
  "dimension_hash": "<computed hash of all current ordered pivot dimensions>"
}
```

IDs are exact decimal **strings**, including values larger than JavaScript's
safe integer. Resolve them from `rowDimensions`/`columnDimensions` using exact
`externalKey`, not display labels, data-input IDs, storage keys or model IDs.
The UI has an Enable Anchor Measure control; `is_enabled` was absent from all
21 exported configs. Do not insert it into this saved subtree or infer a general
disable payload from its absence. Disabling/reset serialization is not established.

Bundled `runtime.anchor_measures` provides:

- `capture_context(properties, owner_visual_id)`: computes the native layout hash
  from all current ordered pivot dimensions. Works with no existing anchors and
  rejects conflicting, mismatched or stale saved anchor state.
- `apply_anchors(properties, owner_visual_id, requests, ...)`: resolves selected
  fields, upserts only anchor configuration and necessary entry totals, and returns
  a local candidate/change list. It preserves input/formula records, aggregation,
  bindings, locks, storage mappings and every unrelated property.
- `save_anchors(client, entity_id, visual_id, requests, label, ...)`: resolves a
  fresh native Planning owner, rejects embeds/stale state, and uses the existing
  ETag-aware `/v1/workload/properties/batch/` writer. No new API is introduced.
  Reports submission, not rendered behavior or completed post-save verification.

**Hash contract (v43):** the supplied `dimension-hash-sample` establishes
seed-zero XXH3-64 and its exact serialization. The portable implementation uses
the existing bundled Python XXH3 engine, with no npm dependency or donor report.
`generate_dimension_id(exact_source_id)` produces an unsigned decimal string;
`generate_dimension_hash(all_ordered_row_ids, all_ordered_column_ids)` hashes
`rows.join("-") + "__" + columns.join("-")` and returns lowercase hexadecimal
without leading zeroes. See [dimension-hashing.md](dimension-hashing.md), the
unaltered supplied source, its tests and provenance record. Local replay matches
all six dimension IDs, the saved `f66e5cc9a49071b9` hash and all 21 anchor configs.
That replay used the earlier exported JSON, not a new live request or UI test.

No saved anchor is required to create the first one. Existing saved anchors must
agree with the computed current pivot hash and contain available dimensions. A
mismatch stops that anchor operation; it does not silently rewrite other anchors
or erase stored values. A captured context also guards the exact owner and state.
Never transplant IDs/hashes, hash display labels, or hash only the anchor subset.
Known active Pivot configs are resolved in order; ambiguous state is rejected.
After an axis change, resolve intended anchors against the new effective layout;
the builder does not invent a general reset or multi-layout migration payload.

Disable/reset serialization, partial-pivot edit enforcement, propagation and
rendering remain outside the hash proof. Base construction and saved-state
mutation are implemented; native execution still has its own acceptance boundary.

## Use the bundled builder

`plan.py discover "keep regional policy in employee formulas but hide repeated rows"`
routes to F20. `plan.py plan-intent` supports `shared-assumption` and
`display-anchor` after the agent interprets the business request. It records the
actual grain, consumers and distribution/display choices; it does
not choose constants or an anchor based only on keywords.

For offline authoring, pass exact current owner properties plus requests:

```json
{
  "properties": "<replace with the complete current properties object>",
  "owner_visual_id": "<actual owner identity in this JSON's namespace>",
  "requests": [{
    "measure_id": "<current managed measure ID>",
    "row_fields": ["PolicyRegion[Region]"],
    "column_fields": ["Calendar[Year]"],
    "display_at_all_levels": false
  }],
  "expose_entry_totals": true
}
```

```sh
python plan.py construct-native anchor --input anchor-request.json --out anchor-candidate.json
python examples/anchor-measures/example.py --out example-output.json
```

The example is a self-contained **synthetic** saved-owner fixture, using the
observed JSON shape and a hash computed from its remapped ordered dimension IDs. It demonstrates binding,
preservation and visibility requests; it is not a deployable reference artifact.
`examples/anchor-measures/saved-profile.json` catalogs all 21 saved selections with
remapped IDs and provenance checksums. No token, tenant, workspace, artifact or
private target identity is needed by the example or shipped as configuration.

For an authorized native update, use `builder-api anchor-apply` with the normal
application session config and a request containing `entity_id`, `visual_id`,
`requests`, and optional `expose_entry_totals`. The API helper obtains current
properties and computes the hash itself; do not pass the offline fixture. Save
the same actual Planning owner used by embeds. This scoped helper is useful for
existing measures and typed-input phases.

For a **new report**, use a per-measure `anchor` object in the ordinary base spec:

```json
{
  "key": "benefits", "kind": "DataInput", "label": "Benefits %",
  "aggregation": "AverageLeaf", "distribute": true,
  "default_value": {"Static": 0.22},
  "anchor": {
    "row_fields": ["Region[Region]"],
    "column_fields": ["Calendar[Year]"],
    "display_at_all_levels": false
  }
}
```

The example rate is illustrative, not a universal default. Resolve source fields,
calendar and business values from the actual request. The base builder supports
Native, Number DataInput, Forecast and Formula measures; typed input factories
retain their separate phases and can use the scoped helper after registration.
The builder generates dimension IDs from exact metadata keys, binds the selected
fields after the final pivot is constructed, computes the hash of the complete
effective pivot, and retains all typed records/formulas. `planning.anchor-measure`
is a composed capability. The import contract rejects omitted or altered requested
anchors and hidden required entry totals. Raw `anchor_config` options are rejected
in a symbolic base spec; they are native output, not user-facing builder syntax.

Run `python examples/anchor-measures/new-report.py --out candidate.json` for a
package-only first-anchor example. It uses synthetic metadata included in the
package and does not fetch or deploy a report.

## Full use-case context and evidence

Read [anchor-business-cases.md](anchor-business-cases.md) for the ten worked
business cases, combined workforce math, reporting examples and transfer rules.
Read [anchor-ppt-source.md](anchor-ppt-source.md) for the full extracted slide text
and speaker notes, including nuances not repeated in the concise guide. These are
source material, not authorization or executable product syntax. Deck highlight
colors illustrate entry semantics; keep the skill's source-role color defaults.

The saved profile establishes the four native keys and current ID representation;
the deck establishes business/design intent. Neither proves partial-pivot writes,
filter exceptions, new-member behavior, edit enforcement, allocation, disabled
serialization. The separate supplied snippet establishes hash generation. Collapse/hide is not actual dimension
removal and must not clear anchoring or values. Preserve the F20 contract's
remaining view/removal distinctions. Respect user-requested validation scope.
