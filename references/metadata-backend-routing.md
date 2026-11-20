# Fabric SQL and OneLake metadata routing

Plan metadata uses Fabric SQL by default. With OneLake mode enabled, migrated
artifacts and newly created artifacts persist metadata in OneLake. An undefined
repository error on one API version is not sufficient evidence of a service-wide
outage. Preserve the same Plan and its saved components while checking the
appropriate metadata handlers.

## Bounded recovery

Use `runtime.session` helpers or the bundled diagnostic:

```text
python plan.py native probe --config destination.json --input empty.json --run diagnostics --label metadata
```

`empty.json` contains `{}`. The config needs `powerbiApiBase`, `tokenEnvironment`,
`workspaceId`, and `planId`. The credential is supplied through the named process
environment variable, never a config value. The probe performs authentication and
metadata GETs, with zero report writes. Its result records attempted routes,
selected versions and direct Planning owner column identities/counts.

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
   column V2 success; read the column catalog separately with `x-target-visual`.
5. If both handlers fail, stop dependent operations and record both errors. Keep
   the Plan ID and receipts. Continue work that does not require that capability.

No version fallback on 401/403, an unrelated 400/500, or transport failure. Existing
bounded transient GET retry rules still apply to the same URL. Never strip inputs,
formulas, Forecast or CF to work around a metadata failure; never create a second
Plan, migrate storage, or alter mode settings as an automatic repair.

## Exact supported scope

| Collection | Fabric SQL handler | OneLake handler |
| --- | --- | --- |
| Entity catalog | GET `/v1/workload/entity/` | GET `/v2/workload/entity/` |
| Entity properties | GET `/v1/workload/entity/{id}/properties/` | GET `/v2/workload/entity/{id}/properties/` |
| Column catalog | GET `/v1/visual/datainput/column/?order=ASC&take=-1` | GET `/v2/visual/datainput/column/?order=ASC&take=-1` |

These are CoreAPI routes within the artifact-scoped proxy returned by the workload
token exchange. This is not a host substitution or general V1-to-V2 rewrite.
Home, properties batch, InfoBridge, engine operations and PowerTable retain their
own contracts. In particular, a V1 Home read may work while V1 entity reads fail.

`create_column` resolves the column profile independently before the already
documented V1/V2 column POST. It sends a mutation only once, journals its intent,
and reads back on that same version. An explicit version remains strict. Read
success is evidence of metadata access, not a guarantee that the writer works.
Never replay a failed/ambiguous POST against another backend; reconcile the same
identity before resuming. SQL/OneLake reads do not authorize storage migration.

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

`examples/metadata-backend-routing/build.py` exercises both profiles with synthetic
responses, without a prior report, chat, credentials or repair script. Tests cover
bounded retries, strict configuration, authentication, migration changes, separate
collection profiles, mutation non-replay and current-context headers.

## Navigation publication on OneLake

Use `runtime.navigation_publish.publish` after native geometry save. Resolve the
current entity collection and select its independently verified writer: SQL uses
PUT `/v1/workload/entity/{id}/`; OneLake uses PUT `/v2/workload/entity/{id}/`.
The request is `{ "isHidden": 20 }` for visible or 10 for hidden. Both bundled
deployment runners use this helper and verify flags plus unchanged memberships.
Never replay a failed mutation against another version.

Live readback on 2026-11-16 confirmed all four OneLake dashboards became visible
through V2 while names, membership and order remained unchanged. ALM accepted
the earlier false flags without exposing those existing pages, although hiding
owners via ALM had worked. An accepted ALM operation is therefore insufficient;
do not use it as the visibility publication path for either profile.

The service may export a Formula source descriptor as `columnType: DI` while
other copies retain FORMULA. `export_lineage.reconcile` resolves the source's
visualId to the same export's dataInput owner, proves the exact measureGuid,
name, and actual Formula record, and corrects only DI-to-FORMULA descriptor
labels. It preserves values, formulas, IDs, transformations and all unrelated
parts. Other identity/type drift is rejected. Recheck all query consumers after
ALM, as described in [consumer-repair.md](consumer-repair.md); visibility readback
does not establish consumer identity or rendering.
