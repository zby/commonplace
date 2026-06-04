---
description: "Hindsight review: service-backed agent memory with LLM fact extraction, observations, hybrid recall, integrations, hooks, transfer, and trace-derived learning"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Hindsight

Hindsight, by Vectorize, is a service-backed agent memory system for retaining documents, conversations, tool traces, and application events as extracted facts, linked entities, observations, mental models, directives, and recall indexes. At the reviewed commit it ships a FastAPI/MCP service, generated clients, CLI, embedded Python/Node launchers, many framework integrations, Claude Code and Codex hook plugins, operation/audit/LLM traces, bank transfer tooling, and provider/runtime optimizations.

**Repository:** https://github.com/vectorize-io/hindsight

**Reviewed commit:** [7683f29004ab9d88e0ef3f0f18b8ffe6fc741905](https://github.com/vectorize-io/hindsight/commit/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905)

**Last checked:** 2026-06-04

## Core Ideas

**The retained memory is a bank-scoped database, not a file vault.** A bank contains documents, chunks, memory units, entities, entity cooccurrences, memory links, observations, mental models, directives, async operations, webhooks, audit rows, and LLM request traces. The primary runtime substrate is PostgreSQL/Oracle-style relational storage with pgvector-style embeddings, BM25/text-search indexes, graph links, and per-bank/schema isolation ([hindsight-api-slim/hindsight_api/models.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/models.py), [hindsight-api-slim/hindsight_api/alembic/versions/5a366d414dce_initial_schema.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/alembic/versions/5a366d414dce_initial_schema.py), [hindsight-api-slim/hindsight_api/alembic/versions/h3c4d5e6f7g8_mental_models_v4.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/alembic/versions/h3c4d5e6f7g8_mental_models_v4.py)).

**Retain is a trace/document-to-fact pipeline.** Retain chunks input content, resolves or creates a document id, skips unchanged chunks on delta retains, calls an LLM fact extractor, generates embeddings, resolves entities, inserts memory units, and creates temporal, semantic, and causal links. Conversation and coding-agent integrations feed transcripts through this same path, so session traces become world/experience facts rather than being stored only as raw logs ([hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py), [hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py), [hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/retain/fact_storage.py)).

**The distinctive learned layer is observations plus mental models.** Consolidation processes unconsolidated world/experience memories, asks an LLM to create, update, or delete observations, records `proof_count`, `source_memory_ids`, tags, temporal rollups, and optional history, and can trigger stale mental-model refreshes. Mental models are separate query-defined documents refreshed through reflect, with update history and structured delta support ([hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py), [hindsight-api-slim/hindsight_api/engine/reflect/agent.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/reflect/agent.py), [hindsight-api-slim/hindsight_api/engine/reflect/observations.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/reflect/observations.py), [hindsight-api-slim/hindsight_api/engine/memory_engine.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/memory_engine.py)).

**Recall is hybrid and budgeted.** Recall combines semantic vector search, BM25, graph/link expansion, temporal retrieval, reciprocal-rank fusion or interleaving, cross-encoder reranking, recency/temporal/proof-count boosts, tag/type/date filters, and token limits. Context efficiency is therefore retrieval-and-rerank bounded, but the returned object can still be complex because it may include facts, observations, chunks, entities, links, source facts, tool traces, and ranking diagnostics ([hindsight-api-slim/hindsight_api/engine/search/retrieval.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/search/retrieval.py), [hindsight-api-slim/hindsight_api/engine/search/reranking.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/search/reranking.py), [hindsight-api-slim/hindsight_api/engine/response_models.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/response_models.py)).

**Read-back exists both as explicit tools and as pre-prompt integration hooks.** The base API/SDK/CLI/MCP surfaces expose retain, recall, reflect, mental-model, directive, document, operation, audit, and webhook operations. Some integrations leave recall to explicit tools; others wire automatic recall into the next model call: Claude Code and Codex `UserPromptSubmit` hooks emit `additionalContext`, OpenAI Agents and Strands expose dynamic `memory_instructions`, and LangGraph can insert a `SystemMessage` or state field before the agent node ([hindsight-api-slim/hindsight_api/mcp_tools.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/mcp_tools.py), [hindsight-integrations/claude-code/scripts/recall.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-integrations/claude-code/scripts/recall.py), [hindsight-integrations/codex/scripts/recall.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-integrations/codex/scripts/recall.py), [hindsight-integrations/openai-agents/hindsight_openai_agents/tools.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-integrations/openai-agents/hindsight_openai_agents/tools.py), [hindsight-integrations/strands/hindsight_strands/tools.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-integrations/strands/hindsight_strands/tools.py), [hindsight-integrations/langgraph/hindsight_langgraph/nodes.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-integrations/langgraph/hindsight_langgraph/nodes.py)).

**Operational affordances are service-grade.** The newer checkout includes async operations, worker retry/backoff, graph-maintenance queue top-up after deletes, bank/document transfer that strips embeddings and regenerates them on import, audit logs, LLM request traces, webhooks, configurable operation validators, and Gemini cached-content management. These do not change the memory taxonomy, but they make Hindsight closer to a deployable memory platform than a research memory library ([hindsight-api-slim/hindsight_api/engine/graph_maintenance.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/graph_maintenance.py), [hindsight-api-slim/hindsight_api/engine/transfer/export.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/transfer/export.py), [hindsight-api-slim/hindsight_api/engine/transfer/importer.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/transfer/importer.py), [hindsight-api-slim/hindsight_api/engine/audit.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/audit.py), [hindsight-api-slim/hindsight_api/engine/llm_trace.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/llm_trace.py), [hindsight-api-slim/hindsight_api/engine/providers/gemini_cache.py](https://github.com/vectorize-io/hindsight/blob/7683f29004ab9d88e0ef3f0f18b8ffe6fc741905/hindsight-api-slim/hindsight_api/engine/providers/gemini_cache.py)).

## Artifact analysis

- **Storage substrate:** `rdbms` — The lead durable substrate is a relational database schema. Vector indexes, full-text indexes, graph links, object/file storage, async queues, webhooks, and service objects are supporting surfaces; they do not displace the bank-scoped database as the source of truth.
- **Representational form:** `prose` `symbolic` `parametric` — Documents, chunks, fact text, observations, mental-model content, directives, prompts, and recalled context are prose; bank ids, document ids, tags, metadata, schemas, API/tool definitions, links, timestamps, operation records, source ids, and validation/config records are symbolic; embeddings, HNSW/vector distance, BM25 scores, cross-encoder scores, cached LLM prefixes, and learned reranking signals are parametric.
- **Lineage:** `authored` `imported` `trace-extracted` — Banks, directives, mental-model definitions, tags, and integration config are authored; documents/files/API payloads are imported; coding-agent transcripts, user/assistant messages, optional tool calls, LLM traces, extracted facts, observations, and refreshed mental models can be trace-extracted or derived from trace-extracted rows.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Recalled facts, chunks, observations, and mental models advise as knowledge; directives and injected memory blocks can become prompt instructions; bank ids, tags, schemas, tenant context, tool lists, operation validators, and integrations route and constrain access; schema checks, operation validators, audits, and tests validate; retrieval, RRF, cross-encoders, boosts, and graph expansion rank; retain/consolidation/refresh loops update learned memory state.

**Documents, chunks, and raw memory units.** Storage substrate: relational rows in `documents`, `chunks`, and `memory_units`. Representational form: original/chunk prose plus symbolic ids, tags, metadata, fact type, timestamps, document ids, and embeddings. Lineage: imported content or trace-derived transcript content, then LLM-extracted into facts. Behavioral authority: source evidence for recall, consolidation, mental-model refresh, transfer, and audit.

**Entities, cooccurrences, and memory links.** Storage substrate: relational graph tables over memory-unit ids. Representational form: symbolic topology with link types and weights plus entity names. Lineage: extracted, resolved, and maintained from stored facts. Behavioral authority: routing and ranking for graph/temporal/causal recall; maintenance top-up restores access structure after deletions.

**Observations.** Storage substrate: `memory_units` with `fact_type='observation'`, proof counts, source memory ids, tags, optional history, and embeddings. Representational form: prose observation text plus symbolic provenance and parametric retrieval. Lineage: trace-extracted or imported raw memories consolidated by an LLM and post-processed by duplicate/update/delete logic. Behavioral authority: higher-salience knowledge and learning output; proof count and source ids also affect ranking and verification.

**Mental models and directives.** Storage substrate: `mental_models` and `directives` tables. Representational form: prose content/rules plus symbolic trigger, subtype, tags, priority, active state, structured content, refresh metadata, and history. Lineage: authored definitions, then refreshed through reflect against selected memories. Behavioral authority: mental models advise and can be pulled/injected; directives are explicit instruction artifacts used by reflect and integration prompts.

**Integration wrappers and hooks.** Storage substrate: repository packages, generated clients, plugin manifests, hook JSON, and host configuration. Representational form: symbolic tool/hook schemas plus prose prompts and preambles. Lineage: authored system-definition artifacts. Behavioral authority: routing and instruction; some wrappers only expose callable tools, while hook/nodes/instruction wrappers actively push recall into the next agent context.

**Transfer, audit, trace, and cache records.** Storage substrate: transfer ZIP payloads, audit rows, LLM request rows, async operation rows, webhook rows, and in-process Gemini cache entries. Representational form: symbolic operational metadata plus prose request/response snippets. Lineage: derived from runtime operations. Behavioral authority: governance, debugging, migration, retry, cost, and reproducibility support, not primary memory advice.

Promotion path: Hindsight has a strong automatic promotion path from raw document/session content to extracted facts, linked entities, observations, mental models, and prompt-injected recall. The promotion strengthens read utility, but much of the epistemic judgment is LLM-mediated and stored as rows/history rather than as a human-reviewable proposal artifact.

## Comparison with Our System

| Dimension | Hindsight | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory service for agents and applications | Git-native methodology KB for agents and maintainers |
| Source of truth | Bank-scoped relational schema with derived indexes and traces | Typed Markdown artifacts with git history, validation, and review |
| Write path | API/SDK/MCP/hooks retain content; LLM extraction and consolidation derive facts/observations | Authored edits, source snapshots, validation, review gates, generated indexes |
| Read-back | Explicit recall/reflect plus push integrations that inject recalled memory | Mostly pull through `rg`, indexes, links, skills, and loaded instructions |
| Learning | Trace/document extraction, observation consolidation, mental-model refresh | Human/agent-authored notes plus review, validation, and explicit promotion |
| Governance | Schema, operation validators, audit logs, LLM traces, webhooks, transfer | Collection contracts, type specs, citations, git diffs, semantic review gates |

Hindsight is stronger where an application needs low-friction runtime memory, automatic extraction, cross-framework integration, user/session scoping, and prompt-time recall. Commonplace is stronger where durable knowledge should be inspectable as authored prose with explicit source citations, review comments, and deterministic validation.

The central tradeoff is authority opacity. Hindsight can turn session traces into behavior-shaping observations quickly, but its consolidation and refresh decisions are mostly LLM outputs recorded in database state. Commonplace would usually require a visible note edit, source citation, and review path before a distilled claim starts steering later agents.

### Borrowable Ideas

**Separate raw facts from consolidated observations.** Ready now as vocabulary. Commonplace already separates sources, notes, and indexes; Hindsight's `source_memory_ids` plus `proof_count` pattern is a concrete way to represent how much raw evidence backs a distilled claim.

**Add explicit operation traces for expensive semantic writes.** Ready with a concrete use case. Hindsight's LLM trace rows link calls to created and consumed memory ids; Commonplace review/ingest commands could retain a compact operation manifest for generated notes and indexes.

**Use push read-back only where the host can bound it.** Ready as a constraint. Hindsight's hook integrations cap query length and recalled tokens; Commonplace should keep any automatic memory injection similarly budgeted and scoped.

**Borrow transfer without importing hidden authority.** Useful for generated views or experiments. Hindsight's export/import regenerates embeddings and links in the target, which maps to Commonplace generated indexes better than to canonical notes.

**Do not borrow unreviewed observation promotion for methodology claims.** Ready as a negative rule. Hindsight's auto-observations are useful operational memory; Commonplace claims need citations and review before becoming durable methodology.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from API/SDK/CLI/MCP calls for retain, bank config, directives, mental models, documents, webhooks, and operations; automatic writes include LLM fact extraction, embeddings, entity resolution, link creation, delta/upsert rewriting, async retain/file conversion, graph maintenance, audit/LLM trace logging, observation consolidation, mental-model refresh, webhook delivery, and integration hooks that retain session transcripts.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` — Consolidation condenses groups of stored facts into observations; exact duplicate creates and repeated updates are suppressed or collapsed; existing observations and mental models are updated with new evidence/history; reflect/consolidation can synthesize new higher-level observations or model content from multiple stored memories.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` — Claude Code and Codex integrations read JSONL transcripts, optionally include tool calls, format the retained transcript, attach session metadata/tags, and submit it to retain. API users can also submit conversations, messages, documents, and application events as retained content.

**Learning scope:** `per-project` `cross-task` — Banks, tags, dynamic bank-id derivation, document ids, sessions, and user/project metadata scope what traces become visible. A bank can preserve learned observations across tasks, sessions, and integrations, while tags can isolate user/session/project slices.

**Learning timing:** `online` `staged` — Hooks can retain after turns and recall before prompts during normal agent operation; async retain, background consolidation, graph maintenance, file conversion, and mental-model refresh are staged worker operations.

**Distilled form:** `prose` `symbolic` `parametric` — Trace content becomes prose facts/observations/mental-model text, symbolic entities/links/tags/source ids/operations, and parametric embeddings/reranker scores/cached-prefix behavior.

**Extraction.** The first-stage oracle is the configured retain LLM, constrained by Pydantic models and extraction prompts; the second-stage oracle is the consolidation or reflect LLM, constrained by create/update/delete response models, duplicate guards, live-source checks, source ids, and optional structured delta application.

**Scope and timing.** The raw trace can be a full session, chunked window, latest turn, file/document, or application event. The behavior-shaping result is not just the raw retained transcript: it is the extracted and consolidated database state that later recall/reflect/hooks select.

**Survey fit.** Hindsight is a trace-to-service-memory system with an unusually broad integration surface. It strengthens the survey axis where traces become durable learned observations and prompt-time recall, while also showing the governance gap that appears when learned rows have no git-style review artifact.

## Read-back

**Read-back:** `both` — Hindsight supports explicit pull through API/SDK/CLI/MCP recall, reflect, document, mental-model, and directive calls, and it supports push where integrations wire recall into the host context before a model call.

**Read-back signal:** `inferred / lexical` `inferred / embedding` — Push integrations usually fire on each user prompt or graph turn, but they derive the selected memories from prompt text or recent transcript text using Hindsight recall, whose retrieval path includes BM25/text search and vector semantic search before graph/temporal expansion and reranking.

**Faithfulness tested:** `no` — The repo has unit/integration tests for recall, hooks, formatting, tracing, and API behavior, but I did not find a with/without behavioral ablation showing that injected memories change downstream agent behavior correctly.

Push occurs at the pre-invocation assembly point. Claude Code and Codex `UserPromptSubmit` hooks call recall, format a `<hindsight_memories>` block, and return it as `hookSpecificOutput.additionalContext`. LangGraph recall nodes insert a `SystemMessage` or state field before the agent node, and OpenAI Agents/Strands-style `memory_instructions` functions compose recalled memories into dynamic instructions. Tool-only integrations remain pull until the agent chooses a recall/reflect tool.

Selection is bounded by query truncation, recall budgets, max-token settings, type filters, tags, tag groups, date filters, top-k/result caps, and reranking. Actual context quality is not knowable from code alone: a host can over-broaden the recall query, misuse tags, place the memory block poorly, or treat advisory memories as stronger than their source evidence warrants.

Consumption authority depends on integration. API/SDK/MCP recall results are advisory knowledge; directives and `memory_instructions` can become prompt instructions; operation validators and schemas constrain service access rather than model beliefs. Effective authority requires host-level prompt behavior and cannot be inferred from Hindsight storage alone.

## Curiosity Pass

**The system is both memory store and memory platform.** The current checkout is no longer just retain/recall/reflect; it includes transfer, traces, audits, webhooks, embedded launchers, multi-framework packages, and plugin hooks. That broadens adoption but also spreads authority across host integrations.

**The README's learning claim is implementation-backed, but not review-backed.** There is real trace-derived consolidation into observations and mental models. The missing piece, from a Commonplace perspective, is a human-readable rationale artifact for each learned observation/update.

**Original text is not just transient.** The retain API and docs emphasize extracted facts, but the schema and transfer path preserve document/chunk text and use it for richer recall, import, and source expansion. That is a useful fidelity affordance if consumers keep source ids visible.

**Push read-back is integration-dependent.** Hindsight itself exposes recall and reflect; the automatic context path lives in wrappers and hooks. Reviews of Hindsight should therefore distinguish service capability from deployed host behavior.

**Provider caching is context engineering, not memory.** Gemini cached-content support reduces repeated prompt prefix cost and latency for stable schemas/prompts, but it is not a retained knowledge artifact that later agents should believe.

## What to Watch

- Whether observation/consolidation decisions gain durable rationale artifacts or review states; that would make learned memories easier to govern.
- Whether default integrations shift from raw fact recall toward observation-only recall; that would change context density and the authority of consolidated claims.
- Whether transfer/import starts preserving more source/rationale history across banks; that would affect lineage quality during migrations.
- Whether operation validators become a public policy layer for read/write authorization; that would make Hindsight's system-definition artifact surface stronger.
- Whether benchmarks include prompt-injection faithfulness tests for auto-recall hooks, not only memory retrieval accuracy.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Hindsight converts session transcripts and retained interaction content into facts, observations, mental models, and prompt-time recall.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Hindsight's store can be pull-only through the API, but specific integrations add push read-back.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Hindsight bundles database rows, prompts, embeddings, links, directives, integrations, and traces under different authority paths.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: coding-agent transcripts and application events become learned observations for later tasks.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: facts, chunks, observations, and mental models mostly advise future action.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: directives, validators, schemas, hooks, tool definitions, and integration configs route or instruct future behavior.
