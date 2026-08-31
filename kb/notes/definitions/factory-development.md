---
description: "Definition — factory development constructs or changes reusable family-level production machinery, rather than one product's lifecycle state"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Factory development

**Factory development** is the process that constructs or changes the reusable, family-level machinery that determines how software products will subsequently be produced. Its targets may include product-family scope, schemas, viewpoints, variability and configuration knowledge, templates, assets, tools, methods, representations, evaluators, workflows, runtime support, and the authority paths that make them operative.

For a fixed reference factory, the defining boundary is the target and reuse scope of the change. **Product development** changes one family member or its lifecycle work products under supplied production machinery. Factory development changes that machinery for later work. A discovery made while building one product crosses into factory development only when it changes reusable machinery that can govern subsequent production.

The distinction is producer-relative. When meta-factory \(A\) constructs factory \(B\), the same work is product development relative to \(A\) and factory development relative to \(B\). \(B\) is a factory-valued member of \(A\)'s family and reusable production machinery for its own family. It becomes a [successor factory](./successor-factory.md) only through a separately declared operative relation to an incumbent.

Greenfield supplies schemas, viewpoints, templates, assets, processes, specialization, composition, and developer roles. Evaluators, representations, authority paths, operative retention, and the producer-relative rule are explicit extensions used by this research program to state what a computational learning transition changes.

## Scope

Factory development includes initial construction, family-template installation or environment configuration that establishes an operative [software factory](./software-factory.md), and later changes to it. Greenfield names factory specialization and factory composition as family-level operations within this broader process:

- **specialization** adds, removes, or changes the reusable or base factory's viewpoints and their artifacts, activities, and assets;
- **composition** integrates production structures from multiple factories; and
- **feedback-supported, versioned factory revision** changes reusable machinery in response to defects, new demands, practices, or technology. *Factory evolution* is this synthesis's umbrella term for such changes, not a named Greenfield operation on the retained evidence.

Greenfield also uses schema modification to accommodate anticipated variation in one product. Viewpoint change alone therefore does not classify the work: a product-local configured-schema variation remains product development, while a change to reusable base-factory structure is specialization.

The definition does not fix the actor or mechanism. Human factory developers, computational generators supplied with metamodels, or a factory's own learning pathway can all perform factory-development work. Those cases differ in actor allocation and in where the family-specific knowledge originates.

A factory-development result may first be a candidate. The transition becomes operative only when the result is installed into a production path and affects later work over the declared horizon. [Operative change](./operative-change.md) supplies that stronger condition.

## Exclusions

- Selecting or binding an anticipated product variant is product configuration, not factory development relative to the producing factory.
- Generating or assembling a family member changes a product relative to the producing factory even when the operation is fully automatic. A factory-valued member may simultaneously be the result of factory development relative to the produced factory.
- Editing a copied asset only for one product is product development unless the change enters the reusable factory machinery.
- Feedback, telemetry, a feature request, or a proposed schema is an input or candidate, not completed factory development by itself.

## Misuse Cases

- Calling every edit made by a factory developer factory development even when the edit affects only one product.
- Calling computational product generation factory construction because both produce software artifacts.
- Treating a stored factory candidate as an operative revision without identifying its later production consumer and authority path.

---

Relevant Notes:

- [A software factory is family-scoped lifecycle production machinery](../a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — grounds: supplies the historical factory/member process split, Greenfield's specialization and composition operations, and the evidence for feedback-supported versioned revision
- [Software factory](./software-factory.md) — defined-in: names the family-scoped production machinery that factory development constructs or changes
- [Behavior-determining organization](./behavior-determining-organization.md) — extends: supplies the general system-level class into which a factory's reusable production machinery falls
- [Operative change](./operative-change.md) — extends: distinguishes an installed, behavior-reaching factory transition from a proposal or inert artifact
