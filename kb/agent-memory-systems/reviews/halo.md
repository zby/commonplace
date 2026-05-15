---
description: "HALO trace-analysis engine for optimizing agent harnesses from OTel JSONL runs, with bounded trace tools, subagent fan-out, sandboxed code analysis, and coding-agent-mediated harness edits"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-30"
---

# HALO

HALO is Context Labs' Python engine and CLI for Hierarchical Agent Loop Optimization: collect execution traces from an agent harness, run a specialized trace-analysis agent over those traces, then feed the diagnostic report to a coding agent or maintainer to change the harness. The repository positions HALO as an RLM-style automatic optimization loop, but the implemented package is more precise: a trace-exploration runtime with bounded inspection tools, optional subagents, LLM synthesis, sandboxed Python analysis, and demos that wire OpenAI Agents SDK and AppWorld traces into the loop.

**Repository:** https://github.com/context-labs/halo

**Source directory:** `related-systems/context-labs--halo/`

**Reviewed commit:** [0c149bd2501b658627bb04f1e1f1cda6181a0a73](https://github.com/context-labs/halo/commit/0c149bd2501b658627bb04f1e1f1cda6181a0a73)

## Core Ideas

**Trace analysis is the central runtime, not a memory database.** The public loop is explicit: collect OpenTelemetry-compatible traces, feed them into the HALO engine, produce findings, then let a coding agent apply harness changes ([README.md](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/README.md)). The engine entrypoint builds a sidecar trace index, loads a `TraceStore`, creates a root OpenAI Agents SDK agent, and streams events back to the caller ([engine/main.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/main.py)). There is no persistent memory store of learned lessons inside the engine; the durable target is the downstream harness artifact changed after the report.

**The trace substrate is JSONL plus a derived sidecar index.** `TraceIndexBuilder` scans the trace file, groups spans by `trace_id`, records byte offsets and lengths, rolls up span counts, model names, agent names, token totals, service names, error flags, and project id, then writes `.engine-index.jsonl` plus metadata atomically ([engine/traces/trace_index_builder.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/traces/trace_index_builder.py)). Reuse is guarded by source size and mtime, so the index is a cache over the trace file rather than a new source of truth.

**Trace tools enforce progressive disclosure over long runs.** The default prompt requires `get_dataset_overview` first, real trace ids only, `query_traces` for pagination, `view_trace` only for small traces, and `search_trace` plus `view_spans` for large traces ([engine/agents/prompt_templates.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/agents/prompt_templates.py)). `TraceStore` backs that discipline with 4 KB discovery truncation, 16 KB surgical-span truncation, noisy OpenInference projection dropping, and a 150K-character per-call guard that returns an oversized summary instead of dumping spans ([engine/traces/trace_store.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/traces/trace_store.py)).

**The engine can decompose analysis through bounded subagents.** The root agent receives trace tools, `synthesize_traces`, `get_context_item`, optional `run_code`, and `call_subagent` when depth allows. Subagent spawning is structurally gated by maximum depth and per-depth semaphores so parallel delegation does not deadlock across recursive levels ([engine/tools/subagent_tool_factory.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/tools/subagent_tool_factory.py)). This is an analysis orchestration mechanism, not a multi-agent shared memory system.

**Sandboxed code analysis is a first-class trace tool.** When Deno/Pyodide resolves, `run_code` gives the model read-only access to the active trace file and index, plus NumPy/Pandas, in a fresh WASM subprocess with scoped read permissions, no network, no write, capped stdout/stderr, and a timeout ([engine/tools/run_code_tool.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/tools/run_code_tool.py), [engine/sandbox/sandbox.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/sandbox/sandbox.py)). That makes aggregate trace measurement available without handing the model host filesystem authority.

**Integration is packaged as copied tracing code plus a CLI, not as transparent framework magic.** The CLI is a thin Typer wrapper over `stream_engine_async`: `halo TRACE_PATH --prompt ...` with depth, turns, model, parallelism, and instruction overrides ([halo_cli/main.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/halo_cli/main.py), [halo_cli/README.md](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/halo_cli/README.md)). The OpenAI Agents SDK integration instructs users to copy `tracing.py`, register a file processor before agent construction, and pass the resulting JSONL into the engine ([docs/integrations/openai-agents-sdk.md](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/docs/integrations/openai-agents-sdk.md)).

## Comparison with Our System

| Dimension | HALO | Commonplace |
|---|---|---|
| Primary substrate | OTel-shaped JSONL execution traces plus derived sidecar index | Markdown KB artifacts under git |
| Durable learned artifact | Harness prompt/tool/code edits made after diagnostic report | Notes, instructions, indexes, skills, validation rules, review decisions |
| Retrieval model | Tool-mediated trace overview, filtering, substring search, span views, LLM synthesis, sandboxed analysis | `rg`, descriptions, generated indexes, authored links, skill-guided reads |
| Consumer | Coding agent or maintainer optimizing an agent harness | Future agents and maintainers operating a knowledge base |
| Governance | Trace-format validation, bounded tools, sandbox policy, tests; promotion is outside engine | Frontmatter/type validation, review gates, collection contracts, explicit artifact lifecycle |
| Learning loop | Trace-derived diagnostic report drives harness revisions | Work traces and reviews can be distilled into library notes/instructions when warranted |

HALO is close to commonplace on the diagnosis that agent improvement is a context-engineering problem, but it starts from runtime behavior instead of curated knowledge artifacts. Commonplace asks "what artifact should future agents read before acting?"; HALO asks "what failure pattern is visible across traces, and what harness change should a coding agent make?" That makes HALO a stronger reference for evidence collection and aggregate behavioral diagnosis, while commonplace remains stronger on artifact contracts, authority, lifecycle, and inspectable accumulated knowledge.

The largest divergence is where learning terminates. HALO's engine output is a report streamed to stdout; the repository's own skill says to treat the engine as diagnostic evidence and verify any code claims before editing ([skills/claude/SKILL.md](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/skills/claude/SKILL.md)). Commonplace tries to make the promoted artifact itself durable, typed, reviewable, and discoverable. HALO instead leaves promotion to the outer coding workflow.

## Borrowable Ideas

**Bounded trace reading as a reusable diagnostic surface.** A commonplace review or fix sweep could benefit from a HALO-like pattern over command logs: overview first, filtered summaries second, surgical reads only when justified. Ready to borrow as a design pattern; not ready as code until we have a stable trace/log schema.

**Sidecar indexes that remain caches.** HALO's index records offsets and rollups but preserves the trace file as the authority. This is the right shape for any future commonplace compiled views over large operational logs: derived, fingerprinted, regenerable, and cheap to invalidate. Ready to borrow when log volume exceeds `rg` comfort.

**Sandboxed analytical code with narrow mounted inputs.** `run_code` is a useful middle ground between "let the model inspect everything" and "force all analysis through fixed tools." For commonplace, this would look like a read-only dataset mount for generated review bundles or validation outputs, with no write authority. Worth borrowing only after a concrete high-volume analysis use case appears.

**Trace evidence before harness edits.** HALO's skill correctly separates diagnosis from execution: engine output is evidence; the coding agent still verifies source before patching. That is directly compatible with commonplace's review discipline and ready to borrow into any future "fix from run traces" instruction.

**AppWorld as an evaluation target for harness-level memory changes.** The AppWorld demo is not just a toy integration: it documents trace patching, parallel trace merge, output locations, and eval workflow ([demo/appworld/README.md](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/demo/appworld/README.md), [demo/appworld/HALO_PATCH.md](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/demo/appworld/HALO_PATCH.md)). This is a good candidate benchmark if we ever want to test whether commonplace-style instructions or skills improve an agent harness.

## Trace-derived learning placement

HALO qualifies, but the placement should be narrow. The implemented engine is a trace-derived diagnostic runtime; the durable learning step is coding-agent- or maintainer-mediated harness modification, not an internal memory store.

**Trace source.** The raw signal is OTel-shaped JSONL spans from agent executions: agent, LLM, tool, guardrail, chain, and generic spans. The OpenAI Agents SDK integration writes one JSON line per span with `trace_id`, `span_id`, timing, status, resource attributes, and normalized `inference.*` keys ([docs/integrations/openai-agents-sdk.md](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/docs/integrations/openai-agents-sdk.md)).

**Extraction.** The engine extracts dataset rollups, filtered trace summaries, substring-localized spans, selected full spans, LLM syntheses, and optional sandbox-computed aggregate statistics. The oracle is the trace-analysis agent plus any downstream human/coding-agent verification; there is no implemented scorer that automatically accepts or rejects harness patches.

**Representational form.** Raw substrate is event traces. The first derived substrate is prose diagnostic output. The final behavior-changing substrate, when the loop succeeds, is symbolic system-definition material: harness prompts, tool descriptions, retry logic, configuration, or code edits.

**Behavioral authority.** The trace index is a knowledge artifact: it expands reach over traces but does not itself change future agent behavior. The promoted harness edits are system-definition artifacts: once deployed, reading or executing the changed prompt/tool/code alters the agent's disposition.

**Scope.** Scope is per harness and per benchmark/deployment. The README's AppWorld example reports improvements on dev and test splits, but the mechanism is still harness-local rather than cross-project generalized learning.

**Timing.** Collection is online during harness execution. Analysis and promotion are staged after trace capture: run HALO over a trace file, inspect the report, patch the harness, redeploy, and collect another batch.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), HALO belongs with trace-to-system-definition outer loops rather than memory-store systems. It strengthens the survey's distinction between trace-derived knowledge and trace-derived disposition: the engine's report is knowledge until an external actor commits a harness change.

## Curiosity Pass

**The README overstates autonomy relative to the code boundary.** The marketing phrase "automatic agent optimization loop" is fair for the whole workflow, but the package does not autonomously edit, verify, or redeploy a harness. The implemented engine is a powerful diagnostic step in that loop.

**The trace tools are more mature than the promotion path.** Bounded reads, oversized summaries, byte-offset indexes, subagent depth gates, and sandbox policy are concrete. By contrast, report-to-patch promotion lives mostly in instructions and demos. That is a good engineering boundary, but it means claims about optimization quality depend on the surrounding coding workflow.

**Compaction is local conversation hygiene, not long-term memory.** The engine compacts older agent context items so the trace-analysis run can continue within context limits ([engine/agents/agent_context.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/agents/agent_context.py), [engine/agents/compactor.py](https://github.com/context-labs/halo/blob/0c149bd2501b658627bb04f1e1f1cda6181a0a73/engine/agents/compactor.py)). Those summaries are not persisted as reusable lessons after the run.

**String search is intentionally simple.** `search_trace` matches literal substrings against raw span JSON. That is robust and cheap, but it leaves semantic grouping to the analysis model or `run_code`. The design bets that trace schemas and tool discipline beat heavier retrieval machinery for this use case.

**The sandbox has a pragmatic availability failure mode.** If Deno or Pyodide assets are unavailable, the engine drops `run_code` from the tool surface rather than failing the whole run. That is operationally sane, but it means reproducibility of a HALO analysis can depend on whether the sandbox resolved on that host.

## What to Watch

- Whether HALO adds an implemented patch-generation and verification stage, or keeps report-to-harness promotion deliberately outside the engine.
- Whether the AppWorld claims become reproducible scripts with checked-in before/after prompts and exact trace-derived reports, not just benchmark deltas in the README.
- Whether the trace index grows beyond scalar rollups into semantic clustering or learned failure taxonomies.
- Whether trace schemas are generalized beyond OpenAI Agents SDK/AppWorld without making integration heavier than the current copied `tracing.py` approach.
- Whether sandboxed analysis becomes mandatory for serious runs, which would make Deno/Pyodide packaging part of the core reliability story rather than an optional tool.

---

Relevant Notes:

- [Distillation](../../notes/definitions/distillation.md) — rationale: HALO is directed compression from execution traces into diagnostic prose and, after promotion, harness changes.
- [System-definition artifacts are crystallized reasoning under context scarcity](../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context-scarcity.md) — extends: HALO's useful endpoint is not the report itself but the harness prompt/tool/code edit that changes future behavior.
- [Memory design adds operational axes to artifact analysis](../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) — compares-with: HALO makes evaluation signal and promotion authority central, but keeps the durable artifact lifecycle outside the engine.
- [Agentic Harness Engineering](./agentic-harness-engineering.md) — compares-with: both use trace-derived diagnosis to improve coding-agent harnesses, but HALO packages the trace-analysis runtime while Agentic Harness Engineering emphasizes the broader observability-to-promotion loop.
