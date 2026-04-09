---
description: Obsidian vault server with SQLite hybrid index, wikilink graph expansion, section-level writes, and local MCP/HTTP surfaces; strongest local-first derived index over a human note substrate
type: related-system
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: 2026-04-07
---

# engraph

engraph is a Rust CLI and server that turns an Obsidian-style markdown vault into a local retrieval and editing service for agents. It indexes vault files into SQLite with FTS5, sqlite-vec, explicit link edges, folder centroids, and some lightweight metadata, then exposes that derived layer through CLI search, an MCP server, and an optional HTTP API. The source of truth remains the vault files themselves; engraph’s main contribution is an operational index and tool surface over that substrate.

**Repository:** https://github.com/devwhodevs/engraph

## Core Ideas

**The primary move is “real files plus a derived local index,” not a new knowledge substrate.** `indexer.rs` walks `.md` files from the vault, chunks them, embeds them, stores file/chunk metadata in SQLite, pushes vectors into a `sqlite-vec` table, and builds an `edges` table from explicit wikilinks and mention heuristics. This is closer to an operational acceleration layer than to a replacement knowledge base. The vault stays human-readable and editable; SQLite exists to make retrieval and mutation tooling fast.

**“Knowledge graph” means wikilinks, mentions, and retrieval scaffolding, not extracted semantics.** The graph layer is concrete, but narrower than the name suggests. `graph.rs` extracts `[[wikilink]]` targets, adds mention edges for people-like notes, and expands search results one or two hops with decay and relevance filters. There is no ontology extraction, no freeform entity graph, and no deeper semantic graph reasoning. The graph is primarily a navigation booster over existing vault structure.

**Hybrid retrieval is genuinely implemented and reasonably disciplined.** `search.rs` runs a pipeline of semantic vector search, FTS5 keyword search, graph expansion, optional cross-encoder reranking, and optional temporal scoring, then fuses lanes with Reciprocal Rank Fusion. When intelligence is enabled, an orchestrator model classifies intent and generates expansions; when it is not, the system falls back to heuristics. This is more than README theater: the retrieval logic is explicit, weighted, and inspectable.

**The write path is an agent-shaped mutation pipeline over markdown, not raw CRUD.** `writer.rs` does more than “write this file”: it resolves tags against a registry, discovers candidate wikilinks, suggests folders via type rules and centroid similarity, writes atomically, preserves or edits frontmatter structurally, and updates the index immediately. Section-level edits by heading are especially notable because they give agents a narrower write target than whole-file replacement.

**The system learns only weakly from its own operation.** The most interesting adaptive loop is folder placement correction. If an engraph-created note lands in inbox with `suggested_folder` metadata and is later moved, the watcher records a placement correction and adjusts folder centroid statistics. That is real feedback, but it is narrow. There is no broader loop that extracts durable symbolic knowledge from agent sessions, search logs, or editing traces.

**Several “intelligence” and maintenance claims are real but partial.** The local LLM stack for embeddings, query orchestration, and reranking is implemented through `llama.cpp`, and the Obsidian CLI wrapper really does use a circuit breaker. But some richer claims are thinner in code. `health.rs` has working orphan/broken-link checks, yet stale-note detection is still a stub. The ignored integration tests also still reference removed `embedder` and `hnsw` modules, which suggests some doc/test drift around the newer sqlite-vec architecture.

## Comparison with Our System

| Dimension | engraph | Commonplace |
|---|---|---|
| Primary purpose | Agent-facing retrieval/edit server over an Obsidian vault | Knowledge methodology for durable agent-operated markdown KBs |
| Source of truth | Markdown vault files | Markdown notes/instructions/tasks/sources in git |
| Derived layer | SQLite index with FTS5, vectors, edges, centroids, caches | Minimal derived structure; mostly direct files, indexes, and grep |
| Link model | Explicit wikilinks plus mention heuristics, used for search expansion | Standard markdown links with explicit relationship semantics |
| Retrieval model | Multi-lane search server with optional LLM orchestration and reranking | Routing, descriptions, curated indexes, `rg`, and explicit traversal |
| Write model | Structured note mutation tools: section edits, frontmatter ops, placement help | Direct file edits guided by templates, review, and validation |
| Learning model | Weak operational adaptation via placement corrections and cached orchestration | Stronger theory of distillation/constraining/codification, but more manual |
| Human/agent coexistence | Strong for Obsidian users who want agents to query/write their existing vault | Strong for repo-native maintenance and reasoning, weaker as a drop-in Obsidian layer |

engraph is stronger where commonplace is intentionally thin: it packages retrieval, editing, and serving into one local agent-facing product with fast derived search and a clear MCP/HTTP integration story. Commonplace is stronger where engraph stays mostly infrastructural: semantic links, note-type discipline, explanatory curation, and a stronger distinction between retrieval convenience and actual knowledge quality.

The deepest split is what each system thinks improvement means. engraph improves agent access to an existing vault. Commonplace tries to improve the knowledge itself so future access becomes easier because the artifacts are better, not just because retrieval is faster.

## Borrowable Ideas

**A derived operational index beneath a file-first substrate.** engraph is a strong reference for keeping files as the truth while building a local database underneath for speed, ranking, and richer queries. Ready to borrow when we need high-volume operational retrieval without giving up inspectable files.

**Section-level editing as a first-class write primitive.** Editing a note by heading is a better agent interface than whole-file rewrites for many maintenance tasks. Ready to borrow now if we expose more structured write tools over the KB.

**Read-only server mode and split auth scopes are practical serving patterns.** The MCP/HTTP surfaces distinguish read from write and include a read-only mode plus HTTP key permissions. Ready to borrow once commonplace needs to serve itself to external agents or web clients.

**Placement suggestions with explicit low-confidence breadcrumbs.** When semantic placement is uncertain, engraph records a suggested folder and confidence in frontmatter rather than pretending the decision is reliable. That is a useful pattern for weak-oracle automation. Ready to borrow now as a general UI/agent honesty principle.

**Obsidian CLI delegation behind a circuit breaker.** If we ever bridge into editor-native actions, engraph’s “delegate when healthy, fall back when not” pattern is worth reusing. Needs a concrete use case first.

## Curiosity Pass

**The “knowledge graph” label overstates the representation change.** The property claimed is graph-aware knowledge access. The mechanism is real but modest: engraph stores existing file structure, explicit links, mention heuristics, and retrieval metadata in SQLite. That helps search, but it does not transform markdown into a richer semantic graph in the stronger knowledge-engine sense. The simpler alternative is “vector index plus FTS over files.” engraph’s extra graph layer earns something, but the gain is better navigation over authored links, not a new knowledge representation.

**The hybrid search pipeline is load-bearing, but mostly for retrieval ranking, not contextual activation.** The orchestrator, RRF fusion, reranker, and temporal lane do improve result selection. But even if they worked perfectly, they would still only choose and rank candidate notes. They do not solve the harder problem of determining what an agent should do with those notes once loaded. This is exactly why retrieval quality and [contextual competence](../an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) should not be conflated.

**The write pipeline is stronger as guardrailed mutation than as learning.** Tag resolution, link discovery, atomic writes, and placement hints are valuable. But the only real adaptive loop is placement correction from later moves. That is useful operational feedback, yet its ceiling is narrow: it can improve folder suggestions, not vault semantics or note quality broadly.

**The health layer shows the boundary between diagnosable structure and subjective quality.** Broken links and orphans are cheap structural checks, so they are implemented. Staleness is much harder to define without stronger semantics, so it remains a stub. That asymmetry is a good reminder that symbolic diagnostics scale best where the target property is structurally verifiable.

**There are signs of rapid iteration around the indexing architecture.** The main code has converged on sqlite-vec, but some ignored integration tests still reference older `embedder` and `hnsw` modules that no longer exist in `lib.rs`. That does not break the primary mechanism, but it is a real maintenance signal: the repo is evolving faster than all of its auxiliary surfaces.

## What to Watch

- Does engraph remain a derived-index layer over files, or drift toward database-first ownership of the vault?
- Does the graph layer become semantically richer, or stay intentionally limited to wikilinks and mentions?
- Does the write pipeline gain stronger feedback loops than placement correction, such as better link-validation or structure-learning from user edits?
- Do the health diagnostics grow beyond structural checks into something more semantically useful, or does that prove too subjective to automate cheaply?
- Do tests and docs fully catch up to the sqlite-vec architecture, or does transition drift keep accumulating?

---

Relevant Notes:

- [Files, not database](../files-not-database.md) — contrasts: engraph is a strong counterexample only if you mistake the derived SQLite layer for the primary substrate; the actual source of truth remains files
- [Inspectable substrate, not supervision, defeats the blackbox problem](../inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — grounds: engraph keeps the inspectable markdown substrate even while adding heavier retrieval machinery underneath
- [Knowledge storage does not imply contextual activation](../knowledge-storage-does-not-imply-contextual-activation.md) — extends: engraph improves storage and retrieval access, but that does not by itself produce good activation decisions for agents
- [Agents navigate by deciding what to read next](../agents-navigate-by-deciding-what-to-read-next.md) — contrasts: engraph automates ranking aggressively, while commonplace leans more on explicit descriptions, indexes, and traversal choices
- [An agentic KB maximizes contextual competence through discoverable, composable, trusted knowledge](../an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) — contrasts: engraph is strong on discoverability, thinner on composability and trustworthiness in the knowledge-design sense
- [Napkin](./napkin.md) — compares: both adapt a human Obsidian-like markdown substrate for agents, but Napkin emphasizes CLI-shaped progressive disclosure while engraph emphasizes a heavier local server and derived index
- [OpenViking](./openviking.md) — contrasts: both add filesystem-shaped agent access over richer retrieval layers, but OpenViking virtualizes the whole filesystem over a database while engraph keeps a real vault and builds a local index under it
- [CocoIndex](./cocoindex.md) — parallels: both are strongest as derived maintenance/index layers below a primary knowledge substrate rather than as the substrate itself
