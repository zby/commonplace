=== PROSE REVIEW: solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md ===

Checks applied: 8

WARN:
- [Source residue] The note explicitly frames the kitchen example as not domain-specific ("This is not domain-specific advice about kitchens; it is a general sequencing rule"), which is good. However, the second substantive paragraph shifts without transition to "agent workflows" and introduces a dense list of agent-specific terms — "required output schema, tool contracts, file locations, deterministic validation requirements, or precedence rules" and "rhetorical or representational: phrasing, narrative order, or which equivalent summary format to use." These are presented as the natural instantiation of the general rule, not as one domain among many. Because the title and opening claim a fully general sequencing rule ("constrained search"), the agent-workflow paragraph reads as residue from the KB's primary concern rather than an explicitly scoped example.
  Recommendation: Either frame the agent-workflow paragraph as an explicit example ("In agent workflows, for instance, ...") or add a second domain example so the general claim doesn't rest on a single application domain. The current phrasing "In agent workflows, low-degree-of-freedom choices usually correspond to..." is close but drops the signaling that this is illustrative rather than definitional.

INFO:
- [Confidence miscalibration] The four-step sequencing rule (identify, commit, recompute, defer) is the note's own construction — not directly attributed to Alexander or any other source. It is presented with imperative framing ("Identify... Commit... Recompute... Defer...") that reads as established procedure. The underlying idea is well-supported by Alexander and constraint-satisfaction literature, but the specific four-step decomposition is the note's synthesis. A brief signal that this is the note's operationalization of Alexander's insight (rather than Alexander's own formulation) would improve calibration.

CLEAN:
- [Pseudo-formalism] No formal notation appears. The note uses the term "degrees of freedom" informally but consistently, and never introduces variables, equations, or pseudo-mathematical apparatus. Clean.
- [Proportion mismatch] The core claim (commit low-DoF decisions first) receives the most development: the opening paragraph sets up the mechanism, the numbered list operationalizes it, and the follow-on paragraph explains why it works. The agent-workflow application and open questions are shorter, appropriately subordinate sections. Proportions match.
- [Orphan references] The note references "Christopher Alexander's kitchen example" without citing a specific work. However, this is a well-known illustration from Alexander's "Notes on the Synthesis of Form" and the note's framing provides enough context (window, table, stove placement) that a reader can evaluate and locate it. No unsupported numbers or empirical claims appear. Clean.
- [Unbridged cross-domain evidence] The Alexander kitchen example is from architectural/spatial design, applied to a general constrained-search claim. The note bridges this explicitly: "This is not domain-specific advice about kitchens; it is a general sequencing rule for constrained search." The shared mechanism (optionality preservation under sequential commitment) is stated. The bridge is adequate.
- [Redundant restatement] No section opens by re-explaining what a prior section established. The note is short and linear; each paragraph advances the argument. Clean.
- [Anthropomorphic framing] The note discusses design processes and agent workflows without attributing mental states to models. No anthropomorphic language detected. Clean.

Overall: 1 warning, 1 info
===
