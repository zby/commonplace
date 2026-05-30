---
description: "HALO review: trace-analysis engine over OTel JSONL with sidecar indexes, bounded trace tools, sandboxed analysis, subagents, and external harness-patch promotion"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# HALO

HALO is Context Labs' "Hierarchical Agent Loop Optimization" engine for improving agent harnesses from execution traces. It ingests OpenTelemetry-shaped JSONL spans, builds a sidecar trace index, gives a root agent and optional subagents bounded tools for trace inspection and sandboxed analysis, and emits a diagnostic report that a coding agent or human can turn into harness changes. The implemented behavior-changing loop is therefore two-stage: HALO produces trace-derived diagnostic knowledge; the actual harness behavior changes only when an external patch is promoted into the target harness.

**Repository:** https://github.com/context-labs/halo

**Reviewed commit:** [e4f0987e2618342c8a2d3fce115636ab29b3ab1e](https://github.com/context-labs/halo/commit/e4f0987e2618342c8a2d3fce115636ab29b3ab1e)

**Last checked:** 2026-05-16

## Core Ideas

**The primary input is flat OTel-compatible JSONL, not a proprietary memory store.** The OpenAI Agents SDK integration writes one JSON object per span with OTel identity fields, `resource.attributes`, `scope`, raw OpenInference-style attributes, and normalized `inference.*` projections such as project, observation kind, model, token counts, and agent name ([docs/integrations/openai-agents-sdk.md](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/docs/integrations/openai-agents-sdk.md), [tracing.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/demo/openai-agents-sdk-demo/tracing.py)). `SpanRecord` strongly models the top-level span fields but deliberately leaves `attributes` open, so HALO can preserve upstream trace detail while indexing a small stable projection ([canonical_span.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/traces/models/canonical_span.py)). Raw traces are retained source evidence and knowledge artifacts; they are not themselves instructions.

**Sidecar indexes make huge trace files navigable without replacing the raw trace.** `TraceIndexBuilder.ensure_index_exists(...)` writes `<trace>.engine-index.jsonl` plus `<trace>.engine-index.meta.json`, reusing the sidecar only when schema version, source size, and `mtime_ns` still match the raw JSONL ([trace_index_builder.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/traces/trace_index_builder.py)). Each `TraceIndexRow` stores byte offsets and lengths for every span in a trace plus rollups for errors, services, models, agents, project id, and token totals ([trace_index_models.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/traces/models/trace_index_models.py)). The index is a runtime/index surface with selection and seek authority; lineage stays simple because the raw JSONL remains canonical and stale sidecars are regenerated from file stats.

**Trace tools implement progressive disclosure as hard runtime affordances.** The root and subagents receive `get_dataset_overview`, `query_traces`, `count_traces`, `view_trace`, `view_spans`, `search_trace`, and `search_span` ([trace_tools.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/tools/trace_tools.py)). The system prompt forces overview-first discovery, warns against broad regex scans, and tells agents to use byte sizes, span ids, and oversized summaries before drilling into trace content ([prompt_templates.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/agents/prompt_templates.py)). The tool implementation backs that instruction with caps: broad `view_trace`/`search_trace` paths head-cap attributes around 4 KB, `view_spans` gives named spans a larger cap, oversized responses return a summary instead of flooding context, and regex search returns bounded match records over raw span JSON ([trace_store.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/traces/trace_store.py)).

**Subagents are orchestration for trace analysis, not a persistent multi-agent memory.** `build_root_sdk_agent(...)` creates a root OpenAI Agents SDK agent with leaf trace tools, synthesis, context lookup, optional sandboxed code execution, and a `call_subagent` tool when depth allows ([subagent_tool_factory.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/tools/subagent_tool_factory.py)). Each subagent gets its own `AgentContext`, depth-specific prompt, and the same bounded trace tools. Semaphores cap parallel children per depth. The retained state inside a HALO run is conversation context plus compaction summaries; it is not persisted as a reusable memory base across runs ([agent_context.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/agents/agent_context.py), [compactor.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/agents/compactor.py)).

**Sandboxed code analysis is a scoped read-only analysis surface.** When Deno/Pyodide is available, HALO exposes `run_code`, which runs Python with `trace_store`, `numpy`, and `pandas` preloaded ([run_code_tool.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/tools/run_code_tool.py)). The sandbox mounts the trace and index read-only into a WASM filesystem, gives each tool call a fresh Deno process, denies network/write/env/run permissions, and caps wall-clock time and captured output ([sandbox.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/sandbox/sandbox.py), [pyodide_runtime.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/sandbox/pyodide_runtime.py)). This gives the model symbolic computation over trace data without giving it authority to mutate the traces or harness.

**The CLI and Python API package HALO as an analysis engine.** The `halo` console script takes a trace file and prompt, builds one `EngineConfig`, and streams root/subagent output; it does not edit the target harness ([halo_cli/main.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/halo_cli/main.py), [halo_cli/README.md](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/halo_cli/README.md)). The lower-level API offers sync and async streaming or collected outputs, with each `AgentOutputItem` carrying agent id, parent id, depth, sequence, and final status ([main.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/main.py), [engine_output.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/models/engine_output.py)). HALO can optionally trace its own analysis run to local JSONL or Catalyst, producing dogfood traces in the same shape it ingests ([local_processor.py](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/engine/telemetry/local_processor.py)).

## Comparison with Our System

| Dimension | HALO | Commonplace |
|---|---|---|
| Primary purpose | Diagnose harness-level failure modes from agent execution traces | Maintain an agent-operated methodology KB |
| Raw substrate | OTel-shaped JSONL spans, often collected from agent SDKs | Git-tracked markdown notes, sources, instructions, reviews, schemas, reports |
| Derived index | JSONL sidecar with byte offsets and trace rollups | Generated directory indexes, validation signals, review outputs |
| Runtime surface | LLM trace tools, synthesis, subagents, sandboxed Python, CLI/Python API | `rg`, authored indexes, skills, `commonplace-*` commands, review/fix workflows |
| Behavior-shaping artifact | Diagnostic report, then external harness patch | Typed notes and stronger system-definition artifacts: instructions, schemas, validators, commands, skills |
| Promotion gate | Outside HALO: a human or coding agent applies harness edits and redeploys | Inside the KB workflow: review, validation, git history, and curated promotion |
| Trace-derived status | Trace-to-diagnostic-to-external-patch loop | Mostly curated artifact workflows, with trace-derived systems studied rather than built in core |

HALO is stronger than commonplace at high-volume execution-trace forensics. It treats trace navigation as an agent UX problem: overview first, cheap indexed narrowing, surgical span reads, bounded regex, oversized summaries, and code analysis over the same `TraceStore`. That is a more specialized interface than asking a general coding agent to grep large logs.

Commonplace is stronger at durable artifact authority. A HALO report is a knowledge artifact when consumed as evidence or advice by a human or coding agent. It becomes behavior-shaping only after promotion into a harness patch, prompt edit, tool change, validator, or other system-definition artifact outside HALO. Commonplace makes those authority shifts explicit inside the repo: notes, instructions, type specs, validators, generated indexes, and review artifacts have different contracts and lifecycles.

The key comparison is that HALO separates raw traces, derived indexes, runtime tools, and reports well, but keeps the final codification step out of process. That is reasonable for a harness optimizer aimed at existing agent deployments. It also means HALO should not be described as a self-contained memory system: the memory-like value is in reusable diagnostic reports and externally applied harness changes, not in a persistent store that automatically conditions future HALO runs.

## Borrowable Ideas

**Byte-offset sidecar indexes for large retained evidence.** Ready for any future commonplace trace/workshop substrate. HALO's sidecar rows preserve raw-file canonicality while making trace summaries and span seeks cheap. If commonplace starts keeping large review traces or agent-run logs, a derived sidecar should point into raw evidence rather than replacing it.

**Tool-enforced progressive disclosure.** Ready to borrow as an agent-tool design pattern. HALO's prompt rules are backed by tool result shapes and size caps, so the model gets structural help staying within context. Commonplace could apply the same pattern to review bundles or large-source snapshots: overview, query, surgical read, oversized summary.

**Sandboxed analysis over canonical evidence.** Worth borrowing when trace datasets become too large for prose-only review. A read-only `trace_store` plus pandas/numpy lets the agent compute distributions without gaining mutation authority. The commonplace analogue would be a sandboxed analysis tool over sources/reports, not write access to the KB.

**Lineage-rich streamed agent output.** Useful for multi-agent review workflows. HALO's `AgentOutputItem` carries sequence, depth, parent agent, and parent tool call, which is enough to reconstruct who produced which conclusion. Commonplace review bundles could use a similar envelope if we start preserving multi-agent QA traces.

**Keep harness patch promotion explicit.** This is a caution as much as a borrow. HALO's README loop says the report is fed to Cursor or Claude Code to generate harness changes ([README.md](https://github.com/context-labs/halo/blob/e4f0987e2618342c8a2d3fce115636ab29b3ab1e/README.md)). Commonplace should preserve that kind of authority boundary: trace-derived findings should remain diagnostic until promoted into instructions, tests, schemas, or code through a visible review path.

## Trace-derived learning placement

**Trace source.** HALO qualifies as trace-derived learning in the broad harness-optimization sense. The source signal is execution traces from agent harnesses: OTel-compatible span rows covering agents, LLM calls, tools, chains, guardrails, timestamps, status, token counts, model names, service identity, project id, and raw input/output attributes. Trace boundaries are `trace_id`s in an append-style JSONL file, usually produced by the supplied OpenAI Agents SDK tracing processor or a compatible exporter.

**Extraction.** Extraction is not a fixed schema-to-rule pipeline. HALO first derives a sidecar index with byte offsets and rollups; then an LLM agent uses overview/query/search/view/synthesis/run-code tools to inspect traces and produce a diagnostic answer to the caller's prompt. The oracle is therefore partly structural and partly external: status/error fields and trace statistics provide hard signals, while the LLM judges which patterns are harness-level failures. The README's benchmark narrative says findings are then independently checked against source traces before prompt edits are made, but that verification and patching step is outside the engine implementation.

**Storage substrate.** Raw retained state persists as JSONL trace files. Derived runtime state persists as `.engine-index.jsonl` and `.engine-index.meta.json` sidecars next to the trace file. In-run reasoning lives in OpenAI Agents SDK context items with optional compaction summaries. Optional HALO self-telemetry writes another local JSONL file or uploads spans to Catalyst. The diagnostic report is streamed to stdout or returned through the Python API; HALO does not persist a canonical report store or patch archive.

**Representational form.** Raw traces are mixed symbolic/prose artifacts: structured span fields plus stringified messages, tool inputs, and outputs. Sidecar indexes are symbolic JSON rows. Trace tools and sandbox APIs are symbolic runtime surfaces. Diagnostic reports are prose knowledge artifacts. External harness patches are symbolic/prose system-definition artifacts depending on whether they edit code, prompts, tools, validators, or configuration.

**Lineage.** Trace-to-index lineage is strong: sidecars include source size and `mtime_ns`, and rows retain byte offsets into the canonical JSONL. Trace-to-report lineage is weaker: reports can cite trace ids and span ids if the agent includes them, but there is no enforced report schema with source-span citations, prompt version, or regeneration record. Report-to-patch lineage is outside HALO unless the surrounding human/coding-agent workflow records it.

**Behavioral authority.** Raw traces are knowledge artifacts when consumed as evidence. Sidecar indexes have runtime selection authority but are derived, not canonical. Trace tools enforce context-budget behavior for the analyst agent. Diagnostic reports advise or direct a harness maintainer; they do not themselves alter runtime behavior. A promoted harness patch becomes a system-definition artifact because the modified prompt, tool, code path, validator, or configuration changes future agent behavior.

**Scope.** HALO is per trace dataset and per target harness. Its findings can generalize across repeated failures in one deployment or benchmark split, but the repository does not implement a cross-project memory bank of learned fixes.

**Timing.** Trace capture happens during the target harness run. HALO analysis is offline or staged after traces exist. Behavior change happens in a later external promotion cycle: apply edits, redeploy, collect new traces, rerun HALO.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), HALO belongs with trace-to-artifact harness optimization systems, closest to Meta-Harness and Agentic Harness Engineering rather than conversation-memory stores. It strengthens the survey split between raw traces, diagnostic artifacts, and system-definition promotion: HALO implements the first two carefully and leaves the final patch promotion as an explicit external step.

## Curiosity Pass

HALO's strongest mechanism is not "RLM" branding; it is the mundane interface design around trace scale. The index, byte budgets, oversized summaries, and surgical reads are what prevent a general LLM from drowning in logs.

The report-to-patch boundary is easy to overstate. The README describes feeding HALO's report into a coding agent to apply harness changes, but the package reviewed here does not perform that edit or verify the changed harness. The system is an optimizer loop only when embedded in an outer workflow that owns patching, evaluation, and redeployment.

The sidecar index chooses local pragmatism over cryptographic certainty. Size and `mtime_ns` are enough for local append-mostly traces, but not enough for content-addressed provenance. That is fine for a CLI engine; it would be too weak for a long-lived evidence archive unless paired with stronger checksums or git/object-store lineage.

Subagents give decomposition capacity, but not shared long-term memory. They are fresh analysis workers with bounded tools and parent lineage. Treating their conversation context as memory would blur a useful boundary: the durable retained artifacts are the traces, sidecars, and external reports.

The sandbox is carefully scoped, but availability-dependent. If Deno/Pyodide resolution fails, `run_code` is simply dropped from the tool surface. That graceful degradation is good operationally, but it means analyses relying on code execution need to record whether the sandbox was actually available during the run.

## What to Watch

- Whether HALO adds a first-class report artifact with enforced trace/span citations, prompt/config provenance, and regeneration metadata.
- Whether the outer patch-promotion loop becomes implemented in-repo rather than described as "feed the report to Cursor or Claude Code."
- Whether benchmark harnesses start storing before/after patches, trace ids, and evaluation deltas as one auditable lineage bundle.
- Whether sidecar fingerprinting moves from size/mtime to content hashes for stronger evidence integrity.
- Whether HALO grows a persistent library of recurring harness failures, which would turn it from a per-dataset analyst into a reusable agent-memory system.

## Bottom Line

HALO is a code-grounded trace-analysis and harness-optimization system, not a conventional memory database. Its useful retained artifacts split cleanly: raw OTel JSONL traces are source evidence, sidecar indexes are derived runtime surfaces, trace tools and subagents provide progressive disclosure and analysis, diagnostic reports are trace-derived knowledge artifacts, and only externally promoted harness edits become system-definition artifacts that change future agent behavior.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: HALO is a trace-to-diagnostic-to-harness-patch system with external promotion.
- [Meta-Harness](./meta-harness.md) - compares-with: both optimize harness behavior from traces, but HALO's reviewed implementation stops at diagnostic reports while Meta-Harness centers executable patch candidates.
- [Agentic Harness Engineering](./agentic-harness-engineering.md) - compares-with: both treat observability traces as the raw substrate for harness improvement, with different packaging around promotion.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: HALO reports advise maintainers and coding agents before any harness edit is applied.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: behavior changes only after a report is promoted into prompts, tools, code, validators, or configuration.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: HALO cleanly separates storage substrate, representational form, lineage, and behavioral authority across traces, indexes, tools, reports, and patches.
