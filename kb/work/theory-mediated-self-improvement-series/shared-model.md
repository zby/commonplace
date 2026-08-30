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

The conjecture concerns causal use, not the presence of a document. Retained
theory contributes a handle for targeted search and revision. It does not supply
correctness, retrieval, credit assignment, evaluation, or continuity by itself,
[because reflection buys addressability rather than those downstream
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
Withholding, replacing, or perturbing the theory and observing a changed
decision is stronger evidence that the use was load-bearing.

A useful theory-guided change can reach mediation or empirical contact without
reaching recurrence. The record should state the strongest level established
rather than force every episode into the full loop.

## Claim truth and theory fit

A theory-mediated learner must evaluate two properties that should not be
collapsed.

- **Truth, validity, or warranted scope:** does the claim survive empirical,
  formal, source, consistency, or bounded predictive checks?
- **Fit in the working theory:** does the claim belong in the larger causal
  account and improve proposal, diagnosis, recovery, revision, or transfer?

A true claim can be irrelevant, redundant, badly scoped, or placed at the wrong
abstraction level. A false claim can appear useful because the current system
already embodies it. Local truth tests therefore do not fully select a working
theory.

No current fixed evaluator fully decides global theory fit. Fit is exposed by a
distributed and delayed portfolio of consequences: changes to decisions,
predictions, later demands, repair cost, theory interventions, rival
formulations, and transfer. The live system under construction is therefore an
[initial selection environment](../../notes/when-global-theory-fit-lacks-a-fixed-oracle-use-in-building-the-system-is-an-initial-selection-environment.md).

System use cannot replace independent truth tests. It can become self-sealing.
Use rival theories, withholding and replacement interventions, preregistered
predictions, held-out demands, delayed consequences, and transfer to keep causal
fit evidence distinct from factual or formal warrant.

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

## Bitter Lesson pressure and the first bootstrap strategy

The only direct rebuttal to the Bitter Lesson is narrow: learned results need not
all live in weights because production method and representational form are
different axes. That does not defend the present hand-crafted artifacts.

Theory-guided bootstrapping is the first strategy being tried under incomplete
global evaluation. It uses a live system as the initial environment in which
claims can make causal differences and meet delayed consequences. At the same
time, computation should be used wherever discrimination is already adequate:

- generate rival claims, theories, decompositions, and designs;
- search for evidence and counterexamples;
- check local consistency, entailments, references, and formal consequences;
- propose experiments, run ablations, and analyze traces;
- search over artifacts inside bounded evaluator domains; and
- identify recurring human judgments that can become reusable selection
  machinery.

When a judgment stabilizes, it can become a methodology, test, validator,
learned critic, search objective, or program. The strategy is to grow the
computational selection surface through use, not to finish a hand-crafted theory
before learning begins.

[A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow
it](../../notes/a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md).
This is a conditional compatibility criterion, not a defense or uniqueness
claim. End-to-end learning, evolutionary search, self-play, weight updates, and
other direct computational methods remain live alternatives.

The long-run challenge is domain-extensibility. The process must eventually
construct the project-specific theory, representations, methods, and checks
needed for domains not enumerated by the designers; reduce the human share of
fit assessment, evaluator construction, and repair; and permit consequential
parts of its own decomposition and update machinery to be challenged.

No carrier receives permanent protection. Natural-language theory, symbolic
machinery, and current evaluators may be absorbed or replaced. The strategy
succeeds when the production path becomes more general and competitive, not when
today's files survive.

## Current testbeds

Commonplace is a human-inclusive reflective testbed. It retains and routes
project theory, supports criticism and revision, and can turn some theory into
operative instructions, validators, schemas, and code. Humans still choose
objectives, supply unrecorded premises, judge much global fit, assign blame,
authorize consequential changes, interpret ambiguous evidence, and repair paths
beyond represented coverage.

Programming agents with persistent project-specific theory are the first
demanding external testbed. They isolate the bearer question without requiring
the target program to be the agent itself. Commonplace then provides the
reflective environment in which the same mechanism can be applied to parts of
the system's own operation.

Current evidence supports useful human-agent theory work, inspectable mechanism
traces, and an initial environment for testing the strategy. It does not
establish independent computational theory possession, recurrent
self-improvement, task-scoped closure, domain-extensible artifact learning, or
superiority to more direct computational approaches.

## Next experiments

### Theory intervention

Test whether prepared project theory is load-bearing on sequential program
modifications. Use the same model, tools, repository state, budget, and
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

### Selection-environment bootstrap

Instrument a sequence of real Commonplace improvements. For each consequential
claim or method, record:

1. which candidates were generated computationally;
2. which truth, validity, or local checks were automatic;
3. which judgment of global fit remained human and why;
4. which downstream system consequences bore on that judgment;
5. whether rival or ablated claims changed the result;
6. whether a recurring judgment became a test, validator, critic, method, or
   program; and
7. how the human and computational shares changed on a later episode.

This is a nearer test of the bootstrap strategy than demanding immediate
cross-domain autonomy. It can show whether the selection machinery is actually
growing or whether "bootstrap" merely renames continued human production.

A later cross-domain test should compare this process with direct computational
baselines and ask whether it constructs new theory and evaluation machinery
without a bespoke human-built ontology for each domain.

## Minimum episode record

A useful episode record should identify:

1. the selected task, objective, boundary, horizon, resources, and starting
   human cut;
2. the retained theory state claimed to guide the decision and the mediation
   evidence;
3. evidence for the truth, validity, or scope of the claims used;
4. the search, realized change, and acceptance mechanism;
5. the independent or delayed outcome and its read-back against that theory;
6. any theory-state or machinery revision, including rejection, rescoping,
   changed confidence, explicit retention, or deferral;
7. whether the revision changed a later operation;
8. which global-fit judgments remained human and whether any became reusable
   selection machinery; and
9. which dimension moved and which decisions remain human.

The record should state the strongest evidence level reached. Without a
same-theory trace, it may show a useful change but not theory mediation. Without
later use, it may show theory learning but not recurrence. Without growth in
selection machinery, it does not support the bootstrap strategy.

## Open questions

- What task distribution and horizon distinguish coherent theory-guided search
  from luck, memorization, or generic search with a permissive evaluator?
- Can project theory improve sample efficiency, recovery, or revision cost after
  accounting for retrieval, maintenance, and evaluation?
- Which parts of global theory fit can be operationalized without encoding the
  present theory into the evaluator?
- How can delayed consequences receive credit when several changes and theory
  revisions intervene?
- Which recurring human judgments should be converted first into tests,
  validators, learned critics, or search objectives?
- What direct computational baseline provides the strongest alternative first
  strategy?
- What cross-domain sequence would demonstrate domain-extensibility rather than
  a broad but fixed ontology?
