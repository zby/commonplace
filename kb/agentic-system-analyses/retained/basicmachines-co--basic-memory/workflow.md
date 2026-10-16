---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Basic Memory workflow account: Pi working-thread capture, note persistence and later prompt-driven recall at the frozen revision."
run-id: AAS-2026-10-16-basic-memory-46fe4c6cfdc3-01
reviewed-boundary: a72751c5d626380dedeed30f55f7a80ba3dc710d
---

# Basic Memory workflow report

## Workflow account

### Selected workflow and evidence limit

The representative workflow is **continue a Pi working thread using a saved checkpoint**: a user request produces user/assistant turns in Pi, the shipped extension captures those turns after the agent settles, and a later eligible agent start searches checkpoints using its prompt and returns reference excerpts to the host. This workflow was selected because its producer, retained intermediate result and later consumer are explicitly connected in the shipped integration, rather than assembled from unrelated note tools. It demonstrates coordination by fixed code around a foreground assistant, not delegation to a team of agents ([RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint)).

The account selects direct capture/recall with `useHookFlow` false. The Python hook alternative is a distinct route, not another step in this sequence ([RT-RTE-hook-checkpoint](runtime.md#rt-rte-hook-checkpoint)). All evidence is implementation or doctrine/design from SRC-1 at the boundary pin. No session, target command, test or provider was executed. Host task completion, successful persistence, actual recall and improved continuation remain unobserved.

### Request, authority and handoffs

1. **The host owns the task.** Pi supplies the request, branch history, lifecycle callbacks and eventual foreground generation. Basic Memory does not determine the assistant's intervening task steps. At `session_start`, the extension resets its one-recall flag and refreshes configuration. Automatic operations require valid configuration, an explicit project mapping and workspace trust. These are automation gates, not per-checkpoint human review. Configured executable overrides have a separate trust requirement (SRC-1, `integrations/pi/extensions/index.ts`; [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint)).
2. **Settled-event capture delegates a draft, not a reasoning task.** At `agent_settled`, fixed extension code extracts current-branch user/assistant text and checks `captureMinChars`. `buildCaptureDraft` also requires at least one user turn. The extractor retains string content and recognized text blocks; other roles and nontext blocks are not passed into the checkpoint. It creates an extractive Markdown thread, a clipped opening-request summary and metadata including project-independent session provenance. This is not a model-generated verification or summary of task success (SRC-1, `integrations/pi/extensions/index.ts`, `integrations/pi/extensions/session.ts`).
3. **The subprocess receives concrete write inputs.** `captureSession` supplies the configured binary with `tool write-note`, title, capture folder, `pi_session` type, tags and explicit project arguments. Markdown travels on stdin; timeout and abort signal bound the subprocess attempt. When session and branch IDs exist, their hash yields a stable default title, and untitled capture requests overwrite. A supplied title removes that overwrite flag. Branch identity uses the deepest detected fork child, falling back to branch/root/leaf identifiers; this implements checkpoint naming, not verified host branch isolation (SRC-1, `integrations/pi/extensions/index.ts`, `integrations/pi/extensions/session.ts`, `integrations/pi/extensions/bm-cli.ts`).
4. **Knowledge services own acceptance and storage work.** The CLI tool feeds the common write route, whose deterministic service owns path conflicts, accepted-note transactions and downstream materialization. An extension event does not bypass these checks. The runtime's separate records establish accepted DB state versus deferred Markdown/index/vector completion, guarded writes and startup recovery; they do not establish successful storage in an actual Pi run ([RT-RTE-note-write](runtime.md#rt-rte-note-write), [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization)).
5. **A later prompt delegates a search, then returns selected data.** On the first eligible `before_agent_start`, the extension searches `pi_session` notes after the configured timeframe, in the configured project, using the prompt or fallback query. The formatter takes the first five returned rows, retains title and note reference, and flattens/clips each matched chunk or content excerpt to 500 characters. It returns a displayed custom message to the host. It does not automatically reload full notes or replay the saved thread. Search ranking quality and the host's incorporation of this message remain unverified (SRC-1, `integrations/pi/extensions/index.ts`; [RT-BAP-recall-data](runtime.md#rt-bap-recall-data)).

The capture draft preserves a thread rather than a certified conclusion:

> "## Thread to date",
> ...thread.map((turn) => `- **${turn.role}:** ${turn.text}`),
> --- `integrations/pi/extensions/session.ts`

The later consumer sees only the selected rendering, not that entire draft:

> const recalled = rows.slice(0, 5).flatMap((row) => {
> --- `integrations/pi/extensions/index.ts`

The runtime record supplies the exact excerpt-clipping and reference-only warning passages. These output-selection rules bound this injection, not the host's entire context. Further explicit reads remain possible; no separate agent frame is created or popped. Direct capture does not itself compact the host context. The saved thread remains in the knowledge store, while full original history is referred to as Pi session history by the draft text; actual host-history retention is outside the inspected implementation ([RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint), [RT-BAP-recall-data](runtime.md#rt-bap-recall-data); SRC-1, `integrations/pi/extensions/session.ts`).

### Verification, rejection, recovery and delivery

There are distinct acceptance levels. First, extension predicates can decline automatic capture or recall before any subprocess runs. Second, common note services can reject a proposed mutation. Third, materialization guards can refuse filesystem publication despite prior DB acceptance. The supplied runtime records contain the write-conflict and external-change passages; these are revision/storage checks, not answer oracles judging whether the thread is true or useful ([RT-RTE-note-write](runtime.md#rt-rte-note-write), [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization)).

The subprocess wrapper rejects nonzero exits and invalid JSON. On a zero exit with parseable JSON, it returns the parsed value without validating a success discriminant. `captureSession` then constructs a capture message using optional title/action/permalink fields and defaults. Consequently a displayed capture message is not independent semantic verification of successful note admission, complete materialization or task completion. No read-after-write check is present in this inspected capture helper (SRC-1, `integrations/pi/extensions/bm-cli.ts`, `integrations/pi/extensions/index.ts`).

> if (result.code !== 0) {
>   throw new BmCommandError(result.stderr.trim() || result.stdout.trim() || "bm command failed", result);
> }
> --- `integrations/pi/extensions/bm-cli.ts`

> return JSON.parse(result.stdout) as T;
> --- `integrations/pi/extensions/bm-cli.ts`

For the checked failure path, a subprocess error or invalid JSON during settled capture throws into the event handler, which emits a warning instead of the success entry. There is no immediate retry in that handler. A later eligible settled event or manual `bm-capture` command can initiate another attempt; this is a new attempt, not guaranteed automatic recovery. Downstream pending/writing/failed materialization recovery belongs to the Python storage subsystem and does not imply retry of a rejected extension request. Previous-content rollback is not established (SRC-1, `integrations/pi/extensions/index.ts`; [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization)).

> notify(ctx, `Basic Memory capture failed: ${formatError(error)}`, "warning");
> --- `integrations/pi/extensions/index.ts`

Recall failure has a different consequence: the one-recall flag is set before the search. Failure emits a warning, but the flag remains set, so subsequent agent starts in that session do not automatically retry. `session_start` resets it; the manual `bm-recall` command provides a separate explicit attempt. No-hit recall instead delivers a no-checkpoints message. These branches preserve host continuation rather than providing a verified continuation result (SRC-1, `integrations/pi/extensions/index.ts`).

Delivery therefore has two bounded meanings. Capture returns a formatted status and, on the normal settled branch, appends an extension entry and notifies the UI. Later recall returns selected reference data through the host-message interface. Neither establishes that the foreground assistant followed the checkpoint's suggested next step, completed the user's original request, or benefited from retention. Human configuration enables automation; fixed code proposes and admits checkpoint text through software checks without a per-content human approval or an expected-answer oracle ([RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint)).

### Inspection coverage

This member directly inspected all of `integrations/pi/extensions/index.ts`, `integrations/pi/extensions/session.ts` and `integrations/pi/extensions/bm-cli.ts` at SRC-1's frozen commit. This checks producer transformations, subprocess protocol, callback ordering and final recall rendering against the runtime baseline. Python acceptance/materialization findings are cited from the supplied runtime records rather than re-established here. Config parser internals, search ranking internals, Pi scheduling/compaction implementation and other host integrations were not inspected for this workflow. These limits prevent claims of default activation, complete branch fidelity, optimal retrieval, host-context safety or cross-host behavior. They do not prevent the bounded source-level handoff account above.

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

#### On [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint)

Workflow selection: this route connects capture of the foreground working thread to later prompt-driven search and host-message delivery. It is coordination by event handlers and a CLI subprocess, not sub-agent delegation. Completion of the subprocess protocol, completion of accepted-note storage and usefulness to the foreground task are separate acceptance levels. The inspected caller checks exit code and JSON syntax, not a write-success discriminant. Capture failure warns without an immediate retry; recall failure consumes the current session's automatic attempt. Manual commands provide explicit re-entry, not rollback.

#### On [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization)

Workflow delivery boundary: this is downstream persistence work, not a task-answer verifier. Its guarded file writes and recovery protocol qualify what a checkpoint notification can mean; they do not certify capture fidelity, search availability at every instant or successful later continuation.

#### On [RT-BAP-recall-data](runtime.md#rt-bap-recall-data)

Workflow final handoff: the extension delivers selected note references and bounded excerpts to the foreground host, with reference-only guidance. The delivery boundary ends before the assistant's interpretation or action. A retained checkpoint and a message-return path establish neither successful use nor a verified answer to the original request.
