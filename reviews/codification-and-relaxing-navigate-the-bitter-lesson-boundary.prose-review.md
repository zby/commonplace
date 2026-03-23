=== PROSE REVIEW: codification-and-relaxing-navigate-the-bitter-lesson-boundary.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The epiplexity paragraph asserts "High-epiplexity regularities are genuinely structural — codifying them is safer because they reflect real patterns, not artefacts of the observer's computational budget." This is the note's own application of the Finzi framework to codification decisions — a novel interpretive bridge — but it is stated as established fact. The source provides the epiplexity/entropy distinction; the claim that this maps onto safe-to-codify vs. unsafe-to-codify is the note's construction and should be flagged as proposed.
  Recommendation: Hedge the application: "If epiplexity reliably identifies structural regularities, codifying high-epiplexity patterns would be the safer bet" or similar. The source result itself can stay asserted; the codification inference is what needs hedging.

- [Confidence miscalibration] The induction bias paragraph ends with a strong claim: "the step-by-step structure that codification encodes is the kind of regularity that persists under scaling." The source supports this for calculator-class state tracking specifically, but the sentence generalises beyond that domain to "the kind of regularity that codification encodes" in general. The qualifier "calculator-class" appears earlier in the paragraph but the concluding sentence drops it.
  Recommendation: Keep the scope marker in the conclusion: "...for calculator-class tasks, the step-by-step structure that codification encodes is the kind of regularity that persists under scaling."

INFO:
- [Proportion mismatch] The note's core contribution is the codify/relax hybrid strategy and how spec mining improves the odds. Section 2 ("Every codification is a bet") is the longest section and develops the spec-mining argument, the epiplexity grounding, and the induction-bias evidence at length. Section 1 ("The trade-off depends on which regime you're in") introduces the two regimes and defines relaxing — arguably the more foundational concept — in a single sentence: "Codification therefore has a complement: **relaxing** — replacing a codified component with a learned or general-purpose one when scale makes that viable." The title promises that both codification AND relaxing navigate the boundary, but relaxing gets only a definition and a brief historical illustration (edge detection, FlashAttention), while codification gets the full argumentative development. This is not severe — the note's emphasis on codification bets is coherent — but the title sets an expectation of balance that the body doesn't quite meet.

- [Pseudo-formalism] The notation "sharing factor kappa approximately 1 or kappa < 1" and "kappa = 0.28 for CoT" imports formal symbols from the source without defining what kappa measures or what its values mean in this note's terms. A reader unfamiliar with the Ebrahimi source cannot interpret "kappa = 0.28" — the number is decorative without a gloss. The notation does genuine work in the source; in this note, a prose paraphrase ("transformers learn isolated, length-specific solutions — adding training diversity actively hurts performance") would carry the same information.
  Recommendation: Either add a one-sentence definition of kappa (e.g., "the sharing factor measures how much a model reuses mechanisms across task variations; kappa = 1 means fully isolated solutions") or replace the notation with its prose interpretation and point the reader to the source for the formal treatment.

CLEAN:
- [Source residue] The note claims to be about the boundary between codification and relaxing as general strategies. The examples — edge detection, FlashAttention, tokenizers, arithmetic, chess — are drawn from multiple domains and framed as illustrative instances of the general pattern. No single source domain's vocabulary dominates. Terms like "spec," "regularity," "component" are domain-neutral. Clean.

- [Orphan references] Specific claims — the edge detection historical trajectory, FlashAttention as hand-crafted optimization, the Finzi and Ebrahimi results — are either cited with source links or are common enough technical knowledge to stand without citation. No unsupported specific numbers or unnamed studies appear outside the cited material (the kappa values are attributed to the Ebrahimi source). Clean.

- [Unbridged cross-domain evidence] The two cited sources (Finzi on epiplexity, Ebrahimi on induction bias) are applied to the codification question with explicit bridge reasoning: Finzi is bridged via "codifying them is safer because they reflect real patterns," and Ebrahimi is bridged via "codification bets in the arithmetic regime are not merely safe-for-now." Whether these bridges are fully convincing is a semantic-review question; the note does not leave them unbridged. Clean.

- [Redundant restatement] Each section opens with new content. Section 2 does not re-explain the arithmetic/vision-feature distinction from Section 1; it builds on it by introducing the betting frame. Section 3 (Working heuristics) does not restate the argument. Clean.

- [Anthropomorphic framing] The note uses "learned" to describe model capabilities (e.g., "learned features," "learned representations"), which is standard ML vocabulary, not anthropomorphic attribution. No instances of "understands," "knows," "believes," or "possesses." Clean.

Overall: 2 warnings, 2 info
===
