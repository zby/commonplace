=== PROSE REVIEW: knowledge-storage-does-not-imply-contextual-activation.md ===

Checks applied: 8

WARN:
- [Source residue] The note claims broad generality — title and opening are domain-neutral ("A model can contain relevant knowledge...") — but the initiative gradient section reverts to software-specific failure families without framing them as examples: "syntax, type mismatches, logical contradictions," "resource exhaustion, race conditions, cascading failures," "deployment topology issues, organizational process gaps." These are presented as direct illustrations of the gradient, not as one domain's instance of it. The open questions section then asks "Does the initiative gradient hold consistently across non-technical domains?" — acknowledging the note hasn't actually established generality despite claiming it.
  Recommendation: Either prefix the initiative gradient section with an explicit domain frame ("In software engineering, for instance, the gradient looks like...") or replace the domain-specific families with domain-neutral descriptions (surface errors, operational errors, systemic errors) and move the software examples into parenthetical illustrations.

- [Anthropomorphic framing] Several passages use language that attributes mental states where more precise alternatives exist. "the model may have equivalent knowledge" uses "have" where "encode" is more precise. "They see a design choice and immediately flag the failure mode" uses "see" for pattern-matching. Most notably, the expert-witness analogy's framing — "The model does the first reliably and the second unreliably" — treats the model as an agent with advisory intent. The note does use precise language elsewhere ("surface," "stores," "retrieval"), so this is inconsistent rather than systematic.
  Recommendation: Tighten the verbs in the expert-witness section: "produces accurate responses to direct queries" rather than "does the first reliably." Replace "have equivalent knowledge" with "encode equivalent knowledge" or "store equivalent knowledge." The expert-witness analogy itself is fine as an analogy — just ensure the surrounding prose doesn't slide from analogy into literal attribution.

INFO:
- [Confidence miscalibration] The three-stage decomposition (cue match, priority arbitration, commitment) is correctly hedged: "A plausible decomposition" and "proposed, not established." However, the initiative gradient section — "Empirically, the activation gap scales with distance from the immediate task artifact" — uses "empirically" without citation. This implies measured evidence exists. If the claim rests on the single source (the-bug-that-shipped), it is a suggestive observation from one study, not an empirical generalization. If it rests on broader observation, the sources aren't identified.
  Recommendation: Either cite the specific evidence behind "empirically" or soften to "In observed cases" or "Based on available evidence."

- [Proportion mismatch] The expertise gap section (~170 words) receives roughly equal or greater treatment than the initiative gradient (~100 words), despite the initiative gradient introducing a novel structural claim (the distance-from-artifact scaling) that arguably carries more analytical weight. The expertise gap, while important, is a more familiar observation (users can't ask what they don't know). This may reflect the expertise gap being easier to articulate rather than being more central.
  Recommendation: Consider whether the initiative gradient deserves development — perhaps with a brief example or a sentence explaining the mechanism (why does distance from the artifact reduce cue availability?). This is a mild finding; the current proportions are defensible if the expertise gap is considered the more actionable insight.

CLEAN:
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus. The three-stage decomposition uses numbered prose, not pseudo-formal structure. Clean.

- [Orphan references] No unsourced specific numbers, percentages, or named studies appear in the body. The note avoids quantitative claims without citation. The linked source (the-bug-that-shipped) is properly referenced in the links section. Clean.

- [Unbridged cross-domain evidence] The note explicitly bridges its human-cognition parallel: "This is not uniquely an LLM phenomenon. Humans show the same structure: 'I knew this, but it didn't occur to me.'" It then explains why the LLM case is distinct: "LLM systems make the control surface unusually explicit: prompt context is where cue match succeeds or fails." The bridge is well-constructed and directional. Clean.

- [Redundant restatement] Each section opens with new material. The expertise gap section doesn't re-explain the question-generation bottleneck before extending it — it immediately introduces the structural asymmetry. The initiative gradient section doesn't restate the activation gap before characterizing it. No wasted openings. Clean.

Overall: 2 warnings, 2 info
===
