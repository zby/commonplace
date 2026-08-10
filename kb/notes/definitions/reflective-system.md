---
description: "Definition — a system is reflective relative to selected aspects when an internal process uses a causally connected self-representation of them in its operation"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Reflective system

A **reflective system** has at least one operational path in which an internal process can use a causally connected representation of selected aspects of that same system. Changes in those aspects can update the representation, and operations mediated through it can affect the system's later behavior.

**Computational reflection** is an established concept in computer science. Commonplace inherits its core ideas—self-representation, causal connection, and aspect-relative description—and assesses them relative to a declared system boundary, which may include human actors, and a named operational path.

## Scope

Assess a claim of reflection relative to five elements:

- The **system boundary**: the processes, artifacts, and environment that count as the system;
- The **represented aspects** of that system and their granularity;
- A **self-representation** of those aspects;
- A process inside the boundary that can use the representation in its operation; and
- The **causal connection** in both directions: changes in the represented aspects update the representation, and representation-mediated operations affect later system behavior.

Reflection is an architectural capacity. The path need not have been exercised, but the system must contain the representation, process, and two-way causal relation. Merely declaring a boundary or naming a representation is not enough. A system is reflective with respect to the named aspects when it contains such a path. The unqualified label *reflective system* is shorthand, not a claim that every part of the system is represented or revisable.

The terminology and granularity of the self-representation determine which questions and interventions an internal process can formulate—Maes's theory-relativity point. Completeness can therefore be claimed only relative to the declared aspects; other aspects and an unrepresented or unmodifiable kernel may remain outside the representation.

The following neighboring terms mark different capabilities:

| Term | Criterion |
|---|---|
| **Self-description** | Information about the system is present, but need not affect operation. |
| **Introspection** | A process can inspect or reason about represented system state. |
| **Reflection** | The self-representation is causally connected to the represented system and participates in later operation. |
| **Intercession** | Reflective access permits direct modification of represented system state or interpretation. |

Intercession is a capability within reflection, but not every reflective architecture permits it.

The definition requires neither a particular artifact authority nor a particular execution mechanism. Evidence or advice can mediate reflection only when it represents an aspect of the same system and participates causally in later operation. Conversely, a [system-definition artifact](./system-definition-artifact.md) does not make a path reflective merely because it shapes behavior. [Behavioral authority](./behavioral-authority.md) helps trace the consumer, channel, and force through which a self-representation becomes operative.

## One realization: retrieval-mediated connection

In a retained-artifact system such as Commonplace, the causal connection can run through retrieval. A process discovers relevant parts of the self-representation and lets them shape what it does. Retrieval is neither required for reflection nor sufficient for it: the retrieved representation must actually participate in the causal path. [A retrieval miss is a local reflective-path failure](../a-retrieval-miss-is-a-local-reflective-path-failure.md); it becomes global only when no qualifying causal path remains inside the declared frame.

## Exclusions

Reflection is not autonomy, successful self-improvement, formal verification, or closure under a set of recommendations. Nor is it **organizational closure**, the recursive regeneration of a network of component interactions, or **autopoiesis**, the narrower self-production of a living system ([Varela 1981, printed pp. 14–18; PDF pp. 1–5](../../sources/varela-autonomy-and-autopoiesis-1981.ingest.md)).

Reflection and **adaptation** are orthogonal. Reflection is a structural relation between a system and its self-representation; adaptation is a process that changes the system in response to evidence. Either can occur without the other.

*Reflection without adaptation.* A Smalltalk image exposes classes, methods, dispatch, and even its compiler as live objects that can inspect and modify one another. Taken by itself as the system boundary, the image is reflective and permits intercession, but it has no process that diagnoses a slow method, decides to revise it, or judges the result. A programmer can supply that evidence-responsive process, but including the programmer changes the boundary and the adaptation claim.

*Adaptation without reflection.* Ashby's Homeostat changes its parameters when essential variables leave viable limits and retains a configuration that restores them ([Ashby 1960, chapters 7–8](../../sources/ashby-design-for-a-brain-ultrastability.md)). It adapts without representing its own organization: it retains a setting rather than a map. [What it lacks is addressability](../reflection-buys-addressability.md).

Reflection therefore supplies a possible path for self-directed operation, not an improvement process. [Self-improving-system membership](./self-improving-system.md) is defined separately; proposal-selection paths additionally require [search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md). This note classifies reflective paths, not whether they improve the system.

## Misuse Cases

- Calling documentation reflective because it describes the software that stores it, without showing a causal path into later operation.
- Treating one reflective path as evidence that every behavior-shaping aspect of the system is represented or revisable.
- Expanding the boundary after a failure so that any helpful outsider counts as an internal reflective component.
- Calling a telemetry-driven controller reflective when its signal is not available inside the declared boundary as a representation of that same system.
- Using **reflexive** and **reflective** interchangeably without identifying a distinct property that the new term would name.

## Provenance and departures

The conceptual core is inherited; Commonplace's operational extensions are identified here so that the definition and its departures remain auditable.

- **Causal connection, self-representation, theory-relativity — inherited.** Maes defines a reflective system as a computational system that reasons about itself “in a causally connected way,” and names the structures representing selected aspects its self-representation ([Maes 1988, printed pp. 1–2, 14–17; PDF pp. 1–2, 14–17](../../sources/maes-computational-reflection-1988.ingest.md)). The introspection/intercession split is corroborated in [Wuyts and Ducasse 2001](../../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md); the embedded-self-theory lineage is [Smith 1984](../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md).
- **Explicit boundary- and path-relative attribution — Commonplace's explication.** The definition makes these coordinates part of assessing a reflection claim; it does not attribute this formulation to the cited literature.
- **Retrieval as a causal connection — Commonplace's own.** None of the cited reflection sources treats discovery over retained artifacts as the causal-connection mechanism. See [A retrieval miss is a local reflective-path failure](../a-retrieval-miss-is-a-local-reflective-path-failure.md).
- **Terminology reservation.** Commonplace retains **reflective system** across boundary choices and reserves **reflexive system** for a future concept only if it names a distinct property. Nothing currently requires the second term.

---

Relevant Notes:

- [Actionable methodology](./actionable-methodology.md) — grounds: an internal process may act through a methodology, but actionability alone does not establish reflection
- [Behavioral authority](./behavioral-authority.md) — enables: names the consumer, channel, and force that make a self-representation operative
- [A retrieval miss is a local reflective-path failure](../a-retrieval-miss-is-a-local-reflective-path-failure.md) — extends: develops the path-relative failure mode of a retrieval-mediated causal connection
- [Reach-assessment](./reach-assessment.md) — contrasts: a semantic-judgment capability not entailed by reflection's structural requirements
- [Reflective coverage is graded across representational forms](../reflective-coverage-is-graded-across-representational-forms.md) — extends: when behavior spans heterogeneous forms, coverage must be claimed per form and operation profile
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — extends: reflection supplies one causal path into the loop, but not the search, evaluation, or operative retention the loop needs
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — contrasts: closure under recommendations is a stronger self-extension property than reflection
- [Smith, Reflection and Semantics in Lisp](../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) — derived-from: supplies the earlier embedded-self-theory and bidirectional-causality lineage
- [Maes, Computational Reflection](../../sources/maes-computational-reflection-1988.ingest.md) — derived-from: supplies causal connection, self-representation, and theory-relativity
- [Wuyts and Ducasse, Symbiotic Reflection](../../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md) — evidenced-by: corroborates the causal self-representation threshold and the introspection/intercession distinction
- [Ashby, Design for a Brain — ultrastability](../../sources/ashby-design-for-a-brain-ultrastability.md) — evidenced-by: a negative case — an adaptive, self-modifying system that is not reflective, having no self-representation
