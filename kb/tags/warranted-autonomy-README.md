---
description: "Curated head for the warranted-autonomy tag — which decisions an AI agent is warranted to take over from humans, how oracles bound that, and how autonomy is measured"
type: types/tag-readme.md
complete: true
---

# warranted-autonomy

Notes on handing decisions from humans to a computational actor: which decisions an agent is warranted to take over, what makes that transfer justified rather than merely possible, and how to measure the autonomy a system actually has. The establishing claim is [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): bare autonomy is free, but warranted evaluation autonomy extends only to the candidates an oracle can assess with the required confidence. It is a child of [self-improving-systems](./self-improving-systems-README.md). Boundary: [reflection](./reflection-README.md) asks whether a system can read and revise its own organization; this tag asks who is warranted to make that revision and the other decisions in the loop.

## What bounds warranted transfer

- [Warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — the establishing claim: autonomy is warranted only where an oracle can assess the candidates
- [A claim without external assessment carries three obligations](../notes/a-claim-without-external-assessment-carries-three-obligations.md) — what a computational actor must supply when no outside assessor grades its claim
- [Naur's human-only conclusion needs more than the absence of explicit criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md) — unformulated judgment does not by itself put a decision beyond computation
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — an actor may carry extension further than its method, but those choices are not thereby settled

## The human–computation allocation

- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](../notes/computationally-directed-self-improvement-is-a-reallocation.md) — progress is which decision-bearing functions humans still supply; the endpoint is contracting the boundary to exclude them
- [Methodological and computational closure track different changes](../notes/methodological-and-computational-closure-track-different-changes.md) — what a method settles and whether a human decided during operation are separate questions
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — easy-to-warrant decisions move first, so the human residue gets harder per decision
- [Increasing computational autonomy relocates human effort to the frontier](../notes/increasing-computational-autonomy-relocates-human-effort.md) — human hours need not fall; count improvements per human judgment
- [A method's ceiling bounds the method, not the transfer it already made](../notes/a-method-ceiling-bounds-the-method-not-the-transfer-already-made.md) — a responsibility that left the human residue stays transferred when the method stops improving

## Measuring autonomy and its evidence

- [Measuring autonomy well enough to see it improve is an open problem](../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — a per-function profile, not a percentage, and not yet comparable across systems or time
- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) — a progress claim must name which one moved; autonomy gains do not license power claims
- [A benchmark that holds the client fixed exports the least-warrantable decisions by design](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md) — fixed-client benchmarks measure worker capability and leave broader closure untested
- [A complete theory path does not establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md) — mediation, empirical contact, and response to criticism each support a different claim
- [Disconnected witnesses do not establish a full causal path through theory](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md) — evidence must show the joins of one path, and still separately show improved capacity

## Related Tags

- [self-improving-systems](./self-improving-systems-README.md) — the parent; this tag holds its actor-allocation question
- [reflection](./reflection-README.md) — the self-revision whose decisions this tag allocates between humans and computation
- [improvement-loop](./improvement-loop-README.md) — the loop functions (search, evaluation, retention) that can be handed to a computational actor
- [theory-builder](./theory-builder-README.md) — an autonomous theory builder is the case where computation performs every internal operation
- [software-factory](./software-factory-README.md) — where production decisions move from human developers to agents
- [continual-learning](./continual-learning-README.md) — the deployed learning whose updates need an authorizing actor
