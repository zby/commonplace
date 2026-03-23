=== PROSE REVIEW: ad-hoc-prompts-extend-the-system-without-schema-changes.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note's own two-strata model is asserted as fact: "Any system with an LLM agent layer has two strata: a deterministic base ... and a prompt layer on top." This is the note's proposed decomposition, not an established framework, but the phrasing ("has two strata") presents it as given. Similarly, "The maturation trajectory is: write ad hoc prompts first, notice when you're writing the same kind repeatedly, extract a skill" asserts a single trajectory as the trajectory rather than a common or proposed one.
  Recommendation: Soften the framing to match epistemic status. E.g., "a useful decomposition is two strata..." or "A common maturation trajectory: ..." — signaling that these are the note's proposed models, not established findings.

- [Unbridged cross-domain evidence] The homoiconicity section claims: "This is the same property that makes Lisp, Emacs, and Smalltalk extensible from within — and carries the same discoverability costs." Homoiconicity in Lisp (code as data, same list structure) and homoiconicity in LLM context (instructions and content as natural language tokens) operate through different mechanisms. The note names the shared concept but doesn't explain why the analogy holds or where it breaks. Asserting "the same property" is stronger than the bridging supports.
  Recommendation: Add a sentence explaining the shared mechanism (both allow new behaviors to be defined in the same medium the system already processes) and note where the analogy diverges (Lisp homoiconicity enables programmatic code generation; LLM homoiconicity enables natural language behavioral extension — these are structurally similar but mechanistically different).

INFO:
- [Confidence miscalibration] "The prompt carries the caller's judgment, not just the caller's data" — "judgment" is a loaded term that the note treats as self-evident. The note is deliberately making this claim (distinguishing what prompts carry from what type signatures carry), so the confidence level may be intentional. But the claim that natural language prompts carry "judgment" while type signatures carry only "data" is a substantive assertion that some readers will want defended rather than asserted.

CLEAN:
- [Source residue] The note claims broad generality ("any system with an LLM agent layer") and the KB-specific material is explicitly framed as an example ("We first noticed this in the KB, where it shows up cleanly" / "The KB example: collections"). The CI pipeline, codebase, and deployment examples in the third paragraph are presented as illustrative instances, not leaked framing. No unframed domain-specific residue detected.

- [Pseudo-formalism] No formal notation, equations, or mathematical apparatus present. The note argues entirely in prose. Nothing to flag.

- [Proportion mismatch] The core claim (ad hoc prompts extend the system) is developed across four complementary sections: a concrete example (KB collections), positioning on the constraining spectrum, the expressiveness argument (prompts carry what types can't), and the mechanistic explanation (homoiconicity). The most load-bearing insight — that this is about expressiveness, not convenience — gets proportional treatment in "Prompts carry what types can't." The KB example is longer but serves as the grounding case. Proportions match the argumentative structure.

- [Orphan references] No specific numbers, percentages, or named studies appear. "Lisp, Emacs, and Smalltalk" are invoked as commonly known exemplars of homoiconic systems, not as empirical claims requiring citation. No orphaned references detected.

- [Redundant restatement] Each section opens with new material. "The constraining spectrum" opens with positioning (new). "Prompts carry what types can't" opens with the expressiveness claim (new). "Why this works: homoiconicity" opens with the mechanistic explanation (new). No section restates a prior section's conclusion as setup.

- [Anthropomorphic framing] Agent-related language ("tells the agent," "the sub-agent executes," "the caller does the judgment-heavy work") uses standard terminology for agent systems. "Inherits" in "the sub-agent inherits nothing beyond what the caller explicitly passed" is metaphorical but precise in context (context inheritance). No language attributes human-like mental states to models.

Overall: 2 warnings, 1 info
===
