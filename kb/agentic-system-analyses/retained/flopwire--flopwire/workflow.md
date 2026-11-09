---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Flopwire workflow: evidence-led contact, local task request, correlated reply and recovery"
run-id: AAS-2026-10-20-flopwire-184bd013bba1-01
reviewed-boundary: "057a4b87603cc878e81d9eb49298ddc4eb9eeb23"
---

# Flopwire workflow report

## Workflow account

This account selects the shipped procedure for recovering another session's work, contacting that session when authorized, requesting an answer, and inspecting its reply. It is representative because the messaging skill explicitly connects retained evidence, session identity and live coordination. The concrete transport traced is two addressable sessions of the same user on one device without a configured server; it does not require team enrollment or a cloud recipient. The workflow is supported by instructions and implementation, not an observed exchange. Flopwire supplies coordination and evidence; the external harness schedules model turns and executes any delegated work. SRC-1: `plugins/codex/flopwire/skills/messaging/SKILL.md`, `internal/devicebus/local.go`; [WF-RTE-request-reply](#wf-rte-request-reply).

1. **Recover the relevant owner and evidence.** When another session's unfinished work or unexplained decision blocks progress, the initiating agent follows the skill's history-first procedure. For change provenance it obtains full commit IDs, queries `flopwire_change`, reads command/result evidence, and uses session discovery and grep if that route cannot answer. Only when contact is needed does it check exact-session presence. The agent must establish the history session before selecting the live recipient; a title or current branch is insufficient. This is an instructed decision process, with backend selection and evidence delivery supplied by [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval). SRC-1: `plugins/codex/flopwire/skills/messaging/SKILL.md`.
2. **Delegate a bounded question.** An authorized initiating agent sends to the full session ID with `intent=request`. The handoff contains the point in its first line, the context and desired answer, and optional transcript addresses for longer evidence. It conveys selected material rather than copying the sender's entire model context. `runSend` resolves the calling session, constructs a request carrying sender, recipient, body, intent, reply linkage and refs, and returns a receipt or refusal. The local daemon resolves the recipient, requires a live sender, and stores an envelope in SQLite. The initiator owns the question; Flopwire owns transport admission and bookkeeping. SRC-1: `cmd/flopwire/bus.go`, `internal/devicebus/local.go`; [RT-RTE-hook-delivery](runtime.md#rt-rte-hook-delivery).
3. **Deliver into the recipient's next eligible context.** The hook route leases pending messages, inserts standing instructions and bounded message text, then confirms after writing output. The renderer preserves sender/intent/identity attributes, escapes body markup, and supplies a concrete reply call. Body clipping carries an inbox-thread recovery hint; refs carry excerpts or addresses and a full-read hint. Thus receipt of the wrapper does not establish receipt of every evidence passage. The recipient must recover decisive clipped material before relying on it. SRC-1: `internal/busrender/busrender.go`, `cmd/flopwire/hook.go`; [RT-RTE-hook-delivery](runtime.md#rt-rte-hook-delivery).
4. **Act and return an answer.** Standing guidance asks the receiving model to treat an own-user message as a teammate request within existing permissions. It asks the recipient to reply through `flopwire_send` addressed to the original sender with `reply_to` equal to the request ID. The local bus looks up that parent and carries its thread ID into the reply. The recipient's task reasoning, tool use and verification are controlled by its external harness and task instructions; this source path does not establish that a request was obeyed or its answer tested. SRC-1: `internal/busrender/busrender.go`, `internal/devicebus/local.go`; [RT-BAP-message-guidance](runtime.md#rt-bap-message-guidance).
5. **Inspect and close.** The reply reaches the requester through the same delivery mechanism at an eligible event. The requester can reread the inbox/thread and must inspect content to decide whether the answer satisfies its question. A send receipt or read state is insufficient. The skill provides `intent=done` for closing a thread; sending it expresses closure, while the MCP receipt explicitly disclaims verified task completion. Delivery of an answer into the requesting context is the coordination result; acceptance of the work and a final user-facing product remain the requesting agent's responsibility. SRC-1: `plugins/codex/flopwire/skills/messaging/SKILL.md`, `cmd/flopwire/bus.go`; [WF-RTE-request-reply](#wf-rte-request-reply).

Recovery has distinct owners. If hook output fails or confirmation is late or fails, the hook leaves the delivery unconfirmed; lease expiry permits another offer. The renderer marks repeated attempts and the standing instruction asks the model not to repeat work when the ID is already in context. That is best-effort recovery plus model guidance, not an exactly-once task-execution guarantee. The requester follows arrival guidance instead of polling: an idle recipient requires resumption, and cloud recipients cannot reply through this mechanism. Those are alternate-path limits, not evidence that a busy local recipient necessarily answers. SRC-1: `cmd/flopwire/hook.go`, `internal/busrender/busrender.go`, `cmd/flopwire/bus.go`; [RT-RTE-adapter-delivery](runtime.md#rt-rte-adapter-delivery).

A concrete rejection path is replying to a parent whose intent is `done`. `checkLocal` returns `reply_to_done`; `sendLocal` records this refusal and returns its message ID. The CLI/MCP refusal renderer instructs the sender to start a new thread without `reply_to` if there is new work. Duplicate and rate checks can also refuse admission; they do not judge the answer's correctness. A rejected answer is therefore not automatically revised or reassigned. Software explains transport recovery; agents or their users decide the next task step. SRC-1: `internal/devicebus/local.go`, `cmd/flopwire/bus.go`; [WF-RTE-request-reply](#wf-rte-request-reply).

Added SRC-1 inspection in this member covers the complete Codex messaging skill, local `sendLocal`/`checkLocal`, `runSend`, refusal rendering and `sendMCPNext` in `cmd/flopwire/bus.go`, message rendering/frame construction, and hook output/confirmation. Skill text supplies doctrine/design; executable branches supply implementation. No target code, tests, evaluator or model was run. The baseline supplies other transport and enrollment paths; this workflow does not establish identical semantics for every backend, reliable task completion, answer quality, or autonomous end-to-end delivery to a user.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-request-reply
Label: Local request and correlated reply

This route joins history-led recipient choice, task handoff, reply correlation and requester acceptance. It overlaps [RT-RTE-history-retrieval](runtime.md#rt-rte-history-retrieval) for evidence recovery and [RT-RTE-hook-delivery](runtime.md#rt-rte-hook-delivery) for transport. Its distinct referent is the multi-call request/answer protocol, which spans both rather than being part of exactly one. No new transport component or message store is asserted. Endpoints are the initiating and receiving own-user sessions; progression is selected evidence → explicit request → eligible hook → recipient work → correlated reply → requester inspection/optional closure. The agent owns each task decision; daemon and hooks own admission, envelope state and insertion. Body/answer prose is natural-language content; IDs, intents, thread linkage and SQLite envelope state are symbolic. SRC-1: `plugins/codex/flopwire/skills/messaging/SKILL.md`, `cmd/flopwire/bus.go`, `internal/devicebus/local.go`, `internal/busrender/busrender.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Each send returns a receipt or refusal; an answer is a separate received message, not the synchronous send result.
- Later read-back: Inbox/thread calls reread retained messages; attached transcript addresses allow separate history reads. Retention can limit later recovery.
- Delegated visibility: Selected body, sender/intent attributes and bounded refs enter the recipient context; neither full sender context nor host permissions is transferred.
- Selection predicate: Agent establishes the historical owner, checks exact-session presence when needed, and explicitly chooses recipient and request intent; daemon resolves and admits the local send.
- Invalidation or expiry: Envelopes carry expiry; unconfirmed leases can be reoffered; a reply to a done parent is refused. An intent label does not invalidate an earlier answer's factual content.
- Activation or effect: Stores and renders requests/replies and enforces local linkage/admission checks; action on the delegated task and correct use of evidence remain unobserved.
- Evidence limits: This traces local own-user coordination and shipped model guidance. It supplies no actual exchange, answer-quality result, exactly-once execution guarantee or universal server/cloud semantics.

Operating mode: open coordination requests, not a bounded improvement trial. The initiating agent proposes a question and selects the recipient; the recipient proposes an answer; the requester decides substantive adequacy. Authorized users constrain action, while software can veto invalid, duplicate, over-limit or done-parent sends. No expected-answer oracle is present in this traced protocol. A `done` message closes coordination by declared intent; it does not run a product verifier. No theory revision or production-machinery admission is claimed.

The skill explicitly supplies the request's content contract:

> Put the point in the first line, which is the preview. Include the context the recipient needs and the answer you want. Attach transcript addresses in `refs` for longer evidence. Use `intent=request` for an answer, `inform` for an update, and `done` to close a thread.
> --- `plugins/codex/flopwire/skills/messaging/SKILL.md`

Its acceptance rule preserves human/model interpretation after correlation:

> `read` means the text entered the recipient's context; a received message whose `reply_to` names your request is a reply; inspect its content to determine whether it answers the request.
> --- `plugins/codex/flopwire/skills/messaging/SKILL.md`

The local rejection and operator recovery are implemented separately:

> return fail(http.StatusConflict, busproto.CodeReplyToDone, "%s closed its thread (intent done); it must not be answered", in.replyTo), nil
> --- `internal/devicebus/local.go`

> e.Fix = "do not answer it: done closes a thread. If there is new work, start a new thread without reply_to"
> --- `cmd/flopwire/bus.go`

The hook's recovery contract is bounded by its output/confirmation mechanism:

> // does not confirm, and a confirmation that fails is not retried: either
> // way the lease ends and they come again (messages marked).
> --- `cmd/flopwire/hook.go`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-hook-delivery](runtime.md#rt-rte-hook-delivery)

Workflow role: carries both the initial delegation and the returning answer. Its print/confirm boundary establishes transport progress, with lease-based recovery, rather than acceptance of the delegated work. The requesting agent owns answer inspection after a correlated return. Within this route, recipient context is bounded and recoverable through explicit reads; the external harness owns scheduling and the agent's wider context.
