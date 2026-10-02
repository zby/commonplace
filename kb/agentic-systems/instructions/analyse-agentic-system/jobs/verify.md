---
description: "Job of an analyse-agentic-system run: independently check the reconciled records and memory profile before public synthesis"
type: types/instruction.md
---

# Verify the reconciled records

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `reconciliation` | Absolute path of the retained reconciliation member. | Always |
| `runtime` | Absolute path of the runtime member. | Always |
| `memory` | Absolute path of the selected memory report, copied unchanged into the set. | Always |
| `epistemic` | Absolute path of the epistemic member. | Always |
| `set-check` | Absolute path of the structural check of the record set. | Always |
| `memory-return` | `yes` when a later reconciliation round may return findings to the memory analyst; otherwise `no`. | Always |

## Task

Read the record set from `boundary`, `runtime`, `memory`, `epistemic` and
`reconciliation`, and read `set-check` for structural validation findings.
There is no overview or public synthesis yet; judge records only. Write
`output` with exactly these sections, which go into the overview's
Verification and blockers:

```markdown
### Record verification

### Blockers
```

Acceptance requires valid verification sections, resolved citations and explicit
blockers when the structural check has failures.

Check the whole set, not the separate returns of the memory and epistemic
analysts, against the Memory comparison fields of the
[memory report type](../../../types/agent-memory-analysis-report.md), whose
definitions govern every profile value: scope agreement with the canonical
records across members, every scoped trace-fed write including compaction,
each push signal's consumer and selector, and the reconciliation member's
amendments and supersessions against the records they name.

Record the checked routes and material dispositions, and the check of every
source anchor, canonical ID, evidence status, boundary, member and unresolved
conflict. Structural validation does not perform this check.

Check every `Part of:` relation against the records' identities and evidence.
An unresolved parent, malformed field, self-reference or unexplained parent
of a different kind is a blocker. A valid part keeps its own fields and
status; a valid container needs no supersession. For a split supersession,
check that every replacement part is already declared and that the amendment
explains why the combined finding fails. A missing part must be returned to
memory when appropriate and permitted, or retained as an `Unresolved
conflict:` with evidence and the prevented conclusion. A multi-record
grouping must retain its comparisons rather than assert unsupported containment.

## Blockers

A blocker is a defect in the records that another reconciliation round can
repair. Reconciliation may correct its own text, amend or supersede a record
with an `Amendment:` paragraph, mark a conflict `Unresolved conflict:`, and,
when `memory-return = yes`, return a finding to the memory analyst. For each
blocker, give the member and IDs it affects and which of these repairs would
resolve it. A known assessment unsupported by its records is a blocker;
properly scoped explicit uncertainty is not. Every failure the set check
lists is a blocker too.

No job rewrites the boundary, the runtime member or the epistemic member,
and the memory member changes only through a return. A defect there that no
amendment can repair is not a blocker when the reconciliation marks it
`Unresolved conflict:` with its IDs, evidence and prevented conclusion: the
synthesis then states it as a limitation. Record it under Record
verification as a checked conflict. When such a defect is unmarked, or its
marking lacks the IDs, evidence or prevented conclusion, the blocker is the
missing marking. Never ask for the boundary or a member to be rewritten or
returned, except the memory member when `memory-return = yes`.

Judge each record as the reconciliation amends it. An original value that an
amendment replaces is not a defect.

Write `problem` instead only when the records as a whole cannot support any
bounded conclusion. A defect that limits individual findings is not that
case.

Under Blockers write exactly `none`, or a Markdown list with one `- ` entry
per blocker; indent any continuation line. Anything else is refused,
including `None.` or `none found`. Code continues only on `none`: a blocker
list starts another reconciliation round, which gets your verification, and
in the last round it stops the run.
