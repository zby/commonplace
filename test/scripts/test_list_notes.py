from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

import pytest


LIST_NOTES_SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "list_notes.py"
SPEC = importlib.util.spec_from_file_location("list_notes", LIST_NOTES_SCRIPT)
assert SPEC and SPEC.loader
list_notes = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = list_notes
SPEC.loader.exec_module(list_notes)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def note(path: Path, title: str = "Test note") -> Path:
    return write(
        path,
        f"""---
description: Test note with enough description text to count as a reviewable note in batch workflows
type: note
traits: []
status: current
---

# {title}
""",
    )


def test_list_reviewable_notes_only_returns_top_level_frontmatter_non_indexes(
    tmp_path: Path,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    kept = note(notes_root / "kept.md", "Kept")
    note(notes_root / "index.md", "Index")
    note(notes_root / "topic-index.md", "Topic index")
    write(notes_root / "raw.md", "# Raw capture\n")
    note(notes_root / "nested" / "ignored.md", "Nested")

    discovered = list_notes.list_reviewable_notes(notes_root)

    assert discovered == [kept]


def test_needs_review_when_review_is_missing(tmp_path: Path) -> None:
    note_path = note(tmp_path / "kb" / "notes" / "fresh.md", "Fresh")

    assert list_notes.needs_review(
        note_path,
        "prose-review",
        tmp_path / "reviews",
    )


def test_needs_review_when_note_is_newer_than_review(tmp_path: Path) -> None:
    note_path = note(tmp_path / "kb" / "notes" / "fresh.md", "Fresh")
    review_path = write(
        tmp_path / "reviews" / "fresh.prose-review.md",
        "# Existing review\n",
    )

    review_ts = 1_700_000_000
    note_ts = review_ts + 60
    os.utime(review_path, (review_ts, review_ts))
    os.utime(note_path, (note_ts, note_ts))

    assert list_notes.needs_review(
        note_path,
        "prose-review",
        tmp_path / "reviews",
    )


def test_skips_note_when_review_is_up_to_date(tmp_path: Path) -> None:
    note_path = note(tmp_path / "kb" / "notes" / "stable.md", "Stable")
    review_path = write(
        tmp_path / "reviews" / "stable.semantic-review.md",
        "# Existing review\n",
    )

    note_ts = 1_700_000_000
    review_ts = note_ts + 60
    os.utime(note_path, (note_ts, note_ts))
    os.utime(review_path, (review_ts, review_ts))

    assert not list_notes.needs_review(
        note_path,
        "semantic-review",
        tmp_path / "reviews",
    )


def test_main_requires_review_type_or_all(capsys: pytest.CaptureFixture[str]) -> None:
    old_argv = sys.argv
    sys.argv = ["list_notes.py"]
    try:
        with pytest.raises(SystemExit) as excinfo:
            list_notes.main()
    finally:
        sys.argv = old_argv

    captured = capsys.readouterr()
    assert excinfo.value.code == 2
    assert "provide a review type or pass --all" in captured.err
