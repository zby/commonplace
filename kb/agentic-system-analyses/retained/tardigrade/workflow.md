---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Tardigrade workflow account tracing the shipped Bun message driver through model/tool handoffs, rejection, recovery and terminal reply."
run-id: AAS-2026-10-15-tardigrade-455e1aaccd4d-01
reviewed-boundary: "1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8"
---

# Tardigrade workflow report

## Workflow account

### Selection and evidence

The representative workflow is the shipped Bun example's `meeseeks` message invocation, already identified by [RT-RTE-bun-message](runtime.md#rt-rte-bun-message). It was selected because a single shipped composition connects request admission, model inference, executable tools, event-derived continuation and caller-visible delivery. The trace follows this composition, not a hypothetical combination of the current actor and legacy server. Its default request is only `Hello`: tool use is a supported branch, not an established step of an actual run.

All source evidence is SRC-1 at the revision in [boundary](boundary.md). This member inspected `packages/examples/bun.ts`, `packages/examples/agents/meeseeks.ts`, `packages/examples/services.ts`, `packages/agent/src/actor/methods.ts`, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/atoms/durable/inference.ts`, `packages/agent/src/services/tools.ts` and `packages/agent/src/atoms/tools.ts`. These are implementation evidence, not observed execution. No target code, tests, providers or services were run. Recovery and model-adapter details below rely on the supplied runtime records; this member does not independently audit their implementations.

### Request and ownership transfer

The driver creates a Bun host with the example actor, actor context, storage path and service layer. It allocates the `example` instance's `main` root thread and calls its message method with invocation ID `example-message`. The driver supplies the problem through `EXPERIMENTAL_MESSAGE`; it does not prescribe a plan or expected answer. Host allocation and durable request delivery are covered by [RT-RTE-bun-message](runtime.md#rt-rte-bun-message), with source SRC-1, `packages/examples/bun.ts`.

The message method admits exactly one of text or content, derives text from text-bearing content when needed, and emits `TurnRequested` with the invocation ID as turn ID and the invocation reference attached. This binds eventual answer projection and cancellation to the request. Evidence: SRC-1, `packages/agent/src/actor/methods.ts`.

> source: "user", turnId: context.id, invocationRef: context.ref,
> --- `packages/agent/src/actor/methods.ts`

The actor composes a short system instruction, `libraryTools()`, `compact(messages)` and `infer`. Its service layer installs model configuration/lock loading, fetch and workspace tools, and an in-memory workspace. Thus a configured tool catalog is available, but the example does not compose the default actor's permission or budget wrappers. The controls of [RT-RTE-governed-tools](runtime.md#rt-rte-governed-tools) cannot be assumed for this workflow. No child-agent package is installed by this service layer; delegation here means model and tool handoffs, not a mandatory parent/child-agent plan. Evidence: SRC-1, `packages/examples/agents/meeseeks.ts`, `packages/examples/services.ts`; the runtime record retains the actor composition passage.

### Model and tool handoffs

Code owns progression. `infer` waits while a model call runs, outstanding tools remain, or context is not ready. When ready, it proposes `Generate` with selected model, system instruction, tool specifications and selected messages. The provider proposes response text and tool calls; it does not directly execute the tools. Context can be summarized before this handoff, so the model need not receive the whole retained journal. [RT-BAP-model-instructions](runtime.md#rt-bap-model-instructions) and [RT-RTE-bun-message](runtime.md#rt-rte-bun-message) retain the model-input and context-selection evidence. Evidence: SRC-1, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/atoms/compact.ts`, `packages/agent/src/services/model.ts`.

The adapter result is converted into events. Duplicate provider tool IDs reject the model result; accepted calls acquire internal IDs derived from the effect reference and index. A reply containing tools is not yet a final answer. The durable reducer records outstanding call IDs and clears the answer until a subsequent tool-free model response arrives. Evidence: SRC-1, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/atoms/durable/inference.ts`.

> ...turn, answer: event.toolCalls.length === 0 ? event.text : null, rejection: null,
> --- `packages/agent/src/atoms/durable/inference.ts`

Tool proposals hand the selected call name and input to the library registry. The tools atom checks catalog membership; the service dispatches a recognized call to its implementation. Immediate tool results or errors become `ToolReturned`; deferred results use a handle and promise path. The reducer removes completed call IDs from the outstanding set. Once no tools remain outstanding and the turn still needs a reply, `infer` can propose another model call. Tool results become later conversation input as described by [RT-RTE-bun-message](runtime.md#rt-rte-bun-message). Evidence: SRC-1, `packages/agent/src/atoms/tools.ts`, `packages/agent/src/services/tools.ts`, `packages/agent/src/atoms/durable/inference.ts`.

### Verification, rejection and recovery

Verification is computational and protocol-scoped. This actor supplies no output contract to `infer`; the generic structured-output correction machinery is therefore not an active acceptance condition in this composition. Neither the driver nor the inspected actor supplies a semantic answer oracle or a human review stage. Model output is not proven correct by turn completion. Evidence: SRC-1, `packages/examples/agents/meeseeks.ts`, `packages/agent/src/atoms/infer.ts`; see [RT-RTE-bun-message](runtime.md#rt-rte-bun-message).

Two supported rejection paths have different recovery owners:

- An unknown tool name produces a non-counted error plan, not a host method execution. The tool service fails that plan and the atom converts the rejection into `ToolReturned`. The model can then receive error content and propose different work; successful correction is not established. Evidence: SRC-1, `packages/agent/src/atoms/tools.ts`, `packages/agent/src/services/tools.ts`.
- A rejected generation or duplicate provider call IDs produces `ModelFailed`. The reducer records turn failure; `infer` settles the turn as failed, and the method projects that error rather than a successful answer. Automatic retry of that failed turn is not shown in this path. Evidence: SRC-1, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/atoms/durable/inference.ts`, `packages/agent/src/actor/methods.ts`.

The unknown-tool veto occurs before library execution:

> if (input.error !== undefined) return Effect.fail(input.error)
> --- `packages/agent/src/services/tools.ts`

Cancellation is another terminal route. The method emits `AbortRequested`; inference cancels pending effects, settles outstanding tool entries and only then settles cancellation. The reducer rejects cancellation settlement while accepted effects remain pending. This is a lifecycle check, not rollback of already performed network or workspace effects. Evidence: SRC-1, `packages/agent/src/actor/methods.ts`, `packages/agent/src/atoms/infer.ts`, `packages/agent/src/atoms/durable/inference.ts`.

> if (event.outcome === "cancelled" && (turn.cancellation === null || turn.effects.some(work => work.pending))) throw new RuntimeError("Turn cancellation must drain accepted work before settlement")
> --- `packages/agent/src/atoms/durable/inference.ts`

Restart recovery belongs to the host/core, not the model. [RT-CLM-request-before-execution](runtime.md#rt-clm-request-before-execution) and [RT-OBJ-journal](runtime.md#rt-obj-journal) establish committed requests, checkpoint/suffix replay and pending input recovery. They do not establish exactly-once external effects: recovery can recreate a producer and call an external service again. No supplied trace demonstrates a restart, cancellation or successful recovery for this example. Evidence: SRC-1, `packages/core/src/runtime/execution.ts`, `packages/platform/src/shared/sql-journal.ts`.

### Delivery boundary

A tool-free model result supplies an answer. `infer` proposes completed settlement only after the turn no longer needs a reply; the reducer rejects completion if the answer is missing, the answer reference disagrees, or model/tool work remains active. `agentReply` then returns `{ text }` for completed settlement, or a failed/cancelled method result. This separates an intermediate model return from a delivered invocation result. Evidence: SRC-1, `packages/agent/src/atoms/durable/inference.ts`, `packages/agent/src/actor/methods.ts`.

> return { status: "completed", output: { text: turn.answer } }
> --- `packages/agent/src/actor/methods.ts`

The driver awaits `thread.methods.message`, logs the response and waits for the thread. Its outer failure handler prints the cause and sets exit code 1. Delivery here means a method result reaches that caller, not successful task performance or durable preservation of every tool's own state. In particular, the installed workspace is in-memory, while journal recovery is a separate persistence mechanism. Evidence: SRC-1, `packages/examples/bun.ts`, `packages/examples/services.ts`; [RT-RTE-bun-message](runtime.md#rt-rte-bun-message).

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

#### On [RT-RTE-bun-message](runtime.md#rt-rte-bun-message)

Workflow selection: the shipped composition supplies a request-to-caller path without mixing API generations. The tool-use branch is conditional; the default greeting does not require it.

Workflow verification: computational admission and lifecycle checks can reject unknown tools, duplicate provider IDs and invalid settlement. This composition supplies no structured-output contract or semantic answer oracle. A tool error can return to model context for another proposal; generation failure instead settles the turn as failed.

Workflow delivery: completed turn projection, awaited method return and driver logging define the caller-visible endpoint. Thread waiting follows receipt of that response. Cancellation drains accepted work before terminal cancellation; recovery does not reverse completed external effects.

Workflow evidence limit: source-supported coordination only. No observed multi-step rollout, recovery episode or successful answer is supplied.
