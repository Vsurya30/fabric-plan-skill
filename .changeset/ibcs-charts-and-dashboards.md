audience: public

### Added

- **IBCS recipe charts.** Dashboard chart specs accept a recipe code (C01–C13) or a native chart template. Recipes cover stacked and 100% stacked charts, overlapped comparisons, waterfalls, line, area, scatter and bubble. Bindings are checked against each template's buckets.
- **IBCS dashboard pages.**
  - A Matrix table can take the place of the embedded Planning grid.
  - A page can carry a message title and footnotes.
  - The IBCS Plan theme is set when the request asks for it explicitly.

### Fixed

- Plain dashboard column charts now set the `COLUMN_VERTICAL` template. Without a template, their category and value bound to no chart role, so the chart rendered empty.
