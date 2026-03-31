Key claims by section:

- **Intro**: Agents are stateless; routing is permanent architecture.
- **Progressive disclosure**: Five-layer loading hierarchy replaces navigation intuition.
- **Degradation cliff**: Binary fall (KB-augmented → generic) vs. human continuum.
- **Source vs. compiled**: Methodology = source; routing artifacts = compiled. Two genres with different quality criteria.
- **Design consequences**: Engineering discipline, staleness detection, behavioral completeness.

---

**Pairwise contradiction: none found**

- "The system learns, the agent doesn't" (intro) vs. "routing scales with the knowledge base itself" (consequences) — consistent; these are about different entities (practices vs. routing infrastructure).
- "Methodology notes are source code... Skills, routing tables... are compiled artifacts" (source/compiled) vs. "Stable procedures are distilled into skills" (lifecycle in related notes) — consistent; the metaphor captures the same flow.
- "Every session is day one" (intro) vs. "Persistent memory across sessions would relax the statelessness assumption" (consequences) — the note explicitly acknowledges the relaxation rather than contradicting its own premise.

**Definition drift: none observed**

"Routing," "statelessness," "progressive disclosure," "source," "compiled" — all used consistently. The "compiled" metaphor is introduced in one section and doesn't reappear elsewhere, so drift is impossible.

**INFO — "worse than no routing" tension with progressive disclosure**

The degradation cliff section says partial routing produces "confident execution with systematic errors — worse than no routing at all." But the progressive disclosure hierarchy is inherently partial — layer 1 (CLAUDE.md) is a deliberately incomplete routing surface, with gaps filled by deeper layers. If partial routing is worse than none, the hierarchy itself would be problematic. The resolution is likely that "partial routing" here means routing that covers some cases without indicating its own boundaries, whereas progressive disclosure explicitly routes to deeper layers. But this distinction isn't made explicit.

No WARN. One INFO on partial routing vs. progressive disclosure tension.
