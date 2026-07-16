---
description: "Curated head for the self-improving-systems tag — evidence-responsive operative change; the stake: reflection may cut target data under structured shifts"
type: kb/types/tag-readme.md
index_source: tag
index_key: self-improving-systems
complete: true
---

# Self-improving systems

A [self-improving system](./definitions/self-improving-system.md) makes operative changes to its own behavior-determining organization in response to evidence about an improvement objective. The definition is deliberately broad — a weight-level learner qualifies, and so does a dev team. The distinction that carries the design information is whether the improvement pathway is **reflective** — routed through a self-representation — or not. Most systems in [agent-memory-systems](../agent-memory-systems/README.md) mine their traces for lessons and load them into later runs — a bid at the reflective kind that succeeds only when the loaded lessons function as a representation of the system's own behavior, not just accumulated knowledge.

## Why reflection might pay

The case for reflective pathways is a four-step chain; only the first step is architectural rather than conjectural.

1. Reflection makes retained lessons **addressable**: later rounds can read, criticize, and selectively revise them — [reflection buys addressability](./reflection-buys-addressability.md).
2. An addressable lesson is **second-order**: it can reject a prior commitment outright, where a gradient can only nudge it — [reflection makes retained lessons second-order](./reflection-makes-retained-lessons-second-order.md).
3. The payoff conjecture: [reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md). This is Commonplace's own bet, not a result; the note carries the prediction and the test design.
4. The standing discount: retrieval is best-effort, and a lesson that never surfaces contributes nothing — [retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md).

## The three gradings

Since membership is cheap, a system is characterized by where it sits on [three independent gradings](./three-independent-gradings-place-a-self-improving-system.md):

- **Retention form** — operative, cumulative, or addressable. The chain above is this axis's payoff; the machinery is the [reflective system](./definitions/reflective-system.md)'s causally connected self-map.
- **Coverage** — [reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md).
- **Closure** — [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).

Autonomy — how much of the pathway runs without a person — is a fourth thing worth reporting for any system, but it is not tracked as a fourth placement here: under Commonplace's strictly computational reflective-system boundary, a pathway that is reflective at all is thereby also autonomous, [since admitting a human into the boundary would only trade that precision for a separate axis](./admitting-a-human-into-the-boundary-trades-reflectivity-for-autonomy.md). Non-reflective pathways are reported human-inclusive or autonomous directly, using the base definition's own boundary-relative grading. What costs is **warrant**, trusting what an unattended loop accepts: [warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md).

## Example placements

- [Ashby's Homeostat](../sources/ashby-design-for-a-brain-ultrastability.md) — the floor: non-reflective, fully autonomous, nothing accumulates.
- Parametric self-improvers (self-play policies, agents fine-tuned on their own trajectories) — compounding without addressability; the dominant paradigm and the conjecture's comparison baseline.
- The [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — reflective, autonomous, proof-gated: the strongest oracle, paid for in reach.
- [Commonplace itself](../reference/commonplace-as-a-reflective-system.md) — pathway-mixed: reflective and autonomous where a validator or agent consults an explicit self-representation, non-reflective and human-inclusive where a maintainer notices what's worth fixing or judges the shape of a fix.

Read every claim at its stated strength: the definitions are stipulated and revisable, the reflective advantage is a hypothesis, and whether it holds is the open empirical question the chain above sharpens.

## Further notes under the tag

- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — the per-function grading above tells you where a system sits, but not whether it is getting more autonomous or how it compares to a differently-decomposed system.
- [Behavior-determining organization](./definitions/behavior-determining-organization.md), [operative change](./definitions/operative-change.md), [evidence bearing on an improvement objective](./definitions/evidence-bearing-on-an-improvement-objective.md) — the definition's three base terms.
- [The definition classifies its boundary cases without ad hoc exceptions](./the-self-improving-system-definition-classifies-its-boundary-cases.md) — nine inclusion tests, from gradient learning to accidental self-modification.
- [A proposal-selection loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) and [false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — the generate-evaluate-retain subtype and why evaluation is its terminal filter.
- [Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — reliability gains move behavior between prose and code, so coverage of one form cannot carry them. The [agent-memory-system reviews](../agent-memory-systems/types/agent-memory-system-review.md) and the [comparison matrix](../agent-memory-systems/systems-table.md) run on this vocabulary.

## Related Tags

- [foundations](./foundations-README.md) — the broader core theory this sits inside
- [constraining](./constraining-README.md) — closure is a constraining property of methodology-as-input
- [computational-model](./computational-model-README.md) — reflection and intercession as computational concepts generalized to socio-technical boundaries
