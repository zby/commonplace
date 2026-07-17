---
description: "A batched LLM-call protocol keyed by each unit's full composite identity, not position or a single axis, lets grouping strategy vary freely without protocol change"
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
---

# Full-identity keys decouple a batch protocol from its packing axis

When a system batches several independent units of work into one LLM call, there is usually more than one plausible axis along which to group them. A protocol that keys each response block by *position within one axis* — first item, second item, or "the note" alone with the other half of the identity implied by call context — locks the wire format to that axis. Supporting a second axis then means a second renderer, a second parser, and a second failure policy, because the grammar has no way to say which axis produced a given block.

Keying every block by the unit's **full composite identity** instead — for example `note_path :: gate_id` rather than an ordinal or a single-axis name — removes that coupling. One grammar, one renderer, and one parser work regardless of which axis groups units into a call, because coverage checking, ordering, and failure attribution never depend on position or on which axis produced the group. Batching becomes a **policy** choice made by the caller — which axis, how many units per call, whether axes mix — instead of a **protocol** choice baked into the wire format: recombining any axes already spanned by the key's components needs no format change. A genuinely new axis — one not yet a component of the key — is a different case: it still requires widening the key shape itself, not just choosing a different grouping of what the key already carries.

## Why this matters more, not less, for LLM calls

Self-identifying batch elements are old wisdom in ordinary batch APIs — request ids in JSON-RPC batches, aliases in GraphQL, explicit keys in map-reduce shuffles — where parsing is exact and cheap, so a positional convention often works well enough. It matters more for a batched LLM-call protocol, because parsing there is probabilistic reconstruction of a keyed structure from free text rather than a deterministic decode: the model can reorder, omit, or duplicate a block, and there is no independent index to fall back on if the grammar itself does not carry the key. A parser that must infer identity from position or from surrounding call context cannot recover cleanly from a single dropped or reordered block; a parser keyed on full identity can detect exactly which units are missing or duplicated without inferring anything from where a block happened to land in the stream.

## Scope

This is a claim about the **wire protocol** for batched call/response exchanges — what makes the grammar itself agnostic to grouping strategy. It says nothing about which axis, or which batch size, produces the best prompt quality or the most efficient context usage for a given task; that remains a separate, use-case-specific tradeoff to measure, not something the protocol choice resolves. Nor does it say the key encoding itself is free of coupling: a concatenated string key such as `note_path :: gate_id` reserves its delimiter and any structural sentinels out of every identity component's value space, and fixes the key's arity to the number of axes composed into it — real costs a caller adopting this pattern inherits, not degrees of freedom this note is asserting away.

## Open Questions

- Does the decoupling still hold when the *content* requested per block legitimately differs by axis — for example, a cross-item comparison field that only makes sense when grouping along one specific axis? A pure key-based grammar says nothing about whether the requested payload itself stays axis-invariant.

---

Relevant Notes:

- [029 - Review execution unified on (note, gate) pairs](../reference/adr/029-review-execution-unified-on-note-gate-pairs.md) — abstracted-from: the review-execution decision this note generalizes from, where a `note_path :: gate_id` key let note-packed and gate-packed jobs share one grammar, renderer, and parser
- [Decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md) — see-also: adjacent heuristics for what a scheduler exposes to a bounded call; this note is about the wire format for the response, not the content-selection choice
- [Agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — see-also: the same "don't collapse independent axes into one taxonomy" move, applied to a batch protocol's grouping strategy instead of orchestration architecture
