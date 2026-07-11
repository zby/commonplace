---
description: "Definition — a text contract is the binding requirement a collection's COLLECTION.md declares; a profile is a named, proven bundle of contract features a collection may adopt, extend, or replace"
type: kb/types/definition.md
tags: [document-system]
---

# Text contract

The binding requirement that every writable collection's `COLLECTION.md` declares: orientation (what the artifacts do), quality goal, title and description conventions, any attribution/evidentiality requirements, maintenance semantics, and outbound link grammar. A **profile** is a named, proven bundle of text-contract features a collection may adopt wholesale, extend, or write from scratch instead of. Three profiles are this KB's defaults:

| Profile | Orientation | Quality goal | Title style |
|---|---|---|---|
| **Theoretical** | Claims about what is true | Reach | Claim |
| **Descriptive** | Accounts for what exists | Fidelity + economy | Topical |
| **Prescriptive** | Directs what to do | Executability + precision | Imperative |

In this KB, the three default profiles map to collections: `kb/notes/` (theoretical), `kb/reference/` (descriptive), `kb/instructions/` (prescriptive). This is a design choice — a text contract could also be encoded in types, metadata, or convention rather than collection placement. Directories work because they make conventions enforceable by path and visible to tooling.

The profile set is **open-ended, not exhaustive**. Why/what/how are strong recurring attractors — every question a consumer asks tends toward "Why is X a good idea?", "How does X work here?", or "How do I do X?" — and the three default profiles are proven, worked-case-tested bundles kept because they cover most collections, not because they partition the space. A collection whose work needs a different quality bar (for example, a dialectical/evidential contract for stance-neutral evidence mapping) writes its own contract rather than being argued into one of the three; new profiles are promoted to the shared library only after surviving a worked case, the same guard [link vocabulary](../../reference/link-vocabulary.md) growth uses. See [ADR 042](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) and the [profile catalogue](../../reference/text-contract-profiles.md) for the currently shipped set.

Profiles are orthogonal to operational roles (what an artifact *does* in the system — evidence, executable instruction, generated report, routing surface). A `note` type in `kb/notes/` uses the theoretical profile; the same type in `kb/reference/` uses the descriptive profile. Profile × type gives the full picture.

Two properties made the original three-way distinction real, and they remain features of specific profiles rather than of the taxonomy: the **formulation constraint** (the theoretical profile's theories must be statable in general terms, without referencing a particular system) and **maintenance asymmetry** (the theory → prescription → description flow: changes flow downstream from theory-profile artifacts through prescriptive ones into descriptive ones).

## Scope

Use **text contract** when the question is what a `COLLECTION.md` is obligated to declare — orientation, quality goal, title/description conventions, attribution requirements, maintenance semantics, link grammar. Use **profile** when naming a specific proven bundle (theoretical, descriptive, prescriptive, or a newly promoted one) a collection adopts by reference instead of writing its contract from scratch.

Text contract is collection-facing vocabulary. `kb/notes/`, `kb/reference/`, and `kb/instructions/` each declare a text contract — by adopting a default profile — so agents can infer the right writing goal before drafting or revising.

## Exclusions

Text contract is not type. A `note` type can appear under multiple text contracts; its type says what structure the artifact has, while the collection's contract says what kind of knowledge it is trying to carry.

Text contract is not trait, status, or [behavioral authority](./behavioral-authority.md). Traits are review-routing properties, status is lifecycle/commitment state, and behavioral authority records what force a retained artifact has when consumed.

Profile is not a closed enum. Do not treat "theoretical, descriptive, prescriptive" as an exhaustive list a fourth collection must be argued into — it is a starting library any collection can extend, per ADR 042.

## Misuse Cases

- Treating `theoretical`, `descriptive`, and `prescriptive` as document types rather than content-mode profiles.
- Treating the three default profiles as exhaustive — arguing a genuinely different quality bar into one of the three instead of writing (and, if it proves out, promoting) a new profile.
- Assuming a prescriptive-profile artifact always has high behavioral authority. A procedure may be advisory if no system loads or enforces it.
- Applying theoretical-profile title conventions to descriptive reference docs, producing claim-shaped titles where fidelity and scanability matter more.

A profile shapes link vocabulary through defaults, not inheritance. Each default profile has a characteristic link grammar — inference labels (extends, grounds, mechanism, contrasts) for theoretical, structural labels (part-of, implements) for descriptive, operational labels (composition, precondition, invokes) for prescriptive. These are *defaults* offered as starting templates when a new collection is authored; the authoritative home of a collection's outbound grammar is its own `COLLECTION.md`, not the profile. Collections can diverge from their profile's default when their work requires it.

Cross-contract links use a shared, smaller vocabulary (rationale, evidence, procedure, operates-on, defined-in) drawn from a common catalogue. A reader crossing a collection boundary typically has a different unmet need (operational vs. evidential vs. definitional) than one moving within a collection, and both endpoints need to recognise the label — so the vocabulary is shared across collections rather than owned by any single one.

---

Relevant Notes:

- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — foundation: the argument for the three default profiles' formulation constraint and maintenance asymmetry, revised to an attractor claim rather than an exhaustiveness claim
- [ADR 042: register becomes a default profile under open-ended text contracts](../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — rationale: the decision that retired the closed taxonomy and opened the profile set
- [Text contract profiles](../../reference/text-contract-profiles.md) — part-of: the catalogue of currently shipped profiles, which collections use each, and which ADR promoted it
- [distillation](./distillation.md) — enables: distillation connects profiles through the theory → prescription → implementation → description chain
- [constraining](./constraining.md) — co-equal mechanism: orthogonal to profiles but interacts — prescriptions are more constrained than theories
