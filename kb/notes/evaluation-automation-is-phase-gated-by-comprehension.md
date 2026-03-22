---
description: Optimization loops require manual error analysis and judge calibration before automation can improve behavior rather than just score
type: note
traits: [has-external-sources]
tags: [learning-theory, llm-interpretation-errors, evaluation]
status: seedling
---

# Evaluation automation is phase-gated by comprehension

When an evaluation loop improves score without improving real behavior, the failure is often not weak search but an objective grounded too weakly in observed failure. Evaluation automation in practice follows a characteristic sequence: **comprehension first, specification second, generalization third**.

Comprehension is the first gate because it supplies the observations that specification turns into verifiers. Before automation can improve output quality, someone must inspect real outputs, identify concrete failure modes, and translate those failures into discriminative judges.

## The three phases

1. **Comprehension**: Read outputs directly, observe where and why the system fails, build non-theoretical intuition for failure patterns.
2. **Specification**: Convert observations into a failure taxonomy and evaluators, then calibrate those evaluators against manually labeled examples.
3. **Generalization**: Run automated optimization against calibrated evaluators with broader input coverage.

This sequencing matches a practitioner pattern described in one detailed field report: auto-generated tests and judges produced early score gains, then degraded real quality exposed that the objective was wrong. The loop functioned correctly; the objective did not.

## Why this is a gate, not a style preference

Skipping comprehension leaves specification unconstrained by observed reality. Skipping specification leaves optimization unconstrained by discriminative checks. Both cases amplify proxy quality rather than task quality.

This is why "more automation" cannot reliably substitute for the early verifier-construction work in cold-start or subjective domains. Automation can help once failure patterns and judges exist, but it cannot safely assume them from zero context.

## Scope limits

- In hard-oracle domains (compilers, strict schemas, deterministic tests), comprehension can be shorter because failure is already legible.
- In soft-oracle domains (writing quality, strategic reasoning, product judgment), comprehension is load-bearing and usually human-led.
- This claim applies to early and mid-stage system tuning. Mature systems may partially automate parts of comprehension, but only after prior manual cycles have stabilized the taxonomy.

## Practical implication

Evaluation pipelines should enforce explicit verifier-construction stage gates before optimization:

1. Output-read pass completed on diverse inputs
2. Failure taxonomy written from observed failures
3. Judges calibrated on a hand-scored mini set

Without these gates, score improvements are weak evidence of capability improvement.

---

Relevant Notes:

- [spec-mining-as-codification](./spec-mining-as-codification.md) — grounds: converting observed failures into reusable evaluators is spec mining
- [specification-strategy-should-follow-where-understanding-lives](./specification-strategy-should-follow-where-understanding-lives.md) — extends: this is the evaluation-specific case where understanding emerges through observation, not upfront
- [the-boundary-of-automation-is-the-boundary-of-verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — narrows: identifies an intra-loop boundary where optimization depends on prior verifier construction
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — frames (provisional — target is speculative): the three phases can be read as a local oracle-hardening sequence before heavy automation
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: calibration ensures judges have discriminative signal before amplification
- [Ingest: Improving AI Skills with autoresearch & evals-skills](../sources/improving-ai-skills-with-autoresearch-evals-skills-2035257434365976671.ingest.md) — evidence: practitioner report where one team saw automation improve only after manual comprehension, taxonomy design, and judge calibration
