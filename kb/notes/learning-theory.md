---
description: Index of notes about how systems learn, verify, and improve — deploy-time learning framework, stabilisation and distillation as orthogonal mechanisms, discovery as synthesis, oracle theory, and memory architecture
type: index
status: current
---

# Learning theory

How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture that KB design draws on but that aren't KB-specific — they apply to any system that adapts through inspectable artifacts.

The collection is organized around [deploy-time learning](./deploy-time-learning-the-missing-middle.md) as the unifying framework, with two orthogonal mechanisms ([stabilisation](./stabilisation.md) and [distillation](./distillation.md)) and a third distinct operation ([discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)).

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — two distinct properties (semantic underspecification and execution indeterminism); the spec-to-program projection model, semantic boundaries, and the stabilise/soften cycle
- [learning-is-not-only-about-generality](./learning-is-not-only-about-generality.md) — capacity decomposes into generality (how broadly it applies) vs a reliability/speed/cost compound (how well it works where it applies); Simon's definition grounds the decomposition

## Deploy-time Learning

The organizing framework: deployed systems adapt through repo artifacts — durable, inspectable, and verifiable — filling the gap between training and in-context learning.

- [deploy-time-learning-the-missing-middle](./deploy-time-learning-the-missing-middle.md) — three timescales of system adaptation; the verifiability gradient from prompt tweaks to deterministic code; concrete before-and-after examples of stabilisation at different grades
- [deploy-time-learning-is-agile-for-human-ai-systems](./deploy-time-learning-is-agile-for-human-ai-systems.md) — deploy-time learning and agile share the same core innovation (co-evolving prose and code); agile assumes code wins eventually, deploy-time learning treats the hybrid as the end state
- [stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — both mechanisms sacrifice generality for compound gains in reliability, speed, and cost; they differ in the operation (constraining vs extracting) and how much compound they yield
- [bitter-lesson-boundary](./bitter-lesson-boundary.md) — determines when stabilisation is permanent (spec IS the problem) vs when softening is needed (spec approximates the problem); composition failure is the tell that specs are theories, not definitions

## Stabilisation

Constraining the interpretation space — from partial narrowing (conventions) to full commitment (deterministic code). The primary mechanism for hardening deployed systems.

- [stabilisation](./stabilisation.md) — definition and spectrum: storing an output, writing a convention, adding structured sections, extracting deterministic code; [crystallisation](./crystallisation.md) is the far end where the medium itself changes from natural language to executable code
- [storing-llm-outputs-is-stabilization](./storing-llm-outputs-is-stabilization.md) — the simplest instance: keeping a specific LLM output resolves underspecification to one interpretation; develops the generator/verifier pattern and verbatim risk
- [stabilisation-during-deployment-is-continuous-learning](./stabilisation-during-deployment-is-continuous-learning.md) — AI labs' continuous learning is achievable through stabilisation with versioned artifacts, which beats weight updates on inspectability and rollback
- [spec-mining-as-crystallisation](./spec-mining-as-crystallisation.md) — crystallisation's operational mechanism: observe behavior, extract deterministic rules, grow the calculator surface monotonically
- [error-messages-that-teach-are-a-stabilisation-technique](./error-messages-that-teach-are-a-stabilisation-technique.md) — the dual-function property: effective enforcement artifacts simultaneously constrain and inform, because in agent systems the error channel is an instruction channel

## Distillation

Targeted extraction from a larger body of reasoning into a focused artifact shaped by use case, context budget, or agent. Orthogonal to stabilisation — you can distil without stabilising (extract a skill, still underspecified) or stabilise without distilling (store an output, no extraction from reasoning).

- [distillation](./distillation.md) — definition: the rhetorical mode shifts to match the target (argumentative → procedural, exploratory → assertive); the dominant mechanism in knowledge work because it creates new artifacts from existing reasoning

## Information & Bounded Observers

- [information-value-is-observer-relative-because-extraction-requires-computation](./information-value-is-observer-relative-because-extraction-requires-computation.md) — deterministic transformations add zero classical information but can make structure accessible to bounded observers; names the gap that distillation and discovery each describe operationally

## Discovery

A third operation, distinct from both stabilisation and distillation: positing a new general concept and simultaneously recognizing existing particulars as instances of it.

- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — the dual structure of discovery (posit the general, recognize the particular); three depths from shared feature through shared structure to generative model; the hard problem is recognition, not linking

## Oracle & Verification

- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — oracle strength (how cheaply and reliably you can verify correctness) determines where a component sits on the automation gradient
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — error correction is viable when the oracle has discriminative power (TPR > FPR) and checks are decorrelated; amplification cost scales with 1/(TPR-FPR)²
- [reliability-dimensions-map-to-oracle-hardening-stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — Rabanser et al.'s four reliability dimensions each harden a different oracle question, mapping empirical agent evaluation onto the oracle-strength spectrum

## Memory & Architecture

- [three-space-agent-memory-maps-to-tulving-taxonomy](./three-space-agent-memory-maps-to-tulving-taxonomy.md) — agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distinction
- [three-space-memory-separation-predicts-measurable-failure-modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) — the three-space claim is testable: flat memory predicts specific cross-contamination failures
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — crystallisation counters the blackbox problem not by requiring human review but by choosing a substrate (repo artifacts) that any agent can inspect, diff, test, and verify
- [A-MEM: Agentic Memory for LLM Agents](../sources/a-mem-agentic-memory-for-llm-agents.md) — academic paper: Zettelkasten-inspired agent memory with automated link generation; flat single-space design provides a test case for whether three-space separation matters at QA-benchmark scale

## Applications

- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — when agents and tools share a calling convention, stabilisation and crystallisation become local operations; llm-do as primary evidence
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — typing, testing, progressive compilation, and version control transfer from programming to LLM prompting, with probabilistic execution making some practices harder
- [ad-hoc-prompts-extend-the-system-without-schema-changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — the counterpoint: sometimes staying at the prompt level is the right choice; ad hoc instructions absorb new requirements faster than schema changes
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — law as an independent source discipline for the underspecified instructions problem: precedent and codification are stabilisation; legal techniques are native to the underspecified medium

## Reference material

- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.md) — empirical study of AGENTS.md/CLAUDE.md evolution in 466 OSS projects; commit-level analysis shows stabilisation maturation trajectory confirming continuous learning through versioned artifacts

## Related Areas

- [kb-design](./kb-design.md) — applies learning theory to KB architecture and evaluation; [methodology-enforcement-is-stabilisation](./methodology-enforcement-is-stabilisation.md) bridges both areas
- [document-system](./document-system.md) — the type ladder (text→note→structured-claim) instantiates the stabilisation gradient for documents
