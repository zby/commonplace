---
description: Formalises agent orchestration as the select/execute/absorb loop over bounded context and argues that the orchestrator's selection function (what to include, how to frame it) is where all the optimisation lives
type: note
traits: []
areas: [computational-model]
status: seedling
---

# Agent capability is bottlenecked by selection over bounded context

An agentic system's capability depends on model quality, tool access, and many engineering choices. But given a fixed model and toolset, the dominant variable is **how well the orchestrator selects what goes into each bounded context window** — what to include, how to frame it, and when to stop. This note formalises that claim.

[Frontloading](./frontloading-spares-execution-context.md) is a single step: pre-compute static parts, insert results, hand to the LLM. But real agentic work is not a single step. The caller discovers what's relevant, delegates a piece, absorbs results, discovers more, delegates again. The single frontloading step generalises to a loop:

```
K₀ = initial knowledge
for i = 1, 2, ...
    (Sᵢ, Iᵢ) = select(G, Kᵢ₋₁, W)     # orchestrator chooses what to frontload
    rᵢ       = execute(Iᵢ)               # sub-agent runs in clean context
    Kᵢ       = absorb(Kᵢ₋₁, rᵢ)          # orchestrator integrates results
    if satisfied(G, Kᵢ): return Kᵢ
```

where G is the goal, K is the orchestrator's accumulated knowledge, W is the sub-agent's context window capacity, and `select` is the function that chooses both *what* to include (Sᵢ ⊆ Kᵢ₋₁) and *how* to frame it as instructions (Iᵢ).

The loop is written as sequential for clarity, but real orchestrators routinely fan out parallel sub-agents — multiple `execute(Iᵢ)` calls running concurrently, with `absorb` merging their results. Parallelism changes the scheduling problem (which calls can run independently?) but not the core claim: `select` still determines what each sub-agent receives.

## What makes `select` hard

The selection function is where the optimisation lives. It is not a simple knapsack problem (fitting the most valuable items into capacity W) for several reasons:

**Framing matters, not just selection.** The same knowledge, presented differently, has different value to a bounded observer. An instruction note that says "here are six documents, synthesise them" is less useful than one that says "documents A and B establish X, documents C and D contradict it, your job is to resolve the tension." Same information, different extractable structure. This is the [observer-relative information](./information-value-is-observer-relative-because-extraction-requires-computation.md) point: the sub-agent's bounded extraction capacity determines what's worth including *and how*.

**Dual cost dimensions.** [Context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) has two dimensions — volume (how many tokens) and complexity (how hard the tokens are to use). Selection must optimise both: include enough to be useful (volume), but frame it so the sub-agent can actually use it (complexity). Overloading a sub-agent with raw material wastes context even if it fits in the window.

**Sequential dependence.** Each selection affects future state. A good first iteration might discover that the goal decomposes differently than expected, changing what subsequent iterations should frontload. This makes the problem sequential, not static — closer to a Markov decision process than a knapsack.

**The selection is itself bounded.** The orchestrator that runs `select` is also a bounded observer with its own context. As K grows, the orchestrator's ability to choose well may degrade — the same [compositional reasoning gap](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) that motivates sub-agent isolation applies to the orchestrator itself.

## The orchestrator's dilemma

The loop has a fundamental tension: the orchestrator needs accumulated knowledge (large K) to make good selections, but accumulated context degrades its judgment. The orchestrator benefits from knowing everything the sub-agents have produced, but it pays for that knowledge in attention degradation and compositional overhead.

Four responses:

1. **Compaction.** The orchestrator doesn't keep raw results — it keeps summaries, conclusions, pointers. K grows in items but not proportionally in tokens. This is distillation applied to the orchestrator's own state.

2. **Externalisation.** Write intermediate state to disk (notes, logs, structured artifacts). The orchestrator can re-read selectively rather than holding everything in context. This is what the KB already does — notes are externalised orchestrator state.

3. **Re-derivation.** Stateless re-computation: keep K small and re-run earlier sub-tasks when their results are needed again. Trades compute for context, accepting redundant execution to avoid context degradation.

4. **Recursion.** The orchestrator delegates its own `select` step to a sub-orchestrator with a clean window. The loop becomes a tree: each node is a select-execute-absorb cycle, and nodes can spawn children. A flat loop is the single-level case; recursion is "the sub-agent can also use the same pattern."

## Why selection dominates

The loop has four functions: `select`, `execute`, `absorb`, and `satisfied`. All four affect outcome quality. But selection dominates the variance for a given model and toolset, because:

- **Execute is constrained by select.** A sub-agent can only work with what it receives — [sub-agents run in clean context frames](./llm-context-is-composed-without-scoping.md) with only what the orchestrator chose to include. A brilliant model given poor instructions underperforms a good model given well-selected, well-framed context. Selection sets the ceiling; execution determines how close you get.
- **Absorb is selection applied to results.** The orchestrator deciding what to keep from results exercises the same judgment as deciding what to include — both are filtering under bounded context. The mechanism is [distillation](./distillation.md) (targeted extraction shaped by the orchestrator's context budget), but the skill it draws on is the same as `select`: what matters given the goal and the budget? Not every absorption is distillation — raw appending is possible — but effective absorption under bounded context requires it. Poor absorption degrades future selections.
- **Satisfied is typically lightweight.** Knowing when to stop matters, but for most tasks it's a cheaper judgment than per-iteration selection. (Exception: verification-heavy tasks where the satisfaction check itself dominates — correctness proofs, completeness checks, multi-criteria evaluation.)

The title claim is therefore conditional: given a fixed model, selection quality is the primary bottleneck. Across models, execution quality also matters — a weaker model extracts less from the same selection. The claim is about what the orchestrator controls, not about what's universally true.

## What optimality means here

In standard optimisation, you can define an objective function and search for its maximum. The loop doesn't have a clean objective function because:

- The goal G is typically underspecified (natural language, [interpreted by the agent](./agentic-systems-interpret-underspecified-instructions.md))
- The `satisfied` check is itself a judgment call, not a verifiable predicate
- The value of including item X in Sᵢ depends on the sub-agent's stochastic interpretation

So "optimisation" here means something looser: the orchestrator makes choices that, given its bounded judgment, seem most likely to advance the goal. The mathematical framing illuminates the *structure* of the problem (sequential, dual-cost, bounded-observer) even though the objective isn't precisely measurable.

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
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — enables: homoiconicity is what makes each iteration partial evaluation rather than just divide-and-conquer
- [distillation](./distillation.md) — mechanism: the absorb step is distillation targeting the orchestrator's own context budget
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — complicates: the goal, the satisfaction check, and the sub-agent's interpretation are all underspecified, preventing clean objective functions
- [a functioning KB needs a workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — context: the loop's externalisation response (writing intermediate state to disk) is the workshop pattern — temporal documents that consume themselves as the loop progresses

Topics:

- [computational-model](./computational-model.md)
