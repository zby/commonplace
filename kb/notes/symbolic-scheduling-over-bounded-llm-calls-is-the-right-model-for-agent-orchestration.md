---
description: Agent orchestration is best modelled as an unbounded symbolic scheduler making bounded LLM calls; the scheduler chooses decompositions, prompt representations, and intermediate artifacts over its evolving symbolic state
type: note
traits: []
areas: [computational-model]
status: seedling
---

# Symbolic scheduling over bounded LLM calls is the right model for agent orchestration

Many agent tasks have the same surface shape as a classical bounded-working-set problem: there is a large symbolic state, a small working context window, and a need to decide what to expose to each bounded call so the task remains feasible. The central bottleneck is bounded LLM context — what can be jointly loaded, attended to, and semantically processed in one call. Symbolic bookkeeping, exact state storage, and deterministic control are not the fundamental constraint; they are cheap and effectively unbounded (they have latency and engineering cost, but not *context* cost), and should be idealised away when asking what such systems can ultimately do.

This determines the right model and the right optimisation problem. Given unbounded symbolic computation and storage, what can be computed with bounded LLM calls, and how should those calls be selected, decomposed, and framed to maximise capability?

This note takes [context efficiency as the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) as its cost model and asks what computational model follows if context is the only fundamental bounded resource.

## The model

The model has two components:

- a symbolic scheduler over unbounded exact state, which assembles prompts and orchestrates the workflow — items in that state may be source artifacts or lossy derived artifacts (relevance labels, cluster summaries, extracted claims) produced by earlier LLM calls
- bounded clean context windows for each LLM call — the only expensive, stochastic operation

Bookkeeping and prompt assembly belong in the symbolic scheduler, not in LLM calls. The scheduler can hold unlimited state, perform arbitrary deterministic computation, read and write files, and assemble prompts. The only thing it cannot do is semantic judgment — for that, it schedules an LLM call. LLMs are good at semantic judgment; they are bad at bookkeeping. The bookkeeping that recursive decomposition demands — tracking processed items, collecting results, managing the recursion stack — is exactly the wrong task for an LLM.

In practice, the scheduler's symbolic state may be implemented using files, in-memory structures, databases, or a mix of these. The model abstracts over that representation.

In practice this means the orchestrator should:

- hold accumulated state in program variables or files, not in an LLM conversation history
- use LLM calls for judgment (relevance, decomposition, synthesis) but return results to code
- assemble the next prompt symbolically from stored results, not by relying on the LLM to remember prior steps

This model also accommodates architectures where the LLM emits a symbolic control program rather than a direct natural-language answer; the scheduler executes that program, using it to inspect symbolic state, manipulate artifacts, and trigger further bounded LLM calls. The symbolic scheduler remains the exact stateful substrate, while the LLM supplies control decisions within it.

## Classical intuition and where it breaks

The closest classical intuition is a two-level I/O model: there is a large exact symbolic state, but only a bounded slice of it can be exposed to an LLM call at once.

But classical I/O models assume a fixed computation DAG and unchanged data. Agent orchestration differs in two ways. First, the DAG is partly a choice — the orchestrator may insert new nodes like "check relevance of note N" or "summarise cluster C", creating new computation rather than scheduling existing computation. Second, representation choice matters — intermediate artifacts are lossy, task-shaped compressions, and framing matters as much as selection: same material presented differently yields different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md). The key decision is not only "which values should occupy the bounded call?" but "which values should exist in symbolic state at all?"

This is closer to "I/O-like scheduling over a dynamically constructed, lossy computation graph" than to classical pebbling on a fixed DAG.

## A minimal model

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

The constructor `φ` is not mere plumbing — it is a first-class decision variable. The same material presented under a different framing yields different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md), so choosing *how* to render state into a prompt matters as much as choosing *which* state to include.

Executing the call produces one or more new items `r`, which are absorbed back into symbolic state. The crucial point is that `r` need not be a direct answer — it can be a relevance label, extracted claim list, cluster summary, contradiction table, partial synthesis, or a set of sub-goals. These are newly materialised items chosen because they are cheap to reuse later and useful under bounded context.

Operationally, the scheduler drives a loop:

```
K₀ = initial symbolic state (including goal)
for i = 1, 2, ...
    (φᵢ, τᵢ)  = select(Kᵢ₋₁)        # choose task from K
    rᵢ         = call(φᵢ(τᵢ, Kᵢ₋₁))  # bounded LLM call
    Kᵢ         = absorb(Kᵢ₋₁, rᵢ)    # may add sub-goals, artifacts, or answers
    if satisfied(Kᵢ): return
```

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

The `select` step is where the entire difficulty concentrates — it must choose both the task and the symbolic procedure that turns scheduler state into a bounded call. `select` itself remains symbolic. When the scheduler cannot determine the next step deterministically, it can symbolically choose a *planning call* — an ordinary iteration whose result `r` is a set of sub-goals absorbed into `K`. Subsequent `select` steps read those sub-goals from `K` and proceed deterministically. Hierarchical decomposition is therefore not a separate mechanism but a pattern of use: some iterations produce task items, others produce control structure, and the flat loop handles both uniformly.

A system that keeps bookkeeping inside an LLM conversation — tracking processed items, assembling prompts, managing the recursion stack — is not a different fundamental model; it is an [inefficient implementation of this one](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), spending bounded context on work the symbolic scheduler handles for free. The clean model reveals what the most efficient system in this regime looks like: one that devotes bounded LLM calls only to the semantic judgments they are uniquely needed for.

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

## Open Questions

- Can prompt constructors be factored cleanly enough that their cost can be ignored in a first theory and reintroduced later?
- How much selection judgment should the scheduler perform before constructing a bounded call, and how much should be delegated to the LLM inside that call?
- Can the stochastic, underspecified semantics of agent calls be modelled as noisy operators on items in `K` without losing the main scheduling insights?
- What restrictions on the model (fixed decomposition templates, bounded branching, finite sub-goal depth) yield tractable optimisation while preserving enough expressiveness to cover practical agent tasks?

---

Relevant Notes:

- [frontloading spares execution context](./frontloading-spares-execution-context.md) — foundation: frontloading removes derivation procedures from bounded context by precomputing what can be known earlier
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — cost model: context is the scarce resource and has both volume and complexity dimensions
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative-because-extraction-requires-computation.md) — explains why representation choice matters: different artifacts expose different structure to a bounded observer
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: fresh sub-agent frames provide the bounded working memory assumed by the model
- [decomposition rules for bounded-context scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — consequence: preliminary practical rules that follow from the model
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: what happens when the scheduler is itself bounded, and three recovery strategies

Topics:

- [computational-model](./computational-model.md)
