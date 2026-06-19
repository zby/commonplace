---
description: "Mem0 review: memory SDK/server/platform with additive trace extraction, hybrid retrieval, agent plugins, hooks, and pushed context injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Mem0

Mem0, from `mem0ai/mem0`, is a memory layer for personalized AI applications and coding agents. At the reviewed commit it includes a Python SDK, TypeScript SDKs, a self-hosted FastAPI server, cloud/platform clients, a LiteLLM chat proxy, a remote MCP/plugin distribution, Claude/Codex/Cursor/OpenCode/Antigravity hooks, and an OpenClaw plugin. The core SDK stores extracted memory in a vector store plus SQLite history, while the agent plugins make Mem0 operational by capturing session traces and injecting selected memories back into future prompts.

**Repository:** https://github.com/mem0ai/mem0

**Reviewed commit:** [64b9646e7dd2c97ed20233732f79ca3d94037c65](https://github.com/mem0ai/mem0/commit/64b9646e7dd2c97ed20233732f79ca3d94037c65)

**Last checked:** 2026-06-04

## Core Ideas

**The current SDK write path is additive extraction, not automatic rewrite/delete.** `Memory.add(..., infer=True)` builds scoped metadata and query filters, retrieves existing memories for deduplication/linking context, asks the LLM to produce ADD-only extractions, skips exact hash duplicates, inserts new memory vectors, records ADD history, and links extracted entities in a separate entity collection ([mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/memory/main.py), [mem0/configs/prompts.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/configs/prompts.py)). Manual `update`, `delete`, and `delete_all` still exist, but the default inferred add path accumulates new facts rather than mutating old facts in place.

**Search is hybrid and session-scoped.** SDK search requires filters containing `user_id`, `agent_id`, or `run_id`; it embeds the query, runs vector search, attempts keyword search, extracts query entities, computes entity boosts from linked-memory ids, normalizes BM25 scores, and ranks candidates with a semantic threshold and optional reranker ([mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/memory/main.py), [mem0/utils/scoring.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/utils/scoring.py), [mem0/utils/entity_extraction.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/utils/entity_extraction.py)). That makes read-back quality heavily dependent on metadata scoping and retrieval parameters, not just on stored facts.

**Context efficiency is mostly bounded retrieval plus plugin-side budgeting.** The SDK over-fetches internally and returns `top_k`; the proxy wrapper searches with only the last six messages before prepending relevant memories to the user query; the Claude/Codex plugin shows at most ten recent memories at session start and five file-context memories before a `Read`; OpenClaw recall defaults to a 1500-token budget, 15 memories, category priority, and threshold filtering ([mem0/proxy/main.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/proxy/main.py), [mem0-plugin/scripts/session_timeline.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/session_timeline.py), [mem0-plugin/scripts/file_context.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/file_context.py), [openclaw/recall.ts](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/openclaw/recall.ts)). There is no global proof that these budgets prevent context dilution; they are visible policies.

**The agent plugins turn a pull API into pushed memory.** Direct SDK, REST, MCP, and CLI search are pull surfaces. The full plugins add push: `SessionStart` prints instructions and recent activity, `UserPromptSubmit` injects search rubrics or resume memories, `PreToolUse(Read)` injects file-specific prior work, `PostToolUse(Bash)` injects prior error memories, and OpenClaw `before_prompt_build` can prepend recalled memories before each agent turn ([mem0-plugin/hooks/hooks.json](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/hooks/hooks.json), [mem0-plugin/hooks/codex-hooks.json](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/hooks/codex-hooks.json), [mem0-plugin/scripts/on_session_start.sh](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/on_session_start.sh), [mem0-plugin/scripts/on_user_prompt.sh](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/on_user_prompt.sh), [openclaw/index.ts](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/openclaw/index.ts)).

**Trace capture is broad and multi-trigger.** The plugin stores recent transcript windows every third substantial prompt, session summaries on Stop, fallback session state before compaction, compact summaries after compaction resumes, imported project-profile files at startup, and OpenClaw agent-end traces unless the agent already used memory tools ([mem0-plugin/scripts/auto_capture.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/auto_capture.py), [mem0-plugin/scripts/capture_session_summary.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/capture_session_summary.py), [mem0-plugin/scripts/on_pre_compact.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/on_pre_compact.py), [mem0-plugin/scripts/capture_compact_summary.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/capture_compact_summary.py), [mem0-plugin/scripts/auto_import.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/auto_import.py), [openclaw/index.ts](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/openclaw/index.ts)).

**Governance is mostly metadata, scoping, and agent instructions.** Hooks inject default `user_id`, `app_id`, metadata type/source/confidence, block writes to Claude `MEMORY.md`, parse optional `mem0.md` settings, and include reviewer/dream skills for duplicate, contradiction, stale-memory, and pruning workflows ([mem0-plugin/scripts/enforce_metadata_defaults.sh](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/enforce_metadata_defaults.sh), [mem0-plugin/scripts/block_memory_write.sh](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/block_memory_write.sh), [mem0-plugin/scripts/parse_mem0_config.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/parse_mem0_config.py), [mem0-plugin/skills/memory-reviewer/SKILL.md](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/skills/memory-reviewer/SKILL.md), [mem0-plugin/skills/dream/SKILL.md](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/skills/dream/SKILL.md)). These are useful operational guardrails, but they are not equivalent to source-level review of extracted memories.

## Artifact analysis

- **Storage substrate:** `vector` `sqlite` `rdbms` `files` `service-object` - The OSS SDK stores memories and entity records in the configured vector store and history/recent-message context in SQLite; the self-hosted server defaults to pgvector/Postgres plus SQLite history; plugins also retain local hash maps, project maps, stats, locks, and settings under `~/.mem0` or `/tmp`; hosted platform storage is consumed as a service object through API/MCP clients ([mem0/memory/storage.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/memory/storage.py), [server/main.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/server/main.py), [mem0-plugin/scripts/_project.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/_project.py), [openclaw/backend/platform.ts](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/openclaw/backend/platform.ts)).
- **Representational form:** `prose` `symbolic` `parametric` - Memories, summaries, imported project profiles, prompts, and tool outputs are prose; IDs, filters, metadata, categories, roles, actor attribution, timestamps, expiration dates, plugin manifests, hook matchers, and skill protocols are symbolic; embeddings and optional rerankers provide parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` - Developers author prompts, skills, hooks, categories, and APIs; plugins import `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `.windsurfrules`, `mem0.md`, and competing-tool memory files as project-profile memories; automatic capture derives memories from conversation transcripts, assistant outputs, tool calls, file paths, command errors, and compaction summaries ([mem0-plugin/scripts/auto_import.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/auto_import.py), [mem0-plugin/scripts/import_competing_tools.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/import_competing_tools.py), [mem0-plugin/scripts/auto_capture.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0-plugin/scripts/auto_capture.py)).
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Retrieved memories mostly advise as knowledge context; session-start banners, rubrics, memory-triage skills, and OpenClaw skill prompts instruct the agent; write blockers and hook-updated inputs enforce or validate parts of the workflow; user/project/session/file identifiers route storage and retrieval; hybrid search and category ordering rank results; extraction, auto-capture, entity linking, and dream workflows implement learning-like memory updates.

**Memory records.** A memory record is prose content plus metadata, hash, timestamps, optional role/actor attribution, vector embedding, and history. It is a knowledge artifact when returned through search or injected as context; it becomes more instruction-like only when the host prompt tells the agent to obey it.

**Entity records and access structures.** Entity extraction creates a separate entity collection with entity text, type, linked memory ids, and scope filters. Those records do not replace the memory text; they boost later retrieval and make entity availability a ranking input ([mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/64b9646e7dd2c97ed20233732f79ca3d94037c65/mem0/memory/main.py)).

**Plugin hooks and skills.** Hook JSON files and shell/Python/TypeScript scripts are system-definition artifacts. They decide when memory is searched, when traces are captured, which metadata is injected, what files are imported, and when the agent is nudged or blocked. The strongest behavioral authority in the reviewed code often sits in this plugin layer rather than in the bare SDK.

**Promotion path.** Mem0 promotes raw conversation/tool traces into extracted prose memories, categories/metadata, embeddings, entity links, summaries, and project profiles. OpenClaw skills mode adds a stronger operational path: recalled memories and memory-dream instructions can be injected into prompt construction, but there is still no Commonplace-style promotion into typed, reviewed, git-native notes or validators.

## Comparison with Our System

| Dimension | Mem0 | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory layer for apps, agents, and plugins | Git-native methodology KB for agents and maintainers |
| Canonical retained artifact | API memory record with embeddings, metadata, entity links, and history | Typed Markdown artifact with frontmatter, links, validation, and git review |
| Write path | SDK/API/MCP/tool writes plus automatic trace capture and imports | Human/agent-authored repo artifacts, snapshots, validation, and review gates |
| Read-back | Pull APIs plus hook/proxy/OpenClaw pushed context | Mostly explicit pull through `rg`, indexes, links, and loaded instructions |
| Governance | Metadata defaults, identity filters, hook blockers, skills, API auth | Collection contracts, schemas, validation, semantic review, git diffs |

Mem0 is stronger as an adoptable runtime substrate. It supplies SDKs, cloud service, self-hosted server, MCP, CLI, hooks, and coding-agent plugins. Commonplace is stronger as an inspectable knowledge system: durable behavior-shaping artifacts are readable in the repo, type-checked, linkable, and reviewable before gaining authority.

The important design divergence is authority. Mem0 optimizes for continuous personalization: memory can be extracted in the background and later pushed into an agent prompt. Commonplace optimizes for reviewable methodology: memory is slower to create, but its provenance and intended authority are explicit. Mem0's plugin work is therefore useful evidence for how agents actually need memory in the loop, while also showing the risks of unreviewed extracted facts becoming prompt context.

### Borrowable Ideas

**Hook-level read-back occasions.** Ready as vocabulary. Commonplace can distinguish session-start, user-prompt, file-read, command-error, and compaction-recovery occasions when designing future activation surfaces.

**Metadata injection before memory tool calls.** Ready now where tools exist. Mem0's hook-updated inputs show a practical way to prevent agents from forgetting user/project scope.

**File-read prior-work context.** Needs a concrete Commonplace use case. A scoped "prior work on this file/note" lookup before reading could help, but only if it cites reviewed local artifacts rather than opaque extracted memories.

**Trace capture with expiration.** Ready for workshop memory, not library notes. Session summaries and compaction snapshots are useful temporary artifacts; Commonplace should keep them in workshop/report space until promoted.

**Do not borrow silent memory authority wholesale.** Mem0's strongest convenience is automatic prompt injection. Commonplace should require a visible provenance and authority boundary before extracted memories become instructions.

## Write side

**Write agency:** `manual` `automatic` - Humans, agents, SDK/API clients, MCP tools, CLI commands, plugin skills, and OpenClaw tools can add, update, delete, import, and search memories; automatic paths extract from messages, session summaries, compaction summaries, file imports, command errors, and agent-end traces.

**Curation operations:** `dedup` `consolidate` `decay` - The SDK and import scripts skip exact or unchanged duplicates by hash/content checks; dream skills can merge near-duplicates into a more complete replacement; session-state and summary captures set expiration dates, and dream can prune stale memories under retention policy. Automatic truth-maintenance is weaker than older Mem0 descriptions suggest: default inferred add is ADD-only, and contradiction resolution requires the dream/reviewer protocol or manual tool use.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` - Qualifying traces include conversation transcripts, assistant outputs, tool-use blocks, file paths touched, Bash command output, compaction summaries, session ids, project ids, and OpenClaw agent-end messages.

**Learning scope:** `per-project` `cross-task` - The plugin scopes most memories by `user_id` plus `app_id`/project id and sometimes branch/session id, so memories can affect later tasks in the same project and user namespace. Session-scoped memories are available when a run/session id is included.

**Learning timing:** `online` `staged` - SDK adds run during requests, UserPromptSubmit auto-capture runs in the background every third substantial prompt, Stop and PreCompact hooks capture at lifecycle boundaries, compact summaries are captured on the next compact SessionStart, and OpenClaw auto-dream is gated by local state plus memory count.

**Distilled form:** `prose` `symbolic` `parametric` - Distilled outputs include prose memories and summaries, symbolic metadata/categories/entities/filters/expiration dates/history rows, and embeddings/entity vectors used for later retrieval.

**Extraction.** The main oracle is an LLM extraction prompt that reads new messages, recent messages, relevant existing memories, observation date, and optional custom instructions, then emits ADD-only memory texts with optional links. Plugin capture paths often call the platform API with `infer=True`; verbatim or imported project-profile paths use `infer=False`.

**Scope and timing.** Mem0's trace loop is optimized for immediate continuity rather than review. The same session can produce user memories, session summaries, compact summaries, project profile chunks, and file/error-context records; retrieval later selects among them through filters and scores.

**Survey fit.** Mem0 belongs in the trace-to-personal-memory and trace-to-agent-work-memory family. Its new code strengthens the survey distinction between acquisition and curation: it extracts many memories from traces, but the default open-source inference path avoids automatic update/delete of existing facts.

## Read-back

**Read-back:** `both` - SDK, REST, MCP, CLI, and OpenClaw tools expose explicit pull search/list/get operations; the proxy wrapper and full agent plugins also push selected memories or memory instructions into prompt/context before the receiving model acts.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` - SessionStart recent activity and setup instructions are coarse; user/project/session/file identifiers scope many searches; prompt, file-path, and error hooks use lexical cues and metadata type filters; SDK/platform search and OpenClaw recall use embedding-backed search, with BM25/entity signals where the backend supports them.

**Faithfulness tested:** `no` - I found tests and code paths for add/search, proxy, plugin hooks, metadata defaults, rubric deduplication, session stats, project resolution, and OpenClaw recall/capture mechanics, but not a with/without memory ablation or post-action audit proving that injected memories changed downstream agent behavior correctly.

**Direction edge cases.** Direct MCP configuration alone is pull: the agent must call `search_memories`, `get_memories`, or related tools. Installing the full plugin changes the classification because hooks inject context without the agent first choosing a memory tool. User-initiated search is still pull machinery, but hook-triggered resume/file/error context is push from the receiving agent's perspective.

**Targeting and signal.** Session-start timeline is broad within the active user/project. File-read context is instance-targeted by file path and basename. UserPromptSubmit resume handling searches fixed session-state and decision queries; Bash-output handling searches anti-pattern and bug-fix memories from detected error text. OpenClaw auto-recall sanitizes the prompt and searches long-term and optionally session memory, then ranks and budgets results.

**Injection point.** Read-back is pre-invocation: proxy code rewrites the last user message before `litellm.completion`; Claude/Codex hooks return `additionalContext`; OpenClaw returns `prependContext` or `prependSystemContext` from `before_prompt_build`. Stop, PreCompact, compact-summary capture, and agent-end capture are write-side maintenance for later turns, not read-back for the current action.

**Selection, scope, and complexity.** Pull searches expose `top_k`, threshold, filters, reranking, and metadata operators. Plugin push paths are bounded but heterogeneous: recent timeline is ten memories, file context is five, UserPromptSubmit resume is two searches of three each, OpenClaw legacy recall caps at configured `topK`, and OpenClaw skills recall has token and memory budgets. Effective precision/recall and context dilution are not verified from code.

**Authority at consumption.** Most retrieved memories are advisory context. SessionStart banners and OpenClaw skills prompts add stronger instruction authority by telling the agent when and how to search/store memories. Write blockers and metadata-enforcement hooks can have enforcement authority before tools run.

**Other consumers.** Humans consume memories through the platform dashboard, server dashboard, CLI, MCP tools, export/import skills, health/stats/tour skills, and plugin output. Background hooks, OpenClaw gates, search managers, and dream/reviewer skills consume the same retained state operationally.

## Curiosity Pass

**Mem0 is no longer just an SDK memory store.** The most consequential behavior at this commit is in the plugin/hook layer: it decides whether memory reaches the model without a tool call.

**The README's v3 claim matters.** The add path really is ADD-only in the inspected SDK inference path, so automatic update/delete claims should be treated as legacy or manual unless tied to a platform feature not visible in this checkout.

**Entity linking is retrieval infrastructure, not a graph memory system by itself.** Entity records link text entities to memory ids and boost retrieval; the reviewed code does not show a graph database with traversed relational reasoning as the canonical store.

**Project-profile import blurs instruction and memory.** Importing `AGENTS.md`, `CLAUDE.md`, and `mem0.md` into a semantic memory service can make local rules retrievable, but the imported chunks lose the review and precedence semantics of the original files.

**OpenClaw's token-budgeted recall is cleaner than the generic hook prompts.** It gives a more inspectable read-back policy: threshold, over-fetch, category priority, max memories, and rough token budget are all visible in one module.

## What to Watch

- Whether the open-source SDK regains automatic update/delete reconciliation or keeps the v3 ADD-only extraction contract; that changes the write-side curation classification.
- Whether platform APIs expose provenance from extracted memories back to exact transcript spans, hook source, model, prompt version, and extraction inputs.
- Whether plugin hook installation becomes default for Codex rather than opt-in; that changes typical deployed read-back from pull/MCP-only to pushed memory.
- Whether dream consolidation becomes an implemented backend job instead of an agent skill/protocol; that would make dedup/decay/contradiction handling more code-owned.
- Whether OpenClaw auto-recall gains behavioral tests or ablations showing that injected memories improve task outcomes rather than merely appearing in context.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Mem0 has storage plus both explicit pull and hook/proxy/OpenClaw push read-back.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Mem0's memory records, embeddings, entity links, hooks, skills, and local files carry different substrates, forms, lineage, and authority.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: retrieved memory records and project-profile imports mostly serve as evidence or advisory context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: hooks, skill protocols, metadata enforcement, write blockers, and recall policies shape future behavior.
- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - places: Mem0 derives durable memories and summaries from session traces, tool traces, compaction events, and agent-end messages.
