---
description: Kirsch's barriers all mark cases where software carries decisions that must survive into future runs, users, and audits; ephemerality is safe only when that knowledge stays local
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, artifact-analysis]
---

# Ephemerality is safe where embedded operational knowledge has low explanatory-reach

Kirsch's [essay against the ephemeral software hypothesis](https://www.blackhc.net/essays/future_of_software/) names four structural barriers to treating software as disposable: edge cases discovered through deployment, state and integration surfaces, interface stability expectations, and ambiguity/auditability requirements. These look like separate engineering concerns, but they share a deeper structure: each is a case where the software embeds operational knowledge that [has explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — knowledge that transfers across runs, versions, users, or audit events. The explanatory-reach of the embedded knowledge, not the complexity of the code, is what makes ephemerality unsafe.

## Kirsch's barriers all describe cross-context transfer

The common structure is not "these systems are complicated" but "a resolution discovered once must keep applying elsewhere." [Explanatory-reach](./first-principles-reasoning-selects-for-explanatory-reach-over.md) is the word for that transfer. Software stops being safely disposable when it becomes the medium where those resolutions live.

**Edge cases** are post-deployment knowledge that transfers. A fix for a timezone edge case in billing applies to every future release of the billing system, and often to sibling systems handling the same data. Discarding the fix forces re-discovery — not just of the code, but of the explanation for why the edge case arises. The fix has explanatory-reach because the explanation does.

**State and integration surfaces** encode constraints that persist across versions. A migration handling a legacy column format embeds knowledge about how past and present schemas relate. That knowledge applies to every future migration touching the same data and often to other systems reading the same store. The constraint is structural, not accidental — it has explanatory-reach because the data model does.

**Interface stability** means the software has become a medium for other people's learned expectations. A consistent API response shape or UI behavior is operational knowledge that users and client systems have internalized. Regenerating the interface differently forces re-learning across every consumer. The explanatory-reach sits in the expectation, not the code.

**Auditability** demands that resolved ambiguities remain traceable. A spec saying "handle errors gracefully" admits many implementations; once deployed, the specific resolution becomes load-bearing for compliance and incident response. The resolution has explanatory-reach because external processes reference it.

## Explanatory-reach predicts where persistence pays

Explanatory-reach is not code size, sophistication, or business importance. A tiny tax patch can have high explanatory-reach if every invoice depends on it. A 200-line exploratory script can have low explanatory-reach if nothing depends on it after today. What matters is how many future contexts benefit from preserving a resolution rather than rediscovering it.

[Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md), but accumulation is only worth its overhead when what you'd accumulate has explanatory-reach. A one-off analysis script embeds operational knowledge — which columns to join, how to handle nulls — that is specific to this query. Discarding it is cheap because the next query needs a different resolution. A production billing service embeds knowledge — edge cases, migration history, audit trails — that transfers across releases, users, and regulatory events. Discarding it forces the same ambiguity to be re-resolved under pressure.

Kirsch's durable artifact stack is therefore not sentimental attachment to code. It is a way of storing high-explanatory-reach operational knowledge in a form future runs, humans, and systems can inherit.

## The boundary

This gives a cleaner prediction: **the ephemeral/malleable boundary sits where the same operational resolution must survive across contexts.**

- **Low-explanatory-reach zone (ephemerality safe):** one-off analyses, spike implementations, local scripts, prototypes. The operational knowledge fits the immediate context and does not transfer far. Re-derivation costs roughly the same as preservation.

- **Boundary zone:** tools that start local but pick up users, persistent state, integrations, or compliance obligations. The artifact may still be easy to regenerate, but the knowledge it must preserve is no longer local.

- **High-explanatory-reach zone (malleability required):** production services, shared internal tools, stateful systems, regulated workflows. The embedded knowledge persists across contexts. [Codification](./definitions/codification.md) is how it gets committed to durable, inspectable, testable artifacts. Re-derivation costs grow because more runs, people, and surrounding processes depend on the same resolutions.

Kirsch's [five-step malleable software model](https://www.blackhc.net/essays/future_of_software/) describes this trajectory in practice: a prototype starts with mostly local knowledge, then deployment discovers memory that must be carried forward.

## Connection to vibe-noting

The [vibe-noting](./vibe-noting.md) framing decomposes LLM-assisted work along inspectability and verifiability axes. Explanatory-reach does not replace those axes — it explains when inspectability becomes worth paying for. Inspectability is the mechanism; explanatory-reach is why that mechanism matters.

This sharpens the vibe-coding/vibe-noting parallel. Vibe coding works well in low-explanatory-reach zones: the code lives in an inspectable substrate, and the cost of discarding it is often tolerable. Vibe-noting is harder because its output is usually meant to transfer — a good note should help future humans and agents in contexts the original session did not anticipate. High-explanatory-reach knowledge work therefore needs a persistent inspectable substrate, or [ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) and every session starts from zero.

## What this framing does and doesn't explain

The explanatory-reach framing predicts *where* durability pressure appears but not *which artifact* should carry the knowledge. AI may expand the low-explanatory-reach zone by making some medium-explanatory-reach knowledge cheaper to re-derive from logs, traces, or tests — but that relocates the durable substrate rather than eliminating it. Kirsch's [falsification criteria](https://www.blackhc.net/essays/future_of_software/) test whether this relocation is happening at scale.

The asymmetry remains: AI can make re-derivation cheaper, but it cannot remove the structural explanatory-reach of constraints like data model compatibility, user expectations, or regulatory traceability. Somewhere, that knowledge still has to survive.

---

Relevant Notes:

- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — complements: the malleable software section names the whole-system framing that this note sharpens with explanatory-reach
- [Ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — foundation: accumulation is only worth its overhead when what you'd accumulate has explanatory-reach; this note adds explanatory-reach as the criterion that determines when the fork matters
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — foundation: Deutsch's reach concept (registered here as explanatory-reach) provides the vocabulary for why some operational knowledge transfers and some doesn't
- [Vibe-noting](./vibe-noting.md) — extends: explanatory-reach explains when inspectability becomes load-bearing for accumulation; low-explanatory-reach coding tolerates discard more often than high-explanatory-reach knowledge work does
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — grounds: codification is how high-explanatory-reach operational knowledge gets committed to durable artifacts; the arithmetic/vision-feature distinction parallels the high/low explanatory-reach boundary
- [Codification](./definitions/codification.md) — extends: the note reframes Kirsch's "malleable software" as systems that codify high-explanatory-reach operational knowledge rather than discarding it
- [The Flawed Ephemeral Software Hypothesis (Kirsch)](https://www.blackhc.net/essays/future_of_software/) — source: the four structural barriers reinterpreted as explanatory-reach indicators
