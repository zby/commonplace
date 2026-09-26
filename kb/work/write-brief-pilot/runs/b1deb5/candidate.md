---
description: Design study of an ideal agent memory system under store-everything premise — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction pipeline
type: types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
status: current
---

# Designing a Memory System for LLM-Based Agents

## The core insight: storage is cheap, context is scarce

The dominant design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Storage is cheap: disk costs little, text compresses well, and append-only logs need no schema design. The binding constraint is *context* -- the finite window of tokens an agent can attend to during one inference call. Context is the only channel through which the agent receives instructions, accesses knowledge, and reasons toward action. Everything competes for that space, and the space degrades before it fills: more material can dilute instructions, contaminate scopes, and distort interpretation below the token limit.

This inverts the usual design. Traditional systems optimize storage and treat retrieval as a lookup. An agent memory system should store aggressively -- all session logs, intermediate artifacts, and observations -- and put the design effort into deciding which fraction of the store enters the context for a given task.

"Store everything" is a bet, not an axiom. It trades storage cost for indexing overhead, search pollution risk, and privacy exposure, and it wins only if selective retrieval can manage what aggressive storage introduces. Its main effect is to move the hard problem to where it belongs: the scarce resource is attention, not disk.

## Memory plays two roles

The [axes of artifact analysis](./axes-of-artifact-analysis.md) names a **role** axis: an artifact is consumed either in a **knowledge role** (as fact; durable writes grow the agent's reach) or in a **system-definition role** (as policy; durable writes change the agent's disposition). The role is relational, not structural. A note saying "we use URL-path versioning" is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the agent's next API design.

The two roles need different machinery:

- **Knowledge retrieval** answers questions posed at consumption time. It fits search and navigation: start with a question, follow links. Standard RAG optimizes for this. Failure mode: nobody asks the question.
- **System-definition activation** injects policy when a matching situation occurs. It fits triggered activation: watch the agent's proposed action for cues and surface the constraint before commitment. This is the territory of the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md). Failure mode: relevant policy is stored but never fires.

Most agent-memory systems optimize for knowledge-role retrieval and underserve the system-definition role, which is where [continual learning's harder problem lies](./continual-learning-requires-governing-behaviour-changing-writes.md). "Adding RAG is learning" holds for the knowledge role and is empty for the system-definition role.

Session logs are the common substrate. One correction in session 47 can yield both a knowledge artifact (an ADR answering "why do we use approach B?") and a system-definition artifact (a cue that fires when a later session proposes approach A). The extraction pipeline must produce both, and retrieval must serve both consumption patterns.

## Why existing approaches fall short

A comparison of eleven agent memory systems -- from vector-first fact stores (Mem0) through knowledge graphs (Graphiti) to filesystem-first curated systems (Ars Contexta, commonplace) -- shows three structural problems that no current system fully solves.

**The agency trilemma.** Who decides what to remember? If the agent manages its own memory (Letta), it has full context but spends reasoning tokens on housekeeping. If an external service manages it (Mem0, Graphiti, Cognee), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-manage it (commonplace, Ars Contexta), curation quality is highest and throughput lowest. AgeMem trains the memory policy with reinforcement learning, which needs a task-completion oracle that open-ended domains may lack and yields an opaque policy. No system combines high agency, high throughput, and high curation quality.

**Search versus navigation.** Mem0, Graphiti, and Cognee treat knowledge as something to *search*: embed a query, return the top-k. Ars Contexta and commonplace treat it as something to *navigate*: follow links with articulated relationships. Search-first systems score well on QA benchmarks, but QA accuracy does not measure whether the agent can follow a chain of decisions or trace a correction back to the episodes that established it. Both patterns serve the knowledge role. Neither serves the system-definition role, which needs a third pattern, triggered activation. That is one reason no reviewed system closes the activation gap.

**Everyone automates extraction; nobody automates synthesis.** Every system can extract structured knowledge from unstructured input. Almost none can synthesize across existing knowledge: produce new insights, recognize when two threads should merge, or reformulate entries for clarity. Store-everything has a structural advantage here: with complete logs retained, synthesis can be attempted retrospectively and rerun as techniques improve.

## Architecture: four layers of progressive distillation

A store-everything system without structure is a haystack. The architecture has four layers, each more distilled than the one below:

**Layer 1: Trace.** Complete session logs -- every interaction, tool call, model output, and user message -- as append-only records with timestamps and session identifiers. Traces are the ground truth from which every higher layer derives. They answer "what exactly happened in session X?" and nothing else efficiently. They serve provenance and offline extraction; the agent never loads raw traces into a working context.

**Layer 2: Observation.** Extracted atomic facts: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each observation is typed, timestamped, linked to its source session, scored for confidence and importance, and **tagged with its role**. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). Others yield paired artifacts: a decision produces a knowledge record for "why we chose A" and a cue for "if B is proposed, surface the reasoning for A." Because observations are derived from retained traces rather than extracted at interaction time (as in ClawVault's scored observations), capture speed is decoupled from extraction quality: extraction can be rerun, improved, and backfilled.

**Layer 3: Episode.** Compressed accounts of bounded work units that may span several sessions: goal, scope (session range and period), outcome, key decisions with pointers to observations, lessons, open threads, and library artifacts produced. Observations answer "have we seen this before?" (lookup). Episodes answer "have we tried something like this, and what happened?" (narrative).

**Layer 4: Library.** Curated notes, structured claims, indexes, procedures, and ADRs. The design does not change the library; it gives it richer inputs and a principled path from raw experience to curated knowledge.

### Why four layers

With only traces and library, every transition from raw log to note needs a human to read the trace and write the note -- the manual bottleneck the system exists to remove. With a single intermediate layer, that layer must serve both atomic lookup and narrative queries. A correction is a trigger-lesson pair; an episode is a compressed story. They need different indexing, extraction, and promotion, so they are different kinds of objects, though they can share storage distinguished by type tags. A fifth layer (say, splitting the library into working and reference knowledge) adds a boundary that inhibits links; the library's types, status fields, and semantic links already handle internal differentiation.

The layers also give the context scheduler progressive disclosure. First scan observation summaries and episode goals, which are compact. Load the full episode or observation cluster only if relevant. Follow the pointer to the trace only if provenance is needed.

### How material moves between layers

The promotion pathways matter more than the layers themselves.

- **Trace to observation (extraction).** Runs automatically at session end, and again over old traces when the extractor improves. An LLM extracts typed observations with confidence, importance, and a source pointer. Failure modes: over-extraction (trivia drowns the layer), under-extraction (subtle preferences missed), and misclassification (a correction tagged as a preference loses its corrective force). Fully reversible, because traces are kept.
- **Observation to episode (compression).** Triggered by work-unit completion, periodic consolidation, or request. Harder than extraction because the LLM must judge what mattered. Boundary heuristics: shared file paths, shared task references, temporal proximity, topic similarity, and explicit markers ("starting work on X" / "done with X") when present.
- **Observation to library (promotion).** Triggered by recurrence, an importance threshold, or request. Thresholds vary by type: a preference may need three or more independent sessions to be stable, while a high-stakes architectural decision may warrant immediate promotion to an ADR.
- **Episode to library (distillation).** Usually deliberate. The episode gives a reviewer the full narrative against which to check that the distilled claim is faithful.
- **Library to observation (backflow).** Library notes should generate activation cues. A note saying "prefer staging specific files over `git add -A`" should produce a cue that fires when a session involves git staging. Without backflow, library knowledge is stored but inert.

### Lifecycle and role are orthogonal tags

Artifacts expire at different rates. Operational observations churn fast (yesterday's debugging procedure may be superseded today). Self-observations change slowly (a preference seen across five sessions is likely stable). Knowledge observations accumulate. Rather than separate stores, which inhibit cross-links, the architecture tags each observation by lifecycle and uses the tag in promotion: recurring knowledge promotes to a library note, recurring operational observations to a procedure, recurring self-observations to CLAUDE.md.

The role tag is independent of the lifecycle tag. Lifecycle answers *when does this expire?*; role answers *how is this consumed?* Retrieval uses lifecycle to weight recency and role to select the activation mechanism.

## Retrieval and activation

The hardest problem is activation: a system can store relevant knowledge, produce it on direct query, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query.

### Two pipelines over one store

The central design move is two retrieval pipelines sharing one store.

**Knowledge-role retrieval** serves questions such as "why did we do X?" The interface is navigable: embedding search over descriptions as a first-pass filter, then articulated library links. Its failure mode, the question never being asked, is an elicitation problem outside this pipeline.

**System-definition activation** serves the agent's in-flight work. The interface is a watcher, not a query: cues are indexed by action signature, preference domain, or situation template and fire when the proposed action matches. Its failure mode, the cue not firing when it applies, is the activation gap proper, and most of the design surface lives here.

The pipelines cross-reference each other. A fired cue can point into the knowledge layer ("this correction belongs to a documented convention, see ADR 014"), and navigation can reveal cues attached to a note. The mechanisms stay separate.

### Three stages of activation failure

- **Cue match.** The task context must carry enough signal to trigger retrieval. Embedding similarity handles topical matches but fails on causal ones: session 47's correction about a deployment mistake will not embed near session 312's code-writing task, even when the lesson applies.
- **Priority arbitration.** In a store with thousands of sessions, any task matches dozens of items, and loading all of them destroys context efficiency.
- **Commitment.** Even loaded knowledge may be ignored in favor of training-time defaults. The agent answers what is asked but does not raise concerns nobody asked about.

### Typed cue indexes

Typed cue indexes are the main mechanism for cue match. Instead of searching raw logs at retrieval time, the system extracts typed cues at ingestion time, each with its own retrieval signature. A **correction cue** matches the action the agent is about to take:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches the decision space, a **precedent cue** the situation description, a **procedure cue** the goal. This is what bridges session 47 to session 312: when the agent's plan includes dropping a column, the trigger matches and the lesson loads before the migration is written.

Matching is the hard part: "database migration that removes a column" must match "drop column deprecated_flag." Three approaches compose: action-type classification (both classify as `schema-migration:column-removal`), embedding similarity with a low threshold (prefer false positives to false negatives), and LLM-judged relevance for high-consequence cues.

### Priority arbitration

When too many cues match, four mechanisms decide what to surface:

- *Recency weighting with a long tail* -- an old correction still matters if the mistake pattern recurs.
- *Consequence weighting* -- sessions with corrections, user frustration, or rework rank higher. The log supplies the signals: message count after a correction, sentiment markers, explicit severity statements.
- *Frequency* -- a cue that fires across many sessions is more likely to matter.
- *Budget allocation by type* -- reserve fixed context slots for corrections, active preferences, and precedents, so no cue type crowds out the others.

### Commitment

- *Imperative framing.* Surface corrections as instructions, not history: "BEFORE doing X, verify Y because Z failed in session 47," not "previously, X failed because Y."
- *Checkpoint insertion.* For high-consequence cues, add a verification step to the task plan.
- *Contradiction surfacing.* When the proposed action contradicts a stored correction or preference, say so explicitly and name the established alternative.

### How the access patterns compose

Search runs over the lower layers, whose items are numerous and weakly structured. Navigation runs over the upper layers, whose items are fewer and richly linked. Activation runs over cues in any layer, because its trigger is the proposed action rather than a query. For an agent about to write a database migration:

1. **Activation** fires matching cues: corrections load as imperative instructions, preferences take their reserved budget, procedures suggest a checklist.
2. **Search** over extracted items surfaces related knowledge-role records: past migration decisions, negative results, draft ADRs.
3. **Navigation** follows their links into the library to assemble the architectural context.

No raw trace is loaded.

## Learning from session logs

Session logs contain four signal types. They differ in oracle clarity, extraction difficulty, and role. Corrections, preferences, and procedures are system-definition. Decision provenance and negative results are knowledge. Discoveries start as knowledge candidates and may graduate into either role. From easiest to hardest:

**Corrections (system-definition).** The user says "no, do X instead" or rejects a tool call. The log holds the wrong output, the rejection, and the corrected direction -- an explicit negative signal paired with a positive one, the clearest oracle in the system. Pi Self-Learning's schema targets exactly this: `{"mistakes": [...], "fixes": [...]}`. A correction seen in two sessions is not a fluke, so the promotion threshold can be two. The graduated artifact moves along the codification gradient within the same role: a CLAUDE.md rule or style-guide convention (prose), then a lint check or validation script (symbolic). A companion note or ADR may explain the reason, but the primary artifact steers behavior. Example: the user corrects alphabetical import sorting to stdlib / third-party / local grouping; on the second occurrence it becomes a documented preference, on the third the question is whether it should be a pre-commit hook.

**Preferences (system-definition).** The user accepts some patterns and rejects others without stating a rule. Each accept/reject is clear, but the rule connecting them must be inferred across sessions. Detection runs bottom-up (cluster decisions by domain, find features that predict acceptance) or top-down (ask an LLM which preferences explain the last 50 decisions in a domain). A reasonable threshold: five or more decisions across three or more sessions with over 80% consistency.

**Procedures (system-definition).** The same workflow recurs with variations. Tool-call sequences are more reliable signals than natural-language descriptions: if four sessions contain `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]`, the pattern is detectable despite different surrounding conversation. The artifact graduates from instruction document (human judgment needed) to skill (parameterizable) to script (fully deterministic). The role stays constant; the constraint tightens.

**Discoveries (knowledge, sometimes system-definition).** An insight emerges: a connection, a principle, a unifying abstraction. These are the highest-value extractions and the hardest to detect, because a discovery is a one-off event with no verifiable signal. Detection heuristics are weak: explicit markers ("write this down"), claims linking previously unlinked notes, unusual elaboration depth, and later reference. Discoveries should enter as low-confidence candidates and promote by reference frequency. Role is assigned at graduation, because operational implications appear only with use: a discovery about async resource-pool failures may later gain a cue that fires on async cleanup code.

### The promotion pipeline

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. First, extraction should be narrow and schema-constrained: one prompt per signal type, each asking for its schema, rather than "summarize the session." Second, the candidate store must be separate from the library. Mixing unvetted candidates with curated knowledge degrades retrieval precision for everything.

### Session logs as composite oracle

Most memory systems lack a signal for "was this memory operation good?" Session logs offer many weak ones: corrections, accept/reject patterns, explicit markers ("this is important"), questions asked, elaboration investment, whether the session goal was reached, return to a topic in a later session, and abandoned investigations. Reviewed systems each use few: Pi Self-Learning uses only corrections, ClawVault importance plus recurrence, cass-memory helpful/harmful feedback plus score decay. The bet is that combining many weak signals yields a usable soft oracle without waiting for a strong one.

## Knowledge-role use cases

**Decision provenance.** The recurring high-value question is *why did we do it this way and not that way?* ADRs answer it, but they are written after the fact and cover only what the author thought to record. Session logs hold the deliberation itself: alternatives, reasoning, active constraints, objections. This enables a semi-automated ADR pipeline: flag sessions where a decision was debated, pre-assemble a draft ADR, and have a human verify it. The "alternatives considered" section, the costliest to reconstruct from memory, is what logs preserve most directly. A drafted ADR often gets a system-definition companion: a cue that fires when the agent re-proposes a rejected alternative.

**Negative results.** What was tried and abandoned has no home in standard project structure; code shows what was built, not what was discarded. Negative results are stored as records (approach, failure reason, source session, the decision that followed) indexed by approach name, so "why didn't we do X?" finds them. A severe one also yields a cue keyed on the approach, so the attempt is prevented rather than merely explained.

## Where memory ends and the project begins

The naive boundary -- "memory stores what project artifacts don't preserve" -- is necessary but not sufficient. Project artifacts themselves spread across the class/role grid: code, tests, and lint rules are symbolic system-definition; documentation and ADRs are prose knowledge; CLAUDE.md is prose system-definition. Against each, memory adds the reasoning and process behind the artifact: code says "retry with exponential backoff," memory adds "a circuit breaker interacted badly with the connection pool in session 47."

**CLAUDE.md is compiled system-definition; the memory system is its source.** A correction repeated three times lives in session logs and graduates to a CLAUDE.md entry, or further to a lint rule (same role, tighter constraint). More generally, **the memory system is the substrate from which project artifacts are distilled**, not a parallel store. Two things blur the boundary. In the *overlap zone*, artifacts such as ADRs, bug-driven tests, or `// Retries capped at 3 -- see incident #412` record a conclusion without its deliberation; memory holds the surrounding context rather than duplicating them. In the *aspiration gap*, undocumented conventions and implicit invariants belong in project artifacts but were never written; memory captures them by default until they are.

### Graduation pathways

The destination depends on what was learned and which role the artifact will play:

| Pattern | Graduation trigger | Destination | Role |
|---|---|---|---|
| Decision debated across sessions | "Why did we decide X?" is expensive to answer | ADR linking back to source sessions | Knowledge |
| Decision with a commonly-proposed reject alternative | Agent re-proposed rejected option | Cue keyed on the rejected alternative | System-definition |
| Same workflow in 3+ sessions | Repetition detection | Documented procedure, skill, or script | System-definition |
| Same mistake corrected 2+ times | Correction frequency | Convention, CLAUDE.md entry, or lint rule | System-definition |
| Same mistake, with instructive rationale | The reasoning for the correction is worth preserving | Companion note or ADR | Knowledge |
| Agent needs same orientation each session | Recurring first-message pattern | CLAUDE.md entry | System-definition |
| Context needed to understand specific code | Explanation given during session | Code comment | Knowledge (usually) |
| Negative result: tried and abandoned | Approach explored and rejected | Negative-result record + "why not X?" index entry | Knowledge |

Recognition is the bottleneck. Clear triggers (correction frequency, repetition count) can be automated; judgment calls (is this decision load-bearing enough for an ADR?) can only be flagged.

Every graduated artifact creates a maintenance obligation: an ADR must stay current, a lint rule must change with conventions. Session logs are append-only and carry no such obligation. Premature graduation is therefore worse than late graduation: graduate when retrieval cost exceeds maintenance cost.

### Reach decides graduation

High-reach knowledge -- an insight that applies across many contexts -- belongs in the library; low-reach knowledge ("the bug in PR #247 was a race in the connection pool") can stay in the logs. Reach is judged differently per role. A knowledge artifact earns promotion when its claim applies widely. A system-definition artifact earns it when its trigger fires accurately and often enough in the situations it covers to justify its context budget; a narrow, accurate cue beats a broad one that misfires. Graduating a correction into CLAUDE.md makes it fire in every session, which also multiplies the cost of its being wrong.

Reach is often unknown when an observation is first made. The pool race might be a one-off or the third instance of a pattern about shutdown ordering in async resource pools. Reach is revealed when low-reach observations cluster around a shared structure. Hence the two-phase policy: accumulate everything, then graduate on revealed reach.

## Alternatives rejected

- **Three layers** (observation and episode merged into one indexed layer): rejected because atomic lookup and narrative retrieval need different indexing; they may share storage.
- **One unified retrieval pipeline** for both roles: rejected because a question-asker navigates from a query, while an acting agent needs policy injected without asking.
- **Extraction at session end only, no backfill**: rejected because it couples capture speed to extraction quality and forfeits the main advantage of retaining traces.
- **Binary memory/project split** routing each artifact to one store: rejected because the boundary follows the class/role grid, not artifact kind.

## Open questions

**Inspectable versus learned retrieval policy.** Inspectable rules are debuggable and incrementally refinable but brittle across domains. Learned policies (such as AgeMem's) adapt but are opaque and need an oracle. The likely answer is inspectable heuristics by default with learned overrides where volume allows. When an override should supersede a rule, and how to detect drift from the heuristic baseline, is unsolved.

**Cross-session structural patterns.** Three incidents -- a deploy failing on stale staging config, a migration failing on stale test config, a flag rollout breaking on out-of-sync production config -- share no keywords but reveal one high-reach pattern: configuration lacks a single source of truth. Detecting shared causal structure needs deep reasoning whose value is speculative. It may require periodic (weekly or monthly) deep-analysis passes over accumulated observations. No current system does this.

**The oracle problem for discoveries.** Corrections have an explicit oracle, preferences a statistical one, procedures a structural one. Discoveries have none except later use, which comes too late to guide extraction. Discovery recognition may stay semi-manual; build the easier extraction types first and accumulate volume before testing discovery heuristics.

**The ephemeral computation trap.** If candidates never promote, the system appears to learn without learning. A candidate store that is never reviewed is ephemerality with extra steps. The promotion filter must run and someone must review its output. This is an operational problem, not a technical one, and the most likely failure in practice.

**Scale.** The design targets one user and one project: hundreds to low thousands of sessions, tens of thousands of observations, hundreds of episodes, one curator. Teams (conflicting preferences, concurrent streams) and very long-lived projects are untested. Progressive disclosure should scale further than flat search, but cross-session pattern detection grows combinatorially harder with session count.

## A practical starting point

A system does not need all four layers on day one. The difficulty gradient suggests a build order:

1. **Session logging.** Capture complete traces. Cheap, needs no extraction, and creates the substrate for everything else.
2. **Correction extraction.** Easiest type, strongest oracle. Run a schema-constrained pass at session end, store corrections as typed cues with triggers, and surface them before the agent repeats a mistake.
3. **Preference and procedure extraction.** Once roughly 50+ sessions accumulate, run periodic passes for accept/reject patterns and recurring tool-call sequences.
4. **Episode layer.** As work units become identifiable, compress multi-session efforts into episodes to answer "have we tried this before?"
5. **Promotion pipeline.** Connect the candidate store to the library, starting with high-confidence, high-frequency promotions (a correction seen three times becomes a convention).

Each step is independently valuable: logging alone beats no memory, and correction extraction alone removes repeated mistakes.
