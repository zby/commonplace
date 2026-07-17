---
description: "HALO review: trace-learning agent-harness optimizer with SQLite desktop trace store, JSONL trace indexes, recursive trace agents, and local analysis runs"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# HALO

HALO, from Context Labs' `context-labs/halo` repository, is a trace-derived diagnostic loop for improving agent harnesses. The inspected revision contains a Python HALO Engine that reads OpenTelemetry-shaped JSONL traces with recursive root/subagent analysis, plus a new ElectroBun/Bun/React desktop app that stores local traces, sessions, imports, analysis runs, and model-provider settings in SQLite before exporting selected trace groups back to the engine.

**Repository:** https://github.com/context-labs/halo

**Reviewed commit:** [d59bb5dde1b074d1a33dc9f875bc051e36dc34e2](https://github.com/context-labs/halo/commit/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2)

**Last checked:** 2026-06-04

## Core Ideas

**HALO learns from execution traces, not from ordinary knowledge notes.** The README describes the loop as collecting agent harness traces, feeding them to the HALO-RLM engine, decomposing common failure modes, and using the report to drive code or prompt changes in the harness ([README.md](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/README.md)). The integration docs make the retained input concrete: one OpenAI Agents SDK trace becomes many OTLP-shaped span JSONL lines with trace/span ids, resource metadata, observation kind, LLM message payloads, tool inputs/outputs, token counts, and status fields ([docs/integrations/openai-agents-sdk.md](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/docs/integrations/openai-agents-sdk.md)).

**The Python engine is a bounded trace-exploration agent, not a general memory server.** `stream_engine_async` builds or reuses a sidecar trace index, loads a `TraceStore`, creates a root agent, and exposes trace query/view/search tools plus synthesis, context lookup, sandboxed code, and depth-gated subagents ([engine/main.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/main.py), [engine/tools/subagent_tool_factory.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/tools/subagent_tool_factory.py)). It returns a streamed diagnostic transcript and final answer; callers decide whether to save or apply the findings.

**Context efficiency is engineered through indexes, truncation, search-first tools, compaction, and subagent isolation.** The trace index stores byte offsets and per-trace rollups so agents can filter before reading raw spans; `TraceStore` caps attribute payloads, drops noisy flat OpenInference projections, returns oversized summaries instead of huge traces, and provides regex search over traces or spans for surgical reads ([engine/traces/trace_index_builder.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/traces/trace_index_builder.py), [engine/traces/trace_store.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/traces/trace_store.py)). Conversation context is compacted in place when old text or tool turns exceed keep-last thresholds ([engine/agents/agent_context.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/agents/agent_context.py), [engine/agents/compactor.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/agents/compactor.py)).

**The desktop app turns HALO into a local trace workspace.** The app README identifies it as a local desktop trace monitor that receives OTLP JSON at `127.0.0.1:8799`, stores traces in SQLite, renders live trace/session views, imports Langfuse history, and runs local HALO analysis over filtered trace or session groups ([app/README.md](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/README.md)). The schema includes spans, trace summaries, ingest batches, live events, Langfuse connections/import jobs, engine settings, model providers, HALO runs, run events, and run artifacts ([app/src/server/db/schema.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/db/schema.ts)).

**The adoption surface is diagnostic-led rather than automatic patching.** The bundled Claude skill explicitly says HALO Engine is a trace-exploration runtime, not a code-modification tool or verifier; Claude or another coding agent must map findings to code, make the smallest change, rerun, and measure ([skills/claude/SKILL.md](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/skills/claude/SKILL.md)). That keeps the highest-authority step outside HALO itself: HALO produces trace evidence and recommendations, while harness mutation remains mediated by a human or coding agent.

## Artifact analysis

- **Storage substrate:** `sqlite` — In the current full system, the standing retained trace/run store is the app's SQLite database (`data/halo-canvas.sqlite` by default), with file JSONL exports, `.engine-index.*` sidecars, result files, and optional telemetry JSONL as derived or bridge artifacts rather than the primary desktop store ([app/src/server/db/client.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/db/client.ts), [app/src/server/halo/exporter.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/halo/exporter.ts), [engine/traces/trace_index_builder.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/traces/trace_index_builder.py)).
- **Representational form:** `prose` `symbolic` — Diagnostic reports, prompts, trace summaries, tool outputs, skill guidance, and final answers are prose; OTLP spans, SQLite rows, Drizzle schema, JSONL indexes, filters, run events, model-provider settings, CLI arguments, and tool schemas are symbolic. I did not find retained embeddings, weights, adapters, or vector indexes in this revision.
- **Lineage:** `imported` `trace-extracted` `authored` — Local OTLP spans and Langfuse history are imported into the app; sidecar indexes, trace summaries, FTS rows, exported JSONL, engine event streams, and final analysis answers are derived from those traces; prompts, code, tool schemas, config, and the Claude skill are authored system-definition artifacts.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `learning` — Stored traces, trace summaries, run events, and reports serve as evidence/knowledge; root/subagent prompts and the Claude skill instruct agents; filters, indexes, session grouping, queues, model-provider settings, and tool schemas route work; trace validation, schema checks, status fields, budgets, cancellation, and bridge status updates provide validation and guards; trace-derived reports become learning input for future harness edits.

**Trace corpus and desktop records.** The app ingests OTLP JSON into normalized span rows, refreshes trace summaries, emits live events, and stores import/run metadata in SQLite ([app/src/server/telemetry/otlp.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/telemetry/otlp.ts), [app/src/server/telemetry/storage.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/telemetry/storage.ts)). These artifacts shape later analysis by deciding which traces are selectable, searchable, grouped into sessions, exported, and counted.

**Trace indexes and search structures.** The engine writes sidecar index and meta files next to a JSONL trace input, keyed by source file size and mtime; the app also maintains `span_search_fts` for UI trace/session search ([engine/traces/trace_index_builder.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/traces/trace_index_builder.py), [app/src/server/db/client.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/db/client.ts), [app/src/server/telemetry/storage.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/telemetry/storage.ts)). These are access-structure artifacts: they do not add new claims, but they strongly determine what the agent or UI can cheaply inspect.

**Diagnostic outputs.** The app's run queue exports matching spans to `traces.jsonl`, writes a runner config, streams engine JSON-line events into `halo_run_events`, stores final answers in `halo_runs`, and writes a standalone `result.json` ([app/src/server/halo/runQueue.ts](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/src/server/halo/runQueue.ts), [app/scripts/halo-local-runner.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/app/scripts/halo-local-runner.py)). The output is a knowledge artifact for humans and coding agents, not an automatically enforced patch.

**Promotion path.** HALO's implemented promotion path is trace data -> indexed/searchable trace corpus -> LLM-generated diagnostic report -> external harness edit. The last step can become a stronger system-definition artifact in the harness, but that promotion is outside HALO's own code path.

## Comparison with Our System

HALO and Commonplace both treat retained artifacts as agent-operational evidence, but they optimize opposite parts of the loop. Commonplace accumulates typed, reviewed Markdown artifacts whose authority is explicit in collection contracts and validation; HALO accumulates execution traces and derives a diagnostic report for a concrete harness improvement cycle. Commonplace's memory is authored and curated for reuse; HALO's memory is imported from runs and useful because it preserves concrete failures, timings, tool calls, and LLM payloads.

The main divergence is authority. HALO's strongest output is advisory: a report that someone or some coding agent must verify against the harness. Commonplace puts more authority into durable repo artifacts, schemas, review gates, and generated indexes. HALO is better at discovering behavioral patterns across executions; Commonplace is better at retaining the resulting methodology or decision once it is understood.

The desktop app narrows one previous gap with Commonplace: it now has a standing local store and navigation UI, not just a one-shot CLI over a trace file. But the store is still trace/run oriented. It does not maintain a durable library of claims with review state, backlinks, promotion status, or type-level governance comparable to Commonplace notes.

### Borrowable Ideas

**Trace-first review workbench.** Commonplace could borrow a local trace/run workspace for review agents: ingest structured run traces, group by task/session, and let agents inspect failures with bounded trace tools. Ready for review-system debugging if traces are already emitted.

**Oversized-read refusal with recommendations.** HALO's `TraceStore` does not blindly return huge trace payloads; it returns an oversized summary and points the agent toward search/span tools. Commonplace could use the same pattern for source snapshots, large review bundles, or generated reports.

**Report-as-learning-input discipline.** The Claude skill's separation between HALO diagnosis and code mutation is a useful guardrail: trace evidence should become a proposed change only after repo verification. Ready now as wording for trace-learning review procedures.

**Desktop-local trace persistence.** SQLite plus JSONL exports is a pragmatic bridge between live telemetry and agent-readable files. Commonplace could use this only with a concrete workflow, because the current repo-first KB does not need a standing event database for ordinary notes.

## Write side

**Write agency:** `manual` `automatic` — Users manually configure providers, start/cancel/retry runs, import sources, and apply any resulting harness edits; automatic paths ingest OTLP spans, import Langfuse traces, upsert summaries/search rows, export selected traces, build sidecar indexes, compact agent context, stream run events, and store final run results.

**Curation operations:** `none` — The inspected automatic writes are acquisition, indexing, summarization, export, logging, and run-result persistence. I did not find code that automatically consolidates, deduplicates, evolves, synthesizes, invalidates, decays, or promotes memory already in HALO's store under the review vocabulary; the harness-edit promotion happens outside HALO.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — HALO consumes OpenTelemetry/OpenInference span streams containing agent, LLM, tool, chain, guardrail, status, timing, token, input, output, and session fields.

**Learning scope:** `per-project` — The app groups and filters local traces by project/session/source-like fields, and a HALO run is created over a trace or session group for one harness/workspace rather than a global cross-project memory.

**Learning timing:** `offline` `staged` — Traces are captured or imported first, then selected/exported and analyzed through a queued local HALO run. Engine telemetry can stream during the analysis run, but the durable learning artifact is produced after a staged diagnostic pass.

**Distilled form:** `prose` `symbolic` — The distilled outputs are prose final answers/reports plus symbolic run events, result JSON, status fields, and trace/report lineage records.

**Extraction.** The extraction oracle is an LLM-driven root/subagent analysis loop over trace tools. The root system prompt requires a dataset overview first, then filtered query/search/view calls, span-level surgical reads, synthesis calls, and subagent delegation when depth permits ([engine/agents/prompt_templates.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/agents/prompt_templates.py), [engine/tools/trace_tools.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/tools/trace_tools.py), [engine/tools/synthesis_tool.py](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/engine/tools/synthesis_tool.py)).

**Scope and timing.** The trace corpus can accumulate continuously in the desktop app through local OTLP ingest or Langfuse import, but analysis runs are explicit jobs over a selected group. The generated report can inform a future harness version, then the next trace batch closes the loop; the code does not automatically apply the harness change.

**Survey fit.** HALO is a trace-derived diagnostic-learning system with human/coding-agent-mediated promotion. It strengthens the survey distinction between deriving knowledge from traces and automatically changing future behavior: HALO performs the former in code, while the behavior-changing patch remains outside the system.

## Read-back

**Read-back:** `pull` — Retained traces and run outputs re-enter agent context through explicit tool calls, UI searches, selected exports, or user/coding-agent review of reports; I did not find a deployed path that pushes retained memory into a future agent invocation without an explicit query/run/review action.

The root prompt does require `get_dataset_overview` first, but that is an instruction to pull from the trace store, not pushed memory content. Likewise, `synthesize_traces` returns a summary only after the agent calls it with trace ids, and desktop live events are pushed to the UI rather than to an autonomous downstream agent.

Selection is bounded by indexed filters, FTS/LIKE search, regex search, span ids, trace ids, session filters, export caps, per-attribute truncation, per-response budgets, compaction thresholds, maximum turns, maximum depth, and maximum parallel subagents. Actual report faithfulness is not proven by code; the README says AppWorld findings were independently verified from source trace files, but I did not find a built-in ablation or post-action audit that tests whether a returned HALO report changed later harness behavior ([README.md](https://github.com/context-labs/halo/blob/d59bb5dde1b074d1a33dc9f875bc051e36dc34e2/README.md)).

Other consumers include the desktop user, the Bun run queue, live WebSocket subscribers, the local Python bridge, coding agents following the bundled skill, and any CLI/API caller that saves streamed `AgentOutputItem` records.

## Curiosity Pass

**The desktop app changes the substrate story.** Earlier HALO was easy to read as "JSONL trace file in, report out." This revision adds a local SQLite trace/run workbench, which makes retention and navigation much stronger even though the engine still consumes exported JSONL.

**The strongest behavioral change is extra-system.** HALO can surface harness-level issues, but the durable improvement is a code or prompt edit made elsewhere. That makes citation discipline and verification more important than in systems that only retrieve context.

**The engine has good context-economy mechanics but no semantic memory curation loop.** It indexes, searches, truncates, compacts, summarizes, and reports. It does not maintain a growing library of validated lessons, rules, or patches inside HALO itself.

**The app stores secrets and engine installs as operational memory.** Provider keys, engine install path/status, and imported Langfuse connection metadata are behavior-shaping app records, but they are configuration and access artifacts rather than agent knowledge.

## What to Watch

- Whether HALO adds an internal library of accepted findings, patches, or harness lessons; that would move it from trace-derived diagnosis toward durable agent memory.
- Whether future desktop releases add provenance spans or review state for individual report claims, not just final answers and run events.
- Whether the local app exports/imports its SQLite trace/run store in a way that keeps reports reproducible across machines.
- Whether the HALO loop gains automated patch proposal, application, or regression gating; that would raise its behavioral authority from advisory learning input to system-definition mutation.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: HALO derives diagnostic reports from session/tool/event traces and feeds them into a harness-improvement loop.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: HALO stores traces and reports, but memory read-back is pull-only in the inspected code.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: HALO's SQLite rows, JSONL spans, sidecar indexes, prompts, and reports carry different forms and authorities.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: HALO uses execution traces to improve an agent harness through a mediated learning loop.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: HALO prompts, tool schemas, app schema, queues, and config records route and constrain later analysis.
