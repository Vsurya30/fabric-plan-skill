# Content-sized headers and hierarchy icons

These user-approved defaults apply to every new applicable report, regardless of
business use case. They are not roll-forward-only rules. Keep all previous
presentation, input, calculation, source-identity, expansion and totals defaults.

Search terms: header fit, clipped title, truncated description, whitespace,
content-based height, dynamic header, buffer, row icon, column icon, gmate.
Use `python plan.py discover --module REPORT-PRESENTATION`.

## Content determines the saved header height

For a rich-text report introduction, size the title, complete business description
and color legend together. Do not truncate or shorten the business meaning to fit
a preset box. Do not use a universal 150/180/220/244-pixel minimum. The five approved
roll-forward examples needed 100 or 120 pixels; those results are not defaults.

1. Read the current HTML paragraphs and their font sizes. Preserve title emphasis,
   description, legend, colors, text element identity and existing non-height state.
2. Resolve the current header width from the visual, text element and canvas. Use
   their minimum, subtracting 32 pixels for horizontal allowance. An explicitly
   known narrower available width can be supplied as an authoring input.
3. Measure the text in Arial, including bold runs, and wrap by words to the usable
   width. Account for explicit line breaks and long unbroken tokens.
4. Sum each paragraph's wrapped lines × font size × 1.2, then add its explicit
   vertical paragraph margins. This matches the normal line-height assumption of
   the generated paragraph-based header; custom typography needs its own sizing.
5. Add `max(8px, ceil(contentHeight × 0.08))` as a small buffer.
6. Round up to the native 10-pixel canvas grid and synchronize all four heights.

| Native path under `visualState.chartCustomTitle` | Stored value |
| --- | --- |
| `customTitleHeight` | Numeric total height in pixels |
| `customTitle.containerMeta.height` | Same numeric height |
| `customTitle.elements[0].dimension.height` | Same height as a string |
| `customTitle.elements[0].layout.h` | Height divided by 10 |

The outer `customTitleHeight` is required: sizing only the inner text/canvas can
leave the normal sheet view clipped even when the header editor shows all text.
Conversely, a large outer value leaves an empty gap above the grid. Keep the four
heights consistent; do not add the buffer again at each nested level.

`runtime.header_sizing.calculate_header_height` calculates the size.
`fit_header` creates a size-only candidate for a single native TEXT description.
`runtime.planning_presentation.header_properties` calls it for every newly authored
Planning header; all business recipes that use the constructor inherit it.

Windows uses GDI Arial glyph widths at 4x precision. Other platforms use the
bundled `arial-header-metrics.json`, with exact captured size tables for the
standard 13/14/22px runs and a scaled table for other sizes. The portable fallback
is an authoring estimate; complex scripts and custom fonts need appropriate font
measurement. No Windows API, external font file, prior report or chat is required
for the fallback.

```text
python plan.py fit-planning-header --input header-fit.request.json --out candidate.json
```

Input: `{"properties": <current native Planning properties>, "available_width": 1000}`.
`available_width` is optional and is not written as a new native property.
Output: `{"properties": <updated properties>, "sizing": <calculation details>}`.
Save only `properties` using the supported visual-property writer and fresh ETags.
See `examples/header-fit.request.json` for a synthetic local candidate.

This is dynamic **content-dependent authoring**, not browser runtime auto-resize.
Recompute when generating or editing the header content, font size or intended
width. A saved numeric height cannot guarantee fit at every future window width.
Do not invent an `autoHeight` field, serialize `"auto"` into numeric dimensions,
or inject scripts. Composite image/chart headers and Intelligence BI_TEXT use
their own layout contracts; transfer the content-plus-buffer principle without
copying these Matrix-specific JSON paths into a different visual family.

## gmate is the universal row and column icon default

Every new report with the native Matrix/Planning hierarchy contract uses:

```json
{
  "visualState": {
    "tableState": {
      "expandCollapseIcon": "gmate",
      "columnExpandCollapseIcon": "gmate"
    }
  }
}
```

The stored value is lower-case `gmate`. UI enum/display labels such as Gmate are
not the serialized value. Apply both keys regardless of domain, time grain,
whether measures appear in rows, or whether the report is a roll-forward.
Icon appearance is separate from hierarchy expansion, visibility, totals and
measure grouping. Preserve those other settings and their current IDs.

The new Planning constructor calls `apply_hierarchy_icons`. Missing keys receive
the defaults; an explicit user-authored icon choice is preserved. For an explicit
request to reset an existing report to the standard, pass `reset: true`:

```text
python plan.py planning-hierarchy-icons --input hierarchy-icons.request.json --out candidate.json
```

Input: `{"properties": <current native properties>, "reset": true}`.
Output is the updated properties object. See
`examples/hierarchy-icons.request.json`. Existing reports are not bulk-modified
merely because a new skill default exists. Use these keys only in visual families
that expose this native hierarchy contract.

## Evidence and current release boundary

The exact icon values came from a sanitized reference fixture and were applied to
the five roll-forward reports. The user approved the subsequent content-sized
header trial and explicitly requested both rules as universal skill defaults.
This approval is evidence for the observed trial, not a runtime check of every
future report. The v20 packaging task did not run tests, validation or live APIs,
as requested. Header sizing and icons alter presentation only; formulas, input
permissions, storage/source mappings and user edits remain independent.
