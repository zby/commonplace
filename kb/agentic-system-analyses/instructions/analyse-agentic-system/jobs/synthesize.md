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

## Situation

The records have passed independent verification and the memory profile has
been classified and verified. The record and profile verifications may have
declared limits: local issues the analysis is published with, each naming the
records it concerns and the conclusions readers should withhold. What remains
is the public account.

## Mission

Write the synthesis to `output` under the supplied synthesis type, with
`run-id` and the `reviewed-boundary` of `boundary` as its identity. Its
`description`, Bounded synthesis and Limitations become the overview's, so
the supplied overview type governs their content, and they must read without
the members' context.

When you are done, every substantive statement cites the records that
support it, as written and with superseded records resolved through the
reconciliation; and Limitations carries every limit the record and profile
verifications declared and every `Unresolved conflict:` in the
reconciliation, each with its affected IDs and the conclusion readers should
withhold. Code refuses a synthesis whose Limitations names none of a declared
limit's records.

## Boundaries

Do not reconcile records or write verification text; the record loop has
passed. A record fault you discover becomes a limitation; it does not reopen
reconciliation. If a fault cannot be stated as a limitation without making the
synthesis misleading, write `problem` and stop.

For `after-blockers`, read the previous synthesis and verification. Recheck
every carried statement against the records and resolve each blocker by
correcting the public text or stating its supported limit. This is the one
synthesis correction round.

Run the acceptance check before submitting.
