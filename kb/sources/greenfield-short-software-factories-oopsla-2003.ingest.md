---
description: "Greenfield and Short define a software factory as family-specific production machinery and distinguish its construction, operation, and recursive bootstrapping."
source: https://www.s23m.com/oopsla2003/greenfield.pdf
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: 6d51198ff3fd49120ad3f301ad02935271e20689a53a8a60151fbff1f7a192a1
ingested: "2026-08-31"
occasion: "reconstruct Greenfield and Short’s original software-factory ontology and distinguish factory construction from family-member production, including their explicit bootstrapping claim."
type: kb/sources/types/ingest-report.md
domains: [software-factories, software-product-lines, model-driven-development, bootstrapping]
---

# Ingest: Software Factories: Assembling Applications with Patterns, Models, Frameworks and Tools

## Classification

This is a scientific conference paper whose main contribution is a design synthesis and technical vision rather than an empirical evaluation. It integrates software product lines, model-driven development, and component-based development into a proposed production system for a specific product family. Author: Jack Greenfield and Keith Short were members of Microsoft’s Visual Studio Enterprise Frameworks & Tools organization and primary proponents of the software-factory approach, giving them direct design knowledge but also a platform-vendor interest in the framing.

## Summary

Greenfield and Short define a software factory as an extensible IDE configured for one product family by a software template. The template packages a software schema—a graph of viewpoints, domain-specific languages, constraints, and transformations—with processes, frameworks, components, patterns, and tools that encode how to produce members of that family. Product-line developers construct these production assets and configure the factory; product developers then use the factory to select variation points, assemble assets, populate the schema, and produce a particular family member. The authors also state that software factories can produce other software factories: an IDE is used to build an initial factory-building template, and the resulting configured IDE helps product-line developers build more specialized templates. This bootstrapping makes factory construction recursive, but the paper continues to assign the design of each produced factory to human product-line developers.

## Quotes

- **Source extract (verbatim):** A grid like the one in Figure 3 can be generalized as a graph of viewpoints for a product family, and tools can be developed inexpensively to support the editing and transformation of the associated DSLs. We call this graph a software schema, because it describes the set of specifications that must be developed to produce a software product. A software schema for a product family, the processes for capturing and using the information it describes, and the tools used to automate that process collectively form a software template.
  - **Source location:** Section 3, discussion following Figure 3, PDF pages 5–6

- **Source extract (verbatim):** An IDE configured with a software template for a product family becomes a factory for producing members of the family. This is what we call a software factory.
  - **Source location:** Section 3, discussion following Figure 3, PDF page 6

- **Source extract (verbatim):** Product line developers build production assets used by the product developers to produce family members. These include implementation assets, such as architecture and components, used to implement the family members, and process assets, such as a process, which describes the use of the implementation assets, and tools, which automate parts of the process.
  - **Source location:** Section 4.2, “Software Product Lines,” PDF page 9

- **Source extract (verbatim):** As it turns out, software factories can be used to produce other software factories. In Step 1 of Figure 9, an IDE is used to build a languages, frameworks and tools for building software factories. These assets comprise a software template that can be loaded into another instance of the same IDE. Configured in this way, the IDE is now Software Factory A in Step 2. This software factory can be used to build software factories.
  - **Source location:** Section 5.2, discussion preceding Figure 9, PDF page 11

- **Source extract (verbatim):** Software product lines are the critical innovation on the specificity axis that capitalizes on the separation of commonality and variability in product families. Figure 6 describes the main steps and deliverables in product line development. Recall that a software product line produces a family of software products that are deliberately designed to take advantage of common features and known forms of variation. Product line developers build production assets used by the product developers to produce family members. These include implementation assets, such as architecture and components, used to implement the family members, and process assets, such as a process, which describes the use of the implementation assets, and tools, which automate parts of the process. A key step in developing the production assets is to produce one or more domain models that describe the common features of problems in the domains addressed by the product line, and the ways in which they can vary. These models become detailed descriptions of the problem domains. They collectively define the scope of the product line, and can be used to qualify prospective family members.
  - **Source location:** Section 4.2, “Software Product Lines,” PDF page 9

## Connections Found

This paper is the KB’s historical ontology anchor for *software factory*. The [versioned Greenfield reconstruction](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) preserves its software-schema, software-template, configured-IDE, developer-role, and family-member distinctions without projecting the mature 2007 vocabulary backward.

It is also primary evidence for [the distinction between factory construction and acquisition of family-specific production knowledge](../notes/factory-construction-does-not-establish-knowledge-acquisition.md). Greenfield and Short explicitly describe a factory producing another factory, but human product-line developers still define the target family and design its specialized template and assets. The source therefore establishes recursive factory construction, not a system-determined process for acquiring the family knowledge embodied in the result.

The configured producer also compares with [the deployed system, not the model alone, as the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md): production depends on the IDE together with its schema, process, tools, and implementation assets, not on a generated model or family member alone. It provides a precise historical counterpoint to the broader modern usage in [Compound Engineering](../agentic-systems/compound-engineering-plugin.md), whose factory boundary is an artifact-mediated lifecycle workflow rather than a declared product family, software schema, and software template.

## Extractable Value

1. **Recover the original factory ontology as a typed composition.** A software factory is a family-specific configured IDE; its software template combines a software schema, processes, and production assets; its schema organizes viewpoints, DSLs, constraints, and transformations needed to specify and implement a family member. This prevents the factory from being collapsed into either a generic tool, a workflow, or the product it emits. [quick-win]
2. **Separate factory construction from family-member production.** Product-line developers build the reusable implementation and process assets and package them for an IDE, while product developers configure and use the resulting factory to assemble a selected member of the product family. The two activities operate on different objects and require different roles. [quick-win]
3. **Treat bootstrapping as recursive construction, not as learning by default.** The paper explicitly claims that software factories can be used to produce other software factories, but its example retains human product-line developers as the agents that define and package the next factory's family-specific machinery. Recursion alone therefore does not establish retained learning, improvement, or acquisition of that family knowledge. [quick-win]
4. **Preserve family scope as part of factory identity.** The reusable production knowledge is justified by economies of scope across multiple related but distinct products, and a domain model of commonality and variability delimits which prospective products count as family members. A system that lacks this declared reuse scope may use the factory metaphor without instantiating Greenfield and Short’s concept. [just-a-reference]
5. **Version the term `software schema` rather than silently equating it with later factory schemas.** Here it means a graph of specification viewpoints and their DSLs, constraints, and transformations for a product family; later sources may attach activities, artifacts, assets, or broader lifecycle structure to a factory schema. [deep-dive]

## Limitations (our opinion)

The paper proposes an integrated architecture and illustrates it with a banking scenario, but it does not implement or empirically compare a complete software factory. Its productivity, quality, supply-chain, and mass-customization claims therefore remain forecasts supported mainly by analogy and prior product-line practice, not outcomes measured for the proposed integration. The concrete mechanisms also reflect the 2003 Microsoft IDE, .NET, and web-services setting, so their architectural roles travel more reliably than their platform examples. Finally, the bootstrapping example demonstrates a recursive tool-construction arrangement only; it does not test whether produced factories improve, whether evidence governs their redesign, or whether human family-design decisions can be removed from the loop.

## Recommended Next Action

Use the versioned ontology reconstruction for the inherited term boundary and the construction-versus-acquisition note for the recursive prior-art boundary. Further work should test how an agentic process could determine and retain family-specific production knowledge from task or production evidence rather than receiving it as a complete human design.

Abstracted into:

- [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — reconstructs the original schema, template, configured-factory, developer-role, family-scope, and family-member account without projecting later vocabulary backward
- [Factory construction is not evidence of production-knowledge acquisition](../notes/factory-construction-does-not-establish-knowledge-acquisition.md) — uses the human-directed factory-building example to separate recursive construction from acquisition of the target family's production knowledge
