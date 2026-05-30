---
description: "Database-backed markdown atom KB with derived chunks, embeddings, tags, semantic edges, generated wiki articles, chat, and MCP tools"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# Atomic

Atomic is Ken Fortwin's personal knowledge-base application: a Rust `atomic-core` library, Actix server, React/Tauri desktop and web clients, browser extension, mobile-facing web stack, and MCP surface for turning markdown "atoms" into searchable, taggable, graphable, and synthesizeable knowledge. The source of truth is not a folder of markdown files. Atom markdown is stored as database rows, then expanded into derived chunks, embeddings, full-text indexes, tags, semantic edges, wiki articles, chat citations, and UI graph state.

**Repository:** https://github.com/kenforthewin/atomic

**Reviewed commit:** [b6ab726e55a5f5cb477e211df2c2418b22bba349](https://github.com/kenforthewin/atomic/commit/b6ab726e55a5f5cb477e211df2c2418b22bba349)

## Core Ideas

**Atoms are authored markdown, but the operational substrate is a database.** The README presents atoms as markdown notes that get chunked, embedded, tagged, and linked, and the implementation backs that with SQLite plus `sqlite-vec` by default, with a runtime-dispatched Postgres/pgvector backend for server deployments ([README.md](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/README.md), [db.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/db.rs), [storage/mod.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/storage/mod.rs), [storage/postgres/mod.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/storage/postgres/mod.rs)). The authored atom content is a knowledge artifact: future users and agents consume it as evidence, context, or reference. The database schema, vector tables, FTS tables, pipeline queues, and semantic-edge tables are system-definition artifacts when they rank, route, filter, or schedule what later agents see.

**The derived layer is explicit and multi-form, not just "semantic search."** The baseline schema includes `atoms`, `tags`, `atom_tags`, `atom_chunks`, `wiki_articles`, `wiki_citations`, `semantic_edges`, conversations, chat tool calls, chat citations, API tokens, wiki links, and tag embeddings ([db.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/db.rs)). The embedding pipeline chunks atom content, writes chunk embeddings into both `atom_chunks` and `vec_chunks`, tracks embedding/tagging status, and later computes semantic edges and tag centroids ([embedding.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/embedding.rs), [storage/sqlite/chunks.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/storage/sqlite/chunks.rs), [graph_maintenance.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/graph_maintenance.rs)). Representational form is mixed: prose markdown atoms and wiki articles, symbolic database rows and relationship tables, and distributed-parametric embeddings.

**Tags are partly authored taxonomy and partly LLM-derived navigation structure.** Atomic stores hierarchical tags, lets users mark tag categories as auto-tag targets, and asks an LLM to extract only valid child tags under configured top-level categories ([models.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/models.rs), [extraction.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/extraction.rs), [storage/traits.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/storage/traits.rs)). These tags behave differently depending on the consumer: they are knowledge artifacts when a person browses categories, and system-definition artifacts when retrieval, wiki generation, graph layout, or chat scope uses them to decide what enters context.

**Wiki synthesis is a real generated-prose layer with citations and versioning.** A wiki article is not the source note; it is a derived retained artifact stored under `wiki_articles`, linked to source chunks through `wiki_citations`, and exposed with versions, proposals, links, and related tags ([wiki/mod.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/wiki/mod.rs), [docs/manual/concepts/wiki-synthesis.md](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/docs/manual/concepts/wiki-synthesis.md)). The agentic strategy runs a research loop with `search`, `select`, and `done` tools, then synthesizes the selected chunks into cited markdown ([wiki/agentic.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/wiki/agentic.rs)). This is a clean lineage split: atoms remain source, chunks and citations carry derivation, and wiki prose is a derived knowledge artifact.

**Chat and MCP turn the same substrate into an agent-facing memory surface.** The in-app chat agent has tools for hybrid atom search, atom reads, atom creation, targeted atom edits, page context, and canvas actions ([agent.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/agent.rs)). The embedded MCP server exposes `semantic_search`, `read_atom`, `create_atom`, `ingest_url`, `update_atom`, and `edit_atom`, with tool descriptions that instruct clients when to search, remember, or mutate memory ([mcp/server.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-server/src/mcp/server.rs)). The MCP bridge adds a stdio-to-HTTP adapter for local clients ([crates/mcp-bridge](https://github.com/kenforthewin/atomic/tree/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/mcp-bridge)). Here the atom content is advisory knowledge, while tool descriptions, pagination limits, edit guards, and search ranking have instruction, routing, and mutation authority.

**Import and capture paths preserve source identity but normalize everything into atoms.** URL ingestion resolves page content and creates atoms; RSS, browser clipping, Obsidian import, Apple Notes import, and scripts all converge on the same atom model ([ingest/mod.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/ingest/mod.rs), [import/obsidian.rs](https://github.com/kenforthewin/atomic/blob/b6ab726e55a5f5cb477e211df2c2418b22bba349/crates/atomic-core/src/import/obsidian.rs), [extension](https://github.com/kenforthewin/atomic/tree/b6ab726e55a5f5cb477e211df2c2418b22bba349/extension)). Lineage is mostly source URL, published date, source field, and derived citations. There is not a review state, claim status, or source-confidence model comparable to commonplace's typed notes and review gates.

## Comparison with Our System

| Dimension | Atomic | Commonplace |
|---|---|---|
| Primary substrate | SQLite or Postgres rows containing markdown atoms and derived indexes | Markdown files in git, with derived indexes kept secondary |
| Source of truth | Database atom records | Repository files and explicit type contracts |
| Knowledge unit | Atom markdown plus source metadata | Typed notes, reference docs, instructions, sources, reviews, workshop artifacts |
| Derived views | Chunks, embeddings, FTS, semantic edges, tag centroids, wiki articles, graph positions | Directory indexes, validation reports, reviews, generated navigation |
| Link model | Materialized `[[...]]` atom links, semantic edges, tags, wiki links | Markdown links with explicit relationship prose and collection-local linking rules |
| Agent surface | In-app chat, MCP HTTP endpoint, stdio bridge, browser and app clients | Agent uses files, `rg`, skills, validation, review bundles, and CLI commands |
| Learning model | Source-derived enrichment from atoms into tags/embeddings/edges/wiki prose | Deliberate distillation from work into library notes, instructions, validation, skills |
| Governance | Status columns, queues, citations, proposal flow, API tokens, OAuth | Frontmatter schema, collection contracts, semantic review, git history, human-readable diffs |

Atomic is the strongest nearby database-first counterexample to commonplace's files-first default. It pays the application and migration cost, but it gets a coherent product in return: cross-client access, fast hybrid search, background pipelines, graph/cache state, auth, MCP, and generated wiki views. Commonplace would have to build those operational surfaces on top of files; Atomic gets them by making the database the real substrate.

The cost is inspectability and artifact-level governance. A commonplace note can be reviewed, diffed, linked, classified, and revised as a file. An Atomic atom can be read as markdown, but its behavior-shaping context depends on database state: pending jobs, chunk boundaries, vector dimensions, FTS rows, auto-tags, semantic edges, wiki citations, and model settings. That makes Atomic better as an app and weaker as a self-describing methodology corpus.

Atomic also separates "knowledge artifact" and "system-definition artifact" less explicitly. In code, the separation is real: atom prose, wiki prose, embeddings, tag rows, edge rows, tool descriptions, and chat citations all have different consumers and force. In the product model, they are mostly presented as one knowledge graph. Commonplace's vocabulary is useful here because the same stored object can advise a reader, route a retriever, or instruct an MCP client depending on the consumption path.

**Read-back:** pull — chat and MCP clients deliberately invoke search/read tools; no proactive injection path is described.

## Borrowable Ideas

**Generated wiki articles with citation-backed lineage.** Ready to borrow as a pattern, not as-is. Atomic's wiki layer is a concrete example of a derived synthesis surface that remains tied to source chunks and can be proposed before acceptance. In commonplace, this would look like generated topic briefs or survey drafts under `kb/work/`, with citations and a promotion path into notes only after review.

**A local operational database for high-volume derived state.** Needs a use case first. Atomic shows exactly where a database earns its keep: vector tables, FTS, status queues, tag centroids, chat citations, graph layout, API tokens. Commonplace should not move authored notes into a database, but a scoped operational database for expensive derived state is defensible once `rg` and generated indexes stop being enough.

**MCP tools with behaviorally explicit descriptions.** Ready to borrow if commonplace gets a serving layer. Atomic's MCP tool descriptions tell the agent when to search, read, remember, and edit. That is a small but important system-definition surface: the tool schema does not just expose capability, it shapes use.

**Targeted edit operations for memory mutation.** Ready to borrow conceptually. Atomic's chat and MCP edit paths prefer exact-text `replace`, `insert_after`, `append`, and guarded `replace_all` operations over blind full-record replacement. That maps cleanly to agent note editing in commonplace, where narrow patches are safer than wholesale rewrites.

**Proposal flow for generated synthesis.** Ready to borrow for generated summaries. Atomic's wiki proposal flow distinguishes draft generation from acceptance or dismissal. Commonplace already has review and promotion concepts; this is the same pattern applied to generated synthesis artifacts before they become durable library content.

**Multi-client packaging around one core.** Mostly a reference. Atomic's `atomic-core` plus server/client/MCP split is useful if commonplace ever becomes a served application. For the current repo-native KB, it would be premature infrastructure.

## Curiosity Pass

**The "markdown note" framing hides a real database commitment.** Atomic does preserve atom bodies as readable markdown strings, but that is not the same architectural bet as file-backed markdown. The durable behavior of the system depends on schema migrations, indexes, background jobs, and provider settings. That is not a flaw; it is the price of being a polished app rather than a repo-native knowledge system.

**The semantic graph is mostly a retrieval and visualization graph.** Semantic edges, tag centroids, and canvas state are useful, but they are derived similarity structures, not authored claims about relationships. Even if they work perfectly, they improve discovery and layout more than they improve trust, explanation, or claim quality.

**Wiki synthesis is the most interesting retained artifact.** Embeddings and tags help retrieve; generated wiki prose changes what a later reader can consume directly. The citation and version model makes it much more reviewable than a generic RAG answer. The open question is whether users treat wiki articles as provisional derived views or as canonical summaries that gradually outrank the source atoms.

**Chat logs are persisted, but this is not trace-derived learning in the survey sense.** Atomic stores conversations, messages, tool calls, and chat citations, and the chat agent can create or edit atoms when the user asks. I did not find an implementation that automatically distills agent traces, tool trajectories, or repeated chat failures into durable lessons, rules, skills, prompt changes, rankers, or model weights. The implemented learning is source-derived enrichment from atoms, not trace-derived learning from agent runs.

**The product has stronger activation surfaces than most personal KBs.** MCP tools, in-app chat, page context, canvas context, and generated wiki articles all create routes from stored knowledge into action. The remaining limitation is the usual one: search and chat can expose candidate context, but they do not guarantee the agent will activate the right knowledge at the right moment.

## What to Watch

- Whether wiki articles become governed derived views with stronger staleness, supersession, and review semantics, or remain convenient generated summaries.
- Whether chat/tool traces begin feeding durable behavior-shaping artifacts, which would move Atomic into trace-derived learning territory.
- Whether Postgres mode becomes a first-class hosted product path or stays an optional backend behind the local SQLite default.
- Whether semantic edges evolve from similarity links into typed, authored, or extracted relationship claims.
- Whether MCP tools gain richer scoped retrieval, citation, and edit contracts that make Atomic usable as a memory backend for coding agents rather than only as a personal KB.

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — contrasts: Atomic is a strong database-first counterexample where app packaging, queues, auth, vectors, and generated views justify a heavier substrate
- [knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — frames: Atomic improves storage-to-context routing through search, chat, MCP, and wiki views, but still faces the context-to-action activation problem
- [retained artifact](../../notes/definitions/retained-artifact.md) — clarifies: Atomic's atoms, embeddings, tags, semantic edges, wiki articles, MCP tool descriptions, and chat citations are different retained artifacts with different consumption paths
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) — classifies: authored atoms and generated wiki prose are knowledge artifacts when consumed as evidence, reference, context, or explanation
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) — classifies: retrieval indexes, tag scopes, tool descriptions, edit guards, and background queues become system-definition artifacts when they route, rank, instruct, or mutate behavior
- [engraph](./engraph.md) — compares: both serve markdown-shaped knowledge to agents, but engraph keeps a human vault as source of truth while Atomic owns the database substrate
- [GBrain](./gbrain.md) — compares: both synthesize durable pages over personal knowledge, but GBrain keeps compiled truth in markdown files while Atomic stores generated wiki articles in the app database
- [Cognee](./cognee.md) — compares: both treat knowledge as a database-backed enrichment pipeline, but Atomic is a personal KB product with authored atoms and wiki synthesis rather than a developer data pipeline
