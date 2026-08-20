---
description: "A stale index is actively harmful when its apparent completeness suppresses fallback discovery that an absent index would have triggered"
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance]
---

# Stale indexes are worse than no indexes

When an agent has no index for a topic, it can fall back to search against current content. But when an incomplete index appears sufficient, the agent can read it, feel oriented, and stop looking. Missing items become invisible not because they are hard to find, but because the index ends discovery before anyone looks for them.

This is the core asymmetry: **absence of an index keeps discovery open; a trusted stale index closes it prematurely.** The failure is in control flow, not only in missing content. The index returns a plausible answer and suppresses the operation that could have corrected it.

The mechanism generalises beyond indexes to any authoritative artifact — specs, documentation, plans, curated lists. Any artifact that an agent treats as exhaustive will suppress fallback discovery when it goes stale. Indexes are the clearest case because their purpose is explicitly navigational, but a stale spec or an outdated architecture doc creates the same trap: the agent reads it, trusts it, and stops looking for current information.

## Staleness enters when a source changes without its view

An index is a derived view of a changing set. It can drift when an item is added, removed, renamed, or reclassified without the same change reaching the view. Omitting a new item is only one instance of the general failure: the source and its navigation surface have separate update paths.

Manual synchronization turns every source change into a coupled-edit obligation. The important question is therefore not which lifecycle moment deserves an extra reminder, but whether a reliable synchronization path connects every relevant source change to the index.

## Defenses

**Derive exhaustive views from canonical membership.** When membership is mechanically queryable, generate the complete listing from that source instead of maintaining a second membership list by hand. This removes the coupled edit; regeneration recovers the current set.

**Check any retained completeness claim.** A materialized or curated view may still be worth retaining, but a claim that it is exhaustive should be machine-readable and checked against the canonical set. A failed check must invalidate that claim, forcing repair or fallback rather than leaving consumers trusting the view. This is the index case of the broader rule that [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

**Separate orientation from enumeration.** A selective index can safely provide editorial grouping without claiming to enumerate the set. Its partiality must be visible, and an independent search or generated listing must remain an expected continuation rather than an exceptional recovery path.

**Do not turn semantic judgment into a false guarantee.** Some membership is inferred from meaning rather than declared in queryable data. Search and review can find omissions in that case, but they cannot prove that none remain. The safe claim is selective or scoped, not exhaustive.

All four defenses protect the same invariant: following an index must not disable a more complete discovery path unless the index's completeness is at least as trustworthy as that path.

## Scope

Not every outdated list is worse than no list. A visibly partial map can still improve orientation while leaving discovery open, and an imperfect index may be the only available discovery path. The stronger comparison applies when absence would trigger a more complete fallback and the index's apparent authority suppresses that fallback.
