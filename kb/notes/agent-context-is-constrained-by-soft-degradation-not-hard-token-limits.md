---
description: The binding constraint on agent context is silent degradation across multiple dimensions (volume, complexity, possibly irrelevant context), not the hard token limit providers advertise
type: note
traits: [has-external-sources]
tags: [learning-theory, foundations]
status: current
---

# Agent context is constrained by soft degradation, not hard token limits

Agent context windows have two bounds: a hard token limit and a soft degradation surface. The hard limit is the maximum tokens the model accepts — exceed it and the API rejects the request. The soft bound is where performance silently degrades: missed instructions, shallow reasoning, ignored context — while output remains well-formed.

The soft bound is the binding constraint — performance degrades well before the hard limit is reached. What constrains work is not running out of tokens but the quality of what those tokens do, driven by at least two dimensions: volume and complexity.

## Dimensions of the soft bound

### Volume

More tokens dilute attention. The "lost in the middle" finding ([Liu et al., 2023](https://arxiv.org/abs/2307.03172)) established primacy and recency bias. Anthropic calls this **context rot** ([2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Paulsen's MECW work confirms that usable context can be far below advertised windows and is task-dependent ([Paulsen, 2025](https://arxiv.org/abs/2509.21361)).

Not all tokens are equal. Irrelevant context is particularly damaging: GSM-DC shows power-law error scaling with distractor count in math problems ([Yang et al., 2025](https://arxiv.org/abs/2505.18761)), and Chung et al. find that injecting irrelevant task sequences into a web agent benchmark collapses success rates from 40–50% to under 10% ([Chung et al., 2025](https://arxiv.org/abs/2512.04307)). Bolt-on retrieval (iRAG) provided only modest improvement, suggesting irrelevant context may need to be excluded rather than compensated for — though this rests on a single retrieval approach.

### Complexity

LLMs pay interpretation overhead proportional to context complexity. Every layer of [indirection costs context and interpretation overhead](./indirection-is-costly-in-llm-instructions.md). ConvexBench shows complexity-driven collapse at low token counts: F1 dropped from 1.0 at depth 2 to ~0.2 at depth 100, even though total tokens (5,331 at depth 100) were far below context limits ([Liu et al., 2026](https://arxiv.org/abs/2602.01075)). Compositional depth, not volume, was the bottleneck.

### Open questions

Volume and complexity are distinguishable but not fully separable — reducing volume often reduces complexity as a side effect.

Irrelevant context may be an independent dimension rather than a sub-mechanism of volume. GSM-DC's degradation occurs at token counts that appear too small for pure attention dilution to explain (our inference, not the paper's), suggesting the distractors interfere with reasoning directly. But no source compares same-volume contexts with and without irrelevant material, so the separation from volume is not empirically isolated. Whether complex distractors impose more interference than simple ones at equal token count is also untested.

## The soft bound is invisible

This is the critical property. The hard limit is visible — exceed it and the API returns an error. The soft bound is invisible at every level.

**To the practitioner.** The model doesn't signal when it crosses the soft bound. Output remains well-formed; problems surface downstream. A CPU signals overflow. A human says "I'm confused." An LLM produces confident output whether it attended to your context or silently ignored half of it.

**To the benchmarker.** The soft bound is not a single number. It shifts with task type, compositional depth, information arrangement, and prompt framing. [Effective context is task-relative and complexity-relative, not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md). Model updates shift the degradation surface without notice.

**To the market.** Providers advertise hard token limits because those are clean, comparable numbers. They don't publish soft degradation surfaces — those are task-dependent and hard to characterize. The number on the box describes the bound that rarely binds; the bound that actually constrains work has no number.

## Consequences

**Don't trust the number on the box.** Usable context depends on what you're doing, how you arrange it, and which model version you're running.

**Silent degradation makes heuristic design rational.** Front-loading critical content, decomposing complexity, isolating scopes, compressing aggressively — these are the rational strategy, not a placeholder until better measurement arrives. This is how [every prior tradition facing soft bounds](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) has operated.

**Programmatic constructability is the genuine advantage.** You can programmatically choose every token that enters the context. This creates a distinctive tension: **high control over inputs, low observability of effective processing.** The engineering opportunity is real, but it must be exercised against a bound you cannot directly observe. Default-loading session history is the most common way this advantage goes unexercised — [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md). [Context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) develops the architectural responses.

---

Relevant Notes:

- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **extends**: takes this note's soft-bound claim and dimensions decomposition as premises and derives architectural responses
- [effective context is task-relative and complexity-relative not a fixed model constant](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — sharpens: the soft bound is not a single number but a task-dependent degradation surface
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — mechanism: indirection cost is a soft-bound phenomenon — interpretation overhead degrades silently
- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: observer-relativity is what makes the soft bound task-dependent
- [soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — extends: if the binding constraint is a soft bound, these traditions have relevant coping strategies
- [On the "Induction Bias" in Sequence Models (Ebrahimi et al., 2026)](../sources/induction-bias-sequence-models-ebrahimi-2026.md) — candidate mechanism (volume dimension): transformers learn length-specific solutions in isolation (sharing factor kappa ≈ 1) and suffer destructive interference at mixed lengths (kappa = 0.28). Caveat: training-time evidence on synthetic tasks, not direct measurement of inference-time context degradation
- [GSM-DC ingest](../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) — exemplifies (volume, irrelevant-context mechanism): power-law error scaling with distractor count in math reasoning
- [Web agent benchmark ingest (Chung et al., 2025)](../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md) — exemplifies (volume, irrelevant-context mechanism): agent-level catastrophic degradation from injected irrelevant task sequences; iRAG provides only modest relief
- [ConvexBench ingest](../sources/convexbench-can-llms-recognize-convex-functions.ingest.md) — exemplifies (complexity dimension): compositional depth collapse at low token counts
- [Paulsen MECW](../sources/paulsen-maximum-effective-context-window-mecw.md) — exemplifies (volume dimension): usable context drastically below advertised windows, task-dependent
