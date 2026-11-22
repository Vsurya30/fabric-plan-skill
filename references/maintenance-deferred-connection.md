# PowerTable sheets with deferred connections

When a source is resolved, prefer the complete bundled constructor in
`powertable-alm-construction.md`; this fallback is only for genuinely unavailable
connections. A generic FabricSql connection path alone does not establish that
the connection is unsuitable for a specific Fabric SQL database.

When maintenance sheets are requested, a missing or unusable connection should defer source binding, not remove the sheets or stop independent Plan deployment. Create native `POWERTABLE` sheets in the same Plan and make them visible. Clearly report **connection required**. Do not promise editing, lookups, saved rows or data access until binding is complete.

**A deferred sheet is only a navigation entry and displays the PowerTable welcome/setup screen.** It is not a table with columns that merely needs credentials. Use this fallback only when the user accepts an uninitialized sheet; the current request takes precedence over an earlier willingness to defer. Preserve the sheet and continue independent modules, but report maintenance as incomplete. Never report an empty `workloadItemEntityVisuals` array as successful table construction.

## Blank sheet contract

`runtime.maintenance_shells.blank_powertable` constructs a new sheet registry entry with a fresh record GUID, a requested name/order, `sheetType: "POWERTABLE"`, `isHidden: false` and `workloadItemEntityVisuals: []`. Add its ordinary `sheets/{recordGuid}/sheet.json` part. A source-less PowerTable does not require an invented visual, fake connection GUID, fake columns or placeholder source settings. Source initialization creates the PowerTable visual and its source records later.

Keep intended schema/table and outstanding lookups/rules in the deployment manifest. The manifest is a handoff artifact, not a made-up Plan property or a guarantee that the table exists. Do not fabricate missing key, identity or lookup metadata. Do not replace a working PowerTable with a blank sheet.

## Prepare and publish through APIs

1. Export a fresh baseline and retain its exact part bytes.
2. Prepare `requests.json` as an array, for example `[{"name":"Employee Master","table":"dbo.DimEmployee"}]`.
3. Run `python plan.py prepare-maintenance --baseline baseline.json --requests requests.json --out prepared`. This constructs the patched transport envelope, readable definition and maintenance manifest; it performs no remote mutation or SQL operations.
4. Publish the envelope with the existing API update operation. Poll Location/Retry-After and reconcile failures before any retry. This is a same-item addition, not a new Plan.
5. Read the native entity catalog and each new page. Verify PowerTable type, correct names, visibility and absence of an initialized source visual. For new reports set final visibility in the public create definition.
6. Re-export and verify all requested PowerTable sheet entries. Distinguish API-persisted navigation from a visually observed setup screen.
7. Compare the pre/post existing pages and chart assignments. Keep `properties.superFilterAssignments[]` for every chart grouping/measure using `ensure_chart_filters` and `audit_chart_filters`; retain external Context, page filters, slicers and existing selections. Also call `consumer_bindings.audit_visual_consumers` with current query metadata: chart and filter IDs can both be wrong while agreeing with each other. Apply the scoped `restore_import_bindings` repair from this deployment's intent when import remaps output suffixes to input-row IDs, then read back and export again. See `consumer-repair.md`.

The helper rejects existing names/GUIDs and leaves every existing non-root part byte-identical in the submitted envelope. If a previous attempt created only some sheets, reconcile the native catalog and rebuild requests for only the genuinely absent sheets; never create duplicates or delete existing records to retry.

Live API evidence on 2026-11-13: seven requested unconnected sheets were accepted in one same-item publication. Native catalog returned PowerTable entity type 30, visible value 20 and no initialized visuals; the final export retained the seven POWERTABLE entries. This validates the deferred sheet contract. It does not prove a rendered setup screen, lookup completion or database write readiness.

## Connect later

Resolve an authorized connection and target SQL artifact, inspect the real table/key/column schema, then initialize the existing PowerTable sheet using the documented source route and its actual page/visual context. Use `creationMode: 2` for an existing table; this does not authorize physical table creation. Keep `schema` in the initialization request distinct from the exported `schemaName` field. Finish the requested lookup column configurations and edit policies only after target source metadata is available. Verify source details, schema and row save/reopen separately.

An OAuth token for the Fabric control plane is not itself a persistent SQL connection credential. A listed connection and an imported `connectionId` do not prove workload credential resolution or SQL access. A `PT_WB_9013` failure can be workload credential lookup failure even when the Fabric connection catalog lists that ID.

## Keep connection evidence separate

When learning from an authorized reference, inspect only its PowerTable sheet/visual parts, source records, column configurations, source settings and the relevant API table schemas. Do not inherit its other application modules or hardcode its identifiers. Record the distinction among cloud connection ID, PowerTable source ID, visual ID, SQL artifact ID, host, database and schema/table. A connection catalog entry, successful source import, schema response and row save are different evidence stages.

If source-details GET fails but table/schema succeeds, report both outcomes and inspect the returned definition before changing routes or assuming the whole connection is broken. Do not change methods or invent query parameters merely to hide a failed check.

The additional script-deployed reference inspected on 2026-11-13 exposed two initialized PowerTable sources. Both returned real SQL table schemas in the actual visual context. The product table's integer primary key was not an identity column; the commercial-validity table's integer primary key was identity-generated. Never treat every primary key as auto-generated or omit a manually supplied key during insert. The source-details requests returned HTTP 400 even while schema requests succeeded. This demonstrates why source-details failure alone is not a sufficient connection verdict. Exact connection/source export evidence is recorded separately from these schema checks.

## Diagnose a welcome screen before changing properties

1. Read the current native entity and page inventory. A type-30 entity with `visuals: []` has no grid to style. The directly owned type-30 visual, its `dataSourceId` and `properties.properties.visualState.columnMeta` are separate requirements. Use `runtime.powertable_readiness.inspect_native` to classify the observed state. Use `require_configured` only for a configured-table completion claim; do not block unrelated Plan modules.
2. In an ALM package, inspect the matching visual declaration and its `properties.json`, `source.json`, `columnConfigs.json` and `sourceSettings.json`. A `sheet.json` alone cannot instantiate the grid. Preserve the PowerTable properties envelope and source-record GUID relationships. Do not copy source or column IDs from an unrelated report.
3. Compare the item's bound connections using `GET /v1/workspaces/{workspaceId}/items/{itemId}/connections` in its resolved Fabric API environment. This is different from listing connections available to the user. A bound semantic-model connection does not establish a SQL source binding. A missing SQL binding is evidence to investigate, not proof of the cause of any given credential error. Do not apply the semantic-model-only `bindConnection` API to a Plan or invent a Plan connection writer.
4. Run existing-table initialization only with the actual target source, valid cloud connection and verified owner-context contract. Reconcile the returned source object and the post-request native catalog. When the attempt fails before visual creation, record `sheet-only-uninitialized`; do not fill `dataSourceId` with a copied reference number or keep creating duplicate connections.
5. After initialization, read the actual table schema in the resolved visual context and compare physical columns with the visual's column configuration. Ordinary chart pivot assignments are not a PowerTable readiness test: both working reference PowerTables had empty top-level `pivotAssignments`.
6. Record schema-read, data-render, lookup and save evidence separately. Source-details failure must not suppress an independent table/schema read. A stuck export does not prevent native property comparison; keep the uncompleted export operation ID and do not claim its source parts were retrieved.

Live comparison on 2026-11-13 confirmed seven target type-30 sheets without any visuals versus two reference type-30 visuals with non-null source IDs and populated column metadata. The reference item listed a FabricSql connection, while the target listed a PowerBIDatasets connection only. These findings explain the missing grid construction and identify a separate binding discrepancy; they do not establish a successful repair or the precise internal cause of the earlier credential lookup error.

Public connection-inventory contract: https://learn.microsoft.com/en-us/rest/api/fabric/core/items/list-item-connections
