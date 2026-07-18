---
description: As the KB grows, /connect will retrieve too many candidates — evidence, type, inbound links, recency, and link strength can rank what is worth evaluating
type: kb/types/note.md
traits: []
tags: [kb-maintenance, observability]
---

# Notes need quality scores to scale curation

The /connect skill searches for candidate notes by keyword, then an agent evaluates each candidate for genuine connections. At current scale (~100 notes) this works — the candidate list is short enough for an agent to scan. As the KB grows, keyword searches will return dozens or hundreds of candidates, most not worth evaluating. Curation doesn't scale if every candidate gets equal attention.

The fix is a quality score per note that lets /connect filter and rank candidates before the agent evaluates them. Only the top N candidates get full attention.

## Scoring dimensions

**No global scalar supplies quality.** `user-verified: true` records human attestation to an artifact as written, not evidence strength, currency, usefulness, or review coverage. It may be a presentation filter when a user explicitly wants only attested artifacts, but it must not dominate connection ranking. Candidate quality has to be assembled from use-shaped signals instead.

**Type** reflects structural maturity. A `structured-claim` with Evidence/Reasoning sections is a more valuable link target than a `text` with no frontmatter — it's a developed argument you can reason with.

**Inbound link count** is a social proof signal. A note that many other notes link to has been repeatedly judged worth connecting to. This is the graph-topology version of citation count. But it must be weighted by [link strength](./link-strength-is-encoded-in-position-and-prose.md) — ten footer "related" links count less than three inline "since [X]" premise links.

**Review vetting** is a use-shaped signal that did not exist when this note was first written: the review store now holds thousands of gate verdicts, so "does this note have fresh baselines, and what is its pass/warn mix" is a quality dimension that costs no authoring at all — it is a byproduct of review operation.

**Recency** matters differently per content type. A source snapshot from yesterday is more relevant than one from six months ago. A design principle note doesn't decay — older often means more refined. Type-dependent recency decay captures this: different content types age at different rates.

| Content type | Recency decay | Why |
|---|---|---|
| Source snapshots, practitioner reports | Fast | Practices and tools evolve |
| Design notes, structured claims | None | Timeless if still current |
| Task-related, session artifacts | Fast | Operational, high churn |
| ADRs | None | Permanent record |

## Where scores get used

**Connect candidate filtering.** /connect searches for keywords, gets N results, filters to top M by score, agent evaluates M. This is the primary driver — without it, /connect doesn't scale past a few hundred notes.

**Retrieval ranking.** When qmd returns semantic search results, scores rerank them so the best notes surface first.

**Budget-bounded titles listings.** The complete claim-title listing — generated fresh at invocation as /connect's cheapest full-recall surface, and a candidate for other loading moments — stays loadable whole only while the corpus is small. Past that, the score is what truncates it: rank titles by the composite, cut at a token budget, and the same mechanism serves three hundred notes (budget covers everything, today's behavior unchanged) or thirty thousand (top slice). The truncation must reserve an exploration slice for low-degree and recent notes, because a listing filtered purely by inbound links starves exactly the orphans connect exists to integrate.

**Quality signals.** The [quality signals](./quality-signals-for-kb-evaluation.md) note identifies graph-topology and content-proxy signals. Note scores are the composite of those signals — a single number that summarises "how valuable is this note as a link target?"

## Implementation spectrum

At our current scale, none of this needs implementation. When it does, there's a spectrum:

- **Cheapest:** /connect ranks by type and strong inbound links, then lets the agent inspect evidence and caveats. No persisted scalar is required.
- **Medium:** A script computes scores from frontmatter + inbound link count, writes them to a derived index. /connect reads the index for candidate ranking.
- **Full:** The SQLite index from the retrieval scoring layer proposal, with composite scores, recency decay, and per-note overrides.

The right point on this spectrum depends on when /connect starts struggling. We'll know because the agent will start producing low-quality connections or taking too long to evaluate candidates.

## Open questions

- ~~Should scores be visible in frontmatter, or computed on demand?~~ Settled by the mark doctrine: computed on demand, never persisted-and-trusted. An authored score field is a hand-maintained copy of a judgment — the forbidden middle, [since a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md). The removal of the `status` field was this doctrine applied: it was the one scoring input that could not be recomputed from ground truth.
- How do you bootstrap scores for new notes? A fresh note with no inbound links scores low, but it might be exactly the right link target. Some grace period or "new note bonus" might be needed.
- Does filtering by score create a rich-get-richer problem? Well-connected notes get more connections, new notes get ignored. This is the scaling version of the orphan detection problem. The exploration slice in budget-bounded listings is the current answer in design: reserve part of any truncated surface for low-degree and recent notes regardless of score.

---

Relevant Notes:

- [link strength is encoded in position and prose](./link-strength-is-encoded-in-position-and-prose.md) — link strength weights feed into note scoring: strong inbound links count more than weak ones
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — note scores are the composite of graph-topology and content-proxy signals this note catalogues
- [available types](../reference/available-types.md) — type as a scoring dimension depends on the type system being meaningful
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — note scoring is what makes automated curation tractable at scale
