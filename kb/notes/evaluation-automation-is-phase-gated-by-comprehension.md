---
description: Optimization loops require manual error analysis and judge calibration before automation can improve behavior rather than just score
type: note
traits: [has-external-sources]
tags: [learning-theory, llm-interpretation-errors, evaluation]
status: seedling
---

# Evaluation automation is phase-gated by comprehension

Optimization loops fail not because search is weak, but because they optimize whatever objective is available—including ungrounded objectives. Evaluation automation therefore follows a necessary sequence: **comprehension first, specification second, generalization third**.

The gate is verifier construction. Before automation can improve output quality, someone must inspect real outputs, identify concrete failure modes, and translate those failures into discriminative judges. Without that work, optimization improves score without improving behavior.

## The three phases

1. **Comprehension**: Read outputs directly, observe where and why the system fails, build non-theoretical intuition for failure patterns.
2. **Specification**: Convert observations into a failure taxonomy and evaluators, then calibrate those evaluators against manually labeled examples.
3. **Generalization**: Run automated optimization against calibrated evaluators with broader input coverage.

This sequencing explains a repeated field pattern: teams see early score gains from auto-generated tests and judges, then discover degraded real quality. The loop functions correctly; the objective is wrong.

## Why this is a gate, not a style preference

Skipping comprehension leaves specification unconstrained by observed reality. Skipping specification leaves optimization unconstrained by discriminative checks. Both cases amplify proxy quality rather than task quality.

This is why "more automation" cannot substitute for the first phase in cold-start or subjective domains. The automation loop depends on a verifier it cannot reliably bootstrap from zero context.

## Scope limits

- In hard-oracle domains (compilers, strict schemas, deterministic tests), comprehension can be shorter because failure is already legible.
- In soft-oracle domains (writing quality, strategic reasoning, product judgment), comprehension is load-bearing and usually human-led.
- This claim applies to early and mid-stage system tuning. Mature systems may partially automate parts of comprehension, but only after prior manual cycles have stabilized the taxonomy.

## Practical implication

Evaluation pipelines should enforce explicit stage gates before optimization:

1. Output-read pass completed on diverse inputs
2. Failure taxonomy written from observed failures
3. Judges calibrated on a hand-scored mini set

Without these gates, score improvements are weak evidence of capability improvement.

---

Relevant Notes:

- [spec-mining-as-codification](./spec-mining-as-codification.md) — grounds: converting observed failures into reusable evaluators is spec mining
- [specification-strategy-should-follow-where-understanding-lives](./specification-strategy-should-follow-where-understanding-lives.md) — extends: this is the evaluation-specific case where understanding emerges through observation, not upfront
- [the-boundary-of-automation-is-the-boundary-of-verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — narrows: identifies an intra-loop boundary where optimization depends on prior verifier construction
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — explains: the three phases progressively harden oracle strength before heavy automation
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: calibration ensures judges have discriminative signal before amplification
- [Ingest: Improving AI Skills with autoresearch & evals-skills](../sources/improving-ai-skills-with-autoresearch-evals-skills-2035257434365976671.ingest.md) — evidence: practitioner report where automation improved only after manual comprehension and judge calibration
