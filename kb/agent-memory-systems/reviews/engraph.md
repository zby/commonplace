---
description: "Obsidian vault server with canonical markdown files, SQLite FTS/vector/graph indexes, hybrid ranking, MCP/HTTP write tools, health diagnostics, and narrow placement-feedback learning"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# engraph

engraph is a Rust CLI and local server by devwhodevs that turns an Obsidian-style markdown vault into an agent-facing knowledge API. Its core shape is canonical markdown files on disk, a derived SQLite index with FTS5, sqlite-vec, graph edges, tags, temporal dates, LLM cache, folder centroids, and audit-ish operation tables, then CLI/MCP/HTTP surfaces that let Claude, Cursor, ChatGPT Actions, scripts, and local tools search, read, edit, migrate, and diagnose the vault.

**Repository:** https://github.com/devwhodevs/engraph

**Reviewed revision:** [ab452322fcac432f6736a1fbc9db967788d01918](https://github.com/devwhodevs/engraph/commit/ab452322fcac432f6736a1fbc9db967788d01918)

## Core Ideas

**Markdown remains canonical; SQLite is a derived operating index.** The primary source of truth is the user's vault of `.md` files walked by the indexer, while `~/.engraph/engraph.db` stores file records, chunks, FTS rows, vector rows, wikilink/mention edges, tags, temporal metadata, LLM query-plan cache, folder centroids, placement corrections, migration logs, identity facts, and CLI events ([`src/indexer.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/indexer.rs), [`src/store.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/store.rs)). That makes the vault files knowledge artifacts when read as evidence or context, and makes the SQLite index a system-definition artifact when it routes, ranks, filters, validates, or updates agent behavior.

**The derived index combines symbolic, lexical, graph, temporal, and distributed-parametric forms.** Markdown chunks are embedded through local llama.cpp models and inserted into sqlite-vec, snippets go into FTS5, wikilinks and person mentions become bidirectional or directed `edges`, note dates are extracted from frontmatter or filenames, and folder centroids become vector summaries used for placement ([`src/indexer.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/indexer.rs), [`src/vecstore.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/vecstore.rs), [`src/graph.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/graph.rs), [`src/temporal.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/temporal.rs), [`src/placement.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/placement.rs)). The representational form is mixed: prose markdown is the inspectable substrate; symbolic tables and Rust policies define resolution; vectors and centroids exert ranking and placement influence.

**Search is an explicit ranking policy, not just vector recall.** `search_with_intelligence` orchestrates query intent and expansions, runs semantic KNN and FTS lanes, expands through the vault graph, optionally reranks candidates with a cross-encoder, adds a temporal lane for date-aware queries, and fuses lanes through weighted reciprocal rank fusion ([`src/search.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/search.rs), [`src/fusion.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/fusion.rs), [`src/llm.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/llm.rs)). The LLM orchestrator and reranker are optional local models; when disabled, heuristic orchestration still supplies lane weights. This is system-definition authority because it controls which retained artifacts reach the agent and with what score.

**The graph layer is pragmatic Obsidian expansion.** engraph extracts `[[wikilinks]]`, resolves targets by exact path or basename, stores both directions for wikilinks, detects people mentions from the configured People folder and aliases, then uses one- or two-hop graph expansion with query-term or shared-tag relevance filtering ([`src/graph.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/graph.rs), [`src/indexer.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/indexer.rs)). It is not a semantic ontology. It is an agent-useful navigation layer over existing note conventions.

**Write tools can mutate the canonical vault, but many edits rely on watcher re-indexing.** The create pipeline resolves tags, discovers wikilinks, chooses a folder, writes atomically, indexes immediately, and adjusts folder centroids; append performs mtime conflict checks and reindexes; metadata updates edit frontmatter; section edit and rewrite write files and update mtimes, with server-side `recent_writes` coordination so the watcher avoids duplicate processing ([`src/writer.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/writer.rs), [`src/watcher.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/watcher.rs), [`src/serve.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/serve.rs)). The authority split matters: read tools expose knowledge artifacts; write, move, archive, migrate, and setup tools are system-definition surfaces because they change the canonical substrate or derived routing layer.

**MCP and HTTP expose the same basic vault affordances with different governance.** The MCP server exposes search, read/list/context tools, write tools, health, migration, delete, and reindex, with a `read_only` mode blocking write operations ([`src/serve.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/serve.rs)). The HTTP server mirrors those capabilities through axum routes, API-key auth with read/write permission, per-key rate limiting, CORS, OpenAPI, and ChatGPT plugin manifest endpoints ([`src/http.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/http.rs), [`src/openapi.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/openapi.rs)). This is stronger distribution packaging than a CLI-only memory tool, but the trust boundary is still local configuration and API key discipline.

**Health diagnostics are useful but thinner than the README implies.** The implemented report detects orphan notes, unresolved wikilinks, inbox backlog, simple work-tag hygiene, total files, and index age ([`src/health.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/health.rs)). Stale-note detection is currently a stub returning an empty vector, even though the README presents stale content as part of vault health ([`README.md`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/README.md), [`src/health.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/health.rs)). Treat health as structural diagnostics, not semantic review.

## Comparison with Our System

| Dimension | engraph | Commonplace |
|---|---|---|
| Canonical substrate | User's Obsidian/markdown vault | Repo-native markdown KB |
| Derived index | SQLite with FTS5, sqlite-vec, graph edges, dates, tags, centroids, caches | Generated indexes and validation outputs, mostly file-readable |
| Retrieval | Hybrid ranked search with semantic, lexical, graph, rerank, and temporal lanes | `rg`, curated indexes, authored links, descriptions, and targeted commands |
| Link model | Wikilink/mention graph inferred from existing notes | Authored links with collection-specific semantic labels and reader-need contracts |
| Write authority | Agent-facing MCP/HTTP/CLI tools can create, edit, rewrite, move, archive, delete, migrate | Agent writes files directly under type and collection rules, validated afterward |
| Governance | Read-only mode, HTTP read/write API keys, mtime checks, temp-file writes, health report | Git discipline, type specs, validation, semantic review, explicit workflow skills |
| Learning | Folder-centroid adaptation and placement-correction records from move events | Workshop-to-library distillation, reviews, skills, and explicit promotion paths |

engraph is the stronger reference for "make an existing human markdown vault immediately useful to agents." It accepts the vault's existing Obsidian affordances and builds an operational layer around them: ranked search, context bundles, write tools, health checks, and ChatGPT/MCP packaging. Commonplace is more opinionated about the knowledge artifact itself: descriptions, type specs, link labels, review status, register, and validation are part of the primary artifact contract rather than a derived service around a general vault.

The main tradeoff is authority location. In engraph, ranking policy, graph expansion, folder placement, and write workflows live in executable Rust and SQLite state. In commonplace, much of the authority lives in inspectable prose contracts and type-specific documents, with scripts as enforcement or maintenance aids. engraph can serve and mutate a user's vault more ergonomically; commonplace can explain why a note means what it means and how an agent should use it.

## Borrowable Ideas

**Read/write API permission split for agent tools.** Ready to borrow if commonplace ever exposes an HTTP/MCP layer. engraph's read/write key distinction is simple but exactly the right first governance line for a local KB API.

**A derived operational index that does not replace file canonicity.** Ready as an architectural reference, not as an immediate implementation. engraph shows that SQLite/FTS/vector/graph state can remain disposable if the markdown vault is canonical and re-indexing is cheap enough.

**Health diagnostics as agent-callable context.** Ready to borrow. A `context health` tool that reports broken links, orphan notes, stale generated indexes, validation age, and inbox/workshop backlog would give agents a maintenance surface before they start editing.

**Folder-placement feedback from corrections.** Needs a concrete commonplace use case first. The pattern is useful: suggestions are written into frontmatter, user moves become corrections, and future centroids adjust. Commonplace has more semantic placement rules than folder similarity, so the borrowed version would likely train triage hints, not authoritative note type or collection assignment.

**Section-level edit tools with frontmatter preservation.** Ready to borrow for narrow automation. engraph's heading-targeted edit surface is the right granularity for agents updating a note without rewriting the entire artifact, but commonplace would need validation and semantic-review hooks around it.

## Trace-derived learning placement

engraph has a narrow trace-derived learning mechanism in placement feedback, not a general session-transcript learning loop.

**Trace source.** The qualifying source is a filesystem event stream observed by the watcher, especially move events for notes that engraph previously placed or suggested for placement ([`src/watcher.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/watcher.rs)). This is weaker than agent conversation traces, but it is still a tool/action event trace: "the note was suggested for folder X and later appeared in folder Y."

**Extraction.** `detect_correction_from_frontmatter` checks frontmatter for `suggested_folder` plus an engraph-created `created_by` value, compares it with the actual folder after a move, and returns a correction only when the user/agent placement differs from the suggestion ([`src/placement.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/placement.rs)). The oracle is the corrective move itself.

**Storage substrate.** Raw signal is the watcher event plus the moved markdown file. Distilled retained state is stored in SQLite as a `placement_corrections` row and as adjusted `folder_centroids`; temporary `suggested_folder` and confidence frontmatter is stripped after confirmation or correction ([`src/store.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/store.rs), [`src/watcher.rs`](https://github.com/devwhodevs/engraph/blob/ab452322fcac432f6736a1fbc9db967788d01918/src/watcher.rs)).

**Representational form.** The correction record is symbolic; the centroid update is distributed-parametric because it changes future cosine-similarity placement behavior. The frontmatter hint is prose/symbolic metadata while pending, but it is not the durable learned state.

**Lineage.** The lineage chain is suggested placement -> frontmatter hint -> observed move event -> correction row and centroid adjustment. The markdown note remains canonical content; the centroid is a regenerable derived view over vault contents plus corrections, while the correction log preserves the feedback event.

**Behavioral authority.** The correction record is a knowledge artifact when inspected as evidence of prior placement mistakes. The centroid is a system-definition artifact because it influences future folder placement suggestions and therefore where new canonical notes are created.

**Scope and timing.** Scope is per vault and folder structure. Timing is online during `engraph serve` watcher operation and during create/move workflows, not offline survey distillation.

**Survey placement.** On the trace-derived survey axes, engraph is a small instance of event-stream-to-symbolic-and-vector feedback. It strengthens the point that agent memory systems can learn from mundane operational corrections, but it should not be grouped with systems that mine chat transcripts, task trajectories, or benchmark rollouts into generalized lessons.

## Curiosity Pass

**The README is mostly aligned with the code, but counts and freshness claims drift.** The README says 25 MCP tools and 26 HTTP endpoints, while `CLAUDE.md` and the current modules describe 22 MCP tools plus REST routes that have continued to move. More importantly, stale-note detection is advertised but stubbed. The core search/write/index architecture is real; the health story is partially aspirational.

**The graph is valuable because it is modest.** It does not try to infer a rich ontology from notes. It follows wikilinks, mentions, shared tags, and FTS relevance. That restraint is why it can work as a derived index over arbitrary Obsidian vaults.

**The derived database is becoming a control plane.** SQLite starts as an index, but `migration_log`, `identity_facts`, `cli_events`, `placement_corrections`, and `folder_centroids` make it more than disposable search cache. That is fine, but it means backup, migration, and reset semantics matter more than the README's "all local/offline" framing suggests.

**Write tools are powerful enough to need policy.** `read_only` mode and HTTP permissions are good first lines, but section edit, rewrite, delete, migrate, setup, and reindex are all high-authority operations. The system has mechanical safety checks; it does not have content-type contracts or semantic approval gates.

## What to Watch

- Whether stale-note diagnostics become implemented and whether health grows into semantic quality checks or stays structural.
- Whether placement corrections become visible in CLI/MCP context, so agents can explain why a folder suggestion changed.
- Whether multi-vault support appears; the current data directory and config posture are single-vault oriented.
- Whether HTTP/MCP tool counts and OpenAPI stay synchronized as the command surface grows.
- Whether the SQLite state gets export/restore semantics proportional to its growing control-plane role.

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — contrasts: engraph keeps files canonical but relies on a substantial derived database for retrieval and write ergonomics
- [pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: engraph turns docids, snippets, lane scores, graph edges, and context bundles into agent-facing pointers over a vault
- [Context engineering](../../notes/definitions/context-engineering.md) — defined-in: engraph is an operational context-engineering layer over existing markdown notes
- [Retained artifact](../../notes/definitions/retained-artifact.md) — defined-in: separates canonical notes, derived indexes, correction logs, and centroids by behavioral consequence
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) — defined-in: distinguishes read/context tools from write/migrate/ranking tools
- [Napkin](./napkin.md) — compares-with: both adapt Obsidian-style markdown for agents, but Napkin is more CLI/context-output shaped while engraph is a richer local server and derived index
- [CocoIndex](./cocoindex.md) — compares-with: both emphasize derived-index maintenance, but CocoIndex is a general dataflow indexing framework while engraph is a vault-specific agent API
