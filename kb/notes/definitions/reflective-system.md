---
description: "Definition — a reflective system has an aspect-bounded, causally connected self-representation available to processes inside a declared system boundary"
type: kb/types/definition.md
tags: [foundations, computational-model, self-improving-systems]
---

# Reflective system

A **reflective system** contains a causally connected representation of itself that is available to its own processes, such that operations mediated through that representation can affect the system's subsequent behavior.

The structural core is the established term in computational reflection: a system that reasons about itself in a causally connected way, through structures that represent selected aspects of it — its **self-representation**. Commonplace applies the criteria relative to an explicitly declared boundary without prescribing whether human actors are included. Departures from the source literature are recorded under [Provenance](#provenance-and-departures).

Changing the boundary alone does not satisfy the definition. The representation must be available inside the boundary *as a representation of that same system*, not merely as telemetry or a control signal correlated with its state.

## Scope

Calling a system reflective requires five things to be stated:

- The **system boundary**—what processes, artifacts, and environment count as the system;
- The **represented aspects** of that system and their granularity;
- A **self-representation** that exposes those aspects;
- Processes inside the boundary that can inspect or act through the representation; and
- The **causal connection** by which changes in the represented aspects update the self-representation and representation-mediated operations affect later system behavior.

Reflection is therefore aspect-bound, not global. The terminology and granularity of the self-representation determine which questions and interventions the system can formulate about itself — Maes's theory-relativity point. No self-representation exhausts every possible aspect, although it may be complete relative to its declared set of represented aspects. A reflective architecture may also retain an unrepresented or unmodifiable kernel.

The following neighboring terms mark different capabilities:

| Term | Criterion |
|---|---|
| **Self-description** | Information about the system is present, but need not affect operation. |
| **Introspection** | A process can inspect or reason about represented system state. |
| **Reflection** | The self-representation is causally connected to the represented system and participates in later operation. |
| **Intercession** | Reflective access permits direct modification of represented system state or interpretation. |

Intercession is a capability within reflection, but not every reflective architecture permits it.

No artifact authority family is required. A representation consumed as evidence or advice can mediate reflective change when it participates in the causal path into the represented organization; a nominal [system-definition artifact](./system-definition-artifact.md) that is not a self-representation cannot. The criterion is causal connection through a representation of the affected aspect, made precise by the consumer, channel, and force in [behavioral authority](./behavioral-authority.md).

## Retrieval-mediated causal connection

The causal connection need not be an interpreter or a compiler. Where the self-representation is a body of retained artifacts, it can run through **discovery**: a process searches the artifacts, finds the ones bearing on what it is doing, and derives its behavior from what it found. Retrieval is then the wire the representation acts along, and it is best-effort where a compiler is exhaustive — so [retrieval failure is reflection failure](../retrieval-failure-is-reflection-failure.md), which develops what that costs and how the wire is strengthened.

## Exclusions

Reflection is not autonomy, successful self-improvement, formal verification, or closure under a set of recommendations. Nor is it **organizational closure**, the recursive regeneration of a network of component interactions, or **autopoiesis**, the narrower self-production of a living system ([Varela 1981, printed pp. 14–18; PDF pp. 1–5](../../sources/varela-autonomy-and-autopoiesis-1981.ingest.md)).

Reflection is also not **adaptation**, and this is the misreading the term invites most. Both directions have occupants.

*Reflection and intercession without adaptation.* A Smalltalk image is the case to hold in mind. Classes are objects; methods can be added at runtime, superclasses changed, message dispatch intercepted, the compiler edited with the compiler. Implementation and self-representation are one structure, so the causal connection is as tight as it gets and intercession is total. Left alone, the image sits there for a decade and improves nothing — nothing in it notices that a method is slow, decides the change is worth making, or judges whether the rewrite helped. **The programmer supplies the evidence-responsiveness.** Remove the programmer and the improvement pathway is not weakened; it is absent. A reflective architecture permitting intercession supplies a causal path by which a system *could* change itself. It does not make any change responsive to evidence about an improvement objective — neither directly, nor through the search, evaluation, and operative retention that [a proposal-selection improvement loop requires](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

*Adaptation without reflection.* Conversely, a system can improve itself with no self-representation at all. Ashby's Homeostat jogs its parameters to random values whenever its essential variables leave viable limits, holds the configuration that restores them, and so adapts — viability-driven, evidence-responsive change to its own organization ([Ashby 1960, chapters 7–8](../../sources/ashby-design-for-a-brain-ultrastability.md)). It is still not reflective, because nothing in it *represents* that organization. What it retains is a setting rather than a map, and [what that costs is addressability](../reflection-buys-addressability.md).

The two properties are orthogonal: reflection is structural, adaptation is a process, and each is available without the other. [Self-improving-system membership](./self-improving-system.md) is defined separately; this note owns only whether a named pathway routes change through a self-representation.

## Misuse Cases

- Calling documentation reflective because it describes the software that stores it, without showing a causal path into later operation.
- Expanding the boundary after a failure so that any helpful outsider counts as an internal reflective component.
- Calling a telemetry-driven controller reflective when its signal is not available inside the declared boundary as a representation of that same system.
- Using **reflexive** and **reflective** interchangeably without identifying a distinct property that the new term would name.

## Provenance and departures

The criteria above are inherited; the extensions are not. Collected here so the definition can be read as a definition, and so each departure is auditable in one place.

- **Causal connection, self-representation, theory-relativity — inherited.** Maes defines a reflective system as a computational system that reasons about itself “in a causally connected way,” and names the structures representing selected aspects its self-representation ([Maes 1988, printed pp. 1–2, 14–17; PDF pp. 1–2, 14–17](../../sources/maes-computational-reflection-1988.ingest.md)). The introspection/intercession split is corroborated in [Wuyts and Ducasse 2001](../../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md); the embedded-self-theory lineage is [Smith 1984](../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md).
- **Retrieval as a causal connection — Commonplace's own.** No source treats discovery over retained artifacts as the wire. See [retrieval failure is reflection failure](../retrieval-failure-is-reflection-failure.md).
- **Terminology reservation.** Commonplace retains **reflective system** across boundary choices and reserves **reflexive system** for a future concept only if it names a distinct property. Nothing currently requires the second term.

---

Relevant Notes:

- [Actionable methodology](./actionable-methodology.md) — grounds: an internal process may act through a methodology, but actionability alone does not establish reflection
- [Behavioral authority](./behavioral-authority.md) — enables: names the consumer, channel, and force that make a self-representation operative
- [Retrieval failure is reflection failure](../retrieval-failure-is-reflection-failure.md) — extends: develops the retrieval-mediated causal connection, and the best-effort weakness that comes with it
- [Reach-assessment](./reach-assessment.md) — contrasts: the semantic judgment capability reflectivity's structural requirements do not entail
- [Reflective coverage is graded across representational forms](../reflective-coverage-is-graded-across-representational-forms.md) — extends: when behavior spans heterogeneous forms, coverage must be claimed per form and operation profile
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — extends: reflection supplies one causal path into the loop, but not the search, evaluation, or operative retention the loop needs
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — contrasts: closure under recommendations is a stronger self-extension property than reflection
- [Smith, Reflection and Semantics in Lisp](../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) — derived-from: supplies the earlier embedded-self-theory and bidirectional-causality lineage
- [Maes, Computational Reflection](../../sources/maes-computational-reflection-1988.ingest.md) — derived-from: supplies causal connection, self-representation, and theory-relativity
- [Wuyts and Ducasse, Symbiotic Reflection](../../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md) — evidence: corroborates the causal self-representation threshold and the introspection/intercession distinction
- [Ashby, Design for a Brain — ultrastability](../../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: a negative case — an adaptive, self-modifying system that is not reflective, having no self-representation
