---
description: Formalises agent orchestration as a symbolic scheduler driving bounded LLM calls through a select/call loop — explains why selection is hard while still supporting local strategy comparisons
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model]
---

# Bounded-context orchestration model

This is a model of the **joint LLM-code system**, not a model of a standalone LLM. The system being modeled includes both the symbolic code that owns state and control flow and the bounded LLM calls that perform semantic judgment. The central question is how the code side should schedule, frame, and absorb those calls when no single LLM context window can hold all relevant state.

Two observations motivate this model. First, [context is the scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) in agent systems — the finite window of tokens the agent can attend to, with both volume and complexity costs. Second, there is reason to think that [bookkeeping and semantic work have different error profiles](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — symbolic substrates eliminate all three sources of error for bookkeeping, while LLMs are needed only for semantic judgment. (The second argument is conjectural; the first is well-established.)

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
- `P` be one complete prompt, including both the requested operation and the material selected for that call
- `M` be the maximum effective context budget for one call
- `||P||` be the effective cost of complete prompt `P` — token count, compositional difficulty, task framing, or all three

The cost measure `||·||` is an idealized effective-cost measure over the whole prompt, not just a token count. The cost may depend on the kind of task that `P` describes: a synthesis prompt and a relevance-check prompt can have different effective costs even when they contain the same source material. [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) develops the empirical case for that task dependence.

The loop alternates between symbolic scheduling and bounded LLM calls. Symbolic scheduling happens outside LLM context: file listing, retrieval, sorting, prompt assembly, deduplication, state update, and cache maintenance. LLM calls are the bounded, stochastic steps that perform semantic judgment under focused prompts.

The `select` function either builds a prompt `P` from the current state `K`, subject to the feasibility constraint `||P|| ≤ M`, or returns `None` when the scheduler has no further LLM call to make. This is where the scheduling difficulty lives.

The result `r` is incorporated back into symbolic state as `K + r`. In the minimal event-sourced case this is append-only: `K` is the complete trace, and `select` recomputes any derived view from that trace. Implementations usually cache derived symbolic state, such as indexes, rankings, dependency maps, queues, phase tags, parsed fields, retry metadata, or satisfaction signals. The model treats those caches as part of explicit `K`, not as hidden conversation state.

Operationally:

```
while (P := select(K)) is not None:
    r  = call(P)
    K  = K + r
```

Real orchestrators routinely fan out parallel calls. Parallelism changes the scheduling problem (the scheduler must merge or arbitrate when parallel results interact), but not the core structure: prompts are still selected from `K`, calls still produce results, and results still return to explicit state.

In practice, `select` cannot usually compute `||P||` exactly. It uses heuristics: token counts, known prompt templates, empirical difficulty estimates, prior relevance labels, decomposition plans, or feasibility judgments returned by earlier LLM calls. When an LLM helps judge feasibility or produce a plan, that judgment is itself another bounded call whose result is incorporated into `K`; a later `select` step consumes it symbolically. Hierarchical decomposition is therefore not a separate mechanism, but a pattern of using the same loop recursively.

The ContextProvider pattern is a concrete source-scoped instance of the loop. The parent agent keeps a small action alphabet such as `query_slack` or `update_github`; `select(K)` chooses the source boundary and frames the question or instruction; `call(P)` runs inside a provider sub-agent that owns the raw tools, source quirks, permissions, and optional skills. The article's token and latency claims are not reproducible evidence from the snapshot, but the architecture strongly validates the model's decomposition mechanism: tool complexity can move out of the parent context when a source boundary gives the bounded call a cleaner frame.

## What makes selection hard

The `select` function is where the optimisation lives. The first problem is that selection is sequential, not static, so the task is already closer to a control problem than to a one-shot packing problem:

**Sequential dependence.** Each selection affects future state. A good first iteration might discover that the goal decomposes differently than expected, changing what later iterations should select. This makes the problem closer to a control problem than to one-shot packing.

**Coupled selection and framing.** [Context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). The same knowledge, presented differently, has different value to a bounded observer: "Here are six documents, synthesise them" is less useful than "documents A and B establish X, documents C and D contradict it, resolve the tension." Same tokens, different yield for a bounded reader. See [information value is observer-relative](./information-value-is-observer-relative.md).

## Scope and open questions

The full global optimisation problem is probably too rich for clean strategy theorems: goals are [underspecified](./agentic-systems-interpret-underspecified-instructions.md), LLM calls are noisy, the decision to halt or continue is itself a judgment call inside `select`, and the value of including item X depends on the sub-agent's stochastic interpretation. There is no clean objective function. But the model supports **local comparative results** — comparing two concrete strategies or justifying a transformation from one strategy to another. The [decomposition rules](./decomposition-heuristics-for-bounded-context-scheduling.md) catalogue specific transformations that the model shows move a system in the right direction.

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
- Ashpreet Bedi (2026). [Context providers: the missing layer between agents and tools](../sources/context-providers-the-missing-layer-between-agents-and-tools.ingest.md) — source-scoped provider sub-agents instantiate `select/call` by hiding raw tool surfaces behind bounded query/update calls.

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivation: context is the scarce resource with volume and complexity dimensions
- [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: usable context is a task-dependent degradation surface, modeled relationally rather than as a single per-model capacity
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — foundation: bookkeeping and semantic work have different error profiles across all three phenomena
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the single-step mechanism this note extends to an iterative loop
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative.md) — explains why framing matters in selection
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make each loop iteration independent
- [any symbolic program with LLM calls is a select/call program](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — universality: the model's invariants hold by construction for all programs with symbolic orchestration and bounded LLM calls
- [decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — consequence: practical heuristics that follow from the model
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: what happens when the scheduler is itself bounded
- [tool loop](./tool-loop-README.md) — consequence: extracts the main architectural implication of the model for real implementations
- [distillation](./definitions/distillation.md) — mechanism: compaction of K is distillation targeting the orchestrator's context budget
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — complicates: the goal, the halt/continue decision, and the sub-agent's interpretation are all underspecified
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalisation response is the workshop pattern
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — component view: names the scheduler as one part of a larger runtime decomposition
- [topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — extends: argues that the select/call loop's decomposition is the first prerequisite in a dependency chain (topology → isolation → verification)
