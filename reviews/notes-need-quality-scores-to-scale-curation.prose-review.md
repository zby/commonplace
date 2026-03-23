=== PROSE REVIEW: notes-need-quality-scores-to-scale-curation.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its proposed scoring framework — status weights, type maturity, inbound link counts, recency decay tables — with assertive language ("Status is the strongest signal," "Type reflects structural maturity," "Inbound link count is a social proof signal") despite being entirely the note's own construction. None of these dimensions are cited from prior work or empirical evidence. The tables assign weight orderings ("highest," "medium," "low," "lowest") and decay rates ("Fast," "None") as if established, yet this is a speculative design proposal. The note's own status is `seedling`, which reinforces that this is unvetted.
  Recommendation: Hedge the framework language. "Status is likely the strongest signal" or "We propose status as the primary dimension" would match the epistemic status. The tables could be introduced with "A plausible weighting:" rather than presented as given.

- [Proportion mismatch] The core claim is that notes need quality scores to scale curation — i.e., this is fundamentally about a scaling problem and its fix. The scaling problem gets one paragraph (the opener). The scoring dimensions section (~20 lines including two tables) gets the bulk of development, but the note never establishes *how bad* the scaling problem actually is or *what evidence* suggests the current approach will break. The "Where scores get used" section (the payoff — what scores actually enable) gets only three short paragraphs. The most load-bearing argument — why filtering is necessary and what happens without it — is underdeveloped relative to the taxonomy of scoring dimensions.
  Recommendation: Develop the opening argument (what does failure look like concretely? at what scale?) or trim the scoring dimensions section. Consider whether the detailed scoring taxonomy belongs in a separate design note.

INFO:
- [Pseudo-formalism] The two tables (Status score weights, Recency decay by content type) look structured but don't add precision beyond the prose. The Status table's "Score weight" column uses ordinal labels (highest/medium/low/lowest) that the prose already conveys. The Recency table's "Recency decay" column uses binary labels (Fast/None) which could be stated in a sentence. These aren't problematic — tables aid scanability — but they risk implying a more rigorous scoring model than exists.

- [Orphan references] The note mentions "~100 notes" as the current scale and "200-500 notes" as a threshold for the cheapest filtering approach. These are reasonable estimates but unsupported — neither is derived from measurement. The "200-500" range in particular implies empirical grounding that doesn't exist. Minor concern given the note is a design proposal, but worth flagging.

CLEAN:
- [Source residue] The note operates at a consistent level of generality throughout. All examples (keyword search, /connect skill, frontmatter status, seedling pruning) are native to the KB domain the note addresses. No leaked framing from an external source domain.

- [Redundant restatement] Each section opens with its own contribution. "Where scores get used" does not re-explain what scores are. "Implementation spectrum" does not re-derive the scoring dimensions. The note reads as a single coherent draft rather than assembled fragments.

- [Anthropomorphic framing] The note refers to "an agent" evaluating candidates, which is accurate operational language for the /connect skill's behavior. No language attributes mental states to models or tools.

- [Unbridged cross-domain evidence] The note does not cite cross-domain studies. All claims stay within the KB-maintenance domain. The "social proof signal" phrase (for inbound link count) is a loose analogy to social dynamics but is immediately clarified as "the graph-topology version of citation count," which is a fair bridge.

Overall: 2 warnings, 2 info
===
