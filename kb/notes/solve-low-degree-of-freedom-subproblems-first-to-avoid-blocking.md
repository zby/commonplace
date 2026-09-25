---
description: "Ordering heuristic for decomposition: commit first to decisions with the fewest viable options, then place flexible choices around them to preserve global optionality."
type: note
traits: []
tags: [computational-model]
---

# Solve low-degree-of-freedom subproblems first to avoid blocking better designs

When a design problem has interdependent subproblems, the highest-leverage ordering is to commit the least flexible decision first. Christopher Alexander's kitchen example illustrates the mechanism: window placement has very few viable positions, table placement depends on the window's light, and stove placement is comparatively flexible. If you place the stove first, you can accidentally consume the only strong position for the window or table.

This is not domain-specific advice about kitchens; it is a general sequencing rule for constrained search:

1. Identify subproblems by the size of their feasible set ("degrees of freedom").
2. Commit low-degree-of-freedom choices first.
3. Recompute feasible sets for remaining choices.
4. Defer high-flexibility choices until constrained decisions are fixed.

The reason this works is optionality preservation. Early decisions with many alternatives should not be allowed to block decisions with very few alternatives.

## Precedent in constraint search

Constraint-satisfaction search tests the same rule under exact conditions. [Bacchus and van Run](../sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md) study minimum remaining values (MRV): at each branch, commit next the variable with the fewest values still consistent with earlier commitments, then prune the remaining domains, which is step 3 above. On their binary benchmarks, MRV ordering beat static orders in every reported test except enumerating all n-Queens solutions. Their explanation differs from this note's. MRV is *fail-first*: it makes a dead end surface at the next step instead of after exponential work. The two explanations agree when a commitment is cheap to undo. When a commitment is hard to reverse, as many design decisions are, only optionality preservation argues for the order, and the CSP evidence does not cover that case. The paper also names where the ordering stops paying: large, easy problems with many solutions, and the cost of computing the ordering itself.

SAT solving shows what replaces the rule when option counts cannot rank candidates, since every Boolean variable has two values. [Chaff](../sources/chaff-engineering-an-efficient-sat-solver.ingest.md) treats a variable with one admissible value as no decision at all: propagation assigns it before the next decision. It ranks the rest by VSIDS, a decayed count of each literal's appearances in recently learned conflict clauses. Reading that count as a substitute measure of how constrained a choice is belongs to this note, not the paper, and the paper does not isolate VSIDS's contribution. The agent-side analogue is a conjecture: when feasible-set sizes cannot be estimated, prioritise the decisions that recently caused failures.

In agent workflows, low-degree-of-freedom choices usually correspond to hard constraints: required output schema, tool contracts, file locations, deterministic validation requirements, or precedence rules. High-degree choices are often rhetorical or representational: phrasing, narrative order, or which equivalent summary format to use. This matches [decomposition rules for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md): selection and constraint-setting happen first; expensive synthesis calls happen after the constrained frame is established.

The rule also applies when commitments are split across an authoring/execution divide — an orchestrator and its subagents, or a plan and the agent that runs it. Role can assign a decision to another actor, while later evidence can defer its timing; those choices may coincide, but they are independent. [An author should fix what the executor can't determine, not what it will](./fix-what-the-executor-cant-determine-not-what-it-will.md) applies that distinction to which facts and choices belong upstream or at execution.

## Open Questions

- Can degree-of-freedom estimates be made explicit enough for deterministic scheduler heuristics? In exact constraint search they can, since MRV maintains a count of remaining values, but that count depends on cheap, exact consistency checks that design choices lack.
- Which "apparently flexible" choices become low-degree once downstream validation is considered?

---

Relevant Notes:

- [alexander-patterns-and-knowledge-system-design](./alexander-patterns-and-knowledge-system-design.md) — operationalization: extracts a concrete sequencing heuristic from the broader generative-process framing
- [decomposition-heuristics-for-bounded-context-scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — extends: applies the same ordering rule to agent decomposition strategy
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — enables: symbolic state lets constrained choices be fixed before costly semantic calls
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — example: hard constraints precede softer interpretive guidance
- [Dynamic variable ordering in CSPs](../sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md) — evidenced-by: MRV ordering in exact constraint search, with fail-first as a rival mechanism and named limits
- [Chaff: engineering an efficient SAT solver](../sources/chaff-engineering-an-efficient-sat-solver.ingest.md) — evidenced-by: forced single-option assignments precede decisions; conflict activity ranks the rest when option counts cannot
- [fix-what-the-executor-cant-determine-not-what-it-will](./fix-what-the-executor-cant-determine-not-what-it-will.md) — extends: applies the ordering rule across the authoring/execution divide while separating when a choice is made from which actor owns it
