---
description: Why LLM output deviates from intent — underspecification, interpreter failure, indeterminism — and the machinery for detecting and correcting it, from oracle theory and error correction to architectural separation
type: kb/types/tag-readme.md
index_source: tag
index_key: llm-reliability
---

# LLM reliability

LLM output deviates from what the user intended for three distinct reasons — underspecification of the spec, error by the interpreter, and indeterminism in sampling — each a property of a different part of the system and each needing a different remedy. This area covers that taxonomy, the detection and correction machinery (oracles, voting, verification), and architectural responses (separation, bounded context) for managing all three.

## The Taxonomy

- [LLM output deviation has three sources with non-substitutable remedies](./llm-output-deviation-has-three-sources-with-non-substitutable.md) — the synthesis: why the three are properties of different objects, why prompt narrowing, error correction, and sampling control cannot stand in for each other, and how to tell the three apart empirically
- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — source 1: the spec admits multiple valid interpretations; a property of the specification language that even a perfect interpreter faces
- [out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — source 2, interpreter failure: the output falls outside what the spec allows; a property of the interpreter, with the worked failure catalogue
- [traditional-software-can-bracket-executor-conformance-llm-systems](./traditional-software-can-bracket-executor-conformance-llm-systems.md) — the foundation under the taxonomy: classical stacks can assume executor conformance and unique meaning, LLM systems can assume neither, so error analysis needs three questions where programming needed one
- [execution-indeterminism-is-a-property-of-the-sampling-process](./execution-indeterminism-is-a-property-of-the-sampling-process.md) — source 3: the same prompt gives different outputs across runs; a property of the sampling process, theoretically eliminable
- [llm-debugging-starts-with-retry-versus-rewrite-triage](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) — the operational move: which remedy to reach for first, for the two-source case

## Error Correction Theory

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the core theory: error correction is viable when oracles have discriminative power (TPR > FPR) and checks are decorrelated; amplification cost scales with 1/(TPR-FPR)²
- [systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — controlled framing changes do two different jobs here: decorrelate weak checks for verification and expose brittleness under semantically fixed prompts; distinct from Deutsch's explanatory-reach test

## Oracle Theory

- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — oracle strength as a gradient from hard (deterministic) to no oracle (vibes); the engineering move is to harden oracles progressively
- [reliability-dimensions-map-to-oracle-hardening-stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — Rabanser et al.'s four reliability dimensions each target a different oracle question; each can be hardened independently
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — crossing from augmentation to automation requires per-instance discrimination, which is empirically stagnant; external oracle construction is the practical path
- [knowledge-storage-does-not-imply-contextual-activation](./knowledge-storage-does-not-imply-contextual-activation.md) — relevant knowledge can be present but remain unelicited; activation failure appears when probe retrievability is high but spontaneous emergence is low
- [elicitation-requires-maintained-question-generation-systems](./elicitation-requires-maintained-question-generation-systems.md) — strategies for closing the activation gap, ordered by expertise required; composes probes into maintained review architectures
- [the-boundary-of-automation-is-the-boundary-of-verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — synthesis: three independent lines of evidence (oracle theory, labor economics, frontier-lab predictions) converge on verification cost as the structural determinant of automation
- [evaluation automation is phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — phase model inside evaluation loops: automation only generalizes after manual comprehension and calibrated specification produce discriminative judges

## Aggregation & Correction

- [synthesis-is-not-error-correction](./synthesis-is-not-error-correction.md) — merging agent outputs propagates errors; voting discards minorities and corrects them; the aggregation operation must match the decomposition structure

## Architectural Responses

- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — separation works because bookkeeping admits cheap error correction (hard oracles) while semantic work resists it; mixing forces bookkeeping onto the expensive substrate (also [computational-model](./computational-model-README.md))
- [specification-level-separation-recovers-scoping-before-it-recovers-error-correction](./specification-level-separation-recovers-scoping-before-it-recovers.md) — OpenProse-like DSLs recover frame isolation before gaining hard-oracle bookkeeping; an intermediate regime (also [computational-model](./computational-model-README.md))

## Related notes in other areas

- [enforcement-without-structured-recovery-is-incomplete](./enforcement-without-structured-recovery-is-incomplete.md) (kb-design, learning-theory) — the enforcement gradient covers detection and blocking but not recovery; oracle strength constrains viable recovery strategies
- [semantic-review-catches-content-errors-that-structural-validation-cannot](./semantic-review-catches-content-errors-that-structural-validation.md) (kb-maintenance) — four semantic checks that are decorrelated weak oracles for content errors
- [spec-mining-as-codification](./spec-mining-as-codification.md) (learning-theory) — the manufacturing step: extracting deterministic checks from observed behavior to construct oracles
- [silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) (observability, computational-model) — adjacent distinction: some bad outcomes come from hidden semantic recovery after an ambiguous spec, not from interpreter failure inside a clear spec

## Sources

- [Ma et al. (Sep 2025) — Prompt Stability in Code LLMs](https://arxiv.org/pdf/2509.13680) — empirical evidence: separates all three phenomena methodologically; performance-stability decoupling confirms they are independent

## Related Tags

- [learning-theory](./learning-theory-README.md) — oracle and verification theory originated there; this area applies it specifically to LLM output deviations
- [computational-model](./computational-model-README.md) — the scheduling architecture that separation notes describe; error correction explains *why* it works
