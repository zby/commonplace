---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Cludebot workflow account: owner-assigned dashboard research task, memory tools, completion and retry at the frozen revision."
run-id: AAS-2026-10-15-cludebot-cb70d11d215b-01
reviewed-boundary: cecf234f10397b1e21dec2ff65ded864982f3564
---

# Cludebot workflow report

## Workflow account

### Selection and evidence

The selected workflow is an owner-assigned dashboard research task: request creation, execution launch, model-directed memory investigation, optional finding storage, completion and owner-visible result retrieval. It is representative because it connects the system's agent executor to both consumption and production of retained memory. It is not the authenticated chat turn and does not inherit that turn's prompt renderer or context fitter. The baseline is [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task), with model and configuration supplied by [RT-CMP-anthropic](runtime.md#rt-cmp-anthropic) and [RT-BAP-agent-configuration](runtime.md#rt-bap-agent-configuration).

This is a source-supported control-flow account, not a reconstructed successful run. SRC-1 supplies implementation and doctrine/design only. Tool order below is requested by the research preset but chosen by the model; neither an actual sequence of calls nor a successful research result was observed. Added inspection at the frozen revision covers `packages/brain/src/agents/executor.ts` in full, `packages/brain/src/agents/tools.ts` in full, research/content/dev/testing presets in `packages/brain/src/agents/types.ts`, and ownership plus task CRUD/execute/retry handlers in `apps/server/src/routes/dashboard.routes.ts`. A bounded symbol search of `apps/workers/src/jobs/index.ts` did not establish poller startup; the manually launched workflow does not depend on that unresolved startup path.

### 1. Request and assignment

The owner-only task creation handler accepts a title, description, assigned agent, priority, optional parent task ID and metadata. It requires a string title, limits title/description length and inserts a task plus creation activity. The request supplies the problem and assignment; the handler does not derive a decomposition. A parent-task identifier is stored, but these inspected handlers and executor do not turn it into a dependency scheduler or an automatic reviewer handoff (SRC-1, `apps/server/src/routes/dashboard.routes.ts`).

The owner gate is inherited from the runtime record, not a claim that every request was human-authored. Manual execution can reject a missing task, missing assignment, unknown agent type or locally running task. Launch returns an acknowledgement, not the task's answer:

> res.json({ status: 'executing', taskId: req.params.id });
> --- `apps/server/src/routes/dashboard.routes.ts:483-500`

For this workflow, the caller assigns an existing research agent. Its preset gives the model a method rather than a fixed tool sequence:

> - Use recall_memories to search existing knowledge first
> - Use get_market_data for market/price context
> - Use store_finding to persist important discoveries as semantic memories
> - Be thorough — pull from multiple memory queries if needed
> - Summarize findings clearly with evidence
> --- `packages/brain/src/agents/types.ts`

The default research configuration allows ten iterations and a 300-second timeout. Configuration may replace defaults, so these are preset values, not universal limits. Guidance to summarize with evidence is not an evidence-verification mechanism (SRC-1, `packages/brain/src/agents/types.ts`).

### 2. Handoff to the model and tools

The executor constructs one task-local conversation. The initial user message contains title, description, priority and JSON-encoded `metadata.input` when present. Other task metadata and foreground chat history are not automatically included. The model receives the resolved agent system prompt, model settings, advertised tool schemas and this conversation. Tool executors receive arguments and task/agent identifiers, not a delegated wallet credential. These context boundaries are those of [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task).

If the model requests recall, the tool returns memory IDs, types, summaries, importance and dates. Full retained content is not delivered by this wrapper. There is no hydration tool in this registry; an ID in the returned prose is not an automatically dereferenceable model pointer (SRC-1, `packages/brain/src/agents/tools.ts`):

> const formatted = summaries.map(m =>
>           `[#${m.id}] (${m.memory_type}) ${m.summary} | importance: ${m.importance?.toFixed(2)} | ${new Date(m.created_at).toISOString().slice(0, 10)}`
>         ).join('\n');
> --- `packages/brain/src/agents/tools.ts`

The model can request further queries, market data, progress logging, finding storage and completion. Code dispatches returned tool calls sequentially and appends assistant blocks plus tool-output text to the next model input. The inspected loop does not trim or summarize this transcript. This is one model/tool loop, not a hierarchy of model sub-agents. Configured schema filtering is not an execution-time per-agent allowlist, as the baseline establishes. Stored findings enter the separate admission route [WF-RTE-store-finding](#wf-rte-store-finding); successful storage is not required before completion.

### 3. Verification and recovery

There are ownership, request-shape, dispatch and tool-operation checks, but no independent answer oracle or research reviewer in this inspected path. The model proposes findings and decides when to finish. The tools can report failures; no per-finding human approval or factual veto is introduced by the research prompt. The operating mode is an open assigned task, not a scored experiment.

An unknown tool is rejected by the dispatcher. Tool exceptions and ordinary tool failure results become text for the next model iteration, rather than automatically failing the whole task. The executor sends `result.output` without an `is_error` flag; recovery depends on the model interpreting that text and choosing another action. There is no code-mandated retry count for a failed recall/store call (SRC-1, `packages/brain/src/agents/tools.ts`, `packages/brain/src/agents/executor.ts`):

> if (!tool) {
>     return { success: false, output: `Unknown tool: ${toolName}` };
>   }
> --- `packages/brain/src/agents/tools.ts`

> toolResults.push({
>                 type: 'tool_result',
>                 tool_use_id: block.id,
>                 content: result.output,
>               });
> --- `packages/brain/src/agents/executor.ts`

Provider-loop exceptions and the timer rejection instead enter `failTask`, which writes failed status, error/log/cost metadata and failure activity. The race does not cancel the losing model/tool work. Already stored findings or posted effects are not rolled back. As established by the runtime baseline, exceptions during client acquisition before the enclosing try block have weaker recovery: the outer launch catch logs a crash rather than necessarily marking the task failed (SRC-1, `packages/brain/src/agents/executor.ts`).

The owner can invoke the retry endpoint, which resets failed or completed tasks to pending and calls manual execution. This starts fresh task messages; old execution logs do not become corrective model context automatically. If retained findings changed memory, later recall can nevertheless expose them. Retry is therefore re-execution, not rollback or guaranteed continuation. Manual launch also retains the runtime's returned-row claim-check limitation (SRC-1, `apps/server/src/routes/dashboard.routes.ts`, `packages/brain/src/agents/executor.ts`).

### 4. Completion and delivery

`complete_task` returns result/summary data with a termination flag. The executor finishes processing the current response's blocks before testing that flag; it is not an immediate veto on subsequent tool blocks in the same response. An end-turn response without tools can also finish, using its text as a fallback. Exhausting the iteration loop reaches the same success section; no completion-tool requirement or output-quality check gates it (SRC-1, `packages/brain/src/agents/tools.ts`, `packages/brain/src/agents/executor.ts`).

> if (terminated) {
>             logEntry('Task completed via complete_task');
>             break;
>           }
> --- `packages/brain/src/agents/executor.ts`

The success section attempts to store completed status, result/summary, execution log, model and estimated cost; it writes completion activity and updates accumulated budget. Those database operations are not one transaction and their returned error fields are not uniformly checked. Consequently control-flow completion establishes neither a durable delivery receipt nor research correctness. A task with no usable result can fall back to `(no output)` (SRC-1, `packages/brain/src/agents/executor.ts`).

> const cResult = String(cd?.['result'] || lastText || '(no output)');
> --- `packages/brain/src/agents/executor.ts`

The owner-only GET task list selects task rows including metadata, making persisted output retrievable through the HTTP interface. That is the inspected delivery boundary; client rendering, owner receipt and acceptance were not traced. Finding-memory admission and task-result delivery are separate effects: one can succeed while the other fails. No observed run establishes either, and no evidence here establishes improved future capacity (SRC-1, `apps/server/src/routes/dashboard.routes.ts`, `packages/brain/src/agents/executor.ts`).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-store-finding
Label: Task finding storage

Part of: [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task)

This is the task executor's `store_finding` tool admission, not a duplicate of the whole task or the general [RT-RTE-memory-entry](runtime.md#rt-rte-memory-entry) surface. It passes model-authored natural-language content and summary plus symbolic type/tags/provenance into the underlying memory store. Tool-specific truncation and task provenance distinguish this material subroute. The executor model proposes; the wrapper and underlying store admit or reject; no per-item human approval or truth oracle is shown. This is open task work, triggered by a model call, with research-preset guidance to preserve important discoveries. Recovery is a returned failure message and a subsequent model choice, not transactional undo. SRC-1, `packages/brain/src/agents/tools.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: tool text reporting a memory ID, null-write failure or caught error; optional memory-ID data is not automatically task completion metadata.
- Later read-back: admitted findings become eligible for subsequent memory recall; actual selection, ownership scope and downstream dependence are not demonstrated.
- Delegated visibility: the memory implementation receives up to 2000 content characters, 200 summary characters, up to ten tags, selected/default type, importance 0.6 and task/agent provenance; the model receives the storage outcome text.
- Selection predicate: the model chooses whether and what to store; the wrapper truncates and defaults fields; underlying store checks remain those of the general memory-entry route.
- Invalidation or expiry: this wrapper has no undo; a failed task or retry does not retract prior admitted findings. Underlying memory management applies separately.
- Activation or effect: an insertion request is wired and can return an ID; no exercised storage or behavioral activation is established.
- Evidence limits: no run trace, truth check or explicit owner credential in this tool context; no claim that stored findings are correct, universally owner-isolated or improved by retries.

> source: `agent-task:${ctx.taskId}`,
>           sourceId: ctx.taskId,
>           importance: 0.6,
>           metadata: { agent_id: ctx.agentId, agent_name: ctx.agentName },
> --- `packages/brain/src/agents/tools.ts`

> return { success: false, output: 'Failed to store finding (returned null).' };
> --- `packages/brain/src/agents/tools.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-dashboard-task](runtime.md#rt-rte-dashboard-task)

Workflow role: selected enclosing research-task route. The request-to-launch acknowledgement, model/tool progression, completion alternatives and persisted HTTP retrieval are traced above. Assignment is supplied by the caller, not automatically delegated through parent-task links. Verification is operational checking plus model self-declared completion, not independent product acceptance. Tool failure leaves the next recovery choice with the model; timeout/loop failure writes failed status when caught; owner retry starts a fresh task frame without replaying old logs. The distinct retained-finding admission part is [WF-RTE-store-finding](#wf-rte-store-finding). Delivery is bounded to attempted persistence and owner-readable task metadata, not observed owner receipt or successful use.
