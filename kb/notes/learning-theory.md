---
description: Index of notes about how systems learn, verify, and improve — accumulation as the basic operation (reach as its key property), stabilisation and distillation as transformation mechanisms, discovery as the source of high-reach theories, oracle theory, and memory architecture
type: index
status: current
---

# Learning theory

How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture that KB design draws on but that aren't KB-specific — they apply to any system that adapts through inspectable artifacts.

The collection is organized around [deploy-time learning](./deploy-time-learning-the-missing-middle.md) as the unifying framework. **Accumulation** — adding knowledge to the store — is the most basic learning operation, with [reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) as its key property: facts sit at the low end, theories at the high end. Two orthogonal mechanisms ([stabilisation](./stabilisation.md) and [distillation](./distillation.md)) transform accumulated knowledge. A third operation ([discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)) produces the high-reach theories that are accumulation's most valuable items.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — two distinct properties (semantic underspecification and execution indeterminism); the spec-to-program projection model, semantic boundaries, and the stabilise/soften cycle
- [learning-is-not-only-about-generality](./learning-is-not-only-about-generality.md) — accumulation is the most basic learning operation, with reach as its key property (facts at the low end, theories at the high end); capacity decomposes into generality vs a reliability/speed/cost compound; Simon's definition grounds the decomposition

## Deploy-time Learning

The organizing framework: deployed systems adapt through repo artifacts — durable, inspectable, and verifiable — filling the gap between training and in-context learning.

- [deploy-time-learning-the-missing-middle](./deploy-time-learning-the-missing-middle.md) — three timescales of system adaptation; the verifiability gradient from prompt tweaks to deterministic code; concrete before-and-after examples of stabilisation at different grades
- [deploy-time-learning-is-agile-for-human-ai-systems](./deploy-time-learning-is-agile-for-human-ai-systems.md) — deploy-time learning and agile share the same core innovation (co-evolving prose and code); agile assumes code wins eventually, deploy-time learning treats the hybrid as the end state
- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — reframes agile: "changing requirements" hide late-surfacing interpretation errors in underspecified specs; short iterations bound interpretation-error propagation, not just change-response latency
- [stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — both mechanisms sacrifice generality for compound gains in reliability, speed, and cost; they differ in the operation (constraining vs extracting) and how much compound they yield
- [bitter-lesson-boundary](./bitter-lesson-boundary.md) — determines when stabilisation is permanent (spec IS the problem) vs when softening is needed (spec approximates the problem); composition failure is the tell that specs are theories, not definitions

## Stabilisation

Constraining the interpretation space — from partial narrowing (conventions) to full commitment (deterministic code). The primary mechanism for hardening deployed systems.

- [stabilisation](./stabilisation.md) — definition and spectrum: storing an output, writing a convention, adding structured sections, extracting deterministic code; [crystallisation](./crystallisation.md) is the far end where the medium itself changes from natural language to executable code
- [storing-llm-outputs-is-stabilization](./storing-llm-outputs-is-stabilization.md) — the simplest instance: keeping a specific LLM output resolves underspecification to one interpretation; develops the generator/verifier pattern and verbatim risk
- [stabilisation-during-deployment-is-continuous-learning](./stabilisation-during-deployment-is-continuous-learning.md) — AI labs' continuous learning is achievable through stabilisation with versioned artifacts, which beats weight updates on inspectability and rollback
- [spec-mining-as-crystallisation](./spec-mining-as-crystallisation.md) — crystallisation's operational mechanism: observe behavior, extract deterministic rules, grow the calculator surface monotonically
- [operational-signals-that-a-component-is-a-softening-candidate](./operational-signals-that-a-component-is-a-softening-candidate.md) — five testable signals (paraphrase brittleness, isolation-vs-integration gap, process constraints, unspecifiable failures, distribution sensitivity) for detecting when to reverse crystallisation
- [error-messages-that-teach-are-a-stabilisation-technique](./error-messages-that-teach-are-a-stabilisation-technique.md) — the dual-function property: effective enforcement artifacts simultaneously constrain and inform, because in agent systems the error channel is an instruction channel
- [enforcement-without-structured-recovery-is-incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — the enforcement gradient covers detection and blocking but not recovery; maps ABC's corrective → fallback → escalation onto each enforcement layer, with oracle strength determining viable recovery strategies

## Distillation

Targeted extraction from a larger body of reasoning into a focused artifact shaped by use case, context budget, or agent. Orthogonal to stabilisation — you can distil without stabilising (extract a skill, still underspecified) or stabilise without distilling (store an output, no extraction from reasoning).

- [distillation](./distillation.md) — definition: the rhetorical mode shifts to match the target (argumentative → procedural, exploratory → assertive); the dominant mechanism in knowledge work because it creates new artifacts from existing reasoning

## Information & Bounded Observers

- [information-value-is-observer-relative-because-extraction-requires-computation](./information-value-is-observer-relative-because-extraction-requires-computation.md) — deterministic transformations add zero classical information but can make structure accessible to bounded observers; names the gap that distillation and discovery each describe operationally
- [minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — reframes "minimum viable ontology" as the vocabulary that maximally reduces extraction cost for a bounded observer entering a domain; synthesizes information-value, discovery, and distillation
- [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — Deutsch's adaptive-vs-explanatory distinction: explanatory knowledge transfers because it captures why, not just what works; grounds the KB's first-principles filter as selecting for reach

## Discovery

A third operation, distinct from both stabilisation and distillation: positing a new general concept and simultaneously recognizing existing particulars as instances of it. Discovery produces theories — the highest-reach items accumulation can store.

- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — the dual structure of discovery (posit the general, recognize the particular); three depths from shared feature through shared structure to generative model; the hard problem is recognition, not linking

## Synthesis

- [a good agentic KB maximizes contextual competence through discoverable, composable, trustworthy knowledge](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — accumulation as the basic operation plus three transformation operations (stabilisation, distillation, discovery) mapped to three knowledge properties (trustworthy, discoverable, composable) serving contextual competence under bounded context; reach as the quality dimension of what's accumulated

## Oracle & Verification

Moved to [LLM interpretation errors](./llm-interpretation-errors.md) — oracle theory, error correction, reliability dimensions, and the augmentation/automation boundary now live in the dedicated error-theory area. Key notes:

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the core theory of error correction via decorrelated weak oracles
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — the gradient from hard to no oracle that determines engineering priorities

## Memory & Architecture

- [three-space-agent-memory-maps-to-tulving-taxonomy](./three-space-agent-memory-maps-to-tulving-taxonomy.md) — agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distinction
- [three-space-memory-separation-predicts-measurable-failure-modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) — the three-space claim is testable: flat memory predicts specific cross-contamination failures
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — crystallisation counters the blackbox problem not by requiring human review but by choosing a substrate (repo artifacts) that any agent can inspect, diff, test, and verify
- [A-MEM: Agentic Memory for LLM Agents](../sources/a-mem-agentic-memory-for-llm-agents.md) — academic paper: Zettelkasten-inspired agent memory with automated link generation; flat single-space design provides a test case for whether three-space separation matters at QA-benchmark scale
- [memory-management-policy-is-learnable-but-oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — AgeMem's RL-trained memory policy demonstrates low-reach accumulation (facts) and distillation (STM); confirms memory policy is vision-feature-like per the bitter lesson boundary, but requires a task-completion oracle the KB cannot yet provide
- [Graphiti](../sources/graphiti-temporal-knowledge-graph.ingest.md) — temporally-aware knowledge graph with bi-temporal edge invalidation; strongest temporal model in the surveyed memory systems and strongest counterexample to files-first architecture

## Applications

- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — when agents and tools share a calling convention, stabilisation and crystallisation become local operations; llm-do as primary evidence
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — typing, testing, progressive compilation, and version control transfer from programming to LLM prompting, with probabilistic execution making some practices harder
- [ad-hoc-prompts-extend-the-system-without-schema-changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — the counterpoint: sometimes staying at the prompt level is the right choice; ad hoc instructions absorb new requirements faster than schema changes
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — law as an independent source discipline for the underspecified instructions problem: precedent and codification are stabilisation; legal techniques are native to the underspecified medium
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — ephemeral vs persistent artifacts as inverse of crystallisation; discarding generated artifacts trades accumulation for simplicity

## Reference material

- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.md) — empirical study of AGENTS.md/CLAUDE.md evolution in 466 OSS projects; commit-level analysis shows stabilisation maturation trajectory confirming continuous learning through versioned artifacts
- [On the "Induction Bias" in Sequence Models](../sources/induction-bias-sequence-models-ebrahimi-2026.md) — 190k-run empirical study showing transformers need orders-of-magnitude more data than RNNs for state tracking; architectural induction bias determines data efficiency and weight sharing, grounding the computational bounds dimension of learning capacity

## Related Areas

- [llm-interpretation-errors](./llm-interpretation-errors.md) — oracle theory, error correction, and reliability dimensions migrated here; the error-theory area applies verification concepts specifically to LLM interpretation failures
- [kb-design](./kb-design.md) — applies learning theory to KB architecture and evaluation; [methodology-enforcement-is-stabilisation](./methodology-enforcement-is-stabilisation.md) bridges both areas
- [document-system](./document-system.md) — the type ladder (text→note→structured-claim) instantiates the stabilisation gradient for documents
