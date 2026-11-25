# Native chart typography completion

Creation path: `runtime.usecases.finish_native` invokes
`runtime.application_typography.finish_native_typography(client)` after native
chart bindings and before publication. For explicit new-application composition,
invoke that same bundled phase after your last chart update. It performs fresh
reads on every run and skips unchanged visuals. It never clones embedded inputs.

The source of the issue is service-expanded `hiddenProperties_!!!_*` JSON,
including appearance, axes and secondary visual styles. These are documented
serialized style boundaries. `normalize_arial` handles their existing font keys,
rich-text CSS and matrix font overrides without interpreting arbitrary strings.
Unknown formulas, field assignments and data remain unchanged. Save uses current
visual/entity ETags; fresh readback must match. A successful write alone is not
enough. This checks saved styling, not UI rendering.

For an unrelated existing-report repair, retain intentional typography. The phase
is for new application defaults or an expressly requested font change.
