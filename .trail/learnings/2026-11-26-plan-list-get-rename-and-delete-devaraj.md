---
title: "Plan list, get, rename and delete are public commands, and delete is double-confirmed"
author: Devaraj
date: 2026-11-26
branch: main
cost: { minutes: 56, tokens: 698607 }
id: l-2b1da13b
scope: repo
status: active
src: agent
touches:
  - SKILL.md
  - catalog/module-routing.json
  - references/definition-part-contracts.md
  - references/definition-part-layout.md
  - references/plan-rest-api.md
  - runtime/codec.py
  - runtime/transport.py
  - tests/test_runtime.py
  - tests/test_plan_items.py
  - tests/test_discovery.py
---

## Decided
- The package now runs all seven public Plan operations. `api list`, `api get`, `api rename` and `api delete` were added on the user's decision after comparing this skill with the community fabric-planning-skill. This reverses the earlier rule that public commands were only export, create and update; the allowed list lives in `tests/test_discovery.py` (`test_catalog_exposes_only_local_or_public_operations`).
- `api delete` requires three agreeing facts: `confirmDeletePlanId` equal to `planId`, `name` equal to the Plan's live display name (read by a GET before deleting), and `authorizedMutation`. Deleting the wrong Plan by a mistyped ID is the risk this guards against.
- After deleting, the command reads the Plan again and records `verifiedAbsent`: true only for a 404 whose error code is `ItemNotFound`, false if it is still returned, null for any other outcome (another 404 code such as a missing workspace does not prove the Plan is gone). `HttpError` keeps the response body for this. A failed check never turns a successful delete into an error.
- A resumed delete (same run and label) skips the name pre-check, because the Plan may already be gone; the journal replays the recorded DELETE instead of sending another.
- Applying `.platform` metadata through the generic item update with `updateMetadata` is still not run here.

## Watch out
- `plan.py` and `tests/test_runtime.py` have mixed CRLF and LF line endings. Editors that normalize endings turn a few changed lines into a diff of dozens of lines. Make byte-preserving edits there, or restore the untouched lines from `git show HEAD:<path>`.

In the code: `runtime/transport.py` `plan_operation`; the `api` dispatch in `plan.py`; the PLAN-ITEMS module and the list/get/rename/delete actions in `catalog/module-routing.json`; `tests/test_plan_items.py`.
