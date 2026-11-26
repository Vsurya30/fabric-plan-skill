# Plan definition part layout

Use this guide to check which parts a PlanV1 definition carries, what each root
part must contain, and how identities line up across parts. It restates the
public Plan definition article and the published part schemas. Where those
sources disagree with each other or with service exports, the difference is
named, so a candidate is not "fixed" toward the wrong source.

## Contents

- [Envelope](#envelope)
- [Part inventory](#part-inventory)
- [Identity rules](#identity-rules)
- [Root contract](#root-contract)
- [Plan, sheet and comment settings](#plan-sheet-and-comment-settings)
- [Data-input columns](#data-input-columns)
- [Where the sources disagree](#where-the-sources-disagree)
- [How Fabric's import treats parts](#how-fabrics-import-treats-parts)
- [Primary sources](#primary-sources)

## Envelope

A definition is an object with a `parts` array and an optional `format`.
`PlanV1` is the only documented format, and the REST contract requires only
`parts`. Every part has a `path`, `payloadType: "InlineBase64"` and a Base64
`payload` holding UTF-8 JSON.

Part paths are relative POSIX paths. The bundled codec refuses absolute paths,
`..`, backslashes, colons, non-canonical forms such as `a//b` or `./a`, and two
paths that differ only by letter case, because none of these maps to exactly one
file on every platform. A malformed part, such as one that is not an object or
has no string `path`, is a validation error before anything is decoded.

## Part inventory

Top level:

| Path | Article status | Holds |
|---|---|---|
| `definition.json` | Required | Semantic-model reference and the sheet registry |
| `planProperties.json` | Required | Plan-wide UI and behavior settings: theme, workload mode panes, filter assignments |
| `.platform` | Listed as required; returned by exports | Fabric Git metadata: item type, display name, logical ID |
| `connectedPlanning/infobridge.json` | When Connected Planning is used | Sources, query pipeline and writeback destinations |
| `cube/cube.json` | When cube-based writeback is used | Cube partitions, measures and input-column mappings |

The bundled builder does not author `.platform`. In an update of an exported
Plan, keep the exported `.platform` part unchanged: its metadata is applied only
through a generic item operation that this package does not run.

Per sheet, under `sheets/{sheetId}/`:

| Part | Article status | Holds |
|---|---|---|
| `sheet.json` | Required | Canvas, filter pane position, commentary and visual groups |
| `commentSettings.json` | Required for `PLANNING` and `POWERTABLE` sheets | Comment panel, notification and indicator settings |

Per visual, under `sheets/{sheetId}/visuals/{visualId}/`:

| Visual | Required parts | Optional parts |
|---|---|---|
| Planning | `dataInput.json`, `properties.json` | `writeback.json`, `insertRows.json`, `scenarios.json`, `modelTemplate.json` |
| PowerTable | `columnConfigs.json`, `properties.json`, `source.json`, `sourceSettings.json` | `approvals.json`, `automations.json`, `forms.json` |
| Intelligence | `properties.json` | None |

The three `properties.json` variants share a file name, not a shape. Never move
one shape into another visual type.

## Identity rules

1. A sheet reference's `recordGuid` in `definition.json` is its `{sheetId}`
   folder name.
2. Each `workloadItemEntityVisuals[].visualId` is the `{visualId}` folder name.
3. Each `dataInput.json` column's `visualId` is the visual that holds it.
4. Authored input and formula columns use one value for `measureGuid` and
   `columnMeta.id`; the bundled builder writes them identically.
5. Column IDs are unique within a visual, and a deleted ID is never reused.

A definition with a broken cross-reference can import and still fail to render.
Check these rules on the candidate before an update, not on the readback after.

## Root contract

`definition.json` requires `$schema`, `workloadItemName`,
`semanticModelReference` and `sheets`. Each sheet reference requires
`recordGuid`, `displayName` and `sheetType`; `isHidden`, `order` and
`workloadItemEntityVisuals` (visual type, visual ID and embedded flag) are
optional.

Documented sheet types are `PLANNING`, `REPORTING`, `POWERTABLE`, `INFOBRIDGE`,
`SUPER_FILTER`, `BI_REPORTING`, `BI_ADHOC_ANALYSIS` and `BI_DASHBOARD`.
Intelligence is a properties-schema family, not a sheet type; do not invent one.

`semanticModelReference` takes one of two forms. The portable form has
`connection` and `semanticModel`. The legacy form has all of `connectionId`,
`semanticModelId`, `semanticModelName`, `semanticModelWorkspaceId`,
`semanticModelWorkspaceName`, `directLakeMode`, `directQueryMode` and
`sourceType` (`POWERTABLE`, `INFOBRIDGE` or `WORKLOAD`). Keep the form an export
already uses.

In the portable form, a connection is either an inline reference with
`connectionId` or a variable-library reference; an item is either an inline
reference with `workspaceId` and `itemId` or a variable-library reference. A
variable-library reference is a string of the form `$(...)`, not an object. The
shared schema checks only that pattern. Fabric's semantic validation resolves
its contents, so confirm the library and variable exist, and resolve real target
IDs when moving a definition between workspaces.

## Plan, sheet and comment settings

`planProperties.json` requires `$schema` and `properties`, and `properties`
requires `workloadModeConfig` with `EDIT` and `READ` objects. `EDIT` holds the
filter, data, fields, elements, bookmarks, personalize, comments and variables
pane booleans. `READ` holds the filter, data, bookmarks, personalize, variables
and comments pane booleans. Theme, data streaming, workload filters and
variables, and page grouping (`pageGroupMapping` with `pageGroups`) are
optional. The published structure manifest notes that exports carry extra
fields and value shapes that the public schema does not allow; preserve them.

`sheet.json` requires `$schema` and `properties`, which hold page filters,
entity variables, filter and control pane positions, commentary, canvas style,
column assignment and visual group maps, and source visual metadata. The
structure manifest notes that exports omit some notes members that the public
schema requires and add fields it does not define. Preserve notes, annotations,
canvas dimensions, background, border and shadow, and the existing visual
grouping.

`commentSettings.json` requires `$schema`, its own `recordGuid`,
`allowComment`, `enableCommentsColumn` and `notification`. Indicator, status,
roll-up and panel options are optional.

## Data-input columns

`dataInput.json` requires `$schema` and a `columns` array. Each column requires
`measureGuid`, `visualId`, `columnMeta`, `name` and `dataInputType`.
`columnMeta` requires `id`, `label`, `measure_type` and `data_type`.

`measure_type` holds exactly one of these keys:

| Key | Requires |
|---|---|
| `Native` | `measure_role` |
| `DataInput` | `id`, `column_type`, `title` |
| `VisualColumn` | Wraps an input, such as `DataInput` |
| `Formula` | `formula` |
| `Forecast` | `forecast_version`, `forecast_period` |

`dataInputType` is a separate numeric code, independent of `measure_type`. Use
the documented value, never `0` or an inferred ordinal:

| Codes | Input types |
|---|---|
| 1 to 5 | `TEXT`, `SINGLE_SELECT`, `MULTI_SELECT`, `DATE_TIME`, `COMMENTS` |
| 6 to 10 | `NUMBER`, `PERSON`, `TIME`, `LAST_UPDATED_BY`, `LAST_UPDATED_AT` |
| 11 to 15 | `CHECKBOX`, `DATETIME`, `DECIMAL`, `IMAGE`, `URL` |
| 16 to 20 | `EMAIL`, `FORMULA`, `BUTTON_COLUMN`, `CURRENCY`, `PHONE_NUMBER` |
| 21 to 25 | `RATING`, `ATTACHMENT`, `PERCENT_SLIDER`, `PERCENT`, `SIMULATION` |
| 101 | `LONG_TEXT` |

Codes run in order within each row; for example `NUMBER` is 6 and `CHECKBOX` is 11.
Keep optional input permissions, on-change formulas, forecast open and closed
periods, edit settings and write-access flags when they are present.

## Where the sources disagree

| Topic | Article | Published schema or export evidence | Rule here |
|---|---|---|---|
| Definition `format` | Shown as `PlanV1` | REST contract requires only `parts` | Optional; never invent another value |
| `.platform` | Listed as required | Builder output omits it; exports return it | Keep the exported part unchanged |
| Planning `properties.json` | A `visuals` object keyed by visual ID | Schema requires only `$schema` and also defines a `properties` object; the structure manifest says exported files match neither, and the builder writes `properties` with `visualState` | Preserve the exported shape |
| DataInput `$schema` | Lower-case `planning/dataInput` | Schema constant uses `Planning/DataInput` | Use the selected schema's exact value for new parts; keep an export's value |
| Forecast period | Described as a start and end | Schema requires date-time strings `start` and `end`, with optional integer `start_utc` and `end_utc` | Keep exported values; record the difference instead of converting |
| `columnMeta.data_type` | `Number` or `Text` | Schema also allows `DateTime` and `Date` | Accept all four |

A schema-conforming definition is not proof of service acceptance, rendering or
runtime behavior.

## How Fabric's import treats parts

These behaviors come from Fabric's current import and export, not from the
article or the schemas. A Plan stored in Fabric SQL and a Plan whose entities
moved to OneLake take different import paths, and the definition doesn't say
which one applies, so plan for both.

- `$schema` is never checked. The import drops it, so its casing doesn't matter.
- IDs stay strings: inserted-row, scenario and template IDs above 2^63 are safe.
- An update replaces by omission. A missing `forms.json`, `automations.json` or
  `approvals.json` deletes every record of that kind. A sheet missing from
  `definition.json` is deleted. An empty list behaves differently on each path:
  - On Fabric SQL, empty `columnConfigs`, `forms` and `automations` lists are
    skipped, and an empty inserted-row list deletes every inserted row.
  - On OneLake, the same empty lists delete everything, and an empty inserted-row
    list is skipped.
  - Approval levels and filters are replaced by what the part lists. On OneLake,
    an approval record without both lists fails the import, so always write both,
    as the constructor does.
  - InfoBridge import deletes unlisted sources.
- Each InfoBridge source needs `sourceGuid` and `queries`.
- The semantic model binding is read from `semanticModelId` or
  `semanticModelVariable` with `sourceType`; a portable
  `semanticModelReference` isn't read.
- Where Fabric's event-trigger import is switched on, Planning
  `properties.json` can carry `eventTriggers`. When present, even as an empty
  list, they replace every existing trigger, so keep the exported list.
- On OneLake, data-input columns are matched by `columnMeta.id`; a column without
  one is skipped. OneLake export also rewrites `sqlPk` measure references to
  `measureGuid`.
- Cube mapping records resolve `cubePartition_RefId` and
  `cubePartitionMeasure_RefId` within `cube/cube.json`. `visual_RefId` resolves
  against the visuals in the same definition, and unresolved records are skipped.
- `scenarios.json` is neither imported nor exported today.

Start every update from a fresh export, and confirm the result in the product.

## Primary sources

- Plan definition article:
  https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/definitions/plan-definition
- Published Plan part schemas:
  https://github.com/microsoft/json-schemas/tree/main/fabric/item/plan/definition
- Shared reference schemas:
  https://github.com/microsoft/json-schemas/tree/main/fabric/common
- Fabric platform metadata:
  https://learn.microsoft.com/en-us/fabric/cicd/git-integration/source-code-format
