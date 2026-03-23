=== PROSE REVIEW: document-types-should-be-verifiable.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The section "What went wrong with flat types" asserts "half the notes were 'design'" as a factual claim about the KB's historical state. This is presented as established fact but reads as an approximation or recollection — no data is cited. If this is a rough estimate, language like "a large fraction" or "many of the notes" would better match the epistemic status.
  Recommendation: Either verify the proportion and state it precisely, or soften to an approximation ("a large share," "many").

- [Proportion mismatch] The core claim is in the title: document types should be verifiable. The section that carries the most weight for this claim — "What 'verifiable' means" — is the shortest substantive section (two short paragraphs). Meanwhile "Base types + traits" and "Programming language parallels" together receive significantly more development. The design solution (base types + traits) is important but is an application of the verifiability principle, not the principle itself. The note's center of gravity sits on the solution rather than the argument for the principle.
  Recommendation: Develop "What 'verifiable' means" with more concrete examples of the boundary between structural and subject-matter types, or consider whether the base-types-plus-traits design deserves its own note (composability — the design is reusable independently of the verifiability argument).

INFO:
- [Source residue] The note draws heavily on programming-language type theory (gradual typing, protocols, refinement types, soft typing). This is deliberate and well-framed — the "Programming language parallels" section explicitly maps each concept. However, the phrase "In object-oriented terms, this is like having `class ResearchInsight` but being forced to inherit from only one of `Research` or `Insight`" in the "What went wrong with flat types" section uses OO vocabulary mid-argument without flagging it as an analogy the way the parallels section does. It reads as though the author momentarily shifted registers.
  Recommendation: Either move this analogy to the parallels section or add a brief framing phrase ("To use an OO analogy, ...") to keep the register consistent with the rest of that section.

- [Anthropomorphic framing] The note uses "an agent reading `type: design` learns nothing" and similar formulations throughout. In context this is reasonable — the note explicitly defines its processor as an LLM agent and consistently uses "agent" as the term of art. The language is anthropomorphic but intentionally so and consistently applied. Flagging only for completeness; no action needed unless the author wants to tighten the distinction between agent-as-software and agent-as-reasoner.

CLEAN:
- [Source residue] The programming-language parallels are the note's explicit framing device, not leaked residue from a source. The note's claimed generality level (document type systems for agent-operated KBs) is maintained throughout; PL concepts are presented as analogies with clear mapping tables.

- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus is used. The YAML blocks serve as concrete examples of the proposed system, not as pseudo-formal proofs. The tables are descriptive, not decorative.

- [Orphan references] No unsourced specific numbers, named studies, or empirical claims appear in the note. The "half the notes" claim (flagged under confidence miscalibration) is the closest case; all other claims are structural arguments or references to other notes in the KB.

- [Unbridged cross-domain evidence] The note's cross-domain moves (PL type theory to document classification) are explicitly bridged. Each parallel is mapped with a clear "X in PL corresponds to Y in this system because Z" structure. The "Programming language parallels" section does this systematically, and inline references (e.g., "like `Any` in a gradually typed language") are brief enough to work as illustrative shorthand.

- [Redundant restatement] Sections open with their own contributions. The "But our processor interprets underspecified instructions" section might appear to restate the previous section's point about enforcement, but it actually introduces a new concern (underspecification of type assignment itself) that the previous section did not address.

Overall: 2 warnings, 2 info
===
