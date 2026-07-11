---
description: What works, what doesn't, what needs testing — empirical observations about KB operations and prompt design
type: kb/types/tag-readme.md
index_source: tag
index_key: evaluation
---

# Evaluation

What works, what doesn't, what needs testing. Empirical observations about KB operations, prompt design, and techniques from other systems.

## Notes

- [cludebot](../agent-memory-systems/reviews/cludebot.md) — techniques from cludebot worth borrowing; richest trajectory-to-lesson loop reviewed
- [prompt-ablation-converts-human-insight-to-deployable-framing](./prompt-ablation-converts-human-insight-to-deployable-framing.md) — methodology for testing prompt framings
- [single-artifact review bundles still cut Claude costs substantially after cache-aware weighting](./evidence/single-artifact-review-bundles-still-cut-claude-costs-substantially.md) — cache-weighted April 2-4, 2026 evidence that the single-artifact refactor remained a significant cost win under Anthropic's prompt-caching prices
- [systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — controlled variation as a family of methods: decorrelating checks, measuring brittleness, and distinguishing both from Deutsch-style reach review
- [brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles](./brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) — experimental ladder for comparing scalar and pairwise judges before treating pairwise ranking as a stronger soft oracle
