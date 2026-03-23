=== PROSE REVIEW: agent-is-a-tool-loop.md ===

Checks applied: 8

WARN:
(none)

INFO:
- [Proportion mismatch] The title gives equal billing to two claims — "useful technical convention" and "not a definition" — but the definitional-debate side is dispatched in a single clause ("carries too much philosophical weight to define cleanly") while the convention side gets the remaining ~90% of the note. The imbalance is defensible (the note is about the convention, not the debate), but the title frames them as co-equal. Consider whether the title should foreground the convention alone, e.g., "An agent is a tool loop — prompt, capability surface, stop condition," and let the not-a-definition point be a subordinate remark.
- [Confidence miscalibration] "a simple equivalence works" is a direct assertion of utility for a note marked `status: seedling`. The convention is the note's own construction, not cited from a source. The rest of the note appropriately frames it as a convention rather than a discovery, but "works" in the opening paragraph makes a success claim the note doesn't yet cash out with evidence beyond one framework-design consequence. Worth checking whether "is useful" or "serves well enough" better matches the seedling status.

CLEAN:
- [Source residue] The note claims to be about a technical convention for organizing agent code. All terms — prompt, capability surface, stop condition, sub-loop, framework — belong to the agent-framework domain the note addresses. No domain leakage detected.
- [Pseudo-formalism] No formal notation, equations, or variables. The note makes its argument entirely in prose.
- [Orphan references] No specific figures, data points, named studies, or empirical claims appear. All assertions are definitional within the proposed convention.
- [Unbridged cross-domain evidence] No cross-domain citations. The note stays within its own domain (agent framework design) throughout.
- [Redundant restatement] Three paragraphs, each advancing: (1) establishes the convention, (2) specifies what it excludes and how identity works, (3) connects to framework design. No paragraph restates a prior paragraph's conclusion as setup.
- [Anthropomorphic framing] "The model finishes" refers to a runtime event (generation completion), not a mental state. "The same model" is used for identity comparison. No anthropomorphic attributions.

Overall: 0 warnings, 2 info
===
