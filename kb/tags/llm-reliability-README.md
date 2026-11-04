---
description: "Diagnosing and correcting LLM output deviations through specification, conformance and execution checks, with the governing reference made explicit."
type: types/tag-readme.md
---

# LLM reliability

How LLM outputs depart from intended requirements, and how to prevent, detect or correct those departures. Assign this tag to substantive accounts of specification gaps, interpreter conformance, execution variation or their remedies, including oracles and architectural separation. [Evaluation](./evaluation-README.md) covers what a check establishes; this tag requires a connection to deviation or correction. Diagnosis must name the governing reference.

## The Taxonomy

- [LLM output deviation requires three-way diagnosis](../theory/llm-output-deviation-requires-three-way-diagnosis.md) — the synthesis: the three diagnostic questions, why prompt narrowing, error correction, and sampling control target different relations and so cannot completely substitute for one another, and how to tell the three apart empirically
- [Prompting changes failure diagnosis with the semantic reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — distinguishes package conformance, the adjudicated English requirement and behavioral prediction
- [Clear instructions can compose into an unsettled contract](../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) — the JSON/exception case exposes uncertainty in which obligations apply before diagnosing interpreter failure
- [out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec](../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — source 2, interpreter failure: the output falls outside what the spec allows; a property of the interpreter, with the worked failure catalogue
- [traditional-software-can-bracket-executor-conformance-llm-systems](../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) — scopes the executor-conformance comparison to ordinary English instruction execution
- [execution-indeterminism-is-a-property-of-the-sampling-process](../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) — source 3: the same prompt gives different outputs across runs; a property of the sampling process, theoretically eliminable
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — three checks for choosing a debugging move; failure frequency alone cannot identify the defect

## Error Correction Theory

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the core theory: error correction is viable when oracles have discriminative power (TPR > FPR) and checks are decorrelated; amplification cost scales with 1/(TPR-FPR)²
- [systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing](../theory/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — controlled framing changes do two different jobs here: decorrelate weak checks for verification and expose brittleness under semantically fixed prompts; distinct from Deutsch's explanatory-reach test

## Oracle Theory

- [oracle-strength-spectrum](../theory/oracle-strength-spectrum.md) — oracle strength as a gradient from hard (deterministic) to no oracle (vibes); the engineering move is to harden oracles progressively
- [reliability-dimensions-map-to-oracle-hardening-stages](../theory/reliability-dimensions-map-to-oracle-hardening-stages.md) — Rabanser et al.'s four reliability dimensions each target a different oracle question; each can be hardened independently
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — crossing from augmentation to automation requires per-instance discrimination, which is empirically stagnant; external oracle construction is the practical path
- [knowledge-storage-does-not-imply-contextual-activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md) — relevant knowledge can be present but remain unelicited; activation failure appears when probe retrievability is high but spontaneous emergence is low
- [elicitation-requires-maintained-question-generation-systems](../theory/elicitation-requires-maintained-question-generation-systems.md) — strategies for closing the activation gap, ordered by expertise required; composes probes into maintained review architectures
- [the-boundary-of-automation-is-the-boundary-of-verification](../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) — synthesis: three independent lines of evidence (oracle theory, labor economics, frontier-lab predictions) converge on verification cost as the structural determinant of automation
- [evaluation automation is phase-gated by comprehension](../theory/evaluation-automation-is-phase-gated-by-comprehension.md) — phase model inside evaluation loops: automation only generalizes after manual comprehension and calibrated specification produce discriminative judges

## Aggregation & Correction

- [synthesis-is-not-error-correction](../theory/synthesis-is-not-error-correction.md) — merging agent outputs propagates errors; voting discards minorities and corrects them; the aggregation operation must match the decomposition structure

## Architectural Responses

- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — separation works because bookkeeping admits cheap error correction (hard oracles) while semantic work resists it; mixing forces bookkeeping onto the expensive substrate (also [computational-model](./computational-model-README.md))
- [specification-level-separation-recovers-scoping-before-it-recovers-error-correction](../theory/specification-level-separation-recovers-scoping-before-it-recovers.md) — OpenProse-like DSLs recover frame isolation before gaining hard-oracle bookkeeping; an intermediate regime (also [computational-model](./computational-model-README.md))

## Related notes in other areas

- [enforcement-without-structured-recovery-is-incomplete](../theory/enforcement-without-structured-recovery-is-incomplete.md) (learning-theory, constraining) — the enforcement gradient covers detection and blocking but not recovery; oracle strength constrains viable recovery strategies
- [semantic-review-catches-content-errors-that-structural-validation-cannot](../theory/semantic-review-catches-content-errors-that-structural-validation.md) (kb-maintenance) — four semantic checks that are decorrelated weak oracles for content errors
- [spec-mining-as-codification](../theory/spec-mining-as-codification.md) (learning-theory) — the manufacturing step: extracting deterministic checks from observed behavior to construct oracles
- [silent disambiguation is the semantic analogue of tool fallback](../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) (observability, computational-model) — adjacent distinction: some bad outcomes come from hidden semantic recovery after an ambiguous spec, not from interpreter failure inside a clear spec

## Sources

- [Ma et al. (Sep 2025) — Prompt Stability in Code LLMs](https://arxiv.org/pdf/2509.13680) — empirical evidence: separates all three phenomena methodologically; performance-stability decoupling confirms they are independent

## Related Tags

- [learning-theory](./learning-theory-README.md) — the parent: oracle and verification theory applied here to LLM output deviations
- [computational-model](./computational-model-README.md) — the scheduling architecture that separation notes describe; error correction explains *why* it works
