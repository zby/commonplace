# Problem: shared record IDs

## Starting problem

The [shared record contract](../../agentic-systems/instructions/agentic-analysis-records.md)
puts both analyst and kind in an ID: `RT-RTE-1`, `MEM-RTE-1`, or
`EPI-RTE-1`. The `RT-` prefix landed in commit `4e5b5d9ae` on 2026-10-02;
bare runtime IDs stay readable only in frozen sets. Kind is also expressed
by the declaration's heading. The contract requires
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

## Observed evidence

Read on 2026-10-02 from
`kb/agentic-systems/reports/retained-archive/`: 60 single-file results
from the method before member sets, and two member sets, pageindex-02 and
instinctual-memory-02, produced before the `RT-` prefix. The archive holds
accepted output only; refusals raised during a run are not retained, so
the operator's reported errors still need their exact refusal text and
stage. The original check was reported as resolving every reference in both
sets, but the current checker recognizes only 24 and 16 declarations in the
unnormalized archive: it ignores bare runtime IDs. The
[pre-adoption rewrite](./pre-adoption-check.md) prefixes runtime IDs in workshop
copies, then resolves all 53 and 34 declared IDs including their source
registers, with no errors. The archive retains historical type paths; these
reference checks do not establish validation against current member schemas.
Bare IDs quoted below (`OBJ-1`, `RTE-1`)
are the archived sets' runtime IDs as written; under the current method
they would be `RT-OBJ-1` and `RT-RTE-1`.

**Part-of is the common relation, and the contract has no name for it.**
In pageindex-02, `EPI-OBJ-1` and `EPI-OBJ-3` are parts of the runtime
containers `OBJ-1` and `OBJ-3`; `EPI-RTE-1` and `EPI-RTE-2` are steps
inside `RTE-1`. In instinctual-memory-02, three `EPI-OBJ` records are
described as possible duplicates: two fact subsets of `OBJ-2` and one writeback
rendering within `OBJ-3`. `MEM-RTE-1`
overlaps two runtime routes without matching either. Analysts file these
as possible duplicates; reconciliation's identity section then explains,
record by record, that none is a duplicate.

**Splits never ran through reconciliation.** Neither member set supersedes
a combined record. The epistemic analyst split containers by declaring
parts under its own prefix and left the container standing. The "allocates
fresh IDs" sentence comes from the single-file method, where one integrator
owned the inventory: dynamic-cheatsheet-01 splits `OBJ-6` into `OBJ-12`
and `OBJ-13` (lines 174, 505); mem0-04 supersedes `OBJ-1` by `OBJ-7` and
`OBJ-8` (line 1365); napkin-05 returned the split to the specialist that
declared the record (line 910). The sentence lost its owner when members
became immutable.

**True duplicates were against runtime, not between the parallel
analysts.** instinctual-memory-02 has two, `MEM-RTE-2` superseded by
`RTE-1` and `MEM-RTE-4` by `RTE-6`, both declared after the memory analyst
had read the runtime member. Neither set has a memory-versus-epistemic
duplicate.

**ID-form slips in the single-file results** (pattern scan over 60 files,
quotations excluded; counts are approximate): 25 files rename `MEM-`
records to canonical IDs (161 arrows such as `MEM-OBJ-1 → OBJ-9`), the
scheme permanent prefixes replaced; 21 files cite ranges such as `RTE-1
through RTE-12` (120 hits), which the checker does not expand; 4 files
invent off-grammar IDs (`EPI-R1`, `MEM-LIM-1`, `EPI-CL-1`; 15 hits).
Nothing in the archive traces an error to the kind code, to numbering, or
to reclassification.

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
