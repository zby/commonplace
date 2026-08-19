# C1 outcome — Executable and documented command sets are equal

**State:** resolved 2026-08-19. There are 22 `commonplace-*` console scripts and
22 unique command-reference sections.

## Resolution

C1 closed independently of F1. `commonplace-verify-quotes` is now documented,
and a test enforces exact name equality between the published and documented
sets. The assertion compares sets rather than freezing 22 as a permanent
command count.

F1 remains open because catalogue presence and command operativity are separate
properties. If F1 removes `commonplace-freshness-accept`, it must remove the
package entry and command section together; the C1 guard then passes at 21
without modification.

## Implemented

1. Added `commonplace-verify-quotes` beside deterministic validation in
   `commands.md`, including:
   - one or more Markdown file/directory targets;
   - recursive directory behavior and `--show-matches`;
   - match, mismatch, and unresolved reporting;
   - exit `1` for mismatches and exit `0` when only unresolved results remain.
2. Added `tests/commonplace/docs/test_command_catalogue_integrity.py`. It reads
   `[project.scripts]` with `tomllib`, parses exact `### commonplace-*`
   headings, rejects duplicates, and compares the name sets with no allowlist.
3. Left `commonplace-freshness-accept` unchanged in both sets. C1 does not
   misrepresent its F1 capability defect as catalogue drift.

## Verification

- The focused catalogue test passes.
- The complete test suite passes: 491 tests.
- The new test passes focused Ruff validation. Repository-wide Ruff still has
  pre-existing failures outside this change.
- `commands.md`, this outcome, the plan index, and workshop state pass
  deterministic Markdown validation.

C1 reopens if a published `commonplace-*` name lacks exactly one matching
reference heading or a reference heading lacks a published command.
