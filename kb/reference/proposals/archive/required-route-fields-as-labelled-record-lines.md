---
description: "Proposal (adopted): Historical route-label observations behind mandatory presence checks; the shared contract and ADR 100 now own the implemented decision."
type: reference/types/design-proposal.md
---

# Required route fields as labelled record lines

> **Archived** (see [archive README](./README.md)). Adopted in narrowed form by
> [ADR 100](../../adr/100-check-required-route-fields-at-member-acceptance.md).
> The shared record contract and member validator carry the live requirement.
> The dated observations below remain historical evidence.

## Current state (as of 2026-09-29)

The original proposal recorded one retained PageIndex set on main,
`AAS-2026-09-28-pageindex-01`. All four runtime route records carried the
`Later read-back:` label; none of the seven memory route records used it.
These were different authoring contracts, so the observation was not an
omission rate. Memory record RTE-5 answered the question with “Later
read-back is RTE-8 and RTE-9” without the colon label.

Runtime paragraphs combined multiple fields and varied labels such as
`Expiry`, `Invalidation`, and `Invalidation/expiry`. The observation showed
that exact-label counts would conflate a formatting difference with missing
analysis unless answers were inspected separately.

The batch-01 rerun trace audit dated 2026-09-28 reported a Basic Memory
specialist output that passed validation, then needed two correction turns
for missing read-back fields, heterogeneous objects and irregular headings
and IDs. The specialist had not opened the runtime type holding the full
route-field requirements. That batch was not on main at the proposal's date.

## Retained boundary

These are the observations reported in the proposal at that time. They do not
measure the reorganized shared contract or the adopted field validator.
The original analysis sets are not migrated or re-certified. Current syntax,
consumer delivery, alternatives, rejected migration and the decision against
an additional adequacy assay are recorded in ADR 100. There is no remaining
implementation commission in this archive entry.
