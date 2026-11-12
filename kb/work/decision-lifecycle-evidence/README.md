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

## Current state — 2026-11-11

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

Choose among these from actual work. No fixed order, required case count or
claim of broad representativeness is imposed.

## Scope and coordination

This commission permits design work in this workshop and its active-list entry.
It does not authorize paid workers, implementation, evidence deletion, harness
changes, history rewriting or framework-wide policy adoption.

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

Close when the selected concrete choices have sufficiently understood
consequences and justified provisional dispositions, including keeping current
practice where appropriate. State where each conclusion applies, its evidence
limits and what would warrant reconsideration. Unresolved broader questions can
be explicitly deferred; a universal solution is not a completion condition.

Promote any warranted reusable finding or authorized proposal, preserve the
selected evidence needed without sessions, and then close the workshop under
its collection contract. A proposal is not an implemented change, and a design
comparison is not measured proof of better agent performance.
