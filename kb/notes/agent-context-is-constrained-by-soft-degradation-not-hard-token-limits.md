---
description: The binding constraint on agent context is silent degradation — undisclosed, unmeasured, and invisible at the point of failure — not the hard token limit providers advertise. The soft bound operates across two dimensions (volume and complexity) while the hard bound is volume-only.
type: note
traits: [has-external-sources]
tags: [learning-theory, foundations]
status: current
---

# Agent context is constrained by soft degradation, not hard token limits

Agent context windows have two bounds: a hard token limit and a soft degradation curve. The hard limit is the maximum number of tokens the model accepts. The soft bound is where context loading silently degrades the model's ability to follow instructions, retrieve information, and reason correctly.

The hard limit is not the binding constraint. Context windows have grown roughly 30x per year since mid-2023 and now exceed 1M tokens; for most practical tasks, the window never fills. What constrains work is the soft bound — performance degradation that sets in well before the hard limit, driven by two dimensions developed below: volume and complexity.

## Two dimensions of the soft bound

The hard bound is a volume-only phenomenon — exceed the token limit and the API rejects the request. The soft bound operates across two dimensions, which partly explains why it dominates.

### Volume: how many tokens

More tokens dilute attention. The "lost in the middle" finding ([Liu et al., 2023](https://arxiv.org/abs/2307.03172)) established primacy and recency bias. Anthropic calls this **context rot** — degradation in recall and reasoning as the window fills ([Anthropic, 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). The resource doesn't just run out; it degrades before it exhausts. Paulsen's MECW work confirms that usable context can be far below advertised windows and is task-dependent ([2025](../sources/paulsen-maximum-effective-context-window-mecw.md)).

### Complexity: how hard the tokens are to use

LLMs pay interpretation overhead proportional to context complexity. Loading a procedure costs more than loading the result it would produce. Every layer of [indirection costs context and interpretation overhead](./indirection-is-costly-in-llm-instructions.md) on every read. ConvexBench shows complexity-driven collapse at low token counts — compositional depth, not volume, was the bottleneck ([Liu et al., 2026](../sources/convexbench-can-llms-recognize-convex-functions.md)).

### The interaction

Volume often creates complexity — more tokens means more potential for interference, scope leakage, and competing instructions. The dimensions are distinguishable but not fully separable; reducing volume often reduces complexity as a side effect.

The soft bound is what practitioners actually fight. When an agent misses an instruction, hallucinates a tool argument, or ignores a relevant document, the context was rarely full. It was too noisy, too complex, or arranged in a way the model couldn't effectively use. [Context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) develops the architectural responses to both dimensions.

## The soft bound is invisible and undisclosed

This is the critical property. The hard limit is visible — exceed it and the API returns an error. The soft bound is invisible at every level:

**To the practitioner at the point of failure.** The model doesn't signal when it crosses the soft bound. Quality degrades — missed instructions, shallow reasoning, ignored context — but output remains well-formed. Problems surface downstream, and attribution is ambiguous. A CPU signals overflow. A human says "I'm confused." An LLM produces confident output whether it attended to your carefully arranged context or silently ignored half of it.

**To the benchmarker.** The soft bound is not a single number. It shifts with task type, compositional depth, information arrangement, and prompt framing. [Effective context is task-relative and complexity-relative, not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md). Volume and complexity interact but are hard to isolate. Model updates shift the degradation curve without notice. There is no specification to test against — only a gradient.

**To the market.** LLM providers advertise hard token limits — "1M context," "2M context" — because those are clean, comparable numbers. They don't publish soft degradation curves; those are task-dependent and genuinely hard to characterize. Features like session summarization, context compaction, and auto-truncation exist, but whether these respond to soft degradation or hard-limit pressure is unclear. Either way, the marketed metric remains the hard limit, and the soft bound is left to practitioners to discover empirically, per task, per model version. The number on the box describes the bound that rarely binds; the bound that actually constrains work has no number.

## Consequences for practitioners

**Don't trust the number on the box.** A 1M-token context window does not mean you have 1M tokens of usable context. Usable context depends on what you're doing, how you arrange it, and which model version you're running. Build degradation awareness through downstream evaluation, not token counting.

**Silent degradation makes heuristic design rational.** If you can't measure the soft bound precisely, heuristic architectural responses — front-loading critical content, decomposing complexity, isolating scopes, compressing aggressively — are the rational strategy, not a placeholder until better measurement arrives. This is how [every prior tradition facing soft bounds](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) has operated for decades.

**Programmatic constructability is the genuine advantage.** What distinguishes agent context from prior soft-bound traditions is not the hardness of the bound but the constructability of the input. You can programmatically choose every token that enters the context — arrange, reorder, pre-compute, strip, decompose across isolated contexts. This creates a distinctive tension: **high control over inputs, low observability of effective processing.** The engineering opportunity is real, but it must be exercised against a bound you cannot directly observe.

---

Relevant Notes:

- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **extends**: takes this note's soft-bound claim and two-dimensions decomposition as premises and derives architectural responses
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — sharpens: the soft bound is not a single number but a task-dependent degradation surface
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — mechanism: indirection cost is a soft-bound phenomenon — interpretation overhead degrades silently
- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: observer-relativity is what makes the soft bound task-dependent
- [soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — extends: if the binding constraint is a soft bound, these traditions have relevant coping strategies
