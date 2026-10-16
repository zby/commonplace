---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Tolaria workflow account: desktop Codex delegation, MCP note replacement, conflict rejection and user-visible delivery."
run-id: AAS-2026-10-14-tolaria-42ddaf2ee8cd-01
reviewed-boundary: "48f2a70844c1e8005a7aa5f1499c66f7678360de"
---

# Tolaria workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a desktop request to revise an existing vault note using the selected Codex agent and Tolaria's MCP read/update tools. It connects the application's foreground invocation, retained-content service and return channel. These are connected by shipped configuration, not inferred from unrelated features: the Codex command configures the bundled MCP server with the request's active vault roots. The application does not prescribe a mandatory read–edit–verify sequence. The read followed by guarded replacement below is an available workflow branch, conditional on the external agent choosing those tools and supplying the conflict token. No captured execution establishes that an agent took this branch or delivered a correct revision (SRC-1, `src-tauri/src/codex_cli.rs`, `mcp-server/index.js`; [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send), [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)).

This account uses SRC-1 implementation and prompt doctrine/design at the frozen commit. Additional selected source inspection covers `src/lib/aiAgentSession.ts`, `src/lib/aiAgentConversation.ts`, `src/lib/aiAgentStreamCallbacks.ts`, `src/utils/streamAiAgent.ts`, `src-tauri/src/codex_cli.rs`, `mcp-server/index.js`, `mcp-server/tool-service.js` and `mcp-server/vault.js`. These reads extend inspection at the same revision, not the source boundary. External Codex internals, actual model decisions, deployed bridge delivery and successful operation remain unobserved. The boundary remains complete artifact, partial loop.

### 1. User request becomes an agent assignment

The user selects the target and submits a prompt with optional note references. `sendAgentMessage` ignores an empty prompt or a send while thinking/tool-executing; missing vault or unavailable target produces a local response instead of delegation. On admission it allocates a streaming message, abort controller and per-request tool map, hydrates references, and constructs the prompt. The delegated material is assembled system guidance plus formatted completed user/assistant history, the latest prompt and hydrated references. The history is a bounded suffix, not the full retained transcript, reasoning or complete previous tool trace. This is application-owned context selection; it does not establish the external CLI's complete context policy (SRC-1, `src/lib/aiAgentSession.ts`, `src/lib/aiAgentConversation.ts`; [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)).

Guidance asks the agent to read vault `AGENTS.md`, keep edits scoped to active vaults, prefer file edit tools, and call `open_note` after creating or editing a note. These instructions shape the proposed work but do not enforce that a read, semantic review or UI opening occurs. The MCP update branch is available despite the preference for file edit tools; it is not the sole edit route (SRC-1, `src/utils/ai-agent.ts`; [RT-OBJ-agent-prompt](runtime.md#rt-obj-agent-prompt)).

### 2. Tolaria delegates decisions, not just text generation

The frontend installs a scoped event listener and invokes native agent streaming. The Codex adapter sends the assembled prompt through stdin to `codex exec --json`, with the vault as working directory, an optional model override, a temporary last-message output path and Tolaria MCP configuration. Its MCP environment supplies `VAULT_PATH`, `VAULT_PATHS` and the UI bridge port. The user initiates the task; Tolaria selects dispatch and supplies capabilities; the external agent/model owns subsequent tool selection and stopping decisions. No internal reviewer or separate worker-agent handoff is established by this selected path (SRC-1, `src/utils/streamAiAgent.ts`, `src-tauri/src/codex_cli.rs`; [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)).

Safe mode selects Codex's read-only sandbox and on-request approval flags. Those flags require the external CLI's enforcement and do not make the separate Node MCP service read-only. Consequently, a safe-mode request can still reach MCP note replacement. User initiation and sandbox choice are not per-content human approval of the replacement (SRC-1, `src-tauri/src/codex_cli.rs`; [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write), [RT-BAP-tool-executor](runtime.md#rt-bap-tool-executor)).

### 3. A note read supplies content and an optional conflict token

If the agent selects `get_note`, the MCP service resolves the requested active vault and returns parsed frontmatter, trimmed body and file `mtimeMs`. The delegate therefore receives structured note content rather than a guaranteed byte-for-byte full-file image. For `update_note`, the proposed `content` is the complete replacement, including any frontmatter the agent chooses to preserve. Tolaria does not reconstruct omitted frontmatter from the earlier read (SRC-1, `mcp-server/vault.js`, `mcp-server/tool-service.js`, `mcp-server/index.js`; [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)).

The tool description explicitly connects the read's token to the write:

> Optionally pass expectedMtime (the note mtimeMs returned by get_note) to fail-fast when the note changed between read and write.
> --- `mcp-server/index.js`

This is guidance for caller sequencing, not a code requirement to read before writing. The caller proposes path, replacement text and optional `expectedMtime`; the service decides active-vault eligibility and filesystem admission. There is no expected-answer oracle or content-quality gate in this inspected service. This is an open user request, not a bounded improvement experiment (SRC-1, `mcp-server/tool-service.js`, `mcp-server/vault.js`; [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)).

### 4. Verification can reject staleness, not establish correctness

For replacement, the service resolves the existing note and forwards the optional token. The filesystem function checks it before writing. A mismatch throws a message instructing the caller to re-read and retry:

> if (expectedMtime === undefined || expectedMtime === null) return
>   if (stat.mtimeMs === expectedMtime) return
>
>   throw new Error(
>     `Note was modified since read: expectedMtime ${expectedMtime} but on-disk mtimeMs is ${stat.mtimeMs}. Re-read the note and retry.`,
>   )
> --- `mcp-server/vault.js`

Omitting the token skips this guard. Even when supplied, stat comparison followed by a separate write is not atomic compare-and-swap. A concurrent change after the comparison can escape detection. Passing the guard says nothing about whether the proposed note answers the user's request or preserves the note's meaning (SRC-1, `mcp-server/vault.js`; [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)).

An admitted update writes a sibling temporary file and renames it over the note, then returns the resulting mtime. The catch branch attempts temporary-file removal and rethrows. This is replacement error handling, not a workflow transaction or a promise of crash durability. If an error occurs after rename, the note can already have changed. The tool service emits `vault_changed` only after the update function returns successfully (SRC-1, `mcp-server/vault.js`, `mcp-server/tool-service.js`; supporting replacement passage in [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)).

### 5. Rejection returns control to the caller

The MCP request handler converts thrown errors to tool-result content:

> return {
>       content: [{ type: 'text', text: `Error: ${error.message}` }],
>       isError: true,
>     }
> --- `mcp-server/index.js`

The service does not automatically re-read, merge or retry. The caller receives the rejection and owns any next attempt; whether Codex follows the retry instruction remains external and unobserved. The adapter serializes MCP result/error material into normalized tool events. Frontend callbacks recognize failed tool output, mark that action error and avoid its success-only file-operation callback. A rejected tool call does not itself force a terminal stream error: only the stream-error callback sets `streamFailed`. Thus the UI can finish a response that contains a failed action (SRC-1, `src-tauri/src/codex_cli.rs`, `src/lib/aiAgentStreamCallbacks.ts`, `mcp-server/index.js`).

### 6. Delivery has separate file and conversation boundaries

A successful MCP update returns path, absolute path, vault root and mtime, and emits a vault-change action. It does not itself open the note. Opening requires a separate `open_note` call as requested by the prompt; that handler emits refresh/open actions, not proof that a deployed window displayed the note (SRC-1, `mcp-server/tool-service.js`, `mcp-server/index.js`; [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)).

For conversation delivery, Codex agent-message events become text deltas; its last-message file can supply text when none was emitted. On normal completion, the frontend finalizes the response, makes it nonstreaming, marks remaining pending actions done and requests a vault refresh. This is a presentation boundary, not independent verification of every action or the user's requested outcome:

> actions: message.actions.map((action) => (
>           action.status === 'pending' ? { ...action, status: 'done' as const } : action
>         )),
> --- `src/lib/aiAgentStreamCallbacks.ts`

A stream error instead preserves partial text and marks pending actions error; regenerate removes the selected conversation suffix and resubmits its prompt. Neither operation rolls back previously changed files. Stop requests cancellation and suppresses later callbacks, but does not reverse writes. Later sends can reuse completed message text through the history builder; session persistence requests are best effort, not a demonstrated durable handover. Those limits are carried by [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send) (SRC-1, `src/lib/aiAgentSession.ts`, `src/lib/aiAgentStreamCallbacks.ts`, `src-tauri/src/codex_cli.rs`).

In short, the shipped path coordinates a user assignment, an external decision-making agent, an executable vault service and a UI return channel. Its checked rejection is stale-file detection when the caller supplies a token. Correctness review, automatic repair and successful end-to-end delivery are not established by these implementation paths.

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

#### On [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)

Workflow role: delegates the user's assignment to the selected external agent and carries normalized progress/results back. Conversation finalization accepts stream completion, not a semantic acceptance test. Regenerate is a conversation retry, not filesystem recovery. The selected Codex branch and its limits are traced above.

#### On [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)

Workflow role: executable content-admission handoff within the delegated request. For existing-note replacement, the agent supplies the complete proposed content and may supply a read-derived mtime token. The service can veto the stale update but does not automatically repair it; subsequent re-read/retry belongs to the caller. File replacement, UI-action emission and conversation completion are separate delivery stages. No new route identity is declared for these already-recorded mechanisms.
