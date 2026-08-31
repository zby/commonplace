---
description: "Definition — a software factory is configured, family-specific production machinery for creating and sustaining software and its lifecycle work products"
type: kb/types/definition.md
tags: [foundations, self-improving-systems]
---

# Software factory

A **software factory** is configured production machinery specialized for a declared software product family. It integrates a family schema, packaged reusable assets, methods or workflows, tools, and development or runtime support so that human and computational actors can produce and sustain family members through their lifecycle work products.

This is a Greenfield-style explication. The [versioned source reconstruction](../a-software-factory-is-family-scoped-lifecycle-production-machinery.md) is the authority for the inherited schema, template, viewpoint, artifact, activity, asset, and developer-role vocabulary. This definition supplies a cheaper term boundary for later theory; it does not project one timeless ontology across every Greenfield source.

## Scope

The product family is part of the factory's identity. Its declared scope, commonality, variability, variants, and constraints delimit the production space for which the reusable machinery is intended. A factory may guide or automate requirements, specification, architecture, implementation, testing, deployment, operation, maintenance, and migration. It produces and sustains a family member by creating and changing lifecycle work products that express the member's state, including executable and deployed realizations where applicable.

The schema organizes family production knowledge. A software factory template packages customizable assets for installation. An **operative factory** is the installed or configured producer whose machinery can govern actual work. None of the schema, template, one asset, or one work product is the whole factory by itself.

Actor allocation must be declared separately. A conventional factory can supply an environment to human solution developers, automate selected activities, or combine both. Calling it a software factory does not imply autonomy, learning, or unattended end-to-end generation.

## Exclusions

- A generic IDE, coding agent, build pipeline, or workflow is not a software factory in this sense merely because someone calls it a factory. The term requires family-specific reusable production knowledge and a declared reuse scope.
- A generator that emits one program is not the whole factory when schema, configuration knowledge, tests, workflows, assets, or human production activities remain outside it.
- A family member and its product-specific work products are not reusable machinery of the factory that produces them. A member may nevertheless be another software factory when the producing factory's family admits factory-valued products.

## Misuse Cases

- Calling a factory schema or installable template the operative software factory without identifying the configured environment and authority path that enacts it.
- Treating every product the machinery happens to emit as a family member even when no declared family boundary admits it.
- Inferring factory learning from improved product output without a retained change to the production machinery.

---

Relevant Notes:

- [A software factory is family-scoped lifecycle production machinery](../a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — grounds: reconstructs the versioned historical ontology and the boundary between family machinery and member state
- [Behavioral authority](./behavioral-authority.md) — extends: identifies the consumer, channel, and force through which installed factory machinery governs later production
