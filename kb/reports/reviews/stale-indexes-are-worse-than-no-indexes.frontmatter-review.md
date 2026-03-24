<!-- REVIEW-METADATA
note-path: kb/notes/stale-indexes-are-worse-than-no-indexes.md
last-full-review-note-sha: b48b793b4e4f772a02af9186e0008dd10a6d2bf0
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:56:56+01:00
last-accepted-note-sha: b48b793b4e4f772a02af9186e0008dd10a6d2bf0
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:56:56+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: stale-indexes-are-worse-than-no-indexes.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] Description "An agent trusts an index as exhaustive — a missing entry doesn't trigger search, it makes the note invisible" adds mechanism (agents trust indexes as exhaustive, suppressing fallback search) and implication (missing entries cause invisibility) that the title alone doesn't carry. In a list of search results about index maintenance or staleness, this description clearly identifies the specific asymmetry this note argues.

- [Title composability] "since stale indexes are worse than no indexes, we designed maintenance routines that..." reads naturally as a sentence fragment. The claim-shaped title composes well in linking contexts.

- [Claim strength] The claim is non-obvious and contestable. A reasonable person could argue that even a stale index provides partial value, or that agents should be designed to not treat indexes as exhaustive. The specific insight — that the absence of an index degrades to search while a stale index suppresses search entirely — is a genuine asymmetry, not a truism.

- [Title-body alignment] The body establishes the title's claim in the first two paragraphs (the asymmetry between no-index and stale-index), then extends into defenses and the critical creation moment. The extensions are practical consequences of the claim, not drift away from it. The body does generalize beyond indexes to "any authoritative artifact" in paragraph 3, but this is clearly marked as a generalization and the core argument stays on indexes as promised by the title.

Overall: CLEAN
===
