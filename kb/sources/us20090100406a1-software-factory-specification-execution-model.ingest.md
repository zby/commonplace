---
description: "Greenfield's patent application formalizes software factories as human-authored schemas that separate family knowledge from product-specific runtime state"
source: https://patentimages.storage.googleapis.com/bf/4b/59/47a31813aafb46/US20090100406A1.pdf
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: design-proposal
snapshot_sha256: cd23d412d0f0526c823a28f8a5cea4c592635f279cc6293f4eb14a87b71a84ba
ingested: "2026-08-31"
occasion: "reconstruct Greenfield's mature ontology—schema, viewpoints/views, concerns, work-product types/instances, task/workstream templates and instances, assets, factory developer versus development team, product state and lifecycle—and preserve the boundary that human factory developers supply family-specific knowledge"
type: kb/sources/types/ingest-report.md
domains: [software-factories, metamodeling, domain-specific-knowledge, development-process]
---

# Ingest: Software factory specification and execution model

## Classification

This is a patent application and design disclosure. It defines the elements and operation of a software-factory specification and execution model, while its claims seek legal coverage rather than reporting an evaluated implementation. Author: Jack Greenfield, Mauro Regio, Wojtek Kozaczynski, and Thomas J. Hollander were Microsoft practitioners and inventors developing the software-factory approach; Microsoft Corporation is the assignee.

## Summary

The application presents a two-level model for product-family development. A metamodel defines the permissible elements and relationships of factory schemas; a factory developer instantiates that metamodel as a factory schema and supplies the editors, task templates, and assets that, together with the schema, form a software factory. The schema defines viewpoints that isolate stakeholder concerns, work-product types, task and workstream templates, relationships, and cross-relationship operations. During product development, a team creates viewpoint instances called views, work-product instances, tasks, and workstreams for a particular product. The product's state is expressed as a collection of work products organized through views, while generated tasks and contextual assets guide its specification, development, deployment, maintenance, and eventual storage.

## Quotes

- **Source extract (verbatim):** The factory schema and the editor(s), task template(s) and asset(s) described collectively form a “software factory’, or simply a “factory”
  - **Source location:** Paragraph 0006, PDF page 2

- **Source extract (verbatim):** Such a model can be defined, for example, by a factory developer. In one implementation, the model and the editor(s), task template(s) and asset(s) defined can be collec tively employed in an interactive development environment by a development team to produce a specific type of product (e.g., client application, mobile client, web service(s), etc.).
  - **Source location:** Paragraph 0021, PDF page 3

- **Source extract (verbatim):** The factory schema 130 can be employed in an interactive development environment, along with the editor (S), task template(s) and asset(s) described, to support the specification, development, deployment and maintenance of a product (e.g., client application, mobile client, web service (s), etc.). The factory schema 130 and the editor(s), task template(s) and asset(s) described collectively form a “soft ware factory’, or simply a “factory’, that can be employed to improve the productivity of software development team(s) by enabling systematic reuse of Software assets that can be applied to produce a wide range of variants of a specific type of software system by exploiting well-defined variability points.
  - **Source location:** Paragraph 0024, PDF page 3

- **Source extract (verbatim):** 4. The system of claim 1, wherein the factory schema further comprises a definition of the types of work products consumed by a particular task. 5. The system of claim 1, wherein the factory schema further comprises a definition of the types of work products to be produced by a particular task. 6. The system of claim 1, wherein the factory schema comprises a particular viewpoint that maps to a designer. 7. The system of claim 1, wherein the factory schema is a schema for a software factory system. 8. The system of claim 1, wherein each task template is part of a workstream template describing a workstream that com prises a custom process. 9. The system of claim 1, wherein the factory schema comprises a description of assets available to each task tem plate.
  - **Source location:** Claims 4–9, PDF page 10

- **Source extract (verbatim):** in order to evaluate and modify the state of the product 420 under development expressed as a collection of work products (i.e., instances of work product type(s) 260)
  - **Source location:** Paragraph 0040, PDF page 4

- **Source extract (verbatim):** factory schema, instances of the viewpoints it describes (i.e., views), and instances of the work product types it describes (i.e., work products)
  - **Source location:** Paragraph 0040, PDF page 4

- **Source extract (verbatim):** The team member(s) can further retrieve and use relationships 220 and operations 230 across viewpoints 210, generate tasks and workstream(s) (i.e., cus tomized processes) from task template(s) 240 and work stream templates 270, and access associated asset(s) 250 for those tasks, in order to evaluate and modify the state of the product 420 under development expressed as a collection of work products (i.e., instances of work product type(s) 260)
  - **Source location:** Paragraph 0040, PDF page 4

## Connections Found

This application is the technical basis and vocabulary anchor for Greenfield's mature software-factory ontology. It compares with the [2003 software-factories paper](greenfield-short-software-factories-oopsla-2003.ingest.md), which packages a product-family software schema with processes and tools as a software template, by replacing that coarser account with an explicit metamodel and named type/instance distinctions. It also compares with the [2007 mass-customization essay](greenfield-mass-customizing-software-factories-2007.ingest.md), which groups concerns, artifacts, activities, and assets under viewpoints, by separating viewpoint from view, work-product type from work product, task and workstream templates from their runtime instances, and assets from the tasks they support. No current KB note reconstructs this later ontology. The application supplies terminology and structure for that reconstruction, not evidence that adopting the factory improved software outcomes.

## Extractable Value

1. **The mature ontology separates product-family definition from product construction.** The metamodel constrains factory schemas; a factory schema declares the family-specific viewpoints, work-product types, process templates, relationships, and operations; and the running factory creates product-specific views, work products, tasks, and workstreams. This layered map resolves terms that the earlier Greenfield sources leave bundled together. [deep-dive]
2. **Human factory developers supply the family-specific knowledge.** The factory developer defines the schema and provisions its editors, task templates, and assets, while the development team uses those definitions to build variants. The IDE exposes and enacts captured knowledge; the application does not claim that the system discovers the family ontology, process, or assets for itself. [quick-win]
3. **A viewpoint is a concern-bearing type, while a view is product state seen through it.** A viewpoint isolates concerns of stakeholders in a role and may specify scope, notation, and editors. A view is its product-specific instance, often mapped to a document in an editor, and may contain work products. This distinction prevents `viewpoint`, `view`, and `concern` from being collapsed during reconstruction. [quick-win]
4. **Work-product and process concepts have parallel type/instance boundaries.** Tasks consume or produce instances of declared work-product types. Task templates describe those tasks; workstream templates relate task templates into custom processes; and runtime tasks and workstreams are generated for a selected view or work product, with context able to supply template parameters. [deep-dive]
5. **Assets are contextual aids, not autonomous actors or product state.** Documents, code templates, scripts, patterns, recipes, and similar reusable assets are assigned to task templates and surfaced when a generated task is selected. Their position in the ontology is therefore task support, distinct from both the work products being changed and the knowledge-bearing schema that makes them available. [quick-win]
6. **The product is modeled as evolving work-product state across a broad lifecycle.** Views organize the product's work products; tasks create or modify them; the environment displays progress and can retain task-experience data; and the factory is said to support specification through maintenance. This is a useful lifecycle skeleton, but not a formal state-transition or learning model. [just-a-reference]

## Limitations (our opinion)

The application is useful for reconstructing the authors' ontology, but not for establishing the claimed gains in productivity, predictability, quality, reuse, traceability, onboarding, or maintenance. It reports no deployment evidence, comparative baseline, measured outcome, or failed adoption. Its metamodel is described in prose and an illustrative UML figure rather than supplied as a complete machine-readable schema, so some cardinalities and execution semantics remain underspecified. The lifecycle account shows project creation, display, task generation, asset use, and product storage, but does not define a full state machine, versioning discipline, change-propagation semantics, or empirical feedback loop. The authors and assignee also have an interest in stating the invention broadly. Most importantly, nothing here supports reassigning family-specific ontology formation to the execution system: that knowledge is supplied by a human factory developer.

## Recommended Next Action

Write `kb/notes/a-software-factory-separates-family-knowledge-from-product-state.md` as a comparative reconstruction from the 2003, 2007, and 2009 Greenfield ingests, using this application as the ontology anchor and making the factory-developer/development-team boundary explicit without promoting its benefit claims as outcome evidence.

Abstracted into:

- [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — uses the later execution model to distinguish viewpoint, work-product, task, and workstream types or templates from their product-specific instances
