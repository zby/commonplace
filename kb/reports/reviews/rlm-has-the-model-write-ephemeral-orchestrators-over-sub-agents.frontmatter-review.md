<!-- REVIEW-METADATA
note-path: kb/notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md
last-full-review-note-sha: f48dd8d6db2f4d0b808d85889d2be7238f666b56
last-full-review-note-commit: 4b60aa26d2cb7ede14d32ed40ff5d3e43d54703a
last-full-review-at: 2026-03-24T20:56:29+01:00
last-accepted-note-sha: f48dd8d6db2f4d0b808d85889d2be7238f666b56
last-accepted-note-commit: 4b60aa26d2cb7ede14d32ed40ff5d3e43d54703a
last-accepted-at: 2026-03-24T20:56:29+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism the title cannot carry — it names the concrete substrate (REPL) and the key trade-off (orchestrators discarded after each run). Against a search result list about orchestration patterns or RLM, this description distinguishes the note clearly.
- [Title composability] "since RLM has the model write ephemeral orchestrators over sub-agents..." reads naturally as a clause in another note's prose. No grammar friction.
- [Claim strength] The title makes a specific architectural characterization — that the model *writes* orchestrators rather than *being* the scheduler, and that these orchestrators are ephemeral. Someone could contest the framing (e.g., argue the orchestrators are recoverable from logs, or that "ephemeral" undersells the design's intent). Not a truism. Note is also status: seedling, so lighter scrutiny applies.
- [Title-body alignment] The body delivers exactly what the title promises in two sections: "What RLM gets right" establishes the model-writes-orchestrators claim with a mapping table and mechanism explanation; "Ephemerality" addresses the ephemeral qualifier and its trade-offs. No drift in either direction.

Overall: CLEAN
===
