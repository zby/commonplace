# Exploration: What layered architecture makes "store everything, load selectively" work?

The framing document establishes: storage is cheap, context is expensive, the design challenge lives entirely in retrieval/activation. But "store everything" without structure is a haystack. This exploration asks what intermediate layers sit between raw session logs and curated library notes, and how material moves between them.

## The four-layer proposal

Working from the KB's existing vocabulary, the architecture has four layers with progressively higher distillation:

| Layer | What it stores | Format | Retention | Who writes |
|-------|---------------|--------|-----------|------------|
| **Trace** | Complete session logs, tool calls, model outputs | Append-only structured log (JSONL or similar) | Indefinite | Automatic (harness) |
| **Observation** | Extracted atomic facts: decisions, corrections, preferences, discoveries, questions asked | Typed records with timestamps, session references, confidence | Indefinite | Automated extraction pipeline |
| **Episode** | Compressed accounts of bounded work units — what was attempted, what happened, what was learned | Short prose with structured metadata (goal, outcome, key decisions, open threads) | Indefinite | Automated with optional human review |
| **Library** | Curated notes, claims, indexes, procedures, ADRs | Markdown with frontmatter, semantic links | Indefinite | Human + agent, validated |

The key claim: **the observation and episode layers are the missing middle.** Raw traces are too verbose for retrieval; library notes are too curated for capture speed. Something must sit between them.

### Layer 1: Trace (raw substrate)

This is the "store everything" layer. Every session interaction is captured with full fidelity — the audit log, the ground truth, the substrate that all higher layers derive from. Concrete format: structured log per session (timestamp, actor, content, session ID; tool calls include inputs and outputs).

The trace layer answers one question well: "What exactly happened in session X?" It answers nothing else well, because searching across thousands of sessions by content similarity will drown in noise. This is by design — the trace layer is for provenance, not for retrieval. Higher layers are the retrieval interface.

**Tension: trace format matters more than it seems.** JSONL is natural for structured logs, but the KB is filesystem-first with markdown as the lingua franca. There might be a case for both: structured data for extraction pipelines, markdown rendering for human review. This decision can be deferred — the layers above don't depend on the specific trace format.

### Layer 2: Observation (indexed atomic facts)

Observations are the first extraction from traces. They answer: "What discrete facts, decisions, preferences, and corrections exist in the session logs?"

Concrete examples from the framing's taxonomy:

- **Decision**: "Chose SQLite over PostgreSQL for review storage because single-file portability matters more than concurrent access" (session 47, 2026-03-15)
- **Correction**: "Agent used `git add -A`; user corrected to stage specific files" (session 12, 2026-01-20)
- **Preference**: "User rejects emoji in prose unless explicitly requested" (observed sessions 3, 8, 14, 22)
- **Discovery**: "Validation script can run in batch mode with `all` argument" (session 33, 2026-02-28)
- **Question**: "How should review findings connect back to the notes they review?" (session 41, 2026-03-10)
- **Procedure fragment**: "When ingesting a source, snapshot first, then classify, then connect" (observed sessions 15, 19, 23)

Each observation is:
- **Typed** (decision, correction, preference, discovery, question, procedure-fragment). This list is illustrative, not exhaustive — plausible additional types include affective/engagement signals (frustration, satisfaction, disengagement patterns) and meta-operational observations (observations about the memory system's own behavior, such as "retrieval missed a relevant note" or "extraction pipeline misclassified X").
- **Timestamped** and linked to source session(s)
- **Scored** — confidence (how certain is the extraction?) and importance (how likely to matter later?)
- **Indexed** for retrieval — keywords, tags, embeddings, whatever the retrieval layer needs

The observation layer is where [ClawVault](../../agent-memory-systems/reviews/clawvault.md), a scored-observation memory system with session lifecycle management and promotion pipelines (see the [comparative review](../../agent-memory-systems/agentic-memory-systems-comparative-review.md)), is most instructive: scored observations with explicit types and promotion pathways. The difference from ClawVault: we derive observations from stored traces rather than extracting them at interaction time. This decouples capture speed from extraction quality — the extraction pipeline can be rerun, improved, and backfilled.

**The extraction bridge (trace -> observation)**: This is an automated pipeline. An LLM reads a session trace and extracts typed observations. The pipeline can run asynchronously — after a session ends, not during it. This means extraction quality can improve over time without changing the capture mechanism. Re-extraction is always possible because traces are retained.

**Open question: observation granularity.** How atomic should observations be? "User prefers dark mode" is too Mem0 — stripped of all context. "In session 47, when setting up the editor, the user said they prefer dark mode because they work late at night and bright screens give them headaches" retains context but is bulky for retrieval. The right granularity is probably: atomic claim + enough context to evaluate relevance + pointer back to full trace. This is the same pattern as the KB's `description` field — a retrieval filter, not a summary.

### Layer 3: Episode (compressed work accounts)

Episodes are the compressed story of a bounded piece of work. They answer: "What happened when we tried to do X?" Not individual facts (that's observations) but the narrative arc of an attempt.

Concrete examples:

- "Implemented review scoring system (sessions 41-45). Started with weighted averages, discovered that gate-based pass/fail was more useful than continuous scores. Key decision: review findings are typed (warn/info/pass) rather than numerically scored. Open thread: how to aggregate gate results across a bundle of reviews."
- "Investigated memory evolution for the KB (session 78). Read A-MEM paper, explored whether neighboring notes should auto-update when new connections form. Concluded: the update trigger is clear (new link added) but the update operation needs a quality oracle we don't have. Parked for later."

Episodes serve a different retrieval need than observations. Observations answer "have we seen X before?" Episodes answer "have we tried something like X before, and what happened?" The distinction maps to the KB's library/workshop separation: observations are proto-library (facts that might graduate), while episodes are workshop records (work accounts that might produce library artifacts).

Episode structure:
- **Goal**: what was attempted
- **Scope**: session range, time period
- **Outcome**: succeeded / partially succeeded / abandoned / ongoing
- **Key decisions**: with pointers to observation-layer decisions
- **Lessons**: what was learned (pointers to observation-layer discoveries)
- **Open threads**: what remains unresolved
- **Produces**: pointers to any library artifacts created during this work

Episodes correspond roughly to compressed episodes in [Slate](../../sources/slate-moving-beyond-react-and-rlm.md) (Random Labs), a thread-weaving agent framework where bounded worker threads return compressed episodes to an orchestrator. The difference is that Slate's episodes are generated at the execution boundary as handoff artifacts, while these episodes are retrospective compressions of stored traces. Both are distillation, but with different timing: boundary compression (Slate) vs. retrospective compression (this design).

**The extraction bridge (trace -> episode)**: This is harder than observation extraction because it requires identifying coherent work units across sessions and compressing a multi-session narrative. The pipeline needs to identify: where does one piece of work begin and end? What sessions belong to the same effort? This might need human hints (explicit "starting work on X" / "done with X" markers) or heuristic clustering (same files touched, same topics discussed, same task referenced).

**Tension: episodes vs. workshop documents.** The KB already has the workshop concept — temporal documents with lifecycles. Are episodes just a specific kind of workshop document, or are they a separate thing? I think they are the *retrospective record* of workshop activity. A task in `kb/tasks/` is a prospective workshop document (here is what we plan to do). An episode is a retrospective one (here is what happened when we did it). Both could live in the workshop layer, but they have different creation triggers and different uses.

### Layer 4: Library (curated knowledge)

The existing KB layer — notes, structured claims, indexes, ADRs, procedures. The new design does not change the library layer; it provides it with richer input channels.

## How material moves between layers

The critical design question is not the layers themselves but the **promotion pathways** between them. Each transition is a distillation step with different characteristics:

### Trace -> Observation (extraction)

- **Trigger**: automatic, after session ends. Could also run periodically on older traces when the extraction pipeline improves (backfill).
- **Operation**: LLM reads trace, extracts typed observations. Each observation gets a type tag, confidence score, importance estimate, and source pointer.
- **Quality control**: confidence scores; low-confidence observations are flagged for human review. A second concern: extraction completeness — did the pipeline miss important observations? Spot-checking a sample of traces against their extracted observations is the most practical audit. Duplicate/near-duplicate detection is also needed since similar observations will recur across sessions.
- **Failure modes**: over-extraction (trivial facts promoted to observations, drowning the layer in noise), under-extraction (subtle preferences or implicit decisions missed), and type misclassification (a correction tagged as a preference loses its corrective force).
- **Reversibility**: high — traces are retained, observations can be re-extracted with improved pipelines.

### Observation -> Episode (compression)

- **Trigger**: work unit completion (explicit "done with X" marker), periodic consolidation (e.g., weekly sweep of unassigned observations), or human request. The hardest trigger to automate: detecting that a work unit is complete without explicit markers.
- **Operation**: LLM clusters related observations across sessions, compresses into narrative. Must identify episode boundaries — which observations belong to the same effort? Heuristics: shared file paths, shared task references, temporal proximity, topic similarity.
- **Quality control**: episode must reference source observations; narrative coherence check. Key risk: the compression step introduces editorial judgment — the LLM decides what mattered, what was incidental. This framing can be wrong. Mitigation: episodes should be treated as one interpretation, not as ground truth; source observations remain canonical.
- **Failure modes**: boundary errors (merging two unrelated efforts or splitting one effort into fragments), narrative distortion (overemphasizing a dramatic decision while omitting a quiet-but-important one), and orphaned observations (observations that never cluster into any episode because the work was too fragmented).
- **Reversibility**: medium — source observations and traces are retained, but the narrative framing involves judgment that may differ on re-extraction.

### Observation -> Library (promotion)

- **Trigger**: recurrence (seen N times across M sessions), human request, or importance threshold. The recurrence threshold should vary by type: a preference may need 3+ independent sessions to be stable, while a single high-stakes architectural decision may warrant immediate promotion. Importance scoring helps — a low-importance observation that recurs 10 times is less promotable than a high-importance one seen twice.
- **Possible operations**:
  - A preference observed 5 times becomes a documented preference (-> self-knowledge note or CLAUDE.md entry)
  - A procedure fragment seen across 3 sessions becomes a documented procedure (-> instruction)
  - A decision with high importance becomes an ADR
  - A discovery becomes a note
- **Quality control**: human review for library-grade promotion; automated for lower-stakes artifacts like preferences. The library layer's own validation (frontmatter checks, link requirements, description quality) applies to promoted artifacts. A promotion candidate that cannot be written to library standards should be deferred, not forced.
- **Failure modes**: premature promotion (a procedure observed 3 times is actually 3 instances of the same mistake), stale promotion (by the time the recurrence threshold is met, the observation is outdated), and semantic drift (merging near-duplicate observations into a library entry that subtly misrepresents any individual instance).
- **This is the extraction bridge from the workshop-layer note**: observations are the intermediate form that makes extraction concrete.

### Episode -> Library (distillation)

- **Trigger**: episode completion (work unit done), human request. Unlike observation promotion, this is usually a deliberate act — someone decides "this episode produced something worth codifying."
- **Operation**: distill lessons, decisions, and open questions from episode into library artifacts. One episode may produce multiple library artifacts (an ADR, a note on a discovered pattern, and updates to existing notes).
- **Quality control**: human review (the library layer's standards apply). The episode provides a richer context for review than raw observations do — the reviewer can assess whether the distilled claim faithfully represents the full episode narrative.
- **Failure modes**: over-distillation (stripping context that was load-bearing, producing a library note that sounds authoritative but lacks the caveats visible in the episode), and orphan episodes (completed work units that never get distilled because no one triggers the process — the most likely failure mode in practice).
- **This is where ADRs come from**: an episode about a decision process produces an ADR; the episode retains the full reasoning the ADR distills.

### Library -> Observation / Episode (backflow)

This is the less obvious direction but equally important. Library notes should generate observations in the form of **activation cues**: when a library note is relevant to a situation, the observation layer should contain triggers that surface it. This is the composition bridge from the workshop-layer note — library knowledge needs to flow into active work.

Concretely: a library note about "prefer staging specific files over `git add -A`" should generate observation-layer entries that activate when a session involves git staging. The activation cue is: "when the agent is about to run git add, check if the user has a preference about staging strategy."

## How does "store everything" interact with lifecycle separation?

The framing identifies three memory spaces with different metabolic rates: knowledge (steady growth), self (slow evolution), operational (high churn). If you store everything, the separation moves from storage to retrieval — you tag/index differently rather than storing differently.

This is mostly right, but with a nuance: **the layers interact with the lifecycle separation, not orthogonally to it.**

| Layer | Knowledge content | Self content | Operational content |
|-------|------------------|-------------|-------------------|
| Trace | Research sessions, source analysis | User interaction patterns | Task execution, debugging sessions |
| Observation | Discovered facts, extracted claims | Preferences, corrections, voice patterns | Procedure fragments, tool usage patterns |
| Episode | Investigation narratives | Calibration episodes ("learned that I should...") | Task completion records |
| Library | Notes, claims, indexes | CLAUDE.md, identity docs | Instructions, procedures, task templates |

The metabolic rate applies within each layer:
- Operational observations churn fast — a debugging procedure that worked yesterday might be superseded today
- Self observations evolve slowly — a preference observed 5 times is likely stable
- Knowledge observations accumulate — a factual discovery doesn't expire (though it may be superseded)

So the practical implication is: **tag observations by lifecycle space, and use the tag in promotion heuristics.** A knowledge observation with high recurrence should promote to a library note. An operational observation with high recurrence should promote to a procedure. A self observation that recurs across many sessions should promote to CLAUDE.md. Different promotion thresholds, different target artifacts, same pipeline.

This is more useful than storing them separately. Separate storage creates boundaries that inhibit cross-space connections (a debugging procedure might reveal a knowledge insight; a self-preference might have implications for operational workflow). Unified storage with lifecycle tags preserves those connections while still allowing lifecycle-appropriate retrieval.

## Retrieval across layers: progressive disclosure

The bounded-context orchestration model says: the scheduler selects what to load into each bounded call. The four layers give the scheduler a natural progressive disclosure strategy:

1. **First pass**: search observation-layer summaries and episode-layer goals/outcomes (compact, indexed, cheap to scan)
2. **If relevant**: load the full episode or the cluster of observations
3. **If provenance needed**: follow the pointer back to the trace layer

This is the same pattern as the KB's description-first navigation: frontmatter descriptions let the agent decide "don't follow this" without loading the full note. Observation summaries and episode goals serve the same function for memory — they are the retrieval filter, not the content.

The scheduler never loads raw traces into a working context. Traces are for offline extraction and human debugging, not for agent consumption. If the agent needs to know what happened in session 47, it reads the episode or the relevant observations, not the 50KB trace.

## Alternative: three layers instead of four

An alternative that collapses observations and episodes into a single "indexed memory" layer:

| Layer | Content |
|-------|---------|
| Trace | Raw logs |
| Indexed memory | Both atomic observations and compressed episodes, distinguished by type |
| Library | Curated notes |

The argument for collapsing: observations and episodes are both extracted from traces, both sit in the middle, and the distinction between "atomic fact" and "narrative account" is a spectrum, not a binary. A "decision" observation with enough context starts looking like a micro-episode.

The argument against: they serve different retrieval needs. "Have we seen this preference before?" needs atomic lookup. "Have we tried this approach before?" needs narrative context. Combining them means the retrieval interface must handle both, which adds complexity.

My current lean: **keep them conceptually distinct but do not require separate storage infrastructure.** They can live in the same store (a `memory/` directory or database) with different type tags, but the extraction pipelines, promotion pathways, and retrieval strategies should treat them as different kinds of objects. This is analogous to how the KB handles notes and structured claims — same directory, different type field, different validation rules.

## Concrete uncertainties

1. **Extraction pipeline quality.** The observation extraction step is an LLM reading a trace and producing typed records. How good is this in practice? Can it reliably distinguish a decision from a discovery? Can it identify preferences that are implicit in user behavior rather than stated explicitly? This is testable — run extraction on 20 session logs and evaluate.

2. **Episode boundary detection.** Grouping sessions into coherent work episodes is hard. Sessions may interleave multiple work streams. A single session may contribute to three different episodes. Do we need explicit work-unit markers ("starting task X" / "pausing task X") or can clustering work well enough?

3. **Promotion thresholds.** ClawVault's "seen twice on different dates" is a starting heuristic for promotion. But what counts as "seen"? Exact match? Semantic similarity? And when is two enough vs. needing five? These thresholds will need tuning, and the right thresholds probably differ by observation type and lifecycle space.

4. **Backflow implementation.** How do library notes generate activation cues in the observation layer? Is this a build-time step (when a library note is written, generate activation cues)? Or a retrieval-time step (when assembling context, check library notes against current situation)? Build-time is more in the spirit of frontloading; retrieval-time is more flexible. Probably both: generate coarse activation cues at build time, refine at retrieval time.

5. **The oracle problem persists.** Extraction, compression, and promotion all require quality judgments. What makes a good observation? A coherent episode? A library-worthy note? The oracle problem from the comparative review does not disappear — it just moves to the extraction and promotion steps. Human review is the current oracle; the question is whether the intermediate layers reduce the amount of human review needed (because the human reviews observations rather than raw traces) enough to be practical.

6. **Episode nesting.** A large effort (e.g., "build the review system") may contain sub-episodes ("design the schema," "implement the runner," "calibrate gates"). Should episodes nest? Flat episodes are simpler to implement and retrieve, but they lose the hierarchical structure of real work. Nested episodes preserve structure but require a tree model that complicates clustering, retrieval, and promotion. A pragmatic middle ground: flat episodes with explicit "part-of" pointers, where a parent episode is a manually or semi-automatically created summary that references its children.

7. **Storage format for observations and episodes.** Markdown files in a directory? SQLite database? JSON files? The KB is filesystem-first, which suggests markdown. But observations are numerous and atomic, which suits a database. Episodes are narrative, which suits markdown. This tension might resolve by storing observations in a lightweight database (SQLite) and episodes as markdown — but that breaks the single-medium principle. Needs more thought.

## Summary of the proposal

The "store everything, load selectively" architecture needs intermediate layers between raw traces and curated library notes. The proposed four layers — trace, observation, episode, library — provide progressive distillation with clear promotion pathways between them. Lifecycle separation (knowledge/self/operational) operates through tagging within layers rather than through separate stores, preserving cross-space connections while enabling lifecycle-appropriate retrieval. The hardest unsolved problems are extraction quality, episode boundary detection, and the oracle for promotion decisions.
