=== PROSE REVIEW: stale-indexes-are-worse-than-no-indexes.md ===

Checks applied: 8

WARN:
- [Source residue] The Defenses section references system artifacts that are specific to an earlier version of this KB's architecture and no longer exist. "`areas:` frontmatter field is the first defense — it declares index membership at creation time" — the `areas:` field has been replaced by `tags:` per ADR 004. "`docs/indexes.md` serves this purpose" — no `docs/indexes.md` file exists in the repository. "The /connect skill's Phase 5 reads `docs/indexes.md`" — references the same nonexistent file. "Topics footer" — removed per ADR 004. These are not illustrative examples; they are presented as the note's concrete defense mechanisms, and they point to infrastructure that doesn't exist.
  Recommendation: Update the Defenses section to reference the current system: `tags:` frontmatter, generated index sections (the ADR 004 mechanism that directly addresses the staleness problem this note describes), and current index discovery paths. Alternatively, abstract the defenses to mechanism-level descriptions that don't depend on specific filenames.

- [Confidence miscalibration] The Defenses section presents a specific four-part defense architecture ("At creation time," "At connection time," "Deterministic check," "What remains unjudgeable") as if it is established and operational. Three of these four defenses reference nonexistent infrastructure (`docs/indexes.md`, the `areas:` field). The note asserts these as active defenses — "The `areas:` frontmatter field *is* the first defense," "`docs/indexes.md` *serves* this purpose" — using present tense for mechanisms that either never existed or have been superseded. This reads as an established system description when it is closer to a historical snapshot or a design proposal.
  Recommendation: Either update to reflect current mechanisms, or flag the Defenses section as describing a prior or proposed state. The core claim (title and first two sections) stands independently and doesn't need the specific defense inventory.

INFO:
- [Proportion mismatch] The core insight — the asymmetry between absent and stale indexes — is established in the opening two paragraphs (~120 words). The Defenses section (~160 words) is comparable in length but carries less argumentative weight; it describes implementation details rather than developing the central claim. The "critical moment is note creation" section (~70 words) identifies the key failure point but gets the thinnest treatment. This section is arguably the most actionable part of the note and could benefit from more development (e.g., why creation time is harder than update time, what makes the agent's index-awareness gap persistent).
  Recommendation: Consider expanding "The critical moment is note creation" to match its importance. The Defenses section could be shortened or split into a separate note if the defenses are updated.

CLEAN:
- [Source residue] The core claim (opening paragraph through the generalization paragraph) is cleanly domain-neutral. The index/search asymmetry is stated in terms of agent behavior, not tied to any specific system. The generalization to "any authoritative artifact — specs, documentation, plans, curated lists" is well-framed.

- [Pseudo-formalism] No formal notation or mathematical apparatus present. The note argues entirely in prose. Clean.

- [Orphan references] No specific numbers, percentages, named studies, or empirical data points appear in the note. The Sourcing section attributes the observation to "arscontexta methodology research" with a paraphrased claim rather than a specific figure. Clean.

- [Unbridged cross-domain evidence] The note operates within a single domain (agent-operated knowledge bases) and the arscontexta reference is from the same domain. The generalization to specs, documentation, and plans stays within the agent/knowledge-system domain. No cross-domain transfer requiring a bridge. Clean.

- [Redundant restatement] Each section opens with new information. "The critical moment is note creation" advances to a specific failure point. "Defenses" advances to mitigations. No section restates a prior section's conclusion. Clean.

- [Anthropomorphic framing] The note uses "agent" throughout, which in this KB's vocabulary refers to both human and LLM operators. "She falls back to search," "feels oriented," and "stops looking" describe observable behavior patterns rather than attributing mental states to a model specifically. The language is appropriate for the note's abstraction level. Clean.

Overall: 2 warnings, 1 info
===
