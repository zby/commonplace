---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Synto workflow from raw Markdown through model compilation, human draft review, rejection recovery and publication."
run-id: AAS-2026-10-15-synto-eabcdcce3da2-01
reviewed-boundary: "91ac6a3681df0552b6c9baef159439c7ebd780c9"
---

# Synto workflow report

## Workflow account

The representative workflow is **compile raw Markdown, review a draft, optionally reject and recompile, then publish**. It is selected because it crosses Synto's central production and admission boundaries without joining unrelated capabilities. The implementation supplies this sequence; no supplied execution trace establishes that a particular draft completed it. All source findings use SRC-1 at the frozen commit. Additional inspected implementation scope is `src/synto/cli.py` (`run`, `review`, `_review_single`), `src/synto/pipeline/orchestrator.py` (stage sequencing), `src/synto/pipeline/compile.py` (prompt construction, confidence, reduced-context recovery, publication and rejection), and `src/synto/state.py` (rejection retention and blocking). This is not an inventory of every Synto workflow.

### Request and model handoffs

1. **Operator to Python coordinator.** With Markdown already in `raw/`, the operator invokes `synto run` for a vault. The CLI loads configuration, model router and database, acquires the pipeline lock and supplies flags and a progress callback to the orchestrator. The ordinary route is [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run). Python, not a parent model, owns the next stage; lock ownership remains a cooperating-caller contract, not protection against every external edit (SRC-1, `src/synto/cli.py`, `src/synto/pipeline/orchestrator.py`).
2. **Coordinator to fast analysis.** Each eligible note is processed separately. Preprocessed source content and concept hints reach the fast endpoint; structured analysis, concept/source relationships and source summaries are retained. Hash and prompt-version checks can avoid duplicate work. Successful ingestion refreshes the index and supplies changed-source concept priorities to compilation. If those priorities are empty, the orchestrator can compile all eligible concepts instead. The handoff is retained database state, not a shared agent conversation ([RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run); SRC-1, `src/synto/pipeline/ingest.py`, `src/synto/pipeline/orchestrator.py`).
3. **Coordinator to heavy writer.** Compilation reconstructs a task-local prompt from the concept, budgeted source text, known article titles, vault conventions, at most 2,000 characters of the existing article, and up to three recent rejection feedback strings. It requests a structured `SingleArticle`, then Python repairs/sanitizes text and writes a draft plus database state. Pending drafts and manually edited published bodies normally prevent replacement unless forced. These model calls delegate content generation, not independent tool choice or publication authority ([RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run); SRC-1, `src/synto/pipeline/compile.py`).

### Checks and technical recovery

The orchestrator runs lint after its first compilation round and can create at most three broken-link stubs when fixing is requested. It then retries transient failures in a second round when allowed, and separately retries truncated concepts with the output soft cap lifted. Those recoveries are code-selected, not a critic agent revising a plan. Lint findings are reported but are not a universal publication veto; retries also occur after the initial lint stage. See the workflow annotation on [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) (SRC-1, `src/synto/pipeline/orchestrator.py`).

Within compilation, provider context overflow can trigger progressively smaller source budgets and smaller existing-article excerpts, eventually no existing text. Success marks the draft degraded. This recovery restores a parseable writing path by reducing evidence delivered to the model; it does not establish complete source coverage or accurate writing. The baseline's retained `prompt_degraded = True` passage supports this distinction ([RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run); SRC-1, `src/synto/pipeline/compile.py`). Unrecovered failures remain in the CLI report, including identification of incompletely compiled source notes (SRC-1, `src/synto/cli.py`).

### Human review, rejection and the next invocation

Without automatic approval, `run` ends with retained drafts and a report. A later `synto review` invocation provides the human decision interface described by [WF-RTE-interactive-review](#wf-rte-interactive-review). The reviewer can publish, stage without publishing, leave the draft, edit it, inspect a published-version diff, inspect a rejected-version diff, or reject it. The default single-draft action is publication, not a requirement to demonstrate verification first (SRC-1, `src/synto/cli.py`).

Rejection deletes the draft and its article record and, when its source binding is available, resets compilation state to pending. Nonempty feedback additionally stores the rejected body and feedback; an empty reason still rejects but does not add a feedback record. A later compilation reads up to three feedback strings and asks the writer to address them; it does not receive the rejected body through that prompt path. The stored body instead supports the human rejection diff. Thus recovery requires a subsequent compilation invocation and, for this manual branch, another human admission decision; rejection does not immediately launch a self-correcting agent ([RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication), [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance); SRC-1, `src/synto/pipeline/compile.py`, `src/synto/cli.py`).

Feedback-bearing rejections accumulate toward a cap of five, which blocks the concept; unblocking removes the block rather than clearing the rejection history. These are scheduling safeguards, not evidence that criticism was correct or successfully addressed (SRC-1, `src/synto/state.py`). The workflow annotation retains the relevant code passage. No theory-builder, improved-capacity or exercised self-improvement conclusion follows from storing feedback and requesting revision.

### Delivery and the automatic alternative

For the manual branch, publication writes the wiki destination, updates database state and only then deletes the draft. The review caller rebuilds the index and logs the approval. Delivery here means a published article available to later consumers, not proof of factual adequacy or downstream use. Ordering preserves the draft until preceding publication steps finish, but does not make filesystem and SQLite changes one atomic transaction ([RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication); SRC-1, `src/synto/pipeline/compile.py`, `src/synto/cli.py`). A prior published version can be inspected during review; general all-state rollback is not established by this path.

With automatic approval, the orchestrator directly submits this invocation's generated draft paths, optionally holds low-confidence drafts back, refreshes the index and reruns lint. Human review and verified status are not required. Confidence is computed from source count and the best source's quality classification, not a reference-answer comparison; its threshold cannot establish semantic correctness. Optional Git auto-commit can fail or be blocked while generated files remain on disk ([RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run), [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication); SRC-1, `src/synto/pipeline/orchestrator.py`, `src/synto/pipeline/compile.py`). The result is a staged knowledge-production workflow with a configurable human gate, not demonstrated reliable autonomous delivery.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-interactive-review
Label: Interactive draft review

Part of: [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication)

This is the CLI's human decision and inspection subroute within draft admission, not a replacement declaration for publication/rejection. Its distinct material responsibility is presenting drafts and routing human actions through `review` and `_review_single`. Endpoints are retained drafts and review metadata → human inspection/action → publication, verification, rejection, edited draft or unchanged deferral. Python owns display and dispatch; the human supplies the admission or rejection judgment. Operating mode is open-ended content review, not an experiment; there is no expected-answer oracle. Proposed content comes from the writer or human edits; the human can veto it by rejecting or leaving it, or publish it directly. Human review quality remains unobserved (SRC-1, `src/synto/cli.py`).

- Immediate return: Menu redisplay or exit, with action-specific messages; publication yields wiki files, staging retains verified drafts, and rejection removes drafts.
- Later read-back: Published or edited files survive for later consumers; nonempty rejection feedback and rejected bodies survive for later compilation guidance and reviewer diffs, respectively.
- Delegated visibility: The reviewer sees metadata, up to three previous feedback strings and an initial body preview limited to 3,000 characters; edit and diff actions offer additional inspection. The writer on a subsequent compile receives feedback strings, not this UI session or its full rejection-body history.
- Selection predicate: Human chooses a numbered draft or the first draft, or a batch action; a separate batch option selects verified drafts. Individual publication can bypass staging.
- Invalidation or expiry: Missing/unreadable drafts stop single-draft review; rejection deletes the candidate and resets bound source compilation state. A later invocation must produce the replacement. There is no demonstrated general rollback transaction.
- Activation or effect: Human action dispatches the mutation helpers; retained feedback is delivered on recompilation as revision guidance. Neither reviewer correctness nor model compliance is established.
- Evidence limits: Inspected CLI implementation and helper wiring only; no observed review, rejected article, editor session or accepted revision was supplied. The default preview does not establish that the reviewer inspected the entire body.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The preview limit and default publication action are explicit (SRC-1, `src/synto/cli.py`):

> body_display = body[:3000] + ("…" if len(body) > 3000 else "")
> --- `src/synto/cli.py`

> elif action in ("", "a", "p"):
> --- `src/synto/cli.py`

Recovery guidance is retained in the supplied [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance) passage. The reviewer does not have to supply feedback: `_review_single` prompts for a reason with an empty default and invokes `reject_draft` with it (SRC-1, `src/synto/cli.py`, `src/synto/pipeline/compile.py`).

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

Workflow ordering: initial compilation → lint/optional stub creation → transient retry → truncation escalation → optional approval → optional Git commit. Initial lint is not a rejection gate and is not rerun after retries on the non-auto-approval branch. After automatic publication the orchestrator explicitly runs lint again. Thus the displayed lint result should not be treated as proof that every final candidate passed a post-recovery check (SRC-1, `src/synto/pipeline/orchestrator.py`).

> transient = [f for f in round1_failed if f.reason == FailureReason.TRANSIENT]
> if transient and report.rounds < max_rounds:
> --- `src/synto/pipeline/orchestrator.py`

> if auto_approve and draft_paths and not dry_run:
> --- `src/synto/pipeline/orchestrator.py`

#### On [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication)

Workflow interpretation of the numeric acceptance gate: the compiler's confidence derives from source count and best source quality, not independent article verification (SRC-1, `src/synto/pipeline/compile.py`).

> best = _source_quality_summary(source_paths, db)
> return min(1.0, len(source_paths) * 0.25 + _QUALITY_BONUS.get(best, 0.0))
> --- `src/synto/pipeline/compile.py`

Rejection recovery has two separate effects: resetting bound source compilation state, and retaining guidance only when feedback is nonempty. The supplied route's deletion/reset account does not mean every rejection increments the cap (SRC-1, `src/synto/pipeline/compile.py`).

> if feedback:
>     db.add_rejection(title, feedback, body=draft_body)
>     count = db.rejection_count(title)
> --- `src/synto/pipeline/compile.py`

The cap is five; blocking occurs after recording feedback. Unblocking only deletes the block row, so retained feedback can still shape a next writer invocation (SRC-1, `src/synto/state.py`).

> _REJECTION_CAP = 5
> --- `src/synto/state.py`

> if self.rejection_count(concept) >= self._REJECTION_CAP:
>     self.mark_concept_blocked(concept)
> --- `src/synto/state.py`

> def unblock_concept(self, concept: str) -> None:
>     with self._tx():
>         self._conn.execute("DELETE FROM blocked_concepts WHERE concept = ?", (concept,))
> --- `src/synto/state.py`
