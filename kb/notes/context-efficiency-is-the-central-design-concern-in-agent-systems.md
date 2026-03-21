---
description: Context is the scarce resource in agent systems — not compute, memory, or storage. This note operationalizes the soft-bound premise (volume and complexity dimensions, decomposed in the soft-degradation note) into architectural responses, making context efficiency the central design concern.
type: note
traits: [has-external-sources]
tags: [computational-model, foundations]
status: current
---

# Context efficiency is the central design concern in agent systems

In traditional systems, the scarce resources are compute, memory, storage, and bandwidth; algorithmic complexity is the dominant cost model. In agent systems, the scarce resource is context — the finite window of tokens the agent can attend to. Context is not just another resource. It is the *only channel* through which an agent receives instructions, understands its task, accesses knowledge, and reasons toward action. A CPU has registers, cache, RAM, disk, and network as separate tiers. An LLM has one context window. Everything competes for the same space.

Context is the lowest-degree-of-freedom resource in agent systems: unitary, impossible to tier, and hard to expand without architectural change. This is an application of [solve low-degree-of-freedom subproblems first to avoid blocking better designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md) — optimize the tightest constraint before others, or later choices will be forced into low-quality tradeoffs.

The binding constraint is soft degradation, not hard token limits — established in [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). Hard limits are visible but rarely binding; the model degrades before hitting them. This note operationalizes that premise as a cost model and set of architectural responses.

Anthropic's engineering team has converged on the same framing, defining **context engineering** as "strategies for curating and maintaining the optimal set of tokens during LLM inference" and describing context as "a critical but finite resource" with an **attention budget** that "every token depletes" ([Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Independent practitioner evidence comes from OpenAI's Codex team: shipping 1M lines of agent-generated code required a 100-line AGENTS.md as a router with pointers to deeper docs — "a map, not a manual" — because the bottleneck was not model capability but the structure of what loaded into context ([Lopopolo, 2026](../sources/harness-engineering-leveraging-codex-agent-first-world.md)).

One property of the medium intensifies this scarcity: natural language has [underspecified semantics](./agentic-systems-interpret-underspecified-instructions.md) with no enforced boundaries — not between instructions and data ([homoiconicity](./llm-context-is-a-homoiconic-medium.md)), not between scopes, not between priority levels. Extra context doesn't just waste space — it can dilute instructions, contaminate scopes, and distort interpretation.

## Prior work

Scarce attention as a central design constraint is well-established:

- **Attention economics** (Simon, 1971) — "a wealth of information creates a poverty of attention." The context window is the literal implementation of this.
- **Working memory** (Miller, 1956; Cowan, 2001) — limited capacity where everything competes for slots. Context windows are working memory for agents.
- **Information overload** (Toffler, 1970) — too much information degrades decision quality, not just slows it.

What's specific to agent systems is the unitary channel (one context window, no separate tiers), the hard token limit, and the interaction between volume and complexity.

**TODO:** This survey is from the agent's training data, not systematic. Revisit with deep search — Paulsen partially answers the degradation-curve question with task-dependent MECW measurements, but the broader attention-economics / working-memory literature and the optimal-loading-strategy question remain open.

## Volume and complexity

The soft bound operates across two dimensions — volume (how many tokens) and complexity (how hard they are to use) — decomposed in [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md). The dimensions are distinguishable but not fully separable; reducing volume often reduces complexity as a side effect. Most architectural responses affect both, but each has a primary target.

Practitioner evidence confirms the volume dimension as a primary concern: Koylan's Personal Brain OS reduced token usage by 40% by splitting merged modules into isolated scopes ([Koylan, 2026](../sources/koylanai-personal-brain-os.md)) — a pure volume intervention with outsized impact on agent reliability. The key point for this note: large windows do not remove complexity costs, and raw token count alone does not predict usable context.

## Growing windows address volume but not complexity

Nominal context windows have grown at roughly 30x per year since mid-2023 ([Epoch AI, 2025](https://epoch.ai/data-insights/context-windows)). This addresses volume but does nothing for complexity. A five-level indirection chain is equally costly whether the window is 8K or 2M tokens.

Even for volume, the gains are partial. Context demand grows with task ambition — richer tool outputs, longer histories, more complex instructions. This is a Jevons paradox: efficiency gains get absorbed by expanding use cases.

## Architectural responses

Context scarcity produces most architectural patterns in agent system design. Most responses affect both dimensions, but each has a primary target:

- **Frontloading and partial evaluation** (primarily complexity) — [pre-compute static parts](./frontloading-spares-execution-context.md) so the agent receives answers instead of procedures to derive them
- **Progressive disclosure** (both) — the [instruction specificity principle](./instruction-specificity-should-match-loading-frequency.md) matches instruction specificity to loading frequency; [directory-scoped types](./directory-scoped-types-are-cheaper-than-global-types.md) load only when working in that directory. Reduces volume directly and complexity as a side effect — fewer loaded instructions means less scope contamination and fewer competing directives
- **Context management** (primarily volume) — compaction, observation masking, and sub-agent delegation manage accumulation in long-running tasks ([JetBrains Research, 2025](https://blog.jetbrains.com/research/2025/12/efficient-context-management/))
- **Sub-agent isolation** (both) — [sub-agents provide lexically scoped frames](./llm-context-is-composed-without-scoping.md) with only what the caller explicitly passes, addressing volume and complexity simultaneously
- **Navigation design** (primarily volume) — [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md); prose-as-title and retrieval-oriented descriptions let the agent decide "don't follow this" without loading the target
- **Instruction notes over data dumps** (primarily complexity) — frontload the caller's judgment about which documents matter and what question to answer, rather than passing raw material

If context is the only fundamental scarce resource, then the natural computational model is [symbolic scheduling over bounded LLM calls](./bounded-context-orchestration-model.md): exact bookkeeping lives in code, while bounded context is reserved for semantic judgment.

Context efficiency should be evaluated at design time, not treated as an optimization to apply later. Architectural choices — what loads when, what gets frontloaded, where sub-agent boundaries go — determine context efficiency structurally and are hard to retrofit.

---

Sources:
- Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
- JetBrains Research (2025). [Cutting through the noise: smarter context management for LLM-powered agents](https://blog.jetbrains.com/research/2025/12/efficient-context-management/).
- Epoch AI (2025). [LLMs now accept longer inputs, and the best models can use them more effectively](https://epoch.ai/data-insights/context-windows).
- Liu et al. (2023). [Lost in the middle: how language models use long contexts](https://arxiv.org/abs/2307.03172).
- Liu et al. (2026). [ConvexBench: Can LLMs recognize convex functions?](../sources/convexbench-can-llms-recognize-convex-functions.md) — empirical evidence that compositional depth, not token count, drives reasoning degradation.
- Paulsen (2025). [Context Is What You Need — The Maximum Effective Context Window](../sources/paulsen-maximum-effective-context-window-mecw.md) — convergent evidence: MECW << MCW across 11 models, but tasks confound volume with LLM-hard exact enumeration, making this a volume × task-difficulty finding rather than pure volume degradation.
- Lopopolo (2026). [Harness engineering: leveraging Codex in an agent-first world](../sources/harness-engineering-leveraging-codex-agent-first-world.md) — independent practitioner convergence on context-as-scarce-resource from 1M LOC agent-generated codebase.
- Koylan (2026). [Koylanai Personal Brain OS](../sources/koylanai-personal-brain-os.md) — 40% token reduction from module isolation demonstrates volume-dimension context efficiency.

Relevant Notes:

- [solve low-degree-of-freedom subproblems first to avoid blocking better designs](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md) — application: this note treats context as the lowest-degree-of-freedom resource and derives architecture priorities from that constraint
- [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — **grounds**: establishes the binding-constraint premise and two-dimensions decomposition this note operationalizes as architectural responses
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: the most direct response to complexity-dimension context cost
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — mechanism: the cost model that makes indirection expensive in context but free in code
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — application: progressive disclosure as a response to volume-dimension context cost
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — foundation: flat context means everything competes; sub-agents are the scoping response
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — application: navigation design as volume-saving strategy
- [directory-scoped types are cheaper than global types](./directory-scoped-types-are-cheaper-than-global-types.md) — application: type system designed around context economy
- [generate instructions at build time](./generate-instructions-at-build-time.md) — application: build-time generation as frontloading applied to skill templates
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — sharpens: makes explicit why usable context cannot be treated as a single per-model number
- [LLM context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — intensifies: instructions and data compete as equal tokens with no priority mechanism
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — intensifies: extra context distorts interpretation, not just wastes space
- [Minimum Viable Ontology / Domain Maps](../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology-or-li-2029332670115614799.ingest.md) — exemplifies: MVO is distillation under context-efficiency pressure — compress domain knowledge into the smallest vocabulary that fits the context window
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — exemplifies: "give Codex a map, not a 1,000-page instruction manual" is independent practitioner convergence on context scarcity as the binding constraint
- [Harness Engineering as Cybernetics (@odysseus0z, 2026)](../sources/harness-engineering-is-cybernetics-2030416758138634583.ingest.md) — grounds: frames context-efficient agent runtime design as feedback-loop calibration from control theory — the shift from direct code production to sensor-actuator design is the same shift this note identifies as moving from capability to context structure
- [The Anatomy of an Agent Harness (Vtrivedy10, 2026)](../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) — exemplifies: derives runtime components (filesystem, sandbox, context management, skills) by working backwards from model limitations — instantiates the architectural responses this note describes abstractly with concrete primitives (compaction, tool-call offloading, progressive tool loading)
- [Epiplexity (Bates et al., 2026)](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — grounds: formalizes the complexity dimension of context cost — epiplexity quantifies structural accessibility under computational bounds, giving theoretical backing to "how hard the tokens are to use"
- [AgeMem (Yu et al., 2025)](../sources/agentic-memory-learning-unified-long-term-and-short-term-memory-management.ingest.md) — exemplifies: RL-trained STM operations (Retrieve/Summary/Filter) achieve 3-5% token reduction while maintaining performance — empirical evidence that learned context management can outperform heuristic approaches
