# Native dimension IDs and anchor layout hashes

Use for anchors, first-anchor creation, `dimension_hash`, current Pivot order,
dimension identity and portability. Discover **F20**.

## Exact contract

1. Take the exact original source metadata field ID (`externalKey`), including
   hierarchy prefixes, punctuation and case. Encode it as UTF-8 unchanged.
2. Hash it with seed-zero **XXH3-64**, not XXH64, FNV, SHA or a salted variant.
3. Serialize the unsigned result as a canonical decimal string. Reuse native IDs
   already supplied by the current owner; do not hash those IDs a second time.
4. Resolve **all** dimensions in current Pivot row order and column order, even
   dimensions not selected by this particular anchor. Join IDs on each axis with
   `-`, and join the two strings with exactly `__` (two underscores).
5. XXH3-64 that UTF-8 string and serialize lowercase hex without `0x` or leading
   zeroes (Rust `{:x}`). Zero itself would be `"0"`. Do not force 16 characters.

```python
from runtime.dimension_hash import generate_dimension_id, generate_dimension_hash
rows = [generate_dimension_id(k) for k in original_ordered_row_field_ids]
cols = [generate_dimension_id(k) for k in original_ordered_column_field_ids]
layout_hash = generate_dimension_hash(rows, cols)
```

An empty axis is `[]`; its joined string is empty. Two empty axes hash `__`, but
an enabled anchor still needs at least one selected dimension. Hash generation
does not override that business/configuration constraint. IDs must be strings
from `"0"` through `"18446744073709551615"`, no signs or leading zeroes. Never pass
them through a JavaScript Number: these values commonly exceed 2^53.

| Exact source ID | Expected native ID |
| --- | --- |
| `DimProduct[Manufacturer]` | `14835107197258497178` |
| `DimProduct[ColorName]` | `8441616133237296584` |
| `Date[Year]` | `11664616959742279520` |
| `Date[Quarter Name]` | `12377755039553282686` |

Changing order or moving a dimension to the other axis changes the hash. Adding
or removing even an **unselected** dimension changes it. Different anchor grains
on one effective pivot share one layout hash; the selected `row_dimensions` and
`col_dimensions` arrays remain specific to each measure.

## Effective pivot and preservation

The builder resolves the established `visualState.pivot.configs` plus `active_id`
contract. A null axis selector inherits the base axis; an explicit ID list uses
that order (including an empty list). Cross-axis dimensions are resolved from
the current native dimension catalog. Unknown IDs, duplicate placement, conflicting
active state and hidden/missing active pivots stop authoring. For other saved/UI
pivot shapes, resolve the effective ordered axes first; do not guess from labels
or assume a UI empty selector has the same meaning as the compiled native list.

Existing anchors are checked against the current computed hash. A stale hash or
unavailable selected dimension is a scoped error, not permission to clear the
anchor or overwrite values. Mere collapse/hide does not change dimension identity.
Changing Pivot views is not authorization to migrate other anchors. General
disable/reset serialization and partial-pivot input enforcement remain separate
contracts. The local SHA-256 context signature only detects concurrent/context
changes; it is never used as the native `dimension_hash`.

## Implementation and evidence

- The operational implementation is Python:
  `runtime.dimension_hash.generate_dimension_id` and
  `runtime.dimension_hash.generate_dimension_hash`, over the bundled XXH3
  implementation in `runtime.identity`. No JavaScript runtime, npm install or
  saved donor hash is needed, and the reference JavaScript implementation and
  tests that accompanied the original notes are not distributed with this package.
- Local replay of an earlier exported report matched six source-field IDs,
  every anchor layout hash, and all 21 anchor configurations. No target IDs,
  tokens, report access or earlier chat are required by the portable builder.
- New-report and scoped-update examples plus regression tests cover first-anchor
  creation, selection versus full-layout hashing, pivot order, precision, stale
  state and input/formula preservation. This is offline evidence, not native
  rendering, edit enforcement, allocation or formula execution validation.

Read the anchor measures guide for symbolic builder options and the anchor
business cases guide for business-grain decisions.
