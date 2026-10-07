---
description: "Job of an analyse-agentic-system run: independently check the reconciled records before public synthesis"
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
| `round` | `first` or `after-blockers`. | Always |
| `runtime` | Absolute path of the current runtime report. | Always |
| `memory` | Absolute path of the current memory report. | Always |
| `epistemic` | Absolute path of the current epistemic report. | Always |
| `set-check` | Absolute path of the structural check of the record set. | Always |
| `previous-verification` | Absolute path of your predecessor's verification. | `after-blockers` |
| `<report>-answers` | Absolute path of an analyst's answers to that verification's blockers. | For each report corrected since |
| `<report>-changes` | Absolute path of the text difference of a corrected report from its predecessor. | For each report corrected since |

## Situation

Three analysts have written reports about `system` and a reconciler has
stated how their records connect and where they disagree. No one has yet
judged, independently of the authors, whether the records are supported by
the frozen source and consistent with each other. There is no overview or
public synthesis yet.

## Mission

Judge the record set as it is written: the three reports, the reconciliation
and the structural findings in `set-check`, against the frozen source and the
supplied contracts. Write the verification to `output` under the supplied
verification type, with `verifies: records`, `run-id` and the
`reviewed-boundary` of `boundary`.

When you are done, every record, source anchor, evidence status, `Part of:`
relation, supersession and unresolved conflict has been checked and the
Verification section says so; defects meet the supplied verification type's
materiality threshold before becoming blockers addressed to a report; local
issues that leave the bounded conclusions valid become limits; disagreements
the sources settle are judged by the same threshold, and those they do not
settle stand as checked conflicts for the synthesis to state as limitations;
and no supported finding has been weakened by a correction nobody asked for.

The contracts fix what counts as a defect. The record contract gives the
coverage and uncertainty rules, including that faithful uncertainty alone is
not a blocker while unsupported claims or concealed gaps are; the source
contract gives evidence and quotation rules; the boundary contract gives what
`whole-system` and the coverage table require. Judge coverage against the
frozen repository tree, not only the listed anchors: listed paths are initial
inspection, and a shipped caller is not external merely because it invokes an
API.

## Boundaries

You mark and explain defects; you do not write corrected text. Each analyst
corrects its own report, the reconciler the reconciliation. The verification
type fixes the blocker threshold: explain the incorrect reader inference and
why a stated limit cannot contain it. A repairable wording, local coverage or
classification defect alone does not require another round when the remaining
conclusions hold. Unsupported findings, evidence strengths and absence or
completeness claims still require correction.

The verification
type gives the blocker form: one report named first, full IDs, the passage,
what is wrong, the evidence; a defect in two reports is two blockers, and a
passage in another report that depends on a defective value is a blocker
addressed to that report. Every failure `set-check` lists is a blocker
addressed to the report it names. A conflict missing its IDs, both findings,
evidence or prevented conclusion is a blocker addressed to `reconciliation`.

No job rewrites the boundary. Write `problem` instead of a verification only
when the records as a whole cannot support any bounded conclusion, or when
the evidence contradicts the frozen target or boundary kind; name the paths,
responsibilities and prevented conclusions. A defect that limits individual
findings within a supported boundary is not that case, and an incorrect
classification is not accepted by moving it into Limitations.

## After blockers

When `round = after-blockers`, read `previous-verification` and each
supplied `<report>-answers` and `<report>-changes`, then judge the current
reports afresh; a blocker is not settled because it was answered. For an
answer `corrected`, check the corrected text and the passages that depended
on the old value; the changes file shows which lines changed, not whether a
change is right. For an answer `declined`, judge the reason against the
sources and either drop the blocker or raise it again saying why the reason
fails; a previous verification can be wrong.

Code continues only when Blockers is `none`. Otherwise it cuts each addressed
analyst the blockers addressed to it, with the records they cite, then starts
another reconciliation and verification; in the last round it stops the run.

Run the draft-at-slot content check in the worker rules before submitting.
A pass does not establish job acceptance; code also checks invocation residue.
