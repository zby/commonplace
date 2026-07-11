---
description: "Universal frameworks should keep closed first-order content taxonomies as guarded defaults until heterogeneous worked cases establish their reach; declared contracts and answerability remain universal"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
---

# A universal knowledge framework demotes content taxonomies to defaults and keeps answerability

A framework that aims to serve *any* knowledge base should not promote a closed first-order content taxonomy — a fixed list of the kinds or roles knowledge artifacts may have, such as exactly three content modes or one fixed type set — to a universal rule merely because it fits the collections already seen. Such a taxonomy should enter the framework as a guarded default. It should become universal only if its top-level categories survive heterogeneous worked cases without exceptions or relabeling. This is a burden-of-proof rule, not proof that a closed upper content ontology is impossible: a role-defined taxonomy that meets the burden may remain universal. Two things do survive universally. First, every collection must *declare its contract* (quality goal, conventions, maintenance semantics) in a form that writers, reviewers, and tools can load. Second, every artifact admitted as knowledge must satisfy one domain invariant: it must be **answerable** under an explicit correctness or currency test.

## Why closed taxonomies fail at universality

The failure mode is induction from too small a sample. A framework's first taxonomies are usually abstracted from the KBs its authors have seen — often just one. The rules can be real and useful while their scope remains limited to the *kind* of KB they came from. A first-person committed methodology KB genuinely needs claim-shaped titles and "do I still believe this?" maintenance; exactly those rules would break a stance-neutral evidence map. They are profile features mistaken for universals because the originating case supplies no visible boundary. Demotion to a default follows because [an experience should be abstracted into a lesson only when its boundary can be stated](./abstract-an-experience-only-when-you-can-state-the-boundary.md). A closed upper taxonomy that maps genuinely heterogeneous collections without exception or post-hoc relabeling would defeat this recommendation rather than be reclassified away.

## Closure did real work; guards and defaults recover it

Demote, don't delete. A closed taxonomy earns its keep three ways, and each has a guarded replacement:

- **Routing.** "This collection is theoretical" lets an agent infer the writing goal from one word. Keep that benefit by treating the taxonomy's entries as *named default profiles*: proven bundles that a new collection can adopt in one line.
- **Growth brake.** "The list is complete" blocks speculative additions. Preserve that discipline with a *worked-case guard*: admit new entries only after they survive use in a real collection, never in anticipation of one.
- **Interoperability.** Shared profile names let readers recognize conventions across collections. Preserve it with a *shared catalogue* whose published entries retain fixed meanings across adopters.

The guard protects the shared catalogue, not local experimentation. A new collection can declare and use a local contract immediately. Local extensions remain explicitly local and carry no cross-collection compatibility guarantee. Promotion waits until a contract has survived real use and its meaning can be shared without collision. This approach accepts a cold-start cost for novel collections while preventing local variation from silently claiming interoperability.

## The invariant that stays closed: answerability

Universality cannot mean "any text." The invariant applies to artifacts admitted as knowledge, not to every workshop document or system-definition artifact used to operate the framework. An answerability relation counts only when the collection contract can name:

- an external referent or outcome;
- the correctness or currency property the artifact asserts about it; and
- an observable discrepancy or change that triggers correction, qualification, or retirement.

Mere usefulness, provenance, audience response, or authorial intent does not count unless the artifact asserts fidelity to it. A claim answers to the world; a description, to a system; a prescription, to the outcomes of following it under stated conditions; an attributed position, to what the party asserts; a capture, to its source; and an index, to its promised coverage of a corpus. First-person commitment ("do I still believe this?") is one relation among several, not the framework's definition.

This gives edge cases a decision rule. An unresolved question qualifies only if the artifact asserts that the question remains open or relevant, with resolution or changed priorities as retirement conditions. Otherwise, it belongs in work-in-flight. A prompt may answer to observed behavior as a system-definition artifact, but that does not make it knowledge. Merely retaining an authored poem asserts no correctness or currency relation, while a capture of a poem can assert fidelity to its source. Maintenance is universal in form — every knowledge artifact has revision conditions — but local in content.

## A consumer-derived universal

Within an agent-operated framework, bounded-context economy also applies to every collection contract because [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). This constraint is inherited from the chosen consumer; it does not establish the same universal for a framework with a different reader architecture.

## Evidence

Commonplace supplies motivating instances, not proof of universal necessity. Types became path references, making the type set open and collection-local (ADR 018). The three [registers](./definitions/text-contract.md) became default text-contract profiles after a dialectical/evidential collection supplied a worked counterexample ([ADR 042](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md)). Link vocabulary made an analogous move to collection-owned selections from a shared catalogue (ADR 019), but link labels classify relationships rather than content, so they are not a direct content-taxonomy case.

External systems expose the same trade-off without settling the theorem. [Sparks](../agent-memory-systems/reviews/sparks.md) gains a clean protocol from a hardcoded page shape because it is narrow, while [ai-modules](../agent-memory-systems/reviews/theafh--ai-modules.md) lets each wiki schema own an extensible page-type enum and accepts softer framework-wide consistency. Together with the Commonplace changes, these observations support guarded defaults as a design policy; they do not prove that no closed upper taxonomy can earn universal status.

## Caveats

Not every closed set is a content taxonomy. Sets fixed by the consumer's architecture or the framework's machinery (e.g., the syntactic shape of frontmatter or the existence of a lifecycle) may stay closed. A semantic category does not become machinery merely because tools consume it: machinery may fix the interface shape while content values remain defaults. The stronger membership test is that [first principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md). A rule stays universal when changing it requires changing a consumer, substrate, domain, or machinery commitment, rather than merely choosing another workable classification under the same commitments. Finally, the claim applies to frameworks that *aim* at universality. A single-purpose KB can benefit from hardcoding its profile; the burden begins when that profile is exported.

---

Relevant Notes:

- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — contrasts: its three recurring attractors survive as profiles, while this note states the burden a closed content taxonomy must meet before becoming universal
- [Title as claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — contrasts: first-person commitment is one answerability relation among several, not the framework's definition
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: why bounded-context economy is consumer-derived and therefore stays universal
- [KB goals in always-loaded context guide inclusion decisions](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — contrasts: the same universal/per-installation split seen from the operator side — purpose, scope, and quality bar need human input, while the demoted taxonomies arrive as framework-shipped defaults
- [017-collection-md-is-the-register-convention-boundary](../reference/adr/017-collection-md-is-the-register-convention-boundary.md) — evidence: shipped instance of the declaration obligation — COLLECTION.md is the mandatory per-collection contract surface, and a missing or vague one is "an operational defect"
- [Text contract](./definitions/text-contract.md) — defined-in: the profile vocabulary the third shipped instance uses
- [Knowledge artifact](./definitions/knowledge-artifact.md) — defined-in: the answerability boundary that separates knowledge artifacts from arbitrary text
- [018-Types are path references to instruction docs](../reference/adr/018-types-are-path-references-to-instruction-docs.md) — evidence: shipped instance of the demotion — an open, collection-local type set
- [019-Collection-owned link vocabulary with per-destination outbound rules](../reference/adr/019-collection-owned-link-vocabulary.md) — evidence: analogous semantic-vocabulary demotion — collection-owned selections from a shared catalogue
- [042-Register becomes a default profile under open-ended text contracts](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — evidence: shipped content-profile demotion backed by a worked counterexample
- [Directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md) — extends: derives how the universal declaration obligation distributes clauses across collection and type surfaces
- [Assertion force separate from lifecycle status](../reference/proposals/assertion-force-separate-from-lifecycle-status.md) — see-also: develops the removed status/lifecycle prediction as a worked proposal with its own evidence and caveats
