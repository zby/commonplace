---
description: "Primary vocabulary anchor for computational reflection: causally connected self-representation, its representational variants, and its limits"
source_snapshot: "kb/sources/maes-computational-reflection-1988.md"
ingested: "2026-07-14"
type: kb/sources/types/ingest-report.md
domains: [computational-reflection, self-representation, meta-level-architecture]
---

# Ingest: Computational Reflection

Source: [maes-computational-reflection-1988.md](./maes-computational-reflection-1988.md)
Captured: 2026-07-14
From: https://maxapress.com/data/article/ker/preview/pdf/S0269888900004355.pdf

## Classification

Genre: scientific-paper -- a peer-reviewed conceptual synthesis that defines computational reflection, compares language architectures, and derives design consequences from implemented examples rather than reporting a controlled experiment.
Domains: computational-reflection, self-representation, meta-level-architecture
Author: Pattie Maes developed this account from doctoral work on computational reflection and surveys procedural, logic-based, rule-based, and object-oriented architectures; this is the corpus's primary general definition.

## Summary

Maes defines computational reflection for any computational model as the behavior of a computational system that reasons about itself “in a causally connected way.” A reflective system contains a self-representation—structures representing aspects of itself—whose maintained causal connection makes the representation track those aspects and makes the system's status and behavior comply with the representation. The paper then separates procedural from declarative reflection, explains that every reflective architecture is relative to the terminology and granularity of its self-representation, distinguishes implicit from explicit activation, and stresses that reflection is necessarily partial and can reduce external understandability and control (printed pp. 1–2, 8–9, 14–18; PDF pp. 1–2, 8–9, 14–18).

## Connections Found

This source is the primary vocabulary anchor and a necessary constraint on [Actionable theories and reflexive system construction](../notes/actionable-theories-and-reflexive-system-construction.md): that note's self-description, mutable artifact, and behavioral-effect loop must be compared with Maes's stricter causal-connection requirement before its terminology is settled. It also narrows the Lisp precedent in [LLM context is a homoiconic medium](../notes/llm-context-is-a-homoiconic-medium.md): a common program/data format enables the meta-circular route to procedural reflection but is not itself reflection. Maes's theory-relativity and declarative/procedural continuum complement, without collapsing into, Commonplace's broader [representational-form](../notes/definitions/representational-form.md) vocabulary.

## Extractable Value

1. **Causal connection is the threshold, not self-description alone.** A system must reason about itself through a representation connected to the represented aspects so that changes propagate appropriately; a stored account that is merely readable or editable is insufficient (printed pp. 1–2; PDF pp. 1–2). This directly constrains later reflection claims. [deep-dive]
2. **Reflection is relative to the self-theory made available.** The self-representation fixes the terms in which the system can reason about and act on itself, so reflective capability is granular and aspect-bound rather than a global yes/no power (printed pp. 14–17; PDF pp. 14–17). [quick-win]
3. **Procedural and declarative reflection solve causal connection differently.** Procedural reflection uses one representation both to implement and reason about the system; declarative reflection separates explicit constraints from the implicit procedure and therefore needs a translation/consistency mechanism. Maes treats them as a continuum (printed p. 14; PDF p. 14). [deep-dive]
4. **Reflective architecture has two explicit obligations.** The interpreter must give the implemented system access to structures representing aspects of itself and must guarantee their causal connection to those aspects (printed p. 9; PDF p. 9). This is a sharper architecture test than generic self-editability. [quick-win]
5. **Reflection's limits belong in the definition's use conditions.** No representation completely captures its referent, some kernel must remain unmodifiable for bootstrapping, and self-modification makes semantics more open-ended and harder for programmers and users to understand (printed pp. 2, 8; PDF pp. 2, 8). [quick-win]

## Inherited Vocabulary

### Exact terminology and definitions

- **Computational reflection / reflective system.** “Computational reflection” is the behavior exhibited by a “reflective system”; a reflective system is “a computational system which reasons about itself in a causally connected way” (printed p. 1; PDF p. 1). The paper thereafter shortens computational reflection to **reflection**.
- **Computational system.** A “computer-based system” that reasons about a problem domain—answers questions and may support actions—using internal representations plus inference rules (printed p. 1; PDF p. 1). A representation has both an internal structure and its referent.
- **Causal connection.** Internal structures and the represented domain are linked such that change in either has a corresponding effect on the other. Maes's robot-arm illustration makes the two directions explicit: external movement updates the internal position structures, while internally changing those structures moves the arm (printed pp. 1–2; PDF pp. 1–2).
- **Self-representation.** A reflective system incorporates structures representing aspects of itself; their sum is the system's “self-representation.” It permits limited questions and actions concerning the system itself (printed p. 2; PDF p. 2).
- **Procedural reflection.** The causally connected self-representation is the program that implements the system; one representation is used both for implementation and reasoning about the system (printed p. 14; PDF p. 14).
- **Declarative reflection.** The self-representation is not the implementation but statements or constraints concerning system status and behavior; the interpreter must translate these into, and maintain consistency with, the procedural interpretation process (printed p. 14; PDF p. 14).
- **Theory relativity of reflection.** The particular self-representation supplies the terminology for reflective reasoning and fixes the aspects and granularity at which self-reasoning and self-modification are possible (printed pp. 14–17; PDF pp. 14–17).
- **Implicit / explicit reflection.** Under implicit reflection the interpreter systematically activates reflective reasoning to fill required “holes” in normal interpretation; under explicit reflection it occurs only when the system's program prescribes a temporary move to the reflective level (printed pp. 17–18; PDF pp. 17–18).

### Necessary conditions versus illustrative features

Necessary for Maes's definition are: a computer-based reasoning system; internal structures representing aspects of that same system; access sufficient for limited self-reasoning or self-action; and a causal connection that preserves representational accuracy and behavioral compliance (printed pp. 1–2; PDF pp. 1–2). A language advertised as having a reflective architecture additionally must expose the self-representing structures and have its interpreter guarantee their causal connection (printed p. 9; PDF p. 9).

Meta-circular interpreters, infinite interpreter towers, a common program/data representation, reflective functions, meta-theories, self-referencing rules, and the specific systems 3-LISP, FOL, SOAR, TEIRESIAS, KRS, and Smalltalk are architectures or illustrations, not general necessary conditions. The shared program/data format is stated only as necessary for a **meta-circular interpreter**, not for reflection in every model (printed pp. 2–7, 9–14; especially p. 14; PDF same pages). Ability to modify every component is also not required: the representation is aspect-selective and a non-explicit, nonmodifiable kernel is unavoidable (printed p. 2; PDF p. 2).

### System boundary and human participation

The defined system boundary is computational: internal representations and inference rules form a computer-based reasoning system, initially related to an external problem domain; in reflection, selected aspects of the computational system itself become the represented domain (printed pp. 1–2; PDF pp. 1–2). The interpreter is functionally inside the reflective architecture because it exposes the representation and enforces the causal connection, even where a lower implementation layer remains outside explicit self-representation (printed pp. 9, 14; PDF pp. 9, 14).

The paper does **not** treat people as components of the reflective system. Programmers and users appear as external parties who may lose control, information, or understanding when a system changes itself (printed p. 8; PDF p. 8). Maes's definition therefore provides no warrant for satisfying computational reflection by counting a human maintainer as part of the causal mechanism; a human-inclusive boundary would need separate theoretical support.

### Causal topology

For ordinary domain representation, causality is bidirectional correspondence: domain change → representation change, and internally produced representation change → domain change (printed pp. 1–2; PDF pp. 1–2). When the domain is the system itself, represented system aspect → accurate self-representation and manipulated self-representation → compliant system status/behavior, enabling self-modification through the system's own reasoning (printed p. 2; PDF p. 2). In reflective languages, the interpreter maintains those arrows (printed p. 9; PDF p. 9). Procedural reflection collapses implementation and self-representation into one operative structure; declarative reflection keeps two representations and requires a translating, consistency-maintaining path between declarative constraints and procedural behavior (printed p. 14; PDF p. 14).

### Distinctions that should constrain later Commonplace notes

- Do not equate a **self-description** or self-referencing text with reflection; require an account of the causal connection to represented system aspects.
- Do not infer whole-system transparency or modifiability from reflection; state which aspects are represented, at what granularity, and which kernel remains outside the representation.
- Keep **procedural versus declarative** separate from Commonplace's **prose versus symbolic** representational forms: Maes classifies how self-representation relates to implementation, not merely its encoding medium.
- Treat theory-relativity as a constraint on reach: the vocabulary exposed by a system's self-representation determines the self-questions and self-changes it can formulate.
- Keep reflective capability separate from activation policy: implicit and explicit reflection concern when reflective reasoning runs, not whether the causal connection exists.
- Do not use Maes to put human operators inside the system boundary; that move requires the second-order-cybernetics sources.
- Preserve the terminological conflict noted by Maes: Smith's later usage calls Maes's sense “introspection” and reserves “reflection” for a more circumstantially situated capacity (printed p. 1 n. 1; PDF p. 1). The Commonplace reflective/reflexive decision must remain open pending the rest of the corpus.

## Limitations (our opinion)

This paper is definitional and architecture-comparative, not an empirical test that causal connection is necessary for every useful modern notion of reflection. Its claim that causal connection ensures an “always” accurate representation and compliant behavior is an idealized architectural requirement whose failure modes under stale files, asynchronous agents, probabilistic interpretation, and human approval paths are not examined. “Reasoning” and “corresponding effect” also remain broad. The examples concern computational languages and knowledge-based systems; extending the account to socio-technical or human-inclusive systems changes the boundary and cannot be assumed. Finally, Maes explicitly records a terminological divergence from Smith, so this source should anchor one lineage rather than erase competing uses (printed p. 1 n. 1; PDF p. 1).

## Recommended Next Action

After the remaining requested primary sources are ingested, revise [Actionable theories and reflexive system construction](../notes/actionable-theories-and-reflexive-system-construction.md) to test each proposed condition against Maes's causal-connection, aspect-boundary, and theory-relativity criteria before choosing “reflective” or “reflexive.”
