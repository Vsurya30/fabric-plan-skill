---
title: "Decomposition and organization trees are built the way Fabric's Elements pane adds them; tenant switches decide whether they show"
author: Devaraj
date: 2026-11-26
branch: main
cost: { minutes: 39, tokens: 432096 }
id: l-5ecc3aac
scope: repo
status: active
src: agent
touches:
  - runtime/tree_visuals.py
  - runtime/intelligence.py
  - runtime/planning_presentation.py
  - references/intelligence-visual-types.md
---

## Decided
- On 2026-11-26 the user hit the skill's "trees are identification only" refusal and asked for tree creation.
- **What a tree is written as.** The Elements pane writes a tree as visual type 25, declared `TREE`, with `DECOMPOSITION_TREE` or `ORGANIZATION_TREE` in both chartType selectors. Its roles are `rows` (levels) and `ameasure`. An organization tree adds `parentid` (max one), `fieldid` (node fields) and `columns` (sparkline).
- **Trees go in a chart slot.** A dashboard chart spec with `tree` builds one.
- **Nothing beyond the add path is written.** No layout, node configuration or filter cards, and no slicer seeding: the tree derives those on load, or they have not been observed for trees.

## Tried and ruled out
- **The old gap reason.** The gap said the tree type number was an unverified numeric domain. That no longer holds: the host enum has TREE = 25, and the backend import and export map the `TREE` name and 25 to each other. The gap entry is removed.

## Watch out
- **The page loader drops a tree when its tenant switch is off.** There is one switch per tree type; the client fallback for both is off. A readback cannot prove the tree shows.
- **Without the parent-data mapping switch, `parentid` is lost for good.** The Matrix host removes the assignment on first render and saves the change.
- **The build reports these switches.** `tree_requirements()` puts them under `treeRequirements` in the dashboard identity.
- **Analytics+ has its own type-50 `DECOMPOSITION_TREE` chart.** `classify_visual` now reports `engine` so the two are not confused.
- **Row and measure trees are not offered** by Fabric's editor and stay recognition-only.

In the code: runtime/tree_visuals.py, runtime/intelligence.py (chart dispatcher, dashboard TREE slot, classify_visual engine), runtime/planning_presentation.py (tree counts as the page chart), references/intelligence-visual-types.md.
