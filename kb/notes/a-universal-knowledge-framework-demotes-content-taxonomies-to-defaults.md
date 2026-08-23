---
description: "Universal frameworks should replace closed content taxonomies with complete local contracts and guarded creation-time defaults; what stays fixed is stipulated or enforced, not certified universal"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
---

# A universal knowledge framework demotes content taxonomies to defaults

A framework that aims to serve *any* knowledge base should not promote a closed first-order content taxonomy — a fixed list of the kinds or roles knowledge artifacts may have, such as exactly three content modes or one fixed type set — to a universal rule merely because it fits the collections already seen. Such a taxonomy should enter the framework as a guarded default. It should become universal only if its top-level categories survive heterogeneous worked cases without exceptions or relabeling. This is a burden-of-proof rule, not proof that a closed upper content ontology is impossible: a role-defined taxonomy that meets the burden may remain universal. The demotion leaves no certified universals behind; what the framework still fixes, it fixes by stipulated definition and by enforced design, as detailed below.

## Why closed taxonomies fail at universality

The failure mode is induction from too small a sample. A framework's first taxonomies are usually abstracted from the KBs its authors have seen — often just one. The rules can be real and useful while their scope remains limited to the *kind* of KB they came from. A first-person committed methodology KB genuinely needs claim-shaped titles and "do I still believe this?" maintenance; exactly those rules would break a stance-neutral evidence map. They are local contract clauses mistaken for universals because the originating case supplies no visible boundary. Demotion to a default follows because [an experience should be abstracted into a lesson only when its boundary can be stated](./abstract-an-experience-only-when-you-can-state-the-boundary.md). A closed upper taxonomy that maps genuinely heterogeneous collections without exception or post-hoc relabeling would defeat this recommendation rather than be reclassified away.

## Closure did real work; guards and defaults recover it

Demote, don't delete. A closed taxonomy earns its keep three ways, but its replacements do not preserve all three equally:

- **Routing.** "This collection is theoretical" lets an agent infer the writing goal from one word. Replace the shortcut with a complete local `COLLECTION.md` and a root routing description that says when to use the path. The extra words remove the need to resolve a distant label before acting.
- **Growth brake.** "The list is complete" blocks speculative additions. Preserve that discipline for reusable starting material with a concrete-need guard: add a [collection prototype](../reference/collection-prototypes.md) only when a real collection-creation case would use it.
- **Interoperability.** A shared name appears to let readers recognize conventions across collections. Clone-once defaults cannot preserve that [coordination value](./definitions/coordination-value.md), because independently owned local contracts may diverge. Genuine interoperability needs a continuing shared authority or an enforced compatibility contract; without one, readers must compare the local contracts themselves.

The guard protects the creation-time catalogue, not local experimentation. A new collection can declare and use a complete local contract immediately. Copying a prototype may lower its cold-start cost, but copying creates no continuing relationship and no cross-collection compatibility guarantee. This prevents local variation from silently claiming interoperability while retaining the practical value of worked starting text.

## What the framework fixes, and how

Universality cannot mean "any text." The framework holds that line with two fixed points, and neither claims certified-universal status:

- **By definition.** An artifact is admitted as knowledge only if it is [answerable](../reference/definitions/answerability.md) — its collection contract can name what it answers to, the property asserted, and the discrepancy that triggers correction. The relation's per-kind forms, exclusions, and edge-case decision rules live in the definition. The invariant applies to artifacts admitted as knowledge, not to workshop documents or system-definition artifacts used to operate the framework; contesting it means proposing a different account of the domain commitment, not finding a counterexample under this one.
- **By enforced design.** Every writable collection declares a loadable contract (quality goal, conventions, maintenance semantics). The machinery refuses collections without one, and [ADR 017](../reference/adr/017-collection-md-is-the-register-convention-boundary.md) records the design and its alternatives. The rationale is consumer-side: bounded agents cannot reliably infer a collection's conventions from examples within a context budget, so heterogeneous collections need their conventions explicit and loadable — a contestable claim, not a certification.

Bounded-context economy likewise applies across every collection contract because [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). That constraint is claimed from the chosen consumer; a framework with a different reader architecture would not inherit it.

## Evidence

Commonplace supplies motivating instances, not proof of universal necessity. Types became path references, making the type set open and collection-local (ADR 018). The former theoretical/descriptive/prescriptive register taxonomy first became nonbinding named defaults after a dialectical/evidential collection supplied a worked counterexample (ADR 042), then became clone-once [collection prototypes](../reference/collection-prototypes.md) when the system audit found that only local contracts ever bound ([ADR 069](../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md)). Link vocabulary made an analogous move to collection-owned selections from a shared catalogue (ADR 019), but link labels classify relationships rather than content, so they are not a direct content-taxonomy case.

External systems expose the same trade-off without settling the theorem. [Sparks](../agent-memory-systems/reviews/sparks.md) gains a clean protocol from a hardcoded page shape because it is narrow, while [ai-modules](../agent-memory-systems/reviews/theafh--ai-modules.md) lets each wiki schema own an extensible page-type enum and accepts softer framework-wide consistency. Together with the Commonplace changes, these observations support guarded defaults as a design policy; they do not prove that no closed upper taxonomy can earn universal status.

## Caveats

Not every closed set is a content taxonomy. Sets fixed by the consumer's architecture or the framework's machinery (e.g., the syntactic shape of frontmatter or the existence of a lifecycle) may stay closed. A semantic category does not become machinery merely because tools consume it: machinery may fix the interface shape while content values remain defaults. The sharper instrument is the demotion test: [a framework rule with a boundary-preserving rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md). A rule demotes when another workable classification preserves the same consumer, substrate, domain, and machinery commitments; it can stay universal only when changing it would change one of those commitments. Finally, the claim applies to frameworks that *aim* at universality. A single-purpose KB can benefit from hardcoding its local contract; the burden begins when that contract is exported as a general taxonomy. This last concession is contested: [task-fitted structure costs cross-task reuse](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md) argues that a single-purpose KB's own question set drifts, so the burden arrives through time even when the contract is never exported.

---

Relevant Notes:

- [Artifact classification separates content kind, lineage, and authority](./artifact-classification-separates-content-kind-lineage-and-authority.md) — contrasts: separates region- and path-level classifications from a collection's whole-artifact writing contract
- [Title as claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — contrasts: first-person commitment is one answerability relation among several, not the framework's definition
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: why bounded-context economy is claimed from the consumer and applies across every collection contract
- [KB goals in always-loaded context guide inclusion decisions](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — contrasts: the same universal/per-installation split seen from the operator side — purpose, scope, and quality bar need human input, while creation-time defaults only lower drafting cost
- [017-collection-md-is-the-register-convention-boundary](../reference/adr/017-collection-md-is-the-register-convention-boundary.md) — evidenced-by: shipped instance of the declaration obligation — COLLECTION.md is the mandatory per-collection contract surface, and a missing or vague one is "an operational defect"
- [Text contract](../reference/definitions/collection.md#text-contract) — defined-in: the binding local declaration that replaces inference from a closed taxonomy
- [Coordination value](./definitions/coordination-value.md) — defined-in: names the interoperability benefit that clone-once defaults cannot preserve without continuing shared authority
- [Answerability](../reference/definitions/answerability.md) — defined-in: the stipulated domain invariant for admission as knowledge, extracted from this note's former invariant section
- [018-Types are path references to instruction docs](../reference/adr/018-types-are-path-references-to-instruction-docs.md) — evidenced-by: shipped instance of the demotion — an open, collection-local type set
- [019-Collection-owned link vocabulary with per-destination outbound rules](../reference/adr/019-collection-owned-link-vocabulary.md) — evidenced-by: analogous semantic-vocabulary demotion — collection-owned selections from a shared catalogue
- [042-Register becomes a default profile under open-ended text contracts](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — evidenced-by: historical first demotion of the closed taxonomy, backed by a worked counterexample
- [069-Collection contract bundles become one-time prototypes](../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md) — evidenced-by: shipped correction from shared labels to clone-once starting contracts after the binding-path audit
- [Directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md) — extends: derives how the declaration obligation distributes clauses across collection and type surfaces
- [044-User verification replaces global note status](../reference/adr/044-user-verification-replaces-global-note-status.md) — evidenced-by: the status/lifecycle prediction played out — the fused field was deleted outright, with the per-collection redefinition of assertion force weighed and rejected in its considered alternatives
- [Current-task fit alone does not warrant costly structural entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — contradicts: contests the single-purpose-KB caveat — question-set drift brings the burden forward to the instance, before any export
