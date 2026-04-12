---
description: Database-backed personal KB that stores markdown atoms in SQLite/Postgres, enriches them with embeddings/tags/semantic edges, and builds per-tag wiki plus search/chat surfaces
type: agent-memory-system-review
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-05"
---

# Atomic

Atomic is a Rust-centered personal knowledge base by `kenforthewin` that treats markdown as the authoring format but not as the primary storage substrate. At version `1.13.3`, the repo ships a Tauri desktop app, a headless HTTP server, a web UI, an iOS client, a browser extension, and an MCP surface, all organized around a shared `atomic-core`. The system's central bet is that a note should be captured once as an "atom," then asynchronously expanded into a richer derived layer: markdown-aware chunks, vector embeddings, LLM-extracted tags, similarity edges, per-tag wiki articles, and chat/search affordances.

**Repository:** https://github.com/kenforthewin/atomic

## Core Ideas

**Markdown is the input medium, but the database is the real substrate.** Atoms start as markdown content with optional source URLs and tags, but the durable system lives in SQLite or Postgres tables, not in a browsable file tree. `db.rs` creates tables for `atoms`, `atom_chunks`, `semantic_edges`, `wiki_articles`, `chat_messages`, and `tag_embeddings`, plus a sqlite-vec virtual table and FTS5 index for search. This makes Atomic closer to a local knowledge service that happens to ingest markdown than to a file-first note library.

**Write-time enrichment is the main knowledge-construction mechanism.** Saving an atom is intentionally cheap for the caller, but it kicks off a background pipeline in `embedding.rs`: markdown-aware chunking (`chunking.rs`), batch embedding generation, optional LLM tag extraction under fixed top-level categories, semantic-edge recomputation, and tag-centroid refresh. The enriched layer is not decorative. Search, wiki generation, canvas layout, and chat all depend on it.

**Hierarchical tags are the routing spine for the whole system.** Tags are not just labels for filtering. The repo seeds five top-level categories (`Topics`, `People`, `Locations`, `Organizations`, `Events`), stores tags as a tree, computes centroid embeddings for them, scopes search/chat to them, and uses them as the owning key for wiki articles. This is the repo's main organizational abstraction: if an atom is not well-tagged, most of Atomic's higher-level surfaces degrade.

**The wiki layer is a maintained derived artifact, not a one-shot answer.** Atomic synthesizes markdown wiki articles per tag, persists citations and wiki-links, versions article revisions, and supports incremental updates that ingest only new atoms since the last article refresh. The default strategy pulls source chunks by tag-centroid similarity; an alternative "agentic" strategy runs a bounded research loop with `search`, `select`, and `done` tools before shared synthesis. This is one of the stronger implemented examples in the repo: the wiki is durable, citable, and treated as a maintained intermediate layer rather than a transient chat output.

**Knowledge access is retrieval-first and tool-mediated rather than link-navigated.** Atomic's search path is hybrid BM25 plus vector similarity, merged through reciprocal rank fusion. The chat agent does not traverse authored relationships or curated indexes; it calls `search_atoms` and `get_atom`, collects citations, and answers from retrieved chunks. The MCP surface exposes the same orientation to external agents through `semantic_search`, `read_atom`, `create_atom`, and `update_atom`. This makes Atomic strong at scoped recall over accumulated notes, but much thinner on authored semantic relationships than commonplace.

**The engineering architecture is intentionally core-plus-wrappers.** `atomic-core` owns the domain logic while `atomic-server`, the Tauri sidecar, the web client, the iOS client, and the MCP bridge stay comparatively thin. The callback-based event design is especially clean: background embedding and chat emit generic events, and each wrapper decides whether to surface them as WebSocket broadcasts, Tauri emits, or MCP-facing behavior. This is more about deployment shape than knowledge theory, but it is a real strength of the implementation.

## Comparison with Our System

| Dimension | Atomic | Commonplace |
|---|---|---|
| Primary substrate | SQLite by default, optional Postgres, with markdown stored inside DB rows | Real markdown files in git |
| Authoring unit | "Atom" record with markdown content and derived DB artifacts | Typed note/instruction/review artifacts with explicit frontmatter and links |
| Main organization primitive | Hierarchical tags under fixed top-level categories | Types, descriptions, freeform tags, and semantic markdown links |
| Retrieval model | Hybrid FTS + vector search, tag scoping, tool-calling chat | Search, descriptions, indexes, and explicit link-following |
| Derived knowledge layer | Per-tag wiki articles with citations, versions, and wiki-links | Curated notes and indexes; no compiled wiki layer |
| Relationship model | Similarity edges inferred from embeddings; tag membership inferred or assigned | Explicit authored links with articulated relationship semantics |
| Integration surface | Desktop, browser, server, iOS, browser extension, MCP, multi-db registry | Repo-first KB inside an agent harness |
| Inspectability | Strong through UI/API and code, weaker at raw-substrate level because knowledge lives in DB tables | Strong at raw-substrate level because the artifacts are the substrate |
| Learning / maintenance posture | Continuous derived-index maintenance after writes; no real contradiction audit or trace-to-artifact learning loop | Manual-but-explicit workshop/library boundary, status transitions, and stronger theory for maturation |

Atomic is stronger where database-backed derived views genuinely earn their cost. It offers hybrid search, citation-bearing synthesized wiki articles, force-layout visualization, multi-client access, and an MCP/HTTP surface without asking each client to re-implement knowledge operations. Commonplace is stronger where inspectable authorship, semantic link meaning, and knowledge maturation matter more than service convenience. Our notes explain why ideas relate; Atomic mostly computes that notes are similar.

The deepest difference is where each system commits structure. Atomic commits structure into runtime-maintained derived artifacts: chunk tables, vector indexes, tag trees, semantic-edge tables, and wiki articles. Commonplace commits structure into the durable authored artifacts themselves: claim-shaped titles, descriptions, note types, and relationship-bearing links. Atomic treats the KB as a live knowledge service. Commonplace treats it as a curated document system that agents navigate directly.

## Borrowable Ideas

**Core domain logic behind thin transport wrappers.** Atomic's `atomic-core` plus wrapper pattern is worth borrowing as an architectural boundary. If commonplace ever needs a server, MCP surface, or alternate client, the right move is not to duplicate knowledge logic per interface but to keep one core and treat each transport as an adapter. Ready to borrow now as a systems pattern.

**Persist generated overview artifacts with citations, not just ephemeral answers.** Atomic's wiki articles are durable objects with citations, versions, and explicit update paths. We do not need tag-owned wiki pages by default, but the general pattern is strong: when a derived summary becomes operationally important, persist it as a maintained artifact rather than recomputing it invisibly every time. Needs a concrete use case first.

**Use background maintenance to keep secondary artifacts fresh.** Atomic's write path keeps chunks, embeddings, semantic edges, and tag centroids synchronized without making the user wait. Commonplace should stay cautious about hiding too much behind background automation, but the underlying pattern is valuable for rebuildable operational layers. Ready to borrow when we introduce more derived indexes or workshop maintenance tasks.

**Store citation structure alongside generated prose.** Atomic does not just ask the model to cite; it persists citation mappings and wiki-link extractions as first-class data. If we add any generated survey, overview, or workshop digest artifact, preserving the evidence map explicitly would keep the generated text inspectable and revisable. Ready to borrow now for generated artifacts.

**Treat collection-level summaries as their own retrieval target.** The tag-centroid plus wiki strategy shows a practical middle layer between raw note retrieval and final answers. Commonplace already has descriptions and indexes, but not maintained collection summaries keyed to a concept cluster. This is a real design option if certain tags or workshops become too large for direct traversal. Needs a use case first.

## Curiosity Pass

**"Semantically-connected knowledge graph" is only partly a graph in the strong sense.** The claimed property is richer, navigable knowledge structure. Mechanistically, Atomic does transform notes into edges, but the edge construction is similarity-based (`compute_semantic_edges_for_atom(...)` over chunk embeddings), not authored or typed relation semantics. The simpler alternative is "vector search over notes without persisting pairwise edges." Atomic's edge table is useful for neighborhood views and canvas layout, but its ceiling is lower than the phrase "knowledge graph" suggests: similarity edges cannot by themselves say whether one atom grounds, contradicts, or supersedes another.

**The asynchronous enrichment pipeline is real transformation, but it centralizes fragility in tagging.** The property is low-friction capture with rich retrieval surfaces. That part is implemented honestly: chunking, embeddings, FTS, centroid embeddings, and edge recomputation all change what the system can do. But the single-call tag extractor is load-bearing for routing, wiki ownership, and chat scoping, and it constrains everything into a fixed two-level category system. The simpler alternative is manual tagging plus search. Atomic's choice buys automation, but the ceiling is bounded by whether its tag tree stays coherent across messy real-world corpora.

**The wiki layer is the repo's most meaningful knowledge artifact.** The property is compounding knowledge rather than repeated answer synthesis. Here the mechanism really does transform the inputs: selected chunks become a cited article with persistent versions and incremental updates. The simpler alternative is "just answer from retrieval on demand." Atomic beats that by making a reusable intermediate layer. But the repo's own `llm-wiki-gist-analysis.md` is revealing: contradiction linting, cross-atom reconciliation, chat-answer promotion, and visible activity history are still missing. So the wiki is maintained, but not yet self-auditing.

**The database-first choice buys synchronized derived views, but gives up raw-substrate inspectability.** The property is an always-on, multi-client personal knowledge service. Mechanistically this is true: SQLite/FTS/sqlite-vec tables, a registry split, API tokens, and optional Postgres all support app-style operation better than flat files would. The simpler alternative is a file vault with derived indexes beside it. Atomic rejects that and gets transactional coordination in return. The ceiling is that every important knowledge surface now depends on Atomic's own code or API. Even though the note content is markdown, the knowledge system is not tool-agnostic in the way a real file substrate is.

**The transport architecture is cleaner than the backend abstraction story.** The wrapper pattern is implemented well. By contrast, the storage abstraction is still mid-migration: comments in `lib.rs` and `storage/mod.rs` explicitly note that search, chat, wiki, pipeline status, and some imports are not fully migrated for Postgres. This does not invalidate the design, but it matters for evaluation. The stronger claim today is "SQLite-first architecture with a serious Postgres migration underway," not "fully backend-agnostic knowledge engine."

## What to Watch

- Whether the tag-centered organization holds up once users push beyond entity-like knowledge into more process-heavy or argument-heavy note collections.
- Whether the wiki layer gains contradiction detection, stale-claim linting, and answer-to-article promotion, or remains a well-implemented but still mostly one-way synthesis surface.
- Whether the Postgres path reaches true feature parity, or SQLite remains the de facto canonical backend despite the abstraction layer.
- Whether Atomic ever exposes a more semantically meaningful relationship layer than embedding-neighborhood edges, especially if it keeps leaning on the "knowledge graph" framing.
- Whether the system's strongest future ends up being "personal wiki compiler with chat" rather than "general PKB platform" as more features accumulate around the tag/wiki core.

---

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — contrasts: Atomic is a strong database-first counterexample where synchronized derived views are central, not a narrow operational exception
- [Substrate class, backend, and artifact form are separate axes that get conflated](../../notes/substrate-class-backend-and-artifact-form-are-separate-axes-that-get-conflated.md) — sharpens: Atomic keeps symbolic artifacts in a database/service backend, which separates the backend choice from the artifact class
- [Pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — contrasts: Atomic leans on query-time retrieval and generated wiki layers where commonplace leans on authored pointers and link phrases
- [Inspectable substrate, not supervision, defeats the blackbox problem](../../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — contrasts: Atomic keeps the code inspectable, but not the knowledge substrate itself at the same raw level as repo-hosted notes
- [The fundamental split in agent memory is not storage format but who decides what to remember](../agentic-memory-systems-comparative-review.md) — extends: Atomic belongs on the database-backed, retrieval-first side of the broader agency/substrate design space
- [browzy.ai](./browzy-ai.md) — compares: both systems maintain a wiki-like intermediate layer, but browzy keeps readable files as the main artifact while Atomic keeps the center of gravity in database-backed atoms and tags
- [Pal](./pal.md) — compares: both systems use a maintained wiki layer inside a broader agent/runtime architecture, but PAL splits routing metadata, learnings, and wiki more explicitly while Atomic recenters everything on tags and atoms
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — boundary: Atomic persists chat transcripts and messages, but the inspected repo does not yet mine them into durable learned artifacts, so it sits outside the trace-derived queue for now
