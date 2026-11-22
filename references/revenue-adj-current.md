# Revenue adjustment example

> Sanitized reference. This document contains only reusable application
> structure and validation guidance. The raw Plan export, environment-specific
> identities, artifact URLs and record IDs are not distributed.

## Business pattern

Build a revenue-adjustment Planning application with one Planning owner and one
Intelligence dashboard.

The Planning owner uses:

- A geographic dimension in Rows, such as Country.
- A chronological hierarchy in Columns, such as Year, Quarter and Month.
- A read-only semantic revenue measure.
- An editable numeric adjustment measure.
- A formula measure that compares the adjusted amount with the original amount.

A conservative measure contract is:

| Measure | Kind | Behavior |
| --- | --- | --- |
| Gross Revenue | Semantic/native | Read-only source amount |
| Revenue Adjustment | Number DataInput | Editable, initialized from the source amount, with parent-to-child distribution enabled |
| Revenue Variance | Formula | Revenue Adjustment minus Gross Revenue |

Resolve source fields and measure identities from the current semantic model.
Do not copy identifiers from another Plan or from this example.

## Planning presentation

- Keep the Country field on Rows.
- Keep the time hierarchy on Columns in parent-to-child order.
- Use Arial and explicit numeric display formatting.
- Keep each assigned source/measure card visible at its unrestricted state.
- Preserve row and column grand totals.
- Keep calculation input IDs, registry IDs and formula references stable.
- Keep header, dimension, formatting and total state separate from the source
  measure binding.

## Dashboard composition

The example's dashboard pattern is:

1. A title and concise instruction block.
2. A supporting text block explaining the three measure roles.
3. Four ordinary slicers for the geographic and calendar fields.
4. A category chart showing source revenue by geography.
5. One embedded reference to the Planning owner.
6. A visible horizontal Page Navigator covering the current visible pages.

Every chart and slicer assignment needs its own ordinary visible filter card.
Numeric measure filters retain unrestricted `null` min/max/equal values unless
the user requests a restriction. Dimension filters preserve their intended
selection and do not replace external Planning Context.

## Geometry and ownership

- Account for every dashboard visual before placing or embedding content.
- Keep direct visual geometry in the visual properties.
- Keep embedded Planning geometry in the page-local embed override.
- Preserve the source Planning owner; never recreate it to position its embed.
- Reserve distinct regions for the header, slicers, chart, navigator and Planning
  workbench.
- Verify bounds, overlap and unrelated-property preservation through a fresh
  readback.

## Presentation defaults

The reusable defaults observed by the synthetic fixture are:

- Arial for text, headers and navigation.
- White visual surfaces with a restrained neutral border.
- A wide header/content canvas with a compact spacing rhythm.
- A complete Navigator state, including disabled icon padding.
- A horizontal all-page navigator with no copied runtime page IDs.
- Explicit row/column total configuration.
- Measure-specific read/edit/source-role colors that remain separate from
  calculation and identity.

## Acceptance boundaries

Passing the following checks is not the same as proving runtime behavior:

- Valid Plan definition parts and schemas.
- Stable source/model references resolved from current metadata.
- Complete native/DataInput/Formula measure records.
- Matching formula references and source bindings.
- Complete visual-level filter registrations.
- Preserved IDs, unrelated properties and current ETags during updates.
- Non-overlapping persisted geometry.
- Independently verified page visibility.

Runtime calculation, input save/reopen, distribution, lock enforcement,
rendered layout, interaction propagation and effective security each require a
separate authorized acceptance test.

## Related reusable contracts

- [Runtime guide](runtime-guide.md)
- [Planning integrity](planning-integrity.md)
- [Input editability](input-editability.md)
- [Numeric column values](numeric-column-values.md)
- [Chart visual filters](chart-visual-filters.md)
- [Integrated variance](integrated-variance.md)
- [Navigators](navigators.md)
- [Planning presentation](planning-presentation.md)
