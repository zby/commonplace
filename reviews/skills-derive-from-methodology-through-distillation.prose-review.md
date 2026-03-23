=== PROSE REVIEW: skills-derive-from-methodology-through-distillation.md ===

Checks applied: 8

WARN:
(none)

INFO:
- [Confidence miscalibration] The note has `status: seedling` but uses assertive language throughout: "Conflating them produces confused designs," "the distillation isn't optional," "Distillation is the process that produces the skill tier from the methodology tier." For a seedling-status note proposing its own terminological framework, these read as established conclusions rather than proposed ones. The structured-claim format and the Caveats section do signal that this is an argument being made, which mitigates the issue — but a reader scanning the Reasoning section alone would encounter confident assertions without hedging. Worth checking whether the seedling status should be promoted (if the author considers the argument settled) or whether a few hedge phrases should be added to the Reasoning section (if it's genuinely still developing).

- [Anthropomorphic framing] "the agent never graduates from needing the loaded context" — "graduates" attributes a human developmental trajectory to the agent. The sentence is making a precise technical point (LLM agents never internalize context across sessions), and the human/LLM contrast is deliberate, so the word choice is defensible as rhetorical. But "the agent never stops needing loaded context" or "the agent permanently requires loaded context" would make the same point without the metaphor. Minor.

CLEAN:
- [Source residue] The note's generality level (methodology→skill relationship in any knowledge base) is consistent throughout. The `/connect` skill is used as a concrete example but is explicitly framed as one ("The `/connect` skill encodes procedures..."). The chemical distillation and ML distillation analogies are both introduced with clear framing as analogies, not as the domain itself. No unframed domain-specific leakage detected.

- [Pseudo-formalism] The comparison table (codification / constraining / distillation) organizes a three-way distinction that the prose develops across multiple sections. Deleting the table would force the reader to reconstruct the comparison from scattered paragraphs — it genuinely aids comprehension. No decorative notation present.

- [Proportion mismatch] The core claim is that distillation is the right term for the methodology→skill relationship. The "Distillation fits" subsection (~4 paragraphs with a bulleted list of mapped properties) is the longest subsection in Evidence, appropriately receiving the most development. The two "It is not X" subsections are concise since they serve as foils. Reasoning develops implications proportionally. No imbalance detected.

- [Orphan references] No unattributed specific numbers, percentages, or named studies. "Cramer's skill synthesis" is linked to its source. The ML distillation comparison references general knowledge in the field rather than a specific study. The chemical distillation description is common knowledge. All specific claims are either linked or self-evidently general.

- [Unbridged cross-domain evidence] Two cross-domain analogies are used: chemical distillation and ML knowledge distillation. Both are explicitly introduced as analogies with mapped properties. The chemical metaphor is walked through property by property ("heat a mixture, the volatile components evaporate...") and its limits are noted in Caveats ("breaks if pushed to 'what are the volatile vs. non-volatile components?'"). The ML analogy gets its own subsection titled "The ML resonance is useful but inexact" with an explicit statement of where the analogy breaks. No unbridged transfers.

- [Redundant restatement] Each section opens with new material. "Why the distinction matters" introduces the three-way comparison table (new). "Distillation is a context-budget operation" introduces the context-economics argument (new). "For agents, distillation is permanent infrastructure" introduces the human/LLM contrast (new). No section opens by restating a prior section's conclusion.

Overall: 0 warnings, 2 info
===
