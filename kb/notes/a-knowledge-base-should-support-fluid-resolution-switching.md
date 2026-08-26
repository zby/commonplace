---
description: "Defines resolution-switching as movement among KB views with different scope and detail, then inventories the mechanisms and limits of that qualitative criterion"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations]
---

# A knowledge base should support fluid resolution-switching

A reader using a knowledge base alternates between broad views that expose
possible routes and narrower views that supply detail. This note calls movement
between those views **resolution-switching**. Resolution here means the scope
and detail exposed by a view, not an intrinsic abstraction rank assigned to an
artifact.

A knowledge base should make task-relevant switches inexpensive in both
directions. A broad view should lead to specific claims or evidence. A detailed
artifact should leave a discoverable route back to wider organizing context.
This is a qualitative design criterion, not yet a metric or a claim that every
task needs the same sequence of views.

## Commonplace mechanisms

**Titles, descriptions, and bodies expose different amounts of detail.** A
claim title carries the assertion. A description adds a fixed routing cue. The
body supplies the mechanism, qualifications, and evidence. Because a
[title-as-claim supports traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md),
a reader can inspect a chain of assertions before choosing which bodies to load.

**Indexes and notes expose different scopes.** A curated index groups claims
and explains their roles in a topic. Following an entry reaches the narrower
claim and its support. Returning to the index restores the topic-level view.
Search supplies another broad entry route, while local link-following uses the
reader's current context. Those routes have [different metadata
requirements](./link-following-and-search-impose-different-metadata-requirements.md),
but both can participate in a resolution switch.

**Link context preserves bearings during a switch.** A contextual phrase says
why the target matters in the current argument. It lets a reader move to a
different scope without reducing the connection to an untyped jump. The link's
relation does not by itself determine which artifact is more abstract; its role
is to preserve the task-relative relationship across the transition. This is
the navigational value of [encoding link strength in position and
prose](./link-strength-is-encoded-in-position-and-prose.md).

**Progressive disclosure supplies intermediate views.** Titles, descriptions,
contextual link phrases, generated summaries, and full bodies can form a cost
gradient. A reader first inspects a cheaper pointer and loads a more expensive
view only when needed. The gradient is useful only when each pointer supports a
sound next-read decision; [pointer types trade off specificity, cost,
availability, and accuracy](./pointer-design-tradeoffs-in-progressive-disclosure.md).

## The evaluative criterion

**Resolution-switching fluidity** asks whether a reader can move among the
views a task needs without paying avoidable transition cost or losing the
relationship between them. It complements retrieval accuracy: a system may
retrieve the right detailed artifact yet make its wider context hard to recover,
or offer an elegant overview that never reaches the required detail.

The criterion prompts four questions:

- Can a reader choose a narrower target from the broader view without opening
  every candidate body?
- Can the reader reach the needed detail without loading unrelated material?
- After opening the detail, can the reader recover a relevant broader view
  through an available route such as an authored link, index, or search?
- Does the transition preserve why the two views belong together for this task?

These questions identify possible friction. They do not yet supply a scoring
rule or universal threshold.

## Connection to discovery

[Recognizing shared structure](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md)
requires more than navigation. Broad views can place several candidate claims in
one context, while detailed reads can expose the mechanisms needed for
comparison. Resolution-switching helps a reader assemble those views; it does
not perform the recognition or guarantee a discovery.

## Boundaries

Resolution-switching is not the same as addressability grain. Grain sets the
smallest amount one access path can retrieve for a matched target;
resolution-switching asks whether useful views at different scopes exist and
whether the reader can move among them. It is also distinct from pointer
accuracy and retrieval recall. Those properties can enable or defeat a switch,
but none alone establishes bidirectional navigability.

An artifact does not need an outbound link in every case. Backlinks, an index,
or search may supply the outward route. Nor does every task need to return to a
broad view after reading detail. Fluidity is relative to the task and to the
navigation operations actually available to the reader.

## Open questions

- Which cost should a measurement use: navigation steps, bytes or tokens read,
  inference calls, or time to a task-relevant view?
- How should a test distinguish a genuine dead end from a route intentionally
  supplied by search or backlinks rather than an authored outbound link?
- How does the useful number of intermediate views vary with the task and the
  reader's available operations?

---

Relevant Notes:

- [Title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — enables: titles expose assertions as a lower-cost view before a reader loads their full support
- [Link-following and search impose different metadata requirements](./link-following-and-search-impose-different-metadata-requirements.md) — enables: supplies the two entry routes whose views can differ in scope and context
- [Agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — operationalized-by: each transition depends on a follow-or-skip decision at the current pointer
- [Link strength is encoded in position and prose](./link-strength-is-encoded-in-position-and-prose.md) — enables: contextual articulation preserves why a target matters across a transition
- [Pointer design tradeoffs in progressive disclosure](./pointer-design-tradeoffs-in-progressive-disclosure.md) — grounds: supplies the pointer tiers and trade-offs that can form intermediate views
- [Recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — bounds: movement can assemble candidate views but does not perform recognition
- [Addressability grain sets a matched selective-read floor](./addressability-grain-sets-a-matched-selective-read-floor.md) — contrasts: grain prices the smallest retrievable matched unit, while resolution-switching evaluates transitions among views
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](./knowledge-access-architecture-must-be-evaluated-end-to-end.md) — extends: places resolution-switching inside a wider task-relative evaluation
