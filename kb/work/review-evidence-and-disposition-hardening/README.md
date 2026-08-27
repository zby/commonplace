# Review evidence and disposition hardening

Opened 2026-08-27 at the operator's request, following the code-grounded review
recorded in [the evidence boundary](./evidence-boundary.md). The workshop closes
when every linked finding is fixed, rejected with a retained reason, or promoted
to a proposal or ADR where implementation depends on an unresolved design choice.

## Findings

### Result delivery and disposition

- [RF-01 — Finalization omits per-pair results from its return payload](./rf-01-finalization-payload-omits-pair-results.md)
- [RF-02 — FAIL has no consequential disposition route](./rf-02-fail-has-no-disposition-route.md)
- [RF-03 — Report results have no standard handling route](./rf-03-report-results-have-no-handling-route.md)
- [RF-07 — Warning extraction precedes the canonical outcome check](./rf-07-warn-extraction-precedes-outcome-check.md)
- [RF-08 — Warning selection ignores live note staleness](./rf-08-warn-selection-ignores-live-note-staleness.md)

### Evidence identity and integrity

- [RF-04 — Linked evidence is outside review freshness](./rf-04-linked-evidence-is-outside-freshness.md)
- [RF-05 — Quote append does not preserve grounding warrant](./rf-05-quote-append-does-not-preserve-grounding-warrant.md)
- [RF-06 — Grounding snapshot invariants are not enforced](./rf-06-grounding-snapshot-invariants-are-not-enforced.md)
- [RF-09 — Result prose is unbound mutable state](./rf-09-result-prose-is-unbound-mutable-state.md)
- [RF-18 — Snapshot-route telemetry prices the wrong artifact](./rf-18-snapshot-route-telemetry-prices-the-wrong-artifact.md)

### Acknowledgement and judging identity

- [RF-10 — Joint note and criterion changes are compressed to one reason](./rf-10-joint-input-changes-are-compressed.md)
- [RF-11 — Acknowledgement is not bound to inspected input hashes](./rf-11-acknowledgement-is-not-bound-to-inspected-inputs.md)
- [RF-12 — Acknowledgement decisions are not auditable](./rf-12-acknowledgement-decisions-are-not-auditable.md)
- [RF-13 — Judging configuration is outside freshness identity](./rf-13-judging-configuration-is-outside-freshness.md)
- [RF-14 — Model partitions lack equivalence evidence](./rf-14-model-partitions-lack-equivalence-evidence.md)

### Operational recovery and capacity

- [RF-15 — Multi-group job creation has partial success without a recovery payload](./rf-15-multi-group-job-creation-has-partial-success.md)
- [RF-16 — Result-file writes are not transactionally atomic](./rf-16-result-file-writes-are-not-transactionally-atomic.md)
- [RF-19 — Worker dispatch and attempt state are not retained](./rf-19-worker-dispatch-state-is-not-retained.md)
- [RF-20 — Review prompts have no context budget](./rf-20-review-prompts-have-no-context-budget.md)

### System-contract cleanup

- [RF-17 — Gate staleness declarations overstate runtime semantics](./rf-17-gate-staleness-overstates-runtime-semantics.md)
- [RF-21 — The declared reviewer system prompt has no registered consumer](./rf-21-reviewer-system-prompt-has-no-consumer.md)

## Low-hanging fruits

1. [RF-07 — move the outcome guard before warning extraction](./rf-07-warn-extraction-precedes-outcome-check.md).
2. [RF-01 — return per-pair outcome and result paths from finalization](./rf-01-finalization-payload-omits-pair-results.md).
3. [RF-10 — report both changed inputs instead of one priority reason](./rf-10-joint-input-changes-are-compressed.md).
4. [RF-21 — either wire or remove the unused reviewer system-prompt constant](./rf-21-reviewer-system-prompt-has-no-consumer.md).
5. [RF-18 — price and report the actual derived snapshot on the snapshot route](./rf-18-snapshot-route-telemetry-prices-the-wrong-artifact.md).
6. [RF-17 — remove the lone unsupported `rewrite(0.5)` declaration or make the field's current exact-change semantics explicit](./rf-17-gate-staleness-overstates-runtime-semantics.md).
