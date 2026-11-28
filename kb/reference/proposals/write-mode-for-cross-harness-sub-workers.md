---
description: "Proposal: extend the read-mode cross-harness verification trial to writing subtasks if an actual assignment justifies the extra permission and coordination"
type: reference/types/design-proposal.md
---

# Cross-harness sub-worker command with verification as first use

A model available only on another harness may be better suited to a writing
assignment. Consider a write mode for `commonplace-sub-worker` when the
operator has such an assignment. It would let the calling agent commission
edits rather than carry a suggested patch between sessions. Do not enable
writing merely because a read-mode profile can technically write files.

## Current state (as of 2026-11-28)

- **Adopted for trial:** [ADR 086](../adr/086-projects-read-the-library-from-the-installed-package.md)
  permits an operator-directed read-mode check with a named model unavailable
  through the native worker facility. The [command](../commands.md#commonplace-sub-worker)
  and [verify skill](../../instructions/verify/SKILL.md) define that trial.
  The exception does not cover writing or another skill's workers.
- The trial uses Workjig's one-call interface. Its checkout guard reports
  changes observed while a run was open; it cannot attribute them to the
  worker. Some profiles cannot enforce a read-only checkout.
- The operator expects different models to excel at different tasks. This
  motivates the trial; it is not a measured advantage. No verification
  result by itself establishes a case for write access.

## Options

**Keep the read-mode command.** A worker can suggest a local fix; the
calling agent checks it and makes any authorized edit. This preserves the
caller's control without requiring a second writer in a shared checkout.
For a model available on the caller's harness, use the native sub-agent.

**Add a writing subtask.** The caller would name a profile, a write grant and
the paths it owns. The worker would edit but not commit. The caller would
inspect the diff and integrate it. `commonplace-task` already demonstrates a
headless worker editing in the checkout, but its runbook and commit check do
not establish who made each edit in a dirty tree. The shared model roster would stay unchanged. A write grant would need
its own selection rule; the model name alone cannot authorize edits.

**Use a harness extension instead.** If a writing assignment needs ongoing
conversation, a one-shot handoff may be the wrong interface. An extension
could preserve a native parent-child relationship, but feasibility on every
calling harness has not been established. Do not replace existing native
worker paths to implement this option.

## Adoption criteria

Keep the read-mode trial narrow. In an actual verification, did the worker
catch a consequential issue that the caller missed, and what did it cost to
check the findings? If checking them costs more than the saved work, or
applied findings often need reverting, reconsider automatic integration.
If a missing follow-up repeatedly blocks useful work, investigate the
extension option before broadening the one-shot command.

Revisit writing when the operator names a concrete assignment for a model
unavailable on the calling harness and returning suggested edits is
insufficient. Before granting writes, decide how the caller can distinguish
the worker's changes from concurrent edits, what happens on a partial or
out-of-scope edit, and what further exception to ADR 086 is warranted.
Until then no write mode or migration of
`commonplace-task` is required.
