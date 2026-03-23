=== PROSE REVIEW: two-context-boundaries-govern-collection-operations.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note introduces a novel analytical framework — the two-boundary model with three operational regimes — but presents it with assertive language throughout. "The two boundaries create three regimes" and "Orientation still works" and "descriptions become the only content that participates in index-level operations" all assert as established what is actually the note's own proposed decomposition. The note's status is `seedling`, which makes the mismatch more notable: the prose reads as settled theory, not as a proposed model being tried on.
  Recommendation: Add hedging at the point of introduction — e.g., "This creates what we can model as three operational regimes" — or at minimum, flag the framework as the note's own construction early on. The consequences section can stay assertive if the conditional framing is established up front ("if the two-boundary model holds, then...").

- [Proportion mismatch] The core claim is the two-boundary model itself (title, opening section, "The two boundaries" section). But the "Consequences" section — especially "Library/workshop separation is an operational necessity" — is substantially longer and more developed than the section that introduces and justifies the boundaries. The full-text boundary gets one paragraph; the index boundary gets one paragraph; then the consequences of the library/workshop separation get three paragraphs with detailed references to ADR 003, quality scores, and bullet-pointed strategy decomposition. The load-bearing idea (the two boundaries and why they diverge) is thinner than what follows from it.
  Recommendation: Develop the "The two boundaries" section — particularly the claim that "the full-text boundary may not [move with growing windows]" due to complexity costs, which is doing significant work but gets one sentence. Consider whether the library/workshop consequence section should be shortened here and developed in its own note (composability concern).

INFO:
- [Redundant restatement] The opening paragraph restates the areas note's argument ("It treats both as sharing one constraint: context is finite. But the two operations have different minimum resolution requirements.") before reaching the note's own contribution. This recapitulation is borderline — it does set up the specific point of departure — but the sentence "Comparative reading needs full note bodies — you can't detect redundancy between two notes from their descriptions alone" could be the opening move, with the areas-note reference as a parenthetical rather than a full paragraph of setup.

- [Source residue] The note is written at a general level (any note collection, context boundaries as abstract concept) but every concrete example is specific to this KB's own tooling: `/connect`, `index.md`, WRITING.md's 40-note threshold, ADR 003, quality scores. This is not exactly domain leakage — the note is explicitly about KB operations. But the title and framing ("any note collection faces two context boundaries") claim a generality that the body doesn't deliver: all evidence is from one system. A reader might wonder whether these boundaries apply to other knowledge systems or only to this one's specific architecture.

CLEAN:
- [Source residue] No unintended domain-specific vocabulary leaking from an external source. The note's domain-specific terms (orientation, comparative reading, index boundary, full-text boundary) are all defined within the note or its predecessor. The note was not generalized from a narrower source — it was built on top of another note in the same KB.

- [Pseudo-formalism] No formal notation or mathematical apparatus. The note uses plain prose throughout. The "three regimes" framing is verbal, not notational.

- [Orphan references] The ~40 note threshold is attributed to WRITING.md. ADR 003 is linked. The quality-scores note is linked. No unattributed specific numbers or empirical claims appear.

- [Unbridged cross-domain evidence] All cited evidence comes from within the KB's own design notes and architecture decisions. No cross-domain transfer is attempted — the note reasons from its own system's properties.

- [Anthropomorphic framing] The note uses "agent" throughout, consistently attributing operational capacities ("the agent can use the index to choose sub-passes intelligently") rather than mental states. "Build a mental model" in the middle-regime description is the closest to anthropomorphism but is used as a standard term in this KB's vocabulary. No instances of "understands," "believes," or "knows."

Overall: 2 warnings, 2 info
===
