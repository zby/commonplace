---
description: "Kompl review: SQLite-backed knowledge compiler that ingests sources into a generated wiki with provenance, FTS/vector retrieval, MCP tools, and chat-derived drafts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Kompl

Kompl, from the `tuirk/Kompl` repository, is a local knowledge compiler that turns URLs, files, bookmarks, text, and connector imports into an automatically written wiki. The inspected revision runs a Next.js app, Python NLP service, n8n trigger layer, SQLite store, compressed page/source files, vector service, CLI, and MCP server; its main behavior-shaping loop is source ingest -> extraction -> entity/concept resolution -> page planning -> LLM drafting -> wikilink/provenance commit.

**Repository:** https://github.com/tuirk/Kompl

**Reviewed commit:** [8f16a0bb43105591daf4f15ececb788f66434305](https://github.com/tuirk/Kompl/commit/8f16a0bb43105591daf4f15ececb788f66434305)

**Last checked:** 2026-06-04

## Core Ideas

**The wiki is a compiled derivative of sources, not a user-authored note garden.** The README frames Kompl as a compiler that reads scattered inputs and writes interlinked entity, concept, comparison, overview, and source-summary pages ([README.md](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/README.md)). The code matches that frame: users stage inputs, the pipeline stores raw markdown, extracts structured knowledge, plans pages, drafts markdown, commits pages, provenance, FTS rows, wikilinks, aliases, and vector upserts ([app/src/app/api/compile/run/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/compile/run/route.ts), [app/src/app/api/compile/commit/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/compile/commit/route.ts)).

**Compilation is staged and resumable.** `/api/compile/run` orchestrates health, ingest, extract, resolve, match, plan, draft, crossref, commit, and schema steps while recording per-step state in `compile_progress`; extraction and planning are derived from database state rather than only from progress flags, so partial failures can retry without redrafting every successful sibling ([app/src/app/api/compile/run/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/compile/run/route.ts)). The new orphan-queue cleanup cancels never-started queued sessions before a fresh finalize, and `updateCompileStep` avoids resurrecting cancelled sessions when late workers report progress ([app/src/lib/db.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/db.ts), [app/src/__tests__/supersede-orphan-queued.test.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/__tests__/supersede-orphan-queued.test.ts)).

**Entity memory is cross-session, but source-grounded.** Extraction writes entity and relationship mentions per source; resolution then uses fuzzy matching, embeddings, existing aliases, existing page titles, and LLM disambiguation to update aliases and re-canonicalize the current session's mention rows ([app/src/app/api/compile/extract/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/compile/extract/route.ts), [app/src/app/api/compile/resolve/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/compile/resolve/route.ts)). The alias and mention tables make later sources compound with older sources without treating chat or tool logs as the main learning input.

**Context efficiency is built around compiled pages plus bounded retrieval.** Kompl does not send raw source piles to the chat model by default. Small wikis send a lightweight page index to an LLM selector; large wikis combine FTS5 search, vector search, source-count weight, and recency, then fetch at most ten pages and give full content only to the top five while later pages get summaries ([app/src/lib/retrieval.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/retrieval.ts), [app/src/app/api/chat/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/chat/route.ts)).

**Adoption surfaces are local-first and agent-readable.** The CLI manages the Docker stack and backups; MCP exposes `search_wiki`, `read_page`, `list_pages`, and `wiki_stats`; direct HTTP routes expose search, page data, graph, chat, and export/import ([README.md](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/README.md), [mcp-server/index.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/mcp-server/index.ts), [cli/src/index.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/cli/src/index.ts)).

## Artifact analysis

- **Storage substrate:** `sqlite` — The central retained store is `/data/db/kompl.db`, with tables for sources, pages, provenance, aliases, extractions, page plans, compile progress, chat messages, ingest failures, vector backfill, mentions, relationships, staging, FTS, and settings; compressed raw/page files and the vector service are important adjuncts, but SQLite is the coordinating substrate ([app/src/lib/db.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/db.ts), [scripts/migrate.py](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/scripts/migrate.py)).
- **Representational form:** `prose` `symbolic` `parametric` — Wiki pages, source summaries, chat answers, draft content, and activity reasons are prose; tables, frontmatter, compile states, aliases, page plans, provenance, FTS rows, links, settings, and MCP schemas are symbolic; vector upserts/search add parametric retrieval state ([app/src/lib/vector-upsert.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/vector-upsert.ts), [app/src/lib/retrieval.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/retrieval.ts)).
- **Lineage:** `authored` `imported` `trace-extracted` — Prompts, code, schemas, workflows, settings, and API contracts are authored; source markdown and connector imports are imported; the narrow trace-extracted path is chat compounding, where a chat question/answer and pages-used list create a pending `query-generated` draft in `page_plans` ([app/src/app/api/chat/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/chat/route.ts), [app/src/lib/db.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/db.ts)).
- **Behavioral authority:** `knowledge` `routing` `validation` `ranking` `learning` `enforcement` — Pages and provenance are knowledge context; aliases, mentions, page plans, wikilinks, compile steps, and n8n triggers route work; health checks, schema/migration checks, source statuses, progress gates, cancellation, thin-draft gates, and pending approvals validate or enforce; FTS/vector/source-count/recency scores rank read-back; extraction, resolution, matching, synthesis, and chat-draft creation implement learning-like updates to the wiki surface.

**Source and page records.** `sources` rows retain metadata, content hashes, compile status, title-rescue markers, and raw markdown paths; `pages` rows retain generated page metadata, summaries, source counts, content paths, pending content, and previous-content paths. Raw markdown and page markdown are compressed files, while SQLite records decide visibility, provenance, searchability, and retry behavior ([app/src/lib/db.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/db.ts)).

**Plans, progress, and drafts.** `page_plans` is a behavior-shaping work queue: compile plans can create, update, record provenance-only links, wait for approval, fail, or commit; chat-generated drafts use the same table with `page_type='query-generated'` and `draft_status='pending_approval'` ([app/src/app/api/compile/plan/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/compile/plan/route.ts), [app/src/lib/approve-plan.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/lib/approve-plan.ts)).

**Access structures.** `pages_fts`, `page_links`, aliases, entity/relationship mentions, vector records, and vector backfill rows are derived access structures. They do not replace the wiki page, but they decide what future compilation, chat retrieval, graph views, and MCP tools can cheaply find.

**Promotion path.** Kompl's main promotion path is imported source -> extraction rows and mentions -> resolved aliases -> page plans -> drafted wiki pages -> committed pages with provenance, links, FTS, and vectors. A secondary path promotes chat answers into pending drafts, then into pages only through approval.

## Comparison with Our System

Kompl and Commonplace both treat Markdown-like prose as operational memory, but they put authority in different places. Commonplace's durable artifacts are authored, typed, reviewed, and validated in git; Kompl's durable wiki pages are generated from source material and governed by SQLite state, LLM calls, retry queues, and approval gates. Commonplace is stronger for explicit methodology claims and reviewable diffs. Kompl is stronger for turning many imported sources into a navigable generated wiki without requiring users to hand-write pages.

The nearest Commonplace analogue is source snapshot -> extraction -> reviewed artifact, but Kompl automates much more of the middle: entity resolution, page promotion thresholds, contradiction triage, overview/comparison page planning, wikilink syncing, and retrieval indexes. The tradeoff is that Kompl must trust LLM extraction and drafting quality; Commonplace leaves more semantic authority with humans or review agents.

### Borrowable Ideas

**Outbox-backed page commit.** Kompl's `pending_content` pattern separates synchronous DB commit from async file flush while leaving a boot-recoverable outbox. Commonplace could borrow this for any future operation that must update an index/database and a file together.

**Wiki-wide promotion thresholds.** Entity and comparison pages are created only when mention/relationship counts cross thresholds. Commonplace could use a similar threshold for promoting repeated log observations into candidate notes, but it needs a concrete log-to-note workflow first.

**Draft approval as a lower-authority buffer.** Auto-approve off mode and chat compounding both hold generated pages in `pending_approval`. Commonplace can borrow the status distinction for generated notes that should be reviewable before entering the library layer.

**Queue supersession for abandoned work.** Cancelling never-started orphan sessions before starting a new one is a practical gate-management pattern for long review or indexing runs. Ready now for workflows with a single-writer constraint.

## Write side

**Write agency:** `manual` `automatic` — Users manually stage inputs, configure settings, approve or reject drafts, delete/archive sources, trigger retries, and request chat; automatic paths ingest source material, extract entities/concepts/relationships, rescue titles, resolve aliases, plan pages, draft/crosslink/commit pages, update provenance and indexes, queue vector backfill, create chat drafts, cancel orphan queued sessions, and prevent cancelled sessions from re-entering running state.

**Curation operations:** `dedup` `evolve` `synthesize` `invalidate` — Alias resolution, existing-page-title matching, within-session canonical dedup, and page-plan dedup avoid duplicate entities/concepts/pages; update plans and mention re-canonicalization evolve existing pages and metadata; comparison/overview pages and chat FAQ drafts synthesize new pages from multiple retained inputs; source delete/archive cleanup, orphan queued-session supersession, stale-session failure, and cancelled-session guards invalidate stale operational state, while contradiction triage logs conflicts without rewriting the contradicted page.

### Trace-derived learning

**Trace source:** `session-logs` — The qualifying trace-derived path is chat compounding: a chat turn stores user/assistant messages, pages used, and citations, then creates a pending `query-generated` page draft when the answer used at least three pages ([app/src/app/api/chat/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/chat/route.ts)).

**Learning scope:** `per-project` — The draft is scoped to the local wiki and cited page ids, not a cross-install memory.

**Learning timing:** `online` — The candidate draft is created during the chat request after synthesis succeeds.

**Distilled form:** `prose` `symbolic` — The draft is prose markdown with frontmatter and symbolic `page_plans` fields linking it to a chat session and pages-used list.

**Extraction.** The oracle is the chat synthesis call over retrieved wiki pages; Kompl then wraps the answer, question, and citations into a pending draft. This is narrower than systems that mine tool traces or repeated trajectories: the main compiler still learns from imported source material, not from agent execution logs.

**Scope and timing.** The trace-derived artifact has no effect until approval runs the shared single-plan commit path. That approval promotes it from candidate draft into a wiki page with FTS, wikilink sync, optional alias backfill, and vector upsert.

**Survey fit.** Kompl splits the survey category: its primary source-to-wiki loop is imported-source distillation, while chat compounding is trace-derived candidate generation with human approval before durable wiki authority.

## Read-back

**Read-back:** `both` — MCP and direct wiki APIs are pull surfaces, while Kompl chat pushes selected retained wiki pages into the synthesis call after the user asks a question; the synthesis model does not issue its own memory lookup.

**Read-back signal:** `inferred / lexical` `inferred / embedding` `inferred / judgment` — Small-wiki chat sends a lightweight page index to an LLM page selector; large-wiki chat combines FTS5 lexical search, vector similarity, source-count and recency scoring, then truncates selected pages for synthesis. Direct MCP `search_wiki` and `read_page` remain explicit pull operations.

**Faithfulness tested:** `no` — The inspected code tests routing, settings, retries, and regressions, but I did not find an ablation or post-answer audit that verifies a selected page actually changed the chat answer or later user action.

**Direction edge cases.** The MCP server cannot push memory by itself: it exposes `search_wiki`, `read_page`, `list_pages`, and `wiki_stats`, all called by a host agent or user ([mcp-server/index.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/mcp-server/index.ts)). The web chat route is different: it receives a user question, retrieves pages internally, and sends those pages to `/chat/synthesize` before the answer is produced ([app/src/app/api/chat/route.ts](https://github.com/tuirk/Kompl/blob/8f16a0bb43105591daf4f15ececb788f66434305/app/src/app/api/chat/route.ts)).

**Selection, scope, and complexity.** Chat selection is bounded to ten retrieved pages; top five get up to 2,000 characters in the synthesis payload and later pages get summaries, while underlying retrieval caps content reads at 8,000 characters per page. Actual context dilution is not proven by code.

**Authority at consumption.** Retrieved pages are advisory evidence for chat answers and MCP clients. Pending drafts and approved pages can later shape compilation and retrieval more strongly through FTS, vectors, provenance, aliases, and page links, but chat read-back itself is not an enforcement gate.

**Other consumers.** Humans consume the wiki UI, source pages, graph, activity feed, saved links, draft approval UI, settings, backups, and CLI output. n8n, the Next.js orchestrator, the NLP service, MCP clients, and vector backfill jobs consume narrower slices of the same retained state.

## Curiosity Pass

**The name "compiler" is fairly literal.** Kompl's most distinctive memory feature is not retrieval; it is the write-time compilation of imported sources into wiki pages so later reads are cheaper and more structured.

**The queue state is part of the memory system.** `compile_progress` and `page_plans` are not just UI bookkeeping. They decide which sources can retry, which drafts survive, which pages can be approved, and whether a new compile session is allowed to start.

**Contradictions are surfaced, not resolved.** Match triage can log contradiction events against a page, but the code does not automatically rewrite or invalidate the page's content on that basis.

**Vector search is adjunct, not canonical.** Vector upsert can fail without failing commit; failed pages are queued for backfill, while SQLite/FTS/provenance still carry the canonical wiki state.

## What to Watch

- Whether the pending chat-draft path gains source-span provenance or review metadata before approval; without it, query-generated pages are less auditable than source-derived pages.
- Whether contradiction events become a first-class stale/superseded page mechanism rather than an activity-log sidebar signal.
- Whether the vector store gains export/import parity with the SQLite and compressed-file backup path, or remains a rebuildable access structure.
- Whether orphan queued-session cleanup grows into a broader single-writer run ledger for all long-running maintenance jobs.
- Whether auto-approval defaults change; that would materially shift generated page authority from reviewed candidate to immediate wiki mutation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Kompl has explicit MCP/API pull surfaces plus chat-time page injection into synthesis.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Kompl's pages, plans, provenance, aliases, FTS rows, vector records, and progress queues carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: compiled pages and provenance primarily serve as evidence and reference.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: compile steps, page plans, settings, gates, indexes, and MCP schemas shape future behavior.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - qualifies narrowly: Kompl derives pending query-generated drafts from chat session turns, while its main wiki compiler is imported-source based.
