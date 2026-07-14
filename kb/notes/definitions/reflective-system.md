---
description: "Definition — a reflective system has an aspect-bounded, causally connected self-representation available to processes inside a declared system boundary"
type: kb/types/definition.md
tags: [foundations, computational-model, reflective-systems]
---

# Reflective system

A **reflective system** contains a causally connected representation of itself that is available to its own processes, such that operations mediated through that representation can affect the system's subsequent behavior.

This definition takes its structural core from the established term in computational reflection. Maes defines a reflective system as a computational system that reasons about itself “in a causally connected way” and calls the structures that represent selected aspects of the system its **self-representation** ([Maes 1988, printed pp. 1–2; PDF pp. 1–2](../../sources/maes-computational-reflection-1988.ingest.md)). The Commonplace knowledge-base framework generalizes these criteria to an explicitly declared computational or socio-technical boundary; Maes does not directly ground the human-inclusive extension.

Changing the boundary alone does not satisfy the definition. The representation must be available inside the boundary *as a representation of that same system*, not merely as telemetry or a control signal correlated with its state. Commonplace therefore retains **reflective system** across boundary choices and reserves **reflexive system** for a future concept only if it names a distinct property.

## Scope

Calling a system reflective requires five things to be stated:

- The **system boundary**—what processes, artifacts, people, and environment count as the system;
- The **represented aspects** of that system and their granularity;
- A **self-representation** that exposes those aspects;
- Processes inside the boundary that can inspect or act through the representation; and
- The **causal connection** by which changes in the represented aspects update the self-representation and representation-mediated operations affect later system behavior.

Reflection is therefore aspect-bound, not global. Maes's theory-relativity point is decisive: the terminology and granularity of the self-representation determine which questions and interventions the system can formulate about itself ([printed pp. 14–17; PDF pp. 14–17](../../sources/maes-computational-reflection-1988.ingest.md)). No self-representation exhausts every possible aspect, although it may be complete relative to its declared set of represented aspects. A reflective architecture may also retain an unrepresented or unmodifiable kernel.

The following neighboring terms mark different capabilities:

| Term | Criterion |
|---|---|
| **Self-description** | Information about the system is present, but need not affect operation. |
| **Introspection** | A process can inspect or reason about represented system state. |
| **Reflection** | The self-representation is causally connected to the represented system and participates in later operation. |
| **Intercession** | Reflective access permits direct modification of represented system state or interpretation. |

Intercession is a capability within reflection, but not every reflective architecture permits it.

## Human-inclusive boundaries

People may be components of a reflective system when the declared boundary includes an established role whose interpretation, authorization, or action forms part of the causal path. A standing human review role can therefore participate inside a socio-technical reflective system. By contrast, a person who occasionally rescues a failed process from outside its established operation does not become an internal component merely because the rescue affected it.

Under Commonplace's extension, a monitored service, dashboard, and operator role qualify only when the dashboard functions within the declared whole as a representation of that same whole. A display used merely as telemetry in an external control loop does not qualify. Second-order cybernetics supports including an observer and the observer's purposes in the analyzed boundary, but observer inclusion alone supplies neither a self-representation nor a causal-connection test ([von Foerster 1979, PDF pp. 2–3](../../sources/von-foerster-cybernetics-of-cybernetics-1979.ingest.md)).

The extension is permissive by consequence: with a standing maintainer role inside the boundary, nearly every maintained system classifies as reflective, so the bare classification is a qualification rather than a discrimination — [human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient](../human-inclusive-boundaries-make-reflection-cheap.md).

## Retrieval-mediated causal connection

The causal connection need not be an interpreter or a compiler. Where the self-representation is a body of retained artifacts, the connection can run through **discovery**: a process searches the artifacts, finds the ones bearing on the change it is making, and derives its behavior from what it found. Editing an artifact then reaches later behavior without anyone deciding to re-derive, provided the retrieval procedure surfaces it.

This puts retrieval inside the reflective architecture rather than alongside it. The search recipes, the fields that make an artifact findable, and the indexes that shortcut the search are the wire along which the self-representation acts, and a represented constraint that no process can find is inert. **Retrieval failure is therefore reflection failure** — the analogue of a compiler silently dropping a declaration, and the reason [stale indexes are worse than no indexes](../stale-indexes-are-worse-than-no-indexes.md): a membership claim that tells an exhaustive consumer to stop looking, while members are missing, cuts the wire precisely where it is trusted.

Retrieval-mediated connection is weaker than procedural reflection in one specific way: it is best-effort. A compiler propagates every change to a representation it consumes; a search propagates the changes it happens to surface. Such a system can strengthen the wire — enforcing a membership claim rather than asserting it, or correcting a search recipe observed to miss a member — but it cannot assume the wire holds by construction.

## Exclusions

Reflection is not autonomy, successful self-improvement, formal verification, or closure under a set of recommendations. Nor is it **organizational closure**, the recursive regeneration of a network of component interactions, or **autopoiesis**, the narrower self-production of a living system ([Varela 1981, printed pp. 14–18; PDF pp. 1–5](../../sources/varela-autonomy-and-autopoiesis-1981.ingest.md)).

Reflection is also not **adaptation**, in either direction. A reflective architecture permitting intercession supplies a causal path by which a system could change itself; it does not supply the search, evaluation, and operative retention that [governed adaptation requires](../governed-adaptation-requires-search-evaluation-and-retention.md). Conversely, a system can run that loop with no self-representation at all — Ashby's Homeostat adapts by varying parameters against a viability test ([Ashby 1960, chapters 7–8](../../sources/ashby-design-for-a-brain-ultrastability.md)). The two properties are orthogonal: reflection is structural, adaptation is a process, and each is available without the other.

## Misuse Cases

- Calling documentation reflective because it describes the software that stores it, without showing a causal path into later operation.
- Expanding the boundary after a failure so that any helpful outsider counts as an internal reflective component.
- Calling a telemetry-driven controller reflective when its signal is not available inside the declared boundary as a representation of that same system.
- Using **reflexive** and **reflective** interchangeably without identifying a distinct property that the new term would name.

---

Relevant Notes:

- [Actionable theory](./actionable-theory.md) — grounds: an internal process may act through theory, but actionability alone does not establish reflection
- [Behavioral authority](./behavioral-authority.md) — enables: names the consumer, channel, and force that make a self-representation operative
- [Reflective coverage is graded across representational forms](../reflective-coverage-is-graded-across-representational-forms.md) — extends: when behavior spans heterogeneous forms, coverage must be claimed per form and operation depth
- [Governed adaptation requires search, evaluation, and operative retention](../governed-adaptation-requires-search-evaluation-and-retention.md) — extends: reflection supplies one causal path into the loop, but not the search, evaluation, or operative retention the loop needs
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — contrasts: closure under recommendations is a stronger self-extension property than reflection
- [Smith, Reflection and Semantics in Lisp](../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) — derived-from: supplies the earlier embedded-self-theory and bidirectional-causality lineage
- [Maes, Computational Reflection](../../sources/maes-computational-reflection-1988.ingest.md) — derived-from: supplies causal connection, self-representation, and theory-relativity
- [Wuyts and Ducasse, Symbiotic Reflection](../../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md) — evidence: corroborates the causal self-representation threshold and the introspection/intercession distinction
- [von Foerster, Cybernetics of Cybernetics](../../sources/von-foerster-cybernetics-of-cybernetics-1979.ingest.md) — derived-from: supports observer-inclusive boundaries without replacing the computational criteria
- [Ashby, Design for a Brain — ultrastability](../../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: a negative case — an adaptive, self-modifying system that is not reflective, having no self-representation
