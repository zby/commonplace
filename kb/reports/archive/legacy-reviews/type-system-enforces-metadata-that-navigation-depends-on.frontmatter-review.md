<!-- REVIEW-METADATA
note-path: kb/notes/type-system-enforces-metadata-that-navigation-depends-on.md
last-full-review-note-sha: 8f608e3ec70a9fa969023f461d96a6382995d9de
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:57:36+01:00
last-accepted-note-sha: 8f608e3ec70a9fa969023f461d96a6382995d9de
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:57:36+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: type-system-enforces-metadata-that-navigation-depends-on.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds both mechanism ("the note base type requires them") and implication ("navigation collapses to opening every document") beyond what the title carries. An agent seeing this in a list of type-system notes would know this one is specifically about the enforcement chain from type definition to metadata presence to navigation viability.
- [Title composability] "since type system enforces metadata that navigation depends on, we can assume descriptions exist" reads naturally as a prose fragment. Works well as a link anchor.
- [Claim strength] The claim is specific and contestable -- someone could argue that social conventions, linting, or CI pipelines are sufficient enforcement without a type system, or that navigation can work without metadata (e.g., full-text search). The note argues a particular mechanism (type-level obligation + validation) rather than stating a truism.
- [Title-body alignment] The body delivers exactly what the title promises: it identifies the note base type's description requirement as the enforcement mechanism, explains the text-to-note boundary as the trigger, and argues that without comprehensive enforcement navigation degrades. No drift in either direction.

Overall: CLEAN
===
