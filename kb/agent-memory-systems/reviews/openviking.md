---
description: "OpenViking review: viking:// context database with AGFS/RAGFS storage, hierarchical retrieval, session extraction, hooks, MCP, tenancy, and metrics"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# OpenViking

**Repository:** https://github.com/volcengine/OpenViking  
**Reviewed commit:** [7bcd66a4510360692043b0afc466381315f85d63](https://github.com/volcengine/OpenViking/commit/7bcd66a4510360692043b0afc466381315f85d63)  
**Last checked:** 2026-06-02

OpenViking is a context database for AI agents. At this revision it is not just a vector-memory service: it is a `viking://` virtual namespace over AGFS/RAGFS content storage, semantic sidecars, a vector index, session archives, trace-derived memory extraction, MCP/HTTP tools, LangChain middleware, Claude/Codex/OpenClaw plugins, tenant scoping, benchmarks, and metrics.

## Core Ideas

OpenViking makes context addressable before it makes it searchable. The `viking://` namespace has typed roots for resources, sessions, user memory, agent memory, temp state, queues, and uploads, with canonicalization and access checks handled by `AccountNamespacePolicy` rather than left to each caller. Public visible roots include `viking://resources`, `viking://session`, and canonical user/agent roots; user and agent shorthand expands through the active request context. This turns "which memory am I talking about?" into an explicit URI, owner, and context-type question. See [`openviking/core/namespace.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/core/namespace.py) and the URI concept doc in [`docs/en/concepts/04-viking-uri.md`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/docs/en/concepts/04-viking-uri.md).

The storage model is a layered filesystem plus vector index. `Context` records carry `uri`, `parent_uri`, `context_type`, `level`, ownership, `active_count`, and vectorization text. AGFS/RAGFS content stores the source objects and generated sidecars; `.abstract.md` and `.overview.md` provide L0/L1 summaries over L2 detail files; `.relations.json` stores graph edges. The vector backend stores URI, level, context type, abstract, ownership, and account-scoped metadata. Writes are funneled through a coordinator that blocks direct writes to derived sidecars, applies namespace policy, and queues semantic refresh. See [`openviking/core/context.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/core/context.py), [`openviking/storage/viking_fs.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/storage/viking_fs.py), [`openviking/storage/content_write.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/storage/content_write.py), and [`openviking/storage/viking_vector_index_backend.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/storage/viking_vector_index_backend.py).

Semantic structure is maintained as an asynchronous lifecycle. The semantic processor generates sidecars bottom-up, vectorizes resources and memories, caches DAG/request stats, coordinates locks, emits telemetry, and can requeue or circuit-break work. Memory directories get special handling: changed memory files are summarized, sidecars are rewritten, L2 files and L0/L1 directories are vectorized, and unchanged summaries can be reused. See [`openviking/storage/queuefs/semantic_processor.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/storage/queuefs/semantic_processor.py) and [`openviking/storage/queuefs/semantic_sidecar.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/storage/queuefs/semantic_sidecar.py).

Retrieval is hierarchical, not a flat top-k memory lookup. `find` performs semantic search without session context; `search` uses session summary and recent messages to run intent analysis and generate typed queries over memory, resources, and skills. The hierarchical retriever embeds once, determines roots, performs global vector search, merges starting points, recursively searches children, propagates score, follows relation candidates, can rerank, and returns matched contexts with level and URI information. See [`openviking/retrieve/hierarchical_retriever.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/retrieve/hierarchical_retriever.py), [`openviking/storage/viking_fs.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/storage/viking_fs.py), and [`docs/en/concepts/07-retrieval.md`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/docs/en/concepts/07-retrieval.md).

Sessions are the trace-to-memory path. A session stores active messages, can externalize large tool outputs, and on async commit splits recent messages from archived messages. The archive gets raw `messages.jsonl`, generated summaries, metadata, and completion/failure markers. A second phase runs memory extraction over hydrated traces, writes memory diffs, records usage-derived relations, increments `active_count`, and produces user memories, agent memories, trajectories, experiences, tools, and session skills according to configured templates. See [`openviking/session/session.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/session/session.py), [`openviking/session/compressor_v2.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/session/compressor_v2.py), [`openviking/session/memory/extract_loop.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/session/memory/extract_loop.py), [`openviking/session/memory/memory_updater.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/session/memory/memory_updater.py), and the memory templates in [`openviking/prompts/templates/memory`](https://github.com/volcengine/OpenViking/tree/7bcd66a4510360692043b0afc466381315f85d63/openviking/prompts/templates/memory).

OpenViking exposes both pull tools and push activation. MCP tools include `find`, `search`, `read`, `list`, `remember`, `add_resource`, watch management, `grep`, `glob`, `forget`, and code-outline/search/expand tools. Those are ordinary pull surfaces. The Claude Code and Codex plugins, however, run `UserPromptSubmit` hooks that search user memory, agent memory, and agent skills, threshold and rerank results, fit them into a token budget, and inject additional context before the model acts. The LangChain middleware similarly wraps a model call, assembles session context and recall documents, and inserts an `<openviking_context>` block into the system message. See [`openviking/server/mcp_endpoint.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/server/mcp_endpoint.py), [`examples/claude-code-memory-plugin/scripts/auto-recall.mjs`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/examples/claude-code-memory-plugin/scripts/auto-recall.mjs), [`examples/codex-memory-plugin/scripts/auto-recall.mjs`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/examples/codex-memory-plugin/scripts/auto-recall.mjs), and [`openviking/integrations/langchain/middleware.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/integrations/langchain/middleware.py).

The system is built as a service with operational boundaries, not just a local library. It has account/user/agent isolation, root and admin roles, API-key or trusted modes, tenant-aware vector indexing, Prometheus metrics, task/queue/lock/session telemetry, usage audit storage, resource watch tasks, and benchmark suites for RAG, LoCoMo, tau2-bench, skills, and contention. See [`docs/en/concepts/11-multi-tenant.md`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/docs/en/concepts/11-multi-tenant.md), [`docs/en/concepts/12-metrics.md`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/docs/en/concepts/12-metrics.md), [`openviking/metrics/collectors/telemetry_bridge.py`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/metrics/collectors/telemetry_bridge.py), [`openviking/observability/usage_audit/README.md`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/openviking/observability/usage_audit/README.md), and [`benchmark`](https://github.com/volcengine/OpenViking/tree/7bcd66a4510360692043b0afc466381315f85d63/benchmark).

## Artifact analysis

- **Storage substrate:** `files` — AGFS/RAGFS under account-scoped local paths, while their public identity is the URI
- **Representational form:** `prose` `symbolic` `parametric` — prose/source files and generated summaries, code/config/structured sidecars and metadata, plus vector-index embeddings
- **Lineage:** `authored` `imported` `trace-extracted` — manual writes and integration code are authored, uploaded/watched resources are imported, and session archives drive extracted memories, summaries, relations, and diffs
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — retrieved files and memories are knowledge; skills/hooks/middleware instruct; access policy and write rules enforce; URI roots, sidecars, vectors, relations, operation validation, and extraction loops route, validate, rank, and learn

OpenViking's source content artifacts are `viking://` files and directories. Their storage substrate is AGFS/RAGFS under account-scoped local paths, while their public identity is the URI. Their representational form can be prose, code, structured data, or mixed files. Their lineage usually comes from manual writes, uploaded resources, watched resources, or session-derived memory writes. Their behavioral authority is mostly knowledge-artifact authority when retrieved or read, but a file under an agent skill or experience memory path can become system-definition material when an integration injects it as action guidance.

The generated semantic artifacts are `.abstract.md`, `.overview.md`, `.relations.json`, and vector-index rows. They are mixed artifacts: prose summaries, symbolic relation files, scalar metadata, and distributed-parametric embeddings. Their lineage is explicitly derived from source content through semantic queue processing, memory summarization, or relation writes. Their authority is retrieval and routing authority: they decide which source artifacts are found, how much context can be loaded, which level of detail is exposed, and which related artifacts are traversed. They should not be treated as source truth.

Session artifacts are trace artifacts and trace-derived artifacts in one namespace. Raw `messages.jsonl`, externalized tool results, and archive metadata preserve execution traces. Archive summaries, `memory_diff.json`, `.done`, `.failed.json`, and extracted usage relations are derived from that trace. Raw traces have evidence authority; archive summaries have compression authority; done/failed markers have lifecycle authority because later archive extraction waits on prior archive state; memory diffs have audit and lineage authority.

User and agent memory files are the most behavior-shaping retained artifacts. User memories include templates such as profile, preferences, entities, and events. Agent memories include tools, trajectories, experiences, skills, soul, and identity templates. Their form is mixed prose and symbolic fields, including page IDs, merge operations, links, backlinks, supersession, and template-specific update rules. Their lineage can be manual, MCP `remember`, HTTP/CLI writes, or LLM extraction from session traces. Their authority changes by consumer: a retrieved user preference is advice; an injected agent experience or session skill is closer to an instruction.

Integration artifacts are system-definition artifacts. MCP tool definitions define pull commands. Hook configs and auto-recall scripts define pre-action push behavior. Auto-capture scripts define what traces get persisted after a turn. LangChain middleware defines how session context and recall documents are inserted into model calls. These are authored code/config artifacts, and their behavioral authority is high because they determine when stored context becomes model input without a user explicitly asking for each item.

Resource watch, task, queue, metrics, and usage-audit artifacts are operational control artifacts. Watch tasks can refresh resource content, semantic queues update sidecars and vectors, task trackers expose commit/extraction status, and metrics/usage audit records provide lifecycle visibility. They do not normally carry domain knowledge, but they affect freshness, observability, failure handling, and governance.

The promotion path is therefore: source or trace enters a `viking://` namespace; semantic processors generate summaries, relations, and vectors; retrieval or hooks select items; session commits derive durable memory artifacts; and integrations can push selected memory back into a later model call. The risky boundary is the extraction step: OpenViking can promote raw traces into reusable agent experiences and skills without an intrinsic human review gate in the core implementation.

## Comparison with Our System

Commonplace is a Git-backed Markdown knowledge base and methodology framework. OpenViking is a service runtime for agent context. Both care about retained artifacts, lineage, context economy, and agent consumption, but they put authority in different places.

OpenViking is stronger at runtime activation. It can attach to Claude Code, Codex, OpenClaw, LangChain, MCP, and HTTP flows; search memory before a prompt; capture traces after a turn; and commit derived memories in the background. Commonplace usually relies on explicit search, typed notes, curated indexes, validation, review commands, and skills.

Commonplace is stronger at explicit review contracts. Collection files, type specs, link rules, validation, review gates, replacement archives, and source-pinned reviews make artifact authority inspectable in the repository. OpenViking has memory diffs, task state, metrics, and summaries, but an extracted experience or skill can become operational guidance before a repo-style review process has accepted it.

OpenViking uses namespace and tenant scoping as first-class mechanics. Commonplace uses directory routing and collection contracts. The OpenViking version is more dynamic and service-ready; the Commonplace version is more legible and easier to audit with ordinary Git tooling.

OpenViking's L0/L1/L2 sidecar model is a concrete implementation of frontloaded context compression. Commonplace has indexes, descriptions, tags, and note links, but it does not yet have a general generated sidecar layer for every artifact. The OpenViking approach is useful where a consumer must choose between overview and detail under a token budget.

OpenViking also demonstrates that "memory" is not one thing. The implementation separates resources, user memories, agent memories, skills, session archives, relations, vector rows, and integration hooks. That matches Commonplace's artifact-authority vocabulary better than simpler vector-store memory systems do.

**Read-back:** `both` — OpenViking supports pull read-back through MCP/HTTP/CLI/search/read/list tools, and it supports push read-back when hooks or LangChain middleware relevance-rank memories and inject selected context before a model acts

### Borrowable Ideas

Borrow the explicit namespace/access-policy boundary. Commonplace already has collection routing, but future agent-runtime integrations should treat "whose artifact is this, and under what authority may it be loaded?" as part of the address, not as metadata discovered after retrieval.

Borrow the sidecar distinction, cautiously. Generated `.abstract.md` and `.overview.md` equivalents could help Commonplace expose cheaper summaries without rewriting source notes. The key constraint is that generated sidecars must remain visibly derived, regenerable, and lower-authority than source artifacts.

Borrow budgeted pre-action recall as an optional runtime layer. The auto-recall hooks show a useful pattern: threshold results, rank them, deduplicate, respect a token budget, and degrade oversized items to URI plus score instead of forcing full text into context.

Borrow per-extraction diffs. OpenViking's `memory_diff.json` pattern is a good fit for Commonplace operations that generate or revise durable artifacts from traces, because it gives reviewers a compact before/after audit target.

Borrow the separation between raw trace, archive summary, and reusable experience. That distinction maps cleanly to Commonplace's distinction between source snapshots, notes, and system-definition artifacts. The part not to borrow unchanged is automatic promotion of extracted experiences or skills into high-authority activation without review.

Borrow low-cardinality operational telemetry for KB commands. Metrics on retrieval, semantic processing, task status, validation, and queue timing would help maintain large agent-operated KBs, provided they do not leak content or create noisy status artifacts in the repository.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
OpenViking qualifies as trace-derived. Durable behavior-shaping artifacts are derived from session traces: user memories, agent tool memories, trajectories, experiences, skills, archive summaries, usage relations, and memory diffs. The durable outputs are not merely logs; they are later retrievable and can be injected into model calls.

- **Trace source:** `session-logs` `tool-traces` `trajectories` — session messages, tool-call/output parts, externalized tool results, transcript slices, archive summaries, and trajectory memories feed extraction
- **Learning scope:** `cross-task` — extracted user memories, agent experiences, tools, skills, and summaries are durable across later sessions rather than confined to the originating turn
- **Learning timing:** `online` `staged` — plugins capture after turns and commits run asynchronously, while archive extraction and memory updates happen as a later phase
- **Distilled form:** `prose` `symbolic` `parametric` — extracted memories and summaries are prose, templates/operations/links/diffs/relations are symbolic, and written files are vectorized for later retrieval

The trace source is a session: user and assistant messages, structured content parts, tool-call/output parts, externalized tool results, recall/context usage records, and archive summaries. Claude/Codex plugins capture transcript slices after a turn and strip injected context blocks to reduce self-contamination. MCP `remember` can also create a short session and commit it.

The extraction mechanism is LLM-mediated but schema-constrained. The extractor runs a ReAct loop with memory templates, page-ID rules, link rules, read/refetch rules, and operation validation. `MemoryUpdater` applies resolved operations, preserves system metadata, writes links/backlinks, supersedes older experience where requested, vectorizes written files, and updates directory overviews.

The placement in the survey is: trace -> archive -> extracted typed memory -> generated summaries/vectors -> retrieval or push injection. It sits closer to long-term agent learning than to ordinary session compression because agent experiences, tools, and skills can change future behavior across sessions.

The main caveat is authority. OpenViking has lineage artifacts such as archive metadata and `memory_diff.json`, but the core implementation does not make human approval a necessary step before a trace-derived experience becomes a future retrieved or injected artifact.

## Read-back placement

OpenViking has both pull and push read-back. Pull read-back is implemented by `find`, `search`, `read`, `list`, `grep`, `glob`, `code_search`, `code_outline`, and related MCP/HTTP/CLI surfaces. These tools return context only when a caller asks.

**Read-back signal:** `identifier` `inferred / lexical` `inferred / embedding` — hooks and middleware narrow by account/user/agent/session/URI roots, then select by semantic search and lexical-overlap boosts over the current prompt or user text

**Faithfulness tested:** `no` — the review notes benchmark claims but did not reproduce them, and the code establishes the activation route rather than proving selected memories change behavior

Push read-back is implemented by integrations. Claude Code and Codex `UserPromptSubmit` hooks search memories and skills before the agent acts, filter by threshold and level, apply ranking boosts, deduplicate, enforce token/content budgets, and emit additional context into the prompt. LangChain middleware does the same kind of pre-call insertion by modifying the model request.

Targeting is `instance`. The hook path narrows by identifier-like scope first: configured account/user/agent identity and fixed URI roots such as `viking://user/memories`, `viking://agent/memories`, and `viking://agent/skills`. The final selector is still `inferred`, primarily `embedding` similarity from the current prompt through `/api/v1/search/find`, then score thresholds, leaf/category boosts, lexical-overlap boosts, deduplication, and token/content budgets. LangChain's middleware is mixed in the same way: the session id is an `identifier` signal for session archive context, while recall documents are selected by `inferred` search over the latest user text and optional target URI/filter constraints.

The activation timing is pre-action. The plugins inspect the current prompt, skip recall when disabled or too short, choose user/agent scopes, search selected sources, rank by semantic score and heuristics, and include only selected items before the model acts. This is stronger than always-loaded config and stronger than a manual slash command, so the `push-activation` tag applies.

The authority of pushed context is advisory but practically important. It is not hard enforcement like a validator, but it appears before model action and may include agent experiences or skills written in imperative form. Precision/recall, context dilution, and effective authority are not verified from code; the code establishes the route, not whether a selected memory changes behavior. That makes artifact authority distinctions important: user memory, agent experience, and generated summaries should not be treated as equivalent.

OpenViking's benchmark directories and README report substantial evaluation work across RAG, LoCoMo, tau2-bench, skills, and other datasets, but this review did not reproduce those benchmark results. They should be treated as project claims unless separately rerun. See [`README.md`](https://github.com/volcengine/OpenViking/blob/7bcd66a4510360692043b0afc466381315f85d63/README.md) and [`benchmark`](https://github.com/volcengine/OpenViking/tree/7bcd66a4510360692043b0afc466381315f85d63/benchmark).

## Curiosity Pass

The filesystem metaphor is useful, but it can hide how much authority lives outside files. Retrieval depends on vector rows, generated summaries, relations, hotness, reranking, tenant policy, and hook budgets. The URI is only the beginning of the behavior path.

The docs and code are not perfectly aligned at this revision. For example, the live memory templates emphasize trajectories and experiences, and the session code stores JSONL message archives. Treat the code as the source of truth when evaluating current behavior.

The plugin layer is one of the most interesting parts of the project. The auto-capture scripts explicitly strip previously injected context blocks before committing transcripts, which shows awareness of memory self-contamination. That same layer also turns extracted memory into pre-action influence, so it deserves the same review attention as the storage engine.

The agent `experiences` template is high-authority. It is designed as reusable future behavior guidance with situation, approach, and reflection fields, plus supersession support. This is closer to a system-definition artifact than to a passive knowledge note.

Tenant scoping is central to correctness. Account, user, and agent boundaries affect namespace expansion, vector rows, retrieval roots, and access checks. Root or trusted modes may be useful for deployment, but they change the safety assumptions of every memory operation.

## What to Watch

Watch whether trace-derived agent experiences and session skills gain explicit review or promotion gates before push activation uses them.

Watch whether the documentation keeps pace with the code-level memory taxonomy, session archive format, and namespace behavior.

Watch whether the benchmark suites are reproducible from the repository and whether the README claims remain tied to pinned configurations.

Watch whether recall hooks gain stronger faithfulness checks, ablation reporting, or post-action audit of which injected memories mattered.

Watch whether resource watches and semantic refresh reliably invalidate summaries, vectors, and relations after move/delete/update operations.

Watch whether metrics and usage-audit surfaces stay low-cardinality, tenant-safe, and content-safe in multi-tenant deployments.

## Relevant Notes

- [[../trace-derived-learning-techniques-in-related-systems]]
- [[../../notes/agent-memory-requirements/use-trace-derived-extraction]]
- [[../../notes/axes-of-artifact-analysis]]
- [[../../notes/frontloading-spares-execution-context]]
- [[../../notes/knowledge-storage-does-not-imply-contextual-activation]]
- [[../../notes/definitions/knowledge-artifact]]
- [[../../notes/definitions/system-definition-artifact]]
