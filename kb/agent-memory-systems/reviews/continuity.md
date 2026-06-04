---
description: "Continuity review: local-first AI workspace with shared SQLite memory, MCP tools, prompt preloading, narrative synthesis, and plugin/org sync"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-03"
tags: [trace-derived]
---

# Continuity

Continuity, by uziiuzair/Ooozzy, is a local-first desktop AI workspace where chat is the main write path for workspace memory. At the reviewed commit, the memory architecture is not only a UI feature: the app and standalone MCP server share a local `memory.db`, the in-app assistant preloads recent memories and synthesized narrative state into its system prompt, and plugins can add organization-level sync and search surfaces.

**Repository:** https://github.com/uziiuzair/continuity

**Reviewed commit:** [4ca8f6b4108aa4494e3861ed33c8019dbd662c67](https://github.com/uziiuzair/continuity/commit/4ca8f6b4108aa4494e3861ed33c8019dbd662c67)

**Last checked:** 2026-06-03

## Core Ideas

**The core memory substrate is shared local SQLite.** The desktop app opens `sqlite:memory.db` through the Tauri SQL plugin, while the standalone `continuity-memory` MCP server opens the same platform-specific app config database with `better-sqlite3` ([lib/db/memory-db.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/db/memory-db.ts), [server/db/connection.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/connection.ts)). Both schema definitions create `memories`, `memory_versions`, `memory_links`, `projects`, `narratives`, and `learnings`, making the app and external MCP clients share one source of truth rather than parallel memory stores ([server/db/schema.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/schema.ts)).

**Memories are typed records with versioning and soft deletion.** The central record is a keyed memory with content, type (`decision`, `preference`, `context`, `constraint`, `pattern`), scope (`global` or `project`), optional project id, tags, metadata, source, archived timestamp, and version. Updates upsert by key/scope/project, bump the version, and write to `memory_versions`; deletes set `archived_at` rather than removing the row ([server/db/memories.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/memories.ts), [lib/db/memories.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/db/memories.ts)). This gives the system a modest governance surface: history exists, but there is no reviewer state or validation gate on memory content.

**The same memory is exposed through in-app tools and MCP tools.** The in-app assistant has `remember`, `recall`, `forget`, `list_projects`, and `get_project`; the standalone server registers memory, project, search, relationship, lifecycle, narrative, and learning tools over stdio MCP ([lib/ai/memory-tools.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/memory-tools.ts), [server/index.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/index.ts)). First-launch setup can add `npx continuity-memory` to Claude Code's global MCP config, which is an adoption affordance: other tools can use the same database without the full desktop app ([lib/mcp-auto-setup.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/mcp-auto-setup.ts), [server/package.json](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/package.json)).

**Read-back is a coarse prompt preload plus explicit search.** `buildSystemPrompt()` loads a synthesized narrative if present, then loads recent memories via `getMemoryContext()`, and includes both ahead of the tool instructions on every in-app chat request ([providers/chat-provider.tsx](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/providers/chat-provider.tsx)). Context efficiency is handled by blunt caps: up to 50 most-recent memories and about 4000 prompt characters, grouped by type, plus explicit `recall`/`memory_search` when the model needs more ([lib/ai/memory-tools.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/memory-tools.ts), [server/db/search.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/search.ts)). This constrains volume but not semantic relevance or complexity: global and project memories are mixed in the preload, and search is `LIKE` over key/content/tags, not embeddings, FTS, or graph traversal.

**Narrative synthesis is a second memory layer.** The app-side synthesis engine reads all non-archived memories, unabsorbed learnings, and the previous narrative, asks the configured AI client for a 2-4 paragraph "mental model" JSON object, writes it to `narratives`, stores a snapshot hash, and marks learnings absorbed ([lib/ai/narrative-synthesis.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/narrative-synthesis.ts)). Synthesis runs at app launch, after conversation activity, or once enough unabsorbed learnings accumulate; the resulting narrative has stronger prompt authority than the raw records because it is injected as "What I Know About You" before each future response.

**Plugins can extend memory authority outside the local user.** The plugin system lets sidecar processes register tools, inject prompt segments, access the database, and subscribe to events through a localhost WebSocket host ([plugin-sdk/README.md](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/plugin-sdk/README.md), [lib/ai/plugin-tools.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/plugin-tools.ts)). The official org memory sync example queues local memory changes, pushes and pulls against an org server, registers `search_org_knowledge`, and injects a prompt telling the AI when to use shared team knowledge ([plugins/continuity-org-memory-sync/src/index.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/plugins/continuity-org-memory-sync/src/index.ts), [plugins/continuity-org-memory-sync/src/sync-engine.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/plugins/continuity-org-memory-sync/src/sync-engine.ts), [org-server/src/db.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/org-server/src/db.ts)).

## Artifact analysis

- **Storage substrate:** `sqlite` — the central retained memory state persists in local SQLite `memory.db`, with a second SQLite subset for the optional org server.
- **Representational form:** `prose` `symbolic` — memories and projects are symbolic database records carrying prose content, while narratives are LLM-synthesized prose stored with symbolic sections, confidence, versions, and hashes.
- **Lineage:** `authored` `imported` `trace-extracted` — memories can be authored or agent-written through tools, imported through bulk/plugin sync paths, and conversation-derived learnings are absorbed into narratives.
- **Behavioral authority:** `knowledge` `instruction` `routing` `learning` — memory rows advise when browsed or searched, prompt/tool definitions instruct behavior, projects and tools route/scoped access, and learnings feed narrative synthesis.

**Memory rows.** Storage substrate: local SQLite in the app config directory. Representational form: mixed symbolic metadata plus prose content. Lineage: authored or agent-written through in-app tools, MCP tools, bulk imports, plugin sync, or manual database access; updates create version rows and soft deletes mark archive time. Behavioral authority: knowledge artifacts when browsed, read, or searched; system-definition context when preloaded into the in-app prompt.

**Version rows and links.** Storage substrate: local SQLite tables `memory_versions` and `memory_links`. Representational form: symbolic history/link metadata with prose content snapshots for versions. Lineage: generated by memory writes, updates, and explicit link operations. Behavioral authority: evidence and navigation for humans or agents inspecting memory history; relationship types can guide retrieval but do not enforce contradiction handling or supersession semantics by themselves.

**Projects.** Storage substrate: local SQLite `projects` rows. Representational form: symbolic id/name/path/scope records plus prose descriptions. Lineage: authored through MCP or in-app project tools. Behavioral authority: routing and scoping metadata for project memories; project ids affect which records `project_get` and scoped memory operations return, but the default in-app prompt preload currently pulls all non-archived memories rather than only the active project.

**Learnings.** Storage substrate: local SQLite `learnings` rows. Representational form: symbolic signal type, confidence, source ids, scope, and prose observation. Lineage: conversation-derived signals recorded through the MCP `learning_record` surface, optionally pointing at a source thread/message, then marked absorbed during narrative synthesis. Behavioral authority: learning input for narrative synthesis, not direct prompt context unless the generated narrative carries it forward.

**Narratives.** Storage substrate: local SQLite `narratives` rows. Representational form: mixed prose briefing plus JSON sections, confidence score, version, synthesis timestamp, and memory snapshot hash. Lineage: LLM-synthesized from current memories, unabsorbed learnings, and prior narrative state. Behavioral authority: prompt-level system-definition context for the in-app assistant because `buildSystemPrompt()` loads it ahead of every response when present.

**MCP tool definitions and in-app tool prompts.** Storage substrate: repository TypeScript modules and the packaged `continuity-memory` server. Representational form: symbolic Zod/tool schemas plus prose descriptions and behavioral guidelines. Lineage: authored integration code. Behavioral authority: write, read, routing, lifecycle, and instruction authority over which memories are created, updated, searched, exposed, and deleted.

**Plugin and org-sync artifacts.** Storage substrate: plugin manifests, plugin sidecar state, local SQLite rows, and optional org-server SQLite. Representational form: symbolic manifests/capabilities/settings, JSON-RPC messages, prose prompt injection, and memory records. Lineage: authored plugin configuration plus copied/synced local or remote memories. Behavioral authority: extension-level system-definition authority because plugins can register agent tools, inject prompt context, and mutate the shared memory database.

**Promotion path.** Continuity has two promotion paths. Ordinary memories can move from live chat tool calls into versioned rows, then into prompt preload or explicit recall. Learning signals can move from conversation-derived observations into a synthesized narrative, then into every future in-app system prompt. Neither path has Commonplace-style source citation, review, or validation before the artifact gains prompt authority.

## Comparison with Our System

| Dimension | Continuity | Commonplace |
|---|---|---|
| Primary purpose | Local-first AI workspace with shared memory for chat, MCP clients, and plugins | Git-native methodology KB for agent operation and review |
| Canonical retained artifact | SQLite memory rows, version rows, links, learnings, narratives | Typed Markdown notes, source snapshots, reviews, ADRs, indexes, reports |
| Storage substrate | Local SQLite plus optional org-server SQLite; repository code for prompts/tools | Repository files plus generated indexes and deterministic scripts |
| Representational form | Mixed database records, prose memory content, synthesized narrative prose, symbolic tool schemas | Mostly prose/frontmatter Markdown with schemas, scripts, links, and validators |
| Lineage | Version history, source field, optional source thread/message ids for learnings | Git history, citations, frontmatter status, replacement archives, validation and review gates |
| Activation | Prompt preload of recent memories/narrative, explicit recall/search tools, MCP/plugin tools | Mostly pull through `rg`, indexes, authored links, skills, and validation/review commands |
| Authority | Advisory memory becomes prompt context quickly; plugins can add tools/prompts | Collection contracts, type specs, instructions, validators, semantic review, curated promotion |

Continuity is stronger than Commonplace as an adoption-friendly live memory surface. It gives ordinary AI workspace users a database-backed memory browser, built-in MCP server, auto-setup for Claude Code, and plugin extension points without asking them to manage a repo. Commonplace is stronger where durable knowledge needs source-grounded argument, review state, validation, and explicit promotion before it becomes behavior-shaping instruction.

The biggest architectural divergence is that Continuity treats memory as runtime state. The app can write and read it continuously, and prompt injection makes it useful immediately. Commonplace treats retained behavior as library state: artifacts accumulate value through source capture, authoring contracts, links, validation, and review. Continuity's approach is practical for personal context and preferences; it is too weak for methodology claims unless source evidence and review gates are added.

Continuity's context-efficiency model is simple and visible. The in-app assistant gets a capped recent-memory digest and a synthesized narrative, then can pull more with recall/search. That is a reasonable local-first baseline, but it does not solve relevance targeting: recent memories can be irrelevant, project-scoped records can enter global context, and `LIKE` search is sense-blind.

**Read-back:** `both` — retained memory reaches the in-app assistant by coarse prompt push of the narrative and recent memories, and by explicit pull through recall/search/project/MCP tools; I did not find an instance-targeted or faithfulness-tested memory push path.

**Read-back signal:** `coarse` — the push path is a bounded prompt preload of recent memories and synthesized narrative, not instance-targeted retrieval.

**Faithfulness tested:** `no` — the review did not find a with/without or other faithfulness test for whether prompt-pushed memory changes behavior.

### Borrowable Ideas

**Use one local operational database for cross-tool memory state.** Ready when Commonplace needs high-churn operational state rather than durable library artifacts. A small SQLite stage layer could hold pending memories, review queue state, run metadata, or trace-derived candidates while the promoted artifacts remain git-tracked Markdown.

**Preload a bounded digest, not the whole memory store.** Ready as a narrow UX idea. Commonplace could expose short generated "current memory digest" files for specific workflows, but those digests should be explicitly derived and easy to invalidate rather than silently replacing source notes.

**Separate raw memories, learning signals, and synthesized narrative.** Ready as vocabulary discipline. Continuity's `memories` -> `learnings` -> `narratives` split is useful even though its governance is light; Commonplace should keep trace observations, distilled claims, and instruction-bearing artifacts in separate lanes.

**Make memory available through MCP without requiring the host app.** Ready for adoption-facing tools. Commonplace could expose selected search/index/read operations over MCP while keeping repository files authoritative.

**Treat plugin prompt injection as a high-authority surface.** Ready as a review warning, not necessarily a feature. Continuity shows how plugins can register tools and add prompt context; Commonplace should classify any future plugin-provided prompts as system-definition artifacts requiring review.

**Do not borrow immediate promotion to prompt authority without gates.** Continuity's convenience comes from letting chat-derived memory affect future responses quickly. Commonplace should only borrow this for low-stakes personal preferences or workshop candidates, not for durable methodology or instructions.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` — the retained learning signals are extracted from conversations with optional source thread/message ids, not from automatic transcript mining.

**Learning scope:** `per-project` `cross-task` — learning records carry global or project scope, and the app-side synthesis currently defaults to the global narrative.

**Learning timing:** `staged` — learning records accumulate and are later absorbed during launch/activity/staleness/count-triggered narrative synthesis.

**Distilled form:** `prose` `symbolic` — distilled narratives are synthesized prose briefings stored as structured JSON sections with confidence, version, timestamp, and snapshot hash.

**Trace source.** Continuity qualifies at the implementation edge of trace-derived learning because it has durable `learnings` records for observations extracted from conversations, with optional `source_thread_id` and `source_message_id`, and a synthesis engine that absorbs those records into prompt-loaded narratives ([server/tools/narrative-tools.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/tools/narrative-tools.ts), [server/db/learnings.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/db/learnings.ts), [lib/ai/narrative-synthesis.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/lib/ai/narrative-synthesis.ts)). The qualification is narrower than systems that parse full transcript logs automatically: the reviewed code exposes recording surfaces for extracted conversation signals, but I did not find an automatic transcript-mining loop that reads stored `messages` and decides learnings itself.

**Extraction.** Extraction is agent/tool-mediated. `learning_record` accepts a signal type, observation, confidence, scope, project id, and optional source ids. The oracle is therefore the agent or caller that decides to invoke the tool and choose the observation. The later narrative synthesis oracle is an LLM prompt that merges current memories, unabsorbed learnings, and the previous narrative into a structured JSON briefing.

**Four fields.** The raw-ish stage is `learnings`: SQLite rows, mixed symbolic/prose observations, lineage from conversation-derived tool calls, and learning-input authority. The distilled stage is `narratives`: SQLite rows, synthesized prose plus JSON sections, lineage from memories/learnings/prior narrative, and prompt-level system-definition authority when injected into future chats.

**Scope and timing.** Scope is global or project, though the app-side scheduler currently synthesizes the global narrative by default. Timing is staged: learning records accumulate, synthesis runs on app launch, after chat activity, when stale with unabsorbed learnings, or when five or more unabsorbed global learnings exist.

**Survey placement.** Continuity belongs in the chat-to-personal-context family, but with a caveat: it implements the retained surfaces and synthesis path, not a fully automated trace miner. It weakens any survey claim that "trace-derived" must mean raw-log batch processing; it strengthens the split between low-authority conversational observations and higher-authority prompt narratives.

## Curiosity Pass

**The README says "12 tools" while the server registers 17.** The source has grown beyond the README's memory-tool count, adding narrative and learning tools to the MCP server path ([README.md](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/README.md), [server/index.ts](https://github.com/uziiuzair/continuity/blob/4ca8f6b4108aa4494e3861ed33c8019dbd662c67/server/index.ts)). That matters because the memory system is no longer just CRUD/search; it now includes synthesis-oriented state.

**The source field is weaker than lineage.** `source` distinguishes user/AI/system, but ordinary memories do not retain exact message ids or source snippets. Learnings can carry thread/message ids, but narratives do not carry per-claim evidence links.

**Versioning records the new value, not a full semantic diff.** Memory updates preserve history and changed-by metadata, but there is no conflict resolution, proof obligation, or contradiction policy beyond optional relationship links.

**The org sync plugin is architecturally important but still example-shaped.** It shows how team memory would be grafted onto the personal database through plugin capabilities, prompt injection, and a central SQLite server, but the sync subset omits local-only fields such as metadata, source, archived state, and project id.

**Prompt push is useful but blunt.** The memory preload probably helps users feel continuity immediately, but the code cannot show whether those memories actually improve behavior or whether stale/recent-but-irrelevant records dilute the prompt.

## What to Watch

- Whether the learning path gains automatic extraction from stored thread messages. That would make Continuity a stronger trace-derived system and raise the need for source-span lineage and curation controls.
- Whether prompt preload becomes project-aware or relevance-gated instead of "most recent memories across all scopes." That is the main context-efficiency decision.
- Whether `LIKE` search moves to FTS5, embeddings, or hybrid search. The current retrieval is simple and inspectable but weak for semantic recall.
- Whether narratives gain per-claim source links or confidence by section. Without that, synthesized prompt context can drift away from reviewable evidence.
- Whether plugin memory events become a robust synchronization contract. The org-sync design depends on event delivery, conflict policy, and local/remote schema alignment.

## Bottom Line

Continuity is a pragmatic local-first memory workspace: one SQLite database is shared by the desktop app, in-app assistant tools, a standalone MCP server, and plugins; recent memories and synthesized narrative state are pushed into chat context; explicit search/read tools provide pull access. Its strongest lesson for Commonplace is adoption architecture, not governance. It makes memory easy to use across tools, but it promotes chat-derived and LLM-synthesized material into prompt authority faster than a methodology KB should.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Continuity records conversation-derived learning signals and synthesizes them into prompt-loaded narratives, but lacks automatic transcript mining.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Continuity couples storage to coarse prompt preload, while still relying on explicit search for targeted recall.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Continuity separates memories, versions, links, learnings, narratives, MCP tools, plugins, and org-sync records by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: memory rows, version history, links, and org-search results advise future behavior as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompt preloads, synthesized narratives, tool schemas, plugin prompts, and sync policies configure future agent behavior.
