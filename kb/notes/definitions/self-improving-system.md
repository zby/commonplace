---
description: "Definition — operative, evidence-responsive change to a system's own behavior-determining organization, relative to a declared boundary"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Self-improving system

A **self-improving system** makes operative changes to its own behavior-determining organization, where those changes are causally responsive to evidence bearing on an **improvement objective**.

*Its own* means the object of change is the system's [behavior-determining organization](./behavior-determining-organization.md) — its parameters, policies, memory, rules, workflows, code — not an external work product. A compiler that optimizes programs is not self-improving; a compiler pipeline that rewrites its own optimizer is. This is Ashby's two-loop distinction: operating a system is one loop, modifying the system that operates is another. The attribution is assessed against a declared boundary: a model fine-tuned by an external training pipeline is being improved, while the composite of model plus pipeline self-improves — [the boundary cases make this dependence explicit](../the-self-improving-system-definition-classifies-its-boundary-cases.md).

*Operative* means the change affects subsequent operation over the relevant horizon, through a consumer, a channel, and a force — [operative change](./operative-change.md), which does not require permanence; a transient compensation, or a change nothing ever acts on, does not qualify.

*Makes* is read over a declared assessment horizon, like operativity: a system is self-improving over that horizon when evidence-responsive operative self-change occurs within it. The dispositional attribution — the system *has* a standing improvement pathway, currently exercised or not — is also available, but it is a different claim and must be marked as such; a pathway nothing has exercised over the relevant horizon supports only the dispositional reading. Tense, like boundary, is declared rather than fixed by the definition.

## Evidence-responsiveness does not require a gate

*Responsive to evidence* is defined in [evidence bearing on an improvement objective](./evidence-bearing-on-an-improvement-objective.md). There must be a loss, reward, error, viability bound, test, judgment, or other criterion for the evidence to bear on; otherwise the change is merely caused, not improvement-directed.

The evidence may directly determine an update that is always adopted, or it may evaluate a candidate that can be rejected. A separately represented candidate, evaluator, or acceptance gate is therefore not required by membership. The [proposal-selection improvement loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) owns that named subtype and its search, evaluation, oracle, and retention vocabulary.

> An improvement criterion is required semantically; an explicit evaluator is not required architecturally.

## What membership leaves open

Membership establishes improvement-directed self-change, not a complete architecture or a successful outcome. Evidence-responsiveness can faithfully pursue a bad objective, and an evaluator can accept a harmful change: only outcome evidence establishes that improvement occurred.

Classify the remaining questions elsewhere:

- [Reflective system](./reflective-system.md) owns whether the pathway changes itself through a causally connected self-representation; reflection is not required for membership.
- [The pathway profile](../a-self-improving-system-needs-a-profile-not-a-ladder.md) owns reflective structure, cumulativity, governance, and actor allocation.
- [Methodological and computational closure](../methodological-and-computational-closure-track-different-changes.md) owns the two closure readings, and [warranted autonomy](../warranted-autonomy-is-bounded-by-oracle-domain.md) owns when unattended evaluation is trustworthy.

## Exclusions

- **Not self-modification alone.** Blind or accidental rewrites lack evidence-responsiveness.
- **Not regulation alone.** A thermostat changes its environment, not its own behavior-determining organization; a learning thermostat that revises its controller does.
- **Not work-product improvement.** Improving an answer or external code does not change the improving system's own organization.
- **Not reflection, a gate, or autonomy.** Each may describe a member, but none is a membership condition.
- **Not guaranteed success.** The term names an improvement-directed mechanism, not a favorable outcome.

## Misuse Cases

- Treating the proposal-selection improvement loop as the definition rather than a named subtype, which re-smuggles an architecture into semantics.
- Reporting an autonomy grade without declaring the boundary it was assessed against.
- Reading a dormant improvement pathway as current self-improvement — the dispositional claim (*has* a pathway) and the horizon claim (evidence-responsive change is occurring over this horizon) are different attributions.
- Treating a helpful change to an external product as self-improvement of the tool that produced it.

## Provenance and departures

One departure is semantic rather than a retired restriction: the predicate is frame-indexed. The bearer of the property is a bounded system — a system under a declared boundary — not a substrate simpliciter, so an attribution is elliptical until the boundary is named. Established classification practice reads category membership frame-independently; the fine-tuning-pipeline case in [the boundary cases](../the-self-improving-system-definition-classifies-its-boundary-cases.md) is why that reading fails here — the same substrate is being improved under one boundary and self-improving under another.

Two earlier restrictions were retired because they excluded central cases. Requiring self-representation excluded parametric learners; the substantive benefit of reflection now belongs to [reflection buys addressability](../reflection-buys-addressability.md). Requiring reject-capable evaluation excluded direct gradient- and viability-driven adaptation; proposal-selection now names that narrower architecture.

This architecture-neutral choice is consistent with uses of “self-improving” for gateless self-tuning algorithms ([Ailon et al. 2011](https://arxiv.org/abs/0907.0884)) and with self-adaptive-systems literature treating feedback-loop models as engineering reference models rather than definitions ([Weyns 2019](https://people.cs.kuleuven.be/~danny.weyns/papers/2017HSE.pdf); [Petrovska, Erjiage, and Kugele 2025](https://arxiv.org/abs/2505.17798)). It is Commonplace's explication, not a claimed field consensus.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — extends: the named subtype where the improvement criterion is implemented as an evaluator, and the three functions that architecture requires
- [A self-improving system needs a profile, not a ladder](../a-self-improving-system-needs-a-profile-not-a-ladder.md) — extends: keeps membership distinct from reflective structure, improvement dynamics, governance, and actor allocation
- [Reflection buys addressability](../reflection-buys-addressability.md) — extends: what routing a change through a readable self-representation adds
- [Reflective system](./reflective-system.md) — grounds: the causally connected self-representation, and the intercession capability, that reflective self-improvement routes through
- [Methodological and computational closure track different changes](../methodological-and-computational-closure-track-different-changes.md) — extends: owns governance and actor-allocation readings outside membership
- [Warranted autonomy is bounded by oracle domain](../warranted-autonomy-is-bounded-by-oracle-domain.md) — extends: owns the trustworthiness of unattended evaluation
- [Behavior-determining organization](./behavior-determining-organization.md) — defined-in: what "its own organization" covers, and why work products are excluded
- [Operative change](./operative-change.md) — defined-in: persistence over a declared horizon plus a behavioral-authority path, without requiring permanence
- [Evidence bearing on an improvement objective](./evidence-bearing-on-an-improvement-objective.md) — defined-in: what counts as the evidence, and why no evaluator component is required
- [Behavioral authority](./behavioral-authority.md) — defined-in: the consumer, channel, and force that operative change requires
- [The definition classifies its boundary cases without ad hoc exceptions](../the-self-improving-system-definition-classifies-its-boundary-cases.md) — extends: applies the membership clauses to ten cases
