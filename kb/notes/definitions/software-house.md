---
description: "Definition — a software house is the complete persistent system responsible for developing and evolving software for external users"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Software house

A **software house** is the complete persistent system responsible for developing and evolving software for external users. It operates in response to their requirements, feedback, and the consequences that arise when the software meets its operating environment. It is not necessarily a company, tool, or particular production method.

The software house includes the software whose evolution it remains responsible for, any production knowledge and machinery it uses, and every person or computational component that fills an internal production role. This functional boundary generalizes ordinary usage, in which a software house is an organization of people and tools. It lets the same term cover human, hybrid, and automated producers without making one role allocation part of the base definition.

## Scope

Users remain outside the software house when they supply requirements, domain knowledge, preferences, feedback, acceptance judgments, or later demands. A person is inside the software house only when the system depends on them for an internal production role, such as interpreting production knowledge, making implementation decisions, or repairing production machinery.

The same person can occupy both positions in different interactions. The boundary follows the role being performed, not the person's identity or legal relationship to an organization.

Product scope and operating horizon are parameters of a software house. Persistence means continuity of responsibility for software evolution across demands and operating consequences. It does not mean indefinite life, immutable membership, or retention of every state change.

Persistence alone establishes neither retention nor learning. It identifies continuity of responsibility, not a causal dependence of later production on a change made from experience. A theoretical software house whose fixed production knowledge and machinery suffice for every admitted demand still meets this definition. Responding to a demand may change the software without changing the house's capacity or production method. Claims that the house retained experience, learned, or revised its production machinery must be derived and tested separately.

An **automated software house** is a software house in which no human is required for an internal production role over its declared product scope and operating horizon. User participation is compatible with automation; dependence on a human for an internal production role is not.

## Exclusions

A company is not the only possible software house, and its legal or organizational boundary need not equal the software house's system boundary. Conversely, a tool, model, agent harness, workflow, or production method is not the whole software house merely because the house uses it.

A [software factory](./software-factory.md), in Greenfield's sense, is family-specific production machinery that a software house may use. It is neither the software house nor a required component of one. Human developers required to operate or revise that machinery are inside the surrounding software house while filling those production roles, even though they are not part of the factory machinery itself. This definition does not import Greenfield's product-family, schema, template, or developer-role ontology.

## Misuse Cases

- Calling an IDE, LLM, agent harness, or generator a software house when it is only one component of the producing system.
- Counting a user as part of the software house merely because their requirements or feedback affect the software.
- Calling a software house automated when a human still performs an internal production role within the declared scope and horizon.
- Treating persistence as indefinite existence rather than continued responsibility across software changes.
- Treating persistence as evidence that the house retained experience or learned from it.

---

Relevant Notes:

- [Software factory](./software-factory.md) — contrasts: names Greenfield's narrower, family-specific production machinery rather than the complete persistent producer
