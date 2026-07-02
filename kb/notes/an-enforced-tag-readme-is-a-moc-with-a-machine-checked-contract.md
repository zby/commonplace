---
description: "Tag-READMEs inherit the Zettelkasten/LYT Map-of-Content tradition; the complete/covered_by marks add a completeness contract human PKM never made — humans neither needed nor could cheaply enforce it"
type: kb/types/note.md
traits: [title-as-claim]
tags: [kb-maintenance, document-system]
status: seedling
---

# An enforced tag-README is a MOC with a machine-checked contract

A tag-README is a Map of Content wearing a validator. Strip the marks and what remains is an ordinary MOC in the sense human personal-knowledge-management already had: a curated hub note that orients a reader through a topic with editorial links and context phrases rather than an exhaustive listing. The `complete`/`covered_by` marks (the mark contract lives in the [`tag-readme` type spec](../types/tag-readme.md)) add one thing on top, and it is the one thing the tradition never supplied: a machine-checked claim that the map's membership is exhaustive, or that its children cover it. The general form is old plus new — an inherited curated hub, plus a completeness contract the hub never carried.

## The inherited half is pure MOC

The curated-hub idea is not a Commonplace invention. Luhmann's Zettelkasten had structure and hub notes — entry-point cards that gathered a line of thought and pointed into the slip-box; Nick Milo's Linking Your Thinking (LYT) named the pattern a Map of Content: a note whose body is a curated, annotated set of links into a topic. A tag-README is exactly this artifact — the orientation paragraph plus selective picks with context phrases — and it inherits the tradition's core commitment, that [curation adds orientation that generation cannot produce](./index-curation-adds-orientation-that-generation-cannot-produce.md). The groupings and context phrases are editorial judgment about role, and they resist automation for the same reason in a slip-box and in a KB.

## Why the tradition never contracted completeness

A MOC in human PKM is *selective by design*, and no Zettelkasten or LYT practitioner writes "this map lists every note on the topic" as an enforced promise. That silence was not an oversight. Two independent conditions had to hold before completeness was worth asserting, and human PKM failed both — which is why the claim never appeared.

**The human reader didn't need it.** A person who reaches an incomplete MOC degrades gracefully: she keeps browsing, runs a search, recalls a note the map omits. The map orients but does not bound her — its incompleteness costs a little friction, not invisibility. So there was no reader demand for a completeness guarantee; the map was a starting point, never an authority on what exists.

**The human maintainer couldn't cheaply supply it.** Verifying that a MOC lists every note on its topic means re-scanning the whole corpus against the map by hand — an expensive, error-prone audit that goes stale on the next note written. Even a practitioner who wanted the guarantee couldn't stand behind it at a price worth paying. A completeness claim a human can't recheck is exactly the hand-maintained-and-trusted copy that [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) forbids — so the disciplined move was to not make the claim.

## Both conditions flip for the agent consumer, together

This is an instance of the general point that [human–LLM differences are load-bearing for knowledge-system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md): the consumer changed, and the same artifact acquires a contract it never had. What makes the tag-README case sharp is that *both* conditions reverse at once, and in the direction that makes the contract both necessary and achievable.

**The agent reader needs the claim.** An LLM does not degrade gracefully against an incomplete map. Since [stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md), an agent who trusts a curated head as exhaustive reads it, feels oriented, and stops looking — a note missing from the map becomes invisible, not merely harder to find. The agent has no browsing-and-recall fallback to recover the omission. So completeness stops being a nicety and becomes information the reader must have: `complete: true` is precisely the signal that tells the agent it may skip the by-tag sweep, and the absence of the mark tells it it may not. The reader now demands the guarantee the human reader could do without.

**The agent maintainer can supply it cheaply.** The audit a human couldn't afford is, for a machine, a scoped `rg` sweep re-derived on every validation pass — detection and verification collapse into one near-zero-cost step, so the check that was prohibitively expensive by hand is free in code. This is the same economics that make a [validated cache worth materializing for a model reader](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md): the recompute is what's dear, so a checked derived value pays. The maintainer can now stand behind the claim the human maintainer couldn't.

The co-arrival is the whole point. Human PKM lacked the contract because *both* the need and the means were absent — and their absence was consistent, so leaving the claim unmade was correct, not lazy. Agent KBs get the contract because both the need and the means appear together — the reader can't recover from a stale map *and* a validator can keep the map non-stale for free. Neither condition alone would produce the mark: a need without cheap enforcement leaves you with the forbidden hand-maintained claim; cheap enforcement without a need leaves a validator guarding a guarantee no reader uses.

## What is and isn't under contract

The contract lands on exactly the mechanically-checkable half and nowhere else. `complete` checks set membership; `covered_by` checks that the children cover the parent. The map's orientation value — the groupings, the "start here" ordering, the context phrase that says *why* a note matters — stays editorial, un-contracted, and inherited wholesale from the MOC tradition. So enforcement does not colonize the curated hub; it bolts a completeness guarantee onto the one dimension a machine can verify, while the dimension that resists automation remains the human (or agent) editor's judgment. An enforced tag-README is therefore not a new kind of artifact — it is the old MOC with a machine-checked contract fastened to its one checkable claim.

## Open Questions

- Does the same MOC-plus-contract split apply to other inherited PKM artifacts (backlink pages, tag hierarchies, folgezettel sequences), or is completeness the only MOC property that is both agent-critical and machine-checkable?
- Is there a MOC property humans *did* contract informally (e.g. a "these are the canonical entry points" claim) that an agent KB should drop rather than enforce?

---

Relevant Notes:

- [Human–LLM differences are load-bearing for knowledge system design](./human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — exemplifies: the general claim this note is a worked instance of — the MOC completeness contract appears because the consumer shifted from human to LLM
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the enforce-or-omit rule that makes an uncheckable completeness claim the forbidden state, so the human tradition was right not to assert it
- [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — grounds: the no-graceful-fallback mechanism that makes the agent reader need the completeness claim a human reader could do without
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: the economics under which the completeness check is cheap enough for the agent maintainer to supply what the human maintainer couldn't
- [Index curation adds orientation that generation cannot produce](./index-curation-adds-orientation-that-generation-cannot-produce.md) — extends: the inherited MOC half; this note keeps its orientation-value claim un-contracted and adds the completeness contract beside it
- [Soft-bound traditions as sources for context engineering strategies](./soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — exemplifies: a concrete case of transferring a Zettelkasten idea (the MOC) into agent context, with the transfer condition made explicit
- [tag-readme type spec](../types/tag-readme.md) — evidence: the shipped, validator-enforced `complete`/`covered_by` marks that are the machine-checked contract this note grounds in tradition
