---
description: Optimization loops need diagnostic error analysis and demonstrated judge discrimination before automation can improve behavior rather than just score
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, llm-reliability, evaluation, deploy-time-learning]
---

# Evaluation automation is phase-gated by comprehension

When an evaluation loop improves score without improving real behavior, the failure may be not weak search but an objective grounded too weakly in observed failure. This note proposes a repair sequence: **comprehension first, specification second, generalization third**.

Comprehension is the first gate because it supplies the observations that specification turns into verifiers. Before automation can improve output quality, the system needs direct evidence of real failures, a way to identify concrete failure modes, and a route for turning those failures into discriminative judges.

## The three phases

1. **Comprehension**: Read outputs directly, observe where and why the system fails, build non-theoretical intuition for failure patterns.
2. **Specification**: Convert observations into a failure taxonomy and evaluators, then calibrate those evaluators against manually labeled examples.
3. **Generalization**: Run automated optimization against calibrated evaluators with broader input coverage.

This sequencing matches one [practitioner field report](../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md): auto-generated tests and judges produced early score gains, but direct inspection found that the skills were not improved because the generated criteria lacked a model of observed failure. The loop functioned against its supplied objective; the objective did not track the practitioner's intended quality.

## Why this is a gate, not a style preference

Skipping comprehension leaves specification unconstrained by observed reality. Skipping specification leaves optimization unconstrained by discriminative checks. Both cases amplify proxy quality rather than task quality.

This is why "more automation" cannot reliably substitute for the early verifier-construction work in cold-start or subjective domains. Automation can help once failure patterns and judges exist, but it cannot safely assume them from zero context.

Meta-Harness shows an important boundary condition. Its proposer can inspect prior harness code, scores, and raw execution traces before writing the next candidate. In the reported information-access ablation, the scores-plus-summary condition reached 34.9 median accuracy while the full trace-access condition reached 50.0. The demonstrated result is that trace access improved this harness-search condition; the paper does not show that the proposer formed a causal failure model. This note interprets the gap as evidence that diagnostic access can automate part of comprehension. The proposed phase gate is therefore not "a human must always understand first," but "optimization needs enough diagnostic access to test a failure model before generalizing." Scalar scores alone do not provide that access.

## Scope limits

- In hard-oracle domains (compilers, strict schemas, deterministic tests), comprehension can be shorter or partly automated when the proposer has rich diagnostic traces, not just scalar scores.
- In soft-oracle domains (writing quality, strategic reasoning, product judgment), comprehension is load-bearing and usually human-led.
- This claim applies to early and mid-stage system tuning. Mature systems may partially automate parts of comprehension, but only after prior manual cycles have stabilized the taxonomy.

## Practical implication

Evaluation pipelines should enforce explicit verifier-construction stage gates before optimization:

1. Output-read pass completed on diverse inputs
2. Failure taxonomy written from observed failures
3. Judges tested on a hand-scored mini set and shown to discriminate above chance

Without these gates, score improvements are weak evidence of capability improvement.

---

Relevant Notes:

- [spec-mining-as-codification](./spec-mining-as-codification.md) — grounds: converting observed failures into reusable evaluators is spec mining
- [specification-strategy-should-follow-where-understanding-lives](./specification-strategy-should-follow-where-understanding-lives.md) — extends: this is the evaluation-specific case where understanding emerges through observation, not upfront
- [the-boundary-of-automation-is-the-boundary-of-verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — narrows: identifies an intra-loop boundary where optimization depends on prior verifier construction
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — frames (provisional — target is speculative): the three phases can be read as a local oracle-hardening sequence before heavy automation
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: the stage gate requires measured discriminative signal before amplification
- [Ingest: Improving AI Skills with autoresearch & evals-skills](../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md) — evidenced-by: one practitioner report of auto-generated criteria improving scores without improving the skill, followed by output reading, taxonomy design, judge validation, and another optimization run
- [Ingest: Meta-Harness](../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — qualifies: rich raw traces let an automated proposer perform part of the comprehension phase in hard-oracle harness search
