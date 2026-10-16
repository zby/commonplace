---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Halo memory: trace caches, isolated analysis contexts, optional checkpoints and desktop conversation/report read-back."
run-id: AAS-2026-10-14-halo-c4ed89d7f99f-01
source-identity: https://github.com/context-labs/halo
reviewed-boundary: b7f8509745d67b499b4e80efe20ea37c03426a74
---

# Halo memory report

## Boundary and evidence

Halo retains both telemetry evidence and model-authored diagnoses. This report covers those objects, working-context controls, desktop follow-ups, report handoff, cleanup and the shipped evaluation example. The frozen source is SRC-1 at `b7f8509745d67b499b4e80efe20ea37c03426a74`, as registered in [boundary](boundary.md#source-register). The enclosing desktop is included. External coding-agent execution, arbitrary harness changes and deployment remain outside the complete-artifact, partial-loop boundary.

Direct source reads added context item/retrieval definitions, compaction selection/rendering, sidecar freshness and schema, trace-view budgets and raw search, desktop turn selection and report rendering, export selection, telemetry ingestion/clear operations, event presentation, and AppWorld evaluation/report/cleanup paths. All are implementation evidence; compaction instructions are doctrine/design. Supplied runtime records supply CLI dispatch, registration, child construction, optional repository/sandbox grants, bridge final-answer fallback, handoff and engine-install findings. No execution, provider state or intervention comparison was inspected. Available adapter internals, task-specific evaluation modules and provider caching internals remain uninspected, not inaccessible or absent.

| Entry point or operation | Source path in SRC-1 | Coverage and remaining limits |
| --- | --- | --- |
| CLI/public engine loading | `halo_cli/main.py`, `engine/main.py` | Supplied [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis); direct index inspection in [MEM-OBJ-trace-index](#mem-obj-trace-index). Caller-provided file provenance is not authenticated. |
| Desktop OTLP and file/Langfuse/Phoenix imports | `app/src/server/telemetry/storage.ts`, `app/src/server/fileimport/importQueue.ts`, `app/src/server/langfuse/importQueue.ts`, `app/src/server/phoenix/importQueue.ts` | Direct common ingestion/clear reads in [MEM-RTE-telemetry-admission](#mem-rte-telemetry-admission); boundary supplies adapter caller discovery. Adapter transformations remain uninspected, preventing fidelity and complete provenance claims. |
| Desktop export and reuse | `app/src/server/halo/exporter.ts`, `app/src/server/halo/runQueue.ts` | Direct selection/reuse reads; [MEM-OBJ-traces-jsonl](#mem-obj-traces-jsonl), annotation on [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis). |
| Trace overview/query/count, views and raw searches | `engine/traces/trace_store.py`, `engine/tools/subagent_tool_factory.py` | Direct view/search/render and schema reads; supplied tool registration. [MEM-RTE-trace-read](#mem-rte-trace-read). Query/filter implementation not exhaustively audited; no exhaustive relevance guarantee. |
| Trace synthesis | `engine/tools/synthesis_tool.py`, `engine/traces/trace_store.py` | Supplied [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis), direct render countercheck; annotation distinguishes a tool result from a persistent summary cache. |
| Child isolation and retry trimming | `engine/tools/subagent_tool_factory.py`, `engine/agents/agent_context.py`, `engine/agents/openai_agent_runner.py` | Supplied child route, direct trimming and terminal branch reads; [MEM-OBJ-agent-context](#mem-obj-agent-context) and annotations. |
| Compaction/checkpoint and original-item retrieval | `engine/agents/compactor.py`, `engine/agents/agent_context.py`, `engine/tools/agent_context_tools.py` | Direct selection, transformation, rendering and retrieval reads; [MEM-RTE-context-reload](#mem-rte-context-reload), checkpoint annotation. No shipped desktop checkpoint consumer. |
| Turns, events and report | `app/src/server/halo/storage.ts`, `app/src/server/halo/report.ts`, `app/src/mainview/halo/haloAgentConsolePresenter.ts` | Direct reads in [MEM-OBJ-halo-run-turns](#mem-obj-halo-run-turns), [MEM-OBJ-halo-run-events](#mem-obj-halo-run-events), [MEM-OBJ-report](#mem-obj-report); follow-up differs from human event display. |
| Cancellation, retry, deletion and telemetry clear | `app/src/server/halo/runQueue.ts`, `app/src/server/halo/storage.ts`, `app/src/server/telemetry/storage.ts` | Direct reads and [MEM-RTE-retention-cleanup](#mem-rte-retention-cleanup). Deletion does not retract already delivered reports or guarantee physical file removal. |
| Coding handoff and installed engine revision | `app/src/desktop/commands.ts`, `skills/claude/SKILL.md`, `app/src/server/halo/engine.ts` | Supplied [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff), [RT-RTE-engine-install](runtime.md#rt-rte-engine-install). Static skill is guidance, not acquired memory; installed code is machinery, not trace-derived memory. External patch approval/rollback uninspected. |
| Demo trace producers, evaluator and output cleanup | `demo/openai-agents-sdk-demo/tracing.py`, `demo/appworld/experiments/code/openai_agents/run.py`, `demo/appworld/src/appworld/evaluator.py`, `demo/appworld/Taskfile.yml` | Boundary supplies producer scope; direct evaluator/task reads in [MEM-OBJ-evaluation-report](#mem-obj-evaluation-report). Task-specific oracle modules and historical results uninspected; no automatic evaluation-to-prompt update established. |
| Optional code/Git tools and sandbox | `engine/tools/subagent_tool_factory.py`, `engine/code/code_repo.py`, `engine/git/git_repo.py`, `engine/sandbox/sandbox.py` | Supplied [RT-RTE-repository-inspection](runtime.md#rt-rte-repository-inspection), [RT-RTE-sandbox-python](runtime.md#rt-rte-sandbox-python). Current-run evidence/results, not a newly retained repository KB or persistent sandbox. |
| Provider model/caching state | `engine/agents/compactor.py`, `engine/model_config.py` | Local configuration and supplied model components; opaque remote state not inspected. Cache-oriented prompt construction does not establish a semantic memory store or provider learning. |

## Core ideas

1. **Evidence stays on disk; returned views are lossy.** Symbolic indexes point into JSONL rather than replacing its payloads. Tool views cap attributes and may return only an oversized summary. Raw regex search can recover selected omitted text, not automatically restore the whole trace. [MEM-OBJ-trace-index](#mem-obj-trace-index), [MEM-RTE-trace-read](#mem-rte-trace-read).
2. **Desktop read-back promotes answers, not full investigation histories.** Software stores selected bridge answers as assistant turns and later sends their text back to the engine. Child/tool events are separately retained for display, not selected by the follow-up history builder. There is no per-answer human approval or factual oracle at that admission point. [MEM-OBJ-halo-run-turns](#mem-obj-halo-run-turns), [MEM-BAP-followup-history](#mem-bap-followup-history).
3. **Working-context controls are route-specific.** Children start with selected delegated input and return an answer; retry removes inconsistent tool tails. Compaction is optional terminal checkpoint preparation, not continuous context-window management in ordinary CLI/desktop runs. Local originals survive compaction, but rendered checkpoints do not carry their full backing items. [MEM-OBJ-agent-context](#mem-obj-agent-context), [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call), [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission).
4. **Retention is not validation.** A completed answer may be a bridge fallback. A report copies retained conversation, including incomplete findings, and affords external action through a path-bearing instruction. Evaluation reports are separate artifacts; the improvement skill asks an external actor to compare results. Neither mechanism establishes improved future diagnosis or a closed automatic revision loop. [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis), [MEM-OBJ-report](#mem-obj-report), [MEM-OBJ-evaluation-report](#mem-obj-evaluation-report).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-traces-jsonl
Label: Captured spans and trace export

Source-native identity: JSONL input and desktop `traces.jsonl`; spans are also retained in SQLite `spans`. Form: symbolic span envelopes, identifiers, times/status/attributes; natural-language prompts, outputs and code strings inside attributes remain interpreter-dependent content. This is raw execution evidence as supplied or normalized, not an adopted diagnosis. Storage: caller files, desktop SQLite and per-run export directory. Lineage: user/service telemetry through adapters and common decoder/upsert, then filtered export. Adapter names do not authenticate originating execution. Evidence: SRC-1, `app/src/server/telemetry/storage.ts`, `app/src/server/halo/exporter.ts`; closest supplied records are [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis) and [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis). This object spans their input/export surfaces rather than duplicating either route.

Export selection uses target type and filters/free text to obtain trace IDs; session selection expands to the sessions' traces. SQL retrieves spans for those IDs and export maps them into Halo envelopes. Later follow-ups reuse the existing path by existence, not by comparison with updated SQLite telemetry. Clearing live telemetry therefore does not itself clear retained exports. The analysis model consumes evidence through tools, with no correctness authority conferred by storage. Export JSONL preserves payload-bearing attributes but is not the original upstream byte stream.

> const jsonl = rows.map((row) => JSON.stringify(spanRowToHaloSpan(row))).join("\n");
> writeFileSync(path, jsonl ? `${jsonl}\n` : "", "utf8");
> --- `app/src/server/halo/exporter.ts`

#### MEM-OBJ-trace-index
Label: Trace index rows and freshness metadata

Part of: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis)

This is the persisted cache part of the diagnosis route, not another agent. Source-native identity: `TraceIndexRow`, `TraceIndexMeta`, `.engine-index.jsonl` and meta sidecars. Form: symbolic offsets/lengths and aggregate fields, separately from symbolic access/freshness metadata. Storage: sidecar disk files loaded into `TraceStore` memory. Lineage: deterministic parsing/grouping of input JSONL; no model authorship or per-row human approval. Consumers: queries/overview/count read rollups; views/search seek source offsets. Authority: access and filtering rules, not model instructions. Evidence: SRC-1, `engine/traces/models/trace_index_models.py`, `engine/traces/trace_index_builder.py`, `engine/traces/trace_store.py`.

Freshness compares schema, size and nanosecond mtime, not a content digest. Writes replace temporary index and metadata files separately; this is not a claim of a two-file transaction. Matching fingerprint allows reuse across runs. Content changes preserving the fingerprint are not detected by this predicate. Unknown initial trace provenance does not obscure this known derived-cache mechanism.

> existing.schema_version == config.schema_version
> and existing.source_size == current_size
> and existing.source_mtime_ns == current_mtime_ns
> --- `engine/traces/trace_index_builder.py`

#### MEM-OBJ-agent-context
Label: Agent context originals and summaries

Source-native identity: `AgentContext.items`, `_index`, `AgentContextItem.compaction_summary`. Storage: per-agent process memory. Form: natural-language message bodies and summaries; symbolic role/tool-call/item and parent lineage fields. Original content/tool fields survive compaction while rendered messages substitute summary text. Current-run accumulation is not automatically durable memory. A summary becomes retained memory only when a later invocation receives it; that is afforded through checkpoints, not shown as desktop read-back. Evidence: SRC-1, `engine/agents/agent_context_items.py`, `engine/agents/agent_context.py`, `engine/agents/compactor.py`.

Closest supplied records are [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis), [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call) and [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission). This shared data structure spans those routes, with separate originals and summary consumption paths rather than duplicating them. Compaction model mutability belongs to [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model).

A caller's leading system message passes through instead of engine-generated guidance, permitting externally retained continuations and caller-authored instructions. Caller identity alone does not establish human content approval. Children use independent contexts; only their returned answer crosses into the parent. This fits a work-frame analogy, but a rendered item ID is not a dereferenceable heap pointer without the backing local `_index`. Retry trimming deletes removed items from both items and index. Checkpoint rendering carries messages/counters, not the full originals/lineage store.

> if has_system:
>     sys_item = AgentContextItem(
>         item_id="sys-0",
>         role="system",
>         content=messages[0].content,
>     )
>     body = messages[1:]
> --- `engine/agents/agent_context.py`

> for item in removed:
>     self._index.pop(item.item_id, None)
> --- `engine/agents/agent_context.py`

#### MEM-OBJ-halo-run-turns
Label: Desktop retained conversation turns

Part of: [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis)

The part is durable conversation content, not the whole scheduling route. Source-native identity: `halo_run_turns`, with legacy prompt/`finalAnswer` fallback from `halo_runs`. Storage: SQLite text rows and per-turn result JSON. Form: natural-language questions/diagnoses, symbolic role/order/status/error metadata. Lineage: user questions plus bridge-selected model output; legacy turns are synthesized and persisted on first follow-up. Software updates assistant content when it receives completed/incomplete events. No per-answer human content approval, independent truth test or semantic rejection gate is shown at retention. The bridge fallback limits answer provenance as [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis) establishes. Evidence: SRC-1, `app/src/server/halo/storage.ts`, `app/src/server/halo/runQueue.ts`.

Later consumer: engine via `buildRunnerMessages`, selecting earlier user turns and every nonempty assistant turn regardless of assistant status; no explicit history length/token cap in that builder. A failed/cancelled nonempty row is not excluded by status. Retry sets the latest assistant status pending without clearing content; the pending turn is excluded by index from that attempt's input, but until overwrite its old content remains retained. Reports apply a different status filter. Authority at the later model is conversational evidence, not dispatcher policy. Reasons persist only if present in the selected answer text; the full investigation does not re-enter through this path.

> .filter(
>   (turn) =>
>     turn.turnIndex < upToTurnIndex &&
>     (turn.role === "user" || turn.content.trim().length > 0),
> )
> .map((turn) => ({ content: turn.content, role: turn.role }));
> --- `app/src/server/halo/storage.ts`

#### MEM-OBJ-halo-run-events
Label: Analysis event payloads and display

Part of: [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis)

Source-native identity: `halo_run_events`, `HaloRunEvent.payload`. Storage: SQLite event rows; live publication is separate delivery. Form: symbolic event IDs, sequence/turn/agent metadata and JSON envelopes containing natural-language messages or executable tool arguments/results. Lineage: bridge stream including root and child activity, not a verified reasoning transcript or learned policy. Event persistence is software admission without human content approval. Human activity UI consumes payloads through a presenter; `rawPayload` remains alongside readable rows. The presenter extracts messages, tool calls/results or falls back to JSON. Display summaries are not the opaque/raw payload itself and are not what follow-up history selects. Evidence: SRC-1, `app/src/server/halo/runQueue.ts`, `app/src/server/halo/storage.ts`, `app/src/mainview/halo/haloAgentConsolePresenter.ts`; no separate durable event-to-agent replay route is established by the inspected history builder.

> rawPayload: payload,
> --- `app/src/mainview/halo/haloAgentConsolePresenter.ts`

#### MEM-OBJ-report
Label: Materialized conversation report

Part of: [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff)

This is the handoff's retained input artifact, produced by desktop code rather than the external actor. Source-native identity: `report.md`, artifact type `report_markdown`. Storage: run directory file plus SQLite artifact path/size metadata. Form: natural-language prompts/findings inside deterministic Markdown sections and symbolic run/status/model/scope headers. Lineage: retained turns, not a second model synthesis or an independently validated report. Software admits content when a nonempty run final answer allows materialization; no per-finding human approval. Human display and the external coding actor are later consumers, the latter afforded by [RT-BAP-report-prompt](runtime.md#rt-bap-report-prompt). Evidence: SRC-1, `app/src/server/halo/report.ts`.

It includes all user turns and nonempty assistant turns marked completed or incomplete. It omits tool/event histories. Missing/stale files are rewritten using run updatedAt versus mtime, not content-aware review; external edits are not an adopted-turn editing surface and may be overwritten. Artifact metadata locates content, not evidence of correctness. Reasons can reach the coding actor if written in included findings, but no structured claim-to-criticism/adoption ledger is generated here.

> turn.role === "user" ||
> ((turn.status === "completed" || turn.status === "incomplete") &&
>   turn.content.trim().length > 0),
> --- `app/src/server/halo/report.ts`

#### MEM-OBJ-evaluation-report
Label: AppWorld task evaluation artifacts

Source-native identity: task `evaluation/report.md`, `version.txt`, dataset evaluation JSON/text. Storage: experiment output files. Form: symbolic scores/test outcomes plus readable report text; not model parameters or engine guidance. Lineage: AppWorld loads task-output databases and task ground truth, then invokes its task-specific evaluation module. This is distinct from the Halo conversation report; closest supplied [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) prescribes a coding actor's remeasurement rather than implementing this evaluator.

Evidence: SRC-1, `demo/appworld/src/appworld/evaluator.py`, `demo/appworld/Taskfile.yml`. The evaluator supplies ground-truth answer/public/private data and before/after models to a reference module; module correctness and individual task internals remain uninspected. `save_report` controls software persistence, not human per-result approval. The returned tracker is immediate computation; files afford later inspection. The supplied skill prescribes human/coding-actor comparison, but the inspected AppWorld analyze task passes traces and a question to Halo, not these evaluation files. No wired evaluation-result-to-Halo instruction revision is established. Output cleanup removes these files with traces; source stays intact.

> evaluation_module.evaluate(
>     test=test_tracker,
>     public_data=ground_truth.public_data,
>     private_data=ground_truth.private_data,
>     main_user=main_user,
>     models=models,
>     ground_truth_answer=ground_truth.answer,
> )
> --- `demo/appworld/src/appworld/evaluator.py`

> test_tracker.report(print_it=False, colorize=False, save_file_path=evaluation_file_path)
> --- `demo/appworld/src/appworld/evaluator.py`

### Routes

#### MEM-RTE-telemetry-admission
Label: Telemetry decoding and admission

Input OTLP body from shipped callers → decode/build rows → transactional span/search upsert and trace-summary refresh → retained telemetry available to later export/UI. Code owns normalization, write admission and transaction; users/services supply telemetry, not a per-span human approval. This is distinct from [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis), which starts from retained telemetry and schedules diagnosis. Evidence: SRC-1, `app/src/server/telemetry/storage.ts`; adapter caller scope is supplied by boundary.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Batch ID and accepted span/trace counts, with optional live publication.
- Later read-back: Desktop export and telemetry queries consume the updated tables on subsequent requests; existing run exports can remain older snapshots.
- Delegated visibility: inapplicable — normalization is host code, not model delegation.
- Selection predicate: Decoder/row builder and keyed span upsert; searchMode can omit search indexing, while summaries refresh for affected trace IDs.
- Invalidation or expiry: Later upsert may replace same-key values; clearTelemetryData removes telemetry/search/summary/batch/live-event tables, not Halo conversation/export artifacts.
- Activation or effect: Database state changes available evidence; no semantic promotion of traces into instructions occurs here.
- Evidence limits: Adapter mapping fidelity and original execution authenticity remain uninspected; acceptance counts are not correctness judgments.

Admission is ingestion mode, not hypothesis testing. Software rejects by decoding/transaction failure rather than a truth oracle; transaction supplies write rollback for this database operation. Generic telemetry caller identity does not establish a human content decision. Original provenance remains local to each adapter/input.

> const decoded = decodeOtlpJsonBody(input.body);
> const rows = buildSpanRowsFromOtlp(decoded, receivedAt);
> --- `app/src/server/telemetry/storage.ts`

> for (const row of rows) {
>   upsertSpan(sqlite, row);
>   if (input.searchMode !== "none") {
>     upsertSearch(sqlite, row, input.searchMode ?? "full");
>   }
> }
> --- `app/src/server/telemetry/storage.ts`

#### MEM-RTE-trace-read
Label: Budgeted trace evidence retrieval

Part of: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis)

This part is the trace selector/delivery mechanism, not the model's whole diagnosis. Calling model supplies IDs, filters/regex and limits → index/JSONL store reads → bounded typed result → calling model's tool context. SRC-1, `engine/traces/trace_store.py`; supplied [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis) is a separate summarizer consumer, not a duplicate of retrieval.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Overview/query/count metadata, span views, oversized summary or regex matches with source IDs and context windows.
- Later read-back: Retained JSONL/index evidence is selected on later tool invocations; results accumulate in the current context, but this route writes no persistent learned summary.
- Delegated visibility: Root/children share the store grant, but only each caller's chosen results enter that caller's context; synthesis gets separately rendered metadata.
- Selection predicate: Model-requested trace/span IDs, filters/regex; view_trace caps attribute strings at 4096 characters, view_spans at 16384; both can drop all spans above 150000 serialized bytes. search_span defaults to 50 matches and 100 context characters, scanning raw JSON.
- Invalidation or expiry: View truncation is non-destructive; original JSONL remains reachable by index/raw search. Store/index freshness is startup-dependent, not a live frozen snapshot guarantee.
- Activation or effect: Tool result delivers selected evidence; reliance and correct interpretation are unobserved. Oversized views include follow-up recommendations rather than silently loading all text.
- Evidence limits: Returned views omit noisy flat projections and long tails. Raw search recovers matching windows, not proof of complete relevant evidence or source truth.

Selection is model-directed evidence acquisition in an open diagnostic request, not an expected-answer oracle. Model decides next read; code decides truncation and returned shape; caller can stop the run. No human per-read approval is shown. Names/IDs are symbolic selectors, while payload prose can influence model interpretation; no inspected provenance/authenticity mechanism elevates source text to trusted instruction.

> if total_bytes > _VIEW_TRACE_RESPONSE_BYTES_BUDGET:
> --- `engine/traces/trace_store.py`

> return TraceView(trace_id=trace_id, spans=[], oversized=summary)
> --- `engine/traces/trace_store.py:344-344`

#### MEM-RTE-context-reload
Label: Original context item retrieval

Part of: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis)

Calling model requests `get_context_item(item_id)` → its own context index → full stored item returned to its tool history. Code confines the lookup to the calling agent's context; it does not open another agent's frame or a durable checkpoint backing store. This is a distinct retrieval part not separately declared in runtime. Evidence: SRC-1, `engine/tools/agent_context_tools.py`, `engine/agents/agent_context.py`; factory registration is supplied by [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Full AgentContextItem, including original content/tool calls, lineage and any compaction summary; unknown ID raises lookup failure.
- Later read-back: A stored original can reach a subsequent model invocation in the same live context via a tool result. Terminal checkpoint replay alone does not recreate the original item index.
- Delegated visibility: Only the requesting agent's items; returned child answer does not automatically grant access to child originals.
- Selection predicate: Explicit item_id, exact local dictionary lookup; no semantic ranking or explicit result budget in the inspected tool.
- Invalidation or expiry: Trimmed items are removed from the index; context ends with the execution. Compacted originals remain locally indexed until then.
- Activation or effect: Restores item content to visible tool output, not an observed change of model behavior.
- Evidence limits: Ordinary terminal compaction leaves no further model turn in that runner branch; therefore a wired local reload capability is not proof of a shipped post-compaction resume/reload cycle.

> agent_context = tool_context.require_agent_context()
> item = agent_context.get_item(arguments.item_id)
> return GetContextItemResult(item=item)
> --- `engine/tools/agent_context_tools.py`

#### MEM-RTE-retention-cleanup
Label: Retained run and telemetry cleanup

User/service deletion or clear request → host cancellation/table deletion/file cleanup → future table-backed consumers no longer select deleted rows. This crosses telemetry admission and desktop retention; it is not a duplicate of [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis). Evidence: SRC-1, `app/src/server/halo/runQueue.ts`, `app/src/server/halo/storage.ts`, `app/src/server/telemetry/storage.ts`, `demo/appworld/Taskfile.yml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Run deletion boolean or telemetry deletion counts; file-removal errors on run deletion are swallowed.
- Later read-back: Deleted run rows stop ordinary history/report lookup; separate telemetry clear leaves existing run exports/answers intact. AppWorld clean:run-outputs deletes experiment outputs, including traces/evaluation files.
- Delegated visibility: inapplicable — host cleanup is not a delegated model operation.
- Selection predicate: Run ID for conversation/event/artifact/run deletion; telemetry clear targets all named telemetry tables; AppWorld cleanup targets output directory.
- Invalidation or expiry: Run directory is recursively removed best effort after database deletion. There is no shown reverse propagation to previously opened coding sessions or copied reports.
- Activation or effect: Withdraws table-backed retained material and attempts physical file removal; cancellation stops ongoing bridge work rather than judging answer truth.
- Evidence limits: Concurrent deletion/queue behavior and physical erasure were not exercised. Separate nontransactional run DELETE statements do not establish atomic multi-table/file withdrawal.

Human invocation can request withdrawal, but the inspected database helper is software deletion, not per-finding criticism. No rollback/recovery of deleted content is shown; reanalysis needs remaining/reacquired inputs. Cancellation/failure statuses do not automatically invalidate all nonempty conversation content at later readers. Retrying marks the latest assistant pending without clearing its old content; next terminal output replaces it. These distinctions matter because history uses content/index while reports use content/status.

> deleteHaloRun(database.sqlite, runId);
> try {
>   rmSync(outputDirForRun(database.path, runId), { force: true, recursive: true });
> } catch {
>   // Leftover files are harmless; the run rows are gone.
> }
> --- `app/src/server/halo/runQueue.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-followup-history
Label: Retained answers in follow-up context

Part of: [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis)

Consumer: root analysis model on a later desktop turn. Channel: SQLite turn text → role/content runner messages → bridge AgentMessage → engine context, with dashboard rendering guidance added by host. Force: model-interpreted conversational evidence and requests, not executable changes or validated system policy. Horizon: follow-ups within the retained run; software selection is wired, actual reliance unobserved. This is a distinct authority part of desktop follow-up, not [RT-BAP-engine-guidance](runtime.md#rt-bap-engine-guidance) or the external coding report path. Evidence: SRC-1, `app/src/server/halo/storage.ts`, `app/src/server/halo/runQueue.ts`, `app/scripts/halo-local-runner.py`; supporting selection passage is in [MEM-OBJ-halo-run-turns](#mem-obj-halo-run-turns).

> messages = [
>     AgentMessage(role=item["role"], content=item.get("content") or "")
>     for item in raw_messages
>     if isinstance(item, dict) and item.get("role")
> ]
> --- `app/scripts/halo-local-runner.py`

## Annotations

#### On [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call)

Working-context control: code initializes a child with system guidance and parent-selected delegated question, keeping parent transcript out. Only answer/counters/IDs/sequence bounds escape to the parent; host event visibility is a different channel. Local child item lineage is retained during execution but no persistent child session reload is shown. A work frame is the useful analogy; the parent's child ID is not a model-followable pointer to the child's context. Evidence is the supplied route's child initialization passage and SRC-1, `engine/tools/subagent_tool_factory.py`; local backing-store behavior is in [MEM-OBJ-agent-context](#mem-obj-agent-context).

#### On [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis)

Trace-fed transformation: selected trace IDs → reduced render → model-authored natural-language tool summary → calling context. The render contains names/status/times/model/token fields, not the full payload reasoning. It is retained current-run output, not a persistent trace-summary writeback; desktop may retain a later final answer that incorporates it, but that incorporation is model-dependent. Derived rationale is not required by the short summary guidance. No separate persistent synthesis consumer is established. Evidence: supplied route and direct SRC-1, `engine/traces/trace_store.py`, `engine/agents/prompt_templates.py`. Its oversized-render omission is confirmed rather than corrected.

#### On [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission)

Write agency: code selects old non-system text and grouped tool turns by independent keep-last thresholds; compaction model authors each item summary; code commits only a fully successful unit. Ordinary failures keep originals. Summaries are admitted without semantic testing or human review; an empty successful model reply is stripped and still returned as summary. Guidance asks key facts, not preservation of every reason. `_item_as_prompt` uses assistant tool calls instead of accompanying content when calls exist, limiting what the summarizer can preserve. Storage of originals stays local; emitted messages render compacted tool rows as assistant prose, with IDs but without a complete backing original-item store. Source: SRC-1, `engine/agents/agent_context.py`, `engine/agents/compactor.py`, `engine/agents/prompt_templates.py`.

A host can persist/re-supply the messages, including mixed original tail and summaries, using the input continuation surface. Desktop instead persists selected turns and ignores checkpoints. No later checkpoint consumer is wired in the inspected desktop path. This route is terminal-only; comments describing older per-agent/end-turn compaction must not override its actual runner condition.

> You summarize a single conversation item for storage. Preserve tool names,
> argument shapes, and key result facts that future reasoning might need.
> Return a short plain-text summary — no JSON wrapping, no surrounding prose.
> --- `engine/agents/prompt_templates.py`

> if item.tool_calls:
>     calls = "\n".join(
>         f"- {tc.function.name}({tc.function.arguments})" for tc in item.tool_calls
>     )
>     return f"ASSISTANT TOOL CALLS:\n{calls}"
> --- `engine/agents/compactor.py`

#### On [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis)

Read-back selector: follow-up trigger automatically loads prior turns by index/content, not a semantic relevance search or bounded token selector. Existing trace exports are reused by path existence; missing export rebuilds from current matching telemetry, potentially changing evidence between turns while old answers persist. Software separately stores raw events, selected turns and result files; only selected turns enter bridge messages. Report materialization is deterministic curation with a status filter distinct from history's. Source: SRC-1, `app/src/server/halo/runQueue.ts`, `app/src/server/halo/storage.ts`, `app/src/server/halo/report.ts`; object records retain the passages.

> const reuseExport =
>   turnIndex > 1 && Boolean(run.exportPath) && existsSync(run.exportPath ?? "");
> --- `app/src/server/halo/runQueue.ts`

#### On [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff)

Retained material is [MEM-OBJ-report](#mem-obj-report), a conversation projection, not all event evidence and not installed edits. The receiving coding actor is afforded path access, with user confirmation before initiation. That confirmation is distinct from approval of each retained finding or each later code edit. Reasons cross only if included in report text; actual criticism retention and later edit selection remain outside inspected operation. Source: SRC-1, `app/src/server/halo/report.ts`; external-consumer guidance and limits are supplied by the runtime route.

## Write side

**Raw and derived evidence.** Common telemetry ingestion performs automatic normalization/upsert and summary/index maintenance; export copies selected retained spans into JSONL. Sidecar indexes derive access metadata and aggregates. These are software admission, not human approval of each datum. Initial source provenance remains unresolved for arbitrary files and remote adapters. Source: [MEM-RTE-telemetry-admission](#mem-rte-telemetry-admission), [MEM-OBJ-traces-jsonl](#mem-obj-traces-jsonl), [MEM-OBJ-trace-index](#mem-obj-trace-index).

**Model-derived material.** Trace synthesis returns a short summary, but does not itself install a persistent behavior policy. Root/child diagnosis produces text and tool results; the desktop automatically retains the bridge-selected answer. This is the implemented raw-traces → investigation → selected-answer → later-follow-up chain. Human starts/questions the run; software selects and persists model text without an oracle. Event payloads survive separately and cannot be assumed to accompany the selected answer. [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis), [MEM-OBJ-halo-run-turns](#mem-obj-halo-run-turns), [MEM-BAP-followup-history](#mem-bap-followup-history).

**Compaction and alternatives.** Code chooses eligible older units; model summarizes; complete successful units replace rendered content while originals remain local. Failed units and recent tail remain original. Checkpoints can thus mix summary and verbatim messages, but are host-owned persistence affordances, not ordinary desktop memory. Retry trims incomplete tool turns without compaction; emitted events cannot be withdrawn. A caller-supplied leading system message offers a different continuation/adoption surface and bypasses generated engine guidance. [MEM-OBJ-agent-context](#mem-obj-agent-context), [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission), [MEM-RTE-context-reload](#mem-rte-context-reload).

**Maintenance, rejection and withdrawal.** Index fingerprint mismatch rebuilds the cache; it does not criticize content. Retry status change retains old answer until replacement; failure/cancellation is not universal semantic invalidation. Report freshness rewrites a projection, not a curated truth set. Deletion attempts files after removing rows; telemetry clearing does not retract run exports/conversations. AppWorld evaluation retains reference-test outcomes and the skill prescribes external acceptance after remeasurement, not a Halo answer-admission veto. [MEM-RTE-retention-cleanup](#mem-rte-retention-cleanup), [MEM-OBJ-report](#mem-obj-report), [MEM-OBJ-evaluation-report](#mem-obj-evaluation-report), [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff).

## Read-back

- **Model-requested evidence:** explicit tool calls select retained traces using IDs/filters/regex and deliver bounded views or raw matching windows. This is request-driven pull, not unsolicited semantic memory injection. [MEM-RTE-trace-read](#mem-rte-trace-read).
- **Local replay and reload:** retries/reprompts reconstruct completed current-run context and remove inconsistent tails; original-item lookup is explicit and agent-local. Child frame isolation keeps its internal work out of parent input; only returned text can enter a later parent invocation. These are working-context controls even without durable new memory. [MEM-RTE-context-reload](#mem-rte-context-reload), [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis), [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call).
- **Follow-up-triggered automatic supply:** user asks a new question; code selects all qualifying earlier turn text without an explicit budget and sends it through runner config to the next root model invocation. This is requested follow-up with automatic history selection, not an independent background push. Its authority is conversational; loading establishes delivery, not changed decisions. [MEM-BAP-followup-history](#mem-bap-followup-history).
- **Optional checkpoint:** terminal summary/tail messages reach an event consumer; later host persistence and re-supply are afforded, not a wired desktop resume. IDs in rendered messages do not guarantee recoverable originals after process/context disposal. [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission).
- **Human and external consumers:** event presenter displays retained activity; Markdown report supplies selected conversation to an external coding actor through a user-selected deep link. AppWorld evaluation files afford later comparison; the analyzed task selects traces, not evaluation reports. These different consumers cannot be collapsed into a single memory-to-code update. [MEM-OBJ-halo-run-events](#mem-obj-halo-run-events), [MEM-OBJ-report](#mem-obj-report), [MEM-OBJ-evaluation-report](#mem-obj-evaluation-report).

## Integration issues

1. **No supplied fact correction required.** Direct terminal-branch, render and history inspection confirms the runtime's checkpoint, synthesis-loss and desktop-retention qualifications. [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission), [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis), [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis).
2. **Containment, not duplicate replacement.** Object records declare retained parts of supplied routes; trace-read/context-reload and follow-up authority are separate parts. AgentContext spans diagnosis, child and checkpoint routes; raw trace storage spans initial diagnosis and desktop export; neither is a new route with identical identity. Telemetry admission precedes desktop scheduling, and cleanup crosses stores. No candidate replacement/possible duplicate was found after comparison with supplied records. All relations and nearest counterparts are stated in declarations.
3. **Continuation loses backing originals.** Local `get_context_item` can retrieve full items, but checkpoints contain rendered messages, not the original index. A resumed caller cannot assume original IDs still address those full items. External host resume/backing-store policy remains unknown; therefore complete post-compaction recoverability is prevented. SRC-1, `engine/agents/agent_context.py`, `engine/agents/openai_agent_runner.py`; [MEM-OBJ-agent-context](#mem-obj-agent-context), [MEM-RTE-context-reload](#mem-rte-context-reload).
4. **Status and evidence freshness are not common validity gates.** History ignores assistant status; reports restrict completed/incomplete findings; retry leaves old content; follow-up reuses export by existence or rebuilds when missing. The next answer can therefore combine retained older diagnoses with changed evidence, and cancellation does not itself establish withdrawal from all readers. SRC-1, `app/src/server/halo/storage.ts`, `app/src/server/halo/report.ts`, `app/src/server/halo/runQueue.ts`; [MEM-OBJ-halo-run-turns](#mem-obj-halo-run-turns), [MEM-OBJ-report](#mem-obj-report), [MEM-RTE-retention-cleanup](#mem-rte-retention-cleanup).
5. **Adapter provenance and evaluation integration remain bounded unknowns.** Common store/export behavior is inspected; individual adapter mapping and task-specific evaluator correctness are not. The skill prescribes comparison, while AppWorld analyze supplies only traces/question. This prevents verified complete trace fidelity and automatic score-to-instruction revision claims, not the positive retention paths. [MEM-RTE-telemetry-admission](#mem-rte-telemetry-admission), [MEM-OBJ-evaluation-report](#mem-obj-evaluation-report).
6. **Semantic preservation and improvement remain unestablished.** Compaction requests key facts and accepts successful units, but drops accompanying assistant content from summarizer input when tool calls exist. It does not guarantee retained reasoning. Diagnosis/report retention supplies later knowledge/evidence channels; learned future capacity or exercised self-improvement needs additional evidence. This does not alter the separately assessed prescribed theory pathway in [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff). SRC-1, `engine/agents/compactor.py`, `engine/agents/prompt_templates.py`; [MEM-OBJ-agent-context](#mem-obj-agent-context), [MEM-BAP-followup-history](#mem-bap-followup-history).

## Limitations and checks

HEAD recheck returned exactly the reviewed commit and Git status was clean. Every new source path is in SRC-1; source identity and repeated run/boundary fields match the supplied inputs. The report follows the supplied member type and shared record contract; no other analysis, source revision or live service was used. Missing guessed `index.py`/`trace_index_row.py` paths were resolved to the actual builder/schema files, not treated as absences.

Counterchecks challenged continuous compaction, full checkpoint recovery, complete span visibility, all-status report inclusion, cancellation-as-withdrawal and complete source refresh. Their limits are retained above rather than converted into system-wide negative findings. No target code/tests/examples were executed. No source-native run artifact or causal comparison was inspected. Provider internal state, deployed operation, actual later reliance and coding-tool execution remain uninspected. Static prompts/skill, installation settings and optional repository reads are covered as guidance/configuration/evidence surfaces, not asserted to be use-acquired semantic memory.

Validation: invocation-specific `commonplace-run validate-output` passed after correcting the report-filter quotation to match source punctuation. This establishes form and quotation occurrence, not analytical correctness or acceptance.
