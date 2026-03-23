# Semantic Review Sweep — 2026-03-23

Reviewed: 155 notes
WARN: 425
INFO: 639
Clean notes: 0

This summary is built from the top rows of the ranked CSV tables.
For the full dataset, read `reviews/csv/`.

## Priority Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [decomposition-heuristics-for-bounded-context-scheduling](../kb/notes/decomposition-heuristics-for-bounded-context-scheduling.md) | 4 | 12 | Completeness, Grounding | The rules do not address the irreducibly-dense-interaction case — tasks where most items interact with most others and the relevant set c... |
| [text-testing-framework](../kb/notes/text-testing-framework.md) | 4 | 5 | Completeness | The six contract types in Section 1 omit an **accessibility contract** (readability level, alt text for images, plain-language requiremen... |
| [trace-derived-learning-techniques-in-related-systems](../kb/notes/trace-derived-learning-techniques-in-related-systems.md) | 4 | 5 | Completeness, Grounding | The five recurring stages claim ("the same five stages appear") omits a stage present in several surveyed systems: **deduplication/confli... |
| [claw-learning-is-broader-than-retrieval](../kb/notes/claw-learning-is-broader-than-retrieval.md) | 4 | 4 | Completeness, Grounding — scope misma... | The four action modes (classification, communication, planning, pattern recognition) are presented as the concrete instances of "what a C... |
| [deploy-time-learning-the-missing-middle](../kb/notes/deploy-time-learning-the-missing-middle.md) | 4 | 4 | Completeness — Three Timescales, Comp... | The note claims exactly three timescales of adaptation. Boundary case: **retrieval-augmented generation (RAG) with a continuously updated... |

## Hot Checks

| Check | WARN | INFO | Sample note | Sample finding |
|-------|------|------|-------------|----------------|
| Completeness | 215 | 199 | [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) | The library/workshop binary may not be exhaustive. A plausible boundary case is a **living checklist or runbook** -- a document that is u... |
| Grounding | 43 | 74 | [a-knowledge-base-should-support-fluid-resolution-switching](../kb/notes/a-knowledge-base-should-support-fluid-resolution-switching.md) | The note says "Link semantics encode zoom direction" and attributes directional meaning: "'Since [X]' zooms into a foundation -- followin... |
| Grounding alignment | 20 | 47 | [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) | The note claims the type system is "text, note, structured-claim, spec, adr" and calls it a "maturity ladder." The linked document-classi... |
| Grounding — domain coverage | 20 | 1 | [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../kb/notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) | The note cites [constraining-and-distillation-both-trade-generality-for-compound] to ground the claim that constraining and distillation ... |
| Grounding — scope mismatch | 12 | 1 | [automated-synthesis-is-missing-good-oracles](../kb/notes/automated-synthesis-is-missing-good-oracles.md) | The note claims: "Discriminating the valuable from the noise requires judgment that is not substantially cheaper than producing the synth... |

## Low-Yield Checks

| Check | WARN | INFO | CLEAN | Sample note | Sample finding |
|-------|------|------|-------|-------------|----------------|
| Internal consistency — definition stability | 0 | 0 | 6 |  | No warning sample |
| Grounding — oracle-strength-spectrum | 0 | 0 | 3 |  | No warning sample |
| Internal consistency — open questions | 0 | 0 | 3 |  | No warning sample |
| Grounding alignment — instruction specificity | 0 | 0 | 2 |  | No warning sample |
| Grounding — attribution accuracy | 0 | 0 | 2 |  | No warning sample |

## Ranked CSV Tables

- `reviews/csv/semantic-review.notes_by_warnings.csv` — note-level queue, most urgent first
- `reviews/csv/semantic-review.checks_summary.csv` — recurring failure modes, highest warning volume first
- `reviews/csv/semantic-review.checks_low_signal.csv` — checks with the fewest warnings, useful for pruning or redesign
- `reviews/csv/semantic-review.notes_summary.csv` — full per-note totals, warning-heavy notes first
- `reviews/csv/semantic-review.findings.csv` — raw finding rows for deeper drill-down, not used in this summary
