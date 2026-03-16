---
description: Formalises agent orchestration as a symbolic scheduler driving bounded LLM calls through a select/call loop — explains why selection is hard while still supporting local strategy comparisons
type: note
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Bounded-context orchestration model

Two observations motivate this model. First, [context is the scarce resource](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) in agent systems — the finite window of tokens the agent can attend to, with both volume and complexity costs. Second, [bookkeeping and semantic work have different error profiles](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — symbolic substrates eliminate all three sources of error for bookkeeping, while LLMs are needed only for semantic judgment.

Together these imply a natural architecture: a symbolic scheduler over bounded LLM calls.

## The model

The model has two components:

- a **symbolic scheduler** over unbounded exact state, which assembles prompts and orchestrates the workflow
- **bounded clean context windows** for each LLM call — the only expensive, stochastic operation

The scheduler's state includes source artifacts, prior prompts, and lossy derived artifacts produced by earlier LLM calls: relevance labels, cluster summaries, extracted claims, sub-goals, partial syntheses. In practice this state may live in files, in-memory structures, databases, or a mix. The operational requirement is simple: accumulated state lives there, not in conversation history; LLM calls do judgment work and return results to code; the next prompt is assembled from stored state rather than from the model's memory of prior turns.

The model also accommodates architectures where the LLM emits a symbolic control program rather than a direct natural-language answer. That still fits as long as execution and state progression remain external to the conversation. A system that keeps bookkeeping inside an LLM conversation is a [degraded variant](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) that spends bounded context on work the symbolic scheduler handles for free.

## The select/call loop

Let:

- `K` be the scheduler's full symbolic state
- `t` be the call type or task family of the next agent step
- `M(t)` be the maximum effective context for that kind of call
- `|P|` be the cost of prompt `P` in the same abstract units — token count, compositional depth, or a function of both

`K` can be read in two equivalent ways. In the minimal reading, it contains only source state and prior call results, `select` recomputes any deterministic projections it needs, and `K + r` means simple concatenation of the new result onto the state sequence. In the materialized reading, `K` also stores goals, prior prompts, cached indexes, rankings, groupings, dependency maps, or other deterministic views for efficiency, and `K + r` stands for the corresponding state update. The theory treats these as equivalent; real orchestrators usually choose the second form. In practice many orchestrators persist the generated prompt `P` itself for audit, refinement, or later reuse; the notation leaves this implicit because `P` is a deterministic projection of `K` at that step, while `r` is the new stochastic output of the call.

`M` is therefore not a universal constant for a model. It is an effective-budget measure indexed by the kind of work the call is doing. Paulsen's MECW result is one empirical reason to write `M(t)`: retrieval, summarisation, extraction, and synthesis can fail at different context sizes even on the same model. In a local analysis where the call type is fixed, we can suppress `t` and write `M` as shorthand.

The scheduler alternates between two kinds of step. **Symbolic steps** happen outside LLM context: file listing, retrieval, sorting, prompt assembly, deduplication. **Agent calls** are bounded LLM invocations under focused prompts.

The `select` function builds a prompt `P` from the current state `K`, subject to the feasibility constraint `|P| ≤ M(t)`. This is where the scheduling difficulty lives: `select` must choose both *which* items from `K` to include and *how* to frame them, because the same material under different framing yields different [extractable structure](./information-value-is-observer-relative.md).

The result `r` is appended back into symbolic state. It need not be a direct answer — it may be a relevance label, claim list, cluster summary, contradiction table, partial synthesis, sub-goal set, or satisfaction signal.

Operationally:

```
while not satisfied(K):
    P  = select(K)
    r  = call(P)
    K  = K + r
```

Real orchestrators routinely fan out parallel calls. Parallelism changes the scheduling problem, but not the core structure. `select` is still symbolic code, even when it asks an LLM planning question: the planning call returns a plan into `K`, and the next step reads that plan from symbolic state and proceeds deterministically. Hierarchical decomposition is therefore not a separate mechanism but a pattern of use.

## What makes selection hard

The `select` function is where the optimisation lives. The first problem is that selection is sequential, not static, so the task is already closer to a control problem than to a one-shot packing problem:

**Sequential dependence.** Each selection affects future state. A good first iteration might discover that the goal decomposes differently than expected, changing what subsequent iterations should select. This makes the problem sequential — closer to a Markov decision process than a knapsack.

**Dual cost dimensions.** [Context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). Selection must optimise both: include enough to be useful, but frame it so the sub-agent can actually use it.

**Framing matters, not just selection.** The same knowledge, presented differently, has different value to a bounded observer. "Here are six documents, synthesise them" is less useful than "documents A and B establish X, documents C and D contradict it, resolve the tension." Same information, different [extractable structure](./information-value-is-observer-relative.md).

## The canonical note-selection example

Suppose the task is: given many notes, find the relevant ones and write an analysis. The full set of notes does not fit in one context window.

Traced through `solve`:

```
K = {goal: "analyse notes", notes: [n₁ ... nₖ]}

# step 1: notes exceed the synthesis budget — planning call to decompose
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

if |relevant| ≤ M(synthesis):
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

## Realising the model with SDKs and tool calling

The model is trivially compatible with ordinary LLM SDKs. The application programmer keeps `K` in code, computes everything deterministic outside the model, and calls the LLM only when semantic judgment is needed. Nothing about the model requires a special agent runtime. [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) develops the framework-design consequence: trouble starts when higher layers hide that application-owned loop behind framework-managed tool sessions.

Tool calling fits this picture naturally. It is just a particular return shape from a bounded call: instead of returning only prose or structured extraction, the model can return a request for application code to run a tool and feed the result back. That is a useful inversion of control, but it does not change the architecture. The scheduler can still live entirely in application code:

- keep `K` in program state, files, or a database
- assemble `P = select(K)` in code
- call the LLM API
- if the result is a tool request, execute it in code and append the result to `K`
- if the result is a semantic judgment, append it to `K`
- issue the next fresh bounded call when the application decides it is needed

This is still the clean model, even if some `select` decisions come from planning calls, because those decisions return to `K` as explicit symbolic state before the next step.

Many frameworks then turned tool calling into an internal **tool loop**: the library keeps re-calling the model, executing tools, and managing intermediate progression inside its own abstraction. The application programmer can still build an outer loop around such a framework, but then starts fighting the framework's hidden scheduler instead of simply using the SDK as a bounded semantic primitive.

So tool calling is not the threshold. Plain SDK calls already suffice; tool calling is an accommodated extension; the real boundary is whether the orchestration loop remains exposed to application code or gets absorbed into a framework-managed conversation/tool loop.

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
- @Vtrivedy10 (2026). [The Anatomy of an Agent Harness](../sources/the-anatomy-of-an-agent-harness-2031408954517971368.md) — the Ralph Loop (prompt → execute → observe → decide) is a concrete instance of the select/call loop; the source's runtime components map to scheduler infrastructure.

Relevant Notes:

- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivation: context is the scarce resource with volume and complexity dimensions
- [scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — foundation: bookkeeping and semantic work have different error profiles across all three phenomena
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the single-step mechanism this note extends to an iterative loop
- [information value is observer-relative because extraction requires computation](./information-value-is-observer-relative.md) — explains why framing matters in selection
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make each loop iteration independent
- [decomposition rules for bounded-context scheduling](./decomposition-rules-for-bounded-context-scheduling.md) — consequence: practical rules that follow from the model
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — consequence: what happens when the scheduler is itself bounded
- [llm frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — consequence: extracts the main architectural implication of the model for real implementations
- [specification-level separation recovers scoping before it recovers error correction](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) — boundary case: tool and schema hardening recover part of the interface discipline without moving the scheduler fully into code
- [distillation](./distillation.md) — mechanism: compaction of K is distillation targeting the orchestrator's context budget
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — complicates: the goal, the satisfaction check, and the sub-agent's interpretation are all underspecified
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalisation response is the workshop pattern
- [agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — component view: names the scheduler as one part of a larger runtime decomposition
- [paper outline v2](../work/paper-bounded-context-orchestration/outline-v2.md) — develops: presents this model for an academic audience
