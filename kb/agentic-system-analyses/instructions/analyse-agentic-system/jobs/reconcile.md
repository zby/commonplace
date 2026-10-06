---
description: "Job of an analyse-agentic-system run: state how the three analysts' records connect and where their reports disagree"
type: types/instruction.md
---

# Reconcile the analysts' records

Read every file under `read-first` in your invocation before any other step.

## Job parameters

Common parameters are defined in the supplied worker rules.

| Name | Meaning | Present |
|---|---|---|
| `round` | `first` or `after-blockers`. | Always |
| `boundary` | Absolute path of the frozen boundary and Source register. | Always |
| `runtime` | Absolute path of the current runtime report. | Always |
| `memory` | Absolute path of the current memory report. | Always |
| `epistemic` | Absolute path of the current epistemic report. | Always |
| `previous-reconciliation` | Absolute path of the previous reconciliation. | `after-blockers` |
| `verification` | Absolute path of the previous record verification. | `after-blockers` |
| `set-check` | Absolute path of the structural check for that verification. | `after-blockers` |
| `<report>-answers` | Absolute path of an analyst's answers to that verification's blockers. | For each report corrected since |
| `<report>-changes` | Absolute path of the text difference of a corrected report from its predecessor. | For each report corrected since |

## Situation

Three analysts have written reports about `system` from different views. The
memory and epistemic analysts worked in parallel and did not see each other's
work; both read the runtime report. Their records overlap: some name the same
thing, some are parts of others, some rest on another report's record.

## Mission

Write the reconciliation report to `output` under the supplied reconciliation
report type, with `run-id` and the `reviewed-boundary` of `boundary` as its
identity. Its subject is the relations between the three reports, so that the
record verifier can judge the set as one account and the synthesizer can read
it as one. The accepted report enters the set unchanged.

When you are done, every identity between records is stated as a supersession
or ruled out, every disagreement between two reports is an `Unresolved
conflict:` paragraph with both findings, the evidence each cites and the
conclusion it prevents, and nothing
in your text replaces, strengthens or narrows a finding a report makes.
Faithful uncertainty alone is not a disagreement. A finding that rests on
another report's record disagrees with that report when the record no longer
says what the finding relies on.

## Boundaries

You connect; you do not judge or correct. Whether a finding is supported by
the sources is the verifier's question, and only the declaring analyst changes
a report. Never allocate an ID or declare a part. Code refuses an
`Amendment:` paragraph that is not a supersession and any ID that does not
resolve in the set your output makes: the Source register and the three
current reports.

## After blockers

When `round = after-blockers`, reconcile the current reports again rather
than copying `previous-reconciliation`. Answer the blockers in `verification`
addressed to `reconciliation`. Blockers addressed to a report are that
analyst's; read its answers and changes to see what moved, and describe a
declined blocker that concerns two reports as a disagreement with both
positions.

Run the acceptance check before submitting.
