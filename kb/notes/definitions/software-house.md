---
description: "Definition — a software house is the complete persistent system that develops and evolves software through ongoing interaction with users"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Software house

A **software house** is a persistent system that develops and evolves software in response to requirements, feedback, and consequences arising from its users and operating environment. It is the whole producing system, not necessarily a company, tool, or production method. Its internal roles may be filled by people, computational machinery, or both.

This definition generalizes ordinary usage, in which a software house is an organization of people and tools. Here the term names the underlying software-production system independently of how its roles are implemented. This lets the same term cover human, hybrid, and automated producers without treating automation as a different kind of system.

## Scope

Users remain outside the software house when they supply requirements, domain knowledge, preferences, feedback, acceptance judgments, or later demands. A person is inside the software house only when the system depends on them for an internal production role, such as interpreting production knowledge, making implementation decisions, or repairing production machinery.

Product scope and operating horizon are parameters of a software house. Persistence means responsibility for software evolution across demands and operating consequences, not indefinite life.

An **automated software house** is a software house in which no human is required for an internal production role over its declared product scope and operating horizon. User participation is compatible with automation; dependence on a human for an internal production role is not.

## Exclusions

A company is not the only possible software house, and its legal or organizational boundary need not equal the software house's system boundary. Conversely, a tool, model, agent harness, workflow, or production method is not the whole software house merely because the house uses it.

Automation, learning, and revision of the house's own production machinery are not part of the base definition. They are additional properties that a software house may or may not have.

A [software factory](./software-factory.md), in Greenfield's sense, is family-specific production machinery that a software house may use. It is neither the software house nor a required component of one. This definition does not import Greenfield's product-family, schema, template, or developer-role ontology.

## Misuse Cases

- Calling an IDE, LLM, agent harness, or generator a software house when it is only one component of the producing system.
- Counting a user as part of the software house merely because their requirements or feedback affect the software.
- Calling a software house automated when a human still performs an internal production role within the declared scope and horizon.
- Treating persistence as indefinite existence rather than continued responsibility across software changes.

---

Relevant Notes:

- [Software factory](./software-factory.md) — contrasts: names Greenfield's narrower, family-specific production machinery rather than the complete persistent producer
