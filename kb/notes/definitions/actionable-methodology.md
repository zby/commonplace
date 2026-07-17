---
description: "Definition — actionable is a relation a methodology stands in, not a property of an artifact: it holds only relative to an operator, available operations, a target system, and a stated setting"
type: kb/types/definition.md
tags: [foundations]
---

# Actionable methodology

**Actionable** is the term this note defines. **Methodology** keeps its ordinary sense — guidance that maps represented conditions to a prescription, exclusion, ranking, or evaluation criterion, close to what information-systems scholar Shirley Gregor calls a Type V theory. A theory that only describes or explains, supplying nothing that discriminates among interventions, is not a methodology in that ordinary sense, however true it is; Commonplace does not additionally stipulate this as a technical condition, since the word already carries it.

A methodology is **actionable** for a particular operator, in a stated setting, when that operator can use its mapping to choose among available interventions in a target system. This is the operator-relative predicate Commonplace adds: a methodology nobody can apply here and now is still a methodology; it is simply not actionable in that setting. Actionability is a relation a methodology stands in, not a kind of artifact — there is no separate thing called an "actionable theory."

## The relation requires four elements

- A **methodology** that applies to the target and supplies an intervention-relevant mapping.
- An **operator**, including any interpreter it relies on, that can follow the mapping with enough fidelity for the mapping's distinctions to change its selection.
- A set of **available operations** for which the operator has the necessary access, resources, and authority in the stated setting.
- A **target system** that those operations can reach and affect.

The operator may be a person, an organization, a trained model, deterministic software, or a combination of them. Within such an arrangement, the interpreter is the part that realizes the mapping from conditions to a selection among operations.

## Scope

The ordinary sense of methodology used here starts from information-systems scholar Shirley Gregor's **theory for design and action**. Type V theory “says how to do something” by prescribing methods, techniques, or principles for constructing an artifact ([Gregor 2006, printed pp. 619–620; PDF pp. 10–11](../../sources/the-nature-of-theory-in-information-systems-gregor-2006.ingest.md)); membership does not require a currently capable or authorized operator.

**Actionable** adds the operational relation Gregor's taxonomy does not carry. A design-and-action theory sitting unread in a paper remains prescriptive — it is still a methodology — but it is not actionable in a particular setting unless an operator can use its mapping through available operations on the target. Theory type and situated actionability therefore answer different questions; actionability is not a proposed sixth type in Gregor's taxonomy.

Prescriptiveness and actionability come apart in both directions. A software-architecture methodology can be actionable for a developer before the developer acts on it: it maps architectural conditions to component and interface choices, and the developer has the access and authority to make those changes. If the developer loses repository access, it remains a methodology but is no longer actionable for that developer in that setting — it is still prescriptive, but the operational relation fails. Conversely, repository access alone actions nothing if the theory supplies no intervention-relevant mapping for the software system — the relation's other elements hold, but there is nothing to act on.

Evaluation contributes to actionability only when its result can affect the selection, retention, or modification of an intervention. Retrospective analysis with no path into action may be informative, but it is not actionable in this sense.

## Exclusions

**Actionable** is not a compliment: the mapping, operator, available operations, target, and setting must be identifiable, or the word is doing no work. **Methodology** is not a synonym for practical-sounding advice — a theory that only describes or explains is not a methodology, however true it is.

Actionability implies neither that the methodology is correct nor that an intervention will succeed. Gregor's “if acted upon” causal expectation remains conditional on the actor and setting ([Gregor 2006, printed p. 619; PDF p. 10](../../sources/the-nature-of-theory-in-information-systems-gregor-2006.ingest.md)).

## Misuse Cases

- Calling a design paper actionable for an organization that lacks the access, resources, or authority to apply it.
- Calling an instruction actionable without identifying the system and operations to which it applies.
- Calling a classification actionable because a resourceful operator could invent a use for it, even though the classification supplies no intervention-relevant mapping.
- Treating actionability as an intrinsic property of prose, independent of an operator and setting.
- Using **actionable theory** as a noun, as if actionability sorted artifacts into kinds rather than relating a methodology to an operator.
- Predicating **actionable** of a methodology without linking to this definition. The bare word is common English with many unrelated ordinary uses (findings, edits, steps, guidance); the technical sense is licensed only where the occurrence links here, on "actionable" itself or on "methodology" in the same clause. An unlinked "actionable" is the ordinary word, not this relation.

---

Relevant Notes:

- [Collisions among load-bearing technical senses should be prevented or visibly scoped at write time](../vocabulary-collisions-prevented-at-write-time-not-read-time.md) — grounds: this definition is the worked case for clausal binding, the scoping device admitted here only because every technical occurrence links back to this note
- [Reflective system](./reflective-system.md) — extends: actionability concerns a methodology–operator–target relation; reflection adds a causally connected representation of the system itself
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — extends: asks how far a methodology's own prescriptions stay governed when the system applies them to itself
- [Gregor, Design Theory in Information Systems](../../sources/design-theory-in-information-systems-gregor-2002.ingest.md) — derived-from: establishes theory for design and action as articulated, prescriptive guidance for a class of artifacts or processes
- [Gregor, The Nature of Theory in Information Systems](../../sources/the-nature-of-theory-in-information-systems-gregor-2006.ingest.md) — derived-from: separates Type V's prescriptive purpose from the operator-dependent relation defined here
- [Gregor and Jones, The Anatomy of a Design Theory](../../sources/the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md) — evidence: separates core design-theory content from the additional agents and actions that implement it
