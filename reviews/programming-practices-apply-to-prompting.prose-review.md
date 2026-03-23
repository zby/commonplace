=== PROSE REVIEW: programming-practices-apply-to-prompting.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim is that programming practices apply to prompting — the title. The section "Practices we apply" carries the most weight for this claim. However, the testing discussion is developed twice: once in "Practices we apply" (a full paragraph) and again at greater length in "The hard cases" (three paragraphs devoted to breaking down the doubled testing surface). Testing gets roughly 40% of the note's body. Other practices (version control, design for testability) get one short paragraph each. If the note is about the breadth of practices that transfer, the proportion is skewed toward testing. If the doubled testing surface is the note's central insight, the title undersells it.
  Recommendation: Either develop the thinner practices (version control, design for testability) to comparable depth, or extract the extended testing analysis into a dedicated note (e.g., a companion to "automated-tests-for-text.md") and keep this note as a survey. The current proportions make the note read as "testing is hard for LLMs, and also some other practices transfer."

- [Redundant restatement] The "Hard cases" section re-explains the indeterminism/underspecification distinction that was already established in the opening paragraph and developed through each practice in "Practices we apply." The sentence "Testing is the clearest example, and it doubles the testing surface — but the two halves come from different phenomena" could serve as a one-sentence transition, but instead the section restates the full decomposition ("Indeterminism doubles the test runs" / "Underspecification doubles the test targets") with material that largely echoes the testing paragraph in "Practices we apply." The final paragraph ("The two phenomena compound...") adds a new point (conflating them leads to misdiagnosis), but it's buried after the restatement.
  Recommendation: Cut the re-explanation of indeterminism and underspecification in "The hard cases." Start with the genuinely new material: the compounding effect and the misdiagnosis risk. The earlier testing paragraph already established the decomposition; the hard-cases section should advance beyond it, not replay it.

INFO:
- [Source residue] The note is cleanly generalized. No domain-specific vocabulary leaks through from a narrower origin context. Terms like "typing," "testing," "compilation," and "version control" are the note's declared subject matter, not residue. The legal-drafting reference is explicitly framed as a comparison domain. No action needed, but one phrase — "the same move as compiling: freezing a flexible representation into a rigid, efficient one" — could mislead readers who take "compiling" literally (traditional compilation preserves semantics; constraining is acknowledged to be projection, which changes semantics). This is not residue per se, but the metaphor imports connotations that the surrounding prose then corrects.

- [Confidence miscalibration] The frontmatter marks the note as `status: speculative`, which is appropriate. However, several internal assertions use confident framing that sits in mild tension with that status. "Execution indeterminism is genuinely novel; underspecification is not" is stated as fact rather than as a claim the note advances. "The practices transfer, but what's a pedagogical convenience for humans is architectural necessity for agents" asserts a strong dichotomy. These read as established conclusions rather than speculative proposals. The tension is small — the note is arguing a position, and some assertive framing is expected — but readers who notice the `speculative` tag may find the interior tone surprising.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus appears in the note. The arguments are made entirely in prose. Nothing to flag.

- [Orphan references] No specific numbers, percentages, or named studies appear without context. The references to McConnell-style claims are absent; all cited sources are linked notes within the KB. The Thalo reference includes enough context ("a system that built a full compiler...27 validation rules") to be evaluable.

- [Unbridged cross-domain evidence] The note's entire structure is explicitly about cross-domain transfer, and it consistently provides bridging. The legal-drafting comparison is framed as an analogy ("legal drafting has centuries of methodology for managing the same underspecification"). The Thalo reference is framed as an endpoint case. The compilation metaphor is bridged by the explicit caveat that "unlike compilation, constraining is projection from an underspecified spec." No unbridged transfers found.

- [Anthropomorphic framing] The note avoids attributing mental states to models. It uses "systems interpret," "agents are permanently stateless," and "the model" language without implying understanding or belief. The phrase "agentic systems interpret underspecified instructions" is the title of a linked note and is used as a technical term for the projection operation, not as an attribution of comprehension.

Overall: 2 warnings, 2 info
===
