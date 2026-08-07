---
gate_id: semantic/conceptual-role-conflation
name: Conceptual-role conflation
description: "A load-bearing passage blurs a term, the concept it names, a prior account, the current artifact's explication or application, or the object of application, making its attribution, scope, or contribution unclear."
type: kb/types/review-gate.md
lens: semantic
watches: [body]
staleness: changed
---

## Failure mode

A load-bearing passage presents things that occupy different conceptual roles as though they were interchangeable or connected by one relation. It may blur:

- a term or label;
- the concept or property the term names;
- a source or prior account of that concept;
- the current artifact's definition, explication, extension, or application; and
- the system, artifact, or case to which the concept applies.

The reader therefore cannot tell which relation the artifact asserts: what merely names something, what is established elsewhere, what the artifact inherits, what it changes, and what it applies the result to. This is not ordinary unfamiliarity with terminology. The wording must permit materially different assignments of these roles.

## Test

Inspect passages that define, import, compare, extend, or apply a concept.

1. Identify the important noun phrases and the relation words connecting them, such as *is*, *names*, *defines*, *inherits*, *extends*, *applies*, or *instantiates*.
2. Assign each noun phrase its apparent role: term, concept, source account, current explication, or object of application.
3. State two reasonable role assignments permitted by the passage. Do not use merely synonymous paraphrases or strained grammatical readings.
4. Check nearby context and any directly relevant provenance. If it settles the roles and relations, do not flag the compressed sentence in isolation.
5. Apply the materiality test. WARN only when choosing between the assignments changes at least one of:
   - who or what receives attribution;
   - what the current artifact claims to inherit or contribute;
   - the scope or boundary of the concept; or
   - whether the passage defines a concept or merely applies it.

For each WARN, quote the smallest useful passage, name the conflated roles, give the competing assignments, and state the authorial relation that must be decided or made explicit. Report at most three highest-impact findings. Do not choose the relation for the author and do not present a rewrite as settled.

Return PASS when no finding clears the materiality threshold. A plausible but immaterial blur may be noted as INFO while the final verdict remains PASS. Return ERROR only when the target cannot be inspected.

Do not flag adjacent problems here:

- A general assertion with materially different meanings but no role conflation belongs to semantic underspecification.
- Modifier attachment, pronoun reference, and negation scope are parsing ambiguities.
- A linked source that does not support an otherwise clear attribution is a grounding or concept-attribution failure.
- A concept used inconsistently across separate passages is an internal-consistency failure.
- A definition that never establishes a useful boundary or operational meaning is an explication-quality failure.
- A buried thesis, excessive detail, duplication, or poor section order is a structural or compression problem. Do not flag it merely because a different organization would be simpler.

## Example (fail)

> The definition's structural core is computational reflection, an established term: a system that reasons about itself through a causally connected self-representation.

The passage moves from the term *computational reflection*, to the concept associated with it, to a system that instantiates the concept, while presenting all three as one “structural core.” A revision must decide whether the definition inherits a term, a property from a prior account, or a criterion applied to systems. Those alternatives change both attribution and what the current definition contributes.

## Example (pass)

> Computational reflection is an established concept in computer science. This definition adopts its requirement for causally connected self-representation and adds an improvement-directed condition.

The passage distinguishes the inherited concept from the specific criterion the current definition adopts and the condition it adds.
