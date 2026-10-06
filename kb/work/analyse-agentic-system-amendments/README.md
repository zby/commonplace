# Analyse-agentic-system amendments

## Current purpose

Evolve the analysis method to chart the design space of agentic systems and
find solutions useful to Commonplace at reasonable cost. A public database
is a secondary goal. The operator supplied this direction on 2026-10-05;
the durable [design brief](../../reference/agentic-system-analysis-design-brief.md)
holds the goals and evaluation priorities.

The workshop opened on 2026-10-02 to investigate shared record ID errors.
Those investigations and completed repair plans are now
[historical evidence](./history/README.md), not the current execution plan.
The earlier [construction workshop](../analyse-agentic-system/README.md)
records the method's initial development.

## Read first

1. [Analysis design brief](../../reference/agentic-system-analysis-design-brief.md)
   — operator intent; read before design or implementation work.
2. [Versioned corrections candidate](./versioned-corrections-for-agentic-analysis-reports.md)
   — the design reasoning for correcting report text instead of keeping
   amendment overlays. Its first part is implemented; its publication step
   and its evidence questions are not settled.
3. [Live method](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md)
   and [method maintenance](../../agentic-system-analyses/instructions/maintain-analysis-method.md)
   — current execution contracts and the route for authorized method edits.

4. [Separate analysis types from instructions](./separate-analysis-types-from-instructions.md)
   — operator-requested plan for content contracts, intermediate results and
   verifier inputs. Implementation remains separately authorized; coordinate
   with agents already editing the method before executing it.

Read history only when a design question needs its observed cases or an
implementation audit needs its original acceptance criteria.

## State and open choices

As of the 2026-10-05 direction:

- The live method remains authoritative. Since ADR 108 it corrects reports
  in place: verifier blockers go to the declaring analyst. No accepted result
  or retained set changed.
- The open design question is now empirical: whether report correction
  reduces total work and correction failures compared with the stopped
  amendment-overlay runs. Round budgets, declined requests and declared
  dependencies between findings remain open to evidence.
- The [report-correction implementation plan](./report-correction-implementation-plan.md)
  scopes a first change from that candidate: verifier findings go to the
  declaring analyst, for all three reports, and reconciliation is narrowed
  to connecting reports. The operator accepted it on 2026-10-05 and it is
  implemented under [ADR 108](../../reference/adr/108-declaring-analysts-correct-their-reports.md);
  its result section lists what was built. No model run has exercised it,
  and it does not include the publication policy.
- The [publication-policy direction](../../reference/proposals/publishing-analyses-with-unresolved-issues.md)
  was selected for implementation after the classification revision. That
  revision closed on 2026-10-05, so the policy is now unblocked but not live.
  Compare correction mechanisms under the same publication policy.
- The classification revision ([ADR 107](../../reference/adr/107-classify-memory-by-scoped-findings.md),
  method `b95a2bb79`) was tested by the four runs listed in the
  [report-correction plan](./report-correction-implementation-plan.md#why-now).
  In the complete Dynamic Cheatsheet run, `write_agency` and `lineage` kept
  supported findings beside named unresolved parts, as intended. The two stopped
  runs failed on correction propagation, which this workshop owns. Open item:
  the cause of the blocked run `AAS-2026-10-05-dynamic-cheatsheet-56ba8ab235b8-01`
  has not been examined.
- The [analysis collection split](../analysis-collection-split/README.md)
  owns its separate design and implementation plan. Its workshop framing is
  historical relative to the shipped collection; inspect the live method
  before inferring what remains unimplemented.
- The older [Sol follow-up plan](./sol-run-follow-up-plan.md) stays visible
  because its full disposition has not been established. Its status section
  distinguishes delivered or superseded interfaces from items needing review.
  It is not a current implementation commission.

The accepted second Dynamic Cheatsheet run remains unchanged. Its duplicate
identity and overstated initial-inspection findings were accepted limitations;
reopen their repair if the same errors recur, not merely because the audit
exists. Earlier deferred audit items remain deferred.

## Authority and next decision

This workshop supports investigation and design. Neither its framing, the
design brief nor the correction candidate authorizes method implementation,
a new model run, recovery of a stopped run or edits to retained analyses.
Keep separately owned work separate. Existing retained sets are frozen
comparison evidence; do not revise an open run's pinned method to resume it.

The next decision is whether to authorize the trial the
[implementation plan](./report-correction-implementation-plan.md#trial-separately-authorized)
describes. The candidate's
[evidence questions](./versioned-corrections-for-agentic-analysis-reports.md#evidence-needed-before-adoption)
remain questions, not an authorized trial plan. Return a bounded proposal for
operator decision before a further method change or a live trial.

## Closure

Close when the current design question has a recorded decision, or the
operator chooses to stop. Promote any adopted design through the live method
and affected consumers; retain an unadopted design only if it earns a library
proposal. Resolve or explicitly transfer the Sol plan's remaining obligations.

Extract independently useful audit evidence into durable retained reports
when another consumer needs it; leave change history in git. Then delete this
workshop, including its local history, and remove its active-list entry. The
design brief already has a durable home and must not be deleted with the
workshop.
