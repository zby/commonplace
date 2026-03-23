=== PROSE REVIEW: learning-substrates-backends-and-artifact-forms.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note introduces its own three-level taxonomy (substrate class / backend / artifact form) and presents it with assertive language throughout: "The primary split is substrate class," "The three-level split prevents category mistakes that keep recurring," "Conflating the three makes the comparison space blurry." This is the note's own analytical construction — it is not cited from any source and not flagged as proposed. The taxonomy is defensible, but the phrasing treats it as the definitive decomposition rather than one useful decomposition.
  Recommendation: Add a brief framing sentence near the opening that marks this as the note's own proposed split — e.g., "A useful decomposition is..." or "One way to untangle this is a three-level split." The "Why the distinction matters" section can then demonstrate the value without needing to hedge every sentence, because the epistemic status was set up front.

INFO:
- [Proportion mismatch] The two definitional sections that carry the core claim — "Backend: where symbolic artifacts live" (~4 sentences) and "Artifact form: what symbolic artifacts look like" (~2 sentences) — are noticeably thinner than the "Why the distinction matters" section (~4 paragraphs plus a table). The artifact-form section in particular gives a list of examples but no development of what distinguishes forms from each other (granularity, retrieval mode, and behavioral directness are named but not unpacked). This is not a clear problem because the definitions may be intentionally tight, but if anyone later needs to classify a new artifact form, the note provides almost no guidance beyond listing examples.

CLEAN:
- [Source residue] The note claims general scope (a taxonomy of learning substrates) and uses domain-specific systems (AgeMem, Cognee, Commonplace, OpenClaw-RL) only as explicitly framed examples. No domain-specific vocabulary leaks through as if it were the default frame.
- [Pseudo-formalism] The only structured apparatus is the comparison table (lines 38–43), which maps real systems to the three taxonomy dimensions. It does genuine organizational work and makes no quantitative claims. No decorative notation.
- [Orphan references] No unsourced empirical claims, statistics, or named studies. All referenced systems are linked to their respective notes or ingest files.
- [Unbridged cross-domain evidence] The note does not cite findings from one domain as evidence for claims in another. All examples are drawn from systems already analyzed elsewhere in this KB, and the note's claims are taxonomic (how to categorize) rather than empirical (what happens).
- [Redundant restatement] Each section opens with its own contribution. "Backend" introduces where artifacts live, "Artifact form" introduces what they look like, "Why the distinction matters" introduces the payoff. No section restates a prior section's conclusion before proceeding.
- [Anthropomorphic framing] "The system learns" (opening paragraph) is used in the context of defining learning substrates — the note is explicitly about what constitutes learning, so this usage is deliberate and definitional. No instances of "possesses," "knows," "understands," or "believes."

Overall: 1 warning, 1 info
===
