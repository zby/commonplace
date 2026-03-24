<!-- REVIEW-METADATA
note-path: kb/notes/claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md
last-full-review-note-sha: aa2845b1b6d2be5e64a15149e2e788541b75b010
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:53:55+01:00
last-accepted-note-sha: aa2845b1b6d2be5e64a15149e2e788541b75b010
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:53:55+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] Description adds mechanism ("three independent threads converged on Toulmin's argument structure") and scope ("separates claim-titled notes (any note) from fully argued claims (the type)"). Neither restates the title. An agent searching for "Toulmin" or "structured argument" would use the convergence detail and the claim-titled vs. type distinction to pick this note from a results list.
- [Title composability] "since claim notes should use Toulmin-derived sections for structured argument, we adopted..." reads naturally as a sentence fragment.
- [Claim strength] Contestable -- someone could argue Toulmin sections are too rigid for KB notes, that free-form argument is preferable, or that the scaffold creates flow problems (the note itself acknowledges this in Caveats). Not a truism.

INFO:
- [Title-body alignment] The title focuses on the prescription "should use Toulmin-derived sections." The body delivers on this but also covers substantial type-system design territory: why `structured-claim` should be a base type rather than a trait, the naming choice over plain `claim`, the promotion path from `note`, the retirement of `has-claim`, and a full section template with deterministic/semantic check specifications. The body reads more like a design decision record for creating the `structured-claim` type than a note arguing that Toulmin sections are the right choice. The title's claim is the foundation for all of this, so the alignment is not broken -- but readers arriving for the Toulmin argument may be surprised by the scope of type-system machinery.

Overall: 1 info
===
