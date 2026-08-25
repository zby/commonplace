---
description: "Ungar and Smith's primary classless-OO attestation: Self rejects the class/instance split for prototypes and parent-based sharing, gaining cloning and per-object flexibility while losing explicit organizational cues"
source: https://bibliography.selflanguage.org/_static/self-power.pdf
captured: "2026-08-19"
capture: pdf-read
genre: design-proposal
snapshot_sha256: f4bf50091d62d2e7028cf3784c8c772348d18583eeb63692158c7394ee3cb863
ingested: "2026-08-19"
type: kb/sources/types/ingest-report.md
domains: [prototype-based-oo, class-instance-model, domain-pricing]
---

# Ingest: SELF: The Power of Simplicity

## Classification

A peer-reviewed programming-language design paper that argues for Self's classless object model and works through its mechanisms and tradeoffs without a comparative experiment.
Author: David Ungar and Randall B. Smith designed Self and compare it directly with Smalltalk; they are primary witnesses for the intended classless design, but interested advocates rather than independent evaluators of its benefits.

## Summary

Ungar and Smith present Self as a deliberately classless object-oriented paradigm. Where class-based systems relate objects through both “instance of” and “subclass of” and create objects by interpreting a class plan, Self uses one “inherits from” relation and creates objects by cloning concrete prototypes. Any object can carry unique state or behavior, while parent objects retain shared behavior and allow one change to affect a family. The authors argue that classes cost conceptual machinery, plan interpretation, awkward one-of-a-kind objects, format restrictions, and metaclass regress. They also state the counter-price: removing language-level distinctions makes system organization less manifest, may cause programmers to recreate class-like objects, and requires better navigation and description. Self is therefore strong evidence that the class commitment is real design content—an object-oriented rival was organized around removing it—not evidence that classes are simply a mistake.

## Quotes

No source quotes have been retained yet.

## Connections Found

The paper is the primary rival-paradigm attestation requested by [domain pricing routes an exception to idealization assessment but does not decide it](../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md): Self calls itself a new object-oriented paradigm and makes eliminating classes a defining move. It also grounds the contrast in [instantiation alone cannot model agent learning across sessions](../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md), because it shows exactly what changes when object creation ceases to mean instantiating a fixed class plan. [A framework rule with a boundary-preserving rival is not an inherited constraint](../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) supplies the correct limit: Self demonstrates that classes are a contestable design choice within a broader object-oriented boundary; it does not establish the adequacy of the immutable-class idealization for the agent analogy. Compared with [the metaobject-protocol attestation](./metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md), Self supplies a different signature: the MOP marks exceptional definition change inside a class-based paradigm, while Self rejects the paradigm's class commitment at the language-design level.

## Extractable Value

1. **The rival is organized around dropping the commitment.** Self's introduction says it includes neither classes nor variables, its comparison table labels the design “SELF: no classes,” and its conclusion calls Self a new object-oriented paradigm whose simplicity comes from realizing that classes are unnecessary. This is direct author-external evidence for the rival-paradigm pricing signature. [quick-win]
2. **The class/instance split carries specific design commitments.** The paper contrasts two relations (`instance of` and `subclass of`) with one (`inherits from`), plan-based instantiation with copying a concrete example, and class-held representation information with objects that describe their own format. The commitment is therefore more than terminology: it determines creation, representation, and inheritance structure. [quick-win]
3. **Removing classes buys concreteness and local variation.** Prototypes are inspectable examples rather than descriptions; cloning replaces interpretation of a plan; one-of-a-kind objects need no singleton class; and any object can acquire unique behavior or replace stored state with computed behavior. These are the positive design reasons for the rival, not mere exceptions to class-based practice. [quick-win]
4. **Parent objects retain shared change without reinstating the full class role.** Self moves family behavior into a shared parent used by the prototype and its siblings. The parent plays a class-like role for behavior and permits sweeping changes, but carries no representation specification and is itself an ordinary object. This is the paper's answer to what prototype mutability gains without restoring the class/instance split. [deep-dive]
5. **The paper states what the simplification gives up.** Without the class-instance distinction it may be harder to see which objects exist only to share information; programmers may recreate class-like organization; the environment needs navigational and descriptive aids; and fewer constructs mean fewer linguistic clues to system structure. This concession prevents “classless” from being read as a free simplification. [quick-win]
6. **Assignable parents make behavioral organization revisable at runtime.** The tree example changes an empty object's parent to tree-node traits, using dynamic inheritance to change what the object does. This shows the prototype model can treat behavior-determining ancestry as ordinary mutable object structure, but the paper does not supply learning, acceptance, or governance around that mutation. [just-a-reference]

## Limitations (our opinion)

The supplied PDF is the 1991 journal version, which calls itself a substantial revision of the OOPSLA ’87 paper. It is valid evidence for Ungar and Smith's developed Self argument, but exact wording should not be attributed to the 1987 proceedings version without checking that original. The paper is design advocacy with examples and conceptual comparisons, not controlled evidence that programmers understand, reuse, or maintain prototype systems better.

Self rejects a language-enforced class/instance split, not shared organization. Its traits or parent objects deliberately centralize behavior and are acknowledged to play a role akin to a class; the narrower difference is that they are ordinary objects, specify no instance representation, and do not sit across an intrinsic class/instance boundary. Likewise, the paper usually calls parent-pointer sharing “inheritance”; describing the mechanism as delegation is standard prototype-language framing but should not be presented as the paper's exclusive term.

For domain pricing, the rival establishes that the class commitment is real and contestable. It does not show that reflective mutation is rare, bounded, or subordinate inside class-based OO, and it cannot decide the adequacy assessment in the current domain-pricing note. Mutable shared parents also expose broad change propagation, but the authors analyze flexibility and navigability rather than safety, review, versioning, or rollback; those governance properties cannot be imported from this source.

## Recommended Next Action

In a separate note-edit pass, add `evidenced-by` citations from the current domain-pricing and instantiation notes to this snapshot, using it narrowly for the rival-paradigm attestation and the class-versus-prototype tradeoff—not for adequacy, prevalence, or safe runtime mutation claims.
