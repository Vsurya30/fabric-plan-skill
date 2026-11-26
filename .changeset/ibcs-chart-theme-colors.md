audience: public

### Fixed

- **IBCS charts show IBCS colors.** A chart built from a recipe code or a native chart template now saves the chart's own IBCS theme with its scenario notation: a solid dark actual, a lighter solid previous period, an outlined plan and a hatched forecast, with grey stack series and green and red variances. Before, the chart stayed on the default Customize theme, which takes its colors from the Plan theme, and showed no IBCS notation.

### Changed

- Charts built from a native chart template without a recipe code keep the IBCS chart theme too, so a stack shows greys in place of the Plan palette. Give `"theme": "plan"` to keep such a chart on the Plan theme.

### Added

- Chart specs accept `theme`: `ibcs`, the default, or `plan` to leave a chart on the Plan theme.
- `runtime.ibcs_charts.apply_chart_theme` applies the IBCS chart theme to an exported chart, and `ibcs_palette` returns its colors.
