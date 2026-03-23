=== PROSE REVIEW: deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The proposed architecture (Phase 1-5) is the note's own construction but is presented with assertive language — "Phase 1: Seed search," "Phase 2: Snapshot & inter-connect," etc. — as though the design is settled. The note's status is `seedling` and the section heading says "Proposed architecture," which is appropriate, but the phase descriptions themselves read as specifications rather than proposals. Phrases like "Run a lightweight /connect-like pass" and "Only after the search graph is internally coherent, connect it to the existing KB" assert a sequence without hedging. Compare with the open questions section, which correctly frames uncertainty.
  Recommendation: Add a framing sentence at the top of the architecture section (e.g., "One plausible decomposition:") and use softer language within the phases ("would run," "could connect") to match the seedling status consistently.

- [Proportion mismatch] The title claim is that deep search IS connection methodology applied to a temporarily expanded corpus — i.e., no new connection logic is needed, only corpus expansion. But the section that carries the most weight for this claim ("Two value propositions," ~6 sentences) is thinner than "Architectural tensions" (~12 sentences) and the "Proposed architecture" section (~10 sentences). The architectural tensions and proposed phases are important but secondary to the core argument. The note never directly demonstrates that /connect's logic transfers unchanged — it asserts it in the opening paragraph and then moves on to design details.
  Recommendation: Develop the core reuse argument. Show concretely how /connect's dual discovery and articulation testing would work on web search results (e.g., what does an articulation test between two search results look like?). This would ground the title claim rather than leaving it as a one-paragraph assertion.

INFO:
- [Pseudo-formalism] The three-level depth framework ("Shared feature," "Shared structure," "Generative model") is borrowed from the discovery epistemology note and numbered 1-2-3, giving it a taxonomic formality. Within this note, only level 1 is concretely characterized ("Embeddings get here cheaply. This is what naive RAG does."). Levels 2 and 3 get one-sentence descriptions. The framework does useful work (it distinguishes naive from deep search), but the precision drops as the levels increase. Worth checking whether levels 2 and 3 are sufficiently characterized to support the claims built on them ("The /connect skill already operates at level 2").
- [Redundant restatement] The opening of "Why this differs from naive search" partially restates what the introduction already established (that /connect provides deeper connections than naive retrieval). The transition from the "Two value propositions" section to "Why this differs from naive search" would be smoother if the latter jumped directly to the three-level framework without re-motivating the distinction.

CLEAN:
- [Source residue] The note operates at a consistent abstraction level throughout. It references KB-specific skills (/connect, /ingest, /snapshot-web) but these are the note's actual domain, not residue from a different source. No leaked vocabulary from an unrelated domain.
- [Orphan references] No unsourced empirical claims, specific numbers, or named studies appear. All specific references point to other KB notes, which is appropriate for a design exploration.
- [Unbridged cross-domain evidence] The note stays within its domain (KB methodology / agent-operated search). It does not cite findings from human cognition or other domains and apply them without bridging. The "boiling cauldron" metaphor is explicitly linked to its source note rather than imported as an unexplained analogy.
- [Anthropomorphic framing] One sentence says "the agent discovers what it doesn't know rather than looking up what it does" — this uses "discovers" and "knows" loosely, but the subject is "the agent" (a system), and the sentence is clearly describing system behavior (active research vs. retrieval), not making claims about mental states. No other anthropomorphic language detected.

Overall: 2 warnings, 2 info
===
