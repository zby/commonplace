---
description: "Continuity review: local-first desktop AI workspace with shared SQLite memory, MCP tools, narrative synthesis, prompt push, and org sync"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Continuity

Continuity, by uziiuzair/Ooozzy, is a local-first Tauri/Next.js AI workspace where chat, canvas, journal, MCP clients, plugins, and a standalone `continuity-memory` MCP server share a local memory database. At the reviewed commit it stores typed/versioned memories, projects, memory links, learnings, and synthesized narratives in SQLite; pushes recent memories and the current narrative into the in-app assistant prompt; exposes memory CRUD/search/project/narrative tools over MCP; and includes an example plugin plus org server for shared team memory sync.

**Repository:** https://github.com/uziiuzair/continuity

**Reviewed commit:** [4ca8f6b4108aa4494e3861ed33c8019dbd662c67](https://github.com/uziiuzair/continuity/commit/4ca8f6b4108aa4494e3861ed33c8019dbd662c67)

**Last checked:** 2026-06-04

## Core Ideas

**The durable memory substrate is one local SQLite file shared by app and MCP server.** The standalone server opens `memory.db` in the platform app config directory, enables WAL mode for concurrent app reads, and initializes tables for projects, memories, versions, links, narratives, and learnings ([server/db/connection.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/connection.ts), [server/db/schema.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/schema.ts)). The Tauri app mirrors that schema through `sqlite:memory.db`, so in-app tools, the Memories UI, and external MCP clients see the same store ([lib/db/memory-db.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/db/memory-db.ts), [providers/memories-provider.tsx](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/providers/memories-provider.tsx)).

**Memory units are small typed records, not freeform notes.** `memories` rows carry a `key`, `content`, type (`decision`, `preference`, `context`, `constraint`, `pattern`), scope (`global` or `project`), optional project id, tags, metadata, source (`user`, `ai`, `system`), soft-delete timestamp, timestamps, and version; updates record history in `memory_versions`, and links record symbolic relationships such as `contradicts` or `supersedes` ([server/db/schema.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/schema.ts), [server/db/memories.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/memories.ts), [server/db/relationships.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/relationships.ts)).

**The app has a two-layer memory model: records plus narrative.** The in-app assistant writes and recalls raw memory rows through `remember`, `recall`, `forget`, `list_projects`, and `get_project`, while `narrative-synthesis` reads all active memories, unabsorbed learning signals, and the previous narrative, calls the configured AI model, saves an updated "mental model" narrative, and marks learning signals as absorbed ([lib/ai/memory-tools.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/memory-tools.ts), [lib/ai/narrative-synthesis.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/narrative-synthesis.ts)). The narrative is refreshed on app launch, after conversation activity, when stale, or when enough unabsorbed learnings accumulate.

**Context efficiency is simple, bounded, and coarse.** Before each in-app model call, Continuity injects at most 50 most-recent memories and caps the memory prompt section at 4,000 characters, grouped by type; it also injects a short current narrative when present ([lib/ai/memory-tools.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/memory-tools.ts), [providers/chat-provider.tsx](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/providers/chat-provider.tsx)). Pull search is `LIKE` over key/content/tags with optional metadata filters and default limits rather than embedding retrieval or graph traversal ([server/db/search.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/search.ts), [server/tools/search-tools.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/tools/search-tools.ts)). This keeps complexity inspectable but makes prompt push mostly recency-based.

**MCP is the external memory interface.** The `continuity-memory` package registers memory, project, search, relationship, lifecycle, and narrative tools over stdio, while the README documents it as a standalone MCP server usable from Claude Code, Cursor, Windsurf, or any MCP-compatible client ([server/index.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/index.ts), [server/package.json](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/package.json), [README.md](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/README.md)). External tools can therefore write memories that the desktop app later pushes into its own assistant prompt.

**The plugin/org-sync path turns local memory into team memory, but the integration looks partly scaffolded.** The example org sync plugin subscribes to memory events, pushes changed memories, periodically pulls remote memories, registers a `search_org_knowledge` tool, and injects a prompt telling the assistant when to search team knowledge ([plugins/continuity-org-memory-sync/src/index.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/plugins/continuity-org-memory-sync/src/index.ts), [plugins/continuity-org-memory-sync/src/sync-engine.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/plugins/continuity-org-memory-sync/src/sync-engine.ts)). The org server itself has authenticated push, pull, and keyword search routes with last-write-wins upsert semantics ([org-server/src/routes/memories-push.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/org-server/src/routes/memories-push.ts), [org-server/src/routes/memories-pull.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/org-server/src/routes/memories-pull.ts), [org-server/src/routes/memories-search.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/org-server/src/routes/memories-search.ts)).

## Artifact analysis

- **Storage substrate:** `sqlite` — The primary behavior-shaping retained state lives in the local `memory.db`; secondary substrates include the app SQLite database for threads/settings, plugin-host runtime state, an optional org-server SQLite store, and generated runtime prompts.
- **Representational form:** `prose` `symbolic` — Memory content, narrative briefings, learning observations, tool descriptions, and injected prompt text are prose; row schemas, types, scopes, tags, source labels, versions, soft-delete fields, relationship types, tool schemas, sync cursors, and plugin capabilities are symbolic. I did not find embedding/vector indexes or model-weight updates in the reviewed memory path.
- **Lineage:** `authored` `imported` `trace-extracted` — Users, the in-app assistant, external MCP clients, and plugins author memory rows; `memory_bulk_import` and org-sync pulls import external rows; learning signals, synthesized narratives, memory prompt sections, version rows, and org-sync change queues are derived from conversation activity or prior retained artifacts.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Memory rows, narratives, links, and UI views advise as knowledge; preloaded memory/narrative prompt sections and plugin-injected prompts instruct the in-app assistant; MCP/project/plugin tool schemas route access; Zod schemas, SQLite checks, auth hooks, manifest validation, and SQL capability checks validate or enforce boundaries; recency ordering, search limits, type grouping, and keyword matching rank what appears; learning rows and narrative synthesis update later behavior.

**Memory rows and versions.** Storage substrate: `memory.db` tables `memories` and `memory_versions`. Representational form: prose content under symbolic keys/types/scopes/tags/source/version fields. Lineage: authored by in-app AI tools, external MCP tools, bulk import, or plugin/database writes; version rows are derived on create/update. Behavioral authority: knowledge when read, instruction-like prompt context when preloaded, and audit/reference through version history.

**Memory links and projects.** Storage substrate: `memory_links` and `projects` tables. Representational form: symbolic relationship and scope records with prose project descriptions. Lineage: authored through MCP/app/plugin operations. Behavioral authority: routing and knowledge organization; links can express contradictions or supersession, but I did not find automatic truth maintenance that acts on those labels.

**Learnings and narratives.** Storage substrate: `learnings` and `narratives` tables. Representational form: prose observations and briefings inside symbolic confidence, scope, version, source-thread, absorbed, and snapshot-hash fields. Lineage: learning rows are trace-extracted when recorded from conversations; narratives are LLM-derived compiled views over memories, unabsorbed learnings, and previous narratives. Behavioral authority: learning input during synthesis and instruction/knowledge when the latest narrative is injected into the assistant prompt.

**Prompt context assembly.** Storage substrate: runtime prompt strings assembled from SQLite rows before each in-app model call. Representational form: prose memory lists, narrative text, and system instructions. Lineage: compiled from active memory rows and latest narrative, capped by count and character budget. Behavioral authority: instruction and context for the receiving model; there is no durable generated prompt file in the reviewed in-app path.

**Standalone MCP server.** Storage substrate: repository code plus the same `memory.db` at runtime. Representational form: symbolic MCP tool contracts and prose tool descriptions/results. Lineage: authored integration surface. Behavioral authority: routing for external agents to read/write/list/search/link/synthesize memory, but the MCP server itself does not push memory into a model prompt.

**Org sync plugin and server.** Storage substrate: local memory DB, plugin sidecar runtime queues, and an org-server SQLite table. Representational form: prose memory content plus symbolic sync payloads, timestamps, versions, API auth, and search results. Lineage: imported/exported memories from local or remote stores. Behavioral authority: knowledge sharing and routing through `search_org_knowledge`; org memory can become instruction-like only when the plugin prompt or host agent chooses to use it.

Promotion path: Continuity's strongest ladder is memory row -> learning signal -> synthesized narrative -> always-injected prompt context. That moves small authored or trace-derived observations toward broader advisory/instruction authority, with snapshot hashes and confidence fields for bookkeeping but no semantic review gate before prompt use.

## Comparison with Our System

| Dimension | Continuity | Commonplace |
|---|---|---|
| Primary purpose | Local-first AI workspace and shared memory server for conversations/tools | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | SQLite memory/narrative row with type, scope, source, version, and links | Typed Markdown artifact with citations, links, validation, and review state |
| Source of truth | Local `memory.db`; org server is optional replicated memory | Repository files; generated indexes/reports are derived |
| Write path | Chat/MCP/plugin writes, versioning, learning records, narrative synthesis, sync | Authored edits, snapshots, review workflows, validation, index refresh |
| Read-back | Always-loaded in-app prompt context plus pull tools/search/UI | Mostly explicit pull through search, indexes, links, skills, and loaded instructions |
| Governance | SQLite constraints, Zod schemas, soft delete, versions, auth hooks, plugin capabilities | Collection/type contracts, schema validation, git diffs, citations, semantic gates |

Continuity is stronger as an adoption surface. It fits a desktop AI workspace, shares memory with MCP clients, and gives the assistant a simple always-present memory context without requiring users to manage files. Commonplace is stronger where claims need durable review: artifacts are readable, cited, diffed, and validated before they become high-authority methodology.

The main tradeoff is activation versus precision. Continuity makes stored memory active by default in the app prompt, which is useful for personal continuity but risks stale or weak memories becoming ambient instruction. Commonplace keeps activation slower and more deliberate because the corpus is meant to preserve transferable methodology rather than personalize a single assistant.

### Borrowable Ideas

**One shared local memory DB for app and external MCP tools.** Needs a concrete Commonplace runtime surface. If Commonplace grows a local service, a single store shared by UI, CLI, and MCP clients would avoid split-brain memory.

**Small typed memories as a capture layer.** Ready as a workshop-layer idea, not as library truth. Continuity's typed rows are useful for low-friction capture before promotion into reviewed notes.

**Narrative as a compiled briefing, not source of truth.** Ready as a constraint. A Commonplace briefing generator could summarize active work, but it should carry source links and be regenerated from durable artifacts.

**Source labels on memories.** Ready now. Distinguishing user-set, AI-inferred, and system-detected memory is a simple authority cue that could help Commonplace review candidate notes or work logs.

**Always-load memory needs strict budgets and provenance.** Ready as a warning. Continuity's 50-memory/4,000-character cap is pragmatic, but Commonplace would need stronger selection and citations before pushing notes into every agent call.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come through in-app `remember`/`forget`, MCP memory/project/link/narrative tools, UI refresh/synthesis controls, bulk import, plugin database writes, and org sync configuration; automatic writes include version rows, soft-delete timestamps, scheduled narrative synthesis, learning absorption flags, app-launch/conversation-triggered synthesis checks, prompt-context compilation, and plugin/org sync push-pull cycles.

**Curation operations:** `consolidate` `synthesize` `evolve` `promote` — Narrative synthesis consolidates many memories and learnings into a compact briefing; it synthesizes a new or updated mental-model artifact; memory and narrative updates evolve existing rows by version/snapshot/confidence; absorbed learning signals and the latest narrative are promoted into the in-app assistant's future prompt context.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` — Continuity records learning signals with source thread/message ids, schedules narrative synthesis after conversation activity, and lets plugins subscribe to memory-change events.

**Learning scope:** `per-project` `cross-task` — Memory rows and narratives can be global or project-scoped, and the global prompt injection carries memory across later conversations in the same local workspace.

**Learning timing:** `online` `staged` — Memory writes and learning records can happen during conversations; narrative synthesis is staged on launch, after a debounce, when stale, or when enough unabsorbed learning signals accumulate.

**Distilled form:** `prose` `symbolic` — Raw memory and learning observations become prose narrative briefings and symbolic sections/confidence/version/snapshot metadata. There is no parametric distilled artifact in the reviewed code path.

**Extraction.** The code exposes `learning_record` as the explicit trace-signal write path and `synthesizeNarrative()` as the distillation step. The synthesis prompt tells the model to combine all stored memories, new learnings, and the previous narrative, preserve old learnings, treat user-set memories as ground truth, and frame AI-inferred memories as hypotheses.

**Scope and timing.** The durable learning unit is a row in `learnings`; the durable distilled unit is the latest row in `narratives` for a scope/project. Synthesis is skipped when the snapshot hash has not changed and no learnings are pending, and learnings are marked absorbed after a successful save.

**Survey fit.** Continuity is a clean example of trace-derived memory where the raw trace artifacts are already structured observations, not full transcripts. Its design strengthens the distinction between a capture layer and a compiled behavior-shaping briefing.

## Read-back

**Read-back:** `both` — Continuity is pull through in-app `recall`, MCP `memory_read`, `memory_search`, project/list/link/narrative tools, Memories UI, and org search; it is push in the desktop app because `buildSystemPrompt()` loads stored memories and the latest narrative before the next in-app model call.

**Read-back signal:** `coarse` — The pushed app prompt uses most-recent active memories up to a count/character cap and the latest narrative for the scope, not instance-specific lexical, embedding, identifier, or judgment targeting.

**Faithfulness tested:** `no` — I found code and tests for storage/sync/search mechanics, especially org-server push/pull/search routes, but not a behavioral ablation showing that preloaded memories or narratives change downstream model behavior correctly.

**Direction edge cases.** MCP memory tools are pull even if a host agent calls them proactively; the server exposes capabilities, not a prompt hook. The in-app `recall` tool is pull. The in-app memory/narrative prompt sections are push because the receiving model gets them before deciding whether to search memory.

**Targeting and signal.** Push targeting is coarse recency plus current narrative. Pull targeting supports exact key/id/project lookups, scope/project/type/tag filters, relationship traversal by memory id, and `LIKE` keyword search over key/content/tags. The org-server search route mirrors the same lexical design.

**Injection point.** Read-back push happens during `buildSystemPrompt()` before the assistant model call. The scheduled synthesis after conversation activity is write-side maintenance for later prompts, not post-action read-back.

**Selection, scope, and complexity.** Prompt push is bounded by `MAX_MEMORIES_IN_PROMPT = 50` and `MAX_PROMPT_CHARS = 4000`, grouped by type and ordered by update time. Narrative push is shorter but broader, because it is a model-generated summary of all current memories plus absorbed learnings. Pull search defaults to bounded result sets and has simple filters, so retrieval is inspectable but semantically shallow.

**Authority at consumption.** Pull results are advisory knowledge unless the caller inserts them into a prompt. Pushed memory context explicitly tells the assistant to use stored memories silently to personalize behavior, and the workspace prompt calls preloaded memories the assistant's primary context. That gives local memory soft instruction force without a hard gate.

**Other consumers.** Humans consume memory through the Memories page, detail view, project tabs, version timeline, and connect modal. Plugins and org-server clients consume memory through database APIs, events, HTTP push/pull/search routes, and registered plugin tools.

## Curiosity Pass

**The README's "12 tools" claim lags the server code.** At this commit the server logs 17 registered tools and includes narrative/learning/project/link/lifecycle surfaces, so the implemented memory server is already more than CRUD plus search.

**The most behaviorally important path is not MCP search.** The always-loaded app prompt makes memory active even when the model never calls `recall`; MCP clients only get that behavior if their host adds its own prompt-loading policy.

**Narrative synthesis is local-first but model-dependent.** The store is local SQLite, but the compiled narrative depends on whichever configured AI provider generates the JSON briefing.

**Links can express contradictions, but nothing resolves them.** `contradicts` and `supersedes` are useful symbolic labels, yet retrieval and prompt assembly do not appear to use them to suppress stale memories.

**Org sync demonstrates portability and authority risk together.** A remote team's memory can enter local search and, through plugin prompt guidance, influence the assistant, but the reviewed path has last-write-wins sync rather than semantic conflict review.

## What to Watch

- Whether prompt push gains instance-specific selection beyond recency; that would move Continuity from coarse ambient memory toward targeted contextual activation.
- Whether `memory_links` labels start affecting retrieval or prompt assembly; that would turn relationships from UI/reference metadata into routing or invalidation authority.
- Whether narrative synthesis gets citation/source ids in the generated briefing; without them, compiled mental models can drift from the rows that produced them.
- Whether plugin-registered prompts/tools are fully surfaced into the frontend state; that determines how operational the org-sync plugin's injected context is in ordinary app use.
- Whether FTS5 or embeddings replace `LIKE` search; that would improve recall breadth but add a less inspectable ranking layer.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Continuity stores memory in SQLite, but only prompt assembly, tool calls, UI browsing, and plugin/org-sync paths activate it.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: memory rows, versions, links, learnings, narratives, prompts, and sync payloads carry different lineage and authority.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: memory rows, links, narratives, search results, and UI views mostly advise as evidence or context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: preloaded memory prompt sections, workspace prompt rules, MCP schemas, plugin prompts, and validation schemas shape later behavior more strongly.
- [Keep Lineage And Compiled Views From Drifting](../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) - warns: Continuity narratives are compiled views over memories/learnings and need source alignment if their authority increases.
- [Use Trace-Derived Extraction As Meta-Learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Continuity distills learning signals and memories into a future-facing narrative briefing.
