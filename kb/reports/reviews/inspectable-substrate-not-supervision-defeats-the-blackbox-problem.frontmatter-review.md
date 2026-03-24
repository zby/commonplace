<!-- REVIEW-METADATA
note-path: kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md
last-full-review-note-sha: 0a8e35cc8570fa10e3a92a6018be6155fd810c78
last-full-review-note-commit: 3c3418d44ae167551bae036f7a968e8d0e8a64f2
last-full-review-at: 2026-03-24T20:55:21+01:00
last-accepted-note-sha: 0a8e35cc8570fa10e3a92a6018be6155fd810c78
last-accepted-note-commit: 3c3418d44ae167551bae036f7a968e8d0e8a64f2
last-accepted-at: 2026-03-24T20:55:21+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("choosing a substrate (repo artifacts) that any agent can inspect, diff, test, and verify") and context (Chollet's ML framing of agentic coding) beyond the title. It also names the rejected alternative ("not by requiring human review"), which helps an agent distinguish this note from supervision-focused notes. Strong discriminator.
- [Title composability] "since inspectable substrate, not supervision, defeats the blackbox problem" reads naturally as a sentence fragment in another note's argument. The parenthetical comma structure is slightly unusual but parses correctly.
- [Claim strength] Contestable: Chollet's own position implicitly argues the opposite (agentic coding produces blackboxes like ML), and many practitioners would argue supervision is necessary regardless of substrate. The claim takes a specific, non-obvious stance.
- [Title-body alignment] The body directly supports the title's claim: it presents Chollet's blackbox framing, argues that repo artifacts break the analogy because they are inspectable (unlike weights), and maps ML failure modes to codification equivalents where every mitigation depends on inspectability. The final section on the verifiability gradient as the "Keras" answer extends the argument but stays within scope — it is presented as an implication of the core inspectability claim, not a separate thesis.

Overall: CLEAN
===
