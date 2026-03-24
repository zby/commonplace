<!-- REVIEW-METADATA
note-path: kb/notes/bitter-lesson-boundary.md
last-full-review-note-sha: 05e22d1128cc4a46b6c2b9b32a03f82b3f47e0ef
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: 05e22d1128cc4a46b6c2b9b32a03f82b3f47e0ef
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: bitter-lesson-boundary.md ===

Checks applied: 4

WARN:
- [Description discrimination] The first clause of the description — "The bitter lesson has a boundary" — is a verbatim restatement of the title. The second clause ("arithmetic vs vision features illustrate when exact solutions survive scaling and when they don't") adds the examples but not the mechanism. The note's core discriminating insight is that the boundary is whether the specification fully captures the problem: spec IS the problem (arithmetic) vs. spec approximates the problem (vision features). The description names the illustrations but omits this mechanism, which is the strongest discriminator.
  Recommendation: Lead with the mechanism. For example: "The boundary is whether the specification fully captures the problem — arithmetic specs ARE the problem and survive scaling; vision-feature specs were theories about the problem and got eaten by learned methods."

CLEAN:
- [Title composability] "since the bitter lesson has a boundary" reads naturally as a sentence fragment in linking contexts (e.g., "since the bitter lesson has a boundary, we need to identify which side a component falls on"). No awkward grammar.
- [Claim strength] "The bitter lesson has a boundary" is genuinely contestable — many practitioners treat the bitter lesson as universal, and arguing it has a firm boundary where exact solutions survive is a non-obvious, specific claim. Not a truism.
- [Title-body alignment] The title promises the bitter lesson has a boundary; the body delivers the boundary criterion (spec IS the problem vs. spec approximates the problem), illustrates it with arithmetic vs. vision features, shows a hybrid case (chess), and provides a confidence-signal table. No drift.

Overall: 1 warning, 0 info
===
