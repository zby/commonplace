---
description: Three sources of deviation between intended and actual LLM output — prompt underspecification, execution indeterminism, and interpreter failure — plus oracle theory, error correction, and architectural responses for managing each
type: index
status: current
---

# LLM interpretation errors

LLM output deviates from what the user intended for three distinct reasons, each a property of a different part of the system and each requiring different remedies:

- **[Underspecification](./agentic-systems-interpret-underspecified-instructions.md)** — the prompt admits multiple valid interpretations. A property of the specification language. Even a perfect interpreter faces this. Remedy: narrow the spec.
- **[Indeterminism](./execution-indeterminism-is-a-property-of-the-sampling-process.md)** — the same prompt produces different outputs across runs. A property of the sampling process. Theoretically eliminable. Remedy: sampling control.
- **[Interpretation error](./interpretation-errors-are-failures-of-the-interpreter.md)** — the LLM's output distribution is biased away from the valid space (for a theoretical deterministic LLM: simply the wrong output). Remedy: error detection and correction.

[Ma et al.'s prompt stability study](https://arxiv.org/pdf/2509.13680) empirically separates all three: temperature+sampling measures indeterminism within each prompt variant, cross-variant comparison measures underspecification, and systematic degradation under emotional prompts reveals bias. Performance and stability are decoupled (Spearman rho = -0.433), confirming these are independent phenomena.

Conflating the three leads to misdiagnosis — e.g. narrowing the spec (underspecification remedy) when the LLM is ignoring constraints it already has (interpretation error), or lowering temperature (indeterminism remedy) when the spec genuinely admits the unwanted output (underspecification). This area covers the taxonomy, the detection and correction machinery (oracles, voting, verification), and architectural responses (separation, bounded context) for managing all three.
## Error Correction Theory

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the core theory: error correction is viable when oracles have discriminative power (TPR > FPR) and checks are decorrelated; amplification cost scales with 1/(TPR-FPR)²
- [systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md) — controlled framing changes do two different jobs here: decorrelate weak checks for verification and expose brittleness under semantically fixed prompts; distinct from Deutsch's explanatory-reach test

## Oracle Theory

- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — oracle strength as a gradient from hard (deterministic) to no oracle (vibes); the engineering move is to harden oracles progressively
- [reliability-dimensions-map-to-oracle-hardening-stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — Rabanser et al.'s four reliability dimensions each target a different oracle question; each can be hardened independently
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — crossing from augmentation to automation requires per-instance discrimination, which is empirically stagnant; external oracle construction is the practical path
- [the-boundary-of-automation-is-the-boundary-of-verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — synthesis: three independent lines of evidence (oracle theory, labor economics, frontier-lab predictions) converge on verification cost as the structural determinant of automation

## Aggregation & Correction

- [synthesis-is-not-error-correction](./synthesis-is-not-error-correction.md) — merging agent outputs propagates errors; voting discards minorities and corrects them; the aggregation operation must match the decomposition structure

## Architectural Responses

- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — separation works because bookkeeping admits cheap error correction (hard oracles) while semantic work resists it; mixing forces bookkeeping onto the expensive substrate (also [computational-model](./computational-model-index.md))
- [specification-level-separation-recovers-scoping-before-it-recovers-error-correction](./specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md) — OpenProse-like DSLs recover frame isolation before gaining hard-oracle bookkeeping; an intermediate regime (also [computational-model](./computational-model-index.md))

## Related notes in other areas

- [enforcement-without-structured-recovery-is-incomplete](./enforcement-without-structured-recovery-is-incomplete.md) (kb-design, learning-theory) — the enforcement gradient covers detection and blocking but not recovery; oracle strength constrains viable recovery strategies
- [semantic-review-catches-content-errors-that-structural-validation-cannot](./semantic-review-catches-content-errors-that-structural-validation-cannot.md) (kb-maintenance) — four semantic checks that are decorrelated weak oracles for content errors
- [spec-mining-as-codification](./spec-mining-as-codification.md) (learning-theory) — the manufacturing step: extracting deterministic checks from observed behavior to construct oracles
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) (observability, computational-model) — adjacent distinction: some bad outcomes come from hidden semantic recovery after an ambiguous spec, not from interpreter failure inside a clear spec

## Sources

- [Ma et al. (Sep 2025) — Prompt Stability in Code LLMs](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — empirical evidence: separates all three phenomena methodologically; performance-stability decoupling confirms they are independent

## Related Tags

- [learning-theory](./learning-theory-index.md) — oracle and verification theory originated there; this area applies it specifically to LLM interpretation errors
- [computational-model](./computational-model-index.md) — the scheduling architecture that separation notes describe; error correction explains *why* it works

## Other tagged notes <!-- generated -->

