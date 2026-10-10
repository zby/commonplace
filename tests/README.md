# Test selection

Use a small selected suite during development. Run the complete default suite
before pushing. Subsystem directories describe responsibility; the `slow` marker
describes cost independently of responsibility.

## Commands

```bash
# Local iteration: general tests plus the affected subsystem (fast tests).
uv run pytest tests/commonplace/general tests/commonplace/review

# Slow coverage for a subsystem. An explicit -m replaces the default filter.
uv run pytest tests/commonplace/agentic_analysis -m slow

# Full verification before pushing: all default tests, including slow tests.
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
| `src/commonplace/artifactrun/`, `cli/run.py` | `artifactrun/`, `agentic_analysis/` (workflow consumer; include slow coverage for behavior changes) |
| `lib/agentic_analysis/`, analysis plan, instructions, roles, schemas | `agentic_analysis/`; also `comparison/`, `validation/`, or `docs/` when their inputs/contracts change |
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
| Test-state capture, isolated Codex runner, `.githooks/pre-push` | `tooling/` |
| Test helpers or fixtures | Every suite importing them; full fast suite if uncertain |

`general/` contains shared parsing, path/library/type resolution, directory-layout,
and store-health checks. Keep it inexpensive and broadly applicable. It is not a
bucket for unclassified tests. Tests for a subsystem's CLI live with that
subsystem's library tests. `docs/` holds repository-wide publication and contract
checks; `installation/` holds scaffolding and package-build checks.

For Markdown KB data changes, use the relevant Commonplace validation commands
rather than pytest unless the change affects code contracts or test inputs.

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

## Pre-push hook

The tracked hook at [`.githooks/pre-push`](../.githooks/pre-push) runs
`uv run pytest -m ''` from the repository root and blocks a push on failure or
interruption. Budget about five minutes; timings vary by machine and checkout.

Enable it once per checkout, after checking for an existing hooks configuration:

```bash
git config --show-origin --get core.hooksPath
# If no existing hooks configuration needs preserving:
git config --local core.hooksPath .githooks
```

If another hooks path is configured, integrate this hook there or deliberately
replace that configuration; do not overwrite it silently. Setting `core.hooksPath`
also changes where Git looks for other hooks.

Commit or stash changes before pushing. The hook rejects tracked modifications,
staged changes, and untracked files (ignored files do not count). It checks again
after tests and rejects a changed HEAD. Do not edit the checkout while tests run.
These checks do not lock the checkout or detect edits that are made and reverted
during verification.

The hook verifies the current checked-out commit and working tree, not every
historical commit or arbitrary ref in a multi-ref push. Push the verified current
branch. Hook configuration is local and is not enforced on other checkouts;
CI remains an independent full-suite check.

`git push --no-verify` bypasses the gate. Use it only as an explicit operator-approved
exception and disclose the skipped verification. The hook intentionally has no
result cache: every ordinary push gets a fresh full-suite run.
