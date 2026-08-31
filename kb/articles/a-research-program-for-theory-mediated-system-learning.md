---
description: "Research program on whether an agentic software-development system can retain and revise project theory to keep successive modifications coherent under delayed feedback"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
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
  - kb/notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
  - kb/notes/a-closed-factory-learning-transition-produces-a-successor-factory.md
  - kb/notes/operative-succession-turns-meta-factory-construction-into-learning.md
  - kb/notes/domain-extensibility-not-closure-determines-factory-reach.md
  - kb/sources/programming-as-theory-building.ingest.md
---

# A research program for theory-mediated system learning

> **Draft.** Comments and counterexamples are welcome through the repository's issue tracker.

> **TL;DR.** A conventional software factory is lifecycle production machinery specialized for a product family. When production evidence computationally changes that machinery and the retained result governs later work, a computationally closed factory-learning occurrence produces a successor factory. Recursive factory construction is prior art; the open question is whether the same process can acquire the specialization needed for previously unanticipated demands. That is a domain-extensibility claim, not a promise of unrestricted universality or universal self-modification.

## The question and the two testbeds

Peter Naur's [1985 essay *Programming as Theory
Building*](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf)
argues that programmers do more than produce code. They build and hold a
project-specific theory: an understanding of what the program must do, why it is
organized as it is, and how that organization can survive new demands.
Crucially, Naur treated this theory as something held by programmers rather than
by the program or its documentation. The machine could execute what had been
formulated, but the theory needed for coherent modification remained with
people—a boundary grounded partly in [Naur's equation of machine execution with
formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).

Modern coding agents make that boundary worth testing. Their learned competence
comes from model weights, while retained project state, tools, and runtime
machinery shape what happens in a particular project.

> Can such a system become a bearer of the fallible project theory Naur reserved
> for programmers — holding and revising it well enough to keep successive
> modifications coherent when decisive feedback arrives only later?

The [deployed system rather than the
model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) is
the learning unit. Learning need not be a weight update; it may also be retained
in project state or executable machinery. A change counts as learning when
evidence from system behavior determines it and operative retention makes later
work depend on it. A [proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
is one implementation; a direct evidence-responsive update need not expose
competing candidates.

The full path is *theory-mediated* when addressable retained theory guides search
or modification, later consequences revise that theory, and the revision affects
later work. Claim-level addressability makes the theory inspectable, citable,
perturbable, and selectively revisable.

The program couples a live testbed with a prospective controlled one.
**Commonplace** is the live human-agent testbed: agents use the knowledge base to
revise both the repository and the theory that guides its operation, while the
operator still supplies much global-fit judgment and final authorization. It
exposes the human-inclusive learning loop and whether recurring judgments can
become reusable machinery. The **programming-agent testbed** will give agents
persistent fallible theory about a software project and a sequence of
modifications whose later demands can expose earlier mistakes. Matched runs will
vary that theory while holding the rest of the system fixed, testing whether it
changes search, recovery, and coherent modification.

## Computationally closed factory learning produces successor factories

A Greenfield-style [software
factory](../notes/definitions/software-factory.md) is configured,
family-specific machinery for producing and sustaining software through its
lifecycle work products. Its schema, assets, tools, methods, and runtime support
encode production knowledge for a declared product family. The term is narrower
than a generic coding agent or harness, and the detailed [historical ontology
belongs in the supporting
note](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md).

For a fixed factory, product development changes one family member; [factory
development](../notes/definitions/factory-development.md) changes reusable
machinery that will govern later members. These roles are producer-relative. A
meta-factory may produce another factory as one of its members, making the same
work product development relative to the first factory and factory development
relative to the second.

Such factory-valued production is prior art. The further step is
evidence-responsive operative succession: experience from production must
computationally determine a reusable change, and the retained result must enter
the authority path for later work. When that learning path is [computationally
closed](../notes/definitions/computationally-closed-software-factory-learning-loop.md),
an actual change produces an operative [successor
factory](../notes/definitions/successor-factory.md). This is a consequence of
closed factory learning, not an independent requirement that a factory reproduce
itself.

Requirements, existing artifacts, user answers, corrections, bug reports,
tests, telemetry, permissions, and acceptance responses may remain external
evidence through declared interfaces. The path remains computationally open
when a person supplies a factory-development decision assigned to it, such as
the required family schema, a task-specific evaluator, a promotion choice, or
ad hoc recovery.

Closure is separate from breadth. A closed updater may remain confined to one
family. [Domain extensibility](../notes/definitions/domain-extensible-software-factory.md)
asks whether computation can acquire and install the family-specific machinery
needed by sufficiently novel covered demands while fixed general learning
machinery remains. The [unqualified universal-software-factory
label](../notes/domain-extensibility-not-closure-determines-factory-reach.md) is
too ambiguous: constructional universality can collapse into ordinary compiler
expressivity, while unrestricted task universality would demand distinctions
that the permitted evidence may not reveal.

## Holding a theory means controlling a fallible search

Naur's test is longitudinal. A coherent modification meets a new demand without
destroying the purpose and organization that make the program work. Because
those are only partly stated, a later demand may expose damage caused by an
earlier locally successful change.

The unit judged is therefore a sequence, not one patch. A failed first candidate
can belong to coherent modification when the process recognizes the failure and
recovers. A successful first candidate can fail the test when it passes narrow
checks but damages the wider organization in a way the process cannot detect.
[Holding a program theory means sustaining coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

Program-relevant understanding may extend beyond the retained theory surface.
The proposed experiment varies one such surface while holding specified
background components fixed. It therefore tests the causal contribution of that
surface, not whether it exhausts the system's whole program theory, [as the
retained-theory intervention note makes
explicit](../notes/a-retained-theory-intervention-isolates-one-explicit-theory-surface.md).

Theory matters before a correct answer is available. [Open-ended improvement
must allocate search before decisive evaluation
exists](../notes/open-ended-improvement-allocates-search-before-evaluation.md).
Retained theory can focus search and guide recovery by exposing commitments a
local fix must preserve.

Generic search can also generate and test patches. The distinction is causal:
withholding or replacing retained theory should change the search or subsequent
revision. One possible mechanism is that [natural-language project state
specializes search heuristics already present in model
weights](../notes/natural-language-project-state-specializes-search-heuristics.md).
A theory that merely accompanies the work remains documentation.

Theory-guided choices need not all meet the standard for final adoption.
[Lightweight search controls](../notes/lightweight-search-control-does-not-license-adoption.md)
can allocate work under weaker evidence, while [backtracking keeps them
provisional](../notes/backtracking-keeps-lightweight-search-control-provisional.md)
when contrary evidence arrives.

## Four roles in the current research design

To make the mechanism testable, the current design separates four functional
roles by how they can fail and be perturbed.

| Functional role | Current realization | Typical failure |
|---|---|---|
| Retained project state | Addressable theory and other persistent project artifacts | Omission, contradiction, drift, or retrieval failure |
| Model-mediated semantic operation | Model weights applied to call-specific context | Theory ignored, misapplied, or rationalized after the fact |
| Independently executed symbolic operation | Code and runtime carrying exact transitions and continuity | Exact execution of the wrong transition or a path that ends too early |
| Independent exposure and read-back | Independent checks and later consequences; the operator supplies much global-fit judgment and authorization | Weak or captured evaluation, delayed credit assignment, or exogenous selection |

These are roles, not permanent carriers. A future substrate may combine them;
the current separation permits targeted interventions on theory, interpretation,
evaluation, and continuity.

The same code may be read into a prompt as evidence and later executed by a
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

The evidence ladder distinguishes four levels:

1. **Mediation:** changing or withholding theory changes a consequential
   decision or intervention.
2. **Empirical contact:** the intervention produces an outcome that bears on the
   theory.
3. **Theory learning:** the outcome changes the retained theory's content, scope,
   or operational force.
4. **Recurrence:** the updated theory changes a later operation on the same
   behavior-determining path.

A [citation at the decision point is a mediation
trace](../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md),
not proof that the theory was load-bearing; withholding, replacement, or
perturbation is stronger evidence. The higher levels must also belong to the
same full causal path. Separate witnesses for theory use, outcome, revision, and
later work do not compose automatically into evidence of theory-mediated
learning, [because disconnected witnesses do not establish a full causal path
through
theory](../notes/disconnected-witnesses-do-not-establish-a-full-causal-path-through-theory.md).

### Warrant and theory fit are different evaluations

A well-warranted claim can still fit a working theory poorly. Conversely, a weak
claim can appear to fit because the current implementation already assumes it.
[A claim's warrant therefore does not determine its fit in a working
theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md).

No present automatic evaluator fully decides global fit. Consequences of live
use and comparisons with rival theories provide an [initial selection
environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md),
but not an independent warrant oracle: [system use provides evidence of theory
fit and causal usefulness, not independent
warrant](../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).

## Current evidence and next tests

The [2026-08-30 Commonplace revision
record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
illustrates part of the proposed path: retained theory guided the work, operator
feedback revised it, and the result affected later work. The episode was not
recorded prospectively enough for causal or comparative attribution.

Future consequential episodes should preserve the joins of the causal path
above, including which theory state guided a decision and which revision later
work consumed. For nondeterministic production, missing joins cannot reliably be
reconstructed after the fact.

The minimum controlled test compares usable theory with theory withheld or
deliberately wrong while holding the model, executable machinery, task sequence,
and budget fixed. Later demands must be able to expose earlier mistakes. The
questions are whether theory changes search and recovery, whether consequences
revise the same theory state, and whether that revision changes later work. Any
result identifies only [the contrast it actually
runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).

A longitudinal Commonplace study should ask whether recurring operator judgments
become reusable machinery and whether named functions move toward computational
supply.

## The bootstrap must outgrow supplied specialization

The Bitter Lesson puts pressure on the program because its present theory and
improvement machinery emerge from a human-guided loop. Agents write much of the
material, but operators still supply decisive high-level direction and
selection. The issue is not who types the artifacts. It is whether computation
can increasingly determine and operatively retain the task- or family-specific
machinery needed as the demand class widens.

[Production method and representational form are different
axes](../notes/the-bitter-lesson-selects-production-methods-not-representational.md):
learning can produce explicit artifacts as well as weights. Fixed general
models, learning methods, runtimes, interfaces, resource controls, and trusted
kernels may remain. The scaling burden falls on human-supplied specialization
that must be recreated for each new task or family, not on every handcrafted
component merely because it is fixed.

The present loop is human-inclusive and computationally open over decisive
high-level selection. Models search and revise project state, while symbolic
machinery executes and retains changes, but operators remain decisive where
reusable evaluators are weak. Recurring judgments are candidates for reusable
machinery.

The bootstrap has two related jobs. First, move named decision-bearing functions
from human toward joint or computational supply while holding the
human-inclusive boundary fixed. Over a declared task scope and horizon, the
technical endpoint is reached when the same improvement path still completes
after the human participants are removed. Quality and warrant require separate
evidence. [The decisions that stay human, and what would move
them](./the-decisions-that-stay-human-and-what-would-move-them.md) develops the
full fixed-boundary and warrant argument.

Second, widen production reach by computationally acquiring the specialization
that novel covered demands require. Task-specific theories, schemas,
decompositions, methods, and evaluators must not remain a new human construction
project for every family the system claims to cover. This does not put every
current component inside one universal revision surface. [Machinery persists by
warrant, not by
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md),
while the bootstrap [fits the Bitter Lesson only if learning outgrows its
supplied specialization](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

Three immediate payoffs motivate this strategy. First, explicit theory may
improve [sample efficiency under structured
shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
Second, it leaves an inspectable learning record. Third, because the system being
improved is itself agentic, theories of agentic systems can become operative
self-theory. Commonplace therefore builds
[agentic-systems theory](../agentic-systems/README.md) both as an external
research topic and as candidate self-theory for the system that runs the research
and for future programming agents. The program tests whether improving that
theory improves the system's ability to understand and modify its own
organization. Each payoff must survive comparison at total system cost.

The strategy must compete with more direct learning and search methods. It
should be narrowed or abandoned if retained theory is causally inert, the
evaluation loop becomes self-confirming, each novel covered family still needs
human-built task-specific decomposition or evaluation machinery, required
in-scope decisions remain human, or another method wins at comparable total
cost.

The companion article [The Bitter Lesson does not require everything to live in
weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops the scaling argument and competing alternatives.
