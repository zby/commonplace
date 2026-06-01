---
description: "Personal-brain CLI and MCP runtime with markdown-canonical pages, Postgres/PGLite indexes, trace-derived synthesis, skills, recipes, and maintenance cycles"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# GBrain

> Replaced 2026-06-01. See [gbrain](./gbrain.md) for the current review.

GBrain is Garry Tan's TypeScript/Bun personal-brain system for agent-operated knowledge work. The inspected implementation is not just a memory backend: it is a CLI, MCP server, Postgres/PGLite engine layer, markdown page contract, hybrid retrieval stack, agent skillpack, cron/minion maintenance loop, and integration recipe library for ingesting meetings, email, social media, voice, files, and code.

**Repository:** https://github.com/garrytan/gbrain

**Reviewed commit:** https://github.com/garrytan/gbrain/commit/3933eb6a7915cb5495b8057b75567e2b1588b5ac

## Core Ideas

**Markdown is the canonical user-knowledge substrate; the database is an operational projection.** The strongest architectural statement is explicit: the GitHub repo of markdown and frontmatter is the system of record, while Postgres/PGLite is a derived cache rebuilt by sync/extract/embed paths. Takes, facts, links, timelines, tags, emotional weight, and synthesis evidence are either markdown-authored or markdown-derived; runtime state such as raw data, minion jobs, OAuth tokens, MCP request logs, eval candidates, dream verdicts, and cycle locks are named DB-only exceptions ([docs/architecture/system-of-record.md](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/docs/architecture/system-of-record.md)).

**The engine boundary supports embedded and server deployments without changing the memory contract.** `createEngine` dispatches between `PGLiteEngine` and `PostgresEngine`; the engine interface covers pages, chunks, links, timeline entries, raw data, versions, code edges, eval candidates, facts, takes, salience, anomalies, and file rows ([src/core/engine-factory.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/engine-factory.ts), [src/core/engine.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/engine.ts)). PGLite loads vector and trigram extensions with a file lock and optional schema snapshot, while Postgres adds pooler-aware connection policy, DDL routing, pgvector schema adaptation, and migration execution ([src/core/pglite-engine.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/pglite-engine.ts), [src/core/postgres-engine.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/postgres-engine.ts), [src/core/db.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/db.ts)).

**Every page has a compiled-truth-plus-timeline contract.** Markdown parsing separates frontmatter, compiled truth, and timeline; the docs define compiled truth as current synthesis and timeline as append-only evidence ([src/core/markdown.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/markdown.ts), [docs/guides/compiled-truth.md](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/docs/guides/compiled-truth.md)). This is the central retained-artifact split: compiled truth is the high-authority knowledge artifact future agents read first; timeline entries preserve lineage and source evidence. The hybrid search stack then explicitly boosts compiled-truth chunks and backlink-heavy pages, with optional salience, recency, query expansion, token budgeting, multimodal search, code-symbol filters, and structural graph walks ([src/core/search/hybrid.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/search/hybrid.ts), [src/core/operations.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/operations.ts)).

**A contract-first operation registry feeds CLI, MCP, HTTP, and tool JSON surfaces.** `operations.ts` defines schemas, scopes, handlers, CLI hints, and local-only flags in one registry, then the CLI and MCP server derive command/tool behavior from it ([src/core/operations.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/operations.ts), [src/cli.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/cli.ts), [src/mcp/server.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/mcp/server.ts)). The surface is broad: page CRUD, search/query, links, timeline, sync, raw data, chunks, ingest logs, jobs, takes, salience, transcripts, facts, contradictions, experts, and code intelligence. Security posture is mixed but explicit: remote MCP strips private facts/takes on read, skips auto-linking on untrusted writes, hides local-only operations such as `sync_brain` and `file_upload`, and source-scopes search and page access.

**Deterministic primitives sit under agent-written content.** The system has zero-LLM lint rules for frontmatter, preamble artifacts, placeholder dates, citations, and empty sections; a filesystem backlink fixer; a publish command that strips frontmatter, sources, brain links, and timeline before generating optional password-protected HTML; and a BrainWriter with pre-commit validators for citations, links, backlinks, and compiled-truth/timeline hygiene ([src/commands/lint.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/commands/lint.ts), [src/commands/backlinks.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/commands/backlinks.ts), [src/commands/publish.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/commands/publish.ts), [src/core/output/writer.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/output/writer.ts), [src/core/output/validators/index.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/output/validators/index.ts)). These are system-definition artifacts in practice: they validate, rewrite, publish, or enforce shape instead of merely advising the agent.

**Skills and recipes are first-class behavior-shaping artifacts.** The resolver routes common tasks to markdown skills; the skillpack documents brain-first lookup, ingestion, enrichment, cron, Minions, publishing, skill development, and operational conventions; recipes encode installable integration workflows for calendar, email, meetings, X/Twitter, voice, credentials, and tunnels ([skills/RESOLVER.md](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/skills/RESOLVER.md), [docs/GBRAIN_SKILLPACK.md](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/docs/GBRAIN_SKILLPACK.md), [recipes](https://github.com/garrytan/gbrain/tree/3933eb6a7915cb5495b8057b75567e2b1588b5ac/recipes)). Their representational form is prose plus command snippets, but their behavioral authority is stronger than ordinary knowledge: agents consume them as routing, workflow, safety, and installation instructions.

**Trace-derived learning is implemented, not only described.** The maintenance cycle composes lint, backlinks, sync, transcript synthesis, extraction, fact extraction, symbol resolution, patterns, emotional-weight recomputation, fact consolidation, embedding, orphan checks, and purge into one lock-protected cycle ([src/core/cycle.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/cycle.ts)). The synthesize phase discovers `.txt`/`.md` transcripts, guards against re-consuming dream-generated output, caches Haiku significance verdicts, dispatches Sonnet subagents through Minions with slug allow-lists, reverse-renders resulting DB pages back to markdown, and writes a deterministic summary page ([src/core/cycle/transcript-discovery.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/cycle/transcript-discovery.ts), [src/core/cycle/synthesize.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/cycle/synthesize.ts)). Separately, the facts backstop extracts facts from page writes, queues or runs the pipeline inline, resolves/deduplicates/inserts facts, and logs absorbed failures; consolidation clusters repeated facts and promotes them into takes while retaining facts as audit trail ([src/core/facts/backstop.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/facts/backstop.ts), [src/core/facts/absorb-log.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/facts/absorb-log.ts), [src/core/cycle/phases/consolidate.ts](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/src/core/cycle/phases/consolidate.ts)).

## Comparison with Our System

| Lens axis | GBrain | Commonplace |
|---|---|---|
| Primary substrate | Markdown repo as system of record; Postgres/PGLite operational index | Markdown repo as both library and operating surface |
| Runtime layer | Large CLI/MCP/HTTP/job/runtime stack with auth, source scopes, engines, queues, code search, eval capture | Smaller Python CLI around validation, note operations, indexing, snapshots, and review workflows |
| Artifact contract | Page type, compiled truth, timeline, frontmatter, facts/takes fences, links, tags | Path-valued type specs, collection conventions, required sections, review status, semantic link labels |
| Trace-derived loop | Transcript synthesis, fact extraction, fact consolidation, eval capture/replay, cron/minion maintenance | Mostly human/agent-authored notes plus source snapshots and review workflows; automation is cautious |
| Behavioral authority | Skills, resolver, cron conventions, validators, operations registry, OAuth scopes, source scopes | AGENTS instructions, cp-skills, validators, type specs, review gates, generated indexes |
| Evidence and lineage | Timeline evidence, raw_data, ingest_log, source_id, page versions, facts fences, transcript files, dream verdicts | Source snapshots, citations, frontmatter, git history, review artifacts, validation reports |
| Retrieval | Hybrid keyword/vector/RRF, backlink boost, salience, recency, query expansion, code graph | Lexical search, generated indexes, backlinks, curated links; heavier search is outside the core method |

GBrain is closer to a production personal AI operating system than to a methodology KB. It has many mechanisms commonplace intentionally leaves outside the knowledge library: OAuth MCP, admin UI, minion job queue, source-scoped multi-repo federation, code-intelligence search, eval capture, multimodal files, integration recipes, cron deployment guidance, and embedded/server database choices.

Commonplace is more disciplined as a transferable knowledge medium. A commonplace review, note, ADR, or instruction has an explicit collection-level type contract and a smaller semantic surface. GBrain's page contract is strong for personal/entity knowledge, but its knowledge types are more product-specific: compiled truth, timeline, facts, takes, emotional weight, raw data, and source scope. That makes it operationally powerful but less general as methodology.

The deepest design divergence is where each system places trust. GBrain trusts automation enough to let scheduled cycles and subagents synthesize transcripts into pages, extract facts from writes, and promote repeated facts into takes. It compensates with allow-lists, caches, lint, fences, logs, source scopes, privacy stripping, and rebuildable indexes. Commonplace keeps more behavior in explicit notes, instructions, reviews, validation, and human-readable diffs before promotion.

**Read-back:** both — agents can query/search through CLI or MCP operations, and loaded skills/resolver guidance can shape behavior without lookup.

## Borrowable Ideas

**Compiled truth plus append-only timeline.** Ready to borrow where notes need a current synthesis plus evidence trail. Commonplace already distinguishes source snapshots from derived notes, but entity/project/workshop artifacts could benefit from making "current synthesis" and "evidence log" an explicit page-local contract.

**One operation registry for CLI, MCP, and generated tool definitions.** Ready when commonplace grows an MCP or API surface. GBrain's `Operation` shape keeps schema, scope, mutability, handler, and CLI hints together; that is cleaner than independently maintaining command help, MCP schemas, and handler dispatch.

**Markdown-canonical facts/takes fences with derived DB tables.** Worth borrowing only with a concrete high-volume fact use case. The design is strong because it preserves inspectable source-of-truth rows while allowing database retrieval and consolidation. It would be overkill for ordinary commonplace notes today.

**Trace capture as opt-in eval data.** Ready to borrow for retrieval evaluation. GBrain's `eval_candidates` loop captures real query/search calls only when contributor mode or config enables it, records retrieved slugs/chunks and retrieval metadata, and supports replay. A commonplace analogue could evaluate search/index changes from real agent lookup traces without making trace capture default.

**Validator lint before strict enforcement.** Ready now as automation rollout discipline. GBrain's BrainWriter defaults to lint mode and can later flip stricter behavior after observing validator noise. That is a good pattern for adding semantic or structural gates without breaking existing libraries immediately.

**Source and brain routing as separate axes.** Needs a multi-repo use case first. GBrain cleanly separates "which database" from "which repo inside that database" and makes agents responsible for cross-brain synthesis ([docs/architecture/brains-and-sources.md](https://github.com/garrytan/gbrain/blob/3933eb6a7915cb5495b8057b75567e2b1588b5ac/docs/architecture/brains-and-sources.md)). Commonplace may eventually need this for consuming projects, but the current single-repo methodology KB does not.

## Trace-derived learning placement

**Trace source.** GBrain consumes several trace classes: conversation transcript files for dream synthesis; meeting/email/social/voice data via recipes and skills; page writes through the facts backstop; query/search calls through opt-in eval capture; and minion/subagent tool executions for provenance of synthesized pages. Raw traces are files, raw_data rows, ingest logs, minion job/tool rows, eval_candidates, or source pages depending on the path.

**Extraction.** Extraction is mixed. Transcript synthesis uses deterministic discovery and self-consumption guards, Haiku significance verdicts, Sonnet subagents, slug allow-lists, idempotency keys, and reverse rendering. Fact extraction uses LLM extraction, entity resolution, embedding-based deduplication, insert/supersede logic, and absorb logs. Fact consolidation is currently deterministic clustering that promotes repeated facts to takes by choosing the highest-confidence fact, with comments noting later Sonnet synthesis as future work. Eval capture is not a learning pipeline by itself; it records retrieval traces for replay/regression.

**Storage substrate.** Raw source material lives in markdown repos, transcript files, raw_data, ingest logs, and runtime tables. Distilled user knowledge is intended to land in markdown pages or fenced facts/takes, then be projected into Postgres/PGLite tables. Runtime/index/tool state lives in Postgres/PGLite tables, PGLite locks, config rows, eval tables, OAuth tables, minion queues, and generated chunks/embeddings.

**Representational form.** The retained forms are mixed. Compiled truth, timeline entries, skills, recipes, and synthesis pages are prose. Operations, scopes, migrations, validators, queues, source routing, link extraction, and fences are symbolic. Embeddings, vector indexes, salience scores, emotional weights, and retrieval telemetry are distributed-parametric or numeric operational state. One stored object often bundles forms: a markdown page carries prose claims, symbolic frontmatter, symbolic fences, and links that become graph edges.

**Lineage.** GBrain has a stronger lineage story than most trace-mining systems because it explicitly separates source-of-truth markdown from derived DB projections, preserves timeline/source citations, records ingest logs, stores page versions, caches dream verdicts by file path and content hash, and marks contributing facts with `consolidated_into` instead of deleting them. The weak spot is semantic lineage after agent synthesis: a synthesized compiled-truth paragraph can be good, but the guarantee that every claim traces back to timeline evidence is a convention plus validators, not a complete proof.

**Behavioral authority.** Raw traces and timeline entries are knowledge artifacts: future agents consume them as evidence and context. Compiled truth is also a knowledge artifact, but with higher prompt-time authority because search boosts it and skills tell agents to rely on it. Skills, resolver rules, migrations, operation schemas, validators, source scopes, OAuth scopes, and cron/minion schedules are system-definition artifacts because they instruct, route, validate, authorize, or schedule behavior. Eval candidates can become system-definition inputs when replay gates retrieval changes.

**Scope and timing.** Scope is personal-brain or source-scoped rather than benchmark-only. Timing is online plus staged: query/search capture happens during tool use; page-write fact extraction can queue immediately; cron/minion cycles synthesize transcripts, extract, consolidate, embed, and purge later; recipes prescribe periodic ingestion.

**Survey placement.** On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), GBrain is a trace-to-artifact system with a unusually broad runtime shell. It strengthens the survey claim that trace-derived learning becomes practical when raw traces, distilled artifacts, and activation surfaces are separated. It also splits the artifact-learning category: some outputs are readable prose pages and takes, while much of the behavior change comes from symbolic runtime surfaces around those pages.

## Curiosity Pass

GBrain is strongest where product runtime and knowledge substrate meet. The operation registry, engine abstraction, MCP scopes, source routing, and minion cycle make the brain a live system, not a passive vault. That also means the trusted surface is large. A future reviewer should check whether the growing number of operations and DB-only exceptions continues to respect the system-of-record contract.

The compiled-truth/timeline contract is powerful but demanding. It assumes agents rewrite synthesis, preserve evidence, keep citations meaningful, and avoid letting stale compiled truth outrank newer timeline evidence. The validators catch several mechanical failures; they cannot fully judge whether the synthesis still follows from the timeline.

The trace-derived status is supported by implementation evidence, but it is not a single clean algorithm. It is a family of loops: transcript-to-page synthesis, page-write-to-fact extraction, repeated-fact-to-take consolidation, and retrieval-trace-to-eval replay. That breadth is useful, but comparisons should name which loop is being discussed.

The "database is only a cache" claim is mostly well-defended, but GBrain still has important DB-only runtime memory: raw_data, page_versions, dream_verdicts, eval candidates, minion logs, request logs, and auth scope state. The docs classify these as non-user-knowledge or infrastructure. That is a reasonable boundary, but it is a boundary worth auditing as features expand.

## What to Watch

- Whether BrainWriter strict mode becomes the default for page writes, and whether validators remain low-noise enough to enforce rather than merely warn.
- Whether fact consolidation moves from deterministic best-fact selection to LLM synthesis, and whether the resulting takes preserve enough source lineage.
- Whether eval capture/replay becomes a real promotion gate for search-mode or ranking changes rather than a contributor diagnostic.
- Whether source/brain federation remains understandable as OAuth scopes, remote MCP, team brains, and cross-source search grow.
- Whether the system-of-record CI gate continues to prevent DB-only user-knowledge drift.
- Whether the skill/recipe ecosystem stays reviewable, or becomes too large for agents to route safely without a stronger resolver/eval layer.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: GBrain combines transcript-to-page synthesis, write-time fact extraction, consolidation into takes, and opt-in retrieval-trace replay.
- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — qualifies: GBrain is explicitly markdown-canonical, but relies on a much heavier database projection than commonplace.
- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — exemplifies: transcript synthesis, minion jobs, eval candidates, and raw_data form a runtime/workshop layer feeding durable pages.
- [agent statelessness means the context engine should inject context automatically](../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) — exemplifies: GBrain exposes MCP/CLI/context-engine surfaces so agents retrieve and receive context at runtime.
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) — defined-in: GBrain's skills, operation registry, validators, migrations, auth scopes, and cron schedules are behavior-shaping system-definition artifacts.
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) — defined-in: GBrain's compiled truth, timeline evidence, facts, takes, and source pages are retained knowledge artifacts.
