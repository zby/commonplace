=== PROSE REVIEW: ephemerality-is-safe-where-embedded-operational-knowledge-has-low-reach.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents "reach" as the single explanatory variable that unifies Kirsch's four barriers, but this unification is the note's own analytical construction, not Kirsch's. Phrases like "they share a deeper structure" and "The reach of the embedded knowledge, not the complexity of the code, is what makes ephemerality unsafe" assert this as established fact rather than flagging it as a proposed reframing. The bold boundary prediction — "the ephemeral/malleable boundary sits where the same operational resolution must survive across contexts" — is similarly presented as a conclusion rather than a hypothesis. Since this is a seedling note building an original interpretive frame on top of someone else's essay, the confidence level should reflect that.
  Recommendation: Add hedging at the two key assertion points. The opening paragraph could say "I read these as sharing a deeper structure" or "These can be unified under a single variable." The bold boundary statement could become "This suggests a cleaner prediction" rather than "This gives a cleaner prediction."

- [Proportion mismatch] The core claim is the title: ephemerality is safe where embedded operational knowledge has low reach. The section that most directly carries this claim is "Reach predicts where persistence pays" and "The boundary" — together about 220 words. Meanwhile "Kirsch's barriers all describe cross-context transfer" gets roughly 250 words walking through four sub-cases that re-describe the source material through the reach lens. The "Connection to vibe-noting" section (~130 words) extends the argument to a different domain. The load-bearing analytical work (what reach means operationally, how to assess it, where the boundary sits) is thinner than the illustrative walkthrough of Kirsch's four barriers.
  Recommendation: Consider whether "Kirsch's barriers all describe cross-context transfer" could be compressed — the four sub-cases follow the same pattern (X encodes knowledge that transfers; discarding X forces re-discovery). One or two exemplars plus a summary sentence might free space to develop the boundary criteria more concretely.

INFO:
- [Source residue] The note is explicitly about software engineering (responding to Kirsch's essay about software), so software-specific vocabulary ("billing system," "migration," "API response shape," "legacy column format") is appropriate rather than residue. However, the vibe-noting section shifts to knowledge work more broadly without signaling the domain change. The phrase "Vibe coding works well in low-reach zones" assumes the reader knows what vibe coding is — it's KB-internal vocabulary that could read as jargon to someone arriving from the Kirsch source alone.
- [Redundant restatement] The opening of "Reach predicts where persistence pays" partially restates the argument just made in the barriers section: "Reach is not code size, sophistication, or business importance" echoes the point already established by the four barrier analyses. This is mild — the sentence does pivot to a new emphasis (the negative definition of reach) — but the paragraph's first two sentences could be tightened.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus is used. The note argues entirely in prose with a clean three-zone classification (low-reach, boundary, high-reach) that is verbal and appropriately informal for a seedling note.
- [Orphan references] No specific figures, percentages, or named studies appear without sourcing. Kirsch is cited throughout with a link to the source. Deutsch's "reach" concept is linked to the foundation note. No unsupported empirical claims.
- [Unbridged cross-domain evidence] The note stays within software engineering for its examples and does not import evidence from unrelated domains. The vibe-noting connection is to another KB note, not an external empirical claim, and the bridge is stated explicitly ("Reach does not replace those axes — it explains when inspectability becomes worth paying for").
- [Anthropomorphic framing] The note does not attribute human-like properties to models. Language is consistently about systems, artifacts, and knowledge rather than about agents possessing or understanding things. "Users and client systems have internalized" refers to actual humans and software, not LLMs.

Overall: 2 warnings, 2 info
===
