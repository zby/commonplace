---
description: Formalises agent orchestration as a symbolic scheduler driving bounded LLM calls through a select/call loop — analyses what makes selection hard and why the model supports local comparative results even when global optimisation is intractable
type: note
traits: [has-external-sources]
areas: [computational-model]
status: seedling
---

# Bounded-context orchestration model

Two observations motivate this model. First, [context is the scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) in agent systems — the finite window of tokens the agent can attend to, with both volume and complexity costs. Second, [bookkeeping and semantic work have different error profiles](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — symbolic substrates eliminate all three sources of error for bookkeeping, while LLMs are needed only for semantic judgment.

Together these imply a natural architecture: a symbolic scheduler over bounded LLM calls.

## The model

The model has two components:

- a **symbolic scheduler** over unbounded exact state, which assembles prompts and orchestrates the workflow — items in that state may be source artifacts or lossy derived artifacts (relevance labels, cluster summaries, extracted claims) produced by earlier LLM calls
- **bounded clean context windows** for each LLM call — the only expensive, stochastic operation

In practice, the scheduler's symbolic state may be implemented using files, in-memory structures, databases, or a mix. What matters operationally is that the orchestrator should:

- hold accumulated state in program variables or files, not in an LLM conversation history
- use LLM calls for judgment (relevance, decomposition, synthesis) but return results to code
- assemble the next prompt symbolically from stored results, not by relying on the LLM to remember prior steps

The model also accommodates architectures where the LLM emits a symbolic control program rather than a direct natural-language answer; the scheduler executes that program, using it to inspect symbolic state, manipulate artifacts, and trigger further bounded LLM calls.

A system that keeps bookkeeping inside an LLM conversation is a [degraded variant of this model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) that spends bounded context on work the symbolic scheduler handles for free.

## The select/call loop

Let:

- `K` be the scheduler's full symbolic state — its items include source artifacts, derived artifacts (including LLM responses), and goals (the user's top-level goal is simply the initial item in `K`; sub-goals produced by decomposition calls are further items)
- `M` be the maximum effective context of one agent call
- `|P|` be the cost of prompt `P` under whichever dimension we want to model — token count, compositional depth, or a function of both

There are two kinds of computation:

**Symbolic steps.** Deterministic procedures outside LLM context: file listing, retrieval by name, sorting, thresholding, prompt assembly, deduplication. In the simplest model these are cheap and unbounded.

**Agent calls.** The `select` function builds a prompt `P` from the current state `K`, subject to the feasibility constraint `|P| ≤ M`. This is where the scheduling difficulty lives: `select` must choose both *which* items from K to include and *how* to frame them, because the same material under different framing yields different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md).

Executing the call produces a result `r`, appended to symbolic state. The crucial point is that `r` need not be a direct answer — it can be a relevance label, extracted claim list, cluster summary, contradiction table, partial synthesis, a set of sub-goals, or a satisfaction signal marking a goal as reached.

Operationally, the scheduler drives a recursive loop:

```
solve(K):
    if satisfied(K):
        return K

    P  = select(K)
    r  = call(P)

    return solve(K + r)
```

Real orchestrators routinely fan out parallel calls. Parallelism changes the scheduling problem (which calls can run independently?) but not the core structure.

`select` is symbolic — it is code, not an LLM call. But many real scheduling decisions require semantic judgment. The model accommodates this without breaking the symbolic/bounded separation: `select` constructs a *planning prompt* that asks the planning question rather than requesting a task output. The `call` returns a plan or selection decision, appended to `K` as ordinary symbolic state. On the next recursive step, `select` reads those decisions from `K` and proceeds deterministically. Hierarchical decomposition is therefore not a separate mechanism but a pattern of use.

## What makes selection hard

The `select` function is where the optimisation lives. It is not a simple knapsack problem for several reasons:

**Framing matters, not just selection.** The same knowledge, presented differently, has different value to a bounded observer. "Here are six documents, synthesise them" is less useful than "documents A and B establish X, documents C and D contradict it, resolve the tension." Same information, different [extractable structure](./information-value-is-observer-relative-because-extraction-requires-computation.md).

**Dual cost dimensions.** [Context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). Selection must optimise both: include enough to be useful, but frame it so the sub-agent can actually use it.

**Sequential dependence.** Each selection affects future state. A good first iteration might discover that the goal decomposes differently than expected, changing what subsequent iterations should select. This makes the problem sequential — closer to a Markov decision process than a knapsack.


## The canonical note-selection example

Suppose the task is: given many notes, find the relevant ones and write an analysis. The full set of notes does not fit in one context window.

Traced through `solve`:

```
K = {goal: "analyse notes", notes: [n₁ ... nₖ]}

# step 1: notes exceed M — planning call to decompose
P = select(K)  →  "decompose this goal"
r = call(P)    →  "filter each note for relevance, then synthesise"
K = K + r

# step 2: scheduler loops over filter sub-goals (symbolic)
for i in 1..k:
    P = select(K)  →  prompt with nᵢ: "relevant? extract claims"
    r = call(P)    →  {nᵢ: relevant/not, claims: [...]}
    K = K + r

# step 3: scheduler collects relevant notes (symbolic)
relevant = [nᵢ for nᵢ in K where nᵢ marked relevant]

if |relevant| ≤ M:
    # step 4a: synthesis call
    P = select(K)  →  synthesis prompt over relevant notes
    r = call(P)    →  final analysis
else:
    # step 4b: cluster, summarise per cluster, then synthesise
    for each cluster:
        P = select(K)  →  summarise prompt for cluster
        r = call(P)    →  cluster summary
        K = K + r
    P = select(K)  →  synthesis prompt over cluster summaries
    r = call(P)    →  final analysis
```

The symbolic scheduler handles the loop, the collection, and the branching — all deterministic. LLM calls handle only the semantic judgments: relevance filtering, summarisation, synthesis. Several [decomposition rules](./decomposition-rules-for-bounded-context-scheduling.md) generalise from this pattern.

## Scope and open questions

The full global optimisation problem is probably too rich for clean strategy theorems: goals are [underspecified](./agentic-systems-interpret-underspecified-instructions.md), LLM calls are noisy, the `satisfied` check is itself a judgment call, and the value of including item X depends on the sub-agent's stochastic interpretation. There is no clean objective function. But the model supports **local comparative results** — comparing two concrete strategies or justifying a transformation from one strategy to another. The [decomposition rules](./decomposition-rules-for-bounded-context-scheduling.md) catalogue specific transformations that the model shows move a system in the right direction.

- Can the framing decisions within `select` be factored cleanly enough that their cost can be ignored in a first theory and reintroduced later?
- How much selection judgment should the scheduler perform before constructing a bounded call, and how much should be delegated to the LLM inside that call?
- What restrictions on the model (fixed decomposition templates, bounded branching, finite sub-goal depth) yield tractable optimisation while preserving enough expressiveness?
- What heuristics make `select` good in practice?
- When should the orchestrator compact vs externalise vs recurse?
- Can the loop be made self-improving — can later iterations learn from the quality of earlier selections? This would connect to [deploy-time learning](./deploy-time-learning-the-missing-middle.md).

---

Sources:
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](../sources/convexbench-can-llms-recognize-convex-functions.md) — scoped recursion with focused context as a clean-model implementation for compositional reasoning.
- Meyerson et al. (2025). [MAKER: Solving a million-step LLM task with zero errors](../sources/meyerson-maker-million-step-llm-zero-errors.md) — maximal decomposition (m=1) as extreme clean-model instantiation; O(s ln s) cost scaling.
- @Vtrivedy10 (2026). [The Anatomy of an Agent Harness](../sources/the-anatomy-of-an-agent-harness-2031408954517971368.md) — the Ralph Loop (prompt → execute → observe → decide) is a concrete instance of the select/call loop; harness components map to scheduler infrastructure.

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivation: context is the scarce resource with volume and complexity dimensions
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — foundation: bookkeeping and semantic work have different error profiles across all three phenomena
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the single-step mechanism this note extends to an iterative loop
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative-because-extraction-requires-computation.md) — explains why framing matters in selection
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make each loop iteration independent
- [decomposition rules for bounded-context scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — consequence: practical rules that follow from the model
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: what happens when the scheduler is itself bounded
- [distillation](./distillation.md) — mechanism: compaction of K is distillation targeting the orchestrator's context budget
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — complicates: the goal, the satisfaction check, and the sub-agent's interpretation are all underspecified
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalisation response is the workshop pattern
- [paper outline v2](../work/paper-bounded-context-orchestration/outline-v2.md) — develops: presents this model for an academic audience

Topics:

- [computational-model](./computational-model.md)
