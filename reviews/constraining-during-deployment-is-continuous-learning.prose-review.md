=== PROSE REVIEW: constraining-during-deployment-is-continuous-learning.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] "covers most of what deployed systems need" in the final paragraph is an unhedged empirical claim with no supporting evidence. The note is careful elsewhere to scope constraining as a subset ("this note is therefore a subset claim"), but this sentence reasserts dominance over the broader space without grounding.
  Recommendation: Hedge the claim — e.g., "covers a substantial share of what deployed systems need" or add a qualifier like "in our experience" — or cite evidence for the coverage proportion.

- [Orphan references] DSPy and ProTeGi are named as systems that "automate one slice of constraining" but neither is cited with a source, paper, or link. A reader encountering these names has no way to verify the characterization or follow up.
  Recommendation: Add citations or links for both systems, or at minimum parenthetical identifiers (e.g., "DSPy (Khattab et al., 2023)").

INFO:
- [Source residue] The examples in paragraph two — `format_date()`, system prompts with house style, validation scripts catching errors "that previously required human review" — all come from a software-engineering context. The note's title and framing claim generality about "continuous learning" in deployed AI systems, not specifically software-engineering deployments. The examples are not framed as illustrative ("in software engineering, for instance..."); they read as if this is the only context. This may be intentional given the KB's domain, but it limits the note's claimed generality about continuous learning as a concept.

- [Anthropomorphic framing] The phrase "the ML community recognizes this as learning" attributes a collective recognition state. This is a minor point — it's a claim about community consensus rather than about model internals — but the note provides no citation for this community recognition. If the claim matters to the argument, it needs a source; if it doesn't, it could be cut.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus appears in the note. The argument is conducted entirely in prose, which is appropriate for its content.

- [Proportion mismatch] The core claim — that constraining constitutes continuous learning — receives the bulk of the note's development. Paragraph one frames the claim, paragraph two provides the mechanism, paragraph three provides the definitional grounding (Simon), paragraph four gives the scoping caveat, paragraph five provides empirical examples, and paragraph six handles the boundary condition. The load-bearing content (mechanism + definition + scope) is proportionally dominant. No section is overdeveloped relative to its importance.

- [Unbridged cross-domain evidence] The Simon definition (paragraph three) is a general learning-theory definition being applied to AI systems, which is a valid move since Simon's definition is intentionally domain-neutral ("any system"). The developer study reference is about human developers, but it's cited as evidence of the same pattern "in manual form," which is a fair characterization since the note's claim is about the system-level learning (artifacts accumulating), not about the developers' cognition.

- [Redundant restatement] Each paragraph opens with new content. Paragraph four ("This note is therefore a subset claim") might appear to restate paragraph three, but it performs distinct work: it scopes the claim to prevent over-reading. No paragraph could be deleted without losing its contribution.

Overall: 2 warnings, 2 info
===
