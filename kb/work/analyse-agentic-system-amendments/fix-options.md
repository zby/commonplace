# Fix options for the shared record IDs

**Status:** brainstorm, 2026-10-02, revised the same day against the
[observed evidence](./problem.md#observed-evidence). Agent-proposed options;
none adopted. Judged against the `RT-` prefixed scheme (commit
`4e5b5d9ae`).

## Verified context

These facts were read from the live method and
[workflow code](../../../src/commonplace/lib/agentic_workflow.py) on
2026-10-02, after the `RT-` change landed.

- **Job order.** Runtime runs first. Memory and epistemic then run in
  parallel; both read the runtime member, neither reads the other. Only
  reconciliation reads all three members.
- **No ID collisions between parallel analysts.** The analyst prefixes
  differ, and each analyst's acceptance refuses declarations without its own
  prefix (`pass_refusals`). Parallel analysts can still declare the same
  referent under two IDs, such as `MEM-OBJ-3` and `EPI-OBJ-2`. That is a
  duplicate referent; only reconciliation sees both and can supersede one.
- **Acceptance checks per analyst job.** `pass_refusals` validates the
  member, resolves its references against the job's inputs, checks the
  declaration prefix, and checks quotations against the frozen source. It
  runs on every analyst job, the first memory round included.
- **`EPI-` IDs reach the memory analyst only in a correction round.** A
  first memory round reads and resolves against `boundary` and `runtime`
  only. A correction round follows a reconciliation return and also receives
  `epistemic`, against which its references then resolve (`memory_job`). The
  memory job's rule to keep supplied `EPI-` IDs unchanged is therefore empty
  in a first round, not contradictory.
- **Splits have no declaring owner.** See the [problem](./problem.md); the
  reconciliation report declares no records.

## A. Targeted repairs, ID grammar unchanged

1. **Better refusal messages.** For an unresolved ID, name the nearest
   declared ID, especially a prefix mismatch: "`RT-OBJ-3` is not declared;
   `MEM-OBJ-3` is." When the unresolved token sits in a range (`RT-RTE-1
   through RT-RTE-4`), say that ranges are not expanded. The archive shows
   ranges in 21 of 60 old results, so this is worth doing regardless.
2. **Reconciliation declares records under a `REC-` prefix.** Give the
   reconciliation report a `## Shared records` section for split parts.
   Cost, corrected on review: beyond the prefix pattern and the type, it
   needs `reconcile_refusals` to stop rejecting any heading other than
   `Reconciliation` and the memory return, `close_round` to copy more than
   the Reconciliation section into the retained member, and a `REC-` prefix
   check; the reconciler would also write route fields and evidence, which
   is the source analysis its job tells it not to redo. Neither member set
   needed it: no reconciliation ever split a record. Dropped.
3. **Return splits to the declaring analyst; block otherwise.** The first
   version of the split-records proposal. Its blocking half turns a
   missing part into a stopped run for runtime or epistemic records, which
   contradicts the current after-blockers rule that such a blocker stays an
   `Unresolved conflict:`. Memory already has a correction round; epistemic
   is read by reconciliation and by memory correction rounds; runtime is
   read by both parallel analysts. Only the return half survives, as rule 3
   of the revised proposal.
4. **Part-of relation and split by declared parts.** The revised
   [split-records proposal](./split-records-proposal.md): a declaration may
   state `Part of: <full ID>`; a split is a supersession by parts members
   already declare; a missing part is a memory return or an unresolved
   conflict. This names the relation the archive shows in every lens
   record that touches a runtime record, removes the ownerless "allocates
   fresh IDs" sentence, and needs no new namespace, grammar, or
   reconciliation declarations. Contract and job-text change; checker
   change optional.

## B. Simpler ID grammar

5. **Drop the kind code: `RT-7`, `MEM-3`.** The `###` kind heading already
   states kind. Reclassifying a record (an object found to be a route) would
   no longer force a new ID. Affected consumers read kind from the enclosing
   heading instead: route-field and conclusion-status checks, `is_absence`,
   and memory comparison profiles; `is_absence` takes a bare ID string, so
   the memory profile check would need a set-wide kind map. Citations would
   stop showing kind, and routes alone are cited about 200 times per set.
   Frozen sets need their own pattern, as bare runtime IDs already do. The
   archive traces no error to kind codes or reclassification.
6. **Code-assigned numbers.** Analysts write local tags such as
   `#### MEM:store-index — label`; a post-acceptance step numbers them
   deterministically. This removes the manual monotonic-allocation rule, a
   plausible error source. Cost: a code step rewrites references in the
   member text. The archive traces no error to numbering.
7. **Label IDs (`rt:session-store`).** Easier to preserve while revising, and
   typos are easier to see. Risk: slugs invite renaming, which the contract
   forbids.

## C. Fewer addressable records

8. **Survey which kinds are cited across members.** Done on 2026-10-02 for
   the two member sets, counting citations from any other member or the
   overview: every declared record of every kind except one claim is cited
   outside its member (pageindex-02: 13 routes, 15 objects, 8 absences, 5
   paths, 2 components, 5 of 6 claims; instinctual-memory-02: all 34). No
   kind can become member-local. Closed.
9. **Machine-readable supersession.** Structured `Supersedes:` and
   `Split into:` lines that the checker resolves, so a reader of an old ID
   can always find its replacements. Compatible with A4; defer until a
   supersession under the current method is observed.

## D. Workflow

10. **Identity pass before reconciliation.** A small job after the parallel
    analysts matches memory and epistemic referents and records merges or
    counterparts. The only observed duplicates are between memory and
    runtime, which the memory analyst had read; no memory-versus-epistemic
    duplicate appears in either member set. Not supported by evidence.

## Current recommendation

1. Do A1 now; ranges and invented IDs are observed habits.
2. Adopt A4 for identity and splits, after the check named in the proposal.
3. Hold B, C9 and D10 until a refusal from a run under the `RT-` method
   points at the grammar, numbering, or parallel-analyst duplicates. The
   operator's reported errors, with their refusal text and stage, are still
   the missing evidence; the archive holds accepted output only.
