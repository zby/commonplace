# Public state repository

## Goal

Decide whether the local operational state under `kb/reports/state/` should be
kept in a second, public Git repository, and if so prepare and create it.

The operator opened this workshop on 2026-11-11. It started from a question
about the [decision lifecycle](../decision-lifecycle-evidence/README.md)
workshop: that workshop asks what earns admission to the main record, and
storage size is not what limits admission. A second repository could keep
state durably without admitting it.

## The idea

`kb/reports/state/` is ignored by the main repository. Its contract says the
contents are local but not disposable. Today that material lives on one
machine, with no backup, no history and no second reader.

A separate repository, checked out at `kb/reports/state/` and still ignored by
the main repository, would give state a durable home without these costs of
tracking it in the main repository:

- search noise: a failed candidate looks like an ingest to `rg`;
- implied status: presence in the main record reads as endorsed;
- commit load: every run would dirty the main tree;
- mixing with library history.

It would be a class-level default: keep the material without curating it and
without claiming it is useful. Promotion into the main record stays a separate,
deliberate decision.

The operator wants this repository public.

## Settled

- **Snapshots are not part of it.** Being publicly readable does not grant a
  right to redistribute, so snapshots went to a private repository,
  `zby/commonplace-sources`, checked out at `kb/sources/.snapshots/`
  (created 2026-11-11). See
  [storage architecture](../../reference/storage-architecture.md#an-ingest-whose-snapshot-is-on-another-machine)
  for what a machine without it can and cannot do.
- **A plain nested checkout, not a submodule**, is the working assumption. An
  ignored directory stays ignored after `git init` inside it, and the validator
  runs its Git calls from the main repository root.
- **Caches stay out.** `kb/reports/cache/` is regenerable by definition.

## What the directory holds

Measured on 2026-11-11: 964 MB in 24,099 files.

- About 500 MB is review data: SQLite stores, their backups, and directories
  the [state README](../../reports/state/README.md) lists as abandoned and
  deletable.
- 231 MB is old agentic-system analysis runs under `agentic-system-analysis/`.
  They examine external repositories and may quote their code.
- 563 files contain `/home/zby` paths.
- 42 files match an API-key pattern. These may only be analyses that discuss
  key handling in other systems; none has been read.
- 2 files carry snapshot frontmatter and may be copied snapshots. 152 files
  mention a snapshot path without copying one.

## Before anything is published

Publishing cannot be undone, so each of these comes before the first push.

1. Delete the abandoned review data the state README already permits deleting.
2. Read the 42 key-pattern files. Remove or exclude any real secret.
3. Decide what to do about local paths: accept, rewrite or exclude.
4. Check what the analysis runs quote from external repositories and under
   which licences. Exclude what cannot be redistributed.
5. Check the 2 files that look like copied snapshots.
6. Decide what a public reader is told about status: unreviewed model output,
   failed candidates and abandoned runs are in there.

## Open questions

- **Who reads a public state repository, and for what?** Durability and sync
  need only a private one. Name the use that public access serves before
  paying the publication checks above.
- **Pairing with the main repository.** A state commit does not say which main
  commit it belongs to. Record the main commit hash, or accept the loss.
- **Sync.** Something must commit and push. The simplest rule is at the end of
  each workflow; the private snapshot repository starts with manual commits.
- **Links.** Library files must not depend on state. Does anything tracked
  link into `kb/reports/state/` today?
- **Binary stores.** SQLite files diff badly in Git. Keep, export or exclude?
- **Effect on retention choices already made.** The
  [ingest working directory case](../decision-lifecycle-evidence/ingest-working-directory.md)
  ends by deleting run records once one decision is made. A durable state
  repository changes that calculation.
- **The fixed boundary it touches.** The decision-lifecycle workshop says not
  to create duplicate primary process records. State files are not session
  traces, but the boundary should be restated if this goes ahead.

## Scope

This workshop permits design work, the measurements and checks listed above,
and deleting the abandoned review data that the state README already permits.
It does not authorize creating or pushing to a public repository; that needs
the operator's explicit go-ahead after the checks.

Coordinate with [decision-lifecycle-evidence](../decision-lifecycle-evidence/README.md),
which owns the retention economics, and
[lineage-mechanisms](../lineage-mechanisms/README.md), which owns general
derived-material retention design.

## Completion

Close when one of these holds:

- the repository exists, the pre-publication checks are recorded as done, and
  the state README and storage architecture describe it; or
- the idea is dropped, with the deciding reason recorded where a later reader
  will look, such as the state README.
