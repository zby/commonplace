---
description: Design study of an ideal agent memory system under store-everything premise — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction pipeline
type: types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Designing a Memory System for LLM-Based Agents

## The core insight: storage is cheap, context is scarce

The central design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Storage is a solved problem: disk is cheap, text compresses well, and append-only logs need no schema design. The binding constraint is *context* — the finite window of tokens an agent attends to in one inference call. Context is the only channel through which the agent receives instructions and knowledge, everything competes for it, and it degrades before it fills: added material can dilute instructions and distort interpretation below the token limit.

This inverts the usual design emphasis. Store aggressively — all session logs, intermediate artifacts, and observations — and put the design intelligence into retrieval and activation, the machinery that decides which fraction of the store enters context for a given task.

"Store everything" is a bet, not an axiom. It trades storage cost for indexing overhead, search pollution risk, and privacy exposure, and it bets that selective retrieval can manage what aggressive storage introduces.

## Memory plays two roles

Stored content is consumed in one of two roles. In the **knowledge role** it is consumed as fact, and durable writes grow what the agent can answer. In the **system-definition role** it is consumed as policy, and durable writes change what the agent does. [Artifact analysis](./axes-of-artifact-analysis.md) records this distinction as behavioral authority. It is relational, not structural: "we use URL-path versioning" is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the next API design.

The two roles need different machinery. Knowledge retrieval answers questions posed at consumption time; it fails when nobody asks. System-definition activation injects policy when a matching situation occurs; it fails when stored policy never fires, which is the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md). Most agent-memory systems optimize for knowledge-role retrieval (RAG over stored facts) and underserve the system-definition role, which is where [continual learning must govern behaviour-changing writes](./continual-learning-requires-governing-behaviour-changing-writes.md). "Adding RAG is learning" holds for the knowledge role and says nothing about the system-definition role.

Session logs feed both. One correction in session 47 can yield a knowledge artifact (an ADR answering "why approach B?") and a system-definition artifact (a cue that fires when a later session proposes approach A). The extraction pipeline must produce both, and retrieval must serve both consumption patterns.

## Why existing approaches fall short

A comparative analysis of eleven agent memory systems — from vector-first fact stores (Mem0) through knowledge graphs (Graphiti) to filesystem-first curated systems (Ars Contexta, Commonplace) — shows three problems no current system fully solves.

**The agency trilemma.** Who decides what to remember? If the agent manages its own memory (Letta), it has full context but spends reasoning tokens on housekeeping. If an external service does (Mem0, Graphiti, Cognee), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-manage it (Commonplace, Ars Contexta), curation quality is highest and throughput lowest. AgeMem trains the memory policy by reinforcement learning, which approaches all three but needs a task-completion oracle that open-ended domains may lack, and the learned policy is opaque. No system combines high agency, high throughput, and high curation quality.

**Navigability versus retrieval.** Mem0, Graphiti, and Cognee treat knowledge as something to *search* (embed a query, return top-k). Ars Contexta and Commonplace treat it as something to *navigate* (follow articulated links). Search scores well on QA benchmarks, but QA accuracy does not measure whether an agent can follow a chain of decisions or trace a correction back to the episodes that established it. Neither pattern serves the system-definition role, which needs a third one, triggered activation; QA benchmarks do not test it, which is one reason no reviewed system closes the activation gap.

**Everyone automates extraction; nobody automates synthesis.** Every system can extract structured knowledge from unstructured input. Almost none can synthesize across existing knowledge — find novel connections, merge threads, reformulate entries. Retaining complete logs gives store-everything designs an advantage here: synthesis can be attempted retrospectively and rerun when techniques improve.

## Architecture: four layers of progressive distillation

A store-everything system without structure is a haystack. The architecture has four layers, each more distilled than the one below.

**Layer 1: Trace.** Complete session logs — every interaction, tool call, model output, and user message — as append-only records with timestamps and session identifiers. Traces are ground truth for provenance and offline extraction. They answer "what exactly happened in session X?" and nothing else efficiently. The agent never loads raw traces into working context.

**Layer 2: Observation.** Extracted atomic facts: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each is typed, timestamped, linked to its source session, scored for confidence and importance, and **tagged with its role**. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). Others yield paired artifacts: a decision yields a knowledge record for "why we chose A" and a cue for "if B is proposed, surface the reasoning for A." ClawVault's scored, typed observations with promotion pathways are the closest precedent; the difference is that observations here are derived from stored traces, not extracted at interaction time. That decouples capture speed from extraction quality, so extraction can be rerun, improved, and backfilled.

**Layer 3: Episode.** Compressed accounts of bounded work units, possibly spanning sessions: goal, session range, outcome, key decisions (pointing to observations), lessons, open threads, and library artifacts produced. Observations answer "have we seen this before?"; episodes answer "have we tried something like this, and what happened?"

**Layer 4: Library.** Curated notes, procedures, indexes, and ADRs. The design does not change the library; it gives it richer input channels and a principled path from raw experience to curated knowledge.

**Why four.** With two layers (trace and library), every transition needs a human to read a trace and write a note — the bottleneck the system exists to remove. With three, one intermediate layer must serve both atomic lookup and narrative retrieval, which need different indexing, extraction, and promotion. Observations and episodes can share storage, distinguished by type tags, but should be treated as different kinds of objects. A fifth layer, such as splitting the library into working and reference knowledge, adds a boundary that inhibits connections; frontmatter types and links already differentiate within the library. The layers also give progressive disclosure: scan observation summaries and episode goals first, load full episodes or clusters if relevant, follow pointers to traces only when provenance is needed.

### How material moves between layers

The promotion pathways matter more than the layers.

- **Trace → Observation (extraction).** Runs automatically at session end, and again over old traces when the pipeline improves. An LLM extracts typed observations with confidence, importance, and a source pointer. Failure modes: over-extraction (noise), under-extraction (missed preferences), and misclassification (a correction tagged as a preference loses its corrective force). Fully reversible, since traces are retained.
- **Observation → Episode (compression).** Triggered by work-unit completion, periodic consolidation, or request. Harder than extraction because it requires editorial judgment about what mattered. Boundary heuristics: shared file paths, shared task references, temporal proximity, topic similarity, and explicit "starting/done with X" markers.
- **Observation → Library (promotion).** Triggered by recurrence, importance, or request. Thresholds should vary by type: a preference may need three or more independent sessions; a single high-stakes architectural decision may warrant immediate promotion to an ADR.
- **Episode → Library (distillation).** Usually deliberate. The episode gives the reviewer the full narrative to check whether a distilled claim represents it faithfully.
- **Library → Observation (backflow).** Library notes should generate activation cues: a note on "stage specific files, not `git add -A`" should yield a cue that fires when a session involves git staging. Without backflow, library knowledge is stored but never activated.

### Lifecycle and role: orthogonal tags on one store

Knowledge, self-knowledge, and operational artifacts change at different rates. Operational observations churn fast; self-observations (preferences) are slow and stable; knowledge accumulates and is superseded rather than expiring. Separate stores would inhibit cross-space connections, so the architecture keeps one store and tags each observation by lifecycle space. The tag selects the promotion target and threshold: recurrent knowledge becomes a library note, a recurrent operational observation becomes a procedure, and a recurrent self-observation becomes a CLAUDE.md entry.

Role is a separate tag. Lifecycle answers *when does this expire?*; role answers *how is this consumed?* A debugging procedure is usually system-definition but becomes knowledge when someone asks how a class of bug is debugged. Retrieval uses lifecycle to weight recency and role to select the activation mechanism.

## Retrieval and activation

The hardest problem is activation: a system can store relevant knowledge, produce it on direct query, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query.

### Two pipelines, split by role

**Knowledge-role retrieval** serves questions such as "why did we do X?" The interface is navigable: embedding search over descriptions as a first-pass filter, then articulated library links. Its failure mode — the question is never asked — is an elicitation problem this pipeline can assist but not solve.

**System-definition activation** serves the agent's in-flight work. The interface is a watcher, not a query: cues indexed by action signature, preference domain, or situation template fire when the agent's proposed action matches. Its failure mode — the cue never fires although it applies — is the activation gap proper, and most of the design surface lives here.

The pipelines share the observation store and cross-reference each other: a fired cue can point to the ADR that explains it, and navigating to a note can reveal a correction attached to it.

### Three stages of activation failure

- **Cue match.** The task context must carry enough signal to trigger retrieval. Embedding similarity handles topical matches but fails on causal ones: session 47's correction about a deployment mistake will not embed near session 312's code-writing task, even when the lesson applies.
- **Priority arbitration.** In a store with thousands of sessions, any task matches dozens of items, and loading them all destroys context efficiency.
- **Commitment.** Even loaded knowledge may lose to training-time defaults. The agent answers what it is asked but does not raise concerns unprompted.

### Typed cue indexes

Typed cue indexes are the main mechanism against the activation gap. Instead of searching raw logs at retrieval time, the system extracts typed cues at ingestion time, each with its own retrieval signature. A **correction cue** matches the action the agent is about to take:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches the decision space, a **precedent cue** the situation description, and a **procedure cue** the goal. When session 312's task plan includes dropping a column, the correction cue fires and the lesson enters context before the agent writes the migration.

Matching is the hard part: "migration that removes a column" must match "drop column deprecated_flag." Three approaches compose: action-type classification (both are `schema-migration:column-removal`), embedding similarity with a low threshold (accept false positives over false negatives), and LLM-judged relevance for high-consequence cues.

### Priority arbitration and commitment

When too many cues match, four mechanisms decide what surfaces:

- *Recency-weighted relevance* with a long tail, so an old correction still counts if the mistake pattern recurs.
- *Consequence weighting*: sessions with corrections, frustration, or rework rank higher. The log supplies the signals — messages needed after a correction, sentiment markers, explicit severity.
- *Frequency*: a cue that fires across many sessions is more likely to matter.
- *Budget allocation by type*: fixed context slots for corrections, preferences, and precedents, so no cue type crowds out the others.

Loading is not using. Three mechanisms address commitment: *imperative framing* ("BEFORE doing X, verify Y because Z failed in session 47", not "previously, X failed"); *checkpoint insertion* of explicit verification steps into the task plan for high-consequence cues; and *contradiction surfacing* ("you are about to use approach A; it failed in session 47; the established alternative is B").

### Search, navigation, and activation compose

Search works over the lower layers, where items are numerous and weakly structured. Navigation works over the upper layers, where items are fewer and richly linked. Activation works over system-definition cues at any layer, because its trigger is the proposed action, not a query. For an agent about to write a migration: activation fires matching cues as imperative instructions; search surfaces related knowledge-role records (past decisions, negative results); navigation follows their links to library notes. The agent gets corrections, alternatives, and architectural constraints without loading a raw trace.

## Learning from session logs: the extraction taxonomy

Session logs carry at least four signal types, differing in oracle clarity, extraction difficulty, role, and graduation target. Corrections, preferences, and procedures are system-definition; decision provenance and negative results are knowledge; discoveries start as knowledge and may graduate into either role. From easiest to hardest:

**Corrections (system-definition): the strongest signal.** The user says "no, do X instead" or rejects a tool call. The log holds the wrong output, the rejection, and the fix — an explicit negative paired with a positive. Pi Self-Learning's extraction schema targets exactly this (`{"mistakes": [...], "fixes": [...]}`). Two occurrences in different sessions can justify promotion. The graduated artifact moves along the codification gradient within one role: a CLAUDE.md rule or style-guide convention (prose), then a lint check or validation script (symbolic). A companion note or ADR may record why. Example: the user corrects alphabetical import sorting to stdlib/third-party/local grouping; on the second occurrence it becomes a documented preference, on the third a candidate pre-commit hook.

**Preferences (system-definition): distributed signal.** The user consistently accepts some patterns and rejects others without stating a rule. Each signal is clear, but the connecting pattern must be inferred as a latent variable across sessions. Detection runs bottom-up (cluster accept/reject decisions by domain, find features that predict acceptance) or top-down (ask an LLM what preferences explain the last 50 decisions in a domain). A reasonable threshold: five or more decisions across three or more sessions with over 80% consistency.

**Procedures (system-definition): sequence alignment.** The same workflow recurs with different content. Tool-call sequences are more reliable than prose descriptions: four sessions containing `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]` form a detectable pattern even when the conversations differ. The graduated artifact tightens along the constraining gradient — instruction document, skill, script — while the role stays constant.

**Discoveries (knowledge, sometimes system-definition): no oracle.** An insight emerging during work is the highest-value extraction and the hardest to detect; it is a one-off event, and "feels important" is not verifiable. Role is assigned at graduation, because operational implications show only with use: a discovery about async pool failures may later yield a cue for async cleanup code. Weak heuristics: explicit markers ("write this down"), claims linking previously unlinked notes, unusual elaboration depth, and later reference. Enter discoveries as low-confidence candidates and promote by reference frequency.

### The promotion pipeline

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. Extraction should be narrow and schema-constrained — one prompt per signal type, not "summarize the session." And the candidate store must be separate from the library; mixing unvetted candidates into curated knowledge causes search pollution that degrades retrieval for everything.

### Session logs as composite oracle

Most memory systems lack a signal for "was this memory operation good?" Session logs offer many weak ones: corrections, accept/reject patterns, explicit markers, questions asked, elaboration investment, whether the session goal was met, returns to a topic, and abandoned investigations. Reviewed systems each use few — Pi Self-Learning only corrections, ClawVault importance plus recurrence, cass-memory helpful/harmful feedback plus decay. The bet is that combining many weak signals yields a soft oracle good enough to be practical.

## Knowledge-role use cases

The system-definition counterpart of these use cases — keeping a rejected approach from being proposed again — runs through the cue index.

**Decision provenance.** The high-value question is *why did we do it this way and not that way?* ADRs answer it, but they are written after the fact. Session logs hold the raw deliberation, which supports a semi-automated ADR pipeline: flag sessions where alternatives were debated and one selected, pre-assemble a draft ADR, and have a human verify and connect it. The "alternatives considered" section, the hardest part to reconstruct from memory, is what logs preserve most directly. Logs also answer "why" questions no ADR anticipated, because they keep what was discarded. A good ADR often gets a companion cue that fires when a rejected alternative is proposed; the two point at each other.

**Negative results.** What was tried and abandoned has no home in standard project structure. Record each as the approach, the failure reason, the source session, and the decision that followed, indexed by approach name so "why didn't we do X?" finds it. A severe one also gets a cue keyed on the approach.

## Where memory ends and the project begins

"The memory system stores what project artifacts don't preserve" is necessary but not sufficient. Project artifacts span representational form and role: code, tests, and lint rules are symbolic system-definition; documentation and ADRs are prose knowledge; CLAUDE.md is prose system-definition. Against each, the memory system adds the reasoning that produced it — the circuit breaker tried before the retry loop, the bug a test guards against, the questions the docs failed to answer.

**CLAUDE.md is compiled system-definition; the memory system is the source.** A correction repeated three times lives in session logs and graduates to a CLAUDE.md entry, or further to a lint rule — same role, tighter constraint.

The boundary blurs in two ways. In the **overlap zone**, artifacts such as ADRs, bug-driven tests, and comments like `// Retries capped at 3 -- see incident #412` capture a conclusion without its deliberation; the memory system holds the surrounding context rather than duplicating them. In the **aspiration gap**, undocumented conventions and implicit invariants belong in project artifacts but nobody wrote them; the memory system captures them by default until they are. Hence the better formulation: **the memory system is the substrate from which project artifacts are distilled**, and project artifacts are curated projections of it.

### Graduation pathways

The destination depends on what was learned and which role the artifact will play; one pattern can produce artifacts in both roles.

| Pattern | Graduation trigger | Destination | Role |
|---|---|---|---|
| Decision debated across sessions | "Why did we decide X?" is expensive to answer | ADR linking back to source sessions | Knowledge |
| Decision with a commonly-proposed rejected alternative | Agent re-proposed rejected option | Cue keyed on the rejected alternative | System-definition |
| Same workflow in 3+ sessions | Repetition detection | Documented procedure, skill, or script | System-definition |
| Same mistake corrected 2+ times | Correction frequency | Convention, CLAUDE.md entry, or lint rule | System-definition |
| Same mistake, with instructive rationale | The reasoning is worth preserving | Companion note or ADR | Knowledge |
| Agent needs same orientation each session | Recurring first-message pattern | CLAUDE.md entry | System-definition |
| Context needed to understand specific code | Explanation given during session | Code comment | Knowledge (usually) |
| Negative result: tried and abandoned | Approach explored and rejected | Negative-result record + "why not X?" index entry | Knowledge |

Recognition is the bottleneck. Clear triggers (correction frequency, repetition count) can be automated; judgment calls (is this decision load-bearing enough for an ADR?) can only be flagged.

Every graduated artifact creates a maintenance obligation; append-only logs create none. Premature graduation is therefore worse than late graduation: graduate only when the cost of retrieving from memory exceeds the cost of maintaining the artifact.

**Reach decides what graduates, and it differs by role.** A knowledge artifact is worth promoting when its claim applies broadly ("systems optimized for normal-load efficiency sacrifice overload resilience"); a narrow fact ("the PR #247 bug was a pool race condition") can stay in the logs. A system-definition artifact is worth promoting when its trigger fires accurately and often enough in its situations to earn its context budget; a narrow accurate cue beats a broad one that misfires, and moving a correction into CLAUDE.md multiplies the cost of being wrong because every session loads it. Reach is often invisible at first observation and revealed by accumulation, when several narrow observations cluster on one structural pattern. So accumulate promiscuously, then graduate on revealed reach.

## Alternatives considered

- **One retrieval pipeline for both roles.** Rejected because a question-asker navigates from a query while an acting agent needs policy injected without asking.
- **Extraction at session end only, no backfill.** Rejected because it couples capture speed to extraction quality; retained traces let the pipeline be rerun and improved.
- **Binary memory/project split.** Rejected because the boundary runs across form and role rather than artifact kind; the memory system is the substrate projects distill from, not a parallel store.
- **Three layers**: see "Why four" above.

## What remains open

**Inspectability versus learnability.** Explicit retrieval rules are debuggable and auditable but brittle as scale and domains grow. Learned policies adapt (AgeMem improves measurably from experience) but are opaque and need an oracle open domains may lack. The likely answer is inspectable heuristics by default with learned overrides where volume allows; when an override should supersede a rule, and how to detect drift from the heuristic baseline, is unsolved.

**Cross-session structural patterns.** Three incidents — a deploy failing on a stale staging config, a migration failing on a stale test config, a rollout breaking on an out-of-sync production config — share no keywords but reveal one high-reach pattern: configuration lacks a single source of truth. Detecting shared causal structure needs deep, expensive reasoning on a speculative payoff, which is where the agency trilemma bites hardest. Periodic deep-analysis passes, weekly or monthly, may be the practical form. No reviewed system addresses this.

**The discovery oracle.** Corrections have an explicit oracle, preferences a statistical one, procedures a structural one. Discoveries have only later use, a trailing indicator. Discovery extraction may stay semi-manual: the system surfaces candidates and a human judges them.

**The ephemeral computation trap.** If extraction runs but candidates never promote, the system looks like it learns without learning. The promotion filter must run and someone must review its output. This is an operational problem, not a technical one, and the most likely failure in practice.

**Scale.** The design targets one user and one project: hundreds to low thousands of sessions, tens of thousands of observations, hundreds of episodes, one curator. Teams (conflicting preferences, concurrent streams) and very long-lived projects are open. Progressive disclosure should scale further than flat search, but cross-session pattern detection grows combinatorially harder with session count.

## A practical starting point

The difficulty gradient suggests a build order; each step is useful on its own.

1. **Session logging.** Capture complete traces. Cheap, no extraction needed, and it creates the substrate for everything else.
2. **Correction extraction.** The easiest type with the strongest oracle. Run a schema-constrained pass at session end, store corrections as typed cues, and surface them when the agent is about to repeat a mistake.
3. **Preference and procedure extraction.** Once roughly 50+ sessions exist, run periodic passes for consistent accept/reject patterns and recurring tool-call sequences.
4. **Episode layer.** As work units become identifiable, compress multi-session efforts into episodes to answer "have we tried this before?"
5. **Promotion pipeline.** Connect the candidate store to the library, starting with high-confidence, high-frequency promotions (a correction seen three times becomes a convention), and extend to lower-confidence types as the system matures.
