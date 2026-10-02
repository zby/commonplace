# Proposal: settle splits before reconciliation

**Status:** proposed for the `analyse-agentic-system` amendments workshop; no
live method change is adopted here.

## Problem

The [record contract](../../agentic-systems/instructions/agentic-analysis-records.md)
says a split allocates fresh IDs for its parts and supersedes the combined
record. It also says the analyst who establishes a record declares it in that
analyst's member. The [reconciliation report
type](../../agentic-systems/types/agentic-system-reconciliation-report.md)
explicitly declares no records. The
[reconciliation job](../../agentic-systems/instructions/analyse-agentic-system/jobs/reconcile.md)
can write amendments and supersessions but cannot write new declarations.
The [checker](../../../src/commonplace/lib/agentic_records.py) accepts an ID
only when a member declares it under `## Shared records` or the overview
registers it as a source. Thus a reconciliation that cites IDs for newly
split parts fails reference validation.

## Proposed rule

Reconciliation may **identify** a needed split and may supersede a combined
record only when separate records for all material parts are already declared
in the set. It never allocates IDs. If a part has no declaration, the split
is a correction to the declaring analyst's inventory, not a reconciliation
amendment. The run must obtain corrected analyst members and repeat their
dependent analysis before it can publish. Until a correction path exists for
the affected analyst, stop that run before publication and open a new run
with the split requirement explicit in its commissioning input.

For example, if `MEM-OBJ-3` combines a stored fact and its selection index,
and `MEM-OBJ-4` already declares the index, reconciliation can amend the
referent and fields of `MEM-OBJ-3` and link the two records. If the index has
no declaration, reconciliation records the defect and returns it to the
memory analyst while a correction round is available. It cannot invent
`MEM-OBJ-4` in an `Amendment:` paragraph. A split of a runtime or epistemic
record currently has no same-run correction path; it blocks completion
rather than appearing as a merely scoped uncertainty.

## Required method changes if adopted

1. Replace the record contract's promise that reconciliation allocates fresh
   IDs with the rule above. State that a supersession can cite only declared
   IDs. Keep old combined IDs as historical references; never change their
   referents silently.
2. Teach reconciliation and verification to distinguish an analytical
   uncertainty from a missing material declaration. The latter blocks
   synthesis and publication. An `Unresolved conflict:` paragraph alone must
   not waive this structural defect.
3. Use the existing memory correction path when the memory analyst owns the
   combined record. For a runtime or epistemic split, either add a guarded
   same-run correction and rerun affected downstream jobs, or explicitly
   terminate the run for a fresh analysis. Choose that recovery cost from
   observed split frequency before building the extra workflow branch.
4. Give a fresh run a concise problem statement identifying the kind of
   conflation and the source locations to inspect, without treating an old
   analysis as source evidence. Preserve the new run's independent source
   boundary and method commit.

This repair needs no new ID namespace or changed parser grammar. It leaves
the broader ID simplification question open. It also avoids a reconciliation
record whose prefix claims one analyst established it while another member
actually declares it.

## Check before adoption

Use one case where two parts are already declared and one where a material
part is missing. Confirm that the first can be superseded with resolving IDs,
and the second cannot reach publication. Check that a corrected memory member
keeps surviving IDs, assigns a fresh number to the new part, and causes its
profile and reconciliation to be reassessed. Decide the runtime and epistemic
recovery path before changing the live contract.
