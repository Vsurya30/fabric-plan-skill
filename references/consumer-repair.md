# Filters, KPI consumers and Fabric SQL connections

This contract describes preservation and identity checks for generated and
updated Plans. Future creation uses the bundled constructors and the destination's
current catalogs. No reference Plan, source checkout or manual JSON repair is required.

## Resolve the model and destination first

If neither the current request nor unambiguous active conversation context identifies a semantic model, ask for its semantic model ID or URL. Never substitute a historical model or deploy the fixture model. Inspect the supplied model through its environment's authorized APIs. Default the new Plan to the workspace that hosts that model. Respect an explicitly requested target workspace. If the model's workspace cannot be resolved or cannot host the Plan, ask which accessible workspace the user wants; do not silently select another workspace. Model discovery, source/schema discovery and destination authorization remain separate checks.

## Connection selection is separate from physical SQL binding

The working FX-rates PowerTable uses a ShareableCloud connection whose `connectionDetails` is `{ "type":"FabricSql", "path":"FabricSql" }`, with OAuth2 credentials. This generic connection has no server/database path. It can be selected for a separately resolved Fabric SQL database; do not reject it merely because its connection name/path does not contain that database.

The PowerTable source independently carries `connectionId`, hostname-only `dbHost`, exact `dbName`, `schemaName`, `tableName` and `sqlTargetArtifact` (workspace, artifact ID and `SQLDbNative`). The observed source's `creationMode:3` means imported file. It is provenance, not a requirement to bind another existing table: use mode 2 for existing tables, as in `powertable_factory.existing_source`. Do not change mode to 3 to work around an OAuth failure or copy the reference database/table.

Live checks established: connection GET succeeded and reported Owner/OAuth2; the existing reference PowerTable's table-schema read succeeded with its resolved `x-target-visual`. New source initialization in the target still returned HTTP 400 / `PT_WB_9013`, with the workload credential lookup reporting connection-not-found/404. This does not establish that the connection was deleted, that OAuth2 is unsupported, or that changing its path/mode will help. Preserve SQL data, isolate the maintenance module, retain evidence and continue independent work. Connection creation and downstream credential resolution have separate acceptance gates. Do not keep creating duplicate connections in response to the same failure.

Public connection contract: [Get Connection](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/get-connection), [Create Connection](https://learn.microsoft.com/en-us/rest/api/fabric/core/connections/create-connection). Use the current environment's actual API base and supported credential contract.

## Side-panel filters and external Context

Page `filterPanePosition` is uppercase `RIGHT` in the verified contract; `controlPanePosition` is separately lowercase `right`. Do not reuse a lower-case enum across these two properties. `topPositionFilterExpandConfig.isFilterPaneCollapsed` controls initial collapse. Workload `workloadModeConfig` separately controls whether the filter pane is available in EDIT/READ.

Each ordinary Planning grouping field needs a complete `superFilterAssignments` registration: exact pivot assignment and bucket, unique filter identity, `position:RIGHT`, `filterLevel:visual`, configuration, and typed selection array. `filters.ensure_axis_filters` constructs missing semantic Rows/Columns filters without changing existing selections or Context. An empty filter array means all members; it is not a missing filter registration. The Planning constructor calls this automatically.

Intelligence charts additionally require a visible ordinary filter for **every assigned dimension and measure**, including KPI measures and comparisons. Planning-axis registration alone does not cover them. Use `chart_filters.ensure_chart_filters` and `audit_chart_filters`; read [chart-visual-filters.md](chart-visual-filters.md) for complete role, grouping-grain and nested identity rules. Hidden `embeddedSuperFilter` scope does not satisfy this requirement.

External Context remains distinct: `isContextDimension:true`, Category assignment, full mirrored embedded registration, filterContextStatus and bound input records. Keep it off Rows/Columns and preserve service-owned context hashes. Dashboard slicers are ordinary filters. Do not relabel Context as a slicer or unlock a version unless downstream calculations are valid for that version.

## Query identity domains

Never use a Planning input-record primary key as an InfoBridge output column ID. Keep these separate:

| Domain | Use |
|---|---|
| Query `id` (opaque Q-prefixed identity in this profile) | Native query metadata and transformation routes; portable query registry |
| Query `sqlPk` | Numeric prefix in the observed native field-catalog keys and native `queryId` assignments |
| Source ID | Source registry ownership; not the query ID |
| Planning input-record `id` | Persisted input/formula record row; not the output identity |
| Source measure `measureGuid` / query selected-field `id` | Stable output column identity, kept as a string |
| Consumer `measureGuid` | Native hash of the qualified field/aggregation for a newly constructed consumer |

Example with synthetic IDs: input record `id:"11", measureGuid:"18446744073709551614"` can yield query output `7[18446744073709551614]`, not `7[11]`. Column names alone cannot resolve identity. Generated transformation fields can have nonnumeric IDs; do not force every output suffix into u64.

Read the external adapter's query metadata, source inventory and ordered
transformations. Use final `selectedDimensions`, `selectedColumns`, and
`selectedMeasures` where present; preserve explicit empty selections. A query
error or null output means configuration evidence only, not successful
materialization.

`runtime/consumer_bindings.py` supplies `output_catalog`, `resolve_assignment` and `assert_resolved`. Match the intended query first, then its proven output ID, then assert name/type/aggregation consistency. Do not accept a matching label, an ordinal, or an ID copied from another Plan. Resolve portable-to-native prefixes after import. Numeric query prefixes are not automatically valid in GUID-based metadata routes.

For new query measures, the native internal identity is XXH3 of `SUM__<native-qualified-field>` (or the explicitly selected aggregation); semantic measures use their own contract. The reference's stored measureGuid matched the native qualified key, not its portable GUID spelling. Use the bundled lossless identity implementation. Before provision of dependent Planning formulas, resolve the runtime external-key map and register companions consistently.

For an existing Planning owner, its measureGuid can be referenced by input defaults, formulas, formatting and hierarchy state. A binding repair must not casually renumber it. Preserve the existing internal alias while repairing the external field reference when the owner supports that alias, or perform an explicit supported dependency migration across all records before changing it. Preserve all planner inputs. A native save is not calculation proof. Standalone KPI cards can use canonical hashes without changing Planning inputs.

## Reconcile identities after every ALM import

A same-item update can rewrite unchanged InfoBridge output suffixes to Planning
input-row IDs. This can also affect nested chart filter assignments and sort
keys. Byte-preserving publication and a matching chart/filter pair alone do not
prove that the IDs resolve.

Retain the current deployment's intended native properties before publication, then fetch fresh native pages and query metadata after it. `audit_visual_consumers(properties, queriesByNativeSqlPk)` checks every top-level and ordinary-filter InfoBridge assignment against the current output catalog, then audits chart filter coverage. Preserve existing Planning `measureGuid` aliases. Metadata with failed/pending query status remains configuration evidence only.

For the same-item identity regression, call `restore_import_bindings(current, intended, queriesByNativeSqlPk)`. It automatically repairs only external assignment `id`/`sourceId` and corresponding ordinary-filter sort identities after proving the intended fields in the current catalog. It rejects unrelated edits, membership changes and unproven intent. This is a scoped repair using this deployment's construction intent, not a dependency on an old report. If a different property changed, reconcile that feature from a fresh read instead of overwriting concurrent work or stopping other independent modules.

Save returned properties through the native batch writer with the freshly read visual ETags; repair the Planning owner, not each embedded copy. Re-read the owner and embeds, audit again, and export a new final definition. Do not re-import the stale envelope after repairing: it can repeat the remapping. Preserve source input/formula records, selections, Context, formatting and layout. A repeated identity regression belongs in the deployment runner, not in a manual JSON instruction for the user.

The live recovery restored five directly owned visuals and their embedded reflection, with all thirteen original pages/visuals matching their pre-publication native properties and all twenty-two chart filter registrations retained. This proves persistence and catalog identity, not rendering or financial propagation.

## Complete KPI store construction

Use `intelligence.card` / `complete_card_state`, not a partial KPI object. Set outer `properties.chartType:"CARD"`, `visualState.chartType:"CARD"` and JSON-string `hiddenProperties_!!!_chartsMode` consistently. Outer mode omission can leave a visual presenting as the default bar/column chart.

The fixture `fixtures/card-defaults.json` includes complete identity-free active KPI controls and number-format defaults derived from the inspected branch. The theme update reads `variance.style.color` even when variance is disabled. Keep title prefix/suffix, total style/value, variance icon/colors/style/border/accent settings, tooltip, image defaults, group containers, and default flags. Replacing a slice with `{variance:{showVariance:false}}` loses required members. The factory fills defaults while retaining intended labels, fonts, display options and layout. Dynamic Title/Value tokens display the assigned measure; never insert financial totals as literal text.

Do not copy fieldsMeta, historical measure keys, cached chart data, success flags or entire reference store bags. For presentational repair, use a fresh native page, preserve current visual identity and complete unrelated settings, save through the batch writer with ETags, and read back exact properties. Existing page-local embed rectangles must remain unchanged.

## Acceptance

1. Verify model/workspace resolution and connection/source identity separately.
2. Verify uppercase page filter position, ordinary registrations, existing selections and separate Context/input binding.
3. Verify every query-bound card against the intended query's final selected-field catalog; preserve a pending/failed query status as such.
4. Verify complete CARD mode and KPI slices; ordinary semantic cards need the same presentation contract.
5. Compare before/after source input/formula records, embedded rectangles, entity membership and unrelated properties.
6. Export after native repairs; confirm portable mappings and stable field suffixes. Do not import a stale pre-repair definition over the native fixes.
7. API persistence, catalog identity, renderer behavior and data propagation are separate outcomes. When UI is prohibited, report rendered behavior as not tested. Honor a user waiver of financial propagation testing without calling it passed.
