---
description: Index of notes about how systems learn, verify, and improve — accumulation, reach, constraining, distillation, discovery, oracle theory, and memory architecture
type: index
status: current
---

# Learning theory

How systems learn, verify, and improve. These notes define learning mechanisms, verification gradients, and memory architecture that KB design draws on but that aren't KB-specific — they apply to any system that adapts through durable substrates, including but not limited to inspectable artifacts.

The collection is organized around [deploy-time learning](./deploy-time-learning-the-missing-middle.md) as the unifying framework. **Accumulation** — adding knowledge to the store — is the most basic learning operation, with [reach](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) as its key property: facts sit at the low end, theories at the high end. Two orthogonal mechanisms ([constraining](./constraining.md) and [distillation](./distillation.md)) transform accumulated knowledge. A third operation ([discovery](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)) produces the high-reach theories that are accumulation's most valuable items.

## Foundations

- [agentic-systems-interpret-underspecified-instructions](./agentic-systems-interpret-underspecified-instructions.md) — two distinct properties (semantic underspecification and execution indeterminism); the spec-to-program projection model, semantic boundaries, and the constrain/relax cycle
- [learning-is-not-only-about-generality](./learning-is-not-only-about-generality.md) — accumulation is the most basic learning operation, with reach as its key property (facts at the low end, theories at the high end); capacity decomposes into generality vs a reliability/speed/cost compound; Simon's definition grounds the decomposition
- [continuous-learning-requires-durability-not-weight-updates](./continuous-learning-requires-durability-not-weight-updates.md) — the live disagreement is whether durable non-weight adaptation counts as learning at all; this note makes the affirmative case and turns artifact-side adaptation from metaphor into learning proper
- [llm-learning-phases-fall-between-human-learning-modes](./llm-learning-phases-fall-between-human-learning-modes.md) — LLM phases (pre-training, in-context, deploy-time) occupy intermediate positions on the evolution-to-reaction spectrum rather than mapping 1:1 to human learning modes; warns against literal human-LLM learning analogies
- [in-context-learning-presupposes-context-engineering](./in-context-learning-presupposes-context-engineering.md) — in-context learning depends on deploy-time learning to select and organize the right knowledge; Amodei's "no continual learning needed" claim relocates the learning to the system layer rather than eliminating it

## Deploy-time Learning

The organizing framework: deployed systems adapt through symbolic artifacts — durable, inspectable, and verifiable — filling the gap between training and in-context learning.

- [deploy-time-learning-the-missing-middle](./deploy-time-learning-the-missing-middle.md) — three timescales of system adaptation; the verifiability gradient from prompt tweaks to deterministic code; concrete before-and-after examples of constraining at different grades
- [learning-substrates-backends-and-artifact-forms](./learning-substrates-backends-and-artifact-forms.md) — separates substrate class from backend and artifact form; explains why repo files, DB rows, and memory-service objects can all host the same broad learning substrate
- [deploy-time-learning-is-agile-for-human-ai-systems](./deploy-time-learning-is-agile-for-human-ai-systems.md) — deploy-time learning and agile share the same core innovation (co-evolving prose and code); agile assumes code wins eventually, deploy-time learning treats the hybrid as the end state
- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — reframes agile: "changing requirements" hide late-surfacing interpretation errors in underspecified specs; short iterations bound interpretation-error propagation, not just change-response latency
- [specification strategy should follow where understanding lives](./specification-strategy-should-follow-where-understanding-lives.md) — names the lifecycle choice across spec-first, bidirectional, and behavior-extracted approaches; the right strategy depends on whether understanding is present before work, discovered during execution, or only visible after repeated runs
- [evaluation automation is phase-gated by comprehension](./evaluation-automation-is-phase-gated-by-comprehension.md) — concretizes the lifecycle for eval loops: comprehension and specification must precede optimization, or automation amplifies the wrong objective
- [constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost](./constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — both mechanisms sacrifice generality for compound gains in reliability, speed, and cost; they differ in the operation (constraining vs extracting) and how much compound they yield
- [bitter-lesson-boundary](./bitter-lesson-boundary.md) — determines when constraining is permanent (spec IS the problem) vs when relaxing is needed (spec approximates the problem); composition failure is the tell that specs are theories, not definitions

## Constraining

Constraining the interpretation space — from partial narrowing (conventions) to full commitment (deterministic code). The primary mechanism for hardening deployed systems.

- [constraining](./constraining.md) — definition and spectrum: storing an output, writing a convention, adding structured sections, extracting deterministic code; [codification](./codification.md) is the far end where the medium itself changes from natural language to executable code
- [storing-llm-outputs-is-constraining](./storing-llm-outputs-is-constraining.md) — the simplest instance: keeping a specific LLM output resolves underspecification to one interpretation; develops the generator/verifier pattern and verbatim risk
- [constraining-during-deployment-is-continuous-learning](./constraining-during-deployment-is-continuous-learning.md) — AI labs' continuous learning is achievable through constraining with versioned artifacts, which beats weight updates on inspectability and rollback
- [spec-mining-as-codification](./spec-mining-as-codification.md) — codification's operational mechanism: observe behavior, extract deterministic rules, grow the calculator surface monotonically
- [operational-signals-that-a-component-is-a-relaxing-candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — five testable signals (paraphrase brittleness, isolation-vs-integration gap, process constraints, unspecifiable failures, distribution sensitivity) for detecting when to reverse codification
- [error-messages-that-teach-are-a-constraining-technique](./error-messages-that-teach-are-a-constraining-technique.md) — the dual-function property: effective enforcement artifacts simultaneously constrain and inform, because in agent systems the error channel is an instruction channel
- [enforcement-without-structured-recovery-is-incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — the enforcement gradient covers detection and blocking but not recovery; maps ABC's corrective → fallback → escalation onto each enforcement layer, with oracle strength determining viable recovery strategies

## Distillation

Targeted extraction from a larger body of reasoning into a focused artifact shaped by use case, context budget, or agent. Orthogonal to constraining — you can distil without constraining (extract a skill, still underspecified) or constrain without distilling (store an output, no extraction from reasoning).

- [distillation](./distillation.md) — definition: the rhetorical mode shifts to match the target (argumentative → procedural, exploratory → assertive); the dominant mechanism in knowledge work because it creates new artifacts from existing reasoning

## Information & Bounded Observers

- [information-value-is-observer-relative](./information-value-is-observer-relative.md) — deterministic transformations add zero classical information but can make structure accessible to bounded observers; names the gap that distillation and discovery each describe operationally
- [epiplexity-eli5](../work/information-measures/epiplexity-eli5.md) — ELI5 explanation of epiplexity through encrypted messages, shuffled textbooks, CSPRNGs, and chess notation; contrasts surprise, shortest description, and observer-relative usable structure
- [minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer](./minimum-viable-vocabulary-is-the-set-of-names-that-maximally-reduces-extraction-cost-for-a-bounded-observer.md) — reframes "minimum viable ontology" as the vocabulary that maximally reduces extraction cost for a bounded observer entering a domain; synthesizes information-value, discovery, and distillation
- [first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit](./first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) — Deutsch's adaptive-vs-explanatory distinction: explanatory knowledge transfers because it captures why, not just what works; grounds the KB's first-principles filter as selecting for reach

## Discovery

A third operation, distinct from both constraining and distillation: positing a new general concept and simultaneously recognizing existing particulars as instances of it. Discovery produces theories — the highest-reach items accumulation can store.

- [discovery-is-seeing-the-particular-as-an-instance-of-the-general](./discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — the dual structure of discovery (posit the general, recognize the particular); three depths from shared feature through shared structure to generative model; the hard problem is recognition, not linking

## Synthesis

- [a good agentic KB maximizes contextual competence through discoverable, composable, trustworthy knowledge](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — accumulation as the basic operation plus three transformation operations (constraining, distillation, discovery) mapped to three knowledge properties (trustworthy, discoverable, composable) serving contextual competence under bounded context; reach as the quality dimension of what's accumulated
- [agent context is constrained by soft degradation not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — the binding constraint is the soft degradation curve (dilution, compositional collapse), not the hard token limit; programmatic constructability is the genuine differentiator
- [soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — catalog of twelve traditions with transfer assessment: what's already working, what's plausible, and what blocks transfer (optimization target mismatch, feedback absence, different failure modes)

## Oracle & Verification

Moved to [LLM interpretation errors](./llm-interpretation-errors-index.md) — oracle theory, error correction, reliability dimensions, and the augmentation/automation boundary now live in the dedicated error-theory area. Key notes:

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the core theory of error correction via decorrelated weak oracles
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — the gradient from hard to no oracle that determines engineering priorities

## Memory & Architecture

- [three-space-agent-memory-maps-to-tulving-taxonomy](./three-space-agent-memory-maps-to-tulving-taxonomy.md) — agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distinction
- [three-space-memory-separation-predicts-measurable-failure-modes](./three-space-memory-separation-predicts-measurable-failure-modes.md) — the three-space claim is testable: flat memory predicts specific cross-contamination failures
- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](./inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — codification counters the blackbox problem not by requiring human review but by choosing a substrate (repo artifacts) that any agent can inspect, diff, test, and verify
- [A-MEM: Agentic Memory for LLM Agents](../sources/a-mem-agentic-memory-for-llm-agents.md) — academic paper: Zettelkasten-inspired agent memory with automated link generation; flat single-space design provides a test case for whether three-space separation matters at QA-benchmark scale
- [memory-management-policy-is-learnable-but-oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — AgeMem's RL-trained memory policy demonstrates low-reach accumulation (facts) and distillation (STM); confirms memory policy is vision-feature-like per the bitter lesson boundary, but requires a task-completion oracle the KB cannot yet provide
- [Multi-Agent Memory from a Computer Architecture Perspective](../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) — computer-architecture analogy for multi-agent memory: shared/distributed paradigms, three-layer hierarchy, and consistency protocols as the critical unsolved problem
- [Graphiti](../sources/graphiti-temporal-knowledge-graph.ingest.md) — temporally-aware knowledge graph with bi-temporal edge invalidation; strongest temporal model in the surveyed memory systems and strongest counterexample to files-first architecture

## Applications

- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — when agents and tools share a calling convention, constraining and codification become local operations; llm-do as primary evidence
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — typing, testing, progressive compilation, and version control transfer from programming to LLM prompting, with probabilistic execution making some practices harder
- [ad-hoc-prompts-extend-the-system-without-schema-changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — the counterpoint: sometimes staying at the prompt level is the right choice; ad hoc instructions absorb new requirements faster than schema changes
- [legal-drafting-solves-the-same-problem-as-context-engineering](./legal-drafting-solves-the-same-problem-as-context-engineering.md) — law as an independent source discipline for the underspecified instructions problem: precedent and codification are constraining; legal techniques are native to the underspecified medium
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — ephemeral vs persistent artifacts as inverse of codification; discarding generated artifacts trades accumulation for simplicity
- [Ephemerality is safe where embedded operational knowledge has low reach](./ephemerality-is-safe-where-embedded-operational-knowledge-has-low-reach.md) — synthesizes Kirsch's four barriers with the reach concept: the ephemeral/malleable boundary sits where embedded operational knowledge crosses from low reach (adaptive, safe to discard) to high reach (explanatory, must accumulate)

## Reference material

- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.md) — empirical study of AGENTS.md/CLAUDE.md evolution in 466 OSS projects; commit-level analysis shows constraining maturation trajectory confirming continuous learning through versioned artifacts
- [On the "Induction Bias" in Sequence Models](../sources/induction-bias-sequence-models-ebrahimi-2026.md) — 190k-run empirical study showing transformers need orders-of-magnitude more data than RNNs for state tracking; architectural induction bias determines data efficiency and weight sharing, grounding the computational bounds dimension of learning capacity

## Related Tags

- [llm-interpretation-errors](./llm-interpretation-errors-index.md) — oracle theory, error correction, and reliability dimensions migrated here; the error-theory area applies verification concepts specifically to LLM interpretation failures
- [tags](./tags-index.md) — applies learning theory to KB architecture and evaluation; [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) bridges both areas
- [document-system](./document-system-index.md) — the type ladder (text→note→structured-claim) instantiates the constraining gradient for documents

## Other tagged notes <!-- generated -->

- [Apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — When framework-owned tool loops recover from broken tools via agent workarounds, final success stops being a reliable signal that the underlying scripts and workflows are healthy
- [Automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) — Generating synthesis candidates (cross-note connections, novel combinations) is easy — LLMs do it readily. The hard part is evaluating whether a candidate is genuine insight or noise.
- [Brainstorming: how reach informs KB design](./brainstorming-how-reach-informs-kb-design.md) — Brainstorming on Deutsch's "reach" concept applied to KB notes — reach is a maintenance risk signal (not a retrieval signal) because high-reach revisions break downstream reasoning silently
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — Since you can't identify which side of the bitter lesson boundary you're on until scale tests it, practical systems must codify and relax — with spec mining avoiding the vision-feature failure mode
- [Epiplexity by example: what entropy and complexity miss](./epiplexity-eli5.md) — ELI5 explanation of epiplexity through encrypted messages, shuffled textbooks, CSPRNGs, and chess notation — contrasting surprise, shortest description, and observer-relative usable structure
- [Reverse-compression (inflation) is the failure mode where LLM output expands without adding information](./reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md) — LLMs can inflate a compact seed into verbose prose that carries no more extractable structure — the test for whether a KB resists this is whether notes accumulate epiplexity across the network, not just token count
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — The library's purpose is to produce notes that can be co-loaded for combinatorial discovery — short atomic notes are a consequence of this goal; longer synthesized artifacts belong in workshops or distilled instructions
- [Silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — When an agent silently resolves unacknowledged material ambiguity in a spec, final success hides that the contract failed to determine the path — an extension of the tool-fallback observability problem
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md) — Controlled prompt variation either decorrelates checks or measures brittleness under fixed task semantics; Deutsch's variation test instead changes the explanation to test mechanism and reach
- [The fundamental split in agent memory is not storage format but who decides what to remember](./related-systems/agentic-memory-systems-comparative-review.md) — Comparative analysis of eleven agent memory systems across six architectural dimensions — storage unit, agency model, link structure, temporal model, curation operations, and extraction schema — revealing that the agency question (who decides what to remember) is the most consequential design choice and that no system combines high agency, high throughput, and high curation quality.
- [Trace-derived learning techniques in related systems](./trace-derived-learning-techniques-in-related-systems.md) — Broad review of Napkin, Pi Self-Learning, OpenViking, ClawVault, Autocontext, OpenClaw-RL, and trajectory learners — compares trace formats, promotion targets, and learning loops
