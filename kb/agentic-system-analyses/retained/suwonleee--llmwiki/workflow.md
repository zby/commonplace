---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "llmwiki workflow account: exact-session warm save through evidence paging, model filing, rejection recovery and checked close-out."
run-id: AAS-2026-11-08-llmwiki-7f7e35008c0f-01
reviewed-boundary: "e6be788bdfd969c3695f839a5d6b5752bb233cfc"
---

# llmwiki workflow report

## Workflow account

### Selection and evidence

The representative workflow is the human-present `/wiki-save` close-out, already identified as [RT-RTE-warm-save](runtime.md#rt-rte-warm-save). It is selected because it connects the system's ordinary knowledge-writing procedure to exact-session evidence selection, durable pages, deterministic checks and a user-visible result. It is not a composite of unrelated commands. Its governing procedure is SRC-1, `skill/wiki-save.md`; its executing model is [RT-CMP-host-model](runtime.md#rt-cmp-host-model), outside llmwiki's implemented scheduler. The optional unattended [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) has different proposal/verifier/publication gates and is not a hidden step in this workflow.

Evidence is source text at the [boundary](boundary.md), not an observed save. Additional direct inspection for this member covered all of `skill/wiki-save.md` and `src/engine/update-pages.ts`, incremental extraction and marking in `src/engine/update.ts`, and the `cmdSaveEvent` dispatch in `src/cli.ts`. These supply doctrine/design and implementation under SRC-1; they add no source identity, execution trace or benefit evidence. Supplied runtime records support the other mechanisms cited below. In particular, a requested model judgment is not evidence of compliance.

### Request and allocation of responsibility

The user invokes the save skill in the current host session. The foreground model owns the multi-step procedure; the engine owns identity resolution, extraction receipts, watermark transitions and deterministic utilities. There is no llmwiki worker-manager handoff here. The skill says to work inline with warm context and no subagent delegation. Its fallback instruction for a subagent asked for a long document is to write a scratchpad and return a path rather than a document body; that is an external-host context protocol, not an implemented scheduler ([RT-OBJ-save-skill](runtime.md#rt-obj-save-skill), SRC-1, `skill/wiki-save.md`).

The model first checks project conventions. A non-default team configuration overrides the default category table and review gates. Existing Q./A. review items are surfaced to the human, applied or discarded after answers, then deleted; engine-managed gap and semantic-review files must not be deleted in this step. Human confirmation, rather than the model's own confirmation, authorizes a direction item's human-verification stamp. This preliminary review is part of the shipped procedure, not evidence that every session has review items (SRC-1, `skill/wiki-save.md`).

### Exact-session evidence handoff

The model must obtain the harness-provided current session ID and pass it to `save-current`. The CLI resolves and enqueues that exact session, returning transcript paths. It must not substitute a recent pending session. The runtime establishes repository-bucket exclusion and the manual path's exemption from the passive 50-line capture threshold; therefore passive capture is useful preparation, not a necessary volume gate for this explicit save ([RT-RTE-warm-save](runtime.md#rt-rte-warm-save), [RT-RTE-passive-capture](runtime.md#rt-rte-passive-capture)).

The next handoff is CLI to model: `update-next` over only those returned paths supplies screened, fixed-snapshot pages starting at the queued watermark. The recorded source kind selects the parser. Interactive extraction requests whole turns without the ordinary character cap; each page groups up to twenty retained utterances. This is bounded by turn count, not necessarily by character volume. The model must follow the continuation until the issued offset becomes available, judge from the extract, and avoid loading the full transcript. A harness summary is draft material, not a replacement grounding source (SRC-1, `skill/wiki-save.md`, `src/engine/update.ts`, `src/engine/update-pages.ts`; [RT-RTE-warm-save](runtime.md#rt-rte-warm-save)).

This handoff deliberately changes what reaches the author: it supplies the screened parser output rather than every raw row. It does not establish transcript completeness or model comprehension. Mutated-root headers can advise filing into another repository's wiki while advancing the watermark in the original queue bucket. Code emits that warning; the model performs the reassignment (SRC-1, `src/engine/update.ts`).

### Authorship, admission and verification

The model selects useful human-expressed results, decisions and insights, classifies them and writes pages with ordinary host filesystem tools. Routine grounded decisions and insights become stable by model judgment, without per-page human approval. Actual direction shifts and unresolved contradictions go to review. The transcript of a direction shift remains pending under the procedure; ambiguous classification alone is not a reason to involve the human. Unsupported claims are omitted and noise may be marked skipped ([RT-RTE-warm-save](runtime.md#rt-rte-warm-save), SRC-1, `skill/wiki-save.md`).

The handoff supplies the model with the save policy, deferred writing/citation conventions and extracted evidence. Page claims require footnotes and verbatim evidence obtained through the excerpt command. After each page write the model must run page-scoped lint and fix errors. These are requested authoring and checking steps, not a universal interception of host writes. Lint can reject formal defects; transcript grounding and usefulness remain model judgments. There is no known-answer page oracle, no mandatory independent critic and no proof that a stable page is true ([RT-RTE-warm-save](runtime.md#rt-rte-warm-save), [RT-BAP-save-instructions](runtime.md#rt-bap-save-instructions)).

For a filed range, `update-done` checks the exact issued end offset, bounds and no rewind. Serving all pages sequentially enables issuance; issuance does not attest that pages were authored or understood. A successful mark consumes the receipt and clears the snapshot. This CLI check is narrower than the authoring policy (SRC-1, `src/engine/update.ts`, `src/engine/update-pages.ts`).

### Rejection and recovery

Two different failure classes must stay separate:

- **Identity failure:** if exact resolution fails, the procedure says to file nothing for this session, report the failure and continue. There is no nearest-session recovery. Completion remains unrecorded ([RT-RTE-warm-save](runtime.md#rt-rte-warm-save), SRC-1, `skill/wiki-save.md`).
- **Extract/offset rejection:** an out-of-order page request throws; a non-skipped mark without an issued receipt, with a mismatching offset or behind the current watermark is refused. The model must obtain/read the proper extract and submit its issued offset. Repeating page one reuses the fixed snapshot; appended source bytes belong to a subsequent increment. The engine preserves the boundary between one served range and later source growth, not a guarantee of saved knowledge (SRC-1, `src/engine/update.ts`, `src/engine/update-pages.ts`).

> if (page > pages.length || page > served + 1) {
> --- `src/engine/update-pages.ts`

> if (problem) throw new Error(`update-done refused: ${problem}`);
> --- `src/engine/update.ts`

`--skipped` deliberately bypasses the non-skipped receipt requirement after the basic bounds/no-rewind checks. It is a judgment of non-filing, not evidence of filing. Lint errors instead require author repair; unresolved citations must be fixed rather than removed. A secret-lint finding requires removing the secret value, not deleting the supported claim or its citation. None of these mechanisms provides automatic rollback of ordinary host edits. Recovery is foreground-model work, with human decisions for direction, and no completion event while exact resolution or final lint remains failed (SRC-1, `skill/wiki-save.md`; [RT-RTE-warm-save](runtime.md#rt-rte-warm-save)).

### Delivery and later consumption

Advancing the transcript is not the final delivery condition. The model next refreshes current-state's now/next and active rules, moving excess detail to a linked page rather than deleting it. It appends the engine-formatted log, then runs transcript registration, conditional OKF normalization, indexing, reconciliation and whole-wiki lint. Topic consolidation and overview rewriting stay outside this fast lane. The daemon sync is explicitly non-fatal; a database-health notice can recommend deep maintenance without authorizing repair here (SRC-1, `skill/wiki-save.md`).

Only after filing, L0/log and checks succeed should the model record the completed save event. That is a model-facing completion rule, not an engine proof of every preceding step; [WF-CLM-closeout-completion](#wf-clm-closeout-completion) captures this distinction. The user receives a short report of filed count, deferred backlog, L0 refresh, lint, feedback and maintenance/deep status. Backlog count is information, not a requirement to drain it before delivery. A failed or partial save must not be reported as a completed one (SRC-1, `skill/wiki-save.md`).

The durable output is project Markdown plus bookkeeping; future sessions can consume it through [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules). Those routes establish possible delivery, not subsequent obedience or improved task performance. No execution evidence here demonstrates that the final report was issued, the saved content was later activated or any task improved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-closeout-completion
Label: Whole-close-out completion policy

Claimed operation: the save skill permits a completed event only after filing, L0/log and deterministic checks succeed; enqueueing and range marking are explicitly insufficient. Source: SRC-1, `skill/wiki-save.md`, doctrine/design. Closest supplied record: [RT-RTE-warm-save](runtime.md#rt-rte-warm-save). This declaration isolates the source's completion claim rather than declaring a second execution route; it does not replace or duplicate that route's identity.

> `save-current` only enqueues, and `update-done` only advances a consumed range; neither proves the whole close-out succeeded.
> --- `skill/wiki-save.md`

The inspected event command checks enrollment and session/event argument form, then calls the event recorder. It does not itself run filing, L0 refresh or lint. Thus the observed code boundary supports a protocol to be followed by the host model, not an engine-enforced whole-save certificate (SRC-1, `src/cli.ts`). No actual completion event was supplied.

> if (!recordSaveNudgeEvent(ws, session, event as "completed" | "declined")) die("save event could not be recorded");
> --- `src/cli.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-warm-save](runtime.md#rt-rte-warm-save)

Workflow-specific acceptance boundary: the CLI can reject a malformed range without judging the authored knowledge. Conversely, it can accept a valid range before L0, log and final checks have succeeded. The workflow therefore has distinct range-consumption and whole-close-out milestones. The foreground model owns repair and truthful final reporting; successful offset advancement cannot substitute for the latter milestone. See [WF-CLM-closeout-completion](#wf-clm-closeout-completion).

Workflow-specific coordination: the shipped save procedure keeps authorship in the warm foreground context and defers backlog and topic work to deep maintenance. Its path-only scratchpad instruction does not establish that a worker was launched or that a host isolates the worker's context. Neither a multi-agent critic chain nor automatic rollback should be inferred from this route.
