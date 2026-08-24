---
description: "For recoverable content and a known one-unit question, a summary lowers the matched raw read-volume floor only when its path loads less answer-bearing material than the source path; whole-artifact compression alone does not decide that relation"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, context-engineering]
---

# Addressability grain, not compression ratio, sets a matched selective-read floor

For a known question, compare the material each access path must load to retrieve one discriminating, answer-bearing unit. Measure both units in one declared read-volume currency, such as bytes under one encoding or tokens under one tokenizer. The smaller addressed unit sets the matched selective-read floor. A summary lowers that floor only when its path loads less material than the source path.

The whole-artifact compression ratio alone cannot determine this comparison unless each whole artifact is itself the selected unit. Otherwise, the selected unit can be much smaller than its containing artifact. A whole artifact's total size equals that path's grain only when the whole artifact is its smallest addressable unit.

This claim applies to **recoverable content**: material that a declared source set can regenerate at the required reliability. It isolates raw read volume only. Answer sufficiency, semantic reconstruction, freshness, retrieval overhead, and maintenance stay in a separate cost ledger.

## A matched selective read compares one addressed unit on each side

An artifact's **addressability grain** is the smallest material a reader can retrieve through the access path in use without loading the rest of the artifact, together with that material's volume in the comparison currency. Here **finer** means lower measured read volume, not greater topical or structural specificity. Grain depends on the exposed search keys, the reader's question, and the retrieval tool. It is not a fixed property of prose or code.

A **matched** comparison holds the question, target information, required reliability, and read-volume currency constant. On each side, the candidate answer must be explicit in one unit. A known key must discriminate that unit, and the access path must retrieve it without loading other units. [Rule-based context selection needs a pre-existing signal](./rule-based-context-selection-needs-a-pre-existing-signal.md) explains the precondition: without such a key, this one-unit comparison does not apply.

These selected units define the raw retrieval floors. A coarser summary can still win overall when it consolidates several source units, disambiguates many hits, supplies unknown vocabulary, or avoids interpretation and verification work. Those wins come from fan-out reduction, discovery help, or cached transformation, not from the two unit volumes alone.

In the Commonplace paths below, source symbols and Markdown metadata or headings provide the keys. Other naming schemes and tools can make either side finer or coarser. The conditional relation stays the same, but the measured units change.

## Two Commonplace cases run in opposite directions

Commonplace, the system this note is written inside, provides one bounded example of each ordering. The pair shows that either side can win. It does not show that read volume is the only difference between the tasks.

**Helps: structured frontmatter descriptions over a note collection.** For a candidate whose path and title do not settle a routing question, a scoped search can retrieve its one-line `description`. Without that layer, the reader must open enough of the same note to judge relevance. This is a matched per-candidate comparison. A collection-wide search can fan out across many candidates, multiplying those units rather than turning the whole task into one unit. Commonplace's move from whole generated inventories to scoped path-plus-description selection is recorded in [ADR 025](../reference/adr/025-complete-generated-indexes-are-build-time-only.md).

**Hurts: a per-module prose reference over a code package.** In a 2026-08-23 Commonplace snapshot, the `lib-modules.md` section for `type_resolver` was 3,657 bytes. A symbol search for `validate_type_eligibility` selected 1,530 bytes of source. For that question, the source path therefore had the lower byte-volume floor, even though the reference compressed the package as a whole. This is a snapshot-bound observation, not a maintained benchmark. It also illustrates the independent [sufficiency](./an-insufficient-summary-precedes-the-source-rather-than-replacing.md) question: if the approximate reference answer cannot license a reliability-compliant stop, the source remains in the path.

The same one-unit rule therefore runs in opposite directions. The helpful layer exposes a smaller per-candidate routing unit. The harmful layer exposes a larger symbol-answer unit. Because the examples involve different tasks and other differences, they show both orderings without isolating read volume as the only cause.

## Consequences

**Specificity helps only until each side reaches its floor.** A more precise key can keep shrinking the material selected from the finer side after the coarser side has reached its minimum unit. Once both sides are at their floors, more specificity changes neither cost. Success on vague questions therefore does not show that a coarse layer will stay competitive on precise ones.

**Distributed recovery needs an aggregate comparison.** A cross-module invariant may be recoverable only by combining several source locations. In that case, the source-side cost is an aggregate reconstruction cost, not one addressed-unit volume, so this test does not decide it.

**Recovery failure sets a relative boundary.** If a declared source set cannot regenerate a decision, intent, or constraint, that content lies outside a cache comparison relative to that source set. But [attempted recovery identifies informational gaps, not provenance or authority](./documentation-generates-the-system-rather-than-describing-it.md). Failed system-only recovery marks a candidate gap; it does not prove global uniqueness, historical derivation, or current governing force.

**Operational test.** Fix the question, required reliability, and read-volume currency. Ask whether the declared source set can regenerate the candidate answer and whether either path must combine several locations. Then identify one discriminating unit on each path and compare their volumes. Test sufficiency and the rest of the ledger separately. A smaller summary unit is necessary to lower this matched raw read-volume floor, but it is not enough to establish positive net value.

## Scope

This claim concerns a matched selective question. Orientation across a whole subject is not selection of one answer-bearing unit. A question that requires synthesis across several units is still selective, but it lies outside the one-unit comparison. [Two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) develops the collection-scale regime. Both cases belong in the broader cache-value ledger discussed in [whether equivalent recompute is worth avoiding](./opposed-recompute-factors-do-not-decide-documentation-segmentation.md).

A missing or non-discriminating key also blocks the comparison. One-letter names, metaprogramming, generated symbols, repeated prose terms, or unfamiliar vocabulary can force discovery or multi-hit inspection. Named paragraphs, anchors, and precise snippets can make prose finer-grained. Such changes alter or prevent the measurement; they do not refute the conditional relation.

## Open Questions

- What aggregate measure should replace grain when one answer requires several addressed units, or when one query returns several plausible hits?
- What is the cheapest routing signal for a reader that knows the task vocabulary but not the source's discriminating key?

---

Relevant Notes:

- [Attempted recovery identifies informational gaps, not provenance or authority](./documentation-generates-the-system-rather-than-describing-it.md) — grounds: defines recoverability relative to a declared source set and bounds what failed system-only recovery establishes before this note compares cache retrieval floors
- [An insufficient summary precedes the source rather than replacing it](./an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — contrasts: grain asks how much one matched answer requires the reader to select, while sufficiency asks whether reading that answer ends the task; a summary must pass both conditions
- [Opposed recompute factors do not decide documentation segmentation](./opposed-recompute-factors-do-not-decide-documentation-segmentation.md) — contrasts: that note prices total cache value and segmentation; grain supplies only the independent retrieval-floor condition for a matched selective read
- [Rule-based context selection needs a pre-existing signal](./rule-based-context-selection-needs-a-pre-existing-signal.md) — grounds: a known discriminating key is the rule-ready signal that makes one-unit selection possible
- [Two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) — contrasts: collection-scale orientation and comparison require multi-unit reading beyond the matched one-unit floor
- [Types give agents structural hints before opening documents](./types-give-agents-structural-hints-before-opening-documents.md) — mechanism: the description layer's win is the routing mechanism that note describes, and grain says why it wins because the hint is addressable at a much finer unit than the document it points at
- [Pointer design tradeoffs in progressive disclosure](./pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: its tier table compares pointers by specificity, cost, and reliability; grain adds the retrieval-floor test against the tier below it
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: frontloading precomputes from known inputs and inserts the result into later context; its volume caveat compares the selectable units replaced, not whole artifacts
- [LLM recompute cost shifts the store-vs-recompute balance](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: model-side derivation can make checked materialization attractive, while this note isolates the matched raw read-volume component of that broader ledger
- [Complete generated indexes are build-time only](../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — evidenced-by: Commonplace's shift from whole inventories to scoped path-plus-description selection is the helping instance implemented as a retrieval path
