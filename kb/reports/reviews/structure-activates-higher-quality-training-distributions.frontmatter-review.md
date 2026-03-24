<!-- REVIEW-METADATA
note-path: kb/notes/structure-activates-higher-quality-training-distributions.md
last-full-review-note-sha: 3ad9d6f2d9fc131339690dafb9cb870d0ca16d1a
last-full-review-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-full-review-at: 2026-03-24T20:57:00+01:00
last-accepted-note-sha: 3ad9d6f2d9fc131339690dafb9cb870d0ca16d1a
last-accepted-note-commit: fd0b8fb01d3e8c63e580847019636c0e1e2eff01
last-accepted-at: 2026-03-24T20:57:00+01:00
last-acceptance-kind: full-review
review-type: frontmatter-review
-->

=== FRONTMATTER REVIEW: structure-activates-higher-quality-training-distributions.md ===

Checks applied: 4

WARN:
- [Title-body alignment] The title asserts "Structure activates higher-quality training distributions" — presenting the distribution-selection mechanism as established. But the body's own conclusion states: "The evidence supports 'structure helps, and the need for it doesn't dissolve with scale' but not the stronger thesis that it works specifically via activating higher-quality training subsets." The title commits to the stronger causal claim that the body explicitly says is unconfirmed.
  Recommendation: Soften the title to match the body's actual established finding. Options: "structure may activate higher-quality training distributions" (hedged), or pivot to the confirmed claim: "structured templates improve generation quality in ways that persist with scale." Alternatively, if the seedling is meant to stake out the strong claim as a hypothesis to be confirmed, the status note could be surfaced into the title framing (e.g., as a question or hypothesis marker).

CLEAN:
- [Description discrimination] The description adds mechanism ("steer autoregressive generation toward higher-quality training data") with concrete examples ("scientific papers, legal analyses") and names the core concept ("distribution selector"). It goes well beyond restating the title and would distinguish this note from adjacent notes about structure helping quality.
- [Title composability] "Since structure activates higher-quality training distributions..." reads naturally as a sentence fragment. The title works as a linkable prose element.
- [Claim strength] The claim is specific and contestable — someone could argue structure helps via constraining output format rather than via activating different training subsets. The note itself discusses this alternative explanation. Not a truism.

Overall: 1 warning, 0 info
===
