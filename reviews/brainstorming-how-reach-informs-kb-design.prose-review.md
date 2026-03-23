=== PROSE REVIEW: brainstorming-how-reach-informs-kb-design.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts cost asymmetries as established fact: "The cost of changing a note is inversely related to its reach in a non-obvious way" and "Low-reach changes... Agents handle this cheaply" vs "High-reach changes... the downstream reasoning across many notes may silently break." These are plausible claims but they are the note's own construction, not cited from Deutsch or any empirical source. The framing uses direct assertion ("is," "may silently break") rather than proposal language. Given the note's own "seedling" status and "Brainstorming" title, the assertive tone in this section overshoots its epistemic standing.
  Recommendation: Reframe the cost-asymmetry model as proposed: "A plausible asymmetry is that..." or "We suspect that..." — matching the exploratory register the title promises.

- [Proportion mismatch] The core claim — that reach is a maintenance risk signal, not a retrieval signal — is the note's distinctive contribution (per the description). The "Reach does not obviously help retrieval" section gets 3 sentences. The "Reach is valuable and dangerous" section, which carries the maintenance-risk argument, is better developed but still only about half the note. Meanwhile "Notes sit on a reach spectrum" — which is context-setting, not the core claim — receives comparable space. The maintenance-risk idea deserves fuller development: what does "silently break" look like concretely? How would a reviewer detect it?
  Recommendation: Expand the maintenance-risk section with at least one concrete scenario showing what a high-reach revision breaking downstream reasoning looks like in practice. The spectrum section could be trimmed or the concrete examples there could be moved into a parenthetical.

INFO:
- [Source residue] The note references "files-not-database," "ADR 004," "ADR 002," "Graphiti," the `/connect` skill, and "Phase 5 abstraction logging" — all specific to this KB installation. The title and opening paragraph claim the note is about Deutsch's "reach" applied to KB design in general, but the body is heavily grounded in this particular KB's vocabulary. This is borderline: the note's description says "applied to KB notes" so some specificity is expected, and the examples are used illustratively. However, a reader unfamiliar with this KB would find "Phase 5 abstraction logging" and "the Graphiti section" opaque.
- [Anthropomorphic framing] Minor: "Three notes making the same argument in different contexts" attributes agency ("making... argument") to notes. This is a common and largely harmless metonymy in KB-about-KB writing, but it technically attributes authorial intent to artifacts.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus. The "high/medium/low" spectrum is presented as a verbal taxonomy, not a formal decomposition. Clean.
- [Orphan references] Deutsch's *The Beginning of Infinity* is named as the source for "reach." The other references (files-not-database, ADRs, Graphiti, `/connect`, Phase 5) are internal to this KB and linked or identifiable. No unsupported empirical claims, specific numbers, or unnamed studies.
- [Unbridged cross-domain evidence] The note draws from Deutsch (epistemology) and applies to KB design. The bridge is explicit in the opening: "Notes in a KB vary in reach, and this variation matters." The transfer mechanism — that explanatory reach as an epistemic property applies to knowledge artifacts generally — is reasonable and the note does not overclaim empirical grounding from Deutsch's philosophical argument.
- [Redundant restatement] Each section opens with new content. "Reach is valuable and dangerous" does not restate "Notes sit on a reach spectrum" — it introduces the cost-asymmetry argument. "Existing machinery already covers the consolidation case" does not restate the heuristics — it maps them onto existing tooling. No restating paragraphs detected.

Overall: 2 warnings, 2 info
===
