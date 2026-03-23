=== PROSE REVIEW: automated-synthesis-is-missing-good-oracles.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] "Experiments with this KB confirm that automated synthesis readily surfaces interesting candidates" — the opening paragraph asserts experimental confirmation without describing the experiments, their scope, or their results. "Confirm" is strong epistemic language for what is presumably informal experimentation. This contrasts with the note's own `status: speculative` frontmatter, which signals lower confidence than the prose delivers.
  Recommendation: Soften to "Informal experiments with this KB suggest..." or "Early trials with this KB indicate..." to match the speculative status. If the experiments were systematic enough to warrant "confirm," describe them briefly.

- [Confidence miscalibration] "Automated synthesis of natural-language knowledge fails at scale because most of what it produces is not useful" — this is stated as established fact, but the note does not cite evidence for it beyond the KB's own experiments (which are described vaguely). The comparative review finding that "almost nobody automates synthesis" is suggestive but could have many explanations beyond evaluation difficulty. Presenting the oracle gap as *the* reason synthesis fails is a causal claim that the evidence supports as plausible rather than confirmed.
  Recommendation: Frame as "In the experiments available to us, automated synthesis..." or "The pattern across existing systems suggests that synthesis fails at scale because..." — language that acknowledges this is an inference from a limited evidence base.

INFO:
- [Source residue] "Cognee memify — promises synthesis-like operations but ships simpler extraction. The gap between ambition and shipping is itself evidence of the difficulty." — The second sentence asserts that a product shipping less than it promises is evidence that the problem is hard. This is a weak inference (products ship less than promised for many reasons — prioritization, engineering effort, market fit). It reads as an aside built from a specific system review that leaked through as a general-purpose argument.
  Recommendation: Either drop the interpretive gloss ("The gap between ambition and shipping is itself evidence of the difficulty") or hedge it: "The gap may reflect the difficulty, though other explanations (prioritization, engineering effort) also apply."

- [Proportion mismatch] The note's core claim is that synthesis evaluation (the oracle) is the bottleneck, not synthesis generation. The section that carries the most weight for this claim — "Why the oracle is hard to build" — is the shortest substantive section (roughly 8 lines of body text). The "Current attempts" section, which provides supporting evidence but is not the core argument, is roughly twice as long. The core analytical contribution is somewhat thin relative to the survey material.
  Recommendation: Consider developing "Why the oracle is hard to build" further — for instance, expanding on why validity judgment resists automation, or providing examples of validity failures that illustrate the difficulty concretely.

CLEAN:
- [Source residue] The note claims generality at the level of "automated synthesis" of "natural-language knowledge." Body vocabulary stays at that level — "oracle," "extraction," "synthesis," "fidelity," "novelty," "validity." The comparative review examples (tip consolidation, A-MEM, Cognee, /connect) are all clearly framed as specific system instances, not as leaked domain assumptions. KB-specific terms like "/connect skill" are explicitly identified as "this KB's."

- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus. The fidelity/novelty/validity decomposition is presented in prose with clear natural-language definitions. No decorative formalism.

- [Orphan references] No unsourced specific numbers, percentages, or named studies. The "eleven systems" claim is supported by a link to the comparative review. The tip consolidation and A-MEM references link to their sources. The Kim et al. reference in the relevant notes section is contextual rather than an evidentiary claim in the body.

- [Unbridged cross-domain evidence] All cited evidence stays within the note's domain (KB/agent systems). The comparative review is about memory systems; the tip consolidation paper is about self-improving agents; the quality signals note is about KB evaluation. No cross-domain transfer claims that would require bridging.

- [Redundant restatement] Sections open with new content. "Why the oracle is hard to build" opens with the fidelity/novelty/validity distinction, not a restatement of the oracle gap. "Relationship to the boiling cauldron" opens by placing synthesis within a broader taxonomy rather than re-explaining the problem. No restating first paragraphs detected.

- [Anthropomorphic framing] The note uses precise language for LLM behavior: "LLMs can combine," "LLM-merges," "LLM judgment." No instances of "understands," "knows," "believes," or "possesses." The phrase "a human reviewer recognizes" refers to an actual human, not a model.

Overall: 2 warnings, 2 info
===
