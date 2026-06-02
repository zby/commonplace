---
description: "Memori review: Rust/Python/TypeScript memory SDK with trace augmentation, BYODB storage, hybrid recall, and pre-call prompt injection"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Memori

Memori, from Memori Labs, is an LLM- and datastore-agnostic memory SDK, cloud service, BYODB storage layer, and agent-integration package. At the reviewed commit it wraps Python and TypeScript LLM clients, persists conversation turns, runs background "advanced augmentation" that derives facts, semantic triples, process attributes, and summaries from conversation and agent traces, and injects relevant recalled facts plus optional conversation history into the next model request.

**Repository:** https://github.com/MemoriLabs/Memori

**Reviewed commit:** [384cb992459cc6b223a34c477eff797b1f586a3e](https://github.com/MemoriLabs/Memori/commit/384cb992459cc6b223a34c477eff797b1f586a3e)

**Last checked:** 2026-06-02

## Core Ideas

**The current implementation is a Rust-centered memory engine with Python and TypeScript shells.** The root `core/` crate owns embedding, retrieval, background worker queues, advanced augmentation orchestration, and storage-bridge contracts, while `memori/` and `memori-ts/` wrap provider SDKs and translate host storage into the Rust callbacks ([core README](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/core/README.md), [core architecture](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/core/docs/architecture.md), [lib.rs](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/core/src/lib.rs), [Python Rust adapter](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/native/_adapter.py), [TypeScript Memori](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori-ts/src/memori.ts)).

**Registration turns ordinary LLM calls into memory lifecycle events.** In Python, provider registration replaces the provider method with `Invoke` wrappers; each invocation runs recall injection and conversation-history injection before the LLM call, then persists and augments the turn after the response ([BaseClient](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/llm/_base.py), [Invoke](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/llm/invoke/invoke.py), [post-invoke pipeline](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/llm/pipelines/post_invoke.py)). In TypeScript, `new Memori().llm.register(client)` registers Axon before/after hooks for recall, persistence, and augmentation ([TypeScript Memori](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori-ts/src/memori.ts)).

**Advanced augmentation is the behavior-shaping write path.** Conversation messages, LLM/provider metadata, attribution, platform/storage metadata, and optional agent trace are sent to Memori Cloud or to the Rust augmentation worker. The response is converted into write operations for `entity_fact.create`, `knowledge_graph.create`, `process_attribute.create`, and `conversation.update`; fact embeddings can be attached before the write batch reaches BYODB storage ([augmentation pipeline](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/core/src/augmentation/pipeline.rs), [TypeScript augmentation](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori-ts/src/engines/augmentation.ts), [Python agent helper](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/agent.py)).

**Storage is BYODB or Cloud, but the artifact model is stable.** BYODB migrations create conversations, messages, entity facts, process attributes, knowledge graph rows, and fact-mention links across SQLite, PostgreSQL/CockroachDB, MySQL/MariaDB, OceanBase, Oracle, TiDB, and MongoDB-style backends. Cloud mode uses hosted conversation, recall, augmentation, and agent endpoints; local mode uses driver tables and a Rust storage bridge ([PostgreSQL migration](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/storage/migrations/_postgresql.py), [SQLite driver](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/storage/drivers/sqlite/_driver.py), [storage models](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/core/src/storage/models.rs), [TypeScript storage manager](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori-ts/src/storage/manager.ts)).

**Context efficiency is engineered at recall time, not by loading the whole memory store.** Local retrieval embeds the user query, loads a dense candidate pool, validates embedding dimensions, expands candidate count dynamically, ranks with dense similarity plus BM25-style lexical scoring, and returns `limit` ranked facts. Python and TypeScript wrappers also threshold results before injecting them into context; OpenClaw's tool guidance pushes agents toward targeted filters rather than every-turn broad dumps ([retrieval pipeline](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/core/src/retrieval/pipeline.rs), [Python recall](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/memory/recall.py), [Python recall injection](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori/llm/pipelines/recall_injection.py), [TypeScript recall](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/memori-ts/src/engines/recall.ts), [OpenClaw recall tool](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/integrations/openclaw/src/tools/memori-recall.ts)).

**Agent integrations split automatic capture from mostly explicit agent recall.** OpenClaw captures completed turns through `agent_end`, extracts tool calls and results into a trace payload, and exposes `memori_recall`, `memori_recall_summary`, `memori_compaction`, feedback, quota, and signup tools. Its README explicitly says memory is not automatically injected into the prompt; the plugin does add static skill/config context and setup warnings before prompt build, but memory content is normally retrieved by tool call. The Claude Code skill is stronger as policy: it instructs the agent to run recall before nearly every substantive turn and advanced augmentation afterward, but the actual read remains a Bash-mediated tool call ([OpenClaw index](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/integrations/openclaw/src/index.ts), [OpenClaw augmentation](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/integrations/openclaw/src/handlers/augmentation.ts), [OpenClaw README](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/integrations/openclaw/README.md), [Claude Code skill](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/integrations/claude-code/SKILL.md)).

**The benchmark surface tests retrieval quality, not governance.** The LoCoMo notebooks download augmented memories, build FAISS indexes, retrieve by hybrid search, generate answers, and judge correctness. That supports efficiency and recall claims, but it does not test whether a memory should become a standing instruction or whether injected memory changed downstream agent behavior ([benchmark README](https://github.com/MemoriLabs/Memori/blob/384cb992459cc6b223a34c477eff797b1f586a3e/benchmarks/README.md)).

## Artifact analysis

- **Storage substrate:** `service-object` — Cloud conversation endpoints or BYODB `memori_conversation` and `memori_conversation_message` rows
- **Representational form:** `prose` — Structured rows carrying prose user/assistant text, roles, message types, session ids, timestamps, and optional summaries

**Conversation and message traces.** Storage substrate: Cloud conversation endpoints or BYODB `memori_conversation` and `memori_conversation_message` rows. Representational form: structured rows carrying prose user/assistant text, roles, message types, session ids, timestamps, and optional summaries. Lineage: raw interaction traces captured from wrapped LLM calls, provider responses, OpenClaw events, Hermes/Claude Code helpers, or direct agent APIs. Behavioral authority: knowledge/audit artifacts by default; in registered SDK mode, stored conversation history can be replayed into later requests, giving it advisory pre-action context authority.

**Entity facts and embeddings.** Storage substrate: Cloud recall service or BYODB `memori_entity_fact` rows with embeddings and mention links back to conversations. Representational form: mixed prose facts, symbolic ids/counts/timestamps/uniqueness keys, and distributed-parametric embeddings. Lineage: distilled from conversation and agent traces by advanced augmentation, or inserted through fallback/manual fact paths; fact-mention links retain coarse conversation lineage but not exact source spans or reviewer acceptance state. Behavioral authority: knowledge artifact when returned by recall; ranking artifact through embedding/BM25 scores, thresholds, and summaries; advisory context when injected before a model call.

**Knowledge graph triples and process attributes.** Storage substrate: BYODB `memori_knowledge_graph` and `memori_process_attribute` tables or hosted equivalents. Representational form: symbolic triples, attributes, ids, and timestamps, with prose values embedded inside subject/predicate/object labels or attribute text. Lineage: extracted from augmentation responses, including agent tool traces where integrations supply them. Behavioral authority: routing/ranking and profile authority: triples and attributes shape future recall and agent context but do not by themselves enforce behavior.

**Conversation summaries and compaction results.** Storage substrate: conversation summary fields, Cloud `agent/recall/summary` and `agent/compaction` endpoints, and BYODB summary reads joined back to mentioned facts. Representational form: prose summaries plus symbolic session/project/time scoping. Lineage: derived from conversations and agent traces through Cloud augmentation/compaction paths; current code records the summary value and scope, not the full derivation prompt/model. Behavioral authority: advisory working-state context when recalled or compacted, with stronger practical force in Claude/OpenClaw skills that tell agents to treat it as continuation state.

**Recall and injection policies.** Storage substrate: repository code, runtime config, environment variables, plugin settings, skill files, and Cloud project settings. Representational form: symbolic thresholds, limits, provider adapters, source/signal enums, date/project/session filters, and prose context templates. Lineage: authored system-definition artifacts. Behavioral authority: system-definition authority over what is retrieved, filtered, formatted, and injected; Python/TypeScript SDK wrappers can mutate system/instructions/messages before the receiving model acts.

**Benchmarks and evaluation notebooks.** Storage substrate: `benchmarks/` notebooks, downloaded augmented-memory datasets, FAISS indexes, result directories, and metric outputs. Representational form: symbolic experiment code plus numeric scores and prose/JSON answers. Lineage: derived from LoCoMo conversations, augmented memories, embedding models, retrieval runs, answer generation, and LLM judging. Behavioral authority: evaluation evidence for product claims, not runtime authority over agent behavior.

Promotion path: Memori has an operational promotion path from raw turn traces to extracted facts/triples/attributes/summaries, then to retrieval candidates, then to injected pre-action context in SDK wrappers. It does not have a review-gated promotion path from extracted memory to durable instruction, validator, or typed knowledge artifact; authority comes from the host path that chooses to inject or instruct retrieval.

## Comparison with Our System

| Dimension | Memori | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory infrastructure for apps, agents, and SDK-integrated LLM clients | Git-native methodology KB for agent-operated knowledge bases |
| Canonical retained artifacts | Conversations, entity facts, embeddings, triples, process attributes, summaries, hook/skill policies | Typed Markdown notes, instructions, reviews, ADRs, source snapshots, indexes, reports |
| Storage substrate | Memori Cloud or BYODB tables plus Rust storage bridge and embeddings | Repository files plus generated indexes, validation reports, and review-run reports |
| Write path | Wrapped LLM calls, agent integrations, background augmentation, storage write batches | Human/agent-authored source snapshots, notes, instructions, reviews, validation, gates |
| Read-back | SDK pre-call injection, conversation-history replay, explicit recall/summary/compaction tools | Mostly explicit pull via `rg`, indexes, links, skills, and loaded instructions |
| Governance | Runtime validation, thresholds, source/signal enums, tests, benchmarks, quotas | Collection contracts, type specs, git diffs, validators, semantic gates, replacement archives |

Memori is stronger than Commonplace as a production integration surface. It meets application teams where they already are: OpenAI/Anthropic/Google clients, TypeScript/Python packages, Cloud APIs, BYODB drivers, OpenClaw plugins, Claude Code skills, and managed quotas. Commonplace is stronger where durable memory must be inspectable and reviewable: each behavior-shaping artifact is a file with type, status, diff, validation, and replacement lineage.

The key design difference is authority. Memori's extracted facts are usually knowledge artifacts until a recall/injection path places them into an LLM request. Commonplace artifacts often start as explicit system-definition artifacts: type specs, collection contracts, skills, validation scripts, and review gates are intended to constrain future agents. Memori makes activation convenient; Commonplace makes promotion and accountability explicit.

**Read-back:** `both` — Registered Python/TypeScript SDK clients implement engineered pre-call push activation by querying relevant facts, threshold-filtering them, and injecting `<memori_context>` or history into the receiving request; OpenClaw and Claude Code integrations mostly expose memory as explicit pull tools plus instructions to use them

### Borrowable Ideas

**Use a storage-bridge boundary for optional acceleration.** Ready as an architecture pattern. Memori keeps the Rust core behind callback interfaces to host storage; Commonplace could use a similar boundary if it adds a fast search/index engine while leaving Markdown files as source of truth.

**Keep capture, augmentation, retrieval, and injection as separate contracts.** Ready now as review vocabulary. Memori's separation makes it easier to ask which stage failed: trace capture, fact extraction, ranking, or prompt activation.

**Borrow source/signal pairs for trace-derived memory triage.** Needs a concrete workshop use case. The OpenClaw `source`/`signal` enum pairs would translate well into Commonplace candidate-memory queues, where facts, decisions, constraints, failures, and strategies require different review policies.

**Use thresholds and summaries as context-efficiency controls, not authority controls.** Ready now. Memori shows that low-token recall can still be unreviewed; Commonplace should treat automatic recall as advisory until promoted through validation or review.

**Do not borrow hidden augmentation as library maintenance.** Memori's augmentation service can create useful facts, triples, and summaries, but those outputs lack source spans, prompt/model lineage, and acceptance review. In Commonplace they should enter as candidates or workshop artifacts, not as direct edits to notes or instructions.

**Treat SDK wrapping as a high-risk adoption affordance.** Needs a use case first. Automatic provider wrapping makes onboarding easy, but Commonplace should be cautious about any integration that mutates the model context without an inspectable report.

## Trace-derived learning placement

**Trace source.** Memori qualifies as trace-derived. Raw signals include wrapped LLM request/response messages, session ids, provider/model metadata, OpenClaw event messages, tool calls and tool results, Claude Code trace JSON, Hermes turns, optional summaries, and benchmark conversation data.

**Extraction.** The SDK and integrations first normalize messages and traces into augmentation payloads. Cloud or Rust-backed augmentation then returns entity facts, semantic triples, process attributes, and conversation summaries; the Rust pipeline translates that response into storage write operations and can attach embeddings before persistence. The oracle is Memori's augmentation service for Cloud/BYODB augmentation, with local Rust code enforcing shape and write routing rather than independently judging memory quality.

**Four fields.** The raw stage is conversation/tool trace state: prose plus symbolic roles, sessions, project/entity/process ids, timestamps, provider metadata, and tool-call structures. The distilled stage is mixed prose-symbolic-distributed memory: facts, embeddings, triples, process attributes, summaries, mentions, and compaction outputs. Raw traces mostly carry audit/context authority; distilled artifacts gain advisory context and ranking authority, then become pre-action context when SDK wrappers inject them.

**Scope and timing.** Scope is by entity, process, session, project, date range, source/signal, and Cloud/BYODB storage mode. Timing is mixed: SDK persistence and recall occur around each LLM call; augmentation runs after responses, often fire-and-forget or on a bounded Rust background worker; OpenClaw captures at `agent_end`; Claude Code guidance says to augment after every non-trivial final response.

**Survey placement.** Memori belongs in the trace-to-fact/triple/summary family with optional push activation. It strengthens the survey distinction between durable trace-derived memory and contextual activation: extraction creates facts and graph state, but behavior changes only when a wrapper, hook, skill, or agent tool reads it back into the next action.

## Read-back placement

**Direction.** Memori is both pull and push. Manual `recall`, agent `memori_recall`, `recall_summary`, and compaction tools are pull. Registered Python and TypeScript SDK clients implement push from the receiving model's perspective because recall runs before the model call and mutates the request without the model choosing to call a tool.

**Trigger and relevance signal.** SDK push is triggered by provider invocation. It extracts the current user query, searches Cloud or local BYODB memory, applies `recall_relevance_threshold`, formats relevant facts and summaries, and appends them to Anthropic/Bedrock `system`, Google system instructions, OpenAI-style `instructions`, or a system message. Local retrieval uses dense embedding candidates plus lexical reranking; Cloud recall returns facts and optional history.

**Timing relative to action.** Recall and conversation-history injection run before the model response, so they can change the next answer. Persistence and augmentation run after the response, so they affect later turns. OpenClaw's `agent_end` capture likewise affects later sessions, while its recall and compaction tools affect only when the agent invokes them.

**Selection, scope, and complexity.** Selection uses entity/session/process/project attribution, date/source/signal filters in agent tools, dense candidate limits, final fact limits, score thresholds, dynamic candidate expansion, summary attachment, and provider-specific sanitization of recalled history. Context complexity is moderate: the injected payload is formatted facts, summaries, and sometimes prior conversation messages, not the entire memory graph.

**Authority at consumption.** Injected `<memori_context>` is advisory context inside a system/instruction channel; it explicitly says to use the context only if relevant. Replayed conversation history has continuity authority. OpenClaw skill/config text and Claude Code skill procedure carry stronger instruction authority, but memory facts themselves remain evidence unless the host skill tells the agent to treat compaction or standing-order outputs as continuation state.

**Faithfulness.** The code and tests verify wrapping, injection, storage, tool validation, augmentation payload construction, and benchmark retrieval. I did not find a with/without ablation proving that injected Memori context reliably changes model behavior in agent tasks. The push mechanism is structurally implemented; effective authority is runtime-dependent.

**Other consumers.** Human operators consume memories through Cloud dashboard/docs, CLI, quota/signup commands, BYODB tables, benchmark notebooks, OpenClaw logs, and feedback tools. Those surfaces matter because Memori is both a runtime memory layer and an operator-facing memory product.

## Curiosity Pass

**The old "injection wrapper" claim is still true, but the locus shifted.** The strongest implementation evidence is now the Rust-core-backed Python/TypeScript SDK registration path; OpenClaw's current memory content read-back is mainly explicit tool use.

**The phrase "memory from what agents do" is partially code-grounded.** OpenClaw captures tool calls/results into trace payloads, and Claude Code accepts explicit trace JSON. Ordinary SDK wrapping captures conversation turns and metadata; it does not automatically know arbitrary external tool effects unless the integration supplies trace.

**The Rust core is not a full standalone memory service.** It depends on host storage callbacks and Memori Cloud augmentation for the main extraction oracle. Its distinctive contribution is deterministic orchestration, embedding, retrieval, queueing, and write-batch normalization.

**Conversation-history replay is a separate read-back path from fact recall.** It can help continuity, but it also risks replaying stale conversational state; the code sanitizes malformed tool-call history but does not judge semantic staleness.

**The benchmark does not answer the governance question.** High LoCoMo accuracy and low token footprint support retrieval efficiency, not whether a distilled memory should become an instruction, policy, or validator.

## What to Watch

- Whether augmentation responses begin recording source spans, prompt/model versions, and extraction confidence per fact/triple; that would make trace-derived lineage much more auditable.
- Whether OpenClaw adds relevance-gated automatic memory-content injection rather than explicit recall tools; that would change the integration from mostly pull to push at the agent-plugin layer.
- Whether BYODB mode can run more of augmentation locally instead of depending on hosted augmentation; that decides how much of Memori is inspectable from the open-source repo.
- Whether source/signal categories become first-class in SDK retrieval, not only agent recall tools; that would improve precision and make memory governance more type-aware.
- Whether benchmark notebooks add hook-level behavior ablations with and without injected memory; that would test effective authority rather than retrieval-answer accuracy alone.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Memori derives facts, triples, attributes, summaries, and compaction state from conversation and agent traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Memori's stored facts need SDK injection, tool recall, or host instructions before they shape action.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Memori requires splitting traces, facts, embeddings, graph triples, summaries, and injection policies by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: conversation rows, facts, summaries, benchmark results, and recall outputs usually advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: SDK wrappers, thresholds, source/signal enums, augmentation routing, and injection templates configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Memori turns conversation and agent traces into durable memory facts and graph state through augmentation.
