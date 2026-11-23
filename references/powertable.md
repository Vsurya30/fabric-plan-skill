# Plan a PowerTable and inspect its definition

Use this skill for the Plan definition. For live Fabric SQL Database work,
use the sibling skill `sqldb-cli`: `az rest` calls the Fabric control plane;
`sqlcmd` runs T-SQL against the database. Before connecting, follow the Fabric
skills collection's [shared CLI setup](https://github.com/microsoft/skills-for-fabric/blob/main/common/COMMON-CLI.md)
for sign-in and workspace discovery, and its [authentication guide](https://github.com/microsoft/skills-for-fabric/blob/main/common/COMMON-CORE.md#authentication--token-acquisition)
for the token audience. A Plan repair does not authorize a database write.

**Existing table.** Start from the physical schema: database, schema, base
table, columns, types, nullability, primary key, identity/generated columns,
and approved connection identity. A display name does not prove any of those
identities. Keep generated keys read-only. Decide row insertion separately
from editability of an existing column.

**New table.** Work out the grain before designing columns. For an employee
master, decide whether a row denotes an employee or an employee assignment;
choose the stable key accordingly. Specify required/default values and unique
constraints. A local Plan definition does not run SQL DDL, provision a
connection, insert rows or grant database privileges.

**Lookup.** For `Employee.DepartmentID` referencing `Department.DepartmentID`,
store the key and display the requested label, e.g. `DepartmentName`. Require
compatible types and a unique target key. Repeated labels do not uniquely
identify rows. A lookup configuration is not a join and must not overwrite
the stored key. Preserve unrelated column metadata, editing and row actions.

```sh
python plan.py repair-powertable-config --baseline current-definition.json --input repair-request.json --out candidate
```

This produces a local candidate using supplied metadata. Compare the complete
candidate to the baseline and verify the change is confined to the intended
source/columns. A syntactically present connection ID does not prove access.

**Analyze across sheets.** Match facts to the unique master key at the fact
grain before aggregation. Count unmatched keys, nulls and duplicate masters;
a many-to-many match can multiply totals. Qualify currency and effective date
when comparing snapshots. If all you have is schema, report which joins and
checks are possible, not counts or conclusions about actual data.
