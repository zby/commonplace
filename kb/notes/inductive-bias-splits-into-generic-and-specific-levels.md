---
description: "Inductive bias is necessary and splits into a generic bet that structure exists, shared by every learner, and a specific choice of which structure, where learners differ and addressability lives"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations]
---

# Inductive bias splits into a generic level shared by all and a specific level where learners differ

No learner generalizes without an inductive bias — an assumption, prior to the data, about which unseen cases resemble the seen ones. Tom Mitchell made this concrete for machine learning: a system with no bias can fit the training set in infinitely many ways and has no basis to prefer any extrapolation, so it cannot generalize at all ("The Need for Biases in Learning Generalizations", 1980). Wolpert's No Free Lunch result sharpens it into an impossibility: averaged over all possible target functions, every learning algorithm has identical off-training-set performance ("The Lack of A Priori Distinctions Between Learning Algorithms", 1996). Superior generalization on real problems is therefore never a property of the algorithm alone; it is the algorithm's bias matching the world. The bias is not optional overhead — it is the whole of what does the generalizing.

That bias decomposes into two levels, and keeping them apart is what the rest of this note buys.

## The generic level: structure exists at all

The **generic** bias is the bet that the target is not the NFL adversary's uniform noise — that there is regularity to find, that simpler hypotheses are more likely than complex ones, that the world is compressible. Solomonoff's universal prior is its formal limit: weight every computable hypothesis by `2^(-length)`, so shorter programs get more prior mass ("A Formal Theory of Inductive Inference", 1964). This is Occam's razor stated as a prior, and it is the assumption NFL says you cannot avoid paying for. Every learner that beats chance on real data makes this bet, and makes it equally. A convolutional network, a symbolic theorem prover, a human scientist, and a self-play policy all presuppose that their domain rewards compression; none of them could function in a world that punished it. Because the generic bet is universal, it cannot be the source of any *differential* advantage between learners — it is the price of admission, not a move in the game.

## The specific level: which structure

The **specific** bias is everything the learner commits to beyond "structure exists": *which* structure. A prior's concentration, a hypothesis class, an architecture's built-in symmetries, a feature set, a stated invariant or mechanism — these say not merely that the world is compressible but *how*. Translation invariance, temporal locality, causal modularity, "this quantity is conserved across the shift" are specific bets, each true in some worlds and false in others. This is the level where learners actually differ, and where a bias can be right or wrong about a particular problem while the generic bet stays untouched. No real learner holds only the generic level — the pure universal prior is uncomputable, and any implemented system commits to a specific class the moment it is built. The two levels are a decomposition of one bias, not two biases a system could hold separately.

## Addressability is a property of the specific level

The generic bet is not an object a learner represents and reads; it is presupposed by the act of generalizing. There is nothing there to inspect, criticize, or revise — a learner does not "believe harder" that structure exists. What can be made explicit, stated, checked, transferred, and selectively corrected is always a *specific* commitment: this invariant, this mechanism, this applicability condition. So [addressability — the affordance a reflective pathway adds to retention](./reflection-buys-addressability-not-compounding.md) can only ever touch the specific level. A parametric learner and a reflective one make the same generic bet; what distinguishes them is how each encodes its *specific* bias — one opaquely in weights, one in an artifact the system can read.

This locates the reach conjecture. [The claim that reflective addressability can make retention more sample-efficient off-distribution](./reach-makes-addressable-retention-sample-efficient-off-distribution.md) cannot be drawing on the generic bet, because every learner already holds it in full. If an addressable pathway wins the amortized evidence ledger, it wins because it represents its *specific* structural hypothesis in a form that can be retrieved, validated, and reused across a structured shift — not because it is any more committed to the world being compressible. The whole contest between pathways lives at the specific level; the generic level is common ground neither side can exploit.

## Scope

- The two-level split is a decomposition, not a ranking: the generic bet is doing indispensable work (it is exactly what NFL says cannot be skipped), it simply does the same work for everyone.
- Addressability of the specific bias does not make it *correct* — an explicit invariant can be wrong, and a legible specific bias that mismatches the world generalizes worse than an opaque one that fits. Reach is not warrant, and neither is legibility.
- NFL's "all problems" average includes anti-structured worlds; the generic bet is precisely the refusal to plan for those. It is falsifiable in principle and simply almost never worth doubting in practice — which is why it earns no differential credit.

## Open Questions

- Whether the generic/specific boundary is sharp or a gradient — a maximally broad specific prior shades toward the generic bet, and it is unclear whether any principled line separates "structure exists" from "this weak structure exists".
- Whether any part of the generic bet can itself be made addressable — a system that represents and revises its own compressibility assumption — which would collapse the two-level story rather than confirm it.

---

Relevant Notes:

- [Reach makes addressable retention more sample-efficient off-distribution](./reach-makes-addressable-retention-sample-efficient-off-distribution.md) — extends: takes the specific-level location established here and develops it into a falsifiable data-efficiency conjecture
- [Reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — grounds: the addressability affordance that this note argues can only apply to the specific level
