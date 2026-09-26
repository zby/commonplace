---
description: Design study of an agent memory system under the store-everything hypothesis — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction and graduation, build order
type: types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Designing a Memory System for LLM-Based Agents

## The premise: storage is cheap, context is scarce

The main design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Disk is cheap, text compresses well, and append-only logs need no schema design. The binding constraint is *context*: the finite window of tokens an agent attends to in one inference call. Context is the only channel through which the agent receives instructions, accesses knowledge, and reasons toward action. Everything competes for that space, and the space degrades before it fills: added material can dilute instructions, contaminate scopes, and distort interpretation below the token limit.

This inverts the usual design. Traditional systems optimize storage and treat retrieval as a lookup. This design stores aggressively — all session logs, intermediate artifacts, and observations — and puts the design effort into the machinery that decides which fraction of the store enters the context for a given task.

"Store everything" is a hypothesis, not an axiom. It trades storage cost for indexing overhead, search pollution risk, and privacy exposure, and bets that selective retrieval can manage what aggressive storage introduces. Those costs are open questions (see below). What the hypothesis settles is where the hard problem sits: the scarce resource is attention, not disk.

## Memory plays two roles

Stored content is consumed in two ways, and a durable write changes different things in each. Consumed as a [knowledge artifact](./definitions/knowledge-artifact.md) — evidence or reference — a write grows what the agent can answer. Consumed as a [system-definition artifact](./definitions/system-definition-artifact.md) — policy — a write changes what the agent does. The distinction belongs to the consumption path, not the bytes ([behavioral authority](./definitions/behavioral-authority.md)): "we use URL-path versioning" is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the next API design.

The two roles need different machinery:

- **Knowledge retrieval** answers questions posed at consumption time. It fits search and navigation: start with a question, follow links. Standard RAG optimizes for this. Failure mode: nobody asks the question.
- **System-definition activation** injects policy when a matching situation occurs. It fits triggered activation: watch the agent's proposed action and surface the constraint before commitment. This is the territory of the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md). Failure mode: relevant policy is stored but never fires.

Most agent-memory systems optimize for knowledge retrieval and underserve the system-definition role, which is the harder half of continual learning because [it requires governing behaviour-changing writes](./continual-learning-requires-governing-behaviour-changing-writes.md). Adding RAG grows knowledge; it does not by itself change behaviour.

Session logs are the common substrate. One correction in session 47 can produce both a knowledge artifact (an ADR answering "why do we use approach B?") and a system-definition artifact (a cue that fires when a later session proposes approach A). The extraction pipeline must produce both, and retrieval must serve both.

## What existing systems leave unsolved

A comparison of eleven agent memory systems — from vector-first fact stores (Mem0) through knowledge graphs (Graphiti) to filesystem-first curated systems (Ars Contexta, Commonplace) — shows three problems no current system fully solves.

**The agency trilemma: who decides what to remember?** If the agent manages its own memory (Letta), it has full context but spends reasoning tokens on housekeeping. If an external service does (Mem0, Graphiti, Cognee), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-manage (Commonplace, Ars Contexta), curation quality is highest and throughput lowest. AgeMem trains the memory policy by reinforcement learning, which needs a task-completion oracle that open-ended domains may lack and yields an opaque policy. No system combines high agency, high throughput, and high curation quality.

**Search versus navigation.** Mem0, Graphiti, and Cognee *search*: embed a query, return top-k. Ars Contexta and Commonplace *navigate*: follow links with articulated relationships. Search scores well on QA benchmarks, but QA accuracy does not measure whether the agent can follow a chain of decisions or trace a correction back to the episodes that established it. QA benchmarks also test only knowledge-role retrieval. System-definition consumption needs a third pattern, triggered activation, which neither search nor navigation supplies and no benchmark tests well.

**Extraction is automated; synthesis is not.** Every system can extract structured facts from unstructured input. Almost none can synthesize across existing knowledge: merge threads, reformulate entries, or produce new insight. Retained session logs help here, because synthesis can be attempted retrospectively and rerun as techniques improve.

## Architecture: four layers of progressive distillation

A store-everything system without structure is a haystack. Between raw logs and curated notes it needs two intermediate layers:

**Layer 1: Trace.** Complete session logs — every interaction, tool call, model output, and user message — as append-only records with timestamps and session IDs. The trace is ground truth and provenance. It answers "what exactly happened in session X?" and nothing else efficiently. The agent never loads raw traces into working context; traces feed offline extraction.

**Layer 2: Observation.** Extracted atomic facts: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each is typed, timestamped, linked to its source session, scored for confidence and importance, and tagged with its role. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). Others yield paired artifacts: a decision yields a knowledge record ("why we chose A") and a cue ("if B is proposed, surface the reasoning for A"). ClawVault's scored, typed observations with promotion pathways are the closest precedent. The difference here is that observations are derived from retained traces rather than extracted at interaction time, so capture speed is decoupled from extraction quality and extraction can be rerun and backfilled.

**Layer 3: Episode.** Compressed accounts of bounded work units, possibly spanning sessions: goal, scope, outcome, key decisions (pointing to observations), lessons, open threads, and library artifacts produced. Observations answer "have we seen this before?"; episodes answer "have we tried something like this, and what happened?"

**Layer 4: Library.** Curated notes, claims, indexes, procedures, and ADRs. The design leaves the library as it is and gives it richer input channels and a principled path from raw experience.

**Why four.** With two layers (trace and library), every step from log to note is manual — the bottleneck the system exists to remove. With three, one intermediate layer must serve both atomic lookup (a trigger–lesson pair) and narrative retrieval (a story with goals and outcomes), which need different indexing; observations and episodes may share storage, distinguished by type, but need separate extraction, promotion, and retrieval. A fifth layer, such as splitting the library into working and reference knowledge, adds a boundary that inhibits links; frontmatter types and links already differentiate within the library. The layers also give the context scheduler progressive disclosure: scan observation summaries and episode goals first, load full episodes or clusters if relevant, follow pointers to traces only for provenance.

### How material moves between layers

The promotion pathways matter more than the layers.

- **Trace → observation (extraction).** Runs automatically at session end, and again on old traces when the extractor improves. Failure modes: over-extraction (noise), under-extraction (missed preferences), and type misclassification (a correction tagged as a preference loses its corrective force). Fully reversible, since traces are retained.
- **Observation → episode (compression).** Runs on work-unit completion, periodic consolidation, or request. Harder than extraction because it requires editorial judgment about what mattered. Boundary heuristics: shared file paths and task references, temporal proximity, topic similarity, and explicit "starting X / done with X" markers.
- **Observation → library (promotion).** Triggered by recurrence, importance, or request. Thresholds vary by type: a preference may need three or more independent sessions; a single high-stakes architectural decision may warrant immediate promotion to an ADR.
- **Episode → library (distillation).** Usually deliberate. The episode gives the reviewer the full narrative to check the distilled claim against.
- **Library → observation (backflow).** Library notes should generate activation cues. A note saying "stage specific files, not `git add -A`" should produce a cue that fires when a session stages files. Without backflow, library knowledge is stored but inert.

### Lifecycle and role are orthogonal tags

Observations also differ in lifecycle. Operational observations churn fast (yesterday's debugging procedure may be superseded today), self-observations about the user's preferences evolve slowly, and knowledge observations accumulate. Rather than separate stores, which inhibit cross-links, tag each observation by lifecycle and use the tag in promotion: recurring knowledge becomes a library note, a recurring operational pattern becomes a procedure, a recurring self-observation becomes an always-loaded instruction-file entry. The role tag is independent: lifecycle answers *when does this expire?*, role answers *how is it consumed?* Retrieval uses lifecycle to weight recency and role to select the mechanism.

## Retrieval and activation

The hardest problem is activation: a system can store relevant knowledge, produce it on direct query, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query.

### Two pipelines over one store

Build one pipeline per role over the shared store.

**Knowledge-role retrieval** serves questions: "why did we do X?", "what do we know about Y?" The interface is navigable — enter at an index, follow links — with embedding search over descriptions as a first filter. Its failure, the unasked question, is an elicitation problem the memory system can assist but not solve.

**System-definition activation** serves in-flight work. Its interface is a watcher, not a query: cues indexed by action signature, preference domain, or situation template fire when the proposed action matches. Its failure, a cue that applies but never fires, is the activation gap proper, and most of the design surface lives here.

The pipelines cross-reference: a fired cue can point into the knowledge layer ("this correction belongs to ADR 014"), and navigation can reveal attached cues ("this note has an active correction attached").

Three access patterns run across the layers. Search suits the lower layers, where items are numerous and weakly structured. Navigation suits the upper layers, where items are fewer and richly linked. Activation operates over cues at any layer, because its trigger is the proposed action rather than a query. A typical flow for an agent about to write a database migration:

1. **Activation** fires cues whose triggers match the action: corrections load as instructions, preferences claim a context budget, procedures suggest a checklist.
2. **Search** over observations surfaces knowledge-role records for the task: past migration decisions, negative results, draft ADRs.
3. **Navigation** follows links from those records to library notes, turning isolated facts into a coherent picture.

The agent gets the corrections (system-definition, via activation), the past alternatives (knowledge, via search and navigation), and the architectural constraints (knowledge, via navigation), without loading a raw trace.

### Three stages of activation failure

- **Cue match.** The task context must carry enough signal to trigger retrieval. Embedding similarity handles topical matches but fails on causal ones: session 47's correction about a deployment mistake will not embed near session 312's code-writing task, though the lesson applies.
- **Priority arbitration.** With thousands of sessions stored, any task matches dozens of items, and loading them all wastes context.
- **Commitment.** Even loaded knowledge may be ignored in favour of training-time defaults. The agent answers what it is asked but does not raise concerns unprompted.

### Typed cue indexes (cue match)

Extract typed cues at ingestion time rather than searching raw logs at retrieval time. Each type has its own retrieval signature. A **correction cue** matches the action about to be taken:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches the decision space, a **precedent cue** the situation description, a **procedure cue** the goal. This bridges session 47 to session 312: when the session-312 plan includes dropping a column, the trigger matches and the lesson loads before the migration is written.

Matching is the hard part: "migration that removes a column" must match "drop column deprecated_flag". Three approaches compose: action-type classification (both are `schema-migration:column-removal`), embedding similarity with a low threshold (prefer false positives to false negatives), and LLM-judged relevance for high-consequence cues.

### Priority arbitration

- *Recency with a long tail:* recent sessions get a boost, but an old correction stays relevant if the mistake recurs.
- *Consequence weighting:* sessions with corrections, frustration, or rework rank higher. The log supplies the signals: messages after a correction, sentiment markers, explicit severity.
- *Frequency:* a cue that fires across many sessions more likely matters.
- *Budget by type:* reserve fixed slots for corrections, preferences, and precedents so no type crowds out the others.

### Commitment

- *Imperative framing:* not "previously, X failed because Y" but "BEFORE doing X, verify Y because Z failed in session 47."
- *Checkpoint insertion:* for high-consequence cues, add a verification step to the task plan.
- *Contradiction surfacing:* when the proposed action contradicts a stored correction, say so: "You are about to use approach A. In session 47, A failed because Z. The established alternative is B."

## Learning from session logs

Session logs contain four signal types, which differ in oracle clarity, extraction difficulty, role, and graduation target. From easiest to hardest:

**Corrections (system-definition).** The user says "no, do X instead" or rejects a tool call. The log holds the wrong output, the rejection, and the corrected direction — an explicit negative paired with a positive, the clearest oracle available. Pi Self-Learning's schema targets exactly this (`{"mistakes": [...], "fixes": [...]}`). Two occurrences in different sessions can justify promotion. The graduated artifact moves along the [constraining](./definitions/constraining.md) gradient within the same role: an instruction-file rule, a style-guide convention, then a lint check. Example: the user twice corrects alphabetical import sorting to stdlib / third-party / local grouping; it becomes a documented preference, and a third recurrence raises the question of a pre-commit hook. A companion note or ADR may record why.

**Preferences (system-definition).** The user consistently accepts some patterns and rejects others without stating a rule. No single session carries enough evidence; extraction must infer the latent rule ("short commit messages") from scattered decisions. Detect bottom-up (cluster accept/reject decisions by domain, find features that predict acceptance) or top-down (ask an LLM what preferences explain the last 50 decisions in a domain). A reasonable threshold: five or more decisions across three or more sessions with over 80% consistency.

**Procedures (system-definition).** A workflow recurs with variations. Tool-call sequences are more reliable signals than descriptions: four sessions sharing `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]` is detectable even when the conversation differs. Graduation follows [codification](./definitions/codification.md): an instruction document where steps need judgment, a parameterized skill, or a script if fully deterministic. The role stays constant; the constraint tightens.

**Discoveries (knowledge, sometimes system-definition).** An insight — a connection, a principle, a unifying abstraction — is the highest-value extraction and the hardest to detect, because it is a one-off event with no verifiable signal. It usually enters as knowledge and may later gain a cue (a discovery about async pool shutdown may yield a note and a cue that fires on async cleanup code); assign the role at graduation, when operational implications show. Heuristics are weak: explicit markers ("write this down"), claims linking previously unlinked notes, unusual elaboration depth, and later reference. Enter discoveries as low-confidence candidates and promote on reference frequency; a discovery never referenced again was probably not worth keeping.

### Knowledge-role yields: decision provenance and negative results

The recurring high-value question is *why did we do it this way and not that way?* ADRs answer it, but they are written after the fact and cover only the decisions the author thought to document. Session logs hold the raw deliberation: alternatives considered, reasons for each, active constraints, objections raised. This supports a semi-automated ADR pipeline: flag sessions where a decision was debated (several alternatives, an explicit selection, stated reasons), pre-assemble a draft with alternatives, reasoning, and consequences, and have a human verify it, add later consequences, and connect it. The "alternatives considered" section, the costliest part to reconstruct from memory, is what logs preserve most directly. A drafted ADR often gets a companion cue that fires when the agent proposes a rejected alternative: the ADR explains why; the cue prevents repetition.

Negative results have no other home. Code shows what was built, not what was tried and discarded, so only memory can answer "we tried that in session 34, and it failed because the proxies strip custom headers." Extract them as records of the approach, the failure reason, the source session, and the decision that followed, indexed by approach name so "why didn't we do X?" finds them. A severe negative result also warrants a cue keyed on the approach: the record answers "why not?", the cue prevents the attempt.

### The promotion pipeline

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. Extraction should be narrow and schema-constrained — one prompt per signal type — not "summarize the session." And the candidate store must be separate from the library: mixing unvetted candidates into curated knowledge degrades retrieval precision for everything.

### Session logs as a composite oracle

Most memory systems lack a training signal for "was this memory operation good?" Retained logs offer many weak ones: corrections, accept/reject patterns, explicit importance markers, questions asked, elaboration investment, whether the session goal was reached, return to a topic in later sessions, and abandoned investigations. Pi Self-Learning uses only corrections; ClawVault uses importance scoring plus recurrence; cass-memory uses helpful/harmful feedback plus score decay. The bet is that a soft oracle built from many weak signals closes enough of the gap to be practical.

## Where memory ends and the project begins

Project artifacts already occupy both roles and both [representational forms](./definitions/representational-form.md): code, tests, and lint rules are symbolic system-definition; documentation and ADRs are prose knowledge; an always-loaded instruction file (CLAUDE.md, AGENTS.md) is prose system-definition. Against each, the memory system adds the reasoning and process that produced it. Code says "retry with exponential backoff"; memory adds "a circuit breaker was tried in session 47 and interacted badly with the connection pool." A test says "this invariant holds"; memory adds "written because of the bug in PR #247."

**The memory system is the substrate from which project artifacts are distilled, not a parallel store.** A binary split that routes each artifact to "project" or "memory" fails for two reasons. Some artifacts belong to both: an ADR, or a comment like `// Retries capped at 3 -- see incident #412`, records the conclusion without the deliberation, and memory holds the surrounding context rather than a duplicate. And much project knowledge *should* be in project artifacts but is not — undocumented conventions, implicit invariants — so memory captures it by default until someone writes it down. The always-loaded instruction file is the clearest case: it is compiled system-definition, and the memory system is its source. Repeated corrections live in logs and graduate into it, or further into a lint rule.

### Graduation pathways

| Pattern | Graduation trigger | Destination | Role |
|---|---|---|---|
| Decision debated across sessions | "Why did we decide X?" is expensive to answer | ADR linking back to source sessions | Knowledge |
| Decision with a commonly proposed rejected alternative | Agent re-proposed the rejected option | Cue keyed on the rejected alternative | System-definition |
| Same workflow in 3+ sessions | Repetition detection | Documented procedure, skill, or script | System-definition |
| Same mistake corrected 2+ times | Correction frequency | Convention, instruction-file entry, or lint rule | System-definition |
| Same mistake, with instructive rationale | Reasoning worth preserving | Companion note or ADR | Knowledge |
| Agent needs same orientation each session | Recurring first-message pattern | Instruction-file entry | System-definition |
| Context needed to understand specific code | Explanation given during session | Code comment | Knowledge (usually) |
| Tried and abandoned | Approach explored and rejected | Negative-result record indexed by approach name | Knowledge |

Across every row the sequence is the same: observation, accumulation, recognition, distillation, placement, provenance. Recognition is the bottleneck. Clear triggers (correction count, repetition) can be automated; judgment calls (is this decision load-bearing enough for an ADR?) can only be flagged. Every graduated artifact also creates a maintenance obligation that append-only logs do not, so premature graduation is worse than late graduation: graduate when retrieval cost exceeds maintenance cost.

**Reach decides what graduates, and it works differently per role.** A knowledge artifact is worth promoting when its claim applies broadly. A system-definition artifact is worth promoting when its trigger fires accurately and often enough in the situations it covers to earn its context budget; a narrow, accurate cue beats a broad one that misfires. Graduating a correction into an always-loaded file makes it fire in every session and multiplies the cost of being wrong. Reach is often invisible at first: a connection-pool race condition may be a one-off or the third instance of a pattern about shutdown ordering. So accumulate promiscuously, then graduate on revealed reach — which is the recognition step again.

## Alternatives considered

- **Three layers instead of four.** An earlier version merged observations and episodes into one "indexed memory" layer distinguished by type tag. Rejected because atomic lookup and narrative retrieval need different indexing, and one interface serving both adds complexity without payoff. They may still share storage.
- **One unified retrieval pipeline.** The two roles were first treated as two phases of one search-and-rank flow. Rejected because the consumers differ: a question-asker navigates from a query, while an acting agent needs policy injected without asking.
- **Extraction at session end only, no backfill.** Rejected because it couples capture speed to extraction quality. Retaining traces so extraction can be rerun and improved is the main structural advantage the store-everything hypothesis offers.
- **A binary memory/project split.** Rejected because the same kind of content appears on both sides with different operational purposes; memory is the substrate project artifacts are distilled from.

## Open questions

**The costs of storing everything.** The premise bets that retrieval can absorb what aggressive storage introduces. How fast indexing overhead grows, how much search pollution survives the candidate/library separation, and what privacy exposure retained traces create — and whether any of these forces selective capture — is untested.

**Inspectable versus learned retrieval policy.** Inspectable rules are debuggable and incrementally refinable but brittle as scale and domains grow. Learned policies (AgeMem) adapt but are opaque and need an oracle. A hybrid — heuristic defaults with learned overrides where volume allows — is plausible, but when an override should supersede a rule, and how to detect drift, is unsolved.

**Cross-session structural patterns.** "The deploy failed because the staging config wasn't updated", "the migration failed because the test env config was stale", and "the rollout broke because the production config wasn't in sync" share no keywords, yet together reveal a high-reach pattern: configuration lacks a single source of truth. Detecting shared causal structure needs expensive reasoning on a speculative payoff. Periodic deep-analysis passes (weekly or monthly) may be required; no current system does this.

**The discovery oracle.** Corrections have an explicit oracle, preferences a statistical one, procedures a structural one. Discoveries have none except later use, a trailing indicator. Discovery extraction may stay semi-manual.

**Candidates that never promote.** If extraction runs but the promotion filter does not, or nobody reviews its output, the system looks like it learns without learning: a candidate store that fills and is never reviewed is ephemerality with extra steps. This is an operational problem, not a technical one, and the most likely failure in practice.

**Scale.** The design targets one user and one project: hundreds to low thousands of sessions, tens of thousands of observations, hundreds of episodes. Teams (conflicting preferences, concurrent streams) and very long-lived projects are open. Progressive disclosure should scale further than flat search, but cross-session pattern detection gets combinatorially harder with session count.

## A practical starting point

The layers need not arrive at once. The difficulty gradient suggests a build order, and each step is useful alone:

1. **Log sessions.** Capture complete traces. Cheap, needs no extraction, and answers "what happened in session X?" by manual search.
2. **Extract corrections.** The strongest oracle. Run a schema-constrained pass at session end, store typed cues with triggers, and surface them before a corrected mistake repeats.
3. **Extract preferences and procedures.** Once roughly 50+ sessions exist, run periodic passes for accept/reject patterns and recurring tool-call sequences.
4. **Build episodes.** Compress multi-session work units once they are identifiable, enabling "have we tried this before?"
5. **Connect promotion to the library.** Start with high-confidence, high-frequency promotions (a correction seen three times becomes a convention) and extend to weaker types as the system matures.
