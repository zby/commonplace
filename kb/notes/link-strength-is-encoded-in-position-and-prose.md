---
description: Not all links are equal — inline premise links ("since [X]") carry more weight than footer "related" links. Position and prose encode commitment level, creating a weighted graph that affects traversal, scoring, and quality signals.
type: note
traits: []
status: seedling
areas: [links]
---

# Link strength is encoded in position and prose

The [link contracts framework](./link-contracts-framework.md) defines what links should contain (relationship type, context phrase, click-decision support). But it treats all links as equal edges. In practice, links carry different commitment levels — an inline "since [X]" that uses a note as a premise is a stronger connection than a footer "related" entry.

This matters because it creates a weighted graph. The weight affects how agents should traverse, how notes should be scored, and how graph health should be measured.

## Strength signals

**Position in the document** is the strongest signal. A link woven into the argument is load-bearing — the prose breaks if you remove it. A link in the footer "Relevant Notes" section is catalogued but not depended on.

| Position | Strength | Why |
|---|---|---|
| Inline, in a premise or argument | Strongest | The current note's reasoning depends on this link |
| Inline, in supporting context | Strong | Referenced as evidence or example |
| Inline, parenthetical mention | Medium | Acknowledged but not load-bearing |
| Footer with context phrase | Weak | Related, catalogued, but not part of the argument |
| Footer bare link | Weakest | Filed without justification |

**Relationship words in prose** refine the signal. The word that introduces a link tells you what role the linked note plays:

| Prose pattern | Role | Strength |
|---|---|---|
| "since [X]", "because [Y]" | Premise — the linked note is a reason | Strongest |
| "extends", "builds on" | Structural — the linked note is a foundation | Strong |
| "contradicts", "but see" | Tension — the linked note challenges this | Strong (different direction) |
| "see also", "related to" | Association — topical overlap | Weak |
| "cf.", bare link | Catalogued — no articulated reason | Weakest |

**The load-bearing test.** The simplest way to assess link strength: would the paragraph still make sense if you removed the link? If yes, the link is decorative. If no, it's structural. Structural links are strong; decorative links are weak.

## What link strength affects

**Traversal priority.** An agent deciding what to read next should follow strong links before weak ones. A "since [X]" link is almost certainly worth following — the current note depends on it. A footer "related" link is a maybe. This is the practical answer to the [navigation decision](./agents-navigate-by-deciding-what-to-read-next.md) problem: link strength is a traversal heuristic.

**Note scoring.** A note's quality score should weight inbound links by strength. Three inline premise links from well-regarded notes say more about a note's value than twenty footer "related" links. This is PageRank with link-weight — and it's the mechanism that prevents the [credibility erosion](../notes/related-systems/arscontexta.md) problem (noisy weak links don't inflate scores the way unweighted link counts would).

**Quality signals.** The ratio of strong to weak links is a graph health signal. A note with mostly strong inbound links is well-integrated into the KB's reasoning. A note with only weak footer links is catalogued but not used. The [quality signals](./quality-signals-for-kb-evaluation.md) note should track this ratio.

**/connect guidance.** When /connect adds links, it should prefer creating strong connections (inline, with relationship articulation) over weak ones (footer "related"). A strong connection is worth more than three weak ones. This is already implicit in the skill's articulation requirement, but making it explicit could improve connection quality as the KB scales.

## Should strength be explicit metadata?

Two options:

**Inferred from position and prose.** A script parses each markdown file, classifies links by position (inline vs footer) and surrounding words. No new metadata to maintain. But parsing prose for relationship words is fuzzy — "since" might be temporal, not causal.

**Explicit in link syntax.** Something like `[note](./note.md "premise")` or a structured footer format. Clean and queryable, but adds ceremony to every link and changes the writing convention.

The inferred approach is probably right for now — position (inline vs footer) is easy to detect, and that alone captures most of the signal. Prose analysis can be added later if the coarser signal isn't enough.

## Open questions

- How much of the strength signal is recoverable from position alone (inline vs footer), without prose analysis?
- Should /connect explicitly choose between inline and footer placement based on relationship strength, or leave that to the author?
- Does link strength decay over time? A premise link from a note that's now `outdated` is weaker than the same link from a `current` note. Should link strength be static (property of the link) or dynamic (property of the link × source note status)?
- The arscontexta "specificity test" ("genuine elaboration is specific enough to be wrong") is a link quality gate. Is there a link strength gate — a minimum strength below which a link isn't worth creating?

---

Relevant Notes:
- [link contracts framework](./link-contracts-framework.md) — defines link semantics (relationship types, context phrases); this note adds the strength dimension that link contracts don't currently address
- [notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — note scores should weight inbound links by strength; strong inbound links count more
- [agents navigate by deciding what to read next](./agents-navigate-by-deciding-what-to-read-next.md) — link strength is a traversal heuristic: strong links are worth following, weak links are maybes
- [quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — strong-to-weak link ratio is a graph health signal
- [title as claim enables traversal as reasoning](./title-as-claim-enables-traversal-as-reasoning.md) — claim titles make link strength legible: "since [claim-title]" is visibly a premise link
- [Ars Contexta](../notes/related-systems/arscontexta.md) — the credibility erosion problem: unweighted link counts let noise drown signal; link-weighted scoring prevents this

Topics:
- [links](./links.md)
