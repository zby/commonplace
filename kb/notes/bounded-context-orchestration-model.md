---
description: Represents closed-world orchestration as explicit scheduler state plus completed bounded LLM calls, and explains why strategy comparisons need stated invariants and criteria
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model]
---

# Bounded-context orchestration model

A joint LLM-code system admits a select/call normal form when all inter-call execution is symbolic, all transition-relevant state is explicit, and each LLM call completes before its result affects later scheduling. Under these conditions, code selects a feasible call from the current state, waits for the LLM result, incorporates it, and selects again. The full state need not fit within any one LLM context window.

This normal form represents the joint system; it does not establish that one orchestration architecture is best. It makes selection a surface for comparing concrete strategies, but any comparison must state both what the strategies preserve and what objective or constraint orders them.

Two observations motivate an external symbolic scheduler. First, [context is the scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) for an LLM call: finite prompt capacity and soft degradation limit the evidence and complexity available to the call. Second, fully specified, code-owned transitions avoid the stochastic omissions and mutations that LLM bookkeeping can introduce. This second architectural advantage remains [conjectural](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), because exact code brings its own specification, maintenance, synchronization, and interface costs. These observations motivate the architecture; neither follows from the normal form itself.

## The model

The model uses four elements:

- **Explicit scheduler state `K`** contains source artifacts, control position, and retained results outside the per-call context window.
- **A call specification `C`** identifies the prompt, task, model, and any execution capabilities that can change the call's behavior.
- **`select(K)`** returns the next call specification or `None` when no further LLM call should run.
- **`transition(K, C, r)`** incorporates the completed result `r` and advances the explicit state.

Prompt feasibility is a relation among the complete prompt, task, model, and required performance threshold; the model does not reduce it to a single measurable scalar. Token count, compositional difficulty, and task framing can all affect feasibility, and [soft degradation can bind before a hard context cap](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md). In practice, `select` estimates feasibility from token counts, known prompt templates, empirical results, or earlier bounded judgments.

The minimal loop is:

```
while (C := select(K)) is not None:
    require feasible(C.prompt, C.task, C.model)
    r = call(C)
    K = transition(K, C, r)
```

This loop is a conditional normal form. [Inter-call symbolic execution can be collapsed into `select`](./any-symbolic-program-with-llm-calls-is-a-select-call-program.md) when `K` represents the complete resumable machine state. Branches, retries, queues, phase tags, cached views, and nested sub-loops are encoded as symbolic state and transitions.

Parallel calls fit when the scheduler selects an independent batch from `K`, waits for every result to complete, and applies an explicit merge or arbitration rule. LLM-assisted planning also fits: a plan is another bounded result incorporated into `K` before a later selection consumes it. Hierarchical decomposition is therefore repeated use of the same loop rather than a separate mechanism.

The boundary matters. The loop excludes calls whose streams influence one another before either call completes. Nor can `K` exactly represent an environment that changes independently between observations. A tool-using call fits only when its transition-relevant effects are observed and incorporated before the next selection. Streaming interaction and independently mutable environments require a richer event-driven or environment-state model.

The ContextProvider pattern is one source-scoped instance. A parent offers a small action set such as `query_slack`, while `select(K)` chooses the source boundary and frames the request. A provider sub-agent owns the raw tools, source quirks, permissions, and optional skills used by `call(C)`. The source provides no reproducible token or latency evidence, so the example illustrates the decomposition without validating its general efficacy.

## What makes selection hard

**Sequential dependence in adaptive workflows.** A completed call can reveal that the goal decomposes differently than expected and thereby change every later selection. Static evaluation sweeps are the limiting case: every call and merge rule can be chosen in advance.

**Coupled selection and framing.** Prompt cost and effectiveness depend on token volume, compositional difficulty, task framing, and the requested operation. The same documents can yield different results when one prompt merely presents them while another identifies a justified relation to test or resolve. Because [information value is observer-relative](./information-value-is-observer-relative.md), material selection and task framing cannot generally be optimized independently.

## Comparing selection strategies

The model does not order strategies by itself. A local comparison must hold relevant semantics or evidence coverage fixed, then state what improves: for example, task success under a prompt budget, reliability under a latency bound, or auditability at a fixed success threshold. Without such a criterion, saying that a transformation moves “in the right direction” has no determinate content. The [decomposition rules](./decomposition-heuristics-for-bounded-context-scheduling.md) are candidate transformations whose value must be tested against a stated criterion.

## Scope and open questions

The model is most useful for closed-world, completed-call workflows with explicit resumable state. Such workflows are unlikely to admit one useful global objective: goals are [underspecified](./agentic-systems-interpret-underspecified-instructions.md), calls are stochastic, and latency, context cost, reliability, and auditability trade off. Instead, the model supplies a common representation in which scoped comparisons can state their own invariants and ordering criteria.

- Which task- and model-relative feasibility predicates predict successful calls well enough to guide `select`?
- When should an orchestrator retain, compress, or discard explicit state?
- Which restrictions on branching, decomposition depth, or call interaction yield tractable strategy comparisons?
- What event-driven extension preserves useful select/call structure for streaming calls and independently mutable environments?

---

Sources:

- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](https://arxiv.org/html/2602.01075v2) — scoped recursion with focused context as an implementation for compositional reasoning.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors](https://arxiv.org/abs/2511.09030) — maximal one-question decomposition as an extreme clean-model instance with near-linearithmic cost scaling in the reported setting.
- @Vtrivedy10 (2026). [The Anatomy of an Agent Harness](https://x.com/Vtrivedy10/status/2031408954517971368) — the Ralph Loop is a concrete prompt-execute-observe-decide instance; its runtime components map to scheduler infrastructure.
- Ashpreet Bedi (2026). [Context providers: the missing layer between agents and tools](../sources/context-providers-the-missing-layer-between-agents-and-tools.ingest.md) — source-scoped provider sub-agents instantiate select/call by hiding raw tool surfaces behind bounded query or update calls.

Relevant Notes:

- [Soft degradation often binds before the hard cap when required evidence fits](./soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — grounds: usable context is a task-dependent degradation surface rather than a single per-model capacity
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — foundation: bookkeeping and semantic work have different conjectured error profiles
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the single-step mechanism this note extends to an iterative loop
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make loop iterations independent
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: conversation-held scheduling spends bounded context on state progression
- [Tool loop](./tool-loop-README.md) — consequence: extracts the main architectural implication for implementations
- [Theory and methodology form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — mechanism: the orchestrator receives a compact task-facing view while fuller state remains available
- [A functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalization response is the workshop pattern
- [Agent-runtime analysis should separate scheduling, context assembly, and external state](./agent-runtime-analysis-should-separate-scheduling-context-state.md) — component view: separates scheduling from context assembly and external state
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — extends: places decomposition first in a topology-isolation-verification chain
