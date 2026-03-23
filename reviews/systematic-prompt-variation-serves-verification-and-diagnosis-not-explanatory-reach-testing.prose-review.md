=== PROSE REVIEW: systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The note's core claim is the three-way distinction (verification vs. diagnosis vs. reach testing), yet the "Prompt ablation is adjacent but distinct" section introduces a fourth category that receives a full paragraph of comparative analysis. This fourth category is not in the title, not in the summary table's three rows, and not in the opening paragraph's two-bullet framing. The section pulls attention away from the core trichotomy and risks making the note's scope ambiguous — is it a three-way or four-way taxonomy? Meanwhile the "Why the distinction matters" section, which carries the note's practical payoff, is roughly the same length as the ablation tangent.
  Recommendation: Either promote prompt ablation into the title/table/intro (making the note explicitly a four-way taxonomy) or shrink the ablation section to a single sentence with a link, keeping the note focused on the three-way distinction it advertises.

INFO:
- [Confidence miscalibration] The sentence "The three operations separate cleanly" followed by the summary table asserts clean separation as a fact. The table itself is the note's own construction (not cited from a source). This is a mild case — the note is a `seedling` and the framing is analytical rather than empirical — but "separate cleanly" reads as established finding rather than proposed decomposition. A phrase like "can be separated along three dimensions" would better match the epistemic status.

CLEAN:
- [Source residue] The note claims to be about methodological distinctions across prompt variation uses. All examples and vocabulary stay at that abstraction level — "prompt," "framing," "soft oracle," "paraphrase," "metamorphic transformations." References to specific linked notes (error correction, PromptSE ingest, reach note) are explicitly framed as instances. No leaked domain-specific residue detected.
- [Pseudo-formalism] The note uses a comparison table, but the table genuinely organizes information (what is varied / what is held fixed / success criterion) that would be harder to parse in prose. No variables, equations, or symbolic apparatus. Clean.
- [Orphan references] All empirical or specific claims are linked to source notes or ingests. The PromptSE reference points to an ingest file. Deutsch's reach test points to the reach note. No floating data points or uncited specifics.
- [Unbridged cross-domain evidence] The note operates within a single domain (LLM evaluation methodology) throughout. The Deutsch reference is to epistemology, but the note explicitly marks the boundary: "This is a quality test for ideas, not for model behavior." The bridge is present and the distinction is the note's entire point. Clean.
- [Redundant restatement] Each section opens with new content. The "Why the distinction matters" section could appear to restate the earlier distinctions, but it adds the misreading failure modes (diagnostic mistaken for aggregation, verification mistaken for instability, reach reduced to robustness) — these are new contributions, not restatements. Clean.
- [Anthropomorphic framing] The note avoids anthropomorphic language. Models are described as having "behavior," producing "output swings," and "tracking surface cues." No attribution of knowledge, understanding, or belief. Clean.

Overall: 1 warning, 1 info
===
