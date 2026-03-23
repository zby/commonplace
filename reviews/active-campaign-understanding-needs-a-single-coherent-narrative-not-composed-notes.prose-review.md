=== PROSE REVIEW: active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md ===

Checks applied: 8

WARN:
- [Proportion mismatch] The core claim — that campaign-level coherence requires holistic rewrite, not composition — is established in one paragraph after the table ("The key insight is that..."). The "Evidence: theorist" section is roughly twice as long and carries most of the note's development. The note reads more like a theorist review with a general framing than a general claim supported by theorist as evidence. The title promises a general structural argument, but the body delivers it thinly and then spends its energy on one tool.
  Recommendation: Develop the general argument (why composition fails for campaign understanding, what properties holistic rewrite preserves) before reaching for theorist. Consider whether the theorist section's design-choice analysis ("Rewrite, don't append," "Update when theory changes," etc.) belongs in a related-system review rather than inline.

- [Source residue] The opening paragraph and table are cleanly general, but the "Relationship to the workshop layer" section slips into theorist-specific framing without signaling: "THEORY.MD has all the predicted workshop properties" and "It fills the 'session logs' slot from the workshop note." These sentences treat theorist's implementation as the referent rather than an example. Similarly, "The bridge question" section opens with "Theorist doesn't address this" — framing the gap in terms of what one tool lacks rather than what the pattern requires.
  Recommendation: In the workshop and bridge sections, lead with the general pattern requirement, then cite theorist as confirmation. E.g., "A campaign narrative needs extraction bridges when the campaign ends. Theorist, for instance, doesn't address this."

INFO:
- [Confidence miscalibration] The phrase "graph composition is the wrong structure" in the opening paragraph is a strong assertion for what the note establishes. The evidence is one tool (theorist) and a structural argument by analogy with the workshop layer. The table's clean dichotomy (durable knowledge vs. working understanding) presents the distinction as settled taxonomy rather than a proposed framing. Given the note's seedling status, this confidence level may be intentional (claim-first, evidence-later), but it is worth flagging.

- [Redundant restatement] The "Relationship to the workshop layer" section opens with "This is a concrete exemplar of the workshop layer the KB identified as missing," which partially restates what the theorist section already showed. The restatement is brief (one sentence) and does add new framing (explicitly naming the workshop connection), so this is borderline.

CLEAN:
- [Pseudo-formalism] No formal notation or mathematical apparatus. The comparison table uses prose throughout and earns its structure — each row captures a genuine dimension of difference. No decorative formalism.

- [Orphan references] All specific claims are traceable. Theorist is cited with URL, author, license, and year. The Augment bidirectional spec pattern is linked to an ingest document. The 200-line maximum is attributed to theorist's design. No floating empirical claims or unsourced numbers.

- [Unbridged cross-domain evidence] The note stays within a single domain (knowledge management for engineering agents). Theorist is cited as a same-domain implementation, not a cross-domain analogy. The Augment reference in the open questions section is framed as "offers a partial answer" with an explanation of the mechanism (distributing coherence-maintenance burden), which constitutes a sufficient bridge.

- [Anthropomorphic framing] The note uses "understanding" throughout, but this is the subject matter (what it means to track understanding during a campaign), not an attribution of mental states to models. Phrases like "what we currently believe" use first-person plural referring to the engineering team, not the model. No problematic agency language.

Overall: 2 warnings, 2 info
===
