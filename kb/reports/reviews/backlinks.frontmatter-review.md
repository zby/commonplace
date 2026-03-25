<!-- REVIEW-METADATA
note-path: kb/notes/backlinks.md
last-full-review-note-sha: 435bea6c25549bd7ec10d7bf8217c14df2144be6
last-full-review-note-commit: cfa5a80e97f831f42b58fa223260538a6c79282f
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: d87b84c0d5844d877748a60003af7957a76d372c
last-accepted-note-commit: 54940c69ea2daa628e8e28ba00f26e0f3b203f2a
last-accepted-at: 2026-03-25T09:26:20+01:00
last-acceptance-kind: trivial-change-ack
review-type: frontmatter-review
-->
=== FRONTMATTER REVIEW: backlinks.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "Analysis of where backlinks (inbound link visibility) would concretely help agents working in the KB — use cases, trade-offs, and design options" paraphrases the title "Backlinks — use cases and design space" with only minor expansion. The parenthetical "(inbound link visibility)" adds a gloss, but "use cases, trade-offs, and design options" restates the title's "use cases and design space." The description adds no mechanism, scope, or implication beyond what the title already conveys. An agent seeing five results for "backlinks" would not be able to distinguish this note from its title alone.
  Recommendation: Replace with a description that adds the note's key finding or scope boundary — e.g., the distinction between read-time visibility and computed-on-demand approaches, or the conclusion that hub identification and source-to-theory bridging are the highest-value use cases while manual bidirectional links fail without enforcement.

INFO:
- [Title composability] The em-dash structure "Backlinks — use cases and design space" reads awkwardly as a prose fragment ("since backlinks — use cases and design space" is ungrammatical). However, the note is a speculative design exploration (status: speculative), not a claim note, so a topical title is appropriate here. If the note matures into a claim, the title should be rewritten as a composable assertion.

CLEAN:
- [Claim strength] The title is topical, not a claim. The note has status `speculative` and explores a design space rather than arguing a point. This falls under the explicit exception for exploratory/seedling notes where ideas are not firm enough to assert as claims.
- [Title-body alignment] The title promises "use cases and design space" and the body delivers both: four concrete use cases (hub identification, source-to-theory bridge, impact assessment, tension surfacing), three explicit non-use-cases, four design options (A-D), trade-offs, and open questions. The scope matches.

Overall: 1 warning, 1 info
===
