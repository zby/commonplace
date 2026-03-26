<!-- REVIEW-METADATA
note-path: kb/notes/deterministic-validation-should-be-a-script.md
last-full-review-note-sha: 45c8a8fbcde688c63e7dd2cb03b6f655bb6c8954
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:54:27+01:00
last-accepted-note-sha: 45c8a8fbcde688c63e7dd2cb03b6f655bb6c8954
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:54:27+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: deterministic-validation-should-be-a-script.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism (hard-oracle checks are deterministic), scope (enums, link resolution, frontmatter structure), and implication (milliseconds vs LLM tokens). It does not restate the title; an agent seeing this in a search result list would immediately know which checks are at issue and what the cost argument is.
- [Title composability] "since deterministic validation should be a script, we split /validate into..." reads naturally as a sentence fragment. No grammar issues when used as an inline link.
- [Claim strength] The title is specific and contestable — someone could argue that maintaining a separate script isn't worth the engineering cost, or that a unified LLM-based validation path is simpler. The review instruction itself cites this exact title as a PASS example for this check.
- [Title-body alignment] The body directly supports the title: it identifies the deterministic subset of /validate checks, contrasts them with judgment-based checks using the oracle strength spectrum, and argues they should become a Python script. No drift between title promise and body delivery.

Overall: CLEAN
===
