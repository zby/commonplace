---
description: Design study of an ideal agent memory system under store-everything premise — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction pipeline
type: types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Designing a Memory System for LLM-Based Agents

This is a design study for single-user, single-project scale (hundreds to low thousands of sessions). Nothing in it has been built or measured; thresholds and build steps below are proposed heuristics, not findings.

## The core insight: storage is cheap, context is scarce

The dominant design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Storage is cheap: disk costs little, text compresses well, and append-only logs need no schema design. The binding constraint is *context* — the finite window of tokens an agent attends to in one inference call. Context is the only channel through which the agent receives instructions and knowledge, so everything competes for it. It also degrades softly well before it fills: more material can dilute instructions and distort interpretation even below the token limit. Selection is therefore the binding problem.

This produces a design inversion. Traditional systems optimize storage and let retrieval be a lookup. An agent memory system should store aggressively and put the design intelligence into retrieval and activation.

"Store everything" is a bet, not an axiom. It trades storage costs for indexing overhead, search pollution risk, and privacy exposure. The bet is that selective retrieval can manage what aggressive storage introduces.

## Memory plays two roles

The [axes of artifact analysis](./axes-of-artifact-analysis.md) name a **role** axis: an artifact is consumed either in a **knowledge role** (as fact; durable writes grow the agent's reach) or in a **system-definition role** (as policy; durable writes change the agent's disposition). The role is relational: the same bytes can play either role depending on the consumer. A note saying "we use URL-path versioning" is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the agent's next API design.

The two roles need different machinery and fail differently:

- **Knowledge retrieval** answers questions posed at consumption time. It fits search plus navigation. Failure mode: *the question is never asked.*
- **System-definition activation** injects policy when a matching situation occurs. It fits a watcher over cues in the agent's proposed action. Failure mode: *the policy is stored but never fires* — the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md).

Most agent-memory systems serve only the knowledge role (RAG over stored facts). That is why "adding RAG is learning" is true for the knowledge role and empty for behavior, which is the half of continual learning that [requires governing behaviour-changing writes](./continual-learning-requires-governing-behaviour-changing-writes.md).

Session logs are the common substrate for both roles. One correction in session 47 can yield a knowledge artifact (an ADR answering "why do we use approach B?") and a system-definition artifact (a cue that fires when a future session proposes approach A).

## Three structural problems in existing systems

A comparative analysis of eleven agent memory systems, from vector-first fact stores through knowledge graphs to filesystem-first curated systems, surfaced three structural problems. Systems named here illustrate positions; they are not reviewed.

**The agency trilemma: who decides what to remember?** If the agent manages its own memory (Letta's position), it has full context but spends reasoning tokens on housekeeping. If an external service extracts (Mem0, Graphiti, Cognee), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-curate (Commonplace, Ars Contexta), quality is highest and throughput lowest. Training the policy with reinforcement learning (AgeMem) needs a task-completion oracle that open-ended domains may lack, and the learned policy is opaque. No system combines high agency, high throughput, and high curation quality.

**Navigability versus search.** Some systems treat knowledge as something you *search* (embed a query, return top-k); others treat it as something you *navigate* (follow articulated links). Search scores well on QA benchmarks, but QA accuracy does not measure whether an agent can follow a chain of decisions to understand why the system works as it does. A memory system needs both. Neither tests system-definition activation, which needs a third pattern: triggered activation.

**Everyone automates extraction; nobody automates synthesis.** Systems extract structured knowledge from input, but almost none synthesize across existing knowledge: merging threads, producing new insight, reformulating entries. A store-everything design has a structural advantage here: because traces are retained, synthesis can be attempted retrospectively and rerun when techniques improve.

## Architecture: four layers of progressive distillation

**Layer 1: Trace.** Complete session logs: every interaction, tool call, model output, and user message, as append-only records. Traces answer "what exactly happened in session X?" and serve provenance and offline extraction. The agent never loads raw traces into a working context.

**Layer 2: Observation.** Extracted atomic items: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each observation is typed, timestamped, source-linked, scored for confidence and importance, and **tagged with its role**. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). Ambiguous types yield paired artifacts: a decision yields a knowledge record ("why we chose A") and a cue ("if B is proposed, surface the reasoning for A"). Observations answer "have we seen this before?" Because they derive from stored traces rather than being captured at interaction time, extraction quality is decoupled from capture speed and the pipeline can be rerun and backfilled.

**Layer 3: Episode.** Narrative accounts of bounded work units that may span sessions: goal, session range, outcome, key decisions (pointing to observations), lessons, open threads, and library artifacts produced. Episodes answer "have we tried something like this before, and what happened?"

**Layer 4: Library.** Curated notes, claims, indexes, procedures, and ADRs. The design leaves the library unchanged; it feeds it through richer input channels and a principled path from raw experience to curated knowledge.

### Why four layers

- **Two layers** (trace and library) leave no intermediate representation. Every transition requires a human to read traces and write notes, which is the manual bottleneck the system exists to remove.
- **Three layers** (one intermediate layer) force atomic lookup ("has this correction been given before?") and narrative retrieval ("what happened when we tried this?") through one interface, although they need different indexing. Observations and episodes can share storage, distinguished by type tags, but extraction, promotion, and retrieval treat them as different kinds of object.
- **A fifth layer** (say, working versus reference library) adds a boundary that inhibits connections. The library's types, status fields, and links already handle internal differentiation.

The layers also give the context scheduler a progressive-disclosure strategy: scan observation summaries and episode goals first, load a full episode or observation cluster when relevant, and follow pointers back to traces only for provenance.

### Promotion pathways

**Trace → Observation (extraction).** Runs after each session and again over old traces when extraction improves. An LLM extracts typed, scored, source-linked observations. Failure modes: over-extraction (noise), under-extraction (missed preferences), and type misclassification (a correction tagged as a preference loses its corrective force). Reversible, because traces are retained.

**Observation → Episode (compression).** Triggered by work-unit completion, periodic consolidation, or human request. Harder than extraction because it needs editorial judgment about what mattered. Boundary heuristics: shared file paths, shared task references, temporal proximity, topic similarity, and explicit "starting/done with X" markers.

**Observation → Library (promotion).** Triggered by recurrence, importance, or human request. Thresholds vary by type: a preference may need three or more independent sessions, while one high-stakes architectural decision may warrant immediate promotion.

**Episode → Library (distillation).** Usually deliberate. One episode may yield several library artifacts, and the episode gives the reviewer the full narrative to check the distilled claim against.

**Library → Observation (backflow).** Library notes generate activation cues in the observation layer. A note saying "prefer staging specific files over `git add -A`" yields a cue that fires when a session stages files. Without backflow, library knowledge sits inert: stored but never activated.

### Lifecycle and role as orthogonal tags

Observations differ in lifecycle. Operational observations churn fast, self-observations (such as preferences) evolve slowly, and knowledge observations accumulate. Separate stores would inhibit cross-connections, so the design keeps one store and tags each observation by lifecycle and by role. Lifecycle answers *when does this expire?* and weights recency; it also selects the promotion target and threshold (a recurring knowledge observation becomes a library note, a recurring operational one a procedure, a recurring self-observation a CLAUDE.md entry). Role answers *how is this consumed?* and selects the retrieval mechanism. The tags vary independently: a debugging procedure is usually system-definition but becomes knowledge when someone asks "how do we debug this class of bug?"

## Retrieval and activation

A system can store relevant knowledge, produce it on direct query, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query, so activation is where most of the design surface lies.

### Retrieval splits by role

The design runs two pipelines over the same store:

- **Knowledge-role retrieval** serves questions such as "why did we do X?" The interface is navigable: embedding search over descriptions as a first-pass filter, then articulated library links. When no one asks the question, this pipeline cannot help; that elicitation problem lies outside it.
- **System-definition-role activation** serves the agent's in-flight work. The interface is a watcher, not a query: cues indexed by action signature, preference domain, or situation template fire when the proposed action matches.

The pipelines cross-reference each other. A fired cue can point into the knowledge layer ("this correction belongs to a documented convention, see ADR 014"), and navigation can reveal dormant cues attached to a note.

### Three stages of activation failure

**Cue match.** The task context must contain enough signal to trigger retrieval. Embedding similarity handles topical matches but misses causal ones: session 47's correction about a deployment mistake will not embed near session 312's code-writing task, even though the lesson applies.

**Priority arbitration.** In a store-everything system, any task context matches dozens of stored items. Loading them all destroys context efficiency, so candidates compete for a limited budget.

**Commitment.** Even loaded knowledge may lose to training-time defaults. The agent behaves like an expert witness: it answers accurately what it is asked but does not raise concerns the questioner has not thought of.

### Typed cue indexes

Cues are system-definition artifacts extracted at ingestion time, typed by what they match against. A **correction cue** matches the action the agent is about to take:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches the decision space, a **precedent cue** the situation description, and a **procedure cue** the goal.

This structure is what bridges session 47 to session 312. In session 47 the user corrects the agent's migration approach, and the correction is extracted with a trigger. In session 312, when the task plan includes dropping a column, the trigger matches and the lesson loads before the agent writes the migration.

Matching is the hard part: "migration that removes a column" must match "drop column deprecated_flag". Three approaches compose: action-type classification (both are `schema-migration:column-removal`), embedding similarity at a low threshold (accepting false positives over false negatives), and LLM-judged relevance for high-consequence cues.

### Priority arbitration and commitment

When too many cues match, four mechanisms decide what surfaces:

- *Recency weighting* with a long tail, since an old correction still matters if the mistake recurs.
- *Consequence weighting*: sessions with corrections, frustration, or rework rank higher. The log supplies the signals (messages spent after a correction, explicit severity statements).
- *Frequency*: a cue that fires across many sessions more likely matters.
- *Per-type budgets*: fixed context slots for corrections, preferences, and precedents, so no cue type crowds out the others.

Three mechanisms address commitment:

- *Imperative framing*: "BEFORE doing X, verify Y because Z failed in session 47," not "previously, X failed."
- *Checkpoint insertion*: for high-consequence cues, add an explicit verification step to the task plan.
- *Contradiction surfacing*: when the proposed action contradicts a stored correction, say so and name the established alternative.

### Search, navigation, and activation compose vertically

Search covers the lower layers, where items are numerous and weakly structured. Navigation covers the upper layers, where items are fewer and richly linked. Activation covers system-definition cues in any layer, because its trigger is the proposed action rather than a query. For an agent about to write a database migration:

1. **Activation** fires matching cues: corrections load as imperative instructions, procedure cues suggest a checklist.
2. **Search** over observations surfaces knowledge-role records: past migration decisions, negative results, draft ADRs.
3. **Navigation** follows links from those records to library notes, turning isolated facts into a coherent picture.

The agent gets corrections (system-definition, via activation) and decisions and constraints (knowledge, via search and navigation) without loading a raw trace.

## Learning from session logs: the extraction taxonomy

Session logs carry four signal types, ranked here from clearest oracle and easiest extraction to hardest. Corrections, preferences, and procedures are system-definition. Discoveries start as knowledge and may acquire a system-definition companion. Each graduates along the [codification](./definitions/codification.md) gradient — prose convention, then skill, then script or lint — and its role stays constant as the constraint tightens.

**Corrections (system-definition): the strongest signal.** The user rejects an output and states the fix, so the log holds an explicit negative paired with a positive. A correction seen in two different sessions is not a fluke, so the promotion threshold can be two occurrences. It graduates to a CLAUDE.md rule or style convention (prose) and, if it keeps recurring, to a lint check or script (symbolic). Example: the user corrects alphabetical import sorting to stdlib / third-party / local grouping; on recurrence it becomes a documented preference; on a third occurrence the question is whether to make it a pre-commit hook. A correction may also yield a companion note or ADR explaining the rationale.

**Preferences (system-definition): distributed signal.** The user accepts some patterns and rejects others without stating a rule. Each accept/reject is clear, but the rule connecting them must be inferred. Detection runs bottom-up (cluster decisions by domain and look for features that predict acceptance) or top-down (ask an LLM which preferences explain the last 50 decisions in a domain). A proposed threshold: five or more decisions across three or more sessions with over 80% consistency.

**Procedures (system-definition): sequence alignment.** The same workflow recurs with variations. Tool-call sequences are more reliable than prose: a subsequence like `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]` in four sessions is detectable even when the conversation differs. The artifact graduates from instruction document (human judgment at steps) to skill (parameterized) to script (fully deterministic).

**Discoveries (knowledge, sometimes system-definition): the oracle problem at its purest.** An insight is a one-off event, and "feels important" is not a verifiable signal. Role is assigned at graduation, because operational implications show only with use: an insight about how async resource pools fail may later add a cue that fires on async cleanup code. Weak heuristics include explicit markers ("write this down"), claims connecting previously unlinked notes, unusual elaboration depth, and later reference. Discoveries enter as low-confidence candidates and promote on reference frequency.

### The promotion pipeline

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. Extraction should be narrow and schema-constrained — one prompt per signal type asking for its schema — rather than open "summarize the session". And the candidate store must be separate from the library, like a [workshop layer](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md): mixing unvetted candidates into curated knowledge causes search pollution that degrades precision for everything.

### Session logs as a composite soft oracle

[Automating KB learning](./automating-kb-learning-is-an-open-problem.md) is bottlenecked on oracles. Session logs offer many weak signals: corrections, accept/reject patterns, explicit importance markers, questions asked, elaboration investment, whether the session goal was met, returns to a topic, and abandoned investigations. Reviewed systems each use one or two signals (corrections only; importance plus recurrence; helpful/harmful feedback with decay). The bet is that a soft oracle composed from many weak signals closes enough of the gap to be practical.

## Knowledge-role use cases

**Decision provenance.** The recurring high-value question is *why did we do it this way and not that way?* Session logs hold the raw deliberation that ADRs summarize after the fact: alternatives, reasoning, constraints, objections. That enables a semi-automated ADR pipeline: flag sessions where alternatives were debated and one was selected, pre-assemble a draft ADR, and have a human verify it and connect it. The "alternatives considered" section, the costliest to reconstruct from memory, is what logs preserve most directly. Companion cue: one that fires when the agent re-proposes a rejected alternative.

**Negative-result preservation.** Code shows what was built, not what was tried and discarded. Negative results are stored as records (approach, failure reason, source session, the decision that followed) indexed by approach name, so "why didn't we do X?" finds them: "we tried that in session 34; the proxy servers strip custom headers." Companion cue: when a failure is severe enough, a cue keyed on the approach prevents the attempt.

## Where memory ends and the project begins

The naive boundary — memory stores what project artifacts do not preserve — is necessary but not sufficient. Project artifacts occupy the class/role grid: code, tests, and lint rules are symbolic system-definition; documentation and ADRs are prose knowledge; CLAUDE.md is prose system-definition. Against each, the memory system adds the reasoning behind the artifact. The code says "retry with exponential backoff"; memory adds "a circuit breaker interacted badly with the connection pool in session 47". The test asserts an invariant; memory adds which bug prompted it.

**CLAUDE.md is compiled system-definition; the memory system is its source.** A correction repeated three times lives in session logs and graduates to a CLAUDE.md entry, or further to a lint rule: same role, tighter constraint.

The boundary blurs in two ways. In the **overlap zone**, artifacts capture process knowledge incompletely: an ADR, a regression test, or a comment like `// Retries capped at 3 -- see incident #412` records the conclusion without the deliberation. The memory system holds the surrounding context rather than duplicating the artifact. The **aspiration gap** is knowledge that belongs in project artifacts but was never written down: conventions, implicit invariants. Memory captures it by default, as a safety net. Hence the substrate formulation: **project artifacts are curated projections of memory.**

### Graduation table

| Pattern | Graduation trigger | Destination | Role |
|---|---|---|---|
| Decision debated across sessions | "Why did we decide X?" is expensive to answer | ADR linking to source sessions | Knowledge |
| Rejected alternative re-proposed | Agent proposes the rejected option | Cue keyed on the rejected alternative | System-definition |
| Same workflow in 3+ sessions | Repetition detection | Procedure, skill, or script | System-definition |
| Same mistake corrected 2+ times | Correction frequency | Convention, CLAUDE.md entry, or lint rule | System-definition |
| Correction with instructive rationale | Reasoning worth preserving | Companion note or ADR | Knowledge |
| Same orientation needed each session | Recurring first-message pattern | CLAUDE.md entry | System-definition |
| Context needed to understand code | Explanation given in session | Code comment | Knowledge (usually) |
| Approach tried and abandoned | Approach explored and rejected | Negative-result record + "why not X?" index | Knowledge |

The meta-pattern is observation, accumulation, recognition, distillation, placement, provenance. Recognition is the bottleneck: it can be automated for clear triggers (correction counts, repetitions) but only flagged and assisted where judgment is needed, such as whether a decision warrants an ADR.

Every graduated artifact carries a maintenance obligation; session logs, being append-only, carry none. So premature graduation is worse than late graduation: graduate only when retrieval cost exceeds maintenance cost.

### The reach heuristic

Reach — how broadly something applies — decides graduation, but asymmetrically across roles. A knowledge artifact earns promotion when its claim applies across many situations. A cue earns promotion when it fires accurately in the situations it covers, often enough to earn its context budget; a narrow cue that fires accurately beats a broad one that misfires. Moving a correction into CLAUDE.md makes it fire every session and also makes every session pay if it is wrong.

Reach is usually unknown when an observation is made. A connection-pool race condition may be a one-off or the third instance of a pattern about shutdown ordering in async resource pools. Reach is revealed by accumulation, when several low-reach observations cluster on one structural pattern. So: accumulate promiscuously, then graduate on revealed reach. Revealing reach is the recognition step of the promotion pipeline.

## Alternatives considered

**Three layers instead of four.** Collapsing observation and episode into one "indexed memory" layer was rejected because atomic lookup and narrative retrieval need different indexing, and one interface serving both adds complexity without payoff. The two share storage but stay distinct.

**A single unified retrieval pipeline.** Treating the two roles as phases of one search-and-rank flow was rejected because the consumers differ: a question-asker navigates from a query, while an acting agent needs policy injected without asking.

**Extraction at session end only, no backfill.** Rejected because it couples capture speed to extraction quality. Retaining traces so extraction can be rerun and improved is the structural advantage of storing everything.

**A binary memory/project split.** Routing each artifact to one store was rejected because the boundary is patterned across the class/role grid, not by artifact kind. The adopted framing treats memory as the substrate from which project artifacts are distilled.

## Open problems

**Inspectability versus learnability of retrieval policy.** Inspectable rules are debuggable and auditable but brittle beyond the cases their authors anticipated. Learned policies (AgeMem's RL-trained policy, for example) adapt but are opaque and need an oracle open-ended domains may lack. A hybrid is likely: inspectable heuristics by default, learned overrides where volume allows. The interface — when an override should supersede a rule, and how to detect drift from the heuristic baseline — is unsolved.

**Cross-session structural pattern detection.** "Deploy failed: staging config not updated" (session 12), "migration failed: test env config stale" (28), and "flag rollout broke: production config out of sync" (45) are each low-reach. Together they reveal a high-reach pattern: configuration has no single source of truth. Detecting the cluster requires recognizing shared causal structure without shared keywords. This is costly and speculative, where the agency trilemma bites hardest; periodic deep-analysis passes may be needed.

**The oracle problem for discoveries.** Corrections have an explicit oracle, preferences a statistical one, and procedures a structural one. Discoveries have only later use, a trailing indicator. Discovery recognition may stay semi-manual.

**The ephemeral-computation trap.** If candidates never promote, the system looks like it learns without learning. A candidate store that fills and is never reviewed is ephemerality with extra steps. The promotion filter must run and someone must review its output. This operational problem is the most likely failure mode in practice.

**Scale.** At the target scale the observation layer holds tens of thousands of entries and the library suits one curator. Teams (conflicting preferences, concurrent streams) and very long-lived projects (where the observation layer itself becomes a search problem) are deferred. Progressive disclosure should scale beyond flat search, but cross-session pattern detection grows combinatorially harder with session count.

## A practical build order

Each step is useful on its own.

1. **Session logging.** Cheap, needs no extraction, and creates the substrate. Raw traces already answer "what happened in session X?"
2. **Correction extraction.** Easiest type, strongest oracle. A schema-constrained pass at session end stores corrections as typed cues and surfaces them before a corrected mistake recurs.
3. **Preference and procedure extraction.** Once roughly 50+ sessions accumulate, run periodic passes for accept/reject patterns and recurring tool-call sequences.
4. **Episode layer.** Compress identifiable multi-session work units, enabling "have we tried this before?"
5. **Promotion pipeline.** Connect the candidate store to the library, starting with high-confidence, high-frequency promotions (corrections seen three times become conventions), then extending to lower-confidence types.

Session logging alone beats no memory, and correction extraction alone stops repeated mistakes. The full architecture is the eventual target.
