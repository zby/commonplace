=== PROSE REVIEW: scenario-decomposition-drives-architecture.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim is that scenario decomposition drives architecture — i.e., decomposing user stories reveals architectural requirements. The section that carries the most weight for this claim is "Architectural principles that fall out" (lines 79-95), which draws architectural conclusions from the decomposition. However, this section is roughly comparable in length to "Two operating contexts" (lines 15-21) and shorter than the combined "Write a note — decomposed" + "Other scenarios" material (lines 37-78). More importantly, the "Where the system is strong" section (lines 97-101) largely restates conclusions already drawn in "Architectural principles that fall out" (e.g., search-and-retrieval strength, common-path efficiency). The same observation about the connection gap appears in both "Architectural principles" (line 95: "The 'connect to existing knowledge' step is the least optimized") and "Where gaps remain" (lines 107-108: "The post-write connection gap"). The redundancy between these three sections dilutes the architecture-driving conclusion that the title promises. Consider whether "Where the system is strong" and "Where gaps remain" could be folded into the architectural principles section, or whether the architectural principles section needs to be developed further to stand as the clear payoff.
  Recommendation: Consolidate the strengths/gaps into the architectural principles section, or restructure so the final sections add genuinely new analysis rather than restating earlier conclusions.

- [Redundant restatement] The "Where the system is strong" section (lines 97-101) restates conclusions already established in the body. "Search and retrieval" repeats what line 87 already demonstrated ("This is where the system is strongest..."). "Common-path efficiency" repeats the conclusion from lines 89-90 and the common-path table. These paragraphs could be deleted and the note would lose no information.
  Recommendation: Cut the "Where the system is strong" section. If a summary is wanted, a single sentence in the architectural principles section suffices.

- [Confidence miscalibration] The "Measurable artifacts" section (lines 113-117) asserts: "The decomposition tables above are now implemented as structured scenario files in `test/scenarios/`" and "The `/evaluate-scenarios` skill reads these files, measures instruction bytes from the referenced sources, and produces a cost table." These are stated as accomplished facts. If `test/scenarios/` and `/evaluate-scenarios` exist and work, this is fine. But if they are planned or partially implemented, the present-tense framing ("are now implemented," "reads these files," "produces a cost table") overstates the status. The note's own status is `seedling`, which creates tension with claims about implemented measurement infrastructure.
  Recommendation: Verify that the referenced artifacts exist and function. If they do, no change needed. If they are planned or incomplete, use language that reflects the actual status ("will be implemented," "is designed to").

INFO:
- [Proportion mismatch] The "Two operating contexts" section (lines 15-21) provides important framing but front-loads detail about the installed-project escalation path before the decomposition that makes that path meaningful. The reader learns about distillation, CLAUDE.md fragments, and escalation before seeing the step-by-step analysis that motivates these concepts. This is a structural choice — the section sets up vocabulary for what follows — but it means the reader must accept several claims on faith before reaching the evidence. Worth considering whether a lighter setup followed by the decomposition and then the full two-context comparison would improve the flow.

- [Confidence miscalibration] Line 100 states: "Most writes stay in `kb/` with 3 hops." The specific number "3 hops" is presented as a finding from the decomposition, but the decomposition table (lines 41-49) shows 7 steps in the common path. The relationship between "steps" and "hops" is not defined — are some steps zero-hop because context is already loaded? The "3 hops" claim needs either a definition of what counts as a hop or a derivation from the table.

CLEAN:
- [Source residue] The note operates entirely within its own domain: agent-operated knowledge bases, installation architecture, context loading. The vocabulary (hops, escalation paths, CLAUDE.md fragments, distillation, skills) is native to the commonplace project. No external domain residue detected — the note was not generalized from a narrower source, so there is nothing to leak through.

- [Pseudo-formalism] The note uses structured tables (lines 41-49, 59-65) rather than mathematical notation. These tables serve a clear organizational purpose — mapping steps to context requirements and locations. Deleting them would make the decomposition harder to follow. No decorative formalism detected.

- [Orphan references] No unsourced specific numbers, percentages, or named studies. The one specific number ("3 hops" on line 100) is derived from the note's own analysis rather than cited from an external source (though the derivation could be more explicit — see INFO above).

- [Unbridged cross-domain evidence] The note does not cite evidence from other domains. All claims are grounded in the note's own decomposition analysis and linked notes within the same knowledge base. No cross-domain transfer issues.

- [Anthropomorphic framing] The note discusses agent behavior using appropriate technical language: "the agent must," "the agent searches," "the agent needs." These describe operational requirements rather than attributing mental states. The one potentially anthropomorphic phrase — "the agent doesn't know or care" (line 51) — is colloquial but accurate: the agent literally does not distinguish between original and copied files because the paths are identical. No problematic anthropomorphism detected.

Overall: 3 warnings, 2 info
===
