---
description: Continuous learning can happen outside of weights; constraining is one symbolic-artifact form where prompts, schemas, tools, and tests accumulate durable adaptive capacity during deployment
type: note
traits: []
tags: [learning-theory]
status: current
---

# Constraining during deployment is continuous learning

AI labs frame "continuous learning" as a weight-update problem: how do you adapt a deployed model to new data, new tasks, and shifting distributions without a full retraining cycle? The standard approaches — fine-tuning on deployment logs, online learning, experience replay — all modify the model's parameters. But [constraining](constraining.md) — accumulating symbolic artifacts like prompts, schemas, evals, tools, and deterministic code — adapts deployed systems through a different mechanism entirely.

Each constraining step [trades generality for compound gains in reliability, speed, and cost](constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). Extracting a deterministic `format_date()` function makes date formatting reliable, fast, and cheap. Versioning a system prompt with house style examples makes tone consistent across sessions. Adding a validation script catches errors that previously required human review. These gains persist, accumulate, and compose — and they produce the same narrowing of the behavior distribution that fine-tuning targets, just through inspectable, rollbackable artifacts instead of opaque weight updates.

Herbert Simon: learning is any change that produces a more or less permanent change in a system's [capacity for adapting to its environment](learning-is-not-only-about-generality.md). Constraining during deployment meets every part of this definition — it changes the system (new or modified artifacts), the change is permanent (versioned, committed), and the capacity for adaptation improves. The definition doesn't require weight updates. It requires capacity change.

This note is therefore a subset claim, not the umbrella claim. It does not argue that symbolic artifacts are the only continuous-learning substrate. It argues that constraining is one concrete way continuous learning happens outside weights.

This isn't hypothetical. Systems like DSPy and ProTeGi already automate one slice of constraining — searching over prompt components to optimize against an objective — and the ML community recognizes this as learning. Research on [professional developers using AI agents](../sources/professional-software-developers-dont-vibe-they-control.ingest.md) shows the same pattern in manual form: developers iteratively refine prompts, tools, and workflows based on deployment experience. Agent memory systems (Claude's memory files, Cursor rules, AGENTS.md conventions) store preferences across sessions. All of this is continuous learning through constraining — it just isn't recognized as such.

Weight-based learning captures distributional knowledge (style, tone, world knowledge) that doesn't reduce to explicit artifacts — not all continuous learning is constraining. But the extractable, testable subset that constraining handles covers most of what deployed systems need. The manual version works; [automating the judgment-heavy parts](./automating-kb-learning-is-an-open-problem.md) is where the real gap is.

---

Relevant Notes:

- [Continuous learning requires durability, not weight updates](./continuous-learning-requires-durability-not-weight-updates.md) — foundation: this note is one concrete non-weight case, not the general claim
- [Learning substrates, backends, and artifact forms](./learning-substrates-backends-and-artifact-forms.md) — sharpens: constraining operates on one family of symbolic artifacts regardless of whether they live in repos or other backends
- [constraining](constraining.md) — foundation: the general mechanism; this note argues it constitutes continuous learning during deployment
- [constraining and distillation both trade generality for compound](constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — foundation: the trade-off that constraining operates on
- [learning is not only about generality](learning-is-not-only-about-generality.md) — foundation: Simon's definition of capacity change that grounds the claim
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — applies: the vocabulary gap and automation challenge that follow from recognising constraining as continuous learning
- [Professional developers don't vibe — they control](../sources/professional-software-developers-dont-vibe-they-control.ingest.md) — empirical evidence that developers naturally practice the constraining loop
