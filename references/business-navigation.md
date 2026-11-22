# Business navigation and optional initial refresh

For new applications, expose native Home, Intelligence dashboards containing
their actual embedded Planning visuals, and requested PowerTables. Hide the
underlying standalone Planning sheets from ordinary navigation. Preserve their
owner identities, inputs, formulas, mappings and connected outputs. An embedded
workbench must use the same visual, not a separate copy of its inputs.

Match each visible Intelligence dashboard’s embedded Planning visual to the owner by `visualId`. Set the matched owner’s `sheets[].isHidden` to `true` in the initial public create definition. A standalone sheet without a visible embed stays visible by default. Keep the dashboard and business PowerTables visible. The public create contains dashboard alignment. Only Home layout uses the workload API.

For example, when Estimate Input and Net Sales Variance each have an embedded workbench, Explorer and Home should offer the two dashboards. The variance sheet can still consume Estimate Input through From Sheets because the original owners and visuals remain in the definition. A Home card for each activity should open its dashboard. Preserve these flags during formatting, cross-sheet linking, Home setup and subsequent exports or imports.

Home preview cards can exclude owner entity IDs when a public destination response establishes them. Do not query the native entity catalog or reuse exclusions from a different Plan. A Page Navigator uses `destinationType.hidden:false` to show visible pages.

Initial InfoBridge refresh is optional for deployment. Users may save the
application and refresh connected planning data manually. Validate the saved
wiring: source owners, selected fields and types, transformation dependencies,
current query identities, semantic dimension/context mappings and every consumer
binding. A pending or failed initial refresh alone must not block a correctly
wired application, omit its dashboards, or trigger a storage-mode change.

Missing or unsupported consumer binding contracts remain configuration gaps;
they cannot be excused by skipping refresh. Keep refresh state, materialized
values and edit-to-P&L propagation separate from saved-definition evidence.
Report those checks as not run or deferred when skipped; never claim they passed.
Explain the user sequence: enter drivers, save, refresh connected planning data,
then review the outlook. Do not claim instant propagation without evidence.
