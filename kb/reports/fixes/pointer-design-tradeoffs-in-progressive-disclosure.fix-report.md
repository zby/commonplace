## Fix Report: pointer-design-tradeoffs-in-progressive-disclosure

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | sentence/clause-packing | new-pattern: clause-unpack | Split four-directive closing sentence into two sentences at the natural seam between established investments and forward-looking stance | fixed |

### Warning-to-fix mapping

- **#1 (sentence/clause-packing):** "~50 words, four distinct directives packed into one sentence [...] Each directive also carries a parenthetical or qualifier. The dash-separated caveat ('but treat it as supplementary...') appends a fifth clause. This is the closing sentence of the note and carries the practical takeaway — the packing makes the conclusion harder to absorb than it should be. Splitting into two or three sentences would give each recommendation its own emphasis."

### Deferred items
- (none)

### New patterns
- **clause-unpack:** A sentence packs multiple independent directives (each with its own qualifier or parenthetical) into a single comma-separated list. Fix: split at the natural seam that separates distinct concerns, preserving all content and qualifiers. Prefer the fewest splits that resolve the overload — two sentences are better than four if two suffice.
