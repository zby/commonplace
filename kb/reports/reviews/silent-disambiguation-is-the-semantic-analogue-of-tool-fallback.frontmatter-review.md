<!-- REVIEW-METADATA
note-path: kb/notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md
last-full-review-note-sha: 65c678f0001117981f4ab408e9ec85fdb4047635
last-full-review-note-commit: 7045e589cd10c6b7b0d8efa6d37c490fc4cf58ff
last-full-review-at: 2026-03-24T20:56:44+01:00
last-accepted-note-sha: 65c678f0001117981f4ab408e9ec85fdb4047635
last-accepted-note-commit: 7045e589cd10c6b7b0d8efa6d37c490fc4cf58ff
last-accepted-at: 2026-03-24T20:56:44+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("silently resolves unacknowledged material ambiguity") and implication ("success hides that the contract failed to determine the path") beyond what the title carries, plus positions the note as an extension of the tool-fallback observability problem. Would clearly discriminate in a list of search results about disambiguation, observability, or spec ambiguity.
- [Title composability] "since silent disambiguation is the semantic analogue of tool fallback, we need observability into which branches the agent chose" reads naturally as a linked prose fragment.
- [Claim strength] The claim that semantic disambiguation and tool fallback share the same observability structure is specific and contestable — someone could argue the two are fundamentally different (tool fallback is operational and detectable via error codes; semantic ambiguity has no error signal at all). The analogy is doing real work.
- [Title-body alignment] The body delivers the analogy the title promises: it opens with the tool-fallback pattern, maps it to unacknowledged spec ambiguity at the semantic layer, and shows the shared observability failure. The distinction from interpreter failure and explicit delegation sharpens scope without drifting.

Overall: CLEAN
===
