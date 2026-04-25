---
description: "Requirements map for realistic agent memory systems: direct creation, import, evidence retention, contracts, activation, promotion, authority, lifecycle, compiled views, and evaluation"
type: kb/types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
status: current
---

# Designing a Memory System for LLM-Based Agents

An ideal memory system for LLM-based agents should start from the needs it must satisfy, not from its storage architecture or from the mechanism that produced each memory. It has to preserve useful evidence, turn experience into future capacity, expose contracts for memory artifacts, assemble the right context for bounded calls, steer future behavior when past lessons apply, and revise or retire memory when it stops earning its cost.

The first version of this note proposed an integrated design around trace, observation, episode, and library layers. That integration was premature. The stronger claim is narrower: agent memory is a [context engineering](./definitions/context-engineering.md) (right-knowledge-into-bounded-context) problem whose success criterion is contextual competence, not recall volume. A memory is useful when it improves what the agent can do under bounded context.

The contextual-competence test from [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](./an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) makes the requirement concrete. Whatever created a memory -- direct authoring, import, trace extraction, synthesis, or codification -- the result must be discoverable enough to find, composable enough to use with other knowledge, and trustworthy enough to rely on without redoing the original work. The hard part is deciding which remembered material should affect a future answer, action, artifact, or system rule.

## The Memory Problem Is Crosscutting

Agent memory cuts across the runtime rather than sitting in one component. As [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) argues, storage belongs on the execution substrate, retrieval and activation belong in the context engine, and learning belongs in the loop that turns experience into readable or executable artifacts.

## Memory Is More Than Retrieval

The learning loop should not stop at prose memory. As [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) argues, deployed agent systems improve across sessions by updating durable system-definition artifacts such as prompts, instructions, schemas, checks, scripts, plugins, and tools. When a learned pattern becomes deterministic enough, it should move toward [codification](./definitions/codification.md) (committing procedure to a symbolic medium), because [bookkeeping work is more reliable on a symbolic substrate than when re-run through the LLM each time](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).

Calling those behavior-changing artifacts "memory" is not just a stretch of retrieval vocabulary. The useful distinction is functional: some memory supports explicit recall, while some memory changes future action. The KB's [Tulving taxonomy note](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) treats human semantic, episodic, and procedural memory as a loose analogy for this split. In the agent setting, a note that answers "what do we know?" is declarative memory; a checklist, skill, test, guard, or instruction that changes what the agent does next is procedural memory.

Agents also need a small control-plane memory layer: purpose, scope, routing hints, vocabulary, quality bars, commands, skills, and safety rules that shape how the agent finds and interprets the rest of memory. This layer is expensive because it is always or frequently loaded. Since [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md), the control plane should route the agent toward the right memory rather than contain the memory itself. It is the stable, high-frequency complement to on-demand retrieval and situation-specific activation.

Bounded context also means memory will not collapse into one model call over one complete store. Long-lived agents need external information because everything cannot fit in weights, but they also need context-construction machinery because everything cannot fit in one context. The agentic loop must repeatedly decide what to inspect, what to load, what to execute, what to update, and what to ignore.

That leaves two plausible end states for the symbolic layer. One is that symbolic artifacts -- indexes, schemas, instructions, scripts, validators, cues, generated views, and work-surface state -- are themselves memory stores, which implies automatic learning over symbolic artifacts. The other is a more universal symbolic layer that operates over a broad prose memory store. Even in that case the symbolic layer has to evolve, because today's routing, validation, activation, source-tracking, and maintenance machinery is not complete enough to be treated as fixed infrastructure.

This role distinction matters because the same remembered material can serve different functions. [Axes of artifact analysis](./axes-of-artifact-analysis.md) distinguishes knowledge-role artifacts, which answer questions, from system-definition-role artifacts, which steer behavior. A decision rationale is knowledge when the agent asks "why did we choose this?" The same rationale becomes system-definition when it prevents the agent from proposing the rejected alternative again.

The role split prevents a common design error: treating memory as better retrieval-augmented generation (RAG). RAG is a declarative-memory pattern: ask a question, retrieve relevant knowledge, and put it in context. Agent memory also needs proceduralization, where lessons become instructions, skills, tests, checks, tools, guardrails, or work-surface changes that alter future action. Search can answer direct questions, but it does not decide which routines should be compiled, when they should fire unasked, or when they should be retired. [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md): a stored lesson has not helped unless it appears in the right bounded context, with enough priority and framing to change what happens next.

## Need 1: Create Memory Directly

Direct memory creation is the lowest-latency path when the lesson is already understood. When current work reveals a stable claim, procedure, policy, index entry, validation rule, or tool extension, the natural operation is to write the useful artifact directly. Waiting for a later extractor to rediscover the same lesson from the transcript is a fallback.

Direct creation should not mean blank-page authoring. The system should help the agent choose the right artifact shape and satisfy that artifact's quality contract at write time. Memory destinations should expose their creation contract, not just accept content after the fact.

Realistic memory artifacts include:

- Notes and decision records for claims, rationales, alternatives, and negative results.
- Instructions, skills, checklists, and runbooks for repeated work patterns.
- Indexes and link maintenance for navigation and context discovery.
- Tests, validators, scripts, plugins, and runtime extensions for deterministic learned behavior.
- Work-surface updates when the authoritative destination is a ticket, report, dashboard, product configuration, or source document rather than the memory system itself.

Realistic authoring supports include:

- Routing cues that suggest which artifact class should receive the learned material.
- Collection or domain quality requirements loaded before writing.
- Type-specific procedures, templates, schemas, or rubrics for producing valid artifacts.
- Link and index obligations that make the new memory findable rather than merely stored.
- Validators, linters, review gates, or preview checks that catch malformed or low-quality memory before promotion.
- Import tools that convert external knowledge into the system's own artifact forms.

These contracts should vary by memory role because [knowledge-role and system-definition-role artifacts serve different functions](./axes-of-artifact-analysis.md). Each role fails differently: an explanatory note fails when its claim has no reach or caveats; a decision record fails when alternatives and consequences are unrecoverable; a source ingest fails when it loses provenance or overstates the source; a procedure fails when the intended agent cannot execute it without hidden context; a generated view fails when it drifts from its source; and a guard fails when authority, rollback, and recovery are unclear. Generic "memory item" schemas are too weak unless they preserve what kind of memory is being created and how that kind earns trust.

Direct authoring still needs evaluation and lifecycle management. A note can be accurate but hard to find. An instruction can steer behavior incorrectly. A check can fossilize a temporary workaround. Direct memory is not automatically good; it is good only when it becomes useful future context or useful future behavior.

Commonplace status: implements this need strongly for direct-authored memory through typed notes, indexes, instructions, skills, validation scripts, review gates, and explicit collection/type contracts.

## Need 2: Import External Knowledge Into Internal Form

Memory creation does not only happen by writing new artifacts from the current session. The system should also import external knowledge bases, documents, repositories, source snapshots, tickets, notes, or prior archives into its own internal form. Import is not copying. It is a [distillation](./definitions/distillation.md) (directed context compression) and [constraining](./definitions/constraining.md) (narrowing interpretation space) step that converts external material into artifacts that obey the receiving system's types, links, quality requirements, provenance rules, and retrieval surfaces.

This matters because much of the memory a system needs already exists elsewhere. A project may have an old wiki, a README forest, issue threads, source snapshots, API docs, chat exports, or another knowledge base. Leaving that material external preserves evidence but does not make it agent-usable. The memory system needs import paths that add structure the external source may not have: summaries, semantic descriptions, typed artifacts, links to existing concepts, authority markers, lifecycle status, and source pointers.

Realistic import methods include:

- Snapshots that preserve external sources before analysis, so later claims can be audited.
- Ingest reports or source reviews that classify external material, summarize it, name limitations, and link it into the internal graph.
- Conversion tools that turn raw text or legacy notes into typed internal artifacts with frontmatter, descriptions, links, and status.
- Directory or repository ingestion that treats a related file tree as one source unit rather than many disconnected snippets.
- Re-ingest workflows that rerun classification and connection after the internal KB has changed.
- Staging in a [workshop](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) when the imported material is too large, messy, or contested to promote directly.

Commonplace status: partially implements this need through source snapshots, ingest reports, conversion tooling, and staged workshops; it does not yet have a mature graph-first or bulk-reingest pipeline.

[sift-kg](../agent-memory-systems/reviews/sift-kg.md) is a partial fulfillment of this import need in a document-to-graph setting. It turns document folders into a derived knowledge graph with discovered schemas, materialized pipeline stages, confidence scores, provenance, and human-gated merge/relation review. The implementation shows what import requires beyond "upload documents": schema choice, source preservation, deduplication, review state, and derived artifacts that can be regenerated.

## Need 3: Preserve Evidence Without Making History The Next Context

The memory system needs a capture substrate that keeps enough source material for later extraction, audit, debugging, and redistillation. Broad trace retention is useful because the future consumer is often unknown at capture time.

For a single-user agent harness, broad retention is usually cheap because the stream is mostly text: prompts, model outputs, tool calls, file diffs, command output, and small structured artifacts. Traditional software and current hardware can store that volume cheaply compared with the cost of reconstructing missing reasoning later. This justifies storing text traces broadly when retention and redaction policy allow it.

The limits are payload class and scale. Once traces include large binary or media artifacts -- movies, long audio, screenshots, screen recordings, datasets, build products, or telemetry firehoses -- "store everything" stops being a safe default. Multi-user systems also change the calculation: aggregate volume grows faster, traces contain other people's private or regulated material, authority over retention becomes contested, and search pollution becomes a shared operational cost.

For large payloads, the memory system may keep metadata, thumbnails, transcripts, hashes, sampled excerpts, or provenance pointers instead of raw files. For shared use, it may need per-user retention policies, access controls, or externally managed blobs.

Store-everything is only a capture posture. [Session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) because persistence and loading are separate decisions. Raw traces should usually remain outside the acting agent's ordinary context and load only for provenance checks, dispute resolution, debugging, redistillation, or evaluation.

Realistic methods for this need include:

- Complete session traces with tool calls, timestamps, outputs, errors, and final artifacts.
- Structured event logs that capture actions, decisions, errors, approvals, and produced artifacts without preserving every token.
- Artifact provenance records that link durable notes, policies, decisions, tests, scripts, or plugins back to the sessions and sources that produced them.
- Redacted trace stores where secret scrubbing and retention policy run before extraction or model inspection.
- Selective capture in high-risk domains where privacy, legal retention, media payloads, or data volume make broad logging unacceptable.

Commonplace status: implements evidence preservation for external sources through snapshots and ingests, but does not yet provide broad session-trace capture, redaction, retention, and replay as a memory substrate.

## Need 4: Use Trace-Derived Extraction As Meta-Learning

Once direct memory creation exists, the system can improve it by studying what direct authoring missed. Session logs contain latent memory-creation opportunities, but they differ by oracle strength.

Corrections are strongest because the log contains both a negative and positive signal. Silent failures are weaker: the task appears completed, but the trace shows errors, retries, fallback paths, warning output, or weakened guarantees. Preferences are distributed over many accept/reject events. Procedures show up as recurring action sequences. Discoveries and broad syntheses have the weakest immediate oracle; their value often appears only through later reuse.

The system therefore needs a meta-learning taxonomy ordered by signal quality, not by topic popularity. It should start where the oracle is strongest and delay automation where the oracle is weak. In [bitter lesson](https://en.wikipedia.org/wiki/Bitter_lesson) terms, memory systems should prefer scalable search and learning where feedback is strong, while keeping weak-oracle knowledge work in reviewable artifacts until evaluation can justify relaxation.

The bitter-lesson analogy should therefore not be read as "eventually memory becomes one opaque learned component." Scalable learning can improve how memories and memory artifacts are searched, generated, ranked, and revised, but bounded context keeps context-construction machinery inside the memory problem rather than outside it.

Realistic methods include:

- Narrow, schema-constrained extraction prompts for one signal type at a time.
- Classifiers or simple rules for explicit events: user correction, command failure, retry, fallback, approval, rejection, or repeated tool sequence.
- Batch analysis over many sessions for preferences, procedures, and recurring failure patterns.
- Manual observation inboxes that let agents record noticed improvement opportunities without interrupting the current task.
- Human or agent review queues for weak-oracle candidates such as discoveries, broad design principles, or high-impact policy changes.
- Confidence, source pointers, and candidate status fields so extracted items do not masquerade as durable knowledge.

This is where the reviewed trace-mining systems contribute most evidence, though not a complete solution. [Trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) shows many systems mining traces into tips, memories, rules, procedures, and skills. Both direct authoring and trace-derived extraction still need evaluation, promotion, retirement, and evidence that memory changes future behavior.

Commonplace status: does not yet implement automated session-trace extraction; `kb/log.md` is a useful but underdeveloped manual observation inbox between raw traces and durable artifacts, while the system's current strength is maintaining high-quality memory artifacts once an agent or maintainer understands what should be written.

[cass-memory](../agent-memory-systems/reviews/cass_memory_system.md) partially fulfills the trace-to-procedure path: it mines sessions from multiple coding agents into a shared YAML playbook, tracks feedback, and stores source sessions on each rule. [REM](../agent-memory-systems/reviews/REM.md) fulfills a narrower trace-to-fact path by storing episodes and compressing clusters into short semantic memories. The contrast is useful because it separates the extraction problem from the later questions of lifecycle, authority, and behavioral uptake.

## Need 5: Serve Multiple Consumers, Not One Retrieval Interface

Different consumers need different memory surfaces. A human maintainer asks why a decision was made. An acting agent needs constraints before it acts. A context scheduler needs compact metadata and budget rules. A reviewer needs provenance. A learning loop needs candidate observations. Governance needs authority, redaction, retention, and retirement state. These consumers should not be forced through one retrieval interface.

No single surface satisfies all of these needs. Search is useful for question answering. Navigation is useful when the reader must follow articulated relationships. Triggered activation is useful when the agent would not know to ask. Trace replay is useful when a summary is under suspicion. Active work artifacts are useful when the task is not yet finished.

Realistic method families include:

- Control-plane memory for stable purpose, scope, routing, quality, and safety constraints that should be available before search.
- Search over traces, observations, source summaries, and durable artifacts for direct questions.
- Link navigation and indexes for reasoning through curated knowledge rather than isolated snippets.
- Progressive-disclosure pointers: descriptions, tags, source links, episode summaries, cue titles, and compact evidence records that help the context engine decide what not to load.
- Retrospective episodes for "what happened when we tried this?" questions, where a bounded effort needs narrative recall.
- Active [workshops](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) (work-in-flight spaces with state and expiration) or work-surface artifacts for current state, unresolved alternatives, task queues, experiments, and discussion threads.
- Trace excerpts for audit and redistillation when compressed memory is insufficient.

The important distinction is between retrospective memory and active work. [A functioning KB needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md): work in motion needs state, dependencies, expiration, and unresolved alternatives. Retrospective episodes should not replace the active work surface. Where possible, memory should also meet the agent at its native work surface: files, tickets, documents, dashboards, configurations, tests, review tools, or whatever substrate the agent already uses to act.

Commonplace status: implements multiple consumer surfaces through notes, reference docs, instructions, sources, reports, workshops, commands, skills, and control-plane files; retrospective episodes and typed cue indexes remain underdeveloped.

## Need 6: Activate Behavior-Changing Memory Before The Mistake

The system must not merely answer "what do we know?" It must sometimes answer an unasked question: "what past lesson applies to the action I am about to take?"

[Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md): adding retrievable facts is easier than changing future action. A stored correction only matters operationally if it fires before the agent repeats the corrected behavior.

Realistic activation methods form a range:

- Always-loaded instructions for stable, high-frequency, low-cost constraints.
- On-reference loading when a document, source, issue, or artifact is explicitly mentioned.
- On-invoke loading through skills, tools, or workflows that carry their own instructions.
- On-situation loading through typed cues that match proposed actions, task domains, risk markers, or decision spaces.
- Checklists, tests, scripts, lint rules, approval gates, or runtime guardrails when the lesson can be moved from prose toward symbolic enforcement.

Typed cue indexes provide the on-situation loading form of this family. A cue can carry a trigger condition, lesson, source pointer, role, consequence weight, and placement target. Matching can use rules, embeddings, action classifiers, or LLM relevance judgments. The choice depends on consequence, false-positive tolerance, and cost.

The harder requirement is behavioral faithfulness. A cue that fires and enters context has not succeeded unless it changes downstream action in the intended direction. High-priority system-definition material needs evidence that it earns its context budget: WITH/WITHOUT comparisons, perturbation tests, post-action trace audits, or other checks against behavior. [Large Language Model Agents are not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v2) is the cautionary example: written or compressed memories can improve measured behavior without being used in the way their designers assume.

[Synapptic](../agent-memory-systems/reviews/synapptic.md) is the clearest reviewed system that treats activation as something to test rather than assume. It extracts behavioral guards from Claude Code sessions, runs WITH/WITHOUT ablations with an LLM judge, records per-model verdicts, and excludes guards marked redundant or harmful before compiling them into assistant-facing memory surfaces. The oracle is still soft, but the test is aimed at the right question: whether the remembered rule changes behavior enough to earn its prompt budget.

Commonplace status: implements always-loaded control-plane context and on-invoke skill loading, but lacks a mature on-situation cue index and behavioral faithfulness tests for activated memory.

## Need 7: Promote Only When Future Value Exceeds Maintenance Cost

Promotion from candidate memory to durable artifacts creates obligations: review, update, invalidation, connection, retirement, and consistency with sources. System-definition promotions add risk because they change behavior. Candidate observations should remain cheaper and less authoritative than library notes, policies, instructions, tests, or scripts until future retrieval or activation value exceeds review and maintenance cost.

An observation inbox can be the lightest candidate stage. Its job is to record a noticed pattern, bug, missing link, possible synthesis, or improvement opportunity before the mechanism is understood. It should be cheap enough to use during unrelated work, but it needs later triage so it does not become a second untrusted library.

Realistic promotion destinations include:

- Knowledge notes, decision records, source reviews, indexes, and negative-result records for material whose value is explanatory.
- Procedures, skills, runbooks, checklists, and instructions for recurring work patterns.
- Schemas, type contracts, review gates, tests, validators, linters, scripts, plugins, runtime extensions, and guardrails when the learned rule is deterministic enough for [codification](./definitions/codification.md) (committing procedure to a symbolic medium).
- Always-loaded policy only when the rule is stable, high-frequency, and cheap enough to spend context on every session.
- Existing domain work surfaces, such as tickets, product configuration, dashboards, CRM records, reports, or documentation, when those are the actual source of authority.

This promotion path is a [constraining](./definitions/constraining.md) (narrowing interpretation space) gradient: prose candidate, curated note, instruction, checklist, test, script, guardrail. Stronger constraints reduce interpretation space and increase reliability, but they also increase brittleness and maintenance cost. [Spec mining is codification's operational mechanism](./spec-mining-as-codification.md) gives the practical loop for moving repeated failures or procedures toward executable checks.

Promotion thresholds should depend on signal type and role. One serious correction may deserve a candidate cue immediately. A preference may require several consistent decisions across sessions. A discovery may need later reuse. Always-loaded or enforced system-definition artifacts should require stronger review than knowledge notes.

The gradient should support relaxation as well as promotion. A rigid check that proves brittle should be demoted to a warning, checklist, or prose guideline rather than left to damage future work. Memory management is partly deciding how much interpretation space a lesson currently deserves.

Commonplace status: supports manual promotion from log entries, notes, and workshops into instructions, skills, type contracts, validators, scripts, and review gates; it lacks a mature candidate queue that scores promotion against future value and maintenance cost.

## Need 8: Keep Memory Roles And Compiled Views From Drifting

Memory systems often create derived surfaces: a note produces a cue, a policy produces a checklist, a convention produces a lint rule, a guide produces an `AGENTS.md` excerpt, or a trace-derived observation produces a generated reminder. These surfaces put knowledge where it can act, but they become dangerous when they turn into independent sources of truth.

The system should distinguish storage forms by memory role and reconstruction cost: durable authored memory, raw evidence, generated navigation views, operational reports, trust ledgers, compiled behavior views, and external authority surfaces. A rebuildable index should not become a policy. A temporal review judgment should not be hidden where staleness checks cannot read it. A ticket, report, dashboard, or source file may remain the true authority even when the memory system keeps a distilled view.

The system needs source-of-truth rules for every behavior-changing derivative. A library-derived cue should be treated as a compiled view, not as a separate policy. It should carry provenance, source version or hash, generation time, owner, and regeneration rules. If the source changes, the cue must regenerate or be marked stale. Direct edits to compiled cues should either flow back to the source or remain candidate-stage material.

This need applies more strongly to system-definition artifacts than to ordinary summaries because drift can change behavior. [Always-loaded context mechanisms in agent harnesses](./always-loaded-context-mechanisms-in-agent-harnesses.md) shows that behavior-shaping context can live in many places: prompts, files, tool descriptions, capabilities, configs, skills, and memory. The more surfaces exist, the more explicit the authority model must be.

The same Synapptic design also provides a concrete compiled-view pattern: the YAML profile is the durable state, while Claude memory, Cursor rules, Copilot instructions, `AGENTS.md`, and other assistant files are render targets with target-specific filtering. That is closer to the right authority model than treating every emitted prompt file as an independent memory.

Commonplace status: distinguishes authored markdown, generated indexes/reports, and review-state ledgers, but compiled behavior-facing views still need more explicit source-of-truth and regeneration rules.

## Need 9: Retire, Redact, Supersede, And Relax Memory

Learning is incomplete without forgetting and revision. Raw traces can contain secrets or obsolete assumptions. Observations can be duplicates, wrong, low-value, or superseded. Cues can grow stale. Policies can become too broad. Tests can fossilize temporary workarounds.

Append-only capture is useful for provenance, but indexes, extracted observations, and activated policy surfaces must support redaction, decay, supersession, retirement, and relaxation.

Realistic methods include:

- Retention classes and redaction status on traces before model extraction.
- Candidate, accepted, superseded, rejected, and retired states on extracted observations.
- Periodic triage for observation inboxes: promote, fold into an existing artifact, keep, reject, or delete.
- Duplicate clustering and source consolidation for repeated observations.
- Recency decay tempered by consequence and recurrence, so old high-impact corrections do not disappear merely because they are old.
- Retirement tests for cues that fire often but do not change behavior or produce too many false positives.
- Relaxation paths from rigid enforcement back to prose guidance when a codified rule proves brittle.

This is the lifecycle side of the same context-efficiency problem. Every stale artifact competes for attention, search rank, review time, or behavioral authority.

Reviewed systems show both partial fulfillment and a common failure mode. cass-memory has candidate/established/proven/deprecated states, harmful-feedback weighting, and decay. REM defines `active`, `contradicted_by`, and `superseded` columns but does not wire them into an actual update path. The distinction is architectural: lifecycle metadata becomes memory management only when some process reads and acts on it.

Commonplace status: implements status fields, validation failures, review staleness, generated-index refresh, workshop closure, and an instruction for evaluating `kb/log.md` entries; retirement, supersession, relaxation, recurrence tracking, and lifecycle scheduling remain developing.

## Need 10: Make Authority Explicit

The memory system must say who or what is allowed to write, promote, activate, enforce, revise, and retire memory. The [comparative review's agency trilemma](../agent-memory-systems/agentic-memory-systems-comparative-review.md) remains decisive: no option combines high agency, high throughput, and high curation quality without trade-offs. Agent-managed memory has task context but spends reasoning budget. External services scale but guess what matters. Humans curate well but slowly. Learned policies need strong oracles.

Authority should vary by risk:

- Automatic systems can capture traces and propose low-authority candidates.
- Extractors can write observations with confidence, source pointers, and candidate status.
- Context engines can activate low-risk cues under explicit budget and ranking rules.
- Human or reviewed-agent workflows should approve durable knowledge artifacts when source interpretation matters.
- High-priority system-definition surfaces, always-loaded instructions, checks, guardrails, and executable policies need the strongest review or behavioral evaluation.
- Retirement and relaxation should be scheduled work, not accidental decay.

This requirement prevents a memory system from silently rewriting the agent's behavior. A system can choose automation, human review, learned policy, or hybrid authority, but the choice is part of the architecture.

Commonplace status: implements authority mostly through explicit files, git review, deterministic validation, and semantic review gates; authority for automatic extraction, promotion, activation, and retirement is not yet fully specified.

## Need 11: Evaluate Memory By Effects, Not By Existence

The system should not count "memory written" as learning. It should evaluate whether memory improved the future task, answer, artifact, or behavior.

Evaluation dimensions include:

- Direct retrieval: can the system answer the question that motivated storage?
- Navigability: can an agent or human follow links and provenance to understand why an answer is trustworthy?
- Contract fitness: does the artifact satisfy the quality goal for its memory role?
- Activation: does relevant policy fire before the action where it matters?
- Behavioral uptake: does the fired memory change the downstream plan, tool use, or artifact in the intended direction?
- Context efficiency: does the memory earn the tokens, latency, and attention it consumes?
- Source alignment: do generated indexes, reminders, rules, and assistant-specific views match their authoritative sources?
- Work-surface fit: does the memory live where the acting agent or human will naturally encounter and maintain it?
- Lifecycle health: are stale, duplicate, low-value, sensitive, or superseded memories retired or demoted?
- Promotion economics: do durable artifacts get reused enough to justify their maintenance burden?

These evaluation dimensions are separable. QA-style retrieval tests can pass while activation fails. A cue can fire while behavior remains unchanged. A note can be accurate but too hard to find. A policy can become harmful after the domain changes.

Commonplace status: implements structural validation and semantic review for artifact quality, but does not yet measure activation, behavioral uptake, context efficiency, source-alignment health, or promotion economics as first-class memory metrics.

## Secondary Nice-To-Haves

The needs above define whether a memory system improves contextual competence. Other properties are not full requirements because a system can be useful without them, but they can make the memory system easier to adopt, cheaper to operate, and harder to strand outside the agent's real work.

- **Native work-environment fit.** Memory should live where agents and humans already act when possible. A file-first system can be inspected, patched, validated, diffed, reviewed, and committed with the same editor, terminal, and git workflows used for code. Commonplace's shipped [architecture](../reference/architecture.md) and [instruction generation](../reference/instruction-generation.md) make this concrete through `AGENTS.md`, `.claude/skills/`, `.agents/skills/`, markdown artifacts, and ordinary commands, which lets Claude Code, Codex, Cursor-like IDE agents, and similar harnesses use the KB through their native discovery and editing surfaces.
- **Cost-model flexibility.** A memory system that rides on the host agent or IDE can use whatever economic model that host already exposes, including subscription-based coding agents where available, instead of requiring every memory lookup, write, or review to consume a separate metered API call. This is an adoption advantage rather than a semantic memory requirement.
- **Portable degradation.** If the specialized agent harness disappears, a markdown-and-git memory system still works in editors, terminals, GitHub, static sites, and ordinary scripts. That makes the memory more durable than a store that can only be queried through one product API.
- **Inspectable generated surfaces.** Generated indexes, reports, and compiled views are easier to trust when they are rebuildable, diffable, and tied to visible source artifacts. This does not replace source-of-truth rules, but it reduces the operational cost of maintaining them.

## Partial Memory Systems Need External Maintenance

Several common designs solve real parts of memory, but leave other requirements to surrounding workflows:

- A vector database can provide retrieval, but artifact contracts, authority, activation, lifecycle, and behavioral evaluation must come from elsewhere.
- A transcript archive can preserve evidence, but usable future context still requires extraction, summarization, promotion, and selective loading.
- A summarizer can compress history, but provenance, uncertainty, scope, and actionability need separate handling.
- An always-loaded profile can activate memory, but ranking, source alignment, and retirement must be maintained outside the profile.
- A self-editing prompt loop can change behavior, but authority, testing, rollback, and source-of-truth rules need external governance.
- A wiki can preserve durable knowledge, but runtime activation, artifact contracts, and behavioral closure need additional machinery.
- A rules engine can enforce behavior, but deciding which lessons deserve enforcement, when rules should relax, and how exceptions are handled remains outside the engine.
- A reusable memory package can give an initial prior, but local truth, local authority, and project-specific lifecycle have to be maintained by the consuming project.

These are real memory systems or memory subsystems. The distinction is that they externalize some of the maintenance burden. A realistic architecture should name which requirements are handled internally and which are delegated to humans, scripts, review processes, host applications, or adjacent systems.

## A Practical Build Order Follows The Needs

The needs do not imply one integrated architecture. They imply a practical build order: start where the signal is strongest, the risk is lowest, and the behavioral test is clearest.

1. Provide a small control-plane memory layer for purpose, scope, routing, quality, commands, and safety.
2. Support direct authoring of notes, decisions, instructions, checks, scripts, plugins, and indexes as the first-order memory operation.
3. Attach artifact contracts so each durable memory says what kind of memory it is, what quality means, and what metadata, provenance, authority, and lifecycle state it needs.
4. Add import paths for existing external knowledge bases, documents, repositories, and source archives.
5. Capture eligible traces with provenance, redaction, access, and retention rules so later meta-learning has evidence.
6. Extract explicit corrections and silent failures as missed memory-creation opportunities before trying to infer discoveries.
7. Test whether correction-derived cues activate in plausible future situations.
8. Test whether activated cues actually change behavior.
9. Add promotion queues for high-confidence candidates whose future value exceeds maintenance cost.
10. Keep generated and compiled views tied to their sources of truth before adding many render targets.
11. Add work-surface and episode support only where retrospective narrative or active state materially improves future tasks.
12. Move repeated, high-confidence lessons toward instructions, checks, scripts, plugins, or guardrails only when authority and evaluation are explicit.

Direct authoring can produce useful memory before trace mining exists at all because it captures understanding when the lesson is already visible. Trace-derived extraction is a meta-learning layer over that path: it looks for useful memory that should have been created but was not. The failure tests are sequential: can correction extraction produce useful candidates, can those candidates activate, and do activated cues change behavior? If not, more trace processing only makes the system more elaborate. The memory system should grow from validated usefulness, not from an attractive taxonomy.

## What Remains Open

The hardest open problem is structural pattern detection across sessions. Many important lessons do not share keywords: stale pricing tables, outdated runbooks, and deprecated templates can all be instances of "derived artifacts drift from sources of truth." Recognizing that causal structure requires deeper analysis than ordinary search.

Discovery extraction also remains weak. Corrections and failures have visible signals; discoveries often have only surprise, elaboration, or later reuse. The realistic stance is to surface discovery candidates, not automatically graduate them.

The boundary between learned memory and work-surface authority is domain-dependent. Software projects have tests, linters, code review, issue trackers, and deployment gates. Other domains may lack those surfaces or have different authorities. A memory design must first name the domain's observable traces, recurring tasks, durable work surfaces, evaluable outcomes, and authority to modify behavior.

Finally, learned memory-management policy is attractive but oracle-dependent. Where the domain has clear success metrics, a learned policy may outperform inspectable heuristics. In open-ended knowledge work, reviewable rules, provenance, and behavioral tests remain the safer default. Memory management sits on the same [bitter-lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md): relax into learned policy where feedback is good, and keep artifact-side control where feedback is weak.

---

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: context scarcity, not storage scarcity, is the reason memory design must focus on selective loading and framing
- [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](./an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) — grounds: useful memory should improve future action by being findable, usable with other knowledge, and reliable enough to act on
- [Agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — grounds: locates capture, activation, scheduling, and promotion in different runtime responsibilities
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — grounds: memory decomposes into storage, context-engine activation, and learning rather than one pluggable subsystem
- [Distillation is transformation, not selection](./distillation-is-transformation-not-selection.md) — grounds: trace-to-observation, trace-to-policy, trace-to-note, and trace-to-check moves are transformations into consumer-specific artifact shapes
- [Session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — grounds: retaining traces and loading next-call context are separate design decisions
- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — grounds: control-plane memory should stay compact because always-loaded context has a higher budget burden
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — grounds: memory-mediated behavior change should happen through durable system-definition artifacts updated across sessions
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — grounds: memory artifacts need different contracts because knowledge-role and system-definition-role artifacts are evaluated by different effects
- [Scheduler-LLM separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: bookkeeping and deterministic state tracking should migrate to symbolic substrates when possible
- [Treat continual learning as substrate coevolution](./treat-continual-learning-as-substrate-coevolution.md) — grounds: memory-mediated behavior change spans prose, symbolic, and opaque substrates rather than one learning surface
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — grounds: trace-derived meta-learning should use scalable search and learning where oracles are strong while keeping weak-oracle updates in reviewable artifacts
- [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — grounds: extraction is easier than deciding which candidate memory deserves durable promotion
- [Automated synthesis is missing good oracles](./automated-synthesis-is-missing-good-oracles.md) — grounds: discovery extraction and cross-session synthesis need stronger success tests than "the artifact was generated"
- [Oracle strength spectrum](./oracle-strength-spectrum.md) — grounds: correction, silent-failure, preference, procedure, decision, and discovery extraction differ by signal quality
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — grounds: prose and symbolic artifacts are the practical substrate for behavior-changing memory
- [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md) — grounds: procedural memory artifacts are pre-compiled reasoning that changes future action under bounded context
- [Specification strategy should follow where understanding lives](./specification-strategy-should-follow-where-understanding-lives.md) — mechanism: direct memory creation and trace-derived meta-learning differ by when understanding becomes available
- [Capability placement should follow autonomy readiness](./capability-placement-should-follow-autonomy-readiness.md) — mechanism: promotion destinations should match how safely the learned capability can execute without human steering
- [Always-loaded context mechanisms in agent harnesses](./always-loaded-context-mechanisms-in-agent-harnesses.md) — mechanism: behavior-shaping memory can live in prompts, files, capabilities, configuration, skills, and generated context surfaces
- [Distilled artifacts need source tracking at the source](./distilled-artifacts-need-source-tracking-at-the-source.md) — mechanism: compiled memory surfaces need provenance and regeneration rules so they do not drift from source authority
- [Commonplace architecture](../reference/architecture.md) — see-also: file-first project layout, shipped library boundary, user collections, and promoted skill discovery surfaces
- [Instruction generation](../reference/instruction-generation.md) — see-also: `commonplace-init`, generated control-plane files, and multi-harness skill promotion
- [Quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — extends: weak composite signals may help evaluate memory lifecycle, promotion, and maintenance when perfect usage oracles are unavailable
- [Spec mining is codification's operational mechanism](./spec-mining-as-codification.md) — mechanism: repeated failures and procedures can harden into tests, scripts, validators, or guardrails
- [A functioning KB needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — grounds: active work-in-motion artifacts satisfy a different need than retrospective memory or durable library artifacts
- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) — contrasts: warns against accepting memory-space taxonomies before identifying the operational needs they serve
- [Flat memory predicts specific cross-contamination failures that are empirically testable](./flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md) — extends: candidate status, lifecycle state, and promotion economics reduce search and activation pollution
- [Silent disambiguation is the semantic analogue of tool fallback](./silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — extends: fallback and silent repair should become memory candidates when final success hides degraded guarantees
- [Enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — extends: system-definition memory should include recovery, reporting, and relaxation paths, not only prohibitions
- [Trace-derived learning techniques in related systems](../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) — evidence: surveyed systems already mine traces into preferences, tips, rules, skills, playbooks, and policy updates
- [Trajectory-informed Memory Generation for Self-improving Agents](https://arxiv.org/html/2603.10600v1) — evidence: trajectory-to-tip learning supports trace-derived future-context artifacts while leaving lifecycle and retirement underdeveloped
- [Large Language Model Agents are not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v2) — evidence: written memory must be evaluated for behavioral influence rather than assumed to work because it is present
- [Meta-Harness: End-to-End Optimization of Model-Harnesses](https://yoonholee.com/meta-harness/paper.pdf) — evidence: raw execution traces and explicit oracles can support later optimization better than premature summaries
