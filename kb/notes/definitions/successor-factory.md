---
description: "Definition — a successor factory is the operative result of a retained factory-development transition that governs later production in a declared scope"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Successor factory

A **successor factory** is the operative [software factory](./software-factory.md) that results from a retained [factory-development](./factory-development.md) transition and governs subsequent production within a declared routing scope and horizon.

*Successor factory* is introduced here; it is not recovered Greenfield terminology.

The term names a relation, not a new implementation kind. Given an incumbent (F_t), a changed factory (F_{t+1}) is its successor only when the change enters a live production path and later work depends on it. The successor may replace the incumbent, serve only selected product families or tasks, coexist behind a router, or later be rolled back. The claim must state which later production it governs.

## Scope

A transition may update any reusable part of the factory's production machinery: schema, family scope, variability model, assets, tools, methods, representations, evaluators, workflows, runtime support, or their authority relations. It may be a direct update or the selected result of a candidate-evaluation process. The definition does not require a particular update architecture.

**Retained** does not mean permanent. It requires persistence over the relevant horizon and an authority path through which the changed machinery actually affects later production, as specified by [operative change](./operative-change.md). A factory version that is installed, used, and then reverted was a successor during its operative interval.

The successor need not be better. *Improved successor factory* adds an outcome claim relative to a declared objective. *Computationally produced successor factory* adds an actor-allocation claim about the transition. Neither follows from succession alone.

## Exclusions

- A proposed, generated, evaluated, approved, or stored factory candidate is not a successor until it becomes operative.
- A changed family member, patch, model, answer, or other product work product is not a successor factory merely because it was produced. A factory-valued member becomes a successor only when its predecessor, routing scope, operative authority, and later governed work are declared.
- Feedback, telemetry, or a lesson that never reaches a production authority path does not produce a successor.
- A release number or redeployment with no behavior-determining factory change is not a successor transition in this technical sense.

## Misuse Cases

- Calling the highest-scoring candidate the successor before installation and later dependence are established.
- Calling every later factory a successor without naming its predecessor and routing scope.
- Using *successor* as a synonym for *improved*, thereby hiding whether evidence actually supports the improvement claim.

---

Relevant Notes:

- [Factory development](./factory-development.md) — defined-in: names the transition that constructs or changes the reusable production machinery
- [Operative change](./operative-change.md) — grounds: requires persistence and an authority path into later behavior
- [Behavioral authority](./behavioral-authority.md) — extends: supplies the consumer, channel, and force by which the successor governs subsequent production
- [A repeatable operative path keeps a redesign class open to revision](../a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) — extends: adds the stronger condition that another transition remains available after succession
