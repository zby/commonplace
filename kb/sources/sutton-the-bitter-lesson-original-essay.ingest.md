---
description: "Sutton argues that scalable search and learning outlast hand-built domain knowledge; this is the primary anchor for three KB interpretations."
source: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
captured: "2026-07-29"
capture: fetch
genre: conceptual-essay
snapshot_sha256: da71c35447d092e5d38d9499a5e86ea43603338bdef65c460cf5d85b7626193b
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [artificial-intelligence, scaling, learning-theory]
---

# Ingest: The Bitter Lesson

## Classification

This is a conceptual essay that generalizes a historical pattern across chess, Go, speech recognition, and computer vision into advice about AI research methods. Author: Richard S. Sutton; the snapshot identifies him as the essay's author but supplies no further credential context.

## Summary

Sutton argues that AI methods built around general search and learning eventually outperform approaches that encode researchers' domain knowledge because increasing computation continues to improve the former while the latter plateau and can obstruct scaling. His historical examples motivate a design preference for meta-methods that discover useful structure over systems that directly contain human discoveries. Read the essay for its original argumentative boundary and examples, but use the KB's interpretation notes for claims about representational form, warranted structure, or reflective machinery that the essay itself does not establish.

## Quotes

No source quotes have been retained yet.

## Connections Found

The essay is the primary-source anchor for [The bitter lesson selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md): Sutton contrasts hand-built domain knowledge with computation-intensive search and learning, not symbolic with learned representational form. It also supplies the historical phenomenon that [Unsupported proxy scope may explain a structured method's loss under scaling](../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) takes as its starting point, while the unsupported-scope diagnosis remains that note's own case-level conjecture rather than anything Sutton argues. Sutton's closing distinction between discoveries and discovering meta-methods is direct evidence for [Machinery persists by warrant, not position, in a reflective loop](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md). Compared with the [Wikipedia Bitter Lesson ingest](wikipedia-bitter-lesson.ingest.md), this source owns the argument itself; Wikipedia is useful for reception and secondary context.

## Extractable Value

1. **Primary wording for the production-method boundary** -- The essay grounds the contrast between hand-built domain knowledge and scalable search or learning without supporting the stronger claim that one representational form must replace another. [quick-win]
2. **A historical pattern for scrutinizing fixed knowledge** -- The cross-domain examples support asking whether manually encoded structure keeps earning its place as compute grows, while leaving the KB's unearned-reach explanation visibly interpretive. [just-a-reference]
3. **The discoveries-versus-meta-methods distinction** -- Sutton's closing prescription gives the reflective-machinery note a direct source basis for retaining discovery procedures without exempting their outputs from review. [quick-win]
4. **A primary/secondary source split** -- Keeping this original essay separate from the Wikipedia ingest lets readers use the former for Sutton's claims and the latter for reception and attribution context. [just-a-reference]

## Limitations (our opinion)

The essay argues from a small set of selected success stories rather than a systematic comparison, so the examples may reflect hindsight and selection bias. It does not define a test for separating harmful hand-built knowledge from warranted structure, quantify when short-term gains repay long-term scaling costs, or test whether search and learning scale arbitrarily. It also does not establish representational-form orthogonality or the KB's unearned-reach mechanism; treating those interpretations as Sutton's own conclusions would overstate the source.

## Recommended Next Action

Update [The bitter lesson selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) to cite this ingest as its primary evidence for Sutton's original contrast.
