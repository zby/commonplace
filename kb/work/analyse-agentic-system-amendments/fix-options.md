# Fix options for the shared record IDs

**Status:** brainstorm, 2026-10-02. Agent-proposed options; none adopted.
Judged against the `RT-` prefixed scheme that was uncommitted on that date.

## Verified context

These facts were read from the live method and
[workflow code](../../../src/commonplace/lib/agentic_workflow.py) on
2026-10-02; recheck them after the `RT-` change lands.

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
   `MEM-OBJ-3` is." If the operator's observed errors are mostly prefix or
   typing slips, this may remove most of them.
2. **Reconciliation declares records under a `REC-` prefix.** Give the
   reconciliation report a `## Shared records` section for split parts.
   `set_record_errors` already collects declarations from every body, so the
   checker change is mainly the prefix pattern plus the type change. A
   distinct prefix avoids attributing the record to an analyst that never
   declared it. Cost: the reconciler writes full route fields for each part,
   drawn from the combined record's evidence already in the set.
3. **Return splits to the declaring analyst.** The
   [split-records proposal](./split-records-proposal.md). Memory has a
   correction round already. Epistemic is read only by reconciliation, so a
   correction round for it would be cheap. Runtime is read by both parallel
   analysts, so correcting it invalidates them; the realistic option is to
   stop the run.

## B. Simpler ID grammar

4. **Drop the kind code: `RT-7`, `MEM-3`.** The `###` kind heading already
   states kind. Reclassifying a record (an object found to be a route) would
   no longer force a new ID. Affected consumers read kind from the enclosing
   heading instead: route-field and conclusion-status checks, `is_absence`,
   and memory comparison profiles. Frozen sets need their own pattern, as bare
   runtime IDs already do.
5. **Code-assigned numbers.** Analysts write local tags such as
   `#### MEM:store-index — label`; a post-acceptance step numbers them
   deterministically. This removes the manual monotonic-allocation rule, a
   plausible error source. Cost: a code step rewrites references in the
   member text.
6. **Label IDs (`rt:session-store`).** Easier to preserve while revising, and
   typos are easier to see. Risk: slugs invite renaming, which the contract
   forbids.

## C. Fewer addressable records

7. **Survey which kinds are cited across members.** Count cross-member
   citations by kind in retained sets. Kinds rarely cited outside their own
   member, perhaps `CLM-*` or `BAP-*`, could become member-local labels and
   leave set-wide identity, duplicate checks and reconciliation duties.
8. **Machine-readable supersession.** Structured `Supersedes:` and
   `Split into:` lines that the checker resolves, so a reader of an old ID
   can always find its replacements.

## D. Workflow

9. **Identity pass before reconciliation.** A small job after the parallel
   analysts matches memory and epistemic referents and records merges or
   counterparts. Reconciliation then handles substance only. This targets
   duplicate referents, not ID collisions, and may lighten each analyst's
   duty to compare with supplied records it cannot fully see.

## Current recommendation

1. Collect the operator's observed errors with their stage first. They
   discriminate between A1 (slips) and B (the grammar itself causes errors).
2. For splits, prefer A2 over A3: a pattern and type change instead of a
   runtime correction branch or a stopped run.
3. Do B4 if the errors involve kind codes or reclassification; its affected
   consumers are few and named.
4. Run C7 as a cheap survey; it may shrink the problem more than any grammar
   change.
