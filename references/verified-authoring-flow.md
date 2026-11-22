> v39: Rows/Columns already define storage grain. External Context is only for additional stored selections, never ordinary page/global filtering. Connected Planning owners must match Context; query outputs must retain it. Read [storage-context.md](storage-context.md) for the bundled guards and build-time query evidence.

# Follow the verified authoring flow

V31 adds [bounded SQL/OneLake metadata recovery](metadata-backend-routing.md). A
single V1 repository error must not be reported as a global service outage.

Use the package's established construction and deployment flow. Translate the
business requirements into its documented inputs; do not invent a replacement
workflow because a helper is unfamiliar or one feature needs a separate phase.

## Required execution order

1. Keep the original application requirements and base specification unchanged.
   Discover the requested features and read their contracts before choosing a
   route. For a matching use case, use `plan.py usecase ...` and its recipe. For
   a supported base application, use `plan.py build` / `provision`. A small
   orchestration wrapper may call documented helpers; it must not redefine their
   payloads, bypass checks, or substitute a different application.
2. Build and import the supported base together: semantic Values, Number inputs,
   formulas, native Forecast, and conditional formatting. Include Arial, enabled
   native Home, rich Intelligence coverage, complete Navigator padding and a Page
   Navigator on each dashboard. Preserve existing formula equality, monthly time
   hierarchy, dimension mapping and default-Sum behavior.
3. Use a separate native phase only where the selected bundled contract requires
   it, for example resolved From Sheets bindings, typed commentary, dependent
   formulas, native dashboard geometry or Home layout persistence. Record that
   exact phase and its dependencies in the recipe/ledger. A need for LongText does
   **not** justify removing unrelated Number inputs, Forecast, formulas or CF from
   the import. A native POST payload is not interchangeable with an ALM record.
4. Check the candidate against the original base specification **before import**.
   The CLI writes `construction.json`, `buildRequest.json` and `importContract.json`.
   For a composed candidate run:

   ```text
   python plan.py check-import-contract --spec application.json --construction draft/construction.json --candidate candidate.json --out import-contract.json
   ```

   Keep `application.json` as the original base spec, not a filtered copy. The
   check detects missing inputs/formulas/Forecast, changed measure kinds or
   formulas, absent registrations and missing/changed CF in either rule store.
   Build/provision/usecase paths enforce these checks on new or resumed builds.
5. When a requested feature creates an additional native column, its writer reads the collection it needs. Skip a separate preflight.
6. Complete the requested feature phases and check the authored grid in the public definition. The public create carries the final visibility. The public create includes dashboard geometry. Only Home uses native layout operations. Ordinary grid delivery has no native registration scan or manual validation step.

## Promote reusable repairs into releases

When authoring exposes a verified reusable compatibility or construction fix,
do not leave it only in a delivery folder, copied runtime or local repair script.
Promote it into the main Fabric Plan skill and shared bundled builder, add
behavioral regression coverage, and update the entrypoint, module discovery and
focused reference. Regenerate the GitHub Copilot package from the same updated
source, retaining all earlier fixes and resources. This is part of completing
the reusable repair so another machine receives the same behavior.

Validate the rebuilt capsule and Copilot ZIP through clean extraction, using
only shipped resources and synthetic fixtures. Verify package hashes, previous
resource preservation and the affected execution/resume paths. Do not depend on
prior chat, task exports, cached logic or working-folder Python imports. Keep
credentials, target identities and task-specific business data out of the skill.
Report package/static evidence separately from live UI and business validation.

Use verified contracts; a reusable release is not permission to guess a missing
service shape, relax unrelated checks or replace a requested workflow. For the
OneLake `dataInputType` / `columnType` readback alias, use the shared validator
and same-identity resume described in
[native-column-readback.md](native-column-readback.md). Do not replay a successful
create merely because an older validator rejected its saved representation.

## Unsupported requirements and partial scope

`prepare-scope` is a **local diagnostic**, not an instruction to deploy its reduced
output. `provision` now returns `mutation: none` when that analysis omits or
substitutes requirements. Resolve the gap through the bundled component route
and explicitly composed recipe. Continue independent local preparation. If no
verified route exists, explain the exact unsupported feature; do not replace a
requested workflow with reference-only sheets, dummy inputs or zero formulas.

A deliberately requested read-only/reference sheet remains valid. An explicitly
requested partial deliverable is also valid; record that revised scope honestly.
Do not silently narrow scope just to obtain a successful import. Typed metadata
such as `inputKind: LongText` or task-specific `typed` objects cannot be passed to
the base Number constructor: it rejects them instead of silently creating a
numeric input. Use the documented typed factory and its selected native phase.

## Native repository failures

Observed error signatures include HTTP 500 `findPaginatedRows` / `findAll` and
HTTP 400 `findOne`, with "Cannot read properties of undefined". The transport
classifies these as `native-repository-unavailable`, preserves the HTTP status,
and does not repeat a deterministic failure on the same URL. The session helper
may try the other documented metadata GET handler once, per the v31 profile. HTTP 401/403 remain a separate
authentication classification. Mutation journaling continues to prevent replay.

Preserve the existing Plan ID and operation receipts. Stop only the dependent
native operations only after the bounded metadata handlers are exhausted; record
the failing phase/route/status and inspect fresh
definitions and exact workload routing. Resume the same artifact after a verified
change or service recovery. Do not create duplicate apps, blindly retry the same
request, invent a V2 endpoint, add a dummy input, or use an undocumented backend
initialization patch. Supported independent work may continue where it does not
depend on the failed capability.

## Evidence and limits

The investigated delivery imported reference-only definitions for four complex
apps after its custom script removed every non-Native measure and all CF. Native
column reads then failed and the deferred components were not created. One app
whose import contained real inputs and Forecast had readable native columns.
Adding a read-only formula to the incomplete apps did not resolve their errors.

These observations establish the workflow deviation and missing components.
They do **not** prove which backend initialization or service defect caused the
repository error. This release prevents the destructive staging shortcut and
adds accurate failure handling; it does not claim to repair the Fabric service.
No target application was changed while implementing these safeguards.

## Portable regression example

`examples/verified-authoring-flow/build.py` constructs a complete synthetic base
using only package resources, then proves that a stripped candidate is rejected.
It needs no prior chat, report cache, token, or task-local repair script. The
offline tests also exercise typed-input rejection, no reduced-scope live writes,
native read failure with zero dependent POSTs, and independent API-version checks.


### v38 recipe adapter integration

Recipe extensions and quarterly review delegate all column creation to `runtime.builder_api.create_column`. The adapter resolves the current collection route before writing and validates existing/saved records with the OneLake type alias. Do not hard-code a v1 column POST in a recipe. Existing identities and pending-job boundaries are preserved.

### v43 anchor construction and scoped update


Interpret broader-grain assumptions and visibility-with-leaf-formulas requirements
through F20, anchor-measures.md and dimension-hashing.md. New base reports accept
per-measure `anchor` options without a prior saved hash. Complete typed measures
are retained; exact source IDs and full effective pivot axes produce the native
XXH3 hash. Import checks reject missing/altered anchors or hidden required entry
totals. Existing-owner/typed-phase updates use `construct-native anchor` and
`builder-api anchor-apply` with the same preservation guards. Never copy the
example's IDs/hash. Stale anchors require explicit reconciliation; the helper
does not invent disable/reset state. A submitted save is not a runtime check.
