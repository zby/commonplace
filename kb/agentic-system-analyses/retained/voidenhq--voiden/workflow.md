---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Voiden workflow account: external-agent discovery, request execution, inspection, recovery and optional response recording through fixed MCP tools."
run-id: AAS-2026-10-14-voiden-98188b4a2f55-01
reviewed-boundary: d7a0d05c40acb6cc483000643c700f17aecba0ef
---

# Voiden workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is **discover a project request, execute it, inspect the outcome, repair if needed, and optionally record the result**. It was selected because shipped agent guidance explicitly connects these steps, and the fixed MCP handlers implement their tool handoffs. It is not assembled from unrelated publishing or plugin-management capabilities. The procedure is interactive authoring/iteration, not a CI gate or an autonomous workflow owned by Voiden. The external host supplies the model-driven decisions and any editing tools; Voiden supplies discovery, execution and response writing ([RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance), [RT-RTE-request-execution](runtime.md#rt-rte-request-execution); SRC-1, `packages/executors/src/skillContent.ts`, `packages/voiden-runner/src/mcpServing.ts`).

This account stays within the [subsystem boundary](boundary.md#boundary-and-evidence). Direct inspection for this member covered SRC-1, `packages/executors/src/skillContent.ts`, `packages/voiden-runner/src/mcpServing.ts`, the execution loop in `packages/voiden-runner/src/runner.ts`, and `packages/voiden-runner/src/resultBlock.ts`. These reads supply doctrine/design and implementation evidence. Runtime records supply the previously established orchestration, compatibility and registration evidence. No execution trace establishes that an agent followed the procedure or delivered a correct result.

### Request, discovery and environment handoff

The operator's registration supplies the project and server command; the external MCP host must launch and discover it. A configuration write alone does not establish that handoff succeeded ([RT-RTE-host-registration](runtime.md#rt-rte-host-registration); SRC-1, `packages/executors/src/mcpInstall.ts`). Once connected, the foreground agent owns the user's request and the next tool choice. There is no internal planner or worker-agent delegation in this selected workflow. Delegation here is an external agent calling symbolic handlers and those handlers invoking executable plugins.

Guidance first requests `list_void_files` and `list_requests`. The first returns relative document paths. The second receives a file path, rereads and parses the document, resolves linked content, and returns section labels, request UIDs and request previews without sending the requests. Those outputs give the agent the selectors needed for execution and later placement of a recorded response. They do not verify endpoint behavior (SRC-1, `packages/voiden-runner/src/mcpServing.ts`).

The environment branch is consequential because execution can use credentials and different endpoints. Guidance requests `list_environments`, then asks the user to choose when several profiles/environments exist unless already specified. The user-choice requirement is policy, not a handler-enforced approval. `select_environment` resolves variables into session state and returns only keys/counts. Subsequent execution receives that state, optionally overridden by the call's env file and explicit variables. This state is independent of the desktop UI's active selection ([RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars); SRC-1, `packages/executors/src/skillContent.ts`, `packages/voiden-runner/src/mcpServing.ts`).

### Execution and return

The agent supplies `filePath`, optionally `sectionLabel`, and any overrides to `run_request`. The handler checks the primary path lexically against the project root, constructs the environment layers and awaits `runVoidFile`. This is not a transitive filesystem sandbox ([RT-CLM-project-confinement](runtime.md#rt-clm-project-confinement); SRC-1, `packages/voiden-runner/src/mcpServing.ts`).

The runner rereads the document rather than executing the earlier preview. It resolves linked content, chooses sections, normalizes blocks and provides a headless editor plus environment and mutable runtime-variable references to the shared orchestration path. Builders/hooks and network execution own the next steps until return. Configured captures can feed subsequent sections and later calls in the session. External plugin implementation and live endpoint effects remain outside the captured evidence ([RT-RTE-request-execution](runtime.md#rt-rte-request-execution), [RT-CMP-request-orchestrator](runtime.md#rt-cmp-request-orchestrator); SRC-1, `packages/voiden-runner/src/runner.ts`).

The returned JSON contains section results and active plugin identities. An explicitly failed section sets the MCP call's `isError`; it does not discard the remaining results. Voiden returns status, body, timing and errors for the agent to inspect. It does not decide whether the user's task is complete (SRC-1, `packages/voiden-runner/src/mcpServing.ts`).

### Verification, rejection and recovery

The installed guidance separates execution success from semantic acceptance. It tells the agent to inspect errors/non-2xx responses, fix and rerun, and to sanity-check a successful body against the intended request. That comparison uses the user's intended outcome, not a core-provided answer oracle or an enforced reference assertion. A successful tool return therefore does not prove task correctness ([RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance); SRC-1, `packages/executors/src/skillContent.ts`).

Two source-supported rejection paths show who recovers. First, on a multi-section file a nonexistent requested label returns a failed result before execution. The external agent must rediscover or correct its selector. A stale label on a single-section file does not reject: the sole section executes. Thus the label is not an unconditional identity guard (SRC-1, `packages/voiden-runner/src/runner.ts`). Second, tagged-block compatibility checks run before orchestration. A gate or orchestration exception becomes a failed section result and the loop continues to later sections; the source does not automatically repair the document or undo earlier remote effects. The compatibility gate is not exact authored-version replay ([RT-CLM-version-gating](runtime.md#rt-clm-version-gating), [RT-RTE-request-execution](runtime.md#rt-rte-request-execution); SRC-1, `packages/voiden-runner/src/runner.ts`).

For an API failure, guidance assigns request editing and rerunning to the external agent. Those edits use the host's editor/shell, not a Voiden request-editing tool. Each subsequent run rereads the file, so an edit can reach execution. No supplied run shows a successful repair. Where environment selection still leaves an unresolved variable, guidance requests surfacing the actual error rather than guessing its cause; it does not authorize fabricating environment values (SRC-1, `packages/executors/src/skillContent.ts`, `packages/voiden-runner/src/runner.ts`).

### Delivery and optional recording

The immediate delivery boundary is the structured MCP return to the host. The host/agent decides how to present it and whether the user's intended result has been achieved. Optional recording is a second explicit call, not an automatic consequence of execution. Guidance requests the corresponding `results[i].result` object and request UID, not the whole run envelope. `write_result` accepts caller-supplied fields; it has no provenance binding to an earlier run. The instruction not to invent a response is consequently policy rather than enforced authenticity ([RT-RTE-result-write](runtime.md#rt-rte-result-write); SRC-1, `packages/executors/src/skillContent.ts`, `packages/voiden-runner/src/mcpServing.ts`).

The writer matches a block UID, inserts or replaces the corresponding response in that separator-bounded section, serializes fields and writes the file. A missing UID rejects the write. Long string bodies are truncated at 20,000 characters and marked truncated, so the recorded artifact need not contain the full immediate result. Matching is by UID, not a restricted request block type. The handler returns `written: true` only after the writer completes; this acknowledges file I/O, not factual verification or final conversational delivery (SRC-1, `packages/voiden-runner/src/resultBlock.ts`, `packages/voiden-runner/src/mcpServing.ts`).

Guidance warns against recording into a file with unsaved concurrent edits. The writer has no lock or transaction history; subsequent replacement can change the recorded response, but no internal rollback restores clobbered edits or reverses remote effects. The changed document is available to later readers; this account does not infer that retained responses influenced a later model decision ([RT-RTE-result-write](runtime.md#rt-rte-result-write); SRC-1, `packages/voiden-runner/src/resultBlock.ts`).

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

#### On [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance)

Workflow-specific role: supplies the explicit progression and assigns semantic inspection and repair to the foreground agent, rather than a Voiden verifier. The source's operative directions are:

> 3. Read the result, don't just assume success:
> --- `packages/executors/src/skillContent.ts`

>    - \`success: true\` — sanity-check the response \`body\` actually matches what the request was supposed to do.
> --- `packages/executors/src/skillContent.ts`

These directions establish requested behavior, not observed compliance or a reference-answer oracle.

#### On [RT-RTE-request-execution](runtime.md#rt-rte-request-execution)

Workflow-specific selection/recovery qualification: rediscovery is needed when a requested multi-section label is rejected. A single-section file deliberately ignores that filter. This affects which request the external agent can infer was selected (SRC-1, `packages/voiden-runner/src/runner.ts`):

> error:     `No section labelled "${options.sectionLabel}" found in ${filePath}`,
> --- `packages/voiden-runner/src/runner.ts`

The handler propagates explicit section failure to the host while preserving structured results (SRC-1, `packages/voiden-runner/src/mcpServing.ts`):

> const anyFailed = result.results.some((r) => r.result?.success === false)
> --- `packages/voiden-runner/src/mcpServing.ts`

#### On [RT-RTE-result-write](runtime.md#rt-rte-result-write)

Workflow-specific delivery qualification: the writer can reject stale/missing UIDs, and successful placement is independent of whether the caller supplied a genuine run result. Its UID lookup is protocol-agnostic rather than a request-type validator (SRC-1, `packages/voiden-runner/src/resultBlock.ts`):

> throw new Error(`No block with uid "${requestUid}" found in ${filePath}`)
> --- `packages/voiden-runner/src/resultBlock.ts`

The optional artifact is smaller than the immediate result when the string body exceeds the retention cap. This transformation prevents treating the recorded body as a complete execution transcript:

> const MAX_BODY_CHARS = 20_000
> --- `packages/voiden-runner/src/resultBlock.ts`
