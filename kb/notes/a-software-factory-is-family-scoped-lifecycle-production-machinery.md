---
description: "Reconstructs Greenfield's versioned software-factory ontology: declared product family, schema, packaged assets, configured environment, two development processes, and lifecycle work products"
type: kb/types/note.md
traits:
  - title-as-claim
  - has-comparison
  - has-external-sources
  - synthesis
---

# A software factory is family-scoped lifecycle production machinery

Here, *software factory* refers to the family-specific production arrangement shared by Greenfield and Short's 2003 account and Greenfield's mature 2007 account. The stable idea is a configured environment carrying reusable production knowledge for a declared family of software products or solutions. The implementation and terminology are versioned: the 2003 account defines an extensible IDE configured with a software template, while the 2007 account explicitly defines a specialized development and runtime environment supplying integrated special-purpose assets.

The [2003 paper](../sources/greenfield-short-software-factories-oopsla-2003.ingest.md) supplies the original `software schema`, `software template`, configured-IDE definition, developer roles, and factory-building example. The [2007 account](../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) supplies the mature software-factory schema and template, lifecycle scope, two interacting development processes, factory specialization, factory composition, and feedback-supported revision. The available [2004 book preview](../sources/greenfield-short-software-factories-book-preview.ingest.md) confirms the book and its broad integration program but is too partial to ground its detailed ontology.

The stable relation is:

```text
declared product or solution family
  -> factory development organizes family production knowledge
  -> schema plus packaged reusable assets
  -> configured production environment
  -> solution development creates and sustains family members
  -> product-specific lifecycle work products express member state
```

## Versioned ontology

| Object | 2003 account | Mature 2007 account | Stable boundary |
|---|---|---|---|
| Product or solution family | A product family is defined through common features, known variation points, variants, constraints, and domain models that delimit prospective members. | Products or solutions vary in features and operational qualities within a family addressed by the factory. | Family scope is part of factory identity; membership is not whatever a tool happens to emit. |
| Schema | A `software schema` is a graph of family viewpoints with associated domain-specific languages, constraints, and transformations. It describes the specifications needed to produce a member. | A `software factory schema` is a dynamic, family-specific architecture framework. Its viewpoints organize stakeholder concerns, artifacts, activities, supporting assets, and relationships across architecture and lifecycle. | The schema organizes family production knowledge. The later schema is richer and should not be projected backward as a mere rename. |
| Template | The schema, the processes for capturing and using its information, and tools that automate those processes collectively form a `software template`. | A `software factory template` is a structured, installable package of customizable tools, processes, content, partial lifecycle artifacts, and implementation assets. | The template packages reusable machinery for installation; it is not itself the configured production environment. |
| Configured factory | An extensible IDE configured with a software template for one product family becomes a software factory. | A software factory is a specialized development and runtime environment supplying an integrated set of special-purpose assets for a family. | The factory is the configured environment that makes family production machinery available in actual work. |
| Reusable assets | Product-line developers build implementation assets such as architecture and components, plus process assets and tools. | Assets include guidance, processes, requirements and architecture prototypes, test suites, deployment and operational material, patterns, samples, templates, libraries, frameworks, models, configuration files, components, and tools. | Reusable assets carry or enact family-level production knowledge. |
| Family member | Product developers configure and assemble one member of the product family. | Solution developers use the factory to build and sustain individual solutions, including selecting, adapting, configuring, completing, assembling, and generating product-specific work. | Product-specific lifecycle work products express the member's state; they are not automatically reusable factory machinery. |
| Development roles | Product-line developers construct the family machinery; product developers use it to build members. | Factory developers construct and revise assets for solution developers; solution developers build and sustain solutions for customers. | Constructing reusable family machinery and developing one family member are different processes. |

## Family knowledge is distributed across the factory

No retained Greenfield source puts all production knowledge in one model. It is distributed across:

- family scope, commonality, variability, variants, and constraints;
- schema viewpoints, concerns, relationships, languages, constraints, and transformations;
- processes, activities, guidance, and expected work products;
- tools, generators, frameworks, components, patterns, libraries, configuration files, and other implementation assets; and
- reusable or prototypical lifecycle content such as requirements, architectures, tests, deployment topologies, operational facilities, maintenance plans, and migration pathways.

Model-driven development is therefore one constituent technique rather than a synonym for the factory. Greenfield's program combines software product lines, model-driven development, guidance automation, and architecture frameworks. Product lines supply managed commonality and variability; models provide metadata for automation; guidance connects activities and assets; architecture frameworks organize viewpoints and lifecycle relationships.

An individual model, workflow, tool, asset, or schema may be part of the production machinery without being the whole factory. Conversely, a generated program can be a family member even when it was built through extensive automation. Mapping newer agentic artifacts such as prompts or evaluators into these roles is a later extension, not part of the historical reconstruction.

## Factory development and solution development update different things

Greenfield's mature account explicitly uses two interacting development processes.

| | Factory development | Solution development |
|---|---|---|
| Primary target | Reusable family-level production machinery | One family member and its lifecycle work products |
| Typical inputs | Domain knowledge, intended family scope, commonality and variability, process knowledge, platform choices, reusable expertise | Requirements for one solution plus the already supplied schema, template, tools, guidance, and assets |
| Typical work | Define or revise family scope and viewpoints; construct processes, content, implementation assets, and tools; package and configure the production environment | Select and bind anticipated variation; adapt, complete, assemble, generate, test, and otherwise sustain product-specific work across the supported lifecycle |
| Output | A configured software factory or a revised reusable asset base | One software product or solution whose state is expressed through lifecycle work products |
| Feedback | Solution developers report defects, requests, and unanticipated variation to factory developers | Customers and environments expose product defects, needs, and consequences |

The same observation may matter to both processes without collapsing them. A failed test can guide repair of the current product. It can also motivate a change to a reusable test asset or production rule. Only the second change is factory development relative to the same producing factory.

Greenfield also describes changing a dynamic schema to accommodate variation in an individual solution. A viewpoint or schema change therefore does not by itself identify factory specialization. A member-specific configured-schema variation remains solution development; a change to reusable base-factory structure intended to govern later solution work is factory development.

The retained sources describe people performing the interpretive and design work in this feedback path. They show that factories can be revised in response to use, but they do not define a computational learning algorithm or establish that the factory itself closes the feedback loop.

## Similar operations act at different levels

The target and reuse scope distinguish operations that otherwise use similar verbs:

- **Product configuration or generation** selects, binds, adapts, assembles, or materializes one member inside supplied family machinery.
- **Factory specialization** adds, removes, or changes reusable viewpoints and their associated artifacts, activities, and assets.
- **Product composition** combines outputs from multiple factories into one deliverable.
- **Factory composition** combines production structures or viewpoints from multiple factories.
- **Feedback-supported factory revision** changes reusable machinery across versions in response to defects, new demands, practices, technology, or variation not handled by the current asset base.

Greenfield does not supply a closed algebra of these operations. In particular, changing a member-specific configured schema is not automatically factory specialization, and producing an artifact that happens to be another tool or factory does not automatically revise the producer.

## The factory spans the lifecycle

The product is not only generated implementation code. The factory may supply machinery for requirements, specification, architecture, implementation, testing, deployment, operation, maintenance, and migration. Its products are correspondingly represented by lifecycle work products, including executable and deployed realizations where relevant.

This lifecycle scope is one reason a generic code generator or coding agent is not automatically a Greenfield-style factory. The term denotes an integrated family production arrangement, not merely a capability to emit source code.

## What the imported ontology does not establish

The Greenfield ontology does not by itself imply:

- that the factory learns from production experience;
- that its family scope or assets are acquired computationally;
- that the configured environment acts without human developers;
- that every useful production decision is inside one computational boundary;
- that producing another factory is self-improvement; or
- that one factory can handle previously unanticipated product families.

Greenfield, Cook and Kent, and MDSoFa do provide real prior art for factories or tool factories producing other production machinery. The separate note [A software factory can produce another factory without acquiring its family-specific production knowledge](./a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md) identifies the remaining distinction: constructing a producer from supplied family knowledge is not the same as acquiring or revising that knowledge from experience.

## Evidence limits

These sources primarily present an architectural and methodological program. The 2003 paper and 2007 essay support the ontology and intended process division more strongly than claims of productivity, quality, predictability, or economic transformation. Their Microsoft tooling context should not be mistaken for a timeless implementation prescription. What transfers most reliably is the family/machinery/member distinction and the separation of factory development from solution development.

---

Relevant Notes:

- [Software factory](./definitions/software-factory.md) — defined-in: supplies the compact term boundary derived from this reconstruction
- [Factory development](./definitions/factory-development.md) — defined-in: isolates the process that constructs or revises reusable family machinery
- [A software factory can produce another factory without acquiring its family-specific production knowledge](./a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md) — extends: uses recursive-construction prior art to identify the acquisition boundary
- [The deployed system, not the model alone, is the unit of learning](./the-deployed-system-not-the-model-is-the-unit-of-learning.md) — compares: likewise treats behavior as determined by a configured arrangement of models, artifacts, tools, and runtime machinery
