---
description: "Zinkevich's online convex-programming regret bounds provide a technical basis for direct, gateless evidence-responsive updates and their assumptions."
source_snapshot: "zinkevich-online-convex-programming.md"
ingested: "2026-07-21"
type: kb/sources/types/ingest-report.md
domains: [online-learning, regret, self-improving-systems, optimization]
---

# Ingest: Online Convex Programming and Generalized Infinitesimal Gradient Ascent

Source: [zinkevich-online-convex-programming.md](zinkevich-online-convex-programming.md)
Captured: 2026-07-21
From: [CMU technical report](https://www.cs.cmu.edu/~maz/publications/techconvex.pdf)

## Classification

Genre: scientific-paper -- a Carnegie Mellon technical report that defines an online optimization model, proves regret bounds, and applies the algorithm to repeated games. The author signal is strong for the mathematical claims, but this is a theoretical result rather than a report on an implemented Commonplace-like system.
Domains: online-learning, regret, self-improving-systems, optimization
Author: Martin Zinkevich, Carnegie Mellon University; CMU-CS-03-110 (February 2003).

## Summary

The paper defines online convex programming as choosing each feasible point before seeing that round's convex cost function. Its Greedy Projection update takes a gradient step on the revealed cost and projects back into the feasible set; with a square-root-decaying learning rate, average regret against the best fixed feasible point tends to zero under boundedness, differentiability, bounded gradients, gradient access, and projection access. It also gives dynamic-regret and lazy-projection bounds, then shows that repeated games are online linear programs and that generalized infinitesimal gradient ascent (GIGA) is universally consistent. The important Commonplace-facing result is architectural: the gradient/error signal directly determines an adopted update, without a separately represented candidate or reject-capable gate.

## Connections Found

Repo-local discovery read `kb/sources/COLLECTION.md`, the connect-report type, the notes titles/descriptions, and the complete `self-improving-systems` tag head. Scoped body searches for `regret`, `gradient`, `online convex`, `universal consistency`, `projection`, and `oracle` followed [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [Self-improving system](../notes/definitions/self-improving-system.md), [Evidence bearing on an improvement objective](../notes/definitions/evidence-bearing-on-an-improvement-objective.md), and [A self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md). The source is a technical basis/evidence anchor for those notes: it supplies the concrete direct-determination case that the notes distinguish from proposal-selection, and it makes the cumulative-but-opaque gradient example mathematically precise. No durable source-to-source connection was strong enough to retain.

## Extractable Value

1. **Direct determination is a complete improvement architecture without a gate.** The update consumes the revealed gradient and is always adopted; this grounds the architecture-neutral definition's claim that evidence-responsiveness does not require reject-capable evaluation. [quick-win]
2. **Regret gives a precise improvement objective and horizon.** Comparing cumulative online cost with the best fixed feasible comparator, and showing sublinear regret, supplies a reusable objective for distinguishing evidence-responsive adaptation from mere reaction. [quick-win]
3. **Projection is an explicit feasibility-preservation operation.** The update separates unconstrained evidence-driven movement from the mechanism that keeps the retained state inside the admissible organization, a useful pattern when mapping gradient-like updates onto bounded artifact or policy spaces. [experiment]
4. **Cumulativity can be opaque yet real.** Each next gradient is evaluated at and applied to the retained parameter state, supporting the pathway-profile example that cumulative improvement does not imply reflective, readable self-representation. [quick-win]
5. **The guarantee depends on strong mathematical assumptions.** Bounded closed feasible sets, bounded gradients, differentiability (or a computable subgradient), and algorithmic gradient/projection access define the regime in which the guarantee holds; these assumptions identify what an operational analogue would need to make explicit. [deep-dive]

## Limitations (our opinion)

This is a theoretical adversarial-sequence result, not evidence that an agent or knowledge base improves its own behavior. The feasible set, convex costs, gradients, and projection oracle are supplied by the problem designer; the paper does not address how a real system discovers an objective, validates a proxy, chooses a boundary, or prevents a bad objective from being optimized consistently. The static comparator and dynamic path-length bounds are informative but do not establish generalization to non-convex, non-stationary, discrete, or human-judged artifact changes. A simpler account of the Commonplace relevance is therefore enough: the paper formalizes one direct update mechanism, while the KB's governance and oracle questions remain outside its scope.

## Recommended Next Action

Update [A proposal-selection improvement loop requires search, evaluation, and operative retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) with a source link to this snapshot and one sentence naming Zinkevich's Greedy Projection/GIGA result as the canonical direct-determination counterexample to a required acceptance gate; preserve the existing online-gradient citation as the conceptual pointer and use this ingest as the technical anchor.
