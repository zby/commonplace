# Analyse-agentic-system amendments

## Commission

Opened on 2026-10-02 at the operator's request. Examine amendments to the
live [`analyse-agentic-system` skill](../../agentic-systems/instructions/analyse-agentic-system/SKILL.md),
starting with its shared record ID system. The operator has encountered ID
errors and wants the scheme simplified. This workshop investigates the errors
and chooses a repair before changing the live method.

The earlier [construction workshop](../analyse-agentic-system/README.md)
records how the skill was developed. This workshop concerns changes to the
method now in use. It does not commission an analysis run, alter a retained
analysis, or adopt an ID design by opening.

## Starting problem

The [shared record contract](../../agentic-systems/instructions/agentic-analysis-records.md)
puts both analyst and kind in an ID: `RTE-1`, `MEM-RTE-1`, or `EPI-RTE-1`.
Kind is also expressed by the declaration's heading. The contract requires
full IDs across members, annotations for shared referents, and reconciliation
of duplicates, corrections, and splits. These rules create several places
where an analyst must preserve an exact identifier while revising a finding.

One inconsistency is visible without a run: the contract says a split
allocates fresh IDs for its parts, but the
[reconciliation job](../../agentic-systems/instructions/analyse-agentic-system/jobs/reconcile.md)
only writes reconciliation text. The
[record checker](../../../src/commonplace/lib/agentic_records.py)
recognizes declarations under `## Shared records` and rejects cited IDs
that no member declares. The intended owner and declaration path for a split
therefore need to be settled. This is a contract finding, not a claim that it
caused the operator's reported errors; collect those errors separately.

## Questions to settle

- Which reported errors arise from ID syntax, assignment, reference checking,
  record identity, or reconciliation? Retain exact refusals and the stage at
  which they occurred before attributing a cause.
- What must an ID identify across the set, and which properties can live in
  the declaration instead? Compare the current analyst-plus-kind scheme with
  simpler schemes using concrete runtime, memory, and epistemic records.
- How should parallel analysts cite shared referents and declare genuinely
  new ones without collisions or duplicate inventories?
- When a finding is corrected, merged, superseded, or split, which member
  owns any new declaration? What can reconciliation express without rewriting
  an already accepted member?
- Which checks and consumers depend on kind-coded IDs, including route-field
  checks, evidenced-absence checks, memory comparison profiles, and set
  validation? How will old frozen sets remain readable if new runs use a
  different grammar?
- Does a simpler record model preserve the distinctions needed for analysis,
  or should some currently mandatory records or references cease to be
  addressable at all?

The [split-records proposal](./split-records-proposal.md) recommends settling
missing declarations in the declaring analyst's member before publication.
It is a proposed repair to the contradiction, not an adopted ID scheme.

## Evaluation boundary

Use the live skill, its job instructions, member types, record contract, and
the code that validates and consumes records. Inspect concrete error evidence
and a small representative set of record interactions. Judge proposals by
whether an analyst can assign IDs reliably, another analyst can identify the
same referent, reconciliation can express the required changes, and readers
can resolve every retained reference.

Keep the run ID, source identity, and `SRC-*` source register separate from
the shared record question unless evidence shows they contribute to an
error. Existing retained sets are frozen evidence; any new grammar needs an
explicit reading path for them. The method commit pinned by an open run is
not changed to make that run resume under a revised method.

## Closure

Close with a concrete decision: a simpler record and reconciliation contract,
or a reasoned decision to keep the present scheme with targeted repairs.
Name the affected instructions, types, validators, and consumers; show how
the chosen rules handle ordinary declarations, cross-member references,
corrections, and splits. Record the observed errors separately from predicted
failure modes. Promote an adopted design through the live method and its
affected interfaces, then remove this workshop and its active-list entry.
