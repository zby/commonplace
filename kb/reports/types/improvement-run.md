---
type: types/type-spec.md
name: improvement-run
description: "One run of an improvement variant on one note, as a directory whose layout declares its report, findings, edit chain and open items"
schema: ./improvement-run.schema.yaml
layout:
  membership: open
  roles:
    report:
      path: report.md
      type: reports/types/improvement-run-report.md
    findings:
      path: findings.md
      type: reports/types/improvement-run-findings.md
      identity:
        - {from: report, fields: [note, start-sha256]}
    changes:
      path: changes.md
      type: reports/types/improvement-run-changes.md
      identity:
        - {from: report, fields: [note, start-sha256, final-sha256]}
    answers:
      path: answers.md
      type: reports/types/improvement-run-answers.md
      identity:
        - {from: report, fields: [note]}
  required:
    always: [report]
    when:
      role: report
      field: ending
      values:
        stopped: [findings, changes, answers]
        applied: [findings, changes, answers]
        partly-applied: [findings, changes, answers]
---

# Improvement run

A directory artifact under `kb/reports/state/improve/<note path without .md>/<YYYYMMDD-HHMMSS>/`
that records one run of an improvement variant on one note. The layout
above declares the members; each member's type says what it contains.

Experimental, registered on 2026-11-14 for the first run of the improvement procedure. The design and its open choices are in the [run type draft](../../work/decision-lifecycle-evidence/improvement-run-type.md); the schema is a starting point and is expected to change.

An open run has the report alone. A closed run has all four members, and an
empty list in a member says "none" explicitly. Beside the members, `texts/`
holds the start text and every text an edit produced, each as
`<sha256>.txt`; these files are not members and are not validated.

The manifest names only the type. No member is pinned, because open items
are decided after the run closes.

## Template

```yaml
type: reports/types/improvement-run.md
```
