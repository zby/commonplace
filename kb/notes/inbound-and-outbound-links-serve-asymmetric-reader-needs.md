---
description: "A note's outbound links show what it rests on; its inbound links show what rests on it — four read-time orientation needs (standing, grounding, impact, tension) that are distinct from batch maintenance, computed rather than authored, and bound differently for human and agent readers"
type: kb/types/note.md
traits: [title-as-claim]
tags: [links]
status: seedling
---

# Inbound and outbound links serve asymmetric reader needs

A note's outbound links are authored prose: they show what the note rests on. Its inbound links show what rests on it — and the note cannot author them, because they are created elsewhere, by every later note that cites it. The two directions answer different reader questions, and treating "linking" as one symmetric concern hides that the inbound direction has its own needs, its own cost structure, and its own consumers.

## Four orientation needs only the inbound view serves

1. **Standing** — is this note foundational or peripheral? Outbound links show what informed it; nothing in the note shows whether ten notes build on it or none do. Seeing "3 extend this, 1 contradicts it" changes how carefully a reader reads and whether editing is risky. Matters most during cold-start orientation in an unfamiliar area.
2. **Grounding** — what evidence has accumulated for this claim? Source captures link *to* theory notes, but the theory note doesn't know practitioner evidence points at it. The inbound view shows how well-grounded a claim is — and flags synthesis opportunities when enough sources converge.
3. **Impact** — what breaks if this changes? Before editing a claim, a reader needs what depends on it. Typed inbound links show this at a glance: notes that build on the claim are affected; notes that merely exemplify it are safe.
4. **Tension** — who disagrees? A `contradicts` edge is visible only from the side that authored it, unless surfaced from both. (Symmetric labels authored at both ends are the existing exception — they exist precisely because this need is two-sided.)

All four are **read-time orientation** needs: they change what the reader does with the note currently open.

## Orientation is not maintenance

Orphan detection consumes the same inverted-link data but is a different need: its threshold is zero-vs-high inbound count, its purpose is batch cleanup, and it runs as a periodic sweep, not at read time. The boundary claim: read-time surfacing machinery is justified only by orientation needs; maintenance needs are served by sweeps over computed data. Conflating the two over-builds the read surface to serve a batch job.

Also out of scope: finding notes to link *to* when writing — that is search and discovery, not inbound visibility.

## The inbound view is computed, not authored

The forward edge is the canonical representation; the inverse view is derived. Two reasons. **Fan-out:** a foundational note accumulates inbound edges from every later note that builds on it — maintaining the reverse list by hand scales with the note's popularity, exactly when it is least affordable. **Register:** an inbound list is metadata, not prose — a footer of twelve "referenced by" entries does not read as argument, so it competes with the principle that links are inline prose carrying commitment. Both push the same way: author one direction, compute the other.

## The needs bind per consumer

Who is reading determines how the computed view should reach them. A human in a rendered view skims and searches sublinearly — materializing the inbound list on the page at build time costs them nothing. An agent reading repo files pays linear context cost for every byte — for it the inbound view should stay a query answered on demand, not a stored section, since [the first-time human wins except where access cost dominates](./design-for-the-first-time-human-except-on-access-cost.md). The four needs are constant across consumers; the delivery mechanism is the variable.

---

Relevant Notes:

- [Linking theory](./linking-theory.md) — extends: the decision-cost model for outbound links, extrapolated here to inbound visibility
- [ADR 020 — theoretical-default additions (contrasts, mechanism)](../reference/adr/020-theoretical-default-contrasts-mechanism.md) — evidence: the directional-asymmetry decision rests on forward edges being canonical and the inverse view computed
- [Backlink surfacing](../reference/proposals/backlink-surfacing.md) — see-also: the Commonplace design space for delivering the inbound view, which takes this note's needs as its requirements
