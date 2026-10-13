---
type: types/write-brief.md
description: "Commission for temporary amendments to published analyses: preserve the operator's bounded alternative to costly full reruns without adding approval or statistical migration machinery"
---

# Brief: temporary amendments to published analyses

## Intent

The operator commissioned this proposal on 2026-10-13 to describe how readers
can receive bounded additions, corrections and staleness qualifications after
an analysis is published, without rerunning the entire analysis for every change.
Keep it a conceptual proposal, not an implementation or an active-run instruction.

## Must keep

- Amendments belong to one exact run. A replacement run ends their applicability
  to the current analysis automatically; historical attachment remains.
- The producer arranges independent verification as part of production, without
  an additional operator-authorization gate for each amendment.
- Changes too broad to remain local require a full rerun. Preserve reader-visible
  warnings while a needed rerun is pending.
- Existing fields remain available to existing statistical consumers when new
  coverage is added. Reader-visible additions do not automatically rewrite
  summaries or statistical outputs.

## Must exclude

- A per-amendment resolution, incorporation or acceptance gate on replacement
  runs; the operator explicitly rejected this requirement.
- A general statistics eligibility, backfill or migration framework. Treatment
  of older reports is decided individually when a future field or collection
  change requires it, not in this proposal.
- Implicit authority to change frozen runs, launch analyses or implement the
  proposal merely because it has been written.

## Reserved decisions

Exact storage layout, schema, commands and display implementation remain for
adoption and implementation. Do not present speculative interfaces as shipped.
