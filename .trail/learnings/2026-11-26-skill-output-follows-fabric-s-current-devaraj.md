---
title: "Skill output follows Fabric's current product behavior for aggregations, lookups, slicers, headers and PowerTable defaults"
author: Devaraj
date: 2026-11-26
branch: main
cost: { minutes: 1, tokens: 2831 }
id: l-19134b9e
scope: repo
status: active
src: agent
touches:
  - runtime/identity.py
  - runtime/semantic_values.py
  - runtime/table_columns.py
  - runtime/intelligence.py
  - runtime/header_sizing.py
  - runtime/planning_presentation.py
  - runtime/planning_integrity.py
  - runtime/measure_bindings.py
  - runtime/powertable_features.py
  - runtime/planning_features.py
---

## Decided
- On 2026-11-26 the user had every fixture and reference checked against Fabric's product source and asked for every finding to be fixed. Where product behavior and the Learn article differ, the skill follows the product, and the references say so.
- Pivot aggregations use the product names: sum, average, minimum, maximum, count. min, max and avg are input aliases only. The Planning engine treats the short names as no aggregation, and IDs prefix the upper-cased name (MINIMUM__, MAXIMUM__, AVERAGE__). InfoBridge query steps keep the short names, because that layer uses them.
- In a PowerTable lookup hop, `id` is the lookup table's key and `linkingColumn` is the preceding table's column.
- Slicers: a tree turns facet mode off; a dropdown turns facet mode on with facetViewType dropdown. Column-chart categories use the `axis` bucket.
- Header sizes go on spans. Fabric's title CSS zeroes paragraph margins and can override a paragraph's font-size.
- A null or missing Column Style mode means no style. Only present modes are completed.
- PowerTable defaults match Fabric's create-table flow (the user chose "Match the product"). A NOT NULL or key column is mandatory. float shows 1 decimal and the other decimal types 2. Date time has no time zone. Forms show the logo and allow multiple entries.
- SQL types follow the server-side mapper: money is Decimal, datetimeoffset is Date time, other types are Text, and timestamp/rowversion have no default.

## Tried and ruled out
- The create-table front-end fallback for SQL types. Its groups come from the server at runtime, and the server's mapper differs for money and time.

## Watch out
- Many fixtures, tests and runtime files use CRLF. Python text-mode writes and some editors convert the whole file, so edit those files at byte level.
- Anchor hashing under an active Pivot view is unchanged. The product may hash the base axes; that is unconfirmed.

In the code: runtime/identity.py (product_aggregation, Registry.semantic), runtime/table_columns.py (column_config, default_kind), runtime/intelligence.py (slicer, column_chart), runtime/header_sizing.py, runtime/planning_integrity.py (complete_styles), runtime/measure_bindings.py (sheet_column_id), runtime/powertable_features.py (approval_record, form_record), runtime/planning_features.py (destination_form).
