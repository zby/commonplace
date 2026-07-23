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


def article(
    path: Path,
    *,
    status: str = "draft",
    source_notes: list[str] | None = None,
    extra: str = "",
) -> Path:
    notes = source_notes if source_notes is not None else ["kb/notes/existing-note.md"]
    rendered_notes = "\n".join(f"  - {note}" for note in notes)
    return write(
        path,
        f"""---
description: "an outward-facing article used by the validation tests of the article type"
type: kb/articles/types/article.md
status: {status}
byline: Test Author
source_notes:
{rendered_notes}
{extra}---

# A test article

Reader-facing prose.
""",
    )


def test_draft_with_resolving_source_notes_passes(tmp_path: Path) -> None:
    articles = setup_repo(tmp_path)
    path = article(articles / "test-article.md")
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


def test_published_without_date_fails_schema(tmp_path: Path) -> None:
    articles = setup_repo(tmp_path)
    path = article(articles / "test-article.md", status="published")
    results = validate_note(path, repo_root=tmp_path)
    assert any("publication date" in f for f in results.fails)


def test_published_with_date_passes(tmp_path: Path) -> None:
    articles = setup_repo(tmp_path)
    path = article(
        articles / "test-article.md",
        status="published",
        extra='published: "2026-07-23"\n',
    )
    results = validate_note(path, repo_root=tmp_path)
    assert not results.fails


def test_superseded_requires_successor(tmp_path: Path) -> None:
    articles = setup_repo(tmp_path)
    path = article(
        articles / "test-article.md",
        status="superseded",
        extra='published: "2026-07-23"\n',
    )
    results = validate_note(path, repo_root=tmp_path)
    assert any("must name its successor" in f for f in results.fails)


def test_missing_byline_fails_schema(tmp_path: Path) -> None:
    articles = setup_repo(tmp_path)
    path = write(
        articles / "test-article.md",
        """---
description: "an outward-facing article used by the validation tests of the article type"
type: kb/articles/types/article.md
status: draft
source_notes:
  - kb/notes/existing-note.md
---

# A test article

Reader-facing prose.
""",
    )
    results = validate_note(path, repo_root=tmp_path)
    assert any("byline" in f for f in results.fails)
