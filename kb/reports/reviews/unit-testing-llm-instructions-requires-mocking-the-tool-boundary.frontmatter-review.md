<!-- REVIEW-METADATA
note-path: kb/notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md
last-full-review-note-sha: 5e0f9b01a4b6f040018784fd55e6a5b5179a5a6f
last-full-review-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-full-review-at: 2026-03-24T20:57:49+01:00
last-accepted-note-sha: 5e0f9b01a4b6f040018784fd55e6a5b5179a5a6f
last-accepted-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-accepted-at: 2026-03-24T20:57:49+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("Skills are programs whose I/O boundary is tool calls") explaining why the tool boundary is the right mock seam, and scope ("complementing text artifact testing with instruction-level regression detection") distinguishing this from artifact-testing notes. Does not restate the title.
- [Title composability] "since unit testing LLM instructions requires mocking the tool boundary, we designed the mock layer around tool calls" reads naturally as a sentence fragment.
- [Claim strength] The claim that instruction testing *requires* mocking the tool boundary is contestable -- someone could argue for sandbox execution against real tools, or for input/output example testing without mocks. The "requires" is a specific architectural stance, not a truism.
- [Title-body alignment] The body argues that skills' dependencies flow through tool calls, making the tool layer the natural dependency-injection seam, then elaborates the mock architecture and assertion types. The additional sections (constraining framing, open questions) extend the core claim without drifting from it.

Overall: CLEAN
===
