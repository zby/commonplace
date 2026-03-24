<!-- REVIEW-METADATA
note-path: kb/notes/document-types-should-be-verifiable.md
last-full-review-note-sha: cff89b75d5ace7bbbeb05d15f477dd261bf12a9a
last-full-review-note-commit: 5bacb391d953759e66f72549c8364d1df5b40731
last-full-review-at: 2026-03-24T20:54:45+01:00
last-accepted-note-sha: cff89b75d5ace7bbbeb05d15f477dd261bf12a9a
last-accepted-note-commit: 5bacb391d953759e66f72549c8364d1df5b40731
last-accepted-at: 2026-03-24T20:54:45+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: document-types-should-be-verifiable.md ===

Checks applied: 4

INFO:
- [Description discrimination] The first clause ("Document types should assert verifiable structural properties, not subject matter") closely paraphrases the title, adding only "structural properties, not subject matter." The second clause ("with a base type + traits model inspired by gradual and structural typing") does genuine discriminating work by naming the specific design approach. The description functions adequately for retrieval but could lead with mechanism or scope rather than a near-restatement. A tighter alternative might foreground the mechanism: e.g., "A base-type-plus-traits model inspired by gradual and structural typing; types assert checkable structure so agents and scripts can act on them, while subject matter belongs in tags."
- [Title-body alignment] The title asserts the principle "document types should be verifiable," and the body supports it thoroughly. However, the body also delivers a complete design (base types + traits, the verifiability gradient, programming language parallels, tolerance of misclassification) that goes well beyond the principle claim. The title names the motivation; the body is really the design note for the type system. This is not a misalignment -- the principle is genuinely argued -- but an agent reading only the title would underestimate the note's scope as a design artifact.

CLEAN:
- [Title composability] "since document types should be verifiable, we designed the type system around checkable structural properties" reads naturally as a sentence fragment. No awkward grammar when linked.
- [Claim strength] The claim is specific and contestable. Someone could reasonably argue that document types serve as loose human-readable labels and don't need machine-checkable structural assertions, or that subject-matter classification is sufficient. The note argues a non-obvious position.

Overall: 0 warnings, 2 info
===
