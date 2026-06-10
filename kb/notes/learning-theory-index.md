---
description: Index of notes about how systems learn, verify, and improve — accumulation, reach, constraining, distillation, discovery, oracle theory, and memory architecture
type: kb/types/index.md
index_source: tag
index_key: learning-theory
status: current
---

# Learning theory

How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture that KB design draws on but that aren't KB-specific — they apply to any system that adapts through durable artifacts, including but not limited to inspectable ones.

The collection is organized around [deploy-time learning](./deploy-time-learning-is-the-missing-middle.md) as the unifying framework. **Accumulation** — adding knowledge to the store — is the most basic learning operation, with [reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) as its key property: facts sit at the low end, theories at the high end. Two orthogonal mechanisms ([constraining](./definitions/constraining.md) and [distillation](./definitions/distillation.md)) transform accumulated knowledge. A third operation ([discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)) produces the high-reach theories that are accumulation's most valuable items.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — two distinct properties (semantic underspecification and execution indeterminism); the spec-to-program projection model, semantic boundaries, and the constrain/relax cycle
- [learning-is-not-only-about-generality](./learning-is-not-only-about-generality.md) — accumulation is the most basic learning operation, with reach as its key property (facts at the low end, theories at the high end); capacity decomposes into generality vs a reliability/speed/cost compound; Simon's definition grounds the decomposition
- [continual-learning-open-problem-is-behaviour-not-knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — splits continual learning into knowledge accumulation (solved by ordinary engineering) and behaviour change (open); names readable system-definition artifacts as the cheap behaviour-change mechanism alongside expensive weight updates
- [llm-learning-phases-fall-between-human-learning-modes](./llm-learning-phases-fall-between-human-learning-modes.md) — LLM phases (pre-training, in-context, deploy-time) occupy intermediate positions on the evolution-to-reaction spectrum rather than mapping 1:1 to human learning modes; warns against literal human-LLM learning analogies
- [in-context-learning-presupposes-context-engineering](./in-context-learning-presupposes-context-engineering.md) — in-context learning depends on deploy-time learning to select and organize the right knowledge; Amodei's "no continual learning needed" claim relocates the learning to the system layer rather than eliminating it

## Deploy-time Learning

The organizing framework: deployed systems adapt through symbolic artifacts — durable, inspectable, and verifiable — filling the gap between training and in-context learning.

- [deploy-time-learning-the-missing-middle](./deploy-time-learning-is-the-missing-middle.md) — three timescales of system adaptation; co-evolving prose and code as agile-style deploy-time learning (prose and code co-evolve, hybrid as end state); concrete before-and-after examples of constraining at different grades
- [the verifiability gradient](./verifiability-gradient.md) — the ladder deploy-time artifacts sit on, from restructured prompts through schemas and evals to deterministic code; hardening moves artifacts along it in both directions
- [axes-of-artifact-analysis](./axes-of-artifact-analysis.md) — four-field artifact analysis: storage substrate, representational form, lineage, and behavioral authority over the operative part or consumption path
- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](./changing-requirements-conflate-genuine-change-with-disambiguation.md) — reframes agile: "changing requirements" hide late-surfacing interpretation errors in underspecified specs; short iterations bound interpretation-error propagation, not just change-response latency
- [specification strategy should follow where understanding lives](./specification-strategy-should-follow-where-understanding-lives.md) — names the lifecycle choice across spec-first, bidirectional, and behavior-extracted approaches; the right strategy depends on whether understanding is present before work, discovered during execution, or only visible after repeated runs
- [evaluation automation is phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — concretizes the lifecycle for eval loops: comprehension and specification must precede optimization, or automation amplifies the wrong objective
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](./constraining-and-distillation-both-trade-generality-for-reliability.md) — both mechanisms sacrifice generality for compound gains in reliability, speed, and cost; they differ in the operation (constraining vs extracting) and how much compound they yield
- [fixed-artifacts-split-into-exact-specs-and-proxy-theories](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — determines when constraining can be hardened confidently (spec IS the problem) vs when relaxing must remain available (spec approximates the problem); composition failure is the tell that specs are theories, not definitions

## Constraining

Constraining the interpretation space — from partial narrowing (conventions) to full commitment (deterministic code). The primary mechanism for hardening deployed systems.

- [constraining](./definitions/constraining.md) — definition and spectrum: storing an output, writing a convention, adding structured sections, extracting deterministic code; [codification](./definitions/codification.md) is the far end where the medium itself changes from natural language to executable code
- [storing-llm-outputs-is-constraining](./storing-llm-outputs-is-constraining.md) — the simplest instance: keeping a specific LLM output resolves underspecification to one interpretation; develops the generator/verifier pattern and verbatim risk
- [constraining-during-deployment-is-continuous-learning](./constraining-during-deployment-is-continuous-learning.md) — AI labs' continuous learning is achievable through constraining with versioned artifacts, which beats weight updates on inspectability and rollback
- [spec-mining-as-codification](./spec-mining-as-codification.md) — codification's operational mechanism: observe behavior, extract deterministic rules, grow the calculator surface monotonically
- [operational-signals-that-a-component-is-a-relaxing-candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — five testable signals (paraphrase brittleness, isolation-vs-integration gap, process constraints, unspecifiable failures, distribution sensitivity) for detecting when to reverse codification
- [error-messages-that-teach-are-a-constraining-technique](./error-messages-that-teach-are-a-constraining-technique.md) — the dual-function property: effective enforcement artifacts simultaneously constrain and inform, because in agent systems the error channel is an instruction channel
- [enforcement-without-structured-recovery-is-incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — the enforcement gradient covers detection and blocking but not recovery; maps ABC's corrective → fallback → escalation onto each enforcement layer, with oracle strength determining viable recovery strategies
- [codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) — synthesis: four lenses on the codify-vs-LLM decision (spec completeness, oracle strength, interpretation space, pattern stability) with evidence they come apart at the edges

## Codification Lifecycle

Codification decisions split into three separable questions:

- [Specification strategy should follow where understanding lives](./specification-strategy-should-follow-where-understanding-lives.md) — when to commit: before execution, during execution, or after repeated observation.
- [Codify-versus-LLM decision heuristics](./codify-versus-llm-decision-heuristics.md) — what to commit: exact-spec subproblem, verifiable operation, stable pattern, or still-underspecified judgment.
- [Unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — how to commit and reverse: keep neural and symbolic components behind the same callable interface.
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — why reversibility matters: codification is a bet that may need relaxing when scale shows the commitment was wrong.

Leaving one question unanswered creates a predictable failure: phase errors without timing, wrong commitments without target heuristics, and big-bang rewrites without reversible interfaces.

## Distillation

Targeted extraction from a larger body of reasoning into a focused artifact shaped by use case, context budget, or agent. Orthogonal to constraining — you can distil without constraining (extract a skill, still underspecified) or constrain without distilling (store an output, no extraction from reasoning).

- [distillation](./definitions/distillation.md) — definition: the rhetorical mode shifts to match the target (argumentative → procedural, exploratory → assertive); the dominant mechanism in knowledge work because it creates new artifacts from existing reasoning

## Information & Bounded Observers

- [information-value-is-observer-relative](./information-value-is-observer-relative.md) — deterministic transformations add zero classical information but can make structure accessible to bounded observers; names the gap that distillation and discovery each describe operationally
- [epiplexity-eli5](../work/information-measures/epiplexity-eli5.md) — ELI5 explanation of epiplexity through encrypted messages, shuffled textbooks, CSPRNGs, and chess notation; contrasts surprise, shortest description, and observer-relative usable structure
- [minimum-viable-vocabulary-is-the-naming-set-that-most-reduces-extraction-cost-for-a-bounded-observer](./minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — reframes "minimum viable ontology" as the vocabulary that maximally reduces extraction cost for a bounded observer entering a domain; synthesizes information-value, discovery, and distillation
- [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — Deutsch's adaptive-vs-explanatory distinction: explanatory knowledge transfers because it captures why, not just what works; grounds the KB's first-principles filter as selecting for reach

## Discovery

A third operation, distinct from both constraining and distillation: positing a new general concept and simultaneously recognizing existing particulars as instances of it. Discovery produces theories — the highest-reach items accumulation can store.

- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — the dual structure of discovery (posit the general, recognize the particular); three depths from shared feature through shared structure to generative model; the hard problem is recognition, not linking

## Synthesis

- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — accumulation preserves material, but ingress work is what gives remembered material handles, scope, relationships, provenance, trust signals, and lifecycle pressure
- [agent context is constrained by soft degradation not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — the binding constraint is the soft degradation curve (dilution, compositional collapse, and relevance/interference), not the hard token limit; programmatic constructability is the genuine differentiator
- [soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — catalog of twelve traditions with transfer assessment: what's already working, what's plausible, and what blocks transfer (optimization target mismatch, feedback absence, different failure modes)

## Oracle & Verification

Moved to [LLM interpretation errors](./llm-interpretation-errors-README.md) — oracle theory, error correction, reliability dimensions, and the augmentation/automation boundary now live in the dedicated error-theory area. Key notes:

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the core theory of error correction via decorrelated weak oracles
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — the gradient from hard to no oracle that determines engineering priorities

## Memory & Architecture

- [three-space-agent-memory-maps-to-tulving-taxonomy](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) — agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distinction
- [flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable](./flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — the three-space claim is testable: flat memory predicts specific cross-contamination failures
- [inspectable-artifact-not-supervision-defeats-the-blackbox-problem](./inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — codification counters the blackbox problem not by requiring human review but by choosing readable artifacts (code, prompts, schemas) that any agent can inspect, diff, test, and verify
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) — academic paper: Zettelkasten-inspired agent memory with automated link generation; flat single-space design provides a test case for whether three-space separation matters at QA-benchmark scale
- [memory-management-policy-is-learnable-but-oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — AgeMem's RL-trained memory policy demonstrates low-reach accumulation (facts) and distillation (STM); frames memory policy as a proxy theory over exact-spec operations, but requires a task-completion oracle the KB cannot yet provide
- [agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — memory decomposes into storage (solved), retrieval/activation (context engineering), and learning (learning theory); the hard problems live at the intersections, not inside a standalone "memory system"
- [Multi-Agent Memory from a Computer Architecture Perspective](https://arxiv.org/html/2603.10062v1) — computer-architecture analogy for multi-agent memory: shared/distributed paradigms, three-layer hierarchy, and consistency protocols as the critical unsolved problem
- [Graphiti](https://github.com/getzep/graphiti) — temporally-aware knowledge graph with bi-temporal edge invalidation; strongest temporal model in the surveyed memory systems and strongest counterexample to files-first architecture

## Applications

- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — when agents and tools share a calling convention, constraining and codification become local operations; llm-do as primary evidence
- [programming-practices-apply-to-prompting](./underspecification-and-indeterminism-complicate-programming-for.md) — typing, testing, progressive compilation, and version control transfer from programming to LLM prompting, with probabilistic execution making some practices harder
- [ad-hoc-prompts-extend-the-system-without-schema-changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — the counterpoint: sometimes staying at the prompt level is the right choice; ad hoc instructions absorb new requirements faster than schema changes
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — law as an independent source discipline for the underspecified instructions problem: precedent and codification are constraining; legal techniques are native to the underspecified medium
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — ephemeral vs persistent artifacts as inverse of codification; discarding generated artifacts trades accumulation for simplicity
- [Ephemerality is safe where embedded operational knowledge has low reach](./ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) — synthesizes Kirsch's four barriers with the reach concept: the ephemeral/malleable boundary sits where embedded operational knowledge crosses from low reach (adaptive, safe to discard) to high reach (explanatory, must accumulate)

## Reference material

- [Context Engineering for AI Agents in OSS](https://arxiv.org/pdf/2510.21413) — empirical study of AGENTS.md/CLAUDE.md evolution in 466 OSS projects; commit-level analysis shows constraining maturation trajectory confirming continuous learning through versioned artifacts
- [On the "Induction Bias" in Sequence Models](https://arxiv.org/pdf/2602.18333) — 190k-run empirical study showing transformers need orders-of-magnitude more data than RNNs for state tracking; architectural induction bias determines data efficiency and weight sharing, grounding the computational bounds dimension of learning capacity

## Related Tags

- [llm-interpretation-errors](./llm-interpretation-errors-README.md) — oracle theory, error correction, and reliability dimensions migrated here; the error-theory area applies verification concepts specifically to LLM interpretation failures
- [tags](./tags-README.md) — applies learning theory to KB architecture and evaluation; [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) bridges both areas
- [document-system](./document-system-README.md) — the type ladder (text→note→structured-claim) instantiates the constraining gradient for documents
