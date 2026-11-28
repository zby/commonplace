---
description: "Proposal: let a cross-harness sub-worker edit the target directly when a concrete assignment cannot be handled by returning suggested edits to the caller"
type: reference/types/design-proposal.md
---

# Write mode for cross-harness sub-workers

Keep suggested edits as the default: the worker returns them and the caller
applies any it has checked and is authorized to make. Reopen the write-mode
question only when the operator names a concrete assignment for a model
unavailable on the calling harness and returning suggested edits is
insufficient for that assignment.

## Current state (as of 2026-11-28)

The shipped [sub-worker command](../commands.md#commonplace-sub-worker) and
[verify skill](../../instructions/verify/SKILL.md) have delivered a Fable
review. [ADR 086](../adr/086-projects-read-the-library-from-the-installed-package.md)
authorizes that read-mode check, not edits to the target. Delivering a review
establishes that the caller can receive suggestions, not that the worker
needs to apply them.

## Decision if the need arises

With a write mode, the caller would give the worker an explicit grant for
named target paths. The worker would edit without committing; the caller
would inspect the diff and decide what to integrate. Choosing a model would
not by itself grant write access.

The [task command](../commands.md#commonplace-task) demonstrates that a
headless worker can edit a checkout. It does not solve the attribution
problem: if two writers change a dirty draft, a before-and-after comparison
cannot separate their edits. Before adopting write mode, decide how to keep
the worker’s changes distinguishable, whether the harness can enforce the
named paths, and what the caller does after a partial or out-of-scope edit.
Then decide whether the assignment warrants a further exception to ADR 086.
Until that case arises, no implementation is needed.
