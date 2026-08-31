---
description: "A 1983 MARA project report uses universal software factory for a lifecycle tool environment portable across microprocessor families, not for acquiring family-specific production knowledge."
source: https://dspace-erf.nlr.nl/bitstreams/20caf012-9a56-4603-b0bc-d383579b5811/download
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
genre: practitioner-report
snapshot_sha256: 796e51fca6123553583c1e21de5ad603ca1955b2355b80babfd4f864b027da34
ingested: "2026-08-31"
occasion: "determine whether established universal-factory terminology conflicts with an unqualified claim about computational acquisition of family-specific production knowledge."
type: kb/sources/types/ingest-report.md
domains: [software-factories, software-configuration, cross-development, product-families]
---

# Ingest: A Top Down Approach to Structured Software Design for MARA

## Classification

This is an industry engineering report presented as a conference paper. Its evidence is a five-year project account and architecture description, not a controlled evaluation. Author: A. Di Giovanni and L. Padella worked at Selenia, the company that developed the MARA airborne-computer line, giving them direct design knowledge and an interest in presenting the project favorably.

## Summary

The paper describes MARA as a modular hardware and software architecture for real-time airborne systems. It separates functional design from physical allocation, represents applications as functions and tasks, and uses paths, operating-system services, and a System Configuration Language to map parameterized software descriptions and already compiled modules onto a selected processor configuration. The surrounding software factory is the lifecycle environment of methods, languages, compilers, assemblers, linkers, configuration tools, and remote debugging facilities. The authors call it universal because the environment can serve different microprocessor families; they do not describe it as generating or redesigning the family-specific production machinery itself.

## Quotes

- **Source extract (verbatim):** The definition of a system with SCL is articulated in two parts: a part, Called "descriptor", which contains a general description of the programs which realize the system, expressed in a parametric and H/W independent way; a part, called "configurator", able to generate a particular configuration for the system. This means that, to modify the configuration of a certain system, it is sufficient to modify the configurator section of the system description without rewriting any modules. The output of the SCL compiler is interpreted by another tool (running on the S/W factory), which combines the system description (made in SCL) and the user files (previously compiled and assembled) to produce automatically a directly loadable and executable output for the SUAYK-203 or the Eprom fusing tapes.
  - **Source location:** Section 3, “System Software Structure,” PDF page 10

- **Source extract (verbatim):** By Software Factory we mean a set of methods and tools which represent the support to all the necessary functions for the development, maintenance and management of S/W projects in their complete work cycle. The factory used by Selenia for the development of programs for the SUAYK-203 is based on the VAA family computers (fig. 5) and presents the following particular characteristics: It can be considered a universal factory, i.e. may be used for different microprocessor families it is multi-user it is oriented towards the maximum portability it is equipped with a powerful set of instruments at the state of art
  - **Source location:** Section 4, “S/W Factory,” PDF page 10

## Connections Found

This report is a historical terminology counterpoint. Its *universal factory* is portable across target-processor families, whereas [Greenfield and Short's software factory](greenfield-short-software-factories-oopsla-2003.ingest.md) is production machinery specialized to one product family and their separate factory-building example recursively constructs more factories. [Program synthesis](program-synthesis-gulwani-polozov-singh-2017.ingest.md) supplies the complementary boundary: construction proceeds within supplied specifications, program spaces, and domain knowledge. The MARA configurator likewise generates a target system inside a human-designed language, architecture, component set, and toolchain, which compares with [the effective-update-space limit of a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

## Extractable Value

1. **Reserve “universal” for a named axis.** In this source, universality means one development environment can target different microprocessor families. Bare *universal factory* therefore collides with an established portability usage if it is repurposed to mean acquisition of family-specific production knowledge. [quick-win]
2. **Separate configuration from acquisition of production knowledge.** SCL combines a human-supplied descriptor, configurator, and compiled files to produce a loadable target image. It varies deployment within a predefined architecture; it does not acquire or construct the language, component family, or production method that makes the configuration possible. [quick-win]
3. **Do not let recursive factory production subsume the acquisition boundary.** Greenfield and Short's later factory-building example concerns production of further factory assets, but still assigns their design to human product-line developers. Factory-valued output therefore remains distinct from computational acquisition of the target family's production knowledge. [deep-dive]
4. **Distinguish independent questions hidden by factory terminology.** A useful taxonomy asks whether a factory spans target hardware, can produce further factory machinery, can realize a factory from a supplied description, and can acquire the production knowledge required by new demands. These properties can vary independently. [deep-dive]
5. **Use the paper as lexical and architectural evidence, not an impossibility result.** It demonstrates a concrete historical meaning and exposes which production choices remain external to configuration, but it does not show that broader computational acquisition is impossible. [just-a-reference]

## Limitations (our opinion)

The authors report on their own industrial system and assert that its practical results met the stated requirements without publishing comparative measurements, failed attempts, development cost, or independent assessment. The account concerns one military-avionics program and a period-specific VAX-hosted cross-development environment, so its architecture should not be generalized into a universal production model. Its use of *universal factory* is strong evidence that the phrase had a target-portability meaning in this source, but one paper cannot establish that this was the field's dominant or exclusive usage. The extracted full-source text also preserves figures poorly, although the terminology and configuration claims are explicit in the prose.

## Recommended Next Action

Keep unqualified *universal software factory* unregistered. Use [Universal software factory needs a declared universality axis](../notes/universal-software-factory-needs-a-declared-universality-axis.md) to distinguish target-platform portability, factory-valued output, constructional expressivity, and production-knowledge acquisition reach.

Abstracted into:

- [Universal software factory needs a declared universality axis](../notes/universal-software-factory-needs-a-declared-universality-axis.md) — uses the report's processor-portability sense to expose the historical collision in unqualified universal-software-factory terminology
- [A software factory can produce another factory without acquiring its family-specific production knowledge](../notes/factory-construction-does-not-establish-knowledge-acquisition.md) — contrasts recursive construction with the production knowledge supplied to the constructor
