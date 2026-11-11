# What review lost in isolation when the store went

## Question and provenance

Posed by the operator on 2026-11-11: what did review lose by leaving the
database, primarily in isolation? Many automated jobs running together could
trip on each other. The operator added that the project is not at that stage
yet. This file records the analysis so the question does not have to be
re-derived. It commissions no build.

Evidence: the write paths in `src/commonplace/lib/review_workflows/` as read
on 2026-11-11, and the store's guarantees as stated in
[ADR 035](../../reference/adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md)
and [ADR 052](../../reference/adr/052-general-freshness-store-review-first-migration.md).
The store's code is deleted and was not inspected. No concurrent runs were
executed; every collision below is read from the code, not observed.

## Conclusion

Review lost protection against wasted work, not against wrong state. A result
file records the hashes of the texts it was produced from. A result that lands
late or out of order is therefore shown as stale; it cannot be read as fresh.
The lost protections can be restored with files when they are needed. None
requires a database.

## The store's guarantees and their present counterparts

| Property | Store | Result files |
|---|---|---|
| No torn reads | SQLite transactions | Kept. Results and notes are written by atomic rename (`results.write_result`, `edits.write_text`). |
| A stale job cannot overwrite newer state | Compare-and-swap on the pair's baseline revision at finalization | Lost. The last writer wins. A slow job that started on old note text can replace a fresh result with a stale one. Status then shows the pair stale and it is reviewed again. |
| In-flight work is visible to other processes | Queued jobs were rows any process could read | Lost across runs. Whether the old selector used those rows to skip pairs already queued was not checked. |
| Several records change together | All-or-nothing job finalization | Lost. A bundle's results are separate writes. A full pass writes its packet, then the note, then its results; it orders them for crash recovery. |
| One writer per run | Database locks | Kept, narrower: Workjig holds an exclusive lock per run directory. |

## Where concurrent jobs would collide

- **Duplicate paid reviews.** Nothing claims a pair. Two overlapping sweeps
  each open their own run directory, each find the pair stale, and each pay
  for it. This is the main loss and it grows with the number of overlapping
  sweeps.
- **The checkout guard.** It reports every path that changed while a run was
  open and cannot attribute the change. With many jobs in one checkout, every
  run would exit nonzero with paths to inspect. This is noise, not corruption,
  but the guard would stop working as a signal.
  [ADR 127](../../reference/adr/127-review-runs-as-workflows-over-result-files.md)
  already lists it as open.
- **Two different workflows on one note.** A full pass and a revision derive
  different run directories, so the run lock does not separate them. Each
  writes the note only over its start text, so the second gets a conflict and
  writes nothing. Its paid work is wasted.
- **A race on the note write.** `edits.apply` checks that the note still holds
  the start text and then writes, as two steps. Another writer could land
  between them. The window is short and is not closed.

Two runs of the same workflow on the same note text are safe. They derive the
same run directory and the lock refuses the second.

## What the store never provided

The store did not isolate the checkout. Concurrent jobs that edit notes,
criteria or Git state in one working tree collided under the store too. That
is the larger problem for many automated jobs. It belongs to
[recurring-task-runner](../recurring-task-runner/README.md), which runs tasks
in the shared checkout without worktrees or branches.

## Disposition

Build nothing now. Reconsider when overlapping review runs become routine, or
at the first observed duplicate review, lost fresh result or guard failure
caused by another job.

Candidate repairs, recorded as options and not selected:

- a per-note claim file taken before paid work starts, which would cover
  duplicate reviews and conflicts between workflows;
- a guard that knows which paths its run owns, so that it reports only changes
  outside them. A claim file does not fix the guard.

This is a follow-on question. It does not extend the workshop's closing
conditions.
