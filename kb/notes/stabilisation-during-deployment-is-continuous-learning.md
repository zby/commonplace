---
description: Continuous learning — adapting deployed systems to new data and tasks — is what stabilisation with versioned artifacts already achieves per Simon's definition; fine-tuning and prompt optimization target the same behavioral changes through different mechanisms
type: note
traits: []
areas: [learning-theory]
status: current
---

# Stabilisation during deployment is continuous learning

AI labs frame "continuous learning" as a weight-update problem: how do you adapt a deployed model to new data, new tasks, and shifting distributions without a full retraining cycle? The standard approaches — fine-tuning on deployment logs, online learning, experience replay — all modify the model's parameters. But [stabilisation](stabilisation.md) — accumulating versioned repo artifacts like prompts, schemas, evals, tools, and deterministic code — adapts deployed systems through a different mechanism entirely.

Each stabilisation step [trades generality for compound gains in reliability, speed, and cost](stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). Extracting a deterministic `format_date()` function makes date formatting reliable, fast, and cheap. Versioning a system prompt with house style examples makes tone consistent across sessions. Adding a validation script catches errors that previously required human review. These gains persist, accumulate, and compose — and they produce the same narrowing of the behavior distribution that fine-tuning targets, just through inspectable, rollbackable artifacts instead of opaque weight updates.

Herbert Simon: learning is any change that produces a more or less permanent change in a system's [capacity for adapting to its environment](learning-is-not-only-about-generality.md). Stabilisation during deployment meets every part of this definition — it changes the system (new or modified artifacts), the change is permanent (versioned, committed), and the capacity for adaptation improves. The definition doesn't require weight updates. It requires capacity change.

This isn't hypothetical. Systems like DSPy and ProTeGi already automate one slice of stabilisation — searching over prompt components to optimize against an objective — and the ML community recognizes this as learning. Research on [professional developers using AI agents](related_works/professional-developers-ai-agents.md) shows the same pattern in manual form: developers iteratively refine prompts, tools, and workflows based on deployment experience. Agent memory systems (Claude's memory files, Cursor rules, AGENTS.md conventions) store preferences across sessions. All of this is continuous learning through stabilisation — it just isn't recognized as such.

Weight-based learning captures distributional knowledge (style, tone, world knowledge) that doesn't reduce to explicit artifacts — not all continuous learning is stabilisation. But the extractable, testable subset that stabilisation handles covers most of what deployed systems need. The manual version works; [automating the judgment-heavy parts](./automating-kb-learning-is-an-open-problem.md) is where the real gap is.

---

Relevant Notes:

- [stabilisation](stabilisation.md) — foundation: the general mechanism; this note argues it constitutes continuous learning during deployment
- [stabilisation and distillation both trade generality for compound](stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — foundation: the trade-off that stabilisation operates on
- [learning is not only about generality](learning-is-not-only-about-generality.md) — foundation: Simon's definition of capacity change that grounds the claim
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — applies: the vocabulary gap and automation challenge that follow from recognising stabilisation as continuous learning
- [professional-developers-ai-agents](related_works/professional-developers-ai-agents.md) — empirical evidence that developers naturally practice the stabilisation loop

Topics:

- [learning-theory](./learning-theory.md)
