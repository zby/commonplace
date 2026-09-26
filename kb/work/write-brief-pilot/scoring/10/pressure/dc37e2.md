---
description: Design study of an agent memory system under a store-everything hypothesis — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction and graduation
type: types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Designing a Memory System for LLM-Based Agents

## The premise: storage is cheap, context is scarce

The main design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Disk is cheap, text compresses well, and append-only logs need no schema design. The binding constraint is *context*: the finite window of tokens an agent can attend to during one inference call. Context is the only channel through which the agent receives instructions, accesses knowledge, and reasons toward action. Everything competes for that space, and the space degrades before it fills: more material can dilute instructions, contaminate scopes, and distort interpretation below the token limit.

This inverts the usual design. Traditional systems optimize storage and treat retrieval as a lookup. This design stores aggressively — all session logs, intermediate artifacts, and observations — and puts the design effort into retrieval and activation: the machinery that decides which fraction of the store enters the context for a given task.

"Store everything" is a hypothesis, not an axiom. It trades storage cost for indexing overhead, search pollution risk, and privacy exposure, and it bets that selective retrieval can manage those costs. Whether it can is an open question (see [What remains open](#what-remains-open)). What the premise does settle is where the hard problem sits: in attention, not disk.

## Memory plays two roles

A memory system does two things that look similar but differ in how stored content is consumed and what a durable write changes. A [knowledge artifact](./definitions/knowledge-artifact.md) is consumed as fact or advice; durable writes grow what the agent can answer. A [system-definition artifact](./definitions/system-definition-artifact.md) is consumed as policy; durable writes change what the agent does. The [axes of artifact analysis](./axes-of-artifact-analysis.md) treats this as behavioral authority over a consumption path.

The distinction is relational, not structural. A note saying "we use URL-path versioning" is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the agent's next API design.

The two roles need different machinery:

- **Knowledge retrieval** answers questions posed at consumption time. It fits search and navigation: start with a question, follow links. Standard RAG optimizes for this. Failure mode: nobody asks the question.
- **System-definition activation** injects policy when a matching situation occurs. It fits triggered activation: watch the agent's proposed action and surface the constraint before commitment. This is the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md). Failure mode: the policy is stored but never fires.

Most agent-memory systems optimize knowledge retrieval and underserve the system-definition role, which is the harder half of continual learning because it requires [governing behaviour-changing writes, not just storing content](./continual-learning-requires-governing-behaviour-changing-writes.md). "Adding RAG is learning" holds for the knowledge role and is empty for the system-definition role.

Session logs feed both roles. One correction in session 47 can produce a knowledge artifact (an ADR answering "why do we use approach B?") and a system-definition artifact (a cue that fires when a later session proposes approach A). Extraction must produce both, and retrieval must serve both.

## What existing systems leave unsolved

A comparison of eleven agent memory systems — from vector-first fact stores (Mem0) through knowledge graphs (Graphiti) to filesystem-first curated systems (Ars Contexta, commonplace) — shows three problems no current system fully solves.

**The agency trilemma.** Who decides what to remember? If the agent manages its own memory (Letta), it has full context but spends reasoning tokens on housekeeping. If an external service manages it (Mem0, Graphiti, Cognee), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-manage it (commonplace, Ars Contexta), curation quality is highest and throughput lowest. AgeMem trains the memory policy with reinforcement learning, which approaches all three goals but needs a task-completion oracle that open-ended domains may lack, and the learned policy is opaque. No system combines high agency, high throughput, and high curation quality.

**Search versus navigation, and neither activates.** Mem0, Graphiti, and Cognee treat knowledge as something to *search*: embed a query, return the top-k. Ars Contexta and commonplace treat it as something to *navigate*: follow articulated links and reason along them. Search-optimized systems score well on QA benchmarks, but QA accuracy does not measure whether an agent can follow a chain of decisions or trace a correction back to the episodes that established it. Both patterns serve the knowledge role. The system-definition role needs a third pattern, triggered activation, which QA benchmarks do not test. This is one reason no reviewed system closes the activation gap.

**Extraction is automated; synthesis is not.** Every system can extract structured knowledge from unstructured input. Almost none can synthesize across existing knowledge: produce new insights, recognize that two threads should merge, or reformulate entries for clarity. Here store-everything has a structural advantage: with complete logs retained, synthesis can be attempted retrospectively and rerun as techniques improve.

## Architecture: four layers of distillation

A store-everything system without structure is a haystack. The design uses four layers, each more distilled than the one below:

**Layer 1: Trace.** Complete session logs — every interaction, tool call, model output, and user message — as append-only records with timestamps and session identifiers. Traces are ground truth and provenance. They answer "what exactly happened in session X?" and nothing else efficiently. They serve offline extraction; the agent never loads raw traces into a working context.

**Layer 2: Observation.** Extracted atomic items: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each is typed, timestamped, linked to its source session, scored for confidence and importance, and **tagged with its role**. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). Others yield paired artifacts: a decision produces a knowledge record for "why we chose A" and a cue for "if B is proposed, surface the reasoning for A." ClawVault's scored, typed observations with promotion pathways are the closest precedent. The difference here is that observations are derived from stored traces rather than at interaction time, which decouples capture speed from extraction quality: extraction can be rerun, improved, and backfilled.

**Layer 3: Episode.** Compressed accounts of bounded work units that may span several sessions: goal, scope (session range and period), outcome, key decisions (pointing to observations), lessons, open threads, and library artifacts produced.

**Layer 4: Library.** Curated notes, structured claims, indexes, procedures, and ADRs. The design leaves the library as it is and gives it richer input channels and a pathway from raw experience to curated knowledge.

**Why four layers.** With only traces and library, every transition from log to note needs a human to read the trace — the manual bottleneck the system exists to remove. With one intermediate layer, that layer must serve both atomic lookup ("has this correction been given before?") and narrative retrieval ("what happened when we tried this approach?"). These need different indexing: a correction is a trigger-lesson pair, an episode is a compressed story. Observations and episodes can share storage, distinguished by type tags, but extraction, promotion, and retrieval should treat them as different objects. A fifth layer, such as splitting the library into working and reference knowledge, would add a boundary that inhibits links; frontmatter types and status fields already differentiate within the library.

The layers also give the context scheduler progressive disclosure: scan observation summaries and episode goals first, load the full episode or observation cluster if relevant, and follow the pointer to the trace only when provenance is needed.

### How material moves between layers

The promotion pathways matter more than the layers.

- **Trace → Observation (extraction).** Runs automatically after a session ends, and again over old traces when the extractor improves. An LLM extracts typed observations with confidence, importance, and a source pointer. Failure modes: over-extraction (trivial facts drown the layer), under-extraction (subtle preferences missed), and misclassification (a correction tagged as a preference loses its corrective force). Fully reversible, because traces are kept.
- **Observation → Episode (compression).** Triggered by work-unit completion, periodic consolidation, or request. Harder than extraction because it requires editorial judgment about what mattered. Boundary heuristics: shared file paths, shared task references, temporal proximity, topic similarity, and explicit markers ("starting work on X") when present.
- **Observation → Library (promotion).** Triggered by recurrence, importance, or request. The threshold should vary by type: a preference may need three or more independent sessions, while a single high-stakes architectural decision may warrant immediate promotion to an ADR.
- **Episode → Library (distillation).** Usually deliberate. One episode may yield several artifacts, and the episode lets a reviewer check that a distilled claim fits the full narrative.
- **Library → Observation (backflow).** Library notes should generate activation cues. A note saying "stage specific files, not `git add -A`" should produce a cue that fires when a session involves git staging. Without backflow, library knowledge is stored but inert.

### Lifecycle and role are separate tags on one store

Observations also differ in how fast they change. Operational observations churn (yesterday's debugging procedure may be superseded today). Self-observations about the user's preferences evolve slowly. Knowledge observations accumulate and are superseded rather than expiring. Separate stores would inhibit cross-space links, so the design tags each observation with a lifecycle space and uses the tag in promotion: recurrent knowledge promotes to a library note, a recurrent operational observation to a procedure, a recurrent self-observation to CLAUDE.md.

Lifecycle and role answer different questions — *when does this expire?* and *how is this consumed?* — and vary independently: an operational debugging observation is usually a cue to fire next time but is knowledge when someone asks "how do we debug this class of bug?" Retrieval uses lifecycle to weight recency and role to select the activation mechanism.

## Retrieval and activation

The hardest problem in the architecture is activation. A system can store relevant knowledge, produce it on direct query, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query.

### Two pipelines over one store

The central design move is one pipeline per role, sharing the observation store.

**Knowledge retrieval** serves questions such as "why did we do X?" The interface is navigable: embedding search over descriptions as a first-pass filter, then articulated links in the library. Its failure mode — the question is never asked — is an elicitation problem outside this pipeline.

**System-definition activation** serves the agent's in-flight work. The interface is not a query but a watcher: cues are indexed by action signature, preference domain, or situation template, and fire when the agent's proposed action matches. Its failure mode — the cue applies but never fires — is the activation gap proper, and most of the design surface lives here.

The pipelines cross-reference: a fired cue can point into the knowledge layer ("this correction belongs to a documented convention, see ADR 014"), and navigation can reveal a dormant cue attached to a note. A full retrieval for an agent about to write a database migration runs all three access patterns:

1. **Activation** fires cues whose triggers match the proposed action: corrections load as imperative instructions, preferences take a reserved context budget, procedures suggest a checklist. Activation works at any layer, because its trigger is the action rather than a query.
2. **Search** over the lower layers, where items are numerous and weakly structured, surfaces related knowledge records: past migration decisions, negative results, draft ADRs.
3. **Navigation** over the upper layers, where items are fewer and richly linked, follows links from those records to library notes.

The agent gets the relevant corrections, past decisions, and architectural constraints without loading a raw trace.

### Three stages of activation failure

Activation can fail at three stages, each with its own design surface:

- **Cue match.** The task context must carry enough signal to trigger retrieval. Embedding similarity handles topical matches but fails when the connection is causal: session 47's correction about a deployment mistake will not embed near session 312's code-writing task, even if the lesson applies.
- **Priority arbitration.** With thousands of stored sessions, any task matches dozens of items, and loading them all destroys context efficiency.
- **Commitment.** Loaded knowledge can still lose to training-time defaults. The agent behaves like an expert witness: accurate on what is asked, silent on concerns nobody raised.

### Cue match: typed cue indexes

Instead of searching raw logs at retrieval time, the system extracts typed cues at ingestion. Each cue type has its own retrieval signature. A **correction cue** matches the action the agent is about to take:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches the decision space, a **precedent cue** the situation description, and a **procedure cue** the goal. In session 47 the user corrects the agent's migration approach and the correction becomes a cue. In session 312, when the task plan includes dropping a column, the trigger matches and the lesson loads before the agent writes the migration.

The matching is the hard part: "migration that removes a column" must match "drop column deprecated_flag." Three approaches compose: action-type classification (both classify as `schema-migration:column-removal`), embedding similarity with a low threshold (accepting false positives over false negatives), and LLM-judged relevance for high-consequence cues.

### Priority arbitration under a context budget

When too many cues match, four mechanisms decide what to surface:

- **Recency with a long tail** — recent sessions get a boost, but a correction from 500 sessions ago still counts if the mistake recurs.
- **Consequence weighting** — sessions with corrections, user frustration, or rework rank higher. The log supplies signals: messages needed after a correction, sentiment, explicit severity.
- **Frequency** — a cue that fires across many sessions is more likely to matter.
- **Budget by type** — fixed context slots for corrections, preferences, and precedents, so no cue type crowds out the others.

### Commitment: from passive context to instruction

Three mechanisms make loaded knowledge get used:

- **Imperative framing.** Not "previously, X failed because Y" but "BEFORE doing X, verify Y because X failed in session 47." Perspective assignments outperform undirected review in elicitation studies, and the same principle plausibly applies here.
- **Checkpoint insertion.** For high-consequence cues, insert a verification step into the task plan.
- **Contradiction surfacing.** When the proposed action contradicts a stored correction, say so: "You are about to use approach A. In session 47, A failed because Z. The established alternative is B."

## Learning from session logs

Session logs carry four signal types. They differ in oracle clarity, extraction difficulty, role, and destination. Easiest first:

**Corrections (system-definition).** The user says "no, do X instead" or rejects a tool call. The log holds the wrong output, the rejection, and the corrected direction — the clearest oracle in the system, an explicit negative paired with a positive. Pi Self-Learning's extraction schema targets exactly this: `{"mistakes": [...], "fixes": [...]}`. Two occurrences in different sessions are enough to promote. The graduated artifact moves along the codification gradient within the system-definition role — CLAUDE.md rule, then style-guide convention, then lint check — optionally with a companion note or ADR explaining why.

**Preferences (system-definition).** The user consistently accepts some patterns and rejects others without stating a rule. No single session holds enough evidence; extraction must infer the latent variable ("short commit messages") from scattered accept/reject decisions. Detection runs bottom-up (cluster decisions by domain, find features that predict acceptance) or top-down (ask an LLM which preferences explain the last 50 decisions in a domain). A reasonable threshold: five or more decisions across three or more sessions, over 80% consistent.

**Procedures (system-definition).** The same workflow recurs with variations. Tool-call sequences are more reliable signals than natural-language descriptions: four sessions sharing the subsequence `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]` show a pattern even when the conversation differs. The artifact tightens along the constraining gradient — instruction document, skill, script — while its role stays constant.

**Discoveries (knowledge, sometimes system-definition).** An insight emerges during work. These are the most valuable extractions and the hardest to detect, because a discovery is a one-off event with no explicit rejection or statistical pattern. Detection heuristics are all weak: explicit markers ("write this down"), claims linking previously unlinked notes, unusual elaboration depth, and later reference. Discoveries enter as low-confidence candidates and promote on reference frequency. Role is assigned at graduation, because a discovery's operational implications show only with use: a discovery about async resource pools may later gain a cue that fires on async cleanup code.

### The promotion pipeline

All four types share one pipeline:

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. Extraction should be narrow and schema-constrained — a separate prompt per signal type, not "summarize the session." And the candidate store must be separate from the library, because unvetted candidates mixed into curated knowledge degrade retrieval precision for everything.

### Session logs as a composite oracle

Most memory systems lack a signal for "was this memory operation good?" Session logs offer many weak ones: corrections, accept/reject patterns, explicit markers ("this is important"), questions asked, elaboration investment, whether the session goal was reached, return visits to a topic, and abandoned investigations. Reviewed systems use few of these: Pi Self-Learning uses only corrections, ClawVault importance plus recurrence, cass-memory helpful/harmful feedback plus decay. The bet is that a soft oracle combined from many weak signals can close enough of the gap to be practical.

## What the memory system is for, beside the project

A software project already has code, tests, docs, ADRs, CLAUDE.md, and lint rules. These split across roles: code, tests, lint rules, and CLAUDE.md steer behavior; docs and ADRs are knowledge. The memory system's contribution to each is the reasoning and process that produced it. Code says "retry with exponential backoff"; memory adds "we tried a circuit breaker in session 47 and it interacted badly with the connection pool." A test asserts an invariant; memory adds the bug that motivated it. An ADR records what was chosen; session logs also preserve the alternatives discarded, which is the part of an ADR most expensive to reconstruct.

The boundary is not a binary split. Some artifacts belong to both sides: a comment like `// Retries capped at 3 -- see incident #412` is code and decision memory at once. Such artifacts record the conclusion without the deliberation; memory holds the surrounding context rather than duplicating them. And much knowledge that belongs in project artifacts is not there yet — undocumented conventions, implicit invariants. Memory captures it by default until someone writes it down.

The working formulation: **the memory system is the substrate from which project artifacts are distilled.** CLAUDE.md is compiled system-definition; the memory system is its source. Three repeated corrections live in the logs until they graduate into a CLAUDE.md entry, or further into a lint rule.

### Graduation pathways

One source pattern can graduate into artifacts in both roles:

| Pattern | Graduation trigger | Destination | Role |
|---|---|---|---|
| Decision debated across sessions | "Why did we decide X?" is expensive to answer | ADR linking back to source sessions | Knowledge |
| Decision with a commonly re-proposed rejected alternative | Agent re-proposed rejected option | Cue keyed on the rejected alternative | System-definition |
| Same workflow in 3+ sessions | Repetition detection | Documented procedure, skill, or script | System-definition |
| Same mistake corrected 2+ times | Correction frequency | Convention, CLAUDE.md entry, or lint rule | System-definition |
| Same mistake, with instructive rationale | The reasoning is worth preserving | Companion note or ADR | Knowledge |
| Agent needs same orientation each session | Recurring first-message pattern | CLAUDE.md entry | System-definition |
| Context needed to understand specific code | Explanation given during session | Code comment | Knowledge (usually) |
| Tried and abandoned approach | Approach explored and rejected | Negative-result record indexed by approach name | Knowledge |

Two use cases show the pairing. For **decision provenance**, the system can pre-assemble a draft ADR from sessions where alternatives were debated (alternatives, reasoning, selection, consequences) for human review, and pair it with a cue that fires when the agent proposes a rejected alternative. For **negative results** — which have no home in standard project structure, since code shows only what was built — a structured record (approach, failure reason, source session, the decision that followed) answers "why didn't we do X?", and a severe one also gets a cue that prevents the attempt.

Recognition is the bottleneck in every pathway. Where triggers are countable (correction frequency, repetition), it can be automated; where it needs judgment (is this decision load-bearing enough for an ADR?), the system can only flag and assist.

Every graduated artifact creates a maintenance obligation: an ADR must stay current, a lint rule must change with conventions. Logs carry no such obligation. So premature graduation is worse than late graduation: graduate when the cost of retrieving from memory exceeds the cost of maintaining the artifact.

### Reach decides graduation, and is revealed by accumulation

How broadly an insight applies decides where it belongs. "Systems optimized for normal-load efficiency sacrifice overload resilience" belongs in the library; "the bug in PR #247 was a race in the connection pool" can stay in the logs. The test differs by role. A knowledge artifact earns promotion by applying widely. A system-definition artifact earns it by firing accurately in the situations it covers, often enough to pay for its context budget; a narrow cue that fires correctly beats a broad one that misfires. Graduating a correction into CLAUDE.md makes it fire every session, and multiplies the cost of being wrong.

Reach is often invisible at first sight. The pool race may be a one-off or the third instance of a pattern where async resource pools need explicit shutdown ordering. Only accumulation reveals it: when several narrow observations cluster around one structural pattern, the pattern should graduate. Hence the two-phase dynamic: accumulate indiscriminately, then graduate on revealed reach.

## Alternatives rejected

- **A single unified retrieval pipeline.** Rejected because a question-asker navigates from a query, while an acting agent needs policy injected without asking.
- **Extraction at session end only, no backfill.** Rejected because it couples capture speed to extraction quality and gives up store-everything's main structural advantage.
- **A binary memory/project split**, routing each artifact to one store. Rejected because the same content appears on both sides with different consumers; memory is the substrate, not a parallel store.
- **Three layers** was rejected for the reasons given under [Why four layers](#architecture-four-layers-of-distillation).

## What remains open

**The costs of storing everything.** Indexing overhead, search pollution, and privacy exposure are the price of the premise. This design does not show that selective retrieval keeps them manageable, how retention should respond to sensitive content, or at what volume indexing cost outgrows the benefit of complete traces.

**Inspectable versus learned retrieval policy.** Inspectable rules are debuggable and auditable but brittle across domains. Learned policies, such as AgeMem's, adapt but are opaque and need a clear oracle. A hybrid — heuristic rules by default, learned overrides where volume allows — is the likely answer, but when an override should win and how to detect drift from the heuristic baseline are unsolved.

**Cross-session structural patterns.** Three incidents — a deploy failing on stale staging config, a migration failing on stale test config, a rollout breaking on out-of-sync production config — share no keywords but reveal one high-reach pattern: configuration lacks a single source of truth. Detecting such clusters needs deep, expensive reasoning over speculative value. Periodic deep-analysis passes, weekly or monthly, may be the practical form.

**The oracle for discoveries.** Corrections have an explicit oracle, preferences a statistical one, procedures a structural one. Discoveries have none except later use, which trails extraction. Discovery recognition may stay semi-manual.

**The ephemeral computation trap.** If candidates are extracted but never promoted or reviewed, the system looks like it learns without learning. This is an operational problem, not a technical one, and it is the most likely failure in practice.

**Scale.** The design targets one user and one project: hundreds to low thousands of sessions, tens of thousands of observations, hundreds of episodes, one curator. Teams (conflicting preferences, concurrent work) and very long-lived projects are untested. Progressive disclosure should scale further than flat search, but cross-session pattern detection gets combinatorially harder as sessions grow.

## A practical starting point

The layers need not arrive at once. Build in order of difficulty:

1. **Session logging.** Cheap, needs no extraction, and creates the substrate. Raw traces already support manual search.
2. **Correction extraction.** The strongest oracle. A schema-constrained pass at session end stores corrections as typed cues and surfaces them when the agent is about to repeat a mistake.
3. **Preference and procedure extraction.** Once roughly 50+ sessions exist, run periodic passes for accept/reject patterns and recurring tool-call sequences.
4. **Episodes.** When work units become identifiable, compress them to answer "have we tried this before?"
5. **Promotion.** Connect the candidate store to the library, starting with high-confidence, high-frequency promotions (a correction seen three times becomes a convention).

Each step is useful on its own: logging alone beats no memory, and correction extraction alone stops repeated mistakes.
