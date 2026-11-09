---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "WikiBrain workflow account: server-side source compilation from user request through tool decisions, rejected writes and browser delivery."
run-id: AAS-2026-11-08-wikibrain-f815b0976cda-01
reviewed-boundary: "32cc135877c8d7cd7be997ce57f25bb83128d891"
---

# WikiBrain workflow report

## Workflow account

### Selected workflow and evidence

This account follows one server-side ingest request over existing workspace sources. It selects [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) because this route connects user-selected material, model-directed multi-page compilation, durable edits and a shipped browser consumer. Importing a source precedes this request; it is not an atomic part of compilation. Chat, lint and external-client orchestration are not appended to make a longer synthetic workflow.

All source findings use SRC-1 at the reviewed commit. The account is implementation and doctrine/design evidence, not a completed run. Direct inspection covers `src/ingest.ts` request/executor/job paths, `src/ai/providers.ts` retry and provider loops, the general English rule page, and `web/src/components/IngestPanel.tsx`; bounded searches in `src/api.ts` and `web/src/pages/Workspace.tsx` confirm request dispatch and terminal reload wiring. These are within the boundary's included paths; the browser panel receives closer inspection here. No model transcript, database result or successful browser delivery was supplied. Thus the sequence below describes wired handoffs and requested model behavior, not demonstrated completion or knowledge quality.

### Request to agent

The user chooses paths and optional compilation guidance. The authenticated API dispatch and imported-source boundary are already established in [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job). In `startIngest`, code checks run eligibility, obtains provider configuration, rejects another built-in workspace job, then selects explicit paths or pending sources. It reads every target to establish workspace-local existence. Empty pending selection rejects the request before creating a job. The process-local running set is cleared on setup failure. These checks do not establish that explicit targets are raw sources or that other clients cannot edit concurrently. [SRC-1: `src/ingest.ts`]

The job receives workspace/user identity, target paths and provider/model identifiers. Guidance is trimmed and appended to the user prompt. `runJob` supplies the system prompt, target request, six note-tool schemas, a workspace-bound executor, an agent actor name and the configured tool-call cap. This is delegation from server code to a provider model, not delegation to independently isolated specialist agents. The model chooses the next reads and writes. [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models) bounds model identity and mutability; [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) establishes the handoff and its admission policy. [SRC-1: `src/ingest.ts`, `src/ai/providers.ts`]

### Requested compilation and actual decision loop

The system prompt asks the agent to call `get_instructions` first and follow the schema ingest sequence. It does not force that call before other tools. Stored rules reach the model by the instruction-return channel in [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions). The general English template requests full source reading, index inspection, related-page search, a source summary, entity/concept updates, index/log updates and explicit conflict marking. These are the intended work products, not executor-checked completion criteria. [SRC-1: `src/ingest.ts`, `templates/general/en/schema/instructions.md`]

> 5. Update `wiki/index.md` and append `## [date] ingest | title` to `wiki/log.md`.
> 6. When a source contradicts an existing page, mark "⚠ conflict" on both and list both sides; never pick silently.
> --- `templates/general/en/schema/instructions.md`

The provider adapter appends the model's tool requests, executes each selected tool sequentially, and returns results to the next model invocation. Full tool results remain in the current model conversation even though event logging clips each result to 400 characters. The model therefore has more recovery evidence than a reader of the job log. No separate critic or semantic acceptance stage appears between generated content and note writes on this route. [SRC-1: `src/ai/providers.ts`, `src/ingest.ts`]. See also [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs).

> o.onEvent({ type: 'result', tool: c.function?.name, output: out.slice(0, 400) });
> messages.push({ role: 'tool', tool_call_id: c.id, content: out });
> --- `src/ai/providers.ts`

Current-run turns and tool outputs accumulate. The inspected ingest handoff supplies no historical chat messages or child-agent frame; these provider loops do not summarize or trim this accumulated context. The budget limits tool calls, not successful pages or all model invocations. This is a single agent/tool loop, not a manager delegating compilation, criticism and integration to separate workers. [SRC-1: `src/ingest.ts`, `src/ai/providers.ts`]

### Rejection, verification and recovery

A proposed create/update is admitted by software checks, not by a person's approval of the generated text. Quota checks and shared note validation can reject writes. Optimistic updates reject a stale version, returning current content to the model; the template asks the model to re-edit it. Successful note operations persist individually, including their derived state, as established in [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job). Those checks verify admissible operations, not factual accuracy, complete source coverage or fulfillment of every requested index/log step. There is no expected-answer oracle for the compilation task. [SRC-1: `src/ingest.ts`, `templates/general/en/schema/instructions.md`]. Note-transaction evidence: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job).

> if (e instanceof ConflictError) return j({ error: 'CONFLICT', status: 409, message: e.localized(await lang), current: e.current });
> --- `src/ingest.ts`

This is a checked rejection branch: conflict becomes a tool response, and the provider loop gives it to the same model for another decision. Code does not itself merge the conflicting page or guarantee that the model retries. Literal schema-path writes likewise return a refusal, but the path-normalization countercase in [RT-RTE-schema-spelling](runtime.md#rt-rte-schema-spelling) prevents treating this as a universal rule-layer invariant. [RT-CLM-schema-guard](runtime.md#rt-clm-schema-guard) retains the distinction between requested policy and enforcement.

Transient provider requests are retried with delays; the tool-call cap throws when exceeded. Unrecovered exceptions cause the job to be marked failed, while restart handling marks stale queued/running jobs failed. Neither path undoes earlier page transactions. The running-set release permits a later request; snapshot rollback and re-editing are per-page recovery, not replay or rollback of the entire ingest. Human inspection may follow, but there is no mandatory post-generation human acceptance stage before these writes become readable. [SRC-1: `src/ai/providers.ts`, `src/ingest.ts`]. Recovery scope: [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job).

### What counts as delivered

Model termination and page delivery are separate events. The provider returns when its response no longer requests tool use; `runJobInner` marks the job done and saves the final text, clipped to 20,000 characters. It does not then check that all intended pages exist or every tool succeeded. A model can stop after receiving a tool refusal. Thus `done` means runner return, not verified compilation. Changes from successful writes are already durable before this terminal status. [SRC-1: `src/ai/providers.ts`, `src/ingest.ts`]. See [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs).

The shipped progress panel polls the job, renders text/tool/error events and triggers its completion callback for either terminal status. Workspace wiring clears its ingesting state, reloads the tree and reloads the selected note. This exposes partial results even after failure; closing the panel is not cancellation. The panel renders log-derived text, not a separately verified inventory of changed pages. Event clipping and the error-parsing limitation retained in the runtime mean that displayed write indicators cannot independently certify successful edits. [SRC-1: `web/src/components/IngestPanel.tsx`, `web/src/pages/Workspace.tsx`, `src/ingest.ts`]

> if ((job.status === 'done' || job.status === 'failed') && !doneRef.current) { doneRef.current = true; onDone(); return; }
> --- `web/src/components/IngestPanel.tsx`

The delivered result is therefore persistent individually admitted page changes plus terminal job status and a model-authored report available through the job/UI path. Later agents can read changed pages, but successful downstream use and improved answers remain unobserved. The source establishes coordination and localized recovery affordances, not end-to-end correctness or transactional delivery of the entire requested compilation.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)

Workflow selection: representative server-side source-compilation route, from user task to durable wiki edits and terminal UI refresh. Delegation is server-to-model and model-to-tool execution, not a hierarchy of isolated agents. Completion has no mandatory semantic verifier: operation-level rejections return to the proposing model; ordinary successful writes need no separate human approval. Browser delivery consumes job status/log events and refreshes pages on both success and failure. The requested multi-page sequence and the actual runner termination condition differ; this annotation makes no claim of observed completion.
