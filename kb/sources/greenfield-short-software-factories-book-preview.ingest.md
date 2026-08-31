---
description: "A partial publisher preview frames Software Factories as domain-specific application-production machinery but cannot support the book's detailed ontology."
source: https://books.google.com/books/about/Software_Factories.html?id=06dQAAAAMAAJ
captured: "2026-08-31"
capture: trafilatura
capture_scope: partial-source
genre: book-preview
snapshot_sha256: f399cd1603a4940b4900312d7013e046b7733f6a545e2cdef9a3a031da9b45ca
ingested: "2026-08-31"
occasion: "Investigate the original 2004 Software Factories book without treating a partial Google Books preview as full-text evidence for the ontology."
type: kb/sources/types/ingest-report.md
domains: [software-factories, domain-specific-languages, software-development-automation]
---

# Ingest: Software Factories book preview

## Classification

The retained source is a Google Books preview consisting of bibliographic data, promotional publisher copy, and three visible contents entries, so `book-preview` captures its evidential form more accurately than a conceptual essay or practitioner report. Author: Jack Greenfield and Keith Short are identified as Microsoft Enterprise Frameworks and Tools architects and as architects of the Software Factories method; Steve Cook and Stuart Kent are named as contributors of two chapters on domain-specific language development. This is a relevant expertise signal, while the available prose remains publisher framing rather than chapter text.

## Summary

The preview presents Software Factories as a method for making application development cheaper, faster, and more reliable through greater automation. Its public framing combines domain-specific visual languages and XML source artifacts with patterns, frameworks, model transformation, code generation, product lines, components, aspects, and service technologies, then applies those reusable assets to assembling applications in specific problem domains. It identifies the authors, contributors, publication date, and broad book program, but a reader seeking the method's precise ontology, supporting argument, worked example, or evidence for claimed outcomes must consult the complete book or fuller primary sources.

## Quotes

No source quotes have been retained yet.

## Connections Found

The preview's role is a bibliographic anchor and public-framing source, not the technical basis for a detailed ontology. It provides limited evidence for the broad integration claim in [A software factory is family-scoped lifecycle production machinery](../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md), while the registered [Software factory](../notes/definitions/software-factory.md) definition supplies the precise family-specific boundary that the publisher copy lacks. [Greenfield and Short's 2003 software-factory paper](greenfield-short-software-factories-oopsla-2003.ingest.md) is the stronger comparison for the method's technical account, and [Cook and Kent's Tool Factory proposal](cook-kent-tool-factory-2003.ingest.md) exposes the chapter-5-derived language-tooling mechanism behind the preview's contributor credit and high-level discussion of domain-specific languages.

## Extractable Value

1. **A bounded record of the original book** -- The preview pins the 2004 title, authors, contributor credits, and public scope without letting a partial capture stand in for the book's argument. [just-a-reference]
2. **An integrated production-machinery framing** -- The publisher description places domain-specific languages, XML, patterns, frameworks, transformations, code generation, and reusable assets in one application-assembly method, providing narrow support for the KB's broad synthesis while leaving its detailed ontology to fuller sources. [quick-win]
3. **Models presented as production inputs** -- The preview contrasts general-purpose UML models used as documentation with tuned DSL and XML models used as source artifacts for transformation and generation; this sharpens a potentially useful distinction, but the complete treatment requires the book. [deep-dive]
4. **A contributor bridge to Tool Factory** -- Naming Cook and Kent as authors of two DSL chapters helps locate their chapter-5-derived Tool Factory proposal within the book's program and narrows where a full-text follow-up should begin. [just-a-reference]
5. **A historical boundary for terminology comparisons** -- The preview associates *software factory* with reusable, domain-specific production assets and application assembly, providing a bounded counterpoint to current uses of the term for agent orchestration systems. [quick-win]

## Limitations (our opinion)

The captured page is partial: it contains metadata, publisher promotional copy, three visible contents entries, and an indication that 19 other sections are not shown. That boundary prevents this ingest from establishing the book's detailed ontology, chapter arguments, examples, citations, implementation mechanics, or the relationship among all of its enabling technologies. Claims of lower cost, greater speed and reliability, broad organizational applicability, and inevitable replacement of existing methods are promotional assertions rather than demonstrated outcomes in the captured material. The authors' relevant institutional roles strengthen the expertise signal but do not remove the publisher's interest in an expansive framing.

## Recommended Next Action

Create a distinct full-source ingest from a lawfully obtained complete copy of the 2004 book before using the book to revise the software-factory definition or ontology synthesis.
