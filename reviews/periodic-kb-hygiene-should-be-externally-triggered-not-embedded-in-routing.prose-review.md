<!-- REVIEW-METADATA
note-path: kb/notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md
last-full-review-note-sha: 3dd5aa981269fdaf5103a7b9359949bc02aa2a2c
last-full-review-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-full-review-at: 2026-03-23T09:32:55+01:00
last-accepted-note-sha: 3dd5aa981269fdaf5103a7b9359949bc02aa2a2c
last-accepted-note-commit: 5d0771d0710a683a620be574bcc3f3b86bbdb60b
last-accepted-at: 2026-03-23T09:32:55+01:00
last-acceptance-kind: full-review
review-type: prose-review
-->
=== PROSE REVIEW: periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts "Routing instructions are loaded every session" and "Periodic hygiene checks are different. They are low-frequency operational maintenance and are typically triggered by something external" as settled facts. These are design choices specific to this KB's architecture, not universal truths, yet they are stated without hedging or attribution. The routing/operations distinction is the note's own construction and could be flagged as a proposed decomposition rather than an established one.
  Recommendation: Add a brief framing phrase that anchors the claim to this system's design: e.g., "In this system, routing instructions are loaded every session..." or "Here, periodic hygiene checks are..." — enough to signal that this is a design stance, not a discovered law.

INFO:
- [Proportion mismatch] The core claim — that hygiene belongs in external triggers, not routing — is developed in two short paragraphs, while the "Relevant Notes" section carries three links with relationship descriptions. The argumentative body is thin relative to the claim's specificity. The note names two responsibilities (routing vs. operations) and asserts they should be separate, but the consequences of blurring them get only one sentence ("adds instruction noise on every session while helping only occasionally"). A reader might want one more concrete sentence about what goes wrong when the separation is violated — a missed audit, a noisy context window, etc.

CLEAN:
- [Source residue] The note operates at the KB-methodology level throughout. Vocabulary ("routing instructions," "session," "operations catalogue," "CI," "heartbeat job") is native to that domain. No leaked framing from a narrower source domain detected.
- [Pseudo-formalism] No formal notation or mathematical apparatus is present. The note argues entirely in prose.
- [Orphan references] No specific figures, data points, percentages, or empirical claims appear. All references are to other notes in the KB.
- [Unbridged cross-domain evidence] The note does not cite evidence from external domains. Its claims are internal design decisions about this KB system.
- [Redundant restatement] The note is short (two body paragraphs plus a links section). No section re-explains what a prior section established; each paragraph advances the argument.
- [Anthropomorphic framing] No language attributing human-like properties to models or systems. The note discusses architectural choices, not model behavior.

Overall: 1 warning, 1 info
===
