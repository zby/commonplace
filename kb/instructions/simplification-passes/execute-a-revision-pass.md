---
description: "Use for a headless revision worker whose artifact, pass, purpose, scope and protected claims are already fixed; return only the assigned candidate or selection list and report"
type: types/instruction.md
---

# Execute a revision pass

Improve the supplied text for the stated purpose within the assigned pass and
scope, without choosing additional work or publishing the result.

The revision workflow supplies this instruction as `workflow` to every pass,
candidate-list and approved-list application worker. It is binding execution
context, whether the caller supplied a fixed plan or an assessment chose the
plan. It does not commission assessment, planning, dispatch or publication.

## Inputs and bounds

Use the captured artifact, pass instruction, purpose, scope, protected claims
and write brief supplied by the worker request. An omitted scope means the
whole artifact; an empty defended-claims list adds no specially protected
claims but does not permit changing claims generally.

Run only the assigned pass. Choose edits within its bounds, not new passes,
a different purpose or a wider scope. Do not add claims or remove evidence.
Preserve qualifications, contrasts, examples and links unless the commission
explicitly permits their change; account for permitted removals in the report.
Keep the title, type, brief declaration and H1. Propose title changes only in
the report. Remove `user-verified` after a substantive body change.

For a candidate-list request, propose selections without applying them. For
an approved-list request, apply only entries left in the approved list and
marked replace; do not restore struck entries or introduce new ones.
Selection approval does not widen the pass or scope.

## Headless write briefs

Treat the captured write brief as binding retained intent. Keep its must-keep,
must-exclude and reserved decisions. Do not amend it or change the artifact's
`brief:` field. Use the captured input rather than rereading the live brief.

If the purpose, protected claims, scope, approved list or pass conflicts with
the brief, use the worker-problem output and stop. Approval of a selection or
publication does not authorize amending the brief. The operator must resolve
that commission change outside the run.

## Return and verification

Write only the outputs named by the request. Do not edit the checkout, commit,
launch further work or approve proposals. For an editing request, return the
complete candidate, or the unchanged text when no edit is warranted, and the
pass report with items noticed but not applied. For a list request, return
only the requested list. Report an unresolved prerequisite through the
worker-problem output rather than guessing or broadening the task.

Before returning a candidate, check that each change belongs to the assigned
pass and scope and that each removed element is accounted for. The controller
checks artifact validation and preserved fields; these mechanical checks do
not establish that the edits preserve meaning. Do not run software tests for
a note-editing task. The candidate remains private until the controller obtains
explicit final-publication approval.
