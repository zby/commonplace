# Proposals

Finished but unadopted designs for the Commonplace system. A proposal describes a design object — the problem, the option space, the forces, the free choices — without claiming the system works this way or deciding that it should.

This directory is the **frontier**: every file in it is a live, undecided design, so listing it answers "what is still open" without a filter. Decided proposals are in [`archive/`](./archive/README.md).

This README is navigation only; it states no rules ([ADR 084](../adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md)). What binds a proposal is in two places:

- [Design proposal type](../types/design-proposal.md) — what a proposal must be, its lifecycle states, and the procedure for each transition.
- [`kb/reference/COLLECTION.md`](../COLLECTION.md) — where proposals and archived proposals may live.

## Multi-repository analysis

- [Multi-repository agentic-system analysis](./multi-repository-agentic-system-analysis.md) — cover systems such as Ars Umbris through one frozen source tree while preserving roles, source IDs and path-only quotations.

## Strategy and measurement

- [Reusable commitment support across kinds of knowledge work](./reusable-commitment-support-across-kinds-of-knowledge-work.md) — Commonplace's strategy as a testable conjecture in `configure(G, K_P)` form: support built for theory building generalizes to other kinds of knowledge work at lower total cost than per-kind tools; three options for how G comes to exist, and the one comparison that would support or defeat it.
- [Cost-per-yield records for routine controllers](./cost-per-yield-records-for-routine-controllers.md) — give each routine search controller a record of yield and cost that states the context regime it ran in, so controllers in unattended pipelines can be compared on cost as well as yield.

## Lifecycle at a glance

Workshop (`kb/work/`, active exploration, closes) → proposal here (finished, undecided, waits) → ADR (decided and implemented) — or retirement, when a later decision forecloses it — or withdrawal, when its problem or trigger lapses with no decision. Partial adoption keeps a proposal here with only its undecided part. Procedures:

- [Refresh a proposal's current state](../../instructions/refresh-a-proposal-current-state.md)
- [Extract the adopted part of a proposal](../../instructions/extract-adopted-part-of-a-proposal.md)
- [Retire an artifact](../../instructions/retire-artifact.md) — archiving

Decision records: [ADR 028](../adr/028-design-proposals-live-in-reference-proposals.md) (this directory), [ADR 056](../adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) (archiving), [ADR 084](../adr/084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) (where the rules live).
