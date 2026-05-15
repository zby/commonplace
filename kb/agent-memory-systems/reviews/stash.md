---
description: "Postgres/pgvector MCP memory service that turns episodes into facts, relationships, causal links, goals, failures, hypotheses, and confidence decay"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-25"
---

# Stash

Stash is Mohamed Al-Ashaal's self-hosted memory service for MCP-compatible agents. The repository is a Go CLI/server that stores raw observations as embedded episodes in Postgres with pgvector, then periodically consolidates them into structured facts, entity relationships, causal links, patterns, goal annotations, failure-pattern memories, hypothesis status changes, and decayed confidence. The project markets this as a "cognitive layer"; the code-backed version is more precise: a database-backed MCP tool plane plus an incremental LLM extraction pipeline over namespaced memories. The repository is https://github.com/alash3al/stash.

**Repository:** https://github.com/alash3al/stash

**Reviewed commit:** https://github.com/alash3al/stash/commit/d1122a699cf2f0022409fbdf97871298273c20a6

## Core Ideas

**Postgres is the memory substrate, and pgvector is mandatory.** Stash is not a file-first memory system. Configuration requires a Postgres DSN, vector dimension, OpenAI-compatible embedding model, and OpenAI-compatible reasoner model ([internal/config/config.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/config/config.go)). The migrations create tables for namespaces, episodes, facts, fact sources, relationships, patterns, contexts, consolidation progress, embedding cache, contradictions, causal links, hypotheses, goals, and failures, all under Postgres with the `vector` extension enabled ([internal/db/migrations](https://github.com/alash3al/stash/tree/d1122a699cf2f0022409fbdf97871298273c20a6/internal/db/migrations)). Docker Compose packages this as a pgvector container plus the Stash MCP server and background consolidation service ([docker-compose.yml](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/docker-compose.yml)).

**The raw write is an embedded episode.** `Remember(...)` validates content and namespace path, resolves the namespace, embeds the text, and inserts an immutable-ish row into `episodes`; `forget` soft-deletes the nearest episode by embedding similarity ([internal/brain/episode.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/brain/episode.go)). The schema keeps source episodes separate from facts through a `fact_sources` join table, so consolidation can preserve provenance at the row level even though the MCP response surfaces are compact.

**Recall prefers consolidated facts but falls back to episodes.** `Recall(...)` embeds the query, searches facts first, then fills remaining slots with episode hits, and sorts the combined result by vector score ([internal/brain/recall.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/brain/recall.go), [internal/queries/recall.sql.tmpl](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/queries/recall.sql.tmpl)). That is a clean two-layer retrieval contract: facts are the higher-quality distilled layer, while episodes remain available as lower-level evidence and fallback.

**Consolidation is incremental and stage-checkpointed.** `ConsolidateByID(...)` reads the namespace's `consolidation_progress` row, then runs stages for episode-to-fact synthesis, fact-to-relationship extraction, causal-link extraction, goal-progress annotation, failure-pattern detection, pattern extraction, hypothesis-evidence scanning, and confidence decay before saving checkpoints ([internal/brain/consolidate.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/brain/consolidate.go)). The checkpoint table tracks separate last-seen IDs for episodes, facts, relationships, pattern inputs, goal facts, failures, failure episodes, hypotheses, and decay ([internal/db/migrations/00010_create_consolidation_progress.sql](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/db/migrations/00010_create_consolidation_progress.sql), [internal/db/migrations/00020_add_consolidation_checkpoints.sql](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/db/migrations/00020_add_consolidation_checkpoints.sql)). This makes the pipeline resumable, but also makes stage ordering and checkpoint semantics load-bearing.

**The LLM reasoner is deliberately extractive.** The OpenAI reasoner uses a strict system prompt, JSON-only outputs, retry-on-invalid behavior, and some grounding checks, then exposes separate methods for facts, relationships, patterns, contradictions, causal links, goal progress, failure patterns, and hypothesis evidence ([internal/reasoner/openai.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/reasoner/openai.go), [internal/reasoner/reasoner.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/reasoner/reasoner.go)). The design is stronger than a single "summarize memories" prompt because each output type has a narrower schema. It is still LLM-judged extraction, not independently verified learning.

**Memory roles are separate database types, not just tags.** Facts carry `entity`, `property`, `value`, confidence, validity windows, and sources; relationships are entity edges; causal links are fact-to-fact edges; goals have status, parent, priority, and notes; failures require content, reason, and lesson; hypotheses have a small state machine and can promote into facts when confirmed ([internal/models/models.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/models/models.go), [internal/brain/goal.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/brain/goal.go), [internal/brain/failure.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/brain/failure.go), [internal/brain/hypothesis.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/brain/hypothesis.go)). This is Stash's best schema-level idea: it distinguishes memory roles that many systems collapse into one vector record.

**MCP is the main agent-facing surface.** The MCP server registers tools for initialization, remember/recall/forget/consolidate, context, namespaces, facts, relationships, contradictions, causal links, hypotheses, goals, and failures ([cmd/cli/mcp.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/cmd/cli/mcp.go)). `init` scaffolds `/self` plus capability, limit, and preference namespaces, which makes self-model memory an explicit convention rather than an emergent tag ([cmd/cli/mcp.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/cmd/cli/mcp.go)). The same binary also exposes CLI commands and an HTTP server, but MCP is the distribution story the README emphasizes ([README.md](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/README.md)).

## Comparison with Our System

| Dimension | Stash | Commonplace |
|---|---|---|
| Primary substrate | Postgres + pgvector tables | Markdown files in git |
| Write unit | Embedded episode, plus explicit goals/failures/hypotheses | Typed notes, instructions, reviews, sources, and indexes |
| Learned unit | Facts, relationships, patterns, causal links, failure facts, hypothesis-derived facts | Authored notes, links, instructions, review decisions, and generated indexes |
| Retrieval | Vector search over facts first, then episodes | Search, descriptions, curated/generated indexes, link traversal |
| Lifecycle | Confidence decay, validity windows, soft deletion, contradiction records, hypothesis state transitions | Status frontmatter, git history, validation, review gates, explicit supersession/replacement |
| Integration surface | MCP tools, CLI, HTTP server, Docker Compose | Agent skills, CLI commands, repository conventions |
| Evaluation | No committed test suite or behavioral benchmark in the inspected repo | Deterministic validation plus semantic review workflows |

Stash is stronger where a live agent needs a compact, typed operational memory service. Its MCP tool set gives an agent direct verbs for self-knowledge, goals, failures, hypotheses, contradictions, and causal chains. Commonplace has richer document semantics, but it does not give an arbitrary MCP client a ready-made `create_failure` or `trace_causal_chain` tool.

Commonplace is stronger where the memory needs to become inspectable knowledge. A Stash fact has content, confidence, source rows, and structured fields, but it is still a short database record. A commonplace note can carry argument, caveats, source links, relationship labels, and review status. Stash improves continuity for the next run; commonplace improves the library an agent can reason over.

The deepest split is agency. Stash lets the agent and background service decide what to remember, synthesize, decay, and surface. Commonplace makes durable knowledge mutation slower and more explicit: the authoring and review process is part of the artifact's trust story. Stash is a better operational memory daemon; commonplace is a better cumulative methodology library.

## Borrowable Ideas

**Typed operational memories deserve separate affordances.** Ready to borrow conceptually. Stash's separation of goals, failures, hypotheses, contradictions, causal links, context, and facts is better than treating every durable memory as the same note-like blob. In commonplace this argues for keeping workshop/runtime state typed when it has different lifecycle rules, rather than forcing everything into library notes.

**Fact-source joins are a good provenance primitive.** Ready to borrow for generated artifacts. Stash's `fact_sources` table is the database version of a citation map. For any future generated commonplace digest or synthesized review, the equivalent should be an explicit source map, not only prose citations.

**Stage-specific checkpoints make background distillation operable.** Ready when automation exists. Stash tracks progress per pipeline stage, not just "last consolidation run." A commonplace automation loop that extracts candidates from work logs, reviews, or sources would need the same granularity to avoid reprocessing and to recover from partial runs.

**Failures should be first-class operational memory.** Ready to borrow. A failure record with content, reason, lesson, optional goal, and later repeat detection is a concrete target for workshop memory. Commonplace has review warnings and notes about failure modes, but not a compact runtime object for "do not repeat this local mistake."

**Hypotheses need lifecycle, not just prose.** Useful but needs a use case. Stash's proposed/testing/confirmed/rejected state machine and confirmation-to-fact promotion show a narrow way to operationalize conjectures. Commonplace should not copy the database form, but a similar lifecycle could help workshop notes that are waiting on evidence.

## Trace-derived learning placement

Stash is a **service-owned trace-derived memory backend** on the trace-derived learning survey's ingestion axis and a **symbolic/prose artifact learner** on the promotion-target axis.

**Trace source.** The raw trace source is whatever an agent records through `remember` or equivalent CLI/API calls: observations, conversations, decisions, failures, preferences, and other session-local content. The repository does not automatically ingest full Claude/Codex transcripts by itself; the consuming agent must call the memory tools. Once stored, each episode has content, an embedding, an occurrence time, and namespace ownership.

**Extraction.** Consolidation clusters new episodes by embedding similarity, asks an LLM to extract one structured fact per cluster, embeds the fact, deduplicates against existing facts by vector score, links fact sources, and then runs additional extraction stages for relationships, causal links, patterns, goal progress, failure patterns, and hypothesis evidence ([internal/brain/consolidate.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/internal/brain/consolidate.go)). The oracle is mostly the reasoner prompt plus schema validation; there is no separate behavioral test or human approval loop.

**Representational form.** The learned state is symbolic database structure plus prose fields. Facts, relationships, causal links, hypotheses, goals, failures, contradictions, and checkpoints are structured rows; fact and pattern content remains natural language; embeddings are opaque numeric support state.

**Behavioral authority.** Most learned artifacts are knowledge artifacts: retrieved facts and episodes inform future prompts. Some rows are closer to system-definition artifacts: `/self/preferences`, failure lessons, active goals, and confirmed hypotheses can change how the agent plans or behaves when recalled. The system still relies on the consumer agent to ask for or heed those memories.

**Scope.** Scope is namespace-local with descendant expansion. The `/self` scaffold gives a conventional self-model area, while arbitrary namespace paths let users split projects, domains, or agents. It is not inherently cross-harness transcript mining; it is cross-client only insofar as multiple MCP clients share the same Stash service and namespaces.

**Timing.** Timing is online plus background/staged. Episodes are written during use. Consolidation can be triggered by MCP/CLI or run as a background service on an interval ([cmd/cli/consolidate.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/cmd/cli/consolidate.go), [cmd/cli/serve_all.go](https://github.com/alash3al/stash/blob/d1122a699cf2f0022409fbdf97871298273c20a6/cmd/cli/serve_all.go)).

**Survey placement.** Stash belongs near REM, Hindsight, Memori, SignetAI, and OpenViking: a service-side memory substrate that turns raw interaction material into structured recall units. It strengthens the survey's recurring finding that extraction is easier to implement than trusted maintenance. Compared with REM, Stash has a richer maintenance schema already wired into code: contradictions, confidence decay, hypothesis transitions, goals, and failures. Compared with SignetAI, it is narrower on capture and governance: no cross-harness hook layer, no transcript lineage, and no benchmark harness in the inspected repo.

## Curiosity Pass

**The "8-stage" framing is mostly real, but the numbering is messy.** The README and docs advertise an 8-stage pipeline. The code does run many stages, but comments label them out of order: stage 3.5 causal links, stage 6 goal progress, stage 7 failure patterns, stage 3 patterns, stage 8 hypotheses, stage 5 decay. The implemented mechanism matters more than the numbering, but the review should treat "8-stage" as product vocabulary over a set of concrete functions.

**The strongest implementation choice is role separation, not vector search.** Many systems have embedding recall. Stash is more interesting because failures, hypotheses, causal links, contradictions, goals, contexts, and self-model namespaces are separate concepts with separate tools. That gives agents different verbs for different kinds of memory.

**Automatic consolidation can create behavior-changing state without a strong correctness oracle.** The reasoner prompt is conservative, and some grounding checks exist, but derived facts, causal links, goal notes, and failure patterns can still be wrong. Stash has lifecycle machinery for decay and contradiction, but not an external evaluator that proves the memory improves future action.

**Fact retrieval outranks episode retrieval by construction.** Recall fills the whole requested limit with facts first, then only searches episodes for leftover slots. This correctly prioritizes distilled memories when enough facts exist, but it can hide raw evidence unless the agent asks through other tools. That is a real tradeoff: concise continuity versus auditability at retrieval time.

**The self-model scaffold is small but important.** `init` creates `/self/capabilities`, `/self/limits`, and `/self/preferences`. That is a practical convention for separating self-knowledge from world knowledge, and it avoids relying on accidental semantic clustering to create that boundary.

**There is little visible evaluation infrastructure.** The inspected repository has release automation and health checks, but no committed Go test files or benchmark harness. For a system that automatically mutates memory, the lack of behavioral regression tests is a real watch item.

## What to Watch

- Whether Stash adds transcript capture or client hooks, so memory creation is less dependent on agents deciding when to call `remember`.
- Whether the reasoner gains a second judge, human approval mode, or benchmark loop for validating extracted facts, causal links, failure patterns, and hypothesis transitions.
- Whether recall exposes stronger provenance by default, especially when returning distilled facts before source episodes.
- Whether stage checkpoints remain correct as the pipeline grows; shared IDs across relationship, causal, pattern, goal, and hypothesis stages are easy to make subtly stale.
- Whether the system develops team or multi-agent authority rules around who can create, confirm, reject, resolve, or purge memory.
- Whether the no-test state changes before the consolidation pipeline becomes more ambitious.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Stash is a service-owned episode-to-structured-memory pipeline with richer operational memory roles than many vector-only backends.
- [Agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) - exemplifies: Stash spans storage, activation, learning, goals, failures, and MCP integration rather than treating memory as only retrieval.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - qualifies: Stash stores and retrieves memory, but behavior still depends on when the agent calls recall and how it uses the returned material.
- [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) - aligns: Stash keeps raw episodes separate from distilled facts, instead of replaying all history into the next context.
- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) - extends: Stash's self namespaces, operational contexts, and factual memories show a practical lifecycle split without needing the cognitive analogy.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - supports: Stash implements candidate extraction and lifecycle machinery, while correctness and usefulness remain the difficult oracle problem.
- [Hindsight](./hindsight.md) - compares: both are Postgres/pgvector service-owned memory backends with LLM fact extraction, typed links, and consolidation; Hindsight is the production-grade, evidence-grounded multi-retriever version.
- [SAGE](./sage.md) - compares: both expose memory through MCP and support database-backed confidence decay; SAGE invests in validation and provenance gates while Stash invests in richer consolidation roles.
- [cass-memory](./cass_memory_system.md) - compares: both treat failures as first-class learned material; cass-memory compiles confidence-decayed playbook guidance while Stash stores typed failure records with reason, lesson, and repeat-pattern extraction.
- [Agent memory coverage](../../reference/agent-memory-coverage.md) - see-also: maps Commonplace's file-backed memory surfaces against requirements, giving a local contrast to Stash's service-owned DB/tool-plane design.
- [Distilled artifacts need source tracking at the source](../../notes/distilled-artifacts-need-source-tracking-at-the-source.md) - rationale: Stash's `fact_sources` table is a concrete database analogue of source-side tracking for distilled artifacts.
- [REM](./REM.md) - compares: both consolidate episodes into facts, but Stash uses one Postgres/pgvector substrate and wires more lifecycle objects into code.
- [SignetAI](./signetai.md) - compares: both are MCP-facing trace-derived memory services, but Signet emphasizes cross-harness capture and governance while Stash emphasizes typed cognitive objects.
- [OpenViking](./openviking.md) - compares: both expose agent memory through service tools and namespace-like organization, but OpenViking builds virtual filesystem tiers while Stash stores typed rows in Postgres.
