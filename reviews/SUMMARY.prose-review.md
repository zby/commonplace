# Prose Review Sweep — 2026-03-23

Reviewed: 153 notes
WARN: 265
INFO: 260
Clean notes: 0

This summary is built from the top rows of the ranked CSV tables.
For the full dataset, read `reviews/csv/`.

## Priority Notes

| Note | WARN | INFO | Top checks | Sample warning |
|------|------|------|------------|----------------|
| [legal-drafting-solves-the-same-problem-as-context-engineering](../kb/notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) | 4 | 2 | Confidence miscalibration, Proportion... | The note asserts "The parallel is not metaphorical" in its opening paragraph, then throughout treats the mapping as structural identity r... |
| [automating-kb-learning-is-an-open-problem](../kb/notes/automating-kb-learning-is-an-open-problem.md) | 3 | 3 | Proportion mismatch, Confidence misca... | The "What is a KB for?" section asserts "A knowledge base exists to answer questions about the project" as settled fact, then builds the ... |
| [quality-signals-for-kb-evaluation](../kb/notes/quality-signals-for-kb-evaluation.md) | 3 | 3 | Confidence miscalibration, Proportion... | The opening paragraph and frontmatter correctly signal "speculative" / "Brainstorming," but several passages later in the note assert as ... |
| [context-efficiency-is-the-central-design-concern-in-agent-systems](../kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) | 3 | 2 | Confidence miscalibration, Proportion... | "Context is the scarce resource in agent systems — not compute, memory, or storage" and "context is the lowest-degree-of-freedom resource... |
| [elicitation-requires-maintained-question-generation-systems](../kb/notes/elicitation-requires-maintained-question-generation-systems.md) | 3 | 2 | Confidence miscalibration, Unbridged ... | The four strategies are the note's own construction but are presented with assertive framing: "Strategies ordered by expertise required" ... |

## Hot Checks

| Check | WARN | INFO | Sample note | Sample finding |
|-------|------|------|-------------|----------------|
| Confidence miscalibration | 129 | 29 | [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) | The bridge taxonomy is asserted rather than proposed: "This means there are two kinds of bridges needed: **Extraction bridges** ... **Com... |
| Proportion mismatch | 84 | 52 | [a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge](../kb/notes/a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) | The title foregrounds three properties (discoverable, composable, trustworthy) as the central claim, but the "Three properties" section (... |
| Source residue | 21 | 73 | [agentic-systems-interpret-underspecified-instructions](../kb/notes/agentic-systems-interpret-underspecified-instructions.md) | The note claims broad generality ("A theoretical framing for LLM-based agentic systems") but several examples are narrowly from software ... |
| Orphan references | 9 | 8 | [agent-context-is-constrained-by-soft-degradation-not-hard-token-limits](../kb/notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) | "Context windows have grown roughly 30x per year since mid-2023" — this is a specific empirical claim with no source citation. It appears... |
| Unbridged cross-domain evidence | 7 | 13 | [ad-hoc-prompts-extend-the-system-without-schema-changes](../kb/notes/ad-hoc-prompts-extend-the-system-without-schema-changes.md) | The homoiconicity section claims: "This is the same property that makes Lisp, Emacs, and Smalltalk extensible from within — and carries t... |

## Low-Yield Checks

| Check | WARN | INFO | CLEAN | Sample note | Sample finding |
|-------|------|------|-------|-------------|----------------|
| anthropomorphic-framing | 0 | 0 | 1 |  | No warning sample |
| orphan-references | 0 | 0 | 1 |  | No warning sample |
| pseudo-formalism | 0 | 0 | 1 |  | No warning sample |
| unbridged-cross-domain-evidence | 0 | 0 | 1 |  | No warning sample |
| redundant-restatement | 0 | 1 | 0 |  | No warning sample |

## Ranked CSV Tables

- `reviews/csv/prose-review.notes_by_warnings.csv` — note-level queue, most urgent first
- `reviews/csv/prose-review.checks_summary.csv` — recurring failure modes, highest warning volume first
- `reviews/csv/prose-review.checks_low_signal.csv` — checks with the fewest warnings, useful for pruning or redesign
- `reviews/csv/prose-review.notes_summary.csv` — full per-note totals, warning-heavy notes first
- `reviews/csv/prose-review.findings.csv` — raw finding rows for deeper drill-down, not used in this summary
