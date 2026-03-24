<!-- REVIEW-METADATA
note-path: kb/notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md
last-full-review-note-sha: 8cb0d1cc4daffc06ce1d646f5f86b80182cbb182
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:54:08+01:00
last-accepted-note-sha: 8cb0d1cc4daffc06ce1d646f5f86b80182cbb182
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:54:08+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md ===

Checks applied: 4

WARN:
- [Description discrimination] The description "Both learning mechanisms — constraining (constraining) and distillation (extracting) — sacrifice generality for compound gains in reliability, speed, and cost; they differ in the operation and how much compound they yield" closely paraphrases the title. The title already says both trade generality for the compound; the description restates this and adds only that they "differ in the operation and how much compound they yield," which is implied by naming two distinct mechanisms. The parenthetical "(constraining)" after "constraining" is also tautological. A discriminating description would add mechanism or implication — for example, that constraining yields its largest compound gain at codification (substrate change) while distillation yields moderate gains through reduced context size, or that the note unifies two mechanisms under one capacity decomposition framework.
  Recommendation: Replace the description with one that names the key differentiator the body establishes — e.g., "Constraining yields its largest compound gain at codification, where the substrate changes; distillation yields moderate gains by compressing source material into smaller context loads. Both reduce generality along the same capacity decomposition."

CLEAN:
- [Title composability] "since constraining and distillation both trade generality for reliability, speed, and cost, we designed..." reads naturally as a sentence fragment. The title works as a linkable prose clause.
- [Claim strength] The claim that both mechanisms make the same fundamental trade-off is contestable — someone could argue distillation merely compresses without sacrificing generality, or that the two mechanisms operate on fundamentally different axes. The note argues against this, making the title a genuine claim.
- [Title-body alignment] The body delivers what the title promises. It defines the trade-off via the calculator example, walks through how each mechanism enacts it, and contrasts the two in a comparison table. No drift detected.

Overall: 1 warning, 0 info
===
