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

Moved to [LLM interpretation errors](./llm-interpretation-errors-index.md) — oracle theory, error correction, reliability dimensions, and the augmentation/automation boundary now live in the dedicated error-theory area. Key notes:

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

- [llm-interpretation-errors](./llm-interpretation-errors-index.md) — oracle theory, error correction, and reliability dimensions migrated here; the error-theory area applies verification concepts specifically to LLM interpretation failures
- [tags](./tags-index.md) — applies learning theory to KB architecture and evaluation; [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) bridges both areas
- [document-system](./document-system-index.md) — the type ladder (text→note→structured-claim) instantiates the constraining gradient for documents

## Other tagged notes <!-- generated -->

- [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) - Behavior-changing memory must activate before relevant actions rather than waiting for explicit retrospective search
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - Frames discoverable, composable, trusted remembered knowledge as the minimal artifact-quality basis for agent memory under bounded context.
- [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](./an-agentic-kb-maximizes-contextual-competence-through-discoverable.md) - Retired note kept as a backlink target; its general memory-quality claim and KB-specific ingress claim now live in narrower successor notes.
- [Apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned.md) - When framework-owned tool loops recover from broken tools via agent workarounds, final success stops being a reliable signal that the underlying scripts and workflows are healthy
- [Automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) - Generating synthesis candidates (cross-note connections, novel combinations) is easy — LLMs do it readily. The hard part is evaluating whether a candidate is genuine insight or noise.
- [Behavioral authority](./definitions/behavioral-authority.md) - Definition - behavioral authority records who consumes a retained artifact, through which channel, and with what force
- [Brainstorming: how reach informs KB design](./brainstorming-how-reach-informs-kb-design.md) - Brainstorming on Deutsch's "reach" concept applied to KB notes — reach is a maintenance risk signal (not a retrieval signal) because high-reach revisions break downstream reasoning silently
- [Choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) - Separates two promotion checks for learning loops: whether a candidate is trustworthy enough to learn from, and whether learning it would improve the current system.
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) - Derives agent-memory design pressures and links to a requirements inventory for agents designing or evaluating memory systems
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) - Outer-loop learning depends on inspectable failure evidence, not only on the oracle used to select winning candidates
- [Evaluate Memory By Effects, Not By Existence](./agent-memory-requirements/evaluate-memory-by-effects.md) - Memory should be evaluated by downstream effects on tasks, artifacts, answers, behavior, context efficiency, and lineage alignment
- [Evolving understanding needs re-distillation, not composition](./evolving-understanding-needs-re-distillation-not-composition.md) - When understanding evolves, reconciling fragments into a coherent picture can exceed effective context; a pre-distilled narrative keeps the whole picture within feasible bounds
- [Knowledge artifact](./definitions/knowledge-artifact.md) - Definition - a knowledge artifact is a retained artifact consumed as evidence, reference, context, explanation, or advice
- [Known-target discovery benchmarks show reachability, not discovery closure](./known-target-discovery-benchmarks-show-reachability-not-discovery.md) - Distinguishes backcast and reinvention benchmarks from autonomous discovery: they show that target insights are reachable from supplied ingredients, not that a system can select and verify new discoveries prospectively.
- [Lineage](./definitions/lineage.md) - Definition - lineage records the source dependencies needed to invalidate, regenerate, retire, or review retained behavior-shaping artifacts
- [Links encode conditional possibilities, not obligations](./links-encode-conditional-possibilities-not-obligations.md) - Links encode conditional possibilities, not obligations — every label must name a specific reader-need (the condition under which following pays off); content required for all reachable readers should be inlined, not linked
- [LLM debugging starts with retry-versus-rewrite triage](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) - The two-phenomena model makes the first LLM debugging question diagnostic — is the failure a bad execution of a good interpretation (retry) or a consistent choice of a bad interpretation (rewrite the spec)? — because the fixes differ and do not substitute
- [LLM↔code boundaries are natural checkpoints](./llm-code-boundaries-are-natural-checkpoints.md) - At each LLM↔code transition both semantic underspecification and execution indeterminism collapse simultaneously, making these boundaries natural places to anchor debugging, testing, and refactoring
- [Memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) - Memory design needs operational policy axes (capture, derivation, activation, authority assignment, lifecycle, evaluation) on top of substrate, form, lineage, and behavioral authority
- [Opacity is a scale threshold, not a class property](./opacity-is-a-scale-threshold.md) - Opacity is not a representational form; any representation becomes practically opaque at sufficient scale, though distributed-parametric artifacts cross that threshold earliest.
- [Operative part](./definitions/operative-part.md) - Definition - an operative part is the behavior-affecting content, structure, parameterization, or mechanism within a retained artifact or consumption path
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) - Constraining via LLM code generation freezes a single projection of the spec in one shot, but progressive constraining observes behavior across many runs and commits only the interpretations that consistently emerge
- [Psychology-to-agent transfer needs per-principle failure-mode testing](./psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) - Brainstorming a methodology for evaluating cognitive-science-to-agent transfer — assembled from three existing KB notes and tested against Youssef's five psychology principles as worked examples
- [Representational form](./definitions/representational-form.md) - Definition - representational form classifies how an operative part is encoded and consumed: prose, symbolic, distributed-parametric, or mixed
- [Retained artifact](./definitions/retained-artifact.md) - Definition - a retained artifact is retained state that a later agentic loop can consume in a behavior-shaping way, regardless of storage substrate
- [Reverse compression is when LLM output expands without adding information](./reverse-compression-is-when-llm-output-expands-without-adding.md) - LLMs can inflate a compact seed into verbose prose that carries no more extractable structure — the test for whether a KB resists this is whether notes accumulate epiplexity across the network, not just token count
- [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) - Compares RLM, Tendril, and llm-do as three placements for symbolic work and interfaces: ephemeral REPL code, workspace-local generated tools, and durable unified callables
- [Selector-loaded review gates could let review-revise learn from accepted edits](./selector-loaded-review-gates-could-let-review-revise-learn-from.md) - Brainstorm on learning reusable review gates from accepted note edits: mine candidate gates from before/after diffs, store them atomically, and load a bounded subset into future reviews
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) - The library's purpose is to produce notes that can be co-loaded for combinatorial discovery — short atomic notes are a consequence of this goal; longer synthesized artifacts belong in workshops or distilled instructions
- [Silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) - When an agent silently resolves unacknowledged material ambiguity in a spec, final success hides that the contract failed to determine the path — an extension of the tool-fallback observability problem
- [Storage substrate](./definitions/storage-substrate.md) - Definition - storage substrate records where retained state persists, as an operational field distinct from form, lineage, and authority
- [System-definition artifact](./definitions/system-definition-artifact.md) - Definition - a system-definition artifact is a retained artifact consumed with instruction, enforcement, routing, validation, configuration, evaluation, or learning force
- [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) - Heuristic system-definition artifacts (tips, playbooks, rules) are mostly crystallized reasoning; under unbounded context heuristic prose collapses into knowledge artifacts plus read-time derivation, while authority-bearing constraints and symbolic codification persist for other reasons
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](./systematic-prompt-variation-serves-verification-and-diagnosis-not.md) - Controlled prompt variation either decorrelates checks or measures brittleness under fixed task semantics; Deutsch's variation test instead changes the explanation to test mechanism and reach
- [The adaptation survey corroborates memory requirements but misses artifact governance](./agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) - The agentic-adaptation survey supports the memory requirements map by treating memory and skills as adaptive tools, but it needs substrate, form, lineage, and authority governance to become design guidance
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) - Within substrate coevolution, the readable pair (prose + symbolic) is the tractable unit to build a first automated loop around — shared context, current tempo, and an existing codification boundary make joint optimization clean; the pair is also under-explored relative to distributed-parametric optimization
- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) - Behaviour change spans three representational forms — distributed-parametric, prose, and symbolic — so the coevolution question is how their improvement loops relate, not which is the real locus of learning
- [Use Trace-Derived Extraction As Meta-Learning](./agent-memory-requirements/use-trace-derived-extraction.md) - Trace-derived extraction is an after-the-fact learning path that must respect signal quality, review, and readable-artifact versus distributed-parametric learning boundaries
