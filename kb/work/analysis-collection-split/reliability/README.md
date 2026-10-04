# Reliability proposals

Proposals for making analysis runs more reliable. The first three were
requested by the operator on 2026-10-04; the named-ID proposal followed a
discussion of recurring range errors. All are agent drafts, **not part of the
[plan](../plan.md)'s commission**. An executor working on the plan does not
implement them. The first three await the operator's adoption and authorize
nothing. The fourth was adopted on 2026-10-04 and is now a separate
implementation plan.

They follow the KB's diagnosis rule: a deviation is repaired only by an
intervention that reaches its cause
([three-way diagnosis](../../../notes/llm-output-deviation-requires-three-way-diagnosis.md)).
Splitting work addresses load. The first three address workers that violate a
clear rule, and what happens after a violation is caught. The fourth changes
the identifier design so that one such violation cannot be written.

- [Code-owned bookkeeping](./code-owned-bookkeeping-proposal.md) — move
  obligations with exact answers from the worker to code.
- [Failures become checks](./failures-become-checks-proposal.md) — retain
  each observed failure as a maintained check where one is possible, and as
  instruction text only where it is not.
- [Structured recovery](./structured-recovery-proposal.md) — make a refused
  output cheap to repair: report all failures at once, say what to do, and
  fix mechanical ones in code.
- [Short named record IDs](./short-named-record-ids-plan.md) — adopted by
  the operator on 2026-10-04 and written as an implementation plan: replace
  numeric record suffixes with short names taken from the analysed system or
  from the record's label. It takes effect when the operator launches an
  executor on it, after the collection-split work is committed.

## Diagnosis method

- [Review design pressure behind recurring errors](../../../instructions/review-design-pressure-behind-recurring-errors.md)
  — reusable instruction: ask what makes a violation convenient and which
  design choice creates that pressure. Available through search or explicit
  invocation, not an automatic gate.
- [Counterfactual design review](./counterfactual-design-review.md) — retained
  episode and reasoning behind the instruction, including why the range
  audits did not initially suggest named IDs.

The first three overlap by design. Bookkeeping removes an obligation, so it cannot
fail. A check catches a failure the worker can still make. Recovery decides
what a caught failure costs. Adopt in that order where the choice exists.

Order, by the operator's decision of 2026-10-04: named record IDs are
implemented first. The other three are then revised against the implemented
state; each carries a section listing what to revise.

Not proposed here, by the operator's decision of 2026-10-04: splitting the
reconcile and verify jobs (too little evidence of their failures yet),
repeated classification with voting, and a different model for verification
(both too heavy for now).

Evidence base for the first three: two audited Dynamic Cheatsheet runs, one stopped
Graphiti run, and the code as read on 2026-10-04 while the plan's
implementation was in progress. Recheck paths and behavior before building.
