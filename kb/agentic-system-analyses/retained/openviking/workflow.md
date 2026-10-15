---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenViking workflow: OpenCode automatic recall, event capture, compaction-triggered commit and later context delivery, with bounded recovery."
run-id: AAS-2026-10-14-openviking-7b5b57541af5-01
reviewed-boundary: "5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b"
---

# OpenViking workflow report

## Workflow account

### Selection and evidence boundary

This account selects the shipped OpenCode v1 hook workflow: recall on a user message, capture of conversation events, flush/commit at compaction, background extraction and recall on a later message. It was selected because the adapter supplies both production and consumption handoffs, rather than requiring a hypothetical caller to join unrelated database APIs. Recall and capture have separate configuration gates; the account is conditional on those gates and the host issuing the relevant hooks. It does not characterize every integration or the v2 scheduling path.

The workflow delivers context to a host, not a completed answer to the user's task. The external OpenCode runtime owns foreground agent/model execution and the final user-facing answer. Its actual scheduling and use of injected text are not frozen evidence. All mechanisms here are SRC-1 implementation at the boundary revision; no execution trace, test run or provider result was supplied. Delivery wiring is established, successful execution and benefit are not.

Additional source inspection covers `examples/opencode-plugin/index.mjs`, the complete `examples/opencode-plugin/lib/memory-session.mjs` and `examples/opencode-plugin/lib/memory-recall.mjs`, the complete `examples/memory-plugin-shared/lib/batch-send.mjs` and `examples/memory-plugin-shared/lib/retryable.mjs`, and enqueue/replay ranges of `examples/memory-plugin-shared/lib/pending-queue.mjs`. These are newly inspected SRC-1 paths or ranges, not additional sources. Canonical shared modules are inspected where the imported generated copies are absent, as already limited in [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall). Capture shaping, queue housekeeping/claim internals and packaged execution remain incompletely inspected.

### Request, recall and host handoff

On `chat.message`, the plugin delegates session-context injection and relevant-memory recall concurrently when recall is enabled. When disabled it only invokes session injection. The hook catches failures and logs a warning rather than guaranteeing either transformation completed (SRC-1, `examples/opencode-plugin/index.mjs`).

> await Promise.all([
>   sessionInject.injectSessionContext(input, output),
>   recall.injectRelevantMemories(input, output),
> ])
> --- `examples/opencode-plugin/index.mjs`

The recall adapter extracts nonsynthetic, nonignored text, checks minimum query length and bypass settings, and requires a healthy service. It supplies the current query, configured peer identity and mapped OpenViking session to the shared recall helper. Database context assembly selects, budgets and optionally rewrites retained content; the client can omit it entirely on `no_relevant`, and otherwise prefers the digest over rendered entries. These consequential transformations and minimum passages are retained in [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) and [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall), with SRC-1 anchors there.

A nonempty block plus session ID permits prepending a synthetic host text part. That is the first delivery boundary: output structure is changed, but model compliance is not enforced. [RT-BAP-recall-context](runtime.md#rt-bap-recall-context) identifies the consumer and force. The full memory store, original traces and intermediate database/model processing are not delivered to the host by this recall route. Session injection is a parallel responsibility; its content and failure interaction were not traced beyond this hook, so this account makes no complete-host-context claim.

### Capture, compaction and asynchronous extraction

The plugin forwards host events to a session manager. Message and part updates accumulate roles and parts by session/message ID when capture is enabled. The new [WF-RTE-session-capture](#wf-rte-session-capture) establishes the adapter handoff that the runtime baseline left unresolved. It maps host sessions to database session IDs, shapes eligible payloads and sends batches, or queues retryable work. This is software delegation to the database, not delegation to a second foreground agent.

Before host compaction, the explicit hook requests a capture flush and commit:

> await sessionManager.flushSession(input.sessionID, {
>   commit: true,
>   reason: "experimental.session.compacting",
> })
> --- `examples/opencode-plugin/index.mjs`

The manager serializes overlapping flushes of the same session. It attempts pending message transmission before requesting commit, but does not require every payload to have reached the server: queued messages count as captured, and failed payload counts are logged rather than necessarily aborting the commit branch. Thus ordering of local calls is established; complete transcript inclusion before every accepted commit is not (SRC-1, `examples/opencode-plugin/lib/memory-session.mjs`; `examples/memory-plugin-shared/lib/batch-send.mjs`). Idle events flush without forcing commit, though a configured pending-token threshold can cause commit; compacted/deleted events and dispose can force it. These are alternatives within the selected adapter, not universal lifecycle promises.

Commit sends `keep_recent_count: 0`. A successful HTTP response is reported as accepted by the adapter. On the server, [RT-RTE-session-commit](runtime.md#rt-rte-session-commit) distinguishes phase-one archive/queue publication from phase-two extraction. The archived messages, RequestContext, task/archive identity and policy coordinate the worker's handoff. Readiness/order checks and terminal markers determine whether resume runs, defers or stops. Task acceptance does not prove that extraction completed or persisted memory successfully.

The extraction loop has its own prepared model context, existing-memory/schema scope and selected tools. It coordinates model proposals, tool callbacks and repair before updater submission, rather than asking the foreground OpenCode agent to perform each extraction step. [RT-CMP-account-vlm](runtime.md#rt-cmp-account-vlm) and [RT-RTE-session-commit](runtime.md#rt-rte-session-commit) retain the implementation evidence. Conditional skill admission is a further branch described by [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), not necessary to establish ordinary recall delivery. Per-item human approval, all-or-nothing persisted rollback and an expected-answer evaluator are not established by those routes.

### Recovery, verification and later delivery

Verification here consists of local eligibility/status checks, server readiness/terminal checks and extraction parsing/repair, not verification of the host's task answer. No supplied reference outcome establishes the truth or usefulness of extracted content. Human initiation and host identity are separate from per-content approval.

For the selected failure path, an unavailable service sends eligible message payloads to a local pending queue; a retryable commit response also requests local enqueue. Initialization and healthy session creation trigger replay. Replay discards successful and nonretryable entries, applies a retry budget by default, and stops after a retryable message failure so later pending work is deferred. [WF-RTE-session-capture](#wf-rte-session-capture) retains the passages. There are separate local replay and server QueueFS recovery owners. Neither constitutes proof of end-to-end exactly-once effects or eventual delivery. In particular the adapter reports `queued` after awaiting commit enqueue without checking the enqueue result.

On a later `chat.message`, the same adapter can request newly retained context through the mapped database session. [RT-RTE-context-assembly](runtime.md#rt-rte-context-assembly) establishes fresh selection, session expansion and cooling; [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall) establishes what crosses into host output after client omission. There is no observed retained item linking an actual extraction to a later invocation here. The evidenced end point is conditional construction of a synthetic text part, not demonstrated memory reuse or an improved answer.

Working-context control is split across owners. The host controls compaction itself; the plugin observes its boundary and attempts persistence. The server prepares a separate extraction context and returns selected recall text rather than all inner tool deliberation. This resembles a separately scoped processing frame, but does not establish subprocess isolation or automatic pointer dereferencing. Archived content and stored memory remain externally addressable through explicit retrieval; later assembly returns selected content by value. Host summary/tail preservation after compaction is uninspected, so the plugin's commit hook cannot be credited with a guaranteed lossless context handoff.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-session-capture
Label: OpenCode session capture

Endpoints/progression/owner: OpenCode event callback → memory-session manager's session/message maps → payload shaping → batch or serial HTTP message calls/local pending enqueue → compaction/threshold/dispose commit request; initialization or session creation can replay queued messages and commits. The host owns event emission; the plugin owns capture, local persistence and request scheduling. SRC-1, `examples/opencode-plugin/index.mjs`; `examples/opencode-plugin/lib/memory-session.mjs`; `examples/memory-plugin-shared/lib/batch-send.mjs`; `examples/memory-plugin-shared/lib/pending-queue.mjs`; `examples/memory-plugin-shared/lib/retryable.mjs`.

Distinct identity: this is the adapter's trace-production and transport route, preceding the database archive/extraction referent in [RT-RTE-session-commit](runtime.md#rt-rte-session-commit), not a replacement or contained server phase. It shares session identity with [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall), but captures events rather than delivering retrieved context. No corresponding adapter capture declaration exists in the supplied runtime after comparison.

- Immediate return: event/flush completion, counts used internally and commit status accepted or queued; nonretryable commit failures throw. These statuses do not mean completed extraction.
- Later read-back: version-2 local session state reloads mappings, message metadata and uncaptured parts; pending payloads replay to session endpoints. Captured messages serialize with empty parts. Server archives then feed the separately declared extraction route.
- Delegated visibility: shaped role/content or role/parts plus optional peer_id reaches message endpoints or local queue; it is not necessarily the complete host transcript. Capture shaping internals remain partially uninspected.
- Selection predicate: capture enabled, uncaptured message, eligible role/parts, assistant-turn setting and nonempty shaped payload; threshold or explicit lifecycle boundary controls commit. Batch 404/405 falls back to serial requests; retryability includes missing status, 408, 429, server errors and explicitly retryable 409.
- Invalidation or expiry: captured flags suppress retransmission from the session map and captured parts are omitted from persisted state; session deletion removes the mapping after flush. Replay removes success/nonretryable entries and drops exhausted retries; full stale cleanup and crash-claim semantics remain uninspected.
- Activation or effect: local state writes, message transmission, pending enqueue and commit scheduling are wired; durable server extraction and host behavioral effects are unobserved.
- Evidence limits: source only; host event completeness, payload-shaping fidelity, deployed package imports, queue storage durability, complete replay ordering and exactly-once delivery are not established. Commit enqueue failure is not checked before returning queued.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal/admission: host events supply trace material, code shapes transport payloads and database responses admit transmission; no model proposes at this adapter stage. The computational host trace can include user and assistant content, but caller identity does not establish per-item human approval. Rejection is local eligibility filtering, message/commit HTTP failure or queue failure. Recovery is pending replay, retaining unsent message flags and per-session flush serialization; no full rollback is shown. Guidance is static plugin configuration and capture rules; persisted material is transport payloads/state, not a formulated theory. Answer oracle: inapplicable — transport/status checks do not evaluate a task answer. Operating mode: open event-fed capture and lifecycle maintenance, not a bounded experiment.

> const added = await flushPendingMessages(opencodeSessionId, state)
> if (commit && isCaptureEnabled(config)) {
>   await commitOvSession(state.ovSessionId, { force: true, reason })
> } else if (added > 0) {
>   await maybeCommitByThreshold(state)
> }
> --- `examples/opencode-plugin/lib/memory-session.mjs`

> const queued = await enqueue("addMessage", state.ovSessionId, item.body)
> if (!queued.ok) break
> item.message.captured = true
> added += 1
> --- `examples/opencode-plugin/lib/memory-session.mjs`

> await writeFile(join(dir, filename), JSON.stringify(entry), {
>   encoding: "utf-8",
>   flag: "wx",
>   mode: PENDING_FILE_MODE,
> });
> --- `examples/memory-plugin-shared/lib/pending-queue.mjs`

> if (entry.type === "addMessage") {
>   deferred += Math.max(0, pending.length - processed);
>   break;
> }
> --- `examples/memory-plugin-shared/lib/pending-queue.mjs`

> if (isRetryableFailure(res)) {
>   await enqueue("commitSession", ovSessionId, body)
> --- `examples/opencode-plugin/lib/memory-session.mjs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-session-commit](runtime.md#rt-rte-session-commit)

Workflow handoff: the selected OpenCode compaction hook requests this route after attempting pending-message flush, with `keep_recent_count: 0`. The adapter distinguishes HTTP acceptance/queued retry from failure, not completed extraction. Its success log therefore cannot serve as the workflow's extraction-completion verifier. SRC-1, `examples/opencode-plugin/index.mjs`; `examples/opencode-plugin/lib/memory-session.mjs`; supporting adapter passages are retained in [WF-RTE-session-capture](#wf-rte-session-capture).

#### On [RT-RTE-plugin-recall](runtime.md#rt-rte-plugin-recall)

Workflow delivery condition: this is the selected workflow's host-context end point, both before initial foreground work and potentially after later extraction. It requires a nonempty selected block and a host session ID. A delivered synthetic text part proves neither that the foreground model used it nor that a particular preceding commit produced it. SRC-1, `examples/opencode-plugin/lib/memory-recall.mjs`; the runtime record retains the delivery passage.
