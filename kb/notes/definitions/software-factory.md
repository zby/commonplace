---
description: "Definition — in the Greenfield lineage, a software factory is a configured family-specific software-production environment"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Software factory

In the Greenfield lineage used here, a **software factory** is a configured, family-specific software-production environment for a declared family of software products or solutions. Greenfield and Short's 2003 account realizes it as an extensible IDE configured with a family-specific software template. Greenfield's mature 2007 account describes it as a specialized development and runtime environment that supplies an integrated set of special-purpose assets.

Across the two accounts, the stable core is an environment configured with reusable production knowledge for one declared family. That knowledge is distributed through a schema, reusable assets packaged in a template, processes or guidance, tools, and development or runtime support used to create and sustain family members across the relevant lifecycle.

This is a version-bounded explication of the [2003 account](../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) and Greenfield's [mature 2007 account](../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md). Their vocabularies are historically related but not identical. The [versioned ontology reconstruction](../a-software-factory-is-family-scoped-lifecycle-production-machinery.md) owns the detailed schema, template, viewpoint, artifact, activity, asset, and developer-role distinctions.

## Core boundary

The declared product or solution family is part of the factory's identity. Its commonality, variability, variants, constraints, and lifecycle concerns delimit the space for which the reusable production machinery is intended.

The schema organizes family production knowledge. A software factory template packages customizable assets for installation. The configured production environment is the factory that solution developers use. A schema, template, tool, workflow, or reusable asset may be part of a factory without being the whole factory.

Product-specific requirements, designs, models, code, tests, deployment descriptions, and other lifecycle work products express the state of one family member. They are outputs or working state of solution development, not reusable factory machinery merely because the factory helped create them.

Actor allocation is separate. Greenfield's accounts primarily describe human factory developers and solution developers supported by automation. Calling an arrangement a software factory does not imply learning, autonomy, computational closure, unattended generation, or self-improvement.

## Exclusions

- A generic IDE, coding agent, agent harness, build pipeline, or workflow is not a software factory in this sense merely because it helps produce software. The family-specific reusable production knowledge and declared reuse scope are essential.
- A generator that emits one program is not the whole factory when the family schema, processes, tools, tests, configuration knowledge, or other reusable assets remain elsewhere.
- A software factory schema or installable template is not by itself the configured production environment that Greenfield calls a factory.
- A family member is not the factory that produced it. A member may itself be another factory only when the producing factory's declared family admits factory-valued products.
- Producing, configuring, or revising one product does not by itself show that the factory has changed or learned.

---

Relevant Notes:

- [A software factory is family-scoped lifecycle production machinery](../a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — grounds: reconstructs the versioned historical ontology and the family-machinery/member boundary
- [Factory development](./factory-development.md) — defined-in: names the separate process that constructs or revises reusable factory machinery
- [A software factory can produce another factory without acquiring its family-specific production knowledge](../a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md) — contrasts: separates recursive construction from acquiring the production knowledge supplied to the constructor
