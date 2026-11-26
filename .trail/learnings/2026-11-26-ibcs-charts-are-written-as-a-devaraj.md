---
title: IBCS charts are written as a chart template plus bucket bindings; IBCS styling is not authored through definitions
author: Devaraj
date: 2026-11-26
branch: feat/intelligence-ibcs
cost: { minutes: 1, tokens: 1804 }
id: l-0ff32146
scope: repo
status: active
src: agent
touches:
  - runtime/ibcs_charts.py
  - runtime/ibcs_report.py
  - runtime/intelligence.py
  - runtime/planning_presentation.py
  - runtime/construct.py
---

## Decided
- **Recipes are template plus bindings.** On 2026-11-26 the user asked for IBCS through public definitions only. A recipe (C01–C13) is written the way Fabric saves an added chart: the same template in `chartType` and `visualState.chartType`, plus pivot assignments in the template's buckets (axis, stack, AC/PY/PL/FC). Bucket limits come from the product's chart templates.
- **Every chart sets a template**, including the plain column chart (`COLUMN_VERTICAL`). Without one, Fabric offers only generic roles, so `axis` and `AC` bind nothing and the chart is empty.
- **The user chose these options:**
  - Set the Plan theme (`theme.type` 5) only on an explicit IBCS-theme request; the theme is Plan-wide.
  - Show IBCS tables as a Matrix (`INFORIVER`) in place of the embedded Planning grid. When no other dashboard embeds the owner, its Planning page stays visible for input.
  - Add a message title (Fabric's IBCS title sizes: 18 bold, 13 and 11px) and footnotes at the page bottom.
  - Skip the asterisk indicator, and do not repair old empty charts for now.

## Tried and ruled out
- **Per-chart AI schema slice in the definition.** The page loader never reads it back, and it needs the Plan AI assistant switch, which is off by default.
- **Theme name alone in the chart's appearance state.** A theme change recomputes many saved settings, so writing only the name gives a mixed look.
- **Flagging authored charts as new.** Nothing clears the flag, so the full theme would re-apply on every load and wipe user edits.

## Watch out
- **Docs versus product.** The IBCS recipe docs list about 20 AI-state sections and canonical measure IDs. The product implements six sections, keyed by measure display names.
- **The Plan theme does not fully restyle everything.**
  - Planning grids follow it only when the tenant enables Plan themes for Planning.
  - A chart changes only settings still at the previous theme's values, so authored charts don't fully restyle.
- **Unconfirmed from an export:**
  - the stack field's filter card;
  - PL/FC filter cards under bucket AC;
  - Matrix slicer scope.

In the code: runtime/ibcs_charts.py, runtime/ibcs_report.py, runtime/intelligence.py (chart, column_chart, dashboard, rectangles), runtime/planning_presentation.py (owner visibility, coverage), references/ibcs-charts.md.
