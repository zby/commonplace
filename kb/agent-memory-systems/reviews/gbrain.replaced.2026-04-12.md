---
description: "Personal-brain CLI and MCP layer over markdown-derived Postgres/pgvector pages, with agent skillpacks for trace-to-entity enrichment and compiled-truth maintenance"
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: []
status: outdated
last-checked: "2026-04-11"
---

# GBrain

> Replaced 2026-04-12. See [gbrain](./gbrain.md) for the current review.

GBrain is Garry Tan's personal knowledge-brain project: a Bun/TypeScript CLI, MCP server, and OpenClaw plugin for indexing a markdown "brain" into Postgres + pgvector, then teaching an agent to read and maintain that brain through fat markdown skills. In the inspected repo, the shipped code is mostly the retrieval/indexing layer; the compounding memory loop lives in docs and skillpacks that tell an external agent how to detect entities, update pages, run cron jobs, and sync the derived database.

**Repository:** https://github.com/garrytan/gbrain

## Core Ideas

**The central page model is compiled truth plus timeline.** GBrain pages split the current assessment from the append-only evidence trail. `parseMarkdown(...)` stores body content above the first standalone `---` as `compiled_truth` and the content below as `timeline`; `importFromContent(...)` chunks those two fields separately. The schema mirrors the distinction with `pages.compiled_truth`, `pages.timeline`, and a separate `timeline_entries` table. This is a strong pattern because it precomputes synthesis while keeping an evidence log close enough for citation and staleness checks.

**The implementation treats Postgres as a derived retrieval engine, but the docs are not fully settled on the source-of-truth boundary.** The README says the markdown repo is the source of truth and GBrain makes it searchable. The code supports that through `gbrain import`, git-diff-based `gbrain sync`, content hashes, and `gbrain export`. But `GBRAIN_RECOMMENDED_SCHEMA.md` also describes database primitives such as an entity registry, event ledger, fact store, and relationship graph as the foundation, with markdown generated from them. The shipped code is closer to "files with a derived database index" than to the fuller database-generated-markdown architecture.

**Retrieval is hybrid and practical.** `PostgresEngine` implements keyword search with `tsvector`, vector search with pgvector HNSW, fuzzy slug resolution with `pg_trgm`, graph traversal with recursive CTEs, and health checks for stale pages, orphans, dead links, and missing embeddings. `hybridSearch(...)` expands the query, embeds each variant, runs keyword search concurrently with the embedding pipeline, fuses ranked lists through reciprocal rank fusion, then applies deduplication. The code's four-layer dedup is less mathematically strong than the comments imply because the cosine-similarity stage uses Jaccard text overlap as a proxy, but the overall retrieval stack is concrete.

**The operation contract is shared across CLI and MCP.** `src/core/operations.ts` defines roughly 30 operations with parameter schemas, handlers, mutability flags, and CLI hints. The local MCP server generates tool definitions and dispatch from the same operations array, while `test/parity.test.ts` checks contract structure. This is the best codified part of the repo: one operation surface feeds CLI, MCP, raw tool calls, and plugin packaging.

**Agent behavior lives in markdown skills, not application code.** The package does not implement its own entity-detection agent or meeting-ingestion scheduler. Instead, `GBRAIN_SKILLPACK.md` and `skills/*.md` tell an external agent to search before responding, detect entities on every message, ingest meetings, propagate facts to people/company/deal pages, run maintenance, and set up a dream cycle. The intelligence loop is therefore prompt-mediated and integration-dependent: OpenClaw or Hermes has to execute the skillpack faithfully.

**Some advertised mechanisms exist as code but are not wired into the main path.** The README describes three chunking strategies: recursive, semantic, and LLM-guided. `semantic.ts` and `llm.ts` do exist, but `importFromContent(...)` and `embed.ts` currently call only the recursive chunker. The repo's implementation is still strongest on core import/search/sync/MCP mechanics, weaker on selecting richer chunking policies and autonomous enrichment.

## Comparison with Our System

| Dimension | GBrain | Commonplace |
|---|---|---|
| Primary substrate | Markdown brain plus Postgres/pgvector index; docs partly tilt toward database primitives | Markdown files in git, with scoped derived indexes only where needed |
| Knowledge shape | Personal/entity intelligence pages: compiled truth plus timeline | Methodology notes, indexes, ADRs, instructions, and workshop artifacts |
| Retrieval | Keyword + vector + RRF + dedup + graph traversal through Postgres | `rg`, indexes, descriptions, explicit links, validation, and review metadata |
| Agent workflow | Fat skills tell external agents how to read/write/enrich | Skills and instructions are part of the KB's own methodology and runtime packaging |
| Link model | Typed DB edges plus wiki/slug conventions; relationship semantics are operational | Markdown links with prose relationship phrases as part of the argument |
| Learning loop | Trace/event ingestion into durable personal brain pages and MEMORY.md, mostly prompt-mediated | Workshop-to-library distillation through human+agent curation and review gates |
| Governance | Health checks, RLS checks, import idempotency, version snapshots | Deterministic note validation, semantic review gates, type instructions |

GBrain and Commonplace share the strongest architectural instinct: keep knowledge inspectable and make derived retrieval rebuildable. The divergence is timing. Commonplace stays files-first until a specific subsystem earns a database. GBrain starts from a large personal corpus where grep has already failed, so it pays the Postgres/pgvector cost early and builds a real operation layer over it.

The tradeoff follows from the domain. GBrain wants to answer high-volume personal-intelligence questions over thousands of people, meetings, notes, and media pages. That makes entity identity, hybrid retrieval, and background sync central. Commonplace wants to preserve methodology and design claims for future agents. That makes document type, link semantics, review quality, and argument structure more central than raw recall.

Relative to [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md), GBrain belongs on the symbolic-artifact side. It mines conversation, meeting, email, and social traces into markdown pages, timelines, and MEMORY.md rather than weights. Its distinctive point is not the database backend; it is the operational claim that every signal pathway should end by enriching durable entity pages.

## Borrowable Ideas

**Compiled truth plus timeline as a page-local staleness contract.** Ready to borrow where notes represent evolving entities, cases, or workshop state. Commonplace already separates workshop artifacts from library artifacts, but some long-running workshop pages could benefit from a first-class "current assessment above, evidence log below" convention.

**Single operation registry for CLI and MCP surfaces.** Ready to borrow if we expose more commands through multiple tool interfaces. GBrain's `operations.ts` pattern prevents CLI/MCP/schema drift and gives tests a clean parity target.

**Treat the derived index as operational infrastructure, not the knowledge substrate.** Ready to borrow as a boundary principle. GBrain's best moments are import/sync/export/idempotency paths that make Postgres rebuildable from markdown. If Commonplace adds richer retrieval, the index should stay disposable unless a specific workflow truly needs database-native state.

**Health checks that expose knowledge freshness, not just service liveness.** Needs a concrete use case first. GBrain's `getHealth()` asks about stale compiled truth, missing embeddings, orphan pages, and dead links. The exact metrics do not transfer cleanly to our file-first KB, but the framing does: retrieval infrastructure should report knowledge-quality failure modes, not merely "database reachable."

**Trace ingestion should terminate in domain pages, not a generic memory bucket.** Needs careful adaptation. GBrain's meeting-ingestion skill is strong because a meeting is not done until attendees, companies, deals, and action items have been updated. For Commonplace, the analogue would be workshop traces that promote into specific notes, ADRs, or instructions rather than one catch-all reflection log.

## Curiosity Pass

The word "brain" risks hiding two different systems. One system is implemented: a Postgres-backed retrieval and MCP layer over markdown-derived pages. The other is prescribed: an autonomous personal-intelligence agent that monitors meetings, email, social feeds, and conversations, then enriches the brain continuously. The second system is plausible, but in this repo it is mostly skills and integration instructions rather than a scheduler, parser, or evaluator in the package itself.

The files-vs-database position is also not fully clean. The README's "markdown repo is the source of truth" framing is compatible with our files-first doctrine and with GBrain's import/sync/export code. The recommended schema's "structured database layer provides the foundation" framing points somewhere else: database identity and event primitives generating markdown views. That may be the right future for GBrain's high-volume personal-entity use case, but it is a different architecture than the current code demonstrates.

The chunking story is a good naming-vs-mechanism check. Semantic and LLM-guided chunkers exist as modules, so the claim is not pure vapor. But the import and embedding paths appear to use the recursive chunker. The current working mechanism is therefore simpler than the docs' three-tier retrieval story.

The strongest idea is page-local synthesis with provenance pressure. Compiled truth plus timeline is not just a storage format; it creates an update discipline. New evidence has somewhere append-only to land, and the current assessment has somewhere explicit to be rewritten. That discipline is closer to our note-maintenance problem than the pgvector machinery is.

## What to Watch

- Whether the main import/embed path starts selecting semantic or LLM-guided chunkers, or whether recursive chunking remains the real default behind richer docs
- Whether GBrain resolves the source-of-truth boundary toward markdown-first with derived Postgres, or toward database primitives with generated markdown views
- Whether OpenClaw/Hermes dream-cycle integration becomes code-inspectable in this repo, instead of remaining a skillpack contract for external agents
- Whether the health checks evolve from retrieval/backend metrics into stronger epistemic checks: contradiction surfacing, entity merge quality, provenance coverage, and stale synthesis review
- Whether the operation registry remains stable as remote MCP and OAuth support expand beyond the local stdio server

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — contrasts: GBrain is the boundary case where a large personal corpus plausibly earns a Postgres/pgvector derived index, while still trying to keep markdown inspectable
- [pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: GBrain's chunks, search scores, stale flags, and page summaries are query-time and page-local pointers rather than authored relationship phrases
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: GBrain should be added as a prompt-mediated conversation/meeting/event-trace to symbolic personal-brain system
- [Claw learning loops must improve action capacity not just retrieval](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — exemplifies: GBrain's skillpack targets meeting prep, entity enrichment, communication, and briefing, not only question answering
- [Distillation](../../notes/definitions/distillation.md) — sharpens: compiled truth is directed compression of timelines and raw traces into current assessments
- [Napkin](./napkin.md) — compares: both adapt markdown knowledge for agents, but Napkin stays closer to Obsidian/file tooling while GBrain pays for a database retrieval layer
- [Cognee](./cognee.md) — contrasts: both use database/graph/vector infrastructure, but GBrain keeps more emphasis on human-readable compiled pages and agent skill workflows
