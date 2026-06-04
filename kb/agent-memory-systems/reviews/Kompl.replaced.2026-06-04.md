---
description: "Kompl review: source-to-wiki compiler with SQLite provenance, LLM extraction and drafting, vector/FTS read-back, MCP tools, and query-derived drafts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-03"
---

# Kompl

> Replaced 2026-06-04. See [Kompl](./Kompl.md) for the current review.

Kompl, from tuirk's `tuirk/Kompl` repository, is a local "knowledge compiler" that ingests links, files, bookmarks, and exports, extracts structured knowledge, and compiles it into a browsable, interlinked wiki. Its memory system is not a simple raw-document store: the inspected code implements a multi-step compile pipeline, SQLite provenance and planning tables, gzip-compressed page files, FTS and Chroma indexes, chat retrieval, query-generated drafts, weekly digest/lint traces, and an MCP server for agent read-back.

**Repository:** https://github.com/tuirk/Kompl

**Reviewed commit:** [ec1616fabc6ff2092215c2cfa9d44883b6dd16ae](https://github.com/tuirk/Kompl/commit/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae)

**Last checked:** 2026-06-03

## Core Ideas

**The canonical product is a compiled wiki, not the source archive.** Kompl keeps raw source markdown and source metadata, but the behavior-shaping memory exposed to humans and agents is the compiled page layer: `pages`, compressed page files, `provenance`, `aliases`, `page_links`, FTS rows, and vector embeddings. The README frames this as a wiki that compounds with every new source, and the commit route turns drafted page plans into durable page rows, page files, provenance edges, FTS entries, wikilink edges, and vector upserts ([README.md](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/README.md), [app/src/app/api/compile/commit/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/compile/commit/route.ts), [app/src/lib/db.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/lib/db.ts)).

**Compilation is staged and stateful.** The session orchestrator runs ingestion prelude steps, extraction, entity/concept resolution, wiki-aware match triage, page planning, LLM drafting, deterministic cross-reference injection, commit, and schema generation. n8n is deliberately just an async trigger; the Next.js app owns orchestration and progress state ([app/src/app/api/compile/run/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/compile/run/route.ts), [n8n/workflows/session-compile.json](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/n8n/workflows/session-compile.json)).

**Extraction separates raw NLP signals from LLM synthesis.** `/api/compile/extract` reads stored raw markdown, calls spaCy NER, chooses keyphrase methods, optionally computes TF-IDF overlap against the existing wiki, then sends those signals plus source text to the LLM extraction endpoint. The result is stored as `extractions.llm_output`, while entity and relationship mention indexes record corpus-wide counts used by later planning ([app/src/app/api/compile/extract/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/compile/extract/route.ts), [nlp-service/routers/extraction.py](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/nlp-service/routers/extraction.py), [nlp-service/services/llm_client.py](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/nlp-service/services/llm_client.py), [scripts/migrate.py](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/scripts/migrate.py)).

**Identity and promotion are corpus-wide.** Entity and concept resolution uses fuzzy matching, existing aliases, existing wiki page titles, embeddings, and LLM disambiguation for ambiguous pairs. Planning then checks wiki-wide `entity_mentions` and `relationship_mentions` counts, so a later source can promote something first seen in older sessions into an entity, concept, comparison, or overview page ([app/src/app/api/compile/resolve/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/compile/resolve/route.ts), [nlp-service/routers/resolution.py](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/nlp-service/routers/resolution.py), [app/src/app/api/compile/plan/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/compile/plan/route.ts)).

**Context efficiency is mostly pre-compute plus budgeted read-back.** The compile path spends tokens at ingest time to produce page summaries, typed pages, provenance, wikilinks, aliases, FTS rows, and vectors so later chat/MCP calls can read synthesized wiki pages rather than re-processing raw sources. Chat retrieval uses an index-first LLM selector while the page index is small; larger wikis switch to hybrid FTS plus vector search, merge scores with source-count and recency weights, and pass only up to ten pages to synthesis, with only the top five receiving larger content slices ([app/src/lib/retrieval.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/lib/retrieval.ts), [app/src/app/api/chat/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/chat/route.ts), [nlp-service/services/vector_store.py](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/nlp-service/services/vector_store.py)).

**Trust comes from provenance and staged gates, not formal semantic validation.** Raw sources are immutable once ingested; compiled pages carry source counts, provenance rows, content hashes, previous-content paths, page links, aliases, and activity events. The system also has thin-draft gates, manual approval mode, lint checks, contradiction scans, archived-source filtering, and export/backup paths. Those mechanisms make lineage inspectable, but the page prose is still LLM-authored synthesis and effective truthfulness depends on the source extraction and drafting quality ([nlp-service/services/file_store.py](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/nlp-service/services/file_store.py), [app/src/app/api/wiki/lint-pass/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/wiki/lint-pass/route.ts), [app/src/lib/approve-plan.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/lib/approve-plan.ts), [app/src/app/api/export/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/export/route.ts)).

## Artifact analysis

- **Storage substrate:** `sqlite` - Kompl's central retained behavior-shaping state spans SQLite tables plus page/source files and Chroma vectors, but SQLite is the coordinating substrate that records sources, pages, provenance, aliases, plans, activity, chat, draft, mention, link, and settings state.
- **Representational form:** `prose` `symbolic` `parametric` - The system combines prose Markdown wiki pages and drafts, symbolic SQLite rows/frontmatter/page links/aliases/settings, LLM output JSON, vector embeddings, and authored TypeScript/Python routing logic.
- **Lineage:** `authored` `imported` `trace-extracted` - Raw source records are imported from connectors and files, authored routes/settings define the integration and pipeline behavior, and chat/session/activity/lint traces can produce pending drafts or maintenance signals.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Compiled pages and sources act as knowledge; routes, tool schemas, status gates, approval paths, lint/archive checks, retrieval scores, and query-generated drafts shape instruction, enforcement, routing, validation, ranking, and learning paths.

**Raw source records and files.** Storage substrate: SQLite `sources` rows plus gzip-compressed raw markdown under `/data/raw`. Representational form: prose source text wrapped by symbolic metadata and content hashes. Lineage: imported from connectors such as URLs, files, Twitter/bookmarks, GitHub README fetches, YouTube transcripts, or text inputs, then stored as source material for compilation. Behavioral authority: knowledge artifacts as preserved evidence; system-definition inputs when source status, session id, title source, and compile status determine which pipeline steps can run.

**Extraction and mention indexes.** Storage substrate: SQLite `extractions`, `aliases`, `entity_mentions`, and `relationship_mentions`. Representational form: symbolic JSON records, mention rows, and alias mappings distilled from LLM and NLP outputs. Lineage: derived from raw source markdown, NER/keyphrase/TF-IDF signals, LLM extraction, resolver decisions, and later canonicalization. Behavioral authority: system-definition artifacts for planning because mention counts, aliases, relationship counts, and existing page titles decide whether a future compile creates, updates, skips, or links pages; they are knowledge artifacts when inspected as explanation.

**Page plans and drafts.** Storage substrate: SQLite `page_plans` and `drafts`/pending plan rows. Representational form: mixed symbolic plan fields plus prose Markdown drafts. Lineage: derived from session sources, canonical entities/concepts, existing-page match triage, relationship thresholds, category rules, and chat-derived question/answer records. Behavioral authority: system-definition artifacts while pending because the commit/approve paths consume `draft_status`, `action`, `source_ids`, and `existing_page_id`; knowledge artifacts when reviewed by a human before approval.

**Compiled wiki pages.** Storage substrate: SQLite `pages` plus gzip-compressed Markdown files under `/data/pages`, with version-preserved previous files. Representational form: mixed prose Markdown, YAML frontmatter, source-count metadata, and linkable page ids. Lineage: derived from source content, extraction dossiers, related pages, existing page content, schema text, LLM drafting, deterministic wikilink injection, and commit-time hashing. Behavioral authority: knowledge artifacts for browsing and MCP responses; system-definition artifacts when inserted into chat synthesis prompts, used as cross-session identity anchors, or exported into Obsidian/Markdown surfaces that later tools consume.

**Provenance, links, FTS, and vector indexes.** Storage substrate: SQLite `provenance`, `page_links`, `pages_fts`, `vector_backfill_queue`, and Chroma at `/data/vectors`. Representational form: symbolic edges and sparse/dense retrieval indexes. Lineage: derived from committed pages and source relationships; vector rows are regenerated from page content and metadata, and backfill queues recover failed upserts. Behavioral authority: routing and ranking influence for search, graph navigation, chat retrieval, MCP result ordering, and archive filtering.

**Chat, digest, lint, and activity records.** Storage substrate: SQLite `chat_messages`, `activity_log`, `compile_progress`, settings rows, and generated draft rows. Representational form: mixed conversation prose, citations, page ids, JSON details, counters, and LLM digest summaries. Lineage: trace-extracted from user questions, assistant answers, pages used, compile events, lint runs, and weekly activity windows. Behavioral authority: knowledge artifacts as audit and history; system-definition candidates when chat creates pending `query-generated` drafts, lint activity flags maintenance, or digest summaries direct human attention.

**MCP server and HTTP routes.** Storage substrate: authored code. Representational form: symbolic tool schemas and route implementations with prose descriptions. Lineage: authored integration layer. Behavioral authority: system-definition artifacts because `search_wiki`, `read_page`, `list_pages`, and `wiki_stats` define how external agents can pull compiled memory, while `/api/chat` defines the built-in agent read-back path ([mcp-server/index.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/mcp-server/index.ts), [app/src/app/api/chat/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/chat/route.ts)).

The promotion path is source -> extraction/mentions -> page plan -> draft -> compiled page -> retrieval index -> chat/MCP read-back, with a smaller trace-derived branch from chat answer -> pending query-generated draft -> human approval -> compiled page. Kompl has good mechanical lineage through rows, hashes, provenance, and page versions; it does not have Commonplace-style typed review gates for deciding whether a synthesized claim deserves durable authority.

## Comparison with Our System

| Dimension | Kompl | Commonplace |
|---|---|---|
| Primary purpose | Compile personal sources into a local wiki and chat/MCP surface | Maintain methodology knowledge for agents and maintainers |
| Canonical substrate | SQLite-coordinated wiki pages, compressed files, provenance, FTS, Chroma | Git-tracked typed Markdown collections, schemas, indexes, reports |
| Main retained unit | Compiled pages plus provenance, aliases, links, vectors, drafts | Typed notes, instructions, reviews, sources, ADRs, indexes |
| Context selection | Precompiled pages, LLM page selection, FTS/vector hybrid ranking, MCP tools | `rg`, authored indexes, links, collection contracts, skills, validation |
| Governance | Source provenance, status gates, manual approval mode, lint/digest activity, backups | Type specs, schemas, validation, semantic review, citation discipline, replacement workflow |

Kompl and Commonplace share the same broad bet that durable agent memory should become inspectable artifacts before it is used. Kompl is more aggressive about compilation: it spends LLM calls during ingestion to turn raw sources into entity, concept, comparison, overview, and source-summary pages, then lets future agents query that distilled surface. Commonplace is more conservative: it keeps authored notes and reviews as the durable layer and uses validation/review to manage authority instead of auto-compiling a broad wiki from arbitrary inputs.

The major divergence is the storage contract. Kompl uses SQLite as the coordination center and file storage as a content sidecar; Commonplace keeps repo files as the primary authoring surface and treats generated indexes or databases as derived support state. Kompl's choice is pragmatic for a local app with sessions, progress polling, chat, vectors, drafts, and backups, but it makes review depend on application routes rather than ordinary file diffs.

Kompl is stronger on end-user activation. Its compiled pages flow into browser search, graph views, chat answers, MCP tools, exports, backups, and weekly digests. Commonplace's activation is currently more agent-operated and explicit: agents search, read, follow links, and invoke skills. Kompl's activation is more convenient, but its LLM-generated page prose needs stronger semantic QA before Commonplace should borrow the same automatic authority level.

**Read-back:** `both` - External MCP agents pull wiki pages through tools, while the built-in chat agent receives instance-targeted retrieved pages selected from the compiled wiki before synthesis; static pages are not enough on their own, but `/api/chat` wires retained memory into the model call.

### Borrowable Ideas

**Use compiled dossiers as an optional read-back product.** Commonplace could generate temporary, source-cited context dossiers from existing notes for a specific task, with FTS/vector/lexical ranking and explicit "why loaded" metadata. Ready only as a scoped command, not as a replacement for authored notes.

**Keep provenance rows close to compiled artifacts.** Kompl makes every page/source relationship queryable. Commonplace already has citations and source snapshots; a generated provenance table for derived reports or context packs would make downstream QA cheaper. Ready for generated artifacts that cite multiple sources.

**Make retrieval strategy switch by corpus size.** Kompl's index-first selector for small wikis and hybrid FTS/vector strategy for larger wikis is a useful pattern. Commonplace could borrow the policy boundary without adopting Chroma immediately: small collections can be offered whole index summaries, large ones need lexical candidates and budget caps.

**Borrow draft approval as an authority boundary for generated notes.** Kompl's `pending_approval` path is the right shape for query-generated pages. Commonplace should keep any generated note or synthesis in a workshop/review state until a human or review gate promotes it.

**Do not borrow automatic source-to-library compilation wholesale.** Kompl's product goal rewards broad synthesis from arbitrary sources. Commonplace's library needs narrower claims, known types, and reviewable mechanisms. The useful import is the staged pipeline, not automatic durable authority for every generated page.

## Write-side placement

**Write agency:** `manual` `automatic` - users can ingest sources, approve or reject drafts, and use manual approval mode, while the compile pipeline automatically extracts, resolves, plans, drafts, commits, indexes, creates query-generated draft candidates, and emits maintenance signals

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `promote` - the review describes summary/page compilation, fuzzy identity and alias resolution, existing-page update planning, LLM-generated entity/concept/comparison/overview/query drafts, and corpus-wide promotion of recurring entities or questions into pending or committed pages

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` - Kompl's trace-derived loop uses chat/session records plus compile progress, activity, lint, and digest events rather than agent tool trajectories.

**Learning scope:** `cross-task` - Approved query-generated drafts enter the local wiki and can be retrieved by later chat or MCP sessions beyond the originating question.

**Learning timing:** `online` `staged` - Chat traces can create pending drafts immediately after an answer, while approval and commit are staged before durable page-level authority.

**Distilled form:** `prose` `symbolic` `parametric` - Trace-derived candidates are prose drafts with symbolic page metadata/citations/page references, and approval adds FTS/vector retrieval indexes.

**Trace source.** Kompl qualifies for trace-derived placement, but the qualifying loop is secondary. Its primary learning loop is source-derived compilation from imported documents and URLs. The trace-derived loop comes from chat/session and operational traces: user questions, assistant answers, pages used, compile progress, activity events, lint results, and weekly activity windows. `/api/chat` stores user and assistant messages, citations, and `pages_used`; when a chat answer used three or more pages, it creates a pending `query-generated` draft from the question, answer, and cited pages ([app/src/app/api/chat/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/chat/route.ts)).

**Extraction.** The chat-derived extraction is simple: the already-produced grounded answer becomes a draft page candidate with `page_type: query-generated`, `draft_status: pending_approval`, and `pages_referenced`. Approval then uses the same commit path as other drafts, adding page rows, page files, provenance where available, FTS, wikilinks, and vector upserts. The weekly digest path summarizes recent activity into a Telegram message, and lint logs maintenance findings; those are trace summaries, but they are mainly human-facing governance artifacts unless a later workflow turns them into wiki changes ([app/src/lib/approve-plan.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/lib/approve-plan.ts), [app/src/app/api/digest/generate/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/digest/generate/route.ts), [app/src/app/api/wiki/lint-pass/route.ts](https://github.com/tuirk/Kompl/blob/ec1616fabc6ff2092215c2cfa9d44883b6dd16ae/app/src/app/api/wiki/lint-pass/route.ts)).

**Scope and timing.** Scope is local-instance and session-scoped. Chat traces are online and can create drafts immediately after an answer; approval is staged and user-mediated. Digest and lint traces are scheduled or manually triggered, and mostly affect human maintenance attention rather than immediate agent behavior.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Kompl belongs in a weak trace-to-readable-candidate family. It strengthens the distinction between source-derived compilation and trace-derived learning: most durable wiki memory comes from user-supplied sources, while traces produce pending drafts, summaries, and maintenance signals. The system therefore should not be counted as a full agent self-improvement loop in the same way as systems that mine action traces into rules, skills, or validators.

## Read-back placement

**Direction.** Kompl has both pull and push read-back over retained memory. External agents pull through MCP tools: `search_wiki`, `read_page`, `list_pages`, and `wiki_stats`. The browser UI and HTTP routes also expose pull surfaces for index, graph, page data, and search. The built-in chat route performs push from the synthesizing model's perspective: it retrieves retained wiki pages from the current question and sends selected page content into `/chat/synthesize` before the answer is generated.

**Read-back signal:** `inferred / lexical` `inferred / embedding` `inferred / judgment` - Chat push selects retained pages by LLM judgment over a small page index or by hybrid FTS/vector relevance for larger wikis.

**Faithfulness tested:** `no` - The review found exposure records and citations, but no ablation or perturbation test proving loaded pages changed model behavior.

**Targeting and signal.** The chat push is instance-targeted and inferred. Small wikis use LLM judgment over the page index to choose page ids; larger wikis use FTS lexical retrieval plus vector similarity, then merge scores with source count and recency. MCP pull starts from the agent's explicit query or page id, so it is pull even when `search_wiki` performs relevance ranking. `read_page` is identifier-based pull over a known `page_id`.

**Injection point.** Chat retrieval happens before the model answers, so selected pages can shape the next response. Query-generated drafts happen after the answer and only influence future behavior after approval or later retrieval. Lint and digest traces also happen after activity; they can guide maintenance but do not directly change the answer that produced the trace.

**Selection, scope, and complexity.** Read-back is local-wiki scoped. The built-in chat path retrieves at most ten pages, sends fuller content for the top five, and truncates page bodies. For small wikis the full index is the selection surface; for large wikis the hybrid retriever avoids sending the full index and raw corpus. MCP tools return summaries or full pages on demand, so complexity is controlled by the calling agent's pull sequence rather than automatic breadth.

**Authority at consumption.** Retrieved pages are advisory context for chat synthesis and MCP agents. The MCP server's tool descriptions and HTTP route schemas have routing authority, while the page contents themselves remain knowledge artifacts unless a host agent treats them as instructions. Query-generated drafts remain candidates until approval gives them page-level authority.

**Faithfulness.** I did not find a read-back ablation or perturbation test proving that loaded pages changed model behavior. The code records chat messages, citations, pages used, and activity, which proves exposure and supports debugging; it does not prove effective use.

**Other consumers.** Human users consume the wiki UI, graph, sources, settings, saved links, drafts, lint findings, exports, and weekly digest. n8n consumes scheduling/webhook surfaces. The backup/import paths consume the same memory as a portable application state bundle.

## Curiosity Pass

**Kompl looks like a wiki compiler more than an agent memory framework.** The retained artifacts are useful to agents through MCP and chat, but the deepest design work is ingestion, synthesis, provenance, and local-app operations.

**The strongest memory is precomputed synthesis, not retrieval.** Vector search helps find pages, but the expensive memory formation happened earlier when sources were extracted, resolved, planned, drafted, cross-linked, and committed.

**The SQLite/file split is practical but subtle.** Page content is in compressed files, but the behavioral control plane is mostly SQLite. That differs from file-first KB designs where a future agent can audit the whole memory layer with plain text tools.

**Trace-derived learning is present but easy to overstate.** Chat-derived drafts are real durable candidates, but source-derived compilation is the main compounding mechanism. Calling all source ingestion "trace-derived" would blur the review vocabulary.

**Manual approval is the most important safety boundary.** Kompl can auto-approve compile drafts, but the code also supports `pending_approval` paths. For a system that writes durable synthesized pages, that gate matters more than the retrieval stack.

## What to Watch

- Whether query-generated chat drafts become common enough to need stronger provenance and review UI; that would move Kompl closer to trace-derived learning rather than source-derived compilation.
- Whether lint findings and weekly digests become actionable edit proposals with diffs, rollback, and approval. That would strengthen governance but also raise authority risks.
- Whether vector search remains a derived index with recoverable backfill, rather than becoming the only practical navigation layer for large wikis.
- Whether entity/concept promotion thresholds and relationship thresholds stay stable under heterogeneous personal corpora. Bad thresholds would either over-produce low-value pages or hide useful cross-source patterns.
- Whether Kompl adds behavioral faithfulness checks for chat read-back, such as WITH/WITHOUT page retrieval tests or citation-use audits.

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - contrasts: Kompl uses SQLite as the control plane and compressed files as page/source content storage.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: Kompl precomputes page summaries, aliases, links, FTS, and vectors to reduce future context load.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - addresses: Kompl wires compiled pages into chat retrieval and MCP tools rather than only storing them.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - partially applies: query-generated drafts turn chat traces into pending durable wiki pages.
- [Preserve evidence without making history the next context](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: raw sources, provenance, activity, and chat logs are retained without automatically loading all history.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Kompl's raw sources, extractions, page plans, compiled pages, indexes, and traces need separate substrate/form/lineage/authority treatment.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: routes, schemas, planning rules, indexes, and approval paths shape future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: compiled pages, raw sources, provenance, and chat records are primarily evidence/context unless consumed with stronger authority.
