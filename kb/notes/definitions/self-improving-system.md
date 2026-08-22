---
description: "Definition — operative, evidence-responsive change to a system's own behavior-determining organization, read against a declared boundary, horizon, and improvement objective"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Self-improving system

A **self-improving system** makes operative changes to its own behavior-determining organization, where those changes are causally responsive to evidence bearing on an **improvement objective**.

*Its own* means the object of change is the system's [behavior-determining organization](./behavior-determining-organization.md) — its parameters, policies, memory, rules, workflows, code — not an external work product. A compiler that optimizes programs is not self-improving; a compiler pipeline that rewrites its own optimizer is. This is Ashby's two-loop distinction: operating a system is one loop, modifying the system that operates is another. The attribution is assessed against a declared boundary: a model fine-tuned by an external training pipeline is being improved, while the composite of model plus pipeline self-improves — [the boundary cases make this dependence explicit](../the-self-improving-system-definition-classifies-its-boundary-cases.md).

*Operative* means the change affects subsequent operation over the relevant horizon, through a consumer, a channel, and a force — [operative change](./operative-change.md), which does not require permanence; a transient compensation, or a change nothing ever acts on, does not qualify.

*Makes* is read over a declared assessment horizon, like operativity: a system is self-improving over that horizon when evidence-responsive operative self-change occurs within it. The dispositional attribution — the system *has* a standing improvement pathway, currently exercised or not — is also available, but it is a different claim and must be marked as such; a pathway nothing has exercised over the relevant horizon supports only the dispositional reading. Tense, like boundary, is declared rather than fixed by the definition.

## The causal anatomy

For an occurrent attribution, four causal obligations must close within the declared boundary and horizon:

1. Evidence bearing on the objective causally shapes the determination of an update.
2. The result becomes a change to the bounded system's own behavior-determining organization, rather than remaining evidence, a proposal, or an external work product.
3. The changed organization enters a live behavioral-authority path with a consumer, channel, and force capable of reaching later behavior.
4. A subsequent operation exercises that path and causally depends on the change.

These are logical roles, not required components or stages. A direct update can determine and install its successor in one transition; another architecture can separate proposal, acceptance, and installation. The membership test asks whether the causal dependencies close, not how many components realize them.

Persistence and availability establish less than this path. A saved episode that never affects an updater fails the first obligation. An accepted proposal that never becomes part of the organization fails the second. An installed artifact with no live consumer fails the third. Mandatory loading establishes a channel, but if the consumer ignores the content, the fourth remains unestablished. Storage, retrieval, acceptance, installation, and loading are therefore evidence about particular links, not substitutes for the end-to-end attribution.

## Evidence-responsiveness does not require a gate

*Responsive to evidence* is defined in [evidence bearing on an improvement objective](./evidence-bearing-on-an-improvement-objective.md). There must be a loss, reward, error, viability bound, test, judgment, or other criterion for the evidence to bear on; otherwise the change is merely caused, not improvement-directed.

The evidence may directly determine an update that is always adopted, or it may evaluate a candidate that can be rejected. A separately represented candidate, evaluator, or acceptance gate is therefore not required by membership. The [proposal-selection improvement loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) owns that named subtype and its search, evaluation, oracle, and retention vocabulary.

Update architecture attaches to a named pathway, target aspect, and granularity, not to a whole system. A gradient step may be direct while a checkpoint-release gate around it uses proposal selection, and one system may compose both kinds of pathway.

> An improvement criterion is required semantically; an explicit evaluator is not required architecturally.

## What membership leaves open

Membership establishes improvement-directed self-change, not a complete architecture or a successful outcome. Evidence-responsiveness can faithfully pursue a bad objective, and an evaluator can accept a harmful change: only outcome evidence establishes that improvement occurred.

Classify the remaining questions elsewhere:

- [Reflective system](./reflective-system.md) owns whether the pathway changes itself through a causally connected self-representation; reflection is not required for membership.
- [The pathway profile](../self-improving-systems-README.md) owns reflective structure, improvement dynamics, governance, and actor allocation; [the cumulativity criterion itself](../accumulation-counts-dependence-through-the-retained-result.md) is held separately.
- [Methodological and computational closure](../methodological-and-computational-closure-track-different-changes.md) owns the two closure readings, and [warranted autonomy](../warranted-autonomy-is-bounded-by-oracle-domain.md) owns when unattended evaluation is trustworthy.

## Exclusions

- **Not self-modification alone.** Blind or accidental rewrites lack evidence-responsiveness.
- **Not regulation alone.** A thermostat changes its environment, not its own behavior-determining organization; a learning thermostat that revises its controller does.
- **Not work-product improvement.** Improving an answer or external code does not change the improving system's own organization.
- **Not reflection, a gate, or autonomy.** Each may describe a member, but none is a membership condition.
- **Not guaranteed success.** The term names an improvement-directed mechanism, not a favorable outcome.

## Misuse Cases

- Treating the proposal-selection improvement loop as the definition rather than a named subtype, which re-smuggles an architecture into semantics.
- Treating stored or retrieved evidence as an operative update without showing that it affects the update determination and results in organizational change.
- Treating acceptance, installation, or loading as proof that a subsequent operation causally depends on the change.
- Reporting an autonomy grade without declaring the boundary it was assessed against.
- Attributing self-improvement without naming the objective it is indexed to, or naming one the pathway's evidence is not diagnostic of — [the first leaves the attribution elliptical, the second makes it false](../self-improvement-is-relative-to-a-declared-objective.md).
- Reading a dormant improvement pathway as current self-improvement — the dispositional claim (*has* a pathway) and the horizon claim (evidence-responsive change is occurring over this horizon) are different attributions.
- Treating a helpful change to an external product as self-improvement of the tool that produced it.

## Provenance

Commonplace treats the predicate as frame-indexed. The bearer of the property is a bounded system — a system under a declared boundary — not a substrate simpliciter, so an attribution is elliptical until the boundary is named. The fine-tuning-pipeline case in [the boundary cases](../the-self-improving-system-definition-classifies-its-boundary-cases.md) shows why: the same substrate is being improved under one boundary and self-improving under another.

Self-representation and reject-capable evaluation are not membership conditions. Reflection instead names a structural property whose distinctive benefit is developed in [reflection buys addressability](../reflection-buys-addressability.md), while proposal selection names the narrower update architecture with a rejectable adoption decision.

This architecture-neutral choice is consistent with uses of “self-improving” for gateless self-tuning algorithms ([Ailon et al. 2011](https://page.mi.fu-berlin.de/mulzer/pubs/selfimpSICOMP.pdf)) and with self-adaptive-systems literature treating feedback-loop models as engineering reference models rather than definitions ([Weyns](https://people.cs.kuleuven.be/~danny.weyns/papers/2017HSE.pdf); [Petrovska, Erjiage, and Kugele 2025](https://arxiv.org/pdf/2505.17798)). It is Commonplace's explication, not a claimed field consensus.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — extends: the named subtype where the improvement criterion is implemented as an evaluator, and the three functions that architecture requires
- [Reflection buys addressability](../reflection-buys-addressability.md) — extends: what routing a change through a readable self-representation adds
- [Reflective system](./reflective-system.md) — grounds: the causally connected self-representation, and the intercession capability, that reflective self-improvement routes through
- [Methodological and computational closure track different changes](../methodological-and-computational-closure-track-different-changes.md) — extends: owns governance and actor-allocation readings outside membership
- [Warranted autonomy is bounded by oracle domain](../warranted-autonomy-is-bounded-by-oracle-domain.md) — extends: owns the trustworthiness of unattended evaluation
- [Behavior-determining organization](./behavior-determining-organization.md) — defined-in: what "its own organization" covers, and why work products are excluded
- [Operative change](./operative-change.md) — defined-in: persistence over a declared horizon plus a behavioral-authority path, without requiring permanence
- [Evidence bearing on an improvement objective](./evidence-bearing-on-an-improvement-objective.md) — defined-in: what counts as the evidence, and why no evaluator component is required
- [Behavioral authority](./behavioral-authority.md) — defined-in: the consumer, channel, and force that operative change requires
- [The definition classifies its boundary cases without ad hoc exceptions](../the-self-improving-system-definition-classifies-its-boundary-cases.md) — extends: applies the membership clauses to ten cases
- [Self-improvement is relative to a declared objective](../self-improvement-is-relative-to-a-declared-objective.md) — extends: the objective as a third declared parameter beside boundary and horizon, and the two conditions it carries
