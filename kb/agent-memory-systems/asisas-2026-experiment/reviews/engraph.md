---
description: "Engraph review: local Obsidian-vault gateway with hybrid search, MCP/HTTP tools, identity context, and folder-feedback learning"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
---

# Engraph

Engraph, from devwhodevs' `engraph` repository, is a Rust CLI, MCP server, and optional HTTP API that turns a local Obsidian-style Markdown vault into a searchable and writable knowledge surface for AI agents. It keeps the vault on disk as source material, derives SQLite/FTS/vector/graph/model-cache state under `~/.engraph/`, and exposes search, context bundles, identity, health, migration, and note-write operations to Claude Code, ChatGPT Actions, REST clients, and ordinary CLI users.

**Repository:** https://github.com/devwhodevs/engraph

**Reviewed commit:** [f9a95bc96accc792c02ee384d9e6bf768a88c8c8](https://github.com/devwhodevs/engraph/commit/f9a95bc96accc792c02ee384d9e6bf768a88c8c8)

**Source directory:** `related-systems/engraph`

## Core Ideas

**The vault stays local and file-native.** The README describes Engraph as a local binary that indexes Markdown vault files, stores derived state in SQLite with FTS5, vectors, edges, centroids, tags, and an LLM cache, then serves agents through MCP and HTTP ([README.md](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md)). The config loader uses `~/.engraph/` for `config.toml`, `vault.toml`, the database, and model files, while vault notes remain ordinary files that can be edited outside Engraph ([src/config.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/config.rs), [src/indexer.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/indexer.rs)).

**Retrieval is a fused plan, not a single vector lookup.** Search can classify intent, expand the query, run semantic vector search, FTS keyword search, graph expansion, optional reranking, and temporal candidate injection, then combine lanes with Reciprocal Rank Fusion ([src/search.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/search.rs), [src/fusion.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/fusion.rs), [src/llm.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/llm.rs)). The optional local llama.cpp intelligence path caches orchestration JSON by query hash, but heuristic orchestration remains available when intelligence is disabled or fails.

**Context efficiency is pull-time bundle shaping.** `context topic` runs search, includes up to five direct matches, adds one-hop graph neighbors from the top three, and trims bodies to a character budget with docid pointers when direct matches are truncated ([src/context.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/context.rs)). Person, project, vault-map, list, read-section, and identity tools provide smaller structured views before a full note read, but arbitrary `read` calls can still load full note bodies.

**The agent surface is broad and operational.** The CLI exposes index, search, status, clear, init, identity, configure, models, serve, graph, context, write, and migrate commands ([src/main.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/main.rs)). The MCP server exposes read, search, list, context, identity, health, setup, migration, reindex, and write tools with read-only protection for mutating operations, and the HTTP server mirrors those capabilities with API keys, read/write permissions, rate limiting, CORS, OpenAPI, and a ChatGPT plugin manifest ([src/serve.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/serve.rs), [src/http.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/http.rs), [src/openapi.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/openapi.rs)).

**Writes are narrow, indexed, and guarded by local state.** Create, append, metadata update, section edit, rewrite, frontmatter edit, move, archive, unarchive, delete, and reindex paths resolve target notes, check mtimes where relevant, write through temporary files or moves, update SQLite rows, embeddings, FTS rows, tags, links, and graph edges, and can be disabled by read-only mode ([src/writer.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/writer.rs), [src/serve.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/serve.rs)). The create path also resolves tags, discovers candidate wikilinks, applies high-confidence links, chooses a folder by type rule or semantic centroid, and returns the resulting docid and write metadata.

**Some derived memory is learned from vault operations, not from agent traces.** Indexing derives identity facts from current vault files, and the file watcher can detect when an Engraph-created note carrying a suggested folder is moved elsewhere, log the correction, strip suggestion metadata, and adjust folder centroids for future folder choice ([src/identity.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/identity.rs), [src/watcher.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/watcher.rs), [src/placement.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/placement.rs)). I did not find durable extraction from session logs, tool traces, event streams, or trajectories, so this review does not mark Engraph as trace-derived.

## Artifact analysis

- **Storage substrate:** `files` — The durable source-of-truth memory is the user's local Markdown vault and local config/model files; Engraph also maintains derived SQLite tables, sqlite-vec rows, FTS rows, graph edges, folder centroids, identity facts, migration logs, and an LLM cache under `~/.engraph/`, but those are regenerated or auxiliary access/control state rather than the canonical note corpus.
- **Representational form:** `prose` `symbolic` `parametric` — Vault notes, frontmatter, skill guidance, and identity blocks are prose; CLI/MCP/HTTP schemas, config, SQLite rows, FTS indexes, graph edges, docids, tags, migration plans, health reports, and OpenAPI are symbolic; embeddings, sqlite-vec rows, folder centroids, GGUF model files, and reranker/orchestrator outputs are parametric or model-mediated selection state.
- **Lineage:** `authored` `imported` — Vault notes and config are authored or externally edited by users and agents, while index rows, chunks, embeddings, FTS rows, edges, identity facts, health reports, migration previews, model caches, and folder-choice feedback are derived from imported vault files, local model outputs, write operations, and file-watcher observations. I did not find a qualifying trace-extraction pipeline.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Retrieved notes advise agents as knowledge; bundled skills, MCP tools, CLI commands, HTTP schemas, and ChatGPT instructions define operation channels; read-only mode, API-key permissions, mtime checks, migration apply/undo, and write guards enforce boundaries; context tools, resolver logic, migration classification, and folder choice route work; health checks, unresolved-link tracking, and setup diagnostics validate vault state; fused search, reranking, temporal scoring, graph expansion, identity selection, and folder centroids rank attention; user move corrections update later folder choice.

**Vault Markdown.** The vault files are the main knowledge artifacts: Markdown bodies, YAML frontmatter, tags, aliases, headings, date-bearing filenames, wikilinks, and person/project conventions are indexed and later served as note content, sections, snippets, context bundles, and write targets ([src/indexer.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/indexer.rs), [src/context.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/context.rs)). Notes do not become instructions just by existing; they gain behavioral force when an agent deliberately reads or searches them.

**Derived local database.** `Store::migrate()` defines tables for files, chunks, tombstones, LLM cache, edges, folder centroids, tag registry, correction logs, CLI events, unresolved links, migration logs, and identity facts, with sqlite-vec initialized for vector search ([src/store.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/store.rs), [src/vecstore.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/vecstore.rs)). This state has stronger system-definition authority than ordinary notes because it decides search ranking, link expansion, tag resolution, identity extraction, diagnostics, migration rollback, and future folder choice.

**Models and cached inference.** The package depends on llama.cpp bindings, tokenizers, and sqlite-vec, and the README describes a mandatory embedding model plus optional orchestrator and reranker models ([Cargo.toml](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/Cargo.toml), [README.md](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md)). Query orchestration results are cached in `llm_cache`, while embeddings and folder centroids persist as vector state that influences retrieval and future note routing ([src/search.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/search.rs), [src/store.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/store.rs)).

**Tool contracts and adapters.** The CLI command tree, MCP tool router, HTTP route table, OpenAPI builders, plugin manifest, and bundled skill package are authored system-definition artifacts. They instruct compatible hosts which operations exist, where read/write authority starts, how to authenticate, and which mutation shapes are available ([src/main.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/main.rs), [src/serve.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/serve.rs), [src/http.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/http.rs), [skills/engraph/SKILL.md](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/skills/engraph/SKILL.md)).

**Identity and current-state facts.** L0 identity comes from authored config fields; L1 facts are automatically extracted from indexed project tags, people folder importance, recent daily-note focus, OOO hints, and blocking bullets ([src/config.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/config.rs), [src/identity.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/identity.rs)). The identity block is compact advisory context when a host calls the identity tool; Engraph itself does not inject it into every model call.

**Promotion path.** Engraph promotes vault files into chunks, embeddings, FTS rows, docids, wikilink/mention edges, identity facts, context bundles, migration previews, and health reports. A narrower feedback path turns user movement of an Engraph-created note into adjusted folder centroids and correction records. The promotion is mostly inspectable through files, SQLite, and returned JSON rather than through opaque service state.

## Comparison with Our System

| Dimension | Engraph | Commonplace |
|---|---|---|
| Primary purpose | Local gateway over an Obsidian-style vault for search, context, identity, writing, health, and migration | Methodology KB and framework for agent-operated knowledge bases |
| Canonical substrate | User Markdown vault plus `~/.engraph/` derived database/config/model state | Git-tracked `kb/` collections, type specs, validators, source snapshots, reviews, and generated indexes |
| Retrieval | Semantic, FTS, graph, temporal, optional orchestration and reranking, plus context bundles | Lexical search, authored indexes, links, collection contracts, skills, validation, reviews, and reports |
| Write authority | Agents can mutate the vault directly through narrow CLI/MCP/HTTP operations | Agents edit repo artifacts under collection/type contracts, validation, review, and git lifecycle |
| Learned state | Embeddings, folder centroids, query cache, identity facts, and correction-informed folder choice | Generated indexes, review reports, validation outputs, source snapshots, workshop artifacts; no default embedding or folder model |
| Governance | API permissions, read-only mode, mtime checks, health diagnostics, migration preview/undo | Type schemas, collection routing, semantic review, validation gates, citation/source discipline, archive lifecycle |

Engraph and Commonplace share a filesystem-first premise, but their authority boundaries differ. Engraph is a tool layer over a user's existing vault: it indexes, searches, mutates, and reorganizes notes without imposing a methodology-specific type system. Commonplace treats the library itself as the governed artifact surface, so collection contracts, frontmatter schemas, validation, links, and reviews are part of the knowledge system rather than a separate API over it.

Engraph is stronger as an immediate context gateway. Its search lanes, docids, one-hop context bundles, person/project/vault-map views, identity block, and REST/MCP surfaces make a large personal vault easier for agents to query without hand-built navigation. Commonplace is stronger where retained artifacts must carry durable methodological authority, because it requires typed artifacts, source discipline, review state, and validation before claims become part of the maintained library.

Engraph's write surface is also more operational. It has narrow section/frontmatter/edit/move/archive/delete/reindex APIs and local safeguards, but those safeguards are not equivalent to Commonplace's review and validation contracts. That is a good fit for a personal vault assistant; it would be too weak as the only gate for durable methodology notes.

### Borrowable Ideas

**Hybrid search as an optional front door.** Commonplace could add a local index that fuses lexical, vector, link-graph, temporal, and explicit type metadata signals while keeping Markdown and validation as the authority source. Ready as an experimental read-only layer, not as a replacement for curated indexes.

**Budgeted context bundles.** Engraph's direct-match-plus-one-hop bundle is a useful command shape for repeated review, ingest, and source-navigation work. Ready for Commonplace if each included section carries path/source metadata and the command remains advisory.

**Docid-style short references.** Stable short ids can make large vault APIs easier for agents to target after search. Needs a Commonplace-specific use case, because repo paths and links are already meaningful and git-visible.

**Narrow write tools.** Section edits, frontmatter operations, append, archive, unarchive, and reindex are better agent affordances than whole-file rewrite by default. Ready as a design constraint for any future Commonplace write API.

**Operator-correction feedback for routing.** Engraph's user-move feedback suggests a lightweight way to improve draft routing without mining chat transcripts. Needs explicit auditability, reversibility, and validation before Commonplace should let such feedback influence collection choice.

**Do not borrow direct mutation without review gates.** Engraph's direct write APIs suit a local personal vault, but Commonplace should keep type validation, semantic QA, and git diffs in the path before durable methodology artifacts gain authority.

## Write side

**Write agency:** `manual` `automatic` — Users, hosts, and agents manually author and edit vault notes through Markdown editors, CLI, MCP, and HTTP. Engraph automatically indexes changed files, rebuilds chunks/embeddings/FTS/edges, extracts identity facts, records migration and correction logs, updates tag and folder state, and cleans incomplete or orphaned write/index artifacts.

**Curation operations:** `promote` — The implemented feedback path promotes an observed user correction into future folder-choice state by logging the move and adjusting folder centroids. Index rebuilds, embedding refreshes, FTS updates, graph edge rebuilds, and health reports are access-structure or diagnostic upkeep rather than deduplication, consolidation, synthesis, invalidation, or trace-derived learning.

## Read-back

**Read-back:** `pull` — From the agent's perspective, retained vault memory enters context when the agent, user, or host deliberately calls `search`, `read`, `read_section`, `context`, `who`, `project`, `vault_map`, `identity`, CLI commands, MCP tools, or HTTP endpoints. Engraph provides tool descriptions and ChatGPT action instructions that encourage retrieval, but I did not find a built-in hook that automatically pushes retained vault memories into every future model invocation.

Pull paths are explicit and broad: search returns ranked snippets, read returns full note content and graph metadata, context topic assembles a budgeted bundle, identity returns L0/L1 current-state text, and migration/health/status commands expose diagnostic or restructuring state. The API can support a host that chooses to push results to an agent, but that push behavior belongs to the host harness, not to Engraph's deployed loop.

Selection, scope, and complexity are mostly controlled by top-k, explicit tool choice, docids, folder/tag/creator filters, context bundle budget, one-hop graph expansion, read-section targeting, person/project helpers, and read-only/write permission boundaries. Effective use of retrieved context is not tested by Engraph itself; the repository tests mechanics, not with/without behavioral uptake by downstream agents.

## Curiosity Pass

**The most concrete learning loop is small.** The folder-choice feedback path is narrower than the product phrase "vault intelligence," but it is one of the few implemented places where observed operator behavior changes later system behavior.

**The identity layer is extraction, not session memory.** L1 identity facts can be useful startup context, but they come from current vault files and deterministic heuristics. They do not preserve conversation history or learn preferences from previous agent runs.

**Health diagnostics are partly weaker than the README implies.** Orphans, broken links, inbox pending, tag hygiene, and index age are implemented, but stale-note detection currently returns an empty list despite README language about stale content ([src/health.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/health.rs), [README.md](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md)).

**OpenAPI wording overstates one person bundle.** The `getWho` summary mentions interaction history, but the implementation returns the person note, mentions, incoming/outgoing links, and graph context, not a separate interaction-history substrate ([src/openapi.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/openapi.rs), [src/context.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/context.rs)).

**The config has future-memory flags ahead of implementation.** `MemoryConfig` includes timeline and mining fields, and the README roadmap lists timeline and mining as future work, but I did not find implemented fact-mining or timeline graph pipelines beyond identity extraction and temporal search support ([src/config.rs](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/config.rs), [README.md](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md)).

## What to Watch

- Whether timeline and mining become durable retained-artifact pipelines. That would change the lineage and possibly the trace-derived verdict if the inputs include agent/session/tool traces.
- Whether stale-note detection and broader health rules become real validators rather than report fields. That would make Engraph closer to a governed KB layer.
- Whether identity facts gain provenance, freshness, and approval controls before hosts treat them as session-start context.
- Whether folder-choice feedback becomes inspectable and reversible enough for users to repair bad centroid updates.
- Whether MCP/HTTP write operations add dry-run or diff-before-apply modes for high-impact writes such as rewrite, delete, and migration apply.
- Whether context bundles move from character budgets to tokenizer-aware budgets aligned with the consuming model.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Engraph stores and indexes a vault, but memory read-back is explicit tool-mediated pull.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: vault notes, SQLite rows, embeddings, graph edges, model cache, tool contracts, identity facts, diagnostics, and folder feedback carry different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - distinguishes: retrieved notes, snippets, context bundles, identity text, and health reports mostly advise as evidence or context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - distinguishes: CLI commands, MCP tools, HTTP schemas, read-only mode, API permissions, migration apply/undo, and search ranking policy instruct or constrain behavior.
- [Storage substrate](../../../notes/definitions/storage-substrate.md) - relates: Engraph separates source-of-truth vault files from derived local database and model state.
- [Context engineering](../../../notes/definitions/context-engineering.md) - frames: Engraph's main design work is routing selected vault material into bounded agent-facing context surfaces.
