---
description: "A generator theory and the action-shaped methodology derived from it run as one system: fast path for covered cases, fallback to the retained theory for corner cases, promotion on recurrence"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining]
---

# Theory and methodology form a two-layer execution system

A general theory and the methodology worked out from it are not two artifacts, one of which supersedes the other. They run together as a single execution system with two layers.

- **The derived layer — the methodology — is the fast path.** It is worked out from the theory and shaped for action: cheaper to execute, and strictly less general. It covers a region of cases directly, without reasoning from first principles each time.
- **The generator layer — the theory — is retained and shipped *with* the methodology, not archived once the methodology exists.** A corner case — an input outside the methodology's covered region — is handled by dropping back to the theory and reasoning it out afresh. This fallback is an expected operation, not a failure of the methodology.
- **Recurrence is the learning signal.** When the same fallback reasoning happens repeatedly, its result is promoted into the methodology, which grows at its boundary, driven by use.

The whole arrangement only works if the executing agent actually holds the theory well enough to reason from it. The theory is not a dusty appendix kept for provenance; it is the live capability the fast path falls back onto.

## Why the theory can never be discarded

The tempting move is to treat the methodology as a finished compression of the theory and drop the generator. That fails because the corner-case distribution is open-ended: the space of inputs the methodology does not yet cover never closes, so the methodology never converges to total coverage. There is always a next case outside the current region.

If corner cases were finite and rare, you could enumerate them, fold them all in, and discard the theory. Because they are neither, fallback is a permanent, load-bearing part of the system, and the generator that fallback consumes must be permanently retained and permanently understood. This is the argument that turns "keep the theory around" from housekeeping into a structural requirement.

## What controls the derived layer: recomputable, checkable, stale-until-rechecked

The methodology's substantive content — the part genuinely worked out from the theory, as against the part discussed below — is a **recomputable copy**. It carries nothing the theory does not already entail under the declared consumer goal; it is a cached fast path over the theory, not a replacement for it. Three maintenance consequences follow, and they are the citable core of this note:

- **Checkable by re-derivation.** Fidelity is verified by reasoning the methodology's content out from the theory again and comparing — the same discipline any cached value owes its source, since [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).
- **Stale-until-rechecked on revision.** When the theory changes, every piece of the methodology recomputable from it is invalidated until re-checked or re-worked. The copy does not silently stay correct across a change in its generator.
- **Checkability graded by the theory's coherence.** The check is only as sharp as the theory is explicit. A crisp, well-stated theory admits a near-mechanical comparison; a tacit, incoherent, or judgment-heavy theory admits only a loose one. Being called "derived" does not make a prose methodology mechanically safe; it inherits exactly the checkability its generator affords.

Physics has worked-out names for the moving parts, borrowed here as loans from effective field theory, not as project vocabulary: **matching** (compute the corner case in the full theory at the boundary, commit the result into the methodology, and never recompute it), **cutoff** (the validity boundary a good methodology declares for itself rather than discovering by failure), and **correspondence** (the constraint running the other way — a revised theory must still reproduce the established methodology on its home turf, or one of the two is wrong).

Promotion, in these terms, **amortizes**: it caches a re-derivation that use has shown to recur, trading a one-time commitment against many future fallbacks. Cognitive architectures run the same move under the name proceduralization — ACT-R and SOAR compile the result of repeated deliberate reasoning into a fast production rule. That is the same trade, and it situates promotion as a form of learning that happens during use rather than during training.

The promotion criterion is testable: a corner case is promoted when its handling no longer requires consulting the theory — checkable by whether the agent can resolve it from the methodology alone.

## The coverage bet is not the correctness bet

Creating the derived layer at all is a bet, and it is a **coverage** bet, distinct from the correctness bet that any codified regularity already carries. Building an action-shaped layer pays only if the cases where it applies are frequent enough to beat the cost of building it, keeping it consistent with its generator, and routing around it. The payoff is cache economics: per-case saving times hit rate, against build cost plus upkeep plus staleness risk.

This bet fails differently from the correctness bet and is detected differently:

- **The correctness bet fails by wrongness.** The extracted regularity turns out not to be load-bearing; the artifact breaks under distribution shift. It is caught by the artifact producing wrong answers.
- **The coverage bet fails by uselessness.** The artifact is right but rarely applicable — most real cases fall outside its cutoff, so you maintain two layers while living in the expensive one. It is caught not by wrong answers but by the **fallback rate**: if corner-case traffic to the theory stays high, the fast path is not earning its keep. The bet is measurable, ongoing, and settled by use rather than by review.

Each individual promotion is a miniature of the same bet — is *this* corner case recurrent enough to promote? — which is why the rule is promote on recurrence, not on first sighting. Waiting for recurrence is the evidence-gathering that de-risks the mini-bet.

### The region choice is a falsifiable hypothesis

The bet has a discovery-shaped rider. Choosing *which* region to work the methodology out for encodes an empirical, falsifiable claim: that future cases will concentrate inside this region. So even when the methodology's content is entirely worked out from the theory — adding no claim the theory does not already contain — the *decision* of which region to cover smuggles in a hypothesis about the future case distribution. Two consequences: choosing the region is mechanically simple but theory-laden, because the selection criterion *is* the distributional hypothesis; and the fallback rate is not merely the bet's scoreboard but the running test of that embedded hypothesis. The two-layer system carries its own experiment.

## Caveat: not all of a methodology is worked out from the theory

Real methodologies are usually mixed. Robert Batterman's singular-limits point — that some structure appearing at a coarse level of description cannot be recovered by taking a limit of the finer theory, but is real and load-bearing there — has a plain analogue here. Part of a methodology is worked out from the theory and gets the maintenance regime above: recomputable, checkable by re-derivation, stale on revision. But part of it consists of organizing concepts that exist only at the methodology's own level of description. That part is not a recomputable copy of anything; it needs semantic review, not re-derivation, and revising the theory does not automatically invalidate it. The worked-out / not-worked-out split *within a single artifact* decides which regime each part gets — and that split is itself a testable claim about the artifact.

## Open Questions

- How to detect the mixed boundary in practice: given one methodology artifact, what signal separates its recomputable part from its level-of-description-native part before a theory revision forces the question?
- Whether the fallback rate is cheap enough to instrument to actually serve as the coverage bet's live adjudicator, or whether it stays a conceptual metric.

---

Relevant Notes:

- [spec mining is codification's operational mechanism](./spec-mining-as-codification.md) — extends: the special case where promotion crosses the codification line into a symbolic artifact, rather than staying prose-to-prose
- [codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — contrasts: same promote/demote dynamics, but there the general fallback layer is the LLM itself, always present for free, not a retained artifact that must be kept and understood
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: the instruction → skill → script trajectory is the symbolic-crossing form of promotion
- [both a narrowed and a use-shaped artifact trade generality for reliability, speed, and cost](./constraining-and-distillation-both-trade-generality-for-reliability.md) — grounds: the trade the fast path makes — cheaper and strictly less general than its generator
- [first-principles reasoning selects for explanatory reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: reach is what the theory layer contributes and the methodology gives up
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: the generality-vs-reliability/speed/cost decomposition the fast path trades along, and the facts-vs-theories reach axis the two layers sit on
- [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — extends: promotion-on-recurrence is deploy-time learning — a durable artifact updated across sessions during use
