=== PROSE REVIEW: the-augmentation-automation-boundary-is-discrimination-not-accuracy.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The route (a)/(b) taxonomy and the three-tier boundary framework (external hard oracle / self-assessment with high discrimination / self-assessment with low discrimination) are the note's own constructions, but they are presented with assertive language: "The augmentation/automation boundary is therefore not a fixed accuracy threshold but a function of available oracle strength" and "The practical consequence follows from the asymmetry." The derivation from Rabanser et al.'s empirical finding is sound, but the framework itself — that there are exactly two routes, that they exhaust the space, that the boundary reduces to this particular function — is a proposed model, not an established result.
  Recommendation: Soften the framing of the note's own framework. For example: "This suggests the augmentation/automation boundary is not a fixed accuracy threshold but a function of available oracle strength" or "A useful decomposition of the path to automation..." The empirical claims (discrimination stagnation) can remain assertive since they are sourced; the interpretive framework built on top should read as proposed.

INFO:
- [Anthropomorphic framing] The note uses "self-knowledge" twice ("derived from the model's self-knowledge," "waiting for models to develop self-knowledge") and "know" once ("the ability to know, per instance, whether this particular output is likely wrong"). The rest of the note uses the more precise "self-assessment," which is the better term — it describes a measurable system behavior rather than implying a cognitive state. "Self-knowledge" is stronger than the note needs and could be read as making an unintended claim about model internals.

CLEAN:
- [Source residue] The note's generality level is consistent throughout. Domain-specific examples (code execution with test suites, arithmetic with exact verification, structured data with schema validation, the MAKER paper) are all explicitly framed as illustrative instances of external hard oracles. No unframed domain-specific vocabulary leaks through.
- [Pseudo-formalism] The TPR > FPR notation and TPR = FPR = 1.0 example are doing genuine work — they make the discrimination concept precise and connect to the formal condition established in the referenced error-correction note. The "(p,delta,k)-satisfaction" notation appears only in a link annotation, not in the body argument. No decorative formalism.
- [Proportion mismatch] The core claim (boundary = discrimination) is established compactly in the introduction and "Accuracy vs discrimination" section. The longest section ("External oracles bypass the discrimination bottleneck") develops the note's original contribution — why this distinction matters practically and what it implies about the path to automation. This is appropriate; the implication is where the note adds value beyond the distinction itself.
- [Orphan references] All specific figures are either attributed ("14 models across 18 months" to Rabanser et al., "a million steps" to MAKER) or clearly hypothetical ("A 90%-accurate agent," "when a model says '80% confident'"). No unsourced empirical claims.
- [Unbridged cross-domain evidence] All cited evidence (Rabanser et al. on model calibration/discrimination, MAKER on LLM agent reliability, ABC on agent behavioral contracts) comes from the same domain the note addresses — AI/LLM system reliability. No cross-domain transfer without bridging.
- [Redundant restatement] Each section opens with new information or new framing. The "External oracles" section opens by connecting to oracle-strength vocabulary from a referenced note, which is bridging rather than restating prior sections of this note. No redundant setup paragraphs.

Overall: 1 warning, 1 info
===
