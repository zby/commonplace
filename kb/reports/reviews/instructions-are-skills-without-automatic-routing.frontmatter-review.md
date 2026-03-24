<!-- REVIEW-METADATA
note-path: kb/notes/instructions-are-skills-without-automatic-routing.md
last-full-review-note-sha: 1aef73df0bc3e0c287b8413b75dd39aef920a85d
last-full-review-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-full-review-at: 2026-03-24T20:55:23+01:00
last-accepted-note-sha: 1aef73df0bc3e0c287b8413b75dd39aef920a85d
last-accepted-note-commit: 2cc208c7d264b0834d0fe6c1fc666e16dbb15a41
last-accepted-at: 2026-03-24T20:55:23+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: instructions-are-skills-without-automatic-routing.md ===

Checks applied: 4

WARN:
(none)

INFO:
(none)

CLEAN:
- [Description discrimination] Description adds mechanism ("same format as skills but without activation triggers or CLAUDE.md routing entries") and invocation context ("invoked when a human points the agent at them") beyond what the title carries. Against 5 search results for "instructions" or "skills," this description pinpoints the specific architectural relationship (skills minus routing) and the concrete location (kb/instructions/), which discriminates well.
- [Title composability] "since instructions are skills without automatic routing, we designed..." reads naturally as a sentence fragment. The title functions as a linkable clause.
- [Claim strength] The claim that instructions ARE skills (minus routing) is contestable — someone could argue instructions are a fundamentally different artifact type, or that all reusable procedures should have automatic routing. The title names a specific architectural equivalence that carries real design commitment.
- [Title-body alignment] The body's core argument matches the title: instructions share distillation quality and format with skills, differing only in discoverability machinery. The extended sections (execution optimization, adjacent concept distinctions, creation process, platform independence) all support or elaborate the central claim without drifting from it.

Overall: CLEAN
===
