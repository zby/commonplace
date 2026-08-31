---
description: "Definition — software-production tasks are longitudinal obligations whose product state, evidence, interaction, acceptance, and coverage extend beyond an initial specification"
type: kb/types/definition.md
tags: [foundations, computational-model]
---

# Software-production task and process

A **software-production task** is a declared obligation to create, change, deploy, operate, maintain, or migrate software under specified conditions. Its identity includes:

- a task-selection and coverage rule;
- the initial product state, including an existing repository and other lifecycle work products;
- an objective and acceptance conditions;
- permitted evidence sources and user or environment interactions;
- a horizon and resource limits; and
- the outcomes that count, including failure, timeout, or abstention where applicable.

A **software-production process** is the temporally extended sequence of activities and product-state transitions by which an operative [software factory](./software-factory.md) handles such tasks. It may create or modify requirements, designs, models, code, tests, deployment descriptions, operational state, maintenance records, and other work products before, during, and after an executable release.

Greenfield supplies the inherited lifecycle activities and work-product ontology. The declared task, evidence, interaction, acceptance, horizon, and coverage frame above is a research-program extension used to make longitudinal learning and closure claims assessable; it is not Greenfield terminology.

## Scope

The initial request is an input to the task, not necessarily its exhaustive specification. Requirements, constraints, an existing codebase, user answers, corrections, bug reports, test results, telemetry, dependency changes, permissions, and acceptance responses may arrive during the process when the declared interaction protocol admits them. A program-synthesis survey likewise reports that users often discover the scope of their intent through interaction and that additional communication is needed to distinguish programs consistent with the same examples ([Gulwani, Polozov, and Singh](../../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md)).

The task declaration fixes how later evidence is interpreted for an assessment. A permitted change of requirements can update the task state; an undeclared change to the objective, acceptance rule, coverage, or allowed interaction produces a different assessment frame. Declaring the frame does not require knowing every future observation or product decision in advance.

One event can serve two causal roles. A failed test can guide repair of the current product and also provide evidence for changing reusable factory machinery. The first role belongs to the software-production process. The second belongs to [factory development](./factory-development.md) only if it changes production machinery for later work.

## Exclusions

- The initial prompt, requirements document, or formal specification is not the whole task unless the declaration explicitly makes it exhaustive.
- The executable program is not the whole product state when other lifecycle work products remain relevant to acceptance or later operation.
- A single model invocation or `specification -> program` mapping is not the whole process when interaction, correction, deployment, maintenance, or changing evidence remains in scope.
- Factory learning is not implied by product correction. It requires an operative change to the factory's own production machinery.

## Misuse Cases

- Claiming success by evaluating only tasks the system chose to finish while silently dropping failures, timeouts, or requests for human rescue.
- Calling a human-supplied design decision ordinary task evidence when the assessed process was meant to determine that decision.
- Treating every later user message as a new task, or treating every objective change as harmless feedback, without applying the declared interaction and task-identity rules.

---

Relevant Notes:

- [Software factory](./software-factory.md) — defined-in: names the lifecycle production machinery that enacts the process
- [Factory development](./factory-development.md) — contrasts: changes reusable production machinery rather than only the selected product state
- [Methodological and computational closure track different changes](../methodological-and-computational-closure-track-different-changes.md) — extends: supplies the declared-crossing and coverage conditions needed to assess closure over these tasks
- [Program theory sustains search under delayed feedback](../program-theory-sustains-search-under-delayed-feedback.md) — extends: explains why later consequences can remain evidence about earlier software decisions
