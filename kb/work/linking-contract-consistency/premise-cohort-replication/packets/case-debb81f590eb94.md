# Case packet

Neutral case identifier: case-debb81f590eb94

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Orchestration strategies and run-state have opposite persistence economics

A scheduler over bounded LLM calls has two symbolic parts: the [accumulated state `K`] and the `select` logic that decides what the next call sees and does. When the [host language plays both roles], it is tempting to treat them as one substrate with one lifecycle. It is the wrong instinct. Measured by **cross-task reuse value** — how much a later, different task gains from keeping the part around — `K` and `select` sit at opposite poles, so a system that promotes them symmetrically gets one of them wrong.

The axis here is *cross-task* persistence: whether a part is worth lifting into a durable library so later tasks reuse it. That is distinct from *within-run* survival — whether `K` outlives its process or fits in memory — which the [companion note] treats separately and which can force `K` to be reified even when it has no cross-task value.

- **Run-state `K`** is the answer to *this* task — source artifacts plus the relevance labels, summaries, and partial syntheses prior calls produced for it. Some of that is expensive to recompute, but recomputing it does not help the next task, because the next task asks something else. Its cross-task reuse value is near zero, so it should stay **ephemeral across tasks**: it may be checkpointed within a run for durability or capacity, but it is not promoted into the library.
- **`select`-strategies** — the decomposition, partitioning, and aggregation patterns the scheduler applies — recur across tasks and are **expensive to rediscover**. Each is a small piece of control logic that took search to find, and the same shape pays off on the next task. These are the **high-value promotion target**, worth lifting into durable, tested library code.

[RLM] discards *both* halves after every query. Discarding `K` is correct: it is query-specific, so even when rebuilding it is costly, the cost buys nothing for the next, different query. Discarding the `select`-strategy with it is the loss. A decomposition the model searched for and got right is gone before the next query arrives, so the same search is paid again. The fix is not the opposite symmetry — reify everything, the durable-execution pole. It is to **split the cross-task lifecycles: let `K` stay ephemeral, promote the recurring `select`-fragments.**

## The control structure: a test-gated orchestrator cache

Splitting the lifecycles turns the scheduler into an **orchestrator cache with a test-gated write-back**, run reuse-first rather than generate-first:

1. On a task, search the library for a fitting tested orchestrator.
2. **Hit** → reuse the verified code: cheap, deterministic, no re-derivation.
3. **Miss** → generate the orchestration fresh (RLM-style); if it clears the promotion gate below and passes tests, write it back to the library.

Two distinct gates run here, and conflating them is the trap. *Fit* (step 1) is a selection judgment — does this stored strategy apply to the task at hand — and it does not get easier just because a fragment is tested. *Trust* (step 2) is what the *tested* qualifier buys: a cache of merely retained code is memoization, whereas a cache of *verified* code is what lets a later run rely on a fitting fragment without re-deriving and re-checking it. Tests certify that the fragment still does what it did, not that it suits a given task; selecting a fitting one remains a separate cost (see the retrieval problem below). Promotion is therefore movement up the [verifiability gradient] — from loose, model-authored REPL code toward deterministic library functions. That is the general shape of [codification], and the loop it closes is [deploy-time learning] through the repo.

## What this costs, and why promotion must be selective

The asymmetry does not make accumulation free; it tells you *which* half is worth paying for. Promoting `select`-fragments takes back, for those fragments, the governance burden that [discarding everything avoids]: provenance, approval, staleness, retirement, dependency drift, and a **retrieval problem** — once the library is large, finding the right orchestrator becomes its own selection cost, and naming noise grows. Keeping `K` ephemeral keeps the corresponding state-management burden off the table, so the bill is paid only on the reusable half, not on everything.

So the promotion gate cannot be "anything that worked." Passing tests is necessary — it is the trust gate above — but not sufficient: the gate must also admit only patterns that are stable, frequently recurring, and expensive to rederive, because [codifying what the model will soon do better unaided] is a net-negative trade. The persistence asymmetry justifies *having* a promotion path; the bitter-lesson boundary governs *what crosses it*. Run-state never crosses — not because it is cheap, but because it never recurs; only the costly, recurring control strategies do.

## Where it lands

This is a third mode on the authorship axis. Two poles already exist: the model re-authoring `select` from scratch every run (RLM), and a programmer authoring it once up front (a hand-written host-language scheduler). The third is distinct from both because authorship is *split across time* — the model authors a fragment during a run, and a promotion step turns the recurring, tested ones into library code that later runs reuse. It is neither purely per-run nor purely up-front: the corpus of `select`-functions grows from execution. So it is the [host-language scheduler] made **self-populating** — built bottom-up from exploration rather than top-down by design — and the concrete form of the combined system the [persistence-boundary comparison] sketches.

A shipped instance partially confirms the prediction. Claude Code's [dynamic workflows] have the model author an ephemeral orchestrator script per task and let a completed run be saved as a reusable `/<name>` command — the promotion path, in the wild. But the shipped form is **coarse and manual**: it promotes the *whole* script by hand, with no test gate and no fragment-level split, so the *fit* and *trust* gates above collapse into a single human decision. The promotion *pole* therefore exists while the machinery this note specifies — the two gates and `select`-fragment granularity — remains unbuilt. The direction is corroborated; the mechanism is not yet.

---

Relevant Notes:

## Artifact B

# Bounded-context orchestration model

This is a model of the **joint LLM-code system**, not a model of a standalone LLM. The system being modeled includes both the symbolic code that owns state and control flow and the bounded LLM calls that perform semantic judgment. The central question is how the code side should schedule, frame, and absorb those calls when no single LLM context window can hold all relevant state.

Two observations motivate this model. First, [context is the scarce resource] in agent systems — the finite window of tokens the agent can attend to, with both volume and complexity costs. Second, there is reason to think that [bookkeeping and semantic work have different error profiles] — symbolic substrates eliminate all three sources of error for bookkeeping, while LLMs are needed only for semantic judgment. (The second argument is conjectural; the first is well-established.)

Together these imply a natural architecture: a symbolic scheduler over bounded LLM calls. This is not a restrictive design choice — [any symbolic program with LLM calls is a select/call program], so the model captures the full space of such architectures.

## The model

The model has two components:

- a **symbolic scheduler** over unbounded exact state, which assembles prompts and orchestrates the workflow
- **bounded clean context windows** for each LLM call — the expensive, stochastic operation that the architecture is designed around

The scheduler's state includes source artifacts, prior prompts, and outputs from earlier LLM calls: relevance labels, cluster summaries, extracted claims, sub-goals, partial syntheses. In practice this state may live in files, in-memory structures, databases, or a mix. The operational requirement is simple: accumulated state lives there, not in conversation history; LLM calls do judgment work and return results to code; the next prompt is assembled from stored state rather than from the model's memory of prior turns.

The model also accommodates architectures where the LLM emits a symbolic control program rather than a direct natural-language answer. That still fits as long as execution and state progression remain external to the conversation. A system that keeps bookkeeping inside an LLM conversation is a [degraded variant] that spends bounded context on work the symbolic scheduler handles for free.

## The select/call loop

Let:

- `K` be the scheduler's full symbolic state — source artifacts plus everything prior calls have produced
- `P` be one complete prompt, including both the requested operation and the material selected for that call
- `M` be the maximum effective context budget for one call
- `||P||` be the effective cost of complete prompt `P` — token count, compositional difficulty, task framing, or all three

The cost measure `||·||` is an idealized effective-cost measure over the whole prompt, not just a token count. The cost may depend on the kind of task that `P` describes: a synthesis prompt and a relevance-check prompt can have different effective costs even when they contain the same source material. [Agent context is constrained by soft degradation, not hard token limits] develops the empirical case for that task dependence.

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

**Coupled selection and framing.** [Context cost] has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). The same knowledge, presented differently, has different value to a bounded observer: "Here are six documents, synthesise them" is less useful than "documents A and B establish X, documents C and D contradict it, resolve the tension." Same tokens, different yield for a bounded reader. See [information value is observer-relative].

## Scope and open questions

The full global optimisation problem is probably too rich for clean strategy theorems: goals are [underspecified], LLM calls are noisy, the decision to halt or continue is itself a judgment call inside `select`, and the value of including item X depends on the sub-agent's stochastic interpretation. There is no clean objective function. But the model supports **local comparative results** — comparing two concrete strategies or justifying a transformation from one strategy to another. The [decomposition rules] catalogue specific transformations that the model shows move a system in the right direction.

- Can the framing decisions within `select` be factored cleanly enough that their cost can be ignored in a first theory and reintroduced later?
- How much selection judgment should the scheduler perform before constructing a bounded call, and how much should be delegated to the LLM inside that call?
- What restrictions on the model (fixed decomposition templates, bounded branching, finite sub-goal depth) yield tractable optimisation while preserving enough expressiveness?
- What heuristics make `select` good in practice?
- When should the orchestrator compress state, offload it to external storage, or delegate to a sub-loop?
- Can the loop be made self-improving — can later iterations learn from the quality of earlier selections? This would connect to [deploy-time learning].

---

Sources:
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?] — scoped recursion with focused context as a clean-model implementation for compositional reasoning.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors] — maximal decomposition (m=1) as extreme clean-model instantiation; O(s ln s) cost scaling.
- @Vtrivedy10 (2026). [The Anatomy of an Agent Harness] — the Ralph Loop (prompt → execute → observe → decide) is a concrete instance of the select/call loop; the source's runtime components map to scheduler infrastructure.
- Ashpreet Bedi (2026). [Context providers: the missing layer between agents and tools] — source-scoped provider sub-agents instantiate `select/call` by hiding raw tool surfaces behind bounded query/update calls.

Relevant Notes:

- [information value is observer-relative because extraction requires computation] — explains why framing matters in selection
- [agent runtimes decompose into scheduler context engine and execution substrate] — component view: names the scheduler as one part of a larger runtime decomposition

## Under-review context phrase

the `select`/`K` decomposition whose two halves this note assigns opposite persistence economics
