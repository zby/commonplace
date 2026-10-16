---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenClerk workflow tracing an auth-callback session artifact through read-only planning, duplicate review and separately approved document delivery."
run-id: AAS-2026-10-16-openclerk-ec0e00c2bb0a-01
reviewed-boundary: "092fb98d243c2d9d95867ad04618ebce88983552"
---

# OpenClerk workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is the shipped **agent session to repository knowledge** example: an external coding agent obtains context, completes auth-callback work, submits a session note, reviews proposed knowledge changes, and separately requests an approved document write. It is selected because the repository supplies both a concrete handoff artifact and a matching planning command. This is a source-supported workflow, not an observed successful execution. The example ends at planning; its durable-write continuation is supported by the agent contract and the runtime's document route, not by an example run receipt (SRC-1, `examples/knowledge-packs/agent-session-to-docs/commands.md`, `docs/agent-contract.md`; [RT-RTE-document-write](runtime.md#rt-rte-document-write)).

The handoff says that retryable renewal errors were introduced while preserving state validation. It suggests updating a source note or adding a decision, and leaves update-versus-new unresolved. Those are fixture assertions, not independently verified facts about application code (SRC-1, `examples/knowledge-packs/agent-session-to-docs/handoffs/session.md`).

> ## Possible Doc Updates
> - Update the auth callback source note with retryable renewal error behavior.
> - Add a short decision note if this becomes policy for all callbacks.
> --- `examples/knowledge-packs/agent-session-to-docs/handoffs/session.md`

### Request, execution and consequential handoffs

1. **The user delegates application work to an external coding agent.** The shipped contract directs the agent to inspect readiness, obtain a context pack and read cited evidence before working outside OpenClerk. The host owns tool selection, model reasoning and application verification; OpenClerk does not schedule those steps. Context selection is the deterministic route [RT-RTE-context-pack](runtime.md#rt-rte-context-pack), not a delegated subagent. Its returned snippets and decision summaries are evidence selections, not proof that the application task was completed correctly (SRC-1, `docs/agent-contract.md`, `internal/chronicler/chronicler.go`).

2. **The external caller supplies explicit after-work evidence.** The example invokes `clerk run --once` with the session Markdown path, a task asking to summarize completed auth-callback work, and limit 5. `RunOnce` enables inbox planning and context construction. Within `runPlan`, inbox processing precedes context-pack construction; the example's expectation that context is cited before planning is not the function's execution order. The separate pre-work context request comes from the agent contract. These should not be conflated (SRC-1, `examples/knowledge-packs/agent-session-to-docs/commands.md`, `internal/chronicler/chronicler.go`, `docs/agent-contract.md`).

3. **Chronicler delegates a bounded data-processing task to the document runner.** It resolves supplied text paths, checks existing storage, and calls artifact planning for each file with `LocalPath`, `ArtifactKind: "note"` and a bounded limit. It does not pass the task text as a request to an authoring model. The internal handoff is a Go call, not an independent model worker. The planner derives title, candidate path, metadata and body preview from explicit content, then checks duplicate evidence. [WF-RTE-artifact-plan](#wf-rte-artifact-plan) records this material part of [RT-RTE-session-plan](runtime.md#rt-rte-session-plan) (SRC-1, `internal/chronicler/chronicler.go`, `internal/runner/artifact_candidate_plan.go`).

4. **Chronicler returns selected planning fields to the host.** It converts the full plan into an inbox candidate: proposed title/path, tags, compact body summary, local source references including a content hash, duplicate status, approval boundary and serialized next-create request. Pending review holds source reference, proposed path and recommended action. The body preview is therefore not delivered as a full standalone preview field in this conversion; when a next-create request exists, its serialized body can carry the proposed content. The nested planner handoff is not copied wholesale. These transformations limit what the external agent can judge from each returned field (SRC-1, `internal/chronicler/chronicler.go`, `internal/runner/artifact_candidate_plan.go`).

> Summary:           compactSummary(plan.BodyPreview),
> --- `internal/chronicler/chronicler.go`

5. **The external agent/user owns substantive acceptance.** The returned plan recommends review and approval, or resolving a duplicate first. It does not decide whether the auth-callback change warrants a new policy note. Neither the duplicate heuristic nor the confidence label is an oracle for correctness of that claim. Human approval is requested by the contract; actual approval and host compliance are unobserved. In particular, the runner's permissive default approval mode means that receiving a write request is not proof of a distinct human approval event ([RT-CLM-approval-boundary](runtime.md#rt-clm-approval-boundary); SRC-1, `docs/agent-contract.md`, `internal/runner/artifact_candidate_plan.go`).

6. **Delivery has two different endpoints.** Planning is delivered when the CLI returns its read-only envelope with candidates, context, pending review and blockers. Durable knowledge delivery requires a separate lifecycle request, admitted and executed through [RT-RTE-document-write](runtime.md#rt-rte-document-write). That route writes canonical Markdown and then synchronizes derived state, allowing later context retrieval. A planning result, approval request or next-request string is not a document receipt. No supplied execution evidence establishes that this example reached a write or influenced a later answer (SRC-1, `internal/chronicler/chronicler.go`, `internal/infra/sqlite/documents.go`).

### Rejection and recovery

A rejected per-file runner result becomes a blocker and processing continues to other files. A missing plan similarly becomes a blocker. A returned Go error instead aborts the call. Missing storage and unreadable/unsupported inbox inputs have their own blockers; an existing database and a readable Markdown/text artifact are prerequisites, not automatically repaired by this read-only workflow (SRC-1, `internal/chronicler/chronicler.go`).

> if taskResult.Rejected {
>     result.Blockers = append(result.Blockers, fmt.Sprintf("%s: %s", sourceRef, taskResult.RejectionReason))
>     continue
> }
> --- `internal/chronicler/chronicler.go`

For duplicate review, the planner uses the first returned search hit as a likely duplicate, not a semantic equivalence judgment. A likely duplicate suppresses the generated create request; Chronicler recommends resolving the duplicate before writing. The external caller must choose an existing-document update, revise the proposal, or abandon it. There is no automatic retry-to-write or persisted approval queue in this inspected chain. If a later write fails after canonical file creation, recovery must account for a potentially written file and incomplete synchronization; the runtime route does not promise transaction-wide rollback ([RT-RTE-document-write](runtime.md#rt-rte-document-write); SRC-1, `internal/runner/artifact_candidate_plan.go`, `internal/chronicler/chronicler.go`).

### Added inspection coverage

Added SRC-1 implementation coverage: `internal/runner/artifact_candidate_plan.go` planning construction, duplicate search, confidence, create-request gating and handoff construction; `internal/chronicler/chronicler.go` inbox validation, per-file rejection, plan-to-candidate conversion and ordering. Added doctrine/design coverage: the example command and session artifact plus `docs/agent-contract.md`. No source execution, tests, provider calls or new experiments were performed. This trace does not establish successful agent compliance, application-test success, content accuracy or knowledge benefit.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-artifact-plan
Label: Artifact candidate planning

Part of: [RT-RTE-session-plan](runtime.md#rt-rte-session-plan)

This is the internal artifact-planning part of the supplied session route, not a second identity for that entire route. Endpoints/progression: explicit local session file → artifact inspection → derived candidate fields → duplicate search → confidence and next-create gating → full plan consumed by Chronicler's conversion. Owner: deterministic runner code; the external agent/user retains the substantive acceptance decision. State/effects: source artifact and existing search state are read; symbolic candidate metadata, natural-language preview and serialized request are returned without applying the document change. SRC-1, `internal/runner/artifact_candidate_plan.go`, `internal/chronicler/chronicler.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: full candidate plan, including body preview, duplicate evidence, confidence, approval boundary and optional next-create request, to Chronicler.
- Later read-back: inapplicable — this planning part retains no candidate as durable knowledge; a separate document write is required.
- Delegated visibility: planner sees the explicitly supplied local artifact and search results; Chronicler passes selected candidate fields, compact summary and optional serialized create request to the host.
- Selection predicate: explicit note artifact; duplicate query defaults to title plus up to 24 body words; default search scope is the candidate's directory, and the first hit is treated as likely duplicate.
- Invalidation or expiry: returned plan is a snapshot; no persisted approval or automatic revalidation on later write is established here.
- Activation or effect: code produces a proposed request or withholds it; neither output applies the candidate or establishes model reliance.
- Evidence limits: implementation inspection only; a search miss does not establish global novelty, and confidence does not verify claim truth.

The trigger is the explicit session artifact. Code proposes candidate content; code can withhold a convenient create request when required fields are missing, confidence is low, or duplicate evidence exists. This is a proposal gate, not a universal veto against a caller constructing another write request. Human review and update-versus-new choice remain external. There is no reference-answer oracle in this open intake mode. Guidance is the contract's explicit-artifact, review-before-write procedure; persistence of approved content occurs only through the separate lifecycle route. Recovery is correction/replanning or choosing an update rather than create, not rollback of a planning mutation (SRC-1, `docs/agent-contract.md`, `internal/runner/artifact_candidate_plan.go`).

> if candidatePath == "" || title == "" || body == "" || confidence == "low" || likelyDuplicate != nil || existingSource != nil {
>     return ""
> }
> --- `internal/runner/artifact_candidate_plan.go`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-session-plan](runtime.md#rt-rte-session-plan)

Workflow role: delivers a planning result, not the completed knowledge write. The newly inspected internal part is [WF-RTE-artifact-plan](#wf-rte-artifact-plan). Per-file rejection is returned as a blocker while other files can proceed; the external caller owns corrective resubmission. The session task informs the accompanying context request, whereas each internal candidate request is supplied the explicit file and note kind rather than a task-conditioned model-writing instruction.

#### On [RT-RTE-document-write](runtime.md#rt-rte-document-write)

Workflow role: the separate durable-delivery endpoint after external acceptance. Its result must be distinguished from the session planner's zero-write envelope. The workflow cannot infer human approval from a successful mode check, or an unchanged vault from an error after the canonical-file write.
