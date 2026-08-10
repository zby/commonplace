---
description: "Addressable retention localizes a sparse change when units match its decomposition; total adaptation stays local only when the affected units also have a small, explicit impact closure"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, deploy-time-learning]
---

# Localized retention pays when sparse changes have bounded impact in a matching decomposition

[Reflection buys addressability](./reflection-buys-addressability.md) — retained commitments that can be inspected, criticized, and revised one at a time — but presents its advantages as expectations without specifying when they materialize. The condition is relational: suppose a system holds *n* operative commitments and an environmental change affects *k* of them, where *k* is much smaller than *n*. A representation whose units correspond to those commitments lets the system express, inspect, and roll back the change by editing the *k* affected units. Total adaptation stays local only when those units also have a small dependency closure — the units that depend on them and must therefore be checked. Localized retention pays most when both the edit footprint and its behavioral impact remain sparse in a decomposition fixed before the change arrives.

## Three requirements, often conflated

Three properties do different work. **Matching** — units aligned with the decomposition in which change is sparse — concentrates the edit in a few places. **Explicit dependencies** — knowing what cites, loads, or tests each unit — makes the impact closure computable. **Bounded impact** — few downstream commitments or behavior surfaces depend on the changed units — keeps validation local. Matching without explicit dependencies gives a cheap edit but leaves the validation scope unknown; explicit dependencies without bounded impact reveal that validation spans the system; bounded impact without matching still leaves the change scattered across many edits. [The readable-artifact loop's bounded validation radius](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) requires all three: a sparse edit, an explicit impact graph, and a small closure within it.

## An inherited criterion, not a new conjecture

The matching condition generalizes David Parnas's information-hiding criterion from his 1972 paper on code modules to retained commitments. "Decompose according to the decisions likely to change" was precisely an instruction to match unit boundaries to anticipated change topology. The [KWIC demonstration](../sources/parnas-1972-criteria-decomposing-systems-modules.md) showed two working decompositions of one program distinguished not by observable execution behavior, but by their response to change. The inherited result is that boundaries hiding volatile decisions localize the required modifications. The further claim that regression assurance also stays local needs the additional bounded-impact condition; Parnas's case does not supply it automatically. This extension recasts the units as prose rules, schemas, tests, and adapters in a learning system, while the revising actor may be a loop rather than a maintainer. Parnas's criterion also requires predicting what will change, a conjecture that earns its scope only in retrospect — the same retrospective-identification problem the [bitter-lesson analysis](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) leaves open.

## The claim is substrate-neutral, and it cuts both ways

Nothing here says prose beats weights. Model editing, adapters, mixture-of-experts routing, and memory layers all attempt to recover localization inside learned substrates; any method that produces scoped, checkable edits qualifies on this note's terms. The reverse case is equally real: when change is dense and diffuse — a broad distributional drift that moves everything a little — no semantic decomposition is sparse, so localized per-unit revision loses this particular advantage. That negative result does not by itself select gradient descent or any other medium. Heterogeneous change classes can favor multiple forms only when their local advantages outweigh the costs of translation, routing, consistency, and coordination between them.

One authoring rule follows: content on different change schedules should remain independently editable and checkable. When an artifact couples them, its fast-changing part forces revisits while its slow-changing part loses credibility. Units should be carved so that what changes together lives together, without mistaking physical co-location for coupling when sections or fields remain independently addressable.

## Scope

- The condition is about *revision* cost, not retrieval or competence: a perfectly matched decomposition still rides the best-effort retrieval wire, and [a retrieval miss is a local reflective-path failure](./a-retrieval-miss-is-a-local-reflective-path-failure.md) regardless of topology.
- *k* and *n* form a schema, not a measurement; real edit and impact footprints are fuzzy. A decomposition chosen after the fact can manufacture apparent sparsity, so the claim has content only when the units were fixed before the change arrived. Whether designers can estimate change topology well enough to choose matching units in advance remains the open half of Parnas's criterion.

---

Relevant Notes:

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](./use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — contrasts: the same boundaries-versus-forces question asked across contexts rather than across time, sharing the Parnas case
