---
description: Design study of an ideal agent memory system under store-everything premise — four-layer architecture (trace/observation/episode/library), role-split retrieval, typed cue indexes, session-log extraction pipeline
type: kb/types/note.md
traits: [synthesis, has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
status: current
---

# Designing a Memory System for LLM-Based Agents

## The core insight: storage is cheap, context is scarce

The dominant design question in agent memory is not "what should we store?" It is "how do we get the right stored information into the right context at the right time?"

Storage is a solved problem. Disk is cheap, text compresses well, and append-only logs require no schema design. The temptation is to spend design effort on what to remember and how to compress it. This is the wrong emphasis. The binding constraint in agent systems is *context* -- the finite window of tokens an agent can attend to during a single inference call. Context is the only channel through which the agent receives instructions, accesses knowledge, and reasons toward action. Everything competes for the same space, and the space degrades softly well before it fills: adding more material can dilute instructions, contaminate scopes, and distort interpretation even when the token limit is not reached.

This produces a design inversion. In traditional systems, you optimize storage and let retrieval be a lookup. In agent memory systems, you store aggressively and put all the design intelligence into retrieval and activation. Store everything -- all session logs, all intermediate artifacts, all observations. Then build the machinery that decides which fraction of that store enters the context for any given task.

"Store everything" is a bet, not an axiom. It trades storage costs for indexing overhead, search pollution risk, and potential privacy exposure. The bet is that selective retrieval can manage what aggressive storage introduces. But it shifts the hard problem to the right place: the scarce resource is attention, not disk.

## Memory plays two roles

A memory system for agents is not doing one thing. It is doing two things that look superficially similar but differ in how the stored content is consumed, how it is retrieved, and what a durable write changes about the system's behavior. The [axes of artifact analysis](./axes-of-artifact-analysis.md) names this as the **role** axis: artifacts are consumed in either a **knowledge role** (as fact — durable writes grow the agent's reach) or a **system-definition role** (as policy — durable writes change the agent's disposition).

The distinction is relational, not structural. The same stored bytes can play either role depending on the consumer. A note documenting "we use URL-path versioning" is knowledge when retrieved to answer "how do we version APIs?" and system-definition when loaded to steer the agent's next API design.

For agent memory, the two roles motivate different machinery:

- **Knowledge retrieval** answers questions posed at consumption time. It fits navigation: start with a question, follow links, reason along connections. Standard RAG optimizes for this. Failure mode: the retrieval never happens because no one asked the question.
- **System-definition activation** injects policy when a matching situation occurs. It fits triggered activation: watch for cues in the agent's proposed action, surface the constraint before commitment. This is the territory the [activation gap](./knowledge-storage-does-not-imply-contextual-activation.md) note targets. Failure mode: relevant policy is stored but never fires.

Most existing agent-memory systems optimize for knowledge-role retrieval (RAG over stored facts) and underserve the system-definition role — which is [the open half of continual learning](./continual-learning-open-problem-is-behaviour-not-knowledge.md). "Adding RAG is learning" is true for the knowledge role and empty for the system-definition role.

Session logs are the common substrate. A single correction in session 47 can produce **both** a knowledge artifact (an ADR that answers "why do we use approach B?") and a system-definition artifact (a cue that fires when a future session proposes approach A). The extraction pipeline must produce artifacts in both roles and the retrieval machinery must serve both consumption patterns.

## Why existing approaches fall short

A comparative analysis of eleven agent memory systems -- from vector-first fact stores (Mem0) through knowledge graphs (Graphiti) to filesystem-first curated systems (Ars Contexta, commonplace) -- reveals three structural problems that no current system fully solves.

**The agency trilemma.** Every memory system must answer: who decides what to remember? If the agent manages its own memory (as Letta does), it has full context but burns reasoning tokens on housekeeping. If an external service manages memory (Mem0, Graphiti, Cognee), extraction runs cheaply but guesses what matters without the agent's reasoning context. If humans co-manage memory (commonplace, Ars Contexta), curation quality is highest but throughput is lowest. AgeMem trains the memory policy through reinforcement learning, which approaches all three goals but requires a task-completion oracle that may not exist in open-ended domains, and the learned policy is opaque. No system combines high agency, high throughput, and high curation quality.

**Navigability versus retrieval.** The systems split on how knowledge is accessed. Mem0, Graphiti, and Cognee treat knowledge as something you *search* for -- embed a query, return the top-k results. Ars Contexta and commonplace treat knowledge as something you *navigate* -- follow links with articulated relationships, reason along connections. Search-optimized systems score well on QA benchmarks. But QA accuracy does not measure whether the knowledge structure supports agent reasoning -- whether the agent can follow a chain of decisions to understand why the system works the way it does, or trace a correction back through the episodes that established it. The two approaches optimize for different things, and a memory system needs both.

This split overlaps the role axis: knowledge-role consumption fits navigation (start with a question, follow links); system-definition-role consumption fits neither search nor navigation directly but requires a third pattern — **triggered activation**, where the system watches for cues in the agent's proposed action and injects relevant policy before commitment. QA benchmarks test knowledge-role retrieval. Neither search nor navigation tests system-definition activation well, which is one reason the comparative review finds no system solving the activation gap.

**Everyone automates extraction; nobody automates synthesis.** Every system that processes incoming data can automatically extract structured knowledge from unstructured input. Almost none can automatically synthesize across existing knowledge to produce novel insights, recognize when two separate threads should merge, or reformulate existing entries for clarity. The boundary between extraction and synthesis remains the open frontier. This is where a "store everything" design has a structural advantage: with complete session logs retained, synthesis can be attempted retrospectively, improved over time, and rerun when techniques improve.

## Architecture: four layers of progressive distillation

A store-everything system without structure is a haystack. Between raw session logs and curated library notes, two intermediate layers are needed. The resulting architecture has four layers, each at a higher level of distillation:

**Layer 1: Trace.** Complete session logs -- every interaction, tool call, model output, user message. Append-only structured records with timestamps and session identifiers. The trace layer is the audit log, the ground truth, the substrate from which all higher layers derive. It answers one question well: "What exactly happened in session X?" It answers nothing else efficiently, and that is by design. Traces are for provenance and offline extraction, not for agent consumption. The agent never loads raw traces into a working context.

**Layer 2: Observation.** Extracted atomic facts: decisions made, corrections given, preferences expressed, discoveries surfaced, questions asked, procedure fragments identified. Each observation is typed, timestamped, linked to its source session, scored for confidence and importance, and **tagged with its role** — knowledge (consumed as fact) or system-definition (consumed as policy). Some observation types commit to a single role at extraction (a correction is system-definition; a negative result is knowledge); others are ambiguous and the extractor produces paired artifacts (a decision observation yields both a knowledge record for "why we chose A" and a system-definition cue for "if B is proposed, surface the reasoning for A"). Observations answer: "What discrete facts, decisions, and corrections exist across all sessions?"

The observation layer is where ClawVault's design -- scored observations with explicit types and promotion pathways -- is most instructive. The difference: observations here are derived from stored traces rather than extracted at interaction time. This decouples capture speed from extraction quality. The extraction pipeline can be rerun, improved, and backfilled because traces are retained.

**Layer 3: Episode.** Compressed accounts of bounded work units -- what was attempted, what happened, what was learned. An episode covers a coherent piece of work that may span multiple sessions. Its structure includes a goal, scope (session range and time period), outcome, key decisions (with pointers to observations), lessons learned, open threads, and references to any library artifacts produced.

Observations and episodes serve different retrieval needs. Observations answer "have we seen this before?" Episodes answer "have we tried something like this before, and what happened?" The distinction maps to two different modes of memory use: lookup (find a specific fact) versus narrative (understand how an effort unfolded).

**Layer 4: Library.** Curated notes, structured claims, indexes, procedures, architecture decision records (ADRs). The existing knowledge base layer. The new design does not change the library; it provides it with richer input channels and a principled pathway from raw experience to curated knowledge.

### Why four layers, not fewer or more

The four-layer structure is driven by the problem, not by aesthetic preference. Consider what breaks with fewer layers.

With only traces and library (two layers), there is no intermediate representation. Every transition from raw log to curated note requires a human to read the trace, extract what matters, and write the note. This is exactly the manual bottleneck the memory system is designed to eliminate.

With traces, a single intermediate layer, and library (three layers), the intermediate layer must handle both atomic lookups ("has this correction been given before?") and narrative queries ("what happened when we tried this approach?"). These are different retrieval problems with different indexing strategies. A correction is a trigger-lesson pair; an episode is a compressed story with goals, outcomes, and open threads. Combining them forces the retrieval interface to handle both, adding complexity. They can share storage infrastructure -- the same directory or database, distinguished by type tags -- but the extraction pipelines, promotion pathways, and retrieval strategies should treat them as different kinds of objects.

Adding a fifth layer (say, splitting the library into "working knowledge" and "reference knowledge") introduces a boundary that inhibits connections. The library's existing mechanisms -- frontmatter types, status fields, semantic links -- already handle internal differentiation without requiring a storage split.

The four layers also provide a natural progressive disclosure strategy for the context scheduler. First pass: search observation summaries and episode goals (compact, cheap to scan). If relevant: load the full episode or observation cluster. If provenance is needed: follow the pointer back to the trace. This is the same pattern as frontmatter-first navigation -- descriptions let the agent decide "don't follow this" without loading the full content.

### How material moves between layers

The layers matter less than the promotion pathways between them. Each transition is a distillation step with distinct characteristics.

**Trace to Observation (extraction).** Triggered automatically after a session ends; can also run on older traces when the extraction pipeline improves. An LLM reads the trace and extracts typed observations, each with a type tag, confidence score, importance estimate, and source pointer. The key failure modes are over-extraction (trivial facts drowning the layer in noise), under-extraction (subtle preferences missed), and type misclassification (a correction tagged as a preference loses its corrective force). Reversibility is high: traces are retained, observations can always be re-extracted.

**Observation to Episode (compression).** Triggered by work-unit completion, periodic consolidation, or human request. Requires identifying coherent work units across sessions and compressing a multi-session narrative. This is harder than observation extraction because it involves editorial judgment -- the LLM decides what mattered and what was incidental. Heuristics for episode boundaries include shared file paths, shared task references, temporal proximity, and topic similarity. Explicit markers ("starting work on X" / "done with X") help when available.

**Observation to Library (promotion).** Triggered by recurrence (seen N times across M sessions), importance threshold, or human request. A preference observed five times becomes a documented preference. A procedure fragment seen across three sessions becomes a documented procedure. A decision with high importance becomes an ADR. The promotion threshold should vary by type: a preference may need three or more independent sessions to be stable, while a single high-stakes architectural decision may warrant immediate promotion.

**Episode to Library (distillation).** Usually a deliberate act -- someone decides "this episode produced something worth codifying." One episode may produce multiple library artifacts. The episode provides richer context for review than raw observations do, because the reviewer can assess whether the distilled claim faithfully represents the full episode narrative.

**Library to Observation (backflow).** The less obvious direction, but equally important. Library notes should generate activation cues in the observation layer. A library note about "prefer staging specific files over `git add -A`" should produce an observation-layer entry that activates when a session involves git staging. Without this backflow, library knowledge sits inert -- stored but not activated.

### Lifecycle and role: orthogonal tags on the same store

Knowledge, self-knowledge, and operational artifacts have different metabolic rates. Operational observations churn fast -- a debugging procedure that worked yesterday might be superseded today. Self-observations evolve slowly -- a preference observed across five sessions is likely stable. Knowledge observations accumulate -- a factual discovery does not expire, though it may be superseded.

Rather than storing these in separate systems (which inhibits cross-space connections), the architecture tags observations by lifecycle space and uses the tag in promotion heuristics. A knowledge observation with high recurrence promotes to a library note. An operational observation with high recurrence promotes to a procedure. A self-observation that recurs across many sessions promotes to CLAUDE.md. Different promotion thresholds, different target artifacts, same pipeline. Unified storage with lifecycle tags preserves connections while enabling lifecycle-appropriate retrieval.

The role tag is orthogonal to the lifecycle tag. A "self" observation is usually system-definition (a stable preference steers future sessions), but can also be knowledge ("I remember that we discussed how I work"). An operational observation about a debugging procedure is typically system-definition (fire it next time the situation recurs) but may also be knowledge when someone asks "how do we debug this class of bug?" The two tags answer different questions: *when does this expire?* (lifecycle) and *how is this consumed?* (role). Retrieval uses both — the lifecycle tag to weight recency, the role tag to select the activation mechanism.

## Retrieval and activation: bridging the gap between storage and context

The hardest problem in the architecture is not extraction or storage. It is activation -- getting the right knowledge into the right context when it matters. The knowledge-activation gap formalizes this: a system can store relevant knowledge, prove that knowledge on demand, and still fail to surface it when it matters. Storage and activation are distinct, and most memory designs test only retrieval under direct query.

### Retrieval splits by role, not by content

The central design move is to build two retrieval pipelines, one for each role, sharing the same underlying store.

**Knowledge-role retrieval** serves questions posed at consumption time. The canonical query is a human or agent asking "why did we do X?" or "what do we know about Y?" The retrieval interface is navigable: enter at an index, follow links, read connected notes. Embedding search over descriptions is a first-pass filter, and the library layer's articulated links do the rest. Failure mode: *the question is never asked.* Mitigation is outside this pipeline — it is the elicitation problem, which the memory system can assist but not solve.

**System-definition-role activation** serves the agent's in-flight work. The canonical trigger is the agent about to take an action that matches a stored cue. The retrieval interface is not a query — it is a watcher. Cues are indexed by action signature, preference domain, or situation template, and fire when the agent's proposed action matches. This is what typed cue indexes, described below, are for. Failure mode: *the cue never fires even though it applies.* This is the activation gap proper, and it is where most of the design surface lives.

The two pipelines share the observation store and cross-reference each other — a fired system-definition cue often carries a pointer into the knowledge layer for context ("this correction is part of a documented convention, see ADR 014"), and knowledge-layer navigation can reveal system-definition cues that would otherwise sit dormant ("while you're here, note that this note has an active correction attached"). But the mechanisms differ: search plus navigation for knowledge, triggered activation for system-definition.

### Three stages of activation failure

Activation decomposes into at least three stages, each with a different failure mode and a different design surface:

**Cue match:** the current task context must contain enough signal to trigger retrieval of relevant knowledge. Embedding similarity handles topical matches ("what did we decide about API versioning?"). It fails when the connection is causal, not topical. Session 47's correction about a deployment mistake will not embed near session 312's code-writing task, even though the lesson applies directly.

**Priority arbitration:** even when partially cued, a candidate competes with other activated knowledge for limited reasoning budget. In a store-everything system with thousands of sessions, any task context will match dozens of stored items. Loading them all destroys context efficiency.

**Commitment:** even when relevant knowledge is loaded into context, the agent may ignore it in favor of training-time defaults. The agent behaves like an expert witness -- giving accurate answers to whatever is asked, but not proactively raising concerns the questioner has not thought of.

### Typed cue indexes (system-definition activation)

The central mechanism for bridging the activation gap is typed cue indexes. These are system-definition artifacts by design — the goal is to inject policy when a matching situation occurs, not to answer a question. Instead of searching raw logs at retrieval time, the system extracts typed cues at ingestion time. Each type has a different retrieval signature:

A **correction cue** matches against the action the agent is about to take. It has a trigger condition and a lesson:

```
type: correction
trigger: "database migration that removes or drops a column"
lesson: "Three-phase column removal: (1) add new column + migrate data,
         (2) deploy and verify, (3) drop old column in separate migration.
         Direct column drops cause data loss if rollback is needed."
source_sessions: [47]
```

A **preference cue** matches against the decision space. A **precedent cue** matches against the situation description. A **procedure cue** matches against the goal.

This typed structure enables the "session 47 to session 312" bridge -- the specific design challenge the framing document identifies. In session 47, the user corrects the agent's approach to database migrations. The correction is extracted as a cue with a trigger condition. In session 312, when the agent's task plan includes dropping a column, the trigger matches, and the lesson is loaded into context before the agent writes the migration.

The matching problem is the hard part. "Database migration that removes a column" must match "drop column deprecated_flag" despite surface differences. Three approaches compose: action-type classification (both actions classify as `schema-migration:column-removal`), embedding similarity with a low threshold (accept false positives over false negatives), and LLM-judged relevance for high-consequence cues (expensive but accurate).

### Priority arbitration under context budgets

When too many cues match, the system needs to decide what to surface. Four mechanisms work together:

*Recency-weighted relevance* -- recent sessions get a boost, but with a long tail. A correction from 500 sessions ago is still relevant if the same mistake pattern is recurring.

*Consequence weighting* -- items from sessions involving corrections, user frustration, or significant rework get higher priority. A plausible heuristic: if the user had to redirect the agent, that session contains more action-relevant knowledge than one where everything went smoothly. The session log itself provides these signals: message count after a correction (more messages means harder to fix), sentiment markers, explicit severity statements.

*Frequency-based promotion* -- if the same cue fires across multiple sessions, it is more likely to matter.

*Budget allocation by type* -- reserve fixed context slots: N tokens for corrections relevant to the current task, M tokens for active preferences, P tokens for relevant precedents. This prevents any single cue type from crowding out the others.

### Commitment: from passive context to imperative instruction

Loading relevant knowledge is not enough. The agent must actually use it. Three mechanisms address the commitment stage:

*Imperative framing.* Surface corrections as instructions, not passive context. Not "previously, X failed because Y" but "BEFORE doing X, verify Y because Z failed in session 47." Framing shapes activation: perspective assignments outperform undirected review in elicitation studies, and the same principle applies to memory.

*Checkpoint insertion.* For high-consequence cues, insert explicit verification steps into the task plan: "Step 3a: Check whether this deployment includes schema changes. If yes, review the session 47 correction before proceeding."

*Contradiction surfacing.* When the agent's proposed action contradicts a stored correction or preference, surface the contradiction explicitly: "You are about to use approach A. In session 47, approach A failed because Z. The established alternative is approach B."

### Search, navigation, and activation compose vertically

Three access patterns run across the layers, and a full retrieval uses all three. Search operates over the lower layers (traces and extracted items) because the items are numerous and weakly structured. Navigation operates over the upper layers (synthesized artifacts and library notes) because the items are fewer and richly linked. Activation operates over system-definition cues, regardless of layer, because the trigger is the agent's proposed action rather than a query.

A typical retrieval flow for an agent about to write a database migration:

1. **Activation** fires any cues whose triggers match the proposed action. Correction cues load as imperative instructions; preference cues reserve a context budget; procedure cues suggest a checklist.
2. **Search** over extracted items surfaces any knowledge-role records related to the task (past decisions about migrations, negative results, ADRs in draft).
3. **Navigation** follows links from the surfaced records to library notes, gathering the articulated relationships that turn isolated facts into a coherent picture.

The agent receives: the specific corrections (system-definition, via activation), the past decisions and alternatives (knowledge, via search + navigation), the architectural constraints (knowledge, via navigation). Three access patterns, two roles, all assembled without loading a raw trace.

## Learning from session logs: the extraction taxonomy

Session logs contain at least four distinct signal types. They differ in how clear the oracle signal is, how difficult extraction is, what role the extracted artifact plays, and what it graduates into. Role sorts the taxonomy cleanly: corrections, preferences, and procedures are system-definition (they change what the agent does); decision provenance and negative results are knowledge (they answer why-questions without changing behavior on their own); discoveries start as knowledge candidates and may graduate into either role. The types, ranked from easiest to hardest:

### Corrections: the strongest signal (system-definition)

The user says "no, do X instead" or rejects a tool call with a different instruction. The session log records the wrong output, the rejection, and the corrected direction. This is the clearest oracle in the entire system -- an explicit negative signal paired with a positive signal. Pi Self-Learning's extraction schema targets exactly this pattern: `{"mistakes": [...], "fixes": [...]}`.

A correction observed twice in different sessions is not a fluke. The promotion threshold can be as low as two occurrences. Corrections are natively system-definition: their value is in firing the next time the situation arises, not in answering a question. The graduated artifact sits on the codification gradient within the system-definition role: a rule in CLAUDE.md (prose), a convention in a style guide (prose), or a linting check or validation script (symbolic). A correction may also produce a companion knowledge artifact -- a note or ADR answering "why do we prefer X over Y?" -- but the primary artifact is the one that steers future behavior.

Concrete example: the agent sorts Python imports alphabetically. The user corrects: "Group by stdlib / third-party / local, not alphabetical." When this correction recurs in a second session, it graduates from session-level memory to a documented preference. If it recurs a third time, the question becomes whether it should be a pre-commit hook.

### Preferences: distributed signal, inferential extraction (system-definition)

The user consistently accepts certain patterns and rejects others, but never articulates a rule. The signal is distributed across many sessions -- no single session contains enough evidence. Individual accept/reject signals are clear, but the pattern connecting them requires inference. The extraction step must hypothesize "short commit messages" as the latent variable from a scatter of individual approvals and rejections. Like corrections, preferences are system-definition: the value is steering future choices, not answering questions.

Detection works bottom-up (cluster accept/reject decisions by domain, look for feature splits that predict acceptance) or top-down (periodically prompt an LLM: "here are the last 50 decisions in domain X; what preferences explain the pattern?"). A reasonable promotion threshold: observed in five or more decisions across three or more sessions with over 80% consistency.

### Procedures: sequence alignment across sessions (system-definition)

The same workflow recurs: search for related notes, read the type template, write the note, connect it, validate. The sequence is analogous across sessions but not identical -- session 14 ingests a blog post, session 45 ingests a paper. Tool-call sequences are more reliable signals than natural-language descriptions. If four sessions all contain the subsequence `[WebFetch -> Read -> Write -> Grep -> Write -> Bash(validate)]`, that is a detectable pattern even when the surrounding conversation differs.

Procedures are system-definition: the graduated artifact is used to steer how the agent performs the task. It sits on the codification gradient within the role: an instruction document (prose, if human judgment is needed at steps), a skill definition (prose-plus-formal-shape, if it can be automated with parameters), or a script (symbolic, if fully deterministic). The graduation pathway mirrors the constraining gradient: observation, then documented convention, then automated check, then deterministic enforcement. Role stays constant; class changes as the artifact constrains tighter.

### Discoveries: the oracle problem at its purest (knowledge, sometimes system-definition)

An insight emerges during work -- a connection between ideas, a design principle, an abstraction that unifies several observations. These are the highest-value extractions and the hardest to detect. Unlike corrections (explicit rejection signal) or preferences (statistical pattern), a discovery is a one-off event. "Feels important" is not a verifiable signal.

Discoveries usually enter as knowledge: a claim that grows the agent's reach when retrieved for reference. Some discoveries then acquire a system-definition companion — a discovery about how async resource pools fail may produce both a note (knowledge) and a cue that fires whenever the agent writes async cleanup code (system-definition). The role assignment is made at graduation, not extraction, because the insight's operational implications only become visible with use.

Detection heuristics are all weak but worth trying: explicit markers ("that's interesting," "write this down"), surprise signals (claims connecting previously unlinked notes), elaboration depth (unusual number of turns spent developing a point), and post-hoc validation (the claimed discovery gets referenced in later sessions). Discoveries should enter as candidates with low confidence and promote based on reference frequency. A discovery that is never referenced again was probably not worth keeping.

### The promotion pipeline

Across all four types, a common pipeline emerges:

```
Session log
  -> Extraction (per-session, schema-constrained, runs at session end)
     -> Candidate store (workshop layer, low-confidence, dated)
        -> Promotion filter (cross-session, runs periodically)
           -> Durable artifact (library layer, authored/reviewed)
```

Two design choices matter. First, extraction should be narrow and schema-constrained, not open-ended summarization. A separate extraction prompt per signal type, each asking for its specific schema, produces far better results than "summarize the session." Second, the candidate store must be separate from the library. Mixing candidates with curated knowledge causes search pollution -- the flat-memory failure mode where unvetted material degrades retrieval precision for everything.

### Session logs as composite oracle

The automating-KB-learning problem identifies the oracle as the bottleneck: most systems lack a training signal for "was this memory operation good?" Session logs in a store-everything system provide a richer oracle substrate than any reviewed system exploits.

Available signals include corrections (explicit negative + positive), accept/reject patterns (clear per-instance, inferential in aggregate), explicit user markers ("this is important"), questions asked (reveal what the user needs to know), elaboration investment (time and tokens spent on a topic correlate with perceived importance), session-end state (was the goal accomplished?), return patterns (user revisits the same topic in a later session), and abandoned investigations (negative signal -- direction was not valuable enough to pursue).

No single signal is sufficient for all extraction types. But the combination is richer than what any reviewed system uses. Pi Self-Learning uses only corrections. ClawVault uses importance scoring plus recurrence. cass-memory uses helpful/harmful feedback plus score decay. The bet is that manufacturing a soft oracle from many weak signals -- rather than waiting for a single strong one -- can close enough of the gap to be practical.

## Use cases: how memory gets consumed

These use cases are the canonical knowledge-role consumption patterns. Their system-definition counterparts — preventing the already-rejected approach from being proposed again — run through the typed cue index described above. Both roles draw from the same session logs; they differ in what consumer uses the extracted artifact.

### Decision provenance: answering "why" (knowledge role)

The recurring high-value question is: *why did we do it this way and not that way?* This is what ADRs are designed to answer, but ADRs are manually authored summaries written after the fact. Session logs contain the raw deliberation: alternatives considered, reasoning for each, constraints that were active, objections raised and addressed.

The memory system enables a semi-automated ADR pipeline. Detection: flag sessions where a design decision was debated (multiple alternatives discussed, explicit selection, reasoning stated). Pre-assembly: extract alternatives, reasoning, selection, and consequences into a draft ADR. Human review: verify accuracy, add later consequences, connect to existing notes. The "alternatives considered" section -- the hardest part of ADR writing and the part most expensive to reconstruct from memory -- is exactly what session logs most directly preserve.

More generally, session logs answer the "why" questions that ADRs do not anticipate. An ADR captures the decisions the author thought to document. Session logs preserve what was discarded, not just what was chosen. The memory system's job is to make those answers findable without requiring someone to write them down first.

A well-drafted ADR often produces a system-definition companion: a cue that fires when the agent proposes one of the rejected alternatives. The ADR explains *why* (knowledge); the cue prevents repetition (system-definition). Both live in the memory system and point at each other.

### Negative result preservation (knowledge role)

"What was tried and abandoned" has no home in standard project structure. The code shows what was built; it does not show what was tried and discarded. When someone later proposes an approach that was already explored and rejected, only the memory system can answer "we tried that in session 34, and it failed because the proxy servers strip custom headers in our infrastructure."

Negative results are extracted as structured records with the approach attempted, the failure reason, the source session, and a link to the decision that followed. They are indexed by the approach name, so a "why didn't we do X?" query finds them directly. When a negative result is severe enough to warrant preventing recurrence, it also produces a system-definition cue keyed on the attempted approach — the knowledge record answers "why not?", the cue prevents the attempt in the first place.

## Where memory ends and the project begins

A memory system for a software project exists alongside code, tests, documentation, CI configuration, and other artifacts. The naive boundary principle -- "the memory system stores what project artifacts don't preserve" -- is necessary but not sufficient.

### The boundary, refined

Project artifacts themselves split across the class/role grid, and that grid makes the boundary clearer. Code and tests are symbolic system-definition. Documentation is prose knowledge. ADRs are prose knowledge. CLAUDE.md is prose system-definition. Lint rules are symbolic system-definition. The memory system is a substrate — prose-class, file-backed — from which both knowledge-role and system-definition-role project artifacts get distilled.

Artifact by artifact, the memory system's contribution is consistent: it adds the reasoning, context, and process knowledge that produced the artifact. Code (symbolic system-definition) says "retry loop with exponential backoff." The memory system adds the knowledge-role complement: "we tried a circuit breaker in session 47 but it interacted badly with the connection pool." Tests (symbolic system-definition) say "this invariant holds." The memory system adds knowledge: "this test was written because of the bug in PR #247." Documentation (prose knowledge) says "use this API." The memory system adds knowledge: "three users asked the same question that the docs failed to answer."

The interesting edge case is CLAUDE.md (or any always-loaded agent instruction file). CLAUDE.md is already a memory artifact -- it is prose system-definition, loaded every session to steer the agent. The proposed distinction: **CLAUDE.md is compiled system-definition; the memory system is the source.** When the user corrects the agent three times for the same mistake, the correction pattern lives in session logs and eventually graduates to a CLAUDE.md entry (or further, to a lint rule — same role, tighter constraining). CLAUDE.md is the deployment artifact; the memory system is the learning substrate.

### Where the boundary blurs

Two problems prevent a clean separation.

**The overlap zone.** Some knowledge legitimately belongs in both places. An ADR is a project artifact and a memory artifact. A test written in response to a specific bug is a project artifact, but the connection between the test and the bug it guards against is memory-layer knowledge that the test file alone does not preserve. A code comment like `// Retries capped at 3 -- see incident #412` is versioned project code and decision memory simultaneously. The overlap consists of artifacts that partially capture process knowledge but incompletely -- they record the conclusion without the deliberation, the fix without the diagnosis, the convention without the three corrections that established it. The memory system does not duplicate these artifacts; it holds the surrounding context that makes them intelligible.

**The aspiration gap.** Much project knowledge *should* be in project artifacts but is not. Undocumented conventions, tribal knowledge, implicit architectural invariants -- these are not in project artifacts because nobody wrote them down, not because they do not belong there. The memory system captures them by default through session logs, but their proper home is elsewhere. The memory system is a safety net for project artifacts that have not been written yet.

A better formulation: **the memory system is the substrate from which project artifacts are distilled.** It preserves everything; project artifacts are curated projections of it.

### Graduation pathways

When a pattern in session logs becomes a durable artifact, the destination depends on both what was learned and which role the artifact will play. The same source pattern can produce artifacts in both roles, serving different consumers:

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

The meta-pattern across all graduation types is: observation, accumulation, recognition, distillation, placement, provenance. Recognition is the bottleneck -- detecting that a pattern deserves graduation requires the kind of judgment the system is trying to automate. For signals with clear triggers (correction frequency, repetition count), recognition can be automated. For signals requiring judgment (when a decision is "load-bearing enough" to warrant an ADR), the system can only flag and assist.

A critical constraint on graduation: every graduated artifact creates a maintenance obligation. An ADR must be kept current. A linting rule must be updated when conventions change. Session logs impose no such obligation -- they are append-only. This means premature graduation is worse than late graduation. Better to keep knowledge in the memory system (cheap to store, no maintenance) and graduate only when the retrieval cost exceeds the maintenance cost.

### The reach heuristic

The concept of *reach* -- how broadly an insight applies across contexts -- maps onto the graduation question. High-reach knowledge ("systems that optimize for normal-load efficiency sacrifice overload resilience") wants to be in the library layer. Low-reach knowledge ("the bug in PR #247 was a race condition in the connection pool") can stay in session logs.

Reach behaves asymmetrically across roles. A knowledge artifact is worth promoting when its claim applies broadly — generalization is what makes the note worth reading across many situations. A system-definition artifact is worth promoting when its trigger fires often enough *in the specific situations it covers* — a narrow cue that fires accurately is more valuable than a broad one that mostly misfires. Graduating a correction into CLAUDE.md increases reach in both directions (it fires in every session, now) but also multiplies the cost of being wrong (every session loads it). The reach heuristic for knowledge is "does this claim apply more widely?"; for system-definition it is "does this trigger fire when it should, often enough to earn its context budget?"

But you often cannot tell the reach of an observation when you first make it. The connection pool race condition might be a one-off, or it might be the third instance of a pattern where async resource pools need explicit shutdown ordering. Reach is revealed by accumulation: when multiple low-reach observations cluster around the same structural pattern, the pattern has high reach and should graduate.

This creates a two-phase dynamic: accumulate promiscuously (because you do not know what is low-reach yet), then graduate based on revealed reach. The reach-revealing mechanism is exactly the recognition step from the promotion pipeline.

## Alternatives considered

Four exploration branches shaped the design. Each considered alternatives that were ultimately folded into the structure above; they are recorded here rather than separately to preserve the "why not otherwise" trail without duplicating their content.

**Three layers instead of four.** An earlier version collapsed observation and episode into a single "indexed memory" layer distinguished by type tag. Rejected because atomic lookup ("has this correction been given before?") and narrative retrieval ("what happened when we tried this approach?") have different indexing strategies, and forcing one interface to serve both adds complexity without payoff. The two share storage but stay conceptually distinct.

**Retrieval as a single unified pipeline.** The knowledge and system-definition roles were initially treated as two phases of the same search-and-rank flow. Rejected because the consumers differ fundamentally: a question-asker navigates from a query, while an acting agent needs policy injected without asking. They share the observation store but run as parallel pipelines — search plus navigation for knowledge, triggered activation for system-definition.

**Extraction at ingestion time only, no backfill.** An alternative kept cue extraction per-session at session end and never revisited older traces. Rejected because it couples capture speed to extraction quality. Retaining raw traces and decoupling extraction from capture is the structural advantage of "store everything" — the pipeline can be rerun, improved, and backfilled as techniques advance.

**Memory/project boundary as a binary split.** A simpler model classified each artifact as "project" or "memory" and routed it to one store. Rejected because the real boundary is patterned across the class/role grid rather than falling along artifact kind — the same class of content appears in both places with different operational purposes. The adopted framing treats the memory system as the substrate from which project artifacts are distilled, not a parallel store.

## What remains open

### The inspectability-learnability trade-off

How much of the retrieval policy should be inspectable (explicit rules a human can read and modify) versus learned (trained from usage patterns)?

Inspectable rules are debuggable, auditable, and incrementally refinable. When the system makes a bad retrieval decision, you can find the rule and fix it. But hand-written rules cannot anticipate every domain, and they grow brittle as the system scales.

Learned policies adapt to usage patterns and handle cases the rule-writer did not anticipate. AgeMem's RL-trained policy improves measurably from experience. But the policy is opaque -- stored in model weights, not inspectable -- and the training requires a clear oracle that may not exist in open-ended domains.

The likely answer is a hybrid: inspectable heuristic rules as the default (threshold-based promotion, type-specific retrieval patterns), with learned overrides for specific domains where enough volume exists to train on. But the interface between the two layers -- when a learned override should supersede a heuristic rule, and how to detect when the learned policy has drifted from the heuristic baseline -- is genuinely unsolved.

### Cross-session structural pattern detection

The hardest retrieval problem is detecting structural similarity across sessions. Consider three incidents:
- Session 12: "The deploy failed because the staging config wasn't updated."
- Session 28: "The migration failed because the test env config was stale."
- Session 45: "The feature flag rollout broke because the production config wasn't in sync."

Each is low-reach individually. Together they reveal a high-reach pattern: configuration management lacks a single source of truth, and every environment drift is a potential failure. But detecting this cluster requires recognizing shared *causal structure* -- the three incidents do not share keywords or surface features.

This is where the agency trilemma bites hardest. Detecting structural patterns across sessions requires deep reasoning (expensive), and the value is speculative (you are betting the pattern has reach before confirming it). No current system addresses this. It may require periodic deep-analysis passes over accumulated observations -- an expensive operation that cannot run on every session but might run weekly or monthly, looking for structural clusters that surface-level indexing misses.

### The oracle problem for discoveries

Corrections have an explicit oracle (the user's rejection is the signal). Preferences have a statistical oracle (consistency across decisions). Procedures have a structural oracle (recurring tool-call sequences). Discoveries have no reliable oracle. An insight that emerges in one session may be profound or trivial, and the only reliable signal is whether it gets used later -- a trailing indicator that provides no guidance at extraction time.

This means discovery extraction may always require human involvement at the recognition stage. The system can surface candidates (claims connecting previously unlinked notes, points where unusual elaboration depth was invested), but the judgment "this is worth keeping" resists automation. The practical implication: build the easier extraction types first (corrections, then preferences and procedures), accumulate enough volume to test discovery heuristics, and accept that the hardest extraction type may remain semi-manual.

### The ephemeral computation trap

If extraction runs but candidates never promote, the system has the appearance of learning without the substance. A candidate store that fills up and is never reviewed is just a more elaborate form of ephemerality -- generating artifacts and discarding them trades accumulation for simplicity. The promotion filter must actually run, and someone (human or agent) must actually review the promoted candidates. Otherwise the whole pipeline is theater. This is a social and operational problem, not a technical one, and it is the most likely failure mode in practice.

### Scale questions

The architecture is designed for a single-user, single-project scale -- hundreds to low thousands of sessions. At that scale, the observation layer holds tens of thousands of entries, episodes number in the hundreds, and the library is manageable by a single curator. Whether the same architecture works for a team (multiple users contributing sessions, conflicting preferences, concurrent work streams) or for a very long-lived project (tens of thousands of sessions, where even the observation layer becomes a search problem) is an open question.

The progressive disclosure strategy -- search compact summaries first, load details on demand -- should scale further than flat search. But the promotion pipeline's dependence on cross-session pattern detection becomes combinatorially harder as session count grows. This is a problem worth deferring until the single-user case is proven.

## A practical starting point

A system built from this design does not need all four layers on day one. The difficulty gradient suggests a build order:

1. **Start with session logging.** Capture complete traces. This is cheap, requires no extraction infrastructure, and creates the substrate for everything else. Even without extraction, raw traces answer "what happened in session X?" and enable manual search.

2. **Add correction extraction.** The easiest extraction type with the strongest oracle. Run a schema-constrained extraction pass at session end, looking specifically for user corrections. Store as typed cues with trigger conditions. Surface them when the agent is about to repeat a corrected mistake.

3. **Add preference and procedure extraction.** Once enough sessions accumulate (roughly 50+), cross-session pattern detection becomes feasible. Run periodic extraction passes for consistent accept/reject patterns and recurring tool-call sequences.

4. **Build the episode layer.** As work units become identifiable (through explicit markers or clustering heuristics), compress multi-session efforts into episode records. This enables "have we tried this before?" queries.

5. **Implement the promotion pipeline.** Connect the candidate store to the library layer. Start with high-confidence, high-frequency promotions (corrections seen three times become conventions). Expand to lower-confidence types as the system matures.

Each step is independently valuable. Session logging alone is better than no memory. Correction extraction alone eliminates repeated mistakes. The full four-layer architecture with typed cue indexes and promotion pipelines is the eventual target, but every intermediate state provides real benefit to the practitioner.
