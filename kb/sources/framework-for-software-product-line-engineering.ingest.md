---
description: "Distinguishes family-level platform and variability engineering from individual-product derivation, grounding the boundary for successor-factory learning."
source: https://sple.de/fileadmin/sse/user_upload/Files/SPLE-Book_Chap02.pdf
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: conceptual-essay
snapshot_sha256: c7431f4fae35d3dd4148e5be0a10851121660bb8010477abf66e29d4f4ed9c7b
ingested: "2026-08-31"
occasion: "Establish the adjacent software-product-line lineage needed to distinguish family-level production machinery from individual product development and to bound the proposed retained successor-factory learning move."
type: kb/sources/types/ingest-report.md
domains: [software-product-lines, software-reuse, variability-management, software-architecture]
---

# Ingest: A Framework for Software Product Line Engineering

## Classification

This book chapter is a conceptual framework: it defines the processes and artifacts of software product line engineering, synthesizes prior product-line work, and organizes the rest of its book, but it does not report a controlled evaluation. Author: Günter Böckle, Klaus Pohl, and Frank van der Linden signal domain expertise by locating the framework in the ESAPS, CAFÉ, and FAMILIES projects and in cited product-line engineering literature.

## Summary

The chapter divides software product line engineering into domain engineering and application engineering. Domain engineering scopes a planned family and creates a reusable platform spanning requirements, a reference architecture, components, tests, a variability model, and traceability. Application engineering derives each product by reusing those artifacts, binding their variability, adding justified product-specific adaptations, and preserving consistency across the lifecycle. The framework makes explicit platform investment, planned reuse, and feedback between the two processes central to economical customization; it is most useful as a lifecycle ontology, not as evidence that this organization outperforms alternatives.

## Quotes

- **Source extract (verbatim):** Domain engineering: This process is responsible for establishing the reusable platform and thus for defining the commonality and the variability of the product line (Definition 2-1). The platform consists of all types of software artefacts (requirements, design, realisation, tests, etc.). Traceability links between these artefacts facilitate systematic and consistent reuse.
  - **Source location:** Section 2.3, “Overview of the Framework,” page 20

- **Source extract (verbatim):** Application engineering is the process of software product line engineering in which the applications of the product line are built by reusing domain artefacts and exploiting the product line variability.
  - **Source location:** Section 2.3, “Overview of the Framework,” pages 20–21

- **Source extract (verbatim):** Define the set of applications the software product line is planned for, i.e. define the scope of the software product line.
  - **Source location:** Section 2.4, “Domain Engineering,” pages 23–24

- **Source extract (verbatim):** The framework introduces four application engineering sub-processes: application requirements engineering, application design, application realisation, and application test. Each of the sub-processes uses domain artefacts and produces application artefacts.
  - **Source location:** Section 2.6, “Application Engineering,” page 31

## Connections Found

The chapter is a historical and conceptual anchor for separating family-level production machinery from individual-product derivation. It **compares with** [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): domain engineering supplies the product-line scope, platform, variability model, and permitted bindings within which application engineering works, so successful product derivation does not establish that the supplied family decomposition is adequate. It is also a technical basis for [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md), because the conventional framework assigns construction of family-specific reusable structure to a separate engineering process; computationally binding its options is therefore weaker than learning to construct or revise that structure.

The platform's inclusion of requirements, architecture, components, tests, variability, and traceability **compares with** [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) by supplying an older production-system boundary broader than a generator alone. The chapter requires feedback between domain and application engineering, but leaves that feedback organizational and human-directed; it is not evidence of a closed learning loop.

## Extractable Value

1. **The framework separates production-system construction from product derivation.** Domain engineering defines and realizes the reusable family platform and its commonality and variability; application engineering reuses that platform and binds its variability for one product. This gives the successor-factory proposal a source-grounded boundary that ordinary single-product development does not provide. [quick-win]
2. **Automating derivation within a supplied variability model is not domain-extensible learning.** In connection with [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the family scope, variation points, variants, constraints, reference architecture, and configuration rules are outside application engineering's effective update space. A domain-extensible successor pathway must construct or revise whichever of those family-level choices a novel covered demand requires; succession by itself does not require every choice to change. [deep-dive]
3. **Family-level production machinery spans the development lifecycle.** The reusable platform includes requirements, architecture, implementation, test assets, a variability model, and traceability among them. This limits any successor-factory account that identifies the factory only with code generation or a model invocation. [quick-win]
4. **Feedback and traceability support evolution without establishing learning.** Feasibility feedback between domain subprocesses, application-to-domain deltas, and links from products back to domain artifacts can expose needed changes, but the framework specifies no computational search, evaluation, or operative retention process that selects those changes. [just-a-reference]
5. **Evaluation has distinct family and product responsibilities.** Domain testing validates reusable components and creates variable test assets before complete applications exist; application testing then checks the derived configuration, its selected variants, and its application-specific additions. A successor-factory evaluation design should therefore test both reusable machinery and concrete descendants. [experiment]

## Limitations (our opinion)

The chapter proposes a normative framework and vocabulary rather than testing the domain/application split against alternative organizational or technical decompositions. Its roots in early-2000s product-line projects and literature provide lineage but not current outcome evidence, and the extracted text does not preserve every visual relationship in the framework diagrams. Most importantly for transfer, its feedback remains an engineering activity: it supplies no computational learner, successor-production mechanism, or evidence that family scope, variability, architecture, and tests can be revised through search and retained on the strength of evaluation. Applying the framework to agent-operated learning systems is therefore an analogy whose causal claims must come from separate evidence.

## Recommended Next Action

Use [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) to carry the domain/application boundary, and [Domain-extensible software factory](../notes/definitions/domain-extensible-software-factory.md) when the stronger claim requires computational acquisition of family-level specialization.

Abstracted into:

- [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — uses the product-line domain/application split to clarify the analogous family-machinery versus member-state boundary
