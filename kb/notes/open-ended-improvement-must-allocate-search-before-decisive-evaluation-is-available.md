---
description: "Open-ended improvement must choose which questions, candidates, experiments, or proof paths to develop before decisive evidence about them is available; even a Gödel machine's proof gate retains this prior search problem"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, computational-model, self-improving-systems]
---

# Open-ended improvement must allocate search before decisive evaluation is available

A decisive evaluator can govern only a branch that is concrete enough to
assess. Open-ended improvement starts before that point. It must decide which
anomaly to investigate, candidate to formulate, experiment to run, or proof path
to pursue while the evidence that could decisively judge those branches is not
yet available.

Here, **decisive evaluation** means evidence strong enough to license adoption
under the declared criterion. It need not establish absolute truth. The claim is
that even this criterion-relative evidence often becomes available only after
search has selected and developed a branch.

This is not merely an economic constraint. Evaluation may be expensive, but it
may also be impossible before a candidate has been formulated, depend on an
intervention that has not been performed, arrive only through later demands, or
require a proof that the current formal system cannot derive. More resources do
not remove the need to choose a direction that makes the candidate and its
evaluation problem available.

## Search precedes its strongest evidence

In a
[proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md),
search brings a possible change into consideration and evaluation determines
whether it may be accepted. The functions are distinct because an evaluator
cannot accept or reject a candidate that search never reaches.

Open-ended improvement makes the separation consequential. Its branch set is
not a finished list supplied in advance. Search can discover new questions,
representations, methods, experiments, and evaluators while it proceeds. The
process therefore needs some prior allocation of attention and computation
across branches before it has the strongest evidence about their value.

A perfect acceptance rule over every candidate presented to it would not by
itself make the overall process effective. The process could still fail to
formulate a useful candidate, pursue the wrong proof direction, or never build
the observation that would expose a better branch. Acceptance quality bounds
what survives after search; search allocation bounds what gets the opportunity
to survive.

## The Gödel machine retains the prior search problem

The Gödel machine is the proof-governed limit case. A self-rewrite may execute
only after the machine proves that switching now has higher expected utility
than continuing its current search, relative to its axioms and utility
function. The proof gate therefore supplies decisive acceptance within the
formalization.

The gate still acts only after proof search reaches a proof technique that
produces a candidate rewrite and proves the target theorem. The initial proof
searcher must allocate computation across proof techniques according to a
supplied bias. The machine's global-optimality result is relative to whichever
initial proof searcher was chosen, and beneficial rewrites outside what the
formal system can prove remain unreachable. See
[Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md).

The machine may later rewrite its proof searcher, but it must find and justify
that rewrite through the searcher it already has. Self-revision moves search
allocation inside the revisable system; it does not eliminate the bootstrap
allocation. Even the strongest acceptance regime in this comparison therefore
retains a prior question: which proof directions receive enough search to reach
the gate?

## What follows

Open-ended improvement needs a search-allocation process whose decisions precede
decisive evaluation of the selected branches. The evidence available to that
process can be weaker than the evidence required for final adoption without
becoming irrelevant: it controls which branches receive further work, not which
changes are finally warranted.

This does not establish which search-allocation method works. It also does not
show that every candidate must be evaluated separately. A proof, abstraction,
or experiment may dispose of a whole class of candidates at once. Choosing to
construct that proof, abstraction, or experiment is itself part of the prior
search problem.

## Scope

- The claim concerns open-ended improvement, where consequential branches are
  generated or elaborated during the process. In a finite task with a supplied
  candidate list and cheap exhaustive evaluation, search allocation may be
  trivial.
- "Before" names a causal dependency, not a rigid execution order. Evaluation
  of earlier branches can guide later search, but it cannot retroactively choose
  which first branch made that evidence available.
- Decisive evaluation remains relative to a criterion and formalization. A
  proof can be decisive within wrong axioms, and an empirical gate can be
  decisive for a weak proxy.
- The note does not identify a successful search-control mechanism or show that
  any current agent allocates open-ended search well.

## Open Questions

- How can a search-allocation policy be evaluated without requiring the
  exhaustive counterfactual search that the policy exists to avoid?
- What evidence should revise the search-allocation process itself rather than
  only the candidate it happened to reach?

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: separates candidate production from reject-capable acceptance and states that evaluation cannot select an unreached candidate
- [Gödel machines are a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md) — exemplifies: the proof-gated limit case still begins from a supplied proof-search bias and excludes beneficial but unprovable rewrites
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — contrasts: verification bounds what can be accepted with warrant, while this note isolates the prior bound on what reaches evaluation
- [Holding a program theory means sustaining coherent search under delayed feedback](./holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md) — extends: develops one candidate account of how open-ended program search can remain coherent before delayed evidence arrives
