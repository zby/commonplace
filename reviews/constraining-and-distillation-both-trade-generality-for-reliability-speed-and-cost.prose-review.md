=== PROSE REVIEW: constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The description says the two mechanisms "differ in the operation and how much compound they yield," asserting that constraining yields more compound than distillation as a general fact. The body's comparison table makes the same assertion: "Compound yield: Highest at codification (substrate change)" vs "Moderate — speed and cost gains from reduced context." But this comparison holds only when constraining reaches codification. Constraining short of codification (e.g., a naming convention) may yield less compound gain than a well-targeted distillation (e.g., a methodology distilled into a single-load skill that eliminates multiple context-loading rounds). The note presents the codification ceiling as the typical case and the distillation ceiling as the typical case, then compares them — which biases toward constraining.
  Recommendation: Qualify the comparison. Either note that the compound-yield comparison holds specifically at the codification end, or reframe the table column as "Maximum compound yield" vs "Typical compound yield" to make the comparison honest.

- [Proportion mismatch] The note's title claims parity between the two mechanisms — "both trade generality for reliability, speed, and cost." But the constraining section gets two substantial paragraphs with a concrete example (LLM validation check → Python script) and a discussion of the full spectrum, while the distillation section gets two shorter paragraphs with a more abstract example (fifteen methodology notes → skill). The constraining section does more argumentative work; the distillation section mostly restates what the distillation definition note already says. Given the title promises equal treatment, the distillation half is underdeveloped.
  Recommendation: Develop the distillation section with a concrete, worked example comparable in specificity to the codification example. The "fifteen methodology notes" example could be made concrete: which methodology, which skill, what specific reliability/speed/cost gains.

INFO:
- [Redundant restatement] The opening sentence of "How distillation trades generality for compound" — "Distillation extracts from a larger body of reasoning into a focused artifact shaped by a specific use case, context budget, or agent" — restates the definition from the distillation note and the opening paragraph's link text. In a short note this is minor, but since the constraining section jumps straight into its argument without re-defining constraining, the asymmetry is noticeable.

CLEAN:
- [Source residue] The note claims to be about a general trade-off between generality and compound for two learning mechanisms. The examples used (LLM vs calculator, LLM validation check vs Python script, methodology notes vs skill) are drawn from the KB/agent domain, which is the note's native domain. No domain-specific residue from an unrelated source was detected.

- [Pseudo-formalism] The comparison table in "The mechanisms differ in operation" is tabular prose, not formal notation. It organizes a verbal comparison. No equations, variables, or formal apparatus present.

- [Orphan references] No specific numbers, percentages, named studies, or empirical claims appear without context. The examples are hypothetical illustrations, not empirical claims requiring sourcing.

- [Unbridged cross-domain evidence] The LLM-vs-calculator example is used as an illustrative scenario within the note's own domain, not as cross-domain evidence. No external studies or findings from other domains are cited.

- [Anthropomorphic framing] The note uses "hallucinates" once ("never hallucinates 7×8=54"), which is standard LLM vocabulary rather than a claim about mental states. No other anthropomorphic language detected.

Overall: 2 warnings, 1 info
===
