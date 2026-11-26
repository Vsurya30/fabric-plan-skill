audience: public

### Added

- **C11 Related Driver Panels.** The recipe catalog now has C11: one line panel for each driver, all on the same axis field. The guide lists how the C01–C13 and T01–T04 template pages are composed.

### Fixed

- The native stacked area accepts only an actual and a forecast, as the template does. A previous-year or plan value on it was bound to a bucket the template lacks.
- Long-running operations complete in tenants that return a regional host for the operation address. The transport polls the public operation address for the same operation ID, and still never sends the token to another host.
