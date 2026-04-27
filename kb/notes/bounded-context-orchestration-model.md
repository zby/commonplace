---
description: Formalises agent orchestration as a symbolic scheduler driving bounded LLM calls through a select/call loop — explains why selection is hard while still supporting local strategy comparisons
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Bounded-context orchestration model

Two observations motivate this model. First, [context is the scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) in agent systems — the finite window of tokens the agent can attend to, with both volume and complexity costs. Second, there is reason to think that [bookkeeping and semantic work have different error profiles](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — symbolic substrates eliminate all three sources of error for bookkeeping, while LLMs are needed only for semantic judgment. (The second argument is [conjectural](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md); the first is well-established.)

Together these imply a natural architecture: a symbolic scheduler over bounded LLM calls. This is not a restrictive design choice — [any symbolic program with LLM calls is a select/call program](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md), so the model captures the full space of such architectures.

## The model

The model has two components:

- a **symbolic scheduler** over unbounded exact state, which assembles prompts and orchestrates the workflow
- **bounded clean context windows** for each LLM call — the expensive, stochastic operation that the architecture is designed around

The scheduler's state includes source artifacts, prior prompts, and outputs from earlier LLM calls: relevance labels, cluster summaries, extracted claims, sub-goals, partial syntheses. In practice this state may live in files, in-memory structures, databases, or a mix. The operational requirement is simple: accumulated state lives there, not in conversation history; LLM calls do judgment work and return results to code; the next prompt is assembled from stored state rather than from the model's memory of prior turns.

The model also accommodates architectures where the LLM emits a symbolic control program rather than a direct natural-language answer. That still fits as long as execution and state progression remain external to the conversation. A system that keeps bookkeeping inside an LLM conversation is a [degraded variant](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) that spends bounded context on work the symbolic scheduler handles for free.

## The select/call loop

Let:

- `K` be the scheduler's full symbolic state — source artifacts plus everything prior calls have produced
- `t` be the task type of the next call
- `M` be the maximum effective context budget for one call
- `||P||_t` be the effective cost of prompt `P` for task type `t` — token count, compositional difficulty, or both

`K` accumulates over the loop. Whether the scheduler recomputes views on the fly or caches them (indexes, rankings, dependency maps) is an implementation choice — the theory treats both as equivalent. Real orchestrators usually cache.

The cost measure `||·||` is not a universal size metric — it depends on what the call is doing. A synthesis call over six notes is harder than six independent relevance checks at the same token count. [Effective context is task-relative and complexity-relative, not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) develops the empirical case. Writing `||P||_t ≤ M` captures this: the cost measure absorbs task difficulty, while `M` stays fixed. When the task type is held constant, we drop the subscript and write `||P||`.

The scheduler alternates between two kinds of step. **Symbolic steps** happen outside LLM context: file listing, retrieval, sorting, prompt assembly, deduplication. **Agent calls** are bounded LLM invocations under focused prompts.

The `select` function builds a prompt `P` from the current state `K`, subject to the feasibility constraint `||P||_t ≤ M`. This is where the scheduling difficulty lives: `select` must choose both *which* items from `K` to include and *how* to frame them, because the same material, framed differently, lets a bounded reader [extract different amounts of useful structure](./information-value-is-observer-relative.md).

The result `r` is appended back into symbolic state. It need not be a direct answer — it may be a relevance label, claim list, cluster summary, contradiction table, partial synthesis, sub-goal set, or satisfaction signal.

Operationally:

```
while not satisfied(K):
    P  = select(K)
    r  = call(P)
    K  = K + r
```

Real orchestrators routinely fan out parallel calls. Parallelism changes the scheduling problem (the scheduler must merge or arbitrate when parallel results interact), but not the core structure — `select` is still symbolic code assembling prompts from `K`.

Note that `select` may *use* the results of a prior planning call — the LLM returned a plan into `K` in an earlier iteration, and `select` now reads that plan from symbolic state and proceeds deterministically. Hierarchical decomposition is therefore not a separate mechanism but a pattern of use.

## What makes selection hard

The `select` function is where the optimisation lives. The first problem is that selection is sequential, not static, so the task is already closer to a control problem than to a one-shot packing problem:

**Sequential dependence.** Each selection affects future state. A good first iteration might discover that the goal decomposes differently than expected, changing what subsequent iterations should select. This makes the problem sequential — closer to a Markov decision process than a knapsack.

**Dual cost dimensions.** [Context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). Selection must optimise both: include enough to be useful, but frame it so the sub-agent can actually use it.

**Framing matters, not just selection.** The same knowledge, presented differently, has different value to a bounded observer. "Here are six documents, synthesise them" is less useful than "documents A and B establish X, documents C and D contradict it, resolve the tension." Same tokens, different yield for a bounded reader. See [information value is observer-relative](./information-value-is-observer-relative.md).

## Scope and open questions

The full global optimisation problem is probably too rich for clean strategy theorems: goals are [underspecified](./agentic-systems-interpret-underspecified-instructions.md), LLM calls are noisy, the `satisfied` check is itself a judgment call, and the value of including item X depends on the sub-agent's stochastic interpretation. There is no clean objective function. But the model supports **local comparative results** — comparing two concrete strategies or justifying a transformation from one strategy to another. The [decomposition rules](./decomposition-heuristics-for-bounded-context-scheduling.md) catalogue specific transformations that the model shows move a system in the right direction.

- Can the framing decisions within `select` be factored cleanly enough that their cost can be ignored in a first theory and reintroduced later?
- How much selection judgment should the scheduler perform before constructing a bounded call, and how much should be delegated to the LLM inside that call?
- What restrictions on the model (fixed decomposition templates, bounded branching, finite sub-goal depth) yield tractable optimisation while preserving enough expressiveness?
- What heuristics make `select` good in practice?
- When should the orchestrator compress state, offload it to external storage, or delegate to a sub-loop?
- Can the loop be made self-improving — can later iterations learn from the quality of earlier selections? This would connect to [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md).

---

Sources:
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](https://arxiv.org/html/2602.01075v2) — scoped recursion with focused context as a clean-model implementation for compositional reasoning.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors](https://arxiv.org/abs/2511.09030) — maximal decomposition (m=1) as extreme clean-model instantiation; O(s ln s) cost scaling.
- @Vtrivedy10 (2026). [The Anatomy of an Agent Harness](https://x.com/Vtrivedy10/status/2031408954517971368) — the Ralph Loop (prompt → execute → observe → decide) is a concrete instance of the select/call loop; the source's runtime components map to scheduler infrastructure.

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivation: context is the scarce resource with volume and complexity dimensions
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — clarifies: explains why usable context should be modeled relationally rather than as a single per-model capacity
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — foundation: bookkeeping and semantic work have different error profiles across all three phenomena
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the single-step mechanism this note extends to an iterative loop
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative.md) — explains why framing matters in selection
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make each loop iteration independent
- [any symbolic program with LLM calls is a select/call program](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — universality: the model's invariants hold by construction for all programs with symbolic orchestration and bounded LLM calls
- [decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: practical heuristics that follow from the model
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: what happens when the scheduler is itself bounded
- [tool loop](./tool-loop-index.md) — consequence: extracts the main architectural implication of the model for real implementations
- [distillation](./definitions/distillation.md) — mechanism: compaction of K is distillation targeting the orchestrator's context budget
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — complicates: the goal, the satisfaction check, and the sub-agent's interpretation are all underspecified
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalisation response is the workshop pattern
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — component view: names the scheduler as one part of a larger runtime decomposition
- [topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) — extends: argues that the select/call loop's decomposition is the first prerequisite in a dependency chain (topology → isolation → verification)
- [paper outline v2](../work/paper-bounded-context-orchestration/outline-v2.md) — develops: presents this model for an academic audience
