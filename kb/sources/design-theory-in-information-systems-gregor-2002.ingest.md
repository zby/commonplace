---
description: "Gregor's initial Type V account grounds design-and-action theory while separating prescriptive content from Commonplace's proposed operator condition"
source_snapshot: "design-theory-in-information-systems-gregor-2002.md"
ingested: "2026-07-14"
type: kb/sources/types/ingest-report.md
domains: [design-theory, theory-taxonomy, actionable-knowledge, information-systems]
---

# Ingest: Design Theory in Information Systems

Source: [design-theory-in-information-systems-gregor-2002.md](./design-theory-in-information-systems-gregor-2002.md)
Captured: 2026-07-14
From: https://ajis.aaisnet.org/index.php/ajis/article/download/439/399/551

## Classification

Genre: scientific-paper -- a peer-reviewed conceptual research article that proposes and argues for a taxonomy of theory in information systems, then elaborates its fifth type.
Domains: design-theory, theory-taxonomy, actionable-knowledge, information-systems
Author: Shirley Gregor, then at the Australian National University, is the originator of the five-type taxonomy developed more fully in 2006; this paper is the short, direct statement of its design-and-action branch.

## Summary

Gregor classifies information-systems theory by primary purpose into analysis/description, understanding, prediction, explanation-and-prediction, and design-and-action. Type V concerns both development methods/tools and design principles intended to be manifested in an artifact, method, process, or system; its principles must be articulable, general enough to cover a class rather than one consulting case, and stated as normative guidance for practice. In the paper's strongest formulation, design theory is a purpose-distinguished special case of explanatory-and-predictive theory: it retains constructs, explanations, predictions, and testability, then adds prescriptions about how something should be done. The paper locates information systems within human-machine systems, but it does not make the presence of a capable operator part of the theory-type definition.

## Connections Found

The primary connection is [Actionable theories and reflexive system construction](../notes/actionable-theories-and-reflexive-system-construction.md): Gregor grounds its opening intuition that some theory prescribes construction or operation, while showing that the note's interpreter and behavioral-effect conditions are later additions rather than inherited Type V criteria. A secondary connection is [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md): Gregor's taxonomy treats prescription as a possible primary goal of theory, so the local theory and prescription text profiles should not be mistaken for mutually exclusive kinds of knowledge.

## Extractable Value

1. **Type V is a theory subtype selected by primary purpose, not by successful execution.** Its distinguishing purpose is design and action; the 2002 formulation makes it a special case of explanatory-and-predictive theory whose added role is normative guidance. This is the inherited base against which any new use of *actionable theory* must state its extension. [quick-win]
2. **Articulation separates design theory from an artifact or one-off method.** Principles embodied in a method, tool, process, or system must be expressible in natural language, diagrams, or similar representation; the articulation is the theory. This directly constrains claims that working machinery alone constitutes actionable theory. [quick-win]
3. **Generality distinguishes theory from consulting.** Gregor's example supplies principles for a class of systems and permits testing on other instances; applying known principles to one unique task is not by itself a theoretical contribution. This fits the KB's reach-oriented theoretical contract. [just-a-reference]
4. **The paper keeps design knowledge and practical agency distinct.** It requires guidance usable in practice and emphasizes people who act in the world, but it never requires an operator to exist, possess authority, or actually apply the guidance for the artifact to count as Type V theory. That gap is the precise location of the proposed Commonplace extension. [deep-dive]
5. **Design theory spans product and process.** It concerns both what an artifact should be and how it should be built; methods, methodologies, tools, system features, and development activities all fall within its design-and-action scope. [just-a-reference]

## Inherited Vocabulary

### Exact terminology and definitions

- **“Theory for Design and Action” / “Type V.”** It concerns, first, methodologies and tools used to develop information systems and, second, design principles intended to be manifested in an artifact, method, process, or system. The principles must be articulable; that articulation is the design theory (printed p. 17; PDF p. 4).
- **“Design theory.”** Gregor calls it normative or prescriptive because it gives guidelines or principles that can be followed in practice (printed p. 17; PDF p. 4). It covers both development-process knowledge and principles for the artifact's form, with the two intertwined (printed p. 17; PDF p. 4).
- **“Design principles.”** These are design decisions and design knowledge intended for manifestation or encapsulation in an artifact, method, process, or system (printed p. 17; PDF p. 4). In the later elaboration on printed p. 18, a principle is also a proposition with predictive content that can be tested on other systems of the relevant class (PDF p. 5).
- **“Kernel theory.”** In the Walls et al. terminology Gregor reports, this is the theory underlying an information-systems design theory; it may be academic theory or a practitioner's theory-in-use (printed p. 18; PDF p. 5).
- **“Theory.”** The paper deliberately adopts a broad usage, including conjectures, models, frameworks, or bodies of knowledge, but retains abstraction and some generalization as a boundary: facts and the method used in one artifact-construction case are not theory (printed pp. 14–15; PDF pp. 1–2).

### Necessary conditions versus illustrative features

- **Necessary in Gregor's formulation:** some abstraction/generalization beyond an individual case (printed p. 15; PDF p. 2); articulated principles rather than an unexplicated artifact or method (printed p. 17; PDF p. 4); normative or prescriptive guidance for action (printed pp. 17, 19–20; PDF pp. 4, 6–7); and, in the paper's stronger concluding account, well-defined constructs, definitions, propositions, explanation, prediction, and testability inherited from Type IV (printed pp. 18–20; PDF pp. 5–7).
- **Reported from Walls et al. as distinctive structure:** a theoretical base plus explicit practitioner guidance, expressed through user requirements, system features or selection principles, and effective development principles (printed p. 18; PDF p. 5). This is important precedent, but Gregor presents it as one prior specification rather than the paper's own final component checklist.
- **Illustrative or evidential, not definitional:** a proof-of-concept instantiation, action research as a suitable method, success in pilot studies, novelty, utility, significant improvement, and particular evaluation metrics. These support theory building/testing or contribution claims; their absence does not by itself erase the Type V purpose (printed pp. 18–20; PDF pp. 5–7).
- **Not required by this source:** an actually available operator, delegated authority, later behavioral effect, self-application, or successful action. The paper says the knowledge must guide practice and be followable/testable by others, not that use is constitutive of the theory type (printed pp. 19–20; PDF pp. 6–7).

### Assumed system boundary and people

Gregor defines the IS field around the design, delivery, use, and impact of information technology in organizations and society and treats artifacts as parts of **human-machine systems** (printed p. 14; PDF p. 1). People therefore can be components or participants in the target system: the object of inquiry includes both machine properties and human behavior. The design theory itself is an abstract, articulated body of principles, not identical to the target human-machine system or its operators (printed pp. 14–15; PDF pp. 1–2). The relevant boundary for a particular theory is the class of artifacts/problems to which its generalized principles apply; the Markus et al. example is explicitly bounded to systems supporting emergent knowledge processes (printed p. 18; PDF p. 5).

### Causal connections

- A design principle implies a comparative prediction: for the bounded class, following one design or development principle should produce a better result than alternatives in some stated respect; other instances can test that implication (printed p. 18; PDF p. 5).
- Development methods and artifact form are mutually implicated: information-technology artifacts evolve through human action and technological development, and their nature is likely to reflect the tools and methodologies used to construct them (printed p. 17; PDF p. 4).
- Type IV or “kernel” theories can inform design principles, while testing or implementing design principles can refine explanatory, predictive, descriptive, or classificatory theory; Gregor makes these relations bidirectional (printed pp. 18–19; PDF pp. 5–6).
- Practitioner guidance reduces developers' uncertainty by narrowing allowable system features and development activities, thereby increasing the likelihood of success; this is Gregor's report of the Walls et al. mechanism (printed p. 18; PDF p. 5).

### Distinctions that should constrain later Commonplace notes

- Preserve **theory for design and action** as Gregor's purpose-defined subtype and do not silently rename it *actionable theory* as though the latter were her term.
- Separate **prescriptive content** from **operational availability**. The source supplies the former; a requirement for a capable, authorized operator would be a relational extension between a Type V theory, an actor, and a target context.
- Separate **the articulated theory** from its **artifact or instantiation**. Embodiment can demonstrate or test principles, but an artifact whose principles cannot be stated is not the theory in Gregor's account.
- Keep **class-bounded generality** distinct from one-off practical success. Guidance may be local in scope, but it must concern a class and support transfer/testing beyond a single case.
- Do not infer reflection or reflexivity from prescription, implementation, or human participation. This paper classifies theory purposes and says nothing about causally connected self-representation or an observing system.
- On the subtype/state/relation question: **design-and-action theory is a subtype in Gregor's taxonomy**; **being actionable under an added operator requirement is best recorded provisionally as a relational property** of theory, capable interpreter, authority, and context. Actual application would be an operational event or state, not a new Gregor subtype. This is a source-constrained classification of vocabulary, not a claim that Commonplace meets it.

## Limitations (our opinion)

Editorial opinion. This is a short conceptual article, not an empirical test of the taxonomy, and its strongest claim that Type V should retain explanation, prediction, and testable propositions is stricter than some later design-science traditions. It also moves between its own proposed characteristics and prior authors' component schemes, so inherited requirements should be attributed carefully. Most importantly for the current investigation, the paper does not theorize operator competence, authority, execution context, self-representation, or reflection. It can ground design-and-action vocabulary but cannot determine whether Commonplace is reflective or reflexive, and it cannot by itself establish the extra condition that makes prescriptive theory operationally applicable.

## Recommended Next Action

After the required literature ingests are complete, revise `kb/notes/actionable-theories-and-reflexive-system-construction.md` so its opening distinguishes Gregor's Type V subtype from the proposed relational condition of actionability, citing this snapshot for the inherited definition.
