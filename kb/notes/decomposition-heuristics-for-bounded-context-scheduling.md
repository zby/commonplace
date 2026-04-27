---
description: Working heuristics for symbolic scheduling over bounded LLM calls — separate selection from joint reasoning, choose representations not just subsets, save reusable intermediates in scheduler state
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Decomposition heuristics for bounded-context scheduling

These rules are motivated by the [symbolic scheduling model](./bounded-context-orchestration-model.md). Each heuristic is a transformation between programs — and since [any symbolic program with LLM calls is a select/call program](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md), applying a heuristic keeps you within the model's program space. The rules are preliminary — we expect to discover more as the model develops.

## What is being optimised

The scheduler has to choose a decomposition, a prompt-construction strategy, and a schedule of state transformations that improves the task result while keeping each LLM call inside its effective context budget.

Even before underspecified semantics enter, there are several objective terms:

- Total token traffic between scheduler state and LLM calls
- Number of agent calls
- Peak prompt size
- Information loss from compression
- Preservation of cross-item interactions needed by later synthesis
- Cost of verifying or reviewing intermediate outputs

This makes the problem different from ordinary knapsack-style context packing. The scheduler must trade off:

- **Early filtering** against the risk of discarding something that matters later
- **Aggressive summarisation** against the risk of destroying interactions needed for synthesis
- **Many narrow calls** against the overhead of orchestration
- **Loading raw state-derived material** against **saving task-shaped intermediate ones**
- **Context-fitting splits** against the cost of checking and merging their outputs

The first two are about optionality — paying context now to keep options open later. The latter three are about cost structure — choosing between representations and decompositions with different efficiency, verification, and merge profiles. Both kinds of trade-off are present in every scheduling decision.

## Working heuristics

These are proposed rules, not established principles. Direct support exists for symbolic exactness, recursive clean frames, delaying co-loading at the zero-interaction extreme, and verifiability-aware boundaries; the remaining heuristics are conjectured from the model's structure and practice.

**Separate selection from joint reasoning.** First use cheap narrow calls to discover sparsity. Only then pay for wide calls that need multiple items together. When the relevant set is irreducibly dense — most items interact with most others — this separation has limited room to operate; the scheduler may need to fall back on hierarchical merging with explicit interface preservation rather than filtering.

**Use symbolic operations wherever exactness is available.** Retrieval, thresholding, sorting, prompt assembly, and name-based routing should be outside the LLM window whenever possible.

**Save reusable intermediate items in scheduler state.** Relevance labels, extracted claims, and task-specific summaries are worth keeping when they are much cheaper to reuse than reconstructing the originals.

**Delay expensive co-loading until interactions justify it.** Joint loading is valuable only when the task depends on relations between items rather than independent judgments about them.

**Decompose toward verifiable boundaries.** Context fit is not the only objective. A decomposition can be necessary simply because the unsplit task exceeds effective context, even if the split does not improve verification. But when several decompositions fit, prefer boundaries whose outputs have cheaper completion checks, clearer contracts, or lower-cost review. Treat splits that improve fit while making verification harder as trade-offs, not free wins.

**Commit low-degree-of-freedom choices first.** When one decision has only a narrow feasible set and another has many workable options, decide the constrained one first. This preserves optionality and avoids consuming scarce valid placements too early. Example: in a multi-source synthesis task, the output schema (few valid options) should be fixed before selecting which sources to foreground (many workable orderings).

**Do not compress away needed interfaces.** If the final answer depends on tensions, contradictions, or alignments between sources, summaries should preserve pointers or extracted structures that keep those interactions recoverable.

**Choose representations, not just subsets.** The main optimisation variable is often not which items to load, but whether to expose bodies, extracts, summaries, or previous synthesis items to the bounded call.

**Exploit clean frames recursively.** A clean frame is a focused call context containing only the material needed for that subtask. When the relevant set is still too large, apply the same pattern again: filter, cluster, compress, and merge in a tree rather than a flat history. The stopping condition is when decomposition overhead (extra calls, interface loss) exceeds the compositional-complexity benefit — but this note does not yet specify how to detect that threshold.

## Empirical grounding

ConvexBench, a benchmark for LLM recognition of convex symbolic expressions under deep composition ([Liu et al., 2026](https://arxiv.org/html/2602.01075v2)), supports two rules through distinct mechanisms. "Use symbolic operations wherever exactness is available" is confirmed by the design: expression structure is recovered via deterministic AST parsing rather than LLM calls. Separately, "exploit clean frames recursively" is supported by two results. Scoped recursion — pruning history to retain only direct dependencies — recovers F1=1.0 at all depths from F1≈0.2 under flat accumulation. Finer decomposition (10-character sub-functions) also consistently outperforms coarser decomposition. The F1 recovery comes from the focused-context scoping strategy (an LLM-call management technique), not from the symbolic parsing step; these are distinct interventions in the source. Both results hold despite trivial token counts (5,331 tokens at depth 100), confirming that the rules respond to compositional complexity, not volume.

MAKER, a maximal-decomposition agent system ([Meyerson et al., 2025](https://arxiv.org/abs/2511.09030)), demonstrates the extreme case: maximal decomposition to m=1 (one step per bounded call) achieves O(s ln s) cost scaling and solves a 1,048,575-step task with zero errors. Without decomposition, cost scales exponentially. This confirms "delay expensive co-loading until interactions justify it" at the zero-interaction extreme: each step depends only on the current disk configuration, so independent calls dominate joint reasoning. The O(s ln s) scaling comes from two parts. Decomposition supplies the s factor, while MAKER's voting-based error correction (first-to-ahead-by-k) supplies the ln s term; decomposition alone does not guarantee the bound. MAKER also illustrates the limit of "exploit clean frames recursively": when every sub-task is atomic, the recursive pattern degenerates to a flat sequence of maximally focused calls — though the source does not frame its architecture as recursive.

Both sources operate in the hard-oracle regime, where sub-step correctness is mechanically checkable. Whether these heuristics hold equally for soft-oracle tasks, where correctness depends on judgment or proxy scores — synthesis, creative work, ambiguous judgment — remains untested.

The intelligent-delegation framework (Tomasev, Franklin, and Osindero, 2026) adds the verification side of the scheduling problem. Its contract-first decomposition rule says that subtasks that remain too subjective, costly, or complex to verify should be split further or routed with stronger oversight. That does not make verification the only reason to decompose; bounded context can force decomposition before verification improves. It does mean the scheduler should track checkability as a separate objective alongside fit.

## Open Questions

- Which classes of lossy derived items preserve enough structure for later synthesis?
- How should a scheduler detect the stopping condition for recursive decomposition — when overhead exceeds compositional-complexity benefit?
- Do the heuristics transfer to soft-oracle tasks where per-step correctness cannot be verified mechanically?

---

Sources:
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](https://arxiv.org/html/2602.01075v2) — finer decomposition and focused context recover full performance from compositional collapse.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors](https://arxiv.org/abs/2511.09030) — maximal decomposition achieves O(s ln s) cost scaling on million-step tasks.
- Tomasev, Franklin, and Osindero (2026). [Intelligent AI delegation: Engineering frameworks for delegating decisions to machines](https://arxiv.org/abs/2604.00389) — contract-first decomposition treats verifiability as a separate constraint on task splitting and oversight.

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — cost model: context is the scarce resource these rules optimise over
- [distillation](./definitions/distillation.md) (directed context compression) — mechanism: saved intermediate items are often distillations shaped for later reuse
- [solve low-degree-of-freedom subproblems first to avoid blocking better designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md) — extends: general ordering heuristic that explains why constraint-setting should happen before flexible synthesis choices
- [topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) — extends: "exploit clean frames recursively" implements the topology → isolation step of a proposed causal chain
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — frames: verification cost is a separate constraint from context fit, especially when decomposed work is delegated or automated
