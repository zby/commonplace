---
type: types/type-spec.md
name: improvement-run-answers
description: "The open items of one improvement run and the decisions made on them, one item per decision, with required reasons"
schema: ./improvement-run-answers.schema.yaml
---

# Improvement run answers

The `answers.md` member of an [improvement run](./improvement-run.md): every
point the run left undecided, and what was later decided there. Open items
are part of the [unresolved frontier](../../reference/definitions/unresolved-frontier.md).

Experimental, registered on 2026-11-14 for the first run of the improvement procedure. The design and its open choices are in the [answers schema draft](../../work/decision-lifecycle-evidence/improvement-run-answers-schema.md); the schema is a starting point and is expected to change.

One item is the smallest thing that can be accepted or rejected by itself.
`atom` names the instruction that produced the proposal and `proposal` the
change, in words a decider can judge. `agent-note` holds the proposing
agent's view and is never a decision. `state` is `pending`, `approved`,
`rejected`, `deferred` or `expired`. A rejection, deferral or expiry carries
a `reason`, a deferral also its `revisit` condition, and a decision made by
a workflow always a reason. `decided-by` is `operator`, the path of the
instruction a deciding workflow followed, or `rule` for an expiry.
`applied-in` names the run whose edit chain applied an approved item.

## Template

````markdown
---
type: reports/types/improvement-run-answers.md
description: "{What the run left open on which note}"
note: {note path}
items:
  - id: "1"
    atom: {instruction path}
    kind: edit
    proposal: "{the change}"
    agent-note: "{the agent's view and how sure it is}"
    text-sha256: {sha256}
    state: pending
    applied-in: null
---

# {Title}

{Prose.}
````
