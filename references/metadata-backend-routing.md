# Fabric SQL and OneLake metadata routing

Plan metadata uses Fabric SQL by default. With OneLake mode enabled, migrated
artifacts and newly created artifacts persist metadata in OneLake. An undefined
repository error on one API version is not sufficient evidence of a service-wide
outage. Preserve the same Plan and its saved components while checking the
appropriate metadata handlers.

## Bounded recovery

Use the relevant session helper when a requested feature needs a particular
metadata collection. Ordinary grid import has no native catalog preflight.

By default, entities and columns each use `auto`. A known artifact profile can
set `"nativeReadVersions": {"entities":"v2", "columns":"v2"}`. Explicit `v1`
or `v2` is strict; use `auto` when diagnosing a stale profile after migration.

1. Reuse the validated version for that collection in the current artifact
   session; otherwise try V1 first. Do not reuse another artifact's result.
2. On `native-repository-unavailable` (`findAll`, `findPaginatedRows`, `findOne`
   with an undefined repository), try the other **documented GET** version once.
   A catalog-route 404 permits the same check. A missing individual page does not.
3. Validate the returned shape, completeness, current owner and registration
   identities before accepting it. A malformed 200 is not a successful recovery.
4. Pin that collection's successful version. Entity V2 success does not establish
   column V2 success; a column-authoring operation reads the column catalog with `x-target-visual`.
5. If both handlers fail, stop dependent operations and record both errors. Keep
   the Plan ID and receipts. Continue work that does not require that capability.

No version fallback on 401/403, an unrelated 400/500, or transport failure. Existing
bounded transient GET retry rules still apply to the same URL. Never strip inputs,
formulas, Forecast or CF to work around a metadata failure; never create a second
Plan, migrate storage, or alter mode settings as an automatic repair.

## Exact supported scope

The bundled runtime no longer reads entity, page or column catalogs through the
workload API. Native workload access is limited to role-specific Home layout.

## Evidence and limits

On 2026-11-16, a live Budget application returned repository errors from V1 entity
and column catalogs, while V2 read eight entities and all 42 columns in three
Planning owners (13, 8, 21). All column identities and metadata matched its saved
definition. V1 Home roles/content and V2 InfoBridge metadata were independently
readable. No report changes were submitted for that diagnosis. This establishes
the compatible read routes; it does not prove physical storage contents, new
write support, calculated results, UI rendering or refresh propagation.

Resolving catalog access does not complete an unfinished financial application.
OneLake InfoBridge query metadata may return `Q...` IDs without numeric `sqlPk`.
The v33 [consumer contract](onelake-query-consumers.md) uses the actual query ID
in the qualified output assignment; the SQL profile retains its returned pk.
Do not cast, hash, truncate or synthesize a numeric query identity.
Validate scenario/period fields, skipped
totals, source grain and financial reconciliation separately. Keep incomplete
dashboards identified as incomplete.

The SQL/OneLake catalog readers and their synthetic example are no longer bundled.

## Visibility for new and existing pages

Set final visibility in the public create request for new applications. Existing-page repairs are a separate operation. The historical OneLake test required the native entity writer to expose an already imported hidden page. That result applies to changing an existing page. See [Business navigation](business-navigation.md) for the new-report flow.

The service may export a Formula source descriptor as `columnType: DI` while
other copies retain FORMULA. `export_lineage.reconcile` resolves the source's
visualId to the same export's dataInput owner, proves the exact measureGuid,
name, and actual Formula record, and corrects only DI-to-FORMULA descriptor
labels. It preserves values, formulas, IDs, transformations and all unrelated
parts. Other identity/type drift is rejected. Recheck all query consumers after
ALM, as described in [consumer-repair.md](consumer-repair.md); visibility readback
does not establish consumer identity or rendering.
