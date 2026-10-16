---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SAGE workflow account: exact-local agent request, passive inspection, session-owned claim, reply and sender-side result retrieval."
run-id: AAS-2026-10-15-sage-d3843de6d2dd-01
reviewed-boundary: e2e0242a421afbd356ed135d7d754a35b0ad5f14
---

# SAGE workflow report

## Workflow account

### Selection and evidence boundary

This account selects the shipped canonical same-node Messages exchange: one agent sends work to an exact recipient, the recipient inspects and explicitly claims it, performs work in its external host, replies, and the sender retrieves the result. It is representative because it exposes consequential coordination decisions beyond the memory API's recall/store cycle: receiving a request is not accepting it, a claim belongs to a runtime session, and completion is distinct from reading a result. The route is [WF-RTE-local-exchange](#wf-rte-local-exchange). It is an implemented protocol for coordinating external agents, not an observed successful research, coding or review run. No concrete task transcript or task-quality outcome was inspected.

The boundary remains SRC-1 at the frozen commit. Added implementation inspection covers `internal/mcp/tools.go` send, explicit claim, handoff, reply and reply-page functions; `api/rest/messages_handler.go` local send/reply handlers; and `internal/store/messages.go` send transaction, claim handoff and reply transaction, plus `internal/store/message_inbox.go` pending-page and exact-claim logic. Tool descriptions in `internal/mcp/tools.go` also supply doctrine/design. These are available paths within the registered source, not new sources. Federation transport, legacy provider completion, task-board assignment and workflow-journal APIs are not traced as substitutes for this selected workflow. Their coexistence does not establish parity with its checks.

### 1. The requesting agent supplies a bounded message, not an execution grant

The external requesting agent decides what to ask and whom to ask. `sage_message_send` requires `to`, `payload` and a caller-generated `idempotency_key`; `intent` and an explicit TTL are optional. MCP resolves the target through signed `/v1/pipe/resolve`. For the selected local branch it rejects a provider-only target and posts to `/v1/messages`. The supplied context is the intent and payload, not an automatically copied caller conversation, filesystem or tool-access grant. Source: SRC-1, `internal/mcp/tools.go`.

> if resolved.ToAgent == "" || resolved.ToProvider != "" {
> 		return nil, fmt.Errorf("canonical messages require one exact local agent target")
> 	}
> --- `internal/mcp/tools.go`

REST checks an exact nonce-bound agent proof, input bounds, local directory membership and current active ordinary-agent enrollment of the recipient. It derives sender identity from request context. The SQLite store binds the request fingerprint and message ID to the sender and key in one transaction with the inbox insert and recipient wake-sequence advance. An identical retry returns the prior row; reusing the key for different message content conflicts. Notifications occur after the durable send and are best-effort acceleration, not delivery authority. Source: SRC-1, `api/rest/messages_handler.go`, `internal/store/messages.go`.

> // Wake metadata is published only after SendLocalMessage has committed the
> 		// inbox row, idempotency binding, and exact-recipient sequence together.
> 		// It is best-effort process-local acceleration; durable catch-up remains
> 		// authoritative across a crash between this return and publication.
> --- `api/rest/messages_handler.go`

The immediate acknowledgement means delivery to the local inbox, not recipient attention or acceptance. The recipient can be offline. Default retention is described by the handler as email-like; callers may instead supply a bounded TTL. No SAGE-owned conversational worker is launched by this send. Source: SRC-1, `api/rest/messages_handler.go`, `internal/mcp/tools.go`.

### 2. Inspection and explicit acceptance are separate handoffs

The receiving agent discovers pending requests through passive inbox inspection. The store selects pending, unexpired rows addressed to the caller, orders by creation time and immutable ID, and returns bounded pages with a client-held continuation cursor. In this selected exact-local route, the recipient identity is already fixed by the message. Provider-addressed compatibility rows use additional rules and are not evidence for exact-local identity guarantees. Source: SRC-1, `internal/store/message_inbox.go`.

The tool contract directs the recipient to verify current user/task authorization before accepting. That is guidance to the external agent, not proof that it performs that check. Authentic sender identity establishes provenance, not authority to issue user or system instructions. The runtime's [RT-BAP-client-guidance](runtime.md#rt-bap-client-guidance) supplies the retained source passage for this trust boundary; no second behavioral-authority record is needed.

To accept, the recipient calls `sage_message_claim(message_id)`. MCP first inspects that exact ID under its claimant session, checks the returned ID/passive flag, and then sends the explicit claim. SQLite atomically changes ownership and inserts the session receipt. Same-session retry is idempotent; an existing sibling-session claim fails. MCP verifies the returned ID, session and claimed status before telling the agent to complete the request. Local read acknowledgement follows the successful claim and may report a separate confirmation error. Source: SRC-1, `internal/mcp/tools.go`, `internal/store/message_inbox.go`.

> // ClaimInboxMessage claims only the named row, atomically with the session
> // fence. Retrying the same claim is safe; another session cannot take it.
> --- `internal/store/message_inbox.go`

Thus inbox delivery, passive visibility, explicit responsibility and read confirmation are distinct events. The tool description permits authorized dismissal through `sage_message_close` without a reply, but that alternate terminal route's store implementation was not traced here. Its presence does not imply that every request must be answered. Source: SRC-1, `internal/mcp/tools.go`.

### 3. The external recipient owns task execution and content verification

After a successful claim, the receiving model and its host own the actual research, review or other requested work. The inspected messaging route has no intermediate plan, tool-execution evaluator or task-answer oracle. It carries natural-language intent, request and result, while deterministic code manages symbolic identities, revisions and states. Neither a claimed request nor a completed row proves the requested investigation occurred. Source: SRC-1, `internal/mcp/tools.go`, `internal/store/messages.go`.

The sender supplies the task's requested purpose; the recipient decides whether to act under its current authorization. SAGE can reject protocol actions through identity, size, lifecycle and session checks. It does not grade whether the returned result satisfies the natural-language request in the inspected local reply transaction. In particular, the optional memory judges in [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) govern a different admission mechanism. Their presence cannot be imported as verification of Messages results. No per-result human approval or model judge is coded into this selected reply path. Source: SRC-1, `api/rest/messages_handler.go`, `internal/store/messages.go`.

### 4. Session rejection and recovery preserve ownership

On the normal MCP path, `sage_message_reply` includes the current claimant session with the result. For a new exact-local completion, the store checks prior fetch evidence, recipient ownership, local scope and the supplied session before completing the original message and recording the result fingerprint/read receipt transactionally. An identical recorded result can be replayed; a different second result conflicts. Importantly, raw `ReplyLocalMessage` checks the local session fence only when a nonempty session was supplied, and its already-completed exact-local replay branch does not reapply that fence. The session protection described here is therefore scoped to new completion through the inspected MCP path, not a universal API invariant. Source: SRC-1, `internal/mcp/tools.go`, `internal/store/messages.go`.

A sibling session's attempted new reply receives a typed HTTP 409, not a generic not-found response. This matters because a not-found route can trigger compatibility fallback; the denial must not silently become a less constrained completion attempt. MCP propagates canonical denials and warns against creating a substitute send without independent authorization. Source: SRC-1, `api/rest/messages_handler.go`, `internal/mcp/tools.go`.

> writeProblemTyped(w, http.StatusConflict, messageClaimSessionProblemType, "Claimed by another session",
> 				"Another session of this agent holds this message's claim. Use sage_message_handoff to take it over, or reply from the claiming session.")
> --- `api/rest/messages_handler.go`

Recovery belongs to the external recipient agent, not an automatic takeover scheduler. The tool contract offers passive `claimed_elsewhere` history and an explicit `sage_message_handoff` after judging the prior runtime stale. The code sends the expected old session and revision with the new MCP session. The store compares both and increments revision transactionally; repeating the exact successful transfer is recognized, while stale transfers conflict. The code fence verifies ownership history, not whether the old worker is actually dead or whether its external side effects have stopped. Source: SRC-1, `internal/mcp/tools.go`, `internal/store/messages.go`.

> if current != fromSessionID || currentRevision != expectedRevision {
> 			return ErrMessageReceiveConflict
> 		}
> --- `internal/store/messages.go`

This recovers coordination state; it is not rollback of shell commands or other effects already performed by the external host. A failed or lost reply response calls for reconciliation or exact retry, not invented new work. No observed failure/recovery execution is supplied.

### 5. Completion and delivered result have different endpoints

A successful local reply returns `status: completed`. This records the recipient's answer; it does not establish that the sender has consumed it. The sender reads replies through `sage_message_replies` or inbox reply items. The explicit pager calls signed `/v1/pipe/results`, applies an inclusive client-side `since` filter and uses a composite completion-time/message-ID continuation cursor. The client must finish the catch-up pages before advancing its saved inbox watermark. Status alone is deliberately payload-free. Source: SRC-1, `api/rest/messages_handler.go`, `internal/mcp/tools.go`.

The returned item labels the result as untrusted data with no reply obligation, attributes the actual `replied_by` identity rather than assuming the addressee wrote it, and truncates long results while returning a route to fuller content. Consequently delivery through the result tool means a labelled, potentially shortened result reached the calling context—not that the entire result was visible or accepted. Source: SRC-1, `internal/mcp/tools.go`.

> if runes := []rune(result); len(runes) > maxReplyResultRunes {
> 		result = string(runes[:maxReplyResultRunes])
> 		truncated = true
> 	}
> --- `internal/mcp/tools.go`

The selected protocol reaches its source-supported terminal result when the answer is recorded and made available to the exact sender; tool consumption supplies a further delivery handoff. The external sender still decides whether the answer meets the task and how to report a final product to its user. That user-facing acceptance and delivery cannot be established from this source-only trace. This is not a missing SAGE executor: [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle) already identifies the external model as next-step owner after SAGE returns context.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-local-exchange
Label: Local agent exchange

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Send returns the durable message ID/status and replay flag; explicit claim returns session/revision ownership; reply returns completed/replay acknowledgement, not sender comprehension.
- Later read-back: Retained inbox/history rows, claim receipts and reply records support subsequent recipient recovery and sender result-tool calls, including across runtime sessions while retained and eligible.
- Delegated visibility: An exact recipient receives the supplied intent/payload through passive inspection and explicit claim; only returned result data crosses back through the sender's reply reader. No worker process or copied caller conversation is launched by the send code.
- Selection predicate: Exact local target resolution and active recipient, signed caller, sender-bound send key; pending/unexpired recipient rows for inspection, exact message/session for claim, ownership/fetch evidence and supplied session for new MCP completion, sender-scoped result paging.
- Invalidation or expiry: Explicit TTL and terminal lifecycle change eligibility; session/revision transfer invalidates an old claimant's new MCP completion. Identical send/reply retries recover prior results; different content under the same key or a different second reply conflicts.
- Activation or effect: Durable message, ownership and completion state transitions are wired; result delivery to model context is implemented. Task execution, model compliance, sender acceptance and changed downstream behavior remain unobserved.
- Evidence limits: Static implementation and tool-contract evidence only. Session checks are scoped to supplied-session new completion, not all raw API calls or completed replays. No complete federation, legacy-provider or user-facing task-delivery trace is established.

This route's endpoints are requesting external agent → signed local Messages service → exact receiving agent/session → recorded reply → sender's reply reader. The external agents own the work and acceptance decisions; deterministic service/store code owns durable sequencing. Context is natural-language request/result text; symbolic IDs, hashes, cursors and revisions constrain protocol actions. Storage is SQLite message and receipt state, not changed model parameters. Source: SRC-1, `internal/mcp/tools.go`, `api/rest/messages_handler.go`, `internal/store/messages.go`, `internal/store/message_inbox.go`; minimum passages and forcing-path analysis are retained in the Workflow account above.

The closest supplied records are [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle) and [RT-BAP-client-guidance](runtime.md#rt-bap-client-guidance). Distinct identity: this is the complete multi-call local request/claim/reply/retrieval protocol, not the turn function that can expose its inbox, and not the instruction channel governing interpretation. It is not wholly contained in either: standalone message tools execute send, ownership transfer and completion outside the turn cycle. [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) is also distinct: Messages completion is not ordinary memory-voter admission, and this account does not generalize legacy journal descriptions into canonical automatic memory writes.

Proposer: requesting agent supplies intent/payload; recipient agent supplies result. Decider/veto: current receiving agent decides whether to accept under its external task authorization; service/store reject inadmissible protocol transitions. Human contribution to particular requests/results is unresolved without a caller trace; the route does not require per-item human approval. Answer oracle: none in the inspected message handlers/store; identity and replay checks are not answer-quality tests. Operating mode: open agent requests, not a bounded experiment or curriculum. Triggers are explicit send, claim, reply and recovery calls. Persisted guidance is the request's stated purpose and content, not an automatically revised method. Recovery uses exact retries, passive reconciliation and revision-fenced claim transfer; it neither undoes external task effects nor establishes semantic correction. Source: SRC-1, `internal/mcp/tools.go`, `api/rest/messages_handler.go`, `internal/store/messages.go`.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-turn-cycle](runtime.md#rt-rte-turn-cycle)

Workflow role: its inbox phase is an opportunity to discover work, not automatic delegation acceptance or task execution. The selected Messages workflow continues through explicit claim, external execution, reply and sender result retrieval outside the single turn call. A successful recall/store cycle does not discharge a claimed message's reply obligation.

#### On [RT-BAP-client-guidance](runtime.md#rt-bap-client-guidance)

Workflow trust boundary: independent current-task authorization belongs before claim and before consequential external execution. Exact sender identity and durable delivery do not grant payload instructions higher authority. The selected message formatter's data-only result labels likewise leave sender-side evaluation outside protocol completion.
