---
description: "The declared boundary under which Commonplace's self-improvement, reflectivity, and allocation attributions are assessed — what is inside, what is outside, and how to cite or depart from it"
type: kb/types/note.md
tags: [computational-model, self-improving-systems]
---

# The declared Commonplace frame

Self-improvement, reflectivity, and autonomy attributions are frame-indexed: the bearer is a bounded system, not a substrate, so an attribution is elliptical until its boundary is named — the semantics is stated in the [self-improving system definition's Provenance](../notes/definitions/self-improving-system.md). This note is the single citable declaration of Commonplace's own frame. Applications cite it instead of re-deriving the boundary; an analysis that needs a different boundary declares its own frame explicitly and names the departure, rather than silently drifting from this one.

## The boundary

**Inside:** the repository and its operative artifacts; the software and agents that consume them — commands, validators, the review store, harness-loaded agents; and designated maintainers acting in their established improvement roles.

**Outside:** arbitrary contributors, readers, and advisers; the model provider and its weights; inference infrastructure; hosting.

## The partition

Within the frame, the repository, commands, validators, review store, and agents are the computational components; designated maintainers are the human components. The partition reports actor allocation and nothing else — it changes neither membership nor reflectivity.

## Using the frame

- Any membership, reflectivity, closure, or allocation claim about Commonplace is read against this frame unless the claim declares a different one. The assessment horizon is declared per attribution; the frame fixes who and what, not when.
- Two consequences of the boundary are standing, not incidental: model weights sit outside, so the parametric form admits selection depth only (Commonplace can rebind a model, not inspect or edit weights); and computational-closure readings under this frame count human dependencies only — how a hosted model's dependence on outside inference infrastructure should read is an acknowledged open question in [the closure note](../notes/methodological-and-computational-closure-track-different-changes.md).

---

Relevant Notes:

- [Self-improving system](../notes/definitions/self-improving-system.md) — defined-in: the frame-indexed predicate whose ellipsis this declaration discharges for Commonplace
- [Reflective system](../notes/definitions/reflective-system.md) — defined-in: the boundary-parametric criterion assessed against this frame
- [Commonplace as a reflective self-improving system](./commonplace-as-a-reflective-system.md) — see-also: the classification and worked trace assessed under this frame
- [Methodological and computational closure track different changes](../notes/methodological-and-computational-closure-track-different-changes.md) — rationale: the allocation and closure readings that require a declared frame to be well-formed
