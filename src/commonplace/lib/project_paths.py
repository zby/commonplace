"""Shared path conventions for a commonplace project."""

from __future__ import annotations

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
        for path in boundary.rglob("COLLECTION.md")
        if not any(part.startswith(".") or part == "types" for part in path.relative_to(boundary).parts)
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
        for path in collection.rglob("*.md")
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
        for path in resolved.rglob("*.md")
        if not is_nested_git_repo(path, resolved)
    )


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
            raise FileNotFoundError(f"Note must live under {boundary}: {repo_candidate}")
        return repo_candidate

    name = arg if arg.endswith(".md") else f"{arg}.md"
    matches = sorted(
        path.resolve()
        for path in list_kb_note_paths(root)
        if path.name == name
    )
    if not matches:
        matches = sorted(
            path.resolve()
            for path in list_kb_note_paths(root)
            if path.stem == arg
        )

    if not matches:
        raise FileNotFoundError(f"No matching note found for: {arg}")
    if len(matches) > 1:
        formatted = "\n".join(str(path.relative_to(root)) for path in matches)
        raise FileNotFoundError(f"Multiple matching notes found:\n{formatted}")
    return matches[0]
