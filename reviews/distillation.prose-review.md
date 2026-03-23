=== PROSE REVIEW: distillation.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] "Distillation creates something new from something larger" and "Most KB learning is distillation" (section "The dominant mechanism in knowledge work") are asserted as fact, but these are the note's own framework claims, not established results. The note introduces a specific decomposition (distillation vs constraining as co-equal, orthogonal mechanisms) that is original to this KB, yet the language throughout treats it as settled — "one of two co-equal learning mechanisms," "constraining and distillation are orthogonal," "creation matters more than hardening." No hedging signals that this is a proposed model rather than a consensus position.
  Recommendation: Add a brief framing sentence early (e.g., "This note proposes distillation and constraining as..." or "In this KB's model...") to signal that the two-mechanism decomposition is the note's own construction. The internal sections can then assert confidently within that frame.

- [Proportion mismatch] The core claim is that distillation is "compressing knowledge for a specific task under a context budget." The section that carries the most weight for that claim — "How distillation works" — is well-developed (~270 words of prose plus a table). However, "The dominant mechanism in knowledge work" (~90 words) makes the bold claim that distillation is the primary learning mechanism AND that "creation matters more than hardening," yet gives only a single-cycle sketch as support. This is the note's strongest and most consequential claim and it gets the thinnest treatment.
  Recommendation: Develop "The dominant mechanism in knowledge work" with at least one concrete example of the explore-notice-extract-write cycle, or move the dominance claim into the opening paragraph as a framing assertion rather than a section that implies it will argue the point.

INFO:
- [Source residue] The "Prior work" section references Vygotsky's scaffolding, Bloom's taxonomy, Nonaka & Takeuchi's externalization, and professional abstracting/indexing. These are appropriate for establishing prior art, but "progressive disclosure is distillation applied to documentation" equates the two without qualification — progressive disclosure is an information architecture pattern about sequencing, not necessarily about compression under a budget. This is a minor conceptual stretch rather than domain leakage, but it could mislead readers familiar with progressive disclosure.

- [Redundant restatement] The opening paragraph defines distillation, then the second paragraph re-situates it relative to context engineering. The "Why distillation exists" section opens with "Different operational contexts need different things from the same body of knowledge" — which is a restatement of the opening paragraph's point that distillation targets "an artifact that equips a consumer (agent, collaborator) to perform a task." The section's own contribution (the agent statelessness argument) starts in its second paragraph. The restatement is mild — one sentence rather than a full paragraph — so this is informational rather than a warning.

CLEAN:
- [Source residue] The note's claimed generality level is agent-operated knowledge bases. The vocabulary throughout is consistent with that domain: "context budget," "agent," "artifact," "skill," "note," "workshop." No leaked vocabulary from a narrower origin domain (e.g., no software engineering debugging examples presented as general, no ML training vocabulary used outside the explicit terminology section). The prior-work survey is framed appropriately as prior art, not as the note's own domain.

- [Pseudo-formalism] The note contains two tables: a Source-to-Distillate mapping and a 2x2 constrained/distilled grid. Both do real work — the first concretizes the abstract definition with specific KB-relevant examples, the second makes the orthogonality claim precise by showing that all four quadrant combinations are populated. Neither could be removed without losing clarity. No variables, equations, or formal notation appear.

- [Orphan references] All specific references are adequately contextualized. "Hinton et al., 2015" is named and its meaning explained in the terminology section. Vygotsky, Bloom, and Nonaka & Takeuchi are named with enough context to identify the relevant concepts. The "Faithful Self-Evolvers" paper is cited with a link and its finding is summarized. No floating numbers, percentages, or unsourced empirical claims.

- [Unbridged cross-domain evidence] The prior-work section cites pedagogy, technical writing, library science, and knowledge management — but frames them as analogues ("is not new — it's the core of several established fields"), not as evidence that distillation works in the agent context. The concluding paragraph of that section explicitly states what's specific to the agent context. The ML distillation comparison in the terminology section explicitly bridges the domains and notes the divergence. No unbridged transfers found.

- [Anthropomorphic framing] The note avoids attributing mental states to models. Agents are described as "performing," "needing," "facing" tasks — operational language, not cognitive. "The model" does not appear as a subject with mental-state verbs. The closest case is "a collaborator who needs the current strategic picture," but "collaborator" here refers to a human or agent in a functional role, not to a model's internal state.

Overall: 2 warnings, 2 info
===
