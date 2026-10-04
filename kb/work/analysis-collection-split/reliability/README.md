# Reliability work

Work on making analysis runs more reliable, started at the operator's request
on 2026-10-04. None of it is part of the [collection-split plan](../plan.md)'s
commission, and an executor working on that plan does not implement it.

It follows the KB's diagnosis rule: a deviation is repaired only by an
intervention that reaches its cause
([three-way diagnosis](../../../notes/llm-output-deviation-requires-three-way-diagnosis.md)).
The preferred repair removes what makes an error attractive or possible. A
check catches a failure the worker can still make. Recovery decides what a
caught failure costs.

## Adopted, with implementation plans

- [Short named record IDs](./short-named-record-ids-plan.md) — replace numeric
  record suffixes with short names from the analysed system or the record's
  label. Implemented; see [its result](./short-named-record-ids-result.md).
- [Analyst acceptance check](./analyst-acceptance-check-plan.md) — a tool
  that lets an analyst run its job's acceptance check on the draft, with all
  independent failures reported together; quotations become a blockquote
  with a path-only attribution, and the quotation helper's generation modes
  are removed. Takes effect when the operator launches an executor on it.

## Proposals awaiting adoption

- [Structured recovery](./structured-recovery-proposal.md) — what remains
  after the acceptance check plan took over reporting all failures together:
  message form, mechanical fixes by code, and recording refusals per rule.
- [Remaining code checks](./remaining-code-checks-proposal.md) — what is left
  for code to do or check after the two redesigns: a short ordered list, a
  failure register, and the classification that decides whether more exists.

## Diagnosis method and its applications

- [Review design pressure behind recurring errors](../../../instructions/review-design-pressure-behind-recurring-errors.md)
  — the library instruction: ask what makes a violation convenient and which
  design choice creates that pressure. Operator-invoked for now.
- [Counterfactual design review](./counterfactual-design-review.md) — the
  retained episode behind the instruction, including why the range audits
  did not initially suggest named IDs.
- [Quotation design review](./quotation-design-review.md) — the instruction
  applied to quotation errors. Its recommended design was superseded by the
  simpler acceptance check plan; it stays as the record of the diagnosis.

## Not pursued

By the operator's decision of 2026-10-04: splitting the reconcile and verify
jobs (too little evidence of their failures yet), repeated classification
with voting, and a different model for verification (both too heavy for now).

## Evidence base

Two audited Dynamic Cheatsheet runs, one stopped Graphiti run, and the code
as read on 2026-10-04. Recheck paths and behavior before building.
