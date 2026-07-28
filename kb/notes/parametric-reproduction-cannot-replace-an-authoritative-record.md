---
description: "A model can learn a mutable authority-bearing record; the copy cannot replace it. Substitution loses currentness, citability, contestability, selective revision, and attribution — so the record stays load-bearing after its content is learned"
type: kb/types/note.md
traits: [title-as-claim]
tags: [agent-memory, foundations]
---

# Parametric reproduction cannot replace an authoritative mutable record

The absorption debate runs together two events. *Reproduction*: a model, trained on a record, can state its content unaided. *Substitution*: the record is retired and parametric recall stands in for it. Reproduction is harmless — a copy in weights takes nothing from the record it copies. Every cost appears at substitution, and the costs are exactly the properties that made the record usable as an authority:

- **Currentness** — the record holds what is operative *now*; weights hold a snapshot as of a training cut. For mutable state, recall answers a question about the past by default, which is why [deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md): the store must be updatable at deployment pace.
- **Citation** — a record has an address that can be quoted, linked, and audited; recall has no stable object to point at.
- **Contestability** — a record can be disputed, amended, and annotated; recall can only be contradicted.
- **Selective revision** — one commitment can be edited in place, while a weight-borne copy entangles with everything else learned, since [only explicit retention is durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md).
- **Attribution** — who adopted this, under what authority, superseding what; recall reproduces the proposition stripped of its provenance.

So the durable role of a retention layer is not exclusivity of information — [unobserved local information cannot be recovered by capability alone](./unobserved-local-information-cannot-be-recovered-by-capability.md) is the narrower informational claim, and it ends once the record enters a training stream. The durable role is authority and currency: being the place where "what holds now, and on whose say-so" has an answer. A model that has learned every record makes the layer's expository copies redundant and its authoritative records more consulted, not less — more of what they license becomes actionable.

The hardest case makes the distinction sharp. Suppose a repository-specific adapter is retrained after every accepted decision, so the model always reproduces current local state, while signed decision records remain external. Substitution has still not occurred: the records are what the retraining reads from, the authority a dispute appeals to, and the object a revision edits. The adapter is a cache of the record layer, and a cache does not replace its source of truth.

## What this licenses

A routing rule, not a survival forecast: content that is stable, repeated, and authority-free is a candidate for weights — or for deletion once models supply it reliably; content that is volatile, local, auditable, or authority-bearing belongs in an explicit record no matter how much of it the model knows. [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) reaches the same survivor class from the context side: an unbounded model might know the facts behind a binding constraint while the artifact still carries the force the facts do not.

## Scope

- The claim covers mutable, authority-bearing records. An immutable, authority-free exposition — a tutorial, a general mechanism writeup — has no substitution cost beyond fidelity, and is the genuinely absorbable case.
- Nothing here says parametric reproduction is worthless: a model that has internalized the record layer navigates it better and needs less of it quoted into context. The claim is only that reproduction does not retire the record.
- Together with [unobserved local information cannot be recovered by capability alone](./unobserved-local-information-cannot-be-recovered-by-capability.md), this note replaces a deleted predecessor that fused the two claims into a categorical "local state is never absorbed" (full-pass `20260728T121249Z-a3f7`). This note owns the half that survived contact with the continual-training counterexample.

---

Relevant Notes:

- [Unobserved local information cannot be recovered by capability alone](./unobserved-local-information-cannot-be-recovered-by-capability.md) — contrasts: the neighbouring informational claim, which holds only until the record is learned; this note holds after
- [Only explicit retention is durable, writable, and addressable at once](./only-explicit-retention-is-durable-writable-and-addressable.md) — grounds: the property comparison behind the substitution costs
- [Deploy-time learning is the missing middle](./deploy-time-learning-is-the-missing-middle.md) — grounds: the update-pace argument behind currentness
- [System-definition artifacts are crystallized reasoning under context scarcity](./system-definition-artifacts-are-crystallized-reasoning-under-context.md) — extends: the same survivor class reached from context abundance rather than capability abundance
- [Retained artifact](./definitions/retained-artifact.md) — defined-in: the umbrella term for the records a retention layer holds
- [Agent-R](../agent-memory-systems/reviews/agent-r.md) — evidenced-by: checkpoint-level learning with no runtime retrieval store loses per-lesson provenance, targeted recall, and invalidation at consumption
- [Exo](../agentic-systems/exo.md) — evidenced-by: a running system that keeps canonical state, lifecycle, and the record of what was tried protected beneath a fully rewritable executor
- [We should take text optimization more seriously](../sources/we-should-take-text-optimization-more-seriously.ingest.md) — evidenced-by: argues the same routing — stable repeated information toward weights, volatile and auditable information in text
- [Claude Workstream Kit and Fable agent scaffolding](../sources/claude-workstream-kit-fable-agent-scaffolding.ingest.md) — abstracted-from: a stronger model let the author delete checklists and compliance scripts while authority constraints and cited-evidence gates were kept
