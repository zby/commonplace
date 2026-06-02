---
description: "Halo review: Python trace-analysis engine that indexes OTel JSONL, delegates bounded trace exploration to subagents, and emits harness-improvement reports"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# Halo

Halo, from Context Labs' `context-labs/halo` repository, is a Python package and CLI for Hierarchical Agent Loop Optimization: it reads OpenTelemetry/OpenInference-shaped JSONL traces from an agent harness, builds a sidecar trace index, and runs a root/subagent LLM analysis loop with trace-query tools to produce findings that a coding agent or human can turn into harness changes. It is closer to a trace-analysis and diagnosis engine than to a general-purpose memory vault.

**Repository:** https://github.com/context-labs/halo

**Reviewed commit:** [c9e4efc7a01adf7292ce32cf0459cf7b40df40de](https://github.com/context-labs/halo/commit/c9e4efc7a01adf7292ce32cf0459cf7b40df40de)

**Last checked:** 2026-06-02

## Core Ideas

**The source layer is agent execution traces.** The README defines the HALO loop as collecting traces from an agent harness, feeding them into the engine, producing a failure-mode report, and using that report to modify the harness ([README.md](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/README.md)). The OpenAI Agents SDK integration writes one JSONL span per agent, LLM, tool, handoff, guardrail, or custom span and stamps normalized `inference.*` attributes such as project id, observation kind, model name, token counts, and agent name ([docs/integrations/openai-agents-sdk.md](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/docs/integrations/openai-agents-sdk.md), [demo/openai-agents-sdk-demo/tracing.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/demo/openai-agents-sdk-demo/tracing.py)).

**Trace indexing is the durable retrieval layer.** `TraceIndexBuilder.ensure_index_exists` writes `<trace>.engine-index.jsonl` and a meta file beside the source trace, reusing the index only when schema version, source size, and mtime still match ([engine/traces/trace_index_builder.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/traces/trace_index_builder.py)). Each `TraceIndexRow` stores byte offsets, byte lengths, span counts, times, error flags, service/model/agent names, project id, and token totals; `TraceStore` then seeks into the canonical JSONL instead of importing the whole trace corpus into a database ([engine/traces/models/trace_index_models.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/traces/models/trace_index_models.py), [engine/traces/trace_store.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/traces/trace_store.py)).

**The runtime is a bounded trace-reasoning harness.** `stream_engine_async` builds the index, loads a `TraceStore`, creates a run state, renders the root context, and wires a root OpenAI Agents SDK agent with trace tools, synthesis, context lookup, optional sandboxed code execution, and `call_subagent` when depth allows ([engine/main.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/main.py), [engine/tools/subagent_tool_factory.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/tools/subagent_tool_factory.py)). Depth, parallelism, turn limits, compaction thresholds, trace-index config, and per-role models live in `EngineConfig` ([engine/engine_config.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/engine_config.py)).

**Context efficiency is the main design pressure.** The system prompt forces the agent to start with `get_dataset_overview`, use indexed filters before raw regex scans, avoid fabricated trace ids, size calls by `raw_jsonl_bytes`, and switch from whole-trace reads to `search_trace`, `view_spans`, or `search_span` when responses would exceed budgets ([engine/agents/prompt_templates.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/agents/prompt_templates.py)). The tools reinforce that policy with per-attribute truncation, 150 KB response budgets, oversized summaries, bounded regex matches, and surgical span reads ([engine/traces/trace_store.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/traces/trace_store.py), [engine/tools/trace_tools.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/tools/trace_tools.py)). Older conversation and tool items are summarized in memory by the compaction model while preserving full originals for `get_context_item` lookup ([engine/agents/agent_context.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/agents/agent_context.py), [engine/tools/agent_context_tools.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/tools/agent_context_tools.py)).

**Subagents isolate exploration instead of increasing one context.** The root prompt tells the root to delegate when depth is available, and `call_subagent` creates a fresh child context with its own system prompt, depth, lineage metadata, tools, and semaphore gate ([engine/agents/prompt_templates.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/agents/prompt_templates.py), [engine/tools/subagent_tool_factory.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/tools/subagent_tool_factory.py)). That is an explicit complexity-management choice: split trace investigation across smaller local contexts and return typed `SubagentToolResult` summaries to the parent rather than loading every trace detail into the root.

**The report does not automatically become a harness patch.** The CLI streams model text and completed agent output items to stdout, while the API exposes streamed or collected `AgentOutputItem` records for callers to persist if they choose ([halo_cli/main.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/halo_cli/main.py), [engine/models/engine_output.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/models/engine_output.py)). The README's optimization loop relies on an external coding agent or maintainer to apply the report's recommendations; the checked-in engine does not rewrite prompts, tools, code, tests, or deployment config itself.

**Telemetry can record Halo's own analysis run, but it is optional.** When `--telemetry` is enabled, Halo emits OpenInference traces of its LLM/tool/agent activity to Catalyst or a local JSONL fallback; when disabled, the engine avoids that output path ([README.md](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/README.md), [engine/main.py](https://github.com/context-labs/halo/blob/c9e4efc7a01adf7292ce32cf0459cf7b40df40de/engine/main.py)). This can create traces of the trace-analysis agent itself, but those traces are observability artifacts unless a later Halo run or user deliberately analyzes them.

## Artifact analysis

**Raw trace JSONL.** Storage substrate is the caller's filesystem path, usually `traces.jsonl` or `HALO_TRACES_PATH` from the integration module. Representational form is mixed symbolic/prose: OTLP-like JSON envelopes with structured span ids, timing, status, resource fields, and attributes, plus natural-language LLM messages, tool inputs, and tool outputs. Lineage comes from the instrumented harness and the exporter; source changes are new span lines or edits to the JSONL. Behavioral authority is knowledge artifact authority when Halo reads traces as evidence about harness behavior.

**Trace index and meta sidecars.** Storage substrate is the sidecar files beside the trace path: `.engine-index.jsonl` and `.engine-index.meta.json`. Representational form is symbolic Pydantic JSONL rows plus a JSON meta fingerprint. Lineage is deterministically derived from the raw trace file, schema version, source size, and mtime; stale fingerprints regenerate the index. Behavioral authority is system-definition artifact authority for routing and ranking: the index controls cheap counts, query results, sample trace ids, byte ranges, filtering, and which trace material the agent can safely request next.

**Trace tools and system prompts.** Storage substrate is package code and prompt templates in the repository. Representational form is mixed symbolic/prose: typed tool schemas and Python code enforce limits, while system prompt prose instructs exploration order and delegation. Lineage is authored implementation, not trace-extracted. Behavioral authority is system-definition artifact authority because these artifacts instruct, route, constrain, and enforce how the model may inspect trace evidence.

**In-run agent context, compaction summaries, and synthesis results.** Storage substrate is in-memory `AgentContext` and `EngineOutputBus` state for a single run; callers may persist `AgentOutputItem` records externally, but the bus itself has no replay buffer. Representational form is mixed: preserved message/tool fields, lineage ids, compaction flags, prose summaries, and synthesized prose. Lineage comes from the input prompt, selected trace spans, tool calls, subagent answers, and LLM summarization. Behavioral authority is mostly knowledge artifact authority inside the run: these items advise the root or parent agent. A final report becomes a system-definition artifact only after an external maintainer or coding agent applies it to prompts, code, validators, or deployment settings.

**Optional Halo telemetry.** Storage substrate is Catalyst or a local `halo-telemetry-{run_id}.jsonl` file when telemetry is enabled. Representational form is trace JSONL again. Lineage is Halo's own analysis execution rather than the user's original harness. Behavioral authority is observability/evidence authority until a later process reads it as input for optimization.

The promotion path is explicit but outside the engine: trace evidence and sidecar indexes support an LLM-written report; the report can then be promoted by a human or coding agent into prompt edits, tool fixes, tests, or code changes. Halo supplies the trace-derived diagnosis step, not the final high-authority patch.

## Comparison with Our System

| Dimension | Halo | Commonplace |
|---|---|---|
| Primary purpose | Diagnose systemic agent-harness failures from execution traces | Build and maintain a typed methodology KB for agents |
| Source evidence | OTel/OpenInference JSONL traces and derived sidecar indexes | Markdown artifacts, source snapshots, reviews, indexes, validation reports |
| Canonical substrate | Caller-owned trace files plus sidecar cache files | Git-tracked `kb/` collections and generated reports |
| Retrieval path | Tool-pull over trace index, regex search, span reads, synthesis, sandbox analysis | `rg`, indexes, authored links, type contracts, skills, review bundles |
| Context efficiency | Hard tool budgets, indexed filtering, subagent delegation, compaction | Collection routing, descriptions, indexes, validation, skills, scoped reviews |
| Behavior change | External: report informs harness edits by a coding agent or maintainer | Internal: instructions, schemas, validators, reviews, and notes directly govern future KB work |

Halo and Commonplace share the assumption that raw accumulation is not enough. Halo turns trace logs into a navigable evidence surface before asking a model to reason over them. Commonplace turns markdown collections into typed, linked, validated artifacts before asking agents to rely on them. Both systems use symbolic retained artifacts to reduce context volume and guide attention.

The main divergence is authority. Halo's core artifacts are strongest during an analysis run: prompts and tools govern how the analyzing agent inspects traces, while the output report remains advice until someone applies it. Commonplace keeps more of the behavior-changing surface inside the repository: `AGENTS.md`, type specs, collection contracts, validators, skills, and review gates already carry instruction, validation, or routing force for future agents.

Halo is also more operationally focused. It is built for deployed agent harnesses with many traces and recurring failure modes, not for accumulating durable conceptual knowledge. That makes its trace index, query tools, and subagent split useful for high-volume diagnostic work, but weak as a long-term memory governance system unless the generated reports are captured, reviewed, and promoted elsewhere.

**Read-back:** pull - a user or caller supplies a trace file and prompt, then Halo's root and subagents deliberately pull trace evidence through tools; the engine does not push stored memory into future host-agent contexts.

### Borrowable Ideas

**Make trace navigation tool-native.** Commonplace review and validation reports could expose a bounded query/view API rather than forcing agents to grep large logs directly. Ready for review artifacts with repeated failure traces.

**Use sidecar indexes with explicit source fingerprints.** Halo's stat-fingerprinted sidecar is lightweight and honest about lineage. Commonplace can borrow the pattern for expensive generated views, while using stronger hashes when correctness matters more than speed.

**Return oversized summaries instead of failing open.** Halo's `view_trace` and `view_spans` do not dump arbitrary payloads into context when a request is too large; they return size statistics and next-step recommendations. Ready as a CLI/tool-output pattern for Commonplace reports and source snapshots.

**Delegate investigation by scope, not by status.** Halo's subagents are not separate authorities; they are bounded investigators with fresh contexts and lineage back to the parent tool call. Commonplace could use this shape for semantic-review bundles that split large artifacts into independently inspectable claims.

**Keep diagnosis separate from patch authority.** Halo's report-to-patch boundary is a useful warning. Commonplace should continue requiring review, validation, and explicit promotion before trace-derived findings become instructions or validators.

## Trace-derived learning placement

**Trace source.** Halo qualifies as trace-derived because its central input is agent/session/tool traces: OpenTelemetry/OpenInference-shaped JSONL spans from an instrumented agent harness. The demo exporter records agent, LLM, tool, handoff, guardrail, and custom spans, with project, service, model, token, and agent-name projections.

**Extraction.** Extraction has two levels. First, deterministic indexing scans the raw JSONL, groups spans by `trace_id`, stores byte offsets/lengths, and derives rollups such as error presence, services, models, agents, project id, and token totals. Second, the root/subagent LLM loop uses tool-pull exploration, regex search, bounded span reads, synthesis calls, optional sandboxed analysis, and compaction to produce a natural-language diagnosis. The extraction oracle for the report is the configured LLM plus the prompt/tool policy; the extraction oracle for the sidecar index is deterministic code.

**Storage substrate.** Raw traces remain in caller-owned JSONL files. The derived index and meta files persist next to the trace file. In-run summaries, subagent answers, and final reports live in process memory and streamed outputs unless the caller captures them. Optional Halo telemetry can persist a second trace corpus for the analysis run itself.

**Representational form.** Raw traces and indexes are symbolic with embedded prose payloads. Tool results and final reports are prose wrapped in symbolic message/output records. There is no distributed-parametric learned state retained by the repository; LLMs are external oracles used at read/extraction time.

**Lineage.** The sidecar index has clear regeneration lineage through schema version, trace file size, and mtime. The final diagnosis has weaker lineage: it can cite trace ids and tool outputs if the agent includes them, but the engine does not automatically attach a complete provenance graph, prompt version, model version, or replay manifest to each recommendation.

**Behavioral authority.** Raw traces are knowledge artifacts. The trace index is a system-definition artifact for retrieval and routing inside Halo. Tool schemas, budgets, prompts, and depth gates are system-definition artifacts for the analyzing agent. The generated report is a knowledge artifact as long as it advises a human or coding agent; it becomes a system-definition artifact only if promoted into harness code, prompts, tests, tool contracts, or deployment config.

**Scope and timing.** Scope is per trace file and per engine run, with sidecar reuse across runs until the trace fingerprint changes. Timing is offline or post-hoc: Halo analyzes accumulated traces after harness executions, then an external loop applies changes and gathers new traces.

**Survey placement.** Halo belongs in the trace-to-diagnosis branch of trace-derived systems. It strengthens the survey claim that trace-derived learning needs an explicit distillation boundary, but it is weaker than systems that automatically write durable rules: Halo stops at diagnosis and leaves high-authority patch promotion outside the engine.

## Curiosity Pass

**The durable "memory" inside Halo is mostly an index, not a lesson.** The sidecar index is valuable because it makes traces navigable, but it does not by itself encode a durable fix or preference. The behavior-changing artifact is downstream of the report, and the repository does not own that artifact.

**The root prompt is unusually procedural.** It tells the model exactly how to size the dataset, avoid expensive scans, choose tools, and delegate. That makes prompt text a major system-definition artifact; changing it could alter the engine as much as changing Python code.

**Compaction preserves originals in memory.** `AgentContext` can render summaries while keeping original content and tool fields available through `get_context_item`. That is a useful split between context efficiency and recoverability, though it remains in-run rather than durable memory.

**The RLM framing is broader than the shipped persistence model.** The README describes recursive self-improvement, but the package at this commit implements trace ingestion, bounded analysis, and reporting. The recursive loop depends on external deployment, patching, and trace recollection infrastructure.

**The optional telemetry path can create a nested diagnostic loop.** Halo can trace its own analysis agent, and those traces can be fed back into Halo. That is promising for debugging the analyzer, but the code does not special-case or govern that recursive use.

## What to Watch

- Whether future releases persist reports with source trace ids, model/prompt metadata, and replayable tool-call provenance.
- Whether the engine gains an apply stage that writes harness prompt/tool/code patches, turning reports into direct system-definition artifacts.
- Whether sidecar invalidation moves from size/mtime fingerprints to content hashes for shared or non-append-only trace stores.
- Whether benchmark and demo loops publish full trace/report/patch/run-lineage bundles rather than aggregate improvement claims alone.
- Whether telemetry of Halo's own analysis run becomes a first-class input for improving the analyzer's prompts and tool policies.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Halo derives trace indexes and diagnostic reports from agent execution traces, but leaves patch promotion outside the engine.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Halo extracts reusable diagnosis from execution traces rather than relying on manually authored observations alone.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Halo separates raw traces, sidecar indexes, prompt/tool policy, in-run summaries, reports, and telemetry by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw traces, span views, synthesis results, and reports advise future work unless promoted into stronger channels.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: trace indexes, tool schemas, budgets, prompts, depth gates, and any externally applied harness patches route, constrain, or instruct behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Halo activates trace evidence through explicit tool-pull analysis, but stored traces and reports do not affect future agents automatically.
