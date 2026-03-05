---
description: Context — not compute, memory, or storage — is the scarce resource in agent systems; context cost has two dimensions (volume and complexity) that require different architectural responses, making context efficiency the central design concern analogous to algorithmic complexity in traditional systems
type: note
traits: [has-external-sources]
areas: [kb-design, computational-model]
status: seedling
---

# Context efficiency is the central design concern in agent systems

In traditional systems, the scarce resources are compute cycles, memory, storage, and network bandwidth. Engineers optimise for these, and algorithmic complexity is the dominant cost model. In agent systems built on LLMs, the scarce resource is context — the finite window of tokens the agent can attend to at once. Nearly every architectural decision in a well-designed agent system is a response to this scarcity.

Anthropic's engineering team has converged on the same framing, defining **context engineering** as "strategies for curating and maintaining the optimal set of tokens during LLM inference" and describing context as "a critical but finite resource" with an **attention budget** that "every token depletes" ([Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). The goal is to "find the smallest possible set of high-signal tokens" that maximise desired outcomes.

## Why context is singular

Context is not just another resource to optimise. It is the *only channel* through which an agent receives instructions, understands its task, accesses knowledge, and reasons toward action. There is no equivalent in traditional systems — a CPU has registers, cache, RAM, disk, and network as separate tiers with different cost profiles. An LLM has one context window. Everything competes for the same space.

One property of the medium intensifies this scarcity beyond what traditional resource constraints produce: the medium has no strict structure. Natural language has [underspecified semantics](./agentic-systems-interpret-underspecified-instructions.md), so there are no enforced boundaries — not between instructions and data ([homoiconicity](./llm-context-is-a-homoiconic-medium.md)), not between scopes, not between levels of priority. Every structural distinction is conventional and fuzzy. This means extra context doesn't just waste space — it can dilute instructions, contaminate scopes, and distort which interpretation the agent chooses.

## Two dimensions of context cost

The context window has a hard token ceiling — every token spent on one thing is unavailable for another. But context efficiency is not only about how many tokens are in the window. It is also about what those tokens demand of the model. These are two distinct cost dimensions, and conflating them leads to architectural mistakes — optimising for token count while ignoring interpretation overhead, or vice versa.

### Volume: how many tokens

More tokens dilute attention to any given token. The classic "lost in the middle" finding ([Liu et al., 2023](https://arxiv.org/abs/2307.03172)) established that models exhibit primacy and recency bias, performing best when relevant information appears at the beginning or end of context. Anthropic calls this **context rot** — the degradation in ability to recall and reason as the window fills. The resource doesn't just run out — it degrades before it runs out.

Volume-driven patterns respond to this dimension: progressive disclosure (don't load what you don't need), context compaction (summarise history), and navigation design (decide what to read without loading it). Sub-agent isolation addresses volume too, though it also responds to the complexity dimension — see below.

### Complexity: how hard the tokens are to use

Traditional systems execute instructions at constant cost — a CPU doesn't slow down because the program is complex. LLMs pay interpretation overhead proportional to context complexity. Giving an agent a procedure ("first do X, then use the result to do Y") costs more than giving it the answer that procedure would have produced ("here is Z") — the agent must parse, track, and execute the procedure instead of just receiving the answer. Every layer of [indirection costs context and interpretation overhead](./indirection-is-costly-in-llm-instructions.md) on every read.

ConvexBench ([Liu et al., 2026](../sources/convexbench-can-llms-recognize-convex-functions.md)) provides direct empirical evidence for this dimension. LLMs verifying convexity of composed functions collapse from F1=1.0 to F1≈0.2 at depth 100, despite using only 5,331 tokens — far below context limits. The authors distinguish "long-context capability" (handling token length) from "long-horizon reasoning capability" (maintaining correctness over dependent steps). Each step conditions on an expanding history of prior sub-steps, creating a **compositional reasoning gap** where accumulated intermediate results interfere with current-step reasoning. Scoped recursion — pruning history to retain only direct dependencies at each step — recovers F1=1.0 at all depths, confirming that the degradation is caused by flat accumulation, not by the reasoning task itself.

Complexity-driven patterns respond to this dimension: frontloading (give the answer, not the procedure to derive it), indirection elimination (resolve variables at build time), instruction notes over data dumps (pre-digest material so the sub-agent doesn't have to), and scoped recursion (clean frames for each reasoning step).

### The interaction

The two dimensions are not independent. High volume amplifies complexity costs — a complex procedure buried in a long context is harder to follow than the same procedure in a short one. But they can also vary independently: ConvexBench shows complexity-driven collapse at trivial token counts, and a long context of simple facts degrades differently from a short context of intricate procedures.

## Growing windows address volume but not complexity

Nominal context windows have grown at roughly 30x per year since mid-2023 ([Epoch AI, 2025](https://epoch.ai/data-insights/context-windows)). This addresses the volume dimension — more room for tokens. It does nothing for the complexity dimension. A procedure that requires the agent to track five levels of indirection is equally costly in interpretation whether the window is 8K or 2M tokens.

Even for volume, the gains are partial. The gap between nominal and effective capacity is large — larger windows create more room but also more opportunity for attention dilution. And context demand grows with task ambition: richer tool outputs, longer conversation histories, more complex instructions. This is a Jevons paradox — efficiency gains get absorbed by expanding use cases.

The practical consequence: growing windows reduce pressure on the volume dimension but leave the complexity dimension untouched. Systems that optimise only for token count will still hit complexity-driven degradation regardless of window size.

## What this explains

Context scarcity is the pressure that produces most of the architectural patterns in agent system design. Each pattern responds to one or both dimensions.

**Frontloading and partial evaluation** (complexity). [Pre-computing static parts of instructions](./frontloading-spares-execution-context.md) and inserting results removes procedures from context — the agent receives answers instead of instructions to derive answers. This is the most direct response to the complexity dimension: reduce interpretation overhead by doing the interpretation outside the window.

**Progressive disclosure** (volume). The [context loading strategy](./context-loading-strategy.md) — always-loaded router, on-demand skills, task-specific docs — matches instruction specificity to loading frequency. [Directory-scoped types](./directory-scoped-types-are-cheaper-than-global-types.md) load only when working in that directory. The principle: don't load what you don't need for this task.

**Context management in long-running tasks** (volume). When context accumulates over many turns, systems need strategies to manage it — compaction (summarising history), observation masking (dropping old turns), or sub-agent delegation. All respond to volume pressure: unmanaged context degrades performance well before hitting the window limit ([JetBrains Research, 2025](https://blog.jetbrains.com/research/2025/12/efficient-context-management/); [Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

**Sub-agent isolation** (both). [Sub-agents provide lexically scoped frames](./llm-context-is-composed-without-scoping.md) — fresh context with only what the caller explicitly passes. This addresses volume (tens of thousands of explored tokens stay out of the caller's window) and complexity (the sub-agent gets a clean frame without accumulated reasoning history).

**Navigation design** (volume). [Agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md). Prose-as-title, retrieval-oriented descriptions, context phrases on index entries — all exist to help the agent make reading decisions *without* loading the target. Every pointer that carries enough context to decide "don't follow this" saves the tokens that loading would have cost.

**Instruction notes over data dumps** (complexity). When delegating to a sub-agent, the efficient interface is an instruction note that frontloads the caller's judgment — which documents matter, which sections, what question to answer — rather than passing raw material. The instruction note carries judgment compactly; raw data forces the sub-agent to spend context on discovery the caller already did.

## The analogy to algorithmic complexity

In traditional systems, algorithmic complexity is the dominant cost model because compute scales but algorithmic class doesn't — an O(n²) algorithm stays O(n²) regardless of hardware. Context efficiency plays the same role in agent systems: context windows grow but the fundamental cost model remains. Loosely, the volume dimension is analogous to space complexity and the complexity dimension to time complexity — a compact program can take forever to run, a fast program can use too much memory. The mapping isn't tight, but the lesson is the same: both matter, and optimising only one is insufficient.

Epoch AI's data makes this concrete: windows grow at 30x/year, but effective utilisation grows from a much lower baseline. A system that wastes context on indirection, dead branches, and unnecessary loading will hit degradation regardless of window size, just as an O(n²) algorithm hits walls regardless of CPU speed.

The practical implication: context efficiency should be evaluated at design time, not treated as an optimisation to apply later. Architectural choices — what loads when, what gets frontloaded, where sub-agent boundaries go, how instructions are structured — determine context efficiency structurally. They are hard to retrofit.

---

Sources:
- Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- JetBrains Research (2025). [Cutting through the noise: smarter context management for LLM-powered agents](https://blog.jetbrains.com/research/2025/12/efficient-context-management/).
- Epoch AI (2025). [LLMs now accept longer inputs, and the best models can use them more effectively](https://epoch.ai/data-insights/context-windows).
- Liu et al. (2023). [Lost in the middle: how language models use long contexts](https://arxiv.org/abs/2307.03172).
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](../sources/convexbench-can-llms-recognize-convex-functions.md) — empirical evidence that compositional depth, not token count, drives reasoning degradation.

Relevant Notes:
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the most direct response to complexity-dimension context cost
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — mechanism: the cost model that makes indirection expensive in context but free in code
- [CLAUDE.md is a router, not a manual](./context-loading-strategy.md) — application: progressive disclosure as a response to volume-dimension context cost
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — foundation: flat context means everything competes; sub-agents are the scoping response
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — application: navigation design as volume-saving strategy
- [directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — application: type system designed around context economy
- [generate instructions at build time](./generate-instructions-at-build-time.md) — application: build-time generation as frontloading applied to skill templates
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — intensifies: instructions and data compete as equal tokens with no priority mechanism
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — intensifies: extra context distorts interpretation, not just wastes space
- [Minimum Viable Ontology / Domain Maps](../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.ingest.md) — exemplifies: MVO is distillation under context-efficiency pressure — compress domain knowledge into the smallest vocabulary that fits the context window

Topics:
- [computational-model](./computational-model.md)
- [kb-design](./kb-design.md)
