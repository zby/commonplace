<!-- REVIEW-METADATA
note-path: kb/notes/alexander-patterns-and-knowledge-system-design.md
last-full-review-note-sha: a2a2caed3b73ce8aacf5a0f974866fb8e9079581
last-full-review-note-commit: db9e52206ad040c2c2c084e0eceeba50a9644881
last-full-review-at: 2026-03-24T20:53:39+01:00
last-accepted-note-sha: a2a2caed3b73ce8aacf5a0f974866fb8e9079581
last-accepted-note-commit: db9e52206ad040c2c2c084e0eceeba50a9644881
last-accepted-at: 2026-03-24T20:53:39+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: alexander-patterns-and-knowledge-system-design.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "Christopher Alexander's pattern language, generative processes, and centers may connect to our knowledge system design at multiple levels — from structured document types to codification to link semantics. Vague but persistent." largely paraphrases the title. The title already says "connect...at multiple levels"; the description repeats this and enumerates the levels, but does not add mechanism (why these connections matter), scope (what conditions make them hold), or implication (what design decisions follow). The qualifier "Vague but persistent" signals epistemic status but does not help discriminate this note from other Alexander-related results.
  Recommendation: Replace the description with what makes this note worth keeping despite its speculative status — e.g., the specific insight that Alexander's pattern structure anticipates typed document contracts, or that his generative-vs-master-plan distinction maps onto the codification trajectory. Lead with the strongest concrete mapping rather than restating the umbrella claim.

- [Claim strength] The title "Alexander's patterns connect to knowledge system design at multiple levels" asserts a connection without specifying what the connection reveals. "Connect to...at multiple levels" is close to unfalsifiable — almost any two design traditions can be said to connect at multiple levels. The body actually develops three specific and increasingly speculative mappings (patterns as document types, generative processes vs master plans, centers as notes), but the title captures none of that specificity. Mitigated by `status: speculative`, which signals the note is exploratory and the claim is not yet firm enough to sharpen — but if the note matures, the title should sharpen with it.
  Recommendation: If the note remains speculative, this is acceptable as-is. If it graduates to a stronger status, sharpen the title to the most defensible mapping — e.g., "Alexander's pattern structure anticipates typed document contracts for knowledge bases" or "Alexander's generative-process argument supports incremental codification over upfront type systems."

CLEAN:
- [Title composability] "since Alexander's patterns connect to knowledge system design at multiple levels, we explored..." reads naturally as a sentence fragment. The title works as a linkable prose element.
- [Title-body alignment] The title promises connections at multiple levels; the body delivers exactly three levels of decreasing concreteness (patterns as document types, generative processes vs master plans, centers strengthening centers). No drift in either direction.

Overall: 2 warnings, 0 info
===
