=== PROSE REVIEW: inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its own analytical framework — the failure mode mapping table, the claim that substrate inspectability is the decisive property — with the same assertoric force as Chollet's original observation. "The blackbox analogy holds only if the output substrate is opaque" is stated as fact, but it is the note's own thesis, not an established finding. Similarly, "Every mitigation relies on the same property: the artifact is inspectable. You can write a test for a function. You can't write a test for a weight" presents a contested claim (that inspectability fully defeats the blackbox problem) as a settled conclusion. The title itself — "defeats the blackbox problem" — asserts complete resolution where the note only demonstrates that mitigations exist.
  Recommendation: Soften the framing to match epistemic status. The mapping table is the note's own construction and could be introduced as "Chollet's predicted ML problems map onto codification failure modes — and in each case, the inspectable substrate opens mitigations unavailable to weight-based systems." The concluding line could become "Every listed mitigation depends on the same property..." to signal it is scoped to the table. Consider whether "defeats" in the title overstates the argument — "mitigates" or "counters" may be more defensible.

- [Proportion mismatch] The core claim is that inspectable substrate (not supervision) is what defeats the blackbox problem. The section that carries this argument — "Where the framing breaks" — is a single short paragraph (two paragraphs, ~100 words). The failure mode mapping table and "The real question" section together receive roughly equal or greater word count, yet they are supporting material. The load-bearing argument (why inspectability is the decisive property, and why supervision is not) gets thin treatment compared to the downstream consequences.
  Recommendation: Develop "Where the framing breaks" further. The key move — that the substrate's structure, not the reviewer's identity, is what breaks the blackbox analogy — deserves more than one paragraph of argument. What specifically makes repo artifacts "inherently inspectable"? What does inspectability require beyond readability?

INFO:
- [Anthropomorphic framing] "An LLM can review a diff and catch a Clever Hans shortcut in generated code" — "catch" implies the LLM recognizes the shortcut the way a human reviewer would. This is mild and arguably intentional (the note's point is precisely that LLMs can do review work), but "detect" or "flag" would be more precise about the mechanism.

CLEAN:
- [Source residue] The note is explicitly about agentic coding and ML failure modes. All domain-specific terms (Clever Hans shortcuts, overfitting, concept drift, data leakage, diff review, CI gates, property-based tests) belong to the domains the note claims to address. No residue from an unrelated source domain was found.

- [Pseudo-formalism] No formal notation, equations, or variable definitions are used. The table in "The failure mode mapping" is a structured comparison, not pseudo-formal apparatus — it organizes a parallel argument rather than pretending to be a formal proof.

- [Orphan references] The Chollet source is linked. The ML failure modes (overfitting, Clever Hans, concept drift, data leakage) are standard terminology that does not require citation. No specific numbers, percentages, or named studies appear without attribution.

- [Unbridged cross-domain evidence] The note explicitly addresses the mapping between ML failure modes and codification failure modes — the cross-domain transfer IS the note's subject. The bridge is provided by the table structure and the repeated argument that inspectability is the shared differentiator. No unbridged transfers were found.

- [Redundant restatement] Each section opens with new material. "Where the framing breaks" does not restate "The claim from ML"; it directly advances the counter-thesis. "The failure mode mapping" does not restate the prior section but extends it with specific parallels. "The real question" picks up Chollet's question and proposes an answer. No redundant restatement detected.

Overall: 2 warnings, 1 info
===
