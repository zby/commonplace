---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Arsumbris workflow account: documented read-before-overwrite coordination, rejection and tool-result delivery within the entry repository's partial loop."
run-id: AAS-2026-10-15-arsumbris-a9be6bac297f-01
reviewed-boundary: "716bb14f2bf50e249d414525c8e07c50478fc786"
---

# Arsumbris workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is an agent overwriting a workspace file under the documented read-before-write policy. It is selected because the same source supplies its tool input, mediator example, session configuration and action pipeline. This permits a connected account of a proposal, rejection condition and tool-result handoff without joining unrelated capabilities. The canonical route is [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action).

This is a documentary workflow, not an observed task execution. I inspected SRC-1, `au-mcp.md` and `au-engine.md` in full at the frozen revision; both were already within the boundary's inspected scope. Their evidence layer is doctrine/design, including illustrative code. The separate harness, adapters, daemon, plugins and engine implementations are outside the frozen entry artifact. The source does not supply a user request transcript, actual read result, successful write or final agent answer. Thus the trace reaches a declared tool acknowledgment, not verified end-to-end delivery to a user.

### Request, context and handoffs

1. **Workspace and session preparation.** The documented engine mounts repositories and holds their file-derived graph in memory. A harness connects through an adapter to the workspace MCP daemon. The adapter maps lifecycle hooks and declares the harness's native tool surface; its launch example materializes skills/injects and prints a spawn command, which does not itself establish a running agent. An agent-profile selects visible tools, hooks, skills, injects and native-tool allowance. These responsibilities belong to [RT-OBJ-agent-profile](runtime.md#rt-obj-agent-profile) and [RT-BAP-profile-guidance](runtime.md#rt-bap-profile-guidance), not to an inferred planner. Profile contents and guidance bodies for a particular task are not supplied. SRC-1, `au-mcp.md` supports these session contracts.

2. **Agent proposal.** A user request to change a file is the illustrative task premise, not a quoted source request. The foreground harness agent owns the decision to read, choose content and propose an overwrite. The documented `write_file` type supplies an absolute `file_path` and full replacement `content`; runtime metadata selects a plugin entry and requests read-write broker access. The handoff is therefore a typed action with a target and replacement text. No sub-agent is delegated a separate task. Agent-to-tool delegation here is execution delegation, not evidence of multi-agent planning. Model selection and reasoning remain unresolved in [RT-CMP-agent-harness](runtime.md#rt-cmp-agent-harness).

3. **Admission before action.** The daemon's mediators decide allow, deny, inject or ask. The read-guard example tests the pending tool name and `ctx.hasRead` for the same target path. A previous read is a procedural witness, not a judgment that replacement content is correct. The model proposes the change; software supplies this veto. `ask` allows for a further decision, but the approval interface, human participation and retained approval scope are not established. This is open editing, with no expected-answer oracle or improvement curriculum. See [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action) and SRC-1, `au-mcp.md`.

4. **Execution and observation.** On the declared admitted path, the plugin acts through the governed engine seam and the pipeline appends events to the session ledger. The tool example returns a content string reporting the path. Its body is a sketch, not an implemented file write:

>       // do the work through ctx (broker = the governed engine write seam)
>       return { content: `wrote ${file_path}` }
> --- `au-mcp.md`

Consequently, even that acknowledgment cannot independently prove a file effect. SRC-1, `au-engine.md` declares that changed files update the live graph; actual write, ledger durability and subsequent graph consumption are unobserved. The existing route record carries these same evidence limits.

### Rejection, recovery and verification

An unread overwrite is the supported rejection case. The mediator returns a denial with the reason to read the file before overwriting it. The natural recovery is for the foreground agent to obtain a read and submit another proposal. That is a possible continuation suggested by the condition and message, not a shipped retry state machine or a demonstrated repair. The source does not define read-tracking lifetime, whether the read becomes stale after another writer's change, or whether the agent reliably follows the denial. Neither automatic rollback nor durable resume is established within SRC-1, `au-mcp.md`.

The governance boundary is conditional. Fail-closed floor loading and fail-open mediation when the daemon is unreachable concern different failure points. [RT-CLM-mediation-floors](runtime.md#rt-clm-mediation-floors) supports only the documented mediated-path policy, not universal read-before-write enforcement. Host edits, external file changes and unsandboxed extension effects cannot be assumed to traverse this guard; see [RT-RTE-host-edit](runtime.md#rt-rte-host-edit) and [RT-CLM-user-privileges](runtime.md#rt-clm-user-privileges).

Verification is also narrower than product acceptance. The read guard checks a procedural precondition. Engine diagnostics check typed structure and references, but do not block saves or reads, as recorded in [RT-CLM-diagnostic-saves](runtime.md#rt-clm-diagnostic-saves). No source-supported reviewer checks the requested meaning, compares a result against an answer oracle or signs off the finished task. Diagnostic findings could inform another agent action, but this source supplies no mandatory diagnose-revise-verify cycle.

### What counts as delivered

The documented local completion boundary is the tool result returned toward the harness after the action stage; the ledger is an observation sink, not proof of user acceptance. The foreground harness owns any subsequent checking, explanation and final response. The entry repository does not specify that terminal response or the user's acceptance condition. Files and ledger events are declared retained effects, but no ledger replay into later model context or trace-fed revision is established. The bounded result is therefore a coherent declared action workflow with an explicit rejection condition and acknowledgment contract, not evidence that a multi-step user task completed successfully.

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

#### On [RT-RTE-mediated-action](runtime.md#rt-rte-mediated-action)

Workflow selection: this is the representative request-to-tool-result path because its proposal fields, veto and acknowledgment are documented together.

Delegation boundary: the foreground agent delegates a typed operation to a plugin through adapter/daemon mediation. No separate agent task frame or returned sub-agent synthesis is established.

Recovery ownership: a denied proposal leaves further action with the harness agent; read-and-retry is a possible continuation, not an evidenced automatic recovery protocol.

Delivery boundary: a tool acknowledgment completes the local handoff. Independent write verification, final user response and task acceptance remain unestablished.
