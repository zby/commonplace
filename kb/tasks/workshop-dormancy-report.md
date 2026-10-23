# Report: Workshop dormancy

List the workshops under `kb/work/` that have not changed in a while, so the
operator can see which open workshops are dormant without walking the
directory. The report only observes; it never edits a workshop, the active
workshops list or any navigation surface.

This file is a stable runbook. Do not edit it per run; only change it when
scope or process changes.

## Scope

- `kb/work/*/` — every workshop directory
- `kb/work/README.md` — read only, to tell listed from unlisted workshops

## Cadence

Weekly. Due when the log's latest dated section is older than seven days or
absent.

## Run Procedure

1. For each workshop directory, find the date of its last commit:
   `git log -1 --format=%cs -- kb/work/<name>`.
2. Classify: `dormant` when the last commit is more than 60 days old,
   `quiet` when more than 21 days, `active` otherwise.
3. Note whether each workshop has an entry in the Active Workshops list of
   `kb/work/README.md`.
4. Compare with the previous section of the log: which workshops changed
   class since the last run, and which dormant workshops are new.

## Output

Record findings in `kb/tasks/workshop-dormancy-report-log.md`.
Append one dated section per run (for example `## 2026-10-30`) with:

- Counts: active, quiet, dormant, and how many of the dormant are listed
- Dormant: a table of workshop, last commit date, listed yes/no
- Changes since last run: workshops that entered or left `dormant`, or
  "first run" when there is no previous section

## Write scope

`kb/tasks/workshop-dormancy-report-log.md` only. The run stages
exactly this file and commits it with the subject
`Run recurring task workshop-dormancy-report`.

## Consumer

The operator reads the latest `Dormant` table when triaging the active
workshops list. Demotion or closure is a separate decision and, if it is
ever automated, a separate task.
