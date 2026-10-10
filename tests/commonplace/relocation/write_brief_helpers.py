"""Shared fixtures for write-brief sidecar pairs (ADR 092)."""

from __future__ import annotations

import shutil
from pathlib import Path

from commonplace.lib import validation

REPO_ROOT = Path(__file__).resolve().parents[3]
TYPE_FILES = (
    "kb/types/note.md",
    "kb/types/note.schema.yaml",
    "kb/types/note-base.schema.yaml",
    "kb/types/write-brief.md",
    "kb/types/write-brief.schema.yaml",
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def install_brief_types(repo_root: Path) -> None:
    """Copy the committed note and write-brief types into a temporary KB."""
    for rel_path in TYPE_FILES:
        dest = repo_root / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / rel_path, dest)


def write_pair(directory: Path, stem: str, *, pointer: str | None = None) -> tuple[Path, Path]:
    """Write a note declaring a brief and its sidecar; return both paths."""
    value = f"{stem}.brief.md" if pointer is None else pointer
    note = write(
        directory / f"{stem}.md",
        f"""---
description: Target note whose commission is carried by a write-brief sidecar next to it
type: types/note.md
brief: {value}
---

# Target

Body.
""",
    )
    brief = write(
        directory / f"{stem}.brief.md",
        f"""---
type: types/write-brief.md
description: "Commission for {stem}: keep what its readers rely on"
---

# Brief: {stem}

## Must keep

- The qualification a later note relies on, see [target](./{stem}.md).
""",
    )
    return note, brief


def pair_fails(repo_root: Path, note: Path, brief: Path) -> list[str]:
    """All validation failures of a pair, after confirming both sides resolved."""
    note_results = validation.validate_note(note, repo_root=repo_root)
    brief_results = validation.validate_note(brief, repo_root=repo_root)
    assert brief_results.note_type == "write-brief"
    assert any("resolves to a write brief" in item for item in note_results.passes)
    return note_results.fails + brief_results.fails
