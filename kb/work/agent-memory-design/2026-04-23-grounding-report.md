# Grounding Report: Designing Agent Memory Systems

Target: [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md)

This report looks for stronger theoretical grounding inside the KB for the design study. It is complementary to [the critique](./2026-04-23-critique.md): the critique identifies tensions and overclaims; this report identifies the best local foundations the note can lean on, plus the places where grounding should change the framing.

## Summary

The design study is already well-aligned with the KB. Its strongest grounding is not "agent memory" as a standalone topic, but the intersection of three theory clusters:

1. **Context engineering:** memory only matters when the context engine selects, frames, and injects it into a bounded call.
2. **Readable-artifact learning:** session traces become durable capacity through distillation, constraining, and codification.
3. **Oracle theory:** extraction and promotion depend on signal quality; corrections are strong, discoveries are weak, and system-definition cues need behavioral faithfulness tests.

The main improvement is to reframe the note around the KB's stronger decomposition: memory is not one subsystem. It is storage on the execution substrate, retrieval/activation in the context engine, and learning across readable artifacts. The four-layer design then becomes a recommended architecture for this decomposition, not the primitive theory itself.

## Best Foundations

### 1. Context Scarcity Grounds the Whole Design

The note's opening premise, "storage is cheap, context is scarce," should be explicitly grounded in [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md).

That note gives the stronger argument:

- context is the only channel through which an agent receives instructions, knowledge, and task state;
- context degrades before the hard token limit because irrelevant material dilutes cues and complicates interpretation;
- architectural responses include progressive disclosure, frontloading, sub-agent isolation, navigation design, and symbolic scheduling.

This supports the memory design's core inversion: do not optimize primarily for storage minimization; optimize for context assembly. But it also makes the design more precise. "Storage is cheap" is not enough. The stronger claim is:

> Memory architecture is a context-efficiency problem: stored material has value only through the context-engine decisions that select, compress, and frame it for a bounded consumer.

[Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) sharpens the same point. It distinguishes persistence from loading: store more than you load. This is the cleanest grounding for the trace layer. Raw traces should persist as external state, but next-call context should be assembled deliberately.

Recommended revision anchor:

- Replace broad "store everything" language with "persist traces broadly; load selectively through the context engine."
- Treat context scarcity as the reason for every downstream layer, not just for retrieval.

### 2. Runtime Decomposition Locates Memory's Subproblems

[Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) gives a better architectural home for the design than "memory system."

Mapping:

| Memory concern | Runtime component | What it owns |
|---|---|---|
| Trace files, observation stores, library artifacts | Execution substrate | Durable exact state outside the model |
| Search, activation, cue injection, progressive disclosure | Context engine | What each bounded call sees |
| Promotion jobs, periodic consolidation, authority decisions | Scheduler plus learning loop | When extraction, review, and mutation run |

[Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) makes this explicit: memory decomposes into storage, retrieval/activation, and learning. This note should probably become one of the primary foundations for the design study.

Recommended revision anchor:

- Introduce the four layers after the runtime decomposition, as one way to arrange substrate state for a context engine and learning loop.
- Avoid implying memory is a pluggable component with one internal architecture.

### 3. Role Split Is Strongly Grounded

The note's knowledge-role versus system-definition-role split is one of its strongest moves. It is grounded by [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md), which separates:

- artifact class: opaque, prose, symbolic;
- backend: files, database, graph store, service memory;
- role: knowledge versus system-definition.

The note uses the role axis correctly: the same bytes can answer a question in one context and steer behavior in another. That distinction is stronger than the usual "RAG vs memory" framing because it explains why ordinary retrieval solves only the knowledge half.

[Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) is the most important companion. It says knowledge accumulation is mostly solved by data engineering, while behavior change is the open problem. The design study's typed cue index is exactly a readable system-definition mechanism: a durable prose or symbolic artifact that changes future action.

[The readable-artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) strengthens this further. It frames prose and symbolic artifacts as the practical near-term learning substrate, because both are inspectable, versionable, and compete for the same context budget.

Recommended revision anchor:

- Make "memory plays two roles" the theory bridge from storage/retrieval into continual learning.
- Use "system-definition activation" as the behavior-change half of continual learning, not merely as a retrieval variant.

### 4. Four Layers Are Grounded by Distillation, but Not Necessity

The four layers, trace, observation, episode, library, are best grounded by [Distillation](../../notes/definitions/distillation.md): directed context compression for a bounded consumer.

Layer mapping:

| Layer transition | Theory |
|---|---|
| Trace to observation | Distillation from raw recorded material into atomic candidate artifacts |
| Observation to episode | Distillation into narrative form for "what happened?" retrieval |
| Observation/episode to library | Distillation plus review into durable knowledge or policy |
| Procedure/cue to script/test | Distillation plus constraining/codification |

[Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) also grounds the layer design. Observations, descriptions, episode summaries, indexes, and link phrases are all pointers at different resolution/cost/reliability tradeoffs. The memory architecture should be described as a progressive-disclosure system, not merely as a hierarchy of storage buckets.

The weaker point is necessity. The KB grounds "progressive distillation" and "separate retrieval interfaces for atomic and narrative memory." It does not prove that every implementation needs exactly four layers. The existing comparative review supports staged distillation and progressive disclosure, not a universal layer count.

Recommended revision anchor:

- State: "This design uses four conceptual layers because atomic lookup, narrative recall, and curated durable knowledge need different retrieval interfaces."
- Avoid: "The problem requires exactly four layers."

### 5. Activation Gap Grounds Typed Cues

[Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) is the direct theoretical foundation for the cue-index design. It decomposes activation failure into:

- cue match;
- priority arbitration;
- commitment.

The design study reuses this decomposition well. Typed cue indexes are a concrete mechanism for cue match. Budgeted cue loading handles priority arbitration. Imperative framing, checkpoint insertion, and contradiction surfacing are commitment interventions.

[Agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) gives a broader context-engine version of the same mechanism: the agent should not have to know what to load; the runtime should inject referenced or triggered context. Typed cues are one special case of automatic injection, keyed on action or situation rather than document reference.

[Always-loaded context mechanisms in agent harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) adds a useful surface distinction. Some policy belongs in always-loaded files, some in capability descriptions, some in memory, and some in configuration injection. Cues should be placed according to read/write cadence and context cost, not all promoted to the same surface.

Recommended revision anchor:

- Define typed cue indexes as an "on situation" loading layer, parallel to "on reference" and "on invoke."
- Add a placement rule: high-frequency, stable, low-cost rules can move toward always-loaded policy; narrow or volatile cues stay triggered.

### 6. Extraction Taxonomy Is an Oracle-Strength Taxonomy

The current extraction taxonomy is useful but can be grounded more sharply in [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md).

Signal mapping:

| Extraction type | Oracle strength | Why |
|---|---|---|
| Corrections | Interactive oracle, strongest | User gives explicit negative and positive signal |
| Silent failures | Hard/soft operational signal | Tool errors and fallback paths are visible, but significance requires judgment |
| Preferences | Statistical/interactive oracle | Individual decisions are weak; recurrence creates confidence |
| Procedures | Structural oracle | Repeated action sequences reveal reusable workflow |
| Discoveries | Weak/delayed oracle | Value often only appears through later reuse |
| Decision provenance | Soft, reviewable oracle | Alternatives and selection are visible, but "load-bearing" status needs judgment |
| Negative results | Soft-to-interactive oracle | Failed attempt may be visible; generality and recurrence need review |

This makes the build order more defensible. Start with corrections because their oracle is strongest. Add silent failures because traces expose explicit runtime signals. Delay discoveries because they lack a reliable extraction oracle.

[Trace-derived learning techniques in related systems](../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) provides the evidence base: systems repeatedly mine traces into tips, memories, playbooks, rules, observations, and sometimes code, but evaluation and retirement remain the open problem. The design study can cite that survey for the recurring stages: trigger, source format, extraction schema, promotion/storage, reinjection.

Recommended revision anchor:

- Reframe the extraction taxonomy as "signals ordered by oracle strength and promotion difficulty."
- Separate extraction confidence from promotion authority. A strong extraction signal does not automatically justify a durable policy write.

### 7. Promotion and Graduation Are Constraining Decisions

[Constraining](../../notes/definitions/constraining.md) and [Codification](../../notes/definitions/codification.md) are the best grounding for graduation paths.

The design already gestures at a codification gradient. The stronger local theory says:

- constraining narrows the interpretation space;
- codification is the far end where natural language crosses into executable/formal artifacts;
- oracle strength determines what can safely codify;
- premature constraining locks in brittle assumptions, so relaxing must remain possible.

[Spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md) is especially relevant for silent failures, repeated corrections, and procedure extraction. It gives the operational loop:

1. observe repeated behavior or failures;
2. identify a deterministic rule or verifier;
3. extract it into tests, schemas, scripts, or checks;
4. monitor for brittleness and relax if needed.

This is stronger than saying "some observations graduate to scripts." It explains when and why they do.

Recommended revision anchor:

- Make each promotion destination a point on the constraining spectrum: candidate observation, prose convention, instruction/skill, checklist, test, script, guardrail.
- Add "relaxation" to the lifecycle so cues and codified checks can move back toward prose when they prove brittle.

### 8. Agency and Authority Need the Comparative Review

The design names the agency trilemma, but its own authority model is still implicit. [The fundamental split in agent memory is not storage format but who decides what to remember](../../agent-memory-systems/agentic-memory-systems-comparative-review.md) should be used more directly.

The review's strongest finding is that agency model determines the architecture:

- agent-self-managed memory has context but spends reasoning budget;
- external services scale but guess what matters;
- human+agent collaboration has high quality but low throughput;
- RL-trained policies can adapt but need strong oracles and become opaque.

The design study implicitly chooses external/post-session extraction plus human or agent review for high-risk promotion. That should be stated as an authority model.

[Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) gives the caution: learned memory policy works when task-completion oracles exist. Open-ended KB/memory work usually lacks that oracle, so inspectable heuristics and review gates are not just conservative; they are a response to oracle weakness.

Recommended revision anchor:

- Add a transition-by-transition authority table:
  - trace capture: automatic;
  - candidate observation: extractor;
  - cue activation: context engine under budget rules;
  - library promotion: human/agent review depending on risk;
  - always-loaded policy or guardrail: strongest review/evaluation;
  - retirement/relaxation: scheduled maintenance plus evidence.

### 9. Navigability Grounds Search + Navigation

The note's retrieval section distinguishes search, navigation, and activation. The strongest local grounding is the comparative review's "navigability versus retrieval" section plus [Quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md).

The key distinction:

- retrieval accuracy tests whether a system can answer direct questions;
- navigability tests whether a system supports reasoning by following articulated relationships;
- activation tests whether relevant policy fires without a direct question.

The design study should preserve all three as separate evaluation dimensions. QA benchmarks can validate knowledge-role retrieval but do not validate link structure or system-definition activation.

Quality-signals also contributes useful evaluation ideas for the memory design:

- link articulation as a proxy for navigability;
- pruning accuracy for progressive-disclosure pointers;
- agent-centric hop cost;
- trust calibration;
- Goodhart risk from noisy links or excessive candidate artifacts.

Recommended revision anchor:

- Add "evaluation dimensions" after the retrieval section: direct retrieval, navigability, activation/behavioral uptake, and lifecycle health.
- Treat noisy observations as a link/search pollution risk, grounded by [Flat memory predicts specific cross-contamination failures](../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md).

### 10. Workshop Theory Grounds the Missing Active Layer

The four memory layers are retrospective: they organize what happened and what should persist. [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) shows what is missing: active work-in-motion artifacts with state machines, dependencies, and expiration.

This matters because memory extraction often runs through active work surfaces:

- a decision thread produces an ADR;
- an experiment produces a note, a negative result, or nothing;
- a task produces a procedure or codified check;
- a session log produces observations and follow-up work;
- a review thread produces policy changes or source-of-truth updates.

The design study's "episode" layer covers retrospective narrative, but not active workshop state. The memory/work-surface section partially addresses this, but it should explicitly distinguish:

- active workshop artifacts: current work state;
- episodes: retrospective memory of bounded work;
- library: durable curated outputs.

Recommended revision anchor:

- Say the four layers are memory layers, not a complete work architecture.
- Add workshop/work-surface artifacts as adjacent producers and consumers of the memory system.

## Where the Note Is Already Well Grounded

The following claims are already strongly grounded and should be preserved:

- **Store more than you load.** Grounded by context scarcity and session-history separation.
- **Knowledge and system-definition roles require different machinery.** Grounded by artifact-role theory and continual-learning theory.
- **Activation is not retrieval.** Grounded by the activation-gap note.
- **Trace-derived extraction is plausible for corrections, preferences, procedures, and lessons.** Grounded by the related-systems trace-mining survey.
- **Promotion must be separate from extraction.** Grounded by oracle weakness, curation operations, and candidate/library separation.
- **Procedures and repeated corrections can harden along a prose-to-symbolic gradient.** Grounded by constraining, codification, and spec mining.
- **Search and navigation solve different problems.** Grounded by the comparative review and quality-signals work.

## Where Grounding Should Change the Framing

### Store-Everything Should Be a Capture Posture

The KB supports broad trace retention, not indiscriminate memory design. "Store everything" should mean:

> Store all eligible traces under retention/redaction policy because future distillation is hard to predict; extraction, promotion, and loading remain output-driven.

This avoids conflict with output-driven KB theory and makes room for privacy, retention, and index-pollution controls.

### Four Layers Should Be a Design Hypothesis

The theory supports:

- traces should be retained separately from next context;
- candidate observations should be distinct from curated artifacts;
- atomic lookup and narrative recall need different retrieval interfaces;
- progressive disclosure needs lower-resolution pointers before full loads.

It does not prove that every system needs exactly trace, observation, episode, library as separate layers. The report should present four layers as the recommended decomposition for this design.

### Cue Firing Is Not Enough

The activation-gap theory decomposes commitment, but recent grounding from faithful-self-evolver and ignored-solution evidence means the design needs a stronger test:

> A cue succeeds only if it causally changes downstream action in the intended direction.

Synapptic-style with/without guard testing, perturbation tests, or post-action trace audits should be mentioned for promoted cues, especially always-loaded or high-priority policy.

### Authority Is Part of the Architecture

Every transition that changes future behavior needs an authority rule. Candidate writes can be cheap; system-definition writes are behavior-changing and should have stronger review or evaluation. The agency trilemma makes this architectural, not operational housekeeping.

### Library-Derived Cues Need Source-of-Truth Rules

If a durable note or policy generates a cue, the cue is a compiled view. It should carry provenance, source hash/version, and regeneration rules. Otherwise the cue and source policy drift into two conflicting system-definition surfaces.

## Candidate Grounding Additions to the Note

High-value "Relevant Notes" additions:

- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — primary foundation for context scarcity.
- [Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — locates storage, activation, and scheduling responsibilities.
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — strongest local summary of memory as storage + context engineering + learning.
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — grounds summaries, descriptions, cue triggers, and episode pointers as progressive-disclosure artifacts.
- [The readable-artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — grounds prose and symbolic memory artifacts as the practical learning substrate.
- [Oracle strength spectrum](../../notes/oracle-strength-spectrum.md) — grounds the extraction taxonomy and build order.
- [Spec mining is codification's operational mechanism](../../notes/spec-mining-as-codification.md) — grounds silent failures, repeated corrections, and procedure-to-check graduation.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — grounds the active work-surface gap.
- [Quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md) — grounds navigability and soft-oracle evaluation.
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — grounds why learned memory policy is attractive but not generally available without task oracles.

## Candidate Extracted Claims

These are the most reusable claims that may deserve standalone notes if the design study is revised:

- **Store-everything is a capture posture, not a memory design.** Broad trace persistence preserves optionality, but output goals govern extraction, promotion, retention, and loading.
- **Typed cue indexes are on-situation context injection.** They are the action-triggered counterpart to on-reference loading and skill activation.
- **Memory layers are progressive distillation interfaces.** Their purpose is not storage taxonomy but matching retrieval interfaces to consumer tasks.
- **Cue promotion needs behavioral faithfulness tests.** A cue that fires but does not change action has not closed the activation gap.
- **Library-derived cues are compiled policy views.** They need provenance and regeneration rules or they become divergent sources of truth.
- **Episode memory is retrospective; workshop memory is active.** A complete agent memory architecture needs both.
- **Extraction taxonomy should follow oracle strength.** Corrections, silent failures, preferences, procedures, and discoveries differ mainly by signal quality and promotion risk.

## Practical Revision Order

1. Add a short theoretical preface: memory = substrate storage + context-engine activation + readable-artifact learning.
2. Reframe store-everything as trace capture under retention/redaction, not as the whole design principle.
3. Make the role axis and continual-learning behavior problem the conceptual center of the "memory plays two roles" section.
4. Weaken the four-layer necessity claim while preserving the recommended architecture.
5. Add authority and source-of-truth rules for promotion and cue compilation.
6. Add behavioral faithfulness evaluation for system-definition cues.
7. Add active workshop/work-surface artifacts as adjacent to episodes, not absorbed by them.

