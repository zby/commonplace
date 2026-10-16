---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Pi Posthorse workflow: save task state, admit a foreground reset, restore notes/history and return an answer, with rejection and retry limits."
run-id: AAS-2026-10-14-pi-posthorse-58b9647d2f29-01
reviewed-boundary: "307ef6bf05bc8bd8d718725761ffdf2f2ef72539"
---

# Pi Posthorse workflow report

## Workflow account

### Selection and evidence

The representative workflow is **save task state → request a fresh window → restore retained evidence → answer**. It is selected because one shipped SDK evaluator scripts the whole sequence and separately checks reopening the journal. It does not require joining unrelated capabilities. The source-supported rejection variant is a failed sibling tool followed by a new checkpoint request (SRC-1, `test/official.test.mjs`). This is an implementation/design account at the [boundary](boundary.md), not an observed execution. The evaluator uses scripted faux model responses; even a passing run would not demonstrate an autonomous model deciding to checkpoint or restoring task state correctly.

Independent inspection for this member covered SRC-1, `test/official.test.mjs` (the explicit-reset/resume scenario and failed-sibling retry scenario), `src/context-tools.ts` (complete), and `src/rollover.ts` (explicit-reset function and registration/turn-end handler). These add implementation and evaluator-design evidence, not observed operation. Other mechanisms below use the supplied runtime records and their retained passages.

### Request, preparation and handoff

Pi receives the user's task and owns foreground model execution and tool scheduling. Posthorse supplies request guidance, not a work scheduler: [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance) tells the model to keep concise notes and restore them after rollover. The selected evaluator starts with a request to save state and reset, then scripts one foreground batch containing a note write and a reset request (SRC-1, `test/official.test.mjs`):

> fauxToolCall("notes", {
> 	op: "write",
> 	path: "task.md",
> 	content: "DURABLE_NEXT_STEP",
> }),
> fauxToolCall("new_context", { handoff: "CONTINUE_HERE" }),
> --- `test/official.test.mjs`

The model is the content author and proposer. The notes executor publishes text under [RT-RTE-note-admission](runtime.md#rt-rte-note-admission); its write receipt establishes filesystem publication, not that the note describes completed work accurately. The reset executor receives readable continuation prose and the host-supplied callback identity. It checks fresh-window capacity before recording the request. Its tool response says requested, not delivered: [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset). No per-handoff human approval is required. Background work remains outside this foreground agreement (SRC-1, `src/context-tools.ts`).

### Admission and next-step ownership

At turn end, Posthorse matches a foreground result to an ID recorded by its own callback, clears the turn-local requests, and checks errors, abort state and capacity including pending input. The supplied reset record retains the sibling-error predicate and identifies the host contract. Posthorse decides whether to offer the draft; Pi decides its final commitment, persistence and scheduling. The draft retains the continuation prose while requesting removal of previous active conversation (SRC-1, `src/rollover.ts`):

> type: "compaction",
> summary,
> firstKeptEntryId: null,
> details: { posthorse: 1, reason: "explicit" },
> --- `src/rollover.ts`

This handoff is between successive foreground invocations, not delegation to a distinct worker. Posthorse neither launches agents nor gives this workflow a delegate completion barrier. Its host-mediated draft is [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft). A successful tool callback is not proof the draft committed; later handler behavior and host compaction semantics remain external conditions (SRC-1, `src/rollover.ts`; [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset)).

### Restoration, verification and delivery

The next invocation receives the handoff, regenerated guidance and current tools under the host projection contract. It does not automatically receive the note or original user turn. The evaluator explicitly checks this omission, then requests note retrieval and history search. Its intended assertions distinguish active input from recoverable retained content (SRC-1, `test/official.test.mjs`):

> assert.doesNotMatch(JSON.stringify(fresh), /RAW_ORIGINAL_OWNER|DURABLE_NEXT_STEP/);
> assert.match(textOf(toolResult(h, "notes")), /DURABLE_NEXT_STEP/);
> assert.match(textOf(toolResult(h, "history")), /RAW_ORIGINAL_OWNER/);
> --- `test/official.test.mjs`

[RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) owns selection and estimated-budget paging. Notes read restores task text; history search returns matching earlier-entry excerpts and identifiers, not necessarily the whole original turn. The selected evaluator does not script subsequent history reads or real-world verification. Request guidance asks the continuing model to verify live state before consequential work, but no task correctness oracle enforces that instruction: [RT-OBJ-context-guidance](runtime.md#rt-obj-context-guidance) and [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance) (SRC-1, `src/budget.ts`, `src/history.ts`).

The scripted terminal response is `Recovered.`. Delivery in this scenario means the host returns an assistant answer after retrieval, with a saved note and journal available for later use. It does not mean the underlying task succeeded. The evaluator also reopens the journal and compares reconstructed model messages; the boundary retains that passage. This is a persistence assertion in test source, not independent certification of the excluded host's persistence or a second model run after reopening (SRC-1, `test/official.test.mjs`; [boundary](boundary.md)). No actual run, model compliance, task benefit or recovery success was observed.

### Rejection and recovery

A failed sibling is a meaningful rejection path, not a content review. The rejection evaluator scripts `new_context` alongside a read of a missing note, expects the next response to address the failure, and then supplies a separate retry request. Its assertions require the old user input to remain available and the explicit boundary not to commit (SRC-1, `test/official.test.mjs`):

> assert.equal(toolResult(h, "notes").isError, true);
> assert.equal(boundaries(h).length, 0);
> assert.match(next, /BATCH_OWNER_INPUT/);
> --- `test/official.test.mjs`

The subsequent scripted checkpoint uses `SUCCESS_AFTER_FAILURE` and expects one committed boundary. Recovery ownership is the foreground model/user initiating another attempt; Posthorse does not repair the missing note or reuse the cleared authorization automatically. Declining the explicit draft is not rollback of completed sibling effects. Nor is it a global prohibition on compaction: the handler may still consider its separate automatic threshold fallback, outside the selected explicit-reset scenario (SRC-1, `src/rollover.ts`; [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery)).

An oversized handoff is rejected at the callback with guidance to save fuller state in notes and retry shorter. If newly queued input makes an initially admitted handoff too large, turn-end processing instead emits a visible deferred-reset message and leaves context unchanged (SRC-1, `src/context-tools.ts`, `src/rollover.ts`):

> "Posthorse reset deferred: queued messages leave too little room for the requested handoff. The current context is unchanged; process those messages, then request a shorter handoff.",
> --- `src/rollover.ts`

These checks accept protocol conditions, not the truth or completeness of continuation prose. The inspected enforcement point cannot guarantee background synchronization or a later handler's abort veto. The runtime records retain those limitations; they prevent interpreting this workflow as transactional task execution or unconditional safe recovery.

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

#### On [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

Workflow role: preparation for the selected foreground checkpoint. Note publication supplies a separately retrievable continuation artifact; it is neither the compaction draft nor its acceptance oracle. The selected evaluator pairs publication with reset admission but establishes no transaction spanning them (SRC-1, `test/official.test.mjs`).

#### On [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset)

Workflow role: transition between foreground invocations. Acceptance is two-stage: callback request admission followed by turn-end draft eligibility; final host commitment is a further external step. A rejected attempt requires another foreground request. The failed-sibling scenario scripts that retry rather than automatic repair (SRC-1, `test/official.test.mjs`, `src/rollover.ts`).

#### On [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval)

Workflow role: restore selected evidence after active context removal. The selected scenario scripts note read plus history search before an answer, not full transcript reload, delegate delivery or live-state verification. Its source assertions concern returned content and journal reconstruction, not task-success acceptance (SRC-1, `test/official.test.mjs`).
