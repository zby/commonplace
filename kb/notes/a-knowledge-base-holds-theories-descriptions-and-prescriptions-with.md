---
description: "Why theory, description, and prescription set communicative and review priorities while content kind, production lineage, and path-relative authority remain independent"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
---

# Theory, description, and prescription profiles do not determine content kind, lineage, or authority

A text-contract profile classifies an artifact's communicative contribution and the quality its writing and review should protect. It does not classify what kind of operative content the artifact retains, how that content was produced, or what force a particular consumption path gives it. Commonplace uses three reusable defaults in an open profile library:

| Profile | Contribution | Quality priority | Reader question |
|---|---|---|---|
| Theoretical | Truth-apt claim, mechanism, or explanation | Assessable truth and explanatory-reach | Why does this hold, and when? |
| Descriptive | Economical account of what exists | Fidelity | What exists here? |
| Prescriptive | Direction for action | Executability and precision | What should the actor do, and how? |

These profiles are proposed as recurring attractors because consumer questions repeatedly take why, what, and how forms. This is a reason to keep reusable defaults, not evidence that the three are exhaustive, optimal, or prevalent across independently designed knowledge bases. A collection should adopt a profile when its orientation, quality priority, conventions, maintenance semantics, and link grammar travel together. Otherwise it should extend, replace, or write its own local contract.

Each collection's contract remains authoritative for its formulation rules and link grammar. In Commonplace's theoretical profile, for example, claims should be general and should stand without any one cited description. The profiles are [defined as open-ended text-contract bundles](./definitions/text-contract.md), while the [theoretical](./COLLECTION.md) and [descriptive](../reference/COLLECTION.md) collection contracts fix their priorities more precisely.

## The other axes are independent

Profile, content kind, production lineage, and behavioral authority answer different questions:

| Axis | Question | What it determines |
|---|---|---|
| Profile | What does this artifact contribute, and what should its writing optimize? | Formulation and review priority |
| Content kind | Which distinctions apply to this operative region—for example, belief-bearing theory or choice-bearing resolution? | The relevant evaluation and defeat questions |
| Lineage | Did the source and declared consumer goal determine this content, or did its author add something? | Ground truth and refresh versus supersession |
| Authority | Does this artifact advise or bind here? | Force on this consumption path |

The content-kind distinction is developed in [belief-bearing theories and choice-bearing resolutions are different kinds of system part](./design-proposals-differ-from-claims-in-kind-not-confidence.md). Its consequence here is simple: a theory can be inherited, derived, or authored abductively and then retained through commitment. In every case it remains truth-apt. Committing an abductive conjecture makes it a belief the system reasons from; it does not prove the conjecture, make it certain, or extend its scope beyond its evidence.

A choice-bearing design resolution arises only after applicable beliefs, requirements, and inherited or formal constraints have narrowed the space but still underdetermine a working design. Selecting among those residual live options is a commitment. This does not make every implementation region a choice: the same implementation can contain consequences determined by its inputs alongside committed resolutions those inputs did not determine.

That boundary is distinct from profile. Under the narrow lineage rule, [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md): derived regions remain answerable to their source, while a committed addition must later be replaced by another commitment or supersession. A theoretical note may therefore hold a derived, inherited, or committed belief. A descriptive reference artifact may record that a commitment was made or give a claim-preserving account derived from implementation. Notes are not a derivation class, and reference is not a commitment class.

Authority is path-relative too. The same theory can be consumed as [knowledge](./definitions/knowledge-artifact.md) when it supplies evidence or advice and as [system definition](./definitions/system-definition-artifact.md) when a runtime, evaluator, validator, instruction-loading path, or similar mechanism directly consumes its content with binding force. An instruction that merely cites the theory as rationale does not make the theory itself binding. A change in force does not change the theory's profile, truth-aptness, or lineage.

## The common path is characteristic and branched

The independent axes still produce a common pattern of dependency:

```text
derived theory ────────────────────────────┐
inherited theory ──────────────────────────┤
abductive conjecture ──retain by commitment┘
                                           ↓
                              truth-apt beliefs
                                           +
                 requirements + inherited/formal constraints
                                           ↓
                     ┌─────────────────────┴────────────────────┐
                     ↓                                          ↓
        determined consequences                       residual live options
                     │                                          ↓
                     │                               committed resolution
                     └─────────────────────┬────────────────────┘
                                           ├──→ prescription
                                           └──→ implementation

actual system, decision, or design object ─────→ faithful description
```

The upper alternatives converge as truth-apt beliefs. Determined consequences and committed resolutions can then inform either prescriptions or implementation. The final line is separate because a description follows its actual referent rather than occupying a mandatory stage after implementation.

This is a characteristic dependency witness, not a lifecycle. Artifacts can combine, skip, or reorder these surfaces. Not every prescription begins in theory, not every implementation region is a residual choice, and no arrow follows automatically from a profile or directory. Commonplace's [design-rationale surfaces](../reference/design-rationale-management.md) illustrate the requirements, constraints, residual-choice, and decision-recording portion while explicitly leaving transitions unenforced.

## Use each axis for its own decision

Profile sets the first review priority: assess theoretical work for truth conditions, evidence, counterexamples, scope, and reach; descriptive work for fidelity and economy; and prescriptive work for executability and precision. Content kind adds a different test. An abductive belief must retain its conjectural force and be reviewed against evidence and rivals. A residual choice must satisfy its requirements and constraints and expose its consequences. Shared adoption can give such a choice [coordination value](./definitions/coordination-value.md), but only where common use creates that value; enforcement alone does not establish it.

Lineage then decides maintenance. Refresh or re-review a derived region from its source. Replace a committed addition through a later commitment or supersession. Author dependency links from actual premises, sources, implementations, and operational needs. A theory change makes another artifact due for review only where a real dependency connects them. Finally, inspect authority on each consumption path rather than inferring it from profile, importance, canonicality, or filename.

One bounded rationale for the profile split is context compression. Since [context efficiency is a central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md), theory can preserve mechanism, truth conditions, and scope; description can preserve the minimum faithful state; and prescription can preserve executable direction while links or fallback sources retain omitted warrant. This is an inference about one benefit of distinct profiles, not a claim that context scarcity historically caused them, empirically validates them, or makes these three optimal.

The methodology-to-skill case is one bounded example. Methodology can retain reasons and scope while a skill reorganizes supported procedure into a context-saving fast path with the methodology as a live fallback. That establishes a real theoretical-to-prescriptive dependency, not whole-skill derivation. Ordering, defaults, operational detail, or coverage that the source plus consumer goal does not determine remain committed regions, and the case says nothing about skills produced from other sources.

## Commonplace's directory mapping is contingent

Commonplace assigns the theoretical profile to `kb/notes/`, the descriptive profile to `kb/reference/`, and the prescriptive profile to `kb/instructions/`. This placement makes the intended contribution and review priority visible. It does not turn directory names into content-kind, lineage, or authority declarations. In particular, `kb/notes/` is not where derivation lives, and `kb/reference/` is not where commitment lives.

## Open Questions

- Across independently designed knowledge bases, how often do these quality priorities covary, and what other stable profiles appear?
- After controlling for actual dependency, content kind, lineage, and authority, what additional behavior or maintenance burden does profile predict?
- What evidence threshold should govern retention and review of fragile or abductively committed theories?

---

Relevant Notes:

- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: the theoretical profile's explanatory-reach priority
- [Text contract](./definitions/text-contract.md) — defined-in: the open profile model and its default quality priorities
- [ADR 042: register becomes a default profile under open-ended text contracts](../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — evidenced-by: Commonplace's decision to keep the default profile library open and worked-case-gated
- [Skills derive from methodology](./skills-derive-from-methodology.md) — evidenced-by: a bounded methodology-to-prescriptive-fast-path dependency with a live fallback, not a claim of whole-skill derivation
