---
description: What works, what doesn't, what needs testing — empirical observations about KB operations and prompt design
type: index
status: current
---

# Evaluation

What works, what doesn't, what needs testing. Empirical observations about KB operations, prompt design, and techniques from other systems.

## Notes

- [cludebot](./related-systems/cludebot.md) — techniques from cludebot worth borrowing; richest trajectory-to-lesson loop reviewed
- [prompt-ablation-converts-human-insight-to-deployable-framing](./prompt-ablation-converts-human-insight-to-deployable-framing.md) — methodology for testing prompt framings
- [single-artifact review bundles still cut Claude costs substantially after cache-aware weighting](./evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially-after-cache-aware-weighting.md) — cache-weighted April 2-4, 2026 evidence that the single-artifact refactor remained a significant cost win under Anthropic's prompt-caching prices
- [systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md) — controlled variation as a family of methods: decorrelating checks, measuring brittleness, and distinguishing both from Deutsch-style reach review
- [brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles](./brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) — experimental ladder for comparing scalar and pairwise judges before treating pairwise ranking as a stronger soft oracle

## Other tagged notes <!-- generated -->

- [Elicitation requires maintained question-generation systems](./elicitation-requires-maintained-question-generation-systems.md) — Four elicitation strategies ordered by user expertise required, composable into review architectures with maintenance loops that prevent ossification
- [Evaluation automation is phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — Optimization loops require manual error analysis and judge calibration before automation can improve behavior rather than just score
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — Distinguishes stored knowledge (retrievable on direct probe) from contextually activated knowledge (brought to bear during task execution without being directly queried); formalizes the activation gap and the expertise gap
