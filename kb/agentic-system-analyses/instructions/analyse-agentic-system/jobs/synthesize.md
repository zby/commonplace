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

Write the synthesis to `output` under the supplied synthesis type, with
`run-id` and the `reviewed-boundary` of `boundary` as its identity. Its
`description`, Bounded synthesis and Limitations become the overview's, so
the supplied overview type governs their content. Read the members for their
findings as written, and resolve superseded records through the
reconciliation. Do not reconcile records or write verification text: the
record loop has already passed independent verification.

Carry every paragraph marked `Unresolved conflict:` into a limitation. A
record fault you discover becomes a limitation too; it does not reopen
reconciliation. If a fault cannot be stated as a limitation without making
the synthesis misleading, write `problem` and stop.

For `after-blockers`, read the previous synthesis and verification. Recheck
every carried statement against the records and resolve each blocker by
correcting the public text or stating its supported limit. This is the one
synthesis correction round. Every cited ID must resolve in the supplied set.

Run the acceptance check before submitting.
