---
description: Practical rules for symbolic scheduling over bounded LLM calls — separate selection from joint reasoning, choose representations not just subsets, save reusable intermediates in scheduler state
type: note
traits: [has-external-sources]
areas: [computational-model]
status: seedling
---

# Decomposition rules for bounded-context scheduling

These rules follow from the [symbolic scheduling model](./bounded-context-orchestration-model.md). They are preliminary — we expect to discover more as the model develops.

## What is being optimised

The optimisation problem is:

Choose a decomposition, a prompt-construction strategy, and a schedule of state transformations that maximises expected task utility while respecting the per-call bound `M`.

Even before underspecified semantics enter, there are several objective terms:

- total token traffic between scheduler state and LLM calls
- number of agent calls
- peak prompt size
- information loss from compression
- preservation of cross-item interactions needed by later synthesis

This makes the problem different from ordinary knapsack-style context packing. The scheduler must trade off:

- **early filtering** against the risk of discarding something that matters later
- **aggressive summarisation** against the risk of destroying interactions needed for synthesis
- **many narrow calls** against the overhead of orchestration
- **loading raw state-derived material** against **saving task-shaped intermediate ones**

The first two are about optionality — paying context now to keep options open later. The latter two are about cost structure — choosing between representations and decompositions with different efficiency profiles. Both kinds of trade-off are present in every scheduling decision.

## Rules

**Separate selection from joint reasoning.** First use cheap narrow calls to discover sparsity. Only then pay for wide calls that need multiple items together.

**Use symbolic operations wherever exactness is available.** Retrieval, thresholding, sorting, prompt assembly, and name-based routing should be outside the LLM window whenever possible.

**Save reusable intermediate items in scheduler state.** Relevance labels, extracted claims, and task-specific summaries are worth keeping when they are much cheaper to reuse than reconstructing the originals.

**Delay expensive co-loading until interactions justify it.** Joint loading is valuable only when the task depends on relations between items rather than independent judgments about them.

**Commit low-degree-of-freedom choices first.** When one decision has only a narrow feasible set and another has many workable options, decide the constrained one first. This preserves optionality and avoids consuming scarce valid placements too early.

**Do not compress away needed interfaces.** If the final answer depends on tensions, contradictions, or alignments between sources, summaries should preserve pointers or extracted structures that keep those interactions recoverable.

**Choose representations, not just subsets.** The main optimisation variable is often not which notes to load, but whether to expose bodies, extracts, summaries, or previous synthesis items to the bounded call.

**Exploit clean frames recursively.** When the relevant set is still too large, apply the same pattern again: filter, cluster, compress, and merge in a tree rather than a flat history.

## Empirical grounding

ConvexBench ([Liu et al., 2026](../sources/convexbench-can-llms-recognize-convex-functions.md)) validates two rules directly. The "use symbolic operations wherever exactness is available" rule is confirmed by the design: expression structure is recovered via deterministic AST parsing (not LLM calls), and scoped recursion — pruning history to retain only direct dependencies — recovers F1=1.0 at all depths from F1≈0.2 under flat accumulation. The ablation result that finer decomposition (10-character sub-functions) consistently outperforms coarser decomposition confirms "exploit clean frames recursively." Both results hold despite trivial token counts (5,331 tokens at depth 100), confirming that the rules respond to compositional complexity, not volume.

MAKER ([Meyerson et al., 2025](../sources/meyerson-maker-million-step-llm-zero-errors.md)) demonstrates the extreme case: maximal decomposition to m=1 (one step per bounded call) achieves O(s ln s) cost scaling and solves a 1,048,575-step task with zero errors. Without decomposition, cost scales exponentially. This validates "delay expensive co-loading until interactions justify it" — each step depends only on the current disk configuration, so independent calls dominate joint reasoning. It also confirms "exploit clean frames recursively" at the limit: when every sub-task is atomic, the recursive pattern degenerates to a flat sequence of maximally focused calls.

## Open Questions

- Which classes of lossy derived items preserve enough structure for later synthesis?

---

Sources:
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](../sources/convexbench-can-llms-recognize-convex-functions.md) — finer decomposition and focused context recover full performance from compositional collapse.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors](../sources/meyerson-maker-million-step-llm-zero-errors.md) — maximal decomposition achieves O(s ln s) cost scaling on million-step tasks.

Relevant Notes:

- [symbolic scheduling over bounded LLM calls is the right model for agent orchestration](./bounded-context-orchestration-model.md) — foundation: the model these rules follow from
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — cost model: context is the scarce resource these rules optimise over
- [distillation](./distillation.md) — mechanism: saved intermediate items are often distillations shaped for later reuse
- [solve low-degree-of-freedom subproblems first to avoid blocking better designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md) — extends: general ordering heuristic that explains why constraint-setting should happen before flexible synthesis choices

Topics:

- [computational-model](./computational-model.md)
