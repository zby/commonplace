<!-- REVIEW-METADATA
note-path: kb/notes/distilled-artifacts-need-source-tracking-at-the-source.md
last-full-review-note-sha: e9242be31ea15efb690133615c1e90e8e7b46cad
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:54:40+01:00
last-accepted-note-sha: e9242be31ea15efb690133615c1e90e8e7b46cad
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:54:40+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: distilled-artifacts-need-source-tracking-at-the-source.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism the title cannot carry: it explains the two-directional design ("should not link back ... but sources should link forward") and names the concrete pattern ("Distilled into:") plus the maintenance rationale ("source changes trigger staleness review"). An agent seeing five results about source tracking would immediately identify this note by the forward-pointer mechanism. Strong discriminator.
- [Title composability] "since distilled artifacts need source tracking at the source, we keep forward pointers in methodology notes" reads as a natural sentence fragment. The title composes well as a linkable clause.
- [Claim strength] The claim is non-obvious and contestable: one could reasonably argue that distilled artifacts should carry provenance links themselves (for auditability), or that tracking should live in a separate metadata layer rather than inline at the source. The note argues a specific design choice with a specific rationale.
- [Title-body alignment] The body establishes exactly what the title promises: distilled artifacts should stay link-free for focus (paragraph 1), but sources need forward pointers to distilled targets for staleness detection (paragraph 2 and the "Source-side tracking" section). The "Two audiences, one link direction" table reinforces the claim without drifting beyond it.

Overall: CLEAN
===
