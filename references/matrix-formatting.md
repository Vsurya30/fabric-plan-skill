> v25: For CF authoring and missing Manage Rules, start with [conditional-formatting.md](conditional-formatting.md). The standard new-report spec now supports conditionalFormatting; current numeric rules populate both CF stores.

> v18: [measure-display-defaults.md](measure-display-defaults.md) is the default: assigned measure cards stay visible at **All**, with no selected values/ranges. Numeric Planning measures use per-measure Auto (`13: "auto"`). Apply dimension selections only to the dimension card itself; preserve all source bindings and intentional existing filters.

> v13: Read [planning-column-presentation.md](planning-column-presentation.md) for dynamic column expansion, selected sizing/default-total rules and native-measure filter cards. Expansion recovery was user-confirmed; the other defaults were subsequently requested. Preserve all existing input and formula identities.

# Matrix formatting authoring

Use for business requests about typography, input colors, time/measure headers,
number formats, conditional indicators, widths and wrapping. This is the selected
Planning/Matrix contract; it does not apply to PowerTable, Charts or Shell styles.

## Business request to command

| Business request | Native owner / implementation |
| --- | --- |
| Make the body 10 pt and time headers dark with white text | `typography`, explicit pt-to-px conversion, then `headers` with the resolved header scopes |
| Distinguish open forecast, closed actuals and stored inputs in both modes | `columnStyles.forecastOpen/forecastClosed/custom`, explicit `read` and `edit` |
| Show favorable/unfavorable signs at detail and totals | `rules`, explicit predicate and row/column scope; text/icons without background when fills must remain |
| Flag a comment using another measure | Separate `target` comment ID and `test` helper ID; leaf rows, column scope matched to the presentation |
| Display currency, ratios and zero/blank differently | `numberFormatting` plus ordered `operations`; do not alter formulas/aggregation |
| Widen comments and keep labels readable | `sizing`, resolved IDs, width-policy warning, preserve custom heights |
| Keep values after a product changes category | `leaf-key-mapping`; read [dimension-leaf-keys.md](dimension-leaf-keys.md), not a formatting operation |

Run locally:

```text
python plan.py format-matrix --input examples/matrix-formatting.request.json --out candidate.json
```

Input has `state` (the resolved owner visualState), `request`, optional `resolved`
identity catalogs and optional previous `ledger`. Output has the candidate `state`,
operation `ledger`, per-section `coverage`, unit conversions and conflict warnings.
Keep the ledger outside the native definition. Preserve the original envelope and
other part bytes when publishing through the existing update adapter. The command
has no network or deployment side effect.

`runtime.matrix_formatting.compile_formatting` supports selected typed settings and
numeric single-condition rules. Unknown top-level requirements are reported as
unsupported/unresolved; malformed supported settings fail before producing a
candidate. General ranking, classifications, custom icons, arbitrary CSS and
arbitrary formatting owners remain outside this compiler. Do not claim a complete
natural-language compiler from this selected implementation.

A new style mode uses the bundled complete preset. A new rule uses the full bundled
native seed, with active targeting, scope and appearance set explicitly. The numeric CF seed is the sanitized current UI-derived matrix-cf-v2 profile;
other formatting defaults retain their separate source provenance. Existing records retain
unknown fields and unrelated rules, styles, operations and business settings.

New Planning construction does not place a direct background over Forecasts.
For an existing Forecast with direct fill, remove only the identified conflicting
format operation after comparing the intended scope; never clear all formatting.
`forecastMeasureIds` requests this conflict check. One unresolved cosmetic detail
must not block independent supported settings.

## Establish the correct contract and evidence boundaries

The supplied source investigation identifies Matrix revision `5b9ffe2d1256733a3ae585a648d93a8a706ed539` and Shell revision `3c5d78fb3bc6e26544ebb86ce49f25bab390c64a`. These are provenance reported by that investigation, not a checkout or deployed-build verification performed by this skill update. See `fixtures/matrix-formatting-v1.json` for the evidence record. Ordinary use requires no private checkout.

Distinguish:
- Supported authoring representation.
- Properties observed in a saved definition.
- Behavior established by inspected renderer code.
- Appearance verified in a particular deployed build.
- Unresolved or unsupported requirements.

An exported property does not establish its active ownership, and API acceptance does not prove rendering support. Absence from one export does not establish that a feature is unsupported.

Record the source revision in a versioned contract snapshot. Do not assume it matches every deployed environment.

Keep transport wrappers separate from Matrix state. For the observed Plan definition export, the visual part is:

sheets/<sheet-id>/visuals/<visual-id>/properties.json

Its styling root is:

properties.visualState

Retain the envelope required by the actual destination API. The examples below are partial objects relative to the resolved Matrix visual state.

## Implement reusable constructors and merge operations

Add or improve reusable authoring components for:
- Global typography and scoped headers.
- Forecast/input Column Styles.
- Ordered scoped-format operations.
- Complete conditional-format rules and conditions.
- Identity-based rule merging.
- Widths, row heights and wrapping.
- Structural validation and requirement coverage.

Bundle sanitized, versioned native defaults and contract metadata. Ordinary skill execution must not require private source checkouts or import private application constants directly.

For new records, construct complete required state from the appropriate versioned defaults.

For existing records:
- Deep-merge only the requested changes.
- Preserve unknown destination fields and unrelated overrides.
- Preserve business logic, input policy, permissions, filters, identities and unrelated definition parts.
- Do not replace an entire map or array with an abbreviated example.

Resolve actual destination measure, dimension, header and rendered-column identities before authoring. Preserve identifier strings exactly; never pass large decimal IDs through JavaScript Number.

## Correct typography types and units

Types are property-specific:

| Property | Authoring type |
| --- | --- |
| globalStyles.fontFamily | String |
| globalStyles.fontSize | String containing a numeric pixel value, such as "14" |
| globalStyles.headerFontSize | String, such as "14px" |
| globalStyles.headerHeight | Number |
| globalStyles.columnStyle[category][mode].fontSize | Number |
| headerLabelFormat[scope]["16"] | Number |
| formatConfig[scope][id][i].format["16"] | Number |

For the inspected Matrix body path, the renderer appends px to globalStyles.fontSize. Do not emit "14px" or "10pt" at that path.

If the business request specifies points, convert explicitly:
pixels = points × 96 / 72

Record any rounding. Do not silently interpret a point size as the same numeric pixel size.

Example typography patch:

{
  "globalStyles": {
    "fontFamily": "Segoe UI",
    "fontSize": "14",
    "fontWeight": "normal",
    "fontStyle": "normal",
    "textColor": "#212121",
    "headerFontSize": "14px",
    "headerFontColor": "#212121",
    "hierarchyfontWeight": "bold",
    "hierarchyFontStyle": "normal",
    "columnHierarchyFontWeight": "normal",
    "columnHierarchyFontStyle": "normal",
    "subTotalFontWeight": "semiBold"
  }
}

Preserve the exact spelling hierarchyfontWeight.

Font availability remains environment-dependent. A later family in a fallback stack does not establish which font rendered.

Inspect Column Style sizes and existing scoped formatting when applying a global typography change. They can override the global fallback.

## Use verified numeric format keys

Use the investigation’s schema-backed mappings:

| Key | Meaning | Type |
| --- | --- | --- |
| "1" | Bold | Boolean |
| "2" | Italics | Boolean |
| "3" | Text color | Color string |
| "4" | Font family | String |
| "5" | Background color | Color string; preserve supported no-fill semantics |
| "6" | Horizontal alignment | 1 left, 2 right, 3 center |
| "7" | Vertical alignment | 1 start, 2 end, 3 center |
| "8" | Prefix | String |
| "9" | Suffix | String |
| "10" | Percentage | Boolean |
| "11" | Decimal places | Number |
| "13" | Scaling factor | String; "none" disables scaling |
| "16" | Font size | Number |
| "17" | Indent | Number |
| "18" | Show scaling | Boolean |

Use only the subset applicable to the owning formatting surface. Header formatting does not accept every number-format operation.

The key "4" identifies font family; it is not a font-selection number.

The entry’s order is formatting-operation metadata. Applicable operations are sorted by order, and later operations can override earlier ones across scopes. Do not invent a fixed cell-over-measure precedence.

When adding operations:
- Use the actual next formatSize.
- Maintain formatSize and relevant housekeeping metadata.
- Preserve unrelated operations.
- Make repeat application idempotent.

## Configure header scopes, sizes and fills explicitly

Time-dimension headers and measure headers are different scopes.

Example partial patch:

{
  "globalStyles": {
    "headerFontColor": "#212121",
    "headerHeight": 48,
    "isHeightUpdatedManually": true
  },
  "headerLabelFormat": {
    "<year-dimension-id>": {
      "1": true,
      "3": "#FFFFFF",
      "4": "Segoe UI",
      "5": "#404E7C",
      "6": 3,
      "7": 3,
      "16": 14
    },
    "<quarter-dimension-id>": {
      "1": true,
      "3": "#FFFFFF",
      "4": "Segoe UI",
      "5": "#404E7C",
      "6": 3,
      "7": 3,
      "16": 14
    },
    "<month-dimension-id>": {
      "1": true,
      "3": "#FFFFFF",
      "4": "Segoe UI",
      "5": "#404E7C",
      "6": 3,
      "7": 3,
      "16": 14
    },
    "measureHeader": {
      "1": true,
      "3": "#FFFFFF",
      "4": "Segoe UI",
      "5": "#404E7C",
      "6": 3,
      "7": 3,
      "16": 14
    }
  },
  "columnHierarchyHeader": {
    "<year-header-id>": {
      "height": 28
    },
    "<quarter-header-id>": {
      "height": 28
    },
    "<month-header-id>": {
      "height": 28
    }
  }
}

Resolve header identities using the owning layout. Do not assume every header identifier equals its dimension identifier.

The sizes and colors are illustrative design choices.

Use:
- columnHierarchyHeader for applicable time-band heights.
- globalStyles.headerHeight for measure-header height.
- isHeightUpdatedManually when following the manual-height writer.
- Explicit scoped "16" values when precise header font sizing is requested.

Do not rely solely on headerFontSize for every header-rendering path.

Inspect conflicting cell-specific and column-hierarchy header overrides. For the inspected measure-header path, lookup proceeds through cell-specific, column-hierarchy, header-scope and global fallback formatting.

Boolean "1" supports bold/normal behavior in the inspected header paths. Do not claim exact 600-weight semibold headers or invent arbitrary fontWeight fields inside headerLabelFormat.

## Configure Forecast and input styling by category and mode

Supported Column Style categories include:
- locked
- native
- custom
- forecastOpen
- forecastClosed

Each has separate read and edit modes.

These modes follow visual/report edit mode. They do not independently establish cell editability.

Example partial merge:

{
  "globalStyles": {
    "columnStyle": {
      "forecastOpen": {
        "read": {
          "background": "#FFFFDD",
          "textColor": "#4F86D9",
          "fontSize": 14,
          "fillType": "none"
        },
        "edit": {
          "background": "#FFFFDD",
          "textColor": "#4F86D9",
          "fontSize": 14,
          "fillType": "none"
        }
      },
      "forecastClosed": {
        "read": {
          "background": "#DDDDDD",
          "textColor": "#212121",
          "fontSize": 14,
          "fillType": "none"
        },
        "edit": {
          "background": "#DDDDDD",
          "textColor": "#212121",
          "fontSize": 14,
          "fillType": "none"
        }
      },
      "custom": {
        "read": {
          "background": "#FFFFDD",
          "textColor": "#212121",
          "fontSize": 14,
          "fillType": "none"
        },
        "edit": {
          "background": "#FFFFDD",
          "textColor": "#212121",
          "fontSize": 14,
          "fillType": "none"
        }
      }
    }
  }
}

Merge into complete native category/mode objects. Preserve unrelated borders, presets and other required state.

Use a target-compatible representation for fields where the checked-in schema and UI presets differ, such as borderSides nullability.

Classify actual measure operations before choosing native/custom styling. Do not classify every formula or non-semantic measure as an editable custom input.

Do not apply a blanket direct yellow fill to an entire Forecast measure: direct formatting can hide the open/closed distinction.

Preserve locking, forecast cutoff, aggregate-total policy and permissions. Styling does not create these behaviors.

Native annotation columns and stored text inputs have different rendering paths; do not treat them as interchangeable.

## Respect actual background, hover and selection behavior

For the inspected standard body-cell path at rest:

CF background
  > direct-format background
  > category-label highlight
  > Column Style background
  > alternating-row/grid fallback

For body text:

CF text color
  > direct-format text color
  > semantic variance text color
  > Column Style/global fallback

These are scoped implementation findings, not a universal precedence order for headers, charts, hover, selection or exports.

For sign and comment-flag rules that must preserve input fills, set applyBackgroundColor=false.

Example banding configuration:

{
  "themeColors": {
    "enableRowHover": "rowAlternate",
    "rowOddColor": "#F5F5F5",
    "rowEvenColor": "#FFFFFF",
    "positiveColor": "#377D22",
    "negativeColor": "#A60000",
    "enableVarianceColor": false
  }
}

enableRowHover selects a background mode. rowAlternate does not simultaneously enable ordinary row-hover recoloring.

The inspected active hover path applies background and text colors with !important and has no Forecast/input exemption. Do not promise preservation of yellow fills or conditional text colors during that hover mode.

Selection can add backgrounds as well as borders. Do not claim a configurable blue border-only selection style from selectionBorder alone.

Report unsupported combinations explicitly. Do not manufacture a “style precedence” property.

## Build complete conditional-format rules with business-specific scope

When exact revision-matched DEFAULT_RULE_PROPERTIES and DEFAULT_CONDITION_PROPERTIES are available, snapshot and deep-copy them. The shipped v1 adapter instead uses a complete sanitized prior bundled native rule/condition seed. Its provenance explicitly distinguishes that seed from a byte-exact copy of the newer constants. Use the adapter only for its supported numeric single-condition branch; preserve current destination extension fields.

Use their complete shape. The samples below show patches, not minimum schemas.

Resolve separately:
- The formatted target.
- The tested measure or helper.
- Human-readable labels.
- Row and column scopes.
- Total exclusions.

Use stable identity when updating an existing rule and a fresh unique identity when creating one.

Example sign-rule patch:

{
  "name": "<positive-variance-rule-id>",
  "displayName": "Positive variance",
  "enabled": true,
  "ruleType": "rule",
  "highlightedMeasure": "<variance-measure-id>",
  "highlightedMeasureName": "<variance-label>",
  "basedOn": "<variance-measure-id>",
  "basedOnMeasureName": "<variance-label>",
  "ruleFor": "both",
  "columnRuleFor": "both",
  "excludeRowTotal": false,
  "excludeColumnTotal": false,
  "conditionalOperator": "or",
  "conditions": [
    {
      "name": "Variance above zero",
      "conditionType": "singleMeasure",
      "basedOn": "<variance-measure-id>",
      "valueType": "static",
      "comparisonMeasure": "<variance-measure-id>",
      "operator": ">",
      "comparisonValue": 0
    }
  ],
  "applyTextColor": true,
  "color": "#377D22",
  "applyBackgroundColor": false,
  "includeNull": false,
  "isIconPresent": true,
  "iconType": "icon",
  "icon": "up",
  "iconPosition": "left",
  "iconColor": "#377D22"
}

Complete each condition from its native defaults before merging the sample fields.

Use both row and column scope when the business request includes valid hierarchy and period rollups.

For an unfavorable negative rule, use the requested negative predicate, red color and, when requested, the confirmed "down" icon. Do not assume positive always means favorable.

Example comment-flag patch for a comment displayed at a leaf-period cell:

{
  "name": "<comment-flag-rule-id>",
  "displayName": "Comment indicator",
  "enabled": true,
  "ruleType": "rule",
  "highlightedMeasure": "<comment-measure-id>",
  "highlightedMeasureName": "<comment-label>",
  "basedOn": "<helper-flag-measure-id>",
  "basedOnMeasureName": "<helper-flag-label>",
  "ruleFor": "child",
  "columnRuleFor": "child",
  "excludeRowTotal": true,
  "excludeColumnTotal": true,
  "conditionalOperator": "or",
  "conditions": [
    {
      "name": "Helper flag is active",
      "conditionType": "singleMeasure",
      "basedOn": "<helper-flag-measure-id>",
      "valueType": "static",
      "comparisonMeasure": "<helper-flag-measure-id>",
      "operator": "==",
      "comparisonValue": 1
    }
  ],
  "applyTextColor": false,
  "applyBackgroundColor": false,
  "includeNull": false,
  "isIconPresent": true,
  "iconType": "icon",
  "icon": "flag",
  "iconPosition": "left",
  "iconColor": "#A60000"
}

Equality uses "==", not "=".

Keep base comment text independently formatted. A flag-only rule must not inherit text recoloring from defaults.

If comments are intentionally displayed in an aggregate selected-period column, resolve the appropriate column scope and total exclusions for that presentation. Retain leaf/product row scope. Do not reuse the leaf-period example unchanged.

Do not blindly rewrite dormant default role tokens. Validate references according to the active rule and condition type.

Historical inspected code used jet_cfProps. The current UI-confirmed numeric profile writes requested rules to both cfProps and jet_cfProps by default, preserving unrelated entries in each existing store. See conditional-formatting.md for the current contract and explicit legacy option.

Preserve unrelated rules. Do not enable stale built-in descriptors merely because they exist in default state.

autoFontColor and applyClassificationToCharts are not universal fixes for missing CF. Select or preserve them deliberately.

## Number formats and ordered scoped operations

Example partial number-format patch:

{
  "numberFormatting": {
    "decimalSeperator": ".",
    "thousandSeperator": ",",
    "noOfDecimal": 0,
    "noOfDecimalPercent": 1,
    "negativeValueFormat": "-x",
    "showZeroAs": "hyphen",
    "showNullAs": "blank",
    "scalingFactor": "none",
    "showScalingUnit": false,
    "semanticFormatting": false,
    "autoLocaleNumberFormat": true
  }
}

Preserve the native spelling Seperator.

`autoLocaleNumberFormat` is optional Boolean source state. The host defaults a
new visual to true only when the Planning auto-locale feature is enabled; an
existing explicit saved value remains authoritative. Do not use it as an input
parser or formula locale setting. The typed patch contract also accepts the
`"1000000000000"` scaling wire value.
The formatter accepts the remaining safe presentation members of the current
native NumberFormatting contract: unit/prefix/suffix state, sign colors/formats,
custom zero/null/error text, scaling labels, tooltip/display units and separator
precision. It intentionally rejects `enableNullAsZero`, because that setting is
calculation context rather than cosmetic number presentation. A `formatType`
mode change also derives the native precision/scaling/signature fields and removes
scoped scaling operations on the same scopes as the Matrix controller: `ibcs`
clears measure/cell/row, `flexible` clears measure, and `default` clears
cell/row; conflicting explicit values are rejected.

Zero-as-hyphen and null-as-blank are separate display choices. They do not implement blank-safe financial formulas or convert blank estimates to zero.

Example scoped operations for a newly initialized format map:

{
  "formatConfig": {
    "measure": {
      "<amount-measure-id>": [
        {
          "order": 0,
          "format": {
            "8": "$",
            "9": "",
            "11": 0,
            "13": "none"
          }
        }
      ],
      "<ratio-measure-id>": [
        {
          "order": 1,
          "format": {
            "10": true,
            "11": 1,
            "13": "none"
          }
        }
      ],
      "<comment-measure-id>": [
        {
          "order": 2,
          "format": {
            "3": "#000000",
            "6": 1
          }
        }
      ]
    },
    "formatSize": 3,
    "__lastHouseKeepedSize": 0
  }
}

This illustrates new ordered entries. For an existing destination, use its actual counters and preserve all other maps and entries.

Select currency, precision and percentage behavior from the measure’s units. Distinguish fractional ratios from percentage-point inputs. Avoid duplicate percent suffixes.

A currency prefix does not prove accounting-style alignment.

Preserve full-precision aggregation. Do not change aggregation to visible rounding to achieve display precision.

## Widths, heights, wrapping and hierarchy

Example partial sizing patch:

{
  "layoutSizes": {
    "labelWidth": 240,
    "isResponsive": false,
    "preferedWidthSelection": "measure"
  },
  "columnMeta": {
    "<resolved-label-column-id>": {
      "width": 240
    }
  },
  "measureAttributes": {
    "<amount-measure-id>": {
      "width": 120
    },
    "<percentage-measure-id>": {
      "width": 80
    },
    "<comment-measure-id>": {
      "width": 300
    }
  },
  "row_height_config": {
    "default_row_height": 26,
    "sub_total_row_height": 26
  },
  "auto_fit_options": {
    "wrapCols": true
  },
  "gridStyles": {
    "indentSpacing": 10
  }
}

These dimensions are illustrative.

row_label is an observed label-column key, not a universal identity. Resolve the destination’s actual key.

Inspect uniform-column-width policy before applying measure or rendered-column widths. In the inspected ordinary width path, uniform width wins, followed by measure width before rendered-column width; other layout branches can differ.

The active row-height owner is row_height_config. Preserve unrelated legacy globalStyles.rowHeight state, but do not require or depend on it. Native row, subtotal, level and custom-row requests use unsigned 32-bit integer heights; the bundled formatter rejects fractional `rowHeight` / `subtotalHeight` values.

Preserve custom_row_height and row_level_height. Decide explicitly whether requested total rows also need their existing custom heights updated.

Wrapping depends on column type, width, orientation, layout and relevant number-format mode. Do not change numberFormatting.formatType solely to force wrapping without checking its effects.

Do not invent per-comment autoHeight properties or promise unlimited automatic growth.

Example hierarchy presentation patch using the investigated defaults:

{
  "totals_config": {
    "row_sub_total": "Top"
  },
  "tableState": {
    "expandCollapseIcon": "plusMinusSquare",
    "columnExpandCollapseIcon": "arrows"
  }
}

Match enum values to the target contract. Do not change existing icon values merely because they differ from a default.

Row expansion and column-member expansion are separate. A global row-level array cannot implement different expansion states for individual quarters.

Preserve hierarchy bindings and identity mappings.

## Grid and Shell boundaries

Example grid patch:

{
  "gridStyles": {
    "horizontalMinorGridLines": "solid",
    "verticalMinorGridLines": "solid",
    "horizontalMinorGridColor": "#E6E6E6",
    "verticalMinorGridColor": "#E6E6E6",
    "headerGridLines": true,
    "gridBackground": "#FFFFFF"
  }
}

A line color does not enable its line. A border color with width zero does not produce a visible outer border.

Matrix grid styling, the visual container, the page canvas and Shell navigation have different owners.

Do not use Matrix globalStyles to promise Shell navigation colors, filter-card themes or selection appearance. In particular, the inspected tabColor affects the active entity icon, not a general active-tab background/text pair.

## Add structural checks and offline regression tests

Validate:
- Property-specific types and supported enums.
- Resolved IDs and safe identifier handling.
- Complete native style, rule and condition state.
- Paired header text/fill and correct header scopes.
- Required read/edit Forecast category pairs.
- No blanket direct fill hiding open/closed distinctions.
- Separate CF target and tested-measure identities.
- Row scope, column scope and total exclusions.
- Explicit icon, text-color and background behavior.
- Distinct zero/null display settings.
- Valid format ordering and counters.
- Width policy and custom-height preservation.
- Identity-based merges without duplicate rules or operations.
- Preservation of unrelated state.

Use synthetic offline cases for:
- Negative, zero, positive and missing values.
- Threshold boundaries.
- Leaf rows, subtotals and period rollups.
- Open/closed, read/edit and locked categories.
- Existing direct-format and width overrides.
- Repeated application of the same update.

Do not hard-code a particular scenario’s thresholds, sheet names or rule counts into generic constructors. Derive expected coverage from the supplied business specification.

Static checks validate construction and saved shapes; they do not certify grid pixels or financial results.


## Evidence and coverage reporting

The command reports configured state separately from rendering. Record each
business clause as supported-and-configured, supported-approximation (state the
chosen alternative), or unsupported-or-unresolved. Every configured or approximated
clause remains rendering-not-yet-verified until observed in the actual build.
No automatic approximation is applied by the compiler. Exact semibold headers,
semantic-preserving hover, custom blue border-only selection, accounting alignment,
unlimited per-comment auto-height and Shell tab colors must not be promised from
these Matrix fields. A font fallback does not establish which font rendered.

The formatter is not a financial evaluator. Offline sign/threshold fixtures test
predicates and serialized scopes, not native calculation or pixels. Respect requests
to omit live value, propagation, writeback, refresh or rendering tests. API completion
and any explicitly requested readback remain separate acceptance levels.

## Planning integrity checks (v8)

Read [planning-integrity.md](planning-integrity.md). Missing known GlobalStyles
defaults are completed by build/format-matrix, and grouping field references use
canonical model names across assignments, filters and lookup metadata. Run
`check-planning-properties` before saving or `repair-planning-properties` to produce
an explicit candidate. Bundled Plan/property-batch writes reject violations.
These are offline checks; they do not require report runtime validation.

## Required presentation defaults (v9)

Read [planning-presentation.md](planning-presentation.md). Normal application builds
require rich Intelligence dashboards above their embedded Planning grids. The
complete native TEXT header writer and semantic measure palette are executable
through present-planning; build/provision apply new-application defaults. Use
check-application-presentation for offline coverage. These defaults preserve the
v8 integrity checks and all prior Forecast, formatting, From Sheets and storage fixes.
Explicit requests to skip runtime validation still take precedence; use the
verified identity/ETag reads and save-only placement options described there.
