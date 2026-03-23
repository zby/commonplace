=== PROSE REVIEW: deploy-time-learning-is-agile-for-human-ai-systems.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts "Agile's real innovation was not 'shorter cycles' or 'embracing change' — it was deciding that code and specs can coexist and co-evolve" as established fact. This is the note's own reframing of agile, not a consensus definition from the agile literature — yet the language ("real innovation was") presents it as correcting a misconception rather than proposing an interpretation. Similarly, "Agile implicitly assumes everything can be codified if you iterate enough" attributes a strong philosophical position to agile without sourcing it. These are plausible readings, but they are the note's constructions and should be flagged as such.
  Recommendation: Hedge the reframing: "A useful way to read agile's core move is..." or "One way to characterize agile's real shift is..." For the implicit-assumption claim, soften to "Agile's implied end state is fully codified software — it treats natural-language specs as temporary" (the note already says this one sentence earlier, so the second assertion is also partially redundant).

- [Proportion mismatch] The core claim is the analogy between agile and deploy-time learning, and the most important intellectual contribution is where they diverge (the boundary-stops-moving argument). The divergence section is ~130 words. The learning-loop section, which enumerates a fairly straightforward five-step cycle, is ~150 words. The waterfall backdrop section, which provides historical context but is not the note's core claim, is ~170 words. The load-bearing section (divergence) is the shortest of the three body sections.
  Recommendation: Develop "Where they diverge" further — the "data report example" is gestured at but not unpacked (see also the orphan-reference finding below). Consider whether the waterfall backdrop section's second paragraph (about changing requirements) could be shortened or split into a brief parenthetical, since it's mostly handled by the linked note.

INFO:
- [Orphan references] "The data report example makes this concrete: statistics move to Python, but narrative interpretation stays with the LLM." This example appears without prior introduction — there is no data report example anywhere earlier in the note, and no source is cited. A reader encountering this note without prior context has no way to evaluate or even picture this example.
  Recommendation: Either introduce the example briefly (one sentence establishing what the data report task involves) or link to a note/source where the example is developed. Alternatively, replace with an example that can be made self-contained in one sentence.

- [Source residue] The note claims a general-level analogy (agile methodology maps onto deploy-time learning), but "the data report example" appears to be residue from a specific project or prior discussion that was not generalized. The phrase "statistics move to Python" is concrete enough to suggest a specific implementation context rather than a general illustration. This is mild — it reads as an example rather than as the note's framing — but its lack of introduction (see orphan-reference finding) makes the residue more noticeable.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus present. The five-step cycle is a numbered list of prose descriptions, which is the appropriate level of formality for the content.
- [Redundant restatement] Each section opens with new material. The waterfall backdrop does revisit the natural-language imprecision theme from the opening, but it adds the formal-methods contrast and the disambiguation-failure link — these are new contributions, not restatements.
- [Anthropomorphic framing] The note discusses LLMs only in terms of their functional role ("behavior in prompts," "narrative interpretation stays with the LLM"). No language attributes mental states or agency to models.
- [Unbridged cross-domain evidence] The note draws an analogy between software methodology (agile) and AI system design (deploy-time learning) but does not cite empirical findings from one domain as evidence for the other. The analogy is structural, and the note explicitly marks the points of divergence. No unbridged transfer present.

Overall: 2 warnings, 2 info
===
