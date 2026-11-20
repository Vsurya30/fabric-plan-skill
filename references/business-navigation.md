# Business navigation and optional initial refresh

For new applications, expose native Home, Intelligence dashboards containing
their actual embedded Planning visuals, and requested PowerTables. Hide the
underlying standalone Planning sheets from ordinary navigation. Preserve their
owner identities, inputs, formulas, mappings and connected outputs. An embedded
workbench must use the same visual, not a separate copy of its inputs.

`build_application` sets Planning specs to `hidden:true`; portable declarations
therefore use `isHidden:true`. `check_application_defaults` rejects visible
Planning owners and hidden business PowerTables. Reporting pages remain staged
hidden until their native geometry/visibility phase succeeds. Every Planning
owner still needs a complete dashboard; hiding its standalone page does not
waive dashboard coverage or permit an inaccessible completed application.

Home preview cards exclude the current native owner entity IDs through
`public_home_layout`. Preserve other explicit card exclusions. Every dashboard's
Page Navigator keeps `destinationType.hidden:false`, includes normal visible
pages and uses complete padding/Arial defaults. Resolve IDs in the new target;
never copy a sample's page IDs. Hiding navigation is not a security restriction.

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
