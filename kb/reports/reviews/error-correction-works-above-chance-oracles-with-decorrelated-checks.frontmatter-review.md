<!-- REVIEW-METADATA
note-path: kb/notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md
last-full-review-note-sha: e0a09796cea2244fa7d1173e4742ea10aadf49b1
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:54:56+01:00
last-accepted-note-sha: e0a09796cea2244fa7d1173e4742ea10aadf49b1
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:54:56+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: error-correction-works-above-chance-oracles-with-decorrelated-checks.md ===

Checks applied: 4

CLEAN:
- [Description discrimination] The description adds mechanism beyond what the title carries. The title states the claim (error correction works with above-chance oracles + decorrelated checks); the description adds quantitative mechanism ("amplification cost scales with 1/(TPR-FPR)^2") and specifies the formal condition ("TPR > FPR"). An agent seeing five results about error correction would use the scaling law and TPR/FPR framing to identify this note. Strong discriminator.

CLEAN:
- [Title composability] "since error correction works with above-chance oracles and decorrelated checks, even weak LLM-as-judge checks can be amplified into reliable validation" reads naturally. The title is a complete claim that composes as a sentence fragment.

CLEAN:
- [Claim strength] The claim is non-obvious and contestable. Someone could reasonably argue that above-chance oracles are insufficient without hard verification (the MAKER paper's position), or that decorrelation among LLM checks is practically unachievable given shared training data. The note explicitly addresses these counterpositions (content bias shared across model families, naive repetition producing correlated checks). This is a genuine claim, not a truism.

CLEAN:
- [Title-body alignment] The title promises two conditions for error correction: above-chance oracles and decorrelated checks. The body delivers on both — Section "The amplification condition: TPR > FPR" establishes the oracle condition with the scaling law, and Section "Decorrelation: the binding constraint for LLM checks" develops the independence requirement with concrete strategies. The body also extends into practical implications (ways to construct oracles, knowledge system applications), but these follow naturally from the two stated conditions. No drift.

Overall: CLEAN
===
