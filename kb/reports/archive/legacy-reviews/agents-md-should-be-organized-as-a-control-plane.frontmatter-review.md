<!-- REVIEW-METADATA
note-path: kb/notes/agents-md-should-be-organized-as-a-control-plane.md
last-full-review-note-sha: ae6fbde449c6736b3e59b2a1d9dc15c5cf991dee
last-full-review-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-full-review-at: 2026-03-24T20:53:38+01:00
last-accepted-note-sha: ae6fbde449c6736b3e59b2a1d9dc15c5cf991dee
last-accepted-note-commit: f510f17f35d4778689dffe6b6c450070001140ef
last-accepted-at: 2026-03-24T20:53:38+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agents-md-should-be-organized-as-a-control-plane.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] Description "Theory for deciding what belongs in AGENTS.md using loading frequency and failure cost, with layers, exclusion rules, and migration paths" adds mechanism (the two decision variables: loading frequency and failure cost) and scope (layers, exclusion rules, migration paths) beyond what the title carries. An agent seeing multiple results about AGENTS.md organization would immediately know this note provides a specific placement framework, not general advice.
- [Title composability] "since AGENTS.md should be organized as a control plane, we designed the routing table with three layers" reads naturally as a sentence fragment. The title composes well in linking contexts.
- [Claim strength] The claim that AGENTS.md should be organized as a "control plane" is specific and contestable. Reasonable alternatives exist: organizing it as a comprehensive reference manual, a minimal pointer file, or a flat checklist. The control-plane metaphor carries a non-obvious commitment to functional placement (invariants, routing, escalation) over topical or chronological organization.
- [Title-body alignment] The body delivers exactly what the title promises. It defines the control-plane model via two placement variables (loading frequency, failure cost), specifies three layers (invariants, routing, escalation boundaries), and adds supporting structure (nested topology, exclusion rules, lifecycle migration, quality tests). No drift in either direction.

Overall: CLEAN
===
