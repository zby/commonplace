---
description: "Earlier concise statement of Maes's causal reflection definition, with 3-KRS as an object/meta-object implementation and granularity case"
source_snapshot: "kb/sources/maes-concepts-and-experiments-computational-reflection-1987.md"
ingested: "2026-07-14"
type: kb/sources/types/ingest-report.md
domains: [computational-reflection, object-oriented-reflection, meta-objects]
---

# Ingest: Concepts and Experiments in Computational Reflection

Source: [maes-concepts-and-experiments-computational-reflection-1987.md](./maes-concepts-and-experiments-computational-reflection-1987.md)
Captured: 2026-07-14
From: https://cse.hkust.edu.hk/~charlesz/comp610/paper/p147-maes.pdf

## Classification

Genre: scientific-paper -- a peer-reviewed conference paper combining a concise general account of reflection with a system-design report on the 3-KRS object-oriented implementation.
Domains: computational-reflection, object-oriented-reflection, meta-objects
Author: Pattie Maes presents an early publication from her computational-reflection research and reports the design and use of 3-KRS; the later 1988 paper is the clearer general vocabulary source.

## Summary

Maes defines computational reflection as the behavior of a computational system that is about itself in a causally connected way, then makes that definition architectural: an interpreter exposes data representing system aspects and guarantees that changes to those data affect system status and computation. The paper contrasts procedural and declarative reflection before presenting 3-KRS, where each object has a meta-object representing its implementation and interpretation; the interpreter uses those meta-objects, so changing them changes runtime behavior. The case demonstrates local control of reflective granularity, modular attachment of reflective behavior, and the ability to vary interpreters within the language (printed pp. 147–150, 153–154; PDF pp. 1–4, 7–8).

## Connections Found

This is a related earlier version of [Maes's 1988 Computational Reflection](./maes-computational-reflection-1988.md), not an independent foundation: the causal-connection and procedural/declarative claims should be deduplicated in favor of the later treatment. Its distinct value for [Reflective system](../notes/definitions/reflective-system.md) is the implemented 3-KRS topology—objects, meta-objects, and interpreter-mediated behavioral effect—and its local granularity. Its meta-circular discussion also limits the analogy in [LLM context is a homoiconic medium](../notes/llm-context-is-a-homoiconic-medium.md): common program/data representation enables one reflective implementation strategy but is not the general definition.

## Extractable Value

1. **An early, concise causal definition.** Reflection requires that a computational system be about itself in a causally connected way; self-representation supports questions/actions on the system, while causal connection makes computation comply with it (printed pp. 147–148; PDF pp. 1–2). Use the 1988 paper for the mature wording. [just-a-reference]
2. **Reflective architecture assigns obligations to the interpreter.** The interpreter provides runtime access to self-representing data and guarantees that modifications are reflected in status and computation (printed p. 148; PDF p. 2). [quick-win]
3. **3-KRS demonstrates component-local reflection.** Every object can have a meta-object containing implementation/interpretation information; a standard protocol and interpreter use make reflective behavior attachable, replaceable, and local to an instance, class, message, or wider class of objects (printed pp. 151–154; PDF pp. 5–8). [deep-dive]
4. **Meta-objects are not meta-classes.** The paper separates the instance/type relation from the object/meta-object relation: the latter carries system information about implementation and interpretation, avoiding an undisciplined mixture with domain information (printed pp. 151–152; PDF pp. 5–6). [quick-win]
5. **Open-endedness is an effect, not the defining condition.** 3-KRS can build or change interpreters from within the language, but this is a capability obtained through the reflective architecture, not the definition of reflection itself (printed p. 153; PDF p. 7). [quick-win]

## Inherited Vocabulary

### Exact terminology and definitions

- **Computational reflection.** In the introduction, the activity a computational system performs when doing computation about—and possibly affecting—its own computation (printed p. 147; PDF p. 1). Formally, it is the behavior of a **reflective system**, defined as a computational system “which is about itself in a causally connected way” (printed p. 147; PDF p. 1).
- **Computational system / about-ness.** A computer-based system intended to answer questions about and/or support actions in a domain. It contains data representing domain entities and relations, a program prescribing manipulation, and a processor executing that program; the system is “about” its domain (printed pp. 147–148; PDF pp. 1–2).
- **Causal connection / self-representation.** Causal connection means represented domain and representing internal structures affect each other correspondingly. Structures representing aspects of the system collectively form its **self-representation**, enabling questions and actions concerning itself; causal connection makes the representation accurate and system status/computation compliant with it (printed p. 148; PDF p. 2).
- **Object computation / reflective computation.** Object computation concerns the external problem domain; reflective computation concerns the computational system and contributes to its internal organization or interface rather than directly solving the external problem (printed p. 148; PDF p. 2).
- **Reflective architecture.** A programming-language architecture that recognizes reflection as fundamental, exposes data representing system aspects to the running system, and has the interpreter guarantee causal connection between those data and represented aspects (printed p. 148; PDF p. 2).
- **Procedural / declarative reflection.** Procedural reflection uses the implementing program itself as self-representation. Declarative reflection uses statements or constraints about the system and requires the interpreter to translate them into the procedural interpretation process; Maes calls the distinction a continuum (printed pp. 149–150; PDF pp. 3–4).
- **Meta-object.** In 3-KRS, every object has a meta-object grouping information about that object's implementation and interpretation. The meta-object represents reflective information about another object and is taken into account by the interpreter (printed pp. 151, 153–154; PDF pp. 5, 7–8).
- **Reification.** 3-KRS makes the implementation blocks explicit as objects—slot fillers in meta-objects—so they can be accessed and modified at runtime (printed p. 152; PDF p. 6).

### Necessary conditions versus illustrative features

The general necessary conditions are a computational system, self-aboutness through internal representation of some system aspects, and causal connection between representation and represented aspects (printed pp. 147–148; PDF pp. 1–2). For a reflective programming-language architecture, runtime access and interpreter enforcement are additionally explicit requirements (printed p. 148; PDF p. 2).

3-KRS's uniform objects, per-object meta-objects, message protocol, lazy creation, meta-circular interpreter, libraries of reflective behavior, and local interpreter variation are implementation features, not universal conditions (printed pp. 151–154; PDF pp. 5–8). A shared program/data format is necessary only for a meta-circular interpreter (printed p. 149; PDF p. 3). Performance statistics, debugging, tracing, interfaces, control reasoning, self-optimization, learning, and monitors are illustrative uses (printed p. 148; PDF p. 2).

### System boundary and human participation

The general boundary includes represented data, program, and executing processor; its external side is the problem domain (printed pp. 147–148; PDF pp. 1–2). In the reflective decomposition, the object part handles that domain while the reflective part handles object computation, and the language interpreter supplies the causal link (printed p. 148; PDF p. 2). In 3-KRS the boundary can be considered locally around an object plus its meta-object and the interpreter protocol that gives the meta-object force, while the full language implementation still depends on an underlying interpreter layer (printed pp. 151–154; PDF pp. 5–8).

People are not components of the defined system. Programmers and users configure or inspect it from outside; the design is motivated partly by making reflective programming modular and manageable for them. Nothing in this paper allows human intervention to substitute for interpreter-maintained causal connection.

### Causal topology

The generic topology is two-way: external domain change ↔ internal representation change; when the represented domain is the system, self-representation change → system status/computation change and system change → accurate self-representation (printed p. 148; PDF p. 2). In procedural reflection, one structure is both implementation and self-representation, making consistency immediate (printed p. 149; PDF p. 3). In declarative reflection, explicit constraint representation → interpreter translation → procedural implementation/behavior, with a reverse accuracy/consistency requirement (printed pp. 149–150; PDF pp. 3–4). In 3-KRS, object ↔ meta-object protocol plus interpreter consultation makes the meta-object an operative representation: changing an evaluation or inheritance method changes future behavior of the represented object (printed pp. 152–154; PDF pp. 6–8).

### Distinctions that should constrain later Commonplace notes

- Preserve **aboutness plus causal connection** as the definitional threshold; the examples of self-modification and interpreter extension are consequences.
- Separate **object/domain information** from **meta/system information**; Maes explicitly rejects conflating the object/meta-object relation with the instance/class relation.
- State the **granularity** of reflection. 3-KRS can target an individual instance, message, class, or family, showing that local scope matters.
- Keep a **meta-object** distinct from a detached description: its interpreter-recognized protocol is what gives it behavioral force.
- Deduplicate the general causal and procedural/declarative claims against Maes 1988; retain this paper chiefly for 3-KRS and historical sequence.
- Do not decide Commonplace's reflective/reflexive label from this source; it uses “reflection” in Maes's computational lineage and does not analyze human-inclusive observing systems.

## Limitations (our opinion)

The paper's general definition is compressed and is better supported by Maes's 1988 treatment. The 3-KRS result establishes feasibility and illustrates programming style, but provides no controlled comparison, performance data, independent usability evaluation, or evidence that its object-oriented advantages generalize beyond that language. The OCR capture also contains typographical recognition errors, so wording-sensitive claims should be checked against the PDF page image. Finally, the system remains computational and interpreter-centered; applying its topology to a socio-technical repository without locating an equivalent causal mechanism would be analogy, not inheritance.

## Recommended Next Action

Use the 3-KRS object/meta-object/interpreter topology as an implementation precedent for [Cross-representational reflection](../notes/cross-representational-reflection.md), while citing Maes 1988—not this related version—for the general definition.
