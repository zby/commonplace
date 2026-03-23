=== PROSE REVIEW: reliability-dimensions-map-to-oracle-hardening-stages.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The four-way mapping between reliability dimensions and oracle questions is the note's own construction — it synthesizes Rabanser et al.'s dimensions with the oracle-strength spectrum. However, the table presents this mapping with full assertive authority ("Converts interactive oracle to hard oracle via repetition," "This is the only dimension that's already a hard oracle by design"). The mapping is plausible but it is the note's interpretive contribution, not something established in either source. The claim that safety "is the only dimension that's already a hard oracle by design: either the failure is bounded or it isn't" is particularly strong — safety bounds can be partial, probabilistic, or context-dependent, making this a proposed binary where a spectrum may exist.
  Recommendation: Flag the table as a proposed mapping ("One way to align these frameworks...") or add a brief qualifier that this is the note's synthesis, not a claim found in either source paper.

- [Proportion mismatch] The core claim is the mapping itself (title: "Reliability dimensions map to oracle-hardening stages"), but the table that carries this claim gets no prose development — each mapping is compressed into a single sentence in the "Hardening move" column. Meanwhile, "The predictability gap" section (lines 33-36) receives two full paragraphs of development and introduces the augmentation/automation boundary, which is arguably a separate claim (and indeed has been extracted into its own note). The load-bearing content is thinner than the downstream implication.
  Recommendation: Develop at least one of the non-predictability mappings with a concrete example or worked scenario — particularly the consistency-to-hard-oracle path, which the MAKER example already supports but is currently only mentioned in "Why this mapping matters" rather than used to flesh out the table's compressed claim. Consider whether the augmentation/automation material (which already has its own note) can be trimmed here to rebalance.

INFO:
- [Pseudo-formalism] The "90%-accurate agent" in line 36 is a specific number used illustratively. It is not presented as formal notation, but it sits in a passage making a general point about the augmentation/automation boundary. The number isn't derived or sourced — it's a round-number example. This is borderline: it reads naturally as illustration, but a reader could mistake it for an empirical threshold.

- [Anthropomorphic framing] "requires the model to know *what it doesn't know*" (line 34) attributes epistemic self-awareness to the model. This is a deliberate framing choice (italicized for emphasis) and the surrounding context makes the technical meaning clear (discrimination at the per-instance level), but "know what it doesn't know" carries connotations of metacognitive awareness that go beyond calibration/discrimination.

CLEAN:
- [Source residue] The note's claimed generality level is the intersection of two frameworks (oracle-strength and reliability dimensions) applied to agent evaluation. The vocabulary throughout stays within this domain. The Towers of Hanoi reference (line 24) is explicitly framed as an example of MAKER's approach and does not leak as unexplained domain-specific residue. No narrower domain framing leaks through without being identified as illustrative.

- [Orphan references] "18 months of model releases" (line 24) is an empirical claim, but it is attributed to context ("The empirical finding that capability gains have outpaced reliability gains") that traces to the Rabanser et al. source, which is cited. The "80%" in line 17 is used illustratively within a conditional ("If the system says 80%..."), not as an empirical claim. The "90%" in line 36 is flagged under INFO above. No unattributed specific data points.

- [Unbridged cross-domain evidence] The note stays within the AI agent evaluation domain throughout. The two main sources (Rabanser et al. reliability framework, MAKER) are both from the same domain as the note's claims. No cross-domain transfer occurs without bridging.

- [Redundant restatement] Each section opens with new content. "Why this mapping matters" builds on the table rather than restating it. "Connection to spec mining" introduces a new operational mechanism. "The predictability gap" introduces a new dimension-specific analysis. No section opens by re-explaining what a prior section established.

Overall: 2 warnings, 2 info
===
