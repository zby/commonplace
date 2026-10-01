---
description: "Job of an analyse-agentic-system run: check the assembled set semantically and write the overview's semantic verification and blockers"
type: types/instruction.md
---

# Verify the set

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `overview-draft` | Absolute path of the overview without this verification. | Always |
| `runtime` | Absolute path of the runtime member. | Always |
| `memory` | Absolute path of the selected memory report, copied unchanged into the set. | Always |
| `epistemic` | Absolute path of the epistemic member. | Always |
| `set-check` | Absolute path of the structural check of the assembled set. | Always |

## Task

Read the assembled set from `overview-draft`, `runtime`, `memory`, and `epistemic`, and read `set-check` for the structural validation findings. Write `output` with exactly these sections, which go into the overview's Verification and blockers:

```markdown
### Semantic verification

### Blockers
```

Acceptance requires that the overview with your verification adds no
validation failures to those the set check already lists.

Check the whole set, not the separate returns of the memory and epistemic analysts, against the Memory comparison fields of the [memory report type](../../../types/agent-memory-analysis-report.md), whose definitions govern every profile value: scope agreement with the canonical records across members, every scoped trace-fed write including compaction, each push signal's consumer and selector, and the Reconciliation's amendments and supersessions against the records they name.

Record the checked routes and material dispositions, and the check of every source anchor, canonical ID, evidence status, boundary, member, limitation and blocker. A known assessment unsupported by its records is a blocker; properly scoped explicit uncertainty is not. Structural validation does not perform this check, but every failure the set check lists is a blocker too. Under Blockers write exactly `none`, or a Markdown list with one `- ` entry per blocker, giving the member and IDs it affects and what would resolve it; indent any continuation line. Anything else is refused, including `None.` or `none found`. Code continues only on `none`: a blocker list starts another reconciliation round, which gets your verification, and in the last round it stops the run.
