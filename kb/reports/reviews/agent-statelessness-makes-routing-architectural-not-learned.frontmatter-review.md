<!-- REVIEW-METADATA
note-path: kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md
last-full-review-note-sha: 6fa79f5a6fac6d778a3cd5c28fd3522e94eaafb2
last-full-review-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-full-review-at: 2026-03-24T20:53:37+01:00
last-accepted-note-sha: 6fa79f5a6fac6d778a3cd5c28fd3522e94eaafb2
last-accepted-note-commit: d1d69393d519758d93ae3c6987b3fc2350077c45
last-accepted-at: 2026-03-24T20:53:37+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agent-statelessness-makes-routing-architectural-not-learned.md ===

Checks applied: 4

CLEAN:
- [description-discrimination] The description adds mechanism ("agents never develop navigation intuition — every session is day one") and implication ("permanent architecture, not scaffolding that learners outgrow") beyond what the title carries. The enumeration of concrete routing artifacts (skills, type templates, routing tables, naming conventions, activation triggers) further discriminates this note from adjacent notes about routing or statelessness in general. An agent searching for "routing architecture" would clearly distinguish this from, say, an instruction-specificity note.
- [title-composability] "since agent statelessness makes routing architectural, not learned, we designed the progressive disclosure hierarchy as permanent infrastructure" reads naturally as a sentence fragment. The title works well as a linkable clause.
- [claim-strength] The claim is specific and contestable. One could argue that persistent memory relaxes the statelessness assumption enough to make routing learned (the note itself acknowledges this in its final paragraph), or that routing is always architectural regardless of consumer type. The title names a specific causal mechanism (statelessness) and a specific consequence (architectural vs. learned), which is a non-obvious position.
- [title-body-alignment] The body directly supports the title's claim through four sections: the statelessness observation (why agents never learn), progressive disclosure (the architectural replacement for navigation intuition), the degradation cliff (what happens when routing is missing), and the source-vs-compiled distinction (the maintenance discipline that follows). All sections develop the title's central argument without drifting into unrelated territory. The design consequences section stays within scope by deriving requirements from the architectural nature of routing.

Overall: CLEAN
===
