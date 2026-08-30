---
description: "Research program on whether an automated software-development system built from weights, prompts, code, and runtime can retain and revise project theory to keep successive modifications coherent under delayed feedback"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md
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
  - kb/notes/lightweight-search-control-does-not-license-adoption.md
  - kb/notes/backtracking-keeps-lightweight-search-control-provisional.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/methodological-and-computational-closure-track-different-changes.md
  - kb/notes/computationally-directed-self-improvement-is-a-reallocation.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/sources/programming-as-theory-building.ingest.md
---

# A research program for theory-mediated system learning

> **Draft.** This article is circulating for comments. Counterexamples, rival mechanisms, and disputed experimental controls are welcome through the repository's issue tracker.

## The question and the two testbeds

Peter Naur's [1985 essay *Programming as Theory
Building*](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf)
argues that programmers do more than produce code. They build and hold a
project-specific theory: an understanding of how the program maps to its world,
why its parts are as they are, and how new demands can be incorporated without
destroying its structure.

Modern coding agents already propose, implement, test, and retain changes inside
larger software-development systems. Model weights supply learned competence;
prompts carry the current task, project theory, evidence, and constraints; code
and runtime provide exact transitions, persistence, tools, and checks. Together
these components form an automated software-development system — a software
factory in the broad sense.

> Can such a system hold and revise a fallible theory of the software it builds
> well enough to keep successive modifications coherent when decisive feedback
> arrives only later?

This article sets out a research program for answering that question. It does
not report that a current system already succeeds.

The [deployed system rather than the
model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) is
the unit of learning. Model weights, prompt templates and retained prompt state,
code, tests, schemas, tools, and runtime policy can all be learning targets. A
change counts as learning when an [improvement
process](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
selects and retains it from evidence so that later operation depends on it. No
weight update is required.

The path is *theory-mediated* when addressable retained theory guides proposal,
diagnosis, evaluation, or recovery, and later consequences can revise the same
theory state. A claim can then be inspected, cited, withheld, perturbed, or
rescoped. A weight checkpoint can also be replaced, but normally offers much
weaker claim-level addressability.

The program uses two linked testbeds. Commonplace, the agent-operated knowledge
base from which this article comes, is the live human-agent system. Programming
agents supplied with persistent program theory are the harder prospective case.
In Commonplace, the model retrieves project knowledge, searches and criticizes
candidate formulations and repository changes, and uses tools for local checks.
The operator still supplies much global-fit selection and final authorization.
The present evidence therefore concerns a human-inclusive learning path, not a
technical subsystem that can complete the same path alone.

## Holding a theory means controlling a fallible search

Naur's test is longitudinal. A coherent modification meets a new demand without
destroying the purpose and organization that make the program work. Because
those are only partly stated, a later demand may expose damage caused by an
earlier locally successful change.

The unit judged is therefore a sequence, not one patch. A failed first candidate
can belong to coherent modification when the process recognizes the failure,
recovers, and revises. A successful first candidate can fail the test when it
passes narrow checks but damages the wider organization in a way the process
cannot detect. [Holding a program theory means sustaining coherent search under
delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

A program theory need not be a complete formal specification or one document. It
may be distributed across retained explanations, architectural decisions,
operational observations, learned competence, and code. *Program theory* names
that wider understanding. The *retained theory state* is the addressable part
the system can retrieve, cite, withhold, and revise. The proposed intervention
isolates this state while holding model weights and symbolic state fixed.

Theory matters before a correct answer is available. [Open-ended improvement
must allocate search before decisive evaluation
exists](../notes/open-ended-improvement-allocates-search-before-evaluation.md).
Retained theory can narrow candidates, identify commitments a local fix must
preserve, interpret unexpected results, guide rollback and recovery, and change
what later demands cause the process to try.

Some of those judgments can remain provisional. As [lightweight search
controls](../notes/lightweight-search-control-does-not-license-adoption.md), they
allocate work among branches or probes without licensing adoption.
[Backtracking keeps them
provisional](../notes/backtracking-keeps-lightweight-search-control-provisional.md)
when contrary evidence arrives.

Generic search can also generate, test, and discard patches. The distinction is
causal: withholding or replacing retained theory should change proposal, branch
allocation, diagnosis, evaluation, recovery, or later revision. One working
mechanism is that [natural-language project state may specialize search
heuristics already present in model
weights](../notes/natural-language-project-state-specializes-search-heuristics.md).
A theory that merely accompanies the work remains documentation.

Naur bound program theory to programmers partly through a premise that
[equates machine execution with formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
Trained recognizers make that premise contestable, but breaking the inference
does not show that any current agent passes Naur's bearer tests.

### Where the program sits

Two older lineages supply different halves of the proposal. Computational
reflection, runtime models, requirements reflection, and architecture-based
self-adaptation make a system's own structure or goals causally available to
guide change, but normally keep the modeling language, adaptation operators, and
evaluation machinery supplied. Explanation-based learning and symbolic theory
refinement let an explicit fallible theory guide inference and change after
empirical failure, but usually model an external domain rather than the
learner's own software organization.

The program proposes to test their conjunction: an addressable theory of a
software system's purposes and organization guides changes to the
behavior-determining system; delayed consequences revise the same theory; and
the revision changes later modifications while the adaptation machinery remains
challengeable. The [positioning
note](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md)
develops the two lineages and the relevant experimental competitors.

[Workspace
Optimization](../sources/workspace-optimization-how-to-train-your-agent.ingest.md)
is a close contemporary LLM-agent implementation analogue, not the overall
closest antecedent. It combines a frozen model with editable code and text,
routes prediction failures toward responsible artifacts, and replays earlier
transitions. Its explicit theory primarily models an external environment within
one run; its decomposition and adoption machinery remain fixed; and
cross-session recurrence of a program self-theory is not shown. [Three 2026
self-improving harnesses examined for the
program](../notes/evidence/three-2026-harnesses-retain-rules-or-weights-not-a-revisable-theory.md)
expose other nearby fragments.

## Four functions that fail differently

Different decompositions answer different questions. A
[proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
describes update-loop anatomy; [residue
analysis](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md)
asks why warranted automatic transfer stops. The table maps those demands onto
the current weight-prompt-code system.

| Functional role | Current realization | Characteristic failure |
|---|---|---|
| Retained project state | Natural-language theory, intent, rationale, and history together with code, tests, schemas, configuration, checkpoints, and evidence records | Omission, contradiction, drift, stale mappings, retrieval failure, or an incomplete symbolic snapshot |
| Model-mediated semantic operation | Model weights plus a call-specific prompt assembled from relevant project state | Underspecification, stochastic deviation, bias, post-hoc rationale, or project theory ignored in practice |
| Independently executed symbolic operation | Code plus a runtime carrying exact transitions, scheduling, validation, installation, rollback, and later reactivation | Faithful execution of the wrong transition, frozen decomposition, incomplete coverage, or truncated horizon |
| Independent exposure and read-back | Tests, validators, held-out tasks, decorrelated criticism, later demands, reviews, and operational consequences; for much global fit and authorization, the operator | Weak proxies, captured evaluation, viability-only gates, delayed credit assignment, unstated preferences, or exogenous selection |

The functions need distinct failure surfaces, not permanently separate
representational forms. This split makes interventions possible: withhold
theory, perturb interpretation, replace evaluation, or truncate continuity. A
future substrate may host several functions at once.

The same code can be read into a prompt as evidence and later executed by a
symbolic runtime. The distinction concerns its consumption path, not its
authorship. Symbolic execution can be exact while implementing the wrong
requirement. Likewise, a model can understand and apply a false theory;
independent evidence must be able to overturn it.

The table also exposes the present actor allocation without making it the
article's second subject: the operator still supplies much of the fourth
function. Converting recurring parts of that work into reusable machinery is a
bootstrap target.

## Evidence and evaluation

The strongest path the program wants to observe is:

```text
retained theory
  -> theory-mediated search or decision
  -> realized change
  -> independent or delayed consequence
  -> read-back against the same theory
  -> retained theory-state revision
  -> changed later operation
```

Useful partial results should not be forced into the strongest claim:

1. **Mediation:** changing or withholding theory changes a proposal, branch
   allocation, evaluation, diagnosis, recovery step, or intervention.
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

### Truth and theory fit are different evaluations

A candidate claim must be evaluated both for truth, validity, or warranted scope
and for its fit in the larger working theory. A true claim may be irrelevant,
redundant, badly scoped, or placed at the wrong abstraction level. A false claim
may appear useful because the current implementation already assumes it. A
warranted contradiction may instead show that the larger theory needs revision.

No present automatic evaluator fully decides global fit. Evidence comes from
changed search and recovery, surviving predictions, later demands, rival or
ablated theories, repair cost, human intervention, and transfer. The live system
can therefore serve as an [initial selection
environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md),
but not as a truth oracle. Independent factual and formal checks, preregistered
predictions, held-out demands, and transfer tests are needed to prevent the
working theory from becoming self-sealing.

## Current status and what evidence is missing

The [2026-08-30 Commonplace revision
record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
is an illustration of the proposed path: retained artifacts were read, the
operator corrected the framing, and the revision affected later work. It was not
recorded prospectively enough to establish how load-bearing the theory was,
separate computational from operator contributions cleanly, or support a
comparative result.

The next step is therefore better evidence retention, not a stronger
retrospective claim. Consequential episodes should preserve the theory and
symbolic state supplied to each decision, the alternatives considered, operator
interventions, later consequences, revisions, and the later operations claimed
to depend on them.

A controlled test would vary retained theory while holding the model, code,
tools, task, and budget fixed. At minimum, it should compare usable theory with
theory withheld or deliberately wrong on a sequence where later demands can
expose earlier mistakes. The relevant questions are whether theory changes
search and recovery, whether consequences revise the same theory state, and
whether that revision changes later work. Any result identifies only [the
contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).
Detailed controls and measures should be fixed when the study is run, not
presented here as completed methodology.

A longitudinal Commonplace study should likewise ask whether recurring operator
judgments become reusable search, selection, or credit-assignment machinery and
whether named functions move from human or joint to computational supply. Until
such records exist, these are research directions rather than results.

## The bootstrap must outgrow its hand-crafted parts

The Bitter Lesson creates an obvious objection: the program's theories, schemas,
validators, decompositions, and evaluators are currently written by people. The
narrow rebuttal is that [production method and representational form are
different
axes](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Search and learning can produce prompts, theories, tests, and programs as well as
weights. That gives explicit artifacts conceptual room; it does not vindicate
the present hand-written ones.

Commonplace is already computational. Model-mediated operations perform
retrieval, proposal, criticism, comparison, diagnosis, and editing; symbolic
operations carry repository changes, testing, validation, scheduling, and
retention. Human judgment remains where global fit lacks a discriminating
evaluator. When a judgment recurs with stable scope, it should become a search
control, test, validator, learned critic, method, schema, or program.

That transition is measured by holding the human-inclusive boundary fixed and
recording each decision-bearing function as human, computational, or joint.
Progress means named functions move toward computational supply. Over a declared
task scope and horizon, the technical endpoint is reached when the same
improvement pathway still completes after the human participants are removed.
That actor-allocation test does not establish quality or warrant. [The decisions
that stay human, and what would move
them](./the-decisions-that-stay-human-and-what-would-move-them.md) develops the
full fixed-boundary, contraction, closure, and warrant argument.

The system must also use its current theory and machinery to search for
successors that replace much, possibly all, of the hand-crafted content. What
should persist is the learning loop and its functions, not any present carrier.
No component inside the declared revision surface is exempt because it
implements the improvement machinery: [machinery persists by warrant, not by
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
The bootstrap [fits the Bitter Lesson only if learning can outgrow
it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

This is the first strategy being tried because global theory fit lacks a
complete fixed evaluator, while prompts, code, and retained artifacts are
available without a training budget. Possible payoffs include [sample efficiency
under structured
shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md)
and an inspectable learning record. These are hypotheses, not exemptions from
full cost accounting.

The strategy competes with end-to-end learning, evolutionary search, self-play,
weight updates, and stronger-model baselines. It should be abandoned or narrowed
when retained theory makes no causal difference; system use becomes
self-confirming; more computation increases candidate volume without improving
search or outcomes; recurring operator judgments do not become reusable
machinery; new domains continue to require bespoke human ontologies and oracles;
the decomposition remains protected from revision; or another method wins at
comparable total cost.

The companion article [The Bitter Lesson does not require everything to live in
weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops the full scaling argument, direct alternatives, domain-extensibility,
and the separate disagreement with Sutton and Javed's later requirement of
weight updates.

### The invitation

Researchers can challenge the account of coherent modification, propose a rival
mechanism, improve the intervention controls, develop a less circular test of
global theory fit, identify a better first computational strategy, or show that
selection and evaluator construction remain dependent on bespoke human
judgment.

The knowledge base can be [vendored read-only into another
project](https://github.com/zby/commonplace/blob/main/INSTALL.md). A researcher
can give an agent that access together with their own objection or rival
mechanism and ask it to reconstruct the strongest response and design a
discriminating test. The goal is not agreement with a finished theory, but a
small set of claims whose status can change through criticism and evidence.
