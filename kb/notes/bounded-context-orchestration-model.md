---
description: Formalises agent orchestration as a symbolic scheduler driving bounded LLM calls through a select/call/absorb loop — analyses what makes selection hard and why the model supports local comparative results even when global optimisation is intractable
type: note
traits: [has-external-sources]
areas: [computational-model]
status: seedling
---

# Bounded-context orchestration model

Since [context is the scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), agent orchestration is fundamentally about selecting what goes into each bounded context window — what to include, how to frame it, and when to stop.

Many agent tasks share the surface shape of a classical bounded-working-set problem: a large symbolic state, a small working window, and a need to decide what to expose to each bounded call so the task remains feasible. Symbolic bookkeeping, exact state storage, and deterministic control are cheap and effectively unbounded — they have latency and engineering cost, but not *context* cost — and should be idealised away when asking what such systems can ultimately do.

The closest classical analogy is a two-level I/O model: a large exact store and a bounded working set. But classical I/O models assume a fixed computation DAG, unchanged data, and deterministic operations. Agent orchestration differs in four ways. First, the DAG is partly a choice — the orchestrator may insert new nodes like "check relevance of note N" or "summarise cluster C," creating new computation rather than scheduling existing computation. Second, representation choice matters — intermediate artifacts are lossy, task-shaped compressions, and framing matters as much as selection: the same material presented differently yields different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md). The key decision is not only "which values should occupy the bounded call?" but "which values should exist in symbolic state at all?" Third, bounded calls are stochastic — they have a per-step error rate that compounds across calls, so the scheduler must account for reliability, not just selection and framing. Fourth, external state is mutable — tool calls interact with changing environments (web pages, APIs, user actions), so the scheduler cannot assume data read once stays valid.

This is closer to I/O-like scheduling over a dynamically constructed, lossy computation graph than to classical pebbling on a fixed DAG. The model below makes the resulting structure explicit.

## The model

The model has two components:

- a **symbolic scheduler** over unbounded exact state, which assembles prompts and orchestrates the workflow — items in that state may be source artifacts or lossy derived artifacts (relevance labels, cluster summaries, extracted claims) produced by earlier LLM calls
- **bounded clean context windows** for each LLM call — the only expensive, stochastic operation

Bookkeeping and prompt assembly belong in the symbolic scheduler, not in LLM calls. The scheduler can hold unlimited state, perform arbitrary deterministic computation, read and write files, and assemble prompts. The only thing it cannot do is semantic judgment — for that, it schedules an LLM call. LLMs are good at semantic judgment; they are bad at bookkeeping. The bookkeeping that recursive decomposition demands — tracking processed items, collecting results, managing the recursion stack — is exactly the wrong task for an LLM.

In practice, the scheduler's symbolic state may be implemented using files, in-memory structures, databases, or a mix. The model abstracts over that representation. What matters operationally is that the orchestrator should:

- hold accumulated state in program variables or files, not in an LLM conversation history
- use LLM calls for judgment (relevance, decomposition, synthesis) but return results to code
- assemble the next prompt symbolically from stored results, not by relying on the LLM to remember prior steps

The model also accommodates architectures where the LLM emits a symbolic control program rather than a direct natural-language answer; the scheduler executes that program, using it to inspect symbolic state, manipulate artifacts, and trigger further bounded LLM calls. The symbolic scheduler remains the exact stateful substrate while the LLM supplies control decisions within it.

[Frontloading](./frontloading-spares-execution-context.md) is the single-step case of this separation: pre-compute static parts, insert results, hand to the LLM. But real agentic work is not a single step — the caller discovers what's relevant, delegates a piece, absorbs results, discovers more, delegates again. The single frontloading step generalises to the loop formalised below.

## The select/call/absorb loop

Let:

- `K` be the scheduler's full symbolic state — this includes source artifacts, derived artifacts, and goals (the user's top-level goal is simply the initial item in `K`; sub-goals produced by decomposition calls are further items)
- each item `x ∈ K` have symbolic structure and, where relevant, token size `s(x)` when rendered into an LLM call
- `M` be the maximum context size of one agent call

There are two kinds of computation:

**Symbolic steps.** Deterministic procedures outside LLM context: file listing, retrieval by name, sorting, thresholding, prompt assembly, deduplication. In the simplest model these are cheap and unbounded.

**Agent calls.** Each call has:

- a task `τ`
- a prompt constructor `φ`

The constructor builds the actual prompt:

`P = φ(τ, K)`

subject to the feasibility constraint:

`|P| ≤ M`

The constructor `φ` is a first-class decision variable, not mere plumbing — choosing *how* to render state into a prompt matters as much as choosing *which* state to include, because the same material under different framing yields different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md). The section on selection difficulty below develops this point.

Executing the call produces one or more new items `r`, absorbed back into symbolic state. The crucial point is that `r` need not be a direct answer — it can be a relevance label, extracted claim list, cluster summary, contradiction table, partial synthesis, or a set of sub-goals. These are newly materialised items chosen because they are cheap to reuse later and useful under bounded context.

Operationally, the scheduler drives a loop:

```
K₀ = initial symbolic state (including goal)
for i = 1, 2, ...
    (φᵢ, τᵢ)  = select(Kᵢ₋₁)        # choose task from K
    rᵢ         = call(φᵢ(τᵢ, Kᵢ₋₁))  # bounded LLM call
    Kᵢ         = absorb(Kᵢ₋₁, rᵢ)    # may add sub-goals, artifacts, or answers
    if satisfied(Kᵢ): return
```

The loop is written as sequential for clarity, but real orchestrators routinely fan out parallel calls — multiple `call` invocations running concurrently, with `absorb` merging their results. Parallelism changes the scheduling problem (which calls can run independently?) but not the core structure.

An equivalent recursive presentation is:

```
solve(K):
    if satisfied(K):
        return K

    (φ, τ) = select(K)
    r      = call(φ(τ, K))
    K'     = absorb(K, r)

    return solve(K')
```

These are two presentations of the same underlying model: iterative state transition and recursive control with state threaded through calls.

The `select` step is where most of the scheduling difficulty concentrates — it must choose both the task and the symbolic procedure that turns scheduler state into a bounded call. `select` itself remains symbolic. When the scheduler cannot determine the next step deterministically, it can symbolically choose a *planning call* — an ordinary iteration whose result `r` is a set of sub-goals absorbed into `K`. Subsequent `select` steps read those sub-goals from `K` and proceed deterministically. Hierarchical decomposition is therefore not a separate mechanism but a pattern of use: some iterations produce task items, others produce control structure, and the flat loop handles both uniformly.

A system that keeps bookkeeping inside an LLM conversation — tracking processed items, assembling prompts, managing the recursion stack — is not a different fundamental model; it is a [degraded variant of this one](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) that spends bounded context on work the symbolic scheduler handles for free. The degradation is qualitative, not just inefficient: the scheduler itself becomes a bounded observer, suffering the same attention dilution and compositional overhead that motivates sub-agent isolation in the first place. The clean model reveals what the most efficient system in this regime looks like: one that devotes bounded LLM calls only to the semantic judgments they are uniquely needed for.

## What makes selection hard

The `select` function is where the optimisation lives. It is not a simple knapsack problem (fitting the most valuable items into capacity M) for several reasons:

**Framing matters, not just selection.** The same knowledge, presented differently, has different value to a bounded observer. "Here are six documents, synthesise them" is less useful than "documents A and B establish X, documents C and D contradict it, resolve the tension." Same information, different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md). The sub-agent's bounded extraction capacity determines what's worth including *and how*.

**Dual cost dimensions.** [Context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). Selection must optimise both: include enough to be useful, but frame it so the sub-agent can actually use it. Overloading a sub-agent with raw material wastes context even if it fits in the window.

**Sequential dependence.** Each selection affects future state. A good first iteration might discover that the goal decomposes differently than expected, changing what subsequent iterations should select. This makes the problem sequential, not static — closer to a Markov decision process than a knapsack.

**The selector is itself bounded.** The orchestrator that runs `select` is also a bounded observer. As K grows, the orchestrator's ability to choose well may degrade — the same [compositional reasoning gap](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) that motivates sub-agent isolation applies to the orchestrator itself. This creates a fundamental tension: the orchestrator needs accumulated knowledge (large K) to make good selections, but accumulated context degrades its judgment.

Four responses to this dilemma:

1. **Compaction.** Keep summaries, conclusions, and pointers rather than raw results. K grows in items but not proportionally in tokens. This is [distillation](./distillation.md) applied to the orchestrator's own state.

2. **Externalisation.** Write intermediate state to disk (notes, logs, structured artifacts). The orchestrator re-reads selectively rather than holding everything in context. This is what the KB already does — notes are externalised orchestrator state.

3. **Re-derivation.** Keep K small and re-run earlier sub-tasks when their results are needed. Trades compute for context, accepting redundant execution to avoid context degradation.

4. **Recursion.** Delegate the orchestrator's own `select` step to a sub-orchestrator with a clean window. The loop becomes a tree: each node is a select-call-absorb cycle, and nodes can spawn children. A flat loop is the single-level case; recursion extends the pattern to the orchestrator itself.

## Why selection dominates

The loop has four functions: `select`, `call`, `absorb`, and `satisfied`. All four affect outcome quality. But for a given model and toolset, selection dominates the variance:

- **Call is constrained by select.** A sub-agent can only work with what it receives — [sub-agents run in clean context frames](./llm-context-is-composed-without-scoping.md) with only what the orchestrator chose to include. Selection sets the ceiling; execution determines how close you get.
- **Absorb is selection applied to results.** Deciding what to keep from results exercises the same judgment as deciding what to include — both are filtering under bounded context. The mechanism is [distillation](./distillation.md) (targeted extraction shaped by the orchestrator's context budget). Not every absorption is distillation — raw appending is possible — but effective absorption under bounded context requires it, and poor absorption degrades future selections.
- **Satisfied is typically lightweight.** Knowing when to stop matters, but for most tasks it is a cheaper judgment than per-iteration selection. (Exception: verification-heavy tasks where the satisfaction check itself dominates — correctness proofs, completeness checks, multi-criteria evaluation.)

This argument is conditional on a fixed model. Across models, execution quality also matters — a weaker model extracts less from the same selection. The claim is about what the orchestrator controls, not about what is universally true.

## The canonical note-selection example

Suppose the task is: given many notes, find the relevant ones and write an analysis. The full set of notes does not fit in one context window.

Traced through the loop:

`K₀` contains the goal "analyse these notes" and the note files. `select(K₀)` cannot construct a single synthesis call — the notes exceed `M` — so it emits a planning call that decomposes the goal into per-note filter sub-goals.

```
K₀ = {goal: "analyse notes", notes: [n₁ ... nₖ]}

iteration 1:  planning call → K₁ adds sub-goals [filter(n₁), ..., filter(nₖ)]

iterations 2..k+1:  select picks each filter sub-goal in turn
    filter(nᵢ) reads one note, produces a relevance artifact
    (relevant/not, rationale, extracted claims)
    → absorbed into K

iteration k+2:  select sees all filter sub-goals resolved
    symbolically collects notes marked relevant
    if |relevant notes| ≤ M:
        synthesis call over relevant notes → done
    else:
        planning call → adds sub-goals [cluster, summarise, synthesise]

remaining iterations:
    cluster (symbolic or LLM-assisted) → cluster assignments in K
    for each cluster: summarise call → cluster summary in K
    synthesis call over cluster summaries → final answer
```

Every step — planning, filtering, clustering, summarising, synthesising — is an iteration of the same flat loop. The hierarchical structure exists only as sub-goals and artifacts in `K`. Several [decomposition rules](./decomposition-rules-for-bounded-context-scheduling.md) generalise from this pattern.

## Empirical exemplars

Two sources demonstrate the clean model in practice.

ConvexBench ([Liu et al., 2026](../sources/convexbench-can-llms-recognize-convex-functions.md)) implements the model for compositional convex-function verification. The symbolic scheduler decomposes nested functions into an AST, then issues bounded LLM calls for each sub-function with only its direct dependencies in context. This "agentic reasoning with focused context" recovers F1=1.0 at all composition depths from F1≈0.2 under flat accumulation — despite using only 5,331 tokens. The scheduler handles decomposition, dependency tracking, and result assembly; the LLM handles only the semantic judgment ("is this sub-function convex?").

MAKER ([Meyerson et al., 2025](../sources/meyerson-maker-million-step-llm-zero-errors.md)) pushes the model to its extreme: maximal decomposition (m=1, one step per bounded call) solves 1,048,575-step Towers of Hanoi with zero errors. The symbolic scheduler holds the full state (disk positions, move history), constructs each prompt with only the current configuration, and applies voting and red-flagging to LLM responses before absorbing results. Two properties jointly produce the O(s ln s) cost scaling: clean separation (each bounded call receives only the current configuration, so per-step reliability stays constant as task length grows) and error correction (the scheduler applies first-to-ahead-by-k voting across independent samples, requiring k_min = O(ln s) votes per step to maintain target success probability). Without error correction, even maximal decomposition yields success probability decaying exponentially in s. Without clean separation, per-step reliability degrades with accumulated context, making error correction progressively more expensive. Single-agent approaches, which lack both properties, degrade exponentially.

Among reviewed systems, [Spacebot](./related-systems/spacebot.md) is the closest production implementation to the clean model. Its cortex is a Rust-level symbolic scheduler — pure code, no LLM calls for scheduling decisions — driving bounded LLM calls in channels and branches while workers handle deterministic tool execution. The cortex tracks process health via a rolling signal buffer, enforces timeouts, and trips circuit breakers, all in the type system rather than in prompts.

## Scope and open questions

The full global optimisation problem is probably too rich for clean strategy theorems: goals are [underspecified](./agentic-systems-interpret-underspecified-instructions.md), LLM calls are noisy, the `satisfied` check is itself a judgment call, and the value of including item X depends on the sub-agent's stochastic interpretation. There is no clean objective function. But the model is still strong enough to support **local comparative results** — comparing two concrete strategies or justifying a transformation from one strategy to another.

Frontloading is the clearest example. If a sub-procedure can be executed before the bounded LLM call without using the LLM's runtime state, then replacing that in-call derivation with its result weakly improves context usage and usually improves reliability. The model is therefore useful not for asking "what is the globally best scheduler?" but for proving that specific transformations — frontloading, externalisation, clean frame isolation, saving reusable derived items — move a system in the right direction. The mathematical framing illuminates the *structure* of the problem (sequential, dual-cost, bounded-observer) even though the objective is not precisely measurable.

- Can prompt constructors be factored cleanly enough that their cost can be ignored in a first theory and reintroduced later?
- How much selection judgment should the scheduler perform before constructing a bounded call, and how much should be delegated to the LLM inside that call?
- Can the stochastic, underspecified semantics of agent calls be modelled as noisy operators on items in `K` without losing the main scheduling insights?
- What restrictions on the model (fixed decomposition templates, bounded branching, finite sub-goal depth) yield tractable optimisation while preserving enough expressiveness to cover practical agent tasks?
- What heuristics make `select` good in practice? Workshop experiments suggest: include the goal, include relevant documents with annotations explaining why they matter, include discovered connections. Is there a more systematic approach?
- When should the orchestrator compact vs externalise vs recurse? These seem like different regimes — small K favours holding in context, medium K favours compaction, large K favours externalisation or recursion.
- Can the loop be made self-improving — can later iterations learn from the quality of earlier selections? This would connect to [deploy-time learning](./deploy-time-learning-the-missing-middle.md).

---

Sources:
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](../sources/convexbench-can-llms-recognize-convex-functions.md) — scoped recursion with focused context as a clean-model implementation for compositional reasoning.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors](../sources/meyerson-maker-million-step-llm-zero-errors.md) — maximal decomposition (m=1) as extreme clean-model instantiation; O(s ln s) cost scaling.

Relevant Notes:

- [frontloading spares execution context](./frontloading-spares-execution-context.md) — foundation: the single-step mechanism this note extends to an iterative loop
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — cost model: context is the scarce resource and has both volume and complexity dimensions
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative-because-extraction-requires-computation.md) — explains why framing matters in selection — the same information has different value depending on how it's presented to a bounded observer
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make each loop iteration independent
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — enables: homoiconicity is what makes each iteration partial evaluation rather than just divide-and-conquer
- [decomposition rules for bounded-context scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — consequence: preliminary practical rules that follow from the model
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: what happens when the scheduler is itself bounded, and three recovery strategies
- [distillation](./distillation.md) — mechanism: the absorb step is distillation targeting the orchestrator's context budget
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — complicates: the goal, the satisfaction check, and the sub-agent's interpretation are all underspecified, preventing clean objective functions
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalisation response (writing intermediate state to disk) is the workshop pattern

Topics:

- [computational-model](./computational-model.md)
