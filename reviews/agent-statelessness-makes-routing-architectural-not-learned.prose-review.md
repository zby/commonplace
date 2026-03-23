=== PROSE REVIEW: agent-statelessness-makes-routing-architectural-not-learned.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The degradation cliff is presented as a binary fact — "The agent system has a cliff: KB-augmented → generic" — but this is the note's own model, not an established result. The claim that agents have no intermediate degradation (no "something feels off" signal, no continuum) is plausible but asserted with the same confidence as the relatively uncontroversial statelessness claim. The human side is also simplified: "expert → competent → novice → uncertain" is the note's own taxonomy, presented with the grammar of established fact. Both the cliff model and the human continuum model are proposed frameworks that would benefit from hedged framing.
  Recommendation: Flag the cliff/continuum contrast as a proposed model: "A useful way to think about this..." or "This suggests a cliff rather than a continuum." The specific four-stage human degradation sequence ("expert → competent → novice → uncertain") should be marked as illustrative rather than taxonomic.

- [Proportion mismatch] The core claim is in the title: routing is architectural, not learned. The section that carries the most weight for this claim is the opening (untitled) section plus "Progressive disclosure replaces navigation intuition" — together roughly 250 words. "The degradation cliff" and "Source vs. compiled" each get comparable or greater development (~200 and ~200 words respectively), but they are consequences of the core claim rather than the claim itself. The "Source vs. compiled" section in particular develops a source-code/compiled-artifact metaphor at length that, while valuable, is arguably a separate note's worth of content (the compilation pattern, quality criteria for source vs. compiled, the relationship to instruction specificity). The core insight — that the agent never develops navigation intuition — is established quickly and then the note moves on to downstream implications that receive more development than the motivating argument.
  Recommendation: Consider whether "Source vs. compiled" warrants its own note (it introduces a distinct framework: methodology-as-source, routing-as-compiled, with its own quality criteria). If kept here, develop the core statelessness argument further — perhaps with concrete examples of what "day one every session" looks like in practice — so it matches the weight of its consequences.

INFO:
- [Anthropomorphic framing] The note uses "the agent cannot compensate," "the agent can't bridge the gap," "the agent recognizes when it's outside scope," and "the agent cannot learn." These are deliberate and the note is explicitly about the contrast between human and agent cognition, so the anthropomorphic phrasing is functional — it sets up the comparison the note depends on. However, "recognizes when it's outside scope" (in Design Consequences, point 3) attributes a capacity the note elsewhere argues the agent lacks. The sentence means "the routing artifact must tell the agent it's outside scope," but the phrasing makes it sound like the agent does the recognizing.
  Recommendation: Consider rephrasing point 3 from "the agent recognizes when it's outside scope" to "the agent can detect when it's outside scope" or restructuring so the routing artifact is the subject: "so the routing artifact signals when the agent is outside scope."

CLEAN:
- [Source residue] The note claims generality at the level of "agent + knowledge base" systems. All examples (routing tables, skill descriptions, type templates, naming conventions, CLAUDE.md) are drawn from this KB's own architecture, which is the note's stated domain. No leaked vocabulary from a narrower source domain detected.

- [Pseudo-formalism] No formal notation, equations, or variable-based decompositions. The numbered lists and layered hierarchy (CLAUDE.md → skill descriptions → skill bodies → type templates → methodology notes) are structural, not pseudo-formal. They describe concrete loading stages, not mathematical relationships.

- [Orphan references] No specific numbers, percentages, named studies, or uncited empirical claims. All references are to other notes in the KB, linked explicitly.

- [Unbridged cross-domain evidence] The note draws on human cognition (navigation intuition, mental models, degradation continuum) as a contrast with LLM agents, not as transferred evidence. The human behavior is used to set up the difference, not to argue that agents share the same properties. The bridge is the contrast itself. No unbridged transfer detected.

- [Redundant restatement] The opening paragraphs of "Progressive disclosure replaces navigation intuition," "The degradation cliff," and "Source vs. compiled" each introduce new content rather than restating prior sections. "Design consequences" opens with "Three requirements follow:" which is a clean transition. No redundant restatement detected.

Overall: 2 warnings, 1 info
===
