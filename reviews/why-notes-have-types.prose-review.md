=== PROSE REVIEW: why-notes-have-types.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The note's title claims to answer "why notes have types," making the core claim the justification for the type system. The Output quality section (lines 30-36) receives the most development — three linked sub-arguments, a bullet list, and a synthesizing paragraph — while Navigation, Metadata enforcement, Verification, Extensibility, and Maturation each get a single paragraph. This is defensible for a hub note that delegates detail to linked notes, but the Output quality section breaks the delegation pattern by developing its argument inline rather than pointing outward. Either the other five sections are underdeveloped relative to Output quality, or Output quality over-develops material that belongs in the linked notes.
  Recommendation: Consider whether the three-bullet argument and the synthesizing paragraph ("The arguments are independent and complementary...") belong in a separate hub note for the output-quality role specifically, with this section matching the delegation depth of the other five. Alternatively, give the other sections comparable inline development.

INFO:
- [Confidence miscalibration] The opening line states "The type system serves six distinct roles" as a definitive inventory. The note then also includes a seventh section, "Why free-form, not enum," which is not a role but a design rationale. The count of six is accurate to the section headings, but the flat assertion of "six distinct roles" implies a complete enumeration. If the type system later acquires a seventh role, the count becomes wrong without anyone noticing. Worth checking whether the hard count adds enough value to justify the maintenance cost.

CLEAN:
- [Source residue] The note discusses a type system for a knowledge base. All vocabulary — "frontmatter," "description," "types/ subdirectory," "structured-claim template," "agents," "LLMs" — belongs to the note's own domain. No leaked terminology from a narrower source domain was detected.
- [Pseudo-formalism] The note contains no formal notation, equations, or symbolic apparatus. The verification gradient description (line 22: "from deterministic... through LLM rubric... to corpus-level") is expressed in prose. Clean.
- [Orphan references] No specific numbers, percentages, named studies, or unsourced empirical claims appear in the note. All claims are either the note's own design arguments or are delegated to linked notes. Clean.
- [Unbridged cross-domain evidence] The Output quality section discusses transfer from human writing structures to LLMs (line 31), but this claim is delegated to a linked note rather than asserted inline. No cross-domain evidence is cited directly in this note without a bridge. Clean.
- [Redundant restatement] Each section opens with its own new content. The Metadata enforcement section references Navigation ("Navigation depends on metadata existing reliably") but as a forward-building dependency, not a restatement. No section re-explains a prior section's conclusion before getting to its own point. Clean.
- [Anthropomorphic framing] Agent language in this note refers to software agents navigating a knowledge base, not to LLMs as cognitive entities. The one sentence about LLMs (line 31: "LLMs exhibit human-like failures") attributes behavioral patterns, not mental states. Clean.

Overall: 1 warning, 1 info
===
