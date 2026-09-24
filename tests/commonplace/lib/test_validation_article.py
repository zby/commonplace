from __future__ import annotations

from pathlib import Path

from commonplace.lib.validation import validate_note
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, copy_repo_files, write


def setup_repo(tmp_path: Path) -> Path:
    copy_repo_files(
        tmp_path,
        *NOTE_TYPE_SPECS,
        "kb/articles/types/article.md",
        "kb/articles/types/article.schema.yaml",
    )
    write(tmp_path / "kb" / "articles" / "COLLECTION.md", "# Articles collection\n")
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    write(
        tmp_path / "kb" / "notes" / "existing-note.md",
        """---
description: an existing source note for article lineage tests
type: kb/types/note.md
---

# Existing note
""",
    )
    return tmp_path / "kb" / "articles"


def article(path: Path, *, source_notes: list[str]) -> Path:
    rendered = "\n".join(f"  - {note}" for note in source_notes)
    return write(
        path,
        f"""---
description: "an outward-facing article used by the validation tests of the article type"
type: kb/articles/types/article.md
source_notes:
{rendered}
---

# A test article

Reader-facing prose.
""",
    )


def test_resolving_source_notes_pass(tmp_path: Path) -> None:
    # The article type is deliberately nearly empty: description, type, and
    # resolving lineage make a valid article.
    articles = setup_repo(tmp_path)
    path = article(
        articles / "test-article.md",
        source_notes=["kb/notes/existing-note.md"],
    )
    results = validate_note(path, repo_root=tmp_path)
    assert not results.fails
    assert any("source_notes: all 1 paths resolve" in p for p in results.passes)


def test_unresolved_source_note_fails(tmp_path: Path) -> None:
    articles = setup_repo(tmp_path)
    path = article(
        articles / "test-article.md",
        source_notes=["kb/notes/existing-note.md", "kb/notes/missing-note.md"],
    )
    results = validate_note(path, repo_root=tmp_path)
    assert any(
        "source_notes" in f and "kb/notes/missing-note.md" in f for f in results.fails
    )
