---
description: Index of notes about how systems learn, verify, and improve — Simon's capacity framework, stabilisation/crystallisation/distillation mechanisms, oracle theory, and memory architecture
type: index
status: current
---

# Learning theory

How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture that claw design draws on but that aren't claw-specific — they apply to any system that adapts through inspectable artifacts.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — two distinct properties (semantic underspecification and execution indeterminism); the spec-to-program projection model, semantic boundaries, and the stabilise/soften cycle

## Definitions

- [learning-is-capacity-change](./learning-is-capacity-change.md) — Simon's framework: learning is any change in a system's capacity to adapt; capacity decomposes into generality vs a reliability/speed/cost compound, and three mechanisms operate on that trade-off differently
- [agentic-systems-learn-through-three-distinct-mechanisms](./agentic-systems-learn-through-three-distinct-mechanisms.md) — the three mechanisms named: stabilisation narrows the interpretation space, crystallisation transitions medium, distillation extracts procedures — all are capacity change per Simon but differ in what changes

## Mechanisms

- [stabilisation](./stabilisation.md) — definition: narrowing the space of valid interpretations, trading generality for reliability/speed/cost
- [crystallisation](./crystallisation.md) — definition: phase transition from natural language to executable code, changing medium, consumer, and verification regime
- [distillation](./distillation.md) — definition: extracting operational procedures from discursive reasoning, staying in the same medium but changing rhetorical mode
- [deploy-time-learning-the-missing-middle](./deploy-time-learning-the-missing-middle.md) — repo artifacts fill the gap between training and in-context learning; the three mechanisms provide a verifiability gradient from prompt tweaks to deterministic code
- [continuous-learning-is-stabilisation-during-deployment](./continuous-learning-is-stabilisation-during-deployment.md) — AI labs' continuous learning is achievable through stabilisation with versioned artifacts, which beats weight updates on inspectability and rollback
- [storing-llm-outputs-is-stabilization](./storing-llm-outputs-is-stabilization.md) — choosing to keep an LLM output collapses a distribution to a point — stabilisation applied to artifacts

## Oracle & Verification

- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — oracle strength (how cheaply and reliably you can verify correctness) determines where a component sits on the automation gradient
- [bitter-lesson-boundary](./bitter-lesson-boundary.md) — the boundary where exact solutions survive scaling vs where they don't — calculators vs vision features
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — error correction is viable when the oracle has discriminative power (TPR > FPR) and checks are decorrelated; amplification cost scales with 1/(TPR-FPR)²
- [reliability-dimensions-map-to-oracle-hardening-stages](./reliability-dimensions-map-to-oracle-hardening-stages.md) — Rabanser et al.'s four reliability dimensions each harden a different oracle question, mapping empirical agent evaluation onto the oracle-strength spectrum

## Memory & Architecture

- [three-space-agent-memory-maps-to-tulving-taxonomy](./three-space-agent-memory-maps-to-tulving-taxonomy.md) — agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distinction
- [three-space-memory-separation-predicts-measurable-failure-modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) — the three-space claim is testable: flat memory predicts specific cross-contamination failures
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — crystallisation counters the blackbox problem not by requiring human review but by choosing a substrate (repo artifacts) that any agent can inspect, diff, test, and verify
- [A-MEM: Agentic Memory for LLM Agents](../sources/a-mem-agentic-memory-for-llm-agents.md) — academic paper: Zettelkasten-inspired agent memory with automated link generation and memory evolution; flat single-space memory provides a test case for whether three-space separation matters at QA-benchmark scale

## Applications

- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — when agents and tools share a calling convention, stabilisation and crystallisation become local operations; llm-do as primary evidence
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — typing, testing, progressive compilation, and version control transfer from programming to LLM prompting, with probabilistic execution making some practices harder
- [ad-hoc-prompts-extend-the-system-without-schema-changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — the counterpoint: sometimes staying at the prompt level is the right choice; ad hoc instructions absorb new requirements faster than schema changes
- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — discovery varies by abstraction depth: the hard problem is positing a new general concept and simultaneously recognizing existing particulars as instances of it
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — law as an independent source discipline for the underspecified instructions problem: precedent and codification are stabilisation; crystallisation is rare in law; legal techniques are native to the underspecified medium

## Reference material

- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.md) — empirical study of AGENTS.md/CLAUDE.md evolution in 466 OSS projects; commit-level analysis shows stabilisation maturation trajectory (add instructions → modify instructions → remove instructions) confirming continuous learning through versioned artifacts

## Related Areas

- [claw-design](./claw-design.md) — applies learning theory to claw architecture and evaluation; [methodology-enforcement-is-stabilisation](./methodology-enforcement-is-stabilisation.md) bridges both areas
- [document-system](./document-system.md) — the type ladder (text→note→structured-claim) instantiates the stabilisation→crystallisation gradient for documents
