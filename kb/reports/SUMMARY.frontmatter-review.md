# Frontmatter Review Sweep — 2026-03-24

Reviewed: 156 notes
WARN: 40
INFO: 64
Clean notes: 79

Current notes reviewed: 39
Current WARN: 16
Current INFO: 14
Current clean notes: 19

This summary is built from the top rows of the ranked CSV tables.
For the full dataset, read `kb/reports/reviews/csv/`.

## Priority Current Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [two-kinds-of-navigation](../notes/two-kinds-of-navigation.md) | 3 | 0 | Title composability, Claim strength, ... | Title "Two kinds of navigation" is a bare topic label that does not compose as a sentence fragment. "since two kinds of navigation" is gr... |
| [scenarios](../notes/scenarios.md) | 2 | 1 | Title composability, Title-body align... | Title is the bare topic word "Scenarios" — it cannot compose into a sentence fragment. "since scenarios..." or "because scenarios..." is ... |
| [what-cludebot-teaches-us](../notes/what-cludebot-teaches-us.md) | 2 | 1 | Description discrimination, Title com... | Description reads as a table-of-contents summary: "Techniques from cludebot worth borrowing — what we already cover, what to adopt now, a... |
| [learning-substrates-backends-and-artifact-forms](../notes/learning-substrates-backends-and-artifact-forms.md) | 1 | 1 | Title composability | The title "Learning substrates, backends, and artifact forms" is a comma-separated list of three terms. It does not compose as a sentence... |
| [link-contracts-framework](../notes/link-contracts-framework.md) | 1 | 1 | Description discrimination | Description reads as a content inventory rather than a retrieval filter: "Reference framework for systematic, testable linking — link con... |

## Priority Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [two-kinds-of-navigation](../notes/two-kinds-of-navigation.md) | 3 | 0 | Title composability, Claim strength, ... | Title "Two kinds of navigation" is a bare topic label that does not compose as a sentence fragment. "since two kinds of navigation" is gr... |
| [scenarios](../notes/scenarios.md) | 2 | 1 | Title composability, Title-body align... | Title is the bare topic word "Scenarios" — it cannot compose into a sentence fragment. "since scenarios..." or "because scenarios..." is ... |
| [three-space-agent-memory-maps-to-tulving-taxonomy](../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) | 2 | 1 | Description discrimination, Title-bod... | The description "Agent memory split into knowledge, self, and operational spaces mirrors Tulving's semantic/episodic/procedural distincti... |
| [what-cludebot-teaches-us](../notes/what-cludebot-teaches-us.md) | 2 | 1 | Description discrimination, Title com... | Description reads as a table-of-contents summary: "Techniques from cludebot worth borrowing — what we already cover, what to adopt now, a... |
| [alexander-patterns-and-knowledge-system-design](../notes/alexander-patterns-and-knowledge-system-design.md) | 2 | 0 | Description discrimination, Claim str... | The description "Christopher Alexander's pattern language, generative processes, and centers may connect to our knowledge system design a... |

## Hot Checks

| Check | WARN | INFO | Sample note | Sample finding |
|-------|------|------|-------------|----------------|
| Description discrimination | 17 | 11 | [agents-navigate-by-deciding-what-to-read-next](../notes/agents-navigate-by-deciding-what-to-read-next.md) | The description "An agent doing a task navigates by deciding what to read — links, index entries, search tools, and skill descriptions ar... |
| Title-body alignment | 10 | 13 | [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) | The title promises "contextual competence through discoverable, composable, trustworthy knowledge" — the three-properties framing — but t... |
| Title composability | 8 | 24 | [context-engineering](../notes/context-engineering.md) | Title "Context engineering" is a bare topic noun phrase. "since context engineering..." does not complete as a sentence fragment. However... |
| Claim strength | 3 | 9 | [alexander-patterns-and-knowledge-system-design](../notes/alexander-patterns-and-knowledge-system-design.md) | The title "Alexander's patterns connect to knowledge system design at multiple levels" asserts a connection without specifying what the c... |
| claim-strength | 1 | 2 | [traversal-improves-the-graph](../notes/traversal-improves-the-graph.md) | Title "Traversal improves the graph" is broad enough that most KB practitioners would nod along without pushback. The note's actual non-o... |

## Low-Yield Checks

| Check | WARN | INFO | CLEAN | Sample note | Sample finding |
|-------|------|------|-------|-------------|----------------|
| description-discrimination | 0 | 0 | 17 |  | No warning sample |
| claim strength | 0 | 0 | 1 |  | No warning sample |
| description discrimination | 0 | 0 | 1 |  | No warning sample |
| title composability | 0 | 0 | 1 |  | No warning sample |
| title-composability | 0 | 1 | 16 |  | No warning sample |

## Ranked CSV Tables

- `kb/reports/reviews/csv/frontmatter-review.notes_by_warnings.csv` — note-level queue, most urgent first
- `kb/reports/reviews/csv/frontmatter-review.checks_summary.csv` — recurring failure modes, highest warning volume first
- `kb/reports/reviews/csv/frontmatter-review.checks_low_signal.csv` — checks with the fewest warnings, useful for pruning or redesign
- `kb/reports/reviews/csv/frontmatter-review.notes_summary.csv` — full per-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/frontmatter-review.findings.csv` — raw finding rows for deeper drill-down, not used in this summary
- `kb/reports/reviews/csv/frontmatter-review.current.notes_by_warnings.csv` — current-note priority queue for manual fixes
- `kb/reports/reviews/csv/frontmatter-review.current.notes_summary.csv` — per-current-note totals, warning-heavy notes first
- `kb/reports/reviews/csv/frontmatter-review.current.checks_summary.csv` — warning-producing checks within current notes
