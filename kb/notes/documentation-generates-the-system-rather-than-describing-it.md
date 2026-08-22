---
description: "Attempted recovery, run per unit of content and in both directions, is a discriminator available before the first silent mismatch — and it finds the documentation's load-bearing part is what the system was worked out from, not what describes it"
type: kb/types/note.md
traits: [title-as-claim]
tags: [artifact-analysis, kb-maintenance]
---

# For its load-bearing part, documentation generates the system rather than describing it

Which artifact is the source of truth, the running system or the document about it? The question is usually answered once, for the whole pair, and answered in the system's favour: code is what actually runs, documentation is a description that can only be accurate or stale. That framing leaves the pruning question unanswerable, because every document then looks equally optional — and it answers at the wrong granularity.

The answer belongs to units of content, not to artifacts, and direction of recovery settles it. For each thing a document says, ask whether the running system can faithfully regenerate it. Where it can, that content is a **cache** of the system. Where it cannot, and part of the system was worked out from it, that content is a **generator**, and the derivation ran from the document to the system.

What follows from the split is already settled: [commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) works out the disposal consequence — deleting recoverable content costs a bounded recomputation, deleting content nothing recovers is an irrecoverable loss of the only record — and establishes that regime membership attaches to a region of an artifact rather than to the file. This note takes that split as given and supplies two things it leaves open: a discriminator that can be run before the boundary announces itself, and what that discriminator finds when the pair under test is a system and its own documentation.

## Attempted recovery is a discriminator available before the first mismatch

The test is to try the regeneration and inspect what comes back. Faithful means the regenerated content would support the same decisions the original supported, not that a competent reader could produce something plausible on the same subject. Rejected alternatives are the sharpest probe, because a decision not taken leaves no trace in the artifact at all: a document recording what was considered and refused is holding something no recovery reaches.

Two questions this answers were previously open. The commitment argument notes that "nothing detects a commitment misfiled as a derivation except its first silent mismatch" — attempted recovery is such a detector, costly and judgment-bearing but available in advance of the mismatch. And [the two-layer execution model](./theory-and-methodology-form-a-two-layer-execution-system.md) asks what separates an artifact's derived part from its level-native part before a revision forces the question; its candidate signal is behavior under distribution shift, which requires waiting for the shift. Attempted recovery requires only the two artifacts.

It also does not require the roles to be known in advance, which matters because a document's nominal role does not settle its actual one. A design document written after the fact by reading the implementation is a cache wearing generator labels, and that is the dangerous case: its framing invites the trust only a generator earns. Run the recovery in both directions and the direction that succeeds reports which artifact is derived, whatever the headings claim.

## What the system cannot give back

Building a system from a design drops the warrant for choices, the branches considered and refused, the boundary of cases the design claims to cover, and the conjectural status of decisions made on a guess. Running code exhibits behavior; it does not distinguish a deliberate commitment from an accident nothing has hit yet, which is one component of why [exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md). The subtraction is structural rather than a documentation failure — the same one that [factors the reasoning out of a skill and leaves the procedure](./skills-derive-from-methodology.md).

So a system's documentation, once the recoverable content is set aside, consists of the content the system was worked out from and cannot reproduce. That is the title claim: the part that survives the cut is generative, and for that part the derivation runs document to system rather than system to document.

Calling the system a compilation of its documentation overstates the relation. That metaphor implies a mechanical transformation, and there is none here: [progressive constraining](./progressive-constraining-commits-only-after-patterns-stabilize.md) shows the crossing is a projection another pass would resolve differently, and the skills case shows the medium and consumer need not change at all. What survives the metaphor is only the subtraction, which is enough for the criterion.

## Both directions run at once, so no artifact wins globally

The inversion is scoped, and the mirror claim holds on the other side. Building the system also *adds* — resolutions the documentation left open arrive in the running artifact as content the document never determined, and the commitment argument's conclusion is that the system, not its spec, is ground truth for those. Nothing recovers them from the documentation either.

A system and its documentation are therefore bidirectionally irrecoverable: each holds content the other cannot regenerate. Asking which one is the source of truth forces a wrong answer for half the content, which is why both "regenerate the docs from the code" and "regenerate the code from the spec" feel nearly right and both quietly destroy something. The mixed boundary the two-layer model asks about is not only a line inside one artifact; it is recovery running in opposite directions across the same pair at the same time, and the granularity at which the question is well-posed is the claim, not the file.

## A generator is only load-bearing while the change loop reads it

Generator status is a claim about a live relation, not a permanent property of text. Content generates the system because future versions will be worked out from it, and that requires whoever changes the system to read it and be able to act on it. A change loop that consults only the code has no path back, and the content that nominally generates the system generates nothing.

Such content does not thereby become cuttable — it is still unrecoverable, so cutting it is still an unbounded loss. It has moved from load-bearing to archival, and the repair belongs to the change loop rather than to the document. This mirrors the two-layer model's requirement that the generator layer stay reachable in the effective execution context: a theory retained only for provenance has stopped being a fallback. The diagnostic is the same in both settings — watch whether the loop ever falls back, and read a generator that is never consulted as a routing defect rather than as evidence the content was surplus.

## Scope

The criterion partitions; it does not promise both partitions are occupied. A system genuinely built code-first — an exploratory prototype, a script whose design space was never articulated — has no generator documentation, and for it "the code is the source of truth" is literally correct rather than a default worth contesting. The title claim is universal about the load-bearing part wherever one exists, and a system with none is the predicted case rather than the awkward one.

Recoverable content is cuttable, which is not the same as worth cutting. A cache can earn its keep as an access accelerator, and for a model reader it often does, since [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md). The criterion says the decision about a cache is an economic one bounded on the downside, while the decision about a generator is not economic at all. Kept cache content carries its own hazard when the system it describes is the one reading it, because [stale self-description conceals its own staleness](./stale-self-description-conceals-its-own-staleness.md).

Recoverability is separate from correctness. A generator can be wrong and a cache can be accurate; nothing here says unrecoverable content deserves belief, only that losing it is not undoable.

## Open Questions

- Attempted recovery can return a false positive when a competent reader reconstructs a plausible rationale the system does not contain, and post-hoc reconstruction is hard to tell from recovery by inspecting the output alone. Is there a cheaper discriminator than fidelity review, beyond the rejected-alternatives probe?
- Where a system was worked out from a generator and is then edited directly, the two diverge with no event to hook. Does detection require re-running the recovery test on a schedule, or can the edit surface carry the interrupt?
- Generator content resists mechanical checking, so it inherits managed staleness. Is there a class of it — declared coverage boundaries, for instance — where the system can be tested against the claim, giving a deterministic check running in the direction the cache-side rule cannot reach?

---

Relevant Notes:

- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — extends: takes its derivation/commitment split and disposal asymmetry as given, supplies the pre-mismatch discriminator its open question asks for, and applies both to the system–documentation pair
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](./theory-and-methodology-form-a-two-layer-execution-system.md) — extends: answers its mixed-boundary question with a test runnable now rather than one waiting on distribution shift, and carries its live-fallback requirement over to the change loop
- [Skills derive from methodology](./skills-derive-from-methodology.md) — exemplifies: the methodology-to-skill instance of the same subtraction, where the warrant is factored out and the source stays live as fallback
- [Exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md) — grounds: the artifact cannot report on the requirement it satisfies, one component of what the derivation drops
- [Progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — grounds: the crossing to a running artifact is a projection rather than a mechanical transformation, which bounds how far the compilation metaphor carries
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: why cuttable cache content is often still worth keeping when the reader is a model paying the recompute
- [Stale self-description conceals its own staleness](./stale-self-description-conceals-its-own-staleness.md) — contrasts: the same pair read in the cache direction, where the failure is the description drifting from its referent rather than the system diverging from what it was worked out from
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — enables: the lineage record that lets a change loop find the generator content a system edit puts at risk
