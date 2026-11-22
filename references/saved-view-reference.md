# Saved views, parameters, Home and PowerTable inspection

Use this guide when a user supplies a working Plan as evidence for bookmarks,
navigators, shared Planning embeds, parameters or an existing SQL PowerTable.
Discover **SAVED-VIEW-REFERENCE**. A reference is evidence for a contract; it is
not a template to clone or a source of IDs for another application.

## Read the complete current configuration

1. Export the current Plan using the bundled `api export` and finish its operation.
   Decode the returned parts. If the user edits the reference during inspection,
   export again after that change; retain the captures separately.
2. Resolve native entities and page properties using the selected metadata
   profile. Use actual visual IDs, not membership/association IDs. An embedded
   Planning visual retains its real owner's identity and inputs.
3. Read each public bookmark by its actual slug with `builder-api bookmark-read`.
   Native snapshots and portable export snapshots are different representations.
4. Read Home role metadata and then the relevant role content with
   `builder-api home-role`. Empty exported `homeLayout.roles` and an omitted
   `show` property do not prove Home is absent or disabled. V2 content lives in
   the role-layout provider. The effective-user endpoint may be unavailable while
   the role-content endpoint works; preserve that distinction and role permissions.
5. For PowerTable, use the native visual's `dataSourceId` to read details and
   schema. `builder-api powertable-schema` now reads both independently and returns
   `readStatus`, `errors`, and `status: complete | partial | failed`. A details
   failure does not discard a successful schema response. Authentication failures
   still stop the call. Inspect each status before consuming that component.
   This behavior does not certify source connection health or row saves.

`python plan.py inspect-reference-views --input inspection.json --out audit.json`
accepts `{"raw": <decoded parts>, "home_roles": <optional role metadata>,
"home_contents": {"<role ID>": <optional role content response>}}`.
It resolves owner/embed membership, bookmark page/visual references, navigator
kinds, current page parameters, exported PowerTable configuration and separately
read Home content. It flags parameters missing from bookmark snapshots. It does
not apply a bookmark, open a dashboard, refresh queries or write any business data.

## Confirmed OneLake reference profile

The 2026-11-17 read-only reference contains two Planning owners, one Intelligence
dashboard with both owners embedded, a Page Navigator and Bookmark Navigator,
one number parameter, three public bookmarks, and an existing SQL PowerTable.
The accompanying evidence records hashes and checks without bundling a customer's
whole report or requiring that report for future builds.

- Public bookmarks contain `cloudMeta.bookmarkMeta` and `bookmarkVisualMeta` in
  the export. Native GET returns those objects directly, plus an ETag. Native
  page/visual references are runtime IDs; export references are record GUIDs.
- Native Planning `manage_measures` snapshot entries retain IDs. The exporter
  converts these entries to labels/order/visibility. Do not feed that label-only
  export fragment directly to the native bookmark upsert or guess IDs by position.
  `reference_views.audit_native_capture(capture, current_page)` detects this error.
- Each captured bookmark keeps the Intelligence page as `activePageId`, with
  `includeCurrentPage`, `includeData` and `includeDisplay` true. Its four snapshots
  include the two Planning owners, a navigator and a slicer. A subsequently added
  navigator is not in those captures. Names/order are independent of array order.
- The current page contains a number parameter, while all three bookmark
  `entityLevelVariables` arrays are empty. Therefore this reference proves page
  parameter storage, not capture/restore of that later parameter. Capture the
  intended context explicitly; do not silently claim every current control is saved.
- The snapshots have no populated named-pivot state. They do not close the separate
  contract for generating arbitrary full-detail/region/specialist pivot snapshots.
  Existing complete native captures can be persisted using the existing ETag-safe
  upsert. Creating new restorable snapshots and validating apply/restore still
  need their documented contracts and runtime checks. Keep an agreed deferral
  until that requirement is actually implemented; navigator tabs are not a substitute.

## Number parameter construction

`python plan.py construct-native number-parameter --input number.json --out bundle.json`
uses `runtime.page_parameters.number_parameter`:

```json
{"label":"Planning assumption","technical_name":"planning_assumption","value":4}
```

The output contains `entityVariable`, `visualGlobalVariable` and
`calculatedVariable`, all with one new `CALC_VARIABLE_...` ID. The page variable
belongs in `sheet.json.properties.entityLevelVariables`; the corresponding
selected Planning owner mirrors belong in `visualState.globalVariables` and
`visualState.calculatedVariables[id]`. These are separate stores; don't replace
unrelated parameters or duplicate the input visual. Resolve the consumers and
page scope intentionally, especially when one Planning owner is embedded on more
than one dashboard. A parameter creates neither an input permission nor a formula
dependency automatically. Use the existing native property-save phase with fresh
identities/ETags, then verify the three stores. `allow_decimal` and `visible` are
optional booleans; the supported profile is an ordinary number input-box with no
percentage display or slider. Dates keep their separate existing constructor.
The supplied value is literal; 4 remains 4. Do not invent a `/100` dependency
unless the requested formula uses whole percentage points.

## PowerTable identity and source boundaries

The reference uses existing-table creation mode 2, Fabric SQL artifact type
`SQLDbNative`, and an authenticated FabricSql connection. Its seven-column table
has a noneditable identity primary key, key-preserving lookup columns and date/bit
columns. Row add/update are enabled and delete is disabled in saved settings;
this is saved configuration, not verification of a successful SQL row write.

Portable `source.json.source.recordGuid`, native visual `dataSourceId`, visual ID,
and page membership ID are different identities. Preserve runtime source IDs as
opaque strings, including the observed nonnumeric compact identifier. Resolve
new source IDs from the current application; don't reuse the reference's source.
Discover the actual target table schema/keys and configure through the bundled
PowerTable constructors. Don't import the reference's other table, rows, database,
lookups or permission settings as an automatic replacement.

The reference's schema read succeeded while its details read returned HTTP 400.
The same connection ID did not, by itself, resolve the existing Budget target's
source-creation error. Treat read/schema, source registration, connection resolution
and physical writeback as separate results. Don't request an unrelated SQL token,
change database schema, recreate the Plan, or replay the same failed mutation
merely because one reader failed. Preserve the current artifact and precise gap.

All existing defaults remain: Arial, populated enabled Home, a visible Page
Navigator with complete padding on every dashboard, hidden Planning owners,
shared embeds, complete inputs/formulas/CF imports, correct OneLake query identity,
and optional initial InfoBridge refresh. The reference's own colors/fonts and
visible source sheets do not override those requested application defaults.
