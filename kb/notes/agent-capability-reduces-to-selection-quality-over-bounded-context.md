---
description: Extending frontloading from a single partial-evaluation step to an iterative loop reveals a sequential optimisation problem — at each step the orchestrator selects what to frontload into a fixed-capacity sub-agent window, with each iteration's results expanding the knowledge available for the next selection
type: note
traits: []
areas: [computational-model]
status: seedling
---

# The frontloading loop is an iterative optimisation over bounded context

[Frontloading](./frontloading-spares-execution-context.md) as described in the existing note is a single step: pre-compute static parts, insert results, hand to the LLM. But real agentic work is not a single step. The caller discovers what's relevant, delegates a piece, absorbs results, discovers more, delegates again. The single frontloading step generalises to a loop:

```
K₀ = initial knowledge
for i = 1, 2, ...
    (Sᵢ, Iᵢ) = select(G, Kᵢ₋₁, W)     # orchestrator chooses what to frontload
    rᵢ       = execute(Iᵢ)               # sub-agent runs in clean context
    Kᵢ       = absorb(Kᵢ₋₁, rᵢ)          # orchestrator integrates results
    if satisfied(G, Kᵢ): return Kᵢ
```

where G is the goal, K is the orchestrator's accumulated knowledge, W is the sub-agent's context window capacity, and `select` is the function that chooses both *what* to include (Sᵢ ⊆ Kᵢ₋₁) and *how* to frame it as instructions (Iᵢ).

Each iteration is a [partial evaluation](./frontloading-spares-execution-context.md) — the orchestrator specialises the goal with respect to what it currently knows, producing a residual program (the instruction note) that the sub-agent executes. The loop is iterated partial evaluation.

## What makes `select` hard

The selection function is where the optimisation lives. It is not a simple knapsack problem (fitting the most valuable items into capacity W) for several reasons:

**Framing matters, not just selection.** The same knowledge, presented differently, has different value to a bounded observer. An instruction note that says "here are six documents, synthesise them" is less useful than one that says "documents A and B establish X, documents C and D contradict it, your job is to resolve the tension." Same information, different extractable structure. This is the [observer-relative information](./information-value-is-observer-relative-because-extraction-requires-computation.md) point: the sub-agent's bounded extraction capacity determines what's worth including *and how*.

**Dual cost dimensions.** [Context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). Selection must optimise both: include enough to be useful (volume), but frame it so the sub-agent can actually use it (complexity). Overloading a sub-agent with raw material wastes context even if it fits in the window.

**Sequential dependence.** Each selection affects future state. A good first iteration might discover that the goal decomposes differently than expected, changing what subsequent iterations should frontload. This makes the problem sequential, not static — closer to a Markov decision process than a knapsack.

**The selection is itself bounded.** The orchestrator that runs `select` is also a bounded observer with its own context. As K grows, the orchestrator's ability to choose well may degrade — the same [compositional reasoning gap](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) that motivates sub-agent isolation applies to the orchestrator itself.

## The orchestrator's dilemma

The loop has a fundamental tension: the orchestrator needs accumulated knowledge (large K) to make good selections, but accumulated context degrades its judgment. The orchestrator benefits from knowing everything the sub-agents have produced, but it pays for that knowledge in attention degradation and compositional overhead.

Three responses:

1. **Compaction.** The orchestrator doesn't keep raw results — it keeps summaries, conclusions, pointers. K grows in items but not proportionally in tokens. This is distillation applied to the orchestrator's own state.

2. **Externalisation.** Write intermediate state to disk (notes, logs, structured artifacts). The orchestrator can re-read selectively rather than holding everything in context. This is what the KB already does — notes are externalised orchestrator state.

3. **Recursion.** The orchestrator delegates its own `select` step to a sub-orchestrator with a clean window. The loop becomes a tree: each node is a frontload-execute-absorb cycle, and nodes can spawn children. A flat loop is the single-level case; recursion is "the sub-agent can also use the same pattern."

## Connection to existing mechanisms

**Distillation as the absorb step.** Each `absorb(K, r)` is a [distillation](./distillation.md): the orchestrator extracts what matters from the sub-agent's results and integrates it into its evolving understanding. The distillation targets the orchestrator's own context budget.

**Instruction notes as the output of select.** The instruction note — the thing the sub-agent reads — is the output of `select`. It is a distillation of K targeted at the sub-agent's bound and task. The quality of `select` determines the quality of the instruction note, which determines the quality of execution.

**Sub-agent isolation as the execute step.** [Sub-agents provide lexically scoped frames](./llm-context-is-composed-without-scoping.md) — each `execute(I)` runs in a clean context with only what the orchestrator chose to include. This is the mechanism that makes the loop work: without clean frames, accumulated context would degrade every iteration.

## What optimality means here

In standard optimisation, you can define an objective function and search for its maximum. The frontloading loop doesn't have a clean objective function because:

- The goal G is typically underspecified (natural language, [interpreted by the agent](./agentic-systems-interpret-underspecified-instructions.md))
- The `satisfied` check is itself a judgment call, not a verifiable predicate
- The value of including item X in Sᵢ depends on the sub-agent's stochastic interpretation

So "optimisation" here means something looser: the orchestrator makes choices that, given its bounded judgment, seem most likely to advance the goal. The mathematical framing illuminates the *structure* of the problem (sequential, dual-cost, bounded-observer) even though the objective isn't precisely measurable.

The practical consequence is that the loop's quality depends almost entirely on the orchestrator's judgment — what to include, how to frame it, when to stop. This is why the previous conversation identified "judgment about what matters" as the orchestrator's irreducible contribution. The sub-agent does the context-heavy work; the orchestrator does the selection.

## Open Questions

- What heuristics make `select` good in practice? The workshop experiments suggest: include the goal, include relevant documents with annotations explaining why they matter, include discovered connections. Is there a more systematic approach?
- When should the orchestrator compact vs externalise vs recurse? These seem like different regimes — small K favours holding in context, medium K favours compaction, large K favours externalisation or recursion.
- Can the loop be made self-improving — can later iterations learn from the quality of earlier selections? This would connect to [deploy-time learning](./deploy-time-learning-the-missing-middle.md).
- How does the loop relate to tree-of-thought and similar search strategies? Those are typically within a single context; this loop uses multiple clean contexts.

---

Relevant Notes:

- [frontloading spares execution context](./frontloading-spares-execution-context.md) — foundation: the single-step mechanism this note extends to an iterative loop
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: the dual-cost model (volume and complexity) that shapes what `select` must optimise for
- [information value is observer-relative](./information-value-is-observer-relative-because-extraction-requires-computation.md) — explains: why framing matters in selection — the same information has different value depending on how it's presented to a bounded observer
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: sub-agent isolation provides the clean frames that make each loop iteration independent
- [distillation](./distillation.md) — mechanism: the absorb step is distillation targeting the orchestrator's own context budget
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — complicates: the goal, the satisfaction check, and the sub-agent's interpretation are all underspecified, preventing clean objective functions
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalisation response (writing intermediate state to disk) is the workshop pattern — temporal documents that consume themselves as the loop progresses

Topics:

- [computational-model](./computational-model.md)
