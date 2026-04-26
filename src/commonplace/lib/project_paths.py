"""Shared path conventions for a commonplace project."""

from __future__ import annotations

import os
import subprocess
from collections.abc import Iterator
from functools import lru_cache
from pathlib import Path


def kb_root(root: Path) -> Path:
    """Return the KB root for a project root."""
    return root / "kb"


def collection_dirs(root: Path) -> list[Path]:
    """Return content collection directories under kb/.

    A collection is identified by a local COLLECTION.md file. This lets
    installed library collections live under kb/commonplace/<collection>/ while
    support directories such as kb/reports/ are ignored unless they explicitly
    opt in as collections.
    """
    boundary = kb_root(root)
    if not boundary.is_dir():
        raise FileNotFoundError(f"KB root does not exist: {boundary}")
    return sorted(
        path.parent
        for path in iter_unignored_markdown_files(boundary, ignore_root=root)
        if not any(
            part.startswith(".") or part == "types"
            for part in path.relative_to(boundary).parts
        )
        and path.name == "COLLECTION.md"
    )


def collection_for_path(path: Path, root: Path) -> Path:
    """Return the nearest COLLECTION.md-bearing directory containing path."""
    boundary = kb_root(root).resolve()
    resolved = path.resolve()
    try:
        resolved.relative_to(boundary)
    except ValueError as exc:
        raise ValueError(f"Path is not under {boundary}: {path}") from exc

    current = resolved if resolved.is_dir() else resolved.parent
    while current != boundary and boundary in current.parents:
        if (current / "COLLECTION.md").is_file():
            return current
        current = current.parent
    raise ValueError(f"Path is not inside a KB collection: {path}")


def is_nested_git_repo(path: Path, boundary: Path) -> bool:
    """Return True when path lives inside a nested git repository under boundary."""
    resolved_boundary = boundary.resolve()
    current = path.resolve().parent
    while current != resolved_boundary and resolved_boundary in current.parents:
        if (current / ".git").exists():
            return True
        current = current.parent
    return False


def is_type_definition_content(path: Path, boundary: Path) -> bool:
    """Return True when path is under a types/ directory beneath boundary."""
    try:
        rel = path.relative_to(boundary)
    except ValueError:
        return False
    return "types" in rel.parent.parts


def is_replaced_archive(path: Path) -> bool:
    """Return True when path is a `.replaced.*.md` archive of a superseded note.

    Replaced archives are frozen snapshots whose links are not maintained as
    referenced notes get renamed; directory sweeps skip them so link-health
    warnings against decayed targets do not accumulate. Direct-path validation
    of a single archive still runs normally.
    """
    return ".replaced." in path.name


def is_collection_metadata(path: Path) -> bool:
    """Return True for collection control files that are not collection content."""
    return path.name == "COLLECTION.md"


def is_collection_dir(path: Path) -> bool:
    """Return True when path is a collection root."""
    return path.is_dir() and (path / "COLLECTION.md").is_file()


def list_collection_note_paths(collection: Path) -> list[Path]:
    """Return markdown note paths under a collection, excluding nested repos,
    types, and replaced archives."""
    if not collection.is_dir():
        raise FileNotFoundError(f"Collection directory does not exist: {collection}")
    if not is_collection_dir(collection):
        raise ValueError(f"Directory is not a KB collection: {collection}")
    return sorted(
        path
        for path in iter_unignored_markdown_files(collection)
        if not is_nested_git_repo(path, collection)
        and not is_type_definition_content(path, collection)
        and not is_collection_metadata(path)
        and not is_replaced_archive(path)
    )


def list_kb_note_paths(root: Path) -> list[Path]:
    """Return markdown note paths under all KB content collections."""
    return [
        path
        for collection in collection_dirs(root)
        for path in list_collection_note_paths(collection)
    ]


def list_type_spec_paths(root: Path) -> list[Path]:
    """Return first-class type-spec markdown paths under kb/**/types/."""
    boundary = kb_root(root)
    if not boundary.is_dir():
        return []
    return sorted(
        path
        for path in boundary.glob("**/types/*.md")
        if not path.name.endswith(".template.md")
        and not path.name.endswith(".instructions.md")
        and path.name != "text.md"
    )


def list_notes_collection_paths(root: Path) -> list[Path]:
    """Return markdown note paths under kb/notes only."""
    return list_collection_note_paths(kb_root(root) / "notes")


def find_repo_markdown_files(root: Path) -> list[Path]:
    """Return markdown files under a repository, excluding nested git repositories."""
    resolved = root.resolve()
    return sorted(
        path
        for path in iter_unignored_markdown_files(resolved, ignore_root=resolved)
        if not is_nested_git_repo(path, resolved)
    )


@lru_cache(maxsize=None)
def is_git_ignored(path: Path, root: Path | None = None) -> bool:
    """Return True when Git ignore rules exclude `path`.

    Git is the source of truth because .gitignore syntax is richer than the
    small subset this package should own. Outside a Git worktree, paths are
    treated as visible so commonplace can still operate in plain directories.
    """
    check_root = (root or path.parent).resolve()
    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(check_root),
                "check-ignore",
                "--quiet",
                "--no-index",
                "--",
                str(path.resolve()),
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except (FileNotFoundError, OSError):
        return False
    return result.returncode == 0


def walk_unignored(
    root: Path,
    *,
    ignore_root: Path | None = None,
) -> Iterator[tuple[Path, list[str], list[str]]]:
    """Yield an os.walk stream with gitignored directories pruned."""
    resolved_root = root.resolve()
    resolved_ignore_root = (ignore_root or resolved_root).resolve()
    if is_git_ignored(resolved_root, resolved_ignore_root):
        return

    for current, dirnames, filenames in os.walk(resolved_root):
        current_path = Path(current)
        dirnames[:] = sorted(
            dirname
            for dirname in dirnames
            if not is_git_ignored(current_path / dirname, resolved_ignore_root)
        )
        yield current_path, dirnames, sorted(filenames)


def iter_unignored_markdown_files(
    root: Path,
    *,
    ignore_root: Path | None = None,
) -> Iterator[Path]:
    """Yield visible markdown files below `root`, pruning gitignored directories."""
    resolved_ignore_root = (ignore_root or root).resolve()
    for current, _dirnames, filenames in walk_unignored(
        root, ignore_root=resolved_ignore_root
    ):
        for filename in filenames:
            path = current / filename
            if path.suffix == ".md" and not is_git_ignored(path, resolved_ignore_root):
                yield path


def resolve_note(arg: str, root: Path) -> Path:
    """Resolve a note argument (path, filename, or stem) to one markdown file under kb/."""
    boundary = kb_root(root).resolve()
    if not boundary.is_dir():
        raise FileNotFoundError(f"KB root does not exist: {boundary}")

    candidate = Path(arg)
    if candidate.is_absolute() and candidate.is_file():
        resolved = candidate.resolve()
        if boundary not in resolved.parents:
            raise FileNotFoundError(f"Note must live under {boundary}: {resolved}")
        return resolved

    repo_candidate = (root / arg).resolve()
    if repo_candidate.is_file():
        if boundary not in repo_candidate.parents:
            raise FileNotFoundError(
                f"Note must live under {boundary}: {repo_candidate}"
            )
        return repo_candidate

    name = arg if arg.endswith(".md") else f"{arg}.md"
    matches = sorted(
        path.resolve() for path in list_kb_note_paths(root) if path.name == name
    )
    if not matches:
        matches = sorted(
            path.resolve() for path in list_kb_note_paths(root) if path.stem == arg
        )

    if not matches:
        raise FileNotFoundError(f"No matching note found for: {arg}")
    if len(matches) > 1:
        formatted = "\n".join(str(path.relative_to(root)) for path in matches)
        raise FileNotFoundError(f"Multiple matching notes found:\n{formatted}")
    return matches[0]
