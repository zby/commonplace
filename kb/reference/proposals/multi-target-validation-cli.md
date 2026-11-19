---
description: "Proposal: allow commonplace-validate to validate multiple explicit file paths in one invocation, sharing startup and parsing indexes while keeping special validation modes and scope guards intact"
type: reference/types/design-proposal.md
tags: []
---

# Multi-target validation in commonplace-validate

## Current state (as of 2026-11-19)

- `commonplace-validate` (`src/commonplace/cli/validate_notes.py`) accepts one
  positional `target` argument: a file, artifact directory, ordinary subtree,
  collection, or one of the special targets (`types`, `landings`, `redirects`,
  `lifecycle`, `today`/`recent` with `--collection`), plus two dedicated modes
  (`--artifact`/`--role` and `--handoff`). Passing `all` or `kb/` is refused by
  a scope guard.
- Under the CLI, `run_validation(paths, repo_root=..., collection=...)`
  (`src/commonplace/lib/validation.py`) already accepts `paths: tuple[Path, ...]`
  and evaluates all paths in one `ValidationRun` with shared parsing, type
  resolution, and tag/source indexes.
- `ValidationReport` emits scalar `target: str`, `scope: str`, and
  `details_command: str` (which passes `[self.target]` to `shlex.join`).
  `--json` emits `commonplace.validation.v1` with those scalar fields plus
  `analysed_artifacts` and `diagnostics`. `--full` iterates `outcome.paths` and
  prints one block per artifact; when `target.collection is None`, it omits the
  collection batch summary.
- Multi-file edits—such as applying cross-references from `cp-skill-connect`
  across notes, tag heads, ingests, and reference documents—currently require
  one `commonplace-validate` invocation per file (for example, an 11-file shell
  `for` loop that pays 11 Python startups and index builds).

## Problem and intended outcome

Routine KB operations frequently edit a small heterogeneous set of files across
several collections (a new note, its bidirectional links in `kb/theory/`, tag
heads in `kb/tags/`, a grounded ingest in `kb/sources/`, and a reference entry
in `kb/reference/`). Validating each touched file currently forces either:

- a shell loop with repeated process startup and index reconstruction, or
- running separate collection sweeps that scan hundreds of untouched files.

**Intended outcome:** validate an explicit set of touched files in one
`commonplace-validate` invocation with one process startup, one shared
`ValidationRun`, and one combined pass/warn/fail exit status—without relaxing
the `all`/`kb/` scope guard or complicating single-artifact special modes.

Because `ValidationRun` already supports arbitrary `paths: tuple[Path, ...]`
with `collection=None`, the runtime cost reduction follows directly from
exposing that existing batch path at the CLI boundary.

## Boundary commitments

- Preserve the existing single-target CLI contract, exit codes, and default
  compact output for every currently valid invocation.
- Keep dedicated single-artifact modes (`--handoff`, `--artifact`/`--role`) and
  special surface targets (`lifecycle`, `redirects`, `landings`, `types`,
  `today`, `recent`) single-target unless a separate need arises.
- Preserve the scope guard against full-KB validation (`all` or `kb/`):
  multi-target support must not quietly become an alias for unbounded whole-KB
  sweeps.
- Add no new validation oracle and relax no existing check; every file receives
  the exact checks `ValidationRun` already runs on it.

## Options

### Option A: Multi-file positional arguments (`commonplace-validate PATH [PATH ...]`)

Change the positional argument to `nargs="+"`. When one target is supplied,
behavior is unchanged. When two or more targets are supplied:

- Every target must resolve to an explicit file or directory artifact (not a
  collection, directory sweep, special keyword, `--handoff`, or
  `--artifact`/`--role`). Mixing a special target or collection with additional
  targets exits with a CLI usage error.
- Paths are resolved, deduplicated preserving order, and passed together to
  `run_validation(paths, repo_root=repo_root, collection=None)`.
- Compact output prints one summary covering all supplied files (using
  `files_analysed`, `failing_subjects`, `warning_subjects`, and per-subject
  `diagnostics`). `--full` prints each file's validation block in order.

**Trade-offs.** Matches standard Unix CLI ergonomics (`git add`, `ruff check`,
`pytest`), solves the 2–20 file post-connect and pre-commit case with zero
extra flags, and avoids collection-batch ambiguity because `collection` stays
`None`. Does not combine two collection sweeps in one call, and very large
lists remain subject to shell argument length limits.

### Option B: Mixed multi-target composition (files, subtrees, and collections)

Allow `nargs="+"` to mix files, subtrees, and collections in one invocation
(still refusing `all`, `kb/`, and special modes).

**Trade-offs.** Eliminates the restriction on mixing a directory with an extra
file, but forces a design choice on collection-scoped batch checks
(`collection_warnings`, `collection_structure`, `excluded_subtrees`):
`ValidationRun` currently holds a single `collection: Path | None`. Either
`ValidationRun` must generalize to multiple collections (grouping batch checks
per collection and widening the report schema), or collection-level checks must
be silently dropped whenever >1 target is passed—which would surprise callers
expecting collection structure checks. It also weakens the practical boundary
against passing every collection name on one command line.

### Option C: Stdin / file-list flag (`--files-from PATH` or `--stdin`)

Keep the positional `target` single-valued and add an explicit list input
(e.g., `git diff --name-only | commonplace-validate --files-from -`), running
the same `ValidationRun(paths=..., collection=None)` path as Option A.

**Trade-offs.** Composes cleanly with `git diff --name-only` and scales past
shell argument limits without changing positional parsing. Worse ergonomics for
the common 2–15 file interactive and agent case (where the caller already has
explicit file paths and must otherwise wrap them in a pipeline or temporary
file). Compatible with Option A as an additive flag later, so choosing Option A
first does not foreclose Option C.

## Operativity and warrant

- **Consumers:** human operators, agents validating multi-file edits after
  `cp-skill-write` or `cp-skill-connect` follow-up passes, and pre-commit or
  helper scripts.
- **Channel and force:** `src/commonplace/cli/validate_notes.py` (executable
  CLI contract) plus documentation updates in [commands reference](../commands.md)
  and relevant skills/instructions if they invoke batch validation.
- **Oracle warrant:** unchanged. Every check executed is an existing
  deterministic check inside `ValidationRun`; this proposal changes invocation
  batching and reporting only, not check semantics.

## Feasibility and commitment scope

- **Feasibility:** high. `run_validation` already evaluates `tuple[Path, ...]`
  in one `ValidationRun`, sharing parsed frontmatter, type resolution, tag
  heads, and source indexes across files (`src/commonplace/lib/validation.py`).
  The main work is CLI argument handling, target validation/deduplication, and
  `ValidationReport` formatting (`target`, `scope`, `details_command`).
- **Reversibility:** high for Option A if `commonplace.validation.v1` stays
  backward-compatible for single-target callers. A breaking change to `--json`
  (`v2`) would raise coordination cost across tests and any scripts consuming
  `commonplace.validation.v1`.

## Free choices

1. **JSON schema representation (`commonplace.validation.v1` vs. `v2`).**
   For a multi-target run, `ValidationReport` currently models scalar
   `target: str`, `scope: str`, and `details_command: str`. Options:
   - keep `v1` compatible by setting `target` to a summary label (e.g.,
     `"<N> targets"` or space-joined paths), keeping `analysed_artifacts` as
     the exact per-file list, formatting `details_command` with all targets via
     `shlex.join`, and optionally adding `targets: list[str]`; or
   - bump to `commonplace.validation.v2` with `targets: list[str]`.
2. **Missing-target handling.** When one of $N$ supplied paths does not exist
   or fails resolution, either fail fast before running `ValidationRun` (exit
   1, matching current single-target resolution) or report all unresolved paths
   together before exiting.
3. **Directory artifacts in multi-target lists.** Whether a multi-target file
   list also admits explicit directory artifacts (directories containing
   `ARTIFACT.yaml`) alongside regular `.md` files, or restricts multi-target
   arguments strictly to files first.
4. **Whether Option C (`--files-from`) ships together or stays deferred** until
   a caller actually needs pipeline/large-batch validation.

## Adoption criteria

Adopt Option A (with the free choices above settled in an implementing commit
or ADR) when multi-file validation friction recurs across authoring/connect
sessions and the operator approves the JSON/compact report shape. Revisit
Option B only if an actual workflow needs multi-collection batch checks in one
run; revisit Option C if a caller needs piped file lists from `git diff` or
hits shell argument limits.

---

Relevant Notes:

- [Commands reference](../commands.md) — see-also: documents the current single-target `commonplace-validate` CLI contract and `commonplace.validation.v1` output
- [Validation contract](../validation-contract.md) — see-also: defines the check domains and file-versus-collection scoping that this proposal preserves
