---
description: "Atomic review: SQLite-backed markdown atoms with embeddings, semantic graph, wiki/report synthesis, chat, and MCP memory tools"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# Atomic

Atomic, from `kenforthewin/atomic`, is a personal knowledge-base app that stores markdown "atoms" in database-backed collections, derives chunks, embeddings, tags, semantic edges, wiki articles, report findings, and chat records from them, and exposes that store through desktop, web, mobile, REST, WebSocket, and MCP surfaces. It is closer to a full local/private PKB application than to a small agent-memory plugin: agents can search, read, create, ingest, and edit atoms, while the app also runs background feed polling, graph maintenance, wiki synthesis, and scheduled research reports.

**Repository:** https://github.com/kenforthewin/atomic

**Reviewed commit:** [dd9a43a29e2afeb815f15f65a9c09bfc01873049](https://github.com/kenforthewin/atomic/commit/dd9a43a29e2afeb815f15f65a9c09bfc01873049)

**Last checked:** 2026-06-04

## Core Ideas

**Atoms are markdown records with database-managed derived state.** The core `Atom` stores content, title/snippet metadata, source URL, timestamps, status columns for embedding/tagging, and a kind discriminator for captured versus report-generated atoms. Data databases hold atoms, tags, atom chunks, vector rows, FTS tables, semantic edges, positions, wiki articles, conversations, report definitions, findings, citations, task runs, and queue rows; a separate registry database holds workspace settings, tokens, OAuth state, and database metadata ([crates/atomic-core/src/models.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/models.rs), [crates/atomic-core/src/db.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/db.rs), [crates/atomic-core/src/registry.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/registry.rs)).

**The write pipeline separates capture from enrichment.** `create_atom`, bulk create, and update write the atom first, enqueue pipeline work, and then process embedding and tagging jobs. The pipeline chunks markdown, batches embedding provider calls, stores chunk embeddings, rebuilds FTS, runs LLM tag extraction when enabled, and marks graph maintenance dirty instead of recomputing all graph state inline ([crates/atomic-core/src/lib.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/lib.rs), [crates/atomic-core/src/embedding.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/embedding.rs), [docs/reference/embedding-tagging-pipeline.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/docs/reference/embedding-tagging-pipeline.md)).

**The semantic graph is derived maintenance, not the canonical note store.** Embedding completion sets `edges_status = pending` and task settings such as `task.graph_maintenance.last_dirty_at`; `GraphMaintenanceTask` later claims pending atoms, recomputes semantic edges, recomputes tag centroids, rebuilds FTS, and invalidates the canvas cache after the pipeline drains or staleness exceeds the configured window ([crates/atomic-core/src/graph_maintenance.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/graph_maintenance.rs)).

**Context efficiency comes from chunk search, limits, and pagination, with some coarse preloading.** Normal search returns deduplicated atoms from chunk-level keyword, semantic, or hybrid RRF search with limits and tag/time filters. Chat and MCP reads page long atoms by line limit/offset. Wiki generation and reports use explicit source budgets, iteration caps, and selected-chunk trimming; report runs can still push a preselected source batch into the agent prompt, so complexity is bounded by report configuration rather than by agent-side retrieval alone ([crates/atomic-core/src/search.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/search.rs), [crates/atomic-core/src/agent.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/agent.rs), [crates/atomic-core/src/wiki/agentic.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/wiki/agentic.rs), [crates/atomic-core/src/reports/agentic.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/reports/agentic.rs)).

**MCP exposes Atomic as long-term memory for external agents.** The MCP server advertises `semantic_search`, `read_atom`, `create_atom`, `ingest_url`, `update_atom`, and `edit_atom`; server instructions tell clients to search before answering from memory, remember durable context, and update stale atoms. The desktop bridge is a stdio-to-HTTP adapter, while remote clients connect to `/mcp` with a bearer token and optional database selector ([crates/atomic-server/src/mcp/server.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-server/src/mcp/server.rs), [crates/atomic-server/src/mcp/types.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-server/src/mcp/types.rs), [docs/manual/guides/mcp-server.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/docs/manual/guides/mcp-server.md)).

**Trust is uneven across artifact classes.** Atoms are editable markdown with source URLs and timestamps, wiki/report outputs carry citations to source atoms, and API tokens/ledger rows govern some operations. But auto-tags, semantic edges, tag centroids, and chat/retrieval effects are not independently validated for truth or behavioral faithfulness; they are useful ranking and synthesis machinery, not reviewed knowledge claims.

## Artifact analysis

- **Storage substrate:** `sqlite` — The default durable substrate is SQLite data databases plus a registry database, with sqlite-vec and FTS virtual tables for retrieval; an optional Postgres backend exists for shared infrastructure, but the reviewed default app architecture is SQLite-first.
- **Representational form:** `prose` `symbolic` `parametric` — Atoms, wiki articles, report findings, chat messages, and prompts are prose; tables, rows, schemas, queues, API routes, MCP tool definitions, task ledgers, and edit operations are symbolic; embeddings, vector indexes, tag centroids, semantic similarity, and provider/model outputs are parametric or parametric-derived.
- **Lineage:** `authored` `imported` — Users and agents author atoms, tags, reports, conversations, wiki proposals, and settings; URL/RSS/browser/Obsidian imports create atoms from external sources; derived chunks, embeddings, tags, edges, wiki articles, report findings, citations, FTS rows, and centroids are regenerated from those authored/imported atoms and configured models.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Atoms and synthesized articles advise agents as knowledge artifacts; MCP/server/chat/report prompts and tool schemas instruct agents; tags, scopes, database selectors, report filters, and graph/canvas views route retrieval; edit guards, stale wiki proposal checks, citation extraction, token limits, leases, and API auth validate operations; search, embeddings, edges, centroids, and RRF rank context; scheduled reports, wiki synthesis, auto-tagging, graph maintenance, and tag compaction learn derived state from the corpus.

**Atoms and tags.** The storage substrate is a data database. The representational form is markdown prose plus symbolic metadata: IDs, timestamps, source URLs, kind, status columns, tag hierarchy, atom-tag links, and source fields. Lineage is authored through the app/MCP/chat tools or imported from URLs, RSS, browser capture, or Obsidian. Behavioral authority is knowledge artifact authority until an atom is read into chat, MCP, report, wiki, or UI context; tags additionally route filtering and scoping.

**Chunks, embeddings, FTS, semantic edges, and tag centroids.** The storage substrate is `atom_chunks`, `vec_chunks`, `atom_chunks_fts`, `semantic_edges`, and `vec_tags`/tag-embedding tables. The representational form is symbolic chunk/index rows plus parametric embeddings and centroid vectors. Lineage is derived from atom content and current provider settings; model/dimension changes, atom edits, and pipeline retries invalidate or rebuild them. Behavioral authority is ranking and routing for search, wiki research, reports, canvas layout, and related-tag discovery, not direct prose instruction.

**Wiki articles and proposals.** The storage substrate is wiki tables, citations, links, versions, and proposals. The representational form is synthesized prose with symbolic citation/link/version metadata. Lineage is derived from captured atom chunks under a tag hierarchy, selected by search or an agentic research loop. Behavioral authority is knowledge and light instruction: articles become readable summaries and cross-linked context, while proposal accept/dismiss state gives humans a promotion gate before updates become live.

**Report definitions and findings.** The storage substrate is `reports`, `report_findings`, `report_finding_citations`, task-run ledger rows, and output atoms with kind `report`. The representational form is symbolic schedule/scope/citation policy plus synthesized prose findings. Lineage is authored report configuration plus source atoms selected by scope and optional semantic-search context; scheduled or manual runs write new finding atoms transactionally with citations. Behavioral authority is learning and knowledge: reports can periodically produce durable findings that later retrieval may include or exclude by atom kind.

**Chat and MCP surfaces.** The storage substrate includes conversations, messages, tool calls, citations, API tokens, OAuth state, and the MCP bridge/server code. The representational form is symbolic tool schemas and route handlers plus prose instructions and message histories. Lineage is authored system code, user/agent chat turns, and tool outputs. Behavioral authority is instruction and routing: these surfaces define how an external or in-app agent may pull memory, mutate atoms, and cite results.

**Promotion path.** Atomic promotes authored/imported atoms into derived chunks, embeddings, tags, graph edges, centroids, summaries, wiki articles, report findings, and MCP/chat-visible memory. The strongest reviewable promotion is wiki proposal -> accepted wiki article and report source atoms -> cited finding atom. The weaker promotions are auto-tags and semantic graph state: they affect retrieval and layout but have no source-span review or faithfulness audit.

## Comparison with Our System

| Dimension | Atomic | Commonplace |
|---|---|---|
| Primary purpose | Personal PKB application with AI augmentation and agent memory tools | Typed methodology KB framework for agent-operated knowledge bases |
| Canonical substrate | SQLite data DBs plus registry DB; optional Postgres | Git-tracked markdown collections, type specs, generated indexes, sources, and reports |
| Main retained unit | Markdown atom with tags, source URL, chunks, embeddings, and derived graph state | Typed markdown artifact with frontmatter, collection contract, links, validation, and review history |
| Retrieval | Hybrid chunk search, vector/FTS indexes, graph/canvas, chat/MCP tools | Lexical search, authored links/indexes, generated indexes, skills, and review reports |
| Automatic writes | Embeddings, tags, graph edges, centroids, wiki articles/proposals, report findings, feed ingestion | Mostly human/agent-authored repo artifacts plus deterministic validation/index generation |
| Governance | Auth tokens, leases, status columns, proposal staleness checks, citations, source URL dedup | Git diffs, type schemas, collection contracts, validation, semantic QA, source snapshots |

Atomic is stronger than Commonplace as an application shell around memory: it has a polished UI, mobile/desktop/server deployments, tokened APIs, chat, MCP, RSS, browser capture, vector search, and scheduled reports. Commonplace is stronger where the memory artifact itself must be audited: every durable library artifact is a file with type contracts, source citations, link semantics, validation, review gates, and git history.

The major design divergence is database-derived memory versus repo-native knowledge. Atomic treats markdown atoms as editable records inside a live app and lets derived indexes/summaries drive access. Commonplace treats the artifact surface and its validation machinery as the system; indexing is secondary to explicit type and link contracts.

### Borrowable Ideas

**A durable pipeline queue for enrichment.** Ready for a concrete Commonplace command. Atomic's coalescing queue, status columns, and lease model are a useful pattern for indexing, embedding, or review jobs that should survive restarts without blocking the authoring write.

**Separate source atoms from generated finding atoms.** Ready now as a design rule. Atomic's `kind` discriminator prevents report-generated findings from accidentally contaminating some source-selection paths. Commonplace could use a similarly explicit generated/source distinction for reports or synthesis outputs.

**Proposal before promotion for synthesized summaries.** Ready now. Wiki proposals show a useful shape for LLM synthesis: write a pending draft with citations and base-version metadata, then require accept/dismiss before it becomes the live summary.

**Expose narrow edit tools instead of whole-file rewrite.** Ready now for agent-facing commands. Atomic's MCP `edit_atom` requires exact replace/insert anchors and fails atomically if an edit is ambiguous, which maps well to safer Commonplace note mutation.

**Do not borrow opaque auto-tag authority without review.** Needs a stronger use case. Atomic's LLM tag extraction and tag compaction are useful for discovery, but Commonplace should keep collection routing and link semantics explicit until generated tags can be audited.

**Scheduled reports as durable findings.** Useful but needs policy. Commonplace could run recurring review/report tasks over scoped notes, but findings should land in a workshop or review queue before gaining library authority.

## Write side

**Write agency:** `manual` `automatic` — Users and agents manually create, edit, tag, ingest, and configure atoms/reports/wiki proposals through UI, REST, chat, and MCP tools; the system also automatically enriches and maintains the store through embedding/tagging queues, graph maintenance, feed polling, wiki synthesis/update proposals, tag compaction, scheduled report runs, and startup migrations.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `promote` — Wiki articles consolidate many tagged atoms into a summary; source URL checks and tag merges remove duplicates; wiki update/proposal paths evolve an existing article from newly selected chunks; wiki generation and scheduled reports synthesize new prose artifacts from existing atoms; accepted wiki proposals and report finding atoms promote derived drafts/findings into durable read surfaces. I did not find a general contradiction invalidation or age-based decay policy for atoms.

The automatic write path is corpus-derived rather than trace-derived. It consumes authored/imported atom content, feed items, URLs, search results, tag scopes, schedules, and model outputs. It does not implement durable learning from session logs, tool/action traces, repeated agent trajectories, or rollouts, so this review does not carry the `trace-derived` tag.

## Read-back

**Read-back:** `both` — Chat and MCP agents usually pull retained memory by calling search/read tools, while scheduled report runs push a scoped source atom batch into the report agent prompt before its tool loop begins.

**Read-back signal:** `identifier` `inferred / embedding` `inferred / lexical` — Push read-back for reports is identifier-scoped by report source tags, time windows, atom kinds, and source caps; pull retrieval uses hybrid lexical and embedding search through chat, MCP, wiki research, and report context search.

**Faithfulness tested:** `no` — Atomic stores citations, tool calls, search scores, and report/wiki provenance, but I did not find an ablation or post-action audit that tests whether a fired memory changed an agent's behavior.

**Direction edge cases.** MCP instructions tell external agents to search before answering and remember durable context, but that instruction is baseline tool guidance, not memory push. The MCP `semantic_search` and `read_atom` tools are pull. The in-app chat agent similarly receives tool definitions and compact UI/canvas context, then chooses whether to call `search_atoms` or `get_atom`. Scheduled reports are the clear push case because `build_user_prompt` places source atoms directly in the report agent's prompt before it can act.

**Targeting and signal.** Report push is instance-targeted by authored report configuration: source tag IDs, source time window, kind filters, max source atoms, and max source tokens. Search-based read-back is inferred relevance: semantic/vector search keys on embeddings, keyword search keys on lexical terms, and hybrid search merges both with RRF. Tag filters and database selectors are identifier constraints around those searches.

**Injection point.** For chat/MCP, retained memory enters only when the agent invokes a tool and receives the result before a later model step or final answer. For scheduled reports, source atoms are inserted into the initial user prompt for the report run. Wiki generation and report context search also assemble memory before synthesis/final pass; after-run writes such as citation persistence, report finding creation, queue clearing, graph maintenance, and broadcasts are write-side maintenance.

**Selection, scope, and complexity.** Search limits, thresholds, recency filters, tag scopes, kind filters, line pagination, report source caps, report max tool iterations, wiki max source tokens, and selected-chunk trimming all constrain context volume. Complexity can still be high: a report source batch or wiki article can mix many atoms, tags, citations, and synthesized summaries. Effective context dilution is not verified from code.

**Authority at consumption.** Retrieved atoms and wiki/report outputs are advisory knowledge unless the specific prompt turns them into instructions. MCP create/update/edit tools give external agents direct write authority, but reads themselves are not hard gates. Report and wiki agents have stronger synthesis authority because their outputs become durable artifacts if saved or accepted.

**Other consumers.** Human users consume atoms, wiki pages, canvas clusters, report findings, chat histories, citations, and logs through the UI. Background schedulers consume reports, feed definitions, pipeline queue rows, dirty graph state, and task ledgers.

## Curiosity Pass

**Atomic is a memory app with agent surfaces, not only an agent memory backend.** The richest machinery is the PKB application: UI, registry, databases, feeds, wiki, reports, canvas, and provider configuration. MCP is one consumer surface over that system.

**The code distinguishes generated findings from captured atoms, but not all retrieval paths treat them the same.** MCP search defaults to captured-only, while in-app chat search includes all kinds by default. That is a meaningful policy split, not just an implementation detail.

**The strongest automatic learning is not from agent traces.** Auto-tags, embeddings, semantic edges, centroids, reports, and wiki articles change future behavior, but their source is the knowledge corpus and schedules, not the agent's own operational history.

**The semantic graph may overstate semantic reliability.** Edges and canvas forces are useful navigation affordances, but they are similarity artifacts. The reviewed code does not test whether an edge is a true conceptual relationship.

**Reports are the most Commonplace-like feature.** They run scoped investigations, use read/search tools, write cited findings, and keep provenance rows. Their weak point is authority: generated findings should not be treated like source atoms unless the retrieval path makes that policy explicit.

## What to Watch

- Whether the optional Postgres backend becomes fully equivalent for search, wiki, and chat paths; the reviewed code still notes places where SQLite-specific modules remain.
- Whether wiki proposals gain stronger source-span review, confidence, or diffable per-section provenance before promotion.
- Whether report findings get explicit review/approval states before entering general in-app retrieval.
- Whether auto-tagging and tag compaction add human approval, source snippets, or reversible histories for generated tag changes.
- Whether chat/MCP memory use gains faithfulness tests that compare responses/actions with and without retrieved atoms.
- Whether future dirty-chunk embedding and chunk-assisted tagging move from strategy hooks to implemented behavior.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Atomic stores a large memory substrate, but most agent read-back is still tool-pull, with scheduled reports as a push exception.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Atomic bundles atoms, vectors, indexes, wiki/report outputs, prompts, tools, and ledgers under different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: atoms, wiki articles, report findings, and chat citations mostly advise rather than enforce behavior.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - distinguishes: MCP tool schemas, report scopes, scheduler rules, edit guards, and routing filters define behavior rather than merely inform it.
- [Storage substrate](../../../notes/definitions/storage-substrate.md) - relates: Atomic's default durable memory is SQLite plus derived vector/FTS state, not files as source of truth.
