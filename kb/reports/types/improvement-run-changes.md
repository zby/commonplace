---
type: types/type-spec.md
name: improvement-run-changes
description: "The edit chain of one improvement run: each applied edit operation in order, with the hashes of the text it started from and produced"
schema: ./improvement-run-changes.schema.yaml
---

# Improvement run changes

The `changes.md` member of an [improvement run](./improvement-run.md).

Experimental, registered on 2026-11-14 for the first run of the improvement procedure. The design and its open choices are in the [run type draft](../../work/decision-lifecycle-evidence/improvement-run-type.md); the schema is a starting point and is expected to change.

`edits` lists the applied edit operations in order. `atom` is the path of
the operation, `from-sha256` the text it was given and `to-sha256` the text
it returned; both texts are stored under the run's `texts/`. `item` names
the open item that authorised the edit, as `<run directory>#<id>`, where
one did. A run that applied no edit has an empty list, and its
`final-sha256` equals its `start-sha256`.

## Template

````markdown
---
type: reports/types/improvement-run-changes.md
description: "{Which edits the run applied, in order}"
note: {note path}
start-sha256: {sha256}
final-sha256: {sha256}
edits: []
---

# {Title}

{Prose.}
````
