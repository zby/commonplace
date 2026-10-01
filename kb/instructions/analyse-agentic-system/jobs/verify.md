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
| `set-check` | Absolute path of the structural check of the assembled set. | Always |

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

Check that every unresolved conflict is marked `Unresolved conflict:` with
its IDs, evidence and prevented conclusion. Record the checked routes and
material dispositions, and the check of every source anchor, canonical ID,
evidence status, boundary, member, limitation and blocker. A known
assessment unsupported by its records is a blocker; properly scoped explicit
uncertainty is not. Structural validation does not perform this check, but
every failure the set check lists is a blocker too. Under Blockers write
exactly `none`, or a Markdown list with one `- ` entry per blocker, giving
the member and IDs it affects and what would resolve it; indent any
continuation line. Anything else is refused, including `None.` or
`none found`. Code continues only on `none`: a blocker list starts another
reconciliation round, which gets your verification, and in the last round it
stops the run.
