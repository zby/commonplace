---
description: "OpenViking review: context database with viking:// files, session-derived memory, hierarchical retrieval, hooks, MCP, and LangGraph injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# OpenViking

OpenViking, by Volcengine, is an open-source context database for AI agents. At the reviewed commit it implements a `viking://` namespace over resources, sessions, user memories, agent memories, and skills; AGFS/RAGFS-backed content storage; semantic sidecars and vector search; session archiving and memory extraction; MCP/REST/CLI surfaces; and hook or middleware integrations that can inject selected context before an agent acts.

**Repository:** https://github.com/volcengine/OpenViking

**Reviewed commit:** [f627a09662cee5a5494eea99853b355c09b659c4](https://github.com/volcengine/OpenViking/commit/f627a09662cee5a5494eea99853b355c09b659c4)

**Last checked:** 2026-06-04

## Core Ideas

**Context is addressed as a filesystem before it is searched.** OpenViking makes memories, resources, skills, sessions, temp uploads, and queues visible through `viking://` URIs. Namespace helpers canonicalize user, agent, and session roots, derive owner fields from URIs, and enforce account/user/agent access policy before tools read or write content ([openviking/core/namespace.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/core/namespace.py), [openviking/core/context.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/core/context.py)).

**The retained store is layered: files, summaries, relations, and vectors.** `Context` records carry URI, parent URI, context type, level, ownership, `active_count`, metadata, and vectorization text. Memory and resource content live in the virtual filesystem; generated `.abstract.md` and `.overview.md` sidecars provide L0/L1 views over L2 detail; links and relations connect artifacts; and the vector backend stores URI, level, type, abstract, ownership, and activity fields for retrieval ([openviking/storage/viking_vector_index_backend.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/storage/viking_vector_index_backend.py), [openviking/session/memory/memory_updater.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/memory/memory_updater.py)).

**Context efficiency is explicitly engineered.** The system avoids flat top-k dumping by combining hierarchical retrieval, L0/L1/L2 levels, token budgets, generated session working-memory summaries, profile sub-budgets, listing truncation, result limits, score thresholds, and graceful degradation to URI-only hints when a recall item does not fit. The tradeoff is complexity: freshness, authority, and relevance depend on several derived layers rather than one inspectable note ([openviking/retrieve/hierarchical_retriever.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/retrieve/hierarchical_retriever.py), [examples/claude-code-memory-plugin/scripts/auto-recall.mjs](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/examples/claude-code-memory-plugin/scripts/auto-recall.mjs), [examples/claude-code-memory-plugin/scripts/lib/profile-inject.mjs](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/examples/claude-code-memory-plugin/scripts/lib/profile-inject.mjs)).

**Sessions are the trace-to-memory pipeline.** A session stores messages and structured parts, can externalize tool results, archives older messages on commit, generates a seven-section working-memory overview, extracts user and agent memories, writes links/backlinks, vectorizes changed memories, records done/failed archive markers, and updates session metadata. This is a durable learning path, not only a transcript log ([openviking/session/session.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/session.py), [openviking/session/compressor_v2.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/compressor_v2.py), [openviking/session/memory/memory_updater.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/memory/memory_updater.py)).

**OpenViking exposes both pull tools and pre-action injection.** The MCP endpoint exposes `find`, `search`, `read`, `list`, `remember`, `add_resource`, watch management, grep/glob, code tools, and forget as explicit pull tools ([openviking/server/mcp_endpoint.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/server/mcp_endpoint.py)). Claude Code, Codex, OpenClaw, and LangGraph integrations add push read-back: hooks and middleware assemble profile, archive, and recall context and insert it before a model call ([examples/claude-code-memory-plugin/hooks/hooks.json](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/examples/claude-code-memory-plugin/hooks/hooks.json), [examples/codex-memory-plugin/hooks/hooks.json](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/examples/codex-memory-plugin/hooks/hooks.json), [openviking/integrations/langchain/middleware.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/integrations/langchain/middleware.py)).

**Operational boundaries are part of the memory design.** Identity headers, tenant-aware namespace policy, vector rows with ownership fields, task tracking, archive failure markers, redo recovery hooks, metrics, and usage audit machinery make OpenViking a service runtime rather than a local notebook. That is important because push read-back and automatic memory extraction need governance surfaces, not just a storage API ([openviking/server/mcp_endpoint.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/server/mcp_endpoint.py), [openviking/session/session.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/session.py), [openviking/storage/viking_vector_index_backend.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/storage/viking_vector_index_backend.py)).

## Artifact analysis

- **Storage substrate:** `files` `vector` `graph` `sqlite` `service-object` — Source content, memory files, session archives, sidecars, and plugin state are file-backed; vector rows support retrieval; links/relations create graph-like traversal; usage audit and task/telemetry state include service-managed stores; runtime sessions and task records are service objects.
- **Representational form:** `prose` `symbolic` `parametric` — Memories, resources, summaries, profile blocks, and archive overviews are prose; URI schemas, templates, JSON metadata, hooks, policies, merge operations, links, task markers, and API contracts are symbolic; embeddings and vector/rerank scores are parametric retrieval artifacts.
- **Lineage:** `authored` `imported` `trace-extracted` — Operators and agents can author memories and skills, resources can be uploaded or watched from external sources, and session messages/tool parts/context parts are archived and distilled into user memories, agent memories, session skills, summaries, relations, and vectors.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Retrieved memories/resources are knowledge; agent skills, profile blocks, and injected context can instruct; namespace policy and write guards enforce; URIs, sidecars, relations, templates, and search filters route; schemas and operation parsing validate; vectors, scores, hotness, and rerankers rank; session extraction learns durable artifacts.

**Source content and memory files.** The operative source artifacts are `viking://` files under resources, user memories, agent memories, skills, and sessions. Their authority changes by path and consumer: a retrieved resource is a knowledge artifact; an agent skill or injected experience can behave as system-definition guidance. Deletion and invalidation are mediated by URI policy, filesystem operations, vector cleanup, and derived sidecar refresh.

**Generated sidecars and vector rows.** `.abstract.md`, `.overview.md`, directory overviews, relation data, and vector-index rows are derived views. They should not be treated as source truth, but they carry high retrieval authority because they determine what is found, which level is loaded, and whether a candidate fits a budget.

**Session archives.** `messages.jsonl`, `.abstract.md`, `.overview.md`, `.meta.json`, `.done`, and `.failed.json` under session history preserve the raw and summarized trace pipeline. Raw messages have evidence authority; summaries compress; done/failed markers have lifecycle authority because later commits wait for prior archive state; metadata records token and extraction counts.

**Extracted memories and skills.** User memory templates cover profile, preferences, entities, and events; agent memory templates include tools, trajectories, experiences, skills, soul, and identity. The extracted files bundle prose content with symbolic fields, links, backlinks, operation modes, filename templates, embedding templates, and directory overview templates. Their lineage may be trace-derived, but their consumption may be advisory, instructional, or retrieval-ranking input depending on integration.

**Integration artifacts.** MCP tool definitions, Claude/Codex hook configs, OpenClaw plugin code, OpenCode plugin code, and LangGraph middleware are system-definition artifacts. They decide when memory becomes input to an agent, what context is captured afterward, what is filtered from transcripts to avoid self-contamination, and which identity scope is used.

Promotion path: source material or trace enters a `viking://` namespace; semantic processing and memory extraction create summaries, typed memories, links, overviews, and vectors; retrieval selects items; hooks or middleware can push selected artifacts into a future model call. The risky boundary is trace-derived extraction into agent memories or skills that later re-enter context without a repo-style review gate.

## Comparison with Our System

Commonplace is a Git-backed methodology KB with typed Markdown artifacts, validation, review gates, generated indexes, and source-pinned reviews. OpenViking is a runtime context database for serving memory to agents. Both care about retained artifacts, context economy, lineage, and agent consumption, but they assign authority differently.

OpenViking is stronger at runtime activation. It wires memory into Claude Code, Codex, OpenClaw, OpenCode, MCP, HTTP, CLI, and LangGraph flows; captures session traces; extracts memories in the background; and can inject relevant context before a model call. Commonplace normally relies on explicit search, curated indexes, links, skills, and validations rather than automatic pre-action activation.

Commonplace is stronger at inspectable acceptance. Collection contracts, type specs, review archives, source citations, deterministic validation, and semantic review runs make a durable artifact's authority visible in Git. OpenViking exposes diffs, archive markers, task status, metrics, and audit surfaces, but a trace-derived experience or session skill can become future context before a human review has accepted it.

OpenViking's URI and tenant model is more dynamic than Commonplace's directory routing. A future Commonplace runtime layer would need the same question OpenViking asks explicitly: whose artifact is this, under which account/user/agent identity, and what authority is allowed on this read path?

### Borrowable Ideas

**Commit-pinned context sidecars.** Ready as a design pattern, not an immediate feature. Commonplace could generate explicit low-authority summaries or abstracts for large artifacts, but they must remain visibly derived and regenerable.

**Budgeted pre-action recall.** Needs a concrete runtime use case. The hook pattern of thresholding, reranking, deduping, token budgeting, and degrading to URI-only hints is useful for agent sessions, but should not be enabled broadly for dense KB notes.

**Session archive diff and done/failed markers.** Ready for generated Commonplace operations. Durable extraction should leave a compact audit target plus lifecycle state, so reviewers can tell whether a trace-derived artifact is complete or blocked.

**Namespace identity as part of an address.** Ready conceptually. Commonplace's directory paths encode collection authority, but agent-runtime reads should also carry actor, project, and consumer identity.

**Separate raw trace, summary, memory, skill, and push path.** Ready now as vocabulary. OpenViking is a good example of why storage substrate alone does not classify authority: the same session can produce evidence, compressed context, advice, instructions, and retrieval indexes.

**Do not borrow automatic high-authority promotion without a gate.** OpenViking's trace-derived experiences and session skills are powerful, but Commonplace should route similar outputs through review before they become instruction-like context.

## Write side

**Write agency:** `manual` `automatic` — Operators and agents can manually write memories/resources through MCP, REST, CLI, and filesystem-like tools; automatic writes include resource processing, semantic sidecar generation, vectorization, session commit archives, working-memory summaries, extracted user memories, extracted agent memories, session skills, relations, active-count updates, directory overviews, and watch refreshes.

**Curation operations:** `consolidate` `evolve` `invalidate` `promote` — Session working memory consolidates archives into overview/abstract forms; memory merge operations can update existing files in place; archive failure markers and supersession-style delete/update operations invalidate or replace prior material; vector rows, active counts, directory overviews, and session skills can promote material into more discoverable or more behavior-shaping paths.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — Session messages, tool calls/results, context parts, externalized tool outputs, hook transcripts, active context usage records, and trajectory/experience memory templates feed extraction.

**Learning scope:** `cross-task` — Extracted user memories, agent memories, session skills, archive summaries, links, and vectors persist beyond the originating session and can affect later sessions for the same identity scope.

**Learning timing:** `online` `staged` — Hooks capture messages during normal agent use; commits archive immediately and run extraction asynchronously; archive ordering and done/failed markers create a staged pipeline.

**Distilled form:** `prose` `symbolic` `parametric` — The outputs include prose summaries and memories, symbolic templates/fields/links/diffs/operation records/skills, and embeddings used for later retrieval.

The trace-derived path is implemented in the session commit pipeline. Phase 1 snapshots and archives messages; Phase 2 hydrates tool outputs, generates archive summaries, calls long-term and agent-memory extraction, writes links and active-count updates, waits for request-scoped queue work, merges metadata, and writes `.done` last ([openviking/session/session.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/session.py)).

The extraction mechanism is LLM-mediated but schema-constrained. `SessionCompressorV2` creates an `ExtractLoop` with a session extract context provider and a memory type registry; the updater applies resolved operations, preserves system-managed fields, merges links/backlinks, vectorizes changed memory files, and regenerates directory overviews ([openviking/session/compressor_v2.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/compressor_v2.py), [openviking/session/memory/memory_updater.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/session/memory/memory_updater.py)).

The survey fit is trace -> archive -> working-memory summary -> typed user/agent memory or session skill -> sidecar/vector/index -> pull or push read-back. This is closer to long-term agent learning than to ordinary session compression because the extracted artifacts can be recalled across later tasks and injected before future actions.

The main caveat is authority. OpenViking preserves useful lineage artifacts, but the core implementation does not make human approval a necessary step before a trace-derived memory, experience, or skill is eligible for later retrieval or injection.

## Read-back

**Read-back:** `both` — OpenViking supports explicit pull through MCP/REST/CLI/search/read/list tools, and it supports push when hooks or LangGraph middleware assemble OpenViking memory and inject it before the model call.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / embedding` — Session-start profile injection is coarse budgeted loading; session archive injection is keyed by session id; auto-recall narrows by identity/URI scopes, searches by semantic similarity, and applies lexical/category/level ranking boosts over the current prompt.

**Faithfulness tested:** `no` — The repository contains benchmark scripts and many implementation tests, but this review did not find an implementation-level with/without ablation or post-action audit proving that injected OpenViking context changes agent behavior as intended.

Pull read-back is ordinary and broad. MCP `find` and `search` return ranked memories, resources, and skills with URI, abstract, and score; `read` expands one or more URIs; `list` traverses a directory; `remember` creates a short session and commits it for memory extraction; `add_resource`, grep/glob, code navigation, watch management, and forget extend the pull surface ([openviking/server/mcp_endpoint.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/server/mcp_endpoint.py)).

Push read-back has several implemented paths. Claude Code `SessionStart` can inject profile memory and, on resume/compact, latest session archive context. Claude Code and Codex `UserPromptSubmit` hooks run `auto-recall` before the agent acts. LangGraph middleware wraps model calls, assembles session context and recall documents, and prepends or appends an OpenViking context block to the system message ([examples/claude-code-memory-plugin/scripts/session-start.mjs](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/examples/claude-code-memory-plugin/scripts/session-start.mjs), [examples/claude-code-memory-plugin/scripts/auto-recall.mjs](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/examples/claude-code-memory-plugin/scripts/auto-recall.mjs), [examples/codex-memory-plugin/hooks/hooks.json](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/examples/codex-memory-plugin/hooks/hooks.json), [openviking/integrations/langchain/middleware.py](https://github.com/volcengine/OpenViking/blob/f627a09662cee5a5494eea99853b355c09b659c4/openviking/integrations/langchain/middleware.py)).

Targeting is mixed. Session-start profile loading is coarse because it loads the active user's profile and memory listings without a task-specific relevance query, though with a token budget. Resume/compact archive loading is identifier-scoped by session id. Auto-recall is instance-targeted: it searches user memory, agent memory, and skills under resolved `viking://user/...` and `viking://agent/...` roots using the current prompt, then filters by score threshold, deduplicates, applies level/category/lexical boosts, limits count, and fits content into a token budget.

The injection point is pre-invocation. `UserPromptSubmit` hooks return `additionalContext`; `SessionStart` returns `additionalContext`; LangGraph middleware modifies the request before calling the handler. Stop, PreCompact, SessionEnd, and after-agent hooks are write-side capture or commit paths, not post-action read-back.

Selection complexity is substantial. Hierarchical retrieval embeds once, chooses root URIs, runs global vector search, merges starting points, recursively searches children, applies score propagation, and can rerank. Hook-level formatting can include full content, abstracts, or URI-only hints depending on the budget. The code establishes the route and controls; actual precision, context dilution, and obedience are runtime qualities not proven by static inspection.

The authority of pushed context is advisory but strong in practice. It is not a validator, but it appears before model action and may include profile facts, preferences, memories, archive summaries, agent memories, skills, or resources. That means generated memories and sidecars need lower-authority treatment unless separately reviewed.

Other consumers include human operators, the web studio, CLIs, metrics dashboards, task trackers, usage audit readers, and resource watchers. Those are governance and observability surfaces, not separate read-back values.

## Curiosity Pass

OpenViking's filesystem metaphor is useful, but the behavior is not just file behavior. Vector rows, generated sidecars, relation links, memory templates, task state, identity policy, hook budgets, and middleware injection all participate in what the next model sees.

The current code has multiple integration generations at once: Claude Code, Codex, OpenClaw, OpenCode, LangChain, LangGraph, MCP, and REST. Reviews should classify deployed wiring per integration rather than treating "OpenViking memory" as one read-back mode.

The profile injection path is a notable coarse push. It is not targeted by the current prompt, but it is budgeted and uses listings/abstracts rather than full recursive memory loading. That is a more disciplined always-load pattern than putting an entire memory tree into context.

The trace-capture hooks explicitly strip previously injected OpenViking blocks before saving new transcripts. That is a strong design signal: the authors are aware that pushed memory can contaminate later memory extraction.

Session working memory is both useful and risky. It frontloads session compression into an inspectable `.overview.md`, but a generated overview can become a future context source. Treating it as a lower-authority derived view is essential.

## What to Watch

- Whether trace-derived agent experiences and session skills gain explicit review or approval gates before push read-back can use them.
- Whether the benchmarks add reproducible with/without activation tests for injected memory, not just retrieval or task-score claims.
- Whether generated sidecars and vectors reliably invalidate after resource updates, deletes, moves, and watch refreshes.
- Whether profile/session-start injection stays within budgets for large real user memories, especially CJK-heavy profiles.
- Whether OpenClaw, OpenCode, Claude Code, Codex, and LangGraph integrations converge on one memory lifecycle or keep diverging in capture and injection semantics.
- Whether usage audit and metrics remain content-safe and tenant-safe in multi-tenant deployments.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes OpenViking's stored memories from its hook and middleware paths that actively insert memory into context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies to OpenViking's split between files, sidecars, vectors, session archives, hooks, and policies.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies retrieved resources, memories, summaries, and profile facts when they act as evidence or advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies hooks, middleware, skills, templates, namespace policy, and generated session skills when they shape behavior with stronger force.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - connects to OpenViking's session archive and memory extraction pipeline.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - explains OpenViking's sidecar summaries, session working memory, and pre-action recall budgets.
