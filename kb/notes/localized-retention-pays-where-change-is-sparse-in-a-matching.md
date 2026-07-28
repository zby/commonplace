---
description: "Addressable retention pays off conditionally on change topology: where a change touches few retained commitments and the units match that decomposition, adaptation scales with the change rather than the system — Parnas's criterion generalized; dense change favors parametric media"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Localized retention pays where change is sparse in a matching decomposition

[Reflection buys addressability](./reflection-buys-addressability.md) — retained commitments that can be inspected, criticized, and revised one at a time — but lists its advantages as expectations without saying when they deliver. The condition is a property of the *change*, not of the representation: suppose a system holds n operative commitments and an environmental change affects k of them, with k much smaller than n. A representation whose units correspond to those commitments lets the system edit the k affected units and validate their dependency closure; adaptation cost scales with the change. An undifferentiated update must first recover *where* the change belongs and then establish behaviorally what else moved; its cost scales with the system. Localized retention pays exactly where change is sparse in a decomposition the retained units match — and buys little where it is not.

## Two requirements, often conflated

Matching and explicitness do different work, and the payoff needs both. **Matching** — units aligned with the decomposition in which change is sparse — puts the edit in few places. **Explicit dependencies** — knowing what cites, loads, or tests each unit — makes the validation closure computable. Matching without explicit dependencies gives a cheap edit with an unbounded check; explicit dependencies without matching give a bounded check over many edits. [The readable-artifact loop's bounded validation radius](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) is the conjunction: its factoring criterion (deployment-pace updates plus bounded radius) presupposes that the change landed in few, dependency-explicit units, which is this note's condition.

## An inherited criterion, not a new conjecture

The claim is Parnas's information-hiding criterion generalized from code modules to retained commitments. "Decompose according to the decisions likely to change" was precisely an instruction to match unit boundaries to anticipated change topology, and the [KWIC demonstration](../sources/parnas-1972-criteria-decomposing-systems-modules.md) showed two working decompositions of one program distinguished by nothing observable in running them — only under change. What is inherited: the mechanism (change footprint versus unit boundaries decides revision cost). What is local extension: the units here are prose rules, schemas, tests, and adapters in a learning system rather than modules in a program, and the revising actor may be a loop rather than a maintainer. What the purchase does not cover: Parnas's criterion requires *predicting* what will change, and that prediction is a conjecture that earns its scope only in retrospect — the same retrospective-identification problem the [bitter-lesson analysis](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) leaves open.

## The claim is substrate-neutral, and it cuts both ways

Nothing here says prose beats weights. The claim favors whatever representation matches the change topology — model editing, adapters, mixture-of-experts routing, and memory layers are attempts to recover matching localization *inside* learned substrates, and one that achieves it with scoped, checkable edits qualifies on this note's own terms. The reverse case is just as real: when change is dense and diffuse — a broad distributional drift that moves everything a little — no semantic decomposition is sparse, per-unit revision is the wrong shape, and gradient descent is the matched medium, because parameter space is the decomposition in which *that* change class is tractable. Forms win where their unit structure matches the change class they face; a system facing heterogeneous change classes has a structural reason to hold more than one form.

One authoring rule falls out directly: an artifact that bundles content on different change schedules is mismatched by construction — its fast half forces revisits, its slow half decays credibility, and no edit touches just one. Units should be carved so that what changes together lives together.

## Scope

- The condition is about *revision* cost, not retrieval or competence: a perfectly matched decomposition still rides the best-effort retrieval wire, and [retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) regardless of topology.
- k and n are a schema, not a measurement: real changes have fuzzy footprints, and "sparse in some decomposition" can usually be forced by gerrymandering units after the fact. The claim has content only where the decomposition was fixed before the change arrived — matching is a prediction that pays or fails, not a relabeling.
- Whether anticipated change topology can be estimated well enough to *design* matching units, rather than discover the mismatch under change, is the open half of Parnas's criterion and remains open here.

---

Relevant Notes:

- [Reflection buys addressability](./reflection-buys-addressability.md) — mechanism: supplies the condition under which its expected advantages deliver — change sparse in a decomposition the retained units match
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — grounds: its bounded validation radius is the matching-plus-explicit-dependencies conjunction this note separates
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — contrasts: the same boundaries-versus-forces question asked across contexts rather than across time, sharing the Parnas case
- [The bitter lesson selects against unearned reach, not against structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — grounds: why the matching prediction earns scope only in retrospect, like any anticipated-change claim
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — contrasts: the delivery weakness that matching does not touch
- [Parnas (1972), "On the Criteria To Be Used in Decomposing Systems into Modules"](../sources/parnas-1972-criteria-decomposing-systems-modules.md) — abstracted-from: the information-hiding criterion whose change-matching mechanism this generalizes from code modules to retained commitments
