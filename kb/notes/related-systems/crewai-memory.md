---
description: Unified vector-memory system for agent crews with LLM-driven scope inference, composite scoring, and consolidation — sophisticated retrieval engineering but no learning theory, treating memory as infrastructure rather than a knowledge medium
type: note
status: current
areas: [related-systems]
last-checked: 2026-03-05
---

# CrewAI Memory

A **unified memory system** for CrewAI's agent framework that replaces separate short-term, long-term, entity, and external memory types with a single `Memory` class. Uses LLM analysis on save (inferring scope, categories, importance) and composite scoring on recall (semantic similarity + recency decay + importance weighting). Storage is LanceDB (embedded vector database), retrieval is either shallow (pure vector search) or deep (multi-step RecallFlow with confidence-based routing).

**Repository:** https://github.com/crewAIInc/crewAI
**Module:** `src/crewai/memory/`
**Status:** Active development, part of the main CrewAI framework

## Core Ideas

**Memory as a single unified API.** The earlier CrewAI design had separate ShortTermMemory, LongTermMemory, EntityMemory, and UserMemory classes. The new system collapses these into one `Memory` class with a hierarchical scope tree (`/`, `/project/alpha`, `/agent/researcher`). The scope hierarchy does the work that separate memory classes used to do — scoping replaces typing. This is an architectural reduction that trades type-level distinctions for namespace-level distinctions.

**LLM-driven scope inference.** When `remember()` is called without an explicit scope, the LLM examines both the content and the existing scope tree, then suggests placement. New scopes are created organically — no upfront schema design. This is self-organisation at the storage layer: the memory system grows its own structure from the content it receives. The risk is that LLM judgment about "where does this belong?" is not easily auditable or correctable at scale.

**Composite scoring for retrieval.** Recall results are ranked by `semantic_weight * similarity + recency_weight * decay + importance_weight * importance`, where decay is exponential (`0.5^(age_days / half_life_days)`). Each weight and the half-life are configurable. This is more nuanced than pure vector similarity — it answers "what's relevant?" rather than "what's similar?" The match reasons are surfaced (`["semantic", "recency", "importance"]`) for transparency.

**Consolidation on save.** When a new memory is similar enough to existing records (cosine similarity > 0.85), the LLM decides: keep both, merge, or replace. This prevents unbounded accumulation of near-duplicate facts. The consolidation decision is an LLM call per similar pair — expensive but principled. Intra-batch deduplication (cosine > 0.98) catches exact duplicates without LLM calls.

**RecallFlow: adaptive-depth retrieval.** Deep recall runs a multi-step pipeline: query analysis → scope selection → parallel vector search → confidence-based routing → optional recursive exploration. If confidence is high, results return immediately. If low, the system explores deeper (up to a configurable budget). Short queries (< 200 chars) skip LLM analysis entirely — a sensible optimisation since "What database do we use?" is already a good search phrase.

**Non-blocking saves with read barriers.** `remember_many()` runs in a background thread; `recall()` automatically drains pending writes before searching. This is a clean producer-consumer pattern that lets agents continue working while memories persist. The crew's `kickoff()` drains writes in its `finally` block to prevent data loss.

**Scoped views and slices.** `MemoryScope` restricts operations to a subtree (agent sees only `/agent/researcher`). `MemorySlice` combines multiple disjoint scopes into a single view, optionally read-only. This gives agents private memory alongside shared knowledge — a genuine access-control primitive, not just filtering.

## Comparison with Our System

The fundamental difference: CrewAI Memory is **infrastructure** — a storage-and-retrieval service that agents consume. Our KB is a **knowledge medium** — a structured space where knowledge develops through type transitions, link semantics, and progressive disclosure. These are different bets about where intelligence should live.

| Dimension | CrewAI Memory | Commonplace KB |
|---|---|---|
| Storage primitive | Vector records in LanceDB | Markdown files in git |
| Organisation | LLM-inferred scope tree | Human-designed area indexes with editorial context |
| Retrieval | Composite-scored vector search | Agent-driven navigation via links and descriptions |
| Knowledge evolution | Consolidation (merge/replace) | Type transitions (text → seedling → note → structured-claim) |
| Quality control | Importance scoring (0-1 float) | Status field, traits, description quality checks |
| Learning mechanism | Implicit (accumulate + consolidate) | Explicit (stabilisation + distillation) |
| Persistence | Embedded database, opaque to tooling | Plain files, readable by any tool |
| Context cost model | Fixed per-record embedding + LLM analysis | Progressive disclosure (description first, full content on demand) |

**Where they're stronger:** The composite scoring formula, non-blocking save architecture, and consolidation pipeline are well-engineered. The scope/slice access-control model is genuinely useful for multi-agent scenarios. The graceful degradation when LLMs fail is thoughtful — memory still works, just with defaults.

**Where we're stronger:** Knowledge in our system has a lifecycle (status, type transitions, link semantics). A note can be challenged, refined, connected, promoted. In CrewAI Memory, a record is either present or consolidated — there's no maturation path. Our system also makes the [verifiability gradient](../deploy-time-learning-the-missing-middle.md) explicit: you can see what's speculative vs. what's been validated. Their importance scores have no such grounding.

### The Three-Space Problem

CrewAI Memory stores everything in one flat vector space partitioned by scope paths. Our [three-space analysis](../three-space-agent-memory-maps-to-tulving-taxonomy.md) predicts this will produce specific failure modes: operational details (task outputs) pollute semantic search for domain knowledge; agent self-knowledge (preferences, learned strategies) has no natural home distinct from project facts. The scope tree partially mitigates this — `/agent/researcher` vs `/project/alpha` is a namespace separation — but it's convention rather than structure. Nothing prevents operational trivia from landing in `/project/alpha` alongside architectural decisions.

The [predicted failures](../three-space-memory-separation-predicts-measurable-failure-modes.md) — search pollution, identity scatter, insight trapping — would be testable against CrewAI crews running real tasks over time.

### Context Efficiency

CrewAI Memory has no [context-efficiency](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) model. Every record is stored at full length, every recall returns full content. There's no progressive disclosure — no mechanism to load descriptions first and full content on demand. For small memory stores this doesn't matter. As memories accumulate into thousands of records, the lack of a summary/detail hierarchy will become a scaling constraint.

The `extract_memories()` function — which breaks raw text into atomic facts before storage — is a [distillation](../distillation.md) operation, even if it isn't named as such. It extracts discrete claims from discursive text. But the distillation is one-shot: once facts are stored, they don't get further refined, connected, or challenged.

## Borrowable Ideas

**1. Composite scoring formula.** The `semantic * w1 + recency * w2 + importance * w3` model with exponential decay is simple, tunable, and more honest than pure vector similarity for real retrieval. If we ever add automated retrieval alongside agent-driven navigation, this formula is ready to borrow. The half-life parameter is particularly well-chosen — it naturally models different knowledge domains (sprint retrospectives vs. architectural principles).

**2. Consolidation on save.** Checking new content against similar existing records and having the LLM decide merge/keep/replace is a principled approach to preventing accumulation. For our system this would apply to the workshop layer — observations in `kb/log.md` that overlap with existing notes could be flagged for merge or promotion rather than accumulating indefinitely. Needs a use case before building.

**3. Non-blocking saves with read barriers.** The pattern of background persistence with automatic drain-before-read is clean engineering. Not immediately relevant (our storage is synchronous file writes) but worth remembering for any future async knowledge operations.

**4. Scoped views with read-only slices.** The `MemoryScope` and `MemorySlice` abstractions are a neat solution to multi-agent access control. Agents can share a knowledge base while maintaining private working memory. Our system doesn't have multi-agent scenarios yet, but the pattern — one shared library, per-agent workshop — aligns with our [workshop/library distinction](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md).

## What We Should Not Borrow

**LLM-driven scope inference.** Letting the LLM decide where to file each memory creates an opaque, non-reproducible organisation. It works well enough when humans don't need to audit the memory — but for a knowledge system where the structure is itself meaningful, automated filing removes the human judgment that makes structure trustworthy. The same concern we raised about [ClawVault's LLM-heavy automation](./clawvault.md) applies more strongly here, because the scope tree has no independent validation.

**Importance as a float.** Importance scores between 0 and 1, inferred by an LLM on save, imply a precision that doesn't exist. What does 0.7 importance mean? The composite scoring formula works despite this because the relative ranking is what matters, not the absolute values. But if we adopted importance scoring, we'd want discrete buckets (structural / potential / contextual, as ClawVault does) rather than continuous floats.

**The unification itself.** Collapsing short-term, long-term, entity, and operational memory into one API simplifies the programming model but erases distinctions that matter for [knowledge lifecycle](../claw-learning-is-broader-than-retrieval.md). Session-scoped observations need different retention policies than domain knowledge. Agent preferences need different retrieval strategies than project facts. The scope tree approximates these distinctions but doesn't enforce them.

## Relation to Other Reviewed Systems

CrewAI Memory and [ClawVault](./clawvault.md) represent two poles of agent memory design:

- **ClawVault** has typed observations, explicit session lifecycles, promotion pipelines, and a reflection cycle. It models the *process* of learning.
- **CrewAI Memory** has a unified vector store, composite scoring, and consolidation. It models the *infrastructure* of remembering.

Neither has a [learning theory](../learning-theory.md). ClawVault has operational patterns for what to do with knowledge (score, promote, reflect); CrewAI has engineering for how to store and retrieve it. What's missing from both is the meta-level: when should knowledge be [stabilised](../stabilisation.md) vs. kept fluid? When does a memory need to become a decision, a procedure, a constraint? These are the questions our [deploy-time learning framework](../deploy-time-learning-the-missing-middle.md) addresses.

The earlier [comparative review of agentic memory systems](./agentic-memory-systems-comparative-review.md) (Mem0, Graphiti, Cognee, Letta) found all four systems converging on vector similarity for retrieval and LLM-driven extraction on save. CrewAI Memory continues this pattern — it's the most polished implementation of the same paradigm, with the composite scoring and consolidation as its distinctive contributions.

## What to Watch

- Does scope inference produce coherent hierarchies over time, or does the tree become a disorganised accumulation of LLM guesses?
- How does consolidation behave with contradictory information? The LLM decides merge/replace, but what if two genuinely conflicting facts should both be retained?
- Does the composite scoring actually change retrieval quality compared to pure semantic search? The weights are configurable but there's no evidence presented for what values work best.
- As memory grows past thousands of records, does the full-content storage model create recall latency or token waste?

---

Relevant Notes:
- [three-space-agent-memory-maps-to-tulving-taxonomy](../three-space-agent-memory-maps-to-tulving-taxonomy.md) — grounds: CrewAI's unified single-space design is the alternative to the three-space separation this note argues for
- [three-space-memory-separation-predicts-measurable-failure-modes](../three-space-memory-separation-predicts-measurable-failure-modes.md) — grounds: predicted failures (search pollution, identity scatter) are testable against CrewAI crews
- [context-efficiency-is-the-central-design-concern-in-agent-systems](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: CrewAI Memory has no context-efficiency model; full-content storage ignores the volume dimension
- [distillation](../distillation.md) — extends: `extract_memories()` is one-shot distillation without refinement or reconnection
- [stabilisation](../stabilisation.md) — contrasts: consolidation is a form of stabilisation (reducing redundancy) but without the interpretation-narrowing that characterises our definition
- [deploy-time-learning-the-missing-middle](../deploy-time-learning-the-missing-middle.md) — contrasts: CrewAI Memory operates at the in-context timescale (accumulate during runs) with persistence, but has no theory of when to crystallise patterns into durable artifacts
- [claw-learning-is-broader-than-retrieval](../claw-learning-is-broader-than-retrieval.md) — contrasts: CrewAI Memory is purely retrieval-oriented; no mechanism for action-oriented knowledge types
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: the scope tree blurs workshop/library distinction rather than making it explicit
- [ClawVault](./clawvault.md) — sibling: both are agent memory systems; ClawVault models the process of learning, CrewAI models the infrastructure of remembering
- [automating-kb-learning-is-an-open-problem](../automating-kb-learning-is-an-open-problem.md) — extends: CrewAI's consolidation is an automated mutation that succeeds on deduplication but doesn't address the harder mutations (synthesise, regroup)

Topics:
- [related-systems](./related-systems-index.md)
