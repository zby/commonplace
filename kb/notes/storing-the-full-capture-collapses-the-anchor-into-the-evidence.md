---
description: When a KB stores the full immutable source body, the drift anchor and the evidence are the same artifact, so no separate hash, byte-offset, or quote-anchor primitive is needed — staleness is found by re-fetching and diffing against the stored body.
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [links, kb-maintenance, architecture]
status: seedling
---

# Storing the full capture collapses the anchor into the evidence

Source-trust machinery composes in layers, and the layer a system chooses to anchor on determines which primitives it needs. A system that links claims to *positions* inside an external source must invent a way to detect when those positions move: content hashes, byte offsets, quote anchors, fuzzy re-locators. A system that stores the full source body needs none of these, because the stored body is simultaneously the thing the claim points at and the thing a later fetch is compared against. The anchor and the evidence collapse into one artifact.

## The layer stack

Source-trust primitives stack from cheapest-to-locate to richest-as-evidence:

1. **Raw anchor** — a pointer that identifies *where* in a source a claim came from without carrying the source content: a URL fragment, a line range, a `quote+prefix+suffix` anchor, a content hash of the span. An anchor is small and stable to store, but it is not evidence: to check it you must go back to the live source, and the live source may have moved or vanished.
2. **Snapshot** — the full source body captured at a point in time and stored locally (`kb/sources/`). A snapshot *is* evidence: the claim can be checked against it without any network call, and it does not move when the upstream does.
3. **Evidence / derived-from link** — the edge from a claim to the snapshot it was abstracted from or that corroborates it. This is the `derived-from` / `evidence` relationship: it says *this claim depends on that captured body*.
4. **Claim** — the note that asserts something, holding a link down the stack to its supporting capture.

Each higher layer subsumes the locating job of the one below it. Once you hold the whole snapshot (layer 2), a within-source anchor (layer 1) buys you only finer-grained pointing, not trust — and within-document pointing is a job `rg` over the stored body already does on demand.

## Why no separate drift primitive is needed

The argument for hash/offset/quote-anchor primitives is drift detection: an external source changes under you, and you want to know your claim is now stale. That argument assumes the source lives *outside* the KB and the anchor is the only thing you hold. Hashing the anchored span lets you notice the span changed; a byte offset lets you re-find it; a quote anchor lets you re-find it fuzzily after edits.

But if the KB already stores the full immutable capture, drift detection reduces to: re-fetch the live source, diff it against the stored body. The stored body is a strictly stronger anchor than any hash of it — a hash answers "did it change?" with one bit, while the stored body answers "what changed, and does the change touch what my claim relied on?" A hash is a lossy projection of the very artifact the KB is already holding in full. Storing the projection alongside the original is redundant; storing it *instead of* the original would throw away the evidence to keep the alarm. This is the same move as [link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md), one rung lower: there the dependency edge plus a timestamp replaces a hand-maintained staleness annotation; here the stored body plus a re-fetch replaces a hand-maintained content hash. In both cases the artifact the system already keeps for another reason carries the drift signal for free.

So source staleness, in a snapshot-holding KB, is detected by *re-fetch-and-diff against the stored body*, not by comparing a stored hash. The diff is also more useful than the hash: it surfaces the substantive change for review rather than a bare "differs" bit, which matters because most upstream edits do not touch the span a given claim depends on — the same false-positive economics that make timestamp-based staleness tolerable.

## Why structured-claim is the wrong seam

A tempting alternative is to push trust down into the claim's representation: give each [structured claim](./types/structured-claim.md) an evidence field that records the exact quoted span, its hash, and its offset, so the claim self-describes its anchor. This puts the seam between *claim* and *source span*. It is the wrong seam for two reasons.

First, it duplicates the snapshot. The quoted span is a copy of bytes the snapshot already holds; the hash is a projection of those bytes; the offset is a pointer into them. All three are derived from the capture and go stale relative to it on re-capture, so the structured claim now carries [lineage](./definitions/lineage.md) it must keep in sync with the snapshot — a maintenance liability the snapshot did not have.

Second, it puts drift detection at the wrong granularity. A source changes as a *document*; claims drift as a *consequence*. Anchoring trust at the claim level means a single upstream edit can require touching every claim that quoted near it, and there is no one place that owns the question "has this source moved?" Anchoring at the snapshot level gives exactly one owner per source: the capture. Re-fetch-and-diff runs once per source and then fans out to the claims through the existing `derived-from` edges. The claim stays a claim — it holds a link, not a forensic record — which keeps it composable as a premise. This is the source-side mirror of why [distilled artifacts need source tracking at the source](./distilled-artifacts-need-source-tracking-at-the-source.md): the dependency edge belongs where the change originates, not embedded in every downstream artifact.

The general principle: **anchor drift detection at the layer that already stores the full body.** Holding the evidence makes the anchor and the alarm the same object, which is why a snapshot-based KB needs neither a quote-anchor primitive nor a content-hash field. This is consistent with the broader files-first stance that [files beat a database for agent-operated knowledge bases](./files-not-database.md): the cheap substrate already retains what a richer schema would have you re-encode.

## Scope

The collapse holds only when the full capture is stored and treated as immutable. It does not hold for sources too large or too licensed to snapshot in full, where you genuinely retain only an anchor into a live document — there a hash or quote anchor is the best available drift signal, and the redundancy argument does not apply. It also does not address *semantic* drift inside the KB's own derived layer (a note going stale because a sibling claim was revised); that is the make-like timestamp problem, not the source-capture problem. The claim is specifically about trust in external sources whose bodies the KB chooses to hold.

## Open Questions

- At what source size or license does retaining only an anchor beat snapshotting, flipping which primitive is cheaper?
- Should re-fetch-and-diff be scheduled (periodic) or event-driven (on traversal of a `derived-from` edge), given that most diffs will not touch any claim's relied-upon span?

---

Relevant Notes:

- [link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: the same "already-stored artifact carries the drift signal" move, one rung lower in the layer stack
- [distilled artifacts need source tracking at the source](./distilled-artifacts-need-source-tracking-at-the-source.md) — contrasts: the source-side mirror — dependency tracking belongs where change originates, not in the downstream artifact
- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — grounds: the files-first stance under which the full capture is cheap to store and re-encoding it as a schema field is the avoidable cost
- [lineage](./definitions/lineage.md) — defined-in: the source-dependency and refresh-obligation field that an in-claim evidence record would force out of sync with the snapshot
- [LLM Wiki](../sources/karpathy-llm-wiki.md) — derived-from: the agent-maintained-wiki source whose raw/wiki/schema layering and immutable-raw-sources premise this layer analysis was abstracted from
