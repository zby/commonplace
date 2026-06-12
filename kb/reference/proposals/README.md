# Proposals

Finished but unadopted designs for the Commonplace system. A proposal describes a design object — the problem, the option space, the forces, the free choices — without claiming the system works this way or deciding that it should.

## Contract

- **Type and trait.** Plain `note` type carrying the `design-proposal` trait. There is no template or schema yet; the trait routes review — design quality (problem stated, forces stated, free choices marked, adoption criteria named), not contestability.
- **No decision.** A proposal may hold multiple options and unresolved forces. When it converges on one choice that ships, the choice becomes an ADR (`../adr/`) and the proposal is superseded by it.
- **Requirements live in theory.** Transferable requirements are claims — they belong in `kb/notes/` and are cited from here via a `rationale` edge. The proposal inlines only system-specific constraints: stats, precedents, integration boundaries.
- **Dated current-state anchor.** State the system facts the proposal rests on under a "Current state (as of YYYY-MM-DD)" heading. Going stale against later ADRs is an expected lifecycle event for a proposal, not a defect — refresh or retire.
- **Unmistakably proposed.** The frontmatter description leads with "Proposal:". Readers of `kb/reference/` are usually trying to act on the shipped system; nothing in this directory describes shipped behavior.

## Lifecycle

Workshop (`kb/work/`, active exploration, closes) → proposal here (finished, undecided, waits) → ADR (decided and implemented) — or retirement, when a later decision forecloses it.

**Partial adoption moves content out.** When part of a proposal ships, remove it from the proposal: the shipped behavior is described in reference docs and recorded in an ADR, and the proposal keeps only what remains undecided (noting the adoption in its current-state anchor). A proposal that silently retains shipped content has become a false description.

Decision record: [ADR 028](../adr/028-design-proposals-live-in-reference-proposals.md).
