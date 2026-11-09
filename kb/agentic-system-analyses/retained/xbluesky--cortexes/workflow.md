---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Cortexes workflow account: bounded Raw distillation, human-admitted notes, inline broadcast, and later retrieval at the frozen revision."
run-id: AAS-2026-11-08-cortexes-af94078f2405-01
reviewed-boundary: "2b8e79f0099203e0453147b708346349952bb963"
---

# Cortexes workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is an explicit request to distill a saved Raw session, taking the `new` outcome through inline broadcast and eventual retrieval. It was selected because the shipped distill procedure explicitly connects bounded source review, human decisions, note creation, indexing, commits and a second maintenance procedure. This is a connected source-prescribed workflow, not a chain inferred from unrelated capabilities. The `pending-merge`, rejection and interruption branches clarify what delivery does and does not mean. Capture supplies the starting artifact through [RT-RTE-session-capture](runtime.md#rt-rte-session-capture); it is not repeated as a synchronous prerequisite of the distill request.

The account uses SRC-1 at the boundary's frozen commit. Direct inspection covered `skills/cortex-distill/SKILL.md`, `skills/cortex-broadcast/SKILL.md`, `skills/cortex-query/SKILL.md`, and the seal/completion functions in `cortex-vec/src/cortex_vec/distill_plan.py`. These add doctrine/design detail and implementation detail respectively under the existing source register, not a new source. No target execution, private vault or successful workflow trace was supplied. Instructions establish requested coordination; code checks establish only their named API conditions. Actual completion and benefit remain unobserved.

### 1. Request, queue and bounded review

The foreground Claude Code agent resolves the configured vault, obtains the unprocessed queue and asks whether to proceed. With multiple files, it proposes normal and oversized lanes for approval, processes one Raw at a time, and carries remaining work forward rather than opening everything. The queue is based on an authoritative header or terminal marker, not substring matches in conversation text. These selectors and the page ledger belong to [RT-RTE-distill-review](runtime.md#rt-rte-distill-review).

Starting a plan hands the CLI a Raw path and returns a plan ID. Subsequent map/span calls carry that ID and cursors or span identifiers. The foreground agent selects expansions from previews and lexical anchors; the code tracks emitted characters, source identity, reviewed ranges and coverage. A positive candidate can stop after recording evidence from already-reviewed ranges. A negative candidate needs the full-map and semantic/ambiguous-span coverage gate. This checks delivered coverage, not whether the model understood the source or whether the candidate is true. Full Raw reads are forbidden by the skill, not prevented by the host tool boundary.

No reviewing subagent is commissioned. The foreground agent remains the next-step owner and receives selected Raw text in its existing context. The plan cache retains accounting outside the context; it does not evict previously returned pages. On budget exhaustion, the prescribed recovery is a takeoff baton containing the plan ID and a fresh session that resumes accounting, not silent continued reading. The baton is a curated handoff rather than a transfer of the whole original conversation; its separate authority and limits are [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff).

### 2. Candidate, human veto and draft

The agent applies the symbol/mechanism/rationale heuristic and presents concrete excerpts with its candidate verdict. The human can agree, reverse the verdict or choose routine skip. A positive verdict then leads to a search using a dense insight passage, followed by a second human decision among new, pending merge and routine skip. Search thresholds shape recommendations, not final admission. There is no expected-answer oracle: excerpts, existing pages and human judgment supply evidence and selection, not an automated correctness proof ([RT-RTE-distill-review](runtime.md#rt-rte-distill-review)).

A search failure is explicitly recoverable as a preference for retaining the insight: propose `new`, record unavailable dedup evidence and still ask the human. The skill's assertion that every returned hit has measured cosine does not hold for all implementation fallbacks; [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) establishes that zero can encode missing cosine. Thus a low/zero score is not a demonstrated absence of duplication.

For `new`, the agent drafts a Notes or Projects page, presents the draft for confirmation and only then writes it. Pending merge instead records an intended existing target without creating or editing a page at this stage. The human supplies per-content decisions; merely starting distillation is not blanket approval. The corresponding interpreted-policy authority is [RT-BAP-plugin-guidance](runtime.md#rt-bap-plugin-guidance).

### 3. Seal, persist and hand off inline

Distill prescribes a note upsert, a human index update for new pages, an outcome log and a Raw marker, followed by a vault commit and optional configured push. It requires sealing before the marker, and completion after the commit. These are different notions of acceptance: draft approval admits content conversationally; seal records an expected outcome and checks negative coverage; completion checks the Raw's normalized source identity and matching outcome. Neither API attests that a note, upsert, log or Git commit succeeded. See the workflow annotations below for the exact checked boundary.

After the commit, new and pending-merge outcomes dispatch broadcast inline without another dispatch permission prompt. The agent announces the transition and remains in the same foreground context. The handoff supplies the Raw's outcome/target marker and passages already paged by distill; it does not create an isolated worker or copy all original source text. Distill's plan is already complete, so broadcast opens a new bounded plan if further passages are needed. SRC-1, `skills/cortex-distill/SKILL.md`, `skills/cortex-broadcast/SKILL.md`; [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit).

> **Inline mode** (dispatched by cortex-distill Step 9): the passages
>     distill paged in this session are already in context. Work from
>     them. Distill has completed its plan, so a passage you still need
>     comes from a plan opened as below.
> --- `skills/cortex-broadcast/SKILL.md`

### 4. Broadcast acceptance and partial recovery

Broadcast searches for related pages, drops the newly created page's own targets, and asks the human to choose destinations. Pending merge preserves the original target as preselected even if it falls below the current threshold. For new outcomes with no candidates, broadcast can finalize without editing any page. An empty confirmed selection similarly ends with no changes; neither terminal state establishes that new knowledge propagated ([RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit)).

For each selected page, the foreground agent reads its full content, expands any necessary Raw evidence, and shows exact before/after proposals. The user can accept, reject or request revisions. Contradictions produce a proposed inline flag or a user-directed rewrite; they are not mechanically adjudicated. Accepted accumulated changes are applied by targeted Edit, upserted and committed per page. Human approval is prescribed, not enforced by the CLI. This is content revision with no supplied amended theory or execution trace; the independent theory and improvement limits in the runtime record still apply.

Menu `quit` aborts without resolving the Raw. Mid-page `abort` discards that page's uncommitted proposals but preserves earlier committed pages. Recovery is a rerun of broadcast on the still-eligible Raw, not a transaction rollback across the session. Final success adds a broadcast/merged segment to the authoritative marker, logs actually committed pages and commits marker plus log. Any temporary broadcast review plan is cleared. Inline mode returns control to distill, which owns selection of the next Raw; standalone mode asks whether to continue. SRC-1, `skills/cortex-broadcast/SKILL.md`; [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit).

> Re-run /cortexes:broadcast <raw-path> to resume.
> --- `skills/cortex-broadcast/SKILL.md`

### 5. What counts as delivery

The prescribed local delivery is a confirmed new page or a recorded non-new outcome, associated index/log/marker updates and commits, followed by a resolved broadcast marker even when no related pages changed. Optional push is a separate remote-persistence step. There is no single inspected transaction spanning Markdown, Git and retrieval indexes; an outcome marker is not proof of all side effects. Capture itself also returns before its detached writer finishes ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture)).

A later explicit query is a separate request, not an automatic callback from distill. Search supplies ranked metadata/summaries first; a human-selected full-file read supplies detailed retained content. This closes the designed retention-to-consumption path without establishing actual behavioral dependence or improved answers ([RT-RTE-vault-search](runtime.md#rt-rte-vault-search)). SRC-1, `skills/cortex-query/SKILL.md`:

> If multiple matches, list them and ask which one to read
> --- `skills/cortex-query/SKILL.md`

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

#### On [RT-RTE-distill-review](runtime.md#rt-rte-distill-review)

Workflow verification boundary: the foreground agent owns recovery from plan rejection. Sealing's negative-coverage rejection does not reject unsupported positive insights. The supplied runtime passage establishes `NO_INSIGHT_COVERAGE_INCOMPLETE`; direct inspection additionally confirms that seal records status/expected outcome, whereas complete checks the normalized Raw hash and terminal outcome. It checks neither the new note nor external side effects. SRC-1, `cortex-vec/src/cortex_vec/distill_plan.py`:

> if outcome != state["expected_outcome"]:
>         raise PageError("RAW_CHANGED",
>                         reason="marker does not match sealed expectation",
>                         found=outcome, expected=state["expected_outcome"])
> --- `cortex-vec/src/cortex_vec/distill_plan.py`

The skill tells the agent to stop and report on `RAW_CHANGED`, not retry until accepted. This preserves the distinction between a procedural completion check and a quality oracle. SRC-1, `skills/cortex-distill/SKILL.md`:

> If it returns `RAW_CHANGED`, the Raw has changed beyond just the marker —
> stop and report, do not retry.
> --- `skills/cortex-distill/SKILL.md`

#### On [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit)

Workflow ownership: inline broadcast returns to distill after finalization; distill retains batch scheduling. No subagent isolation or independent reviewer is prescribed. Destination confirmation and per-change approval remain human decision points even though the handoff itself is automatic. Recovery after abort is partial: prior page commits stand, and an unresolved Raw can re-enter a future run. A completed broadcast with zero pages is a terminal bookkeeping result, not evidence of propagation or consistency. SRC-1, `skills/cortex-broadcast/SKILL.md`:

> Return cleanly to the distill flow when finalized —
>   do not prompt for next Raw; distill manages its own iteration.
> --- `skills/cortex-broadcast/SKILL.md`
