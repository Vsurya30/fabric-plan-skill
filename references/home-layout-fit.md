# Native Home: readable content and layout sizing

Use this when preparing Home content for a new or existing Plan. Native Home rows are separate from Intelligence dashboard rectangles, visual grid coordinates and HTML/CSS. Preserve existing rich-text, role and asset content. Role-specific Home content has no public publication route in this package: prepare and check it locally, publish only Home visibility in the definition, and report the content as not published.

## Authoring defaults

- Make Home a short, readable introduction and navigation surface: one clear title, a concise purpose statement, brief business assumptions if useful, then the available-sheet cards. Keep technical validation status in the delivery notes unless it helps a reader make a business decision.
- **Numeric `rows[].widths` values are pixel sizes, not percentages or grid spans.** `[60,40]` creates tiny fixed blocks; it does not make a 60/40 composition. Use `[null]` for a full-width block and `[null,null]` for two flexible blocks with verified available space. Do not invent CSS strings, a percentage mode, `fontSize`, `minWidth` or other unsupported native properties.
- Default prose, title/banner text and sheet-card rows to `height:null`, `defaultHeightRatio:null`, without `isHeightManual:true`. Fixed text heights can clip wrapped text and large fixed heights create blank space. Do not use one sample's 120/160/260 heights as defaults. Image-only sizing can be deliberate and separate.
- When the available Home content width is unknown, put prose blocks in separate full-width rows. A large monitor does not establish the content width: account for the explorer, editor/side panels, padding and zoom. Side-by-side text is appropriate only when each block has enough space; fall back to stacking rather than shrinking the font or breaking words.
- Align left edges and headings, use consistent gutters and paragraph spacing, keep titles short, and allow descriptions to wrap at normal word boundaries. Check the longest title, formula and description. Avoid manually inserted line breaks solely to fit one viewport.

## Bundled construction and checks

`runtime.home_fit.readable_home_layout(items, rows=None, content_width_px=None)` is the preferred constructor for **new** native Home content. It keeps text and cards flexible and content-sized, stacks text when width is unknown or narrow, and permits two text columns when the supplied content width provides room for 320px per block plus a 24px gutter. These are conservative authoring heuristics, not platform constraints or measured font metrics. `content_width_px` is helper input only, not a property to write into native Home JSON. `workflow.compile_home` uses this constructor automatically; its optional spec input is `contentWidthPx`.

```python
from runtime.surfaces import home_item
from runtime.home_fit import readable_home_layout, audit_home_fit

items = [
    home_item('text', 'Sales forecast', 'Review sales by region and product, then update the monthly forecast.'),
    home_item('text', 'Forecast assumptions', 'Closed periods use actual sales. Open months start from the previous month multiplied by 1.1.'),
    home_item('preview-cards', columns=3),
]
layout = readable_home_layout(items)
report = audit_home_fit(layout)
assert report['passed'] and not report['issues']
```

The low-level `surfaces.home_layout` rejects explicit text widths below the 240px authoring floor. It also rejects nonfinite or invalid dimension values. `audit_home_fit` reports fixed-text-height and unknown-width risks, and can detect row overflow or a narrow flexible remainder when given an available content width. Passing these static checks is **not rendered acceptance**. An intentionally fixed-height existing design needs actual wrapping/fit evidence; do not silently rewrite it just to silence a warning.

## Existing Home content

Role-specific Home content and its metadata have no public read or write route in
this package. A Plan export with empty `homeLayout.roles` does not establish that
the Home page is empty; never guess a service host.

1. Work from Home content the user supplies. Keep a lossless snapshot. Inspect row widths, height, `defaultHeightRatio` and `isHeightManual` alongside decoded text length. Preserve item/instance identities, rich text, image references, role priorities, sheet-card exclusions and unrelated configuration.
2. Correct only the affected geometry. For a narrow-text failure, use flexible widths and content-sized height; stack the two prose items if the target content width is unknown. Preserve the first row identity and allocate a new row identity only if splitting a row. Do not rebuild unrelated report content or change financial measures.
3. Run `audit_home_fit` on the candidate and return it as a prepared change with its checks. Do not report it as saved: publishing role content has no public route here. Home visibility is checked separately in an export.
4. Once the content is published outside this package, inspect it in ordinary reading mode and the Home editor when that validation is available and authorized. Require no character-by-character wrapping, clipping, overlap, excessive empty row space or unreadable text at the target viewport. If working API-only, report saved/static checks separately and leave rendered acceptance explicitly unverified. Do not claim the JSON alone guarantees appearance in every viewport.

## Evidence boundary

Synthetic layout fixtures cover prose wrapping, `widths:[60,40]`,
`height:160`, manual row heights and the related clipping risk. The regression
suite carries no customer IDs, tokens or report content.
