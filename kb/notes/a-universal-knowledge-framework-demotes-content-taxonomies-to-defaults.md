---
description: "Universality forces first-order content taxonomies down to guarded default libraries; what stays universal is second-order — declared collection contracts — plus one invariant: answerability"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
status: seedling
---

# A universal knowledge framework demotes content taxonomies to defaults and keeps answerability

A framework that aims to serve *any* knowledge base cannot keep first-order content taxonomies — closed lists that classify what knowledge is (exactly three content modes, exactly five link labels, one fixed type set) — as universal rules. Every such taxonomy is [distilled](./definitions/distillation.md) experience from the knowledge bases its authors have already operated, and a genuinely new kind of KB will break it. What survives at the universal level is second-order: the obligation that every collection *declare its contract* (quality goal, conventions, maintenance semantics) in a form writers, reviewers, and tools can load — plus one domain invariant that keeps the framework a *knowledge* framework rather than a document framework: every artifact must be **answerable** — capable of being wrong or stale relative to something outside itself.

## Why closed taxonomies fail at universality

The failure is induction from too small a sample. A framework's first taxonomies are abstracted from the KBs its authors have seen — usually one. The rules are real: they encode what made that KB work. But their scope is the *kind* of KB they came from, and nothing in the rules marks that boundary. A first-person committed methodology KB genuinely needs claim-shaped titles and "do I still believe this?" maintenance; a stance-neutral evidence map is broken by exactly those rules. The rules were never wrong — they were profile features mistaken for universals, because with n=1 the difference is invisible. Universality makes the mistake visible: each new kind of knowledge that arrives ("everything goes") falsifies another rule that had quietly assumed the old kind.

## Closure did real work; guards and defaults recover it

Demote, don't delete. A closed taxonomy earns its keep three ways, and each has a second-order replacement:

- **Routing.** "This collection is theoretical" lets an agent infer the writing goal from one word. Recovered by keeping the taxonomy's entries as *named default profiles* — proven bundles a new collection adopts in one line.
- **Growth brake.** "The list is complete" blocks speculative additions. Recovered by a *worked-case guard*: new entries are admitted only after surviving use in a real collection, never from anticipation.
- **Interoperability.** Shared labels mean readers recognize conventions across collections. Recovered by a *shared catalogue* that collections select from and extend, rather than a closed set they must fit.

The guard is the load-bearing piece: open sets without admission discipline proliferate until no convention is shared, which is the other way to fail at being a framework.

## The invariant that stays closed: answerability

Universality cannot mean "any text." The boundary that keeps the framework coherent is that its artifacts are knowledge: each is answerable to something beyond itself and can therefore be wrong or stale. The relation varies — a claim answers to the world, a description to a system, a prescription to the outcomes of following it, an attributed position to what the party actually asserts, a capture to its source — but *having* such a relation does not. First-person commitment ("do I still believe this?") is one answerability relation among several, not the definition of the framework.

This yields an operational scope test instead of a genre list: a collection belongs in the framework iff its contract can state, non-vacuously, **what its artifacts answer to** and **what makes one stale**. A poetry collection cannot fill those fields; a stance-neutral debate map fills them differently than a methodology KB, but fills them. Maintenance is then universal in form — every artifact has revision conditions — while fully local in content.

## What else survives as universal

Only what derives from the consumer or from the second-order layer itself, not from any kind of knowledge: bounded context (economy pressure comes from the reader's architecture, so it applies to every contract — since [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md)); and the declaration obligation itself (a collection without a loadable contract is an operational defect regardless of its content).

## Evidence

Three instances of the same demotion, two shipped and one proposed, each keeping machinery while opening the set: types became path references, so the type set is open and collection-local (ADR 018); link vocabulary became collection-owned selections from a shared catalogue, replacing one universal set (ADR 019); the three [registers](./definitions/register.md) are proposed to become default text-contract profiles (open-ended-collection-text-contracts proposal). Status/lifecycle semantics are a predicted fourth instance: the note type's status field currently fuses structural lifecycle with first-person endorsement, which is one answerability relation hardwired one level too high.

## Caveats

Not every closed set is a content taxonomy. Sets fixed by the consumer's architecture or by the framework's own machinery (e.g., the syntactic shape of frontmatter, the existence of a lifecycle) may stay closed; the test is whether the set classifies *what knowledge can be* (open, demote to defaults) or *what the machinery is* (may stay closed). And the claim is about frameworks that *aim* at universality — a single-purpose KB loses nothing by hardcoding its profile; the cost appears only when the rules are exported.

---

Relevant Notes:

- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](./a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — contradicts: denies its exhaustiveness argument — the tripartition survives as defaults/attractors, not a partition; its formulation constraint and maintenance asymmetry are untouched
- [Title as claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — contrasts: first-person commitment is one answerability relation among several, not the framework's definition
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: why bounded-context economy is consumer-derived and therefore stays universal
- [Register](./definitions/register.md) — defined-in: register
- [Knowledge artifact](./definitions/knowledge-artifact.md) — defined-in: the answerability boundary that separates knowledge artifacts from arbitrary text
- [018-Types are path references to instruction docs](../reference/adr/018-types-are-path-references-to-instruction-docs.md) — evidence: shipped instance of the demotion — an open, collection-local type set
- [019-Collection-owned link vocabulary with per-destination outbound rules](../reference/adr/019-collection-owned-link-vocabulary.md) — evidence: shipped instance — collection-owned vocabulary selecting from a shared catalogue
- [Open-ended collection text contracts](../reference/proposals/open-ended-collection-text-contracts.md) — see-also: the proposed third instance (registers become default profiles)
