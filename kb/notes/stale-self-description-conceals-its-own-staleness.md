---
description: "What artifact drift adds when it is reflexive: the process that would detect it consults the artifact that drifted, the trigger has no edit event to hook, and synchronization load scales with autonomy"
type: kb/types/note.md
traits: [title-as-claim]
tags: [self-improving-systems, artifact-analysis]
---

# Stale self-description conceals its own staleness

A system that retains claims about itself, keeps consuming them, and can change the aspects those claims describe needs a **synchronization path**: some route by which a change in the referent reaches the claim. The general form of that requirement is already settled here. Source-dependent artifacts [need lineage recorded against the source](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md), and [indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — a mechanism that note generalizes to specs, plans, and architecture documents when consumers treat them as exhaustive.

What follows concerns only what the **reflexive** case adds: when the described system, the describing artifact, and the agent that consumes both are one loop. Three things change, and none of them is a special case of ordinary documentation drift.

## The drift hides behind the artifact that drifted

A stale API document conceals the API. It does not impair the compiler, so the mechanism that would catch the discrepancy is untouched.

A stale self-description is consumed by the process that would detect its staleness. An agent navigating by a self map that misplaces a component does not go looking for the component; it reads the map, orients, and proceeds — which is exactly the suppression mechanism stale indexes describe, now applied to the artifact's own subject matter. The result is a fixed point rather than a gap: the error protects itself, because what it conceals is the evidence of its own drift.

This is why "the agent will notice" is not a synchronization path. Noticing is the capability the staleness degrades first.

## The trigger has no edit event to hook

The interruption-first criterion for source lineage assumes the upstream change is an edit to a nameable artifact, so the workflow can surface downstream targets at edit time. Self-description often has no such event. The referent is the system's own organization, and that moves through paths which are not edits to any source file: a tool installed, a configuration changed, a service restarted under a different policy, a dependency upgraded. The description of the system is now false and no artifact was edited.

So artifact-to-artifact dependency records under-cover the reflexive case. They catch the drift that arrived through an edit and miss the drift that arrived through an act. A synchronization path here needs its trigger attached to the operations that change the system, not only to writes against the sources a description was derived from.

## The modifier is the maintainer, and its rate scales with autonomy

In ordinary documentation drift the author of the change and the maintainer of the description are usually different actors, often at different times, sometimes with review between. Reflexively they are one process, so synchronization competes for attention with the very act that made it necessary, at the moment attention is committed elsewhere.

That coupling has a rate consequence. A more autonomous system modifies itself more often, so it generates synchronization load in proportion to its autonomy while its capacity to absorb that load is roughly fixed. The property usually treated as the goal is also what drives the maintenance burden.

## What the path must supply

Synchronization, not intercession over the same artifact. Revalidating a claim that still holds, revising it, regenerating it from source, superseding it, and retiring it all discharge the requirement — which is why this does not amend [reflective system](./definitions/reflective-system.md), where intercession is a capability within reflection rather than a condition on it.

Three parts, failing independently:

- a **trigger** that registers that the referent moved;
- a **dependency relation** identifying which claims a given change bears on — the [lineage](./definitions/lineage.md) record;
- an **operation** able to revalidate, revise, regenerate, supersede, or retire.

Soundness needs the trigger and the operation. Revalidating everything on every change is sound and expensive. The dependency relation buys **selectivity**, which makes it an efficiency requirement rather than a correctness one — the same split as [reusable verification](./verification-needs-a-typed-target-before-it-needs-an-oracle.md), where a check aimed at one artifact is sound but covers nothing new.

[Exo](../agentic-systems/reviews/exo.md) has the third and neither of the first two. Its self map is agent-editable through the same shell path as everything else, so the operation exists; nothing connects a code change to the claims describing it, and the documents holding its theory of itself sit outside the loop's consumption path. Capability without a wire, which is the configuration this note predicts is worst: an operation that is available, unexercised, and describing a system that moves daily.

## Scope

- The requirement is conditional on retention plus consumption. A system that re-derives its self-description each time it needs one has no artifact to synchronize; it pays elsewhere, in re-derivation cost and variance.
- Claims about immutable aspects are exempt, so the load scales with the mutable surface rather than with the system's size. A protected kernel is describable once.
- The self-concealment mechanism needs the description to be *consulted* by the detecting process. A self-description retained purely for external audit, never read by the system, degrades like ordinary documentation.
- Commonplace's snapshot-pinned [freshness baselines](../reference/freshness-architecture.md) are one witness to the three-part path, not evidence that this decomposition is the only one.

## Open Questions

- Whether a modification can reliably declare what it invalidates at the moment it is made, turning the trigger into a by-product of the change rather than a separate detection pass.
- Whether there is a rate condition — a modification frequency above which staleness accumulates regardless of mechanism, because revalidation cannot keep pace.
- Whether self-concealment can be broken from inside the loop at all, or whether detecting drift in a consulted self-description requires a process that does not consult it.

---

Relevant Notes:

- [Indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — grounds: the suppression mechanism this note applies reflexively, where the skipped fallback could expose evidence of the artifact's own drift
- [Source changes should surface downstream review targets](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — grounds: the general dependency-record requirement, and the edit-time trigger criterion the reflexive case escapes
- [Lineage](./definitions/lineage.md) — defined-in: the dependency record that supplies selectivity in the three-part path
- [Reflective system](./definitions/reflective-system.md) — grounds: why synchronization rather than intercession is the requirement
- [Verification needs a typed target before it needs an oracle](./verification-needs-a-typed-target-before-it-needs-an-oracle.md) — contrasts: the parallel soundness-versus-coverage split, there for checks and here for invalidation
- [Reflection buys addressability](./reflection-buys-addressability.md) — mechanism: why a retained claim can be revised selectively at all
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — mechanism: one cheap implementation of the trigger and dependency parts
- [Increasing computational autonomy relocates human effort to the frontier](./increasing-computational-autonomy-relocates-human-effort.md) — extends: the rate coupling, where the autonomy being pursued generates the maintenance load
- [Exo](../agentic-systems/reviews/exo.md) — evidenced-by: operation present, trigger and dependency absent, over a self map injected into every turn
