# Workshop: gate-selector-flexibility

Goal: redesign the selector around flexible query axes while keeping the simplified review-tracking model in [scripts/REVIEW-SYSTEM.md](../../../scripts/REVIEW-SYSTEM.md).

## Why this workshop exists

The storage model is now deliberately simple: gate definitions live in files, recorded reviews are keyed by `(note, gate, model)`, and freshness is just mtime comparison. That simplification removed a lot of architectural weight, but it also means the selector is now the main place where future flexibility has to land.

Today's [gate selector](../../../scripts/gate_selector.py) is intentionally minimal:

- top-level `kb/notes/*.md` inventory only
- bundle directory or `--all-gates` scope only
- note filter by explicit path only
- fixed sort order
- grouped text or JSON output only
- diff generation only for `note-changed` records

That is good for the first system. It is not yet a general selector surface for different maintenance workflows.

## Prior work

- [gate-refactor](../gate-refactor/README.md) — established the simplified gate-native review architecture this workshop should preserve
- [selector-refactor](../selector-refactor/plan.md) — older selector flexibility work from the pre-simplification architecture; useful as contrast, not as a direct blueprint

## Questions

- Which axes of variation belong in selector policy versus plain filtering?
- How should bundle selection, gate selection, and note inventory compose?
- Which outputs are operationally distinct enough to deserve first-class renderers?
- When should the selector compute diffs eagerly, lazily, or not at all?
- What should stay hardcoded because it is system policy rather than user-tunable flexibility?

## Assessment (2026-03-27)

The design brief is ahead of the demand. The current selector works for the two workflows that actually run (review-sweep and warn_selector). The brief identifies 5 layers and 4 design questions for problems that haven't materialized yet — it's designing a general framework from one data point.

Premature elements:
- **Ranking/priority** — no workflow currently needs it
- **Multiple output renderers** — grouped text + JSON covers everything so far
- **Recursive inventory** — no notes outside top-level `kb/notes/` are reviewed yet
- **Grouped JSON packets** — the sweep instruction already groups by note in the agent prompt

The one thing worth doing now is separating inventory from freshness evaluation as a refactor of the existing script — that's a code quality improvement, not speculative flexibility. The rest should wait for the second concrete workflow the current selector can't serve, then refactor to support both.

## Files in this workshop

- [design-brief.md](./design-brief.md) — current constraints, redesign goals, and candidate architecture
