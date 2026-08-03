---
description: "Continual Harness adds a reset-free all-three-form learning case, bounded by direct edit adoption, low artifact reuse, and a fixed embodied-game decomposition"
source_snapshot: "continual-harness-online-adaptation-foundation-agents.md"
ingested: "2026-08-02"
type: kb/sources/types/ingest-report.md
domains: [harness-learning, self-improvement, representational-form, embodied-agents]
---

# Ingest: Continual Harness: Online Adaptation for Self-Improving Foundation Agents

Source: [continual-harness-online-adaptation-foundation-agents.md](continual-harness-online-adaptation-foundation-agents.md)
Captured: 2026-08-02
From: https://arxiv.org/html/2605.09998v1?utm_source=chatgpt.com

## Classification

Genre: scientific-paper -- an arXiv v1 preprint that specifies two online adaptation loops and reports controlled harness conditions, model comparisons, mechanism measurements, and training runs.
Domains: harness-learning, self-improvement, representational-form, embodied-agents
Author: Seth Karten, Joel Zhang, Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, and Kiran Vodrahalli, affiliated with Princeton University, ARISE Foundation, and Google DeepMind; the paper is recent and its results have not been independently reproduced in this KB.

## Summary

Continual Harness turns an embodied agent's prompt, sub-agents, skill library, and memory into mutable runtime state. During one continuous Pokémon episode, an LLM Refiner periodically reads recent trajectory failures and applies component-specific edits; a second loop runs an open-source model inside that changing harness, uses a process reward model and frontier teacher to relabel weak windows, and updates the model with soft SFT while preserving emulator state. Across Red and Emerald, the authors report that the refining harness recovers much of the button-efficiency gap between a minimalist and expert harness for Gemini Pro, produces mixed gains for Flash, and harms Flash-Lite; separate measurements show navigation skills approaching a pathfinding oracle, sparse reuse of stored memory, and sustained but bursty milestone progress in selected Gemma training runs.

## Connections Found

This paper is a second empirical anchor, alongside [Co-Harness](co-harness-co-evolving-harness-and-model-weights.ingest.md), for [continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md): natural-language prompt and memory, symbolic skills and tools, and distributed-parametric weights remain separately mutable but coupled through the same trajectory. Its distinctive role is the reset-free, mid-episode instance of [the readable-artifact loop](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). The Refiner's trajectory windows and failure signatures instantiate [diagnostic richness](../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), while comparison with [Self-Harness](self-harness-harnesses-that-improve-themselves.ingest.md) and [Agentic Harness Engineering](../agent-memory-systems/reviews/agentic-harness-engineering.md) distinguishes architectures: Self-Harness exposes reject-capable proposal selection and regression-gated adoption, while Continual Harness directly determines and adopts edits. Interpretation rests on [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), because the paper varies some harness state and model capability without varying the observation/action interface, four-part harness partition, refinement protocol, or reward design.

## Extractable Value

1. **Reset-free adaptation makes the failure-to-repair interval a design variable** -- a failed skill invocation can be diagnosed, edited, and retried inside the same long episode, preserving late-stage state that reset-based methods cannot cheaply reconstruct. This adds an online timescale to the KB's current harness-learning cases, which mostly revise between benchmark rounds. [quick-win]
2. **The paper supplies a second, structurally different all-three-form loop** -- model weights learn across iterations while prompt, sub-agent, skill, and memory artifacts change within each iteration; unlike Co-Harness, the trajectory-generating environment also persists. This strengthens the existence claim for cross-form coevolution while widening the unresolved credit-assignment problem. [deep-dive]
3. **Component measurements separate invocation, repair, and reuse** -- navigation skills approach a BFS/Dijkstra-derived oracle and are repeatedly repaired, sub-agent handoffs reduce context cost, but from-scratch memory is written much more often than it is consulted and most authored skills are never used. The result argues for measuring artifact effects and lifecycle, not counting writes or store growth as learning. [experiment]
4. **Adaptive scaffolding has a capability floor** -- Continual Harness is Pareto-beneficial for Pro, unstable for Flash, and worse than the minimalist harness for Flash-Lite. Relative to [scaffolding absorption](../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md), this suggests a useful distinction between fixed scaffolding that substitutes for model capability and revisable scaffolding whose value depends on enough capability to author and exploit it. [quick-win]
5. **The effective update space can be audited precisely** -- behavior can condition on frames, local text maps, trajectory history, failure signatures, stored harness state, PRM scores, and teacher relabels; it can compose button actions plus CRUD edits over prompts, sub-agents, executable skills, and memory, with Gemma weight mappings added by soft SFT. Fixed outside that space are the game-derived representation, action basis, four-component partition, meta-tools, refiner schedule and passes, model architectures, reward categories, teacher, milestones, and game family. [deep-dive]
6. **Direct adoption concentrates trust in the evidence-to-edit rule** -- Refiner edits become operative on the next step without a separately rejectable candidate. This is a direct-update architecture, not an omitted universal function; its warrant rests on the fixed Refiner rule and its evidence, while the create-and-forget tail shows that live revision does not establish later artifact uptake or systematic retirement. [experiment]

## Limitations (our opinion)

The evaluation is narrow and the causal claims are under-isolated. Red and Emerald share one game family, the harness comparisons use at least three seeds, and the prominent human-in-the-loop completion record mixes human-authored and agent-authored changes. The online Gemma result combines a refined harness, PRM scoring, frontier-teacher relabeling, soft SFT, persistent emulator state, prior supervised warm-up, and offline GRPO; there is no matched fixed-harness SFT arm, no same-budget reset-based arm, and no factorial comparison that assigns milestone progress specifically to model-harness co-learning. Figure 7 describes the five advancing runs while the appendix says multiple jobs were run, so the absence of a stated denominator limits how strongly the staircase plots support robustness.

The component evidence should not be over-read as validation of the full decomposition. The pathfinding comparison directly tests refined navigation skills against an oracle; bootstrap-frozen versus bootstrap-updating varies continued refinement of an inherited harness; memory and sub-agent analyses mostly measure use and correlated progression. None of these tests whether prompt, sub-agent, skill, and memory are the best partition, whether the local text map and button basis preserve every useful distinction and response, or whether the fixed Refiner schedule, four-pass edit protocol, PRM categories, and milestone objective define the right learning space. Improvement occurs within that compound configuration. The low absolute memory-reference rate, unused-skill tail, Flash-Lite regression, lack of convergence evidence, fixed evidence-to-edit rule, and uneven later artifact use further bound any claim of general or reliably compounding self-improvement.

## Recommended Next Action

Update [Treat continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md) to add Continual Harness as the second automated all-three-form case and contrast its reset-free direct-adoption loop with Co-Harness's regression-gated alternating loop, retaining the missing matched-control and fixed-decomposition caveats.
