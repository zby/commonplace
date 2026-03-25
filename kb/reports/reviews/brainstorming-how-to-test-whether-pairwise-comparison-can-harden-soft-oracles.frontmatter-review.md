<!-- REVIEW-METADATA
note-path: kb/notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md
last-full-review-note-sha: 4153e0186b9fd1dfa17415ad22a7f890cdb08b87
last-full-review-note-commit: 328009802f9033ab971afc8a1f0918d052115c52
last-full-review-at: 2026-03-24T20:53:51+01:00
last-accepted-note-sha: ad14ad7fc5e6f8491e19fe4fe343cbc166c9b389
last-accepted-note-commit: 54940c69ea2daa628e8e28ba00f26e0f3b203f2a
last-accepted-at: 2026-03-25T09:26:20+01:00
last-acceptance-kind: trivial-change-ack
review-type: frontmatter-review
-->
=== FRONTMATTER REVIEW: brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description opens with "Brainstorming note that turns..." which is a "this note does X" summary frame. The procedure flags these as weak because they waste retrieval-facing characters on meta-labeling. The useful discriminating content is "staged test plan for open-ended LLM evaluation loops" -- that adds mechanism and scope beyond the title. Dropping the "Brainstorming note that turns" prefix and leading directly with the discriminating content would improve retrieval value.
  Recommendation: Rewrite to lead with mechanism, e.g. "Designs a three-stage test ladder (judgment quality, ranking quality, optimization-loop value) to determine whether pairwise LLM judging actually hardens soft oracles or merely reformats the prompt."

INFO:
- [Title composability] The "Brainstorming:" prefix and question format ("how to test whether...") make the title awkward as a linkable prose fragment -- "since brainstorming: how to test whether pairwise comparison can harden soft oracles" does not read naturally. However, the note is status: seedling and explicitly exploratory, which is an acknowledged exception for composability. If the note matures past seedling, the title should be reworked into a claim or at least a composable topical phrase.

CLEAN:
- [Claim strength] The title is a question/topical form with a "Brainstorming:" prefix, not a claim. For a seedling-status exploratory note, this is an appropriate exception -- the ideas are explicitly not firm enough to assert as claims. No issue.
- [Title-body alignment] The title promises brainstorming about how to test the pairwise-comparison hardening hypothesis. The body delivers exactly that: a definition of what counts as hardening, a three-stage test ladder (judgment quality, ranking quality, optimization-loop value), concrete benchmark candidates, failure modes to rule out, falsification criteria, and a practical first experiment design. Strong alignment.

Overall: 1 warning, 1 info
===
