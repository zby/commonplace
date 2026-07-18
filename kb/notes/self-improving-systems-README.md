---
description: "Curated head for the self-improving-systems tag — evidence-responsive operative change; the stake: the improvement loop closes as improvised decisions become governed machinery"
type: kb/types/tag-readme.md
index_source: tag
index_key: self-improving-systems
complete: true
---

# Self-improving systems

A [self-improving system](./definitions/self-improving-system.md) makes operative changes to its own behavior-determining organization in response to evidence about an improvement objective. The definition is deliberately broad — a weight-level learner qualifies, and so does a dev team. The distinction that carries the design information is whether the improvement pathway is **reflective** — routed through a self-representation — or not. Most systems in [agent-memory-systems](../agent-memory-systems/README.md) mine their traces for lessons and load them into later runs — a bid at the reflective kind that succeeds only when the loaded lessons function as a representation of the system's own behavior, not just accumulated knowledge.

## The improvement loop

Self-improvement is a recurring loop, not a single act, and its functions can be allocated to people, agents, or code independently: [a proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md). Its failure asymmetry: [false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — evaluation is the terminal filter.

## Reflection makes the loop editable

1. Reflection makes retained lessons **addressable**: later rounds can read, criticize, and selectively revise them — [reflection buys addressability](./reflection-buys-addressability.md).
2. An addressable lesson is **second-order**: it can reject a prior commitment outright, where a gradient can only nudge it — [reflection makes retained lessons second-order](./reflection-makes-retained-lessons-second-order.md).
3. The standing discount: retrieval is best-effort, and a lesson that never surfaces contributes nothing — [retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md).

## Closing the loop

The cluster's organizing thesis: [an improvement loop closes by converting improvised decisions into governed machinery](./an-improvement-loop-closes-by-converting-improvised-decisions.md). A loop is more closed the fewer decisions per cycle need improvised human supply, and it closes decision by decision — inputs made addressable, meta-decisions settled, oracles hardened — so partial closure is the predicted state, not a way station. The human is relocated, not removed: [a closing improvement loop relocates human effort to the frontier instead of reducing it](./a-closing-loop-relocates-human-effort-to-the-frontier.md), so measure improvements per human judgment, not total hours. The payoffs are hypotheses: [reflection may improve sample efficiency under structured shifts](./reflection-may-improve-sample-efficiency-under-structured-shifts.md) sharpens one — reduced target data — into a test design.

## The three gradings

Since membership is cheap, a system is characterized by where it sits on [three independent gradings](./three-independent-gradings-place-a-self-improving-system.md):

- **Retention form** — operative, cumulative, or addressable. The chain above is this axis's payoff; the machinery is the [reflective system](./definitions/reflective-system.md)'s causally connected self-map.
- **Coverage** — [reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md).
- **Closure** — [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).

Read statically the gradings place a system; read dynamically they are the faces of that conversion.

Autonomy — how much of the pathway runs without a person — is a fourth thing worth reporting for any system, but it is not tracked as a fourth placement here: under Commonplace's strictly computational reflective-system boundary, a pathway that is reflective at all is thereby also autonomous, [since admitting a human into the boundary would only trade that precision for a separate axis](./admitting-a-human-into-the-boundary-trades-reflectivity-for-autonomy.md). Non-reflective pathways are reported human-inclusive or autonomous directly, using the base definition's own boundary-relative grading. What costs is **warrant**, trusting what an unattended loop accepts: [warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

## Example placements

- [Ashby's Homeostat](../sources/ashby-design-for-a-brain-ultrastability.md) — the floor: non-reflective, fully autonomous, nothing accumulates.
- Parametric self-improvers (self-play policies, agents fine-tuned on their own trajectories) — compounding without addressability; the dominant paradigm and the conjecture's comparison baseline.
- The [Gödel machine](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — reflective, autonomous, proof-gated: the strongest oracle, paid for in domain.
- [Commonplace itself](../reference/commonplace-as-a-reflective-system.md) — pathway-mixed, part-way up the displacement ladder: reflective and autonomous where a validator or agent consults an explicit self-representation, non-reflective and human-inclusive where a maintainer notices what's worth fixing or judges the shape of a fix.

Read every claim at its stated strength: the definitions are stipulated and revisable, the closing-loop thesis and its payoffs are hypotheses, and whether they hold is the open empirical question the cluster sharpens.

## Further notes under the tag

- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — the per-function grading above tells you where a system sits, but not whether it is getting more autonomous or how it compares to a differently-decomposed system.
- [Behavior-determining organization](./definitions/behavior-determining-organization.md), [operative change](./definitions/operative-change.md), [evidence bearing on an improvement objective](./definitions/evidence-bearing-on-an-improvement-objective.md) — the definition's three base terms.
- [The definition classifies its boundary cases without ad hoc exceptions](./the-self-improving-system-definition-classifies-its-boundary-cases.md) — nine inclusion tests, from gradient learning to accidental self-modification.
- [Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — reliability gains move behavior between prose and code, so coverage of one form cannot carry them. The [agent-memory-system reviews](../agent-memory-systems/types/agent-memory-system-review.md) and the [comparison matrix](../agent-memory-systems/systems-table.md) run on this vocabulary.
- [Reach assessment](./definitions/reach-assessment.md) — the semantic judgment reflectivity's structural requirements do not supply; the sample-efficiency conjecture and second-order rescoping both depend on it, and current evaluators seem to have it with no theory for why.
- [Formal symbolic systems assess reach only through causal and proof obligations](./formal-systems-can-assess-reach-through-causal-and-proof-obligations.md) — reach assessment isn't LLM-exclusive: causal inference and proof search give traditional symbolic systems a formal route to it once a claim's generality is encoded as a checkable obligation.

## Related Tags

- [foundations](./foundations-README.md) — the broader core theory this sits inside
- [constraining](./constraining-README.md) — closure is a constraining property of methodology-as-input
- [computational-model](./computational-model-README.md) — reflection and intercession as computational concepts generalized to socio-technical boundaries
