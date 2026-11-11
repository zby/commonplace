# Review storage went from "not in Git" to "in a database" without a file comparison

## Observation and provenance

Raised by the operator on 2026-11-11: when the review system was analysed, the
move from "reviews are not stored in Git" to "reviews are stored in a database"
was made too quickly.

The record inspected is [ADR 010](../../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md)
in its current text and in its introducing commit `73033b41b` (2026-04-01), and
[ADR 127](../../reference/adr/127-review-runs-as-workflows-over-result-files.md)
(2026-11-10), which superseded it. No session trace of the April analysis was
inspected. The claims below are about what the retained decision account
compares, not about everything the April session considered.

## What the record shows

ADR 010 argues in four steps:

1. Per-gate review artifacts left Git because they produced too much churn.
2. "Once reviews stopped being versioned alongside notes and gates, the main
   file advantage weakened."
3. The untracked files then carried acceptance hashes, acknowledgement state
   and model-partition identity. The system "wanted indexes and current-state
   queries".
4. Therefore review state moves to SQLite.

The ADR has no alternatives section, in either version. The only file
arrangement it describes is the one being left: "flat files holding append-like
state, latest-state state, and human-readable review prose all at once".

Seven months later ADR 127 put review state back in files: one result file per
(note, criterion) pair, with the hashes of both inputs in frontmatter. These
files are untracked and machine-local. That is a third arrangement between the
two that ADR 010 compared.

## Where the jump is

**Step 2 counts Git's advantages as the file's advantages.** Leaving Git loses
history, diff and attribution. It does not lose that a reader can open the
record, that no schema needs managing, or that freshness can be computed from
the files and the current texts. ADR 127 cites those properties as reasons for
its choice.

**Step 3 compares the database with one file layout.** The rejected layout
mixed three kinds of state in one file. A layout keyed by the complete pair,
holding only current state, does not appear in the account. The
[edge-state note](../../theory/many-to-many-edge-state-is-where-files-yield-to-a-database.md)
already records that the case "does not show that the complete key required
SQLite".

**The pressure for indexes came from features.** Acknowledgement, model
partitions and job history each enlarged the key or the state. ADR 127 dropped
all three, and the store went with them. Whether dropping acknowledgement and
partitions is right is open: the operator said on 2026-11-11 that they are not
sure, and that the simplified system should be tried before either returns.
Results record the launch profile and the model the harness reported, so a
later partition scheme could classify existing results.

Two choices were therefore taken as one:

- whether a record is admitted to the main record;
- which carrier holds it when it is not.

## A competing explanation

ADR 127 gives a different cause: "Most of that machinery existed because no
code owned the run." A parent agent scheduled workers, so job state, transport
files and all-or-nothing finalization had to make its handoffs safe. A better
file layout in April would not have removed that need. It would have removed
the database only for acceptance state.

The two explanations are compatible. Neither has been tested. The record does
not say how much of the store each accounts for.

## What this case offers the workshop

- It is a carrier comparison in which content was not held constant. The
  database was compared with files that also carried extra features and a
  mixed layout. Step 2 of [how to advance the work](./README.md#how-to-advance-the-work)
  warns against that comparison for ADRs and commits; this is the same
  confound for operational state.
- "Not admitted to Git" is not one arrangement. The [storage contract](../../reference/storage-architecture.md)
  now distinguishes regenerable cache, local state and retained records, all
  as files. In April the account offered only Git or a database.
- Review results now hold paid judgments that cannot be rebuilt without paying
  again, and they are untracked and machine-local. That status follows from
  the April churn decision. It has not been assessed against this workshop's
  admission questions. This is a candidate choice to examine, not a finding
  that the status is wrong.

## Evidence limits

This is one decision, read from its retained account. It does not show that
SQLite was the wrong choice in April given the features then required, or that
result files will hold up: on 2026-11-11 this checkout had no result files, and
the first collection sweep had not run. It does not establish how often carrier
choices are bundled with admission choices elsewhere.
