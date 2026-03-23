=== PROSE REVIEW: instruction-specificity-should-match-loading-frequency.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The four-level loading hierarchy is presented as definitive ("The loading hierarchy") but it is a design pattern specific to this project's architecture, not an established general framework. The numbered list with bold labels and the definite article reads as a canonical taxonomy rather than one observed decomposition. Compare: "The loading hierarchy" (asserts) vs. "A loading hierarchy this system uses" (proposes).
  Recommendation: Either frame the hierarchy as the observed pattern in this project ("In this system, loading falls into roughly four levels...") or explicitly note it generalizes from Claude Code's architecture. The title claim about specificity matching frequency is well-supported; it is the specific four-tier taxonomy that overshoots its epistemic warrant.

INFO:
- [Source residue] The note is about instruction specificity matching loading frequency as a general design principle, but every concrete example is Claude Code-specific (CLAUDE.md, `/slash` commands, WRITING.md, tasks/README.md). This is mild — the note's tags and context make clear it lives in the Claude Code architecture space — but a reader encountering it via the general title might expect broader applicability before seeing that the body is entirely about one tool's conventions. The principle itself is general; the body treats it as tool-specific without noting the gap.

CLEAN:
- [Source residue] No leaked vocabulary from an unrelated domain. The Anthropic source and the Lopopolo source both address exactly the domain the note discusses (agent context engineering). Terms like "CLAUDE.md," "skill bodies," and "progressive disclosure" all belong to the note's stated scope.
- [Pseudo-formalism] No formal notation or mathematical apparatus present. The numbered list is organizational, not pseudo-formal.
- [Proportion mismatch] The core claim (specificity should match frequency) is stated in the opening paragraph and restated after the hierarchy. The hierarchy section is the load-bearing content and receives the bulk of the word count. The closing paragraph reinforces the prescriptive takeaway. Proportions are well-matched to the claim structure.
- [Orphan references] No unattributed empirical claims, specific numbers, or named studies appear without citation. The two sources are properly linked and contextualized.
- [Unbridged cross-domain evidence] The Anthropic source describes the same system the note discusses (Claude Code). The Lopopolo source (Codex/AGENTS.md) is framed as independent convergence on the same pattern, which is a valid bridging move — it says "converges independently," not "proves."
- [Redundant restatement] The principle is stated in the opening paragraph and restated on line 20 ("The principle: match instruction specificity to loading frequency"). This is deliberate emphasis after the concrete hierarchy, not redundant restatement — the second occurrence adds the concise formulation after the reader has seen the examples. No section opens by re-explaining a prior section's conclusion.
- [Anthropomorphic framing] The note refers to "the agent" doing work and "competes for attention," but these are standard usage in context engineering discussion — "attention" here means token-budget competition, not mental attention. No verbs implying beliefs, understanding, or knowledge possession appear.

Overall: 1 warning, 1 info
===
