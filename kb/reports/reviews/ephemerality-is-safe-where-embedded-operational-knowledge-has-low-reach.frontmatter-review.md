<!-- REVIEW-METADATA
note-path: kb/notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low-reach.md
last-full-review-note-sha: a638b029a416795eabb748cc80aee1343bfc9538
last-full-review-note-commit: 97552f6327e5611cb92cc5d234e33b95ff240e36
last-full-review-at: 2026-03-24T20:54:55+01:00
last-accepted-note-sha: a638b029a416795eabb748cc80aee1343bfc9538
last-accepted-note-commit: 97552f6327e5611cb92cc5d234e33b95ff240e36
last-accepted-at: 2026-03-24T20:54:55+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: ephemerality-is-safe-where-embedded-operational-knowledge-has-low-reach.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description's second clause — "ephemerality is safe only when that knowledge stays local" — restates the title's claim ("low reach" = "stays local") rather than adding new retrieval value. The first clause does useful work by naming the mechanism (Kirsch's barriers as cases where software carries decisions that must survive across runs, users, and audits), but the second half spends its budget paraphrasing the title. A stronger description would use that space to add scope or implication — for example, noting that reach (not code complexity or business importance) is the proposed predictor, or that the note reinterprets Kirsch's four barriers through a single unifying concept.
  Recommendation: Replace the second clause with scope or implication content. For example: "Kirsch's four structural barriers to ephemeral software — edge cases, state surfaces, interface stability, auditability — share a common structure: each embeds operational knowledge that transfers across contexts. Reach, not complexity, predicts where persistence pays."

INFO:

CLEAN:
- [Title composability] "Since ephemerality is safe where embedded operational knowledge has low reach, we can treat one-off scripts as disposable..." reads naturally as a sentence fragment. The title composes well as a linkable clause.
- [Claim strength] The claim is specific and contestable. Someone could argue that ephemerality is never safe in production regardless of reach, or that factors other than reach (e.g., code complexity, team size) are the primary determinants. The note stakes a clear position — reach is the predictor — which is non-obvious and debatable. The seedling status is also noted; this check would apply equally at any status.
- [Title-body alignment] The body directly supports the title's claim. It reinterprets Kirsch's four barriers as reach indicators (sections on edge cases, state surfaces, interface stability, auditability), argues that reach predicts where persistence pays, defines three boundary zones (low-reach, boundary, high-reach), and connects to vibe-noting. The scope of the body matches the title — no drift detected.

Overall: 1 warning, 0 info
===
