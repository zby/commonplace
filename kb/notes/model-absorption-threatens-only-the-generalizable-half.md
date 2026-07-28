---
description: "Absorption threatens content asserting facts about the world; content asserting facts about this deployment — its commitments, evidence, provenance, authority — has no channel into weights, so the halves decay on different curves"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [learning-theory, agent-memory, deploy-time-learning, foundations]
---

# Model absorption threatens only the generalizable half of a retention layer

Every external retention layer — a knowledge base, an agent-memory store, a repository of skills and conventions — faces the objection that improving models will simply internalize what it provides. The objection is sound, and it is bounded. It reaches exactly the content that some other party's copy would state identically, and nothing else.

## The cut is indexicality, not subject matter

Sort a retention layer's content by what its statements are *about*:

- **Generalizable content** asserts facts about the world: a technique, a mechanism, a domain regularity, a methodology. Nothing in it is indexed to this deployment, so anyone's copy would say the same thing.
- **Current local state** asserts facts about *this* system: what it has committed to, the evidence those commitments rest on, where they came from, and who may change them. Each statement is indexed to one deployment at one time.

The line does not follow subject matter. "Retry with exponential backoff" is generalizable. "This service retries with exponential backoff; adopted after the March incident; owned by the platform team" is local state, even though the technique inside it is textbook. A general thing can be *selected* locally, and the selection is local state about a general object.

## Why the generalizable half is on a clock

| | Generalizable content | Current local state |
|---|---|---|
| Present in some training corpus | yes, in some copy | no, by construction |
| A stronger model can supply it unaided | eventually | never |
| Right accounting | amortized: earns its keep before absorption | durable asset |

The generalizable half is absorbable because the training distribution samples the same facts from other sources; an artifact restating what the model already applies buys framing and retrieval convenience, not knowledge. Its value therefore runs on a clock, and the honest accounting is amortization — it must repay authoring and maintenance before the capability floor rises past it.

This is a different partition from the one in [the bitter lesson selects against unearned reach, not against structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md), and the two cross-cut. That note asks whether a generalization's claimed scope was earned, and finds that earned structure survives because scale converges on it. From a retention layer's side, converging on it *is* absorption: agreement, not replacement, still means the artifact stops being the reason the system behaves well. Earning reach protects the claim; it does not protect the copy.

## Three independent reasons the local half has none

**Nothing to derive it from.** Absorption is derivation at scale — a model recovering content from the world's text. But since [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md), a commitment adds resolutions no source determines: a decision among live options, one reading chosen from an admissible space. A model trained on everything ever written still cannot regenerate which option a team picked, because nothing entails it. Local facts that are not commitments — this cluster runs three shards — fail for the weaker sibling reason that they exist but never entered a corpus, being private or postdating the cutoff. Either way the gap is information, not capability, and capability cannot substitute for information the model was never shown. This reason is load-bearing because it makes no claim about substrates at all.

A model with a retrieval tool does reach these facts, which is not a counterexample but the claim restated: something outside the weights is holding them, and reading it is what the retention layer is for. What follows is externality to the model, not to the system.

**Currency.** Local state's use is that it is the *present* value of a mutable commitment. Even granting a channel — continual pretraining on the deployment itself — the retained thing must still be updatable at deployment pace and readable as what holds now, which is why [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md). Closing the channel relocates the store into a slower, coarser substrate rather than removing it, the same relocation [in-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) finds when continual learning is declared unnecessary.

**Authority.** A commitment must be citable, contestable, selectively revisable, and attributable to whoever made it, and parametric recall offers none of these handles, since [only explicit retention is durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md). [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) reaches the same survivor class from the opposite premise — abundant context rather than abundant capability — and concedes that an unbounded model "might know the facts behind" an authority-bearing constraint while the artifact still carries binding force the facts do not. This note removes that concession for local state: the model does not have the facts either. Successfully absorbing a commitment would destroy the properties that made it usable as one, so absorption here would be a loss rather than a saving.

The reasons are ordered by how little they assume. The first survives arbitrary model improvement and any change of substrate; the second and third bind even where a deployment-local training pipeline closes the first one's channel.

## Why two classes and not a finer carve

The tempting refinement sorts by function — competence scaffolding, state, authority, verification, context economy — and predicts that the first recedes while the rest persist. Those distinctions are real, but they cross-cut absorbability rather than refine it. A verification checklist encoding general technique is absorbable; one encoding what *this* project accepts as evidence is not, and the same split runs through every functional category, competence included. Function says what an artifact is for; indexicality says whether a better model could supply it unaided. Absorption asks only the second.

## What this predicts

The durable value of a retention layer concentrates in its local half. A layer of mostly general exposition sits on a decay curve set by model releases; one carrying decisions, their evidence, and their provenance does not, and the difference is structural rather than a matter of writing quality.

That makes mixed artifacts the cost centre. A document interleaving a general mechanism with what this project decided about it decays unevenly — general passages go redundant while local passages stay load-bearing — and there is no clean way to retire half a document. The same reasoning gives evidence and lineage retention a defence independent of their pedagogical value, since provenance is local state by construction: a second argument for the layering in [retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md).

It also changes how the objection should be answered. "Won't the model just know this?" is not a challenge to be met wholesale but a question to be routed by content class, and conceding it for the general half costs nothing.

## Scope

- Absorption is gradual, uneven, and never total. The claim is about which half faces the threat, not that general content is worthless the day a model learns it: retrieval cost, placement in a bounded context, and framing specificity remain reasons to keep a general artifact, and [the framework is often larger than the durable contribution](./the-framework-is-often-larger-than-the-durable-contribution.md) is the write-time discipline that follows.
- "Absorbed" here means the model can supply the content unaided, not that the content is latent somewhere in the weights — [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) is why the latter is the wrong operational question.
- The claim concerns what a model can *hold*, not what it can *use*. Stronger models make local state more valuable, not less, because more of it becomes actionable.
- The cut classifies content, not files, so it restores no foresight about artifacts. [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) denies that you can tell in advance which side a component sits on, and nothing here changes that: a real document mixes both classes, and deciding whether a given sentence is indexed to this deployment is a judgment made per passage.
- "Necessarily external" is relative to a fixed model artifact. A system continuously training on its own deployment closes the information channel for some local state; the currency and authority reasons still bind, so the retention layer moves rather than disappears.

## Open Questions

- Whether general-but-rare content forms a stable third class — absorbable in principle, not reliably held by any near-term model, and therefore worth retaining on the same footing as local state.
- Whether the absorption clock is forecastable at all. Absorption predictions in the wild are typically unfalsifiable as stated, and without a way to tell in advance which general content the next model generation will hold, amortized accounting stays a posture rather than a decision procedure.

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — grounds: supplies the strongest form of the first reason — commitments add what no source determines, so no derivation at any scale regenerates them
- [Only explicit retention is durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: supplies the authority reason; its comparison runs over representational form, which this content-class cut crosses
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — grounds: the timing argument the currency reason rests on
- [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — extends: reaches the same survivor class against unbounded context; this note supplies the capability-side argument and drops its concession that the model knows the underlying facts
- [The bitter lesson selects against unearned reach, not against structure](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — contrasts: partitions the same question by earnedness of reach, which cross-cuts indexicality — earned general structure is the most absorbable kind
- [Continual learning's open problem is behaviour, not knowledge](./continual-learning-open-problem-is-behaviour-not-knowledge.md) — contrasts: splits retention by consumption force where this note splits it by what the content asserts
- [The readable-artifact loop is the tractable unit for continual learning](./readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — extends: asserts this conclusion in passing to defend the natural-language half of its loop; this note is the argument behind that assertion
- [Theory-mediated self-improvement needs interpretation and retention](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: it concedes that scale may absorb the retention half and offers no rebuttal; this note supplies one for the part of that half which is indexed to the deployment
- [Retaining the episode keeps a distilled rule re-derivable](./retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) — extends: gives its episode/rule layering a second, absorption-based justification
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — grounds: production history converts to checkable form only at production time, which is why provenance cannot be recovered later by any reader, model included
- [In-context learning presupposes context engineering](./in-context-learning-presupposes-context-engineering.md) — extends: the same relocation move applied to the claim that continual learning is unnecessary
- [Retained artifact](./definitions/retained-artifact.md) — defined-in: the umbrella term for the state a retention layer holds
- [Claude Workstream Kit and Fable agent scaffolding](../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) — abstracted-from: a stronger model let the author delete checklists, compliance scripts, and sync layers while authority constraints and cited-evidence gates were kept
- [Lessons from building AI agents for financial services](../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) — evidenced-by: an unfalsifiable "models will absorb basic skills" prediction, the failure mode the content-class cut is meant to avoid
