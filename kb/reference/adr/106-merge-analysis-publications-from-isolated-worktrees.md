---
description: Analysis run IDs include a prepared worktree token, and completed publications enter main through a guarded Git merge
type: reference/types/adr.md
status: accepted
---

# 106 — Merge analysis publications from isolated worktrees

**Status:** accepted
**Date:** 2026-10-05

## Context

An analysis publishes in a detached worktree pinned to its method commit.
Several worktrees could allocate the same date, source slug and local run
number. That blocked replacement publication and made run citations
ambiguous. Copying a retained set into `main` could also overwrite a newer
publication without detecting that its method commit had an older incumbent.
Ignored run state carries failure evidence that Git history does not retain.

## Decision

Preparation gives each worktree a random 12-hex token in its ready record.
New analysis IDs have the form `AAS-<date>-<source-slug>-<token>-<nn>`.
`Orchestrator.start` passes its existing base path to `run_location(base)`;
the analysis workflow reads the bound preparation record and refuses an
unprepared start. Opening checks the token even for an explicitly named run.
Existing legacy runs and retained sets remain readable.

After a complete run and handoff, separate operator authorization permits
`commonplace-workflow integrate-analysis <run>`. It commits only the changed
retained source set and incumbent archive on `analysis/<run-id>`, whose parent
is the worktree's method commit. It then merges that branch into the origin
checkout on `main`, provided the method commit is an ancestor of `main`.
Conflicts are aborted and left for an operator decision; the branch and
worktree remain. No automated side preference is permitted.

Run directories stay ignored. Routine worktree removal requires every run
in the worktree to be complete and merged, no pending integration decision,
and extracted audit evidence or an operator statement that none is needed.
It is never automatic. Failed runs stay outside this cleanup rule because
their traces and rejected outputs are evidence; disposal needs a separate
explicit operator decision. New audit evidence records identify `run-id`,
`method-commit` and `source-revision`.

## Considered alternatives

**Copy the retained set into `main`.** This would bypass Git's comparison
against the method commit and could silently replace a newer analysis. Merge
conflicts preserve the choice for the operator.

**Use a fresh token per run or pass a token as a parameter.** A per-run token
would lose the link to the worktree, while a parameter would make the caller
copy the preparation value. A worktree token plus the existing local counter
keeps repeated starts possible with one record.

**Document Git steps without a command.** The stage scope, ancestry check
and conflict recovery require exact refusals. A command enforces them while
the skill keeps the separate authorization boundary.

**Delete failed worktrees with other terminal runs.** Failure may include
uncertain public state. Even after that is resolved, the failed run's trace
may be the only account of the defect. Routine cleanup excludes it.

**Validate the candidate result against current `main` before merging.** This
would add a stronger gate, but the operator accepted the possibility that an
older-method result may be invalid under current contracts. The run retains
its method and source pins; this decision does not claim current validity.

## Consequences

The preparation record and start/open checks enforce run identity in code.
The integration command enforces path and ancestry checks at Git operation
time. The analysis skill, publication instruction and command reference
supply the authority and operator procedure. Local type templates teach the
new ID; their schemas continue accepting legacy IDs. Audit instructions
teach evidence record keys.

Git now detects competing publications for the same source. A completed run
can remain in its worktree until integration is authorized, and a conflict
retains recoverable evidence. Branches and ignored worktrees still need
operator cleanup. This decision applies to analysis runs prepared in
Commonplace source worktrees; it does not make consuming-project workflows
use this preparation channel, and a clean merge does not certify report
validity under the current method.
