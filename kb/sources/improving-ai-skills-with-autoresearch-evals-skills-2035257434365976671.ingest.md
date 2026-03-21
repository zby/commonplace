---
description: Three-take Auto Research field report where optimization only worked after manual error analysis, failure taxonomy design, and judge calibration across the Three Gulfs.
source_snapshot: improving-ai-skills-with-autoresearch-evals-skills-2035257434365976671.md
ingested: 2026-03-21
type: practitioner-report
domains: [evals, verification, skill-optimization]
---

# Ingest: Improving AI Skills with autoresearch & evals-skills

Source: improving-ai-skills-with-autoresearch-evals-skills-2035257434365976671.md
Captured: 2026-03-21T19:45:41.107797+00:00
From: https://x.com/nurijanian/status/2035257434365976671

## Classification
Type: practitioner-report — first-person report of three concrete implementation attempts, what changed between attempts, and what failed before success improved.
Domains: evals, verification, skill-optimization
Author: Nurijanian is reporting direct hands-on iteration with Auto Research and eval tooling; useful for workflow signals, but not a controlled or generalized benchmark.

## Summary
The source argues that automated skill optimization only works after manual comprehension and specification work are done. Across three iterations, the author found that letting tooling auto-generate inputs and judges produced superficially higher scores but worse real behavior, because the objective was ungrounded in observed failure. Improvement came only after manually reading outputs, building a failure taxonomy (open coding -> axial coding), writing judges from that taxonomy, and calibrating judges on a small hand-scored set before rerunning optimization. The "Three Gulfs" framing (comprehension, specification, generalization) is the core contribution: the optimization loop addresses generalization, but only after human work closes comprehension and specification.

## Connections Found
`/connect` found strong links to [spec-mining-as-codification](../notes/spec-mining-as-codification.md) (**exemplifies**), [specification-strategy-should-follow-where-understanding-lives](../notes/specification-strategy-should-follow-where-understanding-lives.md) (**exemplifies**), and [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) (**exemplifies**). It also connects to [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) (**extends**) and [error-correction-works-above-chance-oracles-with-decorrelated-checks](../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) (**exemplifies**) through the judge-calibration step. The key fit is that this source adds practitioner evidence for a phase-gated view of automation: objective construction remains human-gated before loop automation becomes useful.

## Extractable Value
1. [quick-win] Add a phase gate to evaluation workflows: require explicit completion of comprehension -> specification -> generalization before running optimization loops; this has high reach because it explains why optimization can improve the wrong target.
2. [experiment] Treat judge creation as spec mining: derive criteria from observed failures, then calibrate on a hand-labeled mini set before trusting autonomous runs; high reach because it operationalizes verifier construction rather than tool-specific tuning.
3. [quick-win] Introduce a "manual read quota" (for example, read and annotate N outputs before each judge revision) as a hard precondition; high reach because it directly protects against fantasy objectives across domains.
4. [experiment] Keep tuple-based synthetic input generation, but only after failure-taxonomy grounding; medium reach because coverage improvements transfer broadly, while the exact tuple schema is context-bound.
5. [just-a-reference] Use this source as external evidence for the oracle bottleneck argument in automation notes; low-to-medium reach because it is a single-team observational report.

## Limitations (our opinion)
This is a sample-of-one practitioner narrative, not a controlled study. Multiple variables changed at once between takes (course study, manual reading, taxonomy quality, judge design, calibration), so causal attribution to any single change is weak. Reported score/quality improvements are not paired with rigorous held-out evaluation, so the Gulf of Generalization claim is asserted more than demonstrated. The strongest claim ("no automation can close comprehension") may be directionally right but is not hard-to-vary yet: a simpler account is that spending focused attention on outputs improved the objective, regardless of specific framework terminology. This is consistent with [specification-strategy-should-follow-where-understanding-lives](../notes/specification-strategy-should-follow-where-understanding-lives.md): understanding may emerge through observation, but the source does not test whether alternate workflows could surface that understanding with less manual effort. Context factors (skill type, model choice, judge implementation details, budget) are also underspecified, limiting transfer confidence.

## Recommended Next Action
Write a note titled "Evaluation automation is phase-gated by comprehension" connecting to [spec-mining-as-codification](../notes/spec-mining-as-codification.md) and [the-boundary-of-automation-is-the-boundary-of-verification](../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — it would argue that optimization loops should be blocked until failure-taxonomy and judge-calibration gates are met.
