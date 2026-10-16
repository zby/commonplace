---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Ars Contexta's source-to-note pipeline: serial delegation, verification, recovery and batch delivery at the frozen revision."
run-id: AAS-2026-10-12-arscontexta-f9e5f2f34166-01
reviewed-boundary: "2acfd5cc4473c4d06c46be63df748e77e00e2746"
---

# Ars Contexta workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is `/pipeline [source-file]`: admit a source, extract claims, create and connect notes, verify them, then archive the work records and report the result. It was selected because the shipped wrapper joins those steps explicitly and describes both interruption and final delivery. This is not a workflow assembled from unrelated capabilities. Its supplied baseline is [RT-RTE-source-processing](runtime.md#rt-rte-source-processing). The account traces the requested serial procedure, not a successful run. SRC-1: `skill-sources/pipeline/SKILL.md`.

> The pipeline is the convenience wrapper. /ralph is the engine. /seed is the entry point.
> --- `skill-sources/pipeline/SKILL.md`

Added inspection within SRC-1 covers the complete pipeline and ralph instructions; seed's source validation, duplicate decision, relocation, task/queue templates and return; reduce's findings/approval and per-claim handoff template; and verify's cold-read, retrieval and final chaining sections. These are doctrine/design at the boundary's frozen commit. No target procedure was executed. Claude Code's scheduling, actual generated skills, permissions and worker contexts remain outside the supplied execution evidence. Instructions request behavior but do not establish compliance.

### Request, source admission and extraction

The initiating user supplies a source path. The pipeline model reads domain vocabulary from the derivation manifest, falling back to derivation or universal terms. With no target, it lists inbox candidates and asks which to process. The wrapper invokes seed through Skill if available or follows seed directly. Seed validates file existence, checks previous processing by filename and content overlap, and asks the user whether to proceed when it finds a possible duplicate. Declining stops the workflow before new processing. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/seed/SKILL.md`; [RT-RTE-source-processing](runtime.md#rt-rte-source-processing).

Seed establishes the batch archive and extract-task file. Inbox sources move to the archive immediately; sources outside the inbox remain in place. The task file records the final source path, original path, scope, acceptance criteria and next claim number. This gives downstream workers a stable intended source reference rather than requiring a later link rewrite. The wrapper captures batch ID, archive path and numbering start. The queue carries scheduling metadata, while the task file carries source and work context; these have different roles even though both persist as files. SRC-1: `skill-sources/seed/SKILL.md`; [RT-OBJ-queue](runtime.md#rt-obj-queue).

The wrapper requests `/ralph 1 --batch {batch_id} --type extract`, directly or inside a Task call. Ralph is instructed to delegate extraction to another Task worker. That worker receives the extract-task path and identity, the source reference through the task file, `/reduce --handoff`, a one-phase constraint and a handoff requirement. Reduce presents findings and requires user approval before file creation; handoff mode adds task/queue production rather than waiving approval. This remains an integration tension with ralph's requested `dontAsk` worker mode, not evidence that human approval actually occurs inside the worker. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/ralph/SKILL.md`, `skill-sources/reduce/SKILL.md`; [RT-RTE-source-processing](runtime.md#rt-rte-source-processing).

Extraction prepares per-claim task files containing the claim, classification, source reference, extraction rationale, semantic-neighbor distinction and empty downstream phase sections. It also adds claim/enrichment queue entries. These files, not the worker's entire private reasoning, supply later phases. After extraction the lead rereads the queue to discover new work. However, the seed templates do not supply the fields used by ralph's stated extract filters; [WF-CLM-extract-selection](#wf-clm-extract-selection) records this additional instruction mismatch. The end-to-end account is therefore conditional on resolving selection rather than proof that the shipped templates automatically connect. SRC-1: `skill-sources/reduce/SKILL.md`, `skill-sources/seed/SKILL.md`, `skill-sources/ralph/SKILL.md`.

### Serial handoffs and coordination

For claim work, serial ralph selects the first pending entry after batch/type filtering. Each iteration constructs a phase prompt from task ID, target, task-file pointer and current phase; spawns a Task worker; waits for its return; parses a RALPH HANDOFF if present; advances the queue; and rereads/re-filters it. The lead owns the next-step decision and phase advancement, while the worker owns the requested note or graph edits. Fresh context is a requested host contract, not an inspected isolation guarantee. SRC-1: `skill-sources/ralph/SKILL.md`; [RT-RTE-source-processing](runtime.md#rt-rte-source-processing).

Create receives note-format constraints and updates the task's Create section. Reflect receives existing sibling titles from the same batch and requests topic-map plus semantic discovery. Reweave receives a freshly queried sibling list and requests links from older notes and siblings back to the new note. Verify receives the task pointer and the ordered quality-check instruction. Sibling lists contain titles of already-created notes, not necessarily their bodies. Later workers must read the referenced content to judge relationships. SRC-1: `skill-sources/ralph/SKILL.md`.

> **Build sibling list:** Query the queue for other claims in the same batch where `completed_phases` includes "create" (note already exists). Format as wiki links.
> --- `skill-sources/ralph/SKILL.md`

The count passed by pipeline is the number of pending claim/enrichment entries, but serial ralph uses each iteration for one phase and can reselect the same still-pending claim. With one newly extracted claim, a request for one serial iteration can finish create while leaving reflect, reweave and verify pending. The wrapper's separate completion check can stop archiving, but does not turn that count into whole-claim completion. This is the bounded integration issue already retained in [RT-RTE-source-processing](runtime.md#rt-rte-source-processing), not an observed stalled run. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/ralph/SKILL.md`.

Parallel ralph is not substituted silently for this serial path. It delegates remaining phases and queue completion to full-claim workers and waits for all returns, including errors, before cross-connect. That materially changes ownership and context lifetime; [RT-RTE-parallel-claims](runtime.md#rt-rte-parallel-claims) retains the distinction. SRC-1: `skill-sources/ralph/SKILL.md`.

### Verification, rejection and repair

Verify first predicts the note from title and description, then reads its body and scores prediction accuracy. It also requests vector retrieval, schema checking and per-note graph health. Retrieval can be explicitly deferred when semantic search is unavailable. The comparison tests discoverability and local structure, not the truth of the source claim; model judgment is not an independent expected-answer oracle. A prediction score below three or a FAIL-level issue is supposed to keep the task at verify for repair. SRC-1: `skill-sources/verify/SKILL.md`; [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate).

The ordered information restriction is consequential: the verifier cannot perform the requested cold-read test after first reading the body. The worker prompt preserves that order, but the source does not demonstrate that a host-loaded worker lacks prior knowledge of the note. SRC-1: `skill-sources/ralph/SKILL.md`, `skill-sources/verify/SKILL.md`.

> **CRITICAL: Do NOT read the full note yet. Only read frontmatter.**
> --- `skill-sources/verify/SKILL.md`

Ralph's return handling does not provide a hard acceptance gate. It permits continuing without a handoff and warns rather than rejects when a task section is empty. Its ordinary advancement instruction does not require parsing a PASS result before marking the last phase done. The contradictory verification/advancement policies are retained in [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate). Consequently, done state cannot alone establish successful quality verification. Post-Write warnings also cannot repair this gap: they occur after the effect, cover limited paths/tool matches and do not reject writes. SRC-1: `skill-sources/ralph/SKILL.md`, `skill-sources/verify/SKILL.md`, `hooks/hooks.json`, `hooks/scripts/write-validate.sh`; [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks).

The intended failure path is to report the failed phase/task and queue state, stop automatic continuation and let the user remediate and rerun ralph. Ralph describes a crashed worker as leaving the task pending at its current phase; that recovery assumes advancement has not occurred and does not undo partial note edits. A malformed queue stops processing without automatic repair. There is no demonstrated transactional rollback. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/ralph/SKILL.md`.

> **Queue corruption:** If the queue file is malformed, report the error and stop. Do NOT attempt to fix it automatically.
> --- `skill-sources/ralph/SKILL.md`

### Batch completion and delivered result

When all tasks in a multi-claim batch are done, serial ralph requests one additional cross-connect worker. Its input is the full list of note titles and paths recovered from task Create sections. It checks sibling and backward-link gaps that earlier phases may have missed because later sibling notes did not yet exist. This is a repair pass over the resulting graph, not independent proof of correct connections or semantic verification. SRC-1: `skill-sources/ralph/SKILL.md`.

> Verify sibling connections exist between batch notes. Add any that were missed
> because sibling notes did not exist yet when the earlier claim's reflect ran.
> Check backward link gaps. Output RALPH HANDOFF block when done.
> --- `skill-sources/ralph/SKILL.md`

Pipeline then counts non-done batch tasks. Pending tasks cause an incomplete-task report with IDs/current phases and a resume suggestion; archiving is forbidden. If none remain, the procedure requests `/archive-batch` or direct cleanup: move task files into the dated archive, generate a summary and remove completed queue entries or mark them archived. The inspected wrapper specifies that behavior; a standalone archive command implementation is not established here. SRC-1: `skill-sources/pipeline/SKILL.md`; [RT-RTE-source-processing](runtime.md#rt-rte-source-processing).

> **If tasks remain pending:**
> - Report which tasks are incomplete and at which phase
> - Show the specific task IDs and their current_phase
> - Suggest: "Run `/ralph --batch {batch_id}` to continue from where it stopped"
> - Do NOT proceed to archive
> --- `skill-sources/pipeline/SKILL.md`

Delivery comprises persisted notes/enrichments and graph changes, archived work records and a user-facing final report listing created note titles, processing/quality counts and archive/summary locations. With `--handoff`, the wrapper also emits a structured return to an upstream caller. Archive failure leaves the already-created notes in place and requests manual cleanup; it does not retract the substantive work. Queue/task persistence is intended to allow a later invocation to resume without the old session state. Successful delivery, actual quality and later consumption remain unobserved, and the selection/count/gate conflicts prevent equating a requested final report with an assured completed pipeline. SRC-1: `skill-sources/pipeline/SKILL.md`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-extract-selection
Label: Extract task selection mismatch

Claimed operation: pipeline requests extraction through a batch/type-filtered ralph invocation. Seed's YAML and JSON extract-entry templates supply `type: extract` but no `batch` or `current_phase`. Ralph's filter rules require a matching `batch` and interpret `--type` through `current_phase`; its serial prompt dispatch also uses `current_phase`. Following those templates literally therefore does not establish that the new extract task is eligible for the wrapper's extraction request. A model could infer missing fields or special-case extraction, but that reconciliation is not specified by the inspected filter rules. This is a doctrine/design mismatch, not an observed selection failure. SRC-1: `skill-sources/pipeline/SKILL.md`, `skill-sources/seed/SKILL.md`, `skill-sources/ralph/SKILL.md`.

Closest supplied records: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing) describes the containing route, and [RT-OBJ-queue](runtime.md#rt-obj-queue) identifies its phase state. This claim is a distinct finding about seed-to-extract eligibility, not another declaration of the route or queue. It differs from [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate), which concerns advancement after work returns.

> - id: {SOURCE_BASENAME}
>   type: extract
>   status: pending
>   source: "{FINAL_SOURCE}"
>   file: "{SOURCE_BASENAME}.md"
>   created: "{UTC timestamp}"
>   next_claim_start: {NEXT_CLAIM_START}
> --- `skill-sources/seed/SKILL.md`

> Apply filters:
> - If `--batch` specified: keep only tasks where `batch` matches
> - If `--type` specified: keep only tasks where `current_phase` matches (e.g., `--type reflect` finds tasks whose `current_phase` is "reflect")
> --- `skill-sources/ralph/SKILL.md`

- implementation conclusion status: claimed
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Workflow-specific completion distinction: phase return, claim done state, batch cross-connect return, outer completeness check and archive/report are separate milestones. The latter checks queue disposition, not independently verified semantic success. Partial note effects can remain when processing or archiving stops. The workflow account above retains the supporting passages and the selection, count and quality-gate limitations.
