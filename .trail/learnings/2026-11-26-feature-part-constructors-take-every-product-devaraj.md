---
title: "Feature-part constructors take every product value from the request, with no defaults"
author: Devaraj
date: 2026-11-26
branch: main
cost: { minutes: 44, tokens: 690690 }
id: l-18add217
scope: repo
status: active
src: agent
touches:
  - SKILL.md
  - catalog/module-routing.json
  - plan.py
  - references/definition-part-contracts.md
  - references/powertable.md
  - runtime/codec.py
  - runtime/cube_part.py
  - runtime/planning_features.py
  - runtime/powertable_features.py
  - runtime/validate.py
---

## Decided
- The writeback, inserted-row, scenario, row-template, approval and cube constructors apply no product defaults. When asked, the user chose to keep every product value required: writeback layout, scenario status and first scenario order, approval rule type, persist flag and filter order, cube partition measure type, the five template-row flags, and the text for a missing parent or previous template row. Adding any default needs the user's approval first; never infer one from the schemas or the article.
- A writeback destination is copied as given, in either documented form, because exports lack the schema-required settingsHash and the service computes it. The published-schema form passes the pinned schema; the article's connectionId/databaseId form is kept and reported as schema-conflict.
- The approval workflow is one nested `approvals` record, because the import reads approvalLevels and approvalFilter there. The article's top-level layout is reported, not followed.
- New cube records link by recordGuid in the `_RefId` members, so no numeric service ID is ever invented.
- The constructors append and never rebuild: an existing writeback or approval part is refused.

## Tried and ruled out
- Checking new cube measure configs against the published cube schema unchanged: its oneOf for data_type and dataType matches the documented Number and Text twice, so they always fail. The schema view now treats them as a reviewed deviation.
- Pinning the Scenarios and ModelTemplate schemas in this change: the user deferred it to a separate reviewed change, so those parts report schema-gap.

## Watch out
- The Scenarios `$schema` constant is all lower case (planning/scenarios); a capitalized URI fails it. The ModelTemplate schema fetches only from the GitHub path Planning/modelTemplate, so its manifest entry under the `$id` casing returns 404.
- `trail check` stages every changed file as a side effect. When nobody asked for staging, unstage your own paths with `git restore --staged`.

In the code: `runtime/planning_features.py` (writeback_config, inserted_row, scenario_record, row_template, add_planning_features), `runtime/cube_part.py` (cube_records, add_cube_part), `runtime/powertable_features.py` (approval_record), the cube branch of `public_schema_view` in `runtime/validate.py`, `scoped_candidate` in `runtime/codec.py`, the `planning-features` and `cube-part` commands in `plan.py`, and the DEFINITION-CONTRACTS module in `catalog/module-routing.json`.
