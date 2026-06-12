---
description: "Proposal: how Commonplace could surface inbound links — build-time web rendering for humans, on-demand inversion for agents, curated symmetric labels for tension; committed generated footers and full manual bidirectionality are foreclosed"
type: kb/types/note.md
traits: [design-proposal]
tags: [links]
status: seedling
---

# Backlink surfacing

How Commonplace could deliver the inbound-link view to its readers. Requirements — the reader needs this design must serve and the orientation/maintenance boundary it must respect — rest on [inbound and outbound links serve asymmetric reader needs](../../notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md); this proposal holds only the option space and the system-specific constraints.

## Current state (as of 2026-06-12)

- Outbound links are authored: inline prose links plus labelled "Relevant Notes" footers. No inbound visibility exists in the repo; inversion is possible on demand via `rg '<note-slug>' --glob '*.md'`, but agents must think to run it.
- Nothing generated is committed at any size ([ADR 025](../adr/025-complete-generated-indexes-are-build-time-only.md), refined by ADR 026). Generated listings are materialized only at mkdocs build time for the web view; curated tag READMEs receive no generated links.
- Agents discover via curated heads plus scoped `rg`; ADR 025 deliberately added no query command, deferring codification until a recurring failure justifies it.
- Symmetric link labels (`contradicts`, `contrasts`) are authored at both ends, so tension surfacing already works without machinery.

## Design space, split by consumer

- **Human web readers** — render an inbound-links section per page at mkdocs build time: a second materialization of the authored outbound edges, one source of truth, nothing committed. This is the ADR 025 pattern applied to backlinks; browser scroll and find keep long inbound lists cheap to skim.
- **Agents in the repo** — keep the inbound view a query: a documented scoped `rg` inversion recipe, optionally codified later as a `commonplace-*` command. Consistent with ADR 025's no-new-command default and the linear context cost of stored sections.
- **Curated semantics** — where the relationship type matters (tension), the authored symmetric labels remain the mechanism; no generated machinery can infer edge semantics.

## Foreclosed options

- **Committed generated footers** ("Referenced by:" sections written into notes by a sync script) — violates nothing-generated-is-committed; the family precedent (`sync_topic_links.py` Topics footers) was itself retired.
- **Full manual bidirectionality** (agents author a backlink for every outbound link) — fan-out makes upstream maintenance scale with a note's popularity; [ADR 020](../adr/020-theoretical-default-contrasts-mechanism.md) already decided the forward edge is canonical for exactly this reason.

## Open questions

- Noise floor: is a one-entry inbound list worth rendering, or should the web section appear only above a threshold?
- Does the agent-side recipe deserve a command (`commonplace-backlinks <note>`), or is that the codification ADR 025 says to defer until recurring failure?
- Should source→note inbound edges (the grounding need) render distinctly from note→note edges in the web view?

---

Relevant Notes:

- [inbound and outbound links serve asymmetric reader needs](../../notes/inbound-and-outbound-links-serve-asymmetric-reader-needs.md) — rationale: the reader needs and boundaries this design must satisfy
- [ADR 025 — complete generated indexes are build-time only](../adr/025-complete-generated-indexes-are-build-time-only.md) — rests on: the one-source-two-materializations pattern and the no-new-command default this proposal extends to backlinks
