# Earlier amendment investigations and run evidence

These files retain the October 2–3 ID investigation, completed repair checks
and Dynamic Cheatsheet audits. They describe their original method boundary;
they are evidence, not the current plan or a complete description of the live
method. Start new design work at the [workshop README](../README.md).

## ID investigation and adoption

- [Problem](./problem.md) — starting evidence and record-identity questions.
- [Fix options](./fix-options.md) — considered repairs and their dispositions.
- [Split-records proposal](./split-records-proposal.md) — the adopted `Part of:`
  repair at that time, not a new pending proposal.
- [Pre-adoption check](./pre-adoption-check.md) — normalized archive copies,
  part relations, negative checks and bounded workflow fixtures. Links to
  the two copied sets under `rewrite-check/` are in this check.
- [Implementation check](./implementation-check.md) — adopted repairs,
  consumers, verification and original stopping points.
- [Skill inconsistencies](./skill-inconsistencies.md) — audit of the method
  before those repairs; its suggested order is not a current work queue.

## Dynamic Cheatsheet runs

- [Fresh-run audit](./fresh-run-audit.md) and
  [trace evidence](./fresh-run-trace-evidence.md) — recovered errors,
  coverage regression and motivating cases for the repairs.
- [Second-run audit](./second-run-audit.md) and
  [trace evidence](./second-run-trace-evidence.md) — repaired-method outcomes
  and remaining duplicate-identity and inspection-fidelity findings.

The operator accepted the second result unchanged on 2026-10-03. Its remaining
findings are comparison evidence. Their repair was deferred until recurrence;
these files do not commission another repair or rerun.

## Earlier framing and completed plans

The full earlier commission, implementation chronology and completed minimal
pre-run plan remain available through git:

```bash
git show 1b5a5a8b7:kb/work/analyse-agentic-system-amendments/README.md
```

Use that read path to reconstruct historical authority or change sequence.
Use the live code and contracts for current behavior.

## Validation boundary

The eight `rewrite-check/` files are byte-identical to their pre-cleanup
versions. Their historical `type:` pointers name retired global specs:
`types/agentic-system-epistemic-report.md`,
`types/agent-memory-analysis-report.md`,
`types/agentic-system-analysis-overview.md` and
`types/agentic-system-runtime-report.md`. Directory validation reports eight
missing-type-spec failures. Do not silently migrate these copied fixtures to
current schemas and treat the result as the original acceptance evidence.
The surrounding history and current workshop documents validate separately.

## Retention boundary

This is local workshop history, not a permanent archive. At closure, extract
only evidence with an independent durable consumer, preserve any needed
follow-up, and delete the rest with the workshop. The
[Sol follow-up plan](../sol-run-follow-up-plan.md) remains outside history
until its unresolved dispositions are checked.
