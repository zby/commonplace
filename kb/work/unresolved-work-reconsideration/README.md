# Workshop: reconsider unresolved work as the KB changes

## Question and commission

How can Commonplace discover unresolved work across its existing surfaces,
reconsider it against later changes, and identify useful next actions without
creating another stale backlog or treating adoption as final truth?

**Posed:** 2026-11-08, by the operator during the `kb/log.md` reconciliation.
The operator wants to improve automation of work here, including finding new
sub-goals and curiosity-driven exploration. Unresolved problems should remain
findable because we cannot predict which later change will unlock them. The
operator commissioned this workshop and suggested scanning notes' Open Questions
sections as a useful starting source, not the whole scope.

The operator subsequently narrowed the immediate mechanism: agents already
recognize and complete straightforward work well; expose the broad work surface
and let them recommend the next useful bounded task instead of making hard-problem
research or ranking machinery a prerequisite. The current commission authorizes
writing that instruction and a read-only selection trial. It does not authorize
executing discovered tasks, adopting proposals, modifying library claims, or
retiring artifacts. Further execution needs a separate commission.

## Intended result

Develop and test a bounded instruction that scans unresolved items across
notes, logs, ledgers, proposals and workshops, checks that work is still needed,
and recommends one useful task whose scope, approach and verification are clear.
Recent changes can reveal an opportunity, but a change-range comparison is not
required for every invocation. Do not require a complete inventory or a ranking
model before an agent can select straightforward work.

The [unresolved frontier](../../reference/definitions/unresolved-frontier.md)
is the discoverable field of possible further work, including recurring work
that may need attention. The operator directed that we register this broad
term without prematurely separating research from maintenance. The useful unit
is a possible piece of work, not a file. One workshop may contain several items;
one item may appear on several surfaces. Keep source pointers
and preserve the source's authority rather than copying every item into a second
manually maintained queue. The possible question ledger remains a proposal, not
an existing artifact or a prerequisite for this work.

## Related work and boundaries

- [Lifecycle management](../lifecycle-management/README.md) owns the broader
  artifact-lifecycle investigation. Its [model](../lifecycle-management/lifecycle-model.md)
  identifies search-surface cost and distinguishes retirement operations from
  their triggers. This workshop investigates discovery, reconsideration and
  selection of unresolved work. It can supply candidate triggers and worked
  cases, but does not replace type-specific adoption, extraction or retirement
  rules. Reconcile that workshop's dated state before relying on it as current.
- [Open-ended work economics](../open-ended-work-economics/README.md) investigates
  what should guide automatic search, including returns, costs and uncertainty.
  This workshop supplies a concrete work surface and pilot cases, not a rival
  universal ranking theory. Reuse its findings rather than invent a numerical
  priority score here.
- The [vocabulary collision ledger](../../reference/vocabulary-collision-ledger.md)
  and [unification ledger](../../reference/vocabulary-unification-ledger.md)
  are existing unresolved-choice surfaces with their own maintenance contracts.
- [Search precedes decisive evaluation](../../theory/open-ended-improvement-allocates-search-before-evaluation.md)
  explains why selecting an investigation is not the same as accepting its result.

A live, citable artifact need not represent unresolved work. An unresolved issue
need not receive current effort. Removing an issue from active attention need
not retire its source artifact. These distinctions must survive any shared view.

## Candidate distinctions, not adopted classes

The following may help later selection or evaluation, but none partitions the
frontier or determines membership:

- An unanswered question versus a known operation awaiting execution.
- One-off work versus recurring work, such as reviews.
- A change-triggered opportunity versus work noticed during a broader scan.
- A straightforward local action versus a task needing a consequential choice
  or an untested approach.

These can overlap or change during work. A review can reveal a new question;
a question can become a straightforward check after a new capability ships.
Keep or revise a distinction only when a worked case shows how it improves
selection. No classification schema or mandatory status fields are adopted.
The operator reports that reviews have gone unused because operating the review
system was costly and may need redesign; this is a reason to inspect usability,
not a blanket exclusion of reviews or a commission to redesign them.

## First selection trial

A fresh Sol worker loaded the scan instruction without a supplied candidate
and recommended correcting the stale two-template example in
`kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`.
It checked the open log entry against tracked files, packaging configuration
and ADR 027, and proposed a note-only change with explicit verification and
stop conditions. It made no edits. The parent had already identified this
candidate in earlier work, but did not give it to the worker; it was discoverable
in the log. This shows one successful bounded selection, not novel discovery,
autonomous execution or comparative effectiveness. The later broadening to
recurring-work candidates has not been tried.

## Epistemic constraints

Follow the [epistemic stance](../../reference/epistemic-stance.md).
A [tentative theory](../../theory/definitions/tentative-theory.md) remains open
to criticism regardless of its work status. “Settled enough” must name the use
it licenses: a bounded experiment, routine reliance, or an adopted convention,
not absolute truth. A convention is adopted by decision and judged by its
consequences; that decision does not corroborate every supporting claim.

Keep evidence, permission to act and allocation of attention distinct. Record
stopping and reopening reasons where they help future judgment; reopening
conditions are not an exhaustive list of admissible criticisms. Unknown payoff
is not automatic grounds for exclusion. Include a way for neglected questions
and unanticipated connections to receive attention without claiming exhaustive
search or letting curiosity authorize unbounded work.

## Starting evidence

[Open Questions discovery](./open-questions-discovery.md) is a dated inventory
of heading matches in `kb/theory/`. It finds entry points, not individual
questions, and does not establish that any item remains unresolved. The note
template suggests `## Open Questions`, but the spelling and presence are not
schema-enforced; capitalization and combined-heading variants exist.

The initial source scope is deliberately narrow. A later cross-surface pilot
must also consider open log observations, pending vocabulary entries, live
proposals and active or paused workshop issues. Archive and historical material
are not default unresolved items, but may supply evidence or a reopening case.
The scan must state coverage and omissions rather than call a heading inventory
the full list of unresolved work.

## Next decision and pilot

The [batch scan draft](./scan-and-select-frontier-work.md) extends the initial
single-task trial with broader heading discovery, version-bound assessments,
reconsideration of unchanged questions and relative selection of up to ten
useful next steps. The operator commissioned this draft after noting that
tractability can change even when question text does not. The [2026-11-08 scan record](./scan-results-2026-11-08.md)
retains its first batch trial: four recommendations from twelve assessed work
packages, with version limits and deferred items. The operator then requested
one-by-one reconsideration, starting with whether the first note carries too
much local-system detail. No recommended library change has been executed.
Its initial candidate-discovery scope is `kb/theory/` and `kb/reference/` only,
as directed by the operator; other collections will be covered later. Targeted
reads elsewhere may verify an in-scope candidate but may not expand discovery.
It records scan evidence but does not integrate with the freshness store or
adopt a classification schema. A trial defaults to assessing up to twenty
candidates, selecting up to ten next steps and returning its record in the
response. The caller may override the budget, authorize persistent output or
narrow the two-collection scope; no configuration is required to start.

The existing single-task baseline is invoked as follows:

Invoke [Find the next straightforward useful task](../../instructions/find-next-straightforward-task.md)
in a fresh session, with local read access and no task-execution authority.
The consumer loads the instruction explicitly through this pilot handoff; it is
not an automatically scheduled scan or a promoted skill. Let the worker select
its search path without supplying a known answer. Inspect its recommendation
against current evidence and record the result and limits here.

The first trial tests selection only, not successful autonomous execution or
comparative search quality. Later trials should vary the entry surface before
claiming cross-surface usefulness. A promising recommendation can be returned
to the operator for a separate execution commission. Hard questions can remain
open without requiring this procedure to invent an approach to them.

The executor may choose the sampling and comparison method from current evidence;
no fixed cadence, state schema, scheduler or ranking formula is adopted here.
Return for a decision if the pilot needs library mutations, new source grounding,
or work beyond its bounded inspection. Preserve negative results and omissions.

## Evaluation and closure

Evaluate whether the procedure finds useful next investigations or justified
closures that ordinary task execution missed, and whether its cost and operator
burden are acceptable. Distinguish answered questions from merely promising
opportunities; do not reward the number of new questions generated. A few
examples can justify a bounded follow-up, not a general effectiveness claim.

Close when a bounded pilot supports adopting, revising or rejecting a concrete
reconsideration procedure, with evidence and limits retained; the discovery
coverage and relationship to existing lifecycle operations are explicit; and
remaining questions have named homes or are deliberately deferred. Extract
any adopted procedure or transferable result under its destination contract,
then close this workshop under `kb/work/COLLECTION.md`. A negative result is a
valid outcome; a new ledger or automation service is not required for closure.
