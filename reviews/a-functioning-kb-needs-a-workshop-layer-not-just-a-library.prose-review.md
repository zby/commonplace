=== PROSE REVIEW: a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The bridge taxonomy is asserted rather than proposed: "This means there are two kinds of bridges needed: **Extraction bridges** ... **Composition bridges**". This decomposition is the note's own construction — it could be three kinds, or one kind with variants — but the language presents it as the necessary structure. Contrast with the temporal-types section, which correctly hedges: "A knowledge base that supports real workflows would likely need:".
  Recommendation: Reframe the bridge taxonomy with proposal language. E.g., "Two kinds of bridges seem needed:" or "A useful decomposition distinguishes two bridge directions:". This matches the epistemic status — a proposed design, not an established finding.

INFO:
- [Confidence miscalibration] The title and opening claim ("a functioning knowledge base also needs to support work in motion") frame the workshop layer as a universal requirement of functioning knowledge bases rather than a design proposal for this specific KB. The argument is built from observation of one system (this KB's task subsystem not fitting the type hierarchy). The closing paragraph partly corrects this ("when we want to build a knowledge base that supports real workflows"), grounding it as forward-looking design rather than universal law. The title carries the stronger framing, though, and titles are what propagate through indexes and link text.
- [Orphan references] "Indexed by qmd for search, but that's the only integration" — "qmd" appears without introduction or explanation. A reader unfamiliar with the codebase's tooling would not know what this refers to. The term is used elsewhere in the KB but is not a self-evident acronym.

CLEAN:
- [Source residue] The note operates entirely within its native domain (knowledge-base design). Vocabulary — types, frontmatter, state machines, lifecycle, extraction, composition — is consistent with the claimed scope. No leaked framing from an external source domain.
- [Pseudo-formalism] The Library/Workshop comparison table is structured prose, not formal notation. It aids scanability of the contrast without claiming mathematical precision. No equations, variables, or formal decompositions that overstate rigor.
- [Proportion mismatch] The core claim (library vs. workshop distinction) is established concisely via the table and surrounding prose. The bridges section elaborates design implications at proportionate length. Open questions are substantial but appropriate for a seedling note exploring design space. No section starves the core claim of attention.
- [Unbridged cross-domain evidence] The note does not import empirical findings from external domains. Internal cross-references (Tulving taxonomy, spec mining) link to other KB notes rather than claiming cross-domain transfer. The Tulving reference in open questions is self-questioned ("may be decorative rather than load-bearing"), which is appropriate self-policing.
- [Redundant restatement] Each section opens with its own contribution. "Temporal document types" transitions in one sentence ("Tasks aren't the only workshop documents") then moves to new content. "Bridges between the layers" opens with a new claim ("bidirectional"). No section re-explains what a prior section established.
- [Anthropomorphic framing] The note discusses knowledge-base architecture, not model cognition. Metaphorical language ("consume value," "produce outcomes") is standard systems-design vocabulary, not anthropomorphism applied to an AI system.

Overall: 1 warning, 2 info
===
