<!-- REVIEW-METADATA
note-path: kb/notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md
last-full-review-note-sha: 3dd5aa981269fdaf5103a7b9359949bc02aa2a2c
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:56:14+01:00
last-accepted-note-sha: 3dd5aa981269fdaf5103a7b9359949bc02aa2a2c
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:56:14+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md ===

Checks applied: 4

WARN:
- [Description discrimination] Description "Periodic hygiene checks belong in externally triggered operations (user request, scheduler, CI), not in always-loaded routing instructions" closely paraphrases the title. The parenthetical examples (user request, scheduler, CI) add minor detail, and "always-loaded routing instructions" is slightly more specific than "routing," but the core message is a restatement. It does not surface the mechanism (instruction noise on every session while helping only occasionally) or the implication (separation keeps the default path lightweight).
  Recommendation: Lead with the mechanism the body establishes — something like: "Always-loaded routing should optimize for high-frequency decisions; periodic checks add instruction noise every session while helping only occasionally, so they belong in externally triggered operations (user request, scheduler, CI)."

CLEAN:
- [Title composability] "since periodic KB hygiene should be externally triggered, not embedded in routing, we designed..." reads naturally as a sentence fragment. The title works as a linkable prose clause.
- [Claim strength] The claim is specific and contestable — someone could reasonably argue that embedding hygiene in routing ensures checks are never forgotten, or that the instruction overhead is negligible. This is a genuine architectural opinion, not a truism.
- [Title-body alignment] The body directly argues the title's claim: routing instructions load every session and should optimize for high-frequency decisions; periodic checks are low-frequency operational maintenance that blurs the routing/operations boundary. The maintenance-operations-catalogue link operationalizes the separation. Title and body are well aligned.

Overall: 1 warning, 0 info
===
