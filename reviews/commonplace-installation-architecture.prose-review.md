=== PROSE REVIEW: commonplace-installation-architecture.md ===

Checks applied: 8

WARN:
- [Anthropomorphic framing] The note consistently uses "she" pronouns and human-like agency for the agent: "the agent decides she needs more context and goes looking for it," "she searches commonplace/kb/notes/ for deeper reasoning," "the agent isn't sure which semantic fits," "she needs the full reasoning." This framing attributes deliberative judgment and self-directed curiosity to the agent. While the note is about agent workflows (not model internals), the language goes beyond operational description into implying subjective states ("isn't sure"). More precise alternatives: "the agent's loaded instructions are insufficient" rather than "isn't sure"; "the agent reads from" rather than "she searches... for deeper reasoning."
  Recommendation: Replace subjective-state language ("isn't sure," "decides she needs") with operational language ("the loaded context is insufficient," "the workflow escalates to"). The pronoun choice itself is a style decision, but the verbs paired with it carry unintended cognitive claims.

- [Redundant restatement] The "Why copy operational artifacts instead of reading cross-tree" section (line 77-83) restates the argument already made in the "Write path" section. The Write path section already explains that keeping types in commonplace/ would make instructions more complex ("the agent needs to know which tree to read from, and the control-plane routing gets more complex"). The "Why copy" section then re-argues the same point: "requires the agent to understand a cross-tree resolution order... adds friction in prompts." The second pass adds the upgrade story (type file replacement, WRITING.md diff), which is new, but the first two paragraphs are restatement.
  Recommendation: Trim the "Why copy" section to its unique contribution: the upgrade mechanism. The cross-tree friction argument is already established in the Write path analysis and does not need re-arguing.

- [Proportion mismatch] The note's title claims to be about "installation architecture," but the install step itself -- what the script actually does, in what order, with what checks -- gets almost no coverage. The "What gets copied vs what stays" table (lines 65-75) lists artifacts and destinations, but the actual installation procedure is absent. Meanwhile, the read/write optimization rationale (lines 20-59) gets roughly 40 lines of detailed analysis. The design motivation dominates; the architecture (what the system looks like and how it gets built) is secondary.
  Recommendation: This is a design-rationale note wearing an architecture title. Either rename to something like "Commonplace two-tree layout optimizes agent read and write paths" to match the actual weight, or develop the installation procedure (script behavior, idempotency, upgrade path) to match the architecture framing.

INFO:
- [Source residue] Line 131-132 references "llm-do" and "claw-design/" as comparison points: "In llm-do, claw-design/ exists as a separate directory from notes/ because llm-do has notes about many topics." This is a prior-project reference that a reader unfamiliar with llm-do cannot evaluate. It serves as motivating context for why commonplace doesn't need a separate methodology directory, but the argument stands without it. Not a strong residue case since the note is explicitly about commonplace's own architecture, but the llm-do comparison is opaque to outside readers.

- [Confidence miscalibration] The note presents the two-tree design and copy-vs-reference boundary as settled decisions, using direct assertion throughout ("The layout optimizes both," "Both produce a stable commonplace/ directory," "Copying eliminates this"). Given the note's status is "seedling," this confident framing may be premature -- the architecture may still evolve. However, the note documents a design that already exists in this repo, so assertive framing is defensible. Flagging for awareness rather than as a problem.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus. The note uses tables for structured comparison, which serve a genuine organizational purpose (hop counts, artifact routing). Clean.

- [Orphan references] No specific numbers, percentages, named studies, or empirical claims appear without context. The hop counts (0, 1, 3) are derived from the tables in the note itself, not cited from external sources. Clean.

- [Unbridged cross-domain evidence] The note does not cite evidence from other domains. All reasoning is internal to the commonplace system's own design. No cross-domain transfer claims are made. Clean.

Overall: 3 warnings, 2 info
===
