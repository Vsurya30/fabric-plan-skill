audience: public

### Added

- **IBCS recipe charts.** Dashboard chart specs accept a recipe code (C01–C13) or a native chart template. Recipes cover stacked and 100% stacked charts, overlapped comparisons, waterfalls, line, area, scatter and bubble. Bindings are checked against each template's buckets.
- **IBCS dashboard pages.**
  - A Matrix table can take the place of the embedded Planning grid.
  - A page can carry a message title and footnotes.
  - The IBCS Plan theme is set when the request asks for it explicitly.

### Changed

- Plain dashboard column charts now save the `COLUMN_VERTICAL` template that Fabric already loads them with, so their buckets are checked against a known template.
