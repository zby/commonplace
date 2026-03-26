<!-- REVIEW-METADATA
note-path: kb/notes/notes-need-quality-scores-to-scale-curation.md
last-full-review-note-sha: 3aa05d22fb74e8f6a2fdd7f1e8f765f1f665459d
last-full-review-note-commit: 3c3418d44ae167551bae036f7a968e8d0e8a64f2
last-full-review-at: 2026-03-24T20:56:07+01:00
last-accepted-note-sha: 3aa05d22fb74e8f6a2fdd7f1e8f765f1f665459d
last-accepted-note-commit: 3c3418d44ae167551bae036f7a968e8d0e8a64f2
last-accepted-at: 2026-03-24T20:56:07+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: notes-need-quality-scores-to-scale-curation.md ===

Checks applied: 4

WARN:
(none)

INFO:
- [Title-body alignment] The title says "scale curation" broadly, but the body's primary argument is specifically about scaling /connect candidate filtering. Retrieval ranking and quality signals are mentioned as secondary uses but receive much less development. The title is not wrong — /connect is curation — but a reader expecting a general curation-scaling argument may find the scope narrower than advertised.
  Recommendation: Consider whether "scale connection" or "scale /connect" would be more precise, or expand the retrieval-ranking and quality-signals sections to match the breadth the title implies.

CLEAN:
- [Description discrimination] The description adds mechanism (enumerates the five scoring dimensions: status, type, inbound links, recency, link strength) and scope (/connect candidate filtering as the KB grows). It does not restate the title and would clearly distinguish this note from related results about quality signals or curation methodology.
- [Title composability] "since notes need quality scores to scale curation, we designed..." reads naturally as a sentence fragment. The title works as a linkable prose element.
- [Claim strength] The claim is contestable — someone could reasonably argue that simpler approaches (status filtering alone, better search heuristics, or manual curation) suffice and that composite quality scores are over-engineering. The note itself acknowledges the cheapest option is a hard status filter, reinforcing that the "need" for scores is a design judgment, not a truism.

Overall: 0 warnings, 1 info
===
