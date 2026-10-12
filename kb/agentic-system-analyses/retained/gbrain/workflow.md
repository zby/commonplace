---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "GBrain workflow report: an OAuth client's delegated gateway tool-loop job, from scoped submission through replay and result polling."
run-id: AAS-2026-10-11-gbrain-9de8e3c225d3-01
reviewed-boundary: da434385572e0dc0d825649179aabed4107d6e60
---

# GBrain workflow report

## Workflow account

GBrain ships a connected delegation workflow: an authenticated client submits an agent task, a worker runs a bounded model/tool loop, and the client polls the retained job result. This account selects the gateway-enabled branch because it joins task delegation, consequential tool execution, durable recovery and an explicit delivery surface. It does not construct a particular successful task or assume that the model makes several tool calls. The source establishes the machinery for a multi-step task, not its successful execution. The enclosing client's conversation and any user-facing answer after polling remain outside the [boundary](boundary.md). All findings use SRC-1 at the frozen commit; evidence is implementation, with no observed run or causal experiment.

### 1. The client delegates a task, not unrestricted host authority

The `submit_agent` operation accepts a nonempty prompt, optional supported model, tool/prefix subsets, turn bound and queue. It requires an OAuth client identity and agent scope; the local CLI is directed to a different entry point. The operation resolves a current delegation grant, builds a submission snapshot and queues a `subagent` job with the prompt, resolved model, source, owner-client identity and snapshot. This binds the future worker's task to its submitting principal rather than leaving authority to the model. Invalid parameters, unusable model capabilities, invalid subsets and concurrent-job quota can reject submission. The response contains a job ID and queue-state probe, not a completed answer. Identical waiting submissions can be coalesced, with a response flag. See [WF-RTE-agent-submission](#wf-rte-agent-submission). SRC-1 `src/core/ops/jobs.ts`.

> source_id: snapshot.sourceId, __owner_client_id: clientId,
> __delegation_grant: snapshot,
> --- `src/core/ops/jobs.ts`

The gateway branch is conditional: the handler reads `agent.use_gateway_loop`, also permits its selected OpenRouter family, and otherwise can use the legacy Anthropic loop. This account follows a configuration with the gateway branch selected. The nearby submission comment's claim that gateway is automatically enabled is not an unconditional executable guarantee. SRC-1 `src/core/minions/handlers/subagent.ts`.

### 2. The handler prepares the model's actual handoff

The handler refreshes delegated data, selects tools from the registry, guards them, and renders the system prompt from that selected list. The model receives the task as a user message, system guidance and provider-neutral tool definitions, plus a reconstructed transcript on resume. It does not receive every registered operation merely because the operation exists. Default guidance tells it to call tools rather than narrate hypothetical writes; this is an instruction, not a compliance guarantee. SRC-1 `src/core/minions/handlers/subagent.ts`, `src/core/minions/system-prompt.ts`; [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model).

> const selectedTools = selectAllowedTools(registry, data.allowed_tools);
> const guardTools = (tools: ToolDef[], deferEmbeds = false) => guardDelegatedTools(engine, config, submitted, ctx.id, tools, deps.toolRegistry !== undefined, deferEmbeds);
> const toolDefs = guardTools(selectedTools);
> --- `src/core/minions/handlers/subagent.ts`

The accepted snapshot is a ceiling, not permanent permission. `effectiveDelegation` intersects submitted and live tools, prefixes, readable active sources and scopes, and narrows concurrency/budget. Each guarded execution checks the fresh effective grant before rebuilding the executable brain-tool wrapper. Withdrawal can therefore refuse a stored or newly proposed call. This is software authorization; the source does not establish that a human authored or approved each task or tool input. SRC-1 `src/core/minions/delegated-policy.ts`, `src/core/minions/delegated-tools.ts`.

> if (!effective.tools.includes(opName)) throw new DelegationDeniedError(['delegated_tool_withdrawn']);
> --- `src/core/minions/delegated-tools.ts`

### 3. The model proposes; durable callbacks and handlers execute

The model chooses the next tool or final text. The gateway and subagent handler own sequencing: persist assistant output, persist a pending execution with stable identity, invoke a selected executor, settle its outcome, persist the tool-result turn, then supply results to the next model turn. The baseline already declares this route and its quotations: [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop). A rate lease bounds each model round-trip; ordinary gateway callbacks are optional, but this caller supplies them. SRC-1 `src/core/ai/gateway.ts`, `src/core/minions/handlers/subagent.ts`.

For journaled page mutations, the tool wrapper adds another acceptance boundary. It retains a request identity from execution coordinates and waits/replays the same request while the receipt is pending. An admitted write is not counted as a completed tool write merely because it was queued. Deadline/abort can end the wait; pending-write failure escapes without marking the execution failed, preserving its pending state. The publication machinery itself is described in [RT-RTE-capture-write](runtime.md#rt-rte-capture-write), not assumed to be the gateway's responsibility. SRC-1 `src/core/minions/tool-write-identity.ts`, `src/core/minions/handlers/subagent.ts`.

> if (pendingToolWrite) throw pendingToolWrite;
> --- `src/core/minions/handlers/subagent.ts`

Verification here means authorization, receipt settlement and replay safety. It is not an independent answer-quality review. The structural write-accounting finalizer counts settled `brain_put_page` outcomes. Jobs that explicitly require writes can fail on all failed writes or illegitimate zero writes; the inspected `submit_agent` job-data construction does not set `require_writes`. For these open tasks, accounting is supplemental and its read failure is fail-open. Neither counts nor clean model termination certify semantic correctness. SRC-1 `src/core/minions/handlers/subagent-persistence.ts`, `src/core/ops/jobs.ts`.

> // Open-ended agent jobs keep fail-open: accounting is supplemental
> // there, and a transient read error must not crash a finished job.
> --- `src/core/minions/handlers/subagent-persistence.ts`

### 4. Recovery refuses uncertain repetition and distinguishes infrastructure pressure

On resume, the handler reloads messages and tool outcomes, reconciles dangling tool-result turns, and can return already-persisted terminal text without another model call. The pending-row callback rereads the canonical execution UUID rather than treating a newly generated UUID or repeating provider ID as replay identity. Completed/failed outcomes are reused. A pending non-idempotent execution is refused rather than silently repeated; pending idempotent work may execute again. These are bounded replay rules, not universal exactly-once execution. SRC-1 `src/core/minions/handlers/subagent.ts`, `src/core/ai/gateway.ts`; [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop).

The worker, not the model, owns retry disposition. Lease pressure uses a separate release/requeue path without burning an attempt. Other caught errors become delayed retries with backoff, or dead jobs for unrecoverable errors/exhausted attempts. Infrastructure lock-loss paths leave recovery to stall handling. This inspection establishes these branches but does not audit every fleet/reaper path. No run demonstrates recovery succeeding. SRC-1 `src/core/minions/worker.ts`.

> const isUnrecoverable = err instanceof UnrecoverableError;
> const attemptsExhausted = job.attempts_made + 1 >= job.max_attempts;
>
> let newStatus: 'delayed' | 'failed' | 'dead';
> if (isUnrecoverable || attemptsExhausted) {
>   newStatus = 'dead';
> } else {
>   newStatus = 'delayed';
> }
> --- `src/core/minions/worker.ts`

### 5. Delivery is a fenced retained result, not proof of task success

The handler returns final text, turns, usage, accounting where available and a stop reason. Output-cap termination maps to `max_tokens`, not clean `end_turn`; refusal, turn limit and abort remain distinguishable. If the handler returns normally, the worker calls token-fenced job completion. Thus a job's `completed` status means the handler result was recorded under the current claim; its nested stop reason can still describe a limited or refused model run. SRC-1 `src/core/minions/handlers/subagent.ts`, `src/core/minions/worker.ts`, `src/core/minions/queue.ts`.

The submitting client calls `get_agent_job` with the job ID. The database query filters by subagent name and owner client, with uniform not-found for foreign/missing IDs. The response exposes status, timestamps, capped error text, result and waiting queue position. This is the shipped delivery boundary. The result still traverses MCP response handling, including the polling operation's retrieval-redaction classification; this account establishes the handler's returned object, not byte-for-byte transport disclosure or a final host answer. See [WF-RTE-agent-delivery](#wf-rte-agent-delivery) and [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch). SRC-1 `src/core/ops/jobs.ts`.

### Added inspection and limits

Added bounded inspection covers SRC-1 `src/core/ops/jobs.ts` (submission and polling), `src/core/minions/worker.ts` (execution settlement and error disposition), `src/core/minions/queue.ts` (completion transaction), `src/core/minions/handlers/subagent.ts` (registry, gateway adaptation and callbacks), `src/core/ai/gateway.ts` (replay/execution), `src/core/minions/delegated-policy.ts` (effective grant), and `src/core/minions/handlers/subagent-persistence.ts` (write accounting). Complete files read: `src/core/minions/delegated-tools.ts`, `src/core/minions/tool-write-identity.ts`, `src/core/minions/system-prompt.ts`. These are implementation evidence, not a new source register or whole-system coverage claim. Full queue admission/claim, spend-policy internals, fleet scheduling, legacy and oneshot branches, all tool implementations and final transport redaction remain incompletely inspected. They prevent universal security, complete recovery and exact final-disclosure conclusions, not the bounded connected workflow above.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-agent-submission
Label: Delegated agent submission

Distinct identity: this route queues a task and supplies its grant snapshot; [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) is the surrounding dispatch control, and [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop) begins execution from job context. Neither declares the submission operation itself.

Endpoints/progression: OAuth client task → parameter/model/grant checks → submission authority preparation → queue add → job ID/queue-state response. Owner: caller proposes the natural-language task and optional constraints; operation/grant/queue software decides eligibility and can veto. Human involvement in task authorship is unresolved. Symbolic snapshot and owner identity persist in job data. Operating mode: open delegated request; no reference-answer oracle or successor comparison. Trigger is `submit_agent`; it admits queued work, not a certified knowledge revision. Any downstream writes face their tool's admission. Guidance is the granted source, tools, prefixes, budget and turn bound; rejected submission queues nothing. No rollback of downstream effects is established by canceling a task. SRC-1 `src/core/ops/jobs.ts`.

- Immediate return: job ID, subagent name, client identity, queue-state probe and optional coalesced flag; dry-run returns resolved constraints without queuing.
- Later read-back: stored job data supplies prompt and delegation snapshot to a later worker invocation; owner identity fences polling.
- Delegated visibility: selected tool/prefix/source restrictions are handed to the worker; installed grants and private task content were not supplied.
- Selection predicate: authenticated client, agent scope, nonempty task, valid turn/model/queue parameters, permitted subsets, current grant and queue quota.
- Invalidation or expiry: live delegation can narrow or invalidate accepted authority before execution; no task-retention expiry established.
- Activation or effect: queues a subagent task; a response ID alone does not show a live worker or completed task.
- Evidence limits: inspected operation implementation only; full queue admission, deployment liveness and actual client authorization unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> job = await queue.add('subagent', jobData,
>   { queue: (p.queue as string) || 'default' },
>   { allowProtectedSubmit: true, delegatedClientId: clientId, submissionAuthority: authority });
> --- `src/core/ops/jobs.ts`

#### WF-RTE-agent-delivery
Label: Agent result settlement and polling

Distinct identity: [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop) returns a handler result; this route settles that result in the job queue and supplies it to the owning client. [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) wraps polling but does not own job completion.

Endpoints/progression: normal handler return → worker completeJob → transactional active/lock-token match → stored result → owner-filtered get_agent_job response. Owner: worker proposes settlement, queue SQL can reject stale ownership, and polling handler restricts disclosure. Context is job ID, active claim token and owner-client identity. Stored result mixes natural-language final text with symbolic status/usage/accounting fields in SQL JSONB; polling does not judge the truth of text. Operating mode: asynchronous task delivery, no answer oracle or semantic acceptance gate established in these functions. Failed handler execution takes worker retry/dead disposition instead of this normal completion route. SRC-1 `src/core/minions/worker.ts`, `src/core/minions/queue.ts`, `src/core/ops/jobs.ts`.

- Immediate return: completion returns the updated job or null for stale claim; polling returns status, timestamps, result, capped error and waiting position where applicable.
- Later read-back: a later get_agent_job invocation reads the persisted result and status; whether a host incorporates them into its answer is unobserved.
- Delegated visibility: SQL restricts reads to authenticated owner-client subagent jobs; foreign/missing IDs share not_found. Subsequent MCP redaction was not fully traced.
- Selection predicate: completion requires active status and matching lock token; polling requires integer job ID and matching owner client/subagent name.
- Invalidation or expiry: reclaimed claims cannot settle via an old token; job pruning/retention expiry uninspected.
- Activation or effect: commits the handler result as completed and makes it available to polling; neither completion nor delivery establishes semantic success.
- Evidence limits: bounded completion/polling implementation; no observed job, final transport payload, deployed host consumption or semantic-quality evaluation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> `UPDATE minion_jobs SET status = 'completed', result = $1::jsonb,
>   finished_at = now(), lock_token = NULL, lock_until = NULL, updated_at = now()
>  WHERE id = $2 AND status = 'active' AND lock_token = $3
>  RETURNING *`,
> --- `src/core/minions/queue.ts`

> WHERE j.id = $1
>   AND j.name = 'subagent'
>   AND j.data->>'__owner_client_id' = $2`,
> --- `src/core/ops/jobs.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-subagent-loop](runtime.md#rt-rte-subagent-loop)

Workflow position: execution sits between [WF-RTE-agent-submission](#wf-rte-agent-submission) and [WF-RTE-agent-delivery](#wf-rte-agent-delivery). Handoff content is the task, rendered selected-tool guidance, definitions and recovered transcript. Tool outcomes feed the next model decision; live-grant checks and durable-receipt waiting can reject or defer effects without asking the model to certify them. SRC-1 `src/core/minions/handlers/subagent.ts`, `src/core/minions/delegated-tools.ts`, `src/core/minions/tool-write-identity.ts`.

Recovery ownership: the handler reconstructs transcript/tool state; the gateway reuses settled outcomes or refuses uncertain non-idempotent repetition; the worker decides retry/dead/release disposition. Receipt recovery remains owned by persistence, not by model prose. Supplemental write accounting is not a universal task-success gate. The inspected submission does not enable write-required mode; quality approval by an independent reviewer and successful exercised recovery are not established. SRC-1 `src/core/ai/gateway.ts`, `src/core/minions/worker.ts`, `src/core/minions/handlers/subagent-persistence.ts`, `src/core/ops/jobs.ts`.
