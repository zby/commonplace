---
description: "Proposal: generalize validator invalidation or imperative type extension only after explicit selectors and local mark cases prove reusable machinery"
type: kb/types/note.md
traits: [design-proposal]
tags: [type-system, kb-maintenance]
---

# Generalized validation invalidation and imperative extension

[ADR 050](../adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) shipped the small common execution model: validation is artifact-anchored, one library-owned run caches parsed artifacts and collection indexes, and the CLI only resolves targets and presents results. This proposal retains the two questions that implementation deliberately did not answer: when explicit invalidation selectors should become a general dependency mechanism, and how a collection-local type could own a deterministic dereferencing check.

## Current state (as of 2026-07-13)

`ValidationRun` evaluates ordinary per-artifact checks, tag-README marks, collection-scoped orphan detection, and collection structure through one result surface. It parses target artifacts once, builds one shared tag index per consulted collection, and builds the authored-link graph once for a collection target. The base → imperative type rules → schema sequence remains unchanged.

Target expansion is related but deliberately separate. `impacted_marked_tag_readmes` is still an explicit inverse selector: changing a tagged note pulls the corresponding marked tag-README into the run. There is no generic dependency vocabulary, old/new-state comparison, deletion handling, or schema-definition fan-out.

A type's intra-document deterministic rules remain authorable as JSON Schema. Its semantic rules remain authorable in the type-conformance review criterion. A collection-local type still cannot author a deterministic rule that dereferences other artifacts. The one current mark-shaped rule, `tag-readme`, is a framework type with framework Python enforcement.

## The remaining problems

### Incremental invalidation has one worked selector

Evaluation inputs and invalidation dependencies are different. A check may cheaply read a whole collection index while only tag membership changes can alter its result. Deriving a precise inverse from a coarse declaration such as "reads the collection" would over-invalidate; deriving it from current state alone misses removed tags, deleted files, and prior referents.

Schema checks expose the same future issue: their result depends on the note, type spec, schema, and referenced-schema closure, but editing a definition does not currently target every applicable note. This is a real dependency; it is not yet evidence that a generic engine is cheaper than another explicit selector.

### Local imperative ownership has no worked case

JSON Schema cannot dereference. If a future collection-local type declares a mark—a cached value recomputable from other artifacts—review cannot safely enforce it: [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). Yet allowing arbitrary KB-side code would turn an inspectable data substrate into an execution surface.

The extension gap is therefore narrower than "types need plugins": a local type may eventually need one constrained, deterministic, dereferencing primitive. No current local type does.

## Deferred options

### A. General dependency keys and inverse selection

A check could declare artifact, path-existence, frontmatter-field, tag-membership, or definition-closure dependencies, with the run deriving impacted anchors.

*For:* definition edits and cross-artifact changes become first-class invalidators; repeated selectors may share indexes and old/new-state handling.

*Against:* this is an incremental build engine. It needs deletion semantics, previous state, dependency closure, and a conservative fallback. One selector does not establish the right vocabulary.

### B. A declarative mark primitive

A type spec could declare a constrained recomputation such as `tag-members(index_key)` plus a comparison such as `every-member-linked`.

*For:* a local type could own a machine-checked mark without arbitrary code, and the primitive could expose precise invalidation keys.

*Against:* it is a new language designed from one framework example. Languages grow, and a premature primitive would make the example's accidental shape permanent.

### C. KB-side code hooks — rejected

Arbitrary hooks provide maximal reach but violate the commitment that the KB is inspectable data rather than executable code. No current demand justifies reopening that substrate choice.

### D. Collection-owned deterministic checks — no present demand

Collections own text contracts and type menus, not frontmatter semantics. Intra-document mechanical variation belongs in a local type and schema; semantic variation belongs in review. A future heterogeneous collection relation may challenge this boundary, but only after an honest artifact anchor and type owner fail.

## Forces

- **A schema cannot dereference.** This inherited limit keeps an imperative path necessary.
- **A mark must be machine-checked or absent.** Review cannot substitute for deterministic recomputation.
- **Evaluation reads do not determine precise invalidation.** Old state and deletions matter to inverse selection.
- **The KB is data, not code.** Extension should remain constrained and inspectable.
- **YAGNI.** The run context removed current execution duplication; neither remaining mechanism has more than one worked case.

## Adoption criteria

A general invalidation model is ready for its own ADR only after at least two unlike explicit selectors expose a stable shared vocabulary. Its prototype must handle old and new state, deletions, path-existence changes, and definition closures, or be explicitly conservative where it cannot.

A declarative imperative primitive is ready only when a collection-local type needs a mark that neither its schema nor its review criterion can safely enforce. The primitive must be designed from that case together with `tag-readme`, not from `tag-readme` alone.

Collection ownership remains closed until a mechanical relation is inherently collection-wide after attempting an artifact anchor and type owner.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why a mark requires deterministic recomputation
- [The validation contract](../validation-contract.md) — evidence: the shipped owner/mechanism boundary this proposal may eventually extend
- [ADR 050 — Validation runs share parsed artifacts and collection indexes](../adr/050-validation-runs-share-parsed-artifacts-and-collection-indexes.md) — partial-adoption: ships the artifact-anchored evaluation model while leaving invalidation and authoring generalization deferred
- [ADR 038 — Type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — evidence: the existing semantic extension path and why deterministic marks are the remaining gap
- [Collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) — rationale: the boundary collection-owned checks would have to challenge
- [First principles are inherited constraints, not design choices](../../notes/first-principles-are-inherited-constraints-not-design-choices.md) — rationale: separates the schema's inherited dereferencing limit from optional extension machinery
