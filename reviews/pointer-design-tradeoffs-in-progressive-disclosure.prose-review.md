=== PROSE REVIEW: pointer-design-tradeoffs-in-progressive-disclosure.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note asserts its three-axis framework (context-specificity, cost, reliability) and its taxonomy of pointer types (fixed, query-time, crafted) as established fact: "They vary on three axes," "No single type wins all three. A system needs a mix." This is the note's own analytical construction, not a cited framework, yet it is presented with the confidence of settled knowledge rather than proposed analysis. The summary table and "Design implications" table reinforce this by presenting the categories as exhaustive without hedging.
  Recommendation: Add a brief framing sentence near the introduction acknowledging this is a proposed decomposition, e.g., "A useful way to compare them is along three axes" rather than the unqualified "They vary on three axes." The tables could note they capture the primary types rather than implying exhaustiveness.

INFO:
- [Source residue] The note references "OpenViking" extensively, including specific implementation details like ".abstract.md," ".relations.json reason strings," and "L0/L1/L2" tier labels. The note's title and opening paragraph claim general scope ("pointer design tradeoffs in progressive disclosure"), but roughly a third of the body (the "What this looks like in practice" section plus scattered references) is OpenViking-specific comparison. This is not strictly residue — the comparison is explicitly framed — but the volume of OpenViking-specific detail is high relative to the note's general framing. A reader unfamiliar with OpenViking must absorb substantial system-specific terminology to follow the argument.

- [Proportion mismatch] The "Reliability" section (~200 words) carries the note's most distinctive insight — that reliability complicates the naive "maximize specificity" strategy and that agent statelessness creates a degradation cliff. The "Context-specificity" section (~250 words, plus the three link-phrase examples) gets comparable or greater space, but its content is more straightforward (a spectrum from fixed to crafted). The proportions are not severely off, but the reliability insight — which is what makes this note more than a taxonomy — could warrant deeper development relative to the more taxonomic context-specificity section.

CLEAN:
- [Pseudo-formalism] The note uses tables for comparison rather than formal notation. The tables organize genuine distinctions (pointer type vs. properties) rather than decorating prose with symbols. No pseudo-formal apparatus detected.

- [Orphan references] The note contains one specific figure-like claim: "~5-10 tok," "~100 tok," "~50 tok," "~2000 tok," "~20 tok" in the comparison table. These are approximate token counts used as size characterizations rather than empirical measurements, and they are presented with the "~" marker signaling estimation. No named studies, percentages, or empirical claims appear without context.

- [Unbridged cross-domain evidence] The note stays within its own domain (knowledge system design, agent navigation). It references human judgment for crafted pointers but does not cite cross-domain empirical findings that would need bridging. The OpenViking comparison is system-to-system, not cross-domain.

- [Redundant restatement] Sections build on each other without re-explaining prior material. The "Reliability" section opens by directly addressing the new axis rather than restating the context-specificity discussion. The "What this looks like in practice" section moves to concrete comparison without re-deriving the framework.

- [Anthropomorphic framing] The note uses "agent" consistently to refer to LLM agents navigating the knowledge base, not to attribute human-like properties. Verbs applied to agents are appropriate: "scan," "load," "decide." The note does not use "understands," "believes," or "knows" for models.

Overall: 1 warning, 2 info
===
