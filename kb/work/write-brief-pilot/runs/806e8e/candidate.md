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

Storage is cheap: disk costs little, text compresses well, and append-only logs need no schema design. The binding constraint is *context* -- the finite window of tokens an agent can attend to during one inference call. Context is the only channel through which the agent receives instructions, accesses knowledge, and reasons toward action. Everything competes for the same space, and the space degrades well before it fills: more material can dilute instructions, contaminate scopes, and distort interpretation below the token limit.

This inverts the usual design. Traditional systems optimize storage and treat retrieval as a lookup. An agent memory system should store aggressively -- all session logs, intermediate artifacts, and observations -- and put the design effort into deciding which fraction of the store enters the context for a given task.

"Store everything" is a bet, not an axiom. It trades storage cost for indexing overhead, search pollution risk, and privacy exposure, and bets that selective retrieval can manage those costs. It puts the hard problem where the scarce resource is: attention, not disk.

## Memory plays two roles

The [axes of artifact analysis](./axes-of-artifact-analysis.md) name a **role** axis: an artifact is consumed either in a **knowledge role** (as fact; durable writes grow the agent's reach) or a **system-definition role** (as policy; durable writes change the agent's disposition). The role is relational: the same note, "we use URL-path versioning," is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the agent's next API design.

The two roles need different machinery:

- **Knowledge retrieval** answers questions posed at consumption time. It fits navigation: start with a question, follow links. Standard RAG optimizes for this. Failure mode: nobody asks the question.
- **System-definition activation** injects policy when a matching situation occurs. It fits triggered activation: watch the agent's proposed action and surface the constraint before commitment. This is the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md). Failure mode: relevant policy is stored but never fires.

Most agent-memory systems optimize for knowledge-role retrieval and underserve the system-definition role, which is where [continual learning requires governing behaviour-changing writes](./continual-learning-requires-governing-behaviour-changing-writes.md). "Adding RAG is learning" holds for the knowledge role and is empty for the system-definition role.

Session logs are the common substrate. One correction in session 47 can produce both a knowledge artifact (an ADR answering "why approach B?") and a system-definition artifact (a cue that fires when a future session proposes approach A). The extraction pipeline must produce both, and retrieval must serve both consumption patterns.

## Why existing approaches fall short

A comparison of eleven agent memory systems -- from vector-first fact stores (Mem0) through knowledge graphs (Graphiti) to filesystem-first curated systems (Ars Contexta, commonplace) -- shows three structural problems that no current system fully solves.

**The agency trilemma.** Who decides what to remember? If the agent manages its own memory (Letta), it has full context but spends reasoning tokens on housekeeping. If an external service does (Mem0, Graphiti, Cognee), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-manage (commonplace, Ars Contexta), curation quality is highest and throughput lowest. AgeMem trains the memory policy with reinforcement learning, but that needs a task-completion oracle that open-ended domains may lack, and the learned policy is opaque. No system combines high agency, high throughput, and high curation quality.

**Search versus navigation.** Mem0, Graphiti, and Cognee treat knowledge as something to *search*: embed a query, return top-k. Ars Contexta and commonplace treat it as something to *navigate*: follow articulated links. Search-first systems score well on QA benchmarks, but QA accuracy does not measure whether the agent can follow a chain of decisions or trace a correction back to the episodes that established it. Neither pattern serves the system-definition role, which needs a third one -- **triggered activation** on the agent's proposed action. QA benchmarks do not test it, which is one reason no reviewed system closes the activation gap.

**Extraction is automated; synthesis is not.** Every system can extract structured knowledge from unstructured input. Almost none can synthesize across existing knowledge: produce new insights, recognize that two threads should merge, or reformulate entries. A store-everything design has a structural advantage here: with complete logs retained, synthesis can be attempted retrospectively and rerun as techniques improve.

## Architecture: four layers of progressive distillation

A store-everything system without structure is a haystack. The architecture adds two intermediate layers between raw logs and curated notes:

**Layer 1: Trace.** Complete, append-only session logs -- every interaction, tool call, model output, and user message, with timestamps and session identifiers. Traces are the ground truth and the substrate for all higher layers. They answer "what exactly happened in session X?" and nothing else efficiently. They serve provenance and offline extraction; the agent never loads raw traces into a working context.

**Layer 2: Observation.** Extracted atomic facts: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each is typed, timestamped, linked to its source session, scored for confidence and importance, and **tagged with its role**. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). Ambiguous types yield paired artifacts: a decision produces a knowledge record ("why we chose A") and a cue ("if B is proposed, surface the reasoning for A"). ClawVault's scored, typed observations with promotion pathways are the closest precedent. The difference is that observations here are derived from stored traces, not extracted at interaction time, so capture speed is decoupled from extraction quality and extraction can be rerun and backfilled.

**Layer 3: Episode.** Compressed accounts of bounded work units, possibly spanning sessions: goal, scope (session range and time period), outcome, key decisions (pointing to observations), lessons, open threads, and library artifacts produced. Observations answer "have we seen this before?" (lookup). Episodes answer "have we tried something like this, and what happened?" (narrative).

**Layer 4: Library.** Curated notes, structured claims, indexes, procedures, and ADRs. The design leaves the library as it is and gives it richer input channels and a principled path from raw experience.

**Why four layers.** With only traces and library, every transition from log to note needs a human to read the trace -- the bottleneck the system exists to remove. With a single intermediate layer, one interface must serve both atomic lookup and narrative retrieval, which need different indexing, extraction, and promotion; observations and episodes may share storage, distinguished by type tags, but should be treated as different objects. A fifth layer (say, splitting the library into working and reference knowledge) adds a boundary that inhibits connections, while frontmatter types, status fields, and links already differentiate within the library.

The layers also give the context scheduler progressive disclosure: scan observation summaries and episode goals first, load a full episode or observation cluster if relevant, follow the pointer to the trace only when provenance is needed.

### How material moves between layers

The promotion pathways matter more than the layers.

**Trace to Observation (extraction).** Runs automatically after a session ends, and again on older traces when the extractor improves. An LLM extracts typed observations with confidence, importance, and a source pointer. Failure modes: over-extraction (trivia floods the layer), under-extraction (subtle preferences missed), and misclassification (a correction tagged as a preference loses its corrective force). Fully reversible, because traces are kept.

**Observation to Episode (compression).** Triggered by work-unit completion, periodic consolidation, or human request. Harder than extraction because it requires editorial judgment about what mattered. Boundary heuristics: shared file paths, shared task references, temporal proximity, topic similarity, and explicit markers ("starting work on X" / "done with X") when available.

**Observation to Library (promotion).** Triggered by recurrence (seen N times across M sessions), importance, or human request. Thresholds should vary by type: a preference may need three or more independent sessions to be stable, while one high-stakes architectural decision may warrant immediate promotion to an ADR.

**Episode to Library (distillation).** Usually deliberate. One episode may yield several library artifacts, and the episode lets a reviewer check whether a distilled claim faithfully represents what happened.

**Library to Observation (backflow).** Library notes should generate activation cues. A note saying "prefer staging specific files over `git add -A`" should produce a cue that fires when a session involves git staging. Without backflow, library knowledge is stored but never activated.

### Lifecycle and role: orthogonal tags on one store

Artifacts have different lifecycles. Operational observations churn fast (yesterday's debugging procedure may be superseded today); self-observations evolve slowly (a preference seen across five sessions is likely stable); knowledge observations accumulate. Separate stores would inhibit cross-space connections, so the architecture tags observations by lifecycle and uses the tag in promotion: recurring knowledge promotes to a library note, a recurring operational observation to a procedure, a recurring self-observation to CLAUDE.md.

The role tag is independent of the lifecycle tag. A self-observation is usually system-definition but can be knowledge; an operational observation is usually system-definition but becomes knowledge when someone asks "how do we debug this class of bug?" Lifecycle answers *when does this expire?*; role answers *how is this consumed?* Retrieval uses lifecycle to weight recency and role to select the activation mechanism.

## Retrieval and activation

The hardest problem is not extraction or storage but activation: a system can store relevant knowledge, produce it on direct query, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query.

### Retrieval splits by role, not by content

The central design move is two retrieval pipelines over one store. A single search-and-rank flow serving both roles does not work, because the consumers differ: a question-asker starts from a query, while an acting agent needs policy injected without asking.

**Knowledge-role retrieval** serves questions such as "why did we do X?" The interface is navigable: embedding search over descriptions as a first-pass filter, then articulated library links. Its failure mode -- the question is never asked -- lies outside the pipeline; it is an elicitation problem the memory system can assist but not solve.

**System-definition activation** serves the agent's in-flight work. The interface is a watcher, not a query: cues are indexed by action signature, preference domain, or situation template, and fire when the proposed action matches. Its failure mode -- the cue applies but never fires -- is the activation gap proper, and most of the design surface lives here.

The pipelines cross-reference: a fired cue can point into the knowledge layer ("this correction is part of a documented convention, see ADR 014"), and navigation can reveal cues attached to a note.

### Three stages of activation failure

**Cue match.** The task context must contain enough signal to trigger retrieval. Embedding similarity handles topical matches but fails when the connection is causal: session 47's correction about a deployment mistake will not embed near session 312's code-writing task, even though the lesson applies.

**Priority arbitration.** In a store with thousands of sessions, any task matches dozens of items, and loading them all destroys context efficiency.

**Commitment.** Even with the right knowledge loaded, the agent may follow training-time defaults instead. It behaves like an expert witness: accurate on whatever is asked, silent on concerns nobody raised.

### Typed cue indexes (cue match)

The system extracts typed cues at ingestion time instead of searching raw logs at retrieval time. Each type has its own retrieval signature. A **correction cue** matches the action the agent is about to take:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches the decision space, a **precedent cue** the situation description, and a **procedure cue** the goal. This is what bridges session 47 and session 312: when the session 312 plan includes dropping a column, the trigger matches and the lesson loads before the agent writes the migration.

Matching is the hard part: "database migration that removes a column" must match "drop column deprecated_flag." Three approaches compose: action-type classification (both classify as `schema-migration:column-removal`), embedding similarity with a low threshold (accept false positives over false negatives), and LLM-judged relevance for high-consequence cues.

### Priority arbitration under context budgets

- *Recency-weighted relevance* with a long tail: a correction from 500 sessions ago still matters if the mistake pattern recurs.
- *Consequence weighting*: sessions with corrections, user frustration, or rework likely carry more action-relevant knowledge. The log supplies the signals: messages after a correction, sentiment markers, explicit severity statements.
- *Frequency*: a cue that fires across many sessions is more likely to matter.
- *Budget allocation by type*: fixed context slots for corrections, active preferences, and precedents, so no cue type crowds out the others.

### Commitment: from passive context to imperative instruction

- *Imperative framing.* Not "previously, X failed because Y" but "BEFORE doing X, verify Y because Z failed in session 47." Perspective assignments outperform undirected review in elicitation studies; the same principle plausibly applies to memory.
- *Checkpoint insertion.* For high-consequence cues, add a verification step to the task plan: "Step 3a: check whether this deployment includes schema changes; if yes, review the session 47 correction."
- *Contradiction surfacing.* When the proposed action contradicts a stored correction or preference, say so: "You are about to use approach A. In session 47, A failed because Z. The established alternative is B."

### Search, navigation, and activation compose

Search works over the lower layers, where items are numerous and weakly structured. Navigation works over the upper layers, where items are fewer and richly linked. Activation works over system-definition cues in any layer, because its trigger is the proposed action. For an agent about to write a database migration: activation fires matching cues (corrections as imperative instructions, preferences into their budget, procedures as checklists); search surfaces related knowledge records (past migration decisions, negative results, draft ADRs); navigation follows their links into the library. The agent gets corrections, past decisions, and architectural constraints without loading a raw trace.

## Learning from session logs: the extraction taxonomy

Session logs carry at least four signal types, differing in oracle clarity, extraction difficulty, role, and destination. Corrections, preferences, and procedures are system-definition; discoveries start as knowledge and may acquire a system-definition companion. Ranked easiest to hardest:

**Corrections (system-definition): the strongest signal.** The user says "no, do X instead" or rejects a tool call. The log records the wrong output, the rejection, and the corrected direction -- an explicit negative paired with a positive. Pi Self-Learning's extraction schema, `{"mistakes": [...], "fixes": [...]}`, targets exactly this. A correction seen in two different sessions is not a fluke, so the promotion threshold can be two. The graduated artifact moves along the codification gradient within the system-definition role: a CLAUDE.md rule or style-guide convention (prose), then a lint check or validation script (symbolic). A companion note or ADR may record *why*. Example: the user corrects alphabetical import sorting to "stdlib / third-party / local"; on the second occurrence it becomes a documented preference, and on the third the question is whether it should be a pre-commit hook.

**Preferences (system-definition): distributed signal, inferential extraction.** The user consistently accepts some patterns and rejects others without stating a rule. Each accept/reject is clear, but the rule connecting them ("short commit messages") must be inferred across sessions. Detect bottom-up (cluster decisions by domain and look for features that predict acceptance) or top-down (periodically ask an LLM which preferences explain the last 50 decisions in a domain). A reasonable threshold: five or more decisions across three or more sessions with over 80% consistency.

**Procedures (system-definition): sequence alignment.** The same workflow recurs with different content. Tool-call sequences are more reliable signals than natural-language descriptions: four sessions containing `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]` form a detectable pattern even when the conversations differ. The graduated artifact is an instruction document (prose, if steps need judgment), a skill (if it can be parameterized), or a script (if fully deterministic). Role stays constant while the artifact is constrained more tightly.

**Discoveries (knowledge, sometimes system-definition): no oracle.** An insight -- a connection, a principle, a unifying abstraction -- is the highest-value extraction and the hardest to detect, because it is a one-off event and "feels important" is not a verifiable signal. Weak heuristics: explicit markers ("write this down"), claims linking previously unlinked notes, unusual elaboration depth, and later reference. Enter discoveries as low-confidence candidates and promote on reference frequency. Assign role at graduation, since operational implications show up only with use: a discovery about async resource pool failures may yield a note and a cue on async cleanup code.

### The promotion pipeline

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. Extraction should be narrow and schema-constrained: one prompt per signal type, each with its own schema, works far better than "summarize the session." And the candidate store must be separate from the library, because mixing unvetted candidates into curated knowledge degrades retrieval precision for everything.

### Session logs as composite oracle

Most memory systems lack a signal for "was this memory operation good?" Session logs offer many weak ones: corrections, accept/reject patterns, explicit user markers, questions asked, elaboration investment, session-end state (was the goal met?), return to a topic later, and abandoned investigations. Reviewed systems use few of them -- Pi Self-Learning uses corrections, ClawVault importance plus recurrence, cass-memory helpful/harmful feedback plus score decay. The bet is that combining many weak signals yields a soft oracle good enough to be practical.

## Knowledge-role use cases

The system-definition side -- preventing a rejected approach from being proposed again -- runs through the cue index. Two knowledge-role uses carry most of the value:

**Decision provenance.** The recurring high-value question is *why did we do it this way and not that way?* ADRs answer it, but they are written after the fact and cover only what the author thought to record. Session logs keep the deliberation: alternatives, reasoning, active constraints, objections. This enables a semi-automated ADR pipeline: flag sessions where a decision was debated, pre-assemble a draft (alternatives, reasoning, selection, consequences), and have a human verify and connect it. The "alternatives considered" section, the hardest part to reconstruct, is what logs preserve most directly. A drafted ADR often gets a companion cue that fires when a rejected alternative is proposed.

**Negative results.** "What was tried and abandoned" has no home in standard project structure; code shows what was built, not what was discarded. Extract negative results as records (approach, failure reason, source session, link to the decision that followed), indexed by approach name so "why didn't we do X?" finds them. When recurrence would be costly, add a cue keyed on the approach.

## Where memory ends and the project begins

The naive boundary -- "memory stores what project artifacts don't preserve" -- is necessary but not sufficient. Project artifacts themselves span the form/role grid: code, tests, and lint rules are symbolic system-definition; documentation and ADRs are prose knowledge; CLAUDE.md is prose system-definition. Against each, the memory system adds the reasoning and process behind it: code says "retry with exponential backoff," memory adds "a circuit breaker interacted badly with the connection pool in session 47."

CLAUDE.md (or any always-loaded instruction file) is the telling case. **CLAUDE.md is compiled system-definition; the memory system is the source.** A correction given three times lives in the logs and graduates to a CLAUDE.md entry, or further to a lint rule -- same role, tighter constraining.

The boundary blurs in two ways. Some artifacts belong to both: an ADR, or a comment like `// Retries capped at 3 -- see incident #412`, records a conclusion without the deliberation, and memory holds the surrounding context rather than duplicating it. And much knowledge that *should* be in project artifacts (undocumented conventions, implicit invariants) is not; memory catches it by default, but its proper home is elsewhere. So the memory system is not a parallel store with a binary routing rule: **it is the substrate from which project artifacts are distilled**, and project artifacts are curated projections of it.

### Graduation pathways

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

Every graduated artifact creates a maintenance obligation -- an ADR must stay current, a lint rule must change with conventions -- while logs are append-only and impose none. So premature graduation is worse than late graduation: graduate only when the retrieval cost of leaving knowledge in memory exceeds the maintenance cost of the artifact.

### The reach heuristic

*Reach* -- how broadly an insight applies -- decides differently per role. A knowledge artifact earns promotion when its claim applies widely ("systems optimized for normal-load efficiency sacrifice overload resilience" belongs in the library; "the bug in PR #247 was a pool race" can stay in logs). A system-definition artifact earns promotion when its trigger fires accurately and often enough to pay for its context budget; a narrow, accurate cue beats a broad one that misfires. Graduating a correction into CLAUDE.md makes it fire every session and so multiplies the cost of being wrong.

Reach is usually invisible at first observation. The pool race may be a one-off or the third instance of "async resource pools need explicit shutdown ordering." Reach is revealed when low-reach observations cluster around one structural pattern. Hence the two-phase dynamic: accumulate promiscuously, then graduate on revealed reach.

## What remains open

**Inspectable versus learned retrieval policy.** Inspectable rules can be debugged and refined, but cannot anticipate every domain and grow brittle at scale. Learned policies (AgeMem's RL-trained policy) adapt, but are opaque and need an oracle that open-ended domains may lack. The likely answer is inspectable heuristics by default with learned overrides where volume allows; when an override should supersede a rule, and how to detect drift from the heuristic baseline, is unsolved.

**Cross-session structural patterns.** "Deploy failed: staging config not updated," "migration failed: test env config stale," and "rollout broke: production config out of sync" share no keywords, yet together reveal a high-reach pattern -- configuration lacks a single source of truth. Detecting shared causal structure takes expensive reasoning on a speculative payoff, the agency trilemma at its sharpest. No current system does it; periodic (weekly or monthly) deep-analysis passes over accumulated observations may be required.

**No oracle for discoveries.** Corrections, preferences, and procedures each have an oracle (explicit rejection, statistical consistency, recurring sequences). Discoveries have only later use, a trailing indicator. Discovery extraction may stay semi-manual; build the easier types first and accumulate volume before testing discovery heuristics.

**The ephemeral computation trap.** If candidates never promote, the system looks like it learns without learning: an unreviewed candidate store is ephemerality with extra steps. The promotion filter must run and someone must review its output. This operational failure is the most likely one in practice.

**Scale.** The design targets one user and one project: hundreds to low thousands of sessions, tens of thousands of observations, hundreds of episodes, one curator. Teams (conflicting preferences, concurrent streams) and very long-lived projects are open. Progressive disclosure should scale further than flat search, but cross-session pattern detection gets combinatorially harder with session count. Defer this until the single-user case works.

## A practical starting point

The four layers need not exist on day one. Build in order of difficulty:

1. **Session logging.** Capture complete traces. Cheap, needs no extraction, and creates the substrate; raw traces already support "what happened in session X?" and manual search.
2. **Correction extraction.** Strongest oracle, easiest extraction. Run a schema-constrained pass at session end, store corrections as typed cues with triggers, and surface them before the agent repeats a mistake.
3. **Preference and procedure extraction.** After roughly 50+ sessions, run periodic passes for consistent accept/reject patterns and recurring tool-call sequences.
4. **Episode layer.** Once work units are identifiable, compress multi-session efforts into episodes to support "have we tried this before?"
5. **Promotion pipeline.** Connect the candidate store to the library, starting with high-confidence, high-frequency promotions (a correction seen three times becomes a convention), and widen as the system matures.

Each step is useful alone: logging beats no memory, and correction extraction alone stops repeated mistakes.
