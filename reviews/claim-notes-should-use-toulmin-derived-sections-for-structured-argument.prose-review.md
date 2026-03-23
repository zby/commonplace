=== PROSE REVIEW: claim-notes-should-use-toulmin-derived-sections-for-structured-argument.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts "The convergence isn't coincidence" as established fact, but the convergence is the note's own interpretive construction — the three threads could have converged on similar shapes for different reasons, or the mapping to Toulmin could be a post-hoc pattern match. The opening paragraph's "KB conventions independently converged on Toulmin's argumentation model without naming it" also presents interpretation as discovery. The Reasoning section is appropriately direct for an argued claim, but the framing of convergence-as-proof (rather than convergence-as-suggestive) overstates the epistemic basis.
  Recommendation: Hedge the convergence framing: "The convergence suggests..." or "a plausible explanation is that Toulmin describes the structure of practical argument." The claim itself (that Toulmin sections are a good fit) can remain direct — it's the meta-claim about convergence being non-coincidental that needs softening.

- [Proportion mismatch] The core claim is that Toulmin-derived sections should be adopted as a base type. The section that carries the most weight for this claim is Evidence (showing the convergence) and the first part of Reasoning (explaining why the convergence matters). Evidence gets roughly 120 words across four numbered points. Meanwhile, Reasoning's sub-sections — "Why a base type, not a trait," "Why structured-claim, not claim," "The promotion path," and "Evidence vs Reasoning (from Toulmin)" — collectively run to roughly 400 words, and the section template plus the mapping table and check lists add another 250 words. The operational/naming/migration detail substantially outweighs the argument for the core claim.
  Recommendation: The naming rationale, promotion path, and template specification are valuable but are doing implementation design, not argument. Consider whether the template and operational sections belong in a separate implementation note (or in the type template file itself), keeping this note focused on the argument that Toulmin sections are the right model.

INFO:
- [Orphan references] "30 of 62 notes (48%) currently carry `has-claim`" and "perhaps 5-10 are developed enough for `type: structured-claim` today" — these are specific numbers with no date, script reference, or method description. If the note count changes (notes are added or removed), these numbers become stale with no way to verify or regenerate them. The 5-10 estimate is explicitly hedged ("perhaps"), which is appropriate, but the 30/62 figure reads as precise fact.
  Recommendation: Add a parenthetical noting when/how the count was obtained (e.g., "as of [date], per `rg has-claim`"), or replace with a qualitative statement ("nearly half of current notes carry `has-claim`").

CLEAN:
- [Source residue] The note's claimed generality level is the KB's own type system, and all examples are drawn from the KB's own conventions (title-as-claim, Thalo comparison, affordance tables, trait system). No domain-specific vocabulary leaks from an external source domain. The Toulmin terminology is the subject matter, not residue.
- [Pseudo-formalism] No formal notation is used. The Toulmin mapping table and section template are presentational, not pseudo-formal — they organize a concrete proposal rather than dressing prose in symbols.
- [Unbridged cross-domain evidence] The note's evidence is internal (KB conventions, Thalo comparison, affordance table) rather than cross-domain empirical findings. The Toulmin model is cited as a design framework to adopt, not as empirical evidence that transfers across domains. No bridge is needed.
- [Redundant restatement] Each section opens with its own contribution. The Reasoning section's first sentence ("The convergence isn't coincidence...") advances the argument rather than restating the Evidence section. The sub-sections within Reasoning each address distinct questions without re-explaining prior sub-sections.
- [Anthropomorphic framing] The note discusses KB structure, document types, and authoring conventions. The one reference to LLM behavior ("an LLM reading 'titles should be claims' would infer every note needs `type: claim`") uses "infer" appropriately to describe a predictable parsing behavior, not to attribute understanding.

Overall: 2 warnings, 1 info
===
