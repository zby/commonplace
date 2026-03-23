=== PROSE REVIEW: alexander-patterns-and-knowledge-system-design.md ===

Checks applied: 8

WARN:
- [Orphan references] The open questions section references "Alexander's 15 properties of living structure" — a specific numbered set from "The Nature of Order" — with no citation, enumeration, or context for a reader unfamiliar with the source. The two Alexander books ("A Pattern Language," "The Nature of Order") are named but never cited with edition, year, or chapter. The "15 properties" reference is the most problematic because it invites the reader to evaluate a mapping they cannot look up from the note alone.
  Recommendation: Add a parenthetical or footnote with enough detail to locate the 15 properties (e.g., book and chapter), or drop the specific number and say "Alexander's properties of living structure." Consider adding minimal citations for both books on first mention.

INFO:
- [Confidence miscalibration] The frontmatter declares `status: speculative` and the title uses neutral "connect," but individual sentences within the body assert mappings as fact rather than proposing them. "This maps to our codification trajectory" and "Alexander was doing document classification for architectural knowledge decades before any of us" read as established conclusions, not speculative framings. The "Vague" section handles this well ("might work the same way"), but the "Concrete" and "Structural" sections do not consistently match the note's declared epistemic status.
- [Proportion mismatch] The "Concrete" section — labeled as the most grounded level of connection — gets roughly one paragraph of development, while the "Structural" section gets three paragraphs. If the concrete connection is the most defensible, it may deserve more development (e.g., showing how Alexander's pattern structure maps to specific fields in the KB's type definitions). Alternatively, the current proportions may reflect actual development status, in which case the section headers ("Concrete," "Structural," "Vague") overstate the maturity gradient.
- [Unbridged cross-domain evidence] "Alexander was doing document classification for architectural knowledge decades before any of us" asserts a direct equivalence between architectural pattern structure and document type structure. The structural parallel is visible (both have required sections and inter-entry links), but the note does not state why the similarity is more than superficial — i.e., what shared problem makes the same structure appropriate in both domains.

CLEAN:
- [Source residue] The note's claimed scope is the connection between Alexander's architectural theory and knowledge system design. All domain-specific terms (patterns, centers, generative processes) belong to Alexander's domain, which is the explicit subject. References to Thalo, link contracts, and the codification trajectory belong to the KB's own domain, which is the other explicit subject. No leaked framing from an unrelated third domain.
- [Pseudo-formalism] No formal notation, variables, or equations present. The note argues entirely in prose.
- [Redundant restatement] Each section opens with new material. The three level-headings (Concrete, Structural, Vague) partition the argument cleanly; no section re-explains a prior section's conclusion before contributing its own.
- [Anthropomorphic framing] The note discusses knowledge systems and architectural theory, not model internals. No anthropomorphic language detected.

Overall: 1 warning, 3 info
===
