---
type: types/type-spec.md
name: improvement-run-report
description: "Identity, ending and prose report of one improvement run; the member the other members of the run take their identity from"
schema: ./improvement-run-report.schema.yaml
---

# Improvement run report

The `report.md` member of an [improvement run](./improvement-run.md). It is
written at the first step with `ending: open` and completed when the run
closes.

Experimental, registered on 2026-11-14 for the first run of the improvement procedure. The design and its open choices are in the [run type draft](../../work/decision-lifecycle-evidence/improvement-run-type.md); the schema is a starting point and is expected to change.

`note` is the repository path of the note. `variant` is the path of the
instruction the run followed. `start-commit` is the commit at which the
variant and its atoms are to be read; `start-sha256` hashes the note's text
at the start and `final-sha256` the text at the close. `ending` is `open`,
`stopped` (a strong higher-order proposal ended the run without edits),
`applied` (every permitted edit was made and no item was left open) or
`partly-applied` (at least one item was open at the close). The ending
never changes after the close.

The body states what was fixed, what was left open and why, what the
re-review returned, and any step the run skipped.

## Template

````markdown
---
type: reports/types/improvement-run-report.md
description: "{What ran on which note and how it ended}"
note: {note path}
variant: {variant instruction path}
start-commit: {commit}
start-sha256: {sha256}
started-at: "{timestamp}"
ending: open
final-sha256: null
ended-at: null
---

# {Title}

{Prose.}
````
