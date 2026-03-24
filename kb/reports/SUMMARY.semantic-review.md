# Semantic Review Sweep — 2026-03-24

Reviewed: 157 notes
WARN: 433
INFO: 652
Clean notes: 0

Current notes reviewed: 39
Current WARN: 103
Current INFO: 155
Current clean notes: 0

This summary is built from the top rows of the ranked CSV tables.
For the full dataset, read `kb/reports/reviews/csv/`.

## Priority Current Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](../notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) | 4 | 4 | Completeness, Grounding | The failure mode mapping table claims four ML failure modes map to codification equivalents "with mitigations that weight-based systems c... |
| [stale-indexes-are-worse-than-no-indexes](../notes/stale-indexes-are-worse-than-no-indexes.md) | 4 | 3 | Grounding, Completeness | The note claims the mechanism "generalises beyond indexes to any authoritative artifact — specs, documentation, plans, curated lists." Th... |
| [agent-statelessness-makes-routing-architectural-not-learned](../notes/agent-statelessness-makes-routing-architectural-not-learned.md) | 3 | 5 | Completeness, Grounding | The five-level loading hierarchy (CLAUDE.md -> skill descriptions -> skill bodies -> type templates -> methodology notes) omits conversat... |
| [bitter-lesson-boundary](../notes/bitter-lesson-boundary.md) | 3 | 5 | Completeness, Grounding | The confidence signals table enumerates three signals (specifiability, definition-vs-proxy, local-vs-compositional failures), but the not... |
| [files-not-database](../notes/files-not-database.md) | 3 | 5 | completeness, grounding-alignment | The "What actually breaks at scale" section claims three items: finding things, too many files per directory, and structured queries with... |

## Priority Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [decomposition-heuristics-for-bounded-context-scheduling](../notes/decomposition-heuristics-for-bounded-context-scheduling.md) | 4 | 12 | Completeness, Grounding | The rules do not address the irreducibly-dense-interaction case — tasks where most items interact with most others and the relevant set c... |
| [text-testing-framework](../notes/text-testing-framework.md) | 4 | 5 | Completeness | The six contract types in Section 1 omit an **accessibility contract** (readability level, alt text for images, plain-language requiremen... |
| [trace-derived-learning-techniques-in-related-systems](../notes/trace-derived-learning-techniques-in-related-systems.md) | 4 | 5 | Completeness, Grounding | The four-category Axis 1 taxonomy (single-session extension, cross-agent session aggregator, service-owned trace backend, trajectory-run ... |
| [claw-learning-is-broader-than-retrieval](../notes/claw-learning-is-broader-than-retrieval.md) | 4 | 4 | Completeness, Grounding — scope misma... | The four action modes (classification, communication, planning, pattern recognition) are presented as the concrete instances of "what a C... |
| [claw-learning-loops-must-improve-action-capacity-not-just-retrieval](../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) | 4 | 4 | Completeness — action modes, Groundin... | The five action modes (execution, classification, communication, planning, pattern recognition) are presented as "at least these modes" t... |

## Hot Checks

| Check | WARN | INFO | Sample note | Sample finding |
|-------|------|------|-------------|----------------|
| Completeness | 213 | 202 | [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) | The six-property table draws a clean binary between library and workshop, and the paragraph that follows correctly acknowledges "the dist... |
| Grounding | 44 | 75 | [a-knowledge-base-should-support-fluid-resolution-switching](../notes/a-knowledge-base-should-support-fluid-resolution-switching.md) | The note says "Link semantics encode zoom direction" and attributes directional meaning: "'Since [X]' zooms into a foundation -- followin... |
| Grounding — domain coverage | 21 | 1 | [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) | The note cites [constraining-and-distillation-both-trade-generality-for-compound] to ground the claim that constraining and distillation ... |
| Grounding alignment | 19 | 46 | [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) | The note claims that extraction bridges include spec mining "at the deterministic end" and links to spec-mining-as-codification.md. The s... |
| completeness | 15 | 17 | [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) | The note claims the soft bound operates across exactly "two dimensions" — volume and complexity — framing this as a complete decompositio... |

## Low-Yield Checks

| Check | WARN | INFO | CLEAN | Sample note | Sample finding |
|-------|------|------|-------|-------------|----------------|
| Internal consistency — definition stability | 0 | 0 | 6 |  | No warning sample |
| Grounding — oracle-strength-spectrum | 0 | 0 | 3 |  | No warning sample |
| Internal consistency — open questions | 0 | 0 | 3 |  | No warning sample |
| Grounding alignment — context-efficiency note | 0 | 0 | 2 |  | No warning sample |
| Grounding alignment — instruction specificity | 0 | 0 | 2 |  | No warning sample |

## Ranked CSV Tables

- `kb/reports/reviews/csv/semantic-review.notes_by_warnings.csv` — note-level queue, most urgent first
- `kb/reports/reviews/csv/semantic-review.checks_summary.csv` — recurring failure modes, highest warning volume first
- `kb/reports/reviews/csv/semantic-review.checks_low_signal.csv` — checks with the fewest warnings, useful for pruning or redesign
- `kb/reports/reviews/csv/semantic-review.notes_summary.csv` — full per-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/semantic-review.findings.csv` — raw finding rows for deeper drill-down, not used in this summary
- `kb/reports/reviews/csv/semantic-review.current.notes_by_warnings.csv` — current-note priority queue for manual fixes
- `kb/reports/reviews/csv/semantic-review.current.notes_summary.csv` — per-current-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/semantic-review.current.checks_summary.csv` — warning-producing checks within current notes
