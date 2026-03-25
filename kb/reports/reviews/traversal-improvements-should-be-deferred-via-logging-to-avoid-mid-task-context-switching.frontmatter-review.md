<!-- REVIEW-METADATA
note-path: kb/notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid-task-context-switching.md
last-full-review-note-sha: 28e98dc31891d21dd5e1f20d315bff4838ed4ec7
last-full-review-note-commit: bff3a5b014d2d6978434dbb3dc7e86bed7485b68
last-full-review-at: 2026-03-25T09:26:46+01:00
last-accepted-note-sha: 28e98dc31891d21dd5e1f20d315bff4838ed4ec7
last-accepted-note-commit: bff3a5b014d2d6978434dbb3dc7e86bed7485b68
last-accepted-at: 2026-03-25T09:26:46+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: traversal-improvements-should-be-deferred-via-logging-to-avoid-mid-task-context-switching.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "Every traversal is a read-write opportunity — agents should log improvement opportunities during reading, then process them separately to avoid context-switching" largely paraphrases the title. The second half ("agents should log improvement opportunities... to avoid context-switching") restates the title's claim with no additional signal. The opening "read-write opportunity" adds framing but not a discriminator that would help pick this note from search results.
  Recommendation: Lead with the mechanism — why logging specifically beats fixing in place for LLM agents. For example: "Fixing noticed issues mid-traversal forces loading writing methodology into an already-committed context window; a one-line log entry preserves the improvement signal at near-zero cost for later processing."

CLEAN:
- [Title composability] "since traversal improvements should be deferred via logging to avoid mid-task context switching, we designed..." reads naturally as a sentence fragment.
- [Claim strength] The claim is contestable — Luhmann-style in-place correction is a real alternative, and the note itself argues against it. The title makes a specific, non-obvious design choice.
- [Title-body alignment] The body establishes exactly the title's claim: why on-the-spot fixes are wrong for LLM agents (context-switching cost), the log as the deferral mechanism, and how this preserves co-evolution while respecting cost structure. No drift.

Overall: 1 warning, 0 info
===
