"""Shared test helpers for validator tests."""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# The validator resolves global and collection-local type specs from the repo
# root, so fixture repos need the real specs copied in.
NOTE_TYPE_SPECS = (
    "kb/types/note.md",
    "kb/types/note.schema.yaml",
    "kb/types/note-base.schema.yaml",
    "kb/types/type-spec.md",
    "kb/types/type-spec.schema.yaml",
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def copy_repo_files(root: Path, *relative_paths: str) -> None:
    """Copy real repo files (type specs, schemas) to the same paths under root."""
    for relative_path in relative_paths:
        write(
            root / relative_path,
            (REPO_ROOT / relative_path).read_text(encoding="utf-8"),
        )
