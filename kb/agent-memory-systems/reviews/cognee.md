---
description: "Cognee review: graph/vector agent memory control plane with session cache, recall routing, trace-derived improve loops, MCP tools, and decorator push"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Cognee

Cognee, by topoteretes, is an open-source Python memory control plane for agents. At the reviewed commit it ingests raw data into datasets, cognifies it into a graph plus vector indexes, exposes search/recall/remember/improve APIs, keeps optional session memory and agent traces in cache, bridges session-derived feedback and traces back into the permanent graph, and ships MCP, CLI, cloud, UI, and decorator integrations for agent use.

**Repository:** https://github.com/topoteretes/cognee

**Reviewed commit:** [cfb0aa4d0b3ae0154cf9f24e5908263d565341f4](https://github.com/topoteretes/cognee/commit/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4)

**Last checked:** 2026-06-04

## Core Ideas

**The canonical long-term memory is a graph-backed semantic layer, not a note file.** `add()` stores input data in a dataset, `cognify()` classifies documents, chunks text, extracts graph structure and summaries, then persists nodes, edges, and embeddings through graph/vector engines ([cognee/api/v1/add/add.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/api/v1/add/add.py), [cognee/api/v1/cognify/cognify.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/api/v1/cognify/cognify.py), [cognee/tasks/storage/add_data_points.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/tasks/storage/add_data_points.py)). The default storage stack is multi-store: Ladybug/Kuzu-style graph, LanceDB vectors, SQLite relational metadata, and filesystem cache unless configured otherwise ([cognee/infrastructure/databases/graph/config.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/infrastructure/databases/graph/config.py), [cognee/infrastructure/databases/vector/config.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/infrastructure/databases/vector/config.py), [cognee/infrastructure/databases/relational/config.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/infrastructure/databases/relational/config.py), [cognee/infrastructure/databases/cache/config.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/infrastructure/databases/cache/config.py)).

**The public memory vocabulary is `remember`, `recall`, `forget`, and `improve`.** `remember()` either runs permanent `add + cognify` or writes typed session entries, `recall()` routes across graph/session/trace/global-context sources, and `improve()` enriches the graph, applies feedback weights, persists session Q&A and trace feedback, optionally builds a global context index, and syncs graph context back to sessions ([cognee/api/v1/remember/remember.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/api/v1/remember/remember.py), [cognee/api/v1/recall/recall.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/api/v1/recall/recall.py), [cognee/api/v1/improve/improve.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/api/v1/improve/improve.py)).

**Context efficiency is retrieval-first but can still assemble complex context.** Graph completion searches vector collections for relevant nodes/edges, projects a graph fragment, ranks triplets, resolves them to text, and optionally summarizes or prepends global-context summaries; `recall()` also bounds session and trace hits with `top_k` and can auto-route query type by lexical rules ([cognee/modules/retrieval/utils/brute_force_triplet_search.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/retrieval/utils/brute_force_triplet_search.py), [cognee/modules/retrieval/graph_completion_retriever.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/retrieval/graph_completion_retriever.py), [cognee/modules/retrieval/graph_summary_completion_retriever.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/retrieval/graph_summary_completion_retriever.py), [cognee/api/v1/recall/query_router.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/api/v1/recall/query_router.py)). The volume is bounded by `top_k`, `wide_search_top_k`, summary options, graph filters, session `last_n`, and decorator truncation; the complexity can still be high because graph triplets, summaries, session history, trace feedback, and tool/skill manifests may be combined.

**Session memory is deliberately weaker and faster than permanent graph memory.** Session Q&A, feedback, graph usage ids, and agent trace steps live behind `SessionManager` in a cache backend; recall can search session and trace entries by keyword before or alongside graph retrieval, while `improve()` is the promotion bridge into durable graph memory ([cognee/infrastructure/session/session_manager.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/infrastructure/session/session_manager.py), [cognee/memory/entries.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/memory/entries.py), [cognee/tasks/memify/extract_agent_trace_feedbacks.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/tasks/memify/extract_agent_trace_feedbacks.py)).

**Agent integrations are both explicit and ambient.** The MCP server exposes `remember`, `recall`, `forget`, and `improve`; the SDK decorator retrieves graph/session memory before a wrapped async function, stores trace outcomes after it runs, and `LLMGateway` prepends active memory context to structured-output calls ([cognee-mcp/src/server.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee-mcp/src/server.py), [cognee/modules/agent_memory/decorator.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/agent_memory/decorator.py), [cognee/modules/agent_memory/runtime.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/agent_memory/runtime.py), [cognee/infrastructure/llm/LLMGateway.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/infrastructure/llm/LLMGateway.py)).

**Skills and tools make part of the memory executable.** Cognee can parse `SKILL.md` files into graph `Skill` nodes, resolve a skill catalog for the agentic retriever, let the LLM load full procedure bodies on demand, and record `SkillRun` nodes after tool-loop use ([cognee/modules/tools/skill_parser.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/tools/skill_parser.py), [cognee/modules/tools/ingest_skills.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/tools/ingest_skills.py), [cognee/modules/retrieval/agentic_retriever.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/retrieval/agentic_retriever.py), [cognee/modules/tools/builtin/load_skill.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/modules/tools/builtin/load_skill.py)).

## Artifact analysis

- **Storage substrate:** `graph` — The primary behavior-shaping retained state is graph nodes and edges queried as agent memory; secondary substrates include vector indexes for ranking, relational metadata for datasets/users/permissions/pipeline/search logs, cache-backed session/trace entries, local file storage for ingested data, MCP/cloud service objects, and optional alternative graph/vector/cache providers.
- **Representational form:** `prose` `symbolic` `parametric` — Document chunks, summaries, Q&A, session feedback, graph-context text, and skill procedures carry prose; datasets, DataPoints, node sets, graph edges, query routes, ACLs, typed memory entries, session metadata, tool schemas, and pipeline state are symbolic; embeddings and vector distances supply parametric retrieval signals.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author memories, skills, feedback, and DataPoints; documents/files/URLs and structured data are imported; session Q&A, graph-element usage, trace steps, trace feedback, skill-run records, access timestamps, and feedback/frequency weights are extracted from later use.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Retrieved graph/session/trace context advises as knowledge; skill bodies and decorator-injected memory can instruct LLM calls; query routers, node sets, ACL scopes, MCP tools, and agentic tool manifests route access; Pydantic models, permission checks, config validation, and path-safety helpers validate; vector scores, triplet importance, feedback weights, frequency weights, and summaries rank; `improve()` and trace persistence update learned state.

**Permanent graph memory.** Storage substrate: configured graph and vector engines plus relational dataset ownership records. Representational form: symbolic DataPoints, graph nodes/edges, node sets, and prose summaries/chunks indexed by embeddings. Lineage: imported and LLM-extracted from ingested data, or directly authored as DataPoints and skills. Behavioral authority: knowledge and ranking for search/recall, and instruction when Skill procedures are loaded by the agentic retriever.

**Session cache and trace entries.** Storage substrate: configured cache backend, defaulting to filesystem cache with Redis/Tapes alternatives. Representational form: symbolic `SessionQAEntry` and `SessionAgentTraceEntry` records with prose question/context/answer/feedback fields. Lineage: trace-extracted from conversations, decorator-wrapped calls, tool/function results, and feedback updates. Behavioral authority: knowledge for session recall and future LLM completions, learning input for graph weights and trace persistence.

**Retrieval indexes and global context index.** Storage substrate: vector collections and graph/global-context summary nodes. Representational form: parametric embeddings plus symbolic bucket/root summary records and prose summary text. Lineage: derived from graph text summaries, edge types, DataPoint index fields, triplets, and optional graph/vector bucketing. Behavioral authority: routing and ranking for graph completion, summary completion, agent memory, and global-context prelude selection ([cognee/memify_pipelines/global_context_index.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/memify_pipelines/global_context_index.py), [cognee/tasks/memify/global_context_index](https://github.com/topoteretes/cognee/tree/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/tasks/memify/global_context_index)).

**Feedback and frequency weights.** Storage substrate: graph node/edge properties and session memify metadata. Representational form: symbolic numeric weights and processed flags. Lineage: trace-extracted from retrieved graph element ids, QA feedback scores, and frequency records. Behavioral authority: ranking and learning, because later triplet importance can include feedback influence and memify avoids reprocessing already-applied session entries ([cognee/tasks/memify/apply_feedback_weights.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/tasks/memify/apply_feedback_weights.py), [cognee/tasks/memify/apply_frequency_weights.py](https://github.com/topoteretes/cognee/blob/cfb0aa4d0b3ae0154cf9f24e5908263d565341f4/cognee/tasks/memify/apply_frequency_weights.py)).

**MCP and agent decorator surfaces.** Storage substrate: repository code plus runtime server/decorator state. Representational form: symbolic tool schemas and decorator configuration, with prose context inserted into LLM input. Lineage: authored integration surface. Behavioral authority: routing for memory tools, instruction for injected memory context, and learning when wrapped calls persist traces or trigger trace memification.

Promotion path: Cognee has a clear ladder from session trace to durable memory. A wrapped call or MCP/session write can first become cached Q&A or trace feedback, then `improve(session_ids=...)` can apply feedback weights, cognify session Q&A, persist trace feedback into a graph node set, enrich triplet embeddings, and sync a graph-context snapshot back into session cache. The ladder increases durability and reach, but it does not by itself add semantic review of whether the extracted feedback is true or wise.

## Comparison with Our System

| Dimension | Cognee | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory infrastructure for agents over arbitrary data | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | Graph/vector DataPoint, edge, summary, session entry, or skill node | Typed Markdown artifact with collection/type contract |
| Source of truth | Configured graph/vector/relational/cache stores | Repository files plus generated indexes and reports |
| Write path | Ingest/cognify, session writes, trace persistence, feedback weighting, improve pipelines | Authored edits, snapshots, validation, semantic review, index refresh |
| Read-back | Pull APIs/MCP/CLI plus decorator and LLM-gateway push | Mostly explicit pull through search, indexes, links, skills, and loaded instructions |
| Governance | ACLs, Pydantic validation, dataset scopes, config checks, path-safety, tests | Schema validation, collection contracts, git diffs, citations, semantic gates |

Cognee is stronger as a deployable memory substrate: it has APIs, MCP tools, user/dataset permissioning, multiple backing stores, cloud routing, search modes, and session bridges. Commonplace is stronger as a reviewable knowledge corpus: the durable artifacts are inspectable Markdown with explicit types, citations, indexes, and semantic review.

The sharpest tradeoff is authority. Cognee can make memory operational quickly by pushing retrieved context into LLM calls and by feeding trace-derived signals back into graph ranking. Commonplace keeps behavior-shaping artifacts slower and more reviewable: agents have to load or be instructed by files whose provenance is visible in git.

### Borrowable Ideas

**Use sessions as a staging substrate, not the canonical artifact.** Ready now as a design principle. Cognee's session cache is useful precisely because it is fast and disposable, while `improve()` is the explicit promotion point.

**Record which graph elements were used, then attach feedback to those ids.** Needs a concrete Commonplace retrieval surface. If Commonplace starts serving ranked context bundles, storing loaded artifact ids and later feedback would be a better ranking signal than broad usage counts.

**Decorator-local memory context is a useful push interface.** Needs care. Commonplace could use workflow-local decorators or hooks for narrow tools, but only with visible provenance and strict budgets.

**Progressive skill loading is worth borrowing.** Ready for agent-tool design. Cognee's agentic retriever shows a clean split between a compact skill catalog and a `load_skill` tool that opens the full procedure only when needed.

**Do not borrow graph/vector storage as a substitute for semantic governance.** Ready as a constraint. Cognee has strong infrastructure validation, but graph extraction and trace feedback still need review before they should carry high behavioral authority in a methodology KB.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from SDK, CLI, MCP, direct DataPoint/skill ingestion, and feedback APIs; automatic writes include ingestion pipelines, graph extraction, summary generation, vector indexing, session Q&A writes, decorator trace persistence, LLM or fallback trace-feedback generation, feedback/frequency weighting, global-context indexing, skill-run recording, graph-to-session sync, and access timestamp updates when enabled.

**Curation operations:** `consolidate` `synthesize` `evolve` `promote` — Cognify and summary/global-context pipelines consolidate raw document chunks into summaries and graph context; LLM graph extraction and trace persistence synthesize new graph entries from documents or session traces; feedback and frequency pipelines evolve node/edge weights in place; `improve()` promotes session Q&A and trace feedback into permanent graph memory and can sync enriched graph knowledge back to sessions.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Cognee consumes session Q&A, feedback events, graph-element usage ids, agent trace steps with method parameters/returns/errors, skill-run tool traces, and usage/access events.

**Learning scope:** `per-project` `cross-task` — Datasets and node sets scope graph memory; sessions scope short-term traces; persisted session and trace-derived graph entries can affect later tasks in the same dataset.

**Learning timing:** `online` `staged` — Decorator/session writes and session completion storage happen during operation; `improve()`, memify pipelines, global-context indexing, feedback-weight application, and graph-to-session sync are staged workflows.

**Distilled form:** `prose` `symbolic` `parametric` — Traces become prose session feedback, Q&A text, graph-context summaries, and skill-run summaries; symbolic graph nodes/edges, weights, node sets, QA metadata, and trace records; and parametric embeddings or vector-ranked summaries.

**Extraction.** Trace extraction is split across several paths. `SessionManager.add_agent_trace_step()` stores a tool/function step and can use an LLM to summarize method returns into `session_feedback`; `extract_agent_trace_feedbacks()` turns stored trace feedback or raw returns into text blobs; `improve()` persists Q&A and trace feedback into the graph and applies feedback weights to graph elements used during retrieval.

**Scope and timing.** The short-term unit is a `(user_id, session_id)` cache entry. The durable unit is a dataset-scoped graph artifact or weight update. Periodic decorator persistence through `persist_session_trace_after` can move recent trace steps into the graph during an agent workflow, while explicit `improve(session_ids=...)` performs the broader staged bridge.

**Survey fit.** Cognee strengthens the survey split between raw trace artifacts and distilled behavior-shaping artifacts. Raw Q&A and trace steps are cache-resident knowledge artifacts; distilled session feedback, graph weights, graph nodes, and synced graph context can later shape ranking or LLM input.

## Read-back

**Read-back:** `both` — Cognee is pull through SDK/CLI/MCP `search`, `recall`, `memory_search`, graph/session/trace lookups, and UI/API calls; it is push when `agent_memory` retrieves graph/session memory before a wrapped function and `LLMGateway` prepends that memory to the next structured-output prompt.

**Read-back signal:** `coarse` `inferred / lexical` `inferred / embedding` — Recent session feedback is a coarse last-N push when enabled; session and trace recall use keyword overlap; graph memory uses inferred vector search over DataPoint fields, edge types, summaries, and triplets, with optional graph expansion and global-context summary search.

**Faithfulness tested:** `no` — The repository tests retrieval, decorator context assembly, LLMGateway injection, session trace persistence, MCP payloads, and cache behavior, but I did not find behavioral ablations showing that pushed memory reliably changes downstream model behavior correctly.

**Direction edge cases.** `recall()` with a `session_id` is pull even when it searches session first and falls through to graph, because the caller asked. The decorator path is push for the receiving LLM call: a wrapped function can cause Cognee memory to be gathered before the function's LLM call without that model first deciding to search memory. MCP tools expose pull capability; a host agent may decide to call them proactively, but that host policy is outside this repository.

**Targeting and signal.** Decorator graph memory is instance-targeted by a query derived from a fixed string, a named method parameter, or the first usable string argument. Session memory push is coarser: it takes the last N trace feedback strings for the configured session. Graph completion ranks vector hits, maps them through a graph fragment, applies distance/feedback weighting, then resolves selected triplets into text.

**Injection point.** Push happens pre-invocation relative to the model call. `agent_memory` retrieves context before the wrapped async function runs, stores it in a context variable, and `LLMGateway._inject_agent_memory()` prepends it when a structured-output call occurs. Trace persistence in the decorator `finally` block and later `improve()` stages are write-side maintenance, not read-back after an action.

**Selection, scope, and complexity.** Selection is bounded by `memory_top_k`, `MAX_MEMORY_CONTEXT_LENGTH`, session `last_n`, `top_k`, graph dataset permissions, node-set/node-name filters, `wide_search_top_k`, optional neighborhood depth, summary options, and global-context top-k. Complexity can be substantial because returned memory may include graph triplets, summaries, recent trace feedback, graph-context snapshots, skill catalogs, tool manifests, and conversation history.

**Authority at consumption.** Plain recall/search results are advisory knowledge. Decorator-injected memory becomes prompt context for LLM calls and therefore has instruction-like practical force, although the code labels it "Additional Memory Context" rather than a hard system rule. Agentic tools and skill manifests route allowed actions. Effective authority depends on host use, prompt templates, and model compliance.

**Other consumers.** Humans and operators consume the same memory through CLI output, MCP results, local UI, visualization endpoints, session/admin routes, logs, and cloud/API clients. The system is therefore both an agent memory layer and an operator-facing data/graph infrastructure product.

## Curiosity Pass

**The README's four verbs are real, but they hide a large legacy API.** `remember`/`recall`/`forget`/`improve` are implemented, yet the older `add`/`cognify`/`search`/`memify` surface remains the deeper machinery.

**Push is implemented indirectly through the LLM gateway.** The decorator does not pass memory as an argument to the wrapped function. It sets context, and Cognee's own LLM gateway injects that context into structured-output calls. A wrapped function that calls another LLM client would not necessarily receive the memory.

**"Improve" is more infrastructural than epistemic.** It can apply weights, persist traces, and build indexes, but it does not prove the learned content is correct. The quality layer is separate from the promotion mechanism.

**Session memory is intentionally lossy.** Recent session feedback can be useful as compact context, but the default feedback string may be a generated or deterministic summary of a function result, not the full trace.

**The skill system is a bridge from knowledge memory toward system-definition memory.** Ingested skills are graph nodes for retrieval, but once `load_skill` returns the procedure body inside an agentic loop, the artifact behaves more like an instruction.

## What to Watch

- Whether `agent_memory` integration expands beyond `LLMGateway`; that decides whether push memory is a general agent facility or only works for Cognee-mediated LLM calls.
- Whether feedback and frequency weights become default influences in user-facing search; that would make trace-derived ranking more behaviorally central.
- Whether global-context indexing becomes a default read path; that would change Cognee from local top-k graph recall toward hierarchical memory summaries.
- Whether session trace promotion gains semantic review or evaluator gates; without that, `improve()` remains a durability/ranking bridge rather than a truth-maintenance mechanism.
- Whether MCP hosts or external plugins add automatic prompt hooks; that would increase push read-back beyond the SDK decorator reviewed here.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Cognee stores graph and session memory, but only explicit calls and decorator/LLMGateway hooks decide when it reaches model context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: graph nodes, vector indexes, cache entries, feedback weights, skill bodies, and tool schemas carry different lineage and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: graph triplets, summaries, Q&A entries, trace feedback, and recall results mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skill procedures, tool schemas, query routing, ACLs, and decorator/LLMGateway injection shape later behavior more strongly.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Cognee turns session Q&A, feedback, and tool traces into durable graph memory and ranking signals.
