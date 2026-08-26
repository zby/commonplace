---
description: "An apparently complete stale index lowers discovery recall when it suppresses a more complete fallback that would have run had the index been absent"
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance]
---

# Stale indexes reduce discovery when they suppress fallback search

An incomplete index lowers discovery recall relative to no index when it appears exhaustive and thereby suppresses a more complete fallback. In the relevant comparison, the same consumer would search current content if no index existed but accepts the index's result and stops when one does.

The failure is therefore in control flow, not merely in missing content. The index returns a plausible answer and ends discovery before the operation that could reveal additional current items.

The same mechanism applies to any artifact a consumer treats as exhaustive, including specs, documentation, plans, and curated lists. Once an outdated artifact changes the consumer's stopping behavior, it can suppress a check against more current information. Indexes make the pattern especially visible because they explicitly govern navigation; stale specs and architecture documents can do the same when consumers treat them as sufficient.

## Staleness arises when the source changes without the view

An index is a derived view of a changing set. It can drift when an item is added, removed, renamed, or reclassified without a corresponding update to the view. Omitting a new item is only one instance of the broader failure: the source set and its navigation surface have separate update paths.

Manual synchronization makes every source change a coupled-edit obligation. The important question is therefore not which lifecycle event deserves another reminder, but whether every relevant source change reaches the index through a reliable synchronization path.

## Defenses

**Derive exhaustive views from canonical membership.** When membership is mechanically queryable, generate the complete listing from that source instead of maintaining a second membership list by hand. This removes the coupled edit: regeneration recovers the current set.

**Check retained completeness claims.** A stored or curated view may still be useful, but any claim that it is exhaustive should be machine-readable and checked against the canonical set. A failed check must invalidate the claim and force repair or fallback rather than leave consumers trusting the view. This is the index case of the broader rule that [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

**Separate orientation from enumeration.** A selective index can safely provide editorial grouping without claiming to enumerate the set. Make its partiality visible, and keep an independent search or generated listing as an expected continuation rather than an exceptional recovery path.

**Scope claims that depend on semantic judgment.** When membership is inferred from meaning rather than declared in queryable data, search and review can reveal omissions but cannot prove completeness. The index should therefore claim only the selection or scope that those methods can support.

Together, these defenses align stopping behavior with warranted coverage. A consumer may still choose an incomplete index for speed or orientation, but the resulting loss of recall should be an explicit trade-off rather than a hidden consequence of false completeness.

## Scope

An imperfect index may still have greater overall utility when it is the only discovery route or when speed and orientation outweigh omissions. Other routes may also reveal omitted items. The claim therefore concerns recall along the route whose fallback was suppressed, not global visibility or total utility.
