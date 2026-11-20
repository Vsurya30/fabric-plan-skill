const assert = require("node:assert/strict");
const { test } = require("node:test");
const {
  generateDimensionId,
  generateDimensionHash,
} = require("./dimension-utils.js");

test("generates IDs matching the product fixture and prints the layout hash", async () => {
  const sourceRowIds = [
    "DimProduct[Manufacturer]",
    "DimProduct[ColorName]",
  ];
  const sourceColIds = ["Date[Year]", "Date[Quarter Name]"];

  const rowIds = await Promise.all(sourceRowIds.map(generateDimensionId));
  const colIds = await Promise.all(sourceColIds.map(generateDimensionId));

  assert.deepEqual(rowIds, [
    "14835107197258497178",
    "8441616133237296584",
  ]);
  assert.deepEqual(colIds, [
    "11664616959742279520",
    "12377755039553282686",
  ]);

  const dimensionHash = await generateDimensionHash(rowIds, colIds);

  console.log(
    JSON.stringify(
      {
        row_dimensions: rowIds,
        col_dimensions: colIds,
        dimension_hash: dimensionHash,
      },
      null,
      2,
    ),
  );
});

test("layout hashing preserves dimension order and axis placement", async () => {
  const first = await generateDimensionId("Date[Year]");
  const second = await generateDimensionId("Date[Quarter Name]");
  const original = await generateDimensionHash([first, second], []);

  assert.notEqual(
    original,
    await generateDimensionHash([second, first], []),
  );
  assert.notEqual(
    original,
    await generateDimensionHash([], [first, second]),
  );
});

test("rejects invalid source IDs and invalid or imprecise dimension IDs", async () => {
  await assert.rejects(generateDimensionId(123), TypeError);
  await assert.rejects(generateDimensionHash(null, []), TypeError);
  await assert.rejects(generateDimensionHash([14835107197258497178], []), TypeError);
  await assert.rejects(generateDimensionHash(["Date[Year]"], []), TypeError);
  await assert.rejects(generateDimensionHash(["18446744073709551616"], []), TypeError);
  await assert.rejects(generateDimensionHash(["01"], []), TypeError);
});
