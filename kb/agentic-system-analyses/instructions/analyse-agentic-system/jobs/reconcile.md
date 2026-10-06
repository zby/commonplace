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

## Task

Write `output` with `## Reconciliation` and no other section, under the
supplied reconciliation report type. Code writes the retained member's
identity and copies this section unchanged.

Your subject is the relations between the three reports: which records name
the same thing, which are parts of others, where the analysts converged
independently, and where two reports disagree. You do not judge whether one
report's finding is supported by the sources, and you do not correct a
report. The record verifier judges support, and the declaring analyst
corrects.

## Connect the records

Resolve duplicates and identity under the shared record contract. State an
identity judgment as a supersession, `Amendment: <full ID> is superseded by
<full IDs>`, with identity evidence. A split supersedes a combined record only
by parts already declared in analyst reports; never allocate IDs or declare
split parts here. Check `Part of:` relations without superseding valid
containers. Recheck shared-route ownership. Report independent convergence
only when the analysts reached it independently. Attach the admission fields
of memory routes from the memory analyst's findings; do not trace those
mechanisms again.

## Describe disagreements

Where two reports assert incompatible things about the same referent, write
a paragraph starting `Unresolved conflict:` with the full IDs, each report's
finding, the evidence each cites and the conclusion the conflict prevents.
Do not choose a side and do not write a replacement value: an `Amendment:`
paragraph that is not a supersession is refused. The verifier reads the
conflict and addresses a blocker to the report that must change. A required
part that no analyst declared is the same kind of entry: name the combined
ID, the missing part in prose, the evidence and the prevented conclusion.

A report whose finding rests on another report's record disagrees with that
report when the record no longer says what the finding relies on. After a
correction, check the reports that cite the corrected records.

## Limits on your own statements

Do not strengthen an analyst's finding, draft a second analysis, or erase
uncertainty a report states. Preserve source-native positives and their
evidence layers alongside unresolved included parts. Keep inspected but
inconclusive evidence, uninspected evidence, bounded absence and
inapplicability distinct when you restate a finding, and keep independent
epistemic properties separate. Faithful uncertainty alone is not a
disagreement and needs no entry.

Every ID you cite must resolve in the set your output makes: the Source
register and the three current reports. Your output is refused with the
unresolved IDs otherwise.

## After blockers

When `round = after-blockers`, read `previous-reconciliation`,
`verification`, `set-check`, and each supplied `<report>-answers` and
`<report>-changes`. Reconcile the current reports again; recheck anything
you carry over rather than copying it.

- Answer every blocker addressed to `reconciliation` by correcting your own
  account.
- A blocker addressed to an analyst report is that analyst's to answer. Do
  not restate its correction as your own finding.
- A declined blocker that concerns two reports stays an
  `Unresolved conflict:` with both positions, including the analyst's reason.

Run the acceptance check before submitting.
