---
description: "A summary layer helps a selective reader only when its own smallest addressable unit is finer than the source's; whole-artifact compression ratios predict the wrong answer, as one repository's opposite-running instances show"
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: [document-system, context-engineering]
---

# Addressability grain, not compression ratio, decides whether a summary layer helps

A summary layer over an artifact — a description index, a per-module reference document, an abstract tier — helps a selective reader only when the layer's own addressable unit is smaller than the artifact's. Where it is not, the layer raises the floor cost of a selective read while also being non-authoritative, so it loses on cost and on correctness at the same time.

## Selective reading has a floor, and the floor is what gets paid

Selective reading has a floor: the smallest unit a reader can select without reading more. Call the size of that unit the artifact's **addressability grain**. The grain is set by how the artifact is addressed — by what search keys its structure exposes — not by how it is written or how long it is.

Source code is addressable at symbol granularity, because a name is a search key: a function name, a class name, a constant appears at its definition and at every use, so a reader who knows the name can select the definition and its call sites without reading the file. Prose is addressable at heading granularity, because a heading is the finest unit its structure exposes; a paragraph inside a section has no name to search for, and a term appearing in the middle of a section returns the section, since the reader cannot tell where the relevant span begins and ends without reading around the hit.

The floor, not the artifact's total size, is what a selective reader actually pays. A reader with a specific question does not consume whole artifacts; it consumes one unit, or a few. So comparing a summary layer with its source means comparing their floors, and the layer helps only when its floor is lower.

The comparison assumes the layer's content is recoverable from the source — that it is a cache in the sense that [attempted recovery from the system regenerates it](./documentation-generates-the-system-rather-than-describing-it.md). Where content is not recoverable, there is no unit in the source to compare against, and the layer is justified on other grounds entirely; see the third consequence below.

## Two instances that run opposite ways

One repository — Commonplace, the system this note is written inside — supplies both a helping and a hurting instance. That a single system exhibits both is the evidence that the rule discriminates: the two instances differ in grain and in nothing else that a compression-based rule would notice.

**Helps: a frontmatter description layer over a note collection.** Each note carries a one-line `description` of roughly 200 bytes; the notes themselves run to several kilobytes. A grep over descriptions selects at 200-byte grain where opening notes selects at multi-kilobyte grain. The layer's floor is more than an order of magnitude below the source's, and the selective reader pays the difference on every routing decision. The summary layer wins decisively.

**Hurts: a per-module prose reference over a code package.** Measured on one module: the document's section covering that module is 3,657 bytes, the module itself is 15,052 bytes, and the median function within it is 773 bytes. A symbol-level question — what does this function do, what does it return — costs 3,657 bytes from the document, because a section is the smallest unit the prose offers and the question's answer sits somewhere inside it. The same question costs a grep plus about 1,530 bytes from source: the target function and enough surrounding lines to read it. The source is also authoritative, where the document is a description that can be stale. The summary layer loses on cost and on correctness at once.

Same rule, opposite verdicts, decided entirely by which side has the finer grain. Note that the losing document is a perfectly ordinary, well-written reference; nothing about its prose quality is at fault. Its grain is.

## Consequences

**Whole-artifact compression ratios are the wrong metric.** The per-module document compresses its subject by roughly 7 to 13 times, and still loses, because neither reader consumes whole artifacts and the two sides are not selectable at the same grain. A ratio between two totals answers a question — how much smaller is the whole summary than the whole source — that no selective reader asks. Two layers with identical compression ratios can sit on opposite sides of the verdict.

**The margin grows with question specificity.** The coarser side's cost is pinned at its floor no matter how narrow the question gets, while the finer side's cost keeps falling. So a coarse-grained summary performs worst exactly where the reader knows most precisely what it wants, and its apparent adequacy on vague questions is not evidence it will hold on sharp ones.

**Content with no locus in the source is a separate justification, and should not be conflated with grain.** An invariant spanning several modules has no symbol. A layering rule — this layer may not call that one — has no symbol. A protocol ordering across call sites has no symbol. For such content the source's grain is not coarse, it is undefined: no search key selects the content because the content is not in any one place. That is a real reason to author a summary layer, but it is a different reason, and a document that earns its place on this ground does not thereby earn it for the symbol-level material sitting beside it. The two justifications should be applied per unit of content, not per document.

**Operational test.** Ask, of each thing the layer says: *what would I search for?* If there is an answer — a symbol, a name, a distinctive string — read the source; the layer's copy is both coarser and non-authoritative. If there is no answer, that content is worth authoring, and the layer is the only place it can live.

## Scope

This is about the grain of what can be selected, which is distinct from the cost of access at a given grain. A [linear versus sublinear access cost](./design-for-the-first-time-human-except-on-access-cost.md) governs what a reader pays per unit consumed; grain governs how small a unit it can consume at all. The two compose: a reader with sublinear access to a coarse-grained artifact still pays for the whole coarse unit, and a reader with linear access to a fine-grained one pays only for the fine unit. Neither factor substitutes for the other, and a summary layer can improve one while worsening the other.

The claim is about the layer's value to a selective reader. A reader that genuinely needs an orientation pass over the whole subject is not selecting, and the grain comparison does not speak to it; that reader's case is the ordinary cache-value question of [whether the recompute is worth avoiding](./human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md).

Symbol granularity is a property of how code is conventionally written and searched, not a law about code. A codebase with one-letter names, heavy metaprogramming, or generated symbols exposes fewer usable search keys and has a coarser grain than the argument assumes; the rule still applies, but the measurement changes, and in the limit such a source can lose to a document. Likewise, prose can be made finer-grained by giving its units names a reader would search for — the description layer is exactly that move applied at collection scale.

## Open Questions

- Grain is measured here by the smallest unit a reader can select. Where a search returns several hits, the reader pays for all of them until it can discriminate; whether that is better modelled as a coarser grain or as a separate precision term is unresolved.
- The operational test asks whether a search key exists, which a reader can only answer if it already knows the vocabulary. What does the test become for a reader that does not yet know what the source calls things?

---

Relevant Notes:

- [For its load-bearing part, documentation generates the system rather than describing it](./documentation-generates-the-system-rather-than-describing-it.md) — extends: that note partitions a document into recoverable cache and unrecoverable generator; this one supplies the cost rule that decides, inside the cache partition, whether keeping the cache actually helps
- [Design for the first-time human, except on access cost](./design-for-the-first-time-human-except-on-access-cost.md) — contrasts: access cost is what a reader pays per byte consumed, grain is how few bytes it can choose to consume; the two factors compose and neither predicts the other
- [Human recompute is dear and rare; agent recompute is cheap and constant](./human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md) — contrasts: that note leaves the documentation-audience question to magnitudes of a cache-value model; grain supplies a structural term that can settle particular cases without measuring the reader profiles
- [Types give agents structural hints before opening documents](./types-give-agents-structural-hints-before-opening-documents.md) — mechanism: the description layer's win is the routing mechanism that note describes, and grain says why it wins — the hint is addressable at a far finer unit than the document it points at
- [Pointer design tradeoffs in progressive disclosure](./pointer-design-tradeoffs-in-progressive-disclosure.md) — extends: its tier table compares pointers by specificity, cost, and reliability; grain adds the test for whether a given tier is worth having at all against the tier below it
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — contrasts: frontloading's volume caveat is that the inserted result must be smaller than the material it replaces; grain sharpens which sizes are being compared — the selectable units, not the artifacts
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: materializing a derived value for a model reader pays where in-context recompute is the expensive step, which is why a finer-grained summary layer is worth its maintenance at all
