# Problem: shared record IDs

## Starting problem

The [shared record contract](../../agentic-systems/instructions/agentic-analysis-records.md)
puts both analyst and kind in an ID: `RTE-1`, `MEM-RTE-1`, or `EPI-RTE-1`.
A concurrent change, uncommitted when this workshop opened, adds an `RT-`
prefix to runtime IDs (`RT-RTE-1`) and keeps bare runtime IDs readable only
in frozen sets. Judge proposals against that prefixed scheme once it lands.
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
