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

## Situation

The record and profile loops have passed and a synthesizer has written the
public account from the accepted members: a retrieval description, a bounded
synthesis and limitations. Those become the overview and the published
review, read by people who will not open the members.

## Mission

Judge the synthesis against the records it cites and the supplied overview
and synthesis types, and write the verification to `output` under the
supplied verification type, with `verifies: synthesis`, `run-id` and the
`reviewed-boundary` of `boundary`.

When you are done, every substantive statement has been checked against the
records it cites, including supersessions in the reconciliation; the text has
been read as its public readers will read it, without the members; and every
limit the record and profile verifications declared, and every
`Unresolved conflict:` in the reconciliation, is present in Limitations with
its affected IDs and the conclusion readers should withhold. The overview
type fixes what the synthesis and limitations must contain: supported
contributions kept beside unresolved parts without an aggregate completeness
claim, independent properties assessed independently, no bundled negative,
no improved capacity inferred from trace-fed retention.

## Boundaries

You write no correction. A blocker is an unsupported statement, a hidden
coverage gap, an unwarranted absence or completeness claim, or a declared
limit missing from Limitations; explicit faithful uncertainty is not. A record
fault you discover here is a limit to be stated in the public text, not a
reason to reopen reconciliation; if it cannot be stated without making the
synthesis misleading, write `problem` and stop. Structural acceptance does not
establish support.

Code sends your blockers to the synthesizer for one correction; blockers
after it stop the run before publication.

Run the acceptance check before submitting.
