=== SEMANTIC REVIEW: kb-goals-in-always-loaded-context-guide-inclusion-decisions.md ===

Claims identified: 14

**Claims extracted:**

1. "WRITING.md provides universal quality criteria ... but says nothing about domain scope" (opening paragraph)
2. "The routing table says where artifacts go, but not whether they should exist" (opening paragraph)
3. "This gap doesn't surface in commonplace itself — the domain is self-defining" (opening paragraph)
4. Four-item enumeration of what agents cannot do without explicit goals: rejecting out-of-scope material, deciding source worth, choosing note vs log, evaluating accumulated knowledge (bullet list)
5. "KB goals are a new invariant in Layer 1" of the control-plane model (Where goals belong)
6. Three-argument enumeration for why goals belong in the control-plane file: every write is an inclusion decision, loading frequency is high / failure cost is high, no extra hop (numbered list 1-3)
7. "A separate GOALS.md would add one tool call to every write path" (argument 3)
8. Nine-row table dividing concerns into per-installation vs universal (What varies per installation)
9. "Only the per-installation rows require human input. Everything else is generated from commonplace and can be updated mechanically on upgrade." (after table)
10. "The control-plane template includes a KB Goals section with five subsections" (How to fill in the Goals section)
11. Five subsection guidance blocks: Purpose, Domain, Include, Exclude, Quality bar (How to fill in the Goals section)
12. "Reach is a key quality criterion ... Goals are the domain filter" — goals and reach are orthogonal filters (Relation to reach)
13. "Both filters apply. Goals first (is this in scope?), then reach (is this worth the context it costs?)" — strict ordering claim (Relation to reach)
14. "Stale goals are worse than absent goals: they actively misdirect the agent" (Goal revision)

---

WARN:
- [Completeness] The four-item enumeration of what agents "cannot do" without goals (reject out-of-scope, decide source worth, choose note vs log, evaluate accumulated knowledge) omits a boundary case that the note's own "Goal revision" section implies: **detecting scope drift**. If the KB's domain evolves and goals are absent, the agent cannot recognize that the domain has shifted. This is distinct from the four listed capabilities, which all assume a static domain. The note partially addresses this in the "Goal revision" section but does not loop it back into the opening enumeration, creating a gap between the enumeration and the note's own later argument.

- [Grounding — scope mismatch] The note claims "KB goals are a new invariant in Layer 1" and cites the control-plane model (agents-md-should-be-organized-as-a-control-plane.md). The source defines Layer 1 invariants as "rules that must hold in every session and every task" and gives three examples: safety/destructive-action boundaries, repository-wide conventions, universal collaboration constraints. All three examples are behavioral constraints on the agent. "This KB is about X, not Y" is a content-scope constraint, not a behavioral constraint. The source's layer model was designed for behavioral invariants; the note extends it to domain-scope invariants without acknowledging that the category is being widened. The extension may be valid, but readers could mistake the source as already covering domain scope when it does not.

- [Completeness — boundary case] The note claims "A separate GOALS.md would add one tool call to every write path. Since the control-plane file is already loaded, embedding goals there costs nothing." The simplest boundary case — a KB with very long, detailed goals (multi-paragraph domain descriptions, extensive exclude lists) — challenges this. Long goals in the always-loaded file compete for tokens and attention, the very failure modes the control-plane note warns about. The note assumes goals are concise enough to fit without cost, but never states this assumption or addresses what happens when goals are verbose.

INFO:
- [Completeness — between-items case] The per-installation vs universal table lists "Quality bar" as per-installation and "Writing conventions" as universal. There is a case that sits between these two: tone or formality standards (e.g., "notes in this KB should be terse" vs "notes should include worked examples"). These are not domain-specific quality bars, nor are they universal WRITING.md conventions. The table forces a binary that may not fully cover this intermediate case.

- [Grounding — vocabulary mismatch] The note cites the "reach criterion" from first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md and says "Reach is a key quality criterion." The source note defines reach as a property of *explanatory knowledge* specifically (Deutsch's distinction). The goals note uses "reach" more loosely as a general quality measure ("is this worth the context it costs?"). The source's reach criterion is about explanatory depth and transferability, not about context cost. The inference (reach = worth the context cost) is reasonable but compresses away the specific Deutschian meaning.

- [Internal consistency — ordering claim] The note claims "Both filters apply. Goals first (is this in scope?), then reach (is this worth the context it costs?)." This strict ordering implies goals are always evaluated before reach. But the note's own example — "a brilliant insight about compiler optimization in a KB about payment architecture" — is a case where reach is immediately obvious and the goals filter is what rejects it. In reverse cases (a low-reach, clearly in-scope observation), the goals filter passes and only the reach filter decides. The ordering claim is presented as a general rule but only matters in one direction; in most practical cases, both filters can be evaluated independently. This is a minor ambiguity, not a contradiction.

- [Completeness — adjacent concept] The note identifies five subsections for the Goals section (Purpose, Domain, Include, Exclude, Quality bar). A boundary case from adjacent territory: **audience** (who reads this KB — is it for agents only, for human developers, or both?). Audience affects inclusion decisions (agent-optimized notes differ from human-optimized ones) and is not clearly covered by Purpose alone, which focuses on "what decisions/actions the KB supports." The Purpose guidance mentions "Who will use this KB?" in passing, but audience is arguably a distinct concern from purpose, especially when agents and humans have different retrieval patterns.

PASS:
- [Grounding — control-plane model] The note's use of the three-layer model (invariants, routing, escalation) from agents-md-should-be-organized-as-a-control-plane.md is structurally accurate. The source does define these three layers, and the note correctly identifies that routing "says where artifacts go" while goals address a gap the routing layer does not cover.

- [Grounding — installation architecture] The note's claim that the control-plane template includes a KB Goals section with five subsections is confirmed by AGENTS.md.template, which contains exactly Purpose, Domain, Include, Exclude, and Quality bar subsections under "KB Goals."

- [Grounding — loading frequency] The note cites instruction-specificity-should-match-loading-frequency.md to support the argument that goals need zero-hop access. The source does establish loading frequency and failure cost as the two placement variables, and the note's application of these criteria to goals is consistent with the source's framework.

- [Grounding — reach note] The note's characterization of reach as distinguishing knowledge that "transfers to new situations" from knowledge that does not accurately reflects the core argument in first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md. The orthogonality claim (goals filter scope, reach filters quality) is a novel contribution of this note, not attributed to the source, which is appropriate.

- [Internal consistency] The note is internally consistent across sections. The opening gap analysis (WRITING.md lacks scope, routing lacks should-exist) aligns with the proposed solution (goals as a new invariant). The per-installation vs universal table is consistent with the "only goals require human input" claim. The Goal revision section logically follows from the claim that goals are per-installation. No definition drift detected.

- [Internal consistency — compressed summary absent] The note has no compressed summary section, so there is no risk of summary eliding tensions acknowledged in the body. The "Relation to reach" section functions as a scope delimiter rather than a summary and is consistent with the body.

Overall: 3 warnings, 4 info
===
