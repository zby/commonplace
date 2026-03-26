<!-- REVIEW-METADATA
note-path: kb/notes/reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md
last-full-review-note-sha: 13f409d8c58ddf7034c4e13ca40f868db70a3e87
last-full-review-note-commit: 3cc60090d6f8d8ca13e9c8f52a719ae77b7356bd
last-full-review-at: 2026-03-24T20:56:25+01:00
last-accepted-note-sha: 13f409d8c58ddf7034c4e13ca40f868db70a3e87
last-accepted-note-commit: 3cc60090d6f8d8ca13e9c8f52a719ae77b7356bd
last-accepted-at: 2026-03-24T20:56:25+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: reverse-compression-is-the-failure-mode-where-llm-output-expands-without-adding-information.md ===

Checks applied: 4

INFO:
- [Description discrimination] The first clause of the description ("LLMs can inflate a compact seed into verbose prose that carries no more extractable structure") closely paraphrases the title's core claim ("expands without adding information"). However, the second clause ("the test for whether a KB resists this is whether notes accumulate epiplexity across the network, not just token count") adds a genuine discriminator — it names the specific measure (epiplexity) and the level of analysis (network, not individual note). An agent choosing among 5 results would know this note introduces the epiplexity-based test for KB-level inflation resistance. The description works, but tightening the first clause to avoid restating the title would free space for more discriminating detail.
  Recommendation: Consider replacing the first clause with something that adds mechanism or scope rather than restating the definition — e.g., leading with when this failure mode typically occurs (vibe-noting, agent elaboration of compact seeds) so the description covers both the trigger and the test.

CLEAN:
- [Title composability] "since reverse-compression (inflation) is the failure mode where LLM output expands without adding information, we designed..." reads naturally as a sentence fragment. The parenthetical "(inflation)" is a minor speed bump but acceptable as a synonym anchor.
- [Claim strength] The title classifies a specific phenomenon as a failure mode — someone could reasonably argue that expansion sometimes adds value or that "information" is the wrong axis. This is a real, contestable framing claim. Additionally, the note's status is `seedling`, which gives further latitude.
- [Title-body alignment] The title names and defines reverse-compression as a failure mode. The body supports this by defining the concept, developing the epiplexity measure as the right test, explaining how linked KBs resist it, and sketching a validation gate. All sections serve the title's claim. The body extends naturally into implications (KB resistance, validation heuristics) but does not drift away from what the title promises.

Overall: 0 warnings, 1 info
===
