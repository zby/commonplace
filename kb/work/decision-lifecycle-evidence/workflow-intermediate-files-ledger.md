# Workflow intermediate files ledger

## Purpose and authority

Show how Commonplace workflows handle intermediate files now, so we can apply
the operator's provisional retention default without silently losing debugging
material or publishing source copies and sensitive data.

Commissioned by the operator on 2026-11-11 after the cache/state merger. The
operator's direction is to keep intermediate artifacts in the second repository
for debugging and inspection, reconsidering workflows with substantial churn or
repository growth. This is a class-level default, not a requirement to justify
each file's future use. It does not require producing extra artifacts or
copying the harness's primary session archive.

**This ledger describes current handling; it does not change it.** A file under
`kb/reports/state/` is eligible for the proposed state repository's scope, not
proof that it has been committed, synchronized or cleared for public release.
A Git repository cannot retain a version that is overwritten or deleted before
it is committed. Current producer rules continue to apply until separately
changed. No migration, deletion, workflow execution or public upload is
commissioned by this inventory.

## Retention approaches left open — 2026-11-11

The operator asked to record these approaches without resolving them. The
provisional preservation default above remains direction, not a selected
capture mechanism or a settled definition of every intermediate version.

Two retention approaches remain worth comparing:

- **Selective retention:** keep material expected to be hard to find or
  reconstruct from the existing session traces. This limits duplication but
  requires selection effort and can miss a later debugging need.
- **Preserve all intermediate artifacts:** avoid per-artifact selection and
  provide direct access to produced files. This accepts duplication and may
  create substantial churn. It does not require recording every filesystem
  change or generating additional artifacts.

For preserving successive versions, two implementation approaches were discussed:

| Approach | Preservation point | Trade-off |
|---|---|---|
| Commit before replacement or deletion | Commit completed outputs at their existing paths before the next stage changes them; one commit could cover several outputs | Keeps the working layout, but preservation depends on a successful commit at the right time |
| Save immutable copies, commit later | Copy each selected version to a unique, never-overwritten path, then commit copies in batches | Separates capture from Git commit timing, but adds a versioned-copy layout and copies remain uncommitted until the batch succeeds |

Workflow handoffs, worker returns and submissions to checks were suggested as
possible version boundaries, not adopted requirements. It remains open which
versions to capture, whether to combine the approaches, and whether large-churn
workflows need exceptions. Current working files could remain mutable while
history preserves earlier versions; this does not settle cleanup or pruning.
No producer change, commit cadence or capture implementation is authorized by
this discussion. Existing session traces remain the primary process record,
and publication restrictions remain separate from retention.

## Inspection boundary

First pass: 2026-11-11, against committed producer instructions and selected code
at `d4aba3fd57e055e8aca8649ef6f58fd29cbc6d76`. This is an inventory of prescribed
and implemented handling, not an audit of every existing payload or observed
run. The [state README](../../reports/state/README.md) supplied an initial
output list; producer instructions and code supplied the checks below. That
README is ignored by main and is not the sole evidence for a row.

Rows group workflow families when they share handling. They include outputs
outside `state/`, because those are easy to miss when planning a second
repository. A final library artifact is named only to distinguish it from its
intermediates. Harness traces remain under the harness's own contract.

Coverage is not yet exhaustive: the unresolved coverage section names what must
be checked before calling this a ledger of all workflows. No output size, churn
rate or debugging benefit has been measured here. Recheck a row when its owning
producer changes; do not treat this dated inventory as a new runtime contract.

## Outputs currently under the state tree

Paths below are relative to `kb/reports/state/`.

| ID | Workflow and evidence | Intermediate files and current handling | Retention gap or decision |
|---|---|---|---|
| W01 | [Gate sweep](../../instructions/run-review-batches.md); [gates code](../../../src/commonplace/lib/review_workflows/gates.py) | `review/runs/<UTC stamp>/` keeps Workjig calls and accepted artifacts. `review/results/<note-path>/<criterion-id>.md` is the current judgment with input hashes; a later review replaces it. Explicit resume reuses a run; an ordinary rerun opens another. | Runs preserve more than the latest-result surface. Establish whether every superseded result is recoverable from its run or a state commit; latest-path presence alone is insufficient. |
| W02 | [Full improvement pass](../../instructions/run-full-improvement-pass-on-note.md); [full-pass code](../../../src/commonplace/lib/review_workflows/full_pass.py) | `review/runs/full-pass/<note-path>/<start-hash>/` keeps start text, method outputs, edits, packet and closing work. The current packet also lives at `review/packets/<note-path>`. The command publishes final text only after approval. | Preserve the run, not just the current packet. A pending packet is live operational state, not disposable evidence. No cross-machine continuation guarantee follows from copying it. |
| W03 | [Revision](../../instructions/revise-note.md); [revision code](../../../src/commonplace/lib/review_workflows/revise.py) and [run paths](../../../src/commonplace/lib/review_workflows/edits.py) | A workflow/path/start-hash directory under `review/runs/` carries model calls and accepted artifacts. Same inputs return to the same run; a changed start text gives another path. | Already in the candidate repository tree; verify saved rejected attempts as well as accepted outputs before claiming complete intermediate retention. |
| W04 | [Ingest and re-ingest](../../instructions/cp-skill-ingest/SKILL.md); [handoff code](../../../src/commonplace/lib/ingest_handoff.py) | `ingest/<slug>/` holds candidate and `handoff.yaml`. Repair uses the same candidate path. Publish deletes the candidate because it equals the published ingest; close keeps the failed candidate. A later prepare deletes the finished directory before making the next run. `prune` deletes eligible published runs. | Not an all-runs archive: earlier run records and failed primary candidates can disappear. Preserving only the final directory misses overwritten versions. The [prior retention case](./ingest-working-directory.md) needs reconciliation with the new default. |
| W05 | [Connect](../../instructions/cp-skill-connect/SKILL.md) | `connect/<collection>/<artifact-name>.connect.md` is one discovery report per artifact. Same-target runs address the same file. Source-snapshot and accepted-ingest passes have distinct names. No input freshness accounting. | State history must capture a report before replacement to retain all versions. Keeping reports does not make stale findings current. |
| W06 | [Fix system](../../instructions/FIX-SYSTEM.md) and [fix worker](../../instructions/fix-warnings/fix-review-warnings.md) | `fixes/<note-stem>.fix-report.md` records fixed, rejected and deferred findings. The existing report is read before later work; no per-run archive is specified by the path. | Verify append versus replacement and preserve prior versions. Unresolved dispositions must remain available to their operational consumer. |
| W07 | [Composition friction](../../instructions/composition-friction-gate.md) and [premise decomposition](../../instructions/premise-decomposition-gate.md) | `friction/<note-name>.friction.md` and `premise-decomposition/<note-name>.premises.md`; each instruction writes a report only, using the same target-derived path. | Later reports can replace earlier judgments. The state README's remove-when-unused guidance has not yet been reconciled with preservation by default. |
| W08 | [Compression bundle](../../instructions/run-compression-bundle-on-note.md) | Default `compression-bundle/<note-name>.md`, or a caller-selected report path. One report combines four assessments and synthesis. It is explicitly separate from review result files. | The procedure calls the report disposable. Record-path reuse and caller overrides need attention; do not assume all reports land in the state tree. |
| W09 | [Web/PDF snapshot capture](../../instructions/cp-skill-snapshot-web/SKILL.md) | `snapshot-web/capture.XXXXXX/` holds downloaded HTML/PDF, extraction, body and header. The procedure removes this directory after assembling and hashing the snapshot. The final Markdown goes to `.snapshots/`. | Explicit deletion before a normal later state commit. Raw captures may contain third-party or sensitive text: retention and public publication require separate handling, not blind inclusion in the public state repository. |
| W10 | [Recurring tasks code](../../../src/commonplace/lib/tasks.py); [explanatory-reach runbook](../../tasks/review-explanatory-reach.md) and [dormancy runbook](../../tasks/workshop-dormancy-report.md) | `tasks/<name>/<stamp>/` stores the task's Workjig run. Both currently shipped runbooks append results to their named `kb/tasks/*-log.md` and require committing that log. | Wrapper intermediates are in state; the task logs are deliberately tracked products outside it, not misplaced intermediate bundles. Future task-specific outputs still need individual inspection. |
| W11 | [Commonplace transfer scan](../../instructions/scan-agentic-system-transfer/SKILL.md) | Response-only unless a state output is authorized; written scans use `agentic-system-transfer/`. Open stale scans are preserved; a new scan uses a collision-safe sibling. Replacement/deletion is allowed after all candidates have dispositions. | Current final-disposition cleanup differs from the new historical-retention default. Response-only scans produce no separate file to preserve. |

## Outputs outside the state tree or with caller-selected paths

| ID | Workflow and evidence | Intermediate files and current handling | Retention gap or decision |
|---|---|---|---|
| W12 | [Multistage writing](../../instructions/cp-skill-write-multistage/SKILL.md) and [promotion](../../instructions/cp-skill-write-multistage/references/promotion.md) | `kb/work/multistage/multistage-write-<topic>-<date>/` contains brief, original, source reconstruction, candidate, independent reviews and any repairs. Successful closure removes the exact run and active-list entry when no retention reason remains. Blocked, failed, inspection and experiment runs are kept. | Run bundles are outside the second repository tree and successful cleanup can remove them. Preserve a bundle before closure under any future implementation of the default. |
| W13 | [Literature-disposition assessment](../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) | Uses W12's workshop. Adds source comparisons and dispositions; conditional bilateral isolation adds target inventory, source reconstruction and isolated comparison. Grounding may also change ingests. | Same closure gap as W12. Source copies and curated quotes have distinct publication boundaries; assessment outputs are not interchangeable with either. |
| W14 | [AutoReason revision](../../instructions/cp-skill-revise-autoreason/SKILL.md) | `kb/work/revise-autoreason/<source-name>.<timestamp>/` contains incumbents, critics, B/AB candidates, audits, blind packets, judges, rankings and substantive sidecars. On normal apply/decline, deletes the bundle unless the user asks to keep it; substantive sidecar asks about keeping it. | Explicit cleanup default conflicts with preservation by default. Candidate paths can also be overwritten by repair. Moving only the final winner loses the diagnostic material. |
| W15 | [Agentic-system analysis](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md); [controller code](../../../src/commonplace/lib/agentic_analysis/automation.py) | Default controllers and isolated worktrees live under `.commonplace/worktrees/`. Runs retain source/method bindings, role calls, verifications and advisory audits. Integration publishes accepted sets into `kb/agentic-system-analyses/retained/`, not the advisory audit. Worktree cleanup requires separate authority and evidence disposition. | Important debugging evidence is outside state and not included by integration. Inventory exact run/controller members before proposing export; copied source checkouts, environments and nested Git data are not automatically public workflow reports. |
| W16 | [Memory landscape synthesis](../../agentic-systems/instructions/synthesize-agent-memory-landscape/SKILL.md) | Builds a matrix at a temporary caller-chosen path and requires executable queries with their outputs in a working query ledger, without prescribing a state-tree location. Publishes an account bound to an inputs commit, selection rule and matrix hash. | Matrix, query-ledger and draft locations are not fixed to state. Reconstructability of the final evidence does not itself preserve the executed intermediate bytes. |
| W17 | [Source capture commands](../../../src/commonplace/cli/github_snapshot.py) and [X capture](../../../src/commonplace/cli/x_snapshot.py); [paper-with-code branch](../../instructions/ingest-paper-with-code.md) | Captures live under `kb/sources/.snapshots/`; GitHub capture writes Markdown and a JSON companion. Code-grounding checkouts live under `related-systems/`. These are inputs/capture companions rather than just final report text. | Source snapshots have a separate private-repository arrangement. Do not fold them, raw downloaded text or whole checkouts into a public second repository merely because they supported a workflow. Check X companion handling and code-check execution files individually. |
| W18 | [Adversarial critique](../../instructions/critique-note.md) | Caller supplies the report destination; a `commonplace-review` caller supplies a run-owned output path. Manual invocation must name a path before dispatch. | Covered by review runs only when invoked there. The historical `critique/` directory is not a universal current destination. |
| W19 | [Code review](../../instructions/review-code.md), [hidden-failure review](../../instructions/review-recent-logs-for-hidden-failures.md), [design-pressure diagnosis](../../instructions/review-design-pressure-behind-recurring-errors.md), [task selection](../../instructions/find-next-straightforward-task.md) | Code review returns findings; hidden-failure review defaults to conversation unless an output path is supplied. Diagnosis and task selection specify an account, not a universal run directory. Caller-commissioned workshop records may retain results. | Distinguish no separate file produced from a file deleted. A default-retention policy does not yet supply these procedures with persistent report paths. Do not duplicate entire session archives to fill that gap. |
| W20 | [Article staging](../../instructions/stage-an-article-package.md) and [publication](../../instructions/publish-an-article.md) | `kb/work/staging/<slug>/` holds inventory, appendices, references, link map and closure check. Restaging deletes the old staging directory; publication moves package parts to `kb/articles/` and deletes staging. | Inventory and closure evidence can disappear although the published package survives. Outside state; preserve prior staging before replacement or publication if the default is implemented. |
| W21 | [Ordinary writing](../../instructions/cp-skill-write/SKILL.md), [grounding](../../instructions/cp-skill-ground/SKILL.md), [conversion](../../instructions/cp-skill-convert/SKILL.md), [collection creation](../../instructions/cp-skill-add-collection/SKILL.md) | Main artifacts are edited directly or through their named subworkflows. Grounding retains incumbent bytes for restoration, then writes quotes into an ingest. No general persistent draft/backup directory is prescribed across this family. | Git captures committed products, not every uncommitted draft or in-memory backup. Follow invoked ingest, connect, snapshot and relocation rows separately. No new all-edits logging is implied. |
| W22 | [Roughdraft review](../../instructions/roughdraft-review/SKILL.md) | Opens the actual Markdown file for user markup; plans must be on disk before review. No separate universal run-bundle archive is specified. | Inspect editor/tool handling before claiming that each markup version is saved. The edited document is not evidence that rejected user annotations survive. |
| W23 | [Workshop lifecycle](../COLLECTION.md) | Named `kb/work/` directories mix framing, drafts and evidence. Closure extracts durable contributions and deletes the directory and active entry. Some exact captures have publication/validation-ignore markers. | Existing Git history may preserve committed bundles, not uncommitted or ignored files. A retention plan must cover those before closure without changing the workshop layer into permanent library storage. |

## Deterministic outputs and tool-only operations

| ID | Workflow and evidence | Current handling | Retention question |
|---|---|---|---|
| W24 | [Promotion candidates](../../../src/commonplace/cli/promotion_candidates.py) and [producer](../../../src/commonplace/lib/promotion.py) | Deterministic report under `state/promotion-candidates/`; reruns replace the report. | Not exempt from the operator's default merely because it can be rebuilt, but high-frequency replacement may be a churn exception. No exception is adopted here. |
| W25 | Validation, status, quote verification, relocation, initialization, installation checks and scenario evaluation | CLI entry points under `src/commonplace/cli/`; [scenario evaluation](../../instructions/evaluate-scenarios/SKILL.md) returns a report. Many commands return diagnostics or plans rather than prescribing a persistent intermediate bundle. Relocation and init also mutate their authorized project files. | **Screened family, not fully inspected.** Inventory file-producing branches and caller redirection before asserting these commands have no intermediates. Ordinary test/build caches and installed environments are not automatically report payloads. |

## Common run records

The [headless job layer](../../../src/commonplace/headless/jobs.py) supplies
Workjig `calls/` records, launch evidence and accepted `artifact/` files to
review and task runs. Accepted-artifact materialization is not the same as
retention of every failed or rejected attempt. A follow-up should trace the
call-record and launch files needed for debugging, including any replacement
inside a reused run. No such run was executed for this inventory.

## State-tree placement check — 2026-11-11

**Not all workflows save their intermediates in `kb/reports/state/`.** Rechecked
producer instructions and code at
`d3f87187645e736839c55d49fb34aada78a3a802`, without executing workflows or changing
producer paths. The check searched all Markdown/Python files under the three
instruction trees, `src/commonplace/lib/` and `src/commonplace/cli/` for state,
workshop, worktree and temporary-path declarations, then read consequential
matches. A separate script-path search was a lead scan, not a complete audit of
script writes.

Confirmed location exceptions:

- W12–W14: multistage writing, its literature-assessment branch and AutoReason
  keep run bundles under `kb/work/`.
- W15: analysis controllers and isolated runs use `.commonplace/worktrees/` by
  default; integrating final sets does not bring all run/audit evidence into state.
- W16: synthesis requires a temporary matrix and working query ledger without
  fixing either destination to state.
- W20: article staging uses `kb/work/staging/`.
- W18–W19 and W22: caller-selected reports, response-only work and editor markup
  do not have a universal state output. These are not all location violations:
  some produce no separate intermediate file at all.

Confirmed state defaults include review sweeps/full passes/revision runs,
ingest handoff, connect, fixes, friction, premise decomposition, compression
bundle, snapshot scratch and the recurring-task wrapper. Compression allows a
caller override; transfer scans are response-only unless a state file is
authorized. Both current task runbooks were inspected: their tracked task logs
are products, while wrapper call records live under state.

Location is not retention. Snapshot scratch is explicitly removed after capture;
ingest prepare replaces finished runs, publish deletes its candidate, and prune
can delete published records. Connect and current-result paths are reused.
These need separate treatment if the objective is to preserve all versions,
without selecting either capture approach recorded above.

Source snapshots and code checkouts remain a distinct input/publication boundary,
not candidates for indiscriminate migration. This is enough to refute universal
state placement, but not to certify that every workflow or output branch has
been inventoried. No migration or retention implementation was performed.

## Disposition — 2026-11-12

[ADR 129](../../reference/adr/129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md)
records the operator's decision for the location exceptions found above. The
inventory rows above stay as dated evidence of handling before the change.
Paths below are relative to `kb/reports/state/`.

Moved and kept after the workflow finishes:

| Row | New location | Keep rule |
|---|---|---|
| W12 | `multistage/multistage-write-<short-topic>-<YYYYMMDD>/` | Closure no longer removes the run. Runs leave main's tracked history; the promoted artifact is the durable product. |
| W13 | the W12 run it reuses | As W12. |
| W14 | `revise-autoreason/<source basename>.<YYYYMMDD-HHMMSS>/` | Apply and decline no longer delete the bundle. |
| W16 | `agent-memory-landscape/<YYYYMMDD-HHMMSS>/` for matrix, working query ledger and draft | Kept; no longer a caller-chosen temporary path. |
| W20 | `staging/<slug>/<YYYYMMDD-HHMMSS>/` | Restaging adds a package beside the old one; publication copies appendix and reference files into `kb/articles/` and leaves the package. |

Overwrites inside a bundle, such as a repair, still replace the earlier file.
No version capture was added.

**W15 is the recorded exception.** Integration already admits the analysis
workflow's durable outputs to main under `kb/agentic-system-analyses/retained/`.
Its process record stays in the run's worktree under
`kb/agentic-system-analyses/state/<run-id>/`, which is a checkout of main. The
exception lifts when integration copies that record into the origin's
`kb/reports/state/`, a separate code change. The workflow does not delete the
record, so waiting loses nothing.

Still open:

- W18, W19 and W22 produce no separate file by default. The preservation
  default does not authorize new production, so nothing moved.
- W25 remains uncovered; its file-writing branches are uninspected.
- Version capture inside a bundle, commit cadence, history pruning and churn
  exceptions are undecided. Commit cadence and pruning stay with the
  [public-state-repository workshop](../public-state-repository/README.md).
- Deletion and replacement inside the state tree (W04, W05, W09 and the
  current-result paths) are unchanged by this disposition.

## Current gaps against the operator's default

1. **Deletion before capture:** snapshot scratch, AutoReason cleanup, multistage
   closure and article staging can delete intermediate files before the second
   repository sees them.
   *2026-11-12:* AutoReason, multistage and staging deletion is removed by
   ADR 129; snapshot scratch deletion is unchanged.
2. **Replacement before capture:** ingest prepare/repair, same-target discovery
   reports and current-result files can lose earlier versions between commits.
   *2026-11-12:* unresolved; ADR 129 adds no version capture, and overwrites
   inside the moved bundles also remain.
3. **Files outside the publication tree:** workshop bundles and analysis
   controllers/worktrees are not included merely by versioning `state/`.
   *2026-11-12:* resolved for W12–W14, W16 and W20 by ADR 129; the analysis
   process record (W15) is the recorded exception until integration copies it.
4. **No separately produced report:** response-only work has only its normal
   session record unless the caller requests a file. Decide whether any family
   needs a new output; retention alone does not authorize extra production.
   *2026-11-12:* unchanged; ADR 129 adds no new output for W18, W19 or W22.
5. **Publication boundary:** raw captures, source checkouts, traces and report
   bodies can include material unsuitable for public redistribution. The
   [public-state-repository workshop](../public-state-repository/README.md)
   owns publication checks and repository setup; this ledger grants neither.
   *2026-11-12:* unchanged; ADR 129 keeps source snapshots and checkouts out
   of the state tree and makes nothing in it safe to publish.
6. **Current files versus history:** keeping historical intermediates need not
   keep every file in the active working set. No commit cadence, all-versions
   capture mechanism, history-pruning rule or automatic sync has been selected.
   *2026-11-12:* unchanged; ADR 129 decides location and the keep rule only.

These are implementation questions, not instructions to bypass current cleanup
or change producers during unrelated work. The operator permits reconsidering
large-churn cases, but no measured exception has been established in this pass.

## Unresolved coverage and next pass

To finish the all-workflows inventory, inspect rather than infer:

- W25's individual commands and their file-writing branches.
- New or project-specific recurring task runbooks beyond the two currently
  shipped runbooks checked in W10.
- Repo-local scripts and workshop-specific experiment runners. They are not
  covered by enumerating generic skills or CLI entry points.
- The direct simplification/editing instructions, installed-project test
  procedures, maintenance/migration procedures and ad hoc shell redirections;
  split a family row when a distinct file lifecycle is found.
- Call/launch retention inside the shared headless layer and analysis runs,
  plus X capture companions and Roughdraft's annotation handling.

The next inventory pass should resolve those gaps without running paid
workflows or modifying their outputs. Add source paths and distinguish inspected
behavior from unknowns. Once coverage is adequate, choose producer changes and
state-repository capture rules separately. A missing file is not proof that a
workflow never wrote one, and a complete directory listing is not a complete
file-lifecycle audit.
