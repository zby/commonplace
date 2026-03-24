<!-- REVIEW-METADATA
note-path: kb/notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md
last-full-review-note-sha: 62ebf0665c1e483783f9912de555805125e55e06
last-full-review-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-full-review-at: 2026-03-24T20:57:31+01:00
last-accepted-note-sha: 62ebf0665c1e483783f9912de555805125e55e06
last-accepted-note-commit: ce667c93a6031f936b4d019b6cdf12e27b7a461a
last-accepted-at: 2026-03-24T20:57:31+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism ("programmers trained on traditional software expect broken infrastructure to fail loudly; semantic recovery in agent tool loops violates that expectation") and implication ("successful outcomes can create false confidence during debugging and maintenance") beyond what the title carries. An agent searching for notes about debugging in agent systems would be able to distinguish this note from, say, the parent note on apparent success as an unreliable health signal — the description makes clear this one is about the human-cognition side (inherited expectations from traditional software).
- [Title composability] "since traditional debugging intuitions break when tool loops can recover semantically, we designed observability around execution paths rather than final outcomes" reads naturally as a linked prose fragment.
- [Claim strength] The claim is contestable — someone could argue that standard debugging practices (log inspection, trace analysis) transfer adequately to agent tool loops and that semantic recovery does not meaningfully change the debugging model. The title names a specific mechanism (semantic recovery) and a specific consequence (debugging intuitions break), which is sharper than a generic observation about agents being hard to debug.
- [Title-body alignment] The body directly supports the title's claim across three sections: why the old intuition is reasonable (success implies healthy mechanism in traditional software), what changes with semantic recovery (synthesized fallbacks decouple success from mechanism health), and how this misleads in practice (broken helpers persist behind apparently healthy runs). The note stays focused on the debugging-intuition angle and explicitly positions itself as the human-cognition complement to the parent note on apparent success.

Overall: CLEAN
===
