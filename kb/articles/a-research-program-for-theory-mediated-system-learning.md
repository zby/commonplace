---
description: "Research program on whether an automated software-development system built from weights, prompts, code, and runtime can retain and revise project theory to keep successive modifications coherent under delayed feedback"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
  - kb/notes/natural-language-project-state-specializes-search-heuristics.md
  - kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md
  - kb/notes/open-ended-improvement-allocates-search-before-evaluation.md
  - kb/notes/failure-explanation-changes-later-branch-decisions.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/oracle-accumulation-improves-the-selection-environment.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/computationally-directed-self-improvement-is-a-reallocation.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/sources/programming-as-theory-building.ingest.md
---

# A research program for theory-mediated system learning

> **Draft.** This article is circulating for comments. Counterexamples, rival mechanisms, and disputed experimental controls are welcome through the repository's issue tracker.

Peter Naur's [1985 essay *Programming as Theory
Building*](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf)
argues that programmers do more than produce code. They build and hold a
project-specific theory: an understanding of how the program maps to its world,
why its parts are as they are, and how new demands can be incorporated without
destroying its structure.

Modern coding agents can already propose, implement, test, and retain changes as
components of larger software-development systems. Model weights supply learned
competence; prompts carry the current task, project theory, evidence, and
constraints; code and runtime provide tools, exact transitions, persistence,
and checks. Together these components form an automated software-development
system — a software factory in the broad sense.

> Can an automated software-development system hold and revise a fallible theory
> of the software it builds well enough to keep successive modifications
> coherent when decisive feedback arrives only later?

This article sets out a research program for answering that question. It does
not report that a current system already succeeds.

The [deployed system rather than the
model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) is
the unit of learning. Any behavior-determining surface within it can become a
learning target: model weights, prompt templates and the retained state from
which prompts are assembled, code, tests, schemas, tools, or runtime policy. A
change counts as learning when an [improvement
process](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
uses evidence to select and retain it so that later operation depends on it. No
weight update is required.

The path is *theory-mediated* when addressable retained theory does more than
accompany the work: it guides proposal, diagnosis, evaluation, or recovery, and
later consequences can revise the same theory state. An individual claim can
then be inspected, cited, withheld, perturbed, or rescoped. A weight checkpoint
can also be replaced, but normally offers much weaker claim-level
addressability.

The program studies the transition with two linked testbeds. Commonplace, the
agent-operated knowledge base from which this article comes, is the live
human-agent system. Programming agents supplied with persistent program theory
are the harder and still prospective case. In Commonplace, the model retrieves
retained project knowledge, searches and criticizes candidate formulations and
repository changes, and uses tools for local checks. The operator still supplies
much of the sparse global-fit signal and final authorization.

Putting the operator inside the boundary makes the current learning path
visible, but [human-inclusive membership is
cheap](../notes/computationally-directed-self-improvement-is-a-reallocation.md).
The program therefore holds that boundary fixed and reports each
decision-bearing function as [human, computational, or
joint](../notes/methodological-and-computational-closure-track-different-changes.md).
Progress is reallocation toward computational supply. The automation endpoint is
reached when the human participants are no longer a cut set: over the declared
task scope and horizon, the boundary can contract to the technical system and
the same improvement pathway still completes. That is an actor-allocation test,
not a success test; coherent modification and [warrant for unattended
decisions](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) still need
independent evidence.

The immediate Commonplace problem is therefore not to introduce computation,
but to improve computational search and turn recurring operator judgments into
reusable selection and credit-assignment machinery.

Current systems establish adjacent pieces. [Three 2026 self-improving harnesses
examined for the
program](../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)
retain rules or weights rather than a revisable theory that guides patch search.
[Workspace
optimization](../sources/workspace-optimization-how-to-train-your-agent.ingest.md)
revises code and text around a frozen model from prediction failures and replays
recent transitions after edits. Its theory concerns an external environment
within one run; its role decomposition, validation, and adoption policy remain
fixed, and persistence across sessions is not shown. These systems demonstrate
parts of the path without yet demonstrating persistent theory-mediated
modification of the behavior-determining system itself.

## Holding a theory means controlling a fallible search

Naur's test is longitudinal. A modification is coherent when it meets a new
demand without breaking the purpose and organization that make the program work.
Because that organization is only partly stated, a later extension or
operational failure may show that an earlier locally successful change broke
something important.

The unit judged is therefore a sequence of modifications, not one patch. A
failed first candidate can belong to coherent modification when the process
recognizes the failure, recovers, and revises. A successful first candidate can
fail the test when it passes narrow checks while damaging the wider organization
in a way the process cannot detect. [Holding a program theory means sustaining
coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

A program theory need not be a complete formal specification or one document.
It may be distributed across retained explanations, architectural decisions,
operational observations, learned competence, and code. *Program theory* names
that wider understanding. The *retained theory state* is the addressable part
the system can retrieve, cite, withhold, and revise. Code and learned competence
may embody the theory, but only retained state can be withheld while the model
stays fixed in the proposed experiment.

Theory matters before a correct answer is available. [Open-ended improvement
must allocate search before decisive evaluation
exists](../notes/open-ended-improvement-allocates-search-before-evaluation.md),
and retained theory can make that allocation project-specific. It can:

- narrow candidates and identify commitments a local fix must preserve;
- interpret an unexpected result and distinguish a bad candidate from a bad
  theory;
- guide rollback, recovery, and the choice of the next branch; and
- revise what later demands cause the process to try.

Generic search can also generate, test, and discard patches. The distinction is
causal: withholding or replacing the retained theory should change proposal,
diagnosis, evaluation, recovery, or later revision. The working mechanism is
that [natural-language project state may specialize search heuristics already
present in model
weights](../notes/natural-language-project-state-specializes-search-heuristics.md).
A theory that merely accompanies the work remains documentation rather than a
demonstrated part of the learning path.

Naur bound program theory to programmers partly through a crucial [premise that
machine execution means following formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
Trained recognizers make that premise contestable, so his essay does not settle
in advance that only humans can hold a program theory. The companion article
[What bound Naur's theory to
programmers](./what-bound-naurs-theory-to-programmers.md) develops this narrow
departure. Naur's bearer tests and coherent modification standard otherwise
remain the program's tests; removing the premise does not show that any current
agent passes them.

## Four functions that fail differently

The program uses several decompositions for different questions. A
[proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
requires search, reject-capable evaluation, and operative retention. [Residue
analysis](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md)
asks why decisions remain outside a warranted automatic path. The table below
maps those demands onto the present weight-prompt-code system.

| Function | Current realization | Failure it exposes |
|---|---|---|
| Represent project-specific premises, purposes, commitments, and scope | Retained natural-language and symbolic project state | Omission, contradiction, drift, retrieval failure, inert documentation |
| Interpret theory and use it to guide search and diagnosis | Model weights plus prompts assembled from retained project state | Underspecification, stochastic deviation, bias, post-hoc rationale, theory omitted or ignored |
| Execute exact transitions and keep the path alive | Code and a persistent runtime | Faithful execution of the wrong transition, frozen decomposition, truncated horizon |
| Correct proposals and theories, and select what is retained | Tests, validators, held-out tasks, decorrelated criticism, later demands, and operational consequences; for global fit and authorization, the operator | Weak proxies, captured evaluation, viability-only gates, delayed credit assignment, unstated preferences, exogenous selection |

The functions need distinct failure surfaces, not permanently separate
representational forms. A future substrate may host several at once. The current
split is useful because it makes interventions possible: withhold theory,
perturb interpretation, replace evaluation, or truncate continuity.

Interpretation and correction must remain distinct. A model can understand and
apply a false theory; independent or sufficiently decorrelated evidence must be
able to overturn it. The table also exposes the current actor allocation: the
operator supplies much of the global-fit selection and authorization in the
fourth row. Converting recurring parts of that work into reusable machinery is a
central target of the program.

## Evidence comes in levels

The strongest path the program wants to observe is:

    retained theory
      -> theory-mediated search or decision
      -> realized change
      -> independent or delayed consequence
      -> read-back against the same theory
      -> retained theory-state revision
      -> changed later operation

Useful partial results should not be forced into the strongest claim. The
program therefore distinguishes four levels:

1. **Mediation:** changing or withholding theory changes a proposal, evaluation,
   diagnosis, recovery step, or intervention.
2. **Empirical contact:** the intervention produces an outcome that bears on the
   theory.
3. **Theory learning:** the outcome changes the theory's content, scope,
   confidence, status, or operational role.
4. **Recurrence:** the updated theory state changes a later operation on the same
   behavior-determining path.

A [citation at the decision point is a mediation
trace](../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md),
not proof that the theory was load-bearing. Withholding, replacement, or
perturbation is stronger evidence. The higher levels must also be co-indexed:
the theory that guided the change must receive the outcome read-back, and its
revision must be what later operation consumes. [Disconnected witnesses do not
establish learning through
theory](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

## A true claim may still not fit the theory

A theory-mediated system must ask two questions about a candidate claim:

1. Is it true, valid, or otherwise warranted over its stated scope?
2. Does it fit the larger working theory and improve the system's operation and
   revision?

The second question is relational. A true claim can be irrelevant, redundant,
badly scoped, or placed at the wrong level of abstraction. A false claim can
appear useful because the current implementation already assumes it. Fit is not
conformity to doctrine: a warranted contradiction may show that the larger
theory needs revision.

No present automatic evaluator fully decides global fit. Evidence arrives
through changed search and recovery, surviving predictions, later demands,
rival or ablated theories, repair and human-intervention costs, and transfer.
The live system can therefore serve as an [initial selection
environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md):
claims earn provisional standing by affecting building, operation, or repair and
surviving the consequences of that use.

System use is not a truth oracle. It can reward misconceptions already embodied
in the implementation. Independent factual and formal checks, preregistered
predictions, held-out demands, and transfer tests are needed to keep the working
theory from becoming self-sealing.

## One recorded episode, and its limits

The [2026-08-30 Commonplace revision
record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
documents one human-agent episode. The model read the workshop, related notes,
and repository state; proposed distinctions, experiments, and edits; and
revised them after the operator corrected the Bitter Lesson framing. The
revisions were retained and guided later work.

Under the fixed human-inclusive boundary described above, the record shows
retained-state consumption, theory-state revision, and later reuse in a path
consistent with mediation and recurrence. Its actor allocation remains mixed:
the operator supplied decisive global-fit selection and final acceptance, so the
human participants were still a cut set. Because no matched replay or ablation
was run, the episode also does not estimate how load-bearing the artifacts were.
The companion article [The decisions that stay human, and what would move
them](./the-decisions-that-stay-human-and-what-would-move-them.md) develops that
transfer problem and separates it from structural computational closure.

## One experiment and one longitudinal study

The experiment tests whether a prepared retained theory state is load-bearing.
Hold model, tools, repository state, inference budget, judging protocol,
acceptance threshold, and authorization procedure fixed; compare:

1. a reference theory — ground truth for a synthetic task whose generating
   rationale is known, or the maintainers' current best account for a real
   project;
2. a fact-matched record without synthesized theory;
3. theory withheld; and
4. plausible but wrong or outdated theory.

The fact-matched condition is deliberately contested. It carries the same facts,
decisions, and history as the theory but removes their purposes and dependency
structure. The match is therefore on facts, not information. If theory-level
organization does the work, the flattened record should behave more like
withheld theory. If it cannot be removed without smuggling the organization
back in, the conditions collapse. The experiment can identify only [the
contrasts it actually
runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).

Each run is a sequence: an initial modification, a delayed demand exposing a
failure, diagnosis and recovery, explicit theory-state revision, and a further
structurally related demand. The final two stages distinguish theory-guided
editing from learning through theory. Measure candidate generation,
preservation of commitments, diagnosis, backtracking, recovery, collateral
regressions, later-demand performance, and human intervention. Correct theory
should help most when the later demand preserves the structure it names; wrong
theory should produce predictable negative transfer. The withheld condition is
the same-budget direct-search baseline, followed by comparisons at larger
inference budgets and against stronger models.

The longitudinal study instruments real Commonplace improvements. It records
which artifacts guided search, which proposals and checks were computational,
which global-fit and credit judgments remained human and why, which later
consequences bore on them, and whether recurring corrections became tests,
validators, learned critics, methods, schemas, or programs. A lesson helps only
tasks that retrieve it; a [maintained check improves selection for every later
candidate in its
domain](../notes/oracle-accumulation-improves-the-selection-environment.md).
Later episodes should show named functions moving from human or joint to
computational supply, rather than merely more output being generated by agents.

Neither study tests domain-extensibility or superiority to alternative methods.
Those require later cross-domain comparisons against direct computational
approaches at comparable total cost.

## The bootstrap must outgrow its hand-crafted parts

The Bitter Lesson creates an obvious objection: the program's theories, schemas,
validators, decompositions, and evaluators are currently written by people. The
narrow rebuttal is that [production method and representational form are
different
axes](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Search and learning can produce prompts, theories, tests, and programs as well as
weights. That gives explicit artifacts conceptual room; it does not vindicate
the present hand-written ones.

The broader answer is a prediction about the bootstrap. The running system must
use its current theory and machinery to search for successors that replace much,
possibly all, of that hand-crafted content. What should persist is the learning
loop and the functions it performs, not any present carrier. No component inside
the declared revision surface is exempt merely because it implements the
improvement machinery: [machinery persists by warrant, not by
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
The bootstrap [fits the Bitter Lesson only if learning can outgrow
it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

This is not "hand-craft now, learn later." Computation is already used for
retrieval, proposal, criticism, comparison, editing, testing, and retention.
Human judgments remain where global fit lacks a discriminating evaluator; when a
judgment recurs with stable scope, it should become a test, validator, learned
critic, method, or program. Editable files alone are insufficient if humans
still fix what may change and how it is judged. The companion article [The
Bitter Lesson does not require everything to live in
weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops the full argument.

This is the first strategy being tried for two reasons. Global theory fit lacks
a complete fixed evaluator, and prompts, code, and retained artifacts are the
surfaces available to a researcher without a training budget. Possible further
payoffs are [sample efficiency under structured
shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
and an inspectable learning record. These are hypotheses, not exemptions from
full cost accounting.

The strategy competes with end-to-end learning, evolutionary search, self-play,
weight updates, and stronger-model baselines. It should be abandoned or narrowed
when:

- system use becomes self-confirming;
- retained theory makes no causal difference;
- additional computation does not improve useful search or selection;
- human judgment per useful revision fails to fall as the corpus grows;
- each new domain requires a new human-designed ontology and oracle;
- the decomposition remains outside revision, so [learning inside it inherits
  its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  or
- another method performs better at comparable total cost.

## Compatible with the lesson, at odds with Sutton's later bet

Compatibility with Sutton's 2019 essay is not agreement with his later position.
In a 2026 interview Sutton and Khurram Javed allow context to be part of an
agent's state but still require weight change: "So context can be in the state,
too. It could be both, but you still need to be able to update the weights."
([source](../sources/sutton-javed-why-ai-models-stop-learning.ingest.md),
verbatim).

The program treats the necessity of weight updates as an empirical hypothesis.
Its competing hypothesis is that updates to theories, tests, schemas, programs,
or mixtures of representational forms can supply some capabilities needed for
open-ended learning. The comparative test is to hold objectives and evaluation
fixed, vary which surfaces may update, and see where capability grows. The
program therefore parts from Naur on a machine-criteria premise, from the Bitter
Lesson essay on none, and from Sutton and Javed's later position on one open
hypothesis.

## The invitation

The program is open to disagreement at concrete points. A researcher can:

- challenge the account of coherent modification;
- propose a rival mechanism that does not require retained theory;
- improve the controls for the theory intervention;
- develop a less circular test of global theory fit;
- identify a better first computational strategy; or
- show that evaluator and decomposition construction remain dependent on
  bespoke human judgment.

The knowledge base can be [vendored read-only into another
project](https://github.com/zby/commonplace/blob/main/INSTALL.md). A researcher
can give an agent that access together with their own objection or rival
mechanism and ask it to reconstruct the strongest response and design a
discriminating test. The goal is not agreement with a finished theory, but a
small set of claims whose status can change through criticism and evidence.
