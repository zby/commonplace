---
description: "Atomic review: SQLite/Postgres Markdown atoms with embeddings, tags, wiki synthesis, agentic chat, MCP tools, scheduled reports, and canvas graph"
type: ../types/agent-memory-system-review.md
tags: [push-activation]
status: current
last-checked: "2026-06-01"
---

# Atomic

Atomic, from Ken Fortney's `kenforthewin/atomic` repository, is a personal knowledge base that stores Markdown notes as "atoms" and builds an AI-augmented semantic graph around them. It ships as a Rust `atomic-core` crate wrapped by a Tauri desktop app, an Actix HTTP/WebSocket/MCP server, a React frontend, a browser clipper, an Obsidian plugin, a Discord ingestion plugin, and benchmark tooling ([README.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/README.md), [AGENTS.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/AGENTS.md), [Cargo.toml](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/Cargo.toml), [package.json](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/package.json)).

**Repository:** https://github.com/kenforthewin/atomic

**Reviewed commit:** [dd9a43a29e2afeb815f15f65a9c09bfc01873049](https://github.com/kenforthewin/atomic/commit/dd9a43a29e2afeb815f15f65a9c09bfc01873049)

**Last checked:** 2026-06-01

## Core Ideas

**The atom is the source unit, but most behavior comes from derived views.** An atom is Markdown content plus source metadata, timestamps, embedding/tagging status, and a `kind` discriminator for captured versus report-produced atoms. Creation and update paths enqueue an asynchronous pipeline that chunks content, embeds chunks, auto-tags, and later refreshes graph maintenance ([crates/atomic-core/src/models.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/models.rs), [crates/atomic-core/src/lib.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/lib.rs), [docs/reference/embedding-tagging-pipeline.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/docs/reference/embedding-tagging-pipeline.md)). The user-facing memory is therefore not just the Markdown note; it is the note plus chunk vectors, tag hierarchy, semantic edges, wiki articles, search indexes, canvas projections, and report findings.

**Retrieval is hybrid and scope-aware.** Search supports keyword, semantic, and hybrid modes, with Reciprocal Rank Fusion for hybrid results, tag scopes, recency filters, and atom-kind filters ([crates/atomic-core/src/search.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/search.rs), [crates/atomic-core/src/lib.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/lib.rs)). This is the main context-cost control: agents and UIs usually see ranked atom snippets or paginated atom reads rather than the whole corpus.

**The chat agent is a tool-using RAG loop over the same store.** Chat conversations persist messages, tool calls, citations, and tag scopes; the agent receives tools for hybrid search, paginated atom reads, atom creation, atom editing, optional current-page context, and optional canvas actions ([crates/atomic-core/src/agent.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/agent.rs), [crates/atomic-core/src/chat.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/chat.rs), [docs/manual/concepts/chat.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/docs/manual/concepts/chat.md)). This gives agents read and write access, but ordinary chat retrieval remains pull: the model decides when to call `search_atoms` or `get_atom`.

**MCP exposes Atomic as external long-term memory.** The server provides MCP tools for `semantic_search`, `read_atom`, `create_atom`, `ingest_url`, `update_atom`, and `edit_atom`; the bridge adapts stdio MCP clients to the HTTP MCP endpoint ([crates/atomic-server/src/mcp/server.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-server/src/mcp/server.rs), [crates/mcp-bridge/src/main.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/mcp-bridge/src/main.rs)). The MCP surface is deliberately agent-shaped: search before recall, remember durable facts, and update stale atoms.

**Reports are scheduled memory activation, not just summaries.** A report has a research prompt, cron schedule, source scope, context scope, citation policy, and output tags. When due, the runner resolves a source batch, builds a context filter, gives the report agent numbered source atoms plus search/read/done tools, then writes one cited finding atom with provenance and citation rows ([docs/manual/concepts/reports.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/docs/manual/concepts/reports.md), [crates/atomic-core/src/reports/scope.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/reports/scope.rs), [crates/atomic-core/src/reports/agentic.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/reports/agentic.rs), [crates/atomic-core/src/reports/runner.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/reports/runner.rs)). This is the strongest activation mechanism because memory enters an agent context by schedule and scope, before the report agent chooses any search.

**Adoption is multi-surface.** The browser extension captures web pages into atoms with offline queueing, the Obsidian plugin syncs vault notes and adds search/similar/wiki/chat/canvas views, and the Discord plugin captures messages, threads, forums, and slash-command searches into Atomic ([extension/README.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/extension/README.md), [plugins/obsidian-plugin/README.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/plugins/obsidian-plugin/README.md), [plugins/discord/README.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/plugins/discord/README.md)). That makes the system closer to a personal memory platform than a single agent memory library.

## Artifact analysis

**Atoms and tags.** Storage substrate: per-database SQLite or Postgres tables for atoms, atom-tag joins, source metadata, status fields, and hierarchical tags; a registry database stores global settings and tokens for multi-database deployments ([crates/atomic-core/src/db.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/db.rs), [docs/manual/guides/multi-database.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/docs/manual/guides/multi-database.md)). Representational form: mixed prose Markdown plus symbolic metadata. Lineage: user-authored, imported, clipped, synced, or agent-written atom content; tag lineage may be user-authored or LLM-extracted. Behavioral authority: atoms and tags are knowledge artifacts when searched, read, synthesized, or displayed; tags also have routing and scoping authority for search, wiki, chat, reports, and auto-tagging.

**Chunk embeddings, semantic edges, tag centroids, and canvas projections.** Storage substrate: `atom_chunks`, sqlite-vec `vec_chunks` or Postgres vector columns, `semantic_edges`, `tag_embeddings`, cached canvas data, and atom positions. Representational form: distributed-parametric vectors plus symbolic edge/cache records. Lineage: derived from atom content, configured embedding model, tag assignments, and graph-maintenance runs; changing source content or model invalidates embeddings and downstream graph state. Behavioral authority: ranking and navigation influence. They decide which atoms are retrieved, visually clustered, or selected for wiki/report context, but they are not themselves user-facing claims.

**Wiki articles and proposals.** Storage substrate: `wiki_articles`, citations, links, article versions, and `wiki_proposals`. Representational form: generated prose with symbolic citations, links, and version/proposal records. Lineage: derived from tag-scoped atoms and chunk selection, with centroid or agentic strategies and optional human accept/dismiss flow ([crates/atomic-core/src/wiki/centroid.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/wiki/centroid.rs), [crates/atomic-core/src/wiki/agentic.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/wiki/agentic.rs), [crates/atomic-core/src/lib.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-core/src/lib.rs)). Behavioral authority: knowledge artifacts for users and agents; generated articles can influence later search, canvas, and wiki synthesis when included as atoms or linked articles, but the code keeps citations and versions as review aids rather than hard truth guarantees.

**Chat conversations, tool calls, and citations.** Storage substrate: conversation, message, tool-call, citation, and conversation-tag tables. Representational form: symbolic chat metadata plus prose messages and JSON tool payloads. Lineage: runtime interaction logs from user and assistant turns. Behavioral authority: mostly knowledge artifacts for resuming conversation and global keyword search; the chat loop does not mine conversation traces into reusable rules, retrievers, or future instructions at this commit.

**MCP and agent tool schemas.** Storage substrate: Rust server code and generated protocol responses, with MCP bridge configuration outside the data DB. Representational form: symbolic tool definitions plus prose descriptions. Lineage: authored API surface over the same `AtomicCore` operations. Behavioral authority: system-definition artifacts because they route, constrain, and authorize external agents to search, read, create, ingest, update, or edit retained memory.

**Report definitions, run ledgers, findings, and citations.** Storage substrate: reports, task runs, finding provenance, finding citation rows, and finding atoms with `kind = report`. Representational form: symbolic schedules/scopes/policies plus prose prompts and generated prose findings. Lineage: report definitions are authored; source batches are selected from existing atoms; findings are LLM-derived from numbered source atoms and optional context search. Behavioral authority: report definitions and schedulers are system-definition artifacts with activation, routing, and evaluation force; finding atoms are knowledge artifacts when read later, with provenance/citations preserving enough lineage for audit.

**Import and plugin sidecars.** Storage substrate: browser extension local queue, Obsidian plugin state, Discord bot SQLite dedup/config database, RSS feed tables, and source URLs on atoms. Representational form: symbolic state plus imported prose. Lineage: external web pages, vault files, Discord messages, feeds, and captured selections become atoms. Behavioral authority: ingestion and deduplication authority at the boundary; once imported, the material follows the atom pipeline rather than carrying special agent authority.

**Benchmark artifacts.** Storage substrate: `bench/` fixtures and `atomic-bench` run outputs. Representational form: JSON/JSONL datasets, metric records, and Rust harness code. Lineage: authored mini fixtures or LongMemEval cleaned datasets; run outputs derive from temporary Atomic databases and configured providers ([bench/README.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/bench/README.md), [crates/atomic-bench/src/suites/memory_longitudinal.rs](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/crates/atomic-bench/src/suites/memory_longitudinal.rs)). Behavioral authority: evaluation artifacts for maintainers, not runtime memory. They are useful because they measure retrieval over session-like data without turning those benchmark traces into production memory.

## Comparison with Our System

| Dimension | Atomic | Commonplace |
|---|---|---|
| Primary purpose | Personal knowledge base application and agent memory service | Methodology KB and framework for agent-operated knowledge bases |
| Main retained unit | Markdown atom in SQLite/Postgres with derived indexes | Typed Markdown artifact in Git with collection/type contracts |
| Derived context | Chunks, vectors, tags, semantic edges, wiki articles, reports, canvas cache | Directory indexes, connect reports, validation/review outputs, source snapshots |
| Agent surface | Chat tools, MCP tools, scheduled report agents, plugins | Local skills, `commonplace-*` commands, repo navigation, review workflows |
| Governance | Status columns, queue leases, citations, report ledger, wiki proposals, tests/benchmarks | Schemas, collection contracts, validation, semantic review, link vocabulary, git history |

Atomic and Commonplace share a file-like authoring intuition but diverge immediately on substrate. Atomic stores Markdown-like notes inside application databases so it can attach embeddings, queues, graph state, conversations, and server APIs around them. Commonplace keeps artifacts in Git-tracked Markdown so normal editor, diff, review, and validation workflows remain the primary governance layer.

Atomic is much stronger as an end-user memory product. It has desktop/server/mobile/plugin routes, OAuth/API-token surfaces, a browser clipper, Obsidian sync, Discord capture, MCP, WebSockets, and a visual canvas. Commonplace is stronger as a methodology and review environment: artifact types, collection contracts, link semantics, replacement archives, and validation make the authority of each retained artifact explicit.

The most interesting convergence is reports. Atomic's scheduled reports look like a productized version of a Commonplace workshop-to-library loop: define a research prompt and source scope, run an agent over a bounded corpus, produce a cited finding, and keep provenance. The tradeoff is that Atomic writes generated findings directly into the same atom substrate, while Commonplace usually prefers human-readable review and promotion gates before generated synthesis becomes durable library knowledge.

**Read-back:** both. Ordinary search, chat, MCP, wiki browsing, and canvas use are pull. Scheduled reports are engineered push: a cron/report trigger selects source atoms by tag, kind, time window, and token budget, then injects them into a report agent before it writes a finding.

### Borrowable Ideas

**A report primitive with source scope, context scope, and citation policy.** Ready as a pattern, not as immediate infrastructure. Commonplace already has review runs and workshop artifacts; a durable "report definition" could make recurring investigations auditable without hand-assembling each sweep.

**Separate source scope from context scope.** Atomic's reports distinguish the atoms that are the primary evidence from the broader context the agent may search. Commonplace could borrow this distinction for semantic review bundles and source-grounded notes, especially where citations must resolve only to primary material.

**Kind filters for generated outputs.** Atomic's `kind = captured | report` prevents generated report findings from silently mixing with user-authored atoms on external MCP search by default. Commonplace could use a similar explicit generated/artifact-origin filter in indexes or review selectors. Ready for generated artifacts and AutoReason outputs.

**A queue row as the unifying pipeline contract.** The atom pipeline coalesces create/update/retry/re-embed/re-tag work through durable jobs with leases and status columns. Commonplace does not need a database queue now, but the pattern is useful for long-running generated-index or review-bundle work where retries and visible state matter.

**MCP write tools only after edit safety.** Atomic exposes `edit_atom` with exact-text operations and failure-on-ambiguous edits, rather than only whole-note replacement. If Commonplace ever serves write tools over MCP, targeted structural edits should ship before broad write endpoints.

**Cited generated findings as first-class artifacts.** Atomic's report findings preserve citation rows and provenance. Commonplace can borrow the provenance discipline for generated reviews or recurring scans, but should keep stronger promotion gates before treating findings as library notes.

## Read-back placement

**Direction.** Atomic uses both pull and push. Pull paths include UI search, global keyword search, chat-agent tool calls, MCP `semantic_search` / `read_atom`, wiki article generation, similar-note lookup, and canvas browsing. Push exists through scheduled reports: the scheduler launches a report run, source resolution selects atoms, and the report agent receives a numbered source list before it takes any action.

**Trigger and relevance signal.** Pull triggers are user or agent queries, tag scopes, current-page references, atom ids, or UI events. The engineered push trigger is a report schedule or manual run against a saved report definition. Its relevance signal is symbolic rather than embedding-first: report source scope, context scope, kind filters, time windows, max source atoms, token budgets, citation policy, and excluded prior findings. The report agent can then use semantic search inside the bounded context.

**Timing relative to action.** Report source atoms arrive pre-action. They shape the report agent's initial prompt before it chooses tool calls or writes the finding. Chat search and MCP retrieval happen mid-action only when the agent or external client calls a tool.

**Selection, scope, and complexity.** Search selection uses hybrid ranking, thresholds, limits, recency, and optional tag scope. Atom reads are line-paginated. Report selection adds schedule-derived watermarks, tag subtree resolution, kind filters, source caps, token truncation, and context filters. These are real context-budget controls; effective recall/precision still depends on embeddings, tags, prompts, and model behavior at runtime.

**Authority at consumption.** Search results and atom reads are advisory knowledge artifacts. Chat and MCP tool schemas have system-definition authority over what agents may do. Report definitions have stronger activation authority because they decide that a report agent should run at all and which source corpus it receives. Generated findings become knowledge artifacts with provenance and citations, not hard validators.

**Faithfulness.** Atomic benchmarks retrieval surfaces and has smoke/scaffold benchmark suites, including LongMemEval evidence retrieval support, but I did not find a production WITH/WITHOUT ablation proving that pushed report source batches improve downstream behavior versus an ungrounded report prompt ([bench/README.md](https://github.com/kenforthewin/atomic/blob/dd9a43a29e2afeb815f15f65a9c09bfc01873049/bench/README.md)). The `push-activation` tag is therefore about engineered activation structure, not measured behavioral lift.

**Other consumers.** Humans consume atoms, wiki articles, report findings, canvas clusters, search results, Obsidian views, Discord slash-command results, and dashboard briefings. External agents consume MCP responses. Background tasks consume queues, schedules, settings, and graph state.

## Curiosity Pass

**Atomic is closer to a PKB operating system than a narrow memory module.** The reviewed surface includes capture, editing, search, graph visualization, wiki synthesis, chat, reports, MCP, plugins, feeds, multi-database hosting, and benchmarks. That breadth is useful, but it also means "memory" is spread across many authority paths.

**The generated-knowledge boundary is explicit in reports but softer in wiki articles.** Findings carry `kind = report`, report provenance, and citation rows. Wiki articles also have citations, links, versions, and proposals, but they are framed more as synthesized topic pages than as generated findings with a separate kind filter.

**The trace-looking data is not trace-derived learning.** Chat messages and tool calls are durable logs, and benchmark LongMemEval sessions are imported as atoms for evaluation, but I did not find code that mines agent traces into future rules, skills, prompts, validators, or retrieval policies. Atomic should not receive `trace-derived` for this commit.

**Obsidian sync changes the adoption story.** Atomic can sit beside a human note vault and add semantic services, but the canonical storage for synced material becomes Atomic's server database, not the vault files. That is a different trust posture from file-native Obsidian tools.

**The report scheduler is the distinctive activation mechanism.** Many systems offer MCP search. Fewer let users define recurring, scoped, cited research agents whose outputs rejoin the same memory substrate.

## What to Watch

- Whether report findings gain review/promote/dismiss workflow before they influence wiki synthesis and search as ordinary atoms; that would clarify generated-knowledge authority.
- Whether wiki proposals become the default update path and expose stronger claim-level citation/provenance; that would make synthesized articles safer as reusable knowledge artifacts.
- Whether chat logs/tool calls become inputs to a learning loop; that would change the trace-derived decision.
- Whether MCP gains report, wiki, or scoped-query tools beyond atom CRUD/search; that would expand Atomic from memory store to agent-facing research platform.
- Whether the LongMemEval benchmark moves from retrieval-only evidence metrics to answer generation and behavioral ablation; that would make read-back quality claims more comparable with other memory systems.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Atomic needs separate treatment for atoms, vectors, tags, wiki articles, chat logs, MCP schemas, report definitions, findings, and benchmark outputs.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Atomic has many stored artifacts, but only search/chat/MCP/report paths decide what enters context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: MCP schemas, report definitions, schedulers, queues, and task ledgers configure or route future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: atoms, wiki articles, report findings, citations, and benchmark reports are evidence or context unless a stronger consumption path grants authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - contrasts: Atomic stores chat/tool traces but does not derive durable behavior-shaping artifacts from them at this commit.
