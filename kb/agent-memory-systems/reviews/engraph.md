---
description: "Engraph review: local Obsidian vault index with hybrid search, MCP/HTTP tools, identity context, and write-placement learning"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-01"
---

# Engraph

Engraph, from devwhodevs' `engraph` repository, is a Rust CLI and local server that turns an Obsidian-style markdown vault into a searchable and writable knowledge API for AI agents. It indexes markdown files into SQLite, exposes hybrid search and context bundles through CLI, MCP, and HTTP surfaces, and adds local llama.cpp-powered query orchestration and reranking when the user opts into the intelligence models.

**Repository:** https://github.com/devwhodevs/engraph

**Reviewed commit:** [f9a95bc96accc792c02ee384d9e6bf768a88c8c8](https://github.com/devwhodevs/engraph/commit/f9a95bc96accc792c02ee384d9e6bf768a88c8c8)

**Last checked:** 2026-06-01

## Core Ideas

**The vault remains the source of truth.** Engraph indexes local markdown files and keeps durable application state under `~/.engraph/`, not inside the vault itself. The README describes the main flow as vault files -> index -> MCP/HTTP/CLI consumers, and the code loads user config, vault profile, model cache, and the SQLite database from `Config::data_dir()` (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/config.rs).

**Search is a fused retrieval plan rather than one vector lookup.** The search path runs semantic vector search, FTS5 keyword search, graph expansion, optional cross-encoder reranking, and temporal scoring, then combines lanes with Reciprocal Rank Fusion. The orchestrator can classify intent, expand the query, and set lane weights; without the optional model it falls back to heuristics (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/search.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/fusion.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/llm.rs).

**Context efficiency is handled by pull-time bundle shaping.** The `context topic` path searches for top matches, includes direct results first, adds one-hop related notes, and trims note bodies against a character budget with docid pointers to full notes (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/context.rs). Person, project, vault-map, section-read, list, and identity surfaces give agents smaller structured views before full-note loading, but the system does not enforce a global token budget across arbitrary `read` calls.

**The integration surface is unusually broad for a local vault tool.** The CLI includes index/search/status/init/identity/configure/context/write/migrate/serve commands; the MCP server exposes read, write, diagnostic, index, identity, setup, and migration tools; and the HTTP server mirrors those operations through an OpenAPI-described REST API with API-key permissions and rate limiting (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/main.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/serve.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/http.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/openapi.rs).

**Write support is not just file output.** Creating a note resolves tags, discovers candidate wikilinks, chooses a folder by type rules or semantic folder centroids, writes atomically, updates the SQLite index, and registers tags; section edits and frontmatter edits preserve narrower targets where possible (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/writer.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/links.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/tags.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/placement.rs).

**Some memory is extracted from the vault, but not from agent conversation traces.** The identity layer extracts active projects, key people, current focus, OOO, and blocking facts from indexed vault notes into `identity_facts`; placement correction learning records when an engraph-created note with a suggested folder is moved elsewhere and adjusts folder centroids (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/identity.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/watcher.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/store.rs). That is durable behavior-shaping state, but the implementation does not mine session transcripts, tool traces, or answer histories.

## Artifact analysis

- **Storage substrate:** `files` — The user's local vault directory
- **Representational form:** `mixed` — Prose markdown with YAML frontmatter, tags, Obsidian wikilinks, headings, tasks, and date-bearing filenames or frontmatter

**Markdown vault.** The storage substrate is the user's local vault directory. The representational form is prose markdown with YAML frontmatter, tags, Obsidian wikilinks, headings, tasks, and date-bearing filenames or frontmatter. Lineage is authored or externally edited source material; Engraph treats these files as the source of truth and rebuilds derived index state from file content, hashes, mtimes, and path changes. Behavioral authority is mostly knowledge artifact authority: notes become evidence, context, and editable material for agents, but a note does not by itself instruct the agent until a tool reads it into context.

**SQLite index and retrieval state.** The storage substrate is `~/.engraph/engraph.db`. The schema stores files, chunks, FTS rows, sqlite-vec embeddings, wikilink/mention edges, tag registry, folder centroids, placement corrections, unresolved links, migration logs, identity facts, CLI events, and cached LLM orchestration results (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/store.rs). The representational form is mixed symbolic and distributed-vector state. Lineage is derived from vault files, local config, model outputs, write operations, and watcher events; reindexing, file changes, model dimension changes, and moves can invalidate or regenerate parts of it. Behavioral authority is system-definition authority for ranking, routing, identity-context assembly, health diagnostics, folder placement, migration rollback, and file resolution.

**Local model cache and LLM outputs.** The storage substrate is `~/.engraph/models/` plus the `llm_cache` table. The representational form is distributed-parametric GGUF model files for embeddings, orchestration, and reranking, with symbolic cached orchestration JSON keyed by query hash (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/llm.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/search.rs). Lineage is model URI configuration and downloaded Hugging Face artifacts, plus per-query local inference results. Behavioral authority is ranking and selection influence: these artifacts decide what candidate material is retrieved or reranked, but they do not directly become prose instructions.

**MCP, HTTP, OpenAPI, CLI, and skill package.** The storage substrate is repository source code plus a bundled skill under `skills/engraph/` and generated/runtime config in `~/.engraph/config.toml`. The representational form is symbolic Rust handlers, JSON schemas, OpenAPI JSON generation, and prose skill instructions (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/serve.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/openapi.rs, https://github.com/devwhodevs/engraph/tree/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/skills/engraph). Lineage is authored system code and user configuration. Behavioral authority is system-definition artifact authority: these surfaces define available operations, permission boundaries, read-only mode, setup flow, and how hosts are told to use the vault.

**Identity facts.** The storage substrate is `[identity]` config for L0 and the `identity_facts` SQLite table for L1. The representational form is prose key-value facts assembled into a compact identity block. Lineage is split: L0 is user-authored config, while L1 is extracted from indexed vault files using deterministic rules for projects, people, recent daily focus, OOO, and blocking items (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/config.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/identity.rs). Behavioral authority is advisory context when an agent or host calls `identity`; it is not automatically injected by Engraph itself.

**Write-placement feedback.** The storage substrate is note frontmatter (`created_by`, `suggested_folder`, `confidence`), folder centroid rows, and placement correction rows. The representational form is symbolic metadata plus vector centroids. Lineage starts from an engraph-created note and a suggested folder; if the user moves it, the watcher detects the correction, updates centroids, logs the correction, and strips suggestion metadata (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/placement.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/watcher.rs). Behavioral authority is future placement influence. This is a small promotion path from a user correction event to ranking-like placement state, but it is not trace-derived learning under this review's tag rule because the source is not an agent/session/tool trace.

**Promotion path.** Engraph's main path is vault markdown -> chunks/embeddings/FTS/edges -> fused search/context bundle -> agent read or write action. A second path is agent-created note -> suggested folder metadata -> user move correction -> adjusted centroids -> later placement decision. Neither path trains model weights; both keep retained state inspectable through files, config, or SQLite.

## Comparison with Our System

| Dimension | Engraph | Commonplace |
|---|---|---|
| Primary purpose | Local vault gateway for search, context, write, identity, and migration tools | Methodology KB framework with typed markdown artifacts, validation, reviews, and source workflows |
| Canonical substrate | User markdown vault plus `~/.engraph/` SQLite/config/model state | Git-tracked `kb/` collections, type specs, indexes, instructions, sources, and reports |
| Retrieval | Hybrid semantic, FTS5, graph, rerank, temporal, and context bundles | Lexical search, authored indexes, links, generated indexes, skills, and review reports |
| Write authority | Agent-facing create/edit/rewrite/delete tools can mutate the vault directly | Agents edit repo artifacts under collection/type contracts and validation |
| Learned state | Folder centroids, placement corrections, identity facts, LLM orchestration cache | Generated indexes, reviews, work reports, validation outputs; no automatic placement model by default |
| Governance | API permissions, read-only mode, health diagnostics, mtime checks, migration preview/undo | Schema/type validation, review gates, git lifecycle, collection routing, semantic QA |

Engraph and Commonplace share a filesystem-first instinct, but they put authority in different places. Engraph treats the vault as external source material and gives agents operational tools over it. Commonplace treats the library itself as the maintained artifact surface: types, collection contracts, generated indexes, reviews, and validation are part of the knowledge system rather than an external index over it.

Engraph is stronger on immediate context assembly. Its search lanes, context bundle budget, person/project/vault-map views, and identity block are designed to give an agent a useful slice of a large vault without reading the whole corpus. Commonplace is more transparent and reviewable, but its default navigation still depends heavily on `rg`, indexes, and agent judgment.

Engraph is weaker on durable artifact governance. It has health checks, mtime conflict detection, API auth, read-only mode, and migration preview/undo, but it does not attach type contracts, review status, semantic validation, or source-level citation requirements to the notes it reads and writes. That is reasonable for a personal Obsidian gateway; it is a poor substitute for Commonplace's library-layer discipline.

**Read-back:** `pull` — From the agent's perspective. Memory enters context when the agent, user, or host explicitly calls search, read, context, identity, MCP, HTTP, or CLI tools; I did not find relevance-gated pre-action injection beyond ordinary tool calls and server instructions

### Borrowable Ideas

**Hybrid retrieval as a front door.** Commonplace could add an optional local index that fuses lexical, vector, link-graph, and temporal signals while still preserving markdown as source of truth. Ready as an experimental search layer; not a replacement for typed artifacts or validation.

**Context bundle commands with hard budgets.** Engraph's `context topic` shape is useful: direct matches first, related one-hop material second, truncation with pointers to full notes. Commonplace could expose similar bundles for reviews, notes, and sources. Ready for read-only commands.

**Identity/current-state block as an explicit tool.** A compact, callable session-orientation artifact is cleaner than always loading a large memory file. Commonplace could provide a project-state or active-workshop block generated from work reports and indexes. Needs careful authority labeling so it remains advisory.

**Placement correction feedback.** Engraph's user-move correction path is a concrete way to learn from operator behavior without mining chat transcripts. Commonplace could use an analogous signal for routing drafts to collections, but only if corrections are auditable and reversible.

**Expose write tools with narrow mutation shapes.** Section edits, frontmatter operations, append, rewrite, archive, and reindex are better agent affordances than "edit the whole file." Commonplace already has some narrow commands; Engraph reinforces making mutation intent explicit.

**Do not borrow direct vault mutation without gates.** Engraph's direct write API suits personal notes, but Commonplace should keep type validation, review gates, and git diffs in the path before durable methodology artifacts gain authority.

## Curiosity Pass

**The "memory" layer is mostly an index plus a few extracted views.** Config has flags for timeline and mining, and the roadmap lists those as future work, but the inspected code implements identity extraction and placement correction learning, not broad automatic memory mining (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/config.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md).

**The read surface is better engineered than the truth surface.** Search, context, and identity are carefully shaped, but note-level truth still comes from whatever markdown the user wrote. That makes Engraph excellent as a vault gateway and less suitable as a governed knowledge-base framework.

**The OpenAPI text overstates one endpoint.** `build_who()` summarizes a person bundle as including "interaction history," but the implementation returns the person note, mentions, and graph connections, not a separate interaction-history substrate (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/openapi.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/context.rs).

**Health diagnostics are partly aspirational.** Broken links and orphans are implemented, but stale-note detection is a stub returning an empty vector, despite the README listing stale content among health diagnostics (https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/health.rs, https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md).

**The most interesting feedback loop is small.** Placement correction learning does not sound as grand as "agent memory," but it is one of the few places where later behavior changes from observed operator action. That makes it more architecturally concrete than roadmap-level mining.

## What to Watch

- Whether timeline and mining become real retained-artifact pipelines or remain configuration flags and roadmap items. That determines whether a future review should add trace-derived or extraction-oriented analysis.
- Whether identity facts gain provenance, freshness policy, and user approval before being treated as session-start context.
- Whether placement corrections become inspectable and editable enough for users to repair bad centroid learning.
- Whether health diagnostics complete stale-note detection and broader tag hygiene, because those checks are the nearest analogue to Commonplace validation.
- Whether the MCP/HTTP write surface adds stronger dry-run, diff, or approval gates for high-impact operations such as rewrite, delete, and migration.
- Whether context bundles move from character budgets to tokenizer-aware budgets aligned with the consuming agent.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Engraph stores and indexes a vault but relies on explicit tool calls for read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: vault files, SQLite index state, model cache, API contracts, identity facts, and placement corrections differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: vault notes and retrieved context mostly serve as evidence, reference, and advisory material.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: MCP tools, HTTP permissions, CLI commands, retrieval ranking, health diagnostics, and placement policy instruct or route behavior.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - relates: Engraph keeps the user's authored vault separate from generated index/model state under `~/.engraph/`.
