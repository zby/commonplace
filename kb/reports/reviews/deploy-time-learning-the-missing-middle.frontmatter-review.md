<!-- REVIEW-METADATA
note-path: kb/notes/deploy-time-learning-the-missing-middle.md
last-full-review-note-sha: 4f975ac594101e4d33ac29ec9a77d3e9cca18e0a
last-full-review-note-commit: ac86be3f00c729bc7bff685d1338fcad43c3fb39
last-full-review-at: 2026-03-24T20:54:24+01:00
last-accepted-note-sha: 4f975ac594101e4d33ac29ec9a77d3e9cca18e0a
last-accepted-note-commit: ac86be3f00c729bc7bff685d1338fcad43c3fb39
last-accepted-at: 2026-03-24T20:54:24+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: deploy-time-learning-the-missing-middle.md ===

Checks applied: 4

WARN:
- [Title composability] Title "Deploy-time learning: The Missing Middle" uses a colon-subtitle format that does not compose as a prose fragment. "since deploy-time learning: the missing middle" is grammatically broken. The subtitle "The Missing Middle" is an editorial flourish rather than a composable phrase. A claim-form title like "deploy-time learning fills the gap between training and in-context adaptation" would link naturally into sentences in other notes.
  Recommendation: Rewrite as a composable claim, e.g. "deploy-time learning fills the gap between training and in-context learning" or "deploy-time learning is system-level adaptation through durable symbolic artifacts."

INFO:
- [Claim strength] The title is topical with an editorial subtitle rather than a contestable claim. Per the exceptions, topical titles are acceptable for multi-claim framework notes, and this note presents both a taxonomy (three timescales) and a gradient (verifiability). The current title is within bounds but "The Missing Middle" carries framing rather than information -- a claim-form title would be stronger.

CLEAN:
- [Description discrimination] Description "Deploy-time learning fills the gap between training and in-context — durable symbolic artifacts provide inspectable adaptation across sessions along a verifiability gradient" adds mechanism (durable symbolic artifacts, inspectable adaptation) and scope (verifiability gradient) beyond the title. An agent seeing this in a list of 5 results would know immediately that this note covers the how (symbolic artifacts) and the organizing principle (verifiability gradient), not just the gap claim.
- [Title-body alignment] The title frames deploy-time learning as the overlooked middle between training and in-context learning. The body delivers exactly this: a three-timescale taxonomy placing deploy-time learning between the other two, a verifiability gradient organizing the mechanisms, concrete examples at each grade, failure modes, and related work. No drift detected.

Overall: 1 warning, 1 info
===
