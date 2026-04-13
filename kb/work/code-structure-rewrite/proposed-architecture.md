# Proposed Architecture

Companion to [framing.md](./framing.md) — the analysis of current problems and what works well lives there.

## Guiding principles

1. **No module-level path globals.** Every path-dependent function receives `root: Path` explicitly. Only CLI `main()` functions call `Path.cwd()`.
2. **Deduplicate by extraction, not abstraction.** Shared functions move to shared modules. No new classes unless the data genuinely needs coupling.
3. **CLI is a shell.** Argument parsing, one call to a library function, output formatting. Library logic that currently lives in CLI modules gets extracted.
4. **Review is downstream.** Core lib never imports review. Relocation exposes a hook protocol; the CLI wires in the review hook.
5. **No shared link graph.** The three consumers (validation orphan check, promotion scoring, relocation link rewriting) run as separate CLI commands, never in the same process. Each already does a targeted scan appropriate to its needs. A shared precomputed graph would add complexity without saving work.

## Package layout

```
commonplace/
  lib/
    frontmatter.py       # (unchanged — clean)
    naming.py            # (unchanged — clean)
    note_parser.py       # (unchanged — clean)
    project_paths.py     # NEW: shared path conventions and discovery
    type_resolver.py     # Refactored: receives root as argument, no global, collection-scoped only
    validation.py        # Refactored: uses project_paths
    relocation.py        # Refactored: uses project_paths, hook protocol
    index_directory.py   # NEW: extracted from generate_notes_index
    index_generated.py   # NEW: extracted from sync_generated_index
    snapshot.py          # NEW: shared dedup and slug logic for snapshots
  cli/
    init_project.py      # (unchanged — self-contained)
    validate_notes.py    # Thinned: formatting only, calls lib.validation
    generate_notes_index.py  # Thinned: calls lib.index_directory
    sync_generated_index.py  # Thinned: calls lib.index_generated
    refresh_indexes.py   # Calls lib indexing modules directly (not other CLI modules)
    relocate_note.py     # (already thin)
    relocate_directory.py # (already thin)
    promotion_candidates.py  # Thinned: calls lib functions, uses project_paths
    github_snapshot.py   # Uses lib.snapshot for shared logic
    x_snapshot.py        # Uses lib.snapshot for shared logic
    review/              # (unchanged — separate subsystem)
  review/                # (unchanged — separate subsystem)
  scaffold/              # (unchanged)
```

This is conservative — same package structure, no new sub-packages, no new abstraction layers. The changes are: one new module (`project_paths`), two focused indexing extractions, one small shared module (`snapshot`), and refactoring existing modules to take `root` arguments.

## `project_paths` — the central addition

A module of pure functions that encode the path conventions currently scattered across every command.

```python
"""Shared path conventions for a commonplace project."""

from pathlib import Path


def kb_root(root: Path) -> Path:
    return root / "kb"


def collection_dirs(root: Path) -> list[Path]:
    """Top-level content collections under kb/ — notes, work, reports, tasks, etc."""
    kr = kb_root(root)
    return sorted(
        p for p in kr.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name != "types"
    )


def is_nested_git_repo(path: Path, boundary: Path) -> bool:
    """True if path lives inside a nested .git directory under boundary."""
    current = path.parent
    while current != boundary and boundary in current.parents:
        if (current / ".git").exists():
            return True
        current = current.parent
    return False


def list_collection_note_paths(collection: Path) -> list[Path]:
    """All note .md files under a collection, excluding nested repos and type dirs."""
    return sorted(
        p for p in collection.rglob("*.md")
        if not is_nested_git_repo(p, collection)
        and "types" not in p.relative_to(collection).parent.parts
    )


def list_kb_note_paths(root: Path) -> list[Path]:
    """All note .md files under kb/ collections."""
    return [
        path
        for collection in collection_dirs(root)
        for path in list_collection_note_paths(collection)
    ]


def resolve_note(arg: str, root: Path) -> Path:
    """Resolve a note argument (path, name, or slug) to a single file.
    
    Currently duplicated in relocation.py and validate_notes.py.
    """
    ...


def collection_for_path(path: Path, root: Path) -> Path:
    """Return the collection root for a file path.
    
    Currently in sync_generated_index.py.
    """
    ...
```

Behavioral decision: `collection_dirs(root)` treats every top-level `kb/<name>/` directory as a content collection except reserved `kb/types/` and hidden directories. That means `kb/work/`, `kb/reports/`, and `kb/tasks/` are collections, while `kb/work/<workshop>/` directories are areas inside the `work` collection, not separate type scopes. `list_kb_note_paths(root)` means all structured markdown documents under these `kb/*` collections, not only files under `kb/notes`. The current `commonplace-validate-notes all` behavior is narrower: it scans `kb/notes`. Keep that behavior during the first extraction by adding a `list_notes_collection_paths(root)` wrapper or by passing `kb_root(root) / "notes"` to `list_collection_note_paths()`. Widening validation to all collections should be a separate explicit behavior change with its own tests.

This replaces:
- `WORKSPACE_ROOT` global in type_resolver.py
- `KB_ROOT` global in sync_generated_index.py
- `NOTES_DIR` global in promotion_candidates.py
- `is_nested_git_repo_content()` in both validation.py and relocation.py
- `resolve_note()` in both relocation.py and validate_notes.py
- `collection_for_path()` in sync_generated_index.py
- `list_kb_note_paths()` in validation.py, via the collection-scoped primitive
- `find_repo_markdown_files()` in relocation.py

## Indexing — extracted from CLI

Extract the library logic currently embedded in index CLI modules into two focused modules:

- `lib/index_directory.py` — directory listing generation currently in `generate_notes_index.py`
- `lib/index_generated.py` — generated-tail/tag syncing currently in `sync_generated_index.py`

These operations share path conventions (`collection_for_path()`, collection discovery) and frontmatter parsing, but not enough core behavior to justify one broad `indexing.py` module. Shared path behavior should live in `project_paths`; shared parsing should keep using `frontmatter`/`note_parser`.

`refresh_indexes.py` currently imports from `cli.generate_notes_index` and `cli.sync_generated_index` — after extraction it imports from `lib.index_directory` and `lib.index_generated` like any other command.

## Review decoupling via hooks

Current: `relocation.py` imports `review.review_db` and `review.review_metadata` directly.

Proposed: relocation accepts an optional list of hook callables over a batch of note path moves. This covers both `relocate_note` (one move) and `relocate_directory` (many markdown file moves).

```python
from dataclasses import dataclass
from pathlib import Path
from collections.abc import Sequence
from typing import Protocol


@dataclass(frozen=True)
class NotePathMove:
    old_path: Path
    new_path: Path


class RelocationHook(Protocol):
    def plan(self, *, root: Path, moves: Sequence[NotePathMove]) -> object:
        """Return an opaque plan object, or None."""
        ...
    
    def execute(self, plan: object) -> None:
        """Execute the planned updates."""
        ...
    
    def describe(self, plan: object) -> list[str]:
        """Human-readable description for dry-run output."""
        ...


def relocate_note(
    *,
    root: Path,
    note_arg: str,
    new_name: str | None = None,
    dest_path: str | None = None,
    apply: bool = False,
    hooks: list[RelocationHook] | None = None,
) -> int:
    ...


def relocate_directory(
    *,
    root: Path,
    source_arg: str,
    dest_path: str,
    redirect_from: str | None = None,
    redirect_to: str | None = None,
    apply: bool = False,
    hooks: list[RelocationHook] | None = None,
) -> int:
    ...
```

The CLI wires in the review hook:

```python
from commonplace.review.relocation_hook import ReviewRelocationHook

hooks = [ReviewRelocationHook()] if review_db_exists() else []
relocate_note(..., hooks=hooks)
relocate_directory(..., hooks=hooks)
```

Core lib never imports review. The dependency inverts. The core relocation code still owns filesystem moves, markdown link rewriting, and MkDocs redirect updates; the hook owns review-specific export metadata rewrites and review DB rekeys.

Hook lifecycle:

1. Core relocation resolves and validates all source/destination paths and builds a complete `Sequence[NotePathMove]`.
2. Core calls `hook.plan(root=root, moves=moves)` before any filesystem mutation. The hook performs review-specific preflight checks, such as destination export-directory collisions, and returns an opaque plan. A hook may return `None` when it has no work.
3. Core calls `hook.describe(plan)` while printing dry-run/apply output. This replaces the current inline "Review exports" and "Review DB updates" reporting.
4. On dry run, core stops after reporting. No hook execute method runs.
5. On apply, core performs the note/directory move and core markdown/MkDocs writes first, then calls `hook.execute(plan)` for review export moves, review metadata rewrites, and review DB rekeys.
6. If a hook preflight fails, relocation aborts before any core writes.

The review hook should live under `commonplace.review` (for example `commonplace.review.relocation_hook`) so the review dependency remains downstream. The non-review CLIs (`relocate_note.py` and `relocate_directory.py`) are allowed to import this hook because CLI composition is the boundary between subsystems.

## Type resolver refactoring

Minimal change — remove the global, pass `root` explicitly, and simplify lookup to collection scope plus global fallback:

```python
# Before
WORKSPACE_ROOT = Path.cwd().resolve()

def resolve_type(file_path, frontmatter, *, repo_root=None):
    workspace_root = repo_root.resolve() if repo_root else WORKSPACE_ROOT
    ...

# After — just remove the global and the default
def resolve_type(file_path, frontmatter, *, repo_root):
    ...
```

Callers already pass `repo_root` in most places. The few that don't get updated to pass it.

Scope decision: a file at `kb/<collection>/.../foo.md` resolves `type: X` by looking for `kb/<collection>/types/X.schema.yaml` first, then `kb/types/X.schema.yaml`. There is no deeper per-directory override in the first implementation. In particular, `kb/work/<workshop>/types/` is not a resolver scope; workshop directories are areas inside the `work` collection and should use `kb/work/types/` for collection-local types.

## Snapshot dedup extraction

`github_snapshot.py` and `x_snapshot.py` both have nearly identical `_dedup_existing_snapshot()` functions. Extract to `lib/snapshot.py`:

```python
def dedup_existing_snapshot(out_dir: Path, source_url: str) -> Path | None:
    """Check if a snapshot for this source URL already exists."""
    marker = f"source: {source_url}"
    for existing in out_dir.glob("*.md"):
        try:
            header = existing.read_text(encoding="utf-8")[:1000]
        except OSError:
            continue
        if marker in header:
            return existing
    return None
```

Small but removes the duplication and establishes a shared snapshot utilities module if more shared logic emerges.

## What this fixes

| Problem | Fix |
|---------|-----|
| Process globals (3 modules) | `project_paths` functions take `root`; type_resolver takes `repo_root` always |
| Duplicated `is_nested_git_repo_content` | One copy in `project_paths` |
| Duplicated `get_title` | CLI modules call `note_parser.extract_title()` |
| Duplicated `_dedup_existing_snapshot` | One copy in `lib/snapshot` |
| Duplicated link graph traversal | Each consumer keeps its own targeted scan (no shared graph needed — they run in separate processes) |
| lib imports review | Hook protocol; CLI wires in the review hook |
| CLI doing library work | Index generation modules extracted; `refresh_indexes` calls lib not cli |

## What stays the same

- `frontmatter.py`, `naming.py`, `note_parser.py` — already clean
- `init_project.py` — self-contained, creates rather than operates on a workspace
- `ParsedDocument` dataclass — good model
- Validation check types (title/slug, links, schema) — clear separation
- Relocation dry-run pattern — good UX, now formalized via hook protocol
- Type resolver's collection-scoped discovery algorithm — right design, just needs the global removed and the workshop-local override dropped

## Implementation order

0. **Readiness and test contract.** Before touching runtime code, make the behavioral contract explicit in the tests and notes:
   - Record the baseline: `uv run pytest -q` currently passes (`199 passed` on 2026-04-13).
   - Add/update tests for `project_paths`: collection discovery, nested repo exclusion, type-directory exclusion, note resolution, and missing-directory policy.
   - Update the type resolver tests for the intentional behavior change: `kb/work/<workshop>/types/` is no longer a resolver scope; workshop-local type definitions should move to the collection scope (`kb/work/types/`) if they become structural contracts.
   - Preserve current CLI behavior in tests while extracting library logic: `commonplace-validate-notes all` still scans `kb/notes`; sync/refresh index output remains stable; promotion candidates still write `kb/reports/promotion-candidates.md`.
   - Add focused tests for the extraction seams: `lib/index_directory`, `lib/index_generated`, `lib/snapshot.dedup_existing_snapshot`, and relocation hooks.
   - Specify relocation hook failure semantics before implementation: hook preflight failures abort before core writes; hook execute failures after core moves are reported as partial failures and must leave enough information for manual recovery.
1. **Path extraction.** Add `lib/project_paths.py`; update `type_resolver.py`, `validation.py`, `sync_generated_index.py`, and `promotion_candidates.py` to receive `root` explicitly while preserving existing command behavior. Treat all top-level `kb/` directories except reserved `kb/types/` and hidden dirs as collections.
2. **Index extraction.** Add `lib/index_directory.py` and `lib/index_generated.py`; thin `generate_notes_index.py` and `sync_generated_index.py`; update `refresh_indexes.py` to import only library modules.
3. **Snapshot extraction.** Add `lib/snapshot.py`; replace the duplicated `_dedup_existing_snapshot()` functions in `github_snapshot.py` and `x_snapshot.py`.
4. **Relocation decoupling.** Add the relocation hook protocol and review hook implementation; update both `relocate_note` and `relocate_directory`; remove direct `commonplace.review` imports from `commonplace.lib.relocation`.

Relocation should be the last slice because it has the largest behavioral surface and currently mixes core file moves with review export and DB updates.

## Open questions

1. **Missing-directory policy.** Resolved: pure path constructors such as `kb_root(root)` do not raise. Discovery functions raise when the expected boundary is missing (`collection_dirs(root)` if `root/kb` is missing; `list_collection_note_paths(collection)` if the collection is missing), and return `[]` only when the boundary exists but has no matching note files. Resolver functions raise on no match or ambiguous match.

2. **Indexing module shape.** Resolved: split the extraction into `lib/index_directory.py` for directory listing generation and `lib/index_generated.py` for generated-tail/tag syncing. Shared path behavior belongs in `project_paths`; shared parsing stays in existing parser/frontmatter modules.

3. **Hook protocol complexity.** Resolved: keep the plan/execute/describe protocol, but make it operate on a batch of `NotePathMove` records. This matches the existing dry-run behavior and supports both single-note relocation and directory relocation without adding review imports back into core relocation.

4. **Discovery primitive naming.** Resolved: make `list_collection_note_paths(collection)` the primary primitive and keep `list_kb_note_paths(root)` as a wrapper over all collections. In this KB, "note" is the base structured document type across collections, not only files under `kb/notes/`. `kb/types/` is the reserved global type layer and is not a collection. Preserve the current validation command's `kb/notes` scope until a separate behavior-change patch widens it.

5. **Workshop type scope.** Resolved: simplify `kb/work/` into an ordinary collection. Workshop directories under `kb/work/<workshop>/` are areas inside that collection, not independent resolver scopes. Use `kb/work/types/` for work-local type definitions and `kb/types/` for global fallback.
