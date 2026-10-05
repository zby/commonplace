# Versioned corrections for agentic analysis reports

## Design question

Would correcting report text reduce total work and correction failures compared
with keeping the original reports and applying amendments during later use?

This is a candidate under the [process brief](../../reference/agentic-system-analysis-design-brief.md), retained for
future workflow design on 2026-10-05. The single loop below is a working
hypothesis. The brief's priorities govern its evaluation; its worker roles,
report boundaries and correction budget remain design choices.

## Current mechanism and motivating evidence

As of 2026-10-05, [ADR 096](../../reference/adr/096-analysis-passes-declare-their-own-records-under-lens-prefixes.md)
preserves declaring ownership and stable record identities.
[ADR 098](../../reference/adr/098-separate-analysis-reconciliation-from-synthesis.md)
separates reconciliation, record verification and public synthesis.

Corrections have two paths:

- The [reconciler](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/reconcile.md)
  can return findings to the memory analyst. Code retains successive complete
  memory reports and supplies the selected report to later jobs.
- Runtime and epistemic reports stay unchanged. Reconciliation carries
  amendments that the [verifier](../../agentic-system-analyses/instructions/analyse-agentic-system/jobs/verify.md)
  and later consumers must apply, including their effects on dependent tables
  and conclusions. Defects that cannot be repaired can become marked conflicts.

Both memory and epistemic analysts read runtime findings. Correcting a runtime
claim can therefore affect another report as well as passages in its own report.

The local Graphiti run `AAS-2026-10-05-graphiti-0b7292fa4af1-01` stopped after
its final record review. Reconciliation replaced an unsupported extraction
classification with an indeterminate one and named the dependent ledger and
conclusion as affected. The verifier still judged those findings unrepaired.
This suggests difficulty applying the correction, although the amendment's
sufficiency remains a contested semantic judgment. The underlying reports
remain in the ignored run worktree. This was not a controlled comparison.

The current published `dynamic-cheatsheet` set needed only connections in
reconciliation. That clean case does not test correction designs. The earlier
failure described in ADR 096 involved ten registered epistemic records left
undeclared during ID mapping. It supports preserving identities and declaration
ownership; it does not establish that revising report content is unsafe.

## Constraints this candidate tests

The process brief holds the broader priorities. This candidate focuses on three
questions:

- Can a correction reach dependent claims once, instead of requiring each
  later consumer to reconstruct its consequences?
- Can consumers receive a coherent set while originals and rejected revisions
  remain available for auditing the run?
- Does the reduction in interpretation work outweigh additional authoring,
  verification and coordination work?

A revised report can omit a requested repair, lose a supported finding or
introduce a contradiction. Putting the correction into report text does not
establish that the result is correct. Likewise, preserving an original report
moves some work to consumers rather than removing it.

## Candidate: one correction loop

The verifier consolidates findings. The declaring analyst answers requests
about its report. Reconciliation describes cross-report connections and
apparent or standing disagreements. The coordinator applies the publication
policy; code routes work and selects the accepted set.

The repeated sequence would be **reconcile → verify and assess publication
readiness → correct affected reports → repeat**.

1. Reconciliation describes the candidate reports together, addressing any
   previous request about its own account.
2. The verifier assesses the set and earlier responses, distinguishing proposed
   blockers from nonblocking findings. The coordinator accepts it when the
   remaining issues meet the publication policy, or requires corrections from
   the consolidated review.
3. Named analysts revise their reports or explain why a finding should remain.
   Their responses and revisions return through reconciliation and verification.

Only the verifier issues correction requests; reconciliation has no separate
correction cycle. Requests about reconciliation go to its author. A declined
request receives the same evidence-based assessment as any other response;
refusal alone does not establish an irresolvable disagreement.

A request identifies the report, affected records or passages, defect and
supporting evidence. The author supplies a complete revised report, a reason
for retaining a finding, or both for different requests. Changes are limited
to the requests and their consequences. Report differences help the verifier
inspect changes, but cannot establish that unchanged dependent claims remain
supported.

The candidate retains the current ceiling of three verifications as a starting
budget. It can finish earlier with nonblocking issues. A dependent correction
missed in one round may require the next; there is no extra dependency loop.
The trial should determine whether this budget is useful, not treat the number
as an inherent constraint.

### Publication with remaining problems

Use the selected [publication policy for unresolved issues](../../reference/proposals/publishing-analyses-with-unresolved-issues.md).
A local problem can remain when its consequences are explicit and the remaining
conclusions hold. Uncertainty must travel with affected comparison values.
Known false assertions need correction, qualification or withdrawal.

Acceptance means reviewed and usable with its stated limits, not free of
problems. Nonblocking findings need not consume the remaining correction rounds;
later runs can revisit them with better models or methods. At the budget limit,
remaining publication blockers stop the run.

That policy is scheduled for implementation after the
[classification workshop](../analysis-classification-revision/README.md)
closes. Compare correction designs under the same publication policy so that
allowing local issues is not mistaken for evidence that one repair mechanism
works better.

### Selecting reports and retaining evidence

Revised and unchanged reports form one candidate set. The reports and their
review disposition are accepted together. Profile, synthesis and publication
receive that exact set and its declared limits; they do not independently
choose report versions. A refused candidate leaves any prior accepted set
intact.

Predecessors, requests and responses stay in the run directory for audit, as
memory rounds do today. Published sets carry the accepted reports. Storage
layout and selection mechanics remain open; no durable predecessor archive is
proposed without a consumer need.

Today's memory-return machinery supplies part of this path. Requests to all
report authors, coordinator disposition and consistent set selection still
need implementation. An affected analyst adds a job per correction round, and
reconciliation repeats before verification. All repairs wait for verification,
even when reconciliation has already exposed a disagreement.

## Alternatives worth comparing

| Design | Potential benefit | Cost or uncertainty |
|---|---|---|
| Keep amendment overlays | Reuses the current correction path and avoids report rewrites | Every consumer still interprets corrections and their dependencies |
| Let an editor revise reports | Can repair several reports in one step | Gives a worker authority over findings it did not declare; source reinspection and preservation need assessment |
| Produce corrected reports only for publication | Simplifies public consumption | Leaves verification applying overlays and adds a final transformation to check |
| Let reconciliation request repairs before verification | May resolve disagreements sooner | Adds another request authority and correction cycle |

These are alternatives, not designs ruled out by the current evidence.
Author-owned correction, whole-report replacement, separate reconciliation and
review jobs, and a single request authority are choices in this candidate.
Other arrangements may satisfy the same constraints with less total work.

## Evidence needed before adoption

Investigate the uncertain mechanisms before expanding the workflow:

- Judge the consequences of remaining defects for design-space comparisons
  and assessing solutions for Commonplace. A lower defect count alone does
  not establish more useful analyses.
- Exercise a correction that affects a record, ledger and conclusion, and one
  that affects another report. Check the resulting text, not an author's claim
  of completion.
- Exercise a declined request and a local issue accepted with explicit limits.
  Check whether false objections force unnecessary edits or stops.
- Check consistent candidate selection, preservation of unrelated supported
  findings, and uncertainty in downstream comparison values.
- Compare correction failures, rounds and total work with the existing approach
  under the same publication policy. Include later consumption work where it
  can be observed; completion alone is insufficient.

Deterministic checks can establish structure, reference resolution and which
versions were selected. Semantic judgments still depend on models and source
inspection. The trials should narrow the design space and identify the dominant
constraints, not merely demonstrate that this candidate can finish.

Adopting this candidate would require changes to ADR 096's report immutability
and ADR 098's correction organization, plus the code and consumers that enforce
them. This working design does not change live runs or authorize rerunning a
stopped analysis. Extract a library proposal or decision when the design is
settled enough for that role.
