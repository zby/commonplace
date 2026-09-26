---
description: Design study of an ideal agent memory system under store-everything premise — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction pipeline
type: types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
status: current
---

# Designing a Memory System for LLM-Based Agents

This design study targets one LLM-based agent working on one software project, at single-user scale: hundreds to low thousands of sessions. Every threshold below ("two occurrences", "five decisions across three sessions", "50+ sessions") is a proposed heuristic, not a measured result. Nothing here has been built or validated.

## The core insight: storage is cheap, context is scarce

The dominant design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Storage is cheap: disk costs little, text compresses well, and append-only logs need no schema design. The binding constraint is *context*, the finite window of tokens an agent attends to during one inference call. Context is the only channel through which the agent receives instructions and knowledge. Everything competes for the same space, and the space degrades softly well before it fills: more material can dilute instructions, contaminate scopes, and distort interpretation before the token limit is reached. Selection is therefore the binding problem.

This inverts the traditional design. Traditional systems optimize storage and treat retrieval as a lookup. An agent memory system should store aggressively and put its design intelligence into retrieval and activation. **Activation** here means surfacing stored material into context at the moment of need, as distinct from retrieval under a direct query.

"Store everything" is a bet, not an axiom. It trades storage cost for indexing overhead, search pollution, and privacy exposure. The bet is that selective retrieval can manage those costs. The rest of the design follows from the inversion: two consumption roles need two retrieval pipelines, unusable raw traces need intermediate distillation layers, and retained traces let extraction be rerun and synthesis attempted retrospectively.

## Memory plays two roles

The [axes of artifact analysis](./axes-of-artifact-analysis.md) names a **role** axis. An artifact is consumed either in a **knowledge role** (as fact; durable writes grow what the agent can answer) or in a **system-definition role** (as policy; durable writes change what the agent does). The role is relational, not structural. A note saying "we use URL-path versioning" plays the knowledge role when retrieved to answer "how do we version APIs?" and the system-definition role when loaded to steer the agent's next API design.

The two roles fail differently:

- **Knowledge retrieval** answers questions posed at consumption time. Failure mode: *the question is never asked.*
- **System-definition activation** injects policy when a matching situation occurs. Failure mode: *the policy is stored but never fires.* This is the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md).

Most agent memory systems serve only the knowledge role (RAG over stored facts). That leaves the half of continual learning that [changes behaviour](./continual-learning-requires-governing-behaviour-changing-writes.md) unserved. "Adding RAG is learning" is true for the knowledge role and empty for behavior.

Session logs feed both roles. A single correction in session 47 can yield a knowledge artifact (an ADR answering "why do we use approach B?") and a system-definition artifact (a cue that fires when a future session proposes approach A).

## Why existing approaches fall short

A comparative review of eleven agent memory systems finds three structural problems that no system fully solves. The systems named below illustrate positions; they are not ranked.

**The agency trilemma: who decides what to remember?** If the agent manages its own memory (Letta's position), it has full context but spends reasoning tokens on housekeeping. If an external service manages it (Mem0, Graphiti), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-manage it (Commonplace, Ars Contexta), curation quality is highest but throughput is lowest. Training the memory policy with reinforcement learning (AgeMem) needs a task-completion oracle that open-ended domains may lack, and the learned policy is opaque. No system combines high agency, high throughput, and high curation quality.

**Navigability versus search.** Search-first systems embed a query and return the top-k results; they score well on QA benchmarks. Navigation-first systems follow links with articulated relationships, which lets an agent trace a chain of decisions. QA accuracy does not measure whether the structure supports that reasoning. A memory system needs both. The system-definition role needs a third pattern, triggered activation, which neither search nor navigation provides and which QA benchmarks do not test.

**Everyone automates extraction; nobody automates synthesis.** Systems extract structured records from unstructured input. Almost none synthesize across existing knowledge: merging threads, reformulating entries, producing new insight. Retained traces give a store-everything design a structural advantage here, because synthesis can be attempted retrospectively and rerun when techniques improve.

## Architecture: four layers of progressive distillation

**Layer 1: Trace.** Complete, append-only session logs: every message, tool call, and model output, with timestamps and session identifiers. Traces answer "what exactly happened in session X?" and serve provenance and offline extraction. The agent never loads raw traces into a working context.

**Layer 2: Observation.** Extracted atomic records: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each is typed, timestamped, linked to its source session, scored for confidence and importance, and **tagged with its role**. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). For ambiguous types the extractor produces paired artifacts: a decision yields a knowledge record for "why we chose A" and a cue for "if B is proposed, surface the reasoning for A". Observations answer "have we seen this before?" Because they are derived from retained traces rather than captured at interaction time, capture speed is decoupled from extraction quality.

**Layer 3: Episode.** Narrative accounts of bounded work units that may span sessions: goal, session range, outcome, key decisions (pointing to observations), lessons, open threads, and library artifacts produced. Episodes answer "have we tried something like this before, and what happened?"

**Layer 4: Library.** Curated notes, claims, indexes, procedures, and ADRs. The design leaves the library unchanged; it feeds it through principled pathways from raw experience.

### Why four layers

Two layers (trace and library) leave every transition to a human who reads the trace and writes the note. That is the manual bottleneck the memory system exists to remove. Three layers force one intermediate layer to serve atomic lookup ("has this correction been given before?") and narrative retrieval ("what happened when we tried this?"). These need different indexing, extraction, and promotion, even if both share one storage backend distinguished by type tags. A fifth layer, such as splitting the library into working and reference knowledge, adds a boundary that inhibits connections; frontmatter types, status fields, and links already differentiate within the library.

The layers also give the context scheduler a progressive-disclosure strategy. First scan observation summaries and episode goals, which are compact. Then load the full episode or observation cluster if relevant. Follow the pointer to the trace only when provenance is needed.

### Promotion pathways

**Trace to observation (extraction).** Runs automatically after each session, and again over old traces when the extractor improves. Failure modes: over-extraction (noise), under-extraction (missed subtle preferences), and type misclassification (a correction tagged as a preference loses its corrective force). Reversible, because traces are retained.

**Observation to episode (compression).** Triggered by work-unit completion, periodic consolidation, or request. Harder than extraction because it requires editorial judgment about what mattered. Boundary heuristics: shared file paths and task references, temporal proximity, topic similarity, and explicit "starting X" / "done with X" markers.

**Observation to library (promotion).** Triggered by recurrence, importance, or request. Thresholds vary by type: a preference may need three or more independent sessions, while one high-stakes architectural decision may warrant immediate promotion.

**Episode to library (distillation).** Usually deliberate. One episode may yield several artifacts, and the episode gives a reviewer the full narrative against which to check the distilled claim.

**Library to observation (backflow).** Library notes generate activation cues in the observation layer. A note saying "stage specific files, not `git add -A`" should produce a cue that fires when a session involves git staging. Without backflow, library knowledge sits inert.

### Lifecycle and role: orthogonal tags on one store

Observations also carry a lifecycle tag. Operational observations churn fast, self-observations (stable preferences) change slowly, and knowledge observations accumulate. Separate stores would inhibit cross-connections, so the design tags one store instead. The tags set different promotion targets and thresholds: a recurring knowledge observation becomes a library note, a recurring operational one a procedure, a recurring self-observation a CLAUDE.md entry.

Role is orthogonal to lifecycle. A debugging procedure is usually system-definition but is knowledge when someone asks "how do we debug this class of bug?" Lifecycle answers *when does this expire?*; role answers *how is this consumed?* Retrieval uses lifecycle to weight recency and role to select the mechanism.

## Retrieval and activation

A system can store relevant knowledge, reproduce it on demand, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query.

### Retrieval splits by role

The central design move is two pipelines over one store.

**Knowledge retrieval** serves questions such as "why did we do X?" The interface is navigable: embedding search over descriptions as a first-pass filter, then the library's links. Its failure mode, the unasked question, is an elicitation problem that this pipeline can assist but not solve.

**System-definition activation** serves the agent's in-flight work. The interface is a watcher, not a query. Cues are indexed by action signature, preference domain, or situation template, and fire when the agent's proposed action matches.

The pipelines cross-reference each other. A fired cue can point into the knowledge layer ("this correction is part of ADR 014"). Navigating the knowledge layer can surface a dormant cue ("this note has an active correction attached").

### Three stages of activation failure

**Cue match.** The task context must carry enough signal to trigger retrieval. Embeddings handle topical connections but miss causal ones: a session-47 correction about a deployment mistake will not embed near a session-312 coding task to which the lesson applies.

**Priority arbitration.** In a store with thousands of sessions, any task matches dozens of items, and loading them all wastes context.

**Commitment.** Even with the right material loaded, the agent may fall back on training-time defaults. It behaves like an expert witness: it answers what is asked accurately but does not raise concerns the questioner has not thought of.

### Typed cue indexes

Typed cues are system-definition artifacts extracted at ingestion time, so retrieval never searches raw logs. Each type matches against something different. A **correction cue** matches the action about to be taken, a **preference cue** the decision space, a **precedent cue** the situation description, and a **procedure cue** the goal. An illustrative correction cue:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

This is the session-47-to-session-312 bridge. In session 47 the user corrects the agent's migration approach, and the correction becomes a cue with a trigger. In session 312 the agent's plan includes dropping a column, the trigger matches, and the lesson loads before the migration is written.

Matching is the hard part: "database migration that removes a column" must match "drop column deprecated_flag". Three approaches compose. Action-type classification maps both to `schema-migration:column-removal`. Embedding similarity with a low threshold accepts false positives to avoid false negatives. LLM-judged relevance is reserved for high-consequence cues because it is expensive.

### Arbitration and commitment

When too many cues match, four mechanisms decide what surfaces:

- *Recency weighting* with a long tail, since an old correction still matters if the mistake recurs.
- *Consequence weighting*, favoring sessions with corrections, frustration, or rework. The log supplies the signals: messages needed after a correction, sentiment markers, stated severity.
- *Frequency*: a cue that fires across many sessions is more likely to matter.
- *Per-type budgets*: fixed context slots for corrections, preferences, and precedents, so no cue type crowds out the others.

Three mechanisms address commitment:

- *Imperative framing*: "BEFORE doing X, verify Y because Z failed in session 47", not "previously, X failed".
- *Checkpoint insertion*: for high-consequence cues, add an explicit verification step to the task plan.
- *Contradiction surfacing*: "You are about to use approach A. In session 47, A failed because Z. The established alternative is B."

### Search, navigation, and activation compose vertically

Search runs over the lower layers, where items are numerous and weakly structured. Navigation runs over the upper layers, where items are fewer and richly linked. Activation runs over cues at any layer, because its trigger is the proposed action, not a query. For an agent about to write a database migration:

1. **Activation** fires matching cues. Corrections load as imperative instructions, preferences take their budget, and procedures suggest a checklist.
2. **Search** surfaces knowledge-role records about migrations: past decisions, negative results, draft ADRs.
3. **Navigation** follows links from those records to library notes, turning isolated facts into a coherent picture.

The agent gets corrections through activation and decisions and constraints through search and navigation, without loading a raw trace.

## Learning from session logs: the extraction taxonomy

Session logs carry at least four signal types. Ranked from easiest to hardest, they differ in oracle clarity, role, promotion threshold, and graduated artifact. Graduated artifacts move along the [codification](./definitions/codification.md) gradient from prose convention to skill to script or lint rule. The role stays constant as the constraint tightens.

**Corrections (system-definition; strongest signal).** The user rejects an output and states the fix, so the log holds an explicit negative signal paired with a positive one. Single-signal systems such as Pi Self-Learning target exactly this pattern. A correction seen in two sessions is not a fluke, so the threshold can be two occurrences. Graduation runs from a CLAUDE.md rule or style-guide convention to a lint check. Example: the user corrects alphabetical import sorting to stdlib / third-party / local grouping. On a second occurrence it becomes a documented preference; on a third, the question is whether it should be a pre-commit hook. A correction may also yield a companion knowledge note explaining why.

**Preferences (system-definition; distributed signal).** The user consistently accepts some patterns and rejects others without stating a rule. Each accept/reject is clear, but the connecting rule must be inferred across sessions. Detection works bottom-up (cluster decisions by domain and look for features that predict acceptance) or top-down (ask an LLM which preferences explain the last 50 decisions in a domain). Proposed threshold: five or more decisions across three or more sessions at over 80% consistency.

**Procedures (system-definition; sequence alignment).** A workflow recurs with variation. Tool-call sequences are more reliable signals than prose descriptions: four sessions sharing `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]` is detectable even when the conversations differ. Graduation runs from an instruction document (where steps need judgment) to a parameterized skill to a script (where the procedure is deterministic).

**Discoveries (knowledge, sometimes system-definition; weakest oracle).** An insight emerges once; "feels important" is not verifiable. A discovery usually enters as knowledge and may later gain a cue, for example a note on how async resource pools fail plus a cue that fires on async cleanup code. The role is assigned at graduation, because operational implications appear only with use. Detection heuristics are weak: explicit markers ("write this down"), claims linking previously unlinked notes, unusual elaboration depth, and later reference. Discoveries enter at low confidence and promote on reference frequency.

### The promotion pipeline

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. Extraction should be narrow and schema-constrained, with one prompt per signal type, not open-ended summarization. The candidate store must be separate from the library, because mixing unvetted candidates into curated knowledge pollutes search and degrades precision for everything.

### Session logs as a composite soft oracle

Most memory systems lack a signal for "was this memory operation good?" Session logs offer many weak ones: corrections, accept/reject patterns, explicit importance markers, questions asked, elaboration investment, whether the session goal was met, return visits to a topic, and abandoned investigations. Reviewed systems each use one or two signals (corrections only; importance plus recurrence; helpful/harmful feedback with decay). The bet is that a composite of weak signals can close enough of the oracle gap to be practical.

## Knowledge-role use cases

**Decision provenance.** The recurring high-value question is "why did we do it this way and not that way?" ADRs answer it but are written after the fact; session logs hold the raw deliberation. This enables a semi-automated ADR pipeline. It detects sessions where alternatives were debated and one was selected with reasons, pre-assembles a draft ADR, and leaves a human to verify it and connect it to existing notes. The "alternatives considered" section, the hardest part of an ADR to reconstruct, is what logs preserve most directly. The system-definition companion is a cue that fires when the agent re-proposes a rejected alternative.

**Negative-result preservation.** Code shows what was built, not what was tried and discarded. Only memory can answer "we tried that in session 34; it failed because the proxies strip custom headers." Negative results are stored as records (approach, failure reason, session, following decision) indexed by approach name. The system-definition companion is a cue keyed on the attempted approach: the record answers "why not?", and the cue prevents the attempt.

## Where memory ends and the project begins

Project artifacts sit on the class/role grid. Code, tests, and lint rules are symbolic system-definition. Documentation and ADRs are prose knowledge. CLAUDE.md is prose system-definition. For each artifact, the memory system adds the reasoning that produced it. Code says "retry with exponential backoff"; memory adds "a circuit breaker interacted badly with the connection pool in session 47". A test asserts an invariant; memory adds the bug that prompted it.

**CLAUDE.md is compiled system-definition; the memory system is its source.** A correction repeated three times lives in session logs and graduates to a CLAUDE.md entry, or further to a lint rule, which is the same role with tighter constraint.

The boundary blurs in two places. In the **overlap zone**, artifacts capture process knowledge incompletely: an ADR, a test written for a specific bug, a comment such as `// Retries capped at 3 -- see incident #412`. They record the conclusion without the deliberation. Memory holds the surrounding context rather than duplicating them. The **aspiration gap** is knowledge that belongs in project artifacts but was never written down: conventions, tribal knowledge, implicit invariants. Memory captures it by default, but its proper home is elsewhere.

Hence the substrate formulation: **project artifacts are curated projections of memory.** Memory preserves everything, and project artifacts are distilled from it.

### Graduation pathways

| Pattern | Graduation trigger | Destination | Role |
|---|---|---|---|
| Decision debated across sessions | "Why did we decide X?" is expensive to answer | ADR linking back to source sessions | Knowledge |
| Decision with a commonly proposed rejected alternative | Agent re-proposed rejected option | Cue keyed on the rejected alternative | System-definition |
| Same workflow in 3+ sessions | Repetition detection | Documented procedure, skill, or script | System-definition |
| Same mistake corrected 2+ times | Correction frequency | Convention, CLAUDE.md entry, or lint rule | System-definition |
| Same mistake, with instructive rationale | Reasoning worth preserving | Companion note or ADR | Knowledge |
| Agent needs same orientation each session | Recurring first-message pattern | CLAUDE.md entry | System-definition |
| Context needed to understand specific code | Explanation given during session | Code comment | Knowledge (usually) |
| Negative result: tried and abandoned | Approach explored and rejected | Negative-result record + "why not X?" index entry | Knowledge |

The meta-pattern is observation, accumulation, recognition, distillation, placement, provenance. Recognition is the bottleneck. It can be automated for clear triggers such as correction counts; for judgments such as whether a decision is load-bearing enough for an ADR, the system can only flag.

Every graduated artifact carries a maintenance obligation: an ADR must stay current, and a lint rule must change with conventions. Session logs are append-only and carry none. So premature graduation is worse than late graduation. Graduate only when retrieval cost exceeds maintenance cost.

### The reach heuristic

Reach, here, is how widely an item earns its place. It is asymmetric across roles. A knowledge artifact is worth promoting when its claim applies broadly. A cue is worth promoting when it fires accurately in the situations it covers, often enough to earn its context budget; a narrow cue that fires correctly beats a broad one that misfires. Graduating a correction into CLAUDE.md makes it fire in every session and multiplies the cost of being wrong.

Reach is often invisible when an observation is first made. A connection-pool race condition may be a one-off, or the third instance of a pattern in which async resource pools need explicit shutdown ordering. Reach is revealed by accumulation, when low-reach observations cluster around one structural pattern. Hence the two-phase rule: accumulate promiscuously, then graduate on revealed reach. The recognition step does the revealing.

## Alternatives considered

**Three layers instead of four.** An earlier version merged observation and episode into one "indexed memory" layer distinguished by type tag. Rejected because atomic lookup and narrative retrieval need different indexing, and one interface serving both adds complexity without payoff. The two may share storage but stay distinct.

**One unified retrieval pipeline.** The two roles were first treated as phases of one search-and-rank flow. Rejected because the consumers differ: a question-asker navigates from a query, while an acting agent needs policy injected without asking.

**Extraction at ingestion time only, no backfill.** Rejected because it couples capture speed to extraction quality. Retained traces let the pipeline be rerun and backfilled as techniques improve; that is the structural advantage of storing everything.

**A binary memory/project split.** Classifying each artifact as either project or memory was rejected because the real boundary follows the class/role grid, not artifact kind: the same content appears in both places for different purposes. The adopted framing treats memory as the substrate from which project artifacts are distilled.

## What remains open

**Inspectability versus learnability of retrieval policy.** Inspectable rules are debuggable and incrementally refinable but brittle as scope grows. Learned policies such as AgeMem's adapt but are opaque and need a clear oracle. A hybrid is likely: heuristic rules by default, learned overrides where volume permits. The interface between them, when an override should supersede a rule and how to detect drift, is unsolved.

**Cross-session structural pattern detection.** Three incidents, a deploy failing on stale staging config, a migration failing on stale test config, and a rollout failing on out-of-sync production config, share no keywords. Together they reveal a high-reach pattern: configuration lacks a single source of truth. Detecting it requires recognizing shared causal structure, which is expensive and speculative. Periodic deep-analysis passes, weekly or monthly, may be needed.

**The oracle problem for discoveries.** Corrections have an explicit oracle, preferences a statistical one, and procedures a structural one. Discoveries have none except later use, which is a trailing indicator. Recognition may stay semi-manual.

**The ephemeral-computation trap.** If candidates never promote, the system appears to learn without learning. A candidate store nobody reviews is an elaborate form of ephemerality. This is an operational problem, not a technical one, and it is the most likely failure in practice.

**Scale.** At single-user scale the observation layer holds tens of thousands of entries and the library fits one curator. Teams (conflicting preferences, concurrent work) and very long-lived projects (tens of thousands of sessions) are deferred. Progressive disclosure should scale further than flat search, but cross-session pattern detection grows combinatorially harder.

## A practical starting point

Each step below is useful on its own:

1. **Session logging.** Capture complete traces. Cheap, needs no extraction, and already answers "what happened in session X?"
2. **Correction extraction.** The strongest oracle. Run a schema-constrained pass at session end, store corrections as typed cues, and surface them before a repeated mistake.
3. **Preference and procedure extraction.** Once roughly 50 sessions accumulate, run periodic passes for accept/reject patterns and recurring tool-call sequences.
4. **Episodes.** As work units become identifiable, compress them into episode records to answer "have we tried this before?"
5. **The promotion pipeline.** Connect the candidate store to the library, starting with high-confidence, high-frequency promotions and expanding as the system matures.
