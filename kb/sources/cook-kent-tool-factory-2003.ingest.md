---
description: "Cook and Kent specify a language-family tool generator and self-bootstrap, grounding recursive software-factory construction while leaving family specialization human supplied."
source: https://www.s23m.com/oopsla2003/cook.pdf
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: design-proposal
snapshot_sha256: 6353efb3029b5dd59c075569ed911bb3a67d48846ea27e289eeb263ce5cc8b5d
ingested: "2026-08-31"
occasion: "Investigate the book-derived Tool Factory as primary evidence on software factories or tools constructing and bootstrapping other production tools, and distinguish generated production tooling from acquisition of family-specific specialization."
type: kb/sources/types/ingest-report.md
domains: [software-factories, domain-specific-languages, tool-generation, bootstrapping]
---

# Ingest: The Tool Factory

## Classification

This workshop design proposal presents a reference architecture rather than an implemented system or empirical evaluation. Its content is adapted from chapter 5 of *Software Factories: Assembling Applications With Patterns, Models, Frameworks and Tools* by Jack Greenfield and Keith Short.
Author: Steve Cook and Stuart Kent were Microsoft practitioners who report prior involvement in UML 2 and model-driven software development. That experience makes the source a strong signal of the contemporary design program, but not independent evidence that the proposed architecture worked.

## Summary

Cook and Kent reject a universal modeling language in favor of a tool factory that builds tools for members of a domain-specific language family. A language designer combines family-defined fragments and patterns into a language definition covering concrete, abstract, and serialization syntax plus trace-based semantics. A design-tool generator then emits the language-specific part of a designer on top of a shared framework; the resulting environment can include a design surface, serializer, rule checker, pattern engine, interpreter or animator, model-by-example facility, and translators. The recursive step treats the language designer as another generated designer for a language for designing languages, so one version can generate the next and may also bootstrap the generator through supplied mappings. For a reader deciding whether this establishes self-producing software machinery, the answer is yes at the tooling layer, but not at the acquisition layer: people still provide the family definition, fragments, patterns, framework, and implementation mappings.

## Quotes

- **Source extract (verbatim):** A tool factory is a software system used to build tools that manipulate and process the members of a family of domain specific languages from specifications of the family members. In what follows we describe the architecture of a tool factory.
  - **Source location:** “From UML to Domain Specific Languages,” immediately before “Tool Factory Architecture”
- **Source extract (verbatim):** Figure 3 gives another perspective of the makeup of the X-designer. While our long-term vision is to generate complete designers from language definitions, this will certainly not happen soon, so we expect some hand-coding to take place. Code generation works best when the generated code completes an existing framework. Of course, there is a trade-off between placing functionality in the generated code, and placing it in the framework. In practice, a combination of the two approaches usually works best.
  - **Source location:** “Tool Factory Architecture,” discussion of Figure 3 (“Where The Code Comes From”)
- **Source extract (verbatim):** The Language Designer is just another X-designer, where X is the language for designing languages (LDL). Hence, it should have the same architecture as other designers, as illustrated in Figure 4. In particular, it is worth noting that in this case the pattern engine can be used to support the definition of language families. Figure 4 provides the last twist in the tale, observing that it should be possible to generate the LDL-designer from a definition of the language for designing languages (LDL). This allows the tool factory to bootstrap itself from one version to the next. In addition, provided the LDL is rich enough, it should be possible to define a mapping from language designs into the programming languages and frameworks used to implement designers, allowing the design tool generator to be bootstrapped, as well.
  - **Source location:** “Tool Factory Architecture,” paragraph between Figures 3 and 4

## Connections Found

The source's strongest role is technical basis for [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md). It makes recursive factory construction concrete as a dependency chain from a supplied language-family definition to a generated designer and then to a designer capable of regenerating its own kind. It therefore strengthens the note's construction account while preserving its boundary: producing another producer does not establish computational acquisition or revision of the producer's family specialization.

It complements [Greenfield and Short's broader software-factory account](./greenfield-short-software-factories-oopsla-2003.ingest.md) with the internal language-tool architecture, and it precedes [MDSoFa's implemented metamodel-and-expertise pipeline](./langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md). [DreamCoder](./dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) is a useful counterpoint on the acquisition boundary: Cook and Kent generate tools from a human-authored language definition, whereas DreamCoder revises a domain-specific language from task solutions under an explicit selection objective.

## Extractable Value

1. **Generated production tooling is not acquired specialization.** The paper gives a concrete route from a supplied family-member language definition to its designer and support components. This is direct evidence for the construction side of the distinction in [the software-factory synthesis](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md), while the language definition and family assets remain inputs chosen by people. [quick-win]
2. **The bootstrap changes the output type without changing who chooses the operative definition.** Treating the language designer as an instance of the same designer architecture permits one version to generate the next. Bootstrapping the generator is likewise conditional on people supplying a rich enough language for designing languages and mappings into the implementation languages and frameworks. [deep-dive]
3. **A language definition acts as a dependency specification for a suite of production tools.** Concrete syntax, abstract syntax, serialization, and trace semantics jointly determine generated and interpreted facilities such as editing, checking, serialization, animation, and translation. This mechanism adds language-tool granularity to the KB's broader account of family-scoped production machinery. [just-a-reference]
4. **Generation is explicitly divided among generated code, hand-crafted code, and a shared framework.** The proposal expects partial generation in practice and presents complete generation as a long-term goal. This prevents the self-bootstrap diagram from being read as evidence of an autonomous or fully generated tool chain. [quick-win]
5. **Interpretation can preserve a design-time change surface before static generation.** The proposed rule checker interprets well-formedness rules while the language designer experiments, with static code generation available after the rules are fixed. This offers a historical comparison for [progressive constraining](../notes/progressive-constraining-commits-only-after-patterns-stabilize.md), but it does not establish that note's repeated-run or LLM-specific criterion. [experiment]

## Limitations (our opinion)

The paper specifies an architecture and future direction but reports no implementation, benchmark, case study, failure analysis, or comparison with another tool-generation approach. Its strongest claim is therefore about a coherent proposed dependency structure, not feasibility, completeness, productivity, or quality. The claim that complete designers and the design-tool generator can be bootstrapped is conditional on a sufficiently expressive language for designing languages and on mappings that the paper does not define or test.

The bootstrap also omits the hard cross-version questions: how an initial trusted implementation is obtained, how generated output is validated, how incompatible language changes are migrated, and how a failed successor is rejected or rolled back. Most importantly for the acquisition boundary, no operation learns or proposes a family definition, language fragment, design pattern, framework, or implementation mapping from production evidence. Regeneration can propagate a supplied specialization without acquiring, evaluating, or improving that specialization. The architecture is tailored to domain-specific modeling-language families and trace-based semantics, so its component breakdown should not be assumed to cover every kind of production tool.

## Recommended Next Action

Update [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md), in its section on factory construction as prior art, to add Cook and Kent as the mechanism-level primary source for the language-definition-to-generated-designer bootstrap and to state that the human-supplied definition, fragments, patterns, framework, and mappings keep acquisition of family specialization outside the demonstrated computation.

Abstracted into:

- [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) — adds the generated-designer and conditional self-bootstrap mechanism while keeping language-family acquisition human supplied
- [Evidence-responsive operative succession turns meta-factory construction into learning](../notes/operative-succession-turns-meta-factory-construction-into-learning.md) — separates generated or self-bootstrapped production tooling from an evidence-responsive transition that installs machinery governing later work
