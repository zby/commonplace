---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MemexOS workflow account: source-batch compilation through delegated writing, review, bounded repair and publication."
run-id: AAS-2026-11-07-memexos-5cd34a715eb7-01
reviewed-boundary: bb9e9b2ac0adbca87d13a9f7600867128b5f71b9
---

# MemexOS workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is `memex ingest`: compile a pending raw-source batch into the live wiki. It is selected because it connects a concrete request, delegated edits, two acceptance mechanisms, repair and delivered retained knowledge in one shipped caller, rather than joining independent capabilities. Its canonical route is [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish). Source intake precedes this request but is not mandatory for every raw file; later search/get consumes its result but does not complete the compiler's task. Those adjoining routes remain [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) and [RT-RTE-search-get](runtime.md#rt-rte-search-get).

All source findings use SRC-1 at the frozen revision. This is an implementation trace, with English task prompts supplying doctrine/design. No target execution, successful model compliance, production run or causal benefit was observed. Inspection here covers `src/memexos/pipeline/compile.py` through ingest, `src/memexos/pipeline/stage.py`, `src/memexos/pipeline/gate1.py`, `src/memexos/pipeline/gate2.py`, `src/memexos/pipeline/report.py`, and `src/memexos/prompts/en/{compile,rework_gate2}.md`. In particular, the report-to-writer transformation adds implementation coverage beyond the supplied runtime baseline under the same source identity; it introduces no new source or observation.

### Request, selection and first handoff

Code, not the writer, selects the next batch. Ingest checks review-service cooldown and pause, yields to waiting writers and acquires the write lock per batch. Pending selection excludes already-ingested and held files as well as assets and feedback; companion grouping can exceed the nominal batch size. Classification context is supplied with an unclassified fallback. Stage.open commits pending raw changes, records HEAD as the base and creates the draft branch/worktree. Thus the writer receives selected source paths, classification, date and a filesystem snapshot, not ownership of scheduling or the live-vault merge (SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/stage.py`; [RT-OBJ-stage](runtime.md#rt-obj-stage)).

The compiler delegates content work to the configured writer role with staging as cwd and a path-scoped Policy. The prompt requests reading the full vault instructions, interpreting the sources, updating wiki/index/log and routing unresolved questions to inbox. It explicitly sets unattended rather than per-edit human approval:

> (do them all in one go; nobody is online, so do not wait for confirmation):
> --- `src/memexos/prompts/en/compile.md`

Contradictions, uncertain classifications, unverified key claims and schema proposals are requested as inbox items rather than decisions for the writer to settle. That instruction is not proof that a model follows it. The writer's terminal summary is only a bounded event summary; acceptance inspects the files, not the summary's assertion of completion. The writer Policy and its adapter-dependent enforcement are already distinguished in [RT-OBJ-policy](runtime.md#rt-obj-policy) and [RT-RTE-backend-execution](runtime.md#rt-rte-backend-execution). In particular, this workflow does not establish uniform process isolation across backend choices.

### Structural acceptance, self-check and review handoff

After a successful writer call, Gate 1 checks the staged diff against the base. It rejects changes outside wiki/inbox/index/log, including raw changes, and checks new-page structure, index membership, append-only log behavior and selected link/source-path properties. Warnings do not block. This is a structural acceptance rule, not a truth check or a complete audit of old pages (SRC-1, `src/memexos/pipeline/gate1.py`):

> Only what was written this time (lines added in the diff) is checked: problems in
> older content belong to the weekly lint, not to this batch.
> --- `src/memexos/pipeline/gate1.py`

Code sends failed-check JSON back in a fresh writer call with a rework prompt, bounded by the configured Gate 1 repair count (default two). The continuing artifact is the draft worktree, not an inspected shared model conversation. After structural acceptance, optional self-check can request another writer repair. The baseline establishes its new-sentence/source-support selection and that unavailable self-check proceeds to review. Ingest also rechecks Gate 1 after an unsuccessful self-check repair before allowing review; a structurally invalid partial repair is held (SRC-1, `src/memexos/pipeline/compile.py`; [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)).

Gate 2 then delegates judgment, not final admission, to the reviewer role. It supplies the rubric/task, base revision, raw paths, changed wiki/index paths, a computed diff and access to the staging files. The diff is capped at 600,000 characters with a request to open files for the remainder. The returned structured object inventories claims, key points, overwrites, injections and integration notes. This limited delivered context and model-selected inventory prevent treating the review as independently exhaustive (SRC-1, `src/memexos/pipeline/gate2.py`; [RT-BAP-review-verdicts](runtime.md#rt-bap-review-verdicts)).

Deterministic code can veto publication on the reviewer's reported critical unsupported/contradicted claims, substantive overwrites lacking both support and disclosure, followed source instructions, missing critical points, noncritical bad-claim rate above 5%, or must-point coverage below 80%. These are rules over model judgments, not an expected-answer oracle. Neither the label “independent reviewer” nor a passing object establishes model independence, correct judgments or real-world truth. Raw-source comparison is the requested reference procedure; no externally supplied correct-answer oracle is established for this open source-batch workflow (SRC-1, `src/memexos/pipeline/gate2.py`; [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication)).

### Rejection, repair and terminal failure

On a failed review, orchestration records the review and calls `report.for_writer` to build the repair handoff. This transformation matters: the next writer does not simply receive the entire reviewer session or only a pass/fail flag. `report.problems` excludes SUPPORTED and MARKED claims; it retains other claim verdicts with page, claim, evidence, raw location and reason, plus qualifying overwrites/injections, missing critical/must points and integration notes. It sorts by severity. `for_writer` renders these fields into a numbered localized list. This preserves reasons and source locations for repair while selecting away accepted claims; it does not independently verify the reviewer's evidence (SRC-1, `src/memexos/pipeline/report.py`):

> if v in ("SUPPORTED", "MARKED"):
>     continue
> --- `src/memexos/pipeline/report.py`

The rework task narrows the writer's remit:

> Read the raw source before changing anything. Change only what these problems concern. No extra log entry is needed. When done, output a single summary line.
> --- `src/memexos/prompts/en/rework_gate2.md`

The resulting writer call must pass Gate 1 again; then a new review runs in fix mode against the current draft. Default Gate 2 repair count is two. Code owns this progression and can stop it; the reviewer does not self-authorize a merge, and the writer cannot satisfy the gate merely by declaring fixes done (SRC-1, `src/memexos/pipeline/compile.py`; [RT-BAP-review-verdicts](runtime.md#rt-bap-review-verdicts)).

Failure recovery is deliberately nonuniform. An initial writer failure discards the draft so raw files remain eligible next time. Exhausted structural repairs, exhausted review repairs or a writer failure during review repair instead hold the branch and mark the batch held. Review unavailability discards the draft and records a cooldown marker. A transient initial writer failure can retry up to three times with increasing wait and a resume instruction over the existing files; this is not restoration of a proven conversation checkpoint. All are inspected branches, not exercised recoveries (SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/stage.py`).

Holding preserves a committed branch, removes the staging worktree, adds raw paths to held.txt and writes a blocked inbox entry with branch/base and a bounded report tail. It therefore delegates further disposition to a later operator/control action rather than automatically retrying indefinitely. The baseline establishes console abandon as one path to delete a non-live held branch and requeue its raw sources; ordinary ingest alone does not perform that recovery ([RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish); SRC-1, `src/memexos/pipeline/stage.py`).

### Delivery and its exceptions

When review passes, code appends ingested.txt only after the gates and records earlier repaired reviews in fixed-reviews.txt. The passing review may retain minor problems for later fix. Stage.publish commits and merges the draft into the live vault, cleans up staging on success and emits publication. A merge failure attempts merge-abort and ingest holds the branch. Delivery means the retained file changes have merged; a batch returns 0 on that path, while the enclosing ingest can continue to another batch (SRC-1, `src/memexos/pipeline/compile.py`, `src/memexos/pipeline/stage.py`).

This is a conditional publication protocol, not an invariant that every delivered page received model review. Configured Gate 2 off returns an accepted `off` outcome, and no wiki/index changes can produce a passing review result without calling a model. Stage.publish itself does not independently enforce the review gate. These supplied exceptions qualify the checked-publication claim rather than disappearing from the representative trace ([RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish), [RT-CLM-checked-publication](runtime.md#rt-clm-checked-publication)).

Publication attempts immediate FTS refresh but swallows refresh exceptions, then starts detached reindexing. Successful merge therefore does not guarantee fresh retrieval indexes or an atomic multi-file reader snapshot. Later search/get can return retained knowledge, but that caller owns its next reasoning step; delivery is not evidence that an answer changed or improved ([RT-RTE-search-get](runtime.md#rt-rte-search-get), [RT-BAP-retrieved-pages](runtime.md#rt-bap-retrieved-pages); SRC-1, `src/memexos/pipeline/stage.py`).

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

#### On [RT-RTE-compile-publish](runtime.md#rt-rte-compile-publish)

Workflow role: the selected end-to-end source-batch production route, with code retaining scheduling, repair-budget and merge authority. Its handoff boundary is filesystem draft plus selected check feedback rather than a shared persistent conversation. The report-to-writer projection described above is a consequential selection step: only rendered problems cross into review rework, while the current draft and source files remain available. Completion is batch publication, not elimination of every reported minor issue or delivery of an answer to an external question. Failed review and unavailable review have distinct recovery owners and next states: held-branch disposition versus deferred fresh compilation after cooldown.
