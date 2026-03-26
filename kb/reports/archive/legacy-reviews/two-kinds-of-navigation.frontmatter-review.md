<!-- REVIEW-METADATA
note-path: kb/notes/two-kinds-of-navigation.md
last-full-review-note-sha: 96838cdcd8343f0621a9208828ea1577e45fc019
last-full-review-note-commit: 5bacb391d953759e66f72549c8364d1df5b40731
last-full-review-at: 2026-03-24T20:57:33+01:00
last-accepted-note-sha: 96838cdcd8343f0621a9208828ea1577e45fc019
last-accepted-note-commit: 5bacb391d953759e66f72549c8364d1df5b40731
last-accepted-at: 2026-03-24T20:57:33+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: two-kinds-of-navigation.md ===

Checks applied: 4

WARN:
- [Title composability] Title "Two kinds of navigation" is a bare topic label that does not compose as a sentence fragment. "since two kinds of navigation" is grammatically incomplete — it needs a verb to read naturally in a link context.
  Recommendation: Rephrase as a claim that captures the note's actual insight, e.g., "link navigation and search require different metadata and indexes bridge them" or "navigating a knowledge base splits into local link-following and long-range search."

- [Claim strength] The title is topical rather than a claim, yet the body argues a specific, non-obvious point: that the two navigation modes impose different design requirements (links need surrounding context, search needs good titles/descriptions) and that indexes bridge both. This insight is worth surfacing in the title. The note's type is `note` and status is `current`, so there is no exception that justifies a bare topic label here.
  Recommendation: Promote the title to a claim that captures the design implication, e.g., "links need context and search needs descriptions so indexes must provide both."

- [Title-body alignment] The title promises "two kinds of navigation" but the body describes three distinct modes: link-following, search, and indexes-as-bridge. The section "Indexes sit in between" is given equal structural weight to the other two and is presented as the note's central design insight. The title undercounts and understates the body's actual argument.
  Recommendation: Either update the title to reflect the three-part structure (e.g., "navigation splits into link-following, search, and index browsing") or restructure to make indexes a secondary observation rather than a co-equal section.

CLEAN:
- [Description discrimination] Description "Link-following is local with context; search is long-range with titles/descriptions; indexes bridge both modes" adds mechanism (how each mode works) and structure (the bridging role of indexes) that the topical title cannot carry. In a list of search results about navigation, this description would clearly distinguish this note from others.

Overall: 3 warnings, 0 info
===
