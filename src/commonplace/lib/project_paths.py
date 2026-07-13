"""Shared path conventions for a Commonplace project.

Visibility is package-owned: hidden entries (dot-prefixed) and nested git
repositories are invisible to every markdown walk, and repository-wide walks
additionally skip common build/vendor artifact trees. Git is never consulted;
gitignore rules do not affect what the tools see.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path


# Directory names pruned from repository-wide markdown walks: build and vendor
# trees that are never knowledge content. Collection walks under kb/ do not
# apply these; they only matter when sweeping the whole repository.
REPO_ARTIFACT_DIR_NAMES = frozenset(
    {"build", "dist", "node_modules", "site", "tmp", "__pycache__"}
)


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
    boundary = kb_root(root).resolve()
    if not boundary.is_dir():
        raise FileNotFoundError(f"KB root does not exist: {boundary}")
    return sorted(
        path.parent
        for path in iter_visible_markdown_files(boundary)
        if path.name == "COLLECTION.md"
        and "types" not in path.relative_to(boundary).parts
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


def is_type_definition_content(path: Path, boundary: Path) -> bool:
    """Return True when path is under a types/ directory beneath boundary."""
    try:
        rel = path.relative_to(boundary)
    except ValueError:
        return False
    return "types" in rel.parent.parts


def is_type_support_content(path: Path, boundary: Path) -> bool:
    """Return True for non-artifact support files inside a types/ directory."""
    return is_type_definition_content(path, boundary) and (
        path.name.endswith(".template.md")
        or path.name.endswith(".instructions.md")
        or path.name == "text.md"
    )


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
    """Return markdown note paths under a collection, excluding collection
    metadata, replaced archives, and legacy type support files."""
    if not collection.is_dir():
        raise FileNotFoundError(f"Collection directory does not exist: {collection}")
    if not is_collection_dir(collection):
        raise ValueError(f"Directory is not a KB collection: {collection}")
    return sorted(
        path
        for path in iter_visible_markdown_files(collection)
        if not is_collection_metadata(path)
        and not is_replaced_archive(path)
        and not is_type_support_content(path, collection)
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
    """Return markdown files under a repository.

    Excludes hidden entries, nested git repositories, and build/vendor
    artifact trees (`REPO_ARTIFACT_DIR_NAMES`).
    """
    return sorted(
        iter_visible_markdown_files(root, exclude_dir_names=REPO_ARTIFACT_DIR_NAMES)
    )


def walk_visible(
    root: Path,
    *,
    exclude_dir_names: frozenset[str] = frozenset(),
) -> Iterator[tuple[Path, list[str], list[str]]]:
    """Yield an os.walk stream over visible entries.

    Prunes hidden directories (dot-prefixed), nested git repositories, and any
    directory whose name is in `exclude_dir_names`.
    """
    for current, dirnames, filenames in os.walk(root.resolve()):
        current_path = Path(current)
        dirnames[:] = sorted(
            dirname
            for dirname in dirnames
            if not dirname.startswith(".")
            and dirname not in exclude_dir_names
            and not (current_path / dirname / ".git").exists()
        )
        yield current_path, dirnames, sorted(filenames)


def iter_visible_markdown_files(
    root: Path,
    *,
    exclude_dir_names: frozenset[str] = frozenset(),
) -> Iterator[Path]:
    """Yield visible markdown files below `root` (see `walk_visible`)."""
    for current, _dirnames, filenames in walk_visible(
        root, exclude_dir_names=exclude_dir_names
    ):
        for filename in filenames:
            if filename.endswith(".md") and not filename.startswith("."):
                yield current / filename


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
