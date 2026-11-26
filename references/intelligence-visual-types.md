# Intelligence dashboard visual type coverage

An Intelligence dashboard can hold more visual types than this package constructs. Use
this guide to say precisely which type a visual is, what this package may change, and
what must be reported instead of improvised. Classification reads current exported or
locally built properties; it never contacts a service and never rewrites a visual.

## Coverage ledger

| Dashboard content | What this package does | How |
| --- | --- | --- |
| KPI card, column chart | Constructs from the current model or query catalog and completes field registrations. | `intelligence`, `integrated-variance` |
| Semantic slicer, text block, Page Navigator | Constructs with placement and navigation rules for a new or existing dashboard. | `intelligence`, `navigator` |
| Embedded Planning workbench | Constructs the page-local reference to the directly owned visual. | `embed` |
| PowerTable | Constructs a visible sheet, with deferred source binding when no connection resolves. | `powertable`, `maintenance-shell` |
| Decomposition, organizational, row and measure trees | **Names and preserves only.** No tree definition part is constructed here. | `visual-type-coverage` |
| Matrix, Table, Gantt, Map, Shape, Image, Box, Adhoc Matrix, buttons, bookmark tabs and other Analytics+ chart families | **Not named or constructed.** Keep them unchanged and report them as unclassified. | — |
| In-table micro-charts | Not dashboard visual types; they are a column feature of a grid. | — |

## The tree family

The tree types share one discriminator field. `runtime.intelligence.tree_visual_types`
returns the four values and their display names; `runtime.intelligence.classify_visual`
reads either position of that field, the same one a card writes as `CARD`:

```python
from runtime.intelligence import classify_visual, tree_visual_types
props = exported_visual_properties            # one dashboard visual
kind = classify_visual(props)
# {'family': 'tree', 'chartType': 'ORGANIZATION_TREE', 'visual_type': 'Organizational tree'}
```

`classify_visual` returns `None` when the value is absent or belongs to a type this
package does not name. `None` is an answer, not a license to guess: keep the properties
unchanged, then report the type as unclassified.

Each tree carries its own configuration family in the visual state: orientation
(left-to-right or top-to-bottom; the organizational tree defaults to top-to-bottom),
layout (the decomposition tree is restricted to the normal layout), node view
(full or minimal), node components (variance, variance percentage, sparkline, child
count), node template shape (simple, card, metric summary), connector line and arrow,
legend, per-node conditional formatting, header key-performance measure and sparkline
colors. None of these has a bundled writer, default table or formatter here.

## Rules that keep a tree intact

1. **Never retype a tree.** A card-state writer fills the store slices a KPI needs and
   sets the discriminator to card, which would flatten a tree into a single number. The
   bundled card writer refuses when `classify_visual` reports the tree family; pass tree
   properties through untouched and say so.
2. **Do not copy a numeric visual type into a definition part.** This package has three
   separate numeric domains in play: the value a card or chart writes in its own
   properties, the type numbers returned by the native entity catalog, and the tree
   member of the host application enum. Only the first two are evidenced by exports in
   this package. Assigning the third to the first is an unverified inference. In the
   product a tree is visual type 25 (`TREE`) plus its chart type, while Analytics+ also
   has a decomposition tree chart under type 50. `classify_visual` reads only the chart
   type, so it can't tell those two apart; check the visual type before relying on it.
3. **Availability varies by destination.** The product gates the decomposition and
   organizational trees and drops them when a page loads without their feature, so a
   readback can't prove a tree is available. Its editor doesn't offer row or column
   trees, and the measure tree depends on a tenant switch in the Planning grid. When a
   type isn't available, report
   that visual type as unavailable rather than substituting a card, chart or Planning
   grid the user did not ask for.
4. **Tree field roles are not Planning pivot roles.** The organizational tree expects a
   single parent identifier role plus a field role; the decomposition tree expects an
   actual-value measure. Chart and card audits, pivot layout hashes and column
   presentation checks do not classify a tree and must not be used as readiness tests
   for one.
5. **Keep the gap independent.** When a tree is one requested element among several,
   continue the supported modules and record the tree as an incomplete item, the same
   way an unbound PowerTable sheet is recorded. An unconstructed element is never
   evidence that the whole request failed, and never a reason to drop it silently.

## Evidence

Type names, discriminators and configuration families come from the product
implementation of these tree visuals. No Plan definition part containing a tree is
shipped in this package, so nothing here establishes the exact saved shape of a tree
visual, and the rules above are preservation rules rather than construction rules.
Classification and the card-writer refusal are covered offline by tests in this
package; rendering, tenant availability and any future tree authoring remain
unverified until a current export of the actual destination is inspected.
