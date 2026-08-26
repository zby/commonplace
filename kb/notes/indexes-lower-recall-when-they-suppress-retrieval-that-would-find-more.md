---
description: "A plausibly exhaustive index lowers route-level recall only when it prevents retrieval that would have produced greater task-relevant coverage"
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance]
---

# Indexes lower recall when they suppress retrieval that would find more

An incomplete index lowers discovery recall relative to no index when it appears exhaustive and suppresses retrieval that would have produced greater task-relevant coverage. The comparison holds the consumer, task, relevant-item set, and endpoint fixed. Without the index, the consumer runs that retrieval. With the index, the consumer accepts its result and stops.

The failure is therefore in control flow, not merely in missing content. The index returns a plausible answer and ends discovery before the operation that could reveal additional current items.

This is a conditional mechanism, not a prevalence claim. It does not establish that consumers usually stop at apparently complete indexes or that a fallback usually finds more. A system that predicts either behavior needs evidence. A system that binds a consumer to stop may use the control-flow claim directly.

The same mechanism applies to any artifact a consumer treats as exhaustive, including specs, documentation, plans, and curated lists. Once an outdated artifact changes the consumer's stopping behavior, it can suppress a check against more current information. Indexes make the pattern especially visible because they explicitly govern navigation; stale specs and architecture documents can do the same when consumers treat them as sufficient.

## Staleness arises when the source changes without the view

An index is a derived view of a changing set. It can drift when an item is added, removed, renamed, or reclassified without a corresponding update to the view. Omitting a new item is only one instance of the broader failure: the source set and its navigation surface have separate update paths.

Manual synchronization makes every source change a coupled-edit obligation. The important question is therefore not which lifecycle event deserves another reminder, but whether every relevant source change reaches the index through a reliable synchronization path.

## Defenses

**Derive exhaustive views from canonical membership.** When membership is mechanically queryable, generate the complete listing from that source instead of maintaining a second membership list by hand. Derive it at use time, or require a refresh to finish before asserting completeness. This removes the coupled membership edit without pretending that regeneration schedules itself.

**Check retained completeness claims.** A stored or curated view may still be useful, but any claim that it is exhaustive should be machine-readable and checked against the canonical set. A failed check must invalidate the claim rather than leave consumers trusting the view. Repair, recomputation, fallback, and explicit reclassification as partial are all valid responses. This is the index case of the broader rule that [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).

**Separate orientation from enumeration.** A selective index can safely provide editorial grouping without claiming to enumerate the set. Make its partiality visible, and keep an independent search or generated listing as an expected continuation rather than an exceptional recovery path.

**Scope claims that depend on semantic judgment.** When membership is inferred from meaning rather than declared in queryable data, search and review can reveal omissions but cannot prove completeness. The index should therefore claim only the selection or scope that those methods can support.

Together, these defenses prevent a completeness signal from authorizing a stop unless its coverage is warranted. The consuming system must still deliver the signal and make the consumer honor it. A consumer may choose an incomplete index for speed or orientation, but any resulting loss of recall should be an explicit trade-off rather than a hidden consequence of false completeness.

## Scope

The claim requires the suppressed retrieval to have greater realized task-relevant coverage at the fixed endpoint. A fresher corpus or broader search surface is not sufficient if the actual operation would retrieve nothing more. Index-only discoveries may erase the comparison unless the suppressed route still finds more.

An imperfect index may still have greater overall utility when it is the only discovery route or when speed and orientation outweigh omissions. Other routes may also reveal omitted items. The claim therefore concerns recall along the route whose fallback was suppressed, not global visibility or total utility.
