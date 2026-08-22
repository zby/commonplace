---
description: Defines a conditional batched select/call form for closed-world LLM orchestration, including its state, barrier, feasibility, and comparison boundaries
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model]
---

# Bounded-context orchestration model

Closed-world LLM workflows admit a batched select/call normal form when they meet three conditions. Their non-LLM execution between batch barriers is symbolic. Their transition-relevant state is explicit. Calls released in the same batch do not affect one another before the barrier. Under these conditions, code selects a nonempty batch, runs its calls concurrently, waits for all of them, records their results, and selects again. A singleton batch represents sequential execution. No one call must receive the full workflow state.

The form represents qualifying workflows; it does not rank orchestration architectures. It exposes selection as a policy that designers can compare. Any comparison must identify what remains fixed and what outcome should improve.

## Why separate the scheduler from the calls

Designers may choose an external symbolic scheduler for two reasons. First, [context is scarce](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). Prompt capacity and soft degradation limit the evidence and complexity that one call can use, while external state can retain more than the call receives. Second, code can apply fully specified transitions without the stochastic omissions and mutations that LLM bookkeeping can introduce. Whether this difference yields a net reliability advantage remains [conjectural](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), because code also creates specification, maintenance, synchronization, and interface costs. These reasons motivate the architecture; they do not prove that it is superior.

## The model

The form has six elements:

- **Scheduler state `K`** stores source artifacts, control position, and retained results outside any one call's context window.
- **Call specification `C`** identifies a prompt, task, model, and any execution capabilities that can change the call's behavior.
- **Batch `B = (C_1, ..., C_n)`** groups a finite, nonempty indexed family of call specifications selected from the same state. Its members have no transition-relevant interaction before the batch barrier.
- **`select(K)`** returns the next batch. It returns `None` when no more LLM calls should run.
- **`call_all(B)`** runs every `call(C_i)` concurrently. After all calls finish, it returns the aligned results `R = (r_1, ..., r_n)`.
- **`transition(K, B, R)`** records the completed results and advances the scheduler state.

The loop treats prompt feasibility as a relation among a call's complete prompt, task, model, and required performance threshold. The form does not reduce this relation to one measurable scalar. Token count, compositional difficulty, and task framing can each affect it, and [soft degradation can bind before a hard context cap](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md). In practice, `select` estimates feasibility from token counts, known prompt templates, empirical results, or earlier bounded judgments.

The minimal loop is:

```
while (B := select(K)) is not None:
    require independent(B, K)
    require all(feasible(C.prompt, C.task, C.model) for C in B)
    R = call_all(B)
    K = transition(K, B, R)
```

The [conversion lemma](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md) collapses symbolic non-call execution into `select` when `K` stores the complete resumable machine state. Branches, retries, queues, phase tags, cached views, and nested loops become data in `K` and rules in `select` or `transition`. The conversion preserves batch membership and barrier order, so it does not turn parallel calls into serial calls.

## Cases inside the form

A batch with more than one member represents parallel calls. It contains the independent calls released together at one barrier, not every call that could ever overlap. `call_all` waits for all members, and `transition` applies an explicit merge or arbitration rule to their aligned results.

LLM-assisted planning also fits. A planning call returns a result in `R`; `transition` records the plan in `K`; and a later `select` consumes it. Hierarchical decomposition repeats the same loop rather than introducing a different mechanism.

The ContextProvider pattern is a source-scoped singleton-batch instance. A parent offers a small action set such as `query_slack`, and `select(K)` chooses the source boundary and frames the request. A provider sub-agent owns the raw tools, source quirks, permissions, and optional skills used by its `call(C)`. The source supplies no reproducible token or latency evidence, so it illustrates the decomposition without establishing its efficacy.

## Boundary

The form excludes interactions that cross its barriers. One batch cannot contain calls whose streams, results, or transition-relevant side effects influence one another before completion. A tool-using call fits only when the scheduler observes its transition-relevant effects at the barrier and no hidden interaction occurs within the batch.

The form also assumes a closed world and shared barriers. `K` cannot exactly represent an environment that changes independently between observations, and the loop cannot preserve staggered overlaps that have no shared barrier. Streaming interaction, staggered overlap, and independently mutable environments require a richer event-driven or environment-state model.

## What makes selection hard

**Adaptive results create sequential dependence.** A completed batch can reveal that the goal decomposes differently than expected. That result may change every later selection. Static evaluation sweeps mark the opposite limit: designers can choose every batch and merge rule in advance.

**Selection and framing are coupled.** Prompt cost and effectiveness depend on token volume, compositional difficulty, task framing, and the requested operation. The same documents can produce different results when one prompt merely presents them and another names a relation to test or resolve. Because [information value is observer-relative](./information-value-is-observer-relative.md), a scheduler cannot generally optimize material selection independently of task framing.

## Comparing selection strategies

The form supplies no objective function. To compare two selection strategies, hold relevant semantics or evidence coverage fixed and state what should improve. Possible criteria include task success under a prompt budget, reliability under a latency bound, and auditability at a fixed success threshold. Without a criterion, the claim that a transformation moves “in the right direction” has no determinate meaning. The [decomposition rules](./decomposition-heuristics-for-bounded-context-scheduling.md) propose transformations; tests against a stated criterion determine their value.

## Scope and open questions

The form applies most directly to closed-world, barriered-call workflows with explicit resumable state. The representation does not imply one global objective. Goals are [underspecified](./agentic-systems-interpret-underspecified-instructions.md), calls are stochastic, and latency, context cost, reliability, and auditability trade off. The form instead gives scoped comparisons a shared vocabulary for their invariants and criteria.

- Which task- and model-relative feasibility predicates predict successful calls well enough to guide `select`?
- When should an orchestrator retain, compress, or discard explicit state?
- Which restrictions on branching, decomposition depth, or call interaction yield tractable strategy comparisons?
- What event-driven extension preserves useful select/call structure for streaming calls and independently mutable environments?

---

Sources:

- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](https://arxiv.org/html/2602.01075v2) — scoped recursion with focused context as an implementation for compositional reasoning.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors](https://arxiv.org/abs/2511.09030) — maximal one-question decomposition as an extreme singleton-batch instance with near-linearithmic cost scaling in the reported setting.
- @Vtrivedy10 (2026). [The Anatomy of an Agent Harness](https://x.com/Vtrivedy10/status/2031408954517971368) — the Ralph Loop is a concrete prompt-execute-observe-decide instance; its runtime components map to scheduler infrastructure.
- Ashpreet Bedi (2026). [Context providers: the missing layer between agents and tools](../sources/context-providers-the-missing-layer-between-agents-and-tools.ingest.md) — source-scoped provider sub-agents instantiate select/call by hiding raw tool surfaces behind bounded query or update calls.

Relevant Notes:

- [Soft degradation often binds before the hard cap when required evidence fits](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — grounds: usable context is a task-dependent degradation surface rather than a single per-model capacity
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: bookkeeping and semantic work have different conjectured error profiles
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the single-step mechanism this note extends to an iterative loop
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make loop iterations independent
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — extends: conversation-held scheduling spends bounded context on state progression
- [Tool loop](./tool-loop-README.md) — extends: develops the model's main architectural implication for implementations
- [Theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — mechanism: the orchestrator receives a compact task-facing view while fuller state remains available
- [A functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: the workshop is a KB-specific instance of keeping retained state outside bounded calls
- [Agent-runtime analysis should separate scheduling, context assembly, and external state](./agent-runtime-analysis-should-separate-scheduling-context-state.md) — extends: separates scheduling from context assembly and external state inside the broader form
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — extends: places decomposition first in a topology-isolation-verification chain
