---
description: "AI Context OS review: file-first desktop memory layer with L0/L1/L2 routing, MCP adapters, heuristic scoring, observability, and governance suggestions"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-03"
---

# AI Context OS

AI Context OS, distributed as MEMM from Alex DC's `alexdcd/AI-Context-OS` repository, is a Tauri desktop application that turns a local workspace folder into a file-first memory layer for AI tools. The inspected public snapshot implements Markdown memory CRUD, generated adapter files, MCP stdio/HTTP servers, chat-context assembly, deterministic scoring, graph visualization, governance checks, inbox proposals, and SQLite-backed observability; it is not only a README-level concept.

**Repository:** https://github.com/alexdcd/AI-Context-OS

**Reviewed commit:** [f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5](https://github.com/alexdcd/AI-Context-OS/commit/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5)

**Last checked:** 2026-06-03

## Core Ideas

**Files are the canonical memory substrate; SQLite is support state.** The root README and operating-model docs explicitly separate canonical Markdown memories, journal pages, tasks, rules, router artifacts, and scratch files from `.cache/observability.db`, which stores telemetry and optimization suggestions but not memory content. The Rust code reflects that split: memory CRUD reads and writes Markdown with YAML frontmatter, while `ObservabilityDb` creates SQLite tables for context requests, served memories, not-loaded memories, health history, and optimizations ([README.md](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/README.md), [docs/Memm wiki/architecture-and-operating-model.md](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/docs/Memm%20wiki/architecture-and-operating-model.md), [src-tauri/src/core/memory.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/memory.rs), [src-tauri/src/core/observability.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/observability.rs)).

**The retained unit is a tiered Markdown memory.** A memory carries `id`, `type`, `l0`, importance, tags, links, skill dependencies, protection, status, and lineage fields in frontmatter, then splits body text into `<!-- L1 -->` and `<!-- L2 -->` sections. The scanner ignores bare Markdown, skips transient/system directories, tolerates unknown enum values, and enriches records with path-derived `folder_category` and `system_role` rather than serializing those into the canonical file ([src-tauri/src/core/types.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/types.rs), [src-tauri/src/core/levels.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/levels.rs), [src-tauri/src/core/index.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/index.rs), [src-tauri/src/core/paths.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/paths.rs)).

**Context efficiency is the central design mechanism.** `execute_context_query` scores all memories, seeds graph proximity from the first pass, applies skill dependency force-loads and optional boosts, then greedily chooses L2 for only the top cluster, L1 for relevant or forced memories, and L0-only references for lower-confidence candidates inside a token budget. The chat package omits the MCP prelude and includes only loaded memory content, while the MCP package includes rules plus loaded and available-but-unloaded memories ([src-tauri/src/core/engine.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/engine.rs), [src-tauri/src/core/scoring.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/scoring.rs), [docs/algorithms-and-scoring.md](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/docs/algorithms-and-scoring.md)).

**Retrieval is deterministic, hybrid, and intentionally non-embedding.** The active implementation uses English/Spanish tokenization, Snowball stemming, BM25, tag and L0 overlap, ontology/system-role bonuses, intent-specific weights, access frequency, recency, and graph proximity. Graph edges come from `requires`, `related`, `optional`, wikilinks, and tag overlap; Personalized PageRank then contributes to scoring. The docs mention embeddings as future work, not the active retrieval core ([src-tauri/src/core/search.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/search.rs), [src-tauri/src/core/scoring.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/scoring.rs), [src-tauri/src/core/graph.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/graph.rs), [src-tauri/Cargo.toml](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/Cargo.toml)).

**Adapters are derived views, not the source of truth.** Router generation scans canonical memories into a manifest, then writes `claude.md`, `.cursorrules`, `.windsurfrules`, `.ai/index.yaml`, and `.ai/catalog.md`. The MCP prelude is rendered separately from the static router, and filesystem commands block direct mutation of generated artifacts and protected memories ([src-tauri/src/core/router.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/router.rs), [src-tauri/src/core/compat.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/compat.rs), [src-tauri/src/commands/router.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/router.rs), [src-tauri/src/commands/filesystem.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/filesystem.rs)).

**Governance is observable and advisory, not an automatic rewrite loop.** Conflict checks, decay candidates, scratch TTL, consolidation suggestions, health scores, and optimization records surface memory-quality work. Usage traces can produce pending suggestions such as compressing large L1 sections, archiving unused memories, promoting importance, downgrading to L1, removing decayed entries, merging tag-overlapping records, or nudging near-threshold memories. Applying an optimization currently updates its status rather than editing the target memory, so the governance layer is a work queue rather than autonomous repair ([src-tauri/src/core/governance.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/governance.rs), [src-tauri/src/core/health.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/health.rs), [src-tauri/src/core/optimizer.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/optimizer.rs), [src-tauri/src/commands/observability.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/observability.rs)).

## Artifact analysis

- **Storage substrate:** `files` — Canonical memory, task, journal, rule, skill, source, scratch, router, adapter, index, catalog, inbox, and proposal artifacts live as workspace files; SQLite and JSON cache files support observability and usage but do not replace the file tree as the memory source of truth.
- **Representational form:** `prose` `symbolic` — The central artifacts combine prose Markdown memory content with symbolic YAML frontmatter, generated route/index records, Rust scoring logic, SQLite trace tables, JSON proposal records, and tool schemas.
- **Lineage:** `authored` `imported` `trace-extracted` — Memories are authored by users or the app, imported through inbox/source proposals, and trace-extracted through context-serving logs, usage records, session events, and optimizer suggestions.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Memories act as knowledge when retrieved, rules/adapters/context packages instruct and route agents, protected/generated paths enforce boundaries, governance validates, scoring ranks, and trace-derived optimizations advise future maintenance.

**Canonical memory files.** Storage substrate: Markdown files under the workspace, excluding transient or system-managed directories where the scanner says they do not participate. Representational form: mixed prose body plus symbolic frontmatter. Lineage: authored by the human, written through the app, saved through MCP, imported from inbox proposals, or routed to `sources/`; derived fields such as `folder_category`, `system_role`, access count, and last access are injected at scan time rather than serialized into the canonical file. Behavioral authority: knowledge artifacts when searched or opened as background; system-definition artifacts when `system_role = rule` or `skill`, when dependency fields force-load related memories, when the chat or MCP context engine injects them, or when `protected` prevents direct mutation.

**Generated router and adapter artifacts.** Storage substrate: workspace files `claude.md`, `.cursorrules`, `.windsurfrules`, `.ai/index.yaml`, and `.ai/catalog.md`. Representational form: mixed prose instructions, Markdown indexes, and YAML-like structured data. Lineage: derived from the current scan manifest and regenerated by router commands or memory operations. Behavioral authority: system-definition artifacts for agents that receive static adapters as workspace instructions or use the generated index/catalog for routing; knowledge artifacts for humans inspecting the memory roster. Their generated status and filesystem protection reduce accidental drift but do not prove the consuming tool will actually follow the instructions.

**Context-query result packages.** Storage substrate: in-memory during chat, simulation, and MCP calls; selected memory IDs also become usage records. Representational form: symbolic score/load-level records plus prose prompt packages. Lineage: derived at request time from the current file scan, query text, scoring weights, graph proximity, skill dependencies, and token budget. Behavioral authority: system-definition artifacts when inserted into an LLM call as the current context frame; the same result is a knowledge artifact when shown in simulation or observability UI.

**MCP tools and chat-provider bridge.** Storage substrate: Rust code and Tauri command/API surfaces. Representational form: symbolic tool schemas and runtime code with prose descriptions. Lineage: authored implementation. Behavioral authority: system-definition artifacts because `get_context`, `save_memory`, `get_skill`, `log_session`, `build_chat_context`, and `chat_completion` define the routes by which memory is read, written, logged, and injected into future model calls ([src-tauri/src/core/mcp.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/core/mcp.rs), [src-tauri/src/commands/scoring.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/scoring.rs), [src-tauri/src/commands/inbox.rs](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/src-tauri/src/commands/inbox.rs)).

**Observability, usage, and optimization records.** Storage substrate: SQLite in `{workspace}/.cache/observability.db` plus `.cache/memory-usage.json`. Representational form: symbolic rows and JSON entries. Lineage: context requests, served/not-loaded memories, usage reads, health computations, and optimizer runs. Behavioral authority: knowledge artifacts as audit and dashboard evidence; system-definition candidates when optimization records advise memory compression, archive, promotion, merge, or threshold changes. The current `apply_optimization` path marks a row as applied, so a human or later workflow must still perform the actual memory edit.

**Inbox captures and ingest proposals.** Storage substrate: `inbox/` Markdown files, `.ai/ingest/manifest.json`, and `.ai/proposals/*.json`. Representational form: mixed prose capture content, symbolic frontmatter, JSON manifests, and optional LLM-generated proposal fields. Lineage: captured text/link/file material, duplicate heuristics, or provider-generated JSON proposals over the captured item. Behavioral authority: knowledge artifacts while pending; system-definition artifacts only after an accepted proposal writes a canonical memory/source and regenerates router artifacts.

The promotion path is explicit but only partly automated: raw captures become proposals, proposals can become canonical memories or protected sources, canonical memories are scanned into route/index artifacts, query-time selection injects some of them into chat or MCP responses, and usage traces can produce governance suggestions. The system is strongest where the authority boundary is symbolic and visible; it is weaker where a suggestion says "consider" but no reviewed edit, proof, or ablation establishes that the change should become durable policy.

## Comparison with Our System

| Dimension | AI Context OS | Commonplace |
|---|---|---|
| Primary purpose | Desktop memory layer for AI tools and personal/workspace context | Methodology KB and framework for agent-operated knowledge bases |
| Canonical substrate | User workspace Markdown files, with generated adapters and local support state | Git-tracked typed Markdown collections, schemas, commands, indexes, and reviews |
| Context selection | Deterministic scoring, graph proximity, L0/L1/L2 loading, chat injection, MCP tools | Mostly lexical search, authored indexes, skills, collection contracts, and validation; generated indexes support navigation |
| Governance | Runtime observability, health score, heuristic checks, pending optimizations | Type specs, validation, semantic review gates, source citations, status/replacement conventions |
| Integration surface | Tauri UI, local chat, MCP stdio/HTTP, generated tool adapters | CLI commands, skills, repo files, review workflows |

The strongest alignment is the file-first bet. AI Context OS makes the same architectural move Commonplace defends: use inspectable files as source of truth and derived indexes/adapters for capabilities that raw files do not provide. It also shares the progressive-disclosure instinct: summaries and indexes route first, full detail loads only when justified.

The main divergence is the activation layer. AI Context OS implements a runtime context engine with scoring, budgets, adapter generation, MCP, chat injection, and observability. Commonplace is more conservative and review-driven: a note's authority usually comes from its type, placement, validation, citation discipline, and explicit loading by an agent or skill. AI Context OS is more productized and ergonomic for a user's live tools, but its generated suggestions and prompt-active context have lighter semantic governance than Commonplace would normally require before an artifact changes durable behavior.

Another difference is where structured state earns its place. Commonplace mostly keeps structured indexes and review state as repo artifacts or scoped SQLite exceptions. AI Context OS keeps canonical knowledge in files but uses SQLite for request telemetry, memory-serving history, health snapshots, and optimization work queues. That is a reasonable scoped database exception: the access pattern is operational time-series state, not authored knowledge.

**Read-back:** `both` — MCP `get_context`, `get_skill`, static files, simulation, and file navigation are pull surfaces, while the app's chat path can auto-assemble selected vault context from the latest user turn and inject it before the provider call; generated static adapters also provide coarse always-present memory/routing context for tools that load them.

### Borrowable Ideas

**Use support databases for operational traces, not canonical knowledge.** Commonplace already has a scoped review-state exception; AI Context OS is a useful parallel for context-request telemetry and optimization queues. Ready when Commonplace has a recurring runtime context engine to observe.

**Make context selection explainable at the artifact level.** AI Context OS records load level, score breakdowns, token budget, served memories, and not-loaded reasons. Commonplace could borrow that for generated context packs: show what was eligible, what loaded, and why. Ready for any future context-pack command.

**Treat generated adapters as derived products with protection.** The router/adapter pattern cleanly separates canonical files from `claude.md`/`.cursorrules`/`.windsurfrules`. Commonplace already treats indexes as generated; the same protection stance should apply to any future generated AGENTS or prompt-pack artifacts.

**Keep L0/L1/L2 as a product UX, not just a writing convention.** AI Context OS makes tiered summaries visible in retrieval, chat, and simulation. Commonplace has descriptions and indexes but does not yet expose a first-class tiered loading contract for arbitrary notes. Needs a concrete context engine before broad adoption.

**Do not borrow status-only "apply" for high-authority changes.** Marking an optimization as applied without the edit is fine as a UI queue action, but Commonplace should keep acceptance tied to a changed artifact, validation result, or review event.

## Trace-derived learning placement

- **Trace source:** `session-logs` `tool-traces` `event-streams` — The review identifies session events, MCP context-serving traces, served/not-loaded memory events, access telemetry, daily inbox/proposal events, and provider/chat debug context.
- **Learning scope:** `per-project` `cross-task` — Trace-derived governance is workspace-local and uses usage across context requests to produce future maintenance suggestions.
- **Learning timing:** `online` `offline` — MCP serving, skill loading, access tracking, and session logging happen online; optimization extraction is offline or user-triggered.
- **Distilled form:** `prose` `symbolic` — Distilled outputs are maintenance suggestions with prose recommendations recorded as symbolic optimization rows or proposal records.

**Trace source.** AI Context OS qualifies as trace-derived learning, but in a modest governance-advisory form. Raw traces include MCP context requests, served memories, not-loaded memories, access counts, last-access times, session events written through `log_session`, daily inbox/proposal events, and provider/chat debug context. Structured MCP traces are logged to SQLite; memory access telemetry is kept in `.cache/memory-usage.json`; session and daily events live under `.ai/journal/`.

**Extraction.** The clearest extraction path is `run_optimizations`: it reads usage statistics, unused-memory records, recent not-loaded rows, memory token sizes, tags, and decay scores, then emits pending `OptimizationRecord` rows. The extracted suggestions are mostly maintenance candidates, not new operating rules: compress an oversized L1, archive an unused low-importance memory, promote frequently served low-importance memory, downgrade repeated L2 loads to L1, remove decayed low-importance memory, merge high tag-overlap memories, or nudge near-threshold memories. Inbox proposal generation is a separate source-ingestion loop over captured items; it may use an LLM provider, but it is source-derived rather than trace-derived unless the captured item is itself a session record.

**Scope and timing.** Scope is workspace-local. Logging happens online during MCP context serving and skill loading; optimization extraction is offline or user-triggered through the observability command. The current docs note an observability asymmetry: MCP context requests are logged structurally, while the chat path has context debug and auto-assembly logs but does not yet write the same `origin="chat"` request rows ([docs/chat-context-pipeline-architecture.md](https://github.com/alexdcd/AI-Context-OS/blob/f50f6ad42e7b2fbcc61697017b1dcbaf299f1ef5/docs/chat-context-pipeline-architecture.md)).

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), AI Context OS belongs in the trace-to-governance-candidate family. It strengthens the survey's capture-versus-activation split: traces are retained as audit and optimization evidence, but the distilled output remains pending advice until a consumer performs or automates the edit. It is weaker than systems that distill traces into prompt-active playbooks, validators, or model updates.

## Read-back placement

**Direction.** AI Context OS uses both pull and push over retained memory. Pull is explicit through MCP `get_context`, MCP `get_skill`, app simulation, memory CRUD, generated indexes, and direct file navigation. Push appears in the local chat path: if vault context is enabled and no context prompt arrives from the frontend, `chat_completion` queries the engine on the latest user message, assembles a context prompt, and prepends it to the provider conversation. Static adapter files are also a coarse push surface when a host tool always loads them.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` — Static adapters are coarse always-present memory/routing context, skill dependency force-loads key on visible dependency IDs, and chat auto-assembly uses lexical/heuristic relevance from the latest user turn.

**Read-back timing:** `pre-action` — Chat, MCP context packages, and static adapters are assembled before the provider or receiving agent acts.

**Faithfulness tested:** `no` — The review found exposure/observability records but no per-memory behavioral ablation showing that loaded memory changed a model action.

**Targeting and signal.** The engineered push path is `instance` targeted with an `inferred / lexical` signal, broadened by symbolic metadata and graph structure. The current user turn supplies the query; BM25, query expansion, tag/L0 overlap, ontology bonus, recency, importance, access frequency, and PPR graph proximity rank memories; token budget then chooses L1 or L2. Skill dependency force-loads use an `identifier` signal once a scored skill's `requires` or `optional` IDs are visible. Static adapters are `coarse`: they always expose the memory roster and reading rules, not a specific instance's relevant content.

**Timing relative to action.** Chat and MCP context packages are assembled before the provider or receiving agent acts, so they can change the next response. Observability rows, memory-usage updates, daily logs, and optimization records are written after context serving or user actions; they affect future behavior only when later retrieval, router generation, or maintenance workflows consume them.

**Selection, scope, and complexity.** Selection is workspace-scoped and budgeted. The implementation caps L2 loading to at most three top-cluster memories, lets L1 carry mid-relevance or forced dependencies, and keeps L0-only memories as available-but-unloaded references. This reduces token volume and some complexity, but the retrieval model is lexical/heuristic rather than embedding or judgment-based; precision, recall, and context dilution are runtime qualities, not verified by static code.

**Authority at consumption.** In MCP responses, active rules are placed in the prelude and loaded memories become task context. In chat, context is inserted as a `user` message before conversation history, which is advisory in API role terms but likely high-salience in practice. Generated adapter files carry instruction/routing authority for tools that load them. Served memory records and simulation views are knowledge artifacts unless their selected content enters a live prompt.

**Faithfulness.** AI Context OS records what was served, what was not served, tokens used, scores, and health signals, but I did not find a per-memory behavioral faithfulness test showing that a loaded memory changed a model action. Observability proves exposure and enables debugging; it does not prove use.

**Other consumers.** Humans consume the Explorer, Simulation, Graph, Governance, Observability, Settings, and Connector views. Those UI consumers are important: the system is not only an agent-facing API but a human-operated maintenance console for deciding which memories and optimization suggestions deserve durable authority.

## Curiosity Pass

**The public snapshot is coherent but self-described as incomplete.** The README says the repository is an older public snapshot while active development continues privately. That matters for review freshness: the code is readable and implemented, but not necessarily representative of the current private system.

**The docs are unusually honest about capability boundaries.** The architecture docs distinguish MCP progressive loading from static-file conventions, canonical memory from observability state, router artifacts from source of truth, and implemented features from future ingestion/autonomy. That reduces the usual README inflation risk.

**The chat fallback is a useful push pattern with an observability gap.** Backend auto-assembly prevents empty context when the frontend forgets to build it, but the chat-context architecture note says MCP logging is still the only structured context-request observability path. The system knows this is debt.

**"Zero Gravity" is less absolute than the phrase sounds.** User folders do not determine semantic classification, but `.ai/rules`, `.ai/skills`, inbox, sources, tasks, scratch, generated artifacts, and folder contracts still have path-based operational semantics. That is not a contradiction; it is the necessary system boundary around otherwise free user folders.

**The optimizer currently recommends more than it can enforce.** Suggestions such as compressing L1 or merging memories are valuable, but without an edit-producing apply path they remain maintenance prompts. That is appropriate for safety; it also means trace-derived learning stops short of durable self-improvement.

## What to Watch

- Whether chat context serving gains the same structured observability as MCP. That would make trace-derived governance reflect all memory read-back paths instead of only MCP.
- Whether optimization "apply" evolves from status marking into guarded edits with previews, diffs, rollback, and router regeneration. That would move trace-derived suggestions from advisory records toward system-definition changes.
- Whether folder contracts become enforcing rather than warning-only for required fields. That would clarify the boundary between user freedom and typed memory guarantees.
- Whether the embedding roadmap is implemented as an optional derived index rather than replacing file-readable memory as the canonical substrate.
- Whether static adapters stay coherent as MCP integrations expand. If generated adapters become stale relative to live MCP semantics, the no-MCP fallback path will lose trust.

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - aligns: AI Context OS keeps authored memory in files and uses databases only for scoped operational state.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: L0/L1/L2 selection, token budgets, and generated routers make context cost the central design variable.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - addresses: AI Context OS explicitly routes stored memory back into chat, MCP, and static adapters.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - exemplifies: static adapters and skill dependencies key on symbols, while query-time chat push uses inferred lexical relevance.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - partial: AI Context OS mines usage traces into maintenance suggestions but keeps them advisory.
- [Preserve evidence without making history the next context](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: observability traces and usage logs are retained for governance without automatically loading raw history into every prompt.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the system's files, generated routers, prompt packages, telemetry rows, and optimizer records need separate substrate/form/lineage/authority treatment.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: router artifacts, rules, skills, context assembly, and scoring code shape future behavior with instruction or routing force.
