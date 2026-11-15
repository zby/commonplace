# Decision lifecycle and evidence

## Goal

Map the consequences of concrete choices about what work enters the project's
durable record and how later readers use it. Use that map to support justified,
provisional decisions for particular kinds of work—not a generally optimal
retention architecture.

The operator opened this workshop on 2026-09-25 around a prematurely accepted
ADR. The current commission broadens the question from ADR placement and access
to the economics of retaining products and accounts of automated work. Git is
the main record in this project. Requiring it in every Commonplace KB is not
part of the present task.

A useful result may be a small change, different arrangements for different
workflows, or a reasoned decision to keep existing practices. We need enough
comparison to understand consequential commitments, not an exhaustive taxonomy,
a complete cost model or proof of optimality.

## Fixed boundaries

These are operator-set premises for this investigation, not hypotheses it must
first test:

- **Use the available harnesses.** Their session traces exist, contain the
  session information and remain available for some time. Trust that record;
  do not audit its completeness or redesign its capture, retention or deletion
  rules. A future harness change is a separate decision.
- **Preserve intermediate artifacts by default in the second repository.**
  The operator set this provisional direction on 2026-11-11 for debugging and
  inspection, without per-file justification. Reconsider workflows with
  substantial churn or repository growth. This does not by itself implement
  capture, synchronization or permission to publish sensitive material.
- **Do not create duplicate primary process records.** Preserve workflow files
  already produced; this does not require copying the harness's entire session
  archive or generating new accounts. Extra production must still earn its cost.
- **Preservation is not main-record admission.** Operational files may be kept
  durably without curated extraction, endorsement or inclusion in the main
  repository. Lasting value may warrant separate extraction; debugging value
  already supplies the accepted class-level reason for operational preservation.
- **Artifacts admitted to the main record must serve their intended uses without session traces.**
  Preserve the necessary context, evidence, reasons and qualifications, directly
  or through other durably retained material. Trace links can be optional
  provenance, not indispensable dependencies. This does not require preserving
  everything needed for every conceivable investigation.
- **Retention, adoption, implementation and observed benefit are distinct.**
  A rejected option can deserve retention. An accepted choice is not thereby
  implemented or corroborated. Existing publication authority remains binding;
  no universal manual-approval gate is proposed here.

These distinctions would still matter under a future arrangement without the
current harnesses. That possibility does not expand this commission.

## Current state

The workshop holds two lines of work with separate completion conditions:
retention, capture and admission, described first, and the improvement
run and operator-decision evidence, described under 2026-11-13. The
entries are dated and in order; where a later entry changes an earlier
one, the later entry says so.

### 2026-11-11 and 2026-11-12: retention, capture and admission

Two concrete arrangements now have dispositions. The ingest working directory
is kept provisionally for one decision about the repair round, with a recorded
end condition. The cache/state investigation led to
[ADR 128](../../reference/adr/128-one-ignored-operational-tree-under-kb-reports-state.md),
implemented in `9a854f3d0`: ignored report outputs share `state/`, and cleanup
is decided per workflow. This resolves the directory split, not admission to
the tracked record or connect freshness.

The ADR-versus-commit comparison remains a design comparison without a selected
carrier policy. The operator has now commissioned a
[workflow intermediate files ledger](./workflow-intermediate-files-ledger.md)
to show current handling against the preservation default. The first pass
identifies deletion, replacement and location gaps; it does not implement
producer changes. Complete its stated coverage gaps before claiming all
workflows are covered. The second repository's publication and setup remain
with the public-state-repository workshop.

On 2026-11-12 four families from the ledger moved under
[ADR 129](../../reference/adr/129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md):
multistage runs, AutoReason bundles, article staging packages and the
memory-landscape synthesis scratch now live under `kb/reports/state/` and are
kept after their workflow ends. The agentic-system analysis process record is
the recorded exception until integration copies it into the state tree.
Version capture, commit cadence and pruning remain open.

The same day two review exercises on long-untouched theory notes supplied
decision-lifecycle evidence. The two-context-boundaries note went through two
gate sweeps and two fix passes: 44 pairs stayed at 36 pass and 8 warn across
both, because the remaining warnings were claim-level and the fix procedure
only scopes; the note was generalized and retitled by operator decision. The
structural-hints note went through one full improvement pass
(`commonplace-review run full-pass`, 13 launches), which handed back `revise`
without editing; the operator judged the residue owned by its neighbours and
deleted the note, recorded on the packet as `alternative-applied`.

### 2026-11-13: operator decisions and the improvement procedure

The review exercises above opened a second line of work here: what the
operator decides during note improvement is evidence, and the three
improvement procedures recorded it in three incompatible ways. What exists
now:

- **Shipped.** The operator-decision record is the read-only
  `commonplace-review decisions` query over the state tree
  ([ADR 130](../../reference/adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md)).
  A strike in a strike list keeps its entry and carries the operator's
  required reason, collected in a session under
  [resolve a strike list](../../instructions/simplification-passes/resolve-a-strike-list.md).
- **Proposed, not adopted.** [One improvement procedure over atomic instructions](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md)
  replaces the full pass, the fix procedure and the simplification passes
  with one instructed procedure whose variants compose the same atoms, with
  each run a typed directory. [Authority grades and learning from operator decisions](../../reference/proposals/authority-grades-and-learning-from-operator-decisions.md)
  covers what the resulting records are used for.
- **In draft here.** The types the first proposal needs, starting with the
  [improvement run type](./improvement-run-type.md) and its
  [answers schema](./improvement-run-answers-schema.md), and the
  [edit-operation type](./edit-operation-type.md). The
  [first variant](./first-variant-fix-findings.md) has had its
  [first run](./first-run.md), with the run types registered
  experimentally under `kb/reports/types/`.
- **Moved out.** Calibration of the higher-order check is the standing
  [higher-order check evaluation workshop](../higher-order-check-evaluation/README.md).
  The literature on ordering concerns in revision is the
  [order of concerns workshop](../order-of-concerns-in-revision/README.md).
  Where operator answers sit in a published state repository is a question
  of the [public state repository workshop](../public-state-repository/README.md).
  Reading occasions are deferred to the work on the unresolved frontier.

### 2026-11-14: atoms before procedures

The operator redirected this line on 2026-11-14: leave the full procedures
for later and fix the atomic procedures first. Work here now covers every
atom of the procedure proposal, the review operations, edit operations and
stops, and brings each to the proposal's atom contract: a typed
instruction file, inputs that are files, a typed stored result, and a way
to run and test it alone.

The operator then narrowed the first step to review operations. The bounded
first slice is now implemented under
[ADR 132](../../reference/adr/132-review-atoms-retain-observations-behind-current-results.md),
with a retained [acceptance record](../../reports/retained/review-atom-acceptance-20261115/README.md).
That result completes the focused review workshop; it does not admit the
remaining report methods or implement the edit-operation and stop drafts here. The operator confirmed on 2026-11-15 that the two
other groups follow once it is finished: the edit operations and the
stops, each brought to the same atom contract without arranging atoms
into larger units.

Grouping is decided after all three groups are done. The operator's
direction on 2026-11-15 is that there will be several procedures, not one:
a full pass, a faster procedure for a quick pass, and a focused pass in
which the operator names one defect and a single operation is applied.
The full pass takes long, so the operator chooses by the time available
and by what they see in the note.

Several procedures need two declarations from each atom: what it responds
to, so that a named defect leads to one operation, and its level, so that
a procedure can put higher-order concerns first. Both start as best
effort. The first runs are expected to show wrong or missing values, and
the declarations are refined from those runs. No atom declares a cost in
the first version; the operator sees how long a run takes.

The design for the two groups is planned in
[edit operations and stops as atoms](./edit-and-stop-atoms-plan.md),
written on 2026-11-15. It awaits the operator's choices and has not been
run.

This changes the entry above in three ways:

- The [first variant](./first-variant-fix-findings.md) is shelved as
  drafted. Its [first run](./first-run.md) stays as evidence about the
  types. No second run is planned, so the change that run needed in
  `commonplace-review decisions` is deferred with it.
- The run types stay in scope only as the test harness for an edit
  operation, which is tested as a one-atom run.
- The procedure proposal's first-build criterion, which names the first
  variant, no longer describes the order of work. The proposal is not yet
  edited to say so.

Stability of review verdicts is assumed reachable, by operator direction
the same day; the
[gate verdict stability pilot](../stochastic-operation-testing/pilot-gate-verdict-stability.md)
measures the present gap.

## Candidate for the later edit-operation work: check a proposed fix

In the follow-up to the focused writing-tool comparison, the operator asked to
retain a pre-application fix check here. This is a candidate for the edit-operation
work after review unification, not an adopted atom, a new review type, or a change
to the current fix procedure.

The intended result is to catch a defective replacement before applying it. Given
the finding, the authorized evidence, the original passage and the proposed
replacement, check whether the replacement:

- reproduces the defect it was meant to resolve;
- introduces an unsupported fact or relation;
- drops a qualification or changes the claim;
- requires an author-owned decision outside the operation's authority.

A detected problem calls for a revised candidate or an explicit open item; the
check must not invent the missing fact or select a reserved decision. A writer's
self-check is not independent validation and does not replace closing review.

When edit-operation design starts, decide whether this belongs inside each fix
operation or is useful as a separately runnable check. Keep it deferred until
there is a concrete input/output contract and a case that distinguishes a useful
repair from a superficially compliant but defective one. Evaluation cases are
owned by the [controlled-testing workshop](../stochastic-operation-testing/README.md#evaluation-cases-requested-after-the-focused-writing-tool-comparison),
including paired missing/supplied facts and earned-use controls. No implementation
or model trial is commissioned by this entry.

## Working map

| File | Role |
|---|---|
| [Admission to the main record](./admission-to-the-main-record.md) | Main design-space map: choices, benefits, costs, dependencies, reversibility and open questions. |
| [Git and retained artifacts](./git-and-retained-artifacts.md) | Bounded carrier comparison for decision accounts: ADR files, commit messages and access routes, with equivalent content. |
| [ADR 089 premature placement](./adr-089-premature-placement.md) | Historical evidence that committing a decision account can communicate more than the implementation supports; not a current defect or a measured error rate. |
| [Review storage carrier jump](./review-storage-carrier-jump.md) | Historical evidence that leaving Git and choosing a database were decided as one choice, without comparing an untracked file layout; read from the retained ADRs, not from the original session. |
| [Cache and state hold the same kind of record](./cache-and-state-hold-the-same-kind-of-record.md) | Dated inventory and reader comparison, followed by ADR 128's implemented removal of the directory split; connect freshness remains deferred. |
| [Ingest working directory](./ingest-working-directory.md) | Current handoff retention and the repair-round observation trigger; later debugging-retention direction requires reconsidering its original deletion end condition. |
| [Workflow intermediate files ledger](./workflow-intermediate-files-ledger.md) | Current paths, overwrites, deletions and retention gaps across workflow families; explicit remaining coverage, with no producer changes. |
| [Improvement run type](./improvement-run-type.md) | Draft directory type for one run of the improvement procedure: layout, members, what validation checks and open choices. Not registered; no instance exists. |
| [Improvement run answers schema](./improvement-run-answers-schema.md) | Draft schema for the run's operator decisions: one item per decision, required reasons, and the rules that close pending items. Tested against one example; not registered. |
| [Edit-operation type](./edit-operation-type.md) | Draft type for edit operations: the shared contract, what an instance declares, and how the passes and fix strategies fit. Not registered. |
| [First variant, fix findings](./first-variant-fix-findings.md) | Draft of the fix procedure recomposed over the drafted types, with the three gaps it exposed in them and the preconditions of a first run. |
| [First run](./first-run.md) | Record of the one run made on 2026-11-14: result, what the types enforced, and nine observations about the design. |
| [Overlaps among the review operations](./review-operation-overlaps.md) | Historical overlap map and completed merges; [agreed direction for retaining diagnostic probes in result bodies](./review-operation-overlaps.md#agreed-direction-retain-diagnostic-probes-in-review-results), with instruction changes and evaluation pending. |

The general map remains preliminary. The two bounded dispositions above do
not select a universal retention threshold, mining schedule, cache lifetime,
marker, index or record type. The workflow examples
are starting cases, not an obligation to test every combination. Agentic-system
analysis remains outside the original carrier comparison, but its intermediate
files are included in the ledger because worktree integration does not preserve
all local debugging evidence.

## How to advance the work

**Intent:** resolve a consequential choice at proportionate cost while preserving
the reasons and uncertainty needed to reconsider it.

1. Start with one real use and a choice it makes necessary. Name the future
   operation, its consumer and what information it needs. Existing practice is
   an alternative, not a deficient baseline by assumption.
2. Compare only plausible arrangements. Trace what each requires, saves, loses
   or makes harder. State assumptions rather than inventing numerical precision.
   For carrier comparisons, hold decision content constant; do not compare a rich
   ADR with a terse commit and attribute the difference to the carrier.
3. Identify interactions and reversibility. For example, independent retained
   use requires more extraction than a trace pointer, and trace deletion can
   close an option that is inexpensive to preserve temporarily.
4. Use mechanism inspection and ordinary-work evidence first. A new execution
   test is warranted only by an unresolved question that could change the
   decision, with realistic conditions and proportionate setup cost. Do not
   build a benchmark, new index or alternative KB merely to make a test runnable.
5. Retain the bounded conclusion: chosen or recommended arrangement, intended
   use, deciding reasons, important alternatives, acceptable losses, uncertainty
   and conditions for revisiting it. Keep original expectations and contrary
   outcomes distinguishable from later explanations. No fixed record template
   is required.

A partial comparison is useful if it identifies a real constraint or eliminates
an unsuitable arrangement. If the remaining uncertainty does not justify more
work, state it and stop rather than expanding the investigation indefinitely.

## Current choices worth examining

- Which workflows delete or overwrite intermediates before the second
  repository could preserve them? Complete the ledger's coverage, then select
  separately authorized implementation changes.
- Which operational material deserves curated extraction into the main record,
  beyond preservation in the second repository?
- Which workflows, if any, produce enough churn to justify an exception?
  No measured exception or numerical threshold is adopted.
- For a decision worth retaining, what must survive trace deletion, and which
  existing file or Git access route makes it usable at acceptable cost?
- Do the per-workflow cleanup rules adopted by ADR 128 identify acceptable
  losses in actual use? The cache/state split no longer supplies that policy;
  [the investigation](./cache-and-state-hold-the-same-kind-of-record.md) records why.
- What does the [ingest case](./ingest-working-directory.md) show about the
  repair round, and which extra record-producing machinery still earns its
  cost? Historical preservation now has an accepted debugging use beyond that
  decision; it no longer follows that all records should be deleted afterwards. At this update,
  this machine has no `handoff.yaml` records under `kb/reports/state/ingest/`;
  that local count establishes neither activity on other machines nor failure
  of the arrangement. Trace recovery remains the stated fallback.
- When would on-demand extraction be insufficient compared with selective
  proactive mining? No recurring mining programme is preselected.
- Does a typed run directory hold an improvement run's decisions and edit
  chain at acceptable cost? The [run type draft](./improvement-run-type.md)
  lists its open choices; the first run of a first variant is the test.

Choose among these from actual work. No fixed order, required case count or
claim of broad representativeness is imposed.

## Scope and coordination

This commission permits design work in this workshop and its active-list entry.
It does not by itself authorize paid workers, implementation, evidence
deletion, harness changes, history rewriting or framework-wide policy
adoption. The operator has commissioned implementation case by case, as with
ADR 128, ADR 129 and ADR 130; each such step needs its own instruction.

Start from the shipped [storage contract](../../reference/storage-architecture.md),
[Git history convention](../../reference/adr/074-git-is-the-change-history-layer.md),
[commit trailers](../../reference/adr/075-commit-messages-carry-read-path-trailers.md)
and [content routing](../../reference/adr/077-content-routing-by-regeneration-source-and-consumer.md).
The [ADR type](../../reference/types/adr.md) still governs ADR placement; mapping
alternatives does not change it.

- [Lineage mechanisms](../lineage-mechanisms/README.md) owns general derived-material
  provenance and retention design. Coordinate any broader policy rather than
  duplicating it here.
- [Use-and-outcome records](../use-and-outcome-records/README.md) owns growing
  observational histories. [Design-space studies](../design-space-studies/README.md)
  explores richer design accounts.
- [ADR testing](../adr-testing/README.md) examines existing record usefulness;
  [ADR routing](../adr-routing/README.md) owns consultation routes.
- [Conjecture-store](../conjecture-store/README.md) remains independent. Its schema
  and thresholds do not bind this investigation; possible unification is not a
  prerequisite for completing it.

## Completion

The two lines close separately, and neither holds the other open.

**Improvement run and operator-decision evidence.** This line is done here
when the type drafts have been tried on a first run and either registered
under `kb/reports/types/` or dropped, with the reason recorded. Later changes to
the types belong to the procedure proposal, not to this workshop.

**Retention, capture and admission.** Close when the selected concrete choices have sufficiently understood
consequences and justified provisional dispositions, including keeping current
practice where appropriate. State where each conclusion applies, its evidence
limits and what would warrant reconsideration. Unresolved broader questions can
be explicitly deferred; a universal solution is not a completion condition.

Promote any warranted reusable finding or authorized proposal, preserve the
selected evidence needed without sessions, and then close the workshop under
its collection contract. A proposal is not an implemented change, and a design
comparison is not measured proof of better agent performance.
