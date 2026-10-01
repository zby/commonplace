---
description: "Job of an analyse-agentic-system run: write the public synthesis once the reconciled records have passed independent verification"
type: types/instruction.md
---

# Synthesize the verified records

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `round` | `first` or `after-blockers` | Always |
| `boundary` | Absolute path of the frozen boundary and Source register | Always |
| `runtime` | Absolute path of the runtime member | Always |
| `memory` | Absolute path of the accepted memory member | Always |
| `epistemic` | Absolute path of the epistemic member | Always |
| `reconciliation` | Absolute path of the settled reconciliation member | Always |
| `previous-synthesis` | Absolute path of the first synthesis | `after-blockers` |
| `verification` | Absolute path of the synthesis verification naming blockers | `after-blockers` |

## Task

Write `output` with exactly these sections:

```markdown
## Description

## Bounded synthesis

## Limitations
```

The supplied overview type governs the synthesis and limitations. Read the
members for their findings and resolve amended or superseded records through
the reconciliation. Do not reconcile records, return work to an analyst, or
write verification text. The record loop has already passed independent
verification.

Under Description write one sentence of 50 to 250 characters describing the
system's mechanism and limits for retrieval. Code uses it as the description
of the overview and public review. Bounded synthesis and Limitations become
public text unchanged apart from links; they must read without the members'
context. Cite the records supporting each substantive statement rather than
copying their classifications. Member links resolve from the retained set
directory, using sibling names such as `runtime.md`.

Carry every paragraph marked `Unresolved conflict:` into a limitation naming
its affected IDs and prevented conclusion. A newly discovered record fault
also becomes a limitation; it does not reopen reconciliation. If a fault
cannot be stated as a limitation without making the synthesis misleading,
write `problem` and stop.

For `after-blockers`, read the previous synthesis and verification. Recheck
every carried statement against the records and resolve each blocker by
correcting the public text or stating its supported limit. This is the one
synthesis correction round. Every cited ID must resolve in the supplied set.
