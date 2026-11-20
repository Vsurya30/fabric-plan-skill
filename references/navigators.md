> Standalone edition: read [runtime-guide.md](runtime-guide.md) for construction and deployment. Source checkout and historical task links below are optional provenance, not runtime prerequisites. Original feature explanations are preserved; the API-only runtime guide and gap inventory distinguish implemented APIs from blocked contracts. Historical UI steps are not execution instructions.

# Navigators - Agentic Artifact Specification

## Mandatory dashboard page navigation (v27)

Every newly authored Intelligence dashboard includes a visible native Page
Navigator, independently of business prompt, screenshot or reference content.
This is an explicit user-required application default alongside Arial, native
Home and rich Intelligence coverage for every Planning owner. A single button,
bookmark tabs, Home cards or the application Explorer does not satisfy it.

`runtime.intelligence.dashboard` constructs the control through
`runtime.intelligence.page_navigator` and `navigator_api.state`. The declaration
uses `BI_RUNTIME_INPUT`; its properties use numeric `visualType: 203` and
`visualState.navigatorState.type: PAGE_NAVIGATOR_TABS`. The shared factory supplies
complete DEFAULT shape/text/icon padding, including disabled icons, and Arial.
The default horizontal strip is 48 pixels tall and full canvas content width,
with a 16-pixel gap above the embedded Planning grid. The layout reserves this
space and grows the canvas; it never overlays an existing chart or grid.

For portable all-page navigation, omit `navigatorTabsState.selectedPages` and
use `destinationType: {all: true, hidden: false, tooltip: false}`. Omission lets
the renderer use the current eligible page catalog, including newly added pages;
an empty array hides all leaf tabs. Do not copy source runtime page IDs or
persist generated tabs. Horizontal layout derives its count from the live
catalog; rows/columns are only meaningful for manual grid layout.

Normal application delivery registers the control through the ALM declaration
and saves its full authored state with geometry in `intelligence_api.deploy_geometry`
using freshly resolved visual IDs/ETags, before exposing the staged dashboard.
No task-local repair or second create is required. The standalone
`navigator_api.create` remains a separate, host-dependent path; its product-203
endpoint is not assumed to work merely because ALM registration works.

`check-application-defaults` and `require_delivery_phases` require every declared
REPORTING page to own a visible native Page Navigator with the portable all-page
default and complete padding. Orphan properties, an embedded reference, hidden
layers, wrong kinds and restricted/empty selections do not pass. Geometry must
be in bounds and clear of other direct visuals; the normal geometry audit also
checks the page-local Planning embed. Scoped repairs preserve unrelated content
and do not authorize retroactive application-wide changes.

Evidence: the user confirmed the prior live Page Navigators are visible. This
release tests clean construction and the normal save adapter offline. It does
not claim every tab was clicked or a fresh application was deployed.

## Current construction contract (v26)

A disabled Navigator icon still requires a complete render configuration. The
observed dashboard white screen reported `Cannot read properties of undefined
(reading 'topPadding')`; the generated DEFAULT icon contained only `isEnabled`.
Complete icon defaults were saved and read back in the affected dashboards.
This package includes construction regressions; it does not claim a new UI test.

Use `runtime.navigator_api.state` (CLI `construct-native navigator`) for new
Intelligence navigators. Its bundled current fixture includes the complete icon
profile: `isEnabled`, color, weight, size, transparency, placement, horizontal and
vertical alignment, padding, `iconTypeMapping.default`, customIconScale,
iconRotation and gap. Both text and icon padding contain numeric top/bottom/left/
right padding plus boolean `isCustomPaddingSize` and `isEnabled`. Shape padding
is also complete. New text uses Arial. Do not substitute the abbreviated icon
object in older source-contract snippets for this current construction contract.

`runtime.navigator_defaults.complete_defaults(state)` fills only missing members
of DEFAULT text, icon and shape padding using bundled defaults. It returns a copy,
preserves existing values (including custom padding and disabled flags), and
rejects null objects or malformed padding. It keeps HOVER/PRESSED/ACTIVE as
partial overrides and checks their effective padding after inheritance. It does
not conflate legacy `radiusTopLeft` with current `topLeft` corner profiles, change
actions/targets/geometry, or rewrite any other report parts.

Both `navigator_api.state` and `construct.navigator` use the shared completion
helper. `navigator_api.create` also completes incoming render groups before any
network write. For ALM authoring, use the constructed result directly under
`properties.visualState.navigatorState`; the application-default gate calls
`require_complete_defaults` to catch incomplete hand-authored states before
application completion. These helpers are not a report-wide repair operation.

Run `python examples/navigator-defaults/build.py <output-directory>` for all three
native kinds from the package alone. Resolve real destination identities and use
the supported host-registration route before saving; state completeness does not
establish that a target supports a particular creation endpoint. A successful
save/readback and an actual rendered dashboard remain separate evidence.

## 1. Feature Overview

Navigators are native runtime-input visuals that execute button actions or generate page/bookmark navigation tabs. The native configuration is `visualState.navigatorState`, not the friendly AI schema's `button` object. The three verified kinds are `NAVIGATOR_BUTTON`, `BOOKMARK_TABS`, and `PAGE_NAVIGATOR_TABS`.

The feature scope includes action targets, four style states, tab layout, page/bookmark selection, collapsible tabs, hierarchical tabs, and shared shape styling. Application source code is not modified by this investigation.

Evidence: Navigator.types.ts, `INavigatorState`; navigatorAiSchemaCompiler.ts, `NAVIGATOR_FIELDS` and `readVisualState`.

### Representation Boundary

| Representation | Action property | Intended use |
| --- | --- | --- |
| Friendly AI schema | `button.action` | Input to `navigatorAiSchemaCompiler`; not a native artifact fragment |
| Native visual state | `visualState.navigatorState.navigatorButtonState.actionType` | Native configuration consumed by NavigatorButton |

Persisted artifact placement, transport encoding, and deployment requirements are investigated separately below; a native visual-state fragment alone is not a complete deployable artifact.

Investigation date: 2026-11-05. Authority: the product implementation. Coverage is comprehensive for the discovered native Navigator schema, but is not a certification of deployment portability or every renderer's geometry. Section 15 records unresolved boundaries. The required `graft map` command was unavailable and no stored graph directory existed; targeted source investigation was used.

## 2. Feature Architecture

| Component | Parent | Configuration | Inclusion and effect |
| --- | --- | --- | --- |
| NavigatorRenderer | Native visual host, visual type 203 | `N.type` | Button kind renders NavigatorButton; every other kind enters NavigatorTabs. Missing `navigatorState` renders nothing. Unknown kinds are not valid construction choices. |
| NavigatorButton | NavigatorRenderer | `N.navigatorButtonState` | Single generated runtime tab; handles nine action kinds. Its tab-layout configuration is internal, not taken from persisted tab layout. |
| NavigatorTabs | NavigatorRenderer | `N.navigatorTabsState` | Generates page/bookmark tabs, applies selection filtering, computes layout and hierarchy. |
| useNavigatorTabs | NavigatorTabs | Page entities, page groups, workload bookmarks, tab settings | Constructs tab IDs, labels, selected status and callbacks. Do not persist these generated objects. |
| NavigatorTabsService | NavigatorTabs and NavigatorButton | Layout and container dimensions | Calculates item size, row/column counts and scroll requirements. |
| NavigatorTabsContainer | Both renderers | `N.style` and computed tabs | Deep-merges state styles; handles pointer states, scrolling, collapse trigger and keyboard navigation. |
| NavTabRenderer | Container | Merged shape state, collapse, hierarchy | Substitutes generated text and icon choice; draws group expanders and child tabs. |
| ShapeCoreRenderer / shapeComponents | NavTabRenderer | `S` and shape discriminator | Renders one of 17 registered shapes; actual Navigator picker offers 16. |
| NavigatorPropertiesPane | Editor | `N.activeEditStyle` and all settings | Updates store state, coordinates compound edits and per-tab icon maps. |
| PropertiesManager | Page save | Whole native `visualState` | Wraps visual properties in schema 0.0.1; does not convert Navigator to friendly AI schema. |
| ALM export/import | Artifact transport | Visual properties envelope and ID maps | Preserves native state; reference rewiring has gaps described below. |

Evidence: NavigatorRenderer, NavigatorTabs, NavigatorTabsContainer.

## 3. Artifact JSON Location and Structure

### 3.1 Exact Native and Persisted Paths

Use the following path aliases throughout this document. Append the suffix in each property table to obtain its full JSON path.

| Alias | Exact expansion |
| --- | --- |
| `V` | `$.properties.visualState` in a wrapped visual properties file |
| `N` | `$.properties.visualState.navigatorState` |
| `T` | `$.properties.visualState.navigatorState.navigatorTabsState` |
| `B` | `$.properties.visualState.navigatorState.navigatorButtonState` |
| `S` | `$.properties.visualState.navigatorState.style.<STATE>.shapeState`; `<STATE>` is one of `DEFAULT`, `HOVER`, `PRESSED`, `ACTIVE` |
| `D` | `$.properties.visualState.drillThroughTooltipConfig` |

At runtime drop `$.properties` and start from the visual object. For the page-save API the wrapper is beneath `$.visuals[visualId]`, so the native state is at `$.visuals[visualId].properties.visualState.navigatorState`.

**Do not place Navigator under plan-level properties, sheet-level properties, or a root `navigatorState`.** It belongs to one native visual. The native `visualType` is the number `203` (`BI_RUNTIME_INPUT`), not the string `NAVIGATOR`. The outer visual also needs valid page membership, identity, dimensions, position, layer information and creation metadata supplied by the general artifact workflow. They are not generated by `INavigatorState`.

The conceptual save envelope is an object containing `schema: "0.0.1"` and `properties`, with `properties.visualType: 203` and `properties.visualState.navigatorState: N`. Preserve other existing `properties` members. No extra JSON-stringification is required for `visualState`.

### 3.2 Exported Artifact Placement

ALM constants name the exported path `sheets/<sheet-record-guid>/visuals/<visual-record-guid>/properties.json`. Related sheet metadata is in `sheets/<sheet-record-guid>/sheet.json`, not inside Navigator state. Workload-level properties use a separate plan properties file.

The inspected V2 export normalizes visual/query/measure references, removes the save-time `schema` member, adds `$schema: getSchemaUrl('Planning/Properties')`, and retains the `properties` object. Obtain the actual schema URI and record GUIDs from the current exporter or an existing valid artifact. Do not invent a URI or treat a database visual ID as a record GUID. Do not copy the save envelope unchanged into a definition part without applying the general deployment contract.

Evidence: PropertiesManager.generateVisualProperties, preparePropertiesForSave, WorkloadPage.service load, EVisualType. Backend source locations are cataloged as E14-E18 in section 14.

### 3.3 Lifecycle and Defaults Boundary

1. Visual creation calls `getNavigatorInitialState(navigatorType, isNavigationBackForDrillThu)` and `getDefaultShapeStyle`.
2. Editor updates call `activePageStore.updateNavigatorState`; it shallow-merges the Navigator's top level and updates the dirty timestamp and undo state.
3. PropertiesManager saves the full native `visualState`. Navigator-specific fields are not filtered out or renamed.
4. Loader accepts `visual.properties.properties` or legacy `visual.properties`, reads `visualState || {}`, then shallowly overlays synced `visualState` when present. ReportMigrationService subsequently normalizes page destination flags and legacy page/icon fields. This is a targeted migration, not full recursive Navigator default hydration.
5. NavigatorRenderer selects the branch from `N.type`. Tabs are regenerated from entity/bookmark stores and sized from the visual's runtime dimensions.
6. Presentation states are merged at runtime, and text/icon selections are derived. Do not write these derived results back as if they were the schema.

Creation defaults can be themed before saving; the tables describe raw factory defaults, not a guarantee of effective theme colors. Preserve synchronized visual configuration: synced `visualState` may override a locally edited Navigator on load.

## 4. Complete Property Reference

### 4.1 Reading the Tables

All rows below are serializable native property paths. They are not a claim that the server validates every member. Containers and dynamic-map schemas are listed separately. Shared style paths are documented once and apply to all four states; overrides are partial.

Requirement codes: **R** = include for deterministic new construction; **C** = conditionally required for requested behavior; **O** = optional; **P** = preserve existing but do not generate for Navigator behavior without a specific reason. `S` defaults mean DEFAULT creation defaults; HOVER/PRESSED/ACTIVE inherit DEFAULT unless explicitly overridden. No field accepts arbitrary `null` as a general rule. Only inactive button targets have explicit null creation evidence. Omission, `null`, an empty object, and an empty array are not equivalent.

Bounds marked **UI** are input-control limits, not proven server-side validation limits. All generated numbers must be finite JSON numbers. Strings for colors/fonts/icons are dynamically resolved; never substitute display labels for identifiers.

Evidence keys used in the inventory are linked and explained in section 14: E1 types; E2 factory/defaults; E3 tab types; E4 runtime tab source/filter; E5 UI compound rules; E6 layout/style merge; E7 shape contract/defaults; E8 shape conversion and rendering; E9 persistence/store/load; E10 drill-through; E11 icon rendering; E12 variables/bookmarks; E13 friendly AI compiler.

### 4.2 Containers and Structural Requirements

| Container | Type | Contract |
| --- | --- | --- |
| `V.navigatorState` | object | R; missing -> no Navigator rendering. No root-level fallback. E1/E9. |
| `N.navigatorButtonState` | object | R in deterministic construction of every kind, even when inactive for tabs. E1/E2. |
| `N.navigatorTabsState` | object | R; complete factory-compatible state for tabs; retain for button-kind editing compatibility. E1-E3. |
| `N.style` | object | R; must have DEFAULT with complete base shape styles. E1/E6. |
| `N.style.DEFAULT` | object | R; `shapeType` plus `shapeState`. |
| `N.style.HOVER`, `N.style.PRESSED`, `N.style.ACTIVE` | object | R for factory parity; `{}` allowed by partial-state type and merge path; no shape override necessary. |
| `N.style.<STATE>.shapeState` | object | R in DEFAULT; O/deep-partial in other states. |
| `T.collapsible`, `T.collapsible.collapseTriggerIcon` | object | R in factory-compatible state; whole collapsible object has runtime fallback, partial objects do not receive a deep fill. |
| `T.hierarchy`, `T.hierarchy.fixedHeight` | object | O as a whole; include all leaves if enabling hierarchy. |
| `T.destinationType` | object | O by type; normal page loading migrates missing/legacy values to the current flag object. Explicitly include it for deterministic construction and direct rendering paths. |
| `T.tabsShortText` | object map | R by native type; `{}` valid; keys are runtime tab IDs and values are strings. |
| `S.tooltip`, `S.rotation`, `S.border`, `S.fill`, `S.snip`, `S.text`, `S.icon`, `S.initialShapeType` | object | R for complete DEFAULT factory parity. Geometry/tooltip fallbacks exist, but no universal shape-state deep hydration. |
| `S.cornerRadius`, `S.padding`, `S.shadow` | object | R inherited shared style structures. |
| `S.text.padding`, `S.icon.padding` | object | R for enabled overlay rendering; initialize all six leaves. |
| `S.icon.iconTypeMapping` | object map | R; keep `default` entry; dynamic tab IDs or `button` can override it. |
| `S.icon.iconTypeMapping.<tabId>`, `S.icon.iconTypeMapping.<tabId>.customIcon` | object | Entry has `src` and optional customIcon metadata; built-in icons use `customIcon.isEnabled: false`. |
| `S.line`, `S.arrow`, `S.chevronArrow`, `S.hexagon`, `S.octagon`, `S.parallelogram`, `S.speechBubble`, `S.trapezoid`, `S.triangle`, `S.glow`, `S.action`, `S.accentBar` | object | Optional in declaration, normally emitted by factory. Keep when mutating; meaningful geometry depends on selected shape. |
| `S.shortText` | object | O; declared but not used as the short-text source by the active conversion path. |
| `S.accentBar.value` | object | C when accent bar enabled; color, side and width. |
| `D` | object | O; sibling of Navigator state, not inside B or S. |

### 4.3 Navigator and Button Fields

| Property path | Type / allowed values | Raw creation default | Requirement, behavior, omission and validation | Evidence |
| --- | --- | --- | --- | --- |
| `N.type` | string; enum K1 | `NAVIGATOR_BUTTON` | R; chooses renderer. Pass kind explicitly to factory. | E1/E2 |
| `N.activeEditStyle` | string; enum K3 | `DEFAULT` | R for editor; persisted editing cursor, not the current runtime hover/pressed state. Some update paths fallback to DEFAULT, others assume it exists. | E1/E5 |
| `N.isNavigationBackForDrillThu` | boolean | omitted unless supplied | O; exact misspelling is contractual; drill-through-return constructor selects PAGE_NAVIGATION, white fill, empty text and ArrowLeft icon. Runtime can overwrite destination with source entity ID. | E1/E2/E10 |
| `B.actionType` | string; enum K2 | `NONE` | R; unknown falls through to no-op. No general raw-JSON validator observed. | E1/E13 |
| `B.webUrl` | string; null for inactive factory state | `null` | C for WEB_URL. Missing/empty -> no action. UI accepts empty or an HTTPS URL with valid dotted hostname length >=3; runtime passes nonempty string to host.openLink without revalidating. | E2/E5 |
| `B.bookmarkId` | string; null for inactive factory state | `null` | C for BOOKMARK_NAVIGATION; it is a normalized uppercase bookmark slug, not database row ID. Falsy -> no-op. | E4/E12 |
| `B.pageDestinationId` | string; null for inactive factory state | `null` | C for PAGE_NAVIGATION/DRILL_THROUGH; resolved page entity ID. Current-page destination does not navigate. Drill-through has stronger runtime eligibility checks. | E2/E10 |
| `B.variableId` | string, dynamic action-variable ID | omitted | C for VARIABLE; missing/unresolvable/non-action variable -> no-op. `create_new` is a UI command, never a valid persisted target ID. | E5/E12 |
| `N.style.<STATE>.shapeType` | string; enum K4 | `RECTANGLE` in DEFAULT, omitted in overrides | R in DEFAULT; inherited by overrides. UI changes DEFAULT. Do not change only initialShapeType.type. | E1/E5/E8 |
| `V.navigatorType` | string; enum K1 | omitted on ordinary new-state construction | P; visual switching can persist this peer creation hint. It is not the active renderer discriminator; keep N.type authoritative and preserve this hint consistently when present. | E9 |

### 4.4 Tab Layout and Selection

| Property path | Type / allowed values | Raw creation default | Requirement, behavior, omission and validation | Evidence |
| --- | --- | --- | --- | --- |
| `T.layoutType` | string; enum K5 | `horizontal` | R; grid requires positive rows/columns for manual layout; unsupported/missing kind takes auto-grid calculation but container behavior is not a compatibility guarantee. | E2/E6 |
| `T.gap` | number; UI 0..100 px, step 1 | 5 | R; subtracts inter-item space before sizing. Excessive gaps can reduce item size to zero. | E2/E5/E6 |
| `T.rows` | number; UI integer 1..30 | 2 | C for manual grid; ignored by vertical/horizontal/auto-grid sizing. Zero/missing triggers auto-grid fallback, not an error. | E3/E6 |
| `T.columns` | number; UI integer 1..30 | 2 | C for manual grid; same omission behavior as rows. | E3/E6 |
| `T.scrollDirection` | string; enum K6 | `vertical` | R for grid/auto-grid; determines overflow axis and CSS grid flow. Use vertical with hierarchy fixed height. | E2/E6 |
| `T.showScrollButtons` | boolean | true | R; buttons appear only when computed scrolling is needed. False does not disable native scrolling. | E2/E6 |
| `T.destinationType.all` | boolean | true | C for normal page list. Missing object/flag is migrated to true during standard page load; direct hook invocation without migration treats it as false. | E2/E4/E19 |
| `T.destinationType.tooltip` | boolean | false | O; with all=true includes tooltip pages; with all=false includes only matching category (union with hidden). | E4 |
| `T.destinationType.hidden` | boolean | false | O; includes hidden entities by category formula, not a security override. | E4 |
| `T.selectedPages` | array of string tab IDs | omitted | O; omission means every eligible tab; [] means none. Applied to bookmarks too by shared filter despite name. Null is unsafe (`includes` consumer). Order does not reorder tabs. | E2/E4 |
| `T.hiddenBookmarks` | array of uppercase bookmark slug strings | [] | O; authoritative runtime bookmark exclusion set. Runtime does not derive it from group selector or hide flag. Preserve/recompute together with those editor properties. | E2/E4/E5 |
| `T.tabsShortText.<tabId>` | string map value; dynamic key | map is {} | O entry; source reads it into tab.shortText, but active text identifier rendering uses tab.label instead. Do not promise custom abbreviated collapsed text. | E3/E4/E6 |
| `T.allowDeselection` | boolean | false | O; runtime destructuring fallback false. Clicking selected bookmark can clear selected slug or apply a launch bookmark. | E2/E4 |
| `T.launchOnDeselection` | string; `none` or resolved uppercase bookmark slug | `none` | O; runtime destructuring fallback `none`. Used only if allowDeselection=true and clicked bookmark already selected. Null is not equivalent to omitted. | E2/E4 |
| `T.selectedBookmarkNavigatorOption` | string; `all` or existing bookmark-group ID | `all` | O; editor intent selector; runtime uses hiddenBookmarks, not this field. Groups are dynamic, not an enum. | E2/E5 |
| `T.isHideDeselectedBookmark` | boolean | false | O; editor recomputes hiddenBookmarks; alone does not hide any runtime tab. Meaning is hiding the configured deselection-launch bookmark, not every unselected bookmark. | E2/E5 |

Array element schemas: selectedPages and hiddenBookmarks contain strings only, not `{id: ...}` objects. Do not assume uniqueness enforcement; construct deduplicated arrays. Resolve keys against actual page/bookmark stores. `tabsShortText` accepts dynamic string keys, not a fixed `tab1`, `tab2` schema.

### 4.5 Collapsible and Hierarchy Fields

| Property path | Type / allowed values | Raw creation default | Requirement, behavior, omission and validation | Evidence |
| --- | --- | --- | --- | --- |
| `T.collapsible.isEnabled` | boolean | false | R; effective collapse requires visible tabs. UI toggling sets vertical layout and isCollapsed to new enabled value. | E2/E5/E6 |
| `T.collapsible.isCollapsed` | boolean | false | R; persisted collapsed state toggled by runtime store update; does not itself persist to server until save. Keep false if feature disabled: renderer reads this field independently in places. | E2/E6 |
| `T.collapsible.collapsedWidth` | number; UI integer 10..500 px | 44 | C when collapsed; maximum-width constraint, not full visual dimension. | E2/E5/E6 |
| `T.collapsible.identifierType` | string; enum K7 | `number` | R; icon/text/roman/number. Text uses full label; shortText is not used by current identifier switch. | E2/E6 |
| `T.collapsible.collapseAnimation` | string; enum K10 | `instant` | R; smooth uses 0.2-second width transition. | E2/E6 |
| `T.collapsible.collapseDirection` | string; enum K8 | `start` | R; controls alignment and chevron direction; UI labels map start=Left, end=Right. | E2/E5/E6 |
| `T.collapsible.collapseTriggerIcon.position` | string; enum K9 | `start` | R; trigger before/after list, not the same as collapse direction. | E2/E6 |
| `T.collapsible.collapseTriggerIcon.size` | number; UI integer 10..50 px | 12 | R; controls trigger/icon height, clipped relative to item size. | E2/E5/E6 |
| `T.collapsible.collapseTriggerIcon.fillColor` | CSS color string | `#000` | R; chevron stroke; runtime local fallback #000. | E2/E6 |
| `T.collapsible.collapseTriggerIcon.backgroundColor` | CSS color string | `#ffffff` | R; runtime absent value falls back to transparent; UI local missing-value display uses #000000, not factory white. | E2/E5/E6 |
| `T.hierarchy.isEnabled` | boolean | false | O; preserves groups rather than flattening leaves. UI visible only if groups exist and forces vertical layout on toggle. | E2/E4/E5 |
| `T.hierarchy.indentation` | number; UI integer 10..50 px | 10 | C for hierarchy; multiplied by depth. UI display fallback 12 differs from factory; renderer missing fallback 0. | E2/E5/E6 |
| `T.hierarchy.triggerColor` | CSS color string | `#000` | C for hierarchy; group-expander stroke. | E2/E6 |
| `T.hierarchy.fixedHeight.isEnabled` | boolean | false | O; fixedHeight applies to vertical layout only when hierarchy enabled. UI missing-value display true is not a load default. | E2/E5/E6 |
| `T.hierarchy.fixedHeight.value` | number; UI integer 30..100 px | 50 | C when fixed height enabled; use scrollDirection=vertical. | E2/E5/E6 |

### 4.6 Shared Shape Appearance Fields

Each row applies at the `S` alias. Include a complete DEFAULT and inherit with partial overrides; no `null` style sections. Creation defaults below are rectangle Navigator defaults. Boolean enablement may control UI visibility rather than suppressing every geometry consumer; section 8 explains exceptions.

| Property path | Type / allowed values | Raw creation default | Requirement, behavior and constraints | Evidence |
| --- | --- | --- | --- | --- |
| `S.tooltip.isEnabled` | boolean | true | R; enables nonempty shape tooltip. | E7/E8 |
| `S.tooltip.content` | string | empty string | R; custom hover text. Empty content may cause a generated action hint; see tooltip routing caveat. | E7/E8 |
| `S.rotation.all` | number, degrees | 0 | R; shared rotation storage; Navigator advanced panel writes shape instead. | E7/E8 |
| `S.rotation.shape` | number; UI 0..360 | 0 | R; shape rotation consumed by core renderer. | E5/E8 |
| `S.rotation.text` | number | 0 | R factory field; distinct from text.textRotation. Do not assume they are synonyms. | E7/E8 |
| `S.rotation.isEnabled` | boolean | true | R; do not assume false suppresses core shape rotation (core reads rotation.shape directly). | E7/E8 |
| `S.rotation.type` | string; enum K11 | `all` | R; shared rotation mode; Navigator advanced editing specifically changes shape. | E7/E8 |
| `S.fill.isEnabled` | boolean | true | R; false converts fill to #F7F7F7, not transparent. | E7/E8 |
| `S.fill.fillColor` | CSS color string | `#e0e0e0` | R if enabled; drill-through-return factory uses #fff. | E7/E8 |
| `S.border.isEnabled` | boolean | true | R; false converts stroke width to 0. | E7/E8 |
| `S.border.color` | CSS color string | `#d0d0d0` | R if enabled; disabled conversion fallback #E0E0E0. | E7/E8 |
| `S.border.width` | number; UI 0..20 px | 1 | R if enabled. | E5/E7 |
| `S.border.side` | string; enum K12 | `all` | R; shared conversion passes borderSide. Triangle UI excludes top. | E7/E8 |
| `S.border.style` | string; enum K13 | `solid` | O; stored by factory/type; base shape converter does not forward it. Do not promise dashed border rendering for every shape. | E7/E8 |
| `S.cornerRadius.isEnabled` | boolean | true | R; rectangle conversion uses shape-specific default when false. | E7/E8 |
| `S.cornerRadius.isCustomCornerRadius` | boolean | false | R; editor uniform/custom mode, not a replacement for numeric corner leaves. | E7 |
| `S.cornerRadius.radiusTopLeft` | number; Navigator uniform UI 0..70 px | 0 | R; many nonrectangular shapes use only this corner radius. Rounded rectangle factory=25; speech bubble=10 when factory is called for that shape. | E5/E7/E8 |
| `S.cornerRadius.radiusTopRight` | number; custom shared UI 0..50 px | 0 | R for rectangles; uniform editor writes all four. | E7/E8 |
| `S.cornerRadius.radiusBottomLeft` | number; custom shared UI 0..50 px | 0 | R for rectangles. | E7/E8 |
| `S.cornerRadius.radiusBottomRight` | number; custom shared UI 0..50 px | 0 | R for rectangles. | E7/E8 |
| `S.padding.isEnabled` | boolean | true | R inherited factory field; top-level padding is not forwarded by generateShapeProps. Preserve; use text/icon padding for overlays. | E7/E8 |
| `S.padding.isCustomPaddingSize` | boolean | false | R factory field; same caveat. | E7/E8 |
| `S.padding.leftPadding` | number, px | 5 | R factory field; same caveat. | E7/E8 |
| `S.padding.rightPadding` | number, px | 5 | R factory field; same caveat. | E7/E8 |
| `S.padding.topPadding` | number, px | 5 | R factory field; same caveat. | E7/E8 |
| `S.padding.bottomPadding` | number, px | 5 | R factory field; same caveat. | E7/E8 |
| `S.shadow.isEnabled` | boolean | false | R; disabled -> no shadow passed to shape. | E7/E8 |
| `S.shadow.width` | number; UI 0..100 px | 3 | C if enabled; UI tooltip says max 50 but actual range says 100. | E5/E7 |
| `S.shadow.blur` | number; UI 0..100 px | 12 | C if enabled. | E5/E7 |
| `S.shadow.color` | CSS color string | `#000000` | C if enabled. | E7 |
| `S.shadow.side` | string; enum K14 | `bottom` | C if enabled; only custom uses stored distance/angle in getShadowOffsets. | E7/E8 |
| `S.shadow.placement` | string; enum K15 | `outer` | C if enabled; inner/outer choose offset semantics. | E7/E8 |
| `S.shadow.opacity` | number; UI 0..100 | 16 | O; UI transparency is 100-opacity. Not a 0..1 value. | E5/E7/E8 |
| `S.shadow.distance` | number; UI 0..100 px | 10 | C when side=custom; preset sides use factory default distance. | E5/E7/E8 |
| `S.shadow.angle` | number; UI 0..360 degrees | 135 | C when side=custom. | E5/E7/E8 |
| `S.glow.isEnabled` | boolean | false | O; glow object has converter fallback if absent. | E7/E8 |
| `S.glow.blur` | number; UI 0..10 | 10 | C if enabled. | E5/E7 |
| `S.glow.color` | CSS color string | `#F7DE6E` | C if enabled. | E7 |
| `S.glow.opacity` | number; UI 0..100 | 100 | O; UI transparency=100-opacity. | E5/E7 |

### 4.7 Shape Geometry Fields

| Property path | Type / allowed values | Raw creation default | Requirement, behavior and constraints | Evidence |
| --- | --- | --- | --- | --- |
| `S.line.isEnabled` | boolean | true | O; shared geometry flag; line converter reads numeric settings regardless of this flag. LINE is excluded from Navigator picker. | E7/E8 |
| `S.line.thickness` | number; UI 1..50 px | 1 | C for LINE. | E5/E7/E8 |
| `S.line.style` | string; enum K13 | `solid` | C for LINE; forwarded as lineStyle. | E7/E8 |
| `S.line.edgeCap` | string; enum K16 | `normal` | C for LINE; do not use square from downstream ILineProps type as native config. | E7/E8 |
| `S.arrow.isEnabled` | boolean | true | O; converter reads geometry even if false. | E7/E8 |
| `S.arrow.direction` | string; enum K17 | `right` | C for ARROW/CHEVRONARROW/PENTAGONARROW. | E7/E8 |
| `S.arrow.arrowheadSize` | number; UI 0..100 percent | 50 | C for ARROW/PENTAGONARROW; factory for PENTAGONARROW=80. Shape change alone does not rerun factory. | E7/E8 |
| `S.arrow.stemWidth` | number; UI 0..100 percent | 25 | C for ARROW; ignored by pentagon-arrow conversion. | E7/E8 |
| `S.chevronArrow.isEnabled` | boolean | true | O; geometry converter does not gate on flag. | E7/E8 |
| `S.chevronArrow.angle` | number; UI 0..100 | 90 | C for CHEVRONARROW; UI suffix is percent despite name angle. | E5/E7/E8 |
| `S.hexagon.isEnabled` | boolean | true | O; geometry converter does not gate on flag. | E7/E8 |
| `S.hexagon.slant` | number; UI 0..50 percent | 25 | C for HEXAGON. | E5/E7/E8 |
| `S.octagon.isEnabled` | boolean | true | O; geometry converter does not gate on flag. | E7/E8 |
| `S.octagon.snipSize` | number; UI 0..50 percent | 33 | C for OCTAGON. | E5/E7/E8 |
| `S.parallelogram.isEnabled` | boolean | true | O; geometry converter does not gate on flag. | E7/E8 |
| `S.parallelogram.slant` | number; UI 0..50 percent | 33 | C for PARALLELOGRAM. | E5/E7/E8 |
| `S.speechBubble.isEnabled` | boolean | true | O; geometry converter does not gate on flag. | E7/E8 |
| `S.speechBubble.chatBubbleHeight` | number; UI 10..90 | 80 | C for SPEECHBUBBLE; forwarded to both chatBubbleHeight and tailSize; do not persist a separate tailSize. UI suffix px. | E5/E7/E8 |
| `S.speechBubble.tailPosition` | string; enum K18 | `bottom-left` | C for SPEECHBUBBLE; eight UI/runtime positions; declaration has four additional unverified literals. | E5/E7/E8 |
| `S.speechBubble.tailAngle` | number; UI 0..180 degrees | 12.5 | O; raw default fractional despite UI step=1. | E5/E7/E8 |
| `S.trapezoid.isEnabled` | boolean | true | O; geometry converter does not gate on flag. | E7/E8 |
| `S.trapezoid.slant` | number; UI 0..100 percent | 33 | C for TRAPEZOID; converter derives topWidthRatio=1-(slant/100)*0.5. Do not persist derived ratio. | E5/E7/E8 |
| `S.triangle.isEnabled` | boolean | true | O; geometry converter does not gate on flag. | E7/E8 |
| `S.triangle.tipPosition` | number; UI 0..100 percent | 50 | C for TRIANGLE; right-angled triangle does not use it. | E5/E7/E8 |
| `S.snip.isEnabled` | boolean | false | R factory object; rectangular snip enablement. | E7/E8 |
| `S.snip.verticalSnipPosition` | string; enum K19 | `top` | C when snip enabled. | E7/E8 |
| `S.snip.horizontalSnipPosition` | string; enum K20 | `right` | C when snip enabled. | E7/E8 |
| `S.snip.snipSize` | number; UI 0..100, step 1, px suffix | 30 | C when snip enabled; numeric geometry is forwarded to rectangle renderer. | E5/E7/E8 |
| `S.initialShapeType.isEnabled` | boolean | true | R factory metadata; not renderer's shape discriminator. | E7/E8 |
| `S.initialShapeType.type` | string; enum K4 | `RECTANGLE` | R factory metadata; used for editor reset/change comparisons, not current shape selection. | E5/E7 |

### 4.8 Text, Icons, and Accent Bar

| Property path | Type / allowed values | Raw creation default | Requirement, behavior and constraints | Evidence |
| --- | --- | --- | --- | --- |
| `S.text.isEnabled` | boolean | true | R; both explicit button and tabs creation enable text. Factory called with no kind has a nuance in section 13. | E2/E7 |
| `S.text.value` | string | Button=`Button`, tabs=empty | R; tab labels override it. Empty button text supported, e.g. icon-only back button. | E2/E6/E7 |
| `S.text.fontFamily` | string, available CSS font | `"Segoe UI", wf_segoe-ui_normal, helvetica, arial, sans-serif` | R; dynamic font availability, no exhaustive finite enum. | E7 |
| `S.text.fontSize` | number; UI 0..100 px | 12 | R; NavTabRenderer explicit missing fallback 12. | E5/E6/E7 |
| `S.text.fontColor` | CSS color string | `#333333` | R. | E7 |
| `S.text.horizontalAlign` | string; enum K21 | `center` | R; text placement. | E7/E8 |
| `S.text.verticalAlign` | string; enum K22 | `middle` | R. | E7/E8 |
| `S.text.isBold` | boolean | false | R. | E7 |
| `S.text.isItalic` | boolean | false | R. | E7 |
| `S.text.isUnderline` | boolean | false | R. | E7 |
| `S.text.textRotation` | number; UI 0..360 degrees | 0 | R; distinct from shape rotation object. | E5/E7 |
| `S.text.padding.isEnabled` | boolean | true | R; preserve even if padding=0. | E7 |
| `S.text.padding.isCustomPaddingSize` | boolean | false | R; UI uniform writes all four padding values. | E5/E7 |
| `S.text.padding.leftPadding` | number; UI 0..50 px | 0 | R if text enabled. | E5/E7 |
| `S.text.padding.rightPadding` | number; UI 0..50 px | 0 | R if text enabled. | E5/E7 |
| `S.text.padding.topPadding` | number; UI 0..50 px | 0 | R if text enabled. | E5/E7 |
| `S.text.padding.bottomPadding` | number; UI 0..50 px | 0 | R if text enabled. | E5/E7 |
| `S.icon.isEnabled` | boolean | false | R; coordinate all states with identifierType=icon to match UI. | E5/E7/E11 |
| `S.icon.color` | CSS color string | `#000` | R if enabled; built-in icon stroke color. | E7/E11 |
| `S.icon.weight` | number; UI 0..50 px | 1 | R if enabled; built-in stroke thickness, not custom-image weight. | E5/E7/E11 |
| `S.icon.transparency` | number; UI 0..100 | 100 | R; despite name it stores opacity percent: renderer divides by 100. UI shows 100-stored value. | E5/E8/E11 |
| `S.icon.placement` | string; enum K23 | `custom` | R; custom independent alignment, others relative to text. | E7/E11 |
| `S.icon.horizontalAlign` | string; enum K21 | `center` | R; meaningful for custom placement. | E5/E11 |
| `S.icon.verticalAlign` | string; enum K22 | `middle` | R; meaningful for custom placement. | E5/E11 |
| `S.icon.size` | number; UI 0..200 px | 30 | R if enabled; renderer truthy size uses fixed dimensions; zero selects auto sizing, not necessarily invisible. | E5/E11 |
| `S.icon.gap` | number; UI 0..50 px | 4 | R; space between icon and text/custom edges. | E5/E11 |
| `S.icon.iconRotation` | number, degrees | 0 | O; custom overlay rotation is relative to canvas by subtracting shape rotation. | E7/E11 |
| `S.icon.customIconScale` | string; enum K24 | `fit` | R; fill is UI/runtime-supported although native union has a typo. | E7/E8/E11 |
| `S.icon.padding.isEnabled` | boolean | true | R; complete padding required by custom overlay access. | E7/E11 |
| `S.icon.padding.isCustomPaddingSize` | boolean | false | R; uniform editor writes all sides. | E5/E7 |
| `S.icon.padding.leftPadding` | number; UI 0..50 px | 4 | R if enabled. | E5/E7 |
| `S.icon.padding.rightPadding` | number; UI 0..50 px | 4 | R if enabled. | E5/E7 |
| `S.icon.padding.topPadding` | number; UI 0..50 px | 4 | R if enabled. | E5/E7 |
| `S.icon.padding.bottomPadding` | number; UI 0..50 px | 4 | R if enabled. | E5/E7 |
| `S.icon.iconTypeMapping.<tabId>.src` | string, valid built-in icon name or data:image URI | default entry empty | C if enabled; use actual registry name, e.g. verified factory ArrowLeft. Custom remote image URLs are not accepted by current custom-image render branch. | E5/E7/E11 |
| `S.icon.iconTypeMapping.<tabId>.customIcon.name` | string | default entry empty | C for custom image; must be nonempty after trim. | E7/E11 |
| `S.icon.iconTypeMapping.<tabId>.customIcon.isEnabled` | boolean | false | C; true interprets src as uploaded custom image; false selects built-in name. | E7/E11 |
| `S.accentBar.isEnabled` | boolean | false | O; UI available for tabs, not buttons; passed to shape renderer. | E5/E7/E8 |
| `S.accentBar.value.color` | CSS color string | `#252423` | C if enabled. | E7 |
| `S.accentBar.value.side` | string; enum K17 | `left` | C if enabled. | E7/E8 |
| `S.accentBar.value.width` | number; UI 0..20 px | 2 | C if enabled. | E5/E7 |

The default icon-map key is literally `default`. Button runtime tab ID is literally `button`; page IDs, bookmark slugs and group IDs are dynamic keys. Preserve mappings for states and tabs that are not being changed. Tab-specific custom-icon upload checks `1 * 1024 * 1024` bytes (1 MiB); its comment incorrectly says 2MB. This is a UI file check, not a verified server JSON size limit.

### 4.9 Persisted Shared Fields Not Used as Navigator Actions

These are real serializable shape-schema members, not additional Navigator button controls. Preserve them on mutation; do not create competing actions here.

| Property path | Type / allowed values | Raw creation default | Requirement, behavior and constraints | Evidence |
| --- | --- | --- | --- | --- |
| `S.action.actionType` | string; enum K2 | `NONE` | P; actual Navigator click switches on B.actionType. Shared shape action can affect tooltip hint generation. | E7/E8 |
| `S.action.isEnabled` | boolean | false | P; not a switch for Navigator click actions. | E7/E8 |
| `S.action.webUrl` | string or inactive null | `null` | P; use B.webUrl for Navigator behavior. | E7/E8 |
| `S.action.bookmarkId` | string or inactive null | `null` | P; use B.bookmarkId. | E7/E8 |
| `S.action.pageDestinationId` | string or inactive null | `null` | P; use B.pageDestinationId. | E7/E8 |
| `S.shortText.isEnabled` | boolean | omitted | P; declaration only in active Navigator path; converter passes text as shortText. | E7/E8 |
| `S.shortText.value` | string | omitted | P; do not use for collapsed abbreviation recipes. | E7/E8 |
| `S.shortText.identifier` | string | omitted | P; no verified active interpretation. | E7/E8 |

### 4.10 Drill-Through Tooltip Sibling

| Property path | Type / allowed values | Creation/UI fallback | Requirement, behavior and constraints | Evidence |
| --- | --- | --- | --- | --- |
| `D.enabled` | boolean | true in editor fallback | O; false makes DrillThroughService return empty string, but NavigatorButton may then fallback to ordinary Navigator tooltip. Not a global tooltip-off guarantee. | E5/E10 |
| `D.enabledTooltip` | string | empty | O; trimmed nonempty override; otherwise generated destination hint when filters exist. | E10 |
| `D.disabledTooltip` | string | empty | O; trimmed nonempty override; otherwise generated selection guidance when filters exist. | E10 |

## 5. Supported Values and Enumerations

The following finite value families are fully enumerated in the discovered active code. Booleans are always true/false and are not counted as enumeration families. Dynamic IDs, CSS colors and fonts are not enums.

| Key | Property family | Complete verified serialized values and meaning |
| --- | --- | --- |
| K1 | Navigator kind | `NAVIGATOR_BUTTON` single button; `BOOKMARK_TABS` workload bookmarks; `PAGE_NAVIGATOR_TABS` page entities. |
| K2 | Action kind | `NONE` no-op; `BACK` previous distinct page in navigation history; `WEB_URL` host link; `PAGE_NAVIGATION` page ID; `BOOKMARK_NAVIGATION` bookmark slug; `CLEAR_SLICER` clear all slicers; `APPLY_SLICER` apply all slicers; `DRILL_THROUGH` eligible page with selection/filter transfer; `VARIABLE` action-variable activation/toggle. |
| K3 | Style state | `DEFAULT` base; `HOVER` pointer over; `PRESSED` pointer down; `ACTIVE` selected page/bookmark/group or drill-through action. Button appearance picker only lists DEFAULT/HOVER/PRESSED although runtime can use ACTIVE. |
| K4 | Shape | `CIRCLE`, `RECTANGLE`, `ROUNDED_RECTANGLE`, `TRIANGLE`, `RIGHTANGLEDTRIANGLE`, `LINE`, `ARROW`, `PENTAGON`, `HEXAGON`, `HEART`, `CHEVRONARROW`, `OCTAGON`, `PARALLELOGRAM`, `PENTAGONARROW`, `PILL`, `SPEECHBUBBLE`, `TRAPEZOID`. LINE has registered renderer/conversion but is filtered out of Navigator picker. |
| K5 | Layout | `vertical` equal-height vertical list (or fixed hierarchy height); `horizontal` equal-width row; `grid` configured row/column viewport; `auto-grid` computed grid. |
| K6 | Scroll direction | `vertical` row-major grid flow and vertical overflow; `horizontal` column-major and horizontal overflow. |
| K7 | Collapsed identifier | `icon` configured icon; `text` full tab label when collapsed; `roman` one-based Roman numeral; `number` one-based decimal numeral. Number/Roman also prefix labels when expanded and collapse enabled. |
| K8 | Collapse direction | `start` left-aligned collapse; `end` right-aligned collapse. |
| K9 | Trigger position | `start` before list; `end` after list. Separate property from K8. |
| K10 | Animation | `instant` no width animation; `smooth` 0.2-second width animation. |
| K11 | Shared rotation type | `all`, `shape`, `text`; declared native mode set. Navigator advanced control writes rotation.shape; do not assume mode alone rotates the feature. |
| K12 | Border side | `all`, `left`, `top`, `right`, `bottom`; triangle editor omits top. |
| K13 | Stroke style | `solid`, `dotted`, `dashed`; native line style and declared border style. Border style forwarding is not verified for all shapes. |
| K14 | Shadow side | `center`, `left`, `right`, `top`, `bottom`, `bottomRight`, `topRight`, `bottomLeft`, `topLeft`, `none`, `custom`. `none` exists in shared type/offset map but is not a selectable UI option; use isEnabled=false to disable. Triangle UI omits top/topLeft/topRight. |
| K15 | Shadow placement | `inner`, `outer`. |
| K16 | Native line cap | `normal` flat; `round` round. Downstream shape-prop union also names square but native line style contract/UI does not. |
| K17 | Direction / accent side | `right`, `left`, `top`, `bottom`. |
| K18 | Speech-bubble tail | `bottom-left`, `bottom-right`, `top-left`, `top-right`, `left-top`, `left-bottom`, `right-top`, `right-bottom`: the eight UI positions matching downstream speech-bubble props. Native IShapeStyles also declares `left`, `right`, `top`, `bottom`; these extra four are declaration-only/unverified construction values. |
| K19 | Vertical snip | `top`, `bottom`, `both`. |
| K20 | Horizontal snip | `right`, `left`, `both`. |
| K21 | Horizontal alignment | `left`, `center`, `right`. |
| K22 | Vertical alignment | `top`, `middle`, `bottom`. |
| K23 | Icon placement | `left`, `right`, `above`, `below`, `custom`. |
| K24 | Custom-image scale | `normal` object-fit none; `fit` contain; `fill` cover; `tile` repeating image background. UI options and runtime helper support all four. Native TCustomIconScale incorrectly repeats fit and omits fill. |

Evidence: E1/E3 establish K1-K3 and K5-K10; E7/E8/E11 establish K4 and K11-K24. These are source-enumerated sets, not claims that every combination was rendered or server-schema validated.

### Shape-Specific Construction Matrix

| Shape | Companion configuration and runtime distinctions |
| --- | --- |
| CIRCLE | No extra geometry; shared text/icon/fill/border. |
| RECTANGLE | Four corner radii and optional snip. |
| ROUNDED_RECTANGLE | Same converter/component as rectangle; explicit radii needed if switching from existing square defaults. Factory called for this shape uses 25. |
| TRIANGLE | triangle.tipPosition and radiusTopLeft. |
| RIGHTANGLEDTRIANGLE | radiusTopLeft; no triangle.tipPosition consumption. |
| LINE | line.thickness/style/edgeCap; no Navigator-picker support; do not choose for normal generation. |
| ARROW | arrow.direction/arrowheadSize/stemWidth plus radiusTopLeft. |
| PENTAGON | radiusTopLeft. |
| HEXAGON | hexagon.slant plus radiusTopLeft. |
| HEART | No extra geometry. |
| CHEVRONARROW | arrow.direction, chevronArrow.angle, radiusTopLeft. |
| OCTAGON | octagon.snipSize, radiusTopLeft. |
| PARALLELOGRAM | parallelogram.slant, radiusTopLeft. |
| PENTAGONARROW | arrow.direction/arrowheadSize, radiusTopLeft; stemWidth not consumed. |
| PILL | Shared radius field; no additional native pill object. |
| SPEECHBUBBLE | speechBubble.chatBubbleHeight/tailPosition/tailAngle and radiusTopLeft; factory radius 10 when created for this shape. |
| TRAPEZOID | trapezoid.slant, radiusTopLeft; topWidthRatio is derived. |

## 6. Configuration Variants

### 6.1 Button Action Variants

| Action | Required companions | Runtime behavior / eligibility |
| --- | --- | --- |
| NONE | None | Keeps styled visual without navigation. |
| BACK | Navigation history | Uses most recent nonempty history ID different from current page. Empty history -> no-op; no useful prior distinct ID is a context gap. |
| WEB_URL | B.webUrl | HTTPS URL satisfying editor validation; opens through host, not a new manually constructed browser route. |
| PAGE_NAVIGATION | B.pageDestinationId | Existing page entity ID; UI excludes current, hidden and INFO_BRIDGE entities. Runtime current-page target no-ops. |
| BOOKMARK_NAVIGATION | B.bookmarkId | Existing workload bookmark slug; applies bookmark with page-navigation dependency injected. |
| APPLY_SLICER | Existing slicers and their apply semantics | Dispatches activePageStore.applyAllSlicers, not a target-specific operation. |
| CLEAR_SLICER | Existing slicers | Dispatches activePageStore.clearAllSlicers. |
| DRILL_THROUGH | B.pageDestinationId, destination filters and matching single data selection | Disabled when destination is invalid; UI offers reporting pages with configured drill-through filters. |
| VARIABLE | B.variableId, action variable and feature switch | Runtime supports action variables; UI picker narrows to action/button/enableToggle=false. If toggle enabled, flips active/inactive; otherwise activates. |

### 6.2 Page Tabs

Eligible entities exclude INFO_BRIDGE. Standard page loading first migrates missing/legacy destination flags as described in section 13. Eligibility formula is:

- If `all=true`: include when `(hidden || !isHiddenPage) && (tooltip || !isTooltipPage)`.
- Otherwise: include when `(hidden && isHiddenPage) || (tooltip && isTooltipPage)`.
- Then selectedPages filters actual tab IDs; omitted means all eligible, empty means no leaves.

This gives all eight boolean combinations. If all/hidden/tooltip are all false, no pages are eligible. With all=false and both other flags true, hidden OR tooltip pages are included, not their intersection. Eligibility is not an authorization grant.

Page-group data comes from workload `pageGroupingMeta.pageGroups` and `pageGroupMapping`; only the first mapped group is used. Groups are ordered by `order ?? 0`, then ungrouped pages follow. Enable hierarchy to retain group headers; otherwise tabs flatten recursively. There is no persisted arbitrary tabs array or persisted reordering list in Navigator.

### 6.3 Bookmark Tabs

Only workload bookmarks are included, not personal bookmark types. Each tab ID is `getBookmarkSlug(bookmark)` (uppercased). hiddenBookmarks filters before grouping; group IDs/labels/order come from bookmark metadata. The runtime does not re-evaluate selectedBookmarkNavigatorOption to produce hiddenBookmarks.

To select one group, set its actual group ID and materialize hiddenBookmarks with slugs of bookmarks outside that group. To hide the deselection-launch bookmark, add its slug as well when allowDeselection=true, launchOnDeselection is not none, and isHideDeselectedBookmark=true. Changing those intent properties alone does not implement the visibility change.

### 6.4 Layout, Collapse and Hierarchy

Horizontal/vertical divide available width/height after subtracting gaps; large gaps can yield zero-sized items. Manual grid uses rows/columns as a viewport and extends content along scrollDirection. The implementation uses fractional tab-count division in total-content estimation; do not replace it with an assumed ceiling formula in a parity validator.

Auto-grid uses minimum-width 150 and minimum-height 170 heuristics, a preferred near-square row/column count, then the best fitting grid or largest available grid with scrolling. These constants are not persisted settings.

Use vertical when collapse or hierarchy is enabled, matching UI enforcement. In hierarchy mode only one group is expanded at once; expandedGroupId is component state, not persisted. Fixed height is applied only in vertical hierarchy layout; choose vertical scroll for that variant. Collapse trigger is shown only if tabs exist. Collapse width restricts rendered max-width, not outer visual size.

## 7. Property Dependencies and Conditional Rules

| Property or feature | Depends on | Condition | Required action | Expected behavior |
| --- | --- | --- | --- | --- |
| Navigator activation | Native visual type 203 and N | Always | Create/register native visual using general artifact flow; add complete native N | Renderer can find the state. |
| WEB_URL | webUrl | Action selected | Validate HTTPS, URL syntax, hostname; set target explicitly | Host opens link. |
| PAGE_NAVIGATION / DRILL_THROUGH | pageDestinationId | Action selected | Resolve existing entity ID in correct environment | Page navigation or drill-through. |
| BOOKMARK_NAVIGATION | bookmarkId | Action selected | Obtain actual normalized slug | Bookmark applied. |
| VARIABLE | variableId + action variable | Action selected | Check PlanningParameters for UI support and matching action-variable scope | Activation/toggle. |
| Manual grid | rows, columns, dimension | layoutType=grid | Set positive integers 1..30 and usable dimensions/gap | Manual viewport rather than fallback. |
| Collapse | vertical, isCollapsed, width and trigger | collapsible.isEnabled=true | Materialize complete collapse structure; coordinate identifier icons | Collapsible list. |
| Collapse disabled | isCollapsed | isEnabled=false | Set isCollapsed=false | Avoid renderer paths treating a disabled list as collapsed. |
| Icon identifiers | icon.enabled + icon map | identifierType=icon | Enable icon consistently in each state and supply actual mappings | Icon visible when collapsed. |
| Hierarchy | page/bookmark group metadata | hierarchy enabled | Ensure source groups exist and layout is vertical | Group headers and indented children. |
| Fixed hierarchy height | hierarchy.enabled + fixedHeight.enabled | Fixed height desired | Set value and vertical scroll | Consistent item height and overflow handling. |
| Page destinations | destinationType | Page tabs | Explicitly set all/hidden/tooltip | Correct eligible categories. |
| Restrict tabs | selectedPages | Selection desired | Store actual tab IDs; omit to select all | Shared include filter. |
| Bookmark group selection | hiddenBookmarks | Group selector != all | Recompute exclusions; preserve existing intentional exclusions consciously | Runtime group restriction actually applied. |
| Hide deselection launch | allowDeselection, launchOnDeselection, hiddenBookmarks | Hide flag enabled | Add launch slug to exclusion array | Launch target omitted from displayed list. |
| Shape switch | DEFAULT.shapeType and geometry | Different shape requested | Set correct companion geometry; preserve initialShapeType meaning | Correct shape and editor reset metadata. |
| Interaction styles | DEFAULT | Hover/pressed/active | Deep-merge partial overrides; never replace DEFAULT with partial state | Effective style precedence preserved. |
| Custom image | customIcon.isEnabled/name/src | Custom icon desired | data:image URI, nonempty name, compatible scale | Image branch renders. |
| Synced visual | syncConfig / syncVisualsState | Sync enabled | Mutate owning synced state through established workflow | Avoid load overriding local edit. |
| Drill-through tooltip | V.drillThroughTooltipConfig | Drill-through action | Store sibling object, not nested B property; test actual tooltip path | Service computes enabled/disabled strings. |
| Cross-environment promotion | Entity/bookmark/variable mappings | Import/deploy | Re-resolve every dynamic reference after import; do not assume Navigator binding covers nested state | Avoid stale source-environment IDs. |

## 8. Runtime and Functional Behavior

### 8.1 State Merging and Editing

Effective shape style order is DEFAULT, then ACTIVE if selected, then HOVER, then PRESSED. Later values win through `ts-deepmerge`. Disabled tabs return DEFAULT without state merging. Page button ACTIVE depends on target=current page; bookmark button ACTIVE depends on selected slug; drill-through button is considered selected even before eligibility styling is evaluated. ACTIVE is not runtime-selected merely because activeEditStyle is ACTIVE.

`updateNavigatorStyleState` does more than a deep merge: editing DEFAULT propagates changed child keys into HOVER/PRESSED/ACTIVE when the override value is undefined or equals the previous DEFAULT value; explicit differing overrides are retained. For new construction choose intentional overrides. For safe mutation mirror this propagation if matching editor behavior matters.

Geometry editing targets DEFAULT; shape overrides are technically mergeable but are not the standard UI geometry workflow. Resets are section-specific and can preserve geometry; replacing the whole style object with factory defaults is not equivalent to reset appearance.

### 8.2 Rendering and Input

Read mode executes pointer actions directly; edit mode ShapeCoreRenderer requires Ctrl or Command on pointer-up. Tab container keyboard handling similarly requires the modifier in edit mode; do not infer identical keyboard behavior for the single button because its call does not supply shouldRequireCtrlClick. No artifact property configures this requirement.

Labels are derived from page displayName or bookmark name. In collapsed number/Roman modes the identifier is one-based; child indexing restarts within each rendered group. text identifier uses full label, not tabsShortText. Icon lookup prefers current tab ID then default; group-specific maps may be preserved but editor primarily exposes flattened leaf mappings.

Collapsed state is stored in Navigator on trigger click; group-expanded state, hoveredId, pressedId, focus refs, scroll offsets and canScroll flags remain transient. No reload is needed for ordinary store edits; save is necessary for durable changes. No evidence establishes an automatic save merely because a collapse trigger was clicked.

### 8.3 Styling Caveats

- Disabling fill is not transparent: converter supplies #F7F7F7.
- Many geometry enable flags are not checked by the geometry converter; their presence does not define a universal disabled-section rule.
- Some nonrectangle shapes read radiusTopLeft regardless of cornerRadius.isEnabled.
- Changing shapeType does not reconstruct all geometry defaults. Explicitly initialize radii/head sizes for intended appearance.
- Top-level shape padding and S.shortText are not forwarded as independent rendering controls by generateShapeProps. Prefer text.padding and icon.padding.
- Icon transparency is persisted opacity percent; 100 is opaque, 0 transparent. UI labels alone would suggest the opposite.
- Tooltip values computed in NavigatorButton are attached to a runtime tab, but NavTabRenderer does not pass tab.tooltip as ShapeCoreRenderer's tooltip prop. Shape tooltip content can still render through shapeStyles; do not promise service-generated drill-through hints without an end-to-end UI test.
- D.enabled=false returns an empty service tooltip, then NavigatorButton uses logical-OR fallback to ordinary Navigator tooltip. Disable/test both paths for a strict no-tooltip requirement.

### 8.4 Drill-Through and Action Variables

DrillThroughService.isValidDestination requires destination config, selections, matching dimension column IDs or matching source measures, and no merged multiple-selection cross-filter. Certain KPI-only source visuals without sparklines are rejected. Button eligibility only uses selections from a click trigger; another trigger supplies an empty selection array there. Navigation maps destination filter values, stores source page/filter context, and calls the normal page-navigation handler.

The special `isNavigationBackForDrillThu` effect copies runtime sourceEntityId into B.pageDestinationId and clears selections. That target is derived from the active session, not a reusable hardcoded origin page. Preserve the special flag only for an intentional drill-through return button.

VARIABLE looks up workload/entity action variables through VariablesService. With enableToggle omitted/true it toggles current/default active/inactive state; false always activates. Scripts and variable definitions live in their own variable configuration, not in B.variableId. This specification does not authorize or invent action scripts.

## 9. Integration with Other Fabric Plan Features

| Integration | Verified reference mechanism | Construction implication |
| --- | --- | --- |
| Native visual host | EVisualType.BI_RUNTIME_INPUT=203; native visual state | Preserve host visual metadata and renderer registration. |
| Page entities | B.pageDestinationId; selectedPages; map keys | Resolve entity IDs, not page captions or record GUIDs unless current transport explicitly maps them. |
| Page grouping | workload pageGroupingMeta | Group structure is external; toggling hierarchy does not create page groups. |
| Workload bookmarks | Uppercase bookmark slug; bookmarkGroupId | Resolve actual bookmarks, ensure applied bookmark/page context exists. Personal bookmarks excluded. |
| Slicers | applyAllSlicers / clearAllSlicers store actions | Existing slicer config determines results; no target slicer ID on B. |
| Drill-through | Workload destination config filters, selected data field IDs, source filters | A destination ID alone is insufficient to enable button. |
| Variables | B.variableId -> VariablesService scope resolution | Preserve workload/entity variable stores; UI feature gate PlanningParameters. |
| Themes | applyInnerVisualTheme mutates initial shapes/styles | Factory colors can be overridden before persistence; preserve current theme-aware values unless user asks otherwise. |
| Format painter and mobile/layout | Native shape styles and enclosing visual dimensions/mobile metadata | Keep unrelated layout/mobile/layer properties; no separate Navigator mobile schema established. |
| Visual sync | syncVisualsState.visualState overrides loaded visualState | Identify owning source before mutation. |
| ALM | Export/import ID rewrite registries | Portability gaps below must be checked in target environment. |

### 9.1 Deployment Reference-Rewrite Limitations

The shared backend `navigatorElementBinding` declares a partial older Navigator shape and rewrites only navigatorTabsState.hiddenPages and navigatorButtonState.pageDestinationId via entityIdMapping. It neither declares nor rewrites selectedPages, tabsShortText keys, icon map keys, bookmark targets/exclusions/group selector, or variableId.

There is a second boundary: inspected V2 applyPropertyRewires looks for `updated.properties[handler.property]`; Navigator handler property is navigatorState, while frontend persists it at `properties.visualState.navigatorState`. That helper is not recursive. Therefore the existence of the binding is **not proof** that it reaches the current nested state. The inspected export call also supplies only visualIdMapping, not entityIdMapping. A neighboring backend test verifies no changes/no warning for flat Navigator references when only visual mappings are supplied; it does not prove page-reference rewiring on promotion.

Do not move Navigator state to the wrong root location to make a rewire fire. Keep the frontend contract and verify/repair target references through the deployment workflow. The general exporter also normalizes visual/query/measure references; this is not evidence that arbitrary Navigator ID maps or bookmark slugs are normalized. No deployment was executed for this document.

## 10. Valid JSON Configuration Examples

### 10.1 Example Conventions and Validation Levels

All JSON blocks in this section are valid JSON. **R1 is a factory-complete Navigator-state fragment**, not a whole artifact. Insert it as N in a properly created native visual. R2-R9 are **merge fragments** relative to the stated existing object: recursively merge objects into a complete factory-compatible state, replacing arrays deliberately; do not send a fragment directly to the shallow store reducer or treat it as a complete artifact.

References written `${...}` are explicit substitution slots, not fabricated IDs or deployable literal values. Resolve them before deployment. Recipe validation checks syntax, native member names/types/enums, factory parity and focused source behavior where possible. It does not certify tenant authorization, live UI behavior, a service JSON schema, or cross-environment deployment.

### R1. Conservative Minimal No-Action Button

Smallest **factory-complete construction baseline verified here**, rather than a mathematically minimal renderer object. Mandatory structure is retained because load does not hydrate it. Unused variableId, selectedPages, isNavigationBackForDrillThu, shortText and drill-through tooltip are omitted. Empty override objects would inherit; factory overrides are retained for predictable appearance.

```json
{
	"type": "NAVIGATOR_BUTTON",
	"navigatorButtonState": {
		"actionType": "NONE",
		"bookmarkId": null,
		"webUrl": null,
		"pageDestinationId": null
	},
	"navigatorTabsState": {
		"gap": 5,
		"layoutType": "horizontal",
		"scrollDirection": "vertical",
		"showScrollButtons": true,
		"hiddenBookmarks": [],
		"columns": 2,
		"rows": 2,
		"destinationType": { "all": true, "tooltip": false, "hidden": false },
		"collapsible": {
			"isEnabled": false,
			"collapsedWidth": 44,
			"collapseAnimation": "instant",
			"collapseDirection": "start",
			"collapseTriggerIcon": { "backgroundColor": "#ffffff", "fillColor": "#000", "position": "start", "size": 12 },
			"isCollapsed": false,
			"identifierType": "number"
		},
		"tabsShortText": {},
		"hierarchy": { "isEnabled": false, "indentation": 10, "triggerColor": "#000", "fixedHeight": { "isEnabled": false, "value": 50 } },
		"allowDeselection": false,
		"selectedBookmarkNavigatorOption": "all",
		"launchOnDeselection": "none",
		"isHideDeselectedBookmark": false
	},
	"style": {
		"DEFAULT": {
			"shapeType": "RECTANGLE",
			"shapeState": {
				"tooltip": { "content": "", "isEnabled": true },
				"rotation": { "all": 0, "shape": 0, "text": 0, "isEnabled": true, "type": "all" },
				"border": { "isEnabled": true, "color": "#d0d0d0", "side": "all", "width": 1, "style": "solid" },
				"cornerRadius": { "isEnabled": true, "isCustomCornerRadius": false, "radiusBottomLeft": 0, "radiusBottomRight": 0, "radiusTopLeft": 0, "radiusTopRight": 0 },
				"padding": { "isEnabled": true, "isCustomPaddingSize": false, "bottomPadding": 5, "leftPadding": 5, "rightPadding": 5, "topPadding": 5 },
				"shadow": { "isEnabled": false, "blur": 12, "color": "#000000", "side": "bottom", "placement": "outer", "opacity": 16, "width": 3, "distance": 10, "angle": 135 },
				"glow": { "isEnabled": false, "blur": 10, "opacity": 100, "color": "#F7DE6E" },
				"fill": { "fillColor": "#e0e0e0", "isEnabled": true },
				"line": { "thickness": 1, "style": "solid", "edgeCap": "normal", "isEnabled": true },
				"arrow": { "direction": "right", "arrowheadSize": 50, "stemWidth": 25, "isEnabled": true },
				"chevronArrow": { "angle": 90, "isEnabled": true },
				"hexagon": { "slant": 25, "isEnabled": true },
				"octagon": { "snipSize": 33, "isEnabled": true },
				"parallelogram": { "slant": 33, "isEnabled": true },
				"speechBubble": { "chatBubbleHeight": 80, "tailPosition": "bottom-left", "tailAngle": 12.5, "isEnabled": true },
				"trapezoid": { "slant": 33, "isEnabled": true },
				"triangle": { "tipPosition": 50, "isEnabled": true },
				"snip": { "isEnabled": false, "verticalSnipPosition": "top", "horizontalSnipPosition": "right", "snipSize": 30 },
				"text": {
					"value": "Button", "isEnabled": true,
					"fontFamily": "\"Segoe UI\", wf_segoe-ui_normal, helvetica, arial, sans-serif",
					"fontSize": 12, "fontColor": "#333333", "horizontalAlign": "center", "verticalAlign": "middle",
					"isBold": false, "isItalic": false, "isUnderline": false, "textRotation": 0,
					"padding": { "leftPadding": 0, "bottomPadding": 0, "rightPadding": 0, "topPadding": 0, "isCustomPaddingSize": false, "isEnabled": true }
				},
				"icon": {
					"isEnabled": false, "color": "#000", "weight": 1, "size": 30, "transparency": 100,
					"placement": "custom", "horizontalAlign": "center", "verticalAlign": "middle",
					"padding": { "leftPadding": 4, "bottomPadding": 4, "rightPadding": 4, "topPadding": 4, "isCustomPaddingSize": false, "isEnabled": true },
					"iconTypeMapping": { "default": { "customIcon": { "name": "", "isEnabled": false }, "src": "" } },
					"customIconScale": "fit", "iconRotation": 0, "gap": 4
				},
				"action": { "actionType": "NONE", "isEnabled": false, "pageDestinationId": null, "bookmarkId": null, "webUrl": null },
				"initialShapeType": { "isEnabled": true, "type": "RECTANGLE" },
				"accentBar": { "isEnabled": false, "value": { "color": "#252423", "side": "left", "width": 2 } }
			}
		},
		"HOVER": { "shapeState": { "fill": { "fillColor": "#c0c0c0" }, "text": { "fontColor": "#000000" } } },
		"PRESSED": { "shapeState": { "fill": { "fillColor": "#a0a0a0" }, "text": { "fontColor": "#ffffff" } } },
		"ACTIVE": { "shapeState": { "fill": { "fillColor": "#000000" }, "text": { "fontColor": "#ffffff" }, "icon": { "color": "#ffffff" } } }
	},
	"activeEditStyle": "DEFAULT"
}
```

### R2. Typical Business Button: Open Forecast Guidance

Recursive merge at N into R1. No environment-specific references are required for this feature fragment. General visual/artifact creation is still required.

```json
{
	"navigatorButtonState": { "actionType": "WEB_URL", "webUrl": "https://example.com/forecast-guidance" },
	"style": { "DEFAULT": { "shapeState": { "text": { "value": "Forecast Guidance" }, "tooltip": { "isEnabled": true, "content": "Open forecast guidance" } } } }
}
```

### R3. Page Tabs in a Manual Grid

Recursive merge at N into R1. Lists normal, nonhidden, nontooltip pages; title text is generated from actual page display names. Set enclosing native visual dimensions to a usable viewport, e.g. 600 by 240 through the general layout workflow.

```json
{
	"type": "PAGE_NAVIGATOR_TABS",
	"navigatorTabsState": {
		"layoutType": "grid", "rows": 2, "columns": 3, "gap": 8,
		"scrollDirection": "vertical", "showScrollButtons": true,
		"destinationType": { "all": true, "hidden": false, "tooltip": false }
	},
	"style": { "DEFAULT": { "shapeState": { "text": { "value": "" } } } }
}
```

### R4. Advanced Collapsible Hierarchical Page Navigation

Recursive merge at N into R1; requires existing page groups. Numbers identify collapsed items. Fixed tab height=48 and vertical scrolling are coordinated. Initial collapsed state is intentional.

```json
{
	"type": "PAGE_NAVIGATOR_TABS",
	"navigatorTabsState": {
		"layoutType": "vertical", "gap": 6, "scrollDirection": "vertical",
		"collapsible": { "isEnabled": true, "isCollapsed": true, "collapsedWidth": 48, "identifierType": "number", "collapseAnimation": "smooth", "collapseDirection": "start", "collapseTriggerIcon": { "position": "start", "size": 16, "fillColor": "#222222", "backgroundColor": "#ffffff" } },
		"hierarchy": { "isEnabled": true, "indentation": 16, "triggerColor": "#222222", "fixedHeight": { "isEnabled": true, "value": 48 } }
	},
	"style": { "ACTIVE": { "shapeState": { "accentBar": { "isEnabled": true, "value": { "color": "#117865", "side": "left", "width": 3 } } } } }
}
```

### R5. Bookmark Group with Hidden Reset-on-Deselection Target

Recursive merge at N into R1. Resolve the real group ID and slugs. `${OUTSIDE_GROUP_BOOKMARK_SLUG}` stands for a representative exclusion; enumerate **every** out-of-group workload bookmark slug, not just this slot. `${RESET_BOOKMARK_SLUG}` is the actual launch target and must be excluded from visible tabs.

```json
{
	"type": "BOOKMARK_TABS",
	"navigatorTabsState": {
		"layoutType": "horizontal",
		"selectedBookmarkNavigatorOption": "${BOOKMARK_GROUP_ID}",
		"allowDeselection": true,
		"launchOnDeselection": "${RESET_BOOKMARK_SLUG}",
		"isHideDeselectedBookmark": true,
		"hiddenBookmarks": ["${OUTSIDE_GROUP_BOOKMARK_SLUG}", "${RESET_BOOKMARK_SLUG}"]
	}
}
```

### R6. Action Targets and Drill-Through Tooltip Variants

Each array element is an alternative recursive merge at **V**, not an array to store. Start with V.navigatorState=R1. Resolve every slot. All six actions needing no more shape changes are demonstrated; R2 covers WEB_URL and R1 covers NONE.

```json
[
	{ "navigatorState": { "navigatorButtonState": { "actionType": "BACK" } } },
	{ "navigatorState": { "navigatorButtonState": { "actionType": "PAGE_NAVIGATION", "pageDestinationId": "${PAGE_ENTITY_ID}" } } },
	{ "navigatorState": { "navigatorButtonState": { "actionType": "BOOKMARK_NAVIGATION", "bookmarkId": "${BOOKMARK_SLUG}" } } },
	{ "navigatorState": { "navigatorButtonState": { "actionType": "APPLY_SLICER" } } },
	{ "navigatorState": { "navigatorButtonState": { "actionType": "CLEAR_SLICER" } } },
	{ "navigatorState": { "navigatorButtonState": { "actionType": "VARIABLE", "variableId": "${ACTION_VARIABLE_ID}" } } },
	{ "navigatorState": { "navigatorButtonState": { "actionType": "DRILL_THROUGH", "pageDestinationId": "${DRILLTHROUGH_PAGE_ENTITY_ID}" } }, "drillThroughTooltipConfig": { "enabled": true, "enabledTooltip": "Open detail", "disabledTooltip": "Select one matching data point" } }
]
```

This validates native field placement, not action execution. Drill-through additionally needs a matching live selection and destination filters; variable action needs the actual variable definition and scope.

### R7. Materially Different Layout and Identifier Choices

Each element is an alternative recursive N merge. Resolve actual page IDs. For the icon variant the verified ArrowLeft icon is used as a fallback for all tabs; replace with user-appropriate registry names only after resolving them. All four style states explicitly enable icons to mirror UI compound behavior.

```json
[
	{ "type": "PAGE_NAVIGATOR_TABS", "navigatorTabsState": { "layoutType": "auto-grid", "scrollDirection": "horizontal", "showScrollButtons": true } },
	{ "type": "PAGE_NAVIGATOR_TABS", "navigatorTabsState": { "layoutType": "vertical", "selectedPages": ["${PAGE_ENTITY_ID}"], "destinationType": { "all": true, "hidden": true, "tooltip": true } } },
	{ "type": "PAGE_NAVIGATOR_TABS", "navigatorTabsState": { "layoutType": "vertical", "collapsible": { "isEnabled": true, "isCollapsed": true, "identifierType": "roman" } } },
	{ "type": "PAGE_NAVIGATOR_TABS", "navigatorTabsState": { "layoutType": "vertical", "collapsible": { "isEnabled": true, "isCollapsed": true, "identifierType": "text" } } },
	{
		"type": "PAGE_NAVIGATOR_TABS",
		"navigatorTabsState": { "layoutType": "vertical", "collapsible": { "isEnabled": true, "isCollapsed": true, "identifierType": "icon" } },
		"style": {
			"DEFAULT": { "shapeState": { "icon": { "isEnabled": true, "iconTypeMapping": { "default": { "src": "ArrowLeft", "customIcon": { "name": "", "isEnabled": false } } } } } },
			"HOVER": { "shapeState": { "icon": { "isEnabled": true } } },
			"PRESSED": { "shapeState": { "icon": { "isEnabled": true } } },
			"ACTIVE": { "shapeState": { "icon": { "isEnabled": true } } }
		}
	}
]
```

### R8. Shape Variants with Required Geometry

Each element is an alternative recursive merge at `N.style.DEFAULT`, on top of R1's complete style. These are not an array stored in DEFAULT. Shapes without special geometry need only shapeType; all 16 Navigator-picker choices are represented here. LINE is deliberately excluded from generation recipes despite having a downstream renderer.

```json
[
	{ "shapeType": "CIRCLE" },
	{ "shapeType": "RECTANGLE", "shapeState": { "snip": { "isEnabled": true, "verticalSnipPosition": "top", "horizontalSnipPosition": "right", "snipSize": 20 } } },
	{ "shapeType": "ROUNDED_RECTANGLE", "shapeState": { "cornerRadius": { "radiusTopLeft": 25, "radiusTopRight": 25, "radiusBottomLeft": 25, "radiusBottomRight": 25 } } },
	{ "shapeType": "TRIANGLE", "shapeState": { "triangle": { "isEnabled": true, "tipPosition": 50 } } },
	{ "shapeType": "RIGHTANGLEDTRIANGLE" },
	{ "shapeType": "ARROW", "shapeState": { "arrow": { "isEnabled": true, "direction": "right", "arrowheadSize": 50, "stemWidth": 25 } } },
	{ "shapeType": "PENTAGON" },
	{ "shapeType": "HEXAGON", "shapeState": { "hexagon": { "isEnabled": true, "slant": 25 } } },
	{ "shapeType": "HEART" },
	{ "shapeType": "CHEVRONARROW", "shapeState": { "arrow": { "direction": "left" }, "chevronArrow": { "isEnabled": true, "angle": 90 } } },
	{ "shapeType": "OCTAGON", "shapeState": { "octagon": { "isEnabled": true, "snipSize": 33 } } },
	{ "shapeType": "PARALLELOGRAM", "shapeState": { "parallelogram": { "isEnabled": true, "slant": 33 } } },
	{ "shapeType": "PENTAGONARROW", "shapeState": { "arrow": { "isEnabled": true, "direction": "right", "arrowheadSize": 80 } } },
	{ "shapeType": "PILL" },
	{ "shapeType": "SPEECHBUBBLE", "shapeState": { "speechBubble": { "isEnabled": true, "chatBubbleHeight": 80, "tailPosition": "bottom-left", "tailAngle": 12.5 }, "cornerRadius": { "radiusTopLeft": 10 } } },
	{ "shapeType": "TRAPEZOID", "shapeState": { "trapezoid": { "isEnabled": true, "slant": 33 } } }
]
```

### R9. Custom-Image Icon Schema Variant

Recursive merge at `N.style.DEFAULT.shapeState.icon`. Resolve src to a real validated data:image URI and name to nonempty original file name. This is a substitution-dependent schema fragment, **not an asset-validated recipe**. Built-in variant uses `customIcon.isEnabled: false` and a resolved registry name, as R7 shows.

```json
{
	"isEnabled": true,
	"placement": "custom",
	"size": 30,
	"transparency": 100,
	"customIconScale": "fit",
	"iconTypeMapping": { "default": { "src": "${DATA_IMAGE_URI}", "customIcon": { "name": "${IMAGE_FILE_NAME}", "isEnabled": true } } }
}
```

### 10.2 Validation Record

Executed locally with Node.js v24.22.0, using its built-in `module.stripTypeScriptTypes` in transform mode. The repository has no locally resolvable TypeScript dependency, so no dependency installation or full application build was performed. Source modules were transformed in memory, their imports wired to real loaded feature dependencies or minimal unused type/theme stubs, and their actual exported functions executed. These are isolated source-function checks, not a running React application or deployed service.

| Check | Result and boundary |
| --- | --- |
| R1-R9 JSON syntax | All 9 fenced JSON blocks parsed successfully with JSON.parse. |
| R1 factory parity | Exact deep equality against JSON-serialized getNavigatorInitialState(ENavigatorType.NAVIGATOR_BUTTON), including shared shape defaults and interaction overrides. |
| R1-R9 materialized schemas | 34 alternatives after recursive merge passed native member-name/type checks and current finite-value membership checks. R6 contains 7 alternatives, R7 5, R8 16; the remaining groups each have one. These are focused contract checks, not an official server JSON-schema validator. |
| Layout source execution | Actual NavigatorTabsService calculations exercised for vertical, horizontal, grid and auto-grid; manual-grid item dimensions/overflow, zero-row fallback and 48px hierarchy fixed height asserted. |
| Selection and style source execution | getFilteredNavTabPages asserted omission includes all and [] includes none. updateNavigatorStyleState asserted DEFAULT change preserves a different explicit HOVER color. |
| Migration source execution | Actual ReportMigrationService exercised with 9 destination input cases, hiddenPages conversion, existing selection precedence, conversion deferral without page IDs, and legacy tab/button icon migrations. |
| Backend handler source execution | Actual navigatorElementBinding with entity mappings rewrote pageDestinationId and hiddenPages; selectedPages, tabsShortText keys and bookmark target remained unchanged. |
| Backend helper source execution | Actual isolated V2 applyPropertyRewires function did not reach nested properties.visualState.navigatorState even with entity mappings, confirming the documented portability gap. |
| Factory completeness audit | Every one of 151 normalized factory leaf paths appears in the current inventory; repeated interaction-state paths are normalized to the shared S schema. Optional declaration fields and visual-state siblings were audited separately. |
| Evidence and structure | Local link targets and all 15 numbered sections checked. No application source files were edited. |

**Coverage accounting:** 162 distinct current serializable leaf-property templates are individually documented in sections 4.3-4.10. This counts shared style leaves once under S and dynamic maps once per element schema, not once per tab. Expanding the 118 shared style leaves and shapeType across all four states yields 519 possible concrete state-qualified leaf paths, **not** 519 fields emitted by the factory. Seven legacy leaf templates are documented separately in section 13.3. Object containers are documented but excluded from these leaf counts. The 24 current finite-value families in section 5 are fully source-enumerated; the four legacy destination strings are additional compatibility inputs, not recommended current values.

Unvalidated requirements: R5, reference-bearing R6 variants and R7's selected-page variant require real target context; R9 requires a real image payload and asset render check. No browser rendering, action execution, live service-schema validation or deployment was performed for any recipe. R2's HTTPS URL was cross-checked against source validation rules, not opened by a host. No placeholder is proof of an existing authorized reference.

A downstream agent can repeat JSON syntax checking from the repository root without installing packages:

```javascript
const fs = require('node:fs');
const text = fs.readFileSync('Navigators-Artifact-Spec.md', 'utf8');
const recipes = [...text.matchAll(/```json\r?\n([\s\S]*?)```/g)];
for (const recipe of recipes) JSON.parse(recipe[1]);
console.log(`Parsed ${recipes.length} JSON recipe blocks`);
```

This syntax-only command does not repeat the isolated source behavior checks or verify reference/asset resolution.

## 11. Invalid Configurations and Common Mistakes

The following are intentionally **invalid for agent construction** or fail the stated intent; not all are rejected by a server validator.

| Invalid choice | Verified problem | Correction |
| --- | --- | --- |
| Persist friendly `button.action` | Native renderer reads B.actionType | Compile friendly schema or construct native state. |
| Put N at properties.navigatorState | Frontend loader/renderer expects properties.visualState.navigatorState | Preserve correct nested location despite backend legacy binding shape. |
| Use string visualType `NAVIGATOR` | Native visual type enum uses number 203 | Register correct native visual metadata. |
| Write a partial navigatorTabsState via shallow reducer | Replaces entire previous tab object | Merge with existing complete tab state first. |
| Missing/null style.DEFAULT or text/icon padding | No universal deep hydration; direct runtime member access exists | Materialize complete DEFAULT. |
| selectedPages=null | Shared filter calls includes on values other than undefined | Omit for all or supply string array. |
| selectedPages=[] when user means all | All leaves filtered out | Omit property for all eligible tabs. |
| Bypass migration and omit destinationType on page tabs assuming all=true | Direct source hook defaults missing flags false; later container default cannot restore absent source tabs | Explicit `{all:true,hidden:false,tooltip:false}`; normal page-load migration also supplies these defaults. |
| Set bookmark group selector only | Runtime ignores selector for filtering | Recompute hiddenBookmarks. |
| Set hide-deselected flag only | No runtime visibility change | Coordinate allowDeselection, launch target and hiddenBookmarks. |
| Use page caption as pageDestinationId | Navigation resolves actual entity ID | Query existing page context. |
| Use database bookmark ID or lowercase invented slug | Runtime tab IDs are normalized uppercase slugs | Resolve getBookmarkSlug result. |
| WEB_URL=http://... | UI rejects non-HTTPS | Valid https URL with dotted hostname; runtime host acceptance still environment-dependent. |
| VARIABLE variableId=create_new | UI sentinel is not a variable record | Create/resolve variable through variable workflow. |
| grid rows=0 or missing columns | Calculator falls back to auto-grid | Use positive integer rows/columns, both present. |
| Collapsible horizontal/grid | Contradicts coordinated UI vertical layout | Set vertical, retain all required collapse leaves. |
| Disable collapse but retain isCollapsed=true | Some renderer branches still use isCollapsed | Reset isCollapsed=false. |
| icon size=0 to hide | Truthy size check selects auto dimensions | Disable icon or use stored opacity=0 deliberately. |
| icon transparency=100 to make transparent | Stored field is opacity percent | Use 0 for transparent, 100 for opaque. |
| Custom src=https URL | Custom branch requires data:image prefix and nonempty custom name | Use validated uploaded data URI and metadata. |
| tailPosition=left based only on native declaration | Not one of eight verified UI/downstream positions | Choose left-top or left-bottom as intended. |
| Change initialShapeType.type only | Renderer uses style state shapeType | Change DEFAULT.shapeType and related geometry. |
| Persist runtime tabs, onClick, dimensions, expandedGroupId | Derived/component state, not Navigator contract | Persist source settings only. |
| Assume D.enabled=false suppresses all tooltips | Ordinary tooltip fallback and missing prop forwarding | Verify actual rendered path and disable ordinary shape tooltip too when required. |
| Assume ALM rewires selectedPages/icon keys | No such handling in inspected binding | Verify target IDs/maps after import. |

## 12. Agentic Construction Instructions

### 12.1 Translate User Intent

| User requirement | Relevant properties | Required values or configuration | Dependencies |
| --- | --- | --- | --- |
| Open an external planning guide | N.type, B.actionType, B.webUrl | NAVIGATOR_BUTTON, WEB_URL, validated https URL | Host link support. |
| Go to a page | B.actionType, B.pageDestinationId | PAGE_NAVIGATION + resolved entity ID | Existing accessible target page. |
| Apply a saved view | B.actionType, B.bookmarkId | BOOKMARK_NAVIGATION + normalized slug | Workload bookmark context. |
| Show all normal pages as tabs | N.type, T.destinationType | PAGE_NAVIGATOR_TABS; all=true/hidden=false/tooltip=false | Omit selectedPages. |
| Show a selected subset | T.selectedPages | Resolve exact eligible tab IDs | Destination flags must include desired categories. |
| Include hidden/tooltip pages | T.destinationType | Set corresponding flags true, retain all as intended | Does not bypass authorization. |
| Wrap tabs automatically | T.layoutType | auto-grid | Usable visual dimensions, scroll settings. |
| Exact row/column viewport | T.layoutType/rows/columns | grid + integers 1..30 | Gap and dimensions. |
| Collapsed sidebar | T.collapsible, T.layoutType | vertical, isEnabled=true, explicit initial isCollapsed and identifier | Full trigger config and collapse width. |
| Group pages/bookmarks | T.hierarchy | isEnabled=true, vertical, indentation | Existing external group metadata. |
| Fixed-height groups | T.hierarchy.fixedHeight | isEnabled=true + value 30..100 | Hierarchy enabled, vertical scroll. |
| Icons in collapsed navigation | T.collapsible.identifierType, S.icon | icon + enabled state maps | Resolve built-in names or uploaded data:image assets. |
| One bookmark group | T.selectedBookmarkNavigatorOption, hiddenBookmarks | Group ID and explicit out-of-group exclusion slugs | Workload bookmarks. |
| Clicking selected view returns to reset view | allowDeselection, launchOnDeselection | true + actual reset slug | Include reset slug in hiddenBookmarks if hide flag requested. |
| Apply/clear filters with one button | B.actionType | APPLY_SLICER or CLEAR_SLICER | Existing slicer behavior. |
| Drill to matching detail | B.actionType/pageDestinationId | DRILL_THROUGH + eligible page | Destination filters and live matching single data point. |
| Back from drill-through | N.isNavigationBackForDrillThu | true with PAGE_NAVIGATION and back-button style | Runtime sourceEntityId, no fabricated source ID. |
| Trigger action variable | B.actionType/variableId | VARIABLE + actual action variable ID | Variable definition, scope, PlanningParameters UI gate. |
| Different selected appearance | N.style.ACTIVE.shapeState | Partial fill/text/icon/accent overrides | DEFAULT complete; later hover/pressed precedence. |
| Different button shape | DEFAULT.shapeType and geometry | Select exact K4 UI choice; apply shape matrix | Preserve text/icon/style siblings. |

### 12.2 Deterministic Construction Sequence

1. Identify artifact format, native visual owner, target sheet, requested Navigator kind, and deployment environment. Do not start by inventing identities.
2. Obtain or create the native visual through the existing general artifact creation workflow with visualType 203 and valid host metadata.
3. For a new Navigator, call getNavigatorInitialState with explicit kind or construct the R1-equivalent baseline; for tabs use empty default text value. Preserve theme-aware initialization where available.
4. For existing artifacts load the actual properties wrapper and clone the relevant native state without discarding unrelated fields.
5. Select button action or tab source. Resolve actual entity IDs, normalized bookmark slugs, bookmark group IDs, variable IDs and icon names/assets from artifact context.
6. Set required companion targets. Clear irrelevant target fields only deliberately; runtime ignores unused targets, editor does not consistently erase them when changing action.
7. Materialize layout, positive manual grid dimensions and explicit destination flags. Omit selectedPages for all eligible tabs, not [].
8. Recompute bookmark exclusions for group selection and deselection hiding. Deduplicate and validate every slug.
9. Apply compound collapse/hierarchy edits: vertical layout, complete nested configs, consistent collapsed flag and identifier icon enablement across states.
10. Apply shape and geometry; preserve initialShapeType as original/reset metadata unless intentionally recreating the visual. Populate complete DEFAULT overlay padding and icon map.
11. Apply partial interaction styles with known merge precedence; mirror DEFAULT override-propagation rules if making editor-equivalent mutations.
12. Write D only at the visualState sibling location if needed. Keep unrelated visualState properties, sync/layer/mobile metadata and other visuals intact.
13. Validate types, enums, numeric UI ranges where applicable, required targets, dynamic map keys, URL format and context references. Do not treat source-only supported values as tested UI behaviors.
14. Serialize objects once. For live save use schema 0.0.1 wrapper and current etags; for ALM preserve the current exported $schema and part paths through the general deployment workflow.
15. Re-resolve and check all cross-environment references, including nested page targets, selectedPages, bookmark slugs, map keys and variable IDs. The inspected binding is insufficient as proof of remapping.
16. Parse final JSON, run available source/schema checks, then save/deploy only through the authorized existing workflow. Reload and verify requested interactions in the target environment before declaring deployment successful.

### 12.3 Property Selection Rules

- Explicit supported user preference wins over factory defaults; unsupported requests must be reported, not encoded as new enum values.
- Product defaults come from explicit-kind factory output and active theme, not a screenshot or dropdown's null fallback.
- Derived tab labels, dimensions, selection flags, callbacks and sourceEntityId are runtime context; do not create synthetic persisted equivalents.
- Dynamic identifiers must come from the artifact's real metadata/services. Request missing context rather than inventing GUIDs, slugs, hashes or variable IDs.
- For an ambiguous group or target, ask for a resolvable existing object. Do not choose solely by a duplicate display label.
- Do not silently adopt declaration-only tail positions, downstream-only square line caps, or the UI-excluded LINE shape for ordinary construction.

### 12.4 Safe Mutation Rules

The store reducer is shallow at N. Merge B, T, style, individual states, shapeState and nested appearance sections explicitly before dispatch. Preserve unknown fields for forward compatibility and unrelated fields for correctness. Arrays are intentional replacements, not concatenations by default; dynamic maps merge by key.

Keep visual identity, sheet membership, record GUIDs, bookmark slugs, group IDs and variable IDs stable unless the owning workflow explicitly creates/rebinds those objects. Editing labels must not rewrite ID keys. Deleting pages/bookmarks requires pruning related inclusion/exclusion/map entries with awareness of intentionally retained metadata.

Changing kind is a compound edit, not just a discriminator assignment: retain editor-compatible inactive state, initialize correct text/defaults, ensure relevant tab layout or action fields, and avoid carrying drill-through-return behavior into an unrelated Navigator.

Do not bulk-replace properties, visualState, or the plan properties file. Respect synced state ownership and optimistic concurrency etags. Avoid overwriting a newer exported schema or transport metadata with this document's illustrative save-time version.

### 12.5 Validation Checklist

- [ ] Correct visual part, native visual type 203, stable valid page/visual identity and usable dimensions.
- [ ] N is under properties.visualState, not plan-level or root navigatorState.
- [ ] Correct K1 kind, complete DEFAULT shape, complete required nested editor structures.
- [ ] Exact case and member names; no friendly AI-schema-only keys in native state.
- [ ] Every value type correct; no null arrays/style sections and no nonfinite numbers.
- [ ] Enumerations drawn from section 5 with declared/runtime discrepancies respected.
- [ ] Selected action has a resolved target; URL meets HTTPS validation.
- [ ] Page IDs, bookmark slugs, group IDs, variable IDs and icon map keys resolve in correct target scope.
- [ ] Manual grid has positive row/column counts; gaps/dimensions leave visible content.
- [ ] Page destination flags explicit; inclusion/exclusion arrays match intent.
- [ ] Bookmark group and hide-deselection settings coordinated with hiddenBookmarks.
- [ ] Collapse/hierarchy uses vertical layout; icon identifier and state icon flags coordinated.
- [ ] Geometry companions correct for selected shape; DEFAULT versus override semantics preserved.
- [ ] Custom image has valid data:image content and nonempty name; asset rendering checked separately.
- [ ] Unrelated properties, layer/mobile/sync metadata, unknown members and other visuals preserved.
- [ ] Correct live-save wrapper/etag or current exported $schema/part transport, without double serialization.
- [ ] Target-environment references checked after ALM import; no unproven remapping assumptions.
- [ ] Reload and interactions verified in target environment before claiming runtime/deployment validation.

### 12.6 Error Avoidance Rules

Never confuse activeEditStyle with runtime state, textRotation with rotation.shape, original initialShapeType with current shapeType, or bookmark slug with bookmark database ID. Never put action-variable scripts inside variableId. Never assume a UI-only group selector filters runtime tabs without its materialized exclusion array. Never copy transient tab objects into JSON. Never replace a complete nested object through a shallow update. Never describe parsing as live validation.

## 13. Compatibility, Defaults, and Limitations

### 13.1 Verified Missing/Empty/Null Semantics

| Value or boundary | Verified result |
| --- | --- |
| Missing N | NavigatorRenderer returns without rendering. |
| Missing whole T.collapsible | NavigatorTabs supplies getDefaultCollapsibleConfig. Partial object is not recursively defaulted. |
| Missing hierarchy | No hierarchy; leaf tabs flatten. |
| Missing T.destinationType | Normal page-load migration produces all=true/tooltip=false/hidden=false for page navigators. Direct un-migrated hook invocation defaults all flags false. |
| Missing selectedPages | Include all eligible tabs. |
| selectedPages=[] | Include none of the leaf tabs. |
| Missing hiddenBookmarks | Set(undefined) gives empty exclusion set; no group selector derivation. |
| Missing allowDeselection / launchOnDeselection | Hook destructuring defaults false / none for undefined only. |
| Null selectedPages | Unsafe because only undefined is treated as unfiltered. |
| Missing override state | Runtime merge uses empty object. Factory-compatible editor state should retain all four state keys. |
| Empty icon src | No built-in icon rendered; do not fabricate name. |
| Empty text value | Valid; icon-only button possible; tabs still derive labels. |
| Empty tooltip override | Service/shape hint fallbacks can apply; absence is not an unconditional tooltip-off. |
| Inactive B targets null | Factory emits null; runtime falsy guards for bookmark, URL and variable. Active page targets must resolve. |

### 13.2 Important Compatibility Details

- The factory's optional argument has a subtle asymmetry: omitted navigatorType stores type NAVIGATOR_BUTTON, but isNavigatorButton is computed before applying that fallback, so default text/shape flags follow the tabs branch. Always pass the kind explicitly; R1 represents explicit NAVIGATOR_BUTTON creation.
- Calling getDefaultShapeStyle for ROUNDED_RECTANGLE/SPEECHBUBBLE yields different radii than merely switching an existing rectangle's shapeType. The UI shape switch only changes shapeType.
- Shared native TCustomIconScale has duplicate fit and lacks fill; active options include fill. Documented as discrepancy, not silently corrected source.
- Speech-bubble native declaration includes four positions absent from selectable/downstream contract. Only eight corner-side variants are recommended.
- Legacy hiddenPages is supported by a frontend migration and older backend binding. Do not generate it for new artifacts: migration converts exclusions to selectedPages inclusions and usually deletes the legacy field. See section 13.3 for empty-page-context behavior.
- Friendly AI Navigator compiler currently supports only kind and button targets. Tab layout, collapse, hierarchy and per-state styling are outside its documented v1 field map. Native JSON supports more than that convenience schema.
- Navigator-specific migrations normalize destinationType, legacy hiddenPages and legacy icon storage; they do not fill all missing DEFAULT styles, nested padding, tab layout or action state. Generic wrapped/unwrapped compatibility is separate.
- No Navigator-specific automated frontend test file was found by filename/targeted feature search. The backend neighboring ALM tests do not establish full native schema validation.
- No universal Navigator schema validator, runtime deployment gate, or feature-wide flag was established. VARIABLE has the explicit PlanningParameters UI gate; do not generalize it to other kinds.

### 13.3 Verified Legacy Migrations

WorkloadPage.service.fetchVisuals calls ReportMigrationService.processMigration after theme processing and state parsing, supplying `entitiesStore.allEntities.map(entity => entity.id)` as pageIds. For native visual type 203, migrateNavigatorState mutates the loaded state in place. These changes are not a server-side schema guarantee and do not by themselves establish that migrated properties have been saved.

**Legacy destinationType union:** old string values `all` and `custom` become `{all:true,tooltip:false,hidden:false}`; `tooltip` becomes `{all:false,tooltip:true,hidden:false}`; `hidden` becomes `{all:false,tooltip:false,hidden:true}`. Unknown strings, missing values, null and nonobjects use the all=true default. Current object members are individually nullish-defaulted to all=true/tooltip=false/hidden=false. The migration does not coerce incorrect nonboolean nonnull member values; agents must still validate types. These four legacy string literals are a legacy input family, not a 25th recommended current enum.

The seven legacy leaf paths below are documented separately from the current-schema property count. Do not emit them in a new artifact.

| Legacy path | Type and observed default | Migration and conditional behavior | Evidence |
| --- | --- | --- | --- |
| `T.hiddenPages` | optional string array, missing treated as [] | For page tabs only: if nonempty and selectedPages undefined, resolve selectedPages as all supplied pageIds minus hiddenPages. If no pageIds are available, return without deleting hiddenPages. Otherwise delete hiddenPages, including when selectedPages already exists; current explicit selection wins. | E19/E17 |
| `T.tabIconType.<tabId>.src` | string; no whole-map default | For nonbutton Navigators, a truthy tabIconType map replaces DEFAULT.shapeState.icon.iconTypeMapping; tabIconType is deleted. | E19 |
| `T.tabIconType.<tabId>.customIcon.name` | string; no whole-map default | Legacy map copied as-is, so validate entries before construction/mutation. | E19 |
| `T.tabIconType.<tabId>.customIcon.isEnabled` | boolean; no whole-map default | Same map migration; no per-entry type coercion. | E19 |
| `S.icon.src` | string; fallback empty when migrating | For button Navigators, each style with string src or object customIcon gets a new iconTypeMapping.default. The new map replaces any preexisting map; src is deleted. | E19 |
| `S.icon.customIcon.name` | string; fallback empty when migrating | Copied into iconTypeMapping.default.customIcon.name, then legacy customIcon object deleted. | E19 |
| `S.icon.customIcon.isEnabled` | boolean; fallback false when migrating | Copied into iconTypeMapping.default.customIcon.isEnabled; legacy fields deleted. | E19 |

If legacy and modern icon storage coexist, the legacy migration can overwrite the modern map. Reconcile or migrate deliberately before applying new per-tab/state entries. The standalone BI_SHAPE migration adds newer geometry defaults, but that branch is **not** applied to Navigator style states; do not assume Navigator shapes receive those geometry repairs.

## 14. Source Code Evidence

E keys (E1, E2, ...) mark findings observed in the product implementation. The source locations behind them are not published.

## 15. Unverified or Unresolved Areas

1. No end-to-end artifact was deployed, no live target IDs were provided, and no tenant/service authorization or host-specific link behavior was tested. Examples are not certified complete deployable artifacts.
2. Full target-side schema acceptance and import-time creation metadata requirements remain governed by the existing general artifact creation/deployment workflow. The current schema URI must be obtained, not guessed.
3. Inspected V2 Navigator rewiring is not sufficient proof of nested-state page-target remapping, and does not cover current selectedPages or dynamic map/bookmark/variable references. Other rollout/legacy transport paths may differ; no blanket portability guarantee is made.
4. Tooltip service calculations and native tab tooltip forwarding differ; no browser test confirmed generated drill-through hints or disable behavior.
5. Four extra native speech-bubble tail literals, downstream square line cap and UI-excluded LINE are distinguished from recommended UI-native construction values. No runtime assertion is made for those unsupported combinations.
6. Every geometry's visual correctness, border-style fidelity, shared rotation fields and renderer-specific handling of all enable flags were not exhaustively pixel-tested. Values with only declaration/converter evidence are identified in the inventory.
7. Dynamic font/icon registry contents, available pages/bookmarks/groups/variables and security visibility depend on the target artifact/environment; there is no fixed exhaustive list.
8. `S.shortText.*`, top-level S.padding and T.tabsShortText are preserved/documented but do not supply the straightforward active rendering behavior their names suggest. No unverified abbreviation recipe is provided.
9. No application source changes are necessary or made. Only this specification is a deliverable. Validation results and coverage counts below distinguish local checks from unresolved runtime/deployment work.

### Completeness Audit Summary

The final audit revisited Navigator declarations, all factory defaults, optional shape fields, active options/converters, creation/switch code, current consumers, legacy migrations, persistence/load paths, backend rewrite registries, and matching tests. It found and incorporated the normal-load destination migration, legacy hiddenPages and icon conversion, the peer navigatorType hint, custom-icon fill type mismatch, and missing nested ALM rewiring. The current inventory includes every normalized factory leaf, with deliberately inactive/shared fields marked P rather than silently omitted. No Navigator-specific frontend test was found in the targeted test-file search. Exhaustiveness is limited to these accessible verified schemas and inspected paths; unresolved rollout, renderer and live-deployment behavior above remains explicitly outside the validation claim.
