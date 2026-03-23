=== PROSE REVIEW: wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note states "The KB type hierarchy is a codification ladder for thoughts" (opening line) as direct assertion, but this is the note's own metaphor/construction, not an established concept. The codification note defines codification as "constraining that crosses a medium boundary from natural language to a symbolic medium (code)" — moving from text to note to structured-claim stays within natural language the entire time, so calling the type ladder a "codification ladder" asserts an equivalence the note does not defend. The Evidence section then presents the type hierarchy as evidence for the principle, but the mapping (wiki → type ladder) is the note's own argument, not externally grounded.
  Recommendation: Either hedge the framing ("The type hierarchy functions as a refinement ladder — analogous to codification in that each step reduces ambiguity") or explicitly argue why text→note→structured-claim counts as codification despite staying in natural language. The codification note itself distinguishes constraining-within-natural-language from codification proper; this note should acknowledge that distinction.

- [Proportion mismatch] The core claim is in the title: "lowest-friction capture, then progressive refinement in place." The capture-friction half gets one sentence of development ("make saving a thought trivially easy") and is otherwise taken as given. The refinement-in-place half gets substantial development in Reasoning (the paragraph beginning "The key property is refinement in place"). The result is that the note's strongest original contribution — arguing that in-place refinement (stable paths, no migration) is what makes the wiki principle work for a KB — is reasonably developed, but the capture-friction side is asserted without examining what "friction" means in this KB's context (e.g., does adding frontmatter count as friction? Is `text` type actually used?). The two halves of the principle are unequally developed.
  Recommendation: Either develop the capture-friction side (what counts as friction, what the KB's actual capture experience is) or narrow the title/claim to focus on progressive refinement in place, which is where the note's real argument lives.

INFO:
- [Unbridged cross-domain evidence] The note draws a direct parallel between Ward Cunningham's wiki (a multi-user collaborative web platform) and a single-agent KB type system. The shared mechanism is stated as "speed of capture" and "progressive refinement," but the original wiki's refinement was social (many editors converging on quality) while this KB's refinement is structural (one author adding frontmatter and sections). The note does not address whether the mechanism transfers when the social editing dynamic is removed. This may be intentional — the note's claim is about the UX principle, not the social process — but a reader familiar with wikis might expect the distinction to be acknowledged.

- [Source residue] The note uses "WikiWikiWeb (1995)" and the Hawaiian etymology ("wikiwiki" meaning "quick") as framing. These are appropriate for Evidence item 1, which is explicitly about Cunningham's wiki. However, the title itself uses "wikiwiki principle" as if this is a named, established principle. A search for "wikiwiki principle" as a term of art does not surface established usage — this appears to be the note's own coinage. This is minor (the note is clearly constructing an argument, not citing a named principle), but a reader might initially expect a reference to a known concept.

CLEAN:
- [Source residue] Beyond the wiki-specific vocabulary in Evidence item 1 (which is properly scoped as historical evidence), the note's body uses domain-neutral KB terminology throughout. No leaked domain-specific framing from external sources.

- [Pseudo-formalism] The note contains no formal notation, variables, or mathematical apparatus. The "ladder" metaphor is used consistently as a metaphor, not dressed up as a formal model.

- [Orphan references] All specific claims are either about Cunningham's wiki (common knowledge, no citation needed for the basic facts) or about internal KB mechanisms (linked to their defining notes). No unattributed numbers, percentages, or empirical claims.

- [Redundant restatement] Each section opens with new material. The Reasoning section builds on Evidence rather than restating it. The Caveats section addresses genuine limits rather than recapping. No redundant restatement detected.

- [Anthropomorphic framing] The note discusses documents, types, and a KB system — no LLM agency language is present. No anthropomorphic framing issues.

Overall: 2 warnings, 2 info
===
