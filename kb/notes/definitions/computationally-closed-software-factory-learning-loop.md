---
description: "Definition — a computationally closed factory-learning loop turns production evidence into an operative successor factory without an in-scope human learning decision"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Computationally closed software-factory learning loop

A **software-factory learning loop** is a pathway in which evidence from software production causally determines an operative change to the factory's own reusable production machinery. The loop is **computationally closed** when every decision and transition required to determine and make that in-scope change operative is supplied by computational actors assigned to the declared pathway, conditional only on the external evidence and interactions that the declaration permits. Hosted models and other external computational services may be declared dependencies; their infrastructure ownership does not turn them into human decisions, and their control boundary must be reported separately.

This is a path-relative specialization of [computational closure](../methodological-and-computational-closure-track-different-changes.md). It does not require the whole surrounding organization, product-development process, or environment to be autonomous. A conventional factory used within a human-inclusive production process may contain a computationally closed factory-learning path while users continue to state demands, answer questions, report failures, and judge products through declared interfaces.

The compound definition is introduced by this research program. Greenfield supplies the family-scoped factory and its human-directed feedback path, not a claim that the factory-learning path is computationally closed.

## Scope

A closure claim must declare:

- the selected [software-production tasks or processes](./software-production-task-and-process.md) and their coverage rule;
- the improvement objective and acceptance conditions for factory change;
- the system boundary and the factory aspects the pathway can change;
- the permitted external evidence sources and interactions;
- the horizon and resource limits; and
- the response to rejection, failure, timeout, abstention, rollback, and recovery.

Initial requirements, an existing repository, user answers, corrections, bug reports, tests, telemetry, permissions, changing constraints, and later acceptance evidence may remain external. Their causal role decides whether they are evidence or intervention. A human opens the claimed loop when they supply a factory-development decision that the pathway is meant to make: for example, an undeclared interpretation, required family schema, task-specific evaluator, candidate factory, promotion choice, installation step, ad hoc recovery, or decision that a failed case no longer counts.

The responsibility boundary is semantic and must be fixed before outcomes are
known. Task or environment evidence describes desired product behavior,
constraints, or observed consequences through a declared interface. A learning
intervention prescribes a factory representation or decomposition, update
decision, candidate choice, promotion, installation, or recovery that the
claimed pathway assigns to computation. A declared human acceptance judgment
may remain an external oracle input; closure is then conditional on that oracle
and does not establish computational acquisition of its evaluator. When one
contribution mixes evidence with a factory-development decision, only the part
not supplied by the person can count as computationally acquired.

The same input can be legitimate under one claim and an intervention under another. A human-written schema can be an allowed input to a closed *factory-compilation* pathway. It cannot simultaneously count as computational acquisition of that schema. The closure declaration must name which transition is being assessed instead of hiding an exported decision under the label *feedback*.

The learning transition may update machinery directly or use explicit candidate search and selection. When a transition does occur, its retained operative result is a [successor factory](./successor-factory.md). An iteration that computationally rejects every candidate or retains the incumbent may still exercise a closed pathway, but it is not an occurrence of factory learning.

## Exclusions

- Closure is not loop completion. Search, evaluation, and retention can complete once while later iterations still require human decisions.
- Closure is not competence, correctness, warrant, improvement, or breadth. A narrow fixed-family loop can be genuinely closed and perform badly.
- Product repair alone is not factory learning. The change must reach reusable factory machinery that governs later production.
- Computational closure does not require every factory component or fixed general learning mechanism to be self-modifiable.
- Organizational closure or autopoietic self-production is a different concept.

## Misuse Cases

- Calling a loop closed because a model generated most of the bytes while a person chose the decisive interpretation, evaluator, or successor.
- Excluding failed tasks or human rescues after observing outcomes so that only unattended successes remain in the coverage set.
- Treating a human-authored task-specific factory as external evidence while claiming that the loop learned the specialization it contains.
- Inferring broad domain coverage from closure on one product family.

---

Relevant Notes:

- [Methodological and computational closure track different changes](../methodological-and-computational-closure-track-different-changes.md) — grounds: supplies the actor-allocation, declared-crossing, and coverage rules specialized here
- [Self-improving system](./self-improving-system.md) — grounds: requires evidence-responsive operative change to the system's own behavior-determining organization rather than only a better output
- [Factory development](./factory-development.md) — defined-in: names the in-scope change to reusable production machinery
- [Successor factory](./successor-factory.md) — defined-in: names the operative retained result when a factory-learning transition occurs
- [Software-production task and process](./software-production-task-and-process.md) — defined-in: names the longitudinal production frame from which permitted evidence may arrive
