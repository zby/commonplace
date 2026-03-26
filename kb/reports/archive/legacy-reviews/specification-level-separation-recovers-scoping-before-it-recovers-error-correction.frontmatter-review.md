<!-- REVIEW-METADATA
note-path: kb/notes/specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md
last-full-review-note-sha: 01930c59c012749e454bbb81d61dce1b3a912ea5
last-full-review-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-full-review-at: 2026-03-24T20:56:55+01:00
last-accepted-note-sha: 01930c59c012749e454bbb81d61dce1b3a912ea5
last-accepted-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-accepted-at: 2026-03-24T20:56:55+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: specification-level-separation-recovers-scoping-before-it-recovers-error-correction.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism (OpenProse-like DSLs expose control flow and discretion boundaries while leaving scheduling/validation on the LLM substrate) and scope (names the intermediate regime between flat prompting and symbolic scheduling). It does not restate the title's ordering claim; instead it tells the reader what kind of systems this applies to and what the intermediate regime looks like. Strong discriminator in a search result set.
- [Title composability] "since specification-level separation recovers scoping before it recovers error correction, we should expect..." reads naturally as a sentence fragment. The title is long but grammatically complete and composes without awkwardness.
- [Claim strength] The title asserts a specific ordering: scoping benefits arrive before error-correction benefits when separation stays at the specification level. This is non-obvious and contestable -- someone could argue that specification-level approaches recover some error correction early (e.g., compile-time structural validation) or that the two arrive together. The claim carries real information.
- [Title-body alignment] The body uses OpenProse as a case study to establish exactly the title's claim: naming control flow and externalizing state recovers scoping (cleaner frame boundaries, reduced ambiguity, resumability) but not yet error correction (hard-oracle enforcement, deterministic parsing). The body's explicit statement "Syntax and file protocols can recover scoping, resumability, and some orchestration discipline before they recover hard reliability" directly matches the title. The additional distinction from tool-use frameworks is within scope -- it clarifies what specification-level separation is not.

Overall: CLEAN
===
