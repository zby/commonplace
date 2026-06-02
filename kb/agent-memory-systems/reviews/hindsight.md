---
description: "Hindsight review: Vectorize server/API memory bank with LLM fact extraction, observations, mental models, directives, hooks, and push recall"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Hindsight

Hindsight is Vectorize.io's agent memory system: a server, embedded package, clients, MCP surface, and host integrations for retaining conversational or task traces into memory banks, deriving facts and observations, and retrieving or reflecting on them later. Its core implementation is a PostgreSQL/Oracle-backed service with LLM extraction, vector/BM25/graph/temporal retrieval, cross-encoder reranking, background consolidation, pinned mental models, directives, and integrations such as Claude Code hooks that can automatically retain and recall memory around agent turns.

**Repository:** https://github.com/vectorize-io/hindsight

**Reviewed commit:** [867b7b4ab632c2ac0655de6dce2d3451ff4d483f](https://github.com/vectorize-io/hindsight/commit/867b7b4ab632c2ac0655de6dce2d3451ff4d483f)

**Last checked:** 2026-06-02

## Core Ideas

**Memory is a banked service, not a local note substrate.** Hindsight organizes retained material by `bank_id`, with documents, memory units, entities, memory links, chunks, async operations, mental models, directives, and audit/operation state in service tables rather than repo-local files ([README.md](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/README.md), [hindsight-api-slim/hindsight_api/models.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/models.py), [hindsight-api-slim/hindsight_api/alembic/versions/5a366d414dce_initial_schema.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/alembic/versions/5a366d414dce_initial_schema.py)). The storage substrate is operational database state, with clients and integrations treating it as a shared memory service.

**Retain turns raw text into extracted facts, entities, embeddings, links, chunks, and document lineage.** The public `retain` path accepts content, context, timestamps, document ids, metadata, entities, tags, update modes, and strategies, then routes through batch splitting, LLM fact extraction, embedding generation, entity resolution, semantic/temporal/entity link creation, and document tracking ([hindsight-api-slim/hindsight_api/engine/memory_engine.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/memory_engine.py), [hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/retain/fact_extraction.py), [hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py)). Retained raw documents and extracted world/experience facts are knowledge artifacts when consumed as evidence, but their embeddings, indexes, tags, and links also carry ranking and routing authority.

**Observation consolidation is the bottom-up learning loop.** After retain, the engine can submit a consolidation operation; the consolidation worker reads unconsolidated `world` and `experience` memory units, groups by tag scopes, asks an LLM to create/update/delete observations, stores observations back as `memory_units` with `fact_type='observation'`, and records proof/source linkage such as `proof_count`, `source_memory_ids`, and history ([hindsight-api-slim/hindsight_api/engine/memory_engine.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/memory_engine.py), [hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/consolidation/consolidator.py), [hindsight-api-slim/hindsight_api/alembic/versions/p1k2l3m4n5o6_new_knowledge_architecture.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/alembic/versions/p1k2l3m4n5o6_new_knowledge_architecture.py)). This is durable trace-derived learning: raw retained facts become distilled observations that future recall and reflect paths prefer in some integrations.

**Recall is multi-strategy retrieval under explicit context budgets.** `recall_async` defaults to valid fact types, resolves bank config, maps `Budget` to a thinking budget, generates a query embedding, runs semantic, BM25, graph, and temporal retrieval across fact types, fuses candidates, reranks them, diversifies, and stops at `max_tokens` for returned facts; optional entity, chunk, and source-fact payloads can expand context ([hindsight-api-slim/hindsight_api/engine/memory_engine.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/memory_engine.py), [hindsight-api-slim/hindsight_api/engine/search/reranking.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/search/reranking.py), [hindsight-api-slim/hindsight_api/api/http.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/api/http.py)). Context efficiency is therefore engineered at several layers: query truncation in integrations, retrieval budgets, `max_tokens`, fact-type filters, tag scopes, chunk/source-fact include flags, and reflect-loop context caps.

**Reflect is an agentic synthesis loop over retrieved memory plus directives.** `reflect_async` does not preload all memory. It gives an LLM tools for searching mental models, observations, raw facts, and expansion context, then records which facts, observations, mental models, and directives were actually used in the result ([hindsight-api-slim/hindsight_api/engine/memory_engine.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/memory_engine.py), [hindsight-api-slim/hindsight_api/engine/reflect/agent.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/engine/reflect/agent.py)). Mental models are pinned living documents created with a source query and refresh trigger; directives are instruction-like artifacts injected into reflect prompts and applied as hard rules in that operation.

**Integrations decide whether read-back is pull or push.** The generic Python client, REST API, and MCP tools expose explicit `retain`, `recall`, `reflect`, mental-model, directive, and bank operations ([hindsight-clients/python/hindsight_client/hindsight_client.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-clients/python/hindsight_client/hindsight_client.py), [hindsight-api-slim/hindsight_api/api/mcp.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/api/mcp.py)). The Claude Code integration goes further: `UserPromptSubmit` runs recall before the next prompt and injects a `<hindsight_memories>` block as `additionalContext`, while `Stop`/`SessionEnd` hooks retain transcript content in the background ([hindsight-integrations/claude-code/README.md](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/README.md), [hindsight-integrations/claude-code/hooks/hooks.json](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/hooks/hooks.json), [hindsight-integrations/claude-code/scripts/recall.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/scripts/recall.py), [hindsight-integrations/claude-code/scripts/retain.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/scripts/retain.py)).

## Artifact analysis

**Raw retained documents and transcript windows.** Storage substrate: `documents`, `chunks`, and `memory_units` tables in the Hindsight API database, plus host transcript files before retain in integrations such as Claude Code. Representational form: prose or JSON-shaped conversation/tool traces, with symbolic metadata, tags, document ids, timestamps, and update modes. Lineage: imported from client calls, files, or host transcripts; document ids, content hashes, metadata, and source tags preserve coarse lineage, while exact source offsets are not the main retained unit. Behavioral authority: knowledge artifacts as evidence for extraction, recall, reflect, and audit; they gain ranking influence through embeddings, text indexes, entity links, and graph links.

**Extracted world/experience memory units, entities, and links.** Storage substrate: database rows in `memory_units`, `entities`, `unit_entities`, `memory_links`, `entity_cooccurrences`, vector indexes, and text-search indexes. Representational form: mixed prose and symbolic structure: fact text, fact type, entity associations, dates, causal/semantic/entity links, embeddings, BM25 vectors, and graph materialization. Lineage: LLM-extracted or chunk-stored from retained documents, with document id and metadata back to the retain request; embeddings and indexes regenerate from text/config. Behavioral authority: knowledge artifacts when read as remembered facts, and system-definition artifacts when used as ranking, filtering, graph traversal, or validation state.

**Observation memory units.** Storage substrate: the same `memory_units` table with `fact_type='observation'`, plus proof/source fields and history. Representational form: prose observations with symbolic proof counts, source memory ids, tags, and history. Lineage: trace-derived and LLM-consolidated from prior world/experience facts; source-memory arrays and orphan-observation sweeps give a stronger lineage story than raw fact rows alone, though not full prompt/model/source-offset provenance. Behavioral authority: knowledge artifacts when recalled as evidence; ranking/system-definition inputs when integrations default recall to `["observation"]`, when proof count influences scoring, and when observations feed mental-model refresh or reflect.

**Pinned mental models.** Storage substrate: `mental_models` rows with name, source query, content, embedding, tags, max token limit, refresh trigger, structured content, reflect response, and history/version support ([hindsight-api-slim/hindsight_api/alembic/versions/h3c4d5e6f7g8_mental_models_v4.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/alembic/versions/h3c4d5e6f7g8_mental_models_v4.py), [hindsight-api-slim/hindsight_api/alembic/versions/v7q8r9s0t1u2_add_max_tokens_to_mental_models.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/alembic/versions/v7q8r9s0t1u2_add_max_tokens_to_mental_models.py)). Representational form: mixed prose and symbolic metadata. Lineage: authored or created by API/MCP/import, then refreshed by re-running a source query through `reflect`; delta mode can preserve existing sections and store based-on facts. Behavioral authority: knowledge artifacts when listed as summaries; system-definition artifacts when their content is searched and supplied to a reflect agent as high-quality synthesized context.

**Directives and bank templates.** Storage substrate: directive rows/API surfaces and bank-template manifests that can create or update directives and mental models ([hindsight-api-slim/hindsight_api/api/http.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/api/http.py), [hindsight-api-slim/hindsight_api/alembic/versions/k6f7g8h9i0j1_add_directive_subtype.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-api-slim/hindsight_api/alembic/versions/k6f7g8h9i0j1_add_directive_subtype.py)). Representational form: prose instructions plus symbolic priority, active flag, tags, and template matching keys. Lineage: authored/imported, not automatically learned in the inspected code path. Behavioral authority: system-definition artifacts for reflect because active directives are loaded and included as rules the reflect agent must apply.

**Claude Code integration artifacts.** Storage substrate: plugin `settings.json`, hook manifest, Python hook scripts, local state files, `~/.hindsight/claude-code.json`, and Hindsight banks reached by the plugin. Representational form: symbolic hook/config manifests plus prose prompt preambles and formatted memory blocks. Lineage: authored plugin configuration and imported Claude Code JSONL transcripts. Behavioral authority: system-definition artifacts because `UserPromptSubmit` automatically injects recalled memory into future prompt context, and `Stop`/`SessionEnd` automatically submit transcript windows for retention.

Promotion path: Hindsight has a real authority ladder. A host transcript enters as evidence; retain extracts facts; consolidation distills observations; mental model refresh synthesizes living documents from retrieval; directives and host hook configuration can grant stronger instruction or pre-action context authority. The tradeoff is that promotion is mostly service/runtime mediated rather than git-diff mediated.

## Comparison with Our System

| Dimension | Hindsight | Commonplace |
|---|---|---|
| Primary purpose | Service memory for agents and integrations | Git-native methodology KB for agent-operated knowledge bases |
| Storage substrate | PostgreSQL/Oracle service tables, vector/text indexes, clients, plugins | Repository markdown, schemas, type specs, generated indexes, review reports |
| Canonical artifacts | Documents, memory units, observations, mental models, directives, operation state | Typed notes, reference docs, instructions, reviews, sources, ADRs |
| Learning loop | LLM extraction and consolidation from retained traces; optional mental-model refresh | Human/agent-authored artifacts, validation, semantic gates, review workflows |
| Read-back | Pull through API/MCP/SDK; push through host hooks such as Claude Code pre-prompt recall | Mostly deliberate agent pull through `rg`, indexes, links, skills, and explicit instructions |
| Governance | Runtime validators, audit logs, tenant/auth extensions, operations, tests | Git diffs, frontmatter, schemas, collection rules, validation, review gates |

Hindsight is much more runtime-operational than Commonplace. It optimizes for agents that need memory while acting, with latency budgets, retrieval strategy composition, tenant scoping, daemon/server deployment, and host integrations. Commonplace optimizes for durable methodology artifacts whose authority is visible in text, schemas, validation, and repository history.

The strongest overlap is the retained-artifact ladder. Hindsight's raw document -> extracted fact -> consolidated observation -> pinned mental model -> directive/hook context progression is a concrete implementation of artifact promotion across lineage, representational form, and behavioral authority. Commonplace has a related but slower path from source snapshots and work artifacts into notes, instructions, type specs, and validation gates.

The biggest divergence is reviewability. Hindsight has more automatic adaptation, but a reader cannot review a memory change as a normal repo diff unless the deployment exports it. Commonplace has weaker automatic recall but stronger artifact audit: source-pinned citations, replacement archives, explicit type contracts, and deterministic validation.

**Read-back:** both — ordinary API/MCP/client usage is pull, while Claude Code and similar hook integrations push relevance-gated recall into the agent's pre-action context.

### Borrowable Ideas

**Observation consolidation as a middle layer.** Commonplace could use a workshop-local observation layer for repeated trace evidence before promoting anything to notes or instructions. Ready as an experimental workshop pattern; not ready as automatic library promotion.

**Mental models with stored source queries.** A Commonplace analogue would be generated synthesis pages whose source query, source set, token budget, and last refresh are explicit metadata. Worth borrowing when we need living views over large source sets.

**Default to distilled observations for prompt injection.** The Claude Code integration defaults auto-recall to `["observation"]`, not raw facts. If Commonplace ever adds pre-action memory injection, the default should be a reviewed/distilled layer, not arbitrary matching notes.

**Keep per-host push wiring outside the core artifact store.** Hindsight's core can stay API-oriented while host plugins decide how to inject memory. Commonplace should preserve that separation: artifact governance in the repo, activation policies in explicit host/runtime adapters.

**Use source-fact lineage in consolidated artifacts.** `source_memory_ids` and proof counts are a useful minimum for distilled memory. Commonplace generated syntheses should keep backpointers strong enough to invalidate and audit the synthesis.

**Do not borrow service opacity for shared methodology.** Hindsight's database-first substrate fits runtime memory. Commonplace methodology artifacts still need git-native review, status, replacement history, and human-readable contracts.

## Trace-derived learning placement

**Trace source.** Hindsight qualifies as trace-derived learning. Qualifying traces include client-supplied conversation/task content, retained files, and integration transcripts. The Claude Code plugin reads the host JSONL transcript on `Stop` and `SessionEnd`, strips injected memory blocks to avoid feedback loops, formats allowed roles and optional tool content, and submits the result to `retain` ([hindsight-integrations/claude-code/scripts/retain.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/scripts/retain.py), [hindsight-integrations/claude-code/scripts/lib/content.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/scripts/lib/content.py)).

**Extraction.** Retain first extracts/stores facts from submitted content using an LLM or chunk mode, embeddings, entity resolution, and link creation. Consolidation then reads unconsolidated facts and asks an LLM to create, update, or delete observations. Mental-model refresh optionally re-runs a stored source query through the reflect agent and stores synthesized content, with full or delta refresh modes. The extraction oracle is therefore mostly LLM-mediated, bounded by bank config, tags/scopes, prompts, batch sizes, and operation validators.

**Four-field placement.** Raw transcripts and retained documents are database/file knowledge artifacts. Extracted memory units are mixed prose/symbolic knowledge artifacts with ranking influence. Observations are trace-derived mixed artifacts with source-memory lineage and stronger default read-back authority. Mental models are synthesized prose-plus-symbolic artifacts whose behavioral authority depends on whether a reflect agent or host integration consumes them. Directives and hook configs are system-definition artifacts.

**Scope and timing.** Scope is bank-based and can be narrowed by tags, tag groups, dynamic bank id derivation, project/session/user metadata, tenant schema, and host config. Timing is mixed: retain can be synchronous or async; consolidation is a background operation after retain when enabled; mental-model refresh can be explicit or triggered after consolidation when configured; Claude Code recall fires before each user prompt.

**Survey placement.** Hindsight belongs in the trace-to-observation and trace-to-runtime-memory family. It strengthens the survey claim that durable behavior change usually happens after a distillation boundary: raw transcripts are evidence, while observations, mental models, directives, and hook-injected memory blocks are the behavior-shaping outputs.

## Read-back placement

**Direction.** Hindsight is both pull and push. The REST/SDK/MCP surfaces are pull: the agent or host explicitly calls recall, reflect, or mental-model tools. The Claude Code integration is push from the receiving agent's perspective: `UserPromptSubmit` automatically queries Hindsight and injects `additionalContext` before Claude acts on the user's prompt.

**Trigger and relevance signal.** The engineered push trigger is a host hook on user prompt submission. Relevance comes from a composed query built from the latest prompt plus optional prior turns, query truncation, selected banks, configured fact types, retrieval budget, max token cap, and Hindsight's semantic/BM25/graph/temporal retrieval and reranking ([hindsight-integrations/claude-code/scripts/recall.py](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/scripts/recall.py), [hindsight-integrations/claude-code/settings.json](https://github.com/vectorize-io/hindsight/blob/867b7b4ab632c2ac0655de6dce2d3451ff4d483f/hindsight-integrations/claude-code/settings.json)).

**Timing relative to action.** Auto-recall runs before prompt construction for the next user request and can change the next model response. Auto-retain runs after the assistant response or at session end and can only affect later turns/sessions after retain and consolidation complete.

**Selection, scope, and complexity.** The Claude Code defaults are intentionally narrow: `recallTypes` is `["observation"]`, `recallMaxTokens` is 1024, `recallContextTurns` is 1, and `recallMaxQueryChars` is 800. Hindsight itself also has recall budgets, max token filtering, tag filters, optional chunks/source-facts, and reflect context caps. Actual context dilution and precision are runtime qualities, not verified from code.

**Authority at consumption.** The injected `<hindsight_memories>` block is advisory context with a configurable preamble, not a hard gate. Directives have stronger instruction authority inside reflect. The same stored memory can therefore be advisory context in auto-recall, evidence in reflect, ranking input during retrieval, or source material for later distilled observations.

**Faithfulness.** I found implementation tests and tracing for operations, but not a code path that ablates with/without injected memories to prove the receiving agent used them. Faithfulness is structural, not verified: the hook puts selected memories into context, but behavior change depends on the model and host.

**Other consumers.** Human users and operators consume memory through the control plane, API, CLI/client surfaces, operation status, audit logs, and documentation. The service also exposes many integrations where host frameworks consume Hindsight as explicit tools rather than automatic push.

## Curiosity Pass

**The name "mental model" is overloaded.** Hindsight uses "mental model" for pinned, refreshed synthesis documents; newer observation consolidation stores observations in `memory_units`. A reviewer should not infer that every mental-model-related file is a learned world model in the distributed-parametric sense.

**The strongest learning artifact may be `observation`, not `reflect`.** Reflect is impressive because it is agentic, but the routine long-term behavior change comes from retained facts being consolidated into observations and then selected by auto-recall defaults.

**Push activation lives mostly in integrations.** The core API is a pull memory service. The Claude Code plugin supplies the pre-action push path; other integrations may only expose tools. Reviews should distinguish core capability from deployed host behavior.

**Trace lineage is good but not complete.** `source_memory_ids`, document ids, metadata, and operation history are valuable. Full reproducibility would also need extraction prompt/model/version, exact source offsets, and exported diffs for generated observations or mental models.

**Database authority is harder to inspect than repo authority.** Hindsight can adapt quickly in production, but that same speed makes memory mutations less reviewable unless operators export snapshots or audit logs.

**The system has a lot of integration surface.** Python, TypeScript, MCP, Claude Code, OpenClaw, framework-specific tools, Docker, embedded packages, and control-plane pieces are all present. The core review should not treat every integration as equivalent read-back behavior.

## What to Watch

- Whether observation consolidation gains stronger provenance: prompt/model/version, source spans, and deterministic regeneration metadata.
- Whether auto-recall integrations add faithfulness evaluation or post-action audits for injected memory.
- Whether mental-model refresh triggers become common enough that refreshed mental models, not observations, become the main behavior-shaping artifact.
- Whether directives become learnable from traces or remain authored/imported system-definition artifacts.
- Whether Hindsight exports git-readable memory snapshots for review, rollback, and cross-system comparison.
- Whether default recall continues to prefer observations as banks grow, or whether raw facts/chunks become necessary for accuracy.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Hindsight distills retained traces into observations and optionally mental models, then reads them back through recall/reflect and host hooks.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Hindsight's value depends on explicit recall/reflect calls or host push hooks, not merely on stored memory units.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Hindsight separates documents, memory units, observations, mental models, directives, indexes, and hooks by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: retained documents, facts, observations, source facts, and audit evidence are consumed as evidence/context/reference.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: directives, retrieval budgets, validators, hook manifests, plugin settings, and prompt-injection paths configure or instruct future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Hindsight derives durable observations from retained traces rather than relying only on manual memory entry.
