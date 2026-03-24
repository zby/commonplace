<!-- REVIEW-METADATA
note-path: kb/notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md
last-full-review-note-sha: 1a25e340bc17fcf9b37dfa6279dc38273e1b3132
last-full-review-note-commit: 8c9732318328522c7e0e66279d8f969bf591a409
last-full-review-at: 2026-03-24T14:34:00+01:00
last-accepted-note-sha: 1a25e340bc17fcf9b37dfa6279dc38273e1b3132
last-accepted-note-commit: 8c9732318328522c7e0e66279d8f969bf591a409
last-accepted-at: 2026-03-24T14:34:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds the four specific failure modes (contamination, inconsistency, amplification, liability diffusion) and frames what channels actually tell you ("how bounded contexts interact") versus what they miss ("which guarantee prevents..."). This is mechanism plus scope beyond what the title carries. A search returning several orchestration-related notes would let a reader distinguish this one by the failure-mode taxonomy in the description.
- [Title composability] "since agent orchestration needs coordination guarantees, not just coordination channels, we designed..." reads naturally as a sentence fragment. The comma-separated contrast ("not just coordination channels") survives embedding without awkwardness.
- [Claim strength] The claim that guarantees matter more than channels is specific and contestable. Someone could argue that channel choice already implies the guarantee, or that guarantees are too expensive to specify and the channel is the right abstraction level. The note argues against both positions, which confirms the claim is doing real work.
- [Title-body alignment] The body delivers exactly what the title promises: it shows why two systems using the same channel can have different reliability (opening paragraph), enumerates four composition modes with their missing primitives and failure modes (table), and closes with the directive to match guarantee to composition mode. No drift in either direction.

Overall: CLEAN
===
