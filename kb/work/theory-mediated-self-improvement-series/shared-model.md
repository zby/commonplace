# Shared model

This is the workshop's compact working synthesis. It connects the
[target problems](./target-problems.md), durable theory notes, and evaluation
artifacts. It does not promote claims by itself; the linked notes carry their
arguments, evidence, and scope.

## Central research question

Can a computational composite use a fallible, project-specific theory to keep
program modification coherent across proposal, search, backtracking, recovery,
and delayed feedback — and revise both its theory and its behavior when
consequences arrive?

The theory need not deduce the correct first change. Human programmers also
search, fail, reverse changes, and revise their understanding. The relevant
capacity is longitudinal: the program theory must shape which changes are tried,
what the process tries to preserve, how failures are interpreted, and how
recovery and later modification proceed. This is the crux developed in
[holding a program theory means sustaining coherent search under delayed
feedback](../../notes/holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md).

## Working conjecture

Explicit project theory can improve this process by making premises, purposes,
assumptions, and scope addressable. A semantic interpreter can apply and
criticize the theory across cases that no fixed rule already covers. Persistent
execution can carry the process across bounded calls, and evidence can correct
both the candidate change and the theory that guided it.

The conjecture concerns the causal use of theory, not the presence of a document.
Retained theory contributes a handle for targeted use and revision. It does not
supply correctness, retrieval, credit assignment, evaluation, or continuity by
itself, [because reflection buys addressability rather than those downstream
capacities](../../notes/reflection-buys-addressability.md).

## Functional architecture

The current research architecture uses several representational forms because
they make different roles inspectable:

| Functional role | Current realization | Characteristic failure |
|---|---|---|
| Project-specific representation | Retained natural-language and symbolic artifacts carrying premises, objectives, explanations, commitments, and scope | Omission, contradiction, drift, retrieval failure, inert documentation |
| Semantic interpretation and theory-guided search | A language model that applies theory, proposes changes, criticizes candidates, diagnoses failure, and helps recover | Underspecification, stochastic deviation, bias, post-hoc rationale, theory ignored in practice |
| Exact execution and continuity | Code and a symbolic runtime carrying state, scheduling, validation, installation, rollback, and later reactivation | Faithful execution of the wrong transition; frozen decomposition; truncated horizon |
| Independent exposure and read-back | Tests, validators, held-out tasks, decorrelated criticism, later demands, and operational consequences | Weak proxies, captured evaluation, viability-only gates, incomplete coverage, delayed credit assignment |

These roles are distinct because evidence for one does not establish the others.
The architecture need not preserve their current carrier boundaries forever.
[Each residue class needs a different function](../../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md),
but one learned substrate may eventually host several functions. The current
mixed-form arrangement is a provisional, intervention-friendly realization.

## Evidence ladder for theory-mediated improvement

The workshop distinguishes four increasingly strong claims:

1. **Mediation.** The retained theory changes a proposal, evaluation, diagnosis,
   recovery step, or realized intervention.
2. **Empirical contact.** The intervention produces an outcome that bears on the
   theory rather than merely accompanying it.
3. **Theory learning.** The outcome changes the theory's content, scope,
   confidence, status, or operational role. Rejection or deliberate retention
   after a refuting opportunity is a theory-state judgment too.
4. **Recurrent theory-mediated self-improvement.** The updated theory state
   changes a later operation inside the same behavior-determining path.

The strongest recurrent path is:

    retained theory
      -> theory-guided decision or search
      -> realized change
      -> independent or delayed consequence
      -> read-back against the same theory state
      -> retained theory-state revision
      -> changed later operation

The path must be causally co-indexed: provenance must identify which theory state
guided the change and which later state received the outcome. Co-occurrence of a
theory, a successful change, and an unrelated revision inside one boundary is
insufficient. The full distinction is stated in
[theory-mediated self-improvement needs interpretation, retention, and
independent read-back on one path](../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

A contemporaneous citation at the decision point is a cheap
[mediation trace](../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md).
It identifies the theory the process claims to have used. Withholding,
replacing, or perturbing the theory and observing a changed decision is stronger
evidence that the use was load-bearing.

A useful theory-guided change can reach mediation or empirical contact without
reaching recurrence. The record should state the strongest level established
rather than force every episode into the full loop.

## Coherent modification and warranted transfer

The bearer problem and the residual-human-work problem meet at open-ended
modification decisions. No complete local criterion or cheap independent oracle
determines which change preserves the program's organization. A theory-holder
must carry search and recovery until later evidence arrives.

The two problems still ask different questions:

- **Coherent modification:** can the composite use project theory to sustain
  program-specific search, diagnosis, backtracking, and revision?
- **Warranted transfer:** are the premises, authority, correction, and continuity
  needed for that process inside the declared boundary strongly enough that the
  decision can leave the human cut with warrant?

[Warranted transfer may leave people the hardest-to-warrant decisions](../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
when transfer preferentially selects decisions with represented premises,
settled criteria, and checkable outcomes. This is a conditional selection
mechanism, not an established prevalence claim. A cross-sectional shortage of
independent evaluation is consistent with the predicted bottleneck; a direct
test needs before-and-after transfer histories.

An evaluator is necessary for correction but does not replace theory-guided
search or credit assignment. A strong oracle can reject a bad candidate without
identifying which premise, theory, artifact boundary, or production method
should change. The program therefore studies both sides: theory organizes and
interprets search; consequences correct the theory and the changes made through
it.

## Closure, capability, warrant, and power

Computational closure is task-scoped and structural. A claim must declare task
selection, objective and acceptance, system boundary, permitted exogenous
inputs and interactions, horizon, resources, and coverage. Conditional on those
declarations, every required decision and transition must occur inside the
automatic system. See
[task-scoped computational closure](./task-scoped-computational-closure.md).

Closure does not say that the decisions are good. A captured evaluator, a bad
objective, or a no-op loop can be computationally closed. Capability, warrant,
usefulness, and system power require separate evidence. A non-degenerate
milestone pairs structural closure with consequential reach, a declared
capability floor, reject-capable evaluation, continuity, explicit boundary
accounting, and measured outcomes. The
[closure-capability map](./closure-capability-map.md) records these coordinates
and failure patterns.

Performance at least as good as a competent remote programmer is a strong
worker-capability benchmark, not closure. Holding the client fixed exports task
choice, feedback, missing premises, and final acceptance, [because a fixed
client exports the least-warrantable decisions](../../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
The benchmark and warranted closure expose the same difficult client and
acceptance boundary from different sides while measuring different coordinates.

## Bitter Lesson compatibility is a bootstrap thesis

The program does not defend hand-crafted theories and machinery as exceptions
to the Bitter Lesson. It treats them as provisional state for constructing a
more general search-and-learning process over theories, methods, programs,
tests, and eventually parts of the learning machinery itself.

This differs from a hand-designed object-level solution whose features,
heuristics, or decomposition remain the final source of competence in one
predefined area. The intended path can propose, test, retain, revise, and retire
its current artifacts; revise consequential artifact types, decompositions,
routing, and evaluators; and form project-specific theory in domains not
enumerated when the process was designed.

The relevant property is **domain-extensibility**, not competence across several
predefined domains. [A hand-crafted bootstrap fits the Bitter Lesson only if
learning can outgrow it](../../notes/a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md).
The claim is currently architectural and programmatic. It becomes empirical only
where production actually moves from human construction to search, evaluation,
revision, and retention with bounded human judgment.

No carrier receives permanent protection. Natural-language theory, symbolic
machinery, and current evaluators may be absorbed or replaced. The system
succeeds when useful functions continue to earn their place and the production
path becomes more general, not when today's files survive.

## Current bootstrap and testbeds

Commonplace is a human-inclusive reflective testbed. It retains and routes
project theory, supports criticism and revision, and can turn some theory into
operative instructions, validators, schemas, and code. Humans still choose
objectives, supply unrecorded premises, assign much of the blame, authorize
consequential changes, interpret ambiguous evidence, and repair paths beyond
represented coverage.

Programming agents with persistent project-specific theory are the first
demanding external testbed. They isolate the bearer question without requiring
the target program to be the agent itself. Commonplace then provides the
reflective bootstrap in which the same mechanism can be applied to parts of the
system's own operation.

Current evidence supports useful human-agent theory work, inspectable mechanism
traces, and a plausible bootstrap. It does not establish independent
computational theory possession, recurrent self-improvement, task-scoped
closure, or a scalable domain-extensible artifact learner.

## Next discriminating experiment

The next high-value result is a prospective theory intervention on sequential
program modifications. Use the same model, tools, repository state, budget, and
acceptance process under matched conditions:

1. correct project theory;
2. an information-matched record without synthesized theory-level organization;
3. theory withheld; and
4. plausible but wrong or outdated theory.

Each sequence should contain an initial modification and a later demand or
delayed test that exposes whether the first change preserved the program's
organization. Measure candidate generation, architectural preservation,
backtracking, diagnosis, recovery, collateral regressions, later-demand
performance, human intervention, and whether outcome read-back changes a later
episode.

The diagnostic prediction is an interaction: correct theory should help when
the later shift preserves the structure it names; wrong theory should cause
predictable negative transfer; theory withholding should especially damage
recovery and follow-on coherence; and the advantage should shrink where a
complete specification and cheap oracle already settle the task.

## Minimum episode record

A useful episode record should identify:

1. the selected task, objective, boundary, horizon, resources, and starting
   human cut;
2. the retained theory state claimed to guide the decision and the mediation
   evidence;
3. the search, realized change, and acceptance mechanism;
4. the independent or delayed outcome and its read-back against that theory;
5. any theory-state or machinery revision, including rejection, rescoping,
   changed confidence, explicit retention, or deferral;
6. whether the revision changed a later operation; and
7. which dimension moved and which decisions remain human.

The record should state the strongest evidence level reached. Without a
same-theory trace, it may show a useful change but not theory mediation. Without
later use, it may show theory learning but not recurrence.

## Open questions

- What task distribution and horizon distinguish coherent theory-guided search
  from luck, memorization, or generic search with a permissive evaluator?
- Can project theory improve sample efficiency, recovery, or revision cost after
  accounting for retrieval, maintenance, and evaluation?
- How can delayed consequences receive credit when several changes and theory
  revisions intervene?
- Can evaluator construction and decomposition revision move into the learning
  path without relocating unlimited human judgment one level upward?
- What cross-domain sequence would demonstrate domain-extensibility rather than
  a broad but fixed ontology?
