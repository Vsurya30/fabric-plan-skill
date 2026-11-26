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
- A writeback destination must be in the form Fabric exports: tableName, a settings object, and connectionId or connectionIdVariable, copied as given. settingsHash can be absent; that is reported as schema-conflict, not an error. The article's connectionId/databaseId form was dropped on 2026-11-26 because Fabric SQL-backed Plans reject a destination without settings on import, and the import never reads the schema's portable `connection`.
- Fabric exports writeback.json for every Planning visual. The user chose to keep refusing an existing one, so the writeback constructor only works on a definition without one, such as a newly built Planning sheet.
- The current Fabric import neither reads nor exports scenarios.json. The user chose to keep the scenarios constructor and have it warn that the scenarios have no effect after publishing.
- The approval workflow is one nested `approvals` record. Fabric's import reads either the nested record or the top-level members, and its export writes the nested record. The article's top-level layout is reported, not followed. Each record carries `approvalLevel`, the number of levels, as Fabric's own workflow API stores it: multi-level approval finishes only when a request reaches that level. A LOOKUP rule needs `lookup_config` (tableName, approverColumn, conditionalColumn pairs), stored as settings.lookupConfig. A public-API review on 2026-11-26 found that no public source (article, schema, structure manifest or export fixture) shows this nesting, and the article requires a top-level `ruleType`. The user chose to keep the nested layout anyway, so don't re-flag it as a defect; it stays a reported deviation.
- The approval multi-level flag is optional. `multiLevelEnabled` is written only when the request states `multi_level_enabled`, and is never derived from the number of levels. The same review removed the old level-count rule because no public source states it. Making the flag required was tried and reverted, so saved requests without it keep working.
- New cube records link by recordGuid in the `_RefId` members, so no numeric service ID is ever invented.
- The constructors append and never rebuild: an existing writeback or approval part is refused.

## Tried and ruled out
- Checking new cube measure configs against the published cube schema unchanged: its oneOf for data_type and dataType matches the documented Number and Text twice, so they always fail. The schema view now treats them as a reviewed deviation.
- Pinning the Scenarios and ModelTemplate schemas in this change: the user deferred it to a separate reviewed change, so those parts report schema-gap.

## Watch out
- The Scenarios `$schema` constant is all lower case (planning/scenarios); a capitalized URI fails it. The ModelTemplate schema fetches only from the GitHub path Planning/modelTemplate, so its manifest entry under the `$id` casing returns 404.
- `trail check` stages every changed file as a side effect. When nobody asked for staging, unstage your own paths with `git restore --staged`.

In the code: `runtime/planning_features.py` (writeback_config, inserted_row, scenario_record, row_template, add_planning_features), `runtime/cube_part.py` (cube_records, add_cube_part), `runtime/powertable_features.py` (approval_record), the cube branch of `public_schema_view` in `runtime/validate.py`, `scoped_candidate` in `runtime/codec.py`, the `planning-features` and `cube-part` commands in `plan.py`, and the DEFINITION-CONTRACTS module in `catalog/module-routing.json`.
