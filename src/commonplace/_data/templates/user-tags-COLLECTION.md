---
type: types/collection-contract.md
---

# Tag heads for kb/tags/

These defaults are ready to use. Customize them only when the project needs
different conventions. Once installed, this contract belongs to your project;
Commonplace does not synchronize it with later template changes.

## What this collection holds

One head per tag: `kb/tags/<tag>-README.md`, type `types/tag-readme.md`. The
filename names the tag. A head introduces what the tag gathers, in the words
a reader would search for, and picks a few entries with a phrase saying why
each matters. It is the page a tag link leads to on the published site.

Every tag in use has a head. Validation reports a tag on an eligible artifact whose head does not exist; write the head or drop
the tag. A tag not worth a head is not worth assigning.

Heads are the only artifacts here. `README.md` is the collection's landing
and carries no type.

## Tag assignment

Before assigning a tag, read its head. Assign it only when the artifact
substantively addresses the head's stated subject, question, or mechanism;
mention or background use is insufficient. When the head leaves placement
ambiguous, clarify its inclusion condition before assigning the tag. An
artifact may carry neighboring tags when it meets each condition.

A head states that inclusion condition in its opening and distinguishes
neighboring tags where they could be confused. Assignment fit is judged during
authoring and semantic review; deterministic validation does not establish it.

## Membership by collection

The generated list is grouped by collection. No registration is needed. Collection contracts govern assignment. Workflow state and source snapshots are excluded before traversal.

A head is selective. Use it for orientation and the membership collector or published listing for enumeration.

## Outbound links

Link members with a relative path (`../notes/<file>.md`) and a context phrase.
Link other heads under a `## Related Tags` heading. Do not link into
`kb/work/`.
