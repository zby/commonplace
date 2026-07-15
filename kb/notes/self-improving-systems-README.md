---
description: "Curated head for the self-improving-systems tag — membership asks for evidence-responsive operative change; reflective versus non-reflective is the central distinction, four gradings place a system"
type: kb/types/tag-readme.md
index_source: tag
index_key: self-improving-systems
complete: true
---

# Self-improving systems

The object is the [**self-improving system**](./definitions/self-improving-system.md): a system that makes operative changes to its own behavior-determining organization, causally responsive to evidence bearing on an improvement objective. An improvement criterion is required semantically; an explicit evaluator is not required architecturally — evidence may determine an update directly (gradient-, reward-, viability-driven) or select among candidates. Membership is deliberately broad: a weight-level learner is inside, a fully staffed dev team is inside without autonomy. The central distinction is **reflective versus non-reflective self-improvement** — whether the change is routed through a writable, causally connected self-representation of the aspect being changed — and it is pathway-relative: one system may improve some aspects reflectively and others not. The name alone carries little information; the design information is in the gradings, [since four independent gradings place a self-improving system](./four-independent-gradings-place-a-self-improving-system.md). Most systems in [agent-memory-systems](../agent-memory-systems/README.md) are a bid at the reflective kind — mine the traces, write the lesson down, load it next time.

## The proposal-selection subtype

The gate architecture — candidates generated, evaluated with a possibility of non-adoption, selectively made operative — is a named subtype, and it is where the oracle, rejectability, and verification machinery lives.

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — the subtype and its three functions, their weakest viable forms, and the diagnostic use: when a loop stalls, ask which function is missing rather than which component failed.
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — evaluation is the terminal filter: a rejected candidate costs effort, a bad acceptance is kept and compounds. Acceptance is an improvement claim, not evidence of improvement.

## The gradings

Each pairs a nearly free attribution with a costly one, and they move independently.

- **Retention form** — [reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md): operative, cumulative, or addressable, and only the last is knowledge. The machinery is the [reflective system](./definitions/reflective-system.md)'s causally connected map plus intercession, and its wire is best-effort — [retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md).
- **Coverage** — [reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md): claims named per form (prose, symbolic, distributed-parametric) and operation depth.
- **Closure** — [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md): whether each decision a change raises has a governed answer, or must be improvised.
- **Autonomy** — [human-inclusive boundaries make reflection cheap](./human-inclusive-boundaries-make-reflection-cheap.md): assessed per function against a declared boundary. Bare autonomy is free; what costs is warrant — [warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md).

## Occupants, placed on the axes

- [Ashby's Homeostat](../sources/ashby-design-for-a-brain-ultrastability.md) — non-reflective, viability-driven, and fully autonomous, the floor of the category: no evaluator anywhere in the mechanism, retention by equilibrium. It retains without accumulating.
- Parametric self-improvers — self-play policies, agents fine-tuned on their own trajectories, a thermostat learning in weights — non-reflective direct determination: evidence computes the update, nothing is ever rejected, and improvement compounds without addressability. The dominant learning paradigm, and the corner this KB has covered least; new notes belong under this tag.
- The [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — a reflective, autonomous proposal-selection loop, bought with the strongest available oracle and paid for in reach: every improvement it cannot prove is unreachable.
- [Commonplace](../reference/commonplace-as-a-reflective-system.md) — a reflective, human-inclusive proposal-selection loop: humans hold search and the judgment-heavy evaluation, the gates no adequate automatable oracle closes.
- A Smalltalk image alone — maximal machinery, no evidence-responsiveness, not a member: nothing in it responds to evidence about an objective, and the programmer supplies what is missing.

## Consequence for agentic systems

- [Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — reliability gains move behavior between prose and code rather than staying in either, so coverage of a single form cannot carry them.
- The external reviews run on this vocabulary: the [agent-memory-system-review](../agent-memory-systems/types/agent-memory-system-review.md) type asks each system for its representational forms, its behavioral authority as *consumer, channel, and force*, and its promotion path; the [comparison matrix](../agent-memory-systems/systems-table.md) is generated from those terms.

## Related Tags

- [foundations](./foundations-README.md) — the broader core theory this sits inside, including [actionable methodology](./definitions/actionable-methodology.md)
- [constraining](./constraining-README.md) — closure is a constraining property of methodology-as-input
- [computational-model](./computational-model-README.md) — reflection and intercession as computational concepts generalized to socio-technical boundaries
