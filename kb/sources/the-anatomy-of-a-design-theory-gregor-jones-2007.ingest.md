---
description: "Gregor and Jones's six-core/two-additional anatomy separates design-theory content from implementation agents and physical instantiations"
source_snapshot: "the-anatomy-of-a-design-theory-gregor-jones-2007.md"
ingested: "2026-07-14"
type: kb/sources/types/ingest-report.md
domains: [design-theory, theory-structure, artifact-design, implementation]
---

# Ingest: The Anatomy of a Design Theory

Source: [the-anatomy-of-a-design-theory-gregor-jones-2007.md](./the-anatomy-of-a-design-theory-gregor-jones-2007.md)
Captured: 2026-07-14
From: https://openresearch-repository.anu.edu.au/bitstreams/cb19f834-e47c-44dc-9331-1985afe75336/download

## Classification

Genre: scientific-paper -- a peer-reviewed conceptual research essay that synthesizes prior theory and design-science work into a structural specification for information-systems design theories.
Domains: design-theory, theory-structure, artifact-design, implementation
Authors: Shirley Gregor and David Jones. Gregor originated the five-type taxonomy; together they provide the mature component-level treatment of Type V design theory, extending Walls, Widmeyer, and El Sawy.

## Summary

Gregor and Jones distinguish eight possible components of an information-systems design theory. Six are core: purpose and scope, constructs, principles of form and function, artifact mutability, testable propositions, and justificatory knowledge. Two are additional: principles of implementation and an expository instantiation. The first six suffice to specify the idea of an artifact that could be constructed; implementation guidance and a physical example may follow and can strengthen communication or credibility. The paper also distinguishes abstract theory, material instantiation, and human understanding, and locates IS artifacts in human-machine systems. Agents and actions enter explicitly in the implementation process, but a present, capable operator is not a core component of the theory itself.

## Connections Found

The paper supplies the component anatomy needed to revise [Actionable theories and reflexive system construction](../notes/actionable-theories-and-reflexive-system-construction.md), especially by preventing four conflations: design principles with implementation principles, anticipated artifact mutability with an authorized write path, abstract theory with a physical instantiation, and human participation inside the target system with the external operator who applies the theory. It complements [Gregor 2006](./the-nature-of-theory-in-information-systems-gregor-2006.md), which defines Type V by prescriptive purpose, and refines [Gregor 2002](./design-theory-in-information-systems-gregor-2002.md), which introduced the product/process distinction without this complete anatomy. Broader local work on readable artifacts and design rationale is adjacent but does not directly depend on the ISDT component scheme.

## Extractable Value

1. **Six core components define a constructible design idea without requiring implementation.** This is the clearest source constraint on any claim that a theory needs a current operator before it counts as design-and-action theory. [quick-win]
2. **Implementation principles are distinct and additional.** They describe context-specific processes by which agents and actions bring the design into being; they are not identical to the abstract principles of form and function. [quick-win]
3. **Artifact mutability has a precise inherited meaning.** It is the range of state, form, adaptation, or evolution changes anticipated by the theory—not permission for an interpreter to modify an artifact. [quick-win]
4. **The system boundary is both scoped and sociotechnical.** Purpose/scope identifies a whole class of artifacts and their operating environment, while IS theory can include the human-technology interaction that generates the relevant phenomena. [just-a-reference]
5. **Justificatory knowledge is a causal linking mechanism.** It links goals, shape, processes, and materials and explains why the artifact is constructed as it is and why it works, even when the explanation is incomplete. [deep-dive]
6. **An instantiation can represent and test theory without becoming the theory.** An implementation may communicate design principles and expose problems, but an artifact by itself remains craft knowledge if the principles are not abstracted and articulated. [just-a-reference]

## Inherited Vocabulary

### Exact terminology and definitions

- **“Information Systems Design Theory” / “ISDT.”** A theory showing principles inherent in the design of an IS artifact that accomplishes an end, based on knowledge of information technology and human behavior; it permits guidelines for further artifacts of the same type. Its object can be a product or a method, and it can concern both design form and implementation intervention (printed pp. 25–26; PDF pp. 25–26).
- **“Purpose and scope” (causa finalis).** What the system is for: the meta-requirements or goals specifying the artifact type, together defining the theory's scope or boundaries (printed p. 27; PDF p. 27).
- **“Constructs” (causa materialis).** Representations of the entities of interest in the theory (printed p. 27; PDF p. 27).
- **“Principles of form and function” (causa formalis).** The abstract blueprint or architecture describing an IS artifact, whether product or method/intervention (printed p. 27; PDF p. 27).
- **“Artifact mutability.”** Changes in artifact state anticipated by the theory—the degree of change the theory encompasses (printed p. 27; PDF p. 27). The elaboration includes changes to basic form, adaptation, and evolution, not merely transitions among fixed states (printed pp. 35–36; PDF pp. 35–36).
- **“Testable propositions.”** Truth statements about the design theory (printed p. 27; PDF p. 27), commonly of the form that instantiating the stated principles will work or outperform an alternative in some respect (printed p. 37; PDF p. 37).
- **“Justificatory knowledge.”** Underlying natural-, social-, or design-science knowledge that supplies a basis and explanation for the design; earlier literature calls these kernel or micro theories (printed pp. 27, 38; PDF pp. 27, 38).
- **“Principles of implementation” (causa efficiens).** Processes for implementing the theory in specific contexts (printed p. 27; PDF p. 27); the elaboration calls this the means by which the design is brought into being through agents and actions (printed pp. 41–42; PDF pp. 41–42).
- **“Expository instantiation.”** A physical implementation used to represent the theory and assist with testing (printed p. 27; PDF p. 27).

### Necessary conditions versus illustrative features

- **Core/minimum specification:** the authors say any design theory should include purpose/scope, constructs, form/function principles, artifact mutability, testable propositions, and justificatory knowledge (printed pp. 26–27; PDF pp. 26–27). The first six are sufficient to specify the idea of a constructible artifact (printed p. 28; PDF p. 28).
- **Additional rather than core:** principles of implementation and an expository instantiation. Specific construction methods and proof-of-concept can arrive later; an instantiation generally enhances credibility but innovative conceptual work may have merit without one (printed pp. 27–28; PDF pp. 27–28).
- **Maturity qualification:** the conclusion expects all eight to appear in some form in a full, well-developed theory, while early-stage theory may contain a subset (printed p. 46; PDF p. 46). This is a development-quality expectation, not a retraction of the core/additional distinction.
- **Incomplete justification is allowed:** justificatory knowledge remains essential in the authors' view, but it may be incomplete and may derive from natural/social science, other design theory, practitioner theory-in-use, prior practice, or evidence (printed pp. 38–41; PDF pp. 38–41).
- **Illustrations, not necessary features:** relational databases, fault-threshold policy, risk-management process, DSS architecture, prototyping steps, screen mock-ups, and particular implementations exemplify components but do not define them.
- **Not a core requirement:** an available operator, a specific agent class, actual execution, implementation authority, success, self-application, reflection, or reflexivity. Agents/actions occur within the additional implementation component; the core anatomy can exist before the implementation process (printed pp. 28, 41–42; PDF pp. 28, 41–42).

### Assumed system boundary and people

The paper locates IS in **human-machine systems**, explicitly studying phenomena that emerge when technological and social systems interact rather than either system alone (printed p. 4; PDF p. 4). People can therefore be components or participants within an IS artifact's relevant boundary: users interact with DSS components, many people access a database, organizations adapt methods, and human cognition can constrain design (printed pp. 32, 35–36, 38–41; PDF same pages). The boundary is not all of society by default. Purpose and scope specify the operating environment, meta-requirements, artifact class, excluded goals, and range of generalization (printed pp. 31–32; PDF pp. 31–32). A designer or implementation agent may be outside the product boundary but inside a broader intervention or method boundary; the paper allows both product and process artifacts rather than fixing one placement (printed pp. 22, 25–26; PDF same pages).

### Causal connections

- **Humans ↔ theory ↔ instantiation:** human beings create abstract theories and constructs, use them to guide physical instantiations, understand artifacts in use, and can extract design principles by observing and inferring from existing instantiations (printed p. 25; PDF p. 25).
- **Justificatory knowledge → connected design:** justification links goals, form, process, and material capabilities and explains why an artifact has its structure and why it works; stronger knowledge gives designers a basis for adapting guidance to circumstances (printed pp. 38–41; PDF pp. 38–41).
- **Form/process propositions → outcomes:** product propositions test whether architectural principles satisfy meta-requirements; process propositions test whether implementation principles yield an artifact consistent with the architecture (printed p. 37; PDF p. 37).
- **Implementation agents/actions → instantiation:** principles of implementation specify the process by which agents act to bring the design into being in a concrete context (printed pp. 41–43; PDF pp. 41–43).
- **Artifact ↔ context over time:** mutable IS artifacts emerge, evolve, and become interdependent with socioeconomic contexts and practices; feedback can support refinement and adaptation (printed pp. 35–36; PDF pp. 35–36).
- **Component → component interaction:** design decomposition permits partial independence because components primarily affect one another through function rather than hidden mechanism, although higher-level constructs can themselves contain sub-systems with separate design theories (printed pp. 33–34; PDF pp. 33–34).

### Distinctions that should constrain later Commonplace notes

- Preserve **Type V membership** (from Gregor 2006) separately from this paper's **internal anatomy**. The 2007 paper elaborates what design theory may contain; it does not introduce *actionable theory* as a new type.
- Separate **principles of form and function** from **principles of implementation**. A theory can specify the artifact architecture without yet supplying the concrete process or agent that realizes it.
- Separate **artifact mutability** from **write capability/authority**. The former is anticipated change within scope; the latter belongs to a theory–operator–target relation not defined here.
- Separate **abstract theory**, **physical instantiation**, and **human understanding**. Neither executable code nor a working system is automatically the articulated theory.
- Distinguish **people inside the modeled sociotechnical system** from **agents applying the theory**. A boundary may include either or both, but their roles should be stated.
- Keep **meta-requirements for a class** distinct from requirements for one local instance. The theory's generality can be heuristic and context-bounded, but it must reach beyond a single build (printed pp. 32, 37–38; PDF same pages).
- On subtype/state/relation: this source strengthens the earlier result. The **design-and-action class is a subtype**; its anatomy can include implementation guidance; **actionability under an operator condition remains a relational property**, and actual construction is an operational event. The eight components do not justify classifying operator availability as a ninth theory component.
- Nothing in the anatomy establishes causally connected self-representation or an observer observing itself. Do not use its mentions of post-design reflection (printed p. 41; PDF p. 41) or mutable artifacts as evidence that Commonplace is reflective or reflexive.

## Limitations (our opinion)

Editorial opinion. The proposed anatomy is a conceptual synthesis assessed against only a small set of exemplar papers; the authors explicitly call for broader testing. Their assertion that six components are essential sits in some tension with the later allowance that early theory can contain only a subset, and the line between a theory component and supporting report content can be hard to apply. The human-machine scope is specific to information systems and should not be generalized wholesale to every designed system. Finally, the paper analyzes the representation and structure of design knowledge, not the real-world readiness of a particular theory/operator pair and not computational reflection. It cannot determine whether Commonplace is reflective or reflexive.

## Recommended Next Action

When revising `kb/notes/actionable-theories-and-reflexive-system-construction.md`, add a compact anatomy subsection that uses the six-core/two-additional distinction to separate design prescription from operator-dependent realization, and cite this snapshot as the source.
