<!-- REVIEW-METADATA
note-path: kb/notes/agent-is-a-tool-loop.md
last-full-review-note-sha: c39e0443e6b88a4cb78e4a789afb0c986d4a55f5
last-full-review-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: c39e0443e6b88a4cb78e4a789afb0c986d4a55f5
last-accepted-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agent-is-a-tool-loop.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism beyond the title — it names the three components of the convention (prompt, capability surface, stop condition) and states the pragmatic purpose ("a unit that organizes code"). An agent searching for "tool loop" or "agent definition" would distinguish this note from related agent-architecture notes by the specific convention it establishes.
- [Title composability] "since 'agent' is a useful technical convention, not a definition, we designed the framework around tool loops" reads naturally as a sentence fragment. The title works as a linkable prose element.
- [Claim strength] The claim that "agent" should be treated as a technical convention rather than a definition is genuinely contestable — many practitioners and researchers insist on defining agents through properties like autonomy, planning, or goal-directedness. The note explicitly acknowledges this tension and argues for the pragmatic alternative.
- [Title-body alignment] The body delivers exactly what the title promises: it introduces the convention (tool loop = prompt + capability surface + stop condition), explains why it is deliberately minimal ("says nothing about autonomy, planning, or goals"), and demonstrates the payoff in framework design (sub-agents as sub-loops). No drift.

Overall: CLEAN
===
