# Proposals

Finished but unadopted designs for the Commonplace system. A proposal describes a design object — the problem, the option space, the forces, the free choices — without claiming the system works this way or deciding that it should.

This directory is the **frontier**: every file in it is a live, undecided design, so listing it answers "what is still open" without a filter. Decided proposals leave for [`archive/`](./archive/README.md) — see Archiving below.

## Contract

- **Type.** Collection-local [`design-proposal`](../types/design-proposal.md) type. Its schema enforces the mechanical core — the `Proposal` description lead and the dated current-state anchor; the remaining clauses here bind as prose. Review judges design quality (problem stated, forces stated, free choices marked, adoption criteria named), not contestability.
- **No decision.** A proposal may hold multiple options and unresolved forces. When it converges on one choice that ships, the choice becomes an ADR (`../adr/`) and the proposal is superseded by it.
- **First version stays conceptual.** A new proposal commits to the problem, the option space, the forces, and the free choices — not to implementation detail. Field names, schemas, thresholds, and step-by-step procedures invented before the design space is understood are authoring-time snapshots that constrain later design without warrant — the same mistake [an instruction author makes by fixing details the executor could determine](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), landed one layer earlier. Add detail in revisions, when a named force or an adoption decision demands it; a first version that reads like an implementation plan has skipped its own option space.
- **Requirements live in theory.** Transferable requirements are claims — they belong in `kb/notes/` and are cited from here via a `rationale` edge. The proposal inlines only system-specific constraints: stats, precedents, integration boundaries.
- **Dated current-state anchor.** State the system facts the proposal rests on under a "Current state (as of YYYY-MM-DD)" heading. Going stale against later ADRs is an expected lifecycle event for a proposal, not a defect — refresh or retire.
- **Operativity and warrant** (proposals authored 2026-07-24 or later). For each option that changes behavior-determining organization, state its operativity path — what would consume the change, through which channel, with what force ([operative change](../../notes/definitions/operative-change.md)). "No consumer yet; one must be built" is a valid answer and exactly what the adoption decision needs to see. If an option adds or strengthens automated evaluation, also name what warrants the oracle and where that warrant stops.
- **Unmistakably proposed.** The frontmatter description leads with "Proposal:". Readers of `kb/reference/` are usually trying to act on the shipped system; nothing in this directory describes shipped behavior.

## Lifecycle

Workshop (`kb/work/`, active exploration, closes) → proposal here (finished, undecided, waits) → ADR (decided and implemented) — or retirement, when a later decision forecloses it. Either ending archives the proposal.

**Partial adoption moves content out.** When part of a proposal ships, remove it from the proposal: the shipped behavior is described in reference docs and recorded in an ADR, and the proposal keeps only what remains undecided (noting the adoption in its current-state anchor). A proposal that silently retains shipped content has become a false description. A partially adopted proposal stays here — it still holds undecided content, which is what this directory is for.

## Archiving

When a proposal is fully adopted (its choice ships as an ADR) or retired (a later decision forecloses it), it leaves the frontier for `archive/`. Retention is cheap; standing search surface is not, so the archive keeps the design object without letting it dilute what a reader or agent sweeps.

- **Extract first.** Archiving is gated on removing everything still current from the proposal: shipped behavior into reference docs, the decision-relevant reasoning — options weighed and why they lost, deciding forces, free choices resolved or left open — into the ADR's `## Considered alternatives`, and transferable requirements into `kb/notes/`. What stays behind is design texture: dated current-state anchors, corpus statistics, the dialectic the proposal accumulated while it waited.
- **The archive is a link sink.** No library artifact links into it. Two exceptions: [`archive/README.md`](./archive/README.md), the instruction for working with archived proposals, which links its own contents freely; and the workshop layer (`kb/work/`), where archive work — re-extraction, decision audit, re-opening — actually happens, and whose files are deleted rather than accumulated. Archived files may link out to the frontier. This mirrors the workshop layer's own sinks-not-sources rule (`kb/work/COLLECTION.md`) — the KB has two sink layers, one before the frontier and one after.
- **Provenance is a tag, not a pointer.** An ADR names the proposal it adopted or retired by title in prose — no path, no link. The title is enough for anyone doing archive work; a link would route ordinary readers into stale design and re-enter it into the frontier through the back door.
- **Repair by re-extraction, never by linking in.** If something still current turns out to have been left behind, mine it from the archived proposal and promote it into the frontier. Reaching it with a live link instead would make the archived document load-bearing again and end the frontier's completeness.

Decision records: [ADR 028](../adr/028-design-proposals-live-in-reference-proposals.md) (this directory), [ADR 056](../adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) (archiving).
