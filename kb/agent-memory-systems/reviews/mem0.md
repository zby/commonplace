---
description: "Mem0 review: long-term memory SDK/server with trace fact extraction, hybrid vector/entity retrieval, agent hooks, and proxy prompt injection"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Mem0

Mem0, from mem0ai, is an open-source long-term memory layer for AI assistants and agents. At the reviewed commit it provides a Python SDK, hosted-client interface, self-hosted FastAPI server, proxy chat wrapper, OpenMemory MCP/dashboard stack, OpenClaw plugin, and a multi-client `mem0-plugin` for coding agents. The core implementation turns conversation messages into extracted memory facts, stores those facts in vector and entity stores with history/message side tables, and exposes explicit search plus several host integrations that can inject recalled memories before an agent or model responds.

**Repository:** https://github.com/mem0ai/mem0

**Reviewed commit:** [a3154d59e52386d4e1189c1f5f44819868f76514](https://github.com/mem0ai/mem0/commit/a3154d59e52386d4e1189c1f5f44819868f76514)

**Last checked:** 2026-06-02

## Core Ideas

**The core write path is extraction from messages, not raw transcript storage.** `Memory.add()` accepts strings or role-tagged messages scoped by `user_id`, `agent_id`, or `run_id`, normalizes them, and passes them into `_add_to_vector_store()` ([main.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py)). With `infer=True`, the v3 phased pipeline retrieves recent messages and nearby existing memories, calls an LLM with `ADDITIVE_EXTRACTION_PROMPT`, parses extracted memory texts, deduplicates by hash, embeds the texts, inserts them into the vector store, writes history rows, links entities, and saves the source messages ([main.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py), [prompts.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/configs/prompts.py)).

**The current algorithm is ADD-first.** The README describes the April 2026 algorithm as "Single-pass ADD-only extraction", and the code matches that for normal inferred adds: extracted facts are inserted as new records after hash deduplication rather than using the older add/update/delete decision prompt. Direct `update()`, `delete()`, `delete_all()`, and `history()` APIs still exist, so the library is not append-only as an administrative surface ([README](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/README.md), [main.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py)).

**Retrieval fuses semantic, keyword, and entity evidence.** `search()` validates scoped filters, accepts `top_k`, threshold, advanced filter operators, and optional reranking, then `_search_vector_store()` lemmatizes the query, extracts query entities, embeds the query, over-fetches semantic vector candidates, performs keyword search when supported, computes BM25 normalization, computes entity boosts from a separate entity store, and ranks candidates through `score_and_rank()` ([main.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/main.py), [scoring.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/utils/scoring.py), [entity_extraction.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/utils/entity_extraction.py)). Context efficiency in the core library is therefore retrieval-time top-k/threshold filtering, not a bounded prompt memory object.

**Lineage is mostly operational metadata, not source-span provenance.** The vector payload stores text, hash, timestamps, session identifiers, role/actor metadata, lemmatized text, and additional metadata; SQLite stores history events and raw message snippets in separate tables ([storage.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/memory/storage.py), [base.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/configs/base.py)). That is enough to audit when a memory was created or changed and which session scope it belongs to, but inferred memories do not retain exact source spans, prompt/model versions, or reviewer acceptance records.

**Integration surfaces range from pull tools to pre-action hooks.** The self-hosted server wraps the core add/search/update/delete/history APIs behind authenticated FastAPI endpoints ([server/main.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/server/main.py)). OpenMemory is still present but marked as sunsetting in favor of the self-hosted server ([openmemory README](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/openmemory/README.md)). The Python proxy wraps chat completions by asynchronously adding the conversation to memory, searching over the last messages, and rewriting the final user message with "Relevant Memories/Facts" before the LLM call ([proxy/main.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0/proxy/main.py)).

**The coding-agent plugins are where memory becomes an agent-context mechanism.** `mem0-plugin` installs MCP tools, skills, and lifecycle hooks; its Codex/Claude hook installer can add `SessionStart`, `UserPromptSubmit`, and `Stop` entries. `UserPromptSubmit` injects search rubrics, resume-specific retrieved memories, error/file-path cues, and write nudges, while background scripts auto-capture transcript windows and compact summaries into Mem0 ([mem0-plugin README](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/README.md), [on_user_prompt.sh](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/scripts/on_user_prompt.sh), [auto_capture.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/scripts/auto_capture.py), [capture_compact_summary.py](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/mem0-plugin/scripts/capture_compact_summary.py)). OpenClaw goes further: skills mode runs recall in `before_prompt_build`, searches with thresholds and token budgets, and returns `prependContext` for the next agent prompt ([openclaw/index.ts](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/openclaw/index.ts), [openclaw/recall.ts](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/openclaw/recall.ts)).

**Evaluation is benchmark-oriented, not governance-oriented.** The `evaluation/` tree reproduces memory benchmark runs against LOCOMO-style data, Mem0, RAG, LangMem, Zep, OpenAI memory, and full-context baselines, with BLEU/F1/LLM-judge scoring and latency/token tracking ([evaluation README](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/evaluation/README.md), [memzero add](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/evaluation/src/memzero/add.py), [memzero search](https://github.com/mem0ai/mem0/blob/a3154d59e52386d4e1189c1f5f44819868f76514/evaluation/src/memzero/search.py)). These tests evaluate answer quality, not whether a particular stored memory should become a durable rule, instruction, or validator.

## Artifact analysis

**Extracted memory records.** Storage substrate: pluggable vector stores, including local and hosted backends configured through `VectorStoreFactory`; the payload carries `data`, hash, timestamps, session identifiers, actor/role fields, lemmatized text, and arbitrary metadata. Representational form: prose facts plus symbolic metadata and distributed-parametric embeddings. Lineage: trace-extracted from new messages with context from recent messages and existing memories; hash dedup and extraction prompts are part of the derivation policy, while exact source spans and prompt/model versions are not retained per memory. Behavioral authority: knowledge artifact when returned by search or listed through APIs; advisory context when injected by a host; ranking authority belongs to embeddings, BM25 text, filters, entity boosts, and optional rerankers.

**Raw message and history tables.** Storage substrate: SQLite by default at `~/.mem0/history.db` or configured path. Representational form: structured rows with prose message content, roles, session scopes, event names, old/new memory text, deletion flags, actor ids, and timestamps. Lineage: raw message traces and memory mutation history recorded by the SDK; invalidated by retention, reset, or database deletion rather than by source-file changes. Behavioral authority: mostly knowledge/audit artifacts; recent messages are also system-definition inputs to the next extraction prompt, because they shape what the LLM extracts from new messages.

**Entity records and links.** Storage substrate: a separate vector-store collection named from the main collection plus `_entities`. Representational form: symbolic entity type/text, linked memory ids, session filters, and entity embeddings. Lineage: derived from extracted memory text through spaCy-based entity extraction and embedding, with update/delete paths maintaining links. Behavioral authority: ranking/routing artifact: entity matches boost linked memories during search, but entity records do not directly instruct the model.

**Extraction prompts, custom instructions, categories, and filters.** Storage substrate: repository prompt/config code, server/project configuration, plugin configuration, and hosted project settings. Representational form: prose prompts plus symbolic schemas, category maps, thresholds, top-k limits, filter operators, and hook/event matchers. Lineage: authored system-definition artifacts, sometimes generated from a use-case prompt by `/generate-instructions`; changes regenerate different memories and retrieval sets. Behavioral authority: instruction, extraction policy, filtering, ranking, scoping, and mutation policy.

**Read-back wrappers and hook outputs.** Storage substrate: repository code, user plugin configs, shell hook files, OpenClaw config, temporary session marker files, and remote Mem0 API results. Representational form: assembled prose context blocks such as `<recalled-memories>` / `<relevant-memories>`, search rubrics, setup banners, and symbolic hook responses (`additionalContext`, `prependContext`, `prependSystemContext`). Lineage: derived at prompt time from user prompts, session ids, search results, plugin settings, and thresholds; each output is ephemeral, but the code and configuration are durable system-definition artifacts. Behavioral authority: advisory context or system-context instruction for the receiving agent/model before it acts.

**Evaluation artifacts.** Storage substrate: `evaluation/` scripts, datasets outside the repo, result JSON files, and generated scores. Representational form: symbolic experiment parameters and prose/JSON answers plus numeric metrics. Lineage: derived from benchmark conversations, memory-system outputs, model responses, and LLM-judge prompts. Behavioral authority: evaluation evidence for system choice and retrieval claims, not runtime memory authority.

Promotion path: Mem0 has an operational promotion path from raw conversation traces to extracted fact memories, entity-linked retrieval candidates, and pre-action context injection. It can also store compact summaries and auto-captured coding-session learnings. It does not have a Commonplace-style promotion path from candidate memory to reviewed note, instruction, test, or validator; high-authority use is supplied by the host integration that decides to inject the memory.

## Comparison with Our System

| Dimension | Mem0 | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory layer for personalized agents and apps | Git-native methodology KB for agent-operated knowledge bases |
| Canonical retained artifact | Extracted memory fact with embeddings, metadata, history, and entity links | Typed Markdown notes, instructions, reviews, source snapshots, indexes, reports |
| Storage substrate | Vector stores, entity vector collection, SQLite history/messages, hosted API/server databases | Repository files plus deterministic indexes and review/validation reports |
| Write path | LLM extraction from conversations, direct API writes, hooks, skills, auto-capture | Human/agent-authored artifacts, source snapshots, explicit review and validation |
| Read-back | Pull APIs/MCP/search plus proxy and hook-based prompt injection | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Prompt rules, filters, tests, API validation, benchmark evaluation | Collection contracts, type specs, git diffs, validators, semantic gates, replacement archives |

Mem0 is stronger than Commonplace as an application-facing memory service. It provides SDKs, hosted and self-hosted APIs, many vector backends, extraction prompts, search fusion, entity linking, coding-agent plugins, and benchmark harnesses. Commonplace is stronger as an inspectable governed knowledge system: artifacts are ordinary files, citations and status are explicit, indexes are generated, old reviews are archived, and promotion into behavioral authority is reviewable.

The largest design difference is where authority lives. In Mem0, a memory record is usually an advisory knowledge artifact until a wrapper, hook, proxy, or agent chooses to read it back. In Commonplace, many artifacts are authored directly as system-definition artifacts: collection contracts, skills, type specs, validation scripts, and review gates are meant to constrain later agents. Mem0 makes activation easy; Commonplace makes authority easier to audit.

Read-back: both. Core SDK/API/MCP search is pull, but the proxy wrapper and OpenClaw/plugin hooks implement engineered pre-action push paths that search or select memory and inject it into the receiving prompt/context.

### Borrowable Ideas

**Separate memory extraction from memory activation.** Ready now as review vocabulary. Mem0 makes it clear that a good extraction pipeline does not by itself answer how memory reaches an agent; Commonplace reviews should keep write path and read-back path separate.

**Use entity-linked retrieval as a secondary search signal.** Needs a concrete search layer. Commonplace could use entity extraction to boost related notes or sources, but authored links and type contracts should remain the semantic source of truth.

**Borrow hook-level context budgets, not automatic authority.** Ready for workshops. OpenClaw's token-budgeted recall, category ordering, thresholds, and subagent handling are useful for temporary work contexts; Commonplace should keep any automatically recalled material advisory until promoted through review.

**Store compact-summary artifacts with explicit expiry.** Ready now. `capture_compact_summary.py` treats compaction summaries as expiring session-state memories. Commonplace should retain compaction summaries only when they have lineage, scope, and an expiration/promotion decision.

**Do not borrow unreviewed LLM extraction as KB maintenance.** Mem0's extraction prompt is rich, but extracted facts can be redundant, stale, or over-general. For Commonplace, automatic extraction should produce candidates or workshop notes, not direct edits to library methodology.

**Borrow fast agent onboarding only at the integration edge.** The agent signup, plugin installer, and setup banners are adoption affordances. Commonplace can learn from this for tooling ergonomics, but should avoid turning setup convenience into hidden dependency on a hosted memory service.

## Trace-derived learning placement

**Trace source.** Mem0 qualifies as trace-derived. The core `add()` path consumes user/assistant messages, recent saved messages, and nearby existing memories; plugin auto-capture reads transcript JSONL windows; compact-summary capture reads entries flagged `isCompactSummary`; OpenClaw auto-capture reads agent messages after successful turns.

**Extraction.** Extraction is prompt-driven and staged. The SDK uses `ADDITIVE_EXTRACTION_PROMPT` or custom instructions to extract self-contained memory facts from new messages while using recent messages and existing memories for context and deduplication. The plugin and OpenClaw layers pre-filter noise, session-specific metadata, generic acknowledgments, and excessively long messages before calling Mem0's add API. Entity extraction then derives linked entity records from the memory text.

**Four fields.** The raw stage is message/transcript/history data: prose traces plus symbolic roles, session ids, timestamps, branch/project metadata, and run ids. The distilled stage is memory records, entity links, compact-summary memories, and category/metadata assignments: mixed prose-symbolic-distributed artifacts stored in vector/entity stores and SQLite/server state. Raw traces mostly have knowledge/audit authority; extracted memories become advisory context on read-back, and ranking/filtering metadata has system-definition authority over what returns.

**Scope and timing.** Scope is by user, agent, run/session, project/app id, branch, source, and metadata filters. Timing is mixed: SDK writes run during app calls; proxy writes happen asynchronously before a chat completion; `mem0-plugin` auto-capture runs every third substantial user prompt or after compaction; OpenClaw legacy auto-capture runs after successful turns; OpenClaw skills mode disables ordinary auto-capture and instead relies on explicit memory tools and dream/triage flows.

**Survey placement.** Mem0 belongs in the trace-to-memory-record and trace-to-agent-hook families. It strengthens the survey claim that trace-derived systems often stop at advisory facts plus retrieval policy; behavior changes when a separate host path injects those facts into a model call, not merely when facts are stored.

## Read-back placement

**Direction.** Mem0 is both pull and push. The SDK, server, OpenMemory, MCP tools, and most skills expose explicit search/list/get calls. The Python proxy, OpenClaw `before_prompt_build` hook, and parts of `mem0-plugin` push selected or instruction-like memory context into the receiving model/agent before action.

**Trigger and relevance signal.** The proxy triggers on chat completion calls whose last message is from the user and searches with the last six messages. OpenClaw triggers on `before_prompt_build`, skips non-interactive/system prompts, sanitizes the prompt, searches long-term and optionally session memory, applies thresholds, top-k, category priority, token budgets, and subagent namespace rules, then injects `prependContext`. `mem0-plugin` uses `UserPromptSubmit` detections for resume intent, errors, file paths, and remember intent; ordinary prompts get a search rubric rather than pre-fetched memories.

**Timing relative to action.** Proxy and OpenClaw recall happen before the model/agent response, so recalled memories can change the next action. Auto-capture, compact-summary capture, and OpenClaw agent-end capture happen after a turn or on the next compact/start boundary, so they affect later turns.

**Selection, scope, and complexity.** Selection is controlled by entity/user/run filters, project/app ids, thresholds, top-k, dynamic top-score filtering, category priority, token budget, max memory count, identity/config always-include policy, broad cold-start searches, and optional session search. Complexity is moderate: injected context is formatted memory prose plus categories/importance, not a whole graph, but plugin banners and search rubrics can mix operational instructions with recalled facts.

**Authority at consumption.** Retrieved memories are advisory context by default. `prependSystemContext` in OpenClaw skills mode can carry stronger protocol authority, while `prependContext` and proxy-injected "Relevant Memories/Facts" are softer evidence/context. The hooks can also nudge future writes, which gives plugin code system-definition authority over agent memory habits.

**Faithfulness.** The repository has tests and code paths for filtering, threshold handling, hook behavior, tools, and benchmark quality, but I did not find a with/without memory ablation for the plugin hooks proving that injected memories reliably change agent behavior. The push mechanism is structurally implemented; effective authority remains runtime-dependent.

**Other consumers.** Human users and operators consume memories through dashboards, CLI commands, MCP tools, server APIs, memory-reviewer/export/import skills, request logs, and evaluation reports. These consumer surfaces matter because Mem0 is both a runtime memory substrate and an operator-facing memory management product.

## Curiosity Pass

**The most important Mem0 artifact is not the vector row alone.** The behavior-shaping unit includes extraction prompt, vector payload, entity links, filter scope, search ranking, and the host path that injects the result.

**The README's ADD-only claim is true for inferred extraction, not for the whole API.** Normal inferred adds create new memories after deduplication, but direct update/delete/history APIs still make the system mutable.

**The plugin changed the read-back story.** A plain Mem0 SDK integration is pull. The OpenClaw and coding-agent hooks turn the same memory substrate into a pre-action context mechanism with thresholds and budgets.

**Auto-capture is deliberately lossy.** The hook scripts skip short messages, JSON/tool-only messages, generic acknowledgments, metadata prefixes, and session-specific content. That is good context hygiene, but it also means the retained trace-derived memory is a filtered story, not the complete session.

**Benchmarks do not settle governance.** High LOCOMO-style recall scores say something about answer quality under test conditions; they do not say whether an extracted fact should become an enduring rule, skill, or validator.

## What to Watch

- Whether the core SDK begins recording source spans, extraction prompt/model versions, and source-message ids per memory; that would make trace-derived lineage much more auditable.
- Whether the OpenClaw skills-mode recall becomes the primary plugin path across clients; that would make Mem0 a stronger example of budgeted push activation.
- Whether compact-summary and auto-capture memories gain explicit expiry, confidence, and review status across all write paths, not only selected scripts.
- Whether the self-hosted server closes the gap with the hosted API's v3 fields such as `app_id`, categories, and expiration; divergence would complicate claims about one Mem0 behavior.
- Whether evaluations add hook-level ablations that compare agent behavior with and without injected memories, rather than only memory-answer benchmark scores.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Mem0 derives memory facts, compact summaries, and coding-session learnings from conversation/session traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Mem0's stored memories need search/proxy/hook read-back before they affect an agent.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Mem0 requires separating memory facts, entity links, raw traces, prompts, hooks, and benchmark outputs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: extracted memories, raw messages, search results, and benchmark outputs mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: extraction prompts, filters, thresholds, hook scripts, plugin protocols, and proxy wrappers configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Mem0 turns conversation and session traces into durable memories through LLM extraction and hook-driven capture.
