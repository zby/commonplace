# Proposal: a part-of relation and a split rule without an allocator

**Status:** adopted on 2026-10-02 at the operator's direction, after the
[pre-adoption checks](./pre-adoption-check.md). The live contract, jobs and
checker now implement these rules; the fresh analysis remains pending. See
[implementation checks](./implementation-check.md).

## Problem

The [record contract](../../agentic-system-analyses/instructions/agentic-analysis-records.md)
lets a later analyst relate its record to a supplied one in two ways: the
same referent, which it annotates, or a distinct one, which it declares with
"closest supplied IDs" and possible-duplicate evidence. Reconciliation then
either supersedes a duplicate or leaves both declared. For a split, the
contract says reconciliation "allocates fresh IDs for the parts and
supersedes the combined record", but the
[reconciliation report type](../../agentic-system-analyses/types/agentic-system-reconciliation-report.md)
declares no records and the
[checker](../../../src/commonplace/lib/agentic_records.py) accepts only IDs
declared under a member's `## Shared records`.

The retained member sets show that the common relation is neither
identity nor distinctness. A lens analyst finds one produced text, one
step or one function *inside* a runtime container or route and declares it
under its own prefix: `EPI-OBJ-1` is part of `OBJ-1`, `EPI-RTE-1` is a
step inside `RTE-1`, three `EPI-OBJ` records are subsets of `OBJ-2` (bare
runtime IDs as the archived sets wrote them; `RT-OBJ-1` today). The
contract gives this no name, so analysts file it as "possible duplicate"
and reconciliation spends its identity section explaining that nothing is
a duplicate. No reconciliation superseded a combined record in either set;
the split sentence was inherited from the single-file method, where the
integrator owned the inventory and could allocate IDs.

## Proposed rules

1. **Part-of is a declared relation.** A declaration whose referent is a
   material part of exactly one supplied record states `Part of: <full ID>`
   on its own line, beside the existing closest-supplied-IDs comparison.
   The container stays declared and keeps its referent; the part owns its
   own fields and status. A part is not a possible duplicate and needs no
   supersession. Identity checking becomes: same referent (annotate), part
   of one supplied record (declare with `Part of:`), or distinct (declare
   with comparison). A record that overlaps several supplied records
   without being a part of any one of them, such as instinctual-memory-02's
   `MEM-RTE-1` across `RTE-1` and `RTE-4`, stays on the distinct path with
   its comparison naming each overlapped ID; the rule does not force
   overlap into containment.

2. **A split is a supersession by declared parts.** Replace "a split
   allocates fresh IDs for the parts" with: reconciliation may supersede a
   combined record only by parts that members already declare, in the form
   `Amendment: RT-OBJ-3 is superseded by EPI-OBJ-1 and EPI-OBJ-2`, with
   identity evidence. Reconciliation never allocates IDs. Most splits need
   no supersession at all, because a container with declared parts is
   still a valid referent under rule 1; supersede only when the combined
   record's own findings are wrong once the parts are separated.

3. **A missing part is a return or an unresolved conflict.** When a needed
   part has no declaration: if the memory analyst should declare it and
   `may-return = yes`, return it; otherwise retain an `Unresolved
   conflict:` naming the combined ID, the missing part and the conclusion
   it prevents. This follows the existing last-round and after-blockers
   rules; it adds no stopped-run branch and no runtime or epistemic
   correction round. Reassess that choice if observed runs show missing
   parts blocking conclusions that matter.

## Required method changes if adopted

- Record contract, "Identity and grammar": add the `Part of:` line to the
  new-declaration rule; rewrite the split sentence per rule 2; state that
  supersession cites only declared IDs.
- Memory and epistemic job instructions: replace "flag any needed canonical
  split for reconciliation" with "declare the part with `Part of:`", keeping
  the instruction to assess material parts separately.
- Reconcile job and report type: say that a split is a supersession by
  declared parts, and name the missing-part handling in rule 3.
- Verify job: a `Part of:` target that does not resolve, or that names a
  record of another kind without explanation, is a blocker.
- Checker: the target of a `Part of:` line already
  resolves under the existing reference scan, and an undeclared target is
  already an unresolved-reference error, so no resolution check is new. The
  only new check is syntax: the line carries exactly one full ID, and that
  ID is not the declaring record's own. The implemented check also requires
  one unindented field within its declaration and refuses duplicate fields.

No new ID namespace, no prefix change, no code path for reconciliation
declarations. Frozen sets need no reading rule: they contain no `Part of:`
lines and keep reading as before.

## Acceptance checks

Steps 1 and 2 are pre-adoption checks; their execution is recorded in the
[pre-adoption report](./pre-adoption-check.md). Step 3 follows implementation
and committing the amended method, so the fresh run pins the new contract.

1. **Archive rewrite.** Copy the members of pageindex-02 and
   instinctual-memory-02 into the workshop and first prefix every bare
   runtime ID with `RT-`; under the current grammar the checker does not
   see bare IDs at all (it finds 24 and 16 IDs in the sets as archived, not
   53 and 34), so an unnormalized copy would pass without checking any
   runtime reference. Then rewrite the identity paragraphs under rule 1 and
   confirm that every "possible duplicate" that is a subset becomes a
   `Part of:` line, that `MEM-RTE-1` stays on the distinct path, and that
   the two true duplicates (`MEM-RTE-2`/`RT-RTE-1`, `MEM-RTE-4`/`RT-RTE-6`)
   still read as supersessions. Run the checker on the rewritten members,
   then once more with one `Part of:` target deliberately pointed at an
   undeclared ID, to confirm it is reported.

2. **Split cases.** Neither archived set contains a split; the two cited
   supersessions are duplicate merges, and one fresh run can avoid splits
   by chance. Add bounded fixtures to the workflow tests that exercise rule
   2 and rule 3 directly: a combined record superseded by two declared
   parts; a missing part with `may-return = yes`, which must produce a
   memory return; and a missing part with `may-return = no`, which must
   produce an `Unresolved conflict:` and still reach publication.

3. **Fresh run after adoption.** Commit the amended method, then run one
   analysis under that contract. The count
   of identity-section paragraphs reconciliation still writes is a
   secondary measure; the primary evidence is step 2 and any refusals the
   run produces, with their stage.
