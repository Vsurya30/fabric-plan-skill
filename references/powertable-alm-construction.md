# Complete PowerTable grid construction

Use `runtime.powertable_factory.configured_table` when the target SQL base table,
physical schema, authorized cloud connection and SQL artifact are resolved. It
returns a sheet declaration, all parts and a source identity manifest. Generate
column configurations with `runtime.table_columns.column_config` using actual
nullable/key/identity/type metadata and verified lookup targets.

## Lookup and source metadata baseline (v22)

Read [powertable-lookup-source-metadata.md](powertable-lookup-source-metadata.md).
Configured sources include destination connectionName, workspaceId, workspaceName,
databaseId and dbDisplayName under source.meta. Obtain labels from the current
connection/workspace/database records. Retain any existing totalRows metadata.
Database lookup display is independent of column editability and ROW_ADD. Preserve
read-only IDs and disabled inserts during scoped repairs. `column_config` accepts
`allow_edit=False` and ordered lookup chains. The bundled repair CLI preserves all
unrelated definition parts and does not deploy. Respect requested validation scope;
when validation is skipped, report save status separately from UI/runtime behavior.

## Required parts and bindings

For physical schema discovery using the existing Fabric authentication, read
[sql-definition-discovery.md](sql-definition-discovery.md). The SQL database
`getDefinition?format=sqlproj` route can provide current CREATE TABLE metadata
without a separate Azure SQL token; it is independent of PowerTable initialization.

- Root sheet: `sheetType:"POWERTABLE"`, visible, and one directly owned
  `workloadItemEntityVisuals` declaration with `visualType:"POWERTABLE"`.
- `sheets/{sheetGuid}/sheet.json` is the ordinary sheet companion.
- `visuals/{visualGuid}/properties.json` has the **double wrapper**:
  `{"properties":{"schema":"0.0.1","properties":{...}}}`. The inner properties
  use `visualType:30`; `visualState.columnMeta` and `manageMeasures` use the real
  physical column names. PowerTable's `manageMeasures` differs from Planning's
  `manage_measures`. Empty top-level pivot assignments are normal for PowerTable.
- `source.json` contains a new source `recordGuid`, actual `connectionId`,
  `dbHost`, `dbName`, `schemaName`, `tableName`, and `sqlTargetArtifact` with the
  actual artifact/workspace IDs and `artifactType:"SQLDbNative"`.
  `creationMode:2` selects an existing table. It is not permission to create SQL DDL.
- `columnConfigs.json` contains the complete column configuration array.
- `sourceSettings.json` has separate ROW_ADD/ROW_UPDATE/ROW_DELETE records whose
  `sourceId` is the new source GUID. The constructor defaults add/update enabled
  and delete disabled for an authorized maintenance request. These settings do not
  override backend permissions or prove row-save success.

Keep cloud connection ID, SQL artifact ID, source GUID, sheet/visual GUIDs and
native numeric source/visual IDs distinct. Obtain the latter from post-import
catalogs. Never copy `originEntityId`, source IDs or cached options from a template.
Generic presentation defaults are embedded in this skill; no reference report is
needed. Clear assignment maps, persisted pivot/filter state and options when
constructing a new source.

## Connection selection and readback

A FabricSql OAuth cloud connection may have a generic `connectionDetails.path`
of `FabricSql`, rather than a database-specific path. That is not a reason to reject
it: separately resolve the actual SQL artifact/host/database, validate access in
the workload and inspect the item's bound connections. The supplied Power BI token
authorizes control-plane operations; it is not itself a reusable SQL connection
credential. Do not create duplicate connections to work around an unproven error.

If direct source initialization returns PT_WB_9013 while
the complete ALM four-part source/grid construction subsequently created native
grids with SQL schemas accessible in their resolved visual context. Treat those as
different routes/evidence; do not conclude a listed connection was deleted.

After import, read the entity/page catalog and verify one owned type-30 visual with
non-null `dataSourceId`. In that actual visual context call
read the PowerTable table schema and compare columns, PKs,
identity and nullability against the intended configurations. A source-details GET
can fail while the table/schema succeeds; preserve both outcomes. An integer PK
without `isIdentity` must stay visible, mandatory and user-supplied on insert.
Lookup columns must map the stored FK to the correct unique remote key/display
label; do not turn every integer into an auto-generated or lookup column.

An accepted mutation is not enough. Verify bindings and native schema, and export
the saved definition. Check for InfoBridge ID remapping after ALM and apply the
bundled scoped consumer repair using this deployment's intent. Preserve unrelated
filters, Context, owners, formulas and geometry. Never re-import the stale envelope
over native fixes. Database row values remain untouched during configuration.
Before import, `validate_plan` also checks the four-part package's source GUID,
each source-setting reference, unique physical columns, visual column catalog and
managed-column order. This catches incoherent ALM companions without claiming
database access, rendered readiness or row-save behavior.

## Missing connection

Continue independent Plan creation and add the requested visible PowerTable
navigation sheets when the user accepts connection deferral. Explicitly classify
them `sheet-only-uninitialized`: their welcome screen is expected, not a configured
grid. Keep intended table/columns in the credential-free manifest. Do not invent a
connection/source GUID or claim an empty sheet is a complete PowerTable. On later
binding, initialize that existing sheet rather than adding a duplicate. See
`maintenance-deferred-connection.md` for the separate uninitialized-sheet contract.
