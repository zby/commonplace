<!-- REVIEW-METADATA
note-path: kb/notes/commonplace-architecture.md
last-full-review-note-sha: c1473803fe61adee0a1baa80a276e8c629ccd9ab
last-full-review-note-commit: cfa5a80e97f831f42b58fa223260538a6c79282f
last-full-review-at: 2026-03-24T20:54:05+01:00
last-accepted-note-sha: 113618ed5f1f7d2266e33c9a739fbf1441546e1f
last-accepted-note-commit: 54940c69ea2daa628e8e28ba00f26e0f3b203f2a
last-accepted-at: 2026-03-25T09:26:20+01:00
last-acceptance-kind: trivial-change-ack
review-type: frontmatter-review
-->
=== FRONTMATTER REVIEW: commonplace-architecture.md ===

Checks applied: 4

WARN:
- [Description discrimination] Description "The commonplace repo's own internal layout — what exists, what's missing, and the decision to put global types in CLAUDE.md instead of kb/types/" is structured as a table-of-contents summary ("what exists, what's missing, and the decision to..."). The third element (global types placement) adds a concrete discriminator, but the first two are generic content labels. An agent searching for "commonplace layout" among several architecture notes would get limited help from "what exists, what's missing."
  Recommendation: Lead with the specific insight or scope boundary — e.g., "Documents the repo's own directory layout (distinct from the two-tree installation layout) and argues that global types belong in CLAUDE.md because they're policy rules, not structural templates."

INFO:
- [Title composability] "Commonplace architecture" is a bare topic — "since commonplace architecture" does not compose into a sentence. However, this is a seedling note covering multiple concerns (layout, gaps, a design decision), so a topical title is appropriate per the exceptions for multi-claim specs and seedling-status notes. Worth revisiting if the note matures and narrows to a single claim.

CLEAN:
- [Claim strength] The title is topical, not phrased as a claim. Since the note is status: seedling and covers multiple distinct concerns (layout, missing artifacts, global types decision), a topical title is correct — no false claim strength to flag.
- [Title-body alignment] The title "Commonplace architecture" promises an overview of the repo's own architecture. The body delivers exactly that: current layout, missing artifacts, a design decision about global types, and open questions. No drift detected.

Overall: 1 warning, 1 info
===
