# First operability slice result — 2026-08-31

This result compares the bounded implementation with the
[pre-change baseline](./baseline-2026-08-31.md). It does not evaluate the
audit's deferred upgrade, operation-packet, retrieval, receipt, or learning
architecture.

## Compact validation

`commonplace-validate notes` retained exit status, validation scope, every
warning and failure, material notices, and an exact detailed command. It moved
the prior per-artifact transcript behind `--full` and added the structured
`commonplace.validation.v1` result behind `--json`.

| Measure | Before | After |
|---|---:|---:|
| Output lines | 9,686 | 31 |
| Output bytes | 223,847 | 3,571 |
| Elapsed seconds | 3.03 | 2.46 |
| Failures hidden | 0 | 0 |
| Warnings hidden | 0 | 0 |

The after result included 21 orphan notices. The byte reduction was about
98.4%; the purpose is decision-ready output, not the percentage itself.

## Lifecycle validation and reconciliation

The new `commonplace-validate lifecycle` target initially reported eight
missing-framing failures and twenty warnings: eighteen unregistered top-level
directories plus one completed backlog checklist and one absent recurring
output.

Reconciliation established that empty directories contain no Git-retained
project state, so the validator ignores them. Every non-empty top-level
directory is now registered as active or, for `multistage`, identified as a
workflow namespace. The completed backlog task moved to `kb/tasks/completed/`.
The recurring explanatory-reach review now has its declared log. The
`curiosity-prompts` experiment received framing that names its remaining
retained-report relocation. The obsolete `semantic-search-replacement`
workshop was deleted after confirming that commit `4ec3174c` removed qmd from
active instructions and no durable artifact depended on its files.

The same lifecycle command then reported zero failures and zero warnings over
68 inspected subjects. The diagnostic rule IDs are:

- `lifecycle.workshop.unregistered`
- `lifecycle.workshop.missing-framing`
- `lifecycle.task.backlog-complete`
- `lifecycle.task.recurring-output-missing`

Warnings request reconciliation; they do not authorize registration, movement,
file creation, or deletion.

## Read-only status pilot

`commonplace-status` now composes project and command versions, Git state,
notes validation, lifecycle validation, and stable next-action IDs. The
default live result was eight lines and 346 bytes in 3.23 seconds. It reported
no next action from those bounded inputs.

Review warnings, jobs, and freshness state are intentionally excluded from the
default. The review system is not yet used regularly, and stale pairs are
currently normal accumulated state rather than a default operator signal.
`commonplace-status --review` opts into that projection. A code TODO requires
reconsidering the default only after the review system is stable and regularly
used.

The pilot is read-only: it runs deterministic checks, reads Git and the
operational store when explicitly requested, and emits drill-down commands. It
does not rank with a model, schedule work, apply changes, or become authority
for displayed state.

## Verification

- Focused CLI, lifecycle, and documentation tests passed.
- Ruff passed on every changed Python file.
- The complete suite passed after the final status-default change: 634 tests in
  40.20 seconds.
- Every changed KB artifact validated cleanly, and lifecycle validation passed
  with zero findings. Collection-wide `work` validation remained blocked by an
  unrelated concurrent missing-schema failure under
  `kb/work/analyse-agentic-system/`; that artifact was not changed here.
- The editable user-level tool was reinstalled after the new entry point; the
  install exposed `commonplace-status` among 23 executables.
