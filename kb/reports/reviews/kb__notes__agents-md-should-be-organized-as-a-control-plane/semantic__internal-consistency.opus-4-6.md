Key claims by section:

- **Intro**: AGENTS.md is a runtime control plane. "Maximize decision quality per token."
- **Core model**: Loading frequency × failure cost determines placement.
- **Layers**: Invariants, routing, escalation boundaries.
- **Nested topology**: Root → subtree → leaf, with tightening but no contradiction.
- **Exclusion rules**: Six categories that belong elsewhere.
- **Lifecycle**: Guidance migrates from methodology → AGENTS.md → instructions → skills → scripts.
- **Quality tests**: Six questions testing appropriateness.

---

**Pairwise contradiction: none found**

- "Maximize decision quality per token" (intro) is consistent with the two failure modes (token pressure, attention dilution) and with the exclusion rules (keep AGENTS.md short).
- "Child files may add or tighten constraints" but "should not contradict parent invariants" (nested topology) — consistent; tightening is compatible with not contradicting.
- Exclusion rule: "capability inventories" should stay out. But Layer 2 (routing) includes "references to deeper docs." These are different — routing points to capabilities without listing them. Consistent.
- Lifecycle step 2: "AGENTS.md may hold a minimal invariant or routing pointer." This is consistent with the layers — AGENTS.md holds only the pointer, not the full procedure.

**Definition drift: none observed**

"Control plane," "invariant," "routing," "escalation boundary" — all defined in the layers section and used consistently. "Token pressure" and "attention dilution" are introduced as distinct failure modes and stay distinct.

**INFO — lifecycle and exclusion rules create a tension**

The lifecycle says "AGENTS.md may hold a minimal invariant or routing pointer" at step 2. The exclusion rules say "long procedural checklists" and "high-rationale background theory" should stay out. These are compatible on paper, but in practice the boundary between "minimal routing pointer" and "procedural checklist snippet" is judgment-dependent. The quality tests help resolve this but the tension is inherent in any system that says "some things go here, similar things don't."

No WARN. One INFO on the routing/checklist boundary tension.
