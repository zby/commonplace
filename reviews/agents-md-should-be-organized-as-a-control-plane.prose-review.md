=== PROSE REVIEW: agents-md-should-be-organized-as-a-control-plane.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents the three-layer model (Invariants / Routing / Escalation boundaries) and the two-variable placement framework (loading frequency x failure cost) as established architecture rather than a proposed decomposition. Phrases like "Two variables determine placement" and the definitive "Placement rule:" assert a framework the note itself constructs. The layers are the note's own taxonomy, not cited from an external source, yet they receive no hedging.
  Recommendation: Flag these as proposed models. E.g., "A useful decomposition uses two variables..." or "One way to layer this..." rather than bare assertion. Alternatively, if the Harness Engineering source cited at the bottom validates the layering empirically, surface that citation inline where the layers are introduced so the assertive framing is grounded.

INFO:
- [Proportion mismatch] The core claim is the control-plane model with its placement rule (loading frequency x failure cost). The "Core model" section that carries this claim is 10 lines. The "AGENTS.md layers" section that elaborates Layer 1-3 is roughly 30 lines, and "Exclusion rules" gets another 10. The placement framework itself -- the most load-bearing idea -- gets less development than its downstream consequences. The imbalance is mild (the layers section directly instantiates the model), but the core model section could benefit from one more paragraph explaining why these two variables, and not others, are the right discriminators.

CLEAN:
- [Source residue] The note's claimed generality is about AGENTS.md / control-plane organization for agent-operated repos. All examples (routing tables, `kb/sources/`, `/ingest`, `WRITING.md`, `types/` templates) belong to this exact domain. The escalation examples in the "Escalation boundaries" section are concrete but domain-appropriate -- they illustrate the note's own system. No leaked framing from an unrelated domain detected.
- [Pseudo-formalism] No formal notation, equations, or symbolic apparatus appears. The note uses prose throughout with short bullet lists. Clean.
- [Orphan references] No unattributed specific numbers, percentages, or named studies appear in the body. The two source citations at the bottom (Context Engineering for AI Agents in OSS; Harness Engineering) are identified with enough context. The "100-line AGENTS.md" in the final citation is a specific claim but it is attributed to the source. Clean.
- [Unbridged cross-domain evidence] The note operates within a single domain (agent context engineering for repositories). The two cited sources are from the same domain. No cross-domain transfer requiring a bridge. Clean.
- [Redundant restatement] Sections open with their own contributions. The opening paragraph sets up the control-plane framing; "Core model" introduces the two variables; each layer section introduces its own content. No section re-explains what the previous section established. Clean.
- [Anthropomorphic framing] The note discusses "the agent" in operational terms: "agent behavior," "agent misses this instruction," "agent runtime." These are functional descriptions of a software system, not attributions of mental states. No instances of "understands," "believes," "knows," or "possesses knowledge." Clean.

Overall: 1 warning, 1 info
===
