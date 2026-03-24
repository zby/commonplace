<!-- REVIEW-METADATA
note-path: kb/notes/in-context-learning-presupposes-context-engineering.md
last-full-review-note-sha: 68a59a49b84091a9f098f80087aa55d44053ebda
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:55:13+01:00
last-accepted-note-sha: 68a59a49b84091a9f098f80087aa55d44053ebda
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:55:13+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: in-context-learning-presupposes-context-engineering.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism beyond the title: it names what is presupposed ("the selection machinery that ensures this") and adds a scope dimension ("is itself learned and refined over deployment"). An agent seeing five results about in-context learning would be able to pick this note based on the description alone.
- [Title composability] "since in-context learning presupposes context engineering..." reads naturally as a sentence fragment. The claim structure composes well in linking prose.
- [Claim strength] The claim is genuinely contestable. Amodei and others treat in-context learning as a standalone capability of large-context models; asserting that it presupposes an entire engineering discipline (context engineering) is a specific, non-obvious position that the body must argue for.
- [Title-body alignment] The body directly supports the title's claim: it presents Amodei's position (in-context learning suffices), argues that something must select and load the right knowledge before the model sees it, identifies that something as context engineering, and shows that this machinery improves over deployment. The extension into deploy-time learning is a natural consequence of the core claim, not scope drift.

Overall: CLEAN
===
