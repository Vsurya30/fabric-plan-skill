# Discover physical SQL schema without a separate SQL sign-in

When a user supplies a Fabric SQL database for PowerTable maintenance, try the
authorized SQL database definition API before requesting an Azure SQL token.
`runtime.sql_definition.read_sql_project` uses the existing Fabric client (base
ending in `/v1`) and the explicit workspace/database IDs with
`POST /workspaces/{workspace}/sqlDatabases/{database}/getDefinition?format=sqlproj`.
It follows the normal long-running operation and decodes the SQL project parts.
This is read-only metadata export; never deploy the returned DDL.

The current target's exported `CREATE TABLE` scripts proved its physical columns,
primary keys, identity flags, types, nullability, unique and foreign-key constraints.
`physical_table` parses the captured ordinary column syntax conservatively.
Inspect the original constraints too; do not infer unknown columns or identities
from semantic-model labels. Use this metadata with `column_config` and
`configured_table`, then verify native PowerTable table/schema in its actual
visual/source context. Metadata export does not prove SQL credential delegation,
rendering, lookups or row-save access.

The API requires database read/write permissions even though this operation
exports metadata. On a denied/unsupported result, retain the exact failure and
continue independent work; do not invent a schema or create another connection.
Source: [Microsoft SQL database definition API](https://learn.microsoft.com/en-us/rest/api/fabric/sqldatabase/items/get-sql-database-definition)
and [SQL project definition format](https://learn.microsoft.com/en-us/rest/api/fabric/articles/item-management/definitions/sql-database-definition).
