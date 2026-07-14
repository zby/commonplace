---
description: "Definition — a reflective system has an aspect-bounded, causally connected self-representation available to processes inside a declared system boundary"
type: kb/types/definition.md
tags: [foundations, computational-model]
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

## Exclusions

Reflection is not autonomy, successful self-improvement, formal verification, or closure under a set of recommendations. Nor is it **organizational closure**, the recursive regeneration of a network of component interactions, or **autopoiesis**, the narrower self-production of a living system ([Varela 1981, printed pp. 14–18; PDF pp. 1–5](../../sources/varela-autonomy-and-autopoiesis-1981.ingest.md)).

## Misuse Cases

- Calling documentation reflective because it describes the software that stores it, without showing a causal path into later operation.
- Expanding the boundary after a failure so that any helpful outsider counts as an internal reflective component.
- Calling a telemetry-driven controller reflective when its signal is not available inside the declared boundary as a representation of that same system.
- Using **reflexive** and **reflective** interchangeably without identifying a distinct property that the new term would name.

---

Relevant Notes:

- [Actionable theory](./actionable-theory.md) — grounds: an internal process may act through theory, but actionability alone does not establish reflection
- [Behavioral authority](./behavioral-authority.md) — enables: names the consumer, channel, and force that make a self-representation operative
- [Cross-representational reflection](../cross-representational-reflection.md) — extends: asks how aspect-bounded reflection covers systems whose behavior spans heterogeneous representations and their mappings
- [A methodology is agent-extensible only where it is closed under its own recommendations](../methodology-agent-extensible-only-with-closure-under-recommendations.md) — contrasts: closure under recommendations is a stronger self-extension property than reflection
- [Smith, Reflection and Semantics in Lisp](../../sources/smith-reflection-and-semantics-in-lisp-1984.ingest.md) — derived-from: supplies the earlier embedded-self-theory and bidirectional-causality lineage
- [Maes, Computational Reflection](../../sources/maes-computational-reflection-1988.ingest.md) — derived-from: supplies causal connection, self-representation, and theory-relativity
- [Wuyts and Ducasse, Symbiotic Reflection](../../sources/wuyts-ducasse-2001-symbiotic-reflection.ingest.md) — evidence: corroborates the causal self-representation threshold and the introspection/intercession distinction
- [von Foerster, Cybernetics of Cybernetics](../../sources/von-foerster-cybernetics-of-cybernetics-1979.ingest.md) — derived-from: supports observer-inclusive boundaries without replacing the computational criteria
