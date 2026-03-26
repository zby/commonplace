<!-- REVIEW-METADATA
note-path: kb/notes/llm-learning-phases-fall-between-human-learning-modes.md
last-full-review-note-sha: e1c0080e190f59880fe36b6bb8a3c09547c8cd70
last-full-review-note-commit: 576f03dd6d74f713dc3305304b5a79b366047e8f
last-full-review-at: 2026-03-24T20:55:50+01:00
last-accepted-note-sha: e1c0080e190f59880fe36b6bb8a3c09547c8cd70
last-accepted-note-commit: 576f03dd6d74f713dc3305304b5a79b366047e8f
last-accepted-at: 2026-03-24T20:55:50+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: llm-learning-phases-fall-between-human-learning-modes.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism the title cannot carry: it explains *why* pre-training is intermediate ("acquires both structural priors... and world knowledge in one pass") and names the spectrum (evolution-to-reaction). An agent seeing five learning-theory results could pick this one based on the "structural priors in one pass" mechanism alone.
- [Title composability] "since LLM learning phases fall between human learning modes rather than mapping onto them, we should work from actual phase properties" reads naturally as a sentence fragment. The title composes well as a linkable clause.
- [Claim strength] The claim is genuinely contestable. Many practitioners do attempt 1:1 mappings (training = education, context = working memory), and the note argues against that common default. Someone could reasonably defend the 1:1 mapping as a useful enough approximation. The seedling status is also consistent with a real claim rather than a placeholder.

INFO:
- [Title-body alignment] The title frames LLM phases as falling *between* human modes. The body supports this for pre-training (between evolution and learning) and in-context learning (between long-term and short-term). However, point 3 under "Why the non-mapping matters" — "No LLM analogue for embodied procedural learning" — is a case of *no correspondence at all*, not an intermediate position. This supports the broader "rather than mapping onto them" clause but goes beyond the "fall between" framing. The deploy-time learning section also extends the Amodei spectrum with KB-specific content not in the original source. Neither is a real problem — the title's "rather than mapping onto them" clause covers both patterns — but the body's actual argument is slightly broader than "intermediate positions on a spectrum."

Overall: CLEAN (0 warnings, 1 info)
===
