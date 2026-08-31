---
description: "MDSoFa computes tool-specific factory assets from supplied metamodels and expertise, establishing recursive construction but not acquisition of family-specific production knowledge."
source: https://s23m.com/oopsla2004/langlois.pdf
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: d06c8aeb369fc0483bf0cc33b42b0ed7a473e44aee2366ee784360996bf091f6
ingested: "2026-08-31"
occasion: "determine whether established universal-factory and factory-generator terminology conflicts with or subsumes a proposed concept about computational acquisition of family-specific production knowledge."
type: kb/sources/types/ingest-report.md
domains: [software-factories, model-driven-engineering, metamodeling, generative-programming]
---

# Ingest: MDSoFa: A Model-Driven Software Factory

## Classification

This is a scientific paper whose contribution is an implemented model-driven architecture and lessons from its use, not a controlled experiment. Author: Benoît Langlois and Daniel Exertier wrote from THALES Research & Technology as developers of MDSoFa in the MIRROR program, giving them direct implementation and organizational experience but also an interest in presenting their own approach favorably.

## Summary

Langlois and Exertier define a model-driven software factory as a producer whose inputs and outputs can each be metamodels, expertise, tools, and frameworks; when the output is another such producer, they call it a software factory factory. MDSoFa realizes this recursively typed design by combining supplied metamodels, mappings, aspects, generic expertise, and target-platform choices, then using rule selection and template substitution to emit specific expertise, code, configuration, and modeling environments. The paper separates metamodel development, expertise development, asset production, and packaging, reports one THALES modeling chain spanning 14 metamodels and two tool platforms, and presents methodological lessons about architecture, iteration, modularity, and the limits of automation.

## Quotes

- **Source extract (verbatim):** A model-driven software factory is a combination of metamodels, expertise, tools and frameworks for producing output assets in an industrial way, that can be also metamodels, expertise, tools and frameworks, i.e. recursively, a model driven software factory can produce a model-driven factory. Depending on the focus of the produced assets, a software factory has the following functions: • Model factory. In this case, models are produced automatically from models. For instance, a model transformation can be deduced from the application of a model transformation pattern on a domain metamodel. • Expertise factory. In this case, the software factory produces specific or generic expertise from specific or generic expertise. For instance, model checks and wizards can be produced from a methodological metamodel and a generic expertise for model checking and assistance. • Tool factory. In this case, the software factory produces tools or executable environments in a tool, as a tool-specific modeling chain. • Framework factory. In this case, the produced asset is a framework. • Software factory factory. As mentioned above, this specific case covers the reflective approach when all types of asset are involved in input and output of the software factory for producing a software factory.
  - **Source location:** Section 3, “Cartography of the model-driven software factories,” PDF pages 3–4

- **Source extract (verbatim):** Process 1: Metamodel development process. During this process, a METAMODEL DESIGNER is in charge to define the MOF metamodels, the MOF to MOF mappings and the aspect definition. The METAMODEL DESIGNER and the SOFTWARE ARCHITECT must share the same vision in large, especially on the core technology and domains metamodel organization, and in detail, as the UML mapping.
  - **Source location:** Section 4, “The MDSoFa process,” PDF page 6

- **Source extract (verbatim):** Process 3: Asset production process. This process is the heart of the software factory where target assets are produced in series. An asset production in MDSoFa combines metamodels and generic expertise to produce output assets. Asset production uses the pattern matching technique for selecting QVT rules (expertise) involved in the concerned aspect(s), and the template technique for transforming a generic expertise into a specific expertise.
  - **Source location:** Section 4, “The MDSoFa process,” PDF page 6

## Connections Found

This paper is a technical prior-art anchor for computational factory construction. It strengthens [Greenfield and Short's recursive factory account](./greenfield-short-software-factories-oopsla-2003.ingest.md) with a concrete metamodel-to-environment generator, while the later [Greenfield account of factory specialization](./greenfield-mass-customizing-software-factories-2007.ingest.md) establishes **factory specialization** as changing the factory's own viewpoints, artifacts, activities, and assets.

The main boundary is captured by [Factory construction is not evidence of production-knowledge acquisition](../notes/factory-construction-does-not-establish-knowledge-acquisition.md). MDSoFa computes substantial factory assets from supplied metamodels, mappings, expertise, and platform choices. It does not demonstrate a system-determined process that infers those family-defining inputs from task or production evidence.

Like the construction methods surveyed in [Program Synthesis](./program-synthesis-gulwani-polozov-singh-2017.ingest.md), MDSoFa starts after relevant domain and platform knowledge has been supplied. Its human metamodel, expertise, architecture, and strategy roles therefore make it a boundary case for both [hand-crafted bootstraps](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) and [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): recursive generation inside a supplied design does not acquire or evidence-responsively revise that design.

## Extractable Value

1. **Treat construction-only novelty as subsumed.** MDSoFa explicitly names a software factory factory and implements the production of tool-specific modeling factories from metamodel-level definitions and reusable expertise. A proposed concept that claims only computational construction of family-specific factory assets does not distinguish itself from this mechanism. [quick-win]
2. **Reserve new terminology for the acquisition boundary.** `Software factory factory` already names recursive factory production, and `factory specialization` already names changing an existing factory's reusable production structure. A new term earns a separate role only if it denotes acquisition, search, or evidence-responsive revision of family-specific production knowledge rather than application of supplied knowledge. [quick-win]
3. **Use MDSoFa's input-operation-output contract as the comparison test.** Its available inputs are metamodels, mappings, aspects, generic expertise, and target-platform choices; its composable operations are rule selection, template substitution, aspect weaving, and packaging; its expressible mappings turn metamodel-level definitions into specific expertise and modeling environments. This makes the construction boundary inspectable instead of metaphorical. [deep-dive]
4. **Keep the factory-defining decomposition outside the demonstrated computation.** The asset taxonomy, internal language, core architecture, reusable expertise, target parameters, process roles, and strategic choices are designed or selected by people. Successful generation within those coordinates does not show that MDSoFa can discover or repair them. [quick-win]
5. **Separate implementation existence from outcome evidence.** The reported MDSysE counts and two target platforms show that the mechanism produced substantial artifacts in an industrial setting, but they do not measure productivity, quality, adaptability, or superiority over another factory design. [just-a-reference]

## Limitations (our opinion)

The paper is a self-report of one 2004 tool and modeling-chain program. Its validation table gives asset counts, two target platforms, and an extensibility statement, but no baseline, controlled comparison, defect data, development-time result, or longitudinal account of maintenance and failed attempts. It therefore supports the existence and terminology of computational factory construction more strongly than the claimed productivity, quality, or flexibility benefits.

The demonstrated targets are model-driven engineering environments built from deliberately supplied metamodels and expertise. The paper does not show automatic acquisition of domain structure or intent, evidence-based choice among factory revisions, or generalization to arbitrary software families. Calling its output a software factory also depends on the paper's broad asset taxonomy, so the architectural pattern travels more reliably than any claim of unrestricted scope.

## Recommended Next Action

Use MDSoFa as the strongest retained implementation precedent for constructing factory assets from supplied family knowledge. Compare later learning systems by whether task or production evidence determines the family-specific production knowledge that MDSoFa receives as metamodels, mappings, expertise, and strategic choices.

Abstracted into:

- [Factory construction is not evidence of production-knowledge acquisition](../notes/factory-construction-does-not-establish-knowledge-acquisition.md) — uses MDSoFa to bound novelty at construction and locate the stronger production-knowledge acquisition question
- [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — places MDSoFa's recursive asset production beside the inherited Greenfield factory ontology without treating the two definitions as identical
