---
description: "Phantom review: VM-based AI co-worker with Qdrant memory, trace-derived config evolution, scheduler, MCP, and prompt push activation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-02"
tags: [trace-derived, push-activation]
---

# Phantom

Phantom, from `ghostwright/phantom`, is a Bun/TypeScript agent runtime for an AI co-worker that runs on its own machine. It combines Slack, web chat, Telegram, email, webhook, CLI, scheduler, MCP, Qdrant/Ollama memory, dynamic tools, and a self-evolution loop that rewrites selected files under `phantom-config/` after sessions.

**Repository:** https://github.com/ghostwright/phantom

**Reviewed commit:** [f8c7ab42d885936ee54abc785528000260f4acc5](https://github.com/ghostwright/phantom/commit/f8c7ab42d885936ee54abc785528000260f4acc5)

**Last checked:** 2026-06-02

## Core Ideas

**The agent is a persistent runtime, not just a memory API.** Phantom's main process loads configuration, migrations, channels, memory, evolution, MCP, scheduler, web UI, secrets, preview/browser tools, and role state, then routes user/channel events into a Claude Agent SDK query with persistent sessions (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/index.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/runtime.ts). The memory system matters because it sits inside an always-on agent with its own filesystem, Docker access, public UI pages, scheduled jobs, and self-registered MCP tools, not because it exposes a standalone store.

**Prompt assembly is layered and explicit.** `assemblePrompt()` appends identity, environment, security, role, onboarding, evolved config, agent memory instructions, general instructions, working memory, dynamic memory context, and chat runtime context into the Claude Code preset system prompt (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-assembler.ts). The evolved `phantom-config` block becomes Constitution, Communication Style, User Profile, Domain Knowledge, and Learned Strategies, while `data/working-memory.md` is always read into a bounded prompt block when present (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-blocks/evolved.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-blocks/working-memory.ts).

**Context efficiency is split between relevance-gated memory and bounded static blocks.** Before each runtime or web-chat SDK query, Phantom builds memory context from the current user text, retrieves facts, episodes, and one procedure, filters low-signal episodes, and formats only what fits under the configured token budget (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/runtime.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/chat-query.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/context-builder.ts). Static prompt blocks are less selective: evolved config is always appended when loaded, and working memory is always appended up to a 75-line cap. The default memory context budget is large, 50,000 estimated tokens, so Phantom optimizes for continuity more than tight context minimalism (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/config/memory.yaml).

**Qdrant memory has three implemented stores, but only two are automatically populated from sessions.** Episodic, semantic, and procedural stores each create Qdrant collections with dense vectors and sparse BM25-like vectors, and retrieval fuses dense+sparse search via Qdrant RRF (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/episodic.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/semantic.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/procedural.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/qdrant-client.ts). The session consolidation code currently creates one episode and heuristic preference/correction facts; it reports `proceduresDetected: 0`, so repeated-pattern promotion to procedural memory is documented but not implemented in that consolidation path (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/consolidation.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/docs/memory.md).

**Self-evolution is a separate trace-to-config pipeline.** After each channel session, Phantom sends a compact session summary to a Haiku gate; fired rows are stored in SQLite `evolution_queue`, drained on a 180-minute cadence or when depth reaches five, and processed by a Claude Agent SDK reflection subprocess that can edit specific `phantom-config/` files (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/index.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/gate.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/queue.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/cadence.ts). The subprocess prompt teaches it to read the batch and current memory files, decide what to learn, compact, skip, or escalate, and emit a sentinel; TypeScript then runs deterministic invariant checks, commits version metadata, logs the drain, or restores the snapshot (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/subprocess-prompt.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/reflection-subprocess.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/invariant-check.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/versioning.ts).

**Memory is also inspectable and mutable through human and MCP surfaces.** External MCP tools and resources expose status, current evolved config, config changelog, session history, memory search, and recent/domain memory resources (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/mcp/tools-universal.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/mcp/resources.ts). The dashboard memory API can browse, search, detail, and delete Qdrant episodes/facts/procedures; memory-file APIs expose ordinary Claude memory files and read-only `phantom-config/memory/agent-notes.md` (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/ui/api/memory.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/ui/api/memory-files.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory-files/storage.ts).

## Artifact analysis

- **Storage substrate:** `vector` — Qdrant collection named by `config/memory.yaml`, default `episodes`
- **Representational form:** `prose` `symbolic` `parametric` — prose summaries/details and Markdown config, symbolic payload fields/SQLite rows/schemas, and Qdrant dense plus sparse vector state
- **Lineage:** `authored` `trace-extracted` — seed/config/tool surfaces are authored or agent/operator-created, while sessions feed Qdrant memories and evolved config through consolidation and reflection
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — recalled memories are advisory knowledge; evolved config and prompt assembly instruct; invariant rollback enforces and validates; MCP/scheduler/runtime surfaces route; Qdrant/search signals rank; consolidation and evolution learn from traces

**Qdrant episodic memories.** Storage substrate: Qdrant collection named by `config/memory.yaml`, default `episodes`. Representational form: mixed distributed-vector and symbolic payload state, with `summary`, `detail`, and sparse `text_bm25` vectors plus payload fields for session id, user id, tools, files, outcome, importance, access count, timestamps, and lessons. Lineage: trace-extracted from completed channel sessions by `consolidateSession()`, which summarizes the first user message and records tool/file/outcome metadata. Behavioral authority: knowledge-artifact context when recalled into the prompt, and ranking system-definition authority through importance, recency, access reinforcement, and decay.

**Qdrant semantic facts.** Storage substrate: Qdrant collection `semantic_facts`. Representational form: mixed vector, sparse, and symbolic triples/fact payloads. Lineage: currently extracted heuristically from user messages that match correction or preference patterns, linked to source episode ids; contradiction handling can mark earlier facts invalid by setting `valid_until` when a newer high-confidence fact conflicts (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/consolidation.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/memory/semantic.ts). Behavioral authority: advisory context in the prompt's `Known Facts` section, plus selection authority because valid facts are preferentially recalled before episodes.

**Qdrant procedural memories.** Storage substrate: Qdrant collection `procedures`. Representational form: mixed vector, sparse, and symbolic procedure records with trigger, steps, preconditions, postconditions, parameters, success/failure counts, and source episode ids. Lineage: store/update APIs are implemented, but the inspected automatic consolidation path does not create procedures. Behavioral authority: when present, a single relevant procedure is injected as a step list into the prompt; effective procedure quality is not verified from code.

**Dynamic memory context.** Storage substrate: transient system-prompt text assembled per query. Representational form: prose sections generated from Qdrant payloads. Lineage: derived at read time from the current user message, embedding search, sparse search, ranking filters, and token-budget formatting. Behavioral authority: push-style advisory context from the agent's perspective, because the main agent receives matched memories before deciding its next action without explicitly asking for a memory search.

**Evolved `phantom-config/` files.** Storage substrate: repo/filesystem directory `phantom-config/`, with `constitution.md`, `persona.md`, `user-profile.md`, `domain-knowledge.md`, `strategies/*.md`, `memory/corrections.md`, `memory/principles.md`, read-only `memory/agent-notes.md`, read-only `memory/session-log.jsonl`, and metadata under `meta/`. Representational form: mostly prose markdown plus JSON/JSONL metadata. Lineage: `constitution.md` and seed files are authored; selected files are trace-derived through the gate, queue, reflection subprocess, invariant check, and versioning pipeline; metadata records versions, metrics, gate logs, and evolution logs. Behavioral authority: system-definition artifact authority when appended into every main-agent prompt as Constitution, Communication Style, User Profile, Domain Knowledge, and Learned Strategies.

**Working memory file.** Storage substrate: `data/working-memory.md`, created on boot if absent. Representational form: prose markdown. Lineage: authored by the agent or operator during use; the inspected code seeds a stub and reads the file, but does not provide a separate derivation or validation path for it. Behavioral authority: always-loaded advisory/instructional prompt context, capped by line truncation with a compaction warning. This is push by always-load, but not the reason for the `push-activation` tag because it is not relevance-gated.

**Agent notes instructions and `agent-notes.md`.** Storage substrate: `phantom-config/memory/agent-notes.md`. Representational form: prose notes. Lineage: the prompt block tells the main agent to append durable learnings directly during sessions, while the reflection subprocess may read but must not modify the file (https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/agent/prompt-blocks/agent-memory-instructions.ts, https://github.com/ghostwright/phantom/blob/f8c7ab42d885936ee54abc785528000260f4acc5/src/evolution/subprocess-prompt.ts). Behavioral authority: pull-style evidence when the agent chooses to read it, and operator-facing evidence through the dashboard read-only memory-file surface. It is not injected by default.

**SQLite operational state.** Storage substrate: Bun SQLite database tables for sessions, cost events, scheduled jobs, evolution queue/poison rows, audit rows, chat transcripts, secrets, and related state. Representational form: symbolic relational rows. Lineage: generated by runtime, scheduler, MCP, UI, channel, and evolution operations. Behavioral authority: system-definition authority for session resume, scheduled wakeups, queue disposition, audit visibility, cost accounting, retry/poison decisions, and UI/MCP read surfaces.

**MCP, UI, scheduler, and dynamic tools.** Storage substrate: source code plus runtime SQLite/dynamic-tool state. Representational form: symbolic tools, resources, schemas, HTTP routes, and scheduled-job rows. Lineage: authored code and agent/operator-created records. Behavioral authority: system-definition authority: these surfaces expose what outside clients, the agent itself, scheduled tasks, and operators can read or mutate. The scheduler wakes the full runtime with a self-contained prompt; it does not select memories itself, but scheduled runs receive the same evolved config and relevance-gated memory context as other runtime calls.

**Promotion path.** Phantom has two meaningful promotions. First, raw session traces become Qdrant episode/fact knowledge artifacts, then matched memories are pushed into later prompts as advisory context. Second, gated session summaries become edited `phantom-config` prose that is always injected with stronger system-definition authority. The second path crosses the largest authority boundary: trace signal becomes standing prompt instruction after LLM reflection plus deterministic invariant checks.

## Comparison with Our System

| Dimension | Phantom | Commonplace |
|---|---|---|
| Primary purpose | Always-on autonomous co-worker with VM, channels, tools, memory, scheduler, and self-evolution | Agent-operated methodology KB with typed artifacts, validation, reviews, instructions, and source workflows |
| Main substrate | Runtime process, SQLite, Qdrant/Ollama, `phantom-config/`, `data/`, UI, MCP, Docker/VM workspace | Git-tracked markdown collections, type specs, indexes, validation scripts, source snapshots, and review workflows |
| Read-back | Both push and pull: per-query vector-memory prompt injection, always-loaded evolved config/working memory, explicit MCP/UI searches | Mostly pull through `rg`, indexes, links, skills, reports, and explicit validation/review commands |
| Learning | Automatic trace-derived Qdrant episodes/facts and gated trace-derived config evolution | Deliberate artifact writing, review, validation, and promotion; no automatic chat-trace learning by default |
| Governance | Reflection sandbox, allowed file list, immutable constitution checks, invariant rollback, version/evolution log, queue poison pile | Collection contracts, schemas, deterministic validation, semantic review gates, git diffs, archive/replacement workflow |
| Context efficiency | Dynamic memory matching plus large budget; static evolved config and working memory always loaded | Lexical/index navigation and explicit artifact loading; stronger type constraints but less automatic prompt assembly |

Phantom is much more aggressive than Commonplace about letting session traces become future behavior. Commonplace usually makes an agent write or revise an artifact under a collection/type contract, then validation and review determine whether it should persist. Phantom lets two automatic loops persist state: a low-friction vector-memory extractor after every session, and a higher-authority reflection subprocess that edits prompt-injected config after gated batches.

The strongest design divergence is authority placement. Commonplace keeps durable methodology authority in reviewed files and schemas. Phantom keeps some durable authority in reviewed-like files, but the reviewer is an LLM subprocess plus deterministic file invariants rather than a human/agent review workflow tied to source citations. That is a coherent choice for a personal co-worker optimizing continuity, but it is weaker for a public methodology KB where provenance and argument quality matter.

Phantom's context story is operationally better for a chat agent. A user message automatically retrieves relevant memories and attaches evolved state before the agent acts. Commonplace is more inspectable and cheaper in prompt terms, but it depends on the acting agent remembering to search, follow indexes, and load the right notes. Phantom proves that a stateful agent benefits from an engineered read-back path, not just a place to store memories.

**Read-back:** `both` — Phantom has pull surfaces through MCP, UI, and reflective tools, plus memory push from relevance-gated per-query Qdrant injection and coarse always-loaded evolved/working-memory prompt blocks. The `push-activation` tag is justified by the instance-targeted pre-action Qdrant memory context, not by baseline docs, coarse always-loaded memory, or ordinary memory-search tools

### Borrowable Ideas

**Relevance-gated read-back before action.** Commonplace could add a session-start or task-start retrieval layer that assembles candidate notes/reviews/sources from the current request before the agent writes. Ready as an advisory experiment if it preserves citations and makes selected artifacts visible.

**Trace learning with a hard authority boundary.** Phantom's split between low-authority Qdrant memories and higher-authority evolved config is useful. Commonplace could adopt an explicit "candidate from trace" lane that never becomes instruction until it is promoted through validation/review. Needs a concrete use case and retention policy first.

**Invariant checks around self-editing memory.** The reflection subprocess is risky, but the rollback model is good: snapshot, restrict writeable files, deny immutable files, check size/syntax/credential/duplicate/sentinel invariants, then commit or restore. Commonplace could reuse this shape for workshop-to-library promotion helpers. Ready as a pattern, not a direct implementation.

**Queue, cadence, and poison-pile discipline.** Phantom avoids reflecting every turn inline; it batches, deduplicates by session key, serializes drains, retries bounded invariant failures, and moves repeated failures to a poison pile. Commonplace review/ingest automation could borrow that lifecycle for expensive semantic QA jobs. Ready where batch jobs already exist.

**Memory explorer with delete/detail operations.** A dashboard for episodes, facts, procedures, and evolved config makes hidden memory inspectable. Commonplace could borrow the principle for generated reports and candidate notes: every retained behavior-shaping artifact should have an operator-facing read/delete/ack surface. Needs UI demand before implementation.

**Do not borrow large always-loaded config uncritically.** Phantom's always-appended evolved sections fit a single co-worker identity. Commonplace should prefer targeted loading and typed navigation unless a prompt block is small, validated, and clearly session-global.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
- **Trace source:** `session-logs` `tool-traces` — completed sessions supply user/assistant messages, session metadata, tracked files, tool metadata, costs, outcomes, and summaries for consolidation and evolution
- **Learning scope:** `per-task` `cross-task` — per-session memories record individual interactions, while evolved config and reusable facts/strategies shape later sessions
- **Learning timing:** `online` `staged` — normal consolidation runs after each ready-memory session, while evolution queues gated summaries for cadence-based batch reflection
- **Distilled form:** `prose` `symbolic` `parametric` — traces become prose episodes/facts/config, symbolic Qdrant/SQLite payload and metadata rows, and embedded dense/sparse memory vectors

Phantom qualifies for `trace-derived` twice.

The first trace source is the normal completed session: user messages, assistant messages, files tracked, cost, outcome, and session metadata assembled after a channel response. Consolidation creates an episodic memory for every ready-memory session and heuristic semantic facts from explicit correction/preference patterns, then stores embeddings and payloads in Qdrant. This is online, per-session, and low curation: no LLM judge decides the fact content in the current implementation, and procedure extraction remains unimplemented in this path.

The second trace source is the evolution session summary consumed by the gate and reflection subprocess. A Haiku gate decides whether a session has durable learning signal, queued rows survive restarts, cadence drains batches every 180 minutes or at depth five, and a sandboxed SDK subprocess edits `phantom-config/` files after reading the batch and existing memory files. This is staged, batch-oriented, and curated by an LLM memory manager with deterministic invariant checks. The output has stronger authority because it is injected into every future main-agent prompt.

On the survey axes, Phantom combines online trace extraction, LLM-mediated reflection, deterministic post-write governance, and prompt-level read-back. It strengthens the survey claim that trace-derived learning needs a promotion boundary: Phantom's raw Qdrant memory and evolved config both come from traces, but only the latter becomes standing system-definition context.

## Read-back placement

**Direction.** Both push and pull. Pull surfaces include `phantom_memory_query`, `phantom_memory_search`, `phantom_config`, MCP resources, reflective in-process memory tools, and dashboard memory/config APIs. Push occurs when the runtime builds memory context from the incoming message and appends it to the system prompt before the SDK query.

**Read-back signal:** `coarse` `inferred / lexical` `inferred / embedding` — evolved config and working memory are always-loaded coarse memory, while dynamic Qdrant context uses current-message lexical and embedding search before the SDK call.

**Faithfulness tested:** `no` — the review finds insertion, selection, rollback, and invariant mechanisms, but no WITH/WITHOUT ablation or post-action audit proving behavioral uptake.

**Targeting and signal.** Phantom has two memory push shapes. Evolved config and working memory are `coarse`: they are retained memory accumulated or edited during use, but `assemblePrompt()` appends them whenever the blocks exist, so they provide generic standing continuity rather than selection for this instance. Dynamic Qdrant memory is `instance`-targeted: each runtime/web-chat query passes the current user text into `MemoryContextBuilder.build()`, which recalls episodes, facts, and one procedure before the SDK call. The signal is mixed `inferred / embedding` plus `inferred / lexical`: stores embed the query and also build sparse BM25-like vectors from the query text, then Qdrant hybrid search and ranking/validity/top-k filters choose the prompt payload. Payload identifiers such as session id, user id, type, category, and timestamps can filter or rank records, but the deployed per-query selector's relevance signal is content-derived.

**Injection point.** Memory context and evolved config are assembled before the Agent SDK call, so they can change the next action. Consolidation and evolution run after the session, so they only affect future sessions.

**Selection, scope, and complexity.** Defaults are top 10 episodes, top 20 facts, one procedure, and an estimated 50,000-token memory budget. Facts are prioritized, episodes are filtered by durability/recency before formatting, and procedure inclusion requires a successful procedure lookup. The budget is generous enough that context dilution remains a runtime risk not verifiable from source.

**Authority at consumption.** Qdrant memories are advisory context. Evolved config has stronger system-definition authority because it appears as Constitution, Communication Style, User Profile, Domain Knowledge, and Learned Strategies in the system prompt. Working memory is also prompt context, but its lineage and validation are weaker.

**Faithfulness.** The code shows insertion, selection, and rollback mechanisms, but I did not find a WITH/WITHOUT ablation or post-action audit proving that injected memories changed behavior. Effective precision and behavioral uptake are not verified from code.

**Other consumers.** Operators and external clients can inspect memory through MCP resources, MCP tools, dashboard memory APIs, memory-file APIs, evolution/config APIs, health endpoints, and metrics. The same memory state is not only for the main agent; it is also an operator and integration surface.

## Curiosity Pass

**The strongest learning artifact is not the vector store.** Qdrant memories are useful, but the evolved config has more behavioral force because it is injected as prompt instruction. That makes `phantom-config/` the more important memory substrate for long-term behavior, even though the README foregrounds vector memory.

**The docs describe procedural promotion more strongly than the inspected code implements.** The procedural store and prompt injection path exist, but session consolidation currently returns `proceduresDetected: 0`. Learned workflows can still enter `phantom-config/strategies/*.md` through reflection, which is a different substrate and authority path.

**Working memory is a simple always-loaded file, not a scoped memory system.** It is seeded at boot, read into every prompt when present, and truncated by lines. This is cheap and inspectable, but it has no provenance, retrieval, or quality gate.

**The reflection subprocess is intentionally trusted.** TypeScript does not pre-classify observations or choose file targets; it snapshots, spawns, parses the sentinel, checks invariants, and rolls back. That is a sharp design: it accepts LLM judgment for semantic placement but keeps mechanical safety deterministic.

**The scheduler is a wake-up mechanism, not memory activation.** Scheduled jobs run the full runtime with a self-contained task prompt. They become push from the user's perspective, but not a separate memory matcher; memory selection still happens through the normal prompt assembly path.

## What to Watch

- Whether procedural memories start being automatically extracted from repeated episodes. That would change Phantom from episode/fact trace extraction plus prompt-file evolution into a three-tier trace-learning system.
- Whether memory context budget moves from character-estimated 50,000 tokens to tokenizer-aware budgeting and stronger dilution controls.
- Whether evolved config gains source citations or per-bullet provenance in the prompt-injected files, not only in `meta/evolution-log.jsonl`.
- Whether `agent-notes.md` becomes retrievable or promoted into evolved config, since the current prompt tells the main agent to write it but deliberately avoids injecting it.
- Whether the dashboard memory delete/edit surfaces gain review gates or tombstones for high-authority memories.
- Whether Phantom adds faithfulness tests showing that injected memories improve task outcomes rather than merely appearing in context.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Phantom has both storage and explicit activation through pre-action prompt injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: Phantom's Qdrant payloads, SQLite rows, evolved config files, working memory, and prompt sections differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: Qdrant episodes/facts and dashboard-visible memories mostly serve as evidence, reference, and advisory context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: evolved config, prompt assembly, scheduler rows, MCP schemas, and invariant rules configure or constrain behavior.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - positions: Phantom is a code-grounded example of trace-to-vector-memory plus trace-to-prompt-config learning.
