---
description: "Job of an analyse-agentic-system run: reconcile the members of the three analysts, and write the overview's reconciliation, synthesis and limitations"
type: types/instruction.md
---

# Reconcile the analysts' members and write the synthesis

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `round` | `first`, `after-correction`, or `after-blockers`. | Always |
| `may-return` | `yes` permits returning findings; `no` prohibits it. | Always |
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `runtime` | Absolute path of the runtime member. | Always |
| `memory` | Absolute path of the selected memory report. | Always |
| `epistemic` | Absolute path of the epistemic member. | Always |
| `previous-reconciliation` | Absolute path of the previous reconciliation. | `after-correction` or `after-blockers` |
| `verification` | Absolute path of the verification whose blockers you must resolve. | `after-blockers` |
| `set-check` | Absolute path of the structural check for that verification. | `after-blockers` |

## Task

Write `output`, with exactly these sections. The last three go into the overview unchanged; the [overview type](../../../types/agentic-system-analysis-overview.md) fixes what each holds:

```markdown
## Description

## Reconciliation

## Bounded synthesis

## Limitations
```

## Reconcile

Write every section from the members as they are; when `round` is `after-correction` or `after-blockers`, read `previous-reconciliation` and recheck anything you carry over from it rather than copying its text.

Resolve duplicates, corrections and anchored conflicts under the shared
record contract's amendment grammar. Report independent convergence only
when the analysts reached it independently. Recheck shared-route ownership. Attach the admission fields of memory routes from the memory analyst's findings rather than tracing those mechanisms twice. The memory analyst's `memory-comparison` profile stays in the memory member with its scope, per-value evidence bases and records, coverage assessments, uncertainties, and rationale preserved; check it axis by axis, under the definitions of the [memory report type](../../../types/agent-memory-analysis-report.md)'s Memory comparison fields, against the records of the whole set, including every `EPI-` record of a transformation of retained content. Do not draft a second memory analysis, and do not silently strengthen the memory analyst's findings.

Every ID you cite, in amendments too, must resolve in the set your output makes: the Source register, the runtime member, the memory report and the epistemic member. Your output is refused with the unresolved IDs otherwise.

## Return findings to the memory analyst

When a substantive conflict needs the memory analyst, add the section `## Returned to the memory analyst`, listing each returned finding with its IDs and evidence anchor. Code then runs a correction round of the memory analyst and gives you its report in the next reconciliation. Return findings only when `may-return = yes`. When `may-return = no`, retain each unresolved conflict as explicit uncertainty in the Reconciliation and the Limitations. A malformed citation in the memory analyst's report is also a return, not something you fix.

## Resolve a verification's blockers

When `round = after-blockers`, read `verification` and `set-check`. Resolve each blocker in what you write: correct the reconciliation, the synthesis or the limitations; amend or supersede a record through an `Amendment:` paragraph; or return it to the memory analyst when the memory report is at fault. The runtime and epistemic members are not rewritten; a blocker in one of them that no amendment resolves stays a limitation. Read `previous-reconciliation` too: carry over what still holds.

## Synthesize

Write the Bounded synthesis and Limitations under the overview contract
from the reconciled records. They become public review text unchanged.
Check that they read without the members' context.

Under Description write one sentence of 50 to 250 characters that describes the system's mechanism and its limits for retrieval. Code uses it as the `description` of the overview and of the public review.
