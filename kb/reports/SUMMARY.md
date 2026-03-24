# Review Sweep (All Types) — 2026-03-24

Reviewed: 308 notes
WARN: 690
INFO: 899
Clean notes: 0

Current notes reviewed: 80
Current WARN: 174
Current INFO: 222
Current clean notes: 0

This summary is built from the top rows of the ranked CSV tables.
For the full dataset, read `kb/reports/reviews/csv/`.

## Priority Current Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [text-testing-framework](../notes/text-testing-framework.md) | 6 | 7 | Completeness, Confidence miscalibrati... | The note presents a detailed seven-section framework — contracts, test pyramid, metamorphic tests, corpus compatibility, production workf... |
| [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) | 6 | 5 | Completeness, Grounding, Confidence m... | The note presents its own analytical framework — the failure mode mapping table, the claim that substrate inspectability is the decisive ... |
| [stale-indexes-are-worse-than-no-indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) | 6 | 4 | Grounding, Source residue, Confidence... | The Defenses section references system artifacts that are specific to an earlier version of this KB's architecture and no longer exist. "... |
| [learning-is-not-only-about-generality](../notes/learning-is-not-only-about-generality.md) | 5 | 7 | Source residue, Completeness, Groundi... | The table in "Generality" (lines 17-24) uses exclusively KB-domain examples: "Fix a typo," "Sharpen a description," "Add a connection," "... |
| [memory-management-policy-is-learnable-but-oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) | 5 | 7 | Confidence miscalibration, Proportion... | The note presents its own analytical frameworks as established fact rather than proposed interpretation. "Memory management decomposes in... |

## Priority Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [legal-drafting-solves-the-same-problem-as-context-engineering](../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) | 7 | 6 | Confidence miscalibration, Completene... | The note asserts "The parallel is not metaphorical" in its opening paragraph, then throughout treats the mapping as structural identity r... |
| [decomposition-heuristics-for-bounded-context-scheduling](../notes/decomposition-heuristics-for-bounded-context-scheduling.md) | 6 | 14 | Completeness, Grounding, Confidence m... | The rules are presented as imperative directives ("Separate selection from joint reasoning," "Use symbolic operations wherever exactness ... |
| [oracle-strength-spectrum](../notes/oracle-strength-spectrum.md) | 6 | 10 | Completeness, Pseudo-formalism, Orpha... | The amplification section introduces formal-looking notation: "TPR > FPR" and "1/(TPR-FPR)^2" scaling. The scaling formula is stated with... |
| [automating-kb-learning-is-an-open-problem](../notes/automating-kb-learning-is-an-open-problem.md) | 6 | 9 | Proportion mismatch, Completeness, Co... | The "What is a KB for?" section asserts "A knowledge base exists to answer questions about the project" as settled fact, then builds the ... |
| [text-testing-framework](../notes/text-testing-framework.md) | 6 | 7 | Completeness, Confidence miscalibrati... | The note presents a detailed seven-section framework — contracts, test pyramid, metamorphic tests, corpus compatibility, production workf... |

## Hot Checks

| Check | WARN | INFO | Sample note | Sample finding |
|-------|------|------|-------------|----------------|
| Completeness | 215 | 199 | [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) | The library/workshop binary may not be exhaustive. A plausible boundary case is a **living checklist or runbook** -- a document that is u... |
| Confidence miscalibration | 129 | 29 | [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) | The bridge taxonomy is asserted rather than proposed: "This means there are two kinds of bridges needed: **Extraction bridges** ... **Com... |
| Proportion mismatch | 84 | 52 | [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) | The title foregrounds three properties (discoverable, composable, trustworthy) as the central claim, but the "Three properties" section (... |
| Grounding | 43 | 74 | [a-knowledge-base-should-support-fluid-resolution-switching](../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) | The note says "Link semantics encode zoom direction" and attributes directional meaning: "'Since [X]' zooms into a foundation -- followin... |
| Source residue | 21 | 74 | [agentic-systems-interpret-underspecified-instructions](../notes/agentic-systems-interpret-underspecified-instructions.md) | The note claims broad generality ("A theoretical framing for LLM-based agentic systems") but several examples are narrowly from software ... |

## Low-Yield Checks

| Check | WARN | INFO | CLEAN | Sample note | Sample finding |
|-------|------|------|-------|-------------|----------------|
| Internal consistency — definition stability | 0 | 0 | 6 |  | No warning sample |
| Grounding — oracle-strength-spectrum | 0 | 0 | 3 |  | No warning sample |
| Internal consistency — open questions | 0 | 0 | 3 |  | No warning sample |
| Grounding alignment — instruction specificity | 0 | 0 | 2 |  | No warning sample |
| Grounding — attribution accuracy | 0 | 0 | 2 |  | No warning sample |

## Ranked CSV Tables

- `kb/reports/reviews/csv/notes_by_warnings.csv` — note-level queue, most urgent first
- `kb/reports/reviews/csv/checks_summary.csv` — recurring failure modes, highest warning volume first
- `kb/reports/reviews/csv/checks_low_signal.csv` — checks with the fewest warnings, useful for pruning or redesign
- `kb/reports/reviews/csv/notes_summary.csv` — full per-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/findings.csv` — raw finding rows for deeper drill-down, not used in this summary
- `kb/reports/reviews/csv/current.notes_by_warnings.csv` — current-note priority queue for manual fixes
- `kb/reports/reviews/csv/current.notes_summary.csv` — per-current-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/current.checks_summary.csv` — warning-producing checks within current notes
