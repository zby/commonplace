---
description: "Research-program statement on theory-mediated system learning: whether a system that revises retained project theory keeps its own modification coherent under delayed feedback, with the four evidence levels, truth versus fit, and the experiments"
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
---

# A research program for theory-mediated system learning

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples, rival mechanisms, and disputed experimental controls are welcome through the repository's issue tracker.

The hardest programming decisions are not necessarily the ones that require the
most code. They are the ones for which no complete local rule or cheap test says
what change will preserve the program's purpose and organization.

Human programmers handle these decisions imperfectly. They use a partial theory
of the program to choose promising changes, notice conflicts, interpret failed
attempts, backtrack, and revise their understanding. The theory does not replace
search. It keeps search coherent until later requirements and operational
consequences reveal what the first tests could not.

This article presents a research program around one question:

> Can a computational composite use a fallible, project-specific theory to keep
> program modification coherent across proposal, search, backtracking,
> recovery, and delayed feedback — and revise both its theory and its behavior
> when consequences arrive?

The composite in that question is not a model but a system: model, retained
artifacts, tools, runtime, and correction machinery, evaluated together at a
declared boundary.

That makes it a question about learning, not only about editing. A change to a
program, a rule, a schema, or a test is a durable change to the thing that
determines the system's later behavior. When such a change is chosen by a
retained theory, and when its consequences then revise that theory, the
modification is how the system learns — no weight update required. The unit that
learns is [the deployed system rather than the
model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md),
and a change counts as learning when [an improvement
process](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
uses evidence from system behavior to select and retain it, so that it affects
later executions.

What makes the pathway *theory-mediated* is that the theory is represented as an
object the process can apply, doubt, and revise, rather than being compiled away
into behavior. That is what a retained artifact buys and a weight update does
not: something you can point at, withhold, or replace.

Programming agents supplied with persistent project-specific theory are the
first demanding external testbed. Commonplace, an agent-operated knowledge base,
is the live human-agent environment in which the same mechanisms are already
used on parts of the system's own operation.

That loop is already partly computational, and that is the point: computation is
not a later stage waiting to be introduced. A language model reads retained
Commonplace artifacts, searches and synthesizes candidate formulations and
repository changes, criticizes alternatives, uses tools for checks and
retention, and then works from the revised state. What stays human is
concentrated rather than spread: the operator supplies much of the sparse
high-level selection signal about whether a candidate fits the larger theory and
intended system. The research problem is therefore not how to introduce
computation, but how to make that computational search more effective and how to
turn recurring operator judgments into reusable selection and credit-assignment
machinery.

## Holding a theory means controlling a fallible search

A program theory need not be a complete formal specification or one document.
It may be spread across retained explanations, architectural decisions,
operational observations, learned competence, and code. Nor must it determine a
correct first change.

A theory is doing work when it changes the modification process. It can:

- narrow which candidates are considered;
- identify commitments a local fix must not silently break;
- give an unexpected result an interpretation;
- distinguish evidence against a candidate from evidence against the current
  theory;
- guide rollback and recovery; and
- change what the process tries on the next demand.

Generic search can also generate, test, and discard patches. The difference is
causal and project-specific. Withholding or replacing the retained theory should
change proposal, diagnosis, evaluation, recovery, or later revision. A theory
that merely accompanies the work is documentation, not a demonstrated part of
the learning path.

This makes the standard longitudinal. A failed first candidate can belong to
coherent modification when the process recognizes the failure, recovers, and
revises. A successful first candidate can fail the standard when it passes
narrow tests while damaging the wider organization in a way the process cannot
detect. The detailed claim is that [holding a program theory means sustaining
coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

Peter Naur argued in 1985 that programming is theory building, and that the
theory lives in the programmers' heads rather than in the artifacts they leave
behind. The companion article [What bound Naur's theory to
programmers](./what-bound-naurs-theory-to-programmers.md) makes one narrow
repair: his argument does not establish that only humans can hold a program
theory. Removing that premise does not show any current agent passes his bearer
tests, which stays an empirical question.

## Four functions, four ways to fail

The current architecture separates four functions because they fail in
different ways.

| Function | Current realization | Failure it exposes |
|---|---|---|
| Represent project-specific premises, purposes, commitments, and scope | Retained natural-language and symbolic artifacts | Omission, contradiction, drift, retrieval failure, inert documentation |
| Interpret theory and use it to guide search and diagnosis | A language model | Underspecification, stochastic deviation, bias, post-hoc rationale, theory ignored in practice |
| Execute exact transitions and keep the path alive | Code and a persistent runtime | Faithful execution of the wrong transition, frozen decomposition, truncated horizon |
| Correct proposals and theories | Tests, validators, held-out tasks, decorrelated criticism, later demands, and operational consequences | Weak proxies, captured evaluation, viability-only gates, delayed credit assignment |

This is a [functionally mixed
architecture](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md),
not a theorem that the functions must remain in separate representational
forms. A future learned substrate may host
several of them, and stronger models may absorb parts of the present
scaffolding. The current split is valuable because it makes the roles
[addressable](../notes/reflection-buys-addressability.md) and supports
interventions on each one.

Interpretation and correction must remain distinct. A model can understand and
apply a false theory. Semantic competence does not establish that the theory has
genuine reach or that a proposed change is good. Independent or sufficiently
decorrelated evidence must remain able to overturn the candidate's account.

## Evidence comes in levels

The strongest recurrent loop is:

    retained theory
      -> theory-mediated search or decision
      -> realized change
      -> independent or delayed consequence
      -> read-back against the same theory
      -> retained theory-state revision
      -> changed later operation

Using the complete chain as the minimum definition would hide useful partial
results. The program distinguishes four levels:

1. **Mediation:** changing or withholding the theory changes a proposal,
   evaluation, diagnosis, recovery step, or intervention.
2. **Empirical contact:** the intervention produces an outcome that bears on the
   theory.
3. **Theory learning:** the outcome changes the theory's content, scope,
   confidence, status, or operational role.
4. **Recurrence:** the updated theory state changes a later operation inside the
   same behavior-determining path.

[A citation at the decision point is a mediation
trace](../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md),
not proof that the theory was load-bearing. Withholding, replacing, or
perturbing the theory provides stronger evidence. The theory that guided the
change must also be the object against which the outcome is read, and the
resulting theory state must be the one used later. Disconnected witnesses do not
establish learning through theory: interpretation, addressable retention, and
independent read-back [have to share one causal path, not merely one system
boundary](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

## A true claim may still not fit the theory

A theory-mediated learner must answer two different questions about a claim.

First, is the claim true, valid, or otherwise warranted over its stated scope?
Some claims admit factual checks, formal derivations, consistency tests,
controlled experiments, or bounded benchmarks.

Second, does the claim fit the larger working theory and improve the system's
operation and revision? That is relational. A true claim can be irrelevant,
redundant, badly scoped, or placed at the wrong level of abstraction. A false
claim can appear useful because the current implementation already assumes it.

No present automatic evaluator fully decides whether a candidate belongs in the
larger causal picture, what it should displace, or whether it will continue to
guide coherent modification after later demands arrive. This does not make fit
untestable. It means that the evidence is distributed and delayed rather than
supplied by one complete local oracle.

Fit is still exposed, one consequence at a time:

- whether the claim changes search or recovery;
- whether its predictions survive later evidence;
- whether modifications guided by it preserve the system's organization;
- whether a rival or ablated theory does better;
- whether it reduces repair and human intervention; and
- whether it transfers beyond the case that produced it.

The live system under construction can therefore serve as an [initial selection
environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md).
Claims earn provisional standing by making a counterfactual difference to
building, operating, or repairing the system and by surviving the consequences
of that use.

System use is not a truth oracle. A system can reward its own misconceptions.
Independent factual and formal checks, rival theories, preregistered
predictions, withholding interventions, held-out demands, delayed consequences,
and transfer tests are needed to prevent a self-sealing theory.

## One recorded episode, and its limits

The
[2026-08-30 Commonplace revision record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
provides a concrete human-inclusive episode:

1. the model read the workshop, related notes, articles, and repository state;
2. computational synthesis produced a review, candidate distinctions,
   experiments, and repository edits;
3. the operator accepted much of the result but corrected the Bitter Lesson
   framing several times;
4. the theory changed from a defense portfolio, to a conditional bootstrap
   thesis, to a first-strategy account in which current computation and residual
   human selection are explicitly separated;
5. the revisions were retained; and
6. the revised repository state guided later turns.

At the boundary including operator, model, knowledge base, and tools, this
supports mediation, theory-state revision, and recurrence. At a boundary
excluding the operator, global-fit selection and final acceptance remain
exogenous.

The episode does not prove how much each artifact mattered. Reading and citing
many Commonplace artifacts is strong mediation evidence, but an intervention
that withholds, replaces, or reduces them to an information-matched record is
needed to measure their causal contribution.

The episode also raises a boundary question the program treats separately: why
the operator's global-fit judgments have not moved into the automatic part of
the system. The companion article
[The decisions that stay human, and what would move them](./the-decisions-that-stay-human-and-what-would-move-them.md)
develops that transfer argument and separates it from computational closure,
which states where decisions happen rather than whether they are any good.

## The strategy is first, not privileged

The obvious objection is that retained explicit artifacts are exactly the
hand-built structure the Bitter Lesson tells us to stop building. The reply is
deliberately narrow — the [defense portfolio here has one load-bearing
member](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md)
— and the companion article [The Bitter Lesson does not require everything to
live in weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops it: production method and representational form are different axes, so
a theory or a validator can itself be a learned product. That creates room for
explicit artifacts. It does not defend the present hand-written ones.

Building through retained theory is the first strategy being tried, chosen
because global theory fit lacks a complete fixed evaluator, not because it is
the only route. It competes with end-to-end learning, evolutionary search,
self-play, weight updates, and stronger-model baselines. Its scaling test is
whether more computation improves downstream search, and whether recurring
operator judgments become reusable selection machinery. It fails if useful
selection does not improve, if bespoke human judgment does not fall, or if the
current decomposition cannot be challenged — the conditions under which [a
bootstrap stops fitting the Bitter
Lesson](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

## Two next experiments

The first experiment tests whether prepared project theory is load-bearing.
Hold model, tools, repository state, budget, and acceptance fixed; compare:

1. correct project theory;
2. an information-matched record without theory-level organization;
3. theory withheld; and
4. plausible but wrong or outdated theory.

Use sequential programming demands with delayed consequences. Measure candidate
generation, preservation of architectural commitments, diagnosis, backtracking,
recovery, collateral regressions, later-demand performance, and human
intervention. Correct theory should help most where the later demand preserves
the structure it names. Wrong theory should produce predictable negative
transfer. Withholding theory should particularly damage recovery if the
conjecture is right.

The second experiment instruments the current human-agent loop.
Across a sequence of real Commonplace improvements, record which retained
artifacts guided model search, which proposals and checks were computational,
which global-fit and credit judgments remained human and why, whether more
computation changed the result, which downstream consequences bore on the
judgment, and whether a recurring correction became a test, validator, learned
critic, method, schema, or program. A later episode should show whether the
computational selection surface actually grew.

A subsequent cross-domain comparison must test domain-extensibility and compare
the approach with direct computational alternatives. The strategy fails when
system use becomes self-confirming, retained theory makes no causal difference,
additional computation does not improve useful search or selection, human
judgment grows with the corpus, each domain needs a bespoke ontology and oracle,
or another method performs better at comparable total cost.

## The invitation

The program exposes several points where disagreement can be productive. A
researcher can:

- challenge the account of coherent modification;
- propose a rival mechanism that does not require retained theory;
- design stronger controls for the withholding intervention;
- develop a less circular test of global theory fit;
- identify a better first computational strategy; or
- show that evaluator and decomposition construction keep the approach
  permanently dependent on bespoke human judgment.

The goal is not agreement with a finished theory. It is a small set of claims
whose status can change through criticism and evidence. The central one remains
concrete: whether a fallible, project-specific theory can make computational
search and recovery more coherent across novel demands and delayed
consequences.
