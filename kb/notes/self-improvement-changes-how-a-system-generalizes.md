---
description: "Retained lessons are learned inductive commitments and reach is the scope they operate over; reflection may make content and scope addressable without guaranteeing either is correct"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, self-improving-systems]
---

# Self-improvement changes how a system generalizes, not only what it knows or does

Self-improvement changes not only what the system knows or does, but how it generalizes from future evidence. Retained lessons that shape this generalization are **learned inductive commitments**, and **reach** is the scope over which those commitments operate. Reflection may make their content and scope addressable, without guaranteeing that either is correct.

The rest of the note unpacks those three sentences: why retention is a change to the learner and not just to behavior, what the commitment and its reach are, and what reflection does and does not add.

## A retained lesson is inductive bias acquired at runtime

No system generalizes without an inductive bias — an assumption, prior to the data, about which unseen cases resemble the seen ones. Mitchell made this concrete: a learner with no bias can fit its training set in infinitely many ways and has no basis to prefer any extrapolation ("The Need for Biases in Learning Generalizations", 1980). Wolpert's No Free Lunch result sharpens it into an impossibility: averaged over all possible target functions, every learning algorithm has identical off-training-set performance ("The Lack of A Priori Distinctions Between Learning Algorithms", 1996). The bias is not overhead; it is the whole of what does the generalizing.

A lesson retained by an improvement pathway joins that bias. Once kept, it stands prior to the system's future evidence: the next episode is read through it, extrapolations compatible with it are preferred, and candidates it excludes are never generated. Retention is therefore not only a change in what the system does — it is a change in the learner, and its effects run forward through everything the system learns next. A self-improving system is, through its retention step, continuously rewriting its own inductive bias.

One boundary is fixed. The generic half of any bias — the bet that structure exists at all, that the world is compressible — is presupposed by the act of generalizing, held equally by every learner, and not itself learnable: no lesson could teach it, and no retained artifact states it. Every learned commitment is therefore a *specific* commitment — which structure, which invariant, which applicability condition — and everything below about reach and addressability lives at that specific level.

## The commitment threshold is cumulative retention

Not every retained change is a commitment. [Reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) grades retention as operative, cumulative, and addressable; the commitment threshold is the middle grade. The Homeostat's surviving setting is operative only — it steers behavior, but the next round of variation is a blind draw the setting cannot inform, so it commits the system to nothing about future evidence. A parametric learner's weights are commitments in full: they parameterize everything the system makes of what it encounters next — cumulative by construction, and opaque. Addressable retention adds the reflective grade: the commitment is also an object a process inside the boundary can read.

"Learned inductive commitment" thus names cumulative-or-better retention viewed from the generalization side. The grades classify what the system can do *to* a retained change; the commitment vocabulary asks what the retained change does to the system's future learning.

## Reach is the scope of operation, not of validation

A commitment operates wherever the system brings it to bear, and that scope — its **reach** — is normally wider than the evidence that produced it. The asymmetry is the point: a lesson worth retaining earns its keep on episodes unlike the one it came from, which is what Deutsch names when a good explanation "applies far beyond the problem that produced it" (*The Beginning of Infinity*, 2011).

Reach must be kept apart from the reach of an oracle, [which bounds warranted autonomy](./warranted-autonomy-is-bounded-by-oracle-reach.md): oracle reach is the scope over which validation is available at the required confidence. A commitment's reach routinely exceeds the reach of whatever oracle accepted it — the commitment was evaluated against the evidence in hand at acceptance, and operates over its full scope ever after. That gap is structural, not a defect to engineer away, and it is why a commitment can operate confidently far beyond anywhere it was checked. Reach is not warrant.

## Reflection may make content and scope addressable — separately

Route retention through a [causally connected self-representation](./definitions/reflective-system.md) and the commitment's **content** — what it claims — becomes addressable: it can be stated, criticized, revised selectively, and carried to problems other than the one it came from.

**Scope** is a distinct aspect, separately addressable or not addressable at all. Reflection is aspect-bounded — the self-representation's vocabulary determines which questions the system can formulate about itself — so a commitment's applicability conditions are addressable only if boundaries are among the represented aspects. Content-addressable-but-scope-opaque is therefore a real grade, not an edge case: a perfectly legible rule whose boundary is nowhere stated over-generalizes as silently as a weight update. A system that retains lessons as prose can be reflective about what its commitments say while staying blind to where they stop applying.

For a commitment retained in an artifact, one further bound applies: the causal wire is discovery, so the commitment operates only where retrieval surfaces it — [retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md). Its effective reach is its scope intersected with the retrieval wire. A parametric commitment needs no such step: resident in the operative substrate, it operates automatically over everything the system does — an advantage of exactly the kind opacity buys.

## Addressable is not correct

Making a commitment legible makes neither its content true nor its scope right. An explicit invariant can be wrong; a stated applicability boundary can be drawn too wide; and a legible commitment that mismatches the world generalizes worse than an opaque one that fits. What addressability changes is the error's handles, not its rate: a wrong commitment that can be read can be found, blamed, narrowed, or revised in place, where a wrong weight update can only be trained over or rolled back wholesale. Whether those handles convert into a measurable adaptation advantage is not settled here — [addressable hypotheses may reduce target data under structured shifts](./addressable-hypotheses-may-reduce-target-data-under-structured-shifts.md) stakes that as a falsifiable conjecture, and it fails clause by clause when the stable structure is absent, the commitment wrong, or retrieval misses.

## Scope

- Commitments need not be learned. An architecture's built-in symmetries and a designed hypothesis class are specific inductive commitments fixed at construction; this note is about the retained kind, which self-improvement adds on top. The location claim — reach and addressability attach to specific commitments, never the generic bet — covers both.
- Reach, warrant, and addressability are three independent properties of one commitment: it can be general without being justified, justified while narrow, and either while opaque or legible.
- Reach here is the scope over which a commitment *operates*, whether or not correctly; how far it operates correctly is reach and warrant together. The definition deliberately leaves correctness out, because the mismatch between where a commitment operates and where it holds is exactly what needs a name.

## Open Questions

- Whether the generic/specific boundary is sharp or a gradient — a maximally broad specific commitment shades toward the generic bet, and no principled line may separate "structure exists" from "this weak structure exists".
- Whether scope can be made a first-class represented aspect cheaply — retention formats that force an applicability boundary at write time — and what that costs in lessons that then go unrecorded.
- Whether a commitment's reach can be estimated from its addressable form before any shift tests it — whether legibility supplies *evidence* about reach, or only a handle on reach established some other way.
- Whether any part of the generic bet can itself be made addressable — a system that represents and revises its own compressibility assumption — which would collapse the learned/presupposed boundary rather than confirm it.

---

Relevant Notes:

- [Reflection buys addressability, not compounding](./reflection-buys-addressability-not-compounding.md) — grounds: the retention grades whose middle grade this note names the commitment threshold, and the addressability affordance reflection adds
- [Reflective system](./definitions/reflective-system.md) — defined-in: the causally connected, aspect-bounded self-representation through which a commitment's content and scope become addressable
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the improvement pathway whose retention step this note claims rewrites the learner's inductive bias
- [Addressable hypotheses may reduce target data under structured shifts](./addressable-hypotheses-may-reduce-target-data-under-structured-shifts.md) — extends: turns the handles addressability gives a correct, reach-covering commitment into a falsifiable target-data conjecture
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: the discovery wire that bounds an artifact-borne commitment's effective reach
- [Warranted autonomy is bounded by oracle reach](./warranted-autonomy-is-bounded-by-oracle-reach.md) — contrasts: oracle reach is the scope of validation where commitment reach is the scope of operation, and the gap between them is why reach is not warrant
- [Ashby, Design for a Brain — ultrastability](../sources/ashby-design-for-a-brain-ultrastability.md) — evidence: the operative-only floor — retention that steers behavior while committing the system to nothing about future evidence
