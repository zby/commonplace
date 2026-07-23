from __future__ import annotations

from pathlib import Path

from commonplace.lib.validation import validate_note


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def setup_repo(tmp_path: Path) -> Path:
    # The validator resolves global and collection-local type specs from the
    # repo root, so the fixture repo needs the real specs copied in.
    repo_root = Path(__file__).resolve().parents[3]
    real_types = repo_root / "kb" / "types"
    for name in (
        "note.md",
        "note.schema.yaml",
        "note-base.schema.yaml",
        "type-spec.md",
        "type-spec.schema.yaml",
    ):
        write(tmp_path / "kb" / "types" / name, (real_types / name).read_text(encoding="utf-8"))
    article_types = repo_root / "kb" / "articles" / "types"
    for name in ("article.md", "article.schema.yaml"):
        write(
            tmp_path / "kb" / "articles" / "types" / name,
            (article_types / name).read_text(encoding="utf-8"),
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


def article(path: Path, *, source_notes: list[str] | None = None) -> Path:
    lineage = ""
    if source_notes is not None:
        rendered = "\n".join(f"  - {note}" for note in source_notes)
        lineage = f"source_notes:\n{rendered}\n"
    return write(
        path,
        f"""---
description: "an outward-facing article used by the validation tests of the article type"
type: kb/articles/types/article.md
{lineage}---

# A test article

Reader-facing prose.
""",
    )


def test_minimal_article_passes(tmp_path: Path) -> None:
    # The article type is deliberately nearly empty: description and type
    # alone make a valid article; constraints accrue with collected failure
    # modes.
    articles = setup_repo(tmp_path)
    path = article(articles / "test-article.md")
    results = validate_note(path, repo_root=tmp_path)
    assert not results.fails


def test_resolving_source_notes_pass(tmp_path: Path) -> None:
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
