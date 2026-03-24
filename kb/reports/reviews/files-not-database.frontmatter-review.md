<!-- REVIEW-METADATA
note-path: kb/notes/files-not-database.md
last-full-review-note-sha: aee87d4749fd00417d84f19368f7b967b99aebaa
last-full-review-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-full-review-at: 2026-03-24T20:55:04+01:00
last-accepted-note-sha: aee87d4749fd00417d84f19368f7b967b99aebaa
last-accepted-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-accepted-at: 2026-03-24T20:55:04+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: files-not-database.md ===

Checks applied: 4

WARN:
(none)

INFO:
- [title-body-alignment] The title "Files beat a database for agent-operated knowledge bases" is an unqualified claim, but the body substantially qualifies it: "This isn't a files-forever position" and the entire Graphiti section identifies where the trade-off tips in favor of a database. The body's actual argument is closer to "files beat a database early on, for authored agent-navigated knowledge" — which the description captures better than the title does. The mismatch is minor (the title is a reasonable shorthand for the primary claim), but the body's qualified position is meaningfully different from the title's absolute framing.
  Recommendation: Consider whether the title should carry the qualification the description already has, e.g. "Files beat a database for authored agent-navigated knowledge bases" or "Files beat a database early on because schemas commit to unknown access patterns." Alternatively, leave as-is if the unqualified form is preferred for composability — the current title composes well and the description already carries the nuance.

CLEAN:
- [description-discrimination] Description adds mechanism ("a schema commits to access patterns before you know them") and implication ("files let you constrain incrementally while getting free browsing, versioning, and agent access from day one") that the title cannot carry. Strong retrieval discrimination — an agent seeing this among results about file-vs-database trade-offs would know immediately what angle this note takes.
- [title-composability] "since files beat a database for agent-operated knowledge bases, we chose..." reads naturally as a sentence fragment. Composes well.
- [claim-strength] Contestable claim — many engineers would argue databases are superior even early on (structured queries, ACID guarantees, relational integrity). The note itself acknowledges Graphiti as a strong counterexample, confirming the claim is non-trivial.

Overall: 0 warnings, 1 info
===
