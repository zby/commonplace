# Test selection

Use a small selected suite during development. GitHub CI runs the complete
default suite on pushes and pull requests; no additional local full-suite run
is required before pushing. Subsystem directories describe responsibility; the
`slow` marker describes cost independently of responsibility.

## Commands

```bash
# Local iteration: general tests plus the affected subsystem (fast tests).
uv run pytest tests/commonplace/general tests/commonplace/review

# Slow coverage for a subsystem. An explicit -m replaces the default filter.
uv run pytest tests/commonplace/agentic_analysis -m slow

# Full verification when needed locally (also run by CI), including slow tests.
uv run pytest -m ''

# Development lint.
uv run ruff check .
```

The default test paths cover `tests/commonplace/`. Calibration, connect fixtures,
and installed scenarios outside that directory are separate tools or exercises;
this gate does not claim to run them. See
[installed scenarios](scenarios/installed/README.md) for that procedure.

## Selection rules

For local work and before committing code, run `general/` plus all affected
subsystem directories. Include relevant slow tests when changing the behavior
they cover; slow tests are not optional merely because they cost more.
Report the directories and marker filter actually run, not “all tests passed.”

Use the table below as a starting point, not an exhaustive dependency graph.
Select consumers when changing shared code. Run the full fast suite if impact
is uncertain; run the full suite for broad runtime or analysis changes.

All suite paths below are relative to `tests/commonplace/`.

| Changed responsibility or production paths | Required subsystem suites, in addition to `general/` |
|---|---|
| `src/commonplace/headless/` | `headless/`, `agentic_analysis/` (the workflow runs on it; its end-to-end tests are slow) |
| `lib/tasks.py`, `cli/task.py` | `headless/` (the task launcher runs on the fake harness there) |
| `lib/agentic_analysis/`, `cli/analysis.py`, analysis plan, instructions, roles, schemas | `agentic_analysis/` (include the slow workflow tests for behavior changes); also `comparison/`, `validation/`, or `docs/` when their inputs/contracts change |
| `src/commonplace/review/`, `cli/review/` | `review/`; also `freshness/` and `relocation/` when shared review state or selectors change |
| `src/commonplace/freshness/`, `cli/freshness_*.py` | `freshness/`, `review/` |
| `lib/validation.py`, `lifecycle_validation.py`, `full_pass.py`, validation/guard CLIs | `validation/`, `sources/`, `review/`, `agentic_analysis/`, `installation/` (validation consumers); include relevant slow analysis tests |
| `lib/quote_*.py`, `snapshot.py`, `source_identity.py`, snapshot/source/quote CLIs, `scripts/sync_x_likes.py` | `sources/`; also `validation/` and `agentic_analysis/` for shared quote, snapshot, or source-identity changes |
| `lib/relocation.py`, relocation CLIs | `relocation/` |
| `lib/index_*.py`, `promotion.py`, promotion CLI | `indexing/`; also `relocation/`, `installation/`, `docs/` for shared generated-index behavior |
| `lib/systems_matrix.py`, matrix build/render/analyze scripts | `comparison/` |
| `lib/project_status.py`, `cli/status.py` | `review/`, `freshness/` |
| `store.py`, `store-schema.sql` | `review/`, `freshness/`, `relocation/` |
| Foundational parsing, naming, library/type/path resolution, directory contracts | Full fast suite, plus relevant slow tests for affected consumers |
| `cli/init_project.py`, `scaffold_manifest.py`, `build_hooks.py`, packaging/dependency metadata | Full suite; follow editable-installation checks in `INSTALL.md` |
| Site configuration, `src/commonplace/docs/`, published collection/type/command contracts | `docs/`; also `validation/` for schema or validator contract changes |
| Test-state capture, isolated Codex runner | `tooling/` |
| Test helpers or fixtures | Every suite importing them; full fast suite if uncertain |

`general/` contains shared parsing, path/library/type resolution, directory-layout,
and store-health checks. Keep it inexpensive and broadly applicable. It is not a
bucket for unclassified tests. Tests for a subsystem's CLI live with that
subsystem's library tests. `docs/` holds repository-wide publication and contract
checks; `installation/` holds scaffolding and package-build checks.

For Markdown KB data changes, use the relevant Commonplace validation commands
rather than pytest unless the change affects code contracts or test inputs.

## Test value review

Judge tests by the distinct regressions they detect, not by test count or lines
covered. For each new test or proposed removal, name the plausible failure,
its consequence, and the coverage that would otherwise miss it.

- Keep end-to-end cases for behavior that depends on components working
  together. Test local state transitions with narrow fixtures when another
  case already covers the path that produces that state.
- Merge overlapping scenarios only when the retained test preserves their
  distinct assertions. Do not share mutable run state between tests.
- Prefer observable behavior over internal call sequences, unless the sequence
  is itself a requirement such as correction ordering or bounded subprocess cost.
- Instruction-text checks protect the shipped text, not agent compliance. Keep
  exact-string assertions when literal wording is required; otherwise avoid
  pinning incidental line breaks, phrasing or changeable defaults.
- Separate runtime cost from maintenance cost. A cheap test can still be brittle;
  an expensive safety or recovery test can still earn its cost.

Use pytest's `--durations` output to find expensive cases. Compare the same
selected suite before and after a change; moving cases between suites or
excluding them with markers is not a runtime optimization.

## Fixture isolation and performance

Reuse static inputs, not mutable execution state. The agentic-analysis execution
fixtures prepare one session-level repository and expanded plan, then copy the
repository (including Git objects) for each test and deep-copy each requested
plan. The helper hashes library inputs before using the baseline; changed,
added, or removed inputs force a fresh expansion. Generated analysis run state
is excluded from that method-input snapshot. Repositories, run state, preparation
records, coordinators, and monkeypatches remain test-local.

Measure changes with the same selected suite before and after. Keep production
expansion tests uncached, and retain tests for baseline isolation and invalidation.
Do not trade assertions or isolation for a shorter run.

## CI verification

[GitHub CI](../.github/workflows/ci.yml) runs `uv run pytest -m ''` on pushes and
pull requests. There is no repository-managed pre-push test hook. Local test
selection remains governed by the rules above; do not duplicate the CI run
solely to push.
