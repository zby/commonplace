---
description: "Decision that multistage, AutoReason, article-staging and memory-landscape run bundles move into kb/reports/state and are kept after the workflow ends; the analysis process record is the one exception"
type: reference/types/adr.md
tags: []
status: accepted
---

# 129-Workflow run bundles live under the state tree and are kept

**Status:** accepted
**Date:** 2026-11-12
**Amends:** [ADR 128](./128-one-ignored-operational-tree-under-kb-reports-state.md): four workflow families whose bundles lived outside `state/` now write under it, and their rows say "kept"; the analysis process record stays outside the tree until integration copies it.

## Context

On 2026-11-11 the operator set a direction: intermediate workflow artifacts
are preserved by default in the second repository, for debugging and
inspection. Workflows with substantial churn may get exceptions later. No
size, churn rate or debugging benefit has been measured.

ADR 128 made `kb/reports/state/` the one ignored operational tree and the
publication boundary of a future state repository. An inventory of workflow
intermediate files then found four families that keep run bundles elsewhere
and delete them when the workflow finishes:

- Multistage writing runs were tracked workshops under `kb/work/multistage/`,
  removed on successful closure. The literature-disposition assessment reuses
  such a run.
- AutoReason revision bundles under `kb/work/revise-autoreason/` were deleted
  on apply or decline.
- Article staging packages under `kb/work/staging/<slug>/` were deleted on
  restaging and on publication.
- Memory-landscape synthesis built its matrix, working query ledger and draft
  at a temporary path the caller chose.

Each bundle mixes durable and process material in one directory and then
deletes the directory. The preservation default forbids that deletion. The
location outside `state/` meant that versioning the tree would not capture
these bundles even if they survived.

The agentic-system analysis workflow also keeps a process record outside the
tree, but for a different reason. Its durable outputs already enter the main
record by design: integration publishes each accepted set under
`kb/agentic-system-analyses/retained/` with its artifact members,
verification reports, reconciliation and manifest. Its process record
(`run.json`, the effects journal, and the attempts, versions, judgments,
handouts and sequence under the run's `state/`) lives in a commit-bound
worktree under `kb/agentic-system-analyses/state/<run-id>/`. The worktree is
a checkout of main, so that path cannot move without changing how runs are
isolated. The workflow does not delete the record.

## Decision

The four families write their bundles under `kb/reports/state/`, one
directory per family:

- `multistage/multistage-write-<short-topic>-<YYYYMMDD>/` for multistage
  writing runs, including literature-disposition assessments;
- `revise-autoreason/<source basename>.<YYYYMMDD-HHMMSS>/` for AutoReason
  revision bundles;
- `staging/<slug>/<YYYYMMDD-HHMMSS>/` for article staging packages;
- `agent-memory-landscape/<YYYYMMDD-HHMMSS>/` for the synthesis matrix,
  working query ledger and draft.

Each bundle is kept after its workflow finishes. Closure, apply, decline,
restaging and publication no longer delete it. Publication of an article
copies the appendix and reference files into `kb/articles/` and leaves the
staging package in place. Restaging writes a new timestamped package beside
the old one. Where a workflow overwrites a file inside its own bundle, as a
repair does, the overwrite stands; no version capture is added.

Multistage runs change record status. They were the only family tracked in
main. After the move, a run in progress does not appear in main's history,
and the promotion commit no longer carries the run beside the promoted
artifact. This is accepted because the run is process material and the
promoted artifact is the durable product. The `kb/work/` collection contract
no longer carries carve-outs for multistage or AutoReason run directories.

The agentic-system analysis process record is the one ignored operational
tree outside ADR 128's rule. It stays in the run's worktree until
integration copies it into `kb/reports/state/` in the origin checkout. That
copy is a separate code change, not made by this decision. Because the
workflow does not delete the record, nothing is lost while it waits.

Three kinds of material do not move:

- Source snapshots and code checkouts stay in the private snapshots
  repository and local checkouts. They sit behind a publication boundary;
  they are inputs, not intermediates.
- Workflows that produce no separate file, such as code review,
  hidden-failure review and Roughdraft markup, get no new output. The
  preservation default keeps what is produced; it does not authorize new
  production.
- Ordinary workshops stay under `kb/work/`. They are the workshop layer, not
  workflow run bundles.

## Considered alternatives

Keep the bundles as tracked workshops in main and stop deleting them.
Rejected: kept run bundles would accumulate in the workshop layer as
permanent process material, which the workshop contract does not hold, and
every run would mix with library history. Main's history would capture
multistage runs, but AutoReason, staging and synthesis bundles were never
committed there, so their capture would need new commits in main.

Move the bundles but keep the delete steps. Rejected: the bundles would sit
in the right tree only until the workflow finished. A state repository could
capture them only if a commit happened to fall between creation and
deletion, which no workflow arranges.

Add per-file version capture now, so that overwrites inside a bundle are
also kept. Deferred: the capture approaches (commit before replacement, or
immutable copies committed later) remain open in the decision-lifecycle
workshop. No churn has been measured, and the state repository that would
hold the versions does not exist yet. Keeping whole bundles needs no capture
machinery.

Move the analysis process record in the same decision. Rejected for now: the
record lives in a worktree that is a checkout of main, so moving it requires
integration to copy it into the origin's `kb/reports/state/`. That is a code
change to the analysis workflow with its own tests. The record is not
deleted, so deferring the copy loses nothing.

Name a directory per workflow differently, for example by grouping all
writing workflows under one directory. None developed: one directory per
producing family follows ADR 128's layout, and the names match the skills
that own them.

## Consequences

A bundle that existed only until closure now survives it. A reader debugging
a promoted note, an applied revision, a published article or a synthesis can
open the run that produced it. The state README carries one row per family,
so the cleanup rule is stated where ADR 128 put it.

The tree grows with every run, and no pruning rule exists. Multistage runs
lose their visibility in main: a reviewer of a promotion commit sees the
promoted artifact, not the reviews behind it, unless they open the state
tree. Active multistage runs are no longer listed in `kb/work/README.md`.
Bundles are ignored by main, so they exist only on the machine that ran the
workflow until a state repository commits them.

The operativity path: the producing skills and instructions consume the
decision. Each names its state-tree path and drops its delete step, and an
agent running the workflow follows the skill with the force of a loaded
procedure. The `kb/work/` collection contract stops admitting the two run
namespaces, which governs where agents may create workshop directories. The
state README's rows tell a reader or the operator what deleting each bundle
loses.

This decision stops at location and the keep rule. Location is not
retention: the state repository, once created, captures a bundle only when
it is committed there. Commit cadence, history pruning, version capture
inside a bundle and churn exceptions stay with the
[public state repository workshop](../../work/public-state-repository/README.md)
and the [decision lifecycle and evidence workshop](../../work/decision-lifecycle-evidence/README.md).
It does not cover workflows outside the four families, and it does not make
anything in the tree safe to publish.
