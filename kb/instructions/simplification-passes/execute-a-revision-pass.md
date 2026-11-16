---
description: "Use for a headless worker running one edit operation on one supplied text: the shared edit contract for its inputs, bounds and edit result"
type: types/instruction.md
---

# Execute a revision pass

Improve the supplied text within the assigned edit operation and its inputs,
without choosing additional work or publishing the result.

The edit route supplies this instruction as `execution` to every run of an
[edit operation](../../types/edit-operation.md): `commonplace-review run edit`,
and each pass of the revise workflow, including its proposing and applying
runs. It is binding execution context. It does not commission assessment,
planning, dispatch or publication.

## Inputs and bounds

Use the captured text, the operation and the inputs the request names by
role. The revise workflow supplies these roles:

- `purpose`: who the reader is and what they should notice or be able to do.
- `scope`: the only part of the text the operation may change. Without it,
  the whole text is in scope.
- `defend`: claims the operation may not narrow. Without it, no claim is
  specially protected, but claims still may not change generally.
- `brief`: the note's write brief.
- `answers`: the operator's answered list of this operation's proposals.
- `kb-role`: what the note is for in the KB, and which of its terms and claims
  other notes rely on. The full procedure supplies it from the note's role
  report. Do not rename, redefine or drop a term or claim it lists as relied
  on. When the operation would otherwise change one, leave it and say so in
  the report. Terms and claims it lists as unused carry no such limit.

An operation's own Steps section names any further role it reads, such as
`diff` or `findings`. Use the supplied copies; do not read their origins.

Run only the assigned operation. Choose edits within its bounds, not new passes,
a different purpose or a wider scope. Do not add claims or remove evidence.
Preserve qualifications, contrasts, examples and links unless the commission
explicitly permits their change; account for permitted removals in the report.
Keep the title, type, brief declaration and H1. Keep every link target unless
you name its removal under `removed-links`, and keep every quoted span: a
blockquote, or a quotation cited as verbatim. Propose title changes only in
the report. Remove `user-verified` after a substantive body change.

A `per-item` operation first proposes: return `outcome: proposed` with the
proposals and apply nothing. Each proposal's `quote` is a passage copied from
the text that occurs there exactly once. Run again with an `answers` input,
an answers file with one item per proposal, apply only the items whose
`state` is `approved`. List the `rejected` and `deferred` items with the
operator's reasons in the report. Apply no other item and introduce no new
change. The operator's answers do not widen the operation or
scope.

## Headless write briefs

Treat the captured write brief as binding retained intent. Keep its must-keep,
must-exclude and reserved decisions. Do not amend it or change the artifact's
`brief:` field. Use the captured input rather than rereading the live brief.

If the purpose, protected claims, scope, answers or operation conflicts with
the brief, use the worker-problem output and stop. Approval of a selection or
publication does not authorize amending the brief. The operator must resolve
that commission change outside the run.

## Return and verification

Write only the outputs named by the request: the edit result and, for
`outcome: changed`, the complete candidate text. Do not edit the checkout,
commit, launch further work or approve proposals. Return `outcome: unchanged`
when no edit is warranted. The report lists the changes and the items noticed
but not applied. Report an unresolved prerequisite through the worker-problem
output rather than guessing or broadening the task.

Before returning a candidate, check that each change belongs to the assigned
pass and scope and that each removed element is accounted for. The controller
checks artifact validation and preserved fields; these mechanical checks do
not establish that the edits preserve meaning. Do not run software tests for
a note-editing task. The candidate remains private until the controller obtains
explicit final-publication approval.
