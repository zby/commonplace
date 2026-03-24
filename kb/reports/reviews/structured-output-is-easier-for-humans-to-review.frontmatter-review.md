<!-- REVIEW-METADATA
note-path: kb/notes/structured-output-is-easier-for-humans-to-review.md
last-full-review-note-sha: e675de8b5440152011378482fb2b799300954e1e
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:57:02+01:00
last-accepted-note-sha: e675de8b5440152011378482fb2b799300954e1e
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:57:02+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: structured-output-is-easier-for-humans-to-review.md ===

Checks applied: 4

INFO:
- [Claim strength] The title "Structured output is easier for humans to review" is mild — most readers would nod without pushback. The body's actual insight is more specific: structure decomposes a holistic judgment into focused checks (facts vs. logic), each with a clearer correctness standard. A sharper title like "structured output decomposes review into focused independent checks" would carry more information. Noting that `status: seedling` makes this advisory rather than a warning.
  Recommendation: Consider sharpening the title to name the mechanism (decomposition into independent checks) rather than the surface observation (easier to review).

CLEAN:
- [Description discrimination] The description adds both mechanism ("let human reviewers check facts and logic independently") and scope ("purely readability argument that doesn't depend on LLM behavior at all"). These discriminate well beyond the title — a searcher seeing this among results about structured output would immediately know this note is about the human-review angle specifically, and that it is a readability argument rather than an LLM-capability argument.
- [Title composability] "since structured output is easier for humans to review, we require Evidence/Reasoning sections" reads naturally as a prose fragment. No grammar issues when used as a link.
- [Title-body alignment] The body delivers exactly what the title promises: an argument that structured output aids human review. The body stays in scope — it positions this as one of three independent arguments for types, explicitly deferring the other two to linked notes rather than covering them here.

Overall: 0 warnings, 1 info
===
