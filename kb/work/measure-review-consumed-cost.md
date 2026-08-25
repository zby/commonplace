# Handoff: record what a review actually opened

Standalone task, no workshop. Builds measurement **B** from
[Review link budget prices reviewer attention](../reference/proposals/review-link-budget-prices-reviewer-attention.md),
authorized by the operator 2026-08-25. Delete this file when it lands.

Measurement A already shipped (`adbc1cc0`): per-pair *available* cost, recorded
in `review_jobs.telemetry_json`, baseline in
[`kb/reports/review-link-availability.md`](../reports/review-link-availability.md).
A shows what a review was offered. **B shows what it consumed, and only B can
identify the α/β ratio**, because the ratio is estimated from where reviewers
stop.

## What to build

Reviewers report what they opened; that report reaches telemetry beside the
availability figures already there.

**Reuse the self-reported-model mechanism.** `job-output.md` already carries
`self-reported-model` (`SELF_REPORTED_MODEL_FIELD` in
`src/commonplace/review/protocol/format.py`): a field the worker fills in, parsed
at finalization, recorded as provenance, and never treated as review identity.
B is the same shape and should follow it rather than inventing a channel.

**Key it per pair**, matching A. `link_availability_telemetry_json` emits one
record per `(note_path, criterion_path)`; consumed cost should join those records
so offered and consumed sit side by side and are trivially comparable.

**What to ask the reviewer for**, kept to what the ratio needs:

- distinct artifacts opened, and their paths
- whether it stopped because the budget ran out or because it had enough

Bytes are derivable from the paths — do not ask a reviewer to count them. Asking
for a number it cannot compute produces a number you cannot trust.

## The rule that must not break

**A missing, partial, or malformed report must never change an outcome or fail
finalization.** Record what is present, note what is absent, and finalize the
review exactly as it would have finalized before. A measurement that can fail a
review stops being a measurement.

This is the whole reason B needed an operator decision: it adds an obligation on
every reviewer. Keep that obligation soft — the gate still judges grounding, not
bookkeeping — and keep it out of the verdict path entirely.

## Constraints

- **Do not touch verdict semantics.** No gate edit, no outcome change, no stale
  pairs. Whether exceeding a budget should ever fail is a separate open decision
  in [enforcement is separable](../reference/proposals/review-budget-enforcement-is-separable.md);
  this task must not pre-empt it.
- **Do not add a budget.** Nothing enforces a cap yet, and nothing should until
  α, β, and the number are derived from the data this produces.
- **Whole files, as in A.** Route-aware partial charging stays the recorded TODO;
  changing it here would make B's numbers incomparable with A's.
- Expect reports to be imperfect. Reviewers already disclose unopened links
  unprompted when they feel the need — review job 8051 named four — but that is
  a courtesy, not a habit, and it will not be uniform.

## What to report back

Whether consumed cost tracks artifact count, byte volume, or neither. That is
α/β, and it is the only reason this exists.

Also worth surfacing: how often reviewers stop for budget rather than
sufficiency. If they almost never do, a cap is machinery for a case that does not
arise, and
[enforcement](../reference/proposals/review-budget-enforcement-is-separable.md)
resolves to its cheapest option without further work.
