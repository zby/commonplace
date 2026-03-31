Key claims by section:

- **Intro**: Agents can't carry definitions between reads; remedy is automatic context injection.
- **Evidence/Definitions**: Definitions are the cleanest case (small, stable, referential, once-per-session). A `definition` type would enable this.
- **Beyond definitions**: Four injection candidates with different triggers.
- **Reasoning**: Loading hierarchy extended with "on reference" layer.
- **Caveats**: Requires own runtime, context budget, staleness, granularity, discovery.

---

**Pairwise contradiction: none found**

- "The claim here is about the need for injection, not the mechanism" (intro) vs. detailed mechanism discussion (table, hierarchy, definition type). INFO — the note's stated scope (need, not mechanism) is narrower than its actual content. This is common in speculative notes and isn't a contradiction, but the disclaimer understates the note's actual scope.
- "Definitions should be loaded once per session" (evidence) vs. "the agent has the stale version" if updated mid-session (caveats). Consistent — the once-per-session property is both a benefit and a staleness risk, and the note acknowledges both.
- "Definitions are stable enough that [staleness] is unlikely" (caveats) vs. extending injection to ADRs and specs (beyond definitions). Consistent — the note explicitly notes staleness is sharper for less-stable types.

**Definition drift: none observed**

"Auto-injection," "context engine," "on reference," "definition type" — all consistent. "Type" is used in two senses (document type vs. injection trigger) but context disambiguates.

One INFO on scope disclaimer vs. actual content. No WARN, no contradiction, no drift.
