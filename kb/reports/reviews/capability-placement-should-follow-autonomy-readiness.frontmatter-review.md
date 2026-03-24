<!-- REVIEW-METADATA
note-path: kb/notes/capability-placement-should-follow-autonomy-readiness.md
last-full-review-note-sha: f589a0cedda8823d9f274b51e43bc397449a661e
last-full-review-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: f589a0cedda8823d9f274b51e43bc397449a661e
last-accepted-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: capability-placement-should-follow-autonomy-readiness.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description's first clause ("Capability artifacts should be placed by autonomy readiness") closely paraphrases the title ("Capability placement should follow autonomy readiness"). The second clause adds the AGENTS.md consequence, which does provide some discrimination, but the description leads with a near-restatement rather than mechanism. A stronger description would lead with the three-tier decision rule the note actually establishes (skills / instructions / notes) or explain why autonomy readiness is the right organizing variable (safety and reliability of unsupervised execution).
  Recommendation: Rewrite to lead with the mechanism — e.g., "Autonomy readiness (how safely the agent can execute without human steering) determines whether a capability becomes a skill, an instruction, or stays in notes — keeping AGENTS.md free of capability inventories."

CLEAN:
- [Title composability] "since capability placement should follow autonomy readiness, we designed..." reads naturally as a linked prose fragment. The title is a complete claim that composes well in sentences.
- [Claim strength] The claim is specific and contestable — someone could reasonably argue capabilities should be placed by usage frequency, topic area, or implementation complexity rather than autonomy readiness. This is a non-obvious organizational principle, not a truism.
- [Title-body alignment] The body delivers exactly what the title promises: a decision rule for placing capabilities based on autonomy readiness (ready -> skill, reusable but not autonomous -> instruction, exploratory -> notes), the consequence for AGENTS.md design, and a migration path. No drift detected.

Overall: 1 warning, 0 info
===
