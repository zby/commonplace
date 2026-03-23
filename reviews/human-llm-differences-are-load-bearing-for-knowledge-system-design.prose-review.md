=== PROSE REVIEW: human-llm-differences-are-load-bearing-for-knowledge-system-design.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The table in "Reason 2" presents its characterizations of human vs. LLM readers as established fact — "Cannot fill gaps," "Starts fresh every session," "May perform worse with excessive hedging" — but these are the note's own analytical framework, not cited findings. The table format amplifies the effect by presenting claims in declarative cells with no hedging. The row "May perform worse with excessive hedging (reduced instruction clarity)" is the only cell that hedges; the others assert flatly. For instance, "Cannot fill gaps — if it's not in the loaded context, it doesn't exist" is a defensible simplification but still a modeling choice, not a proven law.
  Recommendation: Add a brief framing sentence before the table acknowledging it as a proposed characterization (e.g., "A rough decomposition of how these readers differ:"). Alternatively, soften the most absolute cells — "Cannot fill gaps" could become "Has very limited ability to fill gaps from outside the loaded context."

- [Proportion mismatch] The note's core claim is in the title: human-LLM differences are *load-bearing* for knowledge system design. The section that most directly demonstrates this — "What goes wrong without this awareness" (the consequence section that proves the differences are load-bearing, not merely interesting) — gets roughly 180 words across three short paragraphs. Meanwhile, "Reason 2: KB documents serve dual audiences" gets roughly 350 words. The consequence section is the one that converts the observation into a design principle, yet it receives thinner treatment. Each failure mode ("Naive anthropomorphism," "Naive mechanism-ism," "Audience-blind documents") is developed with a single compressed paragraph, while the dual-audience table gets five detailed rows.
  Recommendation: Consider expanding the failure-mode descriptions with brief concrete examples of each mistake in practice. Alternatively, if the dual-audience observation is genuinely the core contribution (as the description field suggests), consider whether the title should foreground it more directly.

INFO:
- [Anthropomorphic framing] The note uses "cognitive properties" in the closing sentence of the methodological claim: "the genuine partial overlap between human and LLM cognitive properties." This attributes "cognitive properties" to LLMs, which may carry stronger claims about LLM internals than intended. The rest of the note is careful about this — it uses "text processing," "reader," and "consumer" for LLMs. The phrase appears only once and in a context where the comparison is deliberate, so this is INFO rather than WARN.

CLEAN:
- [Source residue] The note claims generality over knowledge system design and maintains it consistently. Examples (Zettelkasten, PKM, Toulmin, library science) are explicitly framed as illustrative instances of "existing traditions and materials." No leaked domain-specific vocabulary from a narrower source context.

- [Pseudo-formalism] No formal notation, variables, or equations appear. The table in Reason 2 functions as structured comparison rather than pseudo-formal apparatus — it organizes parallel claims and would lose clarity if converted to prose.

- [Orphan references] No unattributed specific numbers, percentages, or named studies appear in the body. The "466 OSS projects" claim in the Relevant Notes section is attributed to a cited source. The body text avoids empirical specifics entirely, relying on analytical argument.

- [Unbridged cross-domain evidence] The note's entire argument is about the cross-domain gap between human cognition and LLM processing, so domain-bridging is the subject matter rather than a hidden assumption. Where specific transfer claims are made (e.g., "Toulmin structure works for LLMs"), the note explicitly cites the failure-mode overlap argument as the bridge mechanism. The indirection cost example explicitly states the different reasons (context budget vs. cognitive load) and the similar design response.

- [Redundant restatement] Section openings each introduce new content. "Reason 2" opens with "This is the deeper reason" — a single transition sentence that adds a priority claim rather than restating Reason 1. "What goes wrong without this awareness" opens directly with its first failure mode. "The methodological claim" opens with the operational principle. No section re-explains prior sections before contributing its own content.

Overall: 2 warnings, 1 info
===
