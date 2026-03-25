# Frontmatter Review Sweep — 2026-03-24

Reviewed: 154 notes
WARN: 23
INFO: 62
Clean notes: 85

Current notes reviewed: 35
Current WARN: 1
Current INFO: 10
Current clean notes: 25

This summary is built from the top rows of the ranked CSV tables.
For the full dataset, read `kb/reports/reviews/csv/`.

## Priority Current Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [distillation](../notes/definitions/distillation.md) | 1 | 0 | Title composability | Title is a bare noun ("Distillation") — "since distillation..." does not read as a complete clause. The note is definitional/term-pinning... |

## Priority Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative](../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) | 2 | 1 | Description discrimination, Title-bod... | The description "Agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distincti... |
| [design-methodology-borrow-widely-filter-by-first-principles](../notes/design-methodology-borrow-widely-filter-by-first-principles.md) | 1 | 2 | Title-body alignment | The title "Design methodology — borrow widely, filter by first principles" implies a uniform first-principles filter, but the body's actu... |
| [backlinks](../notes/backlinks.md) | 1 | 1 | Description discrimination | The description "Analysis of where backlinks (inbound link visibility) would concretely help agents working in the KB — use cases, trade-... |
| [brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles](../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) | 1 | 1 | Description discrimination | The description opens with "Brainstorming note that turns..." which is a "this note does X" summary frame. The procedure flags these as w... |
| [commonplace-architecture](../notes/commonplace-architecture.md) | 1 | 1 | Description discrimination | Description "The commonplace repo's own internal layout — what exists, what's missing, and the decision to put global types in CLAUDE.md ... |

## Hot Checks

| Check | WARN | INFO | Sample note | Sample finding |
|-------|------|------|-------------|----------------|
| Description discrimination | 9 | 10 | [backlinks](../notes/backlinks.md) | The description "Analysis of where backlinks (inbound link visibility) would concretely help agents working in the KB — use cases, trade-... |
| Title-body alignment | 8 | 13 | [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) | The title promises "contextual competence through discoverable, composable, trustworthy knowledge" — the three-properties framing — but t... |
| Title composability | 3 | 24 | [context-engineering](../notes/definitions/context-engineering.md) | Title "Context engineering" is a bare topic noun phrase. "since context engineering..." does not complete as a sentence fragment. However... |
| Claim strength | 1 | 7 | [programming-practices-apply-to-prompting](../notes/programming-practices-apply-to-prompting.md) | The title "Programming practices apply to prompting" is close to conventional wisdom — few practitioners in the LLM space would argue the... |
| claim-strength | 1 | 3 | [traversal-improves-the-graph](../notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid-task-context-switching.md) | Title "Traversal improves the graph" is broad enough that most KB practitioners would nod along without pushback. The note's actual non-o... |

## Low-Yield Checks

| Check | WARN | INFO | CLEAN | Sample note | Sample finding |
|-------|------|------|-------|-------------|----------------|
| description-discrimination | 0 | 0 | 19 |  | No warning sample |
| claim strength | 0 | 0 | 1 |  | No warning sample |
| description discrimination | 0 | 0 | 1 |  | No warning sample |
| title composability | 0 | 0 | 1 |  | No warning sample |
| title-composability | 0 | 1 | 18 |  | No warning sample |

## Ranked CSV Tables

- `kb/reports/reviews/csv/frontmatter-review.notes_by_warnings.csv` — note-level queue, most urgent first
- `kb/reports/reviews/csv/frontmatter-review.checks_summary.csv` — recurring failure modes, highest warning volume first
- `kb/reports/reviews/csv/frontmatter-review.checks_low_signal.csv` — checks with the fewest warnings, useful for pruning or redesign
- `kb/reports/reviews/csv/frontmatter-review.notes_summary.csv` — full per-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/frontmatter-review.findings.csv` — raw finding rows for deeper drill-down, not used in this summary
- `kb/reports/reviews/csv/frontmatter-review.current.notes_by_warnings.csv` — current-note priority queue for manual fixes
- `kb/reports/reviews/csv/frontmatter-review.current.notes_summary.csv` — per-current-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/frontmatter-review.current.checks_summary.csv` — warning-producing checks within current notes
