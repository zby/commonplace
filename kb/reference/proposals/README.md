# Proposals

Finished but unadopted designs for the Commonplace system. A proposal describes a design object — the problem, the option space, the forces, the free choices — without claiming the system works this way or deciding that it should.

## Contract

- **Type and trait.** Plain `note` type carrying the `design-proposal` trait. There is no template or schema yet; the trait routes review — design quality (problem stated, forces stated, free choices marked, adoption criteria named), not contestability.
- **No decision.** A proposal may hold multiple options and unresolved forces. When it converges on one choice that ships, the choice becomes an ADR (`../adr/`) and the proposal is superseded by it.
- **First versions stay conceptual.** A new proposal commits to the problem, the option space, the forces, and the free choices — not to implementation detail. Field names, schemas, thresholds, and step-by-step procedures invented before the design space is understood are authoring-time snapshots that constrain later design without warrant — the same mistake [an instruction author makes by fixing details the executor could determine](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), landed one layer earlier. Add detail in revisions, when a named force or an adoption decision demands it; a first version that reads like an implementation plan has skipped its own option space.
- **Requirements live in theory.** Transferable requirements are claims — they belong in `kb/notes/` and are cited from here via a `rationale` edge. The proposal inlines only system-specific constraints: stats, precedents, integration boundaries.
- **Dated current-state anchor.** State the system facts the proposal rests on under a "Current state (as of YYYY-MM-DD)" heading. Going stale against later ADRs is an expected lifecycle event for a proposal, not a defect — refresh or retire.
- **Operativity and warrant** (proposals authored 2026-07-24 or later). For each option that changes behavior-determining organization, state its operativity path — what would consume the change, through which channel, with what force ([operative change](../../notes/definitions/operative-change.md)). "No consumer yet; one must be built" is a valid answer and exactly what the adoption decision needs to see. If an option adds or strengthens automated evaluation, also name what warrants the oracle and where that warrant stops.
- **Unmistakably proposed.** The frontmatter description leads with "Proposal:". Readers of `kb/reference/` are usually trying to act on the shipped system; nothing in this directory describes shipped behavior.

## Lifecycle

Workshop (`kb/work/`, active exploration, closes) → proposal here (finished, undecided, waits) → ADR (decided and implemented) — or retirement, when a later decision forecloses it.

**Partial adoption moves content out.** When part of a proposal ships, remove it from the proposal: the shipped behavior is described in reference docs and recorded in an ADR, and the proposal keeps only what remains undecided (noting the adoption in its current-state anchor). A proposal that silently retains shipped content has become a false description.

Decision record: [ADR 028](../adr/028-design-proposals-live-in-reference-proposals.md).
