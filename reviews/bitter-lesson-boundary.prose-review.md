=== PROSE REVIEW: bitter-lesson-boundary.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The core framework — "specs that are the problem" vs "theories about the problem" — is the note's own analytical construction, but it is presented with the language of established fact: "The difference isn't scope — it's whether the specification fully captures the problem." The same applies to "It's irrational to bet on emergent reliability via scale when deterministic code gives you perfect correctness at near-zero cost" — the word "irrational" is very strong, and the note's own later section ("you often can't tell which side of the boundary you're on until scale tests the distinction") acknowledges the boundary is hard to identify in practice.
  Recommendation: Hedge the framework introduction to match its epistemic status as a proposed model. Something like "The distinguishing factor appears to be whether the specification fully captures the problem." Soften "irrational" to "a poor bet" or similar — the argument is strong enough without the stronger word, and the qualifier avoids tension with the later acknowledgment of boundary uncertainty.

INFO:
- [Source residue] "Composition failure is the tell" is stated as a general diagnostic principle, but it is derived entirely from the vision-features example (edge detection, corner detection, scale-invariant keypoints not composing into "seeing"). The note does not test this heuristic against a non-vision case. If it is meant as a general signal — applicable to, say, NLP pipelines or agent scaffolding — a second example from a different domain would strengthen the claim.
- [Proportion mismatch] The chess paragraph in "Specs that are the problem vs. theories about the problem" is extended (rules vs. strategy, Deep Blue, AlphaZero, then a further extension into NP-hard optimization, vehicle routing, job-shop scheduling). The chess example is valuable for showing the boundary running through a single system, but the NP-hard addendum introduces a second example in the same breath without developing it. This makes the paragraph do double duty and slightly dilutes the chess illustration's clarity. Consider whether the NP-hard case deserves its own short paragraph or should be cut.

CLEAN:
- [Source residue] The note's claimed scope is AI strategy broadly. Domain-specific examples (SIFT, Haar cascades, chess, arithmetic) are explicitly introduced as named examples, not leaked framing. No vocabulary from a narrower source domain appears as unmarked general language.
- [Pseudo-formalism] No mathematical notation, variables, or equation-like apparatus. The confidence signals table is a structured presentation of heuristic criteria, not decorative formalism.
- [Orphan references] No uncited specific numbers, percentages, or named studies. Historical references (Deep Blue, AlphaZero, SIFT, Haar cascades, Canny edge detection) are common knowledge in the field and do not require sourcing. The transistor, Fourier transform, and public-key cryptography references are used as illustrative historical examples, not empirical claims.
- [Unbridged cross-domain evidence] All examples (computer vision, arithmetic, chess, optimization) are drawn from AI and computing — the note's own domain. No cross-domain transfer is attempted without bridging.
- [Redundant restatement] Section openings advance the argument rather than restating prior conclusions. "In practice, the boundary is a working heuristic" transitions from establishing the boundary to its practical difficulty. "Confidence signals" opens with a hedge that frames the table, not a recap.
- [Anthropomorphic framing] No language attributing mental states to models. "Learned features, which never committed to a theory of seeing" describes a design-level property, not a model's intention. "The bitter lesson ate the strategy" is metaphorical but not anthropomorphic about model cognition.

Overall: 1 warning, 2 info
===
