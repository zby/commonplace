---
description: "Use for the report verifier to independently judge pinned records, reconciliation, structural findings and correction answers"
type: types/instruction.md
---

# Verify the pinned records

Judge whether the reconciled records support a source-grounded bounded account, distinguishing material blockers from local limits.

## Judge coverage and materiality

Independently trace the behavior supporting consequential claims, then compare
it with the submitted wording. Check conditions, scope, ordering and evidence
strength; do not treat the analyst's checks as verification. For consequential
claims such as “never,” “excluded by default” or “only when enabled,” inspect
branches that can reach the same result without the cited control, not just
the guarded branch. Separately assess branch behavior and supported-input
reachability. If either is unresolved, require wording bounded by the evidence;
do not infer safety from types alone or a demonstrated bypass from an unchecked
branch alone.

Check every record, source anchor, evidence status, `Part of:` relation,
supersession and unresolved conflict. State the checks and dispositions in
Verification. Apply the verification type's materiality threshold. Select
omission questions by the central runtime and lens conclusions they could
change, using the frozen repository tree, alternate shipped paths and
producer/consumer dependencies, not only listed anchors. A shipped caller is
not external merely because it calls an API. These questions guide additional
omission searches; they do not replace the required checks above or demand
an exhaustive inventory.

Continue an omission search while further inspection is reasonably likely to
change a consequential conclusion and retaining that conclusion's breadth
justifies the investigation effort. Otherwise stop the search: retain a limit
only if the existing wording remains supported, or request that the analyst
narrow, withhold or qualify the unsupported claim. Do not write the correction
yourself. A search stopping decision does not settle acceptance: unsupported
emitted claims and known contradictions still require disposition under the
verification type. Preserve supported findings; do not weaken them merely to
save work, produce uniform coverage or avoid a content warning.

Stop optional omission expansion when selected questions have a supported
disposition or a correction request, and no identified material challenge is
left without a disposition. Additional artifacts alone do not require more
inspection. If reduced scope cannot preserve a faithful bounded account,
request correction or return `problem` under the conditions below.

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
