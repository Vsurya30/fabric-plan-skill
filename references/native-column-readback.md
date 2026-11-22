# Native column readback in Fabric SQL and OneLake

For **new or migrated Plan artifacts in OneLake storage mode**, a saved native
column catalog may expose its numeric type as `dataInputType` rather than
`columnType`. This is a readback representation difference, not evidence that
creation failed. It applies to the native column validation used by From Sheets,
From Queries and other native column construction/registration paths.

## Request versus saved record

| Context | Type field | Required behavior |
| --- | --- | --- |
| Documented native create payload | `columnType` | Keep the current constructor/write contract. |
| Saved catalog, SQL-compatible shape | `columnType` | Compare against the requested type. |
| Saved catalog, OneLake shape | `dataInputType` | Compare the alias against the requested `columnType`. |
| Both saved fields present | Both | Require agreement before comparing to the requested type. |

Synthetic example of the relevant fields only (not a complete create payload):

```json
{"request":{"measureGuid":"123","columnType":6},"saved":{"measureGuid":"123","dataInputType":6}}
```

Use `runtime.builder_api.column_matches(actual, expected)` through the standard
`create_column` and `register_column` helpers. Missing, null, conflicting or wrong
types remain errors; string enums are not coerced to numbers. The comparison
still checks `columnMeta`, `measureGuid`, `name` and the outer
`boundToFilterContext` when requested. Do not infer the native type from
`columnMeta.data_type`, a label, a successful HTTP status or a row count.

This numeric native-column enum is distinct from a semantic/query assignment's
string `columnType` such as `Column`. Do not globally rename JSON fields or
rewrite POST payloads. Storage-specific identity rules remain in
[onelake-linked-values.md](onelake-linked-values.md): preserve SQL row IDs/sqlPk
and OneLake measureGuid/opaque query IDs according to the current catalogs.

## Resume after a successful save and failed readback

Keep the same Plan, owner visual and authored `measureGuid`, along with operation
receipts. Invoke the bundled creation helper again with the original intended
payload. It first reads the current owner-scoped catalog. A single matching saved
record returns `write: already-matched` with **no create POST**. A duplicate ID or
any type, metadata, identity, name or context mismatch stops validation; do not
allocate another ID or replay the mutation on another API version to bypass it.

The shared check also runs before companion registration. Retain normal current
ETag and unchanged-property safeguards for that separate save phase. Reading one
collection successfully does not authorize guessing another write route.

## Portable verification and evidence

`tests/test_native_column_type_readback.py` covers both saved formats, agreeing
and conflicting aliases, missing/wrong types, metadata/context validation,
creation with OneLake-only readback and retry from a fresh client. It verifies
that a previously saved column causes zero new create requests. Run from the
extracted skill directory:

```text
python -m unittest discover -s tests -p test_native_column_type_readback.py
```

The alias was observed on a saved OneLake native column on 2026-11-17. Offline
adapter tests validate the portable readback/resume logic; they do not prove
dashboard rendering, calculations, input writeback or refreshed data propagation.
Initial InfoBridge refresh remains optional when the saved wiring is correct.
No report export, chat history, credentials or local repair script is required
for this compatibility fix.


### v38 recipe adapter integration

Recipe extensions and quarterly review delegate all column creation to `runtime.builder_api.create_column`. The adapter resolves the current collection route before writing and validates existing/saved records with the OneLake type alias. Do not hard-code a v1 column POST in a recipe. Existing identities and pending-job boundaries are preserved.
