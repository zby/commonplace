---
description: "Use for the report verifier to independently judge pinned records, reconciliation, structural findings and correction answers"
type: types/instruction.md
---

# Verify the pinned records

Judge whether the reconciled records support a source-grounded bounded account, distinguishing material blockers from local limits.

## Judge coverage and materiality

Check every record, source anchor, evidence status, `Part of:` relation,
supersession and unresolved conflict. State the checks and dispositions in
Verification. Judge coverage against the frozen repository tree, not just
listed anchors. A shipped caller is not external merely because it calls an
API. Preserve supported findings; do not weaken them to produce uniform
coverage or avoid a content warning. Apply the verification type's
materiality threshold.

Every structural failure in `report-check` requires an explicit blocker
addressed to its report; if the finding cannot be routed within this job's
authority, write `problem` instead of silently dismissing it. A conflict
missing record citations, both findings, evidence or prevented conclusion is
addressed to reconciliation.

Write `problem` instead of a verdict when the records together cannot support
any bounded conclusion or evidence contradicts the frozen target or boundary
kind. Name paths, responsibilities and prevented conclusions. A local defect
within a supported boundary is not that case. Do not move an incorrect
classification into Limitations to accept it.
