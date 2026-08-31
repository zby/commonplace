---
description: "Definition — factory development constructs or revises reusable family-level production machinery rather than one product's lifecycle state"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Factory development

**Factory development** is the process that constructs or revises the reusable, family-level production machinery of a [software factory](./software-factory.md). Its targets can include the declared product-family scope, commonality and variability, the factory schema and viewpoints, processes or guidance, packaged assets, tools, frameworks, generators, and development or runtime support.

Greenfield's mature account distinguishes factory development from **solution development**. Factory developers build and revise production assets for solution developers; solution developers use those assets to create and sustain particular family members. The earlier 2003 account makes the analogous distinction between product-line developers and product developers.

The boundary is the target and reuse scope of the work. Changing one product's requirements, design, code, tests, deployment state, or other lifecycle work products is solution development relative to the producing factory. A discovery made during that work becomes factory development only when it changes reusable family-level machinery intended to govern later family members or later work on the family.

## Scope

Factory development includes initial definition of the family and its production knowledge, construction and packaging of the schema and reusable assets, and later revision of that machinery. Greenfield's 2007 account names two important family-level operations:

- **factory specialization** adds, removes, or changes viewpoints and their associated artifacts, activities, and assets; and
- **factory composition** combines production structures from multiple factories.

Feedback from solution development can motivate factory revision. A defect report, feature request, or unanticipated variation is evidence for factory development, not the revision itself. In Greenfield's account, human factory developers interpret that evidence and decide how the reusable machinery changes.

This definition does not fix the future actor allocation. A later theory may assign some factory-development work to computational actors. That is an extension of the inherited ontology and must be stated separately rather than read back into Greenfield's definition.

## Exclusions

- Selecting or binding an anticipated product variant within the supplied family machinery is solution configuration, not factory development.
- Generating or assembling a family member is product work even when it is fully automated.
- Editing a copied asset only for one product is not factory development unless the change enters the reusable family machinery.
- A report, observation, candidate schema, or proposed tool is an input to factory development until it is incorporated into the reusable production arrangement.
- Factory development does not by itself imply learning, improvement, reflection, self-production, computational closure, or autonomy.

---

Relevant Notes:

- [Software factory](./software-factory.md) — defined-in: names the family-specific development and runtime environment whose reusable machinery is constructed or revised
- [A software factory is family-scoped lifecycle production machinery](../a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — grounds: supplies the historical two-process distinction and the specialization and composition operations
- [A software factory can produce another factory without learning its specialization](../a-software-factory-can-produce-another-factory-without-learning-its-specialization.md) — contrasts: shows that automated factory construction can still consume human-supplied family specialization
