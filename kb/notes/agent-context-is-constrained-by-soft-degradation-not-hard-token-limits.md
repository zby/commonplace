---
description: Agent context is bounded by silent reliability degradation across volume, complexity, and relevance/interference, not just by provider token limits
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, foundations]
status: current
---

# Agent context is constrained by soft degradation, not hard token limits

Agent context windows have two bounds: a hard token limit and a soft degradation surface. The hard limit is the maximum tokens the model accepts — exceed it and the API rejects the request. The soft bound is where performance silently degrades: missed instructions, shallow reasoning, ignored context — while output remains well-formed.

The soft bound is the binding constraint — performance degrades well before the hard limit is reached. What constrains work is not running out of tokens but the quality of what those tokens do, driven by at least three dimensions: volume, complexity, and relevance/interference. Other factors — information arrangement and prompt framing — also shift the degradation surface, often by changing one of these dimensions indirectly.

## Dimensions of the soft bound

### Volume

More tokens dilute attention. The "lost in the middle" finding ([Liu et al., 2023](https://arxiv.org/abs/2307.03172)) established primacy and recency bias — models overweight information near the beginning and end of the context, underweighting the middle. Because agent prompts face the same flat-sequence selection problem, this positional bias applies whenever the model must recover the right items from a long unscoped context. Anthropic (the AI lab) calls this **context rot** ([2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Paulsen's Maximum Effective Context Window (MECW) work confirms that usable context can be far below advertised windows and is task-dependent ([Paulsen, 2025](https://arxiv.org/abs/2509.21361)).

### Relevance/interference

Not all tokens are equal. Irrelevant context is not merely extra volume; it can actively interfere with task execution. GSM-DC, a math-reasoning benchmark with synthetic distractors, shows power-law error scaling with distractor count ([Yang et al., 2025](https://arxiv.org/abs/2505.18761)). The interaction with reasoning depth is the key signal: distractors hurt more as the task requires more dependent steps, and they degrade both reasoning path selection and arithmetic execution.

The same pattern appears at the agent-workflow level. Chung et al. find that injecting irrelevant task sequences into web-agent benchmarks collapses success rates from 40-50% to under 10% ([Chung et al., 2025](https://arxiv.org/abs/2512.04307)). The failures are not just slower retrieval from a larger context; agents loop, lose objectives, and treat stale history as live problem state. Bolt-on retrieval (iRAG) provides only modest improvement in that benchmark, which is weak but useful evidence that irrelevant context often needs to be excluded or scoped away rather than compensated for after loading.

This is why the mitigation is architectural. Summarization can shrink irrelevant material, but it does not by itself decide whether the material belongs in the active problem frame. Selective loading, scoped state, and sub-agent boundaries attack relevance/interference directly by preventing non-task state from competing with the task.

### Complexity

Some forms of context complexity add interpretation overhead. Every layer of [indirection costs context and interpretation overhead](./indirection-is-costly-in-llm-instructions.md), and deeper compositional structure may impose similar costs. ConvexBench, a benchmark on compositional symbolic reasoning, shows complexity-driven collapse at low token counts: F1 dropped from 1.0 at depth 2 to ~0.2 at depth 100, even though total tokens (5,331 at depth 100) were far below context limits ([Liu et al., 2026](https://arxiv.org/abs/2602.01075)). The shared mechanism is that both agent operations and symbolic reasoning fail when the model must carry many intermediate dependencies without scoped subproblems or externalized state. Compositional depth, not volume, was the bottleneck.

### Open questions

Volume, complexity, and relevance/interference are distinguishable but not fully separable — reducing volume often reduces complexity and interference as side effects.

The main unresolved question is interaction, not existence. GSM-DC cleanly shows that distractor count and reasoning depth interact in synthetic math problems; web-agent benchmarks show an agent-level analogue under long multi-session histories. We do not yet know how stable the interaction surface is across natural-language tasks, partially relevant material, or different model families.

## The soft bound is invisible

The hard limit is visible — exceed it and the API returns an error. The soft bound is invisible at every level.

**To the practitioner.** The model doesn't signal when it crosses the soft bound. Output remains well-formed; problems surface downstream. A CPU signals overflow. A human says "I'm confused." An LLM produces fluent output whether it reflects the supplied context or leaves large portions unused.

**To the benchmarker.** The soft bound is not a single number. It shifts with task type, compositional depth, relevance mix, information arrangement, and prompt framing. [Effective context is task-relative and complexity-relative, not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md). Model updates shift the degradation surface without notice.

**To the market.** Providers advertise hard token limits because those are clean, comparable numbers. They don't publish soft degradation surfaces — those are task-dependent and hard to characterize. The number on the box describes the bound that rarely binds; the bound that actually constrains work has no number.

## Consequences

**Don't trust the number on the box.** Usable context depends on what you're doing, how you arrange it, and which model version you're running.

**Silent degradation makes heuristic design rational.** Front-loading critical content, decomposing complexity, isolating scopes, compressing aggressively, and excluding irrelevant state are the rational strategy, not a placeholder until better measurement arrives. This is how [surveyed traditions facing soft bounds](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) have operated.

**Programmatic constructability is the genuine advantage.** You can programmatically choose every token that enters the context. This creates a distinctive tension: **high control over inputs, low observability of effective processing.** The engineering opportunity is real, but it must be exercised against a bound you cannot directly observe. Default-loading session history is the most common way this advantage goes unexercised — [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md). The [context-efficiency note](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) develops the architectural responses.

---

Relevant Notes:

- [Context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **extends**: takes this note's soft-bound claim and dimensions decomposition as premises and derives architectural responses
- [Effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — sharpens: the soft bound is not a single number but a task-dependent degradation surface
- [Indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — mechanism: indirection cost is a soft-bound phenomenon — interpretation overhead degrades silently
- [Information value is observer-relative](./information-value-is-observer-relative.md) — grounds: observer-relativity is what makes the soft bound task-dependent
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — complements: soft degradation supplies one mechanism for why relevant knowledge can stay stored but fail to activate when extra context dilutes or crowds out the right cues
- [Soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — extends: if the binding constraint is a soft bound, these traditions have relevant coping strategies
- [On the "Induction Bias" in Sequence Models (Ebrahimi et al., 2026)](https://arxiv.org/pdf/2602.18333) — candidate mechanism (volume dimension): transformers learn largely length-specific solutions in isolation and show much weaker sharing when lengths are mixed
  - Caveat: training-time evidence on synthetic tasks, not direct measurement of inference-time context degradation
- [GSM-DC ingest](https://arxiv.org/html/2505.18761v2) — exemplifies (relevance/interference dimension): power-law error scaling with distractor count in math reasoning, with reasoning-depth interaction
- [Web agent benchmark ingest (Chung et al., 2025)](https://arxiv.org/html/2512.04307v1) — exemplifies (relevance/interference dimension): agent-level catastrophic degradation from injected irrelevant task sequences; iRAG provides only modest relief
- [ConvexBench ingest](https://arxiv.org/html/2602.01075v2) — exemplifies (complexity dimension): compositional depth collapse at low token counts
- [Paulsen MECW](https://arxiv.org/pdf/2509.21361) — exemplifies (volume dimension): usable context drastically below advertised windows, task-dependent
