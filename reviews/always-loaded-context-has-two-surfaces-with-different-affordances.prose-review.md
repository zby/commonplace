=== PROSE REVIEW: always-loaded-context-has-two-surfaces-with-different-affordances.md ===

Checks applied: 8

WARN:
(none)

INFO:
- [Anthropomorphic framing] "The agent sees a menu of available commands and decides whether to invoke one" and "the agent recognizes when a skill is relevant" attribute perceptual and cognitive states to the agent. More precise alternatives: "the agent receives a list of available commands" and "the agent matches a skill to the current task." The note is about agent behavior by design, so agent-as-subject is natural, but "sees" and "recognizes" carry slightly more cognitive implication than the note needs.
  Recommendation: Substitute "receives" for "sees" and "identifies when" or "detects when" for "recognizes when." Minor — the note's domain makes these less misleading than they would be in a note about model internals.

- [Confidence miscalibration] The push/pull and imperative/suggestive taxonomy is the note's own construction, presented with direct assertion: "CLAUDE.md is imperative," "Skill descriptions are suggestive." Since this is a design note about a system the author controls, asserting how the system works is reasonable. The only slight tension is that "imperative" and "suggestive" are being proposed as a general framing for always-loaded context surfaces — if the note intends this as a transferable framework (not just a description of this system), a brief flag like "a useful way to characterize the difference" would calibrate it.
  Recommendation: No change needed if the note is purely descriptive of this system. If it's meant to generalize, add one hedging phrase.

CLEAN:
- [Source residue] The note discusses CLAUDE.md, skill descriptions, git conventions, and the `/connect` command — all specific to this knowledge system. Since the note's subject IS this system's design, the specificity is appropriate, not residue from a narrower domain.
- [Pseudo-formalism] No formal notation, variables, or equations. The note argues entirely in prose.
- [Proportion mismatch] The core claim (two surfaces, different affordances) receives balanced treatment: roughly equal space for CLAUDE.md and skill descriptions, followed by an overlap discussion and a crystallizing design question. Proportions match the claim's structure.
- [Orphan references] No specific figures, data points, named studies, or empirical claims appear in the note.
- [Unbridged cross-domain evidence] No cross-domain citations. All evidence is drawn from the system the note describes.
- [Redundant restatement] The final "Key design question" paragraph restates the push/pull distinction, but it does so to compress it into a decision heuristic — a different rhetorical function from the earlier exposition. This is summary, not redundancy.

Overall: 0 warnings, 2 info
===
