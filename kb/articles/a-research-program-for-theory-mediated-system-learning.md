---
description: "Research-program statement on theory-mediated system learning: whether a system that revises retained program theory keeps its own modification coherent under delayed feedback, with the four evidence levels, truth versus fit, and the experiments"
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
---

# A research program for theory-mediated system learning

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples, rival mechanisms, and disputed experimental controls are welcome through the repository's issue tracker.

Suppose an endpoint is slow and a cache is put in front of the service behind
it. The change is small, the tests pass, and the endpoint is fast. Two
requirements later, a feature that needs every read to reflect the preceding
write fails in production: the service had been kept transactional for exactly that
reason, and the reason was written down nowhere the change touched. Nothing in
the change request, the touched files, or the local tests said the cache would
break the program. A later demand exposed the unstated dependency.

The hardest programming decisions are of this kind: not necessarily the ones
that require the most code, but the ones for which no complete local rule or
cheap test says what change will preserve the program's purpose and
organization.

Human programmers handle these decisions imperfectly. They use a partial theory
of the program to choose promising changes, notice conflicts, interpret failed
attempts, backtrack, and revise their understanding. The theory does not replace
search. It keeps search coherent until later requirements and operational
consequences reveal what the first tests could not.

This article presents a research program around one question:

> Can a system use a fallible program theory to keep its own modifications
> coherent under delayed feedback, and revise that theory when the consequences
> arrive?

The system in that question is not a model. It is retained artifacts, tools,
runtime, and correction machinery alongside the model, evaluated together at a
declared boundary. And the question is about learning, not only about editing.

A change to a program, a rule, a schema, or a test is a durable change to the
thing that determines the system's later behavior. When such a change is chosen by a
retained theory, and when its consequences then revise that theory, the
modification is how the system learns — no weight update required. The unit that
learns is [the deployed system rather than the
model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md),
and a change counts as learning when [an improvement
process](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
uses evidence from system behavior to select and retain it, so that it affects
later executions.

What makes this learning path *theory-mediated* is that the theory is
represented as an object the process can apply, doubt, and revise, rather than
being compiled away into behavior. What retained artifacts buy is
addressability at the level of claims: an individual claim can be inspected,
cited, perturbed, withheld, or rescoped. A weight checkpoint can be swapped out
too, but offers far weaker addressability at that level. Claim-level
addressability is also what [three 2026 self-improving harnesses examined for
the program turn out not to
have](../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md):
they retain rule sets or weights, not a revisable theory that guides patch
search and gives later failures a shared target for diagnosis and revision.

The program has two testbeds. Programming agents supplied with persistent
program theory are the harder one, and still prospective. Commonplace —
an agent-operated knowledge base, and the system this article comes from — is
the live one, where the same mechanisms already run on parts of the system's own
operation.

In that loop a language model reads retained Commonplace artifacts, searches and
synthesizes candidate formulations and repository changes, criticizes
alternatives, uses tools for checks and retention, and then works from the
revised state. What stays human is concentrated: the operator supplies most of
the sparse selection signal about whether a candidate fits the larger theory and
the intended system. The research problem is therefore not how to introduce
computation, but how to make that computational search more effective and how to
turn recurring operator judgments into reusable selection and credit-assignment
machinery.

The rest of the article sets out the program's parts: what coherent
modification is, the four functions the architecture separates, the levels at
which evidence for the path is graded, the difference between a claim's truth
and its fit, one recorded episode, the conditions under which the strategy
should be abandoned, where the program parts company with Sutton's later
position, and the two studies that come next.

## Holding a theory means controlling a fallible search

A modification is coherent when it meets the new demand without breaking the
purpose and organization that make the program work. This is the test Peter
Naur set in 1985 for whoever holds a program's theory, and no checklist stands
behind it. What the program's organization requires is not fully stated
anywhere; a partial, fallible account of it is what the theory is. So a change
is rarely shown coherent when it is made. It is shown incoherent later, when a
further demand, an extension, or an operational failure reveals that it broke
something the purpose depended on. The cache change above was incoherent, and
nothing local to the change showed that.

The unit judged is therefore a sequence of modifications, not one change. A
process modifies coherently when the changes it retains keep meeting later
demands, and when it detects and repairs the ones that turn out not to. A
failed first candidate can meet this standard if the process recognizes the
failure, recovers, and revises. A successful first candidate can fail it if it
passes narrow tests while damaging the wider organization in a way the process
cannot detect. The full argument is that [holding a program theory means
sustaining coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

A program theory need not be a complete formal specification or one document.
It may be spread across retained explanations, architectural decisions,
operational observations, learned competence, and code. Two senses need
separating. *Program theory* names that distributed understanding, wherever it
lives. What the program can manipulate is the *retained theory state*: the
addressable artifacts the system can retrieve, cite, perturb, withhold, and
revise. Code and learned competence may embody program theory; only the
retained state can be withheld in an experiment while the model stays fixed.
Nor must a program theory determine a correct first change. It is needed earlier than that: [open-ended improvement
must allocate search before decisive evaluation is
available](../notes/open-ended-improvement-allocates-search-before-evaluation.md),
and the theory is what makes that allocation project-specific.

A theory is doing work when it changes the modification process. It can:

- narrow which candidates are considered;
- identify commitments a local fix must not silently break;
- give an unexpected result an interpretation, one that [counts as search
  control only when it changes a later branch
  decision](../notes/failure-explanation-changes-later-branch-decisions.md);
- distinguish evidence against a candidate from evidence against the current
  theory;
- guide rollback and recovery; and
- change what the process tries on the next demand.

Generic search can also generate, test, and discard patches. What separates
theory-guided search from it is causal: withholding or replacing the retained
theory should change proposal, diagnosis, evaluation, recovery, or later
revision. The working conjecture about the mechanism is that [natural-language
project state specializes search heuristics already present in the model's
weights](../notes/natural-language-project-state-specializes-search-heuristics.md).
A theory that merely accompanies the work is documentation, not a demonstrated
part of the learning path.

Naur also argued that programming is theory building, and that the theory
lives in the programmers' heads rather than in the artifacts they leave behind. The companion article [What bound Naur's theory to
programmers](./what-bound-naurs-theory-to-programmers.md) makes one narrow
repair: his argument binds the theory to humans only through [the premise that
machine execution means following formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md),
so it does not establish that only humans can hold a program theory. That
premise is the program's one disagreement with Naur; his account of what a
theory is, his bearer tests, and coherent modification as the decisive test
are adopted as they stand. Removing the premise does not show any current
agent passes his bearer tests, which stays an empirical question.

## Four functions that fail differently

The current architecture separates four functions because they fail in
different ways.

| Function | Current realization | Failure it exposes |
|---|---|---|
| Represent project-specific premises, purposes, commitments, and scope | Retained natural-language and symbolic artifacts | Omission, contradiction, drift, retrieval failure, inert documentation |
| Interpret theory and use it to guide search and diagnosis | A language model | Underspecification, stochastic deviation, bias, post-hoc rationale, theory ignored in practice |
| Execute exact transitions and keep the path alive | Code and a persistent runtime | Faithful execution of the wrong transition, frozen decomposition, truncated horizon |
| Correct proposals and theories, and select what is retained | Tests, validators, held-out tasks, decorrelated criticism, later demands, and operational consequences; for global fit and authorization, the operator | Weak proxies, captured evaluation, viability-only gates, delayed credit assignment, unstated preferences, exogenous selection |

This is a [functionally mixed
architecture](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md),
not a claim that the functions must stay in separate representational forms: a
future learned substrate may host several at once, and stronger models may
absorb parts of the present scaffolding. The split earns its place now because
it makes each role [addressable](../notes/reflection-buys-addressability.md) and
separately testable.

Interpretation and correction must remain distinct. A model can understand and
apply a false theory. Semantic competence does not establish that the theory is
right or that a proposed change is good. Independent or sufficiently
decorrelated evidence must remain able to overturn the candidate's account.

The fourth row contains the operator, and that is where the program's target
lives. Tests can reject a candidate. They do not choose among several viable
candidates for an underspecified purpose, and they do not grant authority to
change the live system. At present those selection and authorization
judgments are mostly human. They are the function the program aims to convert
into reusable machinery, one recurring judgment at a time.

## Evidence comes in levels

The full loop the program wants to observe is:

    retained theory
      -> theory-mediated search or decision
      -> realized change
      -> independent or delayed consequence
      -> read-back against the same theory
      -> retained theory-state revision
      -> changed later operation

Requiring the whole chain before anything counts would discard useful partial
results, so the program distinguishes four levels:

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
not proof that the theory was load-bearing; withholding, replacing, or
perturbing the theory is stronger evidence. The higher levels must also chain:
the theory that guided the change must be the object against which the outcome
is read, and the revised theory must be the one used later. Interpretation,
retention, and read-back [have to share one causal path, not merely one system
boundary](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md);
disconnected witnesses do not establish learning through theory.

## A true claim may still not fit the theory

A theory-mediated system must answer two different questions about a candidate
claim — in Commonplace a note, in a programming project the rationale a change
is made under.

First, is the claim true, valid, or otherwise warranted over its stated scope?
Some claims admit factual checks, formal derivations, consistency tests,
controlled experiments, or bounded benchmarks.

Second, does the claim fit the larger working theory and improve the system's
operation and revision? That is relational. A true claim can be irrelevant,
redundant, badly scoped, or placed at the wrong level of abstraction. A false
claim can appear useful because the current implementation already assumes it.
Fit is not conformity to existing doctrine. A warranted claim that contradicts
the larger theory is evidence that the theory may need revision; fit concerns
the claim's scope, role, and integration.

No present automatic evaluator fully decides whether a candidate belongs in the
larger causal picture, what it should displace, or whether it will keep guiding
coherent modification as later demands arrive. The evidence for fit is
distributed and delayed rather than supplied by one complete local oracle, so it
is exposed one consequence at a time:

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

System use is not a truth oracle, since a system can reward its own
misconceptions. The separate correction function exists to prevent a
self-sealing theory: independent factual and formal verification, and
predictions registered before the evidence arrives, are the checks system use
cannot supply by itself.

## One recorded episode, and its limits

The
[2026-08-30 Commonplace revision record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
provides one concrete human-agent episode. The model read the workshop,
related notes, and repository state, and produced a review, candidate
distinctions, experiments, and repository edits. The operator accepted much of
the result but corrected the Bitter Lesson framing several times, and under
those corrections the theory moved from a set of several defenses against the
objection, to the account given below of the hand-written artifacts as a
bootstrap, and then to that account's first-strategy form, in which current
computation and residual human selection are explicitly separated. The revisions were retained and guided later turns.

At the boundary including operator, model, knowledge base, and tools, this is
observational support for a mediation path, theory learning, and recurrence. At a boundary excluding
the operator, global-fit selection and final acceptance remain exogenous. That is the residue to expect: [transferring the decisions whose
premises, criteria, and checks are available leaves people the
hardest-to-warrant
ones](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).

The episode does not show how much each artifact mattered. Reading and citing
many Commonplace artifacts is a mediation trace; the intervention that would
measure their contribution is the experiment below.

The episode also raises a boundary question the program treats separately: why
the operator's global-fit judgments have not moved into the automatic part of
the system. The companion article
[The decisions that stay human, and what would move them](./the-decisions-that-stay-human-and-what-would-move-them.md)
develops that transfer argument and separates it from [computational
closure](../notes/methodological-and-computational-closure-track-different-changes.md),
which states where decisions happen rather than whether they are any good.

## The hand-crafted parts are a bootstrap the program expects to replace

The obvious objection is that retained explicit artifacts are exactly the
hand-built structure the Bitter Lesson tells us to stop building. The program
cannot deny the premise. Its theories, schemas, validators, decompositions, and
evaluators are at present written by people.

The program's compatibility with the lesson rests on two arguments. The first
is the only rebuttal to the objection that [holds
up](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md):
[production method and representational form are different
axes](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
The lesson is against hand-crafting, not against learning in prompts and code,
so a theory or a validator can itself be a learned product. That makes room for
explicit artifacts. It says nothing in favour of the present hand-written ones.

The second argument is that the present artifacts are a bootstrap: a
hand-crafted starting state that the program expects learning to replace —
much of it, possibly all of it — while the system it started continues. That
is what makes it a bootstrap rather than a scaffold: a scaffold is discarded
once the product stands, whereas here the running system uses its current
theory to guide the search that produces its successors. What is meant to
persist is the loop and its four functions, not any artifact now performing
them. Every present theory, schema, validator, and decomposition is a plank
that search and learning may swap out, and the system stays the same system
through the replacement, as the ship of Theseus does. Hand-crafted
names who produced the current version of an artifact, not a class of artifact
that must stay so: in a loop that has no outside, [machinery persists by
warrant, not by its
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md),
and the starting artifacts are as exposed to replacement as anything else in
the loop's scope. Stated as a condition, the bootstrap [fits the Bitter Lesson
only if learning can outgrow
it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md);
a promised path beyond hand-crafting is cheap, so the expectation has to be
checked rather than asserted, and the abandonment conditions below are the
check.

The bootstrap is not "hand-craft now, learn later". Computation is used inside
the loop from the start; the human judgments that remain where global fit has no
evaluator are recorded as missing selection machinery rather than accepted as
the permanent arrangement; and a judgment that recurs with a stable scope
becomes a test, validator, learned critic, method, or program. The
hand-designed vision and game-playing methods in Richard Sutton's essay put
designer knowledge into the object-level solution and never learned to replace
it. The present strategy differs from them only if its theories, schemas,
validators, decompositions, and evaluators remain challengeable in practice.
Editable files are not enough: a model may rewrite a prompt while every choice
about what may change and how it is judged stays fixed human design. The
companion article [The Bitter Lesson does not require everything to live in
weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops both the rebuttal and the bootstrap account.

Building through a bootstrap is the first strategy being tried, for two
reasons. The first is that global theory fit lacks a complete fixed evaluator.
The second is access: prompts, code, and retained artifacts are the part of the
system a researcher without a training budget can change, and this is the
author's situation. The strategy also has payoffs beyond the reasons for
choosing it. If the [sample-efficiency
conjecture](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
holds, retained theory needs fewer observations where later demands preserve
the structure it names. The theory under test is readable, so the strategy can
be tested by many people, and what the system has learned can be audited, which
serves alignment research. The cost advantage is a starting one: if most of the
loop becomes computational, further gains will again cost compute.

The strategy competes with end-to-end learning, evolutionary search, self-play,
weight updates, and stronger-model baselines. Its scaling test is the research
problem stated at the start: more computation must improve search, and
recurring operator judgments must become reusable selection machinery. The
bootstrap stops fitting the lesson, and the strategy should be abandoned, when:

- system use becomes self-confirming;
- retained theory makes no causal difference;
- more computation does not improve useful search or selection;
- human judgment grows with the corpus instead of falling;
- each new domain needs its own ontology and oracle;
- the current decomposition cannot be challenged, so [learning inside it
  inherits its
  mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md);
  or
- another method does better at comparable total cost.

## Compatible with the lesson, at odds with Sutton's later bet

Compatibility with the 2019 essay is not agreement with what its author now
holds. In a 2026 interview Sutton and Khurram Javed grant that context can be
part of an agent's state and still hold weight change necessary: "So context
can be in the state, too. It could be both, but you still need to be able to
update the weights."
([source](../sources/sutton-javed-why-ai-models-stop-learning.ingest.md),
verbatim). The structuring and generation of new concepts, on their account,
is weight learning, and an agent that stops updating its weights has stopped
learning in the sense that matters.

The program disagrees, and the disagreement is a hypothesis rather than a
premise on either side. Whether updates to readable artifacts — theories,
tests, schemas, programs — can supply the capabilities open-ended learning
needs is the empirical question this program is built to test; the lesson does
not settle it by definition, and neither does the interview. The target is the
same on both sides: Sutton names as his lab's largest ambition a mind that
keeps training itself while staying self-consistent and coherent, which is
coherent modification pursued in weights. The comparative test is to hold
objectives and evaluation fixed and vary which surfaces may update — weights,
natural-language artifacts, symbolic artifacts, or a mixture — and see where
capability grows.

The program's disagreements are therefore few and named: with Naur, one
premise; with the Bitter Lesson essay, none; with Sutton and Javed's later
position, one hypothesis.

## One experiment and one longitudinal study

The experiment tests whether a prepared retained theory state is load-bearing.
Hold model, tools, repository state, inference budget, judging protocol,
acceptance threshold, and authorization procedure fixed; compare:

1. the reference theory — ground truth for a synthetic task whose generating
   rationale is known, or the maintainers' current best account for a real
   project;
2. a fact-matched record without synthesized theory;
3. theory withheld; and
4. plausible but wrong or outdated theory.

The comparison [identifies only the contrasts it actually
runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md),
and the second condition is the contested one. A fact-matched record carries
the same facts, decisions, and history as the theory — commit messages, issue
threads, a changelog — flattened, with the purposes behind decisions and the
dependencies between them removed. The match is on facts, not on information,
since the removed purposes and dependencies are information too. If theory-level
organization is what does the work, the record should behave like withheld
theory. If the record cannot be matched without smuggling that organization
back in, the two conditions collapse, and that is the disagreement the program
most wants exposed.

Each run is a sequence: an initial modification; a delayed demand that
exposes a failure in it; diagnosis and recovery; explicit revision of the
retained theory state; and a further, structurally related demand that can
benefit from the revision. Without the last two stages the experiment can show
theory-guided modification but not learning through theory. Measure candidate
generation, preservation of architectural commitments, diagnosis, backtracking,
recovery, collateral regressions, later-demand performance, and human
intervention. The reference theory should help most where [the later demand preserves
the structure it
names](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
— in the cache case, a theory that records why the service is transactional.
Wrong theory should produce predictable negative transfer. If the central
conjecture is right, withholding theory should damage recovery most. The
same-budget withheld condition is the direct-search baseline; a follow-on
scaling study should compare retained theory against direct search at larger
inference budgets and against stronger models.

The longitudinal study instruments the current human-agent loop. Across a
sequence of real Commonplace improvements, record which retained
artifacts guided model search, which proposals and checks were computational,
which global-fit and credit judgments remained human and why, whether
additional computation was associated with a changed proposal or judgment,
which downstream consequences bore on the
judgment, and whether a recurring correction became a test, validator, learned
critic, method, schema, or program. That last conversion is the one that
compounds: a correction retained as a lesson helps only the tasks that retrieve
it, whereas one retained as a [maintained check improves selection for every
later candidate in its
domain](../notes/oracle-accumulation-improves-the-selection-environment.md). A
later episode should show whether more of the selection decisions had become
computational.

Neither study reaches two of the abandonment conditions: whether the approach
extends to new domains, and whether another method does better. Those need a
later cross-domain comparison against direct computational alternatives.

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

A researcher need not begin by accepting the framing. The knowledge base can
be [vendored read-only into another
project](https://github.com/zby/commonplace/blob/main/INSTALL.md); an agent
given that access, the researcher's own objection or rival mechanism, and the
instruction to reconstruct the strongest available response and design a
discriminating test is a way in that keeps the adversarial control with the
researcher.

The goal is not agreement with a finished theory. It is a small set of claims
whose status can change through criticism and evidence — starting with the one
this article is built around, which is concrete enough to turn out false.
