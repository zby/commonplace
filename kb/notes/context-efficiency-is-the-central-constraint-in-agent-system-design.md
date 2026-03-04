---
description: Context — not compute, memory, or storage — is the scarce resource in agent systems; nearly every architectural decision is a response to context scarcity, making context efficiency the dominant cost model analogous to algorithmic complexity in traditional systems
type: note
traits: [has-external-sources]
areas: [kb-design, computational-model]
status: seedling
---

# Context efficiency is the central constraint in agent system design

In traditional systems, the scarce resources are compute cycles, memory, storage, and network bandwidth. Engineers optimise for these, and algorithmic complexity is the dominant cost model. In agent systems built on LLMs, the scarce resource is context — the finite window of tokens the agent can attend to at once. Nearly every architectural decision in a well-designed agent system is a response to this scarcity.

Anthropic's engineering team has converged on the same framing, defining **context engineering** as "strategies for curating and maintaining the optimal set of tokens during LLM inference" and describing context as "a critical but finite resource" with an **attention budget** that "every token depletes" ([Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). The goal is to "find the smallest possible set of high-signal tokens" that maximise desired outcomes.

## Why context is singular

Context is not just another resource to optimise. It is the *only channel* through which an agent receives instructions, understands its task, accesses knowledge, and reasons toward action. There is no equivalent in traditional systems — a CPU has registers, cache, RAM, disk, and network as separate tiers with different cost profiles. An LLM has one context window. Everything competes for the same space.

Two properties of the medium intensify this scarcity beyond what traditional resource constraints produce. First, the medium is [homoiconic](./llm-context-is-a-homoiconic-medium.md) — instructions and data are the same tokens, so there is no mechanism to prioritise instructions over data or protect them from dilution. In traditional systems, program and data occupy separate memory regions; here they compete as equals. Second, [instructions are underspecified](./agentic-systems-interpret-underspecified-instructions.md) — extra context doesn't just waste space, it actively influences which interpretation the agent chooses. In a system with precise semantics, irrelevant data merely sits there; in a system with underspecified semantics, it distorts.

These properties produce three consequences:

**Finite capacity with hard limits.** The context window has a token ceiling. Every token spent on one thing is unavailable for another. Unlike disk or RAM, you cannot add more — the architecture fixes the budget.

**Attention degradation under load.** Even within the window, more content means weaker attention to any given part. The classic "lost in the middle" finding ([Liu et al., 2023](https://arxiv.org/abs/2307.03172)) established that models exhibit primacy and recency bias, performing best when relevant information appears at the beginning or end of context. Anthropic calls this **context rot** — the degradation in ability to recall and reason as the window fills. The resource doesn't just run out — it degrades before it runs out.

This degradation has two distinct dimensions. **Token-volume degradation** is positional: more tokens dilute attention to any given token, producing the lost-in-the-middle effect. **Compositional-depth degradation** is structural: chaining dependent reasoning steps causes performance collapse even when token count is trivial. ConvexBench ([Liu et al., 2026](../sources/convexbench-can-llms-recognize-convex-functions.md)) isolates the second dimension: LLMs verifying convexity of composed functions collapse from F1=1.0 to F1≈0.2 at depth 100, despite using only 5,331 tokens — far below context limits. The authors distinguish "long-context capability" (handling token length) from "long-horizon reasoning capability" (maintaining correctness over dependent steps). The mechanism: each step conditions on an expanding history of prior sub-steps, creating a **compositional reasoning gap** where accumulated intermediate results interfere with current-step reasoning. Scoped recursion — pruning history to retain only direct dependencies at each step — recovers F1=1.0 at all depths, confirming that the degradation is caused by flat accumulation, not by the reasoning task itself.

**Interpretation cost compounds.** Traditional systems execute instructions at constant cost — a CPU doesn't slow down because the program is complex. LLMs pay interpretation overhead proportional to context complexity. Giving an agent a procedure ("first do X, then use the result to do Y") costs more than giving it the answer that procedure would have produced ("here is Z") — the agent must parse, track, and execute the procedure instead of just receiving the answer. Every layer of [indirection costs context and interpretation overhead](./indirection-is-costly-in-llm-instructions.md) on every read.

## Growing windows don't eliminate the constraint

Nominal context windows have grown at roughly 30x per year since mid-2023 ([Epoch AI, 2025](https://epoch.ai/data-insights/context-windows)). One might expect this to dissolve context scarcity. It hasn't, for two reasons.

First, the gap between nominal and effective capacity is large. Models' ability to *use* input effectively is improving faster than raw window size, but effective capacity still lags far behind nominal. Larger windows create more room but also more opportunity for attention dilution — the "lost in the middle" effect doesn't disappear with longer contexts.

Second, context demand grows with task ambition. The gains from longer windows get consumed by richer tool outputs, longer conversation histories, and more complex instructions. This is a Jevons paradox: when a resource becomes cheaper to use, total consumption increases rather than decreasing. Efficiency gains in window utilisation get absorbed by expanding use cases. The constraint shifts but doesn't disappear.

## What this explains

Context scarcity is the pressure that produces most of the architectural patterns in agent system design. Each pattern is a different strategy for the same underlying problem: making the best use of a finite, degradation-prone, interpretation-heavy resource.

**Frontloading and partial evaluation.** [Pre-computing static parts of instructions](./frontloading-spares-execution-context.md) and inserting results removes procedures from context — the agent receives answers instead of instructions to derive answers. This is the most direct response: reduce what's in context by doing work outside it.

**Progressive disclosure.** The [context loading strategy](./context-loading-strategy.md) — always-loaded router, on-demand skills, task-specific docs — matches instruction specificity to loading frequency. [Directory-scoped types](./directory-scoped-types-are-cheaper-than-global-types.md) load only when working in that directory. Anthropic's own Claude Code follows this pattern: a CLAUDE.md file dropped upfront as a router, with grep/glob for just-in-time retrieval of everything else. The principle: don't load what you don't need for this task.

**Context management in long-running tasks.** When context accumulates over many turns, systems need strategies to manage it — compaction (summarising history), observation masking (dropping old turns), or sub-agent delegation. The approaches differ in fidelity and cost, but all respond to the same pressure: unmanaged context degrades performance well before hitting the window limit ([JetBrains Research, 2025](https://blog.jetbrains.com/research/2025/12/efficient-context-management/); [Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

**Sub-agent isolation.** [Sub-agents provide lexically scoped frames](./llm-context-is-composed-without-scoping.md) — fresh context with only what the caller explicitly passes. Anthropic recommends sub-agents return 1,000–2,000 token summaries; the tens of thousands of tokens each sub-agent explores stay out of the caller's window. This is the only mechanism that truly isolates context.

**Navigation design.** [Agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md). Prose-as-title, retrieval-oriented descriptions, context phrases on index entries — all exist to help the agent make reading decisions *without* loading the target. Every pointer that carries enough context to decide "don't follow this" saves the tokens that loading would have cost. Anthropic identifies the failure mode: "bloated tool sets that cover too much functionality or lead to ambiguous decision points about which tool to use." If a human engineer can't say which tool to use in a situation, neither can the agent.

**Instruction notes over data dumps.** When delegating to a sub-agent, the efficient interface is an instruction note that frontloads the caller's judgment — which documents matter, which sections, what question to answer — rather than passing raw material. The instruction note carries judgment compactly; raw data forces the sub-agent to spend context on discovery the caller already did. The caller's work is judgment (expensive in context, done once); the sub-agent's work is execution (clean context, focused task).

## The analogy to algorithmic complexity

In traditional systems, algorithmic complexity is the dominant cost model because compute scales but algorithmic class doesn't — an O(n²) algorithm stays O(n²) regardless of hardware. Context efficiency plays the same role in agent systems: context windows grow but the fundamental scarcity remains. Epoch AI's data makes this concrete: windows grow at 30x/year, but effective utilisation (the length at which models still perform well) grows from a much lower baseline. A system that wastes context on indirection, dead branches, and unnecessary loading will hit attention degradation and capacity limits regardless of window size, just as an O(n²) algorithm hits walls regardless of CPU speed.

The practical implication: context efficiency should be evaluated at design time, not treated as an optimisation to apply later. Architectural choices — what loads when, what gets frontloaded, where sub-agent boundaries go, how instructions are structured — determine context efficiency structurally. They are hard to retrofit.

---

Sources:
- Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- JetBrains Research (2025). [Cutting through the noise: smarter context management for LLM-powered agents](https://blog.jetbrains.com/research/2025/12/efficient-context-management/).
- Epoch AI (2025). [LLMs now accept longer inputs, and the best models can use them more effectively](https://epoch.ai/data-insights/context-windows).
- Liu et al. (2023). [Lost in the middle: how language models use long contexts](https://arxiv.org/abs/2307.03172).
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](../sources/convexbench-can-llms-recognize-convex-functions.md) — empirical evidence that compositional depth, not token count, drives reasoning degradation.

Relevant Notes:
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the most direct response to context scarcity; this note explains *why* frontloading matters
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — mechanism: the cost model that makes indirection expensive in context but free in code
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — application: progressive disclosure as a response to always-loaded context being expensive
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — foundation: flat context means everything competes; sub-agents are the scoping response
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — application: navigation design as context-saving strategy
- [directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — application: type system designed around context economy
- [generate instructions at build time](./generate-instructions-at-build-time.md) — application: build-time generation as frontloading applied to skill templates
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — intensifies: instructions and data compete as equal tokens with no priority mechanism
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — intensifies: extra context distorts interpretation, not just wastes space

Topics:
- [computational-model](./computational-model.md)
- [kb-design](./kb-design.md)
