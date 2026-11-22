const { xxhash3 } = require("hash-wasm");

const MAX_U64 = (1n << 64n) - 1n;

// Matches Rust's Id::for_str, serialized as a decimal string.
async function generateDimensionId(sourceId) {
  if (typeof sourceId !== "string") {
    throw new TypeError("sourceId must be a string");
  }

  const hex = await xxhash3(sourceId);
  return BigInt(`0x${hex}`).toString(10);
}

async function generateDimensionHash(rowIds, colIds) {
  for (const ids of [rowIds, colIds]) {
    if (
      !Array.isArray(ids) ||
      ids.some(
        (id) =>
          typeof id !== "string" ||
          !/^(0|[1-9]\d*)$/.test(id) ||
          BigInt(id) > MAX_U64,
      )
    ) {
      throw new TypeError(
        "Dimension IDs must be arrays of canonical unsigned 64-bit decimal strings",
      );
    }
  }

  const input = `${rowIds.join("-")}__${colIds.join("-")}`;
  const hex = await xxhash3(input);

  // Matches Rust's {:x}: lowercase hexadecimal without leading zeros.
  return BigInt(`0x${hex}`).toString(16);
}

module.exports = { generateDimensionId, generateDimensionHash };
