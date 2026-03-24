<!-- REVIEW-METADATA
note-path: kb/notes/design-methodology-borrow-widely-filter-by-first-principles.md
last-full-review-note-sha: eea7b4302fe189249827322e48cca42141c0416d
last-full-review-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-full-review-at: 2026-03-24T20:54:26+01:00
last-accepted-note-sha: eea7b4302fe189249827322e48cca42141c0416d
last-accepted-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-accepted-at: 2026-03-24T20:54:26+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: design-methodology-borrow-widely-filter-by-first-principles.md ===

Checks applied: 4

WARN:
- [Title-body alignment] The title "Design methodology — borrow widely, filter by first principles" implies a uniform first-principles filter, but the body's actual thesis is a tiered adoption system: programming patterns get an explicit fast pass that bypasses first-principles justification, empirical observation is called "the second strongest source" with its own path (not borrowed, so not filtered), and legal drafting is flagged as a separate untested candidate category. The title undersells the body's nuanced hierarchy by suggesting a single filter where the body establishes at least four distinct adoption tiers.
  Recommendation: If the note matures past seedling, consider a title that captures the asymmetry, e.g., "design methodology borrows widely but gives programming patterns a fast pass because knowledge bases are software systems" or split the uniform-filter framing from the programming-fast-pass argument.

INFO:
- [Title composability] The em-dash subtitle format ("Design methodology — borrow widely, filter by first principles") makes inline linking awkward: "because design methodology — borrow widely, filter by first principles" reads as two fragments glued together rather than a natural clause. Acceptable for a seedling, but worth revisiting if the note promotes.
- [Claim strength] The title is topical rather than a falsifiable claim. This is acceptable for a seedling note, but the body argues a specific, contestable position (programming patterns deserve a fast pass due to structural similarity to interpreters; cognitive science patterns do not). That asymmetry is the actual insight and could become the claim title when the note matures.

CLEAN:
- [Description discrimination] The description adds the programming-fast-pass exception and the underlying bet ("knowledge bases are a new kind of software system") that the title cannot carry. In a list of search results about design methodology or first-principles filtering, this description would clearly distinguish this note from adjacent ones. It supplies mechanism (first-principles as gate) and scope (the exception for programming patterns).

Overall: 1 warning, 2 info
===
