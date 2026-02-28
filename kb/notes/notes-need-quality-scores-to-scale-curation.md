---
description: As the KB grows, /connect will retrieve too many candidates — note quality scores (status, type, inbound links, recency, link strength) filter candidates and prioritise what's worth connecting
type: note
traits: []
status: seedling
areas: [claw-design]
---

# Notes need quality scores to scale curation

The /connect skill searches for candidate notes by keyword, then an agent evaluates each candidate for genuine connections. At current scale (~100 notes) this works — the candidate list is short enough for an agent to scan. As the KB grows, keyword searches will return dozens or hundreds of candidates, most not worth evaluating. Curation doesn't scale if every candidate gets equal attention.

The fix is a quality score per note that lets /connect filter and rank candidates before the agent evaluates them. Only the top N candidates get full attention.

## Scoring dimensions

**Status** is the strongest signal. A `current` note has been reviewed and endorsed — it's worth linking to. A `seedling` hasn't been vetted; linking to it couples your note to something that might be pruned. An `outdated` note should rarely be a link target.

| Status | Score weight | Rationale |
|---|---|---|
| current | highest | reviewed, endorsed, stable |
| speculative | medium | deliberately exploratory but acknowledged |
| seedling | low | unvetted, may be pruned |
| outdated | lowest | superseded, kept for reference only |

**Type** reflects structural maturity. A `structured-claim` with Evidence/Reasoning sections is a more valuable link target than a `text` with no frontmatter — it's a developed argument you can reason with.

**Inbound link count** is a social proof signal. A note that many other notes link to has been repeatedly judged worth connecting to. This is the graph-topology version of citation count. But it must be weighted by [link strength](./link-strength-is-encoded-in-position-and-prose.md) — ten footer "related" links count less than three inline "since [X]" premise links.

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

**Quality signals.** The [quality signals](./quality-signals-for-kb-evaluation.md) note identifies graph-topology and content-proxy signals. Note scores are the composite of those signals — a single number that summarises "how valuable is this note as a link target?"

## Implementation spectrum

At our current scale, none of this needs implementation. When it does, there's a spectrum:

- **Cheapest:** /connect filters by status (`rg '^status: current'`) and ignores seedlings. No scoring, just a hard filter. Probably enough for 200-500 notes.
- **Medium:** A script computes scores from frontmatter + inbound link count, writes them to a derived index. /connect reads the index for candidate ranking.
- **Full:** The SQLite index from the retrieval scoring layer proposal, with composite scores, recency decay, and per-note overrides.

The right point on this spectrum depends on when /connect starts struggling. We'll know because the agent will start producing low-quality connections or taking too long to evaluate candidates.

## Open questions

- Should scores be visible in frontmatter, or computed on demand? Visible scores are queryable but add maintenance burden. Computed scores are always fresh but need tooling.
- How do you bootstrap scores for new notes? A fresh note with no inbound links scores low, but it might be exactly the right link target. Some grace period or "new note bonus" might be needed.
- Does filtering by score create a rich-get-richer problem? Well-connected notes get more connections, new notes get ignored. This is the scaling version of the orphan detection problem.

---

Relevant Notes:
- [link strength is encoded in position and prose](./link-strength-is-encoded-in-position-and-prose.md) — link strength weights feed into note scoring: strong inbound links count more than weak ones
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — note scores are the composite of graph-topology and content-proxy signals this note catalogues
- [document classification](./document-classification.md) — type as a scoring dimension depends on the type system being meaningful
- [automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — note scoring is what makes automated curation tractable at scale

Topics:
- [claw-design](./claw-design.md)
