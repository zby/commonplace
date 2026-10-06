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

## Task

Read the record set from `boundary`, `runtime`, `memory`, `epistemic` and
`reconciliation`, and read `set-check` for structural validation findings.
There is no overview or public synthesis yet; judge records only. Write
`output` with exactly these sections, which go into the overview's
Verification and blockers:

```markdown
### Record verification

### Blockers
```

Acceptance requires valid verification sections, resolved citations and explicit
blockers when the structural check has failures.

Judge the reports as they are written. Check the whole record set, including
reconciliation's supersessions and conflicts, against the shared source and record contracts.

Record the checked routes and material dispositions, and the check of every
source anchor, canonical ID, evidence status, boundary, member and unresolved
conflict. Structural validation does not perform this check. Apply the supplied record
contract's coverage dimensions: positives must retain their part/mechanism and
evidence layer, and unresolved included parts must remain named with missing
facts and prevented conclusions. Check complete inventories and bounded
negatives against evidence, not the existence of one route. Distinguish generic
callers from human admission control, requested transformations from implemented
ones, selection from delivery, and trace-fed writes from improved capacity.
Verify epistemic functions and independent properties separately. Faithful
uncertainty alone is not a blocker; unsupported claims or concealed gaps are.
Use full IDs; list numbered `SRC-*` references separately.

For a Git source, compare the boundary kind and top-level coverage table
with the frozen repository tree, not just with the listed citation anchors.
Listed paths are initial inspection coverage, not an allowlist. Inspect
unlisted material files when checking the selected target. For a
`whole-system` memory or knowledge system, check that the coverage account
names shipped prompts and maintenance instructions, persistence and reload
callers, later consumers, and evaluators, and that their material wiring is
covered by the members or justified exclusions. Check any additional paths
the analysts discovered. A shipped caller is not external merely because
it invokes an API. Distinguish real source-access gaps from available files
omitted during analysis.

If an omitted file affects an individual finding while the boundary kind
remains supported, use the existing blocker and conflict rules below. If
the evidence contradicts `whole-system` or the selected target's functional
exclusions, write `problem` naming the paths, responsibilities and prevented
conclusions: no job rewrites the frozen boundary metadata.
Do not accept an incorrect classification by moving it into Limitations.

Check every `Part of:` relation against the records' identities and evidence.
An unresolved parent, malformed field, self-reference or unexplained parent
of a different kind is a blocker. A valid part keeps its own fields and
status; a valid container needs no supersession. For a split supersession,
check that every replacement part is already declared and that the
supersession explains why the combined finding fails. A missing part is a
blocker addressed to the analyst who should declare it. A multi-record
grouping must retain its comparisons rather than assert unsupported containment.

## Blockers

A blocker is a defect that a change to one report's text can repair. Each
analyst corrects its own report; the reconciler corrects the reconciliation.
You do not write corrected text.

Start each blocker with the one report whose text must change:
`- runtime: `, `- memory: `, `- epistemic: ` or `- reconciliation: `. Code
routes work by this word and refuses a blocker without it. Then give the full
IDs, the section or field holding the defective text, what is wrong, and the
evidence. A defect that needs changes in two reports is two blockers. Name
every passage you found that depends on the defective value, in that report
and in others: a ledger row, a field of another record, a conclusion. A
dependent passage in another report is a blocker addressed to that report.

An unsupported finding is a blocker; properly scoped explicit uncertainty is
not. Every failure the set check lists is a blocker addressed to the report
it names. No job rewrites the boundary.

Read each `Unresolved conflict:` in the reconciliation. When the sources
settle it, address a blocker to the report that is wrong. When they do not,
the conflict stands: check that it gives its IDs, both findings, the evidence
and the prevented conclusion, and record it under Record verification as a
checked conflict. The synthesis then states it as a limitation. A conflict
missing one of those parts is a blocker addressed to `reconciliation`.

## After blockers

When `round = after-blockers`, read `previous-verification` and each
supplied `<report>-answers` and `<report>-changes`. Judge the current
reports afresh; a blocker is not settled because it was answered.

- For an answer `corrected`, check the corrected text against the sources
  and check the passages that depended on the old value. The changes file
  shows which lines changed. It does not show whether a change is right or
  whether unchanged text is still supported.
- For an answer `declined`, judge the analyst's reason against the sources.
  Accept it and drop the blocker, or raise the blocker again and say why the
  reason fails. A previous verification can be wrong.
- Check that a correction did not remove or weaken a supported finding that
  no blocker concerned.

Write `problem` instead only when the records as a whole cannot support any
bounded conclusion, or when the frozen target or boundary-kind classification
is contradicted as described above. A defect that limits individual findings
within a supported boundary is not that case.

Under Blockers write exactly `none`, or a Markdown list with one `- ` entry
per blocker; indent any continuation line. Anything else is refused,
including `None.` or `none found`. Code continues only on `none`. A blocker
list sends each addressed analyst your verification, then starts another
reconciliation and verification; in the last round it stops the run.

Run the acceptance check before submitting.
