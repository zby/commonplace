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
  - kb/notes/a-retained-theory-intervention-isolates-one-explicit-theory-surface.md
  - kb/notes/disconnected-witnesses-do-not-establish-a-full-causal-path-through-theory.md
  - kb/notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
  - kb/notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/natural-language-project-state-specializes-search-heuristics.md
  - kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md
  - kb/notes/open-ended-improvement-allocates-search-before-evaluation.md
  - kb/notes/lightweight-search-control-does-not-license-adoption.md
  - kb/notes/backtracking-keeps-lightweight-search-control-provisional.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/computationally-directed-self-improvement-is-a-reallocation.md
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
larger software-development systems. Their learned competence comes from model
weights, while prompts, retained project state, code, tools, tests, and runtime
policy shape what happens in a particular project.

> Can such a system hold and revise a fallible theory of the software it builds
> well enough to keep successive modifications coherent when decisive feedback
> arrives only later?

This article sets out a research program for answering that question. It does
not report that a current system already succeeds.

The [deployed system rather than the
model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) is
the unit of learning. Model weights, retained prompt state, code, tests, schemas,
tools, and runtime policy can all be learning targets. A change counts as
learning when an [improvement
process](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
selects and retains it from evidence so that later operation depends on it. No
weight update is required.

The path is *theory-mediated* when addressable retained theory guides proposal,
diagnosis, evaluation, or recovery, and later consequences can revise that
theory so the revision affects later work. Claim-level addressability makes the
theory inspectable, citable, perturbable, and selectively revisable.

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

Program-relevant understanding may be distributed across explanations,
architectural decisions, code, tests, operational state, model competence, and
human participants. The proposed experiment varies one explicit retained theory
surface while holding specified background components fixed. It therefore tests
the causal contribution of that surface, not whether it exhausts the system's
whole program theory, [as the retained-theory intervention note makes
explicit](../notes/a-retained-theory-intervention-isolates-one-explicit-theory-surface.md).

Theory matters before a correct answer is available. [Open-ended improvement
must allocate search before decisive evaluation
exists](../notes/open-ended-improvement-allocates-search-before-evaluation.md).
Retained theory can narrow candidates, identify commitments a local fix must
preserve, interpret unexpected results, guide rollback and recovery, and change
what later demands cause the process to try.

Generic search can also generate, test, and discard patches. The distinction is
causal: withholding or replacing retained theory should change proposal, branch
allocation, diagnosis, evaluation, recovery, or later revision. One possible
mechanism is that [natural-language project state specializes search heuristics
already present in model
weights](../notes/natural-language-project-state-specializes-search-heuristics.md).
A theory that merely accompanies the work remains documentation.

Theory-guided choices need not all meet the standard for final adoption.
[Lightweight search controls](../notes/lightweight-search-control-does-not-license-adoption.md)
can allocate work among branches or probes under weaker evidence, while
[backtracking keeps them
provisional](../notes/backtracking-keeps-lightweight-search-control-provisional.md)
when contrary evidence arrives.

Naur bound program theory to programmers partly through a premise that
[equates machine execution with formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
Trained recognizers make that premise contestable, but breaking the inference
does not show that any current agent passes Naur's bearer tests.

### Where the program sits

Runtime reflection and self-adaptation supply the structural lineage: a system's
own organization or requirements become causally available to guide change.
Theory-refinement work supplies the epistemic lineage: an explicit fallible
theory guides inference and is revised after empirical failure. This program
tests their conjunction while leaving the adaptation machinery itself open to
revision. The [positioning
note](../notes/theory-mediated-system-learning-combines-runtime-self-modeling-with-theory-refinement.md)
develops the comparison and relevant baselines.

[Workspace
Optimization](../sources/workspace-optimization-how-to-train-your-agent.ingest.md)
is a close contemporary LLM-agent implementation analogue rather than the
overall closest antecedent. It combines a frozen model with editable code and
text, but its explicit theory primarily models an external environment within
one run, while its decomposition and adoption machinery remain supplied.

## Four functions that fail differently

The system can be decomposed in several ways. A proposal-selection loop asks
what an improvement update must contain; residue analysis asks why warranted
automatic transfer stops. The table below instead asks which functional roles
carry the current path and how each can fail.

| Functional role | Current realization | Characteristic failure |
|---|---|---|
| Retained project state | Natural-language theory, intent, rationale, and history together with code, tests, schemas, configuration, checkpoints, and evidence records | Omission, contradiction, drift, stale mappings, retrieval failure, or an incomplete symbolic snapshot |
| Model-mediated semantic operation | Model weights plus a call-specific prompt assembled from relevant project state | Underspecification, stochastic deviation, bias, post-hoc rationale, or project theory ignored in practice |
| Independently executed symbolic operation | Code plus a runtime carrying exact transitions, scheduling, validation, installation, rollback, and later reactivation | Faithful execution of the wrong transition, frozen decomposition, incomplete coverage, or truncated horizon |
| Independent exposure and read-back | Tests, validators, held-out tasks, decorrelated criticism, later demands, reviews, and operational consequences; for much global fit and authorization, the operator | Weak proxies, captured evaluation, viability-only gates, delayed credit assignment, unstated preferences, or exogenous selection |

The roles need distinct failure surfaces, not permanently separate
representational forms. That separation permits targeted interventions: withhold
theory, perturb interpretation, replace evaluation, or truncate continuity. A
future substrate may host several roles at once.

The same code may also be read into a prompt as evidence and later executed by a
symbolic runtime. Its role follows the consumption path, not its authorship;
exact execution does not establish that the encoded requirement or theory is
correct.

The table also exposes the present actor allocation. The operator still supplies
much of the fourth role. Moving recurring parts of that work into reusable
machinery is therefore a bootstrap target.

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
not proof that the theory was load-bearing; withholding, replacement, or
perturbation is stronger evidence. The higher levels also have to belong to the
same full causal path. Separate witnesses for theory use, outcome, revision, and
later work do not compose automatically into evidence of theory-mediated
learning, [because disconnected witnesses do not establish a full causal path
through
theory](../notes/disconnected-witnesses-do-not-establish-a-full-causal-path-through-theory.md).

### Warrant and theory fit are different evaluations

A claim can be well warranted yet irrelevant, redundant, badly scoped, or at the
wrong abstraction level for a working theory. Conversely, a weak or false claim
can appear to fit because the current implementation already assumes it.
[A claim's warrant therefore does not determine its fit in a working
theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md).

No present automatic evaluator fully decides global fit. The live system can
supply evidence through changed search and recovery, surviving predictions,
later demands, rival or ablated theories, repair cost, intervention, and
transfer. That makes system use an [initial selection
environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md),
but not an independent warrant oracle: [system use provides evidence of theory
fit and causal usefulness, not independent
warrant](../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).

## Current status and what evidence is missing

The [2026-08-30 Commonplace revision
record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
is an illustration of the proposed path: retained artifacts were read, the
operator corrected the framing, and the revision affected later work. It was not
recorded prospectively enough to establish how load-bearing the theory was,
separate computational from operator contributions cleanly, or support a
comparative result.

Future consequential episodes should therefore preserve enough information to
connect the relevant theory state, decision, realized change, consequence,
revision, and later use. For nondeterministic production, omitted causal joins
cannot reliably be reconstructed after the fact.

The minimum controlled test varies retained theory while holding the model,
code, tools, task, and budget fixed. It should compare usable theory with theory
withheld or deliberately wrong on a sequence where later demands can expose
earlier mistakes. The relevant questions are whether theory changes search and
recovery, whether consequences revise the same theory state, and whether that
revision changes later work. Any result identifies only [the contrast it
actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).

A longitudinal Commonplace study should likewise ask whether recurring operator
judgments become reusable search, selection, or credit-assignment machinery and
whether named functions move from human or joint to computational supply. Until
such records and comparisons exist, these are research directions rather than
results.

## The bootstrap must outgrow its hand-crafted parts

The Bitter Lesson creates an obvious objection: the program's theories, schemas,
validators, decompositions, and evaluators are currently written by people. The
narrow rebuttal is that [production method and representational form are
different
axes](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Search and learning can produce prompts, theories, tests, and programs as well as
weights. That gives explicit artifacts conceptual room; it does not vindicate
the present hand-written ones.

The present loop is already computational. Models retrieve, propose, criticize,
compare, diagnose, and edit; symbolic operations carry repository changes,
testing, validation, scheduling, and retention. Human judgment remains where no
sufficiently discriminating reusable evaluator exists. Recurring judgments are
therefore candidates for search controls, methods, tests, validators, learned
critics, schemas, or programs rather than evidence for a permanently protected
human role.

The bootstrap has two related jobs. First, move named decision-bearing functions
from human toward joint or computational supply while holding the human-inclusive
boundary fixed. Over a declared task scope and horizon, the technical endpoint
is reached when the same improvement path still completes after the human
participants are removed. That actor-allocation test does not establish quality
or warrant. [The decisions that stay human, and what would move
them](./the-decisions-that-stay-human-and-what-would-move-them.md) develops the
full fixed-boundary and warrant argument.

Second, keep the current improvement machinery itself inside the revision
surface. The system must use its present theory and machinery to search for
successors that can replace them. What should persist is the learning loop and
its functions, not any current carrier. [Machinery persists by warrant, not by
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md),
and the bootstrap [fits the Bitter Lesson only if learning can outgrow
it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

This first strategy has three potential payoffs. Explicit theory may improve
[sample efficiency under structured
shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md),
and it leaves an inspectable learning record. More distinctively, the system
being improved is itself an agentic system, so theories of agentic systems can
become part of the theory it uses to diagnose and redesign itself. Commonplace
therefore develops [agentic-systems theory](../agentic-systems/README.md) both as
an external research topic and as candidate operative self-theory for the
model–prompt–tool–runtime system that runs the research and for future
programming agents. If the program works, improving that theory should improve
the system's ability to understand and modify its own organization. These are
hypotheses, not exemptions from full cost accounting.

The strategy competes with end-to-end learning, evolutionary search, self-play,
weight updates, and stronger-model baselines. It should be abandoned or narrowed
when retained theory makes no causal difference, system use becomes
self-confirming, additional computation fails to improve search or outcomes,
recurring human judgments do not become reusable machinery, new domains still
require bespoke human ontologies and oracles, the decomposition remains
protected from revision, or another method wins at comparable total cost.

The companion article [The Bitter Lesson does not require everything to live in
weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops the scaling argument, direct alternatives, domain-extensibility, and
the separate disagreement with Sutton and Javed's later requirement of weight
updates.

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