---
description: "Curated head for the goal-prioritization tag — which of the goals, requirements, quality criteria and candidate improvements that could govern a task gets effort, on whose authority and what evidence, and when work stops"
type: types/tag-readme.md
---

# Goal prioritization

Recognizing a concern differs from deciding that it should govern this
case. Several things could govern what is done next — requirements, quality
criteria, candidate improvements, further search — and the question here is
which of them gets effort, how much, on whose authority, on what evidence,
and when the work stops. Assign this tag to an artifact that treats that
decision substantively: precedence among goals, trade-offs and hard
boundaries, stated non-requirements, effort allocation among candidates
before decisive evidence exists, and stopping or deferral. Misordering is
one case: an invented requirement, a silently relaxed goal or a low-value
tangent qualifies when the artifact analyses it as a precedence failure.
The test is subtractive: the artifact qualifies if removing its treatment
of that decision would remove its main claim; if the claim stands without
it, the goal was background. Mentioning a goal, reporting a poor result or
measuring accuracy is insufficient.

No single note yet defines the area; the sources supply hypotheses and
boundary cases, and none establishes prevalence. Name the object of
allocation ("effort allocation", "search allocation"), as the
[vocabulary collision ledger](../reference/vocabulary-collision-ledger.md)
requires. Boundaries with neighbouring tags are under Related Tags; search
control carries both this tag and improvement-loop.

## Allocating effort under uncertainty

- [Open-ended improvement must allocate search before decisive evaluation is available](../theory/open-ended-improvement-allocates-search-before-evaluation.md) — choosing which questions, candidates or proof paths to develop before decisive evidence exists
- [Lightweight search control does not license adoption](../theory/lightweight-search-control-does-not-license-adoption.md) — a search judgment's authority stops at allocating investigation, continuation or abandonment
- [A search controller is tested by what it brings to stronger evaluation](../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — judged by what it routes forward under matched-resource or net-value comparison
- [An optimal long-run learning strategy invests in its own machinery](../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) — when a one-time machinery improvement outranks immediate learning
- [Choosing what to learn requires both validity and learning-value gates](../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — trustworthy enough to learn from is a different question from worth learning now
- [Productive deferral requires option evidence and convergence](../theory/productive-deferral-requires-option-evidence-and-convergence.md) — controlled postponement against hidden commitment and indecision

## Objectives, requirements and who sets them

- [Unattended work needs the functions that interaction supplied](../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) — interactive work can hide who resolved purpose, redirected effort and decided when to stop
- [Revising an improvement objective is licensed from outside it](../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — objective change counts as improvement only against a level outside both objectives
- [A proximate target is checked for achievement, not for warrant](../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) — no check in the loop evaluates the claim that the pursued target serves the objective
- [Intent controls choices by distinguishing live alternatives](../theory/intent-controls-choices-by-distinguishing-live-alternatives.md) — a stated intent governs only when it changes what is admissible, preferred, worth further search or sufficient to stop
- [What requirements don't you have?](../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md) — unrequested guards show why legitimate concerns still need task-specific tolerances and scope
- [Nostalgebraist on persistent coding-agent mistakes and benchmark gaps](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md) — reported tangents and repeated steering make the operator's prioritization visible

## Priority failures

- [LLM generation can hide a relaxed goal where human writing exposes a stall](../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) — conjectural account of a necessary constraint losing force while fluent completion remains
- [A guard against a conjectured requirement removes the experiment that would test it](../theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md) — why test-selected agents add guards by default, and when omitting one is the cheaper experiment
- [Context isolation for focus conflicts with global prioritization](../theory/context-isolation-for-focus-conflicts-with-global-prioritization.md) — isolating an agent for task focus removes the live comparison set relational prioritization requires, flattening urgency and tangents unless execution is split from wide-shallow triage
- [Human Routers of Machine Words](../sources/borretti-human-routers-of-machine-words.ingest.md) — asks whether a complete-looking text has displaced the work of resolving its constraints

Sources are linked by hand because generated membership omits them.

## Related Tags

- [Improvement-loop](./improvement-loop-README.md) — neighbour: how a change becomes a candidate, is selected and retained; here, how effort is distributed among goals and candidates, including work that changes nothing
- [Learning-theory](./learning-theory-README.md) — neighbour: what learning is and how knowledge grows; here, what to spend on it
- [Warranted-autonomy](./warranted-autonomy-README.md) — neighbour: who is authorized to decide; here, how the decision is made
- [Self-improving-systems](./self-improving-systems-README.md) — neighbour: the system changing itself; here, a decision every task makes
- [LLM reliability](./llm-reliability-README.md) — neighbour: deviations from intent and their correction; here, which consideration governs a choice
- [Constraining](./constraining-README.md) — neighbour: which interpretations remain admissible, rather than which admissible outcome deserves priority
- [Evaluation](./evaluation-README.md) — neighbour: what checks can establish; an adequate check still needs the right task criteria
- [Prose readability](./prose-readability-README.md) — neighbour: ease of following a passage; readable prose can still serve the wrong goal
