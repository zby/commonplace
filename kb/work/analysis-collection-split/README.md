# Analysis collection split

## Commission

Opened on 2026-10-03 at the operator's request. The work moves agentic-system
analysis into a self-contained collection, `kb/agentic-system-analyses/`, and
takes the memory comparison profile out of the memory analyst's job. The
purpose is simpler analyst jobs: an analyst should hold only the analysis.
The operator made the design decisions on 2026-10-03 and will launch an
executor on the plan.

This workshop was separated from
[analyse-agentic-system-amendments](../analyse-agentic-system-amendments/README.md)
so that an executor finds only material that bears on this work. That
workshop's audits are background on observed failures, not design.

## Read in this order

1. [Plan](./plan.md) — the commission: intent, end state, boundaries, a
   supported route in two phases, and when to return to the operator. Start
   here. Where files disagree, the plan governs.
2. [Collection design](./collection-design.md) — the collection, publication
   into a stable path per system, what moves, the contract, vocabulary and
   the Decisions list.
3. [Profile job design](./profile-job-design.md) — the separate profile job,
   its verification and the replay that gates it.

## Drafts

Starting points for files the work produces. Revise them toward the plan's
end state.

- [Analysis collection contract](./drafts/analysis-collection-contract.md) —
  becomes `kb/agentic-system-analyses/COLLECTION.md`.
- [Remaining contract of the old collection](./drafts/agentic-systems-contract.md)
  — replaces `kb/agentic-systems/COLLECTION.md`.
- [Method maintenance](./drafts/method-maintenance.md) — instruction for
  method authors in the new collection; analysts do not load it.
- [Decision draft](./drafts/decision-draft.md) — source for the decision
  record that revises ADR 099; carries two `TODO` revisit conditions.

Links inside the drafts resolve from this workshop. Rewrite them when a draft
is promoted to its destination.

## Evidence

How the decisions were reached. Not design. Use it for measurement baselines
and for the decision records' context. File paths recorded inside these files
are those at the time of measurement, before this workshop was separated.

- [Motivation, alternatives and pre-decision checks](./evidence/motivation.md)
- [Complexity measurements](./evidence/complexity-measurements.md), with
  itemized data in `evidence/complexity-measurements.json`
- [Input byte comparison](./evidence/input-coverage.md), with data in
  `evidence/input-measurements.json`
- [Contract coverage check](./evidence/contract-coverage-check.md)
- [Shortened contract](./evidence/shortened-agentic-systems-contract.md) —
  the rejected alternative, kept as the comparison basis

## State

2026-10-03: design decided; nothing implemented; no live method changed. The
executor writes `result.md` here as work proceeds.

## Closure

Close when both decision records are accepted and the plan's end state holds,
or when the operator records a rejection. Then delete this directory and its
entry in the workshop index; the decision records carry what must last,
including the revisit conditions.
