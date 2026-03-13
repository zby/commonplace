---
description: Ordering heuristic for decomposition: commit first to decisions with the fewest viable options, then place flexible choices around them to preserve global optionality.
type: note
traits: []
tags: [computational-model]
status: seedling
---

# Solve low-degree-of-freedom subproblems first to avoid blocking better designs

When a design problem has interdependent subproblems, the highest-leverage ordering is to commit the least flexible decision first. Christopher Alexander's kitchen example illustrates the mechanism: window placement has very few viable positions, table placement depends on the window's light, and stove placement is comparatively flexible. If you place the stove first, you can accidentally consume the only strong position for the window or table.

This is not domain-specific advice about kitchens; it is a general sequencing rule for constrained search:

1. Identify subproblems by the size of their feasible set ("degrees of freedom").
2. Commit low-degree-of-freedom choices first.
3. Recompute feasible sets for remaining choices.
4. Defer high-flexibility choices until constrained decisions are fixed.

The reason this works is optionality preservation. Early decisions with many alternatives should not be allowed to block decisions with very few alternatives.

In agent workflows, low-degree-of-freedom choices usually correspond to hard constraints: required output schema, tool contracts, file locations, deterministic validation requirements, or precedence rules. High-degree choices are often rhetorical or representational: phrasing, narrative order, or which equivalent summary format to use. This matches [decomposition rules for bounded-context scheduling](./decomposition-rules-for-bounded-context-scheduling.md): selection and constraint-setting happen first; expensive synthesis calls happen after the constrained frame is established.

## Open Questions

- Can degree-of-freedom estimates be made explicit enough for deterministic scheduler heuristics?
- Which "apparently flexible" choices become low-degree once downstream validation is considered?

---

Relevant Notes:

- [alexander-patterns-and-knowledge-system-design](./alexander-patterns-and-knowledge-system-design.md) — operationalization: extracts a concrete sequencing heuristic from the broader generative-process framing
- [decomposition-rules-for-bounded-context-scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — extends: applies the same ordering rule to agent decomposition strategy
- [bounded-context-orchestration-model](./bounded-context-orchestration-model.md) — enables: symbolic state lets constrained choices be fixed before costly semantic calls
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — example: hard constraints precede softer interpretive guidance
