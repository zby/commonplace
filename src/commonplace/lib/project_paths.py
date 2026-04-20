"""Shared path conventions for a commonplace project."""

from __future__ import annotations

from pathlib import Path


def kb_root(root: Path) -> Path:
    """Return the KB root for a project root."""
    return root / "kb"


def collection_dirs(root: Path) -> list[Path]:
    """Return top-level content collection directories under kb/."""
    boundary = kb_root(root)
    if not boundary.is_dir():
        raise FileNotFoundError(f"KB root does not exist: {boundary}")
    return sorted(
        path
        for path in boundary.iterdir()
        if path.is_dir() and not path.name.startswith(".") and path.name != "types"
    )


def collection_for_path(path: Path, root: Path) -> Path:
    """Return the top-level kb/<collection>/ directory containing path."""
    boundary = kb_root(root).resolve()
    try:
        rel = path.resolve().relative_to(boundary)
    except ValueError as exc:
        raise ValueError(f"Path is not under {boundary}: {path}") from exc
    if not rel.parts:
        raise ValueError(f"Path is not inside a KB collection: {path}")
    collection = boundary / rel.parts[0]
    if collection.name == "types" or collection.name.startswith("."):
        raise ValueError(f"Path is not inside a content collection: {path}")
    return collection


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


def list_collection_note_paths(collection: Path) -> list[Path]:
    """Return markdown note paths under a collection, excluding nested repos and types."""
    if not collection.is_dir():
        raise FileNotFoundError(f"Collection directory does not exist: {collection}")
    return sorted(
        path
        for path in collection.rglob("*.md")
        if not is_nested_git_repo(path, collection)
        and not is_type_definition_content(path, collection)
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


def list_kb_validation_paths(root: Path) -> list[Path]:
    """Return KB markdown artifacts validated in batch mode, including type specs."""
    return sorted([*list_kb_note_paths(root), *list_type_spec_paths(root)])


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
