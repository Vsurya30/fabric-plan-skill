# PowerTable modes, SQL ownership and Plan definition

Choose the source state before planning. The bundled skill supports
**existing-table** and **from-scratch-after-DDL** Plan authoring. It does not
call the private PowerTable CoreAPI from scratch.

| Mode | SQL state | Supported route |
|---|---|---|
| Existing table | Table already exists in an authorized Fabric SQL Database | Inspect physical catalog with `sqldb-cli`, construct `creationMode: 2`, then create/update the Plan through public Fabric APIs |
| From scratch | Table must be designed and created | Model and approve DDL, execute it with the external `sqldb-cli` companion, re-inspect the committed table, then construct `creationMode: 1` and create/update the Plan through public Fabric APIs |
| Import file | Table is created by the PowerTable CoreAPI upload/batch flow | Not exposed by this skill; the observed routes are workload-internal and require a pre-existing PowerTable create-table task |
| Semantic model / template | Source is assembled by internal workload routes | Not exposed by this skill; report as unavailable rather than emulating CoreAPI calls |
| Existing-sheet analysis | Read-only data question about a saved PowerTable | Decode the Plan definition, confirm database/schema/table and column mappings, then query read-only with `sqldb-cli` |

The external `sqldb-cli` companion is the SQL Database authoring/consumption
skill: <https://github.com/gim-home/skills-for-fabric/tree/main/skills/sqldb-cli>.
Install or attach that skill separately. `fabric-plan-skill` owns the PowerTable
definition and Fabric Plan lifecycle; `sqldb-cli` owns SQL catalog inspection,
DDL, DML and read-only T-SQL. A Plan-definition request alone never authorizes a
database write.

## From-scratch workflow

1. Resolve the destination workspace, Fabric SQL Database and one explicit user
   schema. List every user schema; mark `dbo` as the default but require
   confirmation.
2. Model at most five tables with stable primary keys, required foreign keys and
   a reviewed SQL type mapping. Use `sqldb-cli` for catalog/collision checks.
3. Preview the complete table layout and obtain explicit DDL approval.
4. Use `sqldb-cli` to execute the approved transactional DDL. Roll back on SQL
   failure. Offer synthetic rows separately, only 1-100 per new table, and never
   insert them without separate inclusion in the approval.
5. Re-inspect the committed table through the authorized SQL catalog. DDL
   success is not enough; capture the actual columns, types, keys and identity
   metadata.
6. Construct the PowerTable with `configured_table(..., creation_mode=1)`.
   The generated `source.json` records origin mode 1 while referencing the
   verified physical table.
7. Create the Plan through the documented public Fabric Plan API, then read back
   the complete definition and confirm source identity, column configs and row
   actions.
8. Report partial state if SQL committed but Plan creation failed. Never rerun
   DDL merely to resume Plan creation.

For existing tables, skip DDL and use `configured_table(..., creation_mode=2)`
or the default constructor. The local `powertable-source` command accepts
`creation_mode` in its input; pass `1` only after verified from-scratch DDL and
`2` for an existing source.

## Why internal CoreAPI is not the fallback

The attached `powertable-core` implementation is evidence for the product's
private workload flow, not a public API contract. Its `CREATE_FROM_SCRATCH`
mode and create-table batch endpoints live behind workload-scoped CoreAPI
services, parent upload tasks, background workers, artifact context and
privileged database credentials. The batch worker currently accepts uploaded
Excel/CSV source tasks rather than arbitrary SQL DDL. Calling those endpoints
directly would bypass the skill's public-API boundary and the required plan,
connection and task context.

Therefore:

- do not construct or call `/CoreAPI/.../databases/create-table/...` routes;
- do not present a private workload endpoint as a supported Fabric REST API;
- do support from-scratch creation through reviewed `sqldb-cli` DDL followed by
  public Plan creation;
- keep import-file, semantic-model and template source creation documented as
  unsupported until an approved public contract or external adapter exists.

## Approvals and Forms

Approvals and Forms are source-scoped workload-service records, not Plan
definition parts. They cannot be satisfied by changing
`properties.json` or `sourceSettings.json`.

Use `plan.py powertable-service` only with an approved external profile:

```json
{
  "apiBase": "https://resolved-approved-workload-service-host",
  "allowedHosts": ["resolved-approved-workload-service-host"],
  "tokenEnvironment": "FABRIC_PLAN_POWERTABLE_TOKEN",
  "authScheme": "Bearer",
  "contextHeaders": {
    "x-ms-workload-resource-moniker": "<current Plan ID>"
  },
  "approvedExternalAdapter": true,
  "authorizedMutation": true
}
```

Resolve the runtime `sourceId` from the configured table; do not substitute the
Plan definition's `recordGuid`. The adapter's source-resolution request returns
the configured `dataSourceId`, runtime `visualId` and column catalog. Resolve
approver Graph IDs and each form field's runtime `columnConfigId` through the
authorized directory/current source context; never use display names as IDs.

```sh
python plan.py powertable-service source-resolve \
  --config service.json --input source.request.json --run run --label source

python plan.py powertable-service approval-create \
  --config service.json --input approval.request.json --run run --label approval

python plan.py powertable-service form-create \
  --config service.json --input form.request.json --run run --label form
```

Approval input:

```json
{
  "sourceId": "<runtime sourceId>",
  "approvers": [
    {"graphId": "<Microsoft Graph user ID>", "entityType": "USER"}
  ],
  "ruleType": 10,
  "multiLevelEnabled": 0,
  "approvalLevel": 1
}
```

Form input:

```json
{
  "sourceId": "<runtime sourceId>",
  "title": "New employee",
  "fields": [
    {
      "columnConfigId": "<runtime column config ID>",
      "description": "",
      "mandatory": 1,
      "defaultValue": ""
    }
  ]
}
```

The adapter writes only these exact source-scoped routes:

- `POST /v2/powertable/sources/{sourceId}/approvals/`
- `POST /v2/powertable/sources/{sourceId}/forms/`

It rejects unapproved hosts, missing mutation approval, missing runtime
identities, invalid approver entity types, and empty/non-identified form fields.
Re-read the approval/form source after the call and report the saved state
separately from Plan definition creation.

## Existing-table workflow

Use this skill for the Plan definition. For live Fabric SQL Database work,
use the sibling skill `sqldb-cli`: `az rest` calls the Fabric control plane;
`sqlcmd` runs T-SQL against the database. Before connecting, follow the external
companion's sign-in, workspace-discovery and token-audience setup. A Plan repair
does not authorize a database write.

**Existing table.** Start from the physical schema: database, schema, base
table, columns, types, nullability, primary key, identity/generated columns,
and approved connection identity. A display name does not prove any of those
identities. Keep generated keys read-only. Decide row insertion separately
from editability of an existing column.

**New table.** Work out the grain before designing columns. For an employee
master, decide whether a row denotes an employee or an employee assignment;
choose the stable key accordingly. Specify required/default values and unique
constraints. Use the external SQL companion for DDL and re-inspect the committed
catalog before constructing the Plan definition. A local Plan definition does
not itself provision a connection, grant privileges or prove SQL completion.

**Lookup.** For `Employee.DepartmentID` referencing `Department.DepartmentID`,
store the key and display the requested label, e.g. `DepartmentName`. Require
compatible types and a unique target key. Repeated labels do not uniquely
identify rows. A lookup configuration is not a join and must not overwrite
the stored key. Preserve unrelated column metadata, editing and row actions.

**Row access selection.** A configured PowerTable row action must include its
audience selection, not only `settings.enabled`. Existing-table and from-scratch
constructors use **All Users** by default: `ROW_ADD` and `ROW_UPDATE` receive one
filter named `all_users` with `filterType: 1` and `filter: {}`. `ROW_DELETE`
remains disabled and has no filter until explicitly configured. If an action is
enabled later, add a valid row-access selection before publishing; validation
rejects enabled row actions with no filters.

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
