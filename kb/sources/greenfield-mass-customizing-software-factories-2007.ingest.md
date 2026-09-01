---
description: "Greenfield's mature software-factory ontology separates family-specific production machinery and its feedback-supported revision from the development of individual solutions."
source: https://www.methodsandtools.com/archive/archive.php?id=64
captured: "2026-08-31"
capture: trafilatura
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: b5938962d1b49a39dc81edfa1d4eb722f6f703cd63e18c4db9c51f71e32e763f
ingested: "2026-08-31"
occasion: "Reconstruct the established software-factory ontology and distinguish factory development from solution development as a basis for later agentic-learning extensions."
type: kb/sources/types/ingest-report.md
domains: [software-factories, software-product-lines, model-driven-development, mass-customization]
---

# Ingest: Mass Customizing Solutions with Software Development Factories

## Classification

This is a conceptual essay that consolidates a software-factory methodology and argues for its role in software supply chains rather than reporting a controlled implementation or evaluation. Author: Jack Greenfield wrote as a Microsoft software-factory proponent and co-author of the approach's foundational book, which gives him direct design knowledge but also an interest in presenting the paradigm and its market potential favorably.

## Summary

Greenfield defines a software factory as a specialized development and runtime environment for a family of products or solutions. An installable factory template supplies customizable tools, processes, content, partial lifecycle artifacts, and implementation assets, while a dynamic factory schema organizes the target family's viewpoints, stakeholder concerns, artifacts, activities, assets, and relationships. The method explicitly integrates software product lines, model-driven development, guidance automation, and architecture frameworks; MDD automates lifecycle tasks from model metadata but is not the whole factory. Solution developers use this machinery to select, adapt, configure, complete, assemble, generate, and maintain individual solutions. Factory developers instead harvest domain practice, build and revise the reusable machinery, and respond to feedback or variation the existing asset base did not anticipate. Composition, specialization, and organizational partitioning can distribute both kinds of work across a supply chain. The article describes feedback-supported, versioned revision as human factory development; *factory evolution* is the KB synthesis's umbrella label, not a named operation established by this source.

## Quotes

- **Source extract (verbatim):** A software factory is a specialized development and runtime environment that supplies an integrated set of special purpose assets encapsulating proven patterns and practices, including tools, processes and content. Examples of content assets include partial or prototypical life cycle artifacts, such as requirements, logical and technical architectures, test suites, deployment topologies, operational facilities, maintenance plans and migration pathways, and implementation artifacts, such as guidelines, patterns, code samples, templates, libraries, frameworks, models, and configuration files.
  - **Source location:** “What Is A Software Factory?”

- **Source extract (verbatim):** The assets are delivered in a structured and installable package called a software factory template. The assets are usually customizable, and the organization of the template is designed to make it easy to select, adapt, configure, complete, assemble and parameterize the assets, enabling the factory to produce a wide range of solutions with varying features and operational qualities.
  - **Source location:** “What Is A Software Factory?”

- **Source extract (verbatim):** In addition to a set of stakeholder concerns, a viewpoint in a software factory schema defines a set of related artifacts relevant to those concerns, the activities that act upon the artifacts, and the assets used to perform the activities. The schema organizes the factory, and uses the relationships among viewpoints to integrate the activities, artifacts and assets across the software architecture and life cycle.
  - **Source location:** “Architecture Frameworks”

- **Source extract (verbatim):** A factory uses two interacting development processes. The first is the traditional development process by which solution developers build solutions for customers who use them to automate business processes, and who provide feedback to the solution developers, such as defect reports and feature requests. The second is a separate and more specialized development process by which factory developers build assets for solution developers who use them to build solutions, and who provide feedback to the factory developers, such as defect reports and feature requests.
  - **Source location:** “Factory Partitioning”

- **Source extract (verbatim):** Factory composition involves combining the viewpoints of the constituent factories, and factory specialization involves adding or removing viewpoints, and modifying viewpoints of the base factory by changing the artifacts produced, the activities that produce them, and the assets used to support and automate the activities.
  - **Source location:** “Factory Assembly”

- **Source extract (verbatim):** A key feature of the methodology is that the products of two or more factories can be composed. Instead of a single factory that helps them build the ultimate deliverable in its entirety, users can work with multiple factories, each helping them build a portion of the ultimate deliverable.
  - **Source location:** “Factory Composition”

## Connections Found

This article is the KB's mature historical ontology anchor for software factories, extending the earlier [Greenfield and Short account](./greenfield-short-software-factories-oopsla-2003.ingest.md) with explicit factory-development and solution-development processes, lifecycle operation, specialization, composition, feedback-supported revision, and supply-chain partitioning. The [versioned ontology reconstruction](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) preserves these additions without projecting them backward into the 2003 terminology.

The source also supplies the organizational precursor for [factory-level continual learning](../notes/factory-learning-is-experience-responsive-retention-that-improves.md). Feedback flows from solution developers to factory developers, but human factory developers interpret it and decide how reusable production machinery changes. The account therefore establishes feedback-supported factory development, not a system-determined learning process.

It compares with both [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) and [the hand-crafted-bootstrap boundary](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md): ordinary solution development operates inside the supplied family structure, while previously unanticipated variation can require people to revise the reusable machinery.

## Extractable Value

1. **Separate the two development processes by the artifacts they update.** Factory developers build and revise reusable assets for a product family; solution developers use those assets to build and maintain a particular family member. Defect reports and feature requests can flow between the processes without turning product development into factory development. [quick-win]
2. **Reconstruct the factory as family-scoped production machinery.** The factory is not the generated solution or a generic workflow: it is a specialized development and runtime environment whose installable template packages reusable tools, processes, content, lifecycle artifacts, and implementation assets for a declared family. [quick-win]
3. **Place MDD inside the wider factory synthesis.** The article names software product lines, MDD, guidance automation, and architecture frameworks as four integrated contributors. Models provide source metadata for lifecycle automation; product lines supply managed family variation; guidance connects assets to tasks; and architecture frameworks organize concerns and viewpoints. No contributor alone is the factory. [quick-win]
4. **Use the schema as the ontology's integration structure.** A factory schema is a dynamic, family-specific architecture framework. Its viewpoints join stakeholder concerns to artifacts, activities, and supporting assets, while relations among viewpoints enable trace, navigation, validation, analysis, synchronization, generation, and change-impact operations across the lifecycle. [deep-dive]
5. **Keep configuration distinct from factory specialization.** Solution work selects and parameterizes anticipated variation within the asset base. Previously unanticipated variation can require factory developers to adapt that base, while factory specialization changes reusable viewpoints and their artifacts, activities, and assets. Viewpoint change alone is not sufficient to classify the operation because a configured schema may also vary for one solution; target and reuse scope matter. [quick-win]
6. **Do not collapse product composition into factory composition.** Products from multiple factories can contribute portions of one deliverable, whereas composing factories combines their viewpoints into a larger production system. The distinction matters when deciding whether a loop is changing its output, its production machinery, or both. [just-a-reference]
7. **Treat feedback-supported, versioned revision as an open human process.** The article specifies feedback from customers to solution developers and from solution developers to factory developers, but people still interpret that evidence and redesign the assets. It therefore supplies the precursor ontology, not evidence that a computational system acquired the required family-specific production knowledge. [quick-win]

## Limitations (our opinion)

The essay presents a broad architectural and economic program, but it does not evaluate a complete factory, compare alternative factory decompositions, or substantiate its productivity, quality, predictability, and supply-chain claims with reported measurements. Its automobile-manufacturing analogy does not establish that software suppliers can achieve the same modularity, interface stability, or market coordination. The account also reflects Microsoft's platform and tooling interests and gives little evidence about failed deployments, governance costs, schema evolution conflicts, or the organizational burden of maintaining reusable assets.

Its two feedback processes show how humans may improve a factory; they do not establish that the factory learns, that its fixed family decomposition is adequate, or that revision can occur without people supplying the factory-development decisions.

## Recommended Next Action

Use the source as the mature ontology anchor and as the human-directed precursor to factory-level continual learning. A later experimental account should state which feedback remains external evidence and which factory-development decisions the computational learner itself determines.

Abstracted into:

- [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — reconstructs the mature lifecycle ontology, two development processes, factory specialization, factory composition, and feedback-supported revision
- [A software factory learns when production experience changes reusable machinery used later](../notes/factory-learning-is-experience-responsive-retention-that-improves.md) — extends the human-directed feedback path with the system-determined retained-change condition required for factory-level continual learning
