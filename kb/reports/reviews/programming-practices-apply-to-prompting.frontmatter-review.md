<!-- REVIEW-METADATA
note-path: kb/notes/programming-practices-apply-to-prompting.md
last-full-review-note-sha: 2ae0ce4c09bb624062b8e246406dd4d4eef1ab77
last-full-review-note-commit: d4237bd4b4d2593667e2675f27766515cdacba25
last-full-review-at: 2026-03-24T20:56:17+01:00
last-accepted-note-sha: 2ae0ce4c09bb624062b8e246406dd4d4eef1ab77
last-accepted-note-commit: d4237bd4b4d2593667e2675f27766515cdacba25
last-accepted-at: 2026-03-24T20:56:17+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: programming-practices-apply-to-prompting.md ===

Checks applied: 4

WARN:
- [Claim strength] The title "Programming practices apply to prompting" is close to conventional wisdom — few practitioners in the LLM space would argue the opposite. The note's actual analytical contribution is sharper: it identifies two distinct phenomena (semantic underspecification and execution indeterminism) that create qualitatively different challenges when each practice transfers, and argues that agent statelessness turns what is pedagogical convenience for humans into architectural necessity. A title that captures the distinctive insight — e.g., "programming practices transfer to prompting but underspecification and indeterminism create distinct failure modes" — would be more contestable and more informative as a link fragment.
  Recommendation: Sharpen the title to reflect the note's actual analytical contribution — the two-phenomenon decomposition or the statelessness point — rather than the umbrella observation that practices transfer.

INFO:
- [Description discrimination] The description enumerates the practices and names the two complicating phenomena, which adds retrieval value beyond the title. However, "making some practices harder in distinct ways" restates the title's implication without adding mechanism. The body's strongest discriminator — that indeterminism doubles test runs while underspecification doubles test targets, and that agent statelessness makes these transfers architectural rather than pedagogical — is absent. Adding one of these mechanisms would strengthen discrimination.

CLEAN:
- [Title composability] "since programming practices apply to prompting, we designed..." reads naturally as a sentence fragment. The title works as a linkable prose element.
- [Title-body alignment] The body delivers on the title's promise — it catalogs five practices, shows how each transfers, and explains what makes the transfer non-trivial. The body goes further than the title promises (the two-phenomenon analysis, the statelessness argument), but this is a case of the title underselling the content rather than misaligning with it. No drift detected.

Overall: 1 warning, 1 info
===
