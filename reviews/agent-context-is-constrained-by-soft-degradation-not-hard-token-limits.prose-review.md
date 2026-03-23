=== PROSE REVIEW: agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md ===

Checks applied: 8

WARN:
- [Orphan references] "Context windows have grown roughly 30x per year since mid-2023" — this is a specific empirical claim with no source citation. It appears mid-paragraph as if it were common knowledge, but the growth rate is precise enough to need attribution. If the number is approximate, the precision of "30x per year" overstates the confidence; if it's sourced, the source should be cited.
  Recommendation: Either cite the source for the 30x figure, soften to a qualitative claim ("have grown dramatically"), or remove the specific multiplier.

- [Confidence miscalibration] "LLMs pay interpretation overhead proportional to context complexity" — the word "proportional" asserts a specific functional relationship (linear scaling) that the note does not establish or cite. The ConvexBench reference supports complexity-driven collapse, but collapse is not proportionality. The claim is stronger than the evidence offered for it.
  Recommendation: Weaken "proportional to" to something like "that increases with" or "driven by," which matches the evidence without asserting a specific scaling relationship.

INFO:
- [Unbridged cross-domain evidence] "A CPU signals overflow. A human says 'I'm confused.' An LLM produces confident output..." — the CPU and human analogies are used to sharpen the contrast with LLMs, not as evidence claims, so this is not a full bridging failure. However, "A CPU signals overflow" is slightly misleading — integer overflow in most architectures is silent (wraps without trapping) unless explicitly checked, which actually parallels the LLM case rather than contrasting with it. The analogy may undercut its own point for readers who know this.
  Recommendation: Consider whether the CPU example is worth the risk. A substitute like "A database returns an out-of-memory error" would be unambiguous. Alternatively, keep it but acknowledge the nuance.

CLEAN:
- [Source residue] The note claims generality at the level of "agent context" and "practitioners." Body vocabulary stays at that level — "token," "context window," "API," "model," "benchmark." No leaked domain-specific framing from a narrower source. The three external citations (Liu et al., Anthropic, Paulsen, ConvexBench) are all from the LLM/agent domain the note addresses.

- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus in the note. The "two dimensions" decomposition (volume and complexity) is presented in prose and argued through evidence and mechanism, not through decorative formalism.

- [Proportion mismatch] The core claim is that the soft bound, not the hard limit, is the binding constraint. Section weight is well-allocated: the two-dimension decomposition gets substantial development (volume, complexity, interaction), the invisibility argument gets the longest single section with three sub-arguments, and consequences get proportional closing treatment. No section is starved relative to its load-bearing role.

- [Redundant restatement] Sections open with new content rather than restating prior conclusions. The opening paragraph of "The soft bound is invisible and undisclosed" does briefly echo the hard/soft distinction, but it does so to set up the new "visible vs. invisible" axis, not to restate the prior section's conclusion. The interaction subsection similarly advances rather than repeats.

- [Anthropomorphic framing] The note uses precise language throughout: "the model's ability to follow instructions, retrieve information, and reason correctly," "quality degrades," "the model doesn't signal." No instances of "understands," "knows," "believes," or "possesses knowledge." The phrase "reason correctly" could be flagged but is standard usage in the LLM performance literature and the note does not claim anything about model internals by using it.

Overall: 2 warnings, 1 info
===
