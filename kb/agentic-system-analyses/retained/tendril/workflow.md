---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Tendril's request-to-delivery workflow for creating and executing a missing capability, including rejection and model-directed repair."
run-id: AAS-2026-10-15-tendril-f560fb299a37-01
reviewed-boundary: "e671a4143d28de68289efd81580002041bb4cb6a"
---

# Tendril workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a desktop request for which the model finds no suitable retained capability: submit the request, list available tools, author and register a new TypeScript implementation, execute it, inspect the result and return to the user. This is selected because the shipped prompt explicitly connects these steps; it is not a constructed sequence of unrelated features. The matching-capability branch skips creation. Both are policies for a single foreground agent, not a manager delegating to specialist agents. [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence) retains the sequence passage; [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) and [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution) establish its write and execution handoffs (SRC-1, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/loop/tools.ts`).

The evidence is implementation and doctrine/design at the revision fixed in [boundary](boundary.md), not an observed task transcript. This member inspected the complete `tendril-agent/src/index.ts`, `tendril-agent/src/transport/{protocol,stream}.ts`, `tendril-agent/src/loop/{prompt,tools,registry,sandbox}.ts`, `tendril-ui/src/hooks/useAgent.ts`, `tendril-ui/src/context/AgentContext.tsx` and `tendril-ui/src-tauri/src/events.rs`, all within SRC-1. These reads independently check selection, rejection, return transformation and desktop completion. No target, test, example or provider was executed. SDK iteration internals remain outside the frozen source, and no actual generated capability or user outcome is supplied.

### Request and decision ownership

The user supplies a task through desktop chat. The React hook appends the user message, sets processing state and invokes `send_prompt`. The Rust-to-Node transport is the supplied baseline's [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream). The Node protocol acknowledges the request before awaiting the work; a concurrent prompt is rejected rather than becoming a second workflow. The entry point extracts the last message's string or first usable text block and calls the existing agent's stream. Thus acknowledgement means transport acceptance, not delivered work, and the desktop message history is not replayed by this adapter (SRC-1, `tendril-ui/src/hooks/useAgent.ts`, `tendril-agent/src/transport/protocol.ts`, `tendril-agent/src/index.ts`).

The foreground model decides whether available tools match the task, supplies new code when needed and decides its next tool call. The SDK drives model/tool iteration. Tendril's Node callbacks own disk I/O and process launching. The user starts the task but does not approve each code registration or execution. Natural-language instruction supplies the desired order; the callbacks do not implement a list/create/execute state machine. These responsibilities and limits are established by the supplied runtime routes and claim, not by an assumption that the prompt is obeyed (SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/prompt.ts`; [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence)).

### Consequential handoffs

1. **Registry to model.** `listCapabilities` reloads the index and returns summaries containing name, capability, triggers and suppression. It does not return implementation bodies. The model interprets this metadata against the task; there is no fixed semantic matcher. Empty results explicitly request creation. A corrupt index can appear empty, so this branch does not prove no source files exist (SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`; [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)).
2. **Model to registry.** Registration supplies definition fields and a TypeScript string. Node validates the name and writes metadata plus source, then returns an instruction to execute the new name. Same-name registration replaces the current definition/source. This admits executable material before its first trial; neither compilation, a task oracle nor human approval gates that write. The supplied admission record retains the sequential-write passage and its inconsistency risk (SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`; [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)).
3. **Model through Node to Deno.** Execution supplies a name and optional JSON argument string, not inline code. Node reloads the source, parses arguments, prepends symbolic bindings for `args` and `__workspace`, writes a temporary script and spawns Deno with workspace read/write and configured network permission. The capability can produce persistent file or network effects before returning. Name-based loading is not an index-membership check, and the workspace grant includes the registry itself (SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/sandbox.ts`; [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution), [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation)).
4. **Deno result to ongoing agent work.** A zero exit returns trimmed stdout, or `(no output)`; nonzero exit, timeout, excess output, cancellation and spawn failure reject. The shipped tool loop delegates subsequent reasoning to the SDK/model. The model is instructed to log only needed data, so stdout is the authored program's selected result, not an independently complete account of its effects. External SDK treatment of tool exceptions is not inspected (SRC-1, `tendril-agent/src/loop/sandbox.ts`, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/loop/tools.ts`; [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution)).

### Rejection, verification and recovery

The inspected failure branch is execution of retained code that exits nonzero. Deno's close handler rejects with stderr or the exit code, rather than returning stdout as successful data:

> if (exitCode === 0) resolve(stdout.trim() || '(no output)');
>         else reject(new Error(stderr.trim() || `Exit code ${exitCode}`));
> --- `tendril-agent/src/loop/sandbox.ts`

This is an execution-result check, not task verification. Zero exit can accompany wrong output. Invalid names, failed source loading or malformed argument JSON can reject even before Deno starts. No reference answer or independent critic is wired into these callbacks. Their inspected branches support mechanical acceptance/rejection, not answer correctness (SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/sandbox.ts`; [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution)).

The instructed recovery owner is the same model: fix code and retry, using same-name registration to replace the retained implementation when appropriate. This is requested behavior, not a deterministic repair controller or a demonstrated repair. There is no retained previous version automatically restored by registration. A process kill stops current execution but does not reverse earlier writes or network calls. The repair policy and replacement mechanism are already evidenced in [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission); the execution record bounds timeout and cancellation (SRC-1, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/sandbox.ts`).

If an exception escapes `agent.stream`, the entry point emits a classified error and then calls the same turn-end routine used after normal streaming. Thus workflow termination need not mean recovery succeeded (SRC-1, `tendril-agent/src/index.ts`).

### Delivery and its limits

Delivery is a desktop event path, not a separate artifact-approval stage. Streamed model text becomes `agent_message_chunk`; tool input/output becomes correlated tool-call events. Rust maps these notifications to typed Tauri events; React appends text and tool results to the current assistant message. At `prompt-complete`, React stops processing and resets its assistant-message marker. Retained capability source/index are a separate durable result of registration, available for later listing/loading; the displayed chat message itself stays in reducer memory in this inspected path (SRC-1, `tendril-agent/src/transport/stream.ts`, `tendril-ui/src-tauri/src/events.rs`, `tendril-ui/src/context/AgentContext.tsx`; [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream)).

The completion event does not certify success: the entry point emits `end_turn` after its stream-error handler too. Likewise the observer marks tool results `completed` without evaluating task success; the supplied runtime account retains that passage. The frontend's operative consequence of prompt completion is only:

> case 'PROMPT_COMPLETE':
>       return { ...state, isProcessing: false };
> --- `tendril-ui/src/context/AgentContext.tsx`

The source therefore establishes a connected request/create/execute/return workflow with mechanical failure signals and model-directed recovery instructions. It does not establish that any particular request followed the sequence, that a repair occurred or that a delivered answer was correct (SRC-1, `tendril-agent/src/index.ts`, `tendril-agent/src/transport/stream.ts`, `tendril-ui/src/context/AgentContext.tsx`; [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream)).

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

#### On [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream)

Workflow role: request ingress and user-facing return enclose the selected capability-building workflow. The early acknowledgement, streamed content and end-of-turn signal are different milestones. The last ends desktop processing even after an error; it is not product acceptance. This workflow adds no separate delivery oracle.

#### On [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)

Workflow role: the no-match branch crosses from model-authored proposal to retained executable content before execution feedback exists. A later repair repeats this same admission mechanism. No worker-to-reviewer handoff intervenes; the model is both initial author and instructed repairer.

#### On [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution)

Workflow role: the trial of the retained implementation supplies process-result feedback, not independent verification of the user's task. Rejection leaves recovery to subsequent model/SDK behavior; replacement and retry are available but not forced. Successful termination and successful task delivery remain separate conclusions.
