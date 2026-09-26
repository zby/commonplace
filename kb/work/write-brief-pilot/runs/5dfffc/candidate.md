---
description: Design study of an ideal agent memory system under store-everything premise — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction pipeline
type: types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
status: current
---

# Designing a Memory System for LLM-Based Agents

## The core insight: storage is cheap, context is scarce

The main design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Storage is a solved problem: disk is cheap, text compresses well, and append-only logs need no schema design. The binding constraint is *context* -- the finite window of tokens an agent attends to in one inference call. Context is the only channel through which the agent receives instructions, accesses knowledge, and reasons toward action. Everything competes for that space, and quality degrades before the window fills: extra material can dilute instructions and distort interpretation below the token limit.

This inverts the usual design. Store aggressively -- all session logs, all intermediate artifacts, all observations -- and put the design intelligence into the machinery that decides which fraction of the store enters the context for a given task.

"Store everything" is a bet, not an axiom. It trades storage cost for indexing overhead, search pollution risk, and privacy exposure. The bet is that selective retrieval can manage what aggressive storage introduces.

## Memory plays two roles

Stored content is consumed in two ways. [Axes of artifact analysis](./axes-of-artifact-analysis.md) records this as behavioral authority; this note uses the shorthand **role**. In the **knowledge role**, content is consumed as fact, and durable writes extend what the agent can answer. In the **system-definition role**, content is consumed as policy, and durable writes change what the agent does.

The role belongs to the consumer, not to the bytes. A note saying "we use URL-path versioning" is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the agent's next API design.

The two roles need different machinery:

- **Knowledge retrieval** answers questions posed at consumption time. It fits search and navigation: start from a question, follow links, reason along connections. Standard RAG optimizes for this. Failure mode: nobody asks the question.
- **System-definition activation** injects policy when a matching situation occurs. It fits a third access pattern, **triggered activation**: watch the agent's proposed action for cues and surface the constraint before commitment. This is the territory of the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md). Failure mode: relevant policy is stored but never fires.

Most agent-memory systems optimize for knowledge retrieval and underserve the system-definition role, which is where [continual learning's hard part lies](./continual-learning-requires-governing-behaviour-changing-writes.md). "Adding RAG is learning" holds for the knowledge role and is empty for the system-definition role.

Session logs feed both roles. One correction in session 47 can produce a knowledge artifact (an ADR answering "why approach B?") and a system-definition artifact (a cue that fires when a later session proposes approach A). The extraction pipeline must produce both, and retrieval must serve both.

## Why existing approaches fall short

A comparison of eleven agent memory systems -- from vector-first fact stores (Mem0) through knowledge graphs (Graphiti) to filesystem-first curated systems (Ars Contexta, commonplace) -- shows three problems none fully solves.

**The agency trilemma.** Who decides what to remember? If the agent manages its own memory (Letta), it has full context but spends reasoning tokens on housekeeping. If an external service does (Mem0, Graphiti, Cognee), extraction is cheap but guesses what matters without the agent's reasoning context. If humans co-manage (commonplace, Ars Contexta), curation quality is highest and throughput lowest. AgeMem trains the memory policy by reinforcement learning, which needs a task-completion oracle that open-ended domains may lack and yields an opaque policy. No system combines high agency, high throughput, and high curation quality.

**Search versus navigation.** Mem0, Graphiti, and Cognee treat knowledge as something to *search*: embed a query, return top-k. Ars Contexta and commonplace treat it as something to *navigate*: follow articulated links. Search scores well on QA benchmarks, but QA accuracy does not measure whether the agent can trace a chain of decisions or follow a correction back to the episodes that established it. A memory system needs both. Neither tests triggered activation, which is one reason no reviewed system closes the activation gap.

**Everyone automates extraction; nobody automates synthesis.** Systems extract structured knowledge from input, but almost none synthesize across existing knowledge: merging threads, producing new insights, reformulating entries. Retaining complete logs is an advantage here, because synthesis can be attempted later and rerun as techniques improve.

## Architecture: four layers of progressive distillation

A store-everything system without structure is a haystack. The architecture has four layers, each more distilled than the one below:

**Layer 1: Trace.** Complete session logs -- every interaction, tool call, model output, and user message -- as append-only records with timestamps and session identifiers. Traces are the ground truth for provenance and offline extraction. The agent never loads raw traces into a working context.

**Layer 2: Observation.** Extracted atomic facts: decisions, corrections, preferences, discoveries, questions, procedure fragments. Each is typed, timestamped, linked to its source session, scored for confidence and importance, and tagged with its role. Some types commit to one role at extraction (a correction is system-definition; a negative result is knowledge). Others yield paired artifacts: a decision gives both a knowledge record ("why we chose A") and a cue ("if B is proposed, surface the reasoning for A"). Following ClawVault's scored, typed observations, but derived from stored traces rather than at interaction time, so extraction can be rerun, improved, and backfilled.

**Layer 3: Episode.** Compressed accounts of bounded work units that may span sessions: goal, scope (session range and period), outcome, key decisions (pointing to observations), lessons, open threads, and library artifacts produced. Observations answer "have we seen this before?" Episodes answer "have we tried something like this, and what happened?"

**Layer 4: Library.** Curated notes, claims, indexes, procedures, and ADRs. The design leaves the library unchanged and gives it richer input and a principled path from raw experience.

Why four: with only traces and library, every note requires a human to read traces and extract what matters -- the bottleneck the system exists to remove. With one intermediate layer, that layer must serve both atomic lookup and narrative retrieval, which need different indexing, extraction, and promotion. Observations and episodes can share storage, distinguished by type tags, but are treated as different objects. A fifth layer, such as splitting the library into working and reference knowledge, adds a boundary that inhibits links; frontmatter types and status fields already differentiate inside the library.

The layers also give the context scheduler progressive disclosure: scan observation summaries and episode goals first, load a full episode or observation cluster if relevant, follow the pointer to the trace only when provenance is needed.

### How material moves between layers

**Trace to observation (extraction).** Runs after each session, and reruns over old traces when the pipeline improves. An LLM extracts typed observations with confidence, importance, and a source pointer. Failure modes: over-extraction (trivia drowning the layer), under-extraction (subtle preferences missed), and misclassification (a correction tagged as a preference loses its corrective force). Fully reversible, because traces are kept.

**Observation to episode (compression).** Triggered by work-unit completion, periodic consolidation, or request. Harder than extraction because it requires editorial judgment about what mattered. Boundary heuristics: shared file paths, shared task references, temporal proximity, topic similarity, and explicit "starting X" / "done with X" markers.

**Observation to library (promotion).** Triggered by recurrence (N times across M sessions), importance, or request. Thresholds vary by type: a preference may need three or more independent sessions; a high-stakes architectural decision may warrant immediate promotion to an ADR.

**Episode to library (distillation).** Usually deliberate. The episode gives a reviewer the full narrative to check whether a distilled claim represents it faithfully.

**Library to observation (backflow).** Library notes generate activation cues. A note preferring "stage specific files over `git add -A`" should produce a cue that activates when a session involves git staging. Without backflow, library knowledge is stored but inert.

### Lifecycle and role are orthogonal tags

Knowledge, self-knowledge, and operational artifacts change at different rates. Operational observations churn fast; self-observations such as preferences are stable once recurrent; knowledge observations accumulate until superseded. Separate stores would block connections across these spaces, so the architecture keeps one store and tags each observation with a lifecycle space. The tag sets promotion thresholds and targets: recurrent knowledge becomes a library note, recurrent operational observations a procedure, recurrent self-observations a CLAUDE.md entry.

Role is a separate tag. The lifecycle tag answers *when does this expire?* and weights recency; the role tag answers *how is this consumed?* and selects the retrieval mechanism.

## Retrieval and activation

The hardest problem is activation. A system can store relevant knowledge, produce it on direct query, and still fail to surface it when it matters. Most memory designs test only retrieval under direct query.

### Two pipelines over one store

**Knowledge retrieval** serves questions such as "why did we do X?" Embedding search over descriptions is a first-pass filter; the library's articulated links do the rest. Its failure, the unasked question, is an elicitation problem the memory system can assist but not solve.

**System-definition activation** serves the agent's in-flight work. It is a watcher, not a query: cues are indexed by action signature, preference domain, or situation template, and fire when the proposed action matches. Its failure, a cue that applies but never fires, is the activation gap proper and holds most of the design surface.

The pipelines cross-reference: a fired cue can point to its knowledge context ("this correction belongs to the convention in ADR 014"), and navigation can reveal cues attached to a note.

### Three stages of activation failure

**Cue match.** The task context must carry enough signal to trigger retrieval. Embedding similarity handles topical matches but fails on causal ones: a session-47 correction about a deployment mistake does not embed near session 312's code-writing task, though the lesson applies.

**Priority arbitration.** In a store of thousands of sessions, any task matches dozens of items, and loading all of them destroys context efficiency.

**Commitment.** Loaded knowledge can still lose to training-time defaults. The agent behaves like an expert witness: accurate on what is asked, silent on concerns nobody raised.

### Typed cue indexes

Cues are extracted at ingestion time rather than searched for in raw logs at retrieval time. Each type matches against something different. A **correction cue** matches the action the agent is about to take:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches the decision space, a **precedent cue** the situation description, and a **procedure cue** the goal. When session 312's task plan includes dropping a column, the trigger matches and the lesson loads before the agent writes the migration.

The hard part is matching "migration that removes a column" to "drop column deprecated_flag". Three methods compose: action-type classification (both are `schema-migration:column-removal`), embedding similarity with a low threshold (accept false positives over false negatives), and LLM-judged relevance for high-consequence cues.

### Priority arbitration under a context budget

When too many cues match:

- *Recency-weighted relevance* with a long tail: a correction from 500 sessions ago still matters if the mistake recurs.
- *Consequence weighting*: sessions with corrections, frustration, or rework carry more action-relevant knowledge. The log supplies signals such as message count after a correction and explicit severity statements.
- *Frequency*: a cue that fires across many sessions is more likely to matter.
- *Budget by type*: fixed slots for corrections, preferences, and precedents, so no type crowds out the others.

### Commitment: from passive context to instruction

- *Imperative framing*: "BEFORE doing X, verify Y because Z failed in session 47," not "previously, X failed because Y."
- *Checkpoint insertion*: for high-consequence cues, add an explicit verification step to the task plan.
- *Contradiction surfacing*: when the proposed action contradicts a stored correction, say so and name the established alternative.

### Search, navigation, and activation compose

Search works over the lower layers, where items are numerous and weakly structured. Navigation works over the upper layers, where items are fewer and richly linked. Activation works over cues at any layer, because its trigger is the proposed action. For an agent about to write a database migration: activation fires matching correction and procedure cues; search surfaces past migration decisions and negative results; navigation follows their links to library notes. The agent gets corrections, past alternatives, and architectural constraints without loading a raw trace.

## Learning from session logs

Session logs carry four signal types. They differ in oracle clarity, extraction difficulty, role, and graduation target. Corrections, preferences, and procedures are system-definition. Decision provenance and negative results are knowledge. Discoveries start as knowledge candidates and may graduate into either role. From easiest to hardest:

**Corrections (system-definition).** The user says "no, do X instead" or rejects a tool call. The log records the wrong output, the rejection, and the fix: an explicit negative paired with a positive, the clearest oracle available. Pi Self-Learning extracts exactly this (`{"mistakes": [...], "fixes": [...]}`). Two occurrences in different sessions can justify promotion. The graduated artifact moves along the codification gradient: a CLAUDE.md rule or style-guide convention, then a lint check or validation script. Example: the user corrects alphabetical import sorting to stdlib / third-party / local grouping; on recurrence it becomes a documented preference, on a third occurrence a pre-commit hook candidate. A correction may also produce a companion note or ADR explaining why.

**Preferences (system-definition).** The user accepts some patterns and rejects others without stating a rule. Each signal is clear, but the latent rule ("short commit messages") must be inferred across sessions. Detection runs bottom-up (cluster accept/reject decisions by domain and look for predictive features) or top-down (ask an LLM which preferences explain the last 50 decisions in a domain). A reasonable threshold: five or more decisions across three or more sessions, over 80% consistent.

**Procedures (system-definition).** A workflow recurs with variations. Tool-call sequences are more reliable signals than prose: four sessions containing `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]` form a detectable pattern despite different conversations. The graduated artifact tightens with confidence: an instruction document if steps need human judgment, a skill if the procedure can be parameterized, a script if it is fully deterministic. The role stays system-definition throughout; only the representational form and the strength of the constraint change.

**Discoveries (knowledge, sometimes system-definition).** An insight emerges during work. These are the most valuable and hardest to detect: a discovery is a one-off event, and "feels important" is not a verifiable signal. Weak heuristics: explicit markers ("write this down"), claims linking previously unlinked notes, unusual elaboration depth, and later reference. Discoveries enter as low-confidence candidates and promote on reference frequency. Role is assigned at graduation, because operational implications show only with use: a finding about async resource pools may yield a note and a cue for async cleanup code.

### The promotion pipeline

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two choices matter. Extraction should be narrow and schema-constrained, with one prompt per signal type, not "summarize the session." The candidate store must be separate from the library, because mixing unvetted candidates into curated knowledge degrades retrieval precision for everything.

### Session logs as a composite oracle

Most memory systems lack a signal for "was this memory operation good?" Session logs offer many weak ones: corrections, accept/reject patterns, explicit importance markers, questions asked, elaboration investment, whether the session goal was met, return visits to a topic, and abandoned investigations. Reviewed systems use few of these: Pi Self-Learning uses corrections; ClawVault uses importance plus recurrence; cass-memory uses helpful/harmful feedback plus score decay. No single signal serves every extraction type. The bet is that combining many weak signals yields a usable soft oracle, rather than waiting for one strong signal that open-ended work does not provide.

## Knowledge-role use cases

**Decision provenance.** The recurring high-value question is *why did we do it this way and not that way?* ADRs answer it, but are written after the fact. Session logs keep the deliberation: alternatives, reasoning, active constraints, objections. This supports a semi-automated ADR pipeline: flag sessions where a decision was debated, pre-assemble alternatives, reasoning, selection, and consequences into a draft, and have a human verify and connect it. The "alternatives considered" section, the hardest to reconstruct from memory, is what logs preserve most directly. Logs also answer why-questions no ADR anticipated, because they keep what was discarded. An ADR often gets a system-definition companion: a cue that fires when the agent proposes a rejected alternative.

**Negative results.** What was tried and abandoned has no home in standard project structure; code shows only what was built. Negative results are stored as records of the approach, failure reason, source session, and follow-up decision, indexed by approach name so "why didn't we do X?" finds them. A severe one also gets a cue keyed on the approach.

## Where memory ends and the project begins

"The memory system stores what project artifacts don't preserve" is necessary but not sufficient. Project artifacts span both roles and both representational forms: code, tests, and lint rules are symbolic system-definition; documentation and ADRs are prose knowledge; CLAUDE.md is prose system-definition. Against each, the memory system adds the reasoning and process that produced it: the circuit breaker tried and abandoned behind a retry loop, the bug that motivated a test, the questions the docs failed to answer.

CLAUDE.md is the instructive edge case. It is already a memory artifact, loaded every session to steer the agent. The proposed distinction: **CLAUDE.md is compiled system-definition; the memory system is the source.** A correction repeated three times lives in session logs and graduates into CLAUDE.md, or further into a lint rule: same role, tighter constraint.

Two things blur the boundary. Some artifacts belong to both sides: an ADR, or a comment like `// Retries capped at 3 -- see incident #412`, records a conclusion without its deliberation, and the memory system holds the surrounding context rather than duplicating the artifact. And much knowledge *should* be in project artifacts but is not -- undocumented conventions, implicit invariants -- so the memory system catches it by default until someone writes it down. The better formulation: **the memory system is the substrate from which project artifacts are distilled.**

### Graduation pathways

| Pattern | Graduation trigger | Destination | Role |
|---|---|---|---|
| Decision debated across sessions | "Why did we decide X?" is expensive to answer | ADR linking back to source sessions | Knowledge |
| Decision with a commonly proposed rejected alternative | Agent re-proposed rejected option | Cue keyed on the rejected alternative | System-definition |
| Same workflow in 3+ sessions | Repetition detection | Documented procedure, skill, or script | System-definition |
| Same mistake corrected 2+ times | Correction frequency | Convention, CLAUDE.md entry, or lint rule | System-definition |
| Same mistake, with instructive rationale | The reasoning is worth preserving | Companion note or ADR | Knowledge |
| Agent needs same orientation each session | Recurring first-message pattern | CLAUDE.md entry | System-definition |
| Context needed to understand specific code | Explanation given during session | Code comment | Knowledge (usually) |
| Negative result: tried and abandoned | Approach explored and rejected | Negative-result record + "why not X?" index entry | Knowledge |

Recognition is the bottleneck. Clear triggers such as correction frequency and repetition count can be automated; judging whether a decision is load-bearing enough for an ADR can only be flagged and assisted.

Every graduated artifact creates a maintenance obligation; session logs, being append-only, create none. So premature graduation is worse than late graduation: graduate only when the cost of retrieving from logs exceeds the cost of maintaining the artifact.

**Reach decides what graduates.** High-reach knowledge ("systems optimized for normal-load efficiency sacrifice overload resilience") belongs in the library; low-reach knowledge ("the bug in PR #247 was a pool race condition") can stay in logs. For system-definition artifacts the test differs: does the trigger fire when it should, often enough to earn its context budget? A narrow, accurate cue beats a broad one that misfires, and graduating into always-loaded CLAUDE.md multiplies the cost of being wrong. Reach is usually invisible at first observation and revealed by accumulation, when several low-reach observations cluster around one structural pattern. Hence: accumulate promiscuously, graduate on revealed reach.

## Alternatives considered

**Three layers instead of four.** Merging observations and episodes into one indexed layer was rejected because atomic lookup and narrative retrieval need different indexing; they share storage but stay distinct.

**One unified retrieval pipeline.** Treating both roles as phases of one search-and-rank flow was rejected because a question-asker navigates from a query while an acting agent needs policy injected unasked.

**Extraction at session end only, no backfill.** Rejected because it couples capture speed to extraction quality; retained traces let extraction improve and rerun.

**Binary memory/project split.** Routing each artifact to one store was rejected because the same content appears on both sides with different purposes; memory is the substrate projects are distilled from, not a parallel store.

## What remains open

**Inspectable versus learned retrieval policy.** Explicit rules are debuggable and auditable but brittle as the system scales. Learned policies (AgeMem) adapt but are opaque and need an oracle that open-ended domains may lack. The likely answer is inspectable defaults with learned overrides where volume allows. When an override should supersede a rule, and how to detect drift from the baseline, is unsolved.

**Cross-session structural patterns.** Three incidents -- a deploy failing on stale staging config, a migration failing on stale test config, a flag rollout breaking on out-of-sync production config -- share no keywords but reveal one high-reach pattern: configuration lacks a single source of truth. Detecting shared causal structure takes expensive reasoning whose payoff is speculative. No current system does it; periodic deep-analysis passes over accumulated observations may be the practical form.

**The discovery oracle.** Corrections, preferences, and procedures have explicit, statistical, and structural oracles respectively. Discoveries have only later use, a trailing indicator. The system can surface candidates, such as claims linking previously unlinked notes or points of unusual elaboration, but the judgment "this is worth keeping" resists automation. Discovery recognition may stay semi-manual; build the easier extraction types first and accumulate enough volume to test discovery heuristics.

**The ephemeral computation trap.** If candidates are extracted but never promoted or reviewed, the system looks like it learns without learning: a candidate store that fills and is never read is a more elaborate form of discarding. The promotion filter must run, and a human or agent must review what it promotes. This is an operational failure, not a technical one, and the most likely failure in practice.

**Scale.** The design targets one user and one project: hundreds to low thousands of sessions, tens of thousands of observations, hundreds of episodes, and a library one curator can manage. Teams (multiple contributors, conflicting preferences, concurrent streams) and very long-lived projects (where the observation layer itself becomes a search problem) are open. Progressive disclosure should scale further than flat search, but cross-session pattern detection gets combinatorially harder as sessions grow. This is worth deferring until the single-user case works.

## A practical starting point

The layers do not need to exist on day one. A build order that follows difficulty:

1. **Session logging.** Cheap, needs no extraction, and creates the substrate. Raw traces already answer "what happened in session X?"
2. **Correction extraction.** Strongest oracle. A schema-constrained pass at session end stores corrections as typed cues and surfaces them before a repeat.
3. **Preference and procedure extraction.** Once roughly 50+ sessions accumulate, run periodic passes for accept/reject patterns and recurring tool-call sequences.
4. **Episode layer.** Compress identifiable multi-session work units, enabling "have we tried this before?"
5. **Promotion pipeline.** Connect candidates to the library, starting with high-confidence, high-frequency promotions such as corrections seen three times.

Each step is valuable alone: logging beats no memory, and correction extraction alone stops repeated mistakes.
