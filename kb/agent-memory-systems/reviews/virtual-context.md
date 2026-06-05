---
description: "Virtual Context review: proxy-owned context virtualization with trace-derived compaction, facts, paging tools, and prompt-time memory injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-05"
---

# Virtual Context

Virtual Context, from `virtual-context/virtual-context`, is a Python context-virtualization layer for LLM conversations. It runs mainly as an HTTP proxy that sits between clients and upstream providers, stores normalized conversation traces, compacts old turns into summaries and facts, retrieves selected memory before the next model call, and can expose paging tools, CLI commands, MCP tools, a dashboard, and a TUI around the same engine.

**Repository:** https://github.com/virtual-context/virtual-context

**Reviewed commit:** [4acad1285455e61ad88db312dc909f1bbeeb2917](https://github.com/virtual-context/virtual-context/commit/4acad1285455e61ad88db312dc909f1bbeeb2917)

**Last checked:** 2026-06-05

## Core Ideas

**The proxy manages the live request, not just an external memory store.** The documented request pipeline detects Anthropic, OpenAI Chat, OpenAI Responses, or Gemini format, strips envelope metadata, waits for previous turn processing, ingests history, runs `on_message_inbound`, injects a `<virtual-context>` block, forwards upstream, then runs `on_turn_complete` in the background ([docs/architecture.md](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/docs/architecture.md), [docs/proxy.md](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/docs/proxy.md)). The implementation in `prepare_payload()` follows that shape and also handles media compression, payload filtering, tool/chain stubbing, context injection, tool injection, and bloat fallback ([virtual_context/proxy/server.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/proxy/server.py), [virtual_context/proxy/helpers.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/proxy/helpers.py)).

**Inbound read-back and post-turn learning are separated.** `VirtualContextEngine.on_message_inbound()` delegates to retrieval and assembly before an upstream provider call, while `on_turn_complete()` tags the completed turn and then compacts if thresholds require it ([virtual_context/engine.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/engine.py)). That split is architecturally important: retrieved memory can affect the current response, while tagging, compaction, fact extraction, tag summaries, embeddings, and supersession shape later responses.

**Context efficiency is the central mechanism.** Retrieval tags the inbound message, expands related tags, scores candidates through IDF tag overlap, BM25/FTS text matches, and embedding similarity, skips active recent tags when appropriate, and applies result/budget limits ([virtual_context/core/retriever.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/retriever.py), [virtual_context/core/retrieval_scoring.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/retrieval_scoring.py)). The assembler then allocates a bounded pool across tag sections and facts, trims conversation history, and can serve topics at summary, segment, or full-text depth ([virtual_context/core/assembler.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/assembler.py), [virtual_context/core/retrieval_assembler.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/retrieval_assembler.py)).

**Trace compaction creates layered memory.** The compactor summarizes semantic segments, preserves original tags while allowing refined and related tags to add vocabulary, extracts structured facts from raw conversation text, and retains full text/messages alongside the summary ([virtual_context/core/compactor.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/compactor.py)). The compaction pipeline stores segments, propagates tool-output links, replaces per-segment facts, checks supersession/fact links, marks canonical turns compacted, and builds tag-level rollups and embeddings ([virtual_context/core/compaction_pipeline.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/core/compaction_pipeline.py)).

**Raw evidence remains addressable after compression.** SQLite storage keeps canonical turns, request captures, tool outputs, turn/segment-to-tool-output joins, chain snapshots, and media metadata; the proxy can restore tool output, chain snapshots, or media references when the model calls restoration/search tools ([virtual_context/storage/sqlite.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/storage/sqlite.py), [virtual_context/proxy/handlers.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/proxy/handlers.py), [virtual_context/proxy/media.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/proxy/media.py)). This is stronger than silent truncation: the model sees stubs and has a path back to full material.

**Adoption surfaces are deliberately broad.** The package installs a `virtual-context` CLI, supports local proxy/daemon setup, exposes a Python engine, includes MCP tools for recall/compaction/topic expansion/quote search/fact query, ships a TUI, and serves a dashboard for requests, sessions, compaction, cost, and recall inspection ([pyproject.toml](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/pyproject.toml), [virtual_context/mcp/server.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/mcp/server.py), [docs/proxy.md](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/docs/proxy.md)).

## Artifact analysis

- **Storage substrate:** `sqlite` `rdbms` `files` `graph` `in-memory` `service-object` — The default durable store is SQLite; PostgreSQL exists for multi-worker deployments; filesystem segment storage exists as an alternate backend; Neo4j/FalkorDB can hold fact links; current working state also lives in in-memory indexes; the active proxy/engine instance is a service object controlling request mutation and background writes ([virtual_context/storage/sqlite.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/storage/sqlite.py), [virtual_context/storage/postgres.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/storage/postgres.py), [virtual_context/storage/filesystem.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/storage/filesystem.py), [virtual_context/storage/neo4j.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/storage/neo4j.py), [virtual_context/storage/falkordb.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/storage/falkordb.py)).
- **Representational form:** `prose` `symbolic` `parametric` — Segment summaries, tag summaries, fact `what` strings, context blocks, and tool descriptions are prose; schemas, canonical turns, tags, aliases, facts, fact links, compaction operations, payload format adapters, and tool definitions are symbolic; chunk/tag-summary embeddings and embedding tagger signals are parametric.
- **Lineage:** `authored` `imported` `trace-extracted` — Proxy/engine/tool/config code is authored; ChatGPT/Grok/Claude import adapters and MCP `compact_context()` accept imported message material; canonical turns, segments, facts, tag summaries, embeddings, request captures, tool outputs, chain snapshots, media outputs, aliases, and supersession state are derived from conversation/tool/request traces ([virtual_context/import_adapters](https://github.com/virtual-context/virtual-context/tree/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/import_adapters), [virtual_context/mcp/server.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/mcp/server.py)).
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Stored traces, summaries, facts, quotes, and restored tool outputs advise future responses; injected context/tool descriptions instruct the model; payload budgets, protected windows, command interception, bloat fallback, and compaction leases enforce operational constraints; tags, aliases, session identities, provider adapters, and MCP/CLI commands route access; schemas and guards validate writes; RRF scores, BM25/FTS, embeddings, facts, active-tag skipping, and tag summaries rank what gets served; post-turn tagging/compaction/fact extraction updates later memory.

**Canonical turns and request captures.** Storage substrate is database rows keyed by conversation/session identity. Representational form is symbolic rows containing normalized and raw user/assistant content, hashes, tags, fact signals, code refs, timestamps, batch ids, and compaction state, plus raw request capture JSON. Lineage is trace-extracted from client payloads, provider responses, imports, and dashboard replay. Behavioral authority is knowledge and learning input: these rows are the raw evidence used for compaction, store recovery, quote search, dashboards, and future derived artifacts.

**Segments and tag summaries.** Storage substrate is `segments`, `segment_tags`, `tag_summaries`, FTS tables, chunk embeddings, and tag-summary embeddings. Representational form is prose summaries/full text plus symbolic metadata and parametric vectors. Lineage is trace-extracted and LLM-derived from compacted canonical turns; tag summaries are derived rollups over segment summaries. Behavioral authority is knowledge, routing, ranking, and instruction when selected into `<virtual-context>`.

**Facts and fact links.** Storage substrate is `facts`, `fact_tags`, `fact_links`, and optional graph backends. Representational form is symbolic subject/verb/object/status/date/link records with prose `what` and link context. Lineage is LLM-extracted from raw conversation during compaction, then supersession/link-checked against existing facts ([virtual_context/types.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/types.py), [virtual_context/ingest/supersession.py](https://github.com/virtual-context/virtual-context/blob/4acad1285455e61ad88db312dc909f1bbeeb2917/virtual_context/ingest/supersession.py)). Behavioral authority is knowledge when queried; routing/ranking when facts are preselected for a request; weak enforcement where superseded facts are hidden from default fact queries.

**Proxy payload mutations, paging tools, and commands.** Storage substrate is package code plus runtime request bodies and engine state. Representational form is symbolic provider adapters, tool schemas, command regexes, request filters, and prompt-injection formats, plus prose tool descriptions. Lineage is authored system-definition code operating over trace-derived store contents. Behavioral authority is instruction, routing, enforcement, and ranking because these surfaces decide whether retained memory is injected, which raw turns are dropped or stubbed, and which paging tools the model can call.

Promotion path: raw conversation/tool traces can become compacted segment summaries, tag summaries, structured facts, fact links, embeddings, paging hints, and prompt-injected memory. The path strengthens operational availability, but not epistemic authority in the Commonplace sense: summaries and facts are generated and regression-tested structurally, not promoted through source-cited semantic review.

## Comparison with Our System

| Dimension | Virtual Context | Commonplace |
|---|---|---|
| Primary purpose | Runtime context-window management for long LLM sessions | Git-native methodology KB for agent-operated knowledge bases |
| Canonical substrate | Service-owned store plus proxy/engine state | Typed Markdown artifacts, schemas, indexes, reviews, and source snapshots |
| Main read path | Prompt-time injection plus paging tools, CLI, MCP, dashboard | Agent pull through `rg`, indexes, links, skills, and explicit file reads |
| Write path | Automatic trace capture, tagging, compaction, facts, summaries, aliases, tool/media stubs | Authored notes/reviews/snapshots plus validation and review workflows |
| Governance | Schemas, compaction fences, tests, dashboards, bloat fallback, command guards | Collection contracts, type specs, deterministic validation, semantic review, citations, git history |

Virtual Context is a strong counterexample to treating "memory" as only a vector store or only a note repository. It manages the provider request path itself: it can remove old raw bulk, inject selected summaries/facts, expose paging tools, and leave restore references for hidden evidence. Commonplace deliberately avoids owning the runtime LLM call; it makes durable knowledge easier to inspect, cite, validate, connect, archive, and revise.

The trust tradeoff is the main divergence. Virtual Context is better at live continuity and token control, but its central retained artifacts are generated summaries, generated facts, embeddings, and database rows. Commonplace is slower and more manual, but a durable claim can be read as prose, checked against citations, reviewed, and versioned in git before it becomes high-authority context.

### Borrowable Ideas

**Treat prompt context as a budgeted working set.** Ready as a design lens. Commonplace already has progressive loading through titles, descriptions, indexes, source snapshots, and full files; Virtual Context's summary/segment/full depth vocabulary is a useful way to make those levels explicit for agent-facing commands.

**Use visible restore handles for compressed tool output.** Ready for runtime agents. Replacing bulky tool traces with explicit stubs plus a restore/search tool preserves lineage better than silent truncation.

**Keep trace-derived artifacts in separate raw, compacted, and promoted layers.** Ready as a rule for Commonplace workshop workflows. Raw transcripts, distilled notes, and instruction-bearing artifacts should not share the same authority just because they came from the same session.

**Borrow request-path ownership only for systems that actually need it.** Needs a concrete use case. A Commonplace daemon that rewrites every model call would add a lot of operational complexity; it makes sense only if agents need live prompt budgeting, tool-output restoration, or cross-client continuity.

**Do not borrow opaque summary authority.** Ready as a constraint. Generated summaries and facts can be excellent candidates, but Commonplace should keep citations, review state, and explicit promotion boundaries before they shape durable methodology.

## Write side

**Write agency:** `manual` `automatic` — Manual writes include CLI commands, MCP compaction tools, user-facing VC commands such as label/recall/compact/forget/attach, imports, and direct configuration. Automatic writes include request capture, canonical turn ingestion, per-turn tagging, tag aliases/splitting, compaction, segment/fact/tag-summary persistence, embeddings, fact supersession/linking, tool-output/chain/media storage, telemetry, dashboard records, and state checkpoints.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `promote` — Compaction consolidates raw turns into segment summaries and tag rollups; exact duplicate facts can be marked superseded; existing fact/status fields and tag aliases can evolve; tag summaries and linked facts synthesize cross-turn/topic structure not present as one raw turn; supersession invalidates older facts without deleting the historical trace; planned facts can be promoted to completed and retrieved topics can be promoted in the working set.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Virtual Context consumes client message history, user/assistant turns, provider request/response streams, tool calls/results, media blocks, imported conversation exports, dashboard replay prompts, command events, and session/alias identity events.

**Learning scope:** `per-project` `cross-task` — The default scope is a configured conversation/store, but labels, aliases, `VCATTACH`, shared stores, and multi-client proxy use can make memories available across sessions, clients, and tasks.

**Learning timing:** `online` `staged` — Inbound tagging/retrieval and request capture happen online before a model call; response tagging and compaction run after the turn; manual compaction, backfill, import, and dashboard replay are staged operations.

**Distilled form:** `prose` `symbolic` `parametric` — Traces become prose summaries and prompt blocks, symbolic canonical turns/facts/fact links/tags/aliases/tool refs, and parametric chunk/tag-summary embeddings.

Extraction is staged rather than a single learner. The inbound path tags the current user message and retrieves already-stored memory. The completion path persists the completed turn, derives tags and fact signals, and triggers compaction when thresholds or manual commands require it. The compactor then writes segment summaries, facts, tag summaries, embeddings, supersession/link state, and compaction watermarks.

The survey placement is the trace-to-working-memory branch with engineered read-back. Virtual Context strengthens the survey's raw-versus-distilled distinction: canonical turns, request captures, chain snapshots, tool outputs, and media files are mostly raw evidence; segment summaries, tag summaries, facts, embeddings, working-set depth, and injected context are the behavior-shaping outputs.

## Read-back

**Read-back:** `both` — Retained memory is pulled through CLI, MCP, user VC commands, dashboard/TUI views, and model paging tools; it is also pushed because the proxy can inject selected `<virtual-context>` sections, facts, hints, and paging/restoration tool definitions into a provider request before the receiving model asks for them.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — Coarse push comes from context hints and tool availability once the proxy chooses an active path; identifier signals include session/conversation ids, labels, aliases, tags, and explicit VC commands; lexical signals include BM25/FTS and command/query text; embedding signals include inbound tag matching, tag-summary embeddings, chunk embeddings, and fact semantic search.

**Faithfulness tested:** `no` — The repository has dense tests for request formatting, retrieval, compaction lifecycle, storage, paging tools, fact querying, command handling, and proxy behavior, and README benchmark claims report outcome improvements. I did not find code-level with/without read-back ablations or post-action audits proving that each pushed memory item was faithfully used by the model.

The main push injection point is pre-invocation: `prepare_payload()` obtains `assembled.prepend_text`, mutates the provider-specific request through `_inject_context()`, optionally injects VC tools, then forwards the enriched body. Tool restoration and continuation rounds can reassemble the request after a VC tool call, but that is still serving retained memory into the current model interaction, not a post-action read-back.

Selection is budgeted and multi-layered. Recent turns are protected, active tags may be skipped, compacted turns can be dropped or stubbed, old tool/media content can be replaced with restore references, and the assembler limits tag sections/facts under configured caps. Complexity is bounded by budgets and presenter format, but effective context dilution is not verifiable from static code.

Authority at consumption varies. Retrieved summaries, facts, quotes, and restored tool output are advisory knowledge; injected tool descriptions and hints are instruction-like; provider adapters, budget gates, command interception, and payload mutation are stronger system-definition authority. The receiving model's compliance with injected memory remains a runtime behavior question.

## Curiosity Pass

**The OS metaphor is unusually literal.** Protected recent turns, compacted pages, topic summaries, restore tools, working-set depth, and payload mutation make the virtual-memory analogy more than marketing.

**The system is strongest where it owns the pipe.** The proxy can remove and replace old prompt material, while pure MCP/CLI use mostly provides pull retrieval and manual compaction.

**Service-owned state buys scale and costs inspectability.** SQL schemas, dashboards, and tests make the store inspectable, but a generated fact is still not as reviewable as a cited Markdown claim.

**Fact supersession is useful but epistemically narrow.** Supersession hides stale facts from default queries and can link relationships, but it does not prove that the new fact is true, complete, or instruction-worthy.

**Benchmarks test end-to-end memory usefulness, not per-artifact truth.** The LongMemEval-style results are relevant adoption evidence, but they should not be read as validation for every generated summary or fact.

## What to Watch

- Whether read-back gets explicit faithfulness tests or ablations around injected summaries, facts, and restore tools; that would make the push path easier to compare with reviewed instruction artifacts.
- Whether generated facts and summaries gain source quote/proof fields; that would narrow the governance gap with citation-bearing KB notes.
- Whether `VCMERGE` moves from guarded refusal/placeholder paths into implemented cloud-side merge; that will matter for cross-session lineage and alias authority.
- Whether graph backends become primary rather than optional fact-link stores; that would shift the artifact analysis toward graph-native memory.
- Whether cache-aware deferred payload mutation remains compatible with accurate retrieval after client truncation; that is the main operational risk in owning the request path.

## Relevant Notes

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Virtual Context implements both durable storage and proxy-mediated read-back, including prompt-time push.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Virtual Context derives summaries, facts, tags, embeddings, and restore handles from conversation and tool traces.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Virtual Context belongs in the trace-to-working-memory family with engineered read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw traces, summaries, facts, embeddings, tools, and proxy rules carry different storage, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: stored turns, summaries, facts, quotes, and restored tool outputs advise later reasoning when consumed.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: proxy mutation, provider adapters, tool schemas, compaction fences, retrieval scoring, and command handlers shape behavior with stronger force.
