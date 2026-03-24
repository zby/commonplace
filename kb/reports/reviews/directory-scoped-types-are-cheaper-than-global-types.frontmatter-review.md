<!-- REVIEW-METADATA
note-path: kb/notes/directory-scoped-types-are-cheaper-than-global-types.md
last-full-review-note-sha: 356796374e0455f43f8d2fda4ad603732fb8c1c9
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:54:29+01:00
last-accepted-note-sha: 356796374e0455f43f8d2fda4ad603732fb8c1c9
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:54:29+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: directory-scoped-types-are-cheaper-than-global-types.md ===

Checks applied: 4

WARN:
(none)

INFO:
(none)

CLEAN:
- [description-discrimination] Description adds mechanism ("Global types tax every session's context") and scope ("most structural affordances are directory-local") beyond the title's bare comparative claim. An agent seeing this in a list of five results about type systems would know this note argues from context-cost economics, not from e.g. maintainability or developer ergonomics. Discriminates well.
- [title-composability] "since directory-scoped types are cheaper than global types, we keep the global layer thin" reads naturally as a sentence fragment. No awkward grammar when linked.
- [claim-strength] The claim is specific and contestable: someone could argue global types provide cross-directory consistency worth the context cost, or that on-demand loading makes the cost moot. The note itself acknowledges this tension in the "Why this doesn't happen in programming" section. Not a truism.
- [title-body-alignment] The body directly supports the title's cost comparison through four lines of evidence: a table showing affordances are already directory-local, an explanation of why LLM context lacks cheap resolution (unlike programming imports), the economic argument grounded in loading-frequency principles, and a concrete sketch of what the thin global layer looks like. No drift detected.

Overall: CLEAN
===
