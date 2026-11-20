> Standalone edition: read [runtime-guide.md](runtime-guide.md) for construction and deployment. Source checkout and historical task links below are optional provenance, not runtime prerequisites. Original feature explanations are preserved; the API-only runtime guide and gap inventory distinguish implemented APIs from blocked contracts. Historical UI steps are not execution instructions.

# Verified Contract Addendum

This supplements the [existing internal reference](feature-contracts.md), not a new skill package. Applies to Matrix `5b9ffe2d1`, Charts `8c9db2ac`, Shell `3c5d78fb3`, backend `00fe77986e`. Every addition below is **partial**: source inspection is not an executed serializer, import, export, or runtime test. The reports are untrusted observations, never specification authorities.

## A01 Export and Import Envelopes

Part paths below mean `sheets/{sheetRecordGuid}/visuals/{visualRecordGuid}/<filename>`, not paths inside the decoded report map. JSON Pointers in this table are relative to the definition part.

| Family | Actual current exporter shape | Import reader / consequence |
| --- | --- | --- |
| Planning properties | `$schema` plus transformed properties payload. The inspected samples use `/properties`; do not manufacture `/visuals/{id}`. | Reads whole properties file, extracts event triggers, normalizes schemas, restores selected target state, reverses rewires, resolves visual GUIDs, then uploads. |
| Planning inputs | `/columns` array, emitted only when columns exist; source numeric `sqlPk` removed in V2. | V2 uses columns only if an array, otherwise empty. This fallback is not permission to construct incomplete records. |
| Planning rows | `/rows` array, emitted only when rows exist. | V2 uses rows only if an array; row-reference/import dependencies remain feature-specific. |
| Planning writeback | Settings at root, optional nonempty `/destinations` in inspected V2 emitter. | Settings and destinations imported separately; a public required field and code omission remain distinct claims. |
| PowerTable source | `{"$schema":...,"source":...}`; `/source` object. | Reader uses `fileData.source ?? fileData`. Actual source members are not the public flat `connection`/`database` example. |
| PowerTable configs | `{"$schema":...,"columnConfigs":[...]}`; `/columnConfigs` array. | Reader uses `fileData.columnConfigs ?? fileData`. Reconciles by normalized record GUID and deletes existing configs missing from incoming GUIDs. **Collection replacement/reconciliation, not a partial column patch.** |
| PowerTable settings | `{"$schema":...,"sourceSettings":[...]}`; `/sourceSettings` array. | Reader uses `fileData.sourceSettings ?? fileData`; row filters and source-settings references require mapping. |
| PowerTable properties | `{"$schema":...,"properties":...}`. | Different family/handler from Planning even with the same filename. |
| PowerTable optional branches | `/approvals` object, `/forms` array, `/automations` array, in their own files. | Not observed in these reports; their internal DTOs, prerequisites and import behavior are unresolved here, not unsupported. |

Evidence: Planning emitter, Planning importer, PowerTable emitter including absent optional variants, PowerTable source/config importer, settings reader.

Actual V2 import helpers set root internal `schema` to `0.0.1` if falsy and remove truthy `$schema`. The restoration body overwrites imported `properties.visualState.notes`, `cell_lock`, and `auditLog` only when those target values are defined and both visual-state objects exist. Do not equate this with the export cleanup's `lock_state` or assume all incoming notes win. Reverse rewiring operates through registered top-level `properties[handler.property]`, with visual mapping supplied and workload/entity maps empty; all nested handlers and reference domains are not closed by that loop alone.

The source object is constructed with `connectionId`, `dbName`, `dbHost`, `tableName`, `schemaName`, `connectionIdVariable`, `databaseVariable`, `recordGuid`, `tableType`, timestamp-sanitized `meta`, `creationMode`, `sqlTargetArtifact`, `fileImportType`. These are **exported member names**, not a required-field schema: JavaScript undefined omission and each domain's validation remain relevant. No fake connections, host names, target users, lookup tables, or record IDs are provided.

Version rule: migration state selects SQL versus OneLake, independently of schema version `1.0.0`. Neither file naming nor a schema URL identifies the source route. Preserve incompatible representations and resolve the target migration state before generation. Broad passthrough of a generic `visualState` does not prove meaningful support for all its leaves.

## A02 Charts Number Formatting and Encoded State

This is **not** Matrix F03 Quick Format. Native Charts binding is `hiddenProperties.numberFormatting`. ModulePropsBuilder passes the setting through getParsedJSON, which calls `JSON.parse`; errors return `{}`. On initial update, an empty decoded object may use the registered model default. This is a reader fallback, not an export requirement. Object-valued report variants must not be blindly converted to strings: the precise host adapter and version are still unresolved.

Observed location: `/properties/visualState/hiddenProperties_!!!_numberFormatting`, a JSON string in the sampled Charts instances. After decoding it, the paths below are relative to that string's JSON root. Native interface/reducers/default factory: numberFormatting.ts.

| Member family | Complete interface members in inspected file | Types / constraints |
| --- | --- | --- |
| Flags | `enabled`, `ibcsformat`, `showScalingUnit`, `semanticFormatting`, `showValueColor`, `includeBetweenSign`, `isIndividual`, `isCustomUnitLabel`, `showInPP`, `showInBPS`, `enforceSign`, `enableTextCategoryNF` | Boolean. `isIndividual` comment restricts intended use to multi-chart trellis; owning enforcement not closed. |
| Optional contextual flags | `isPercentageMeasure`, `isPPCalculationEnabled`, `isMeasureBreakdownVariance`, `nullSuppression` | Optional boolean; PBI-dependent, not unconditional saved defaults. |
| Precision | `noOfDecimal`, `noOfDecimalPercent` | Number in interface; defaults 1, 2. Bounds and integer validation not established. |
| Text | `thousandSeparator`, `decimalSeparator`, `prefix`, `suffix`, `positiveValueColor`, `positiveValueFormat`, `negativeValueColor`, `negativeValueFormat`, `showNullAs`, `showZeroAs` | String. Observed/default strings are not finite allowed enums. This spelling differs from Matrix `thousandSeperator`. |
| Scaling | `scalingFactor` | String or number, **not** an exhaustive `uniform/auto/percentage` enum. Factory/default use does not close accepted strings or numeric units. |
| Total mode | `kpiTotalType` | `native` or `custom`. |
| Scaling display | `displayScalingIn` | `title`, `breadcrumbs`, or `both`. |
| Table mode | `tableFormatType` | `uniform`, `default`, `auto`, `native`, or `none`. |
| Custom roles | `customFormat` | Map of role to `ICustomNumberFormat`; role domain requires imported measure-role definitions, not arbitrary synthetic roles. |
| Custom role member | `enabled`, `noOfDecimal`, `prefix`, `suffix`, `scalingFactor` | Boolean, number, string, string, string-or-number respectively. |
| Unit text | `shortUnitText`, `longUnitText` | Each has string `thousands`, `billions`, `millions`, `trillions`; optional string `percentagePoints`, `basisPoints`. |

Theme-dependent defaults: separator depends on requested `theme`, but several computed defaults and colors use `DEFAULT_THEME`. Do not assume passing a different theme parameter recalculates every default. The factory uses a measure-role list to initialize custom formats; roles ending in `%` get `percentage`, others `auto`. Unit strings and flags in the factory are initial UI values, not schema materialization rules.

Updates: `updateFormatSync` shallow-merges; `updateCustomFormatSync` clones and merges one role's format; `resetNumberFormatSync` replaces; `updateIbcsFormatSync` can force `uniform`; the CARD chart-mode subscription selectively resets precision/scaling/prefix/suffix only for `isFromKpiSettings`. Effects clear KPI width caches and trigger resize. All reducer branches in this file were read, including the branch absent from the sampled configurations.

Synthetic **native subtree only**, at `customFormat[resolvedRole]`, not a whole setting or deployable part:

```json
{"enabled":true,"noOfDecimal":2,"prefix":"","suffix":"","scalingFactor":"auto"}
```

Validation: JSON syntax only; `auto` is evidenced factory use, not a finite scaling enum claim. No formula evaluation, rendered result, or import preservation was executed.

Known structural variations: sampled Charts state contains both JSON-string and object forms under other `hiddenProperties_!!!_*` keys and a second JSON-string layer below `secondaryVisualsState.textMode.text`. The inventory records both forms and each decoding boundary without unifying them. Rich-text nodes, chart types, axis/trellis/gantt families, migration, host-state producer, and full leaf semantics remain unresolved. Do not equate these with the Matrix plain `numberFormatting` object.

## A03 Native Measure and Input Unions

Complete enum **discriminants**, not complete leaf closure, from calculated_measure_impl.rs:

| Native enum | All variants / nested rule |
| --- | --- |
| `MeasureType` | `Native`, `Formula`, `DataInput`, `Forecast`, `VisualColumn`, `AutoVariance`. These payload variants use default serde externally tagged objects, not a simultaneous-fields object. |
| `VisualColumnConfig` | `Formula` or `DataInput`, nested beneath `VisualColumn`. |
| `VarianceType` | `Absolute(string)` or `Relative(string)`, beneath AutoVariance `variance_type`; formula is a defaulted string. |
| `MeasureRole` | Unit strings `Measure`, `ACMeasure`, `PYMeasure`, `PLMeasure`, `FCMeasure`, `AnnotationMeasure`, `OtherMeasure`; `ExtraMeasure(string)` is a tagged payload variant. |
| `CustomColumnType` | `Number`, `ShortText`, `LongText`, `SingleSelect`, `MultiSelect`, `Date`, `Person`, `Checkbox`, `Simulation`. All carry distinct metadata. |
| `AllowInputType` | Unit strings `Edit`, `ReadAndEdit`, or object `{"BasedOnFormula":string}`. Omitted native field defaults to `Edit`; explicit null is not established as accepted by this non-Option enum. |

This corrects a five-measure-type assumption from the public prose; `AutoVariance` is code-supported but not listed there. It does not certify ALM support for AutoVariance. Numeric backend `dataInputType` values belong to a different enum layer and must not be substituted for these native discriminants.

DataInputConfig has string `id` and `title`, `column_type`, optional `cube_partition_measure_id`, optional `cube_model`, optional string `on_change_formula`, `allow_input`, optional `user_permission`, and boolean `bound_to_filter_context`. The redesigned dynamic branch uses `cube_model:"DYNAMIC"`; other strings do not establish a supported model. Critical serde rules:

The checked-in generated TypeScript/schema artifacts omit `cube_model` even
though the current Rust DataInput and Forecast structs, tests and runtime
classification support it. Treat the Rust saved record and current native
readback as authoritative for this field; do not infer that the generated
interface's omission makes a native record invalid.

- `disable_write_access` is defaulted and **skip_deserializing** in this struct; emitting it does not prove the hydrated value controls permission.
- `user_permission` is **skip_serializing**; `AccessControl` and `AccessingUser` use camelCase (`readWrite`, `graphId`, `entityType`). These are not a portable target-user recipe.
- `bound_to_filter_context` omission defaults true, distinct from a UI filter-context enable flag.
- Absent `cube_partition_measure_id` and `cube_model` are omitted on serialization. `on_change_formula` is Option and is not given the same omission rule here. ForecastConfig has the same current optional cube model/binding pair; FormulaConfig has only `cube_partition_measure_id`.
- Select migration moves nonempty legacy `options` into `options_source: Static(...)`. Preserve the source/target version boundary instead of emitting both as an invented superset.
- Number and Simulation do not use the same total-entry predicate as text/select/date/person; Checkbox uses `edit_on_total.unwrap_or(false)`. Simulation always represents a measure reference in the default-source reader.

Minimal synthetic **native Formula payload only**, beneath a resolved `measure_type.Formula` or `measure_type.VisualColumn.Formula`:

```json
{"formula":"1 + 1"}
```

Validation is syntax only. FormulaConfig defaults `formula` and omits absent `cube_partition_measure_id`; this example neither proves expression execution nor supplies required column/visual/metadata context. Metadata structs for all nine column kinds, Forecast period/configuration branches, dynamic row metadata, HTTP writers/validators, and every reference conversion are still open. No full input-column generation recipe is enabled by this addendum.

## A04 Public Contract Conflicts and Validation Boundaries

Public page re-read 2026-11-06, documentation revision `4fc644d095a0406fcc7bb563984edc028ec50675`: [Plan definition](https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/definitions/plan-definition). Inspecting schemas is distinct from executing a validator.

- The reachable lower-case [definition schema](https://developer.microsoft.com/json-schemas/fabric/item/plan/definition/definition/1.0.0/schema.json) declares upper-case `Definition` in `$id` and `$schema` const. URL reachability is not string-const equivalence.
- The reachable [Planning properties schema](https://developer.microsoft.com/json-schemas/fabric/item/plan/definition/planning/properties/1.0.0/schema.json) has root required list containing only `$schema`, accepts a direct open `properties` object, and also defines optional `visuals`. The prose calls `visuals` required. Both claims must remain version-bound and distinct.
- That schema defines SuperFilter `filter` as array and `position` as string enum, whereas prose tables describe object and integer. Configuration `scale`, `slider`, `regex`, `measureSearch`, `sort` also differ in shape from the prose. Do not use prose as a replacement for schema or the actual Shell writer.
- Lower-case `planning/dataInput/...` returned HTTP 404. The exporter constructs `Planning/DataInput/...`; universal casing equivalence was not established.
- Planning and PowerTable share filenames but not necessarily payload roots, native serializers, cleanup, references or import behavior. The PowerTable envelope findings in A01 are source-supported despite prose differences.

The exporter-cased [DataInput schema](https://developer.microsoft.com/json-schemas/fabric/item/plan/definition/Planning/DataInput/1.0.0/schema.json) is reachable. It excludes `AutoVariance`; its column-kind properties do not match all nine native kinds; its native input `allow_input` permits `ReadAndEdit`/`ReadOnly` strings, not native `Edit`/`BasedOnFormula`. It describes forecast period start/end as date-time strings, while the prose PeriodRange table says numbers. These are explicit schema/native/prose conflicts, not permission to blend formats. Published `DateTime` is not a tenth variant of the inspected native `CustomColumnType`.

No installed Python `jsonschema` was found, and none was installed. The installed PowerShell `Test-Json -FetchExternalReference` was used instead: **338 parts accepted, 202 not accepted, one model-template schema unavailable, three platform parts outside this Plan-only validator scope**. External references were fetched from the public schemas, not inferred from the reports. See the coverage report for per-family results. These are static schema results, not native support, import/export, rendering, authorization, or deployment validation. A source-open property bag is not positive coverage of each inventoried leaf. Unsupported and unresolved are different: no property is declared unsupported merely because it was not found or an example omitted it.

## A05 Native Input Metadata

All seven metadata definition files were read, including the kinds absent from the reports. Native insertion prefix is `measure_type.DataInput.column_type.<Kind>` or `measure_type.VisualColumn.DataInput.column_type.<Kind>`. This specifies native nesting only, not a closed exported-column recipe. Every field below has a source serde default unless stated otherwise; Option omission becomes None, not the inner enum's default. Native `Id` encoding/resolution, HTTP conversion, runtime validation callers, and ALM parity remain open.

| Kind / metadata owner | Complete metadata struct fields |
| --- | --- |
| Number | `min_value`, `max_value`, `default_value`: optional `NumberDefaultValue`; `distribute_parent_value_to_children`: bool. Optional values are tagged enum payloads or null, not an asserted raw-number schema. |
| ShortText / LongText | `default_value`: optional TextDefaultValue; `allow_entry_on_totals_or_subtotals`: bool; `prevent_null`: optional bool; `field_validation`: ValidationType; `minimum_length`, `maximum_length`: optional u32; `roll_up_delimiter`: optional TextRollupDelimiter, omitted on serialization when None. |
| SingleSelect / MultiSelect | `options`: SelectOption array; `options_source`: SelectOptionsSource; `option_style`: SelectOptionStyle; `advanced`: optional `{visual_identifier?: string|null, columns?: string|null}`; `default_value`: optional SelectDefaultValue; `allow_user_to_add_new_option`, `allow_entry_on_totals_or_subtotals`: bool; `prevent_null`: optional bool; `icon_position`: optional string. The bundled factory validates and preserves `advanced`. |
| Date | `format`: DateFormat; `min_date`, `max_date`: optional string; `allow_entry_on_totals_or_subtotals`: bool; `default_value`: optional DateDefaultValue. Strings alone do not prove accepted date formats/units. |
| Person | `allow_entry_on_totals_or_subtotals`: bool. No default_value member in this struct. |
| Checkbox | `default_value`: optional CheckboxDefaultValue; `edit_on_total`: optional bool. |
| Simulation | `source_measure_id`: Id; `simulation_slider`: bool; `simulation_range`: i32; `distribute_parent_value_to_children`: bool; `simulation_value_align`, `variance_formatting_style`: strings. Source measure must be resolved, not fabricated. |

Nested default-value unions use serde external tags:

| Type | All payload variants |
| --- | --- |
| NumberDefaultValue | `Static(f64)`, `Measure(Id)`. |
| TextDefaultValue | `Static(string)`, `Dimension(Id)`, `Measure(Id)`. |
| SelectDefaultValue | `Static(SelectOption)`, `Dimension(Id)`, `Measure(Id)`. |
| DateDefaultValue | `Static(string)`, `Dimension(string)`, `Measure(Id)`. |
| CheckboxDefaultValue | `Static(bool)`, `Dimension(Id)`, `Measure(Id)`. |

Full nested SelectOption has string `display_name`, `value`, `color`, `icon`, and i32 `order`, with **no serde field-default annotations**; deriving Rust Default does not make these optional in a supplied option record. AdvancedStyle has optional string `visual_identifier` and `columns`. SelectOptionStyle is `Chip`/`Arrow`/`PlainText`, default Chip. SelectOptionsSource is `Static(SelectOption[])` or unit `Lookup`, default empty Static. Do not confuse this persisted source with metadata-only `SelectOptionsSourceKind`, which is unit `Static` or `Lookup(map<string,string>)` and appears in SelectColumnMetadataKind.

Text validation enum: unit `AnyValue` (default), `Numeric`, `NonNumeric`, `AlphaNumeric`, `Email`, `Url`, or tagged `Custom(string)`. Rollup delimiter wire literals are **`,` and `|`** through explicit serde renames; display separators add spaces, so they are not the same stored string. DateFormat applies SCREAMING_SNAKE_CASE to these 13 Rust variants: `DefaultLocale`, `MonthDdYyyy`, `DdMonthYyyy`, `DdFullmonthYyyy`, `DdMmYyyySlash`, `DdMmYyyyHyphen`, `DdMmYySlash`, `DdMmYyHyphen`, `MmDdYyyySlash`, `MmDdYyyyHyphen`, `MmDdYySlash`, `MmDdYyHyphen`, `DdddMmmmDYyyy`. Default is DefaultLocale; date rendering/parse consumers are untraced.

The whole text validation implementation was read: `validate_short_text` uses configured `maximum_length` or 255; `validate_long_text` uses configured `maximum_length` or 25,000. The comparison uses Rust string `len()` (UTF-8 bytes), not a demonstrated Unicode-character count. That helper does not enforce minimum length or the field-validation enum; do not generalize its limited check into complete server validation.

Synthetic complete **NumberColumnMetadata subtree only**, no target references and no deployable column:

```json
{"min_value":null,"max_value":null,"distribute_parent_value_to_children":false,"default_value":{"Static":0}}
```

Validation: JSON syntax and source-declaration comparison only. No Rust serde execution or import test. This native tagged default is not interchangeable with every form accepted by the published number-column schema. Existing metadata must be preserved through verified writers; no migration is performed here.