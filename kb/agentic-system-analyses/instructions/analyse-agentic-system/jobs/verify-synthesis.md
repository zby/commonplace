---
description: "Job of an analyse-agentic-system run: independently verify public statements and limitations against the settled records"
type: types/instruction.md
---

# Verify the public synthesis

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `synthesis` | Absolute path of the synthesis being judged | Always |
| `boundary` | Absolute path of the frozen boundary and Source register | Always |
| `runtime` | Absolute path of the runtime member | Always |
| `memory` | Absolute path of the accepted memory member | Always |
| `epistemic` | Absolute path of the epistemic member | Always |
| `reconciliation` | Absolute path of the settled reconciliation member | Always |

## Task

Write `output` with exactly these sections:

```markdown
### Synthesis verification

### Blockers
```

Judge every substantive synthesis statement against the records it cites,
including amendments and supersessions in the reconciliation. Check that
Description, Bounded synthesis and Limitations meet the supplied overview
type, read without the members' context, and carry every `Unresolved conflict:`
into a limitation with its affected IDs and prevented conclusion. Record the
checked claims and limits. Structural acceptance does not establish support.
List every referenced ID in full in your output; ranges such as
`RT-RTE-1 through RT-RTE-5` and `RT-BAP-1–RT-BAP-2` are refused.

Write no correction. Under Blockers write exactly `none`, or a Markdown list
with one `- ` entry per blocker, its affected statement and IDs, and what
would resolve it. Indent continuation lines. An unsupported statement is a
blocker; a faithfully stated uncertainty is not. Record faults discovered
here must be bounded in the public text; they do not reopen reconciliation.
If a fault cannot be stated as a limitation without making the synthesis
misleading, write `problem` and stop.

Code sends a blocker list to the synthesizer for one correction round. If
the final verification still names blockers, the run stops before publication.
