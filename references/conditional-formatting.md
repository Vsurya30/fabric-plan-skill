# Planning conditional formatting: new reports and missing rules

Use this guide for CF, Conditional Formatting, Manage Rules, missing rules,
favorable/unfavorable variance, colored numbers, arrows, and comment flags.
The supported constructor is for numeric single-condition Planning/Matrix rules.
This is not a general Charts or PowerTable formatting contract.

## New reports: put rules in the sheet spec

`build`, `build_application`, and `provision` consume each sheet's
`conditionalFormatting` list. `target` and `test` refer to that sheet's stable
measure **keys**, including hidden helper measures. The builder resolves native
IDs after constructing the measures. Do not use display labels or copy IDs from
a reference report. Add `planning.conditional-formatting` to requiredCapabilities
when using `provision`.

```json
{
  "conditionalFormatting": [
    {
      "id": "unfavorable-variance",
      "label": "Unfavorable variance",
      "target": "variance",
      "test": "variance",
      "operator": "<",
      "threshold": 0,
      "rowScope": "both",
      "columnScope": "both",
      "excludeRowTotal": false,
      "excludeColumnTotal": false,
      "appearance": {"textColor": "#A60000", "icon": "down", "iconColor": "#A60000"}
    }
  ]
}
```

Favorable direction is a business decision: higher revenue can be favorable,
while higher cost can be unfavorable. Blank values are excluded; equality uses
`==`. Choose `parent`, `child`, or `both` independently for rows and columns.
Do not put a background in `appearance` when existing input/forecast fills must
remain. An icon-only flag uses `icon` and `iconColor` without `textColor`.

Run the self-contained two-sheet example from any working directory:

```text
python examples/conditional-formatting/build.py /absolute/output-directory
```

It uses only shipped synthetic model metadata, a normal report spec, and the
standard builder. It generates fresh identities, two Planning sheets with four
and three rules, native Home content, and two Intelligence dashboards. The
synthetic model is for offline construction, never deployment. To create a real
report, provide current model metadata and an application spec with real field
references to `plan.py build` / `provision`; no prior report or repair script is
required. See `runtime-guide.md` for authorized deployment and all save phases.

## Existing reports: scoped authoring

Use `format-matrix` / `runtime.matrix_formatting.compile_formatting` against the
current owner's `visualState`. Here `target` and `test` are resolved native
measure IDs from `manage_measures`, kept as strings. The request has a stable
`id`, label, predicate, scopes, total exclusions and appearance as above.

The compiler updates only the requested rules. Unrelated user rules, opaque
extensions, business calculations, input settings and filters survive. A
selected old business-key rule is migrated to its stable native name, rather
than left behind as a duplicate. Repeated application is idempotent. Ambiguous
legacy/current duplicates and complex selected rules require explicit
reconciliation; this helper does not silently flatten them.

## Current native representation

The default numeric-rule profile uses sanitized `fixtures/matrix-cf-v2.json`,
derived from current UI-saved rules and the repair whose panels the user
confirmed visible. It emits:

- Both `visualState.cfProps` and `visualState.jet_cfProps` for new rules.
  Updating requested rules preserves unrelated entries in each existing store.
- A target-measure-prefixed name with a deterministic suffix, `newRule: true`,
  and `null` for unrestricted row/column/member selectors. Empty arrays are not
  substituted for these null selectors.
- Resolved target, test, bubble reference and all condition measure slots,
  including inactive comparison/calculation/from/to references.
- The complete current condition/default shape and a current row-dimension
  reference when one exists. Inactive bucket values are synthetic defaults;
  they do not define the numeric predicate or imply support for ranking modes.

`mirrorCompatibilityRules: false` is an explicit legacy-profile escape hatch
for a separately established target contract. It is not the default for new
reports. Never choose it merely because an older guide says only jet is active.

The observed failure was a representation mismatch. Changing several related
fields together fixed it; no single field was proven to be the sole cause.
Do not patch only a count or add empty containers and call that a fix.

## Evidence and troubleshooting

Saved rule counts prove serialized configuration, not UI recognition. If Manage
Rules is empty, first identify the active Planning owner (not its embedded
dashboard), compare both saved stores and current measure IDs, and check the
native profile above. Preserve any user-created working examples. When UI
verification is authorized, reopen the affected owner and check its rule panel
and a representative positive/negative value. When the user skips validation,
save the full correct definition and report that UI behavior remains untested.

The prior corrected report was user-confirmed. New offline artifacts and new
deployments need their own evidence; do not inherit its runtime claim.
