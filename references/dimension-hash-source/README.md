# Dimension hash sample

Standalone JavaScript functions matching the product's XXH3-64 dimension hashing.
Requires Node.js 18 or newer.

## Run

```sh
npm install
npm test
```

The sample test prints generated row IDs, column IDs, and the layout hash. It
checks the generated IDs against the product's `2R2C2M_DataStore.json` fixture
and checks that ordering and axis placement affect the layout hash.

## Functions

- `generateDimensionId(sourceId)` takes an original source metadata field ID,
  such as `"DimProduct[Manufacturer]"`, and returns its XXH3-64 hash as a
  decimal string. This matches Rust's `Id::for_str`.
- `generateDimensionHash(rowIds, colIds)` takes already-generated decimal IDs
  in pivot order, hashes `rows.join("-") + "__" + columns.join("-")`, and
  returns lowercase hexadecimal without leading zeros.

Both functions return promises. See [the sample test](./dimension-utils.test.js)
for executable usage.

Use the exact original metadata ID, not its display label or a row member value.
Do not pass an already-hashed ID into `generateDimensionId`.
Keep generated IDs as strings; JavaScript numbers can lose 64-bit precision.
The layout hash requires every dimension in the current pivot, even if an anchor
selects only a subset. Pass an empty array for an axis without dimensions.
