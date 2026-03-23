=== PROSE REVIEW: kb-goals-in-always-loaded-context-guide-inclusion-decisions.md ===

Checks applied: 8

WARN:
- [Confidence miscalibration] The note presents its five-subsection Goals framework (Purpose, Domain, Include, Exclude, Quality bar) with assertive framing: "The control-plane template includes a KB Goals section with five subsections." This framework is the note's own construction, but the language throughout that section uses directive phrasing — "Start from the users, not the domain," "Draw a scope boundary," "Name specific things" — that reads as established methodology rather than a proposed design. Since the note is status: seedling, the framework hasn't been validated by installation experience yet.
  Recommendation: Add a brief framing sentence acknowledging this is a proposed structure, e.g., "The proposed template includes..." or note that this design is untested. Alternatively, if the template already exists and has been used, upgrade the note's status from seedling.

- [Proportion mismatch] The core claim is in the title: KB goals in always-loaded context guide inclusion decisions. The section that argues *why* goals belong in always-loaded context ("Where goals belong") is 3 short numbered points totaling roughly 80 words. The section on *how to fill in* goals ("How to fill in the Goals section") is roughly 200 words across five subsections. The actionable guidance gets more development than the architectural argument that justifies it. The "What varies per installation" table (roughly 130 words) also outweighs the core argument section, and its content — that routing, type system, writing conventions, and link semantics are universal — is largely already known from the control-plane note it extends.
  Recommendation: Develop "Where goals belong" with more substance — e.g., a concrete example of what happens when goals are absent (the failure mode the description promises), or evidence from the self-hosting case. Consider whether the table duplicates what the control-plane note already establishes and could be trimmed.

INFO:
- [Anthropomorphic framing] The note uses "the agent has no basis for" and "an agent that ingests off-topic material" — these attribute decision-making to the agent. In this KB's domain (agentic systems), this is standard vocabulary and the note is genuinely talking about agent behavior, so this is appropriate. However, "Rejecting knowledge" in the bullet list anthropomorphizes slightly — the agent rejects *material* or *candidates*, not knowledge per se (knowledge implies it has already been validated).
- [Redundant restatement] The opening sentence of "Where goals belong" — "The control-plane model defines three layers: invariants, routing, escalation boundaries" — restates what the preceding paragraph already established by linking to the control-plane note. This is mild; it serves as a brief orienting transition, but a reader who followed the link already knows this.

CLEAN:
- [Source residue] The note's claimed generality level is KB architecture methodology. All vocabulary stays within that domain: "control plane," "routing table," "inclusion decision," "domain scope," "context budget." The illustrative examples (legal research, system architecture, API design, payment architecture, compiler optimization) are explicitly framed as examples of installation domains, not leaked residue from a specific source. Clean.
- [Pseudo-formalism] No formal notation, variables, or equations appear. The table in "What varies per installation" is organizational, not pseudo-formal. Clean.
- [Orphan references] No specific figures, percentages, or named studies appear. The note references its own linked notes (control-plane model, reach criterion) with sufficient context. The mention of "the control-plane template" references a linked file (AGENTS.md.template). Clean.
- [Unbridged cross-domain evidence] The note operates entirely within its own domain (KB methodology for agentic systems). No cross-domain evidence is cited. The reach note is referenced but only to distinguish goals from reach, not to import findings from another domain. Clean.

Overall: 2 warnings, 2 info
===
