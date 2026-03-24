from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


review_metadata = load_module("review_metadata", SCRIPTS_DIR / "review_metadata.py")
notes_selector = load_module("notes_selector", SCRIPTS_DIR / "notes_selector.py")
migrate_review_metadata = load_module(
    "migrate_review_metadata",
    SCRIPTS_DIR / "migrate_review_metadata.py",
)
ack_review = load_module("ack_review", SCRIPTS_DIR / "ack_review.py")


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def note(path: Path, title: str = "Test note", body: str = "") -> Path:
    return write(
        path,
        f"""---
description: Test note with enough description text to count as a reviewable note in batch workflows
type: note
traits: []
status: current
---

# {title}
{body}
""",
    )


def init_repo(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.name", "Test User"],
        cwd=path,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=path,
        check=True,
        capture_output=True,
    )


def commit_all(path: Path, message: str) -> str:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=path,
        check=True,
        capture_output=True,
    )
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=path,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def test_list_reviewable_notes_only_returns_top_level_frontmatter_non_indexes(
    tmp_path: Path,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    kept = note(notes_root / "kept.md", "Kept")
    note(notes_root / "index.md", "Index")
    note(notes_root / "topic-index.md", "Topic index")
    write(notes_root / "raw.md", "# Raw capture\n")
    note(notes_root / "nested" / "ignored.md", "Nested")

    discovered = notes_selector.list_reviewable_notes(notes_root)

    assert discovered == [kept]


def test_missing_review_returns_changed_record(tmp_path: Path) -> None:
    note_path = note(tmp_path / "kb" / "notes" / "fresh.md", "Fresh")

    record = notes_selector.build_change_record(
        note_path,
        "prose-review",
        tmp_path / "reviews",
        tmp_path,
    )

    assert record.status == "changed"
    assert record.reason == "missing-review"
    assert record.review_path is None


def test_blob_match_marks_note_unchanged(tmp_path: Path) -> None:
    note_path = note(tmp_path / "kb" / "notes" / "stable.md", "Stable")
    blob_sha = review_metadata.git_blob_sha(note_path)
    review_text = review_metadata.inject_review_metadata(
        """=== PROSE REVIEW: stable.md ===

Checks applied: 8

WARN:
- [Source residue] Example

Overall: 1 warnings, 0 info
===
""",
        review_metadata.ReviewMetadata(
            note_path="kb/notes/stable.md",
            last_full_review_note_sha=blob_sha,
            last_full_review_note_commit="abc123",
            last_full_review_at="2026-03-23T10:00:00+01:00",
            last_accepted_note_sha=blob_sha,
            last_accepted_note_commit="abc123",
            last_accepted_at="2026-03-23T10:00:00+01:00",
            last_acceptance_kind="full-review",
            review_type="prose-review",
        ),
    )
    write(tmp_path / "reviews" / "stable.prose-review.md", review_text)

    record = notes_selector.build_change_record(
        note_path,
        "prose-review",
        tmp_path / "reviews",
        tmp_path,
    )

    assert record.status == "unchanged"
    assert record.reason == "blob-match"


def test_changed_note_returns_diff_summary_from_reviewed_blob(tmp_path: Path) -> None:
    init_repo(tmp_path)
    note_path = note(
        tmp_path / "kb" / "notes" / "changed.md",
        "Changed",
        "\nOriginal body line.\n",
    )
    commit_all(tmp_path, "Add note")
    old_blob_sha = review_metadata.git_blob_sha(note_path)
    review_text = review_metadata.inject_review_metadata(
        """=== PROSE REVIEW: changed.md ===

Checks applied: 8

CLEAN:
- [Pseudo-formalism] Clean.

Overall: CLEAN
===
""",
        review_metadata.ReviewMetadata(
            note_path="kb/notes/changed.md",
            last_full_review_note_sha=old_blob_sha,
            last_full_review_note_commit="review-commit",
            last_full_review_at="2026-03-23T10:00:00+01:00",
            last_accepted_note_sha=old_blob_sha,
            last_accepted_note_commit="review-commit",
            last_accepted_at="2026-03-23T10:00:00+01:00",
            last_acceptance_kind="full-review",
            review_type="prose-review",
        ),
    )
    write(tmp_path / "reviews" / "changed.prose-review.md", review_text)
    note(
        note_path,
        "Changed",
        "\nUpdated body line.\nAnother addition.\n",
    )

    record = notes_selector.build_change_record(
        note_path,
        "prose-review",
        tmp_path / "reviews",
        tmp_path,
    )

    assert record.status == "changed"
    assert record.reason == "content-changed"
    assert record.diff_added_lines == 2
    assert record.diff_removed_lines == 1
    assert "Updated body line." in record.diff


def test_commit_path_metadata_is_resolved_without_crashing(tmp_path: Path) -> None:
    init_repo(tmp_path)
    note_path = note(
        tmp_path / "kb" / "notes" / "history.md",
        "History",
        "\nFirst version.\n",
    )
    first_commit = commit_all(tmp_path, "Add history note")
    review_text = (
        "<!-- REVIEW-METADATA\n"
        "reviewed-path: kb/notes/history.md\n"
        f"reviewed-blob-sha: {first_commit}:kb/notes/history.md\n"
        "reviewed-at: 2026-03-23T10:00:00+01:00\n"
        f"reviewed-commit: {first_commit}\n"
        "review-type: semantic-review\n"
        "-->\n"
        "=== SEMANTIC REVIEW: history.md ===\n\n"
        "Claims identified: 1\n\n"
        "PASS:\n"
        "- [Internal consistency] Clean.\n\n"
        "Overall: CLEAN\n"
        "===\n"
    )
    write(tmp_path / "reviews" / "history.semantic-review.md", review_text)
    note(
        note_path,
        "History",
        "\nSecond version.\n",
    )

    record = notes_selector.build_change_record(
        note_path,
        "semantic-review",
        tmp_path / "reviews",
        tmp_path,
    )

    assert record.status == "changed"
    assert record.reason == "content-changed"
    assert record.accepted_note_sha == review_metadata.blob_sha_at_commit(
        tmp_path,
        first_commit,
        Path("kb/notes/history.md"),
    )
    assert "Second version." in record.diff


def test_migrate_review_file_uses_note_blob_from_review_commit(tmp_path: Path) -> None:
    init_repo(tmp_path)
    note_path = note(
        tmp_path / "kb" / "notes" / "example.md",
        "Example",
        "\nFirst version.\n",
    )
    commit_all(tmp_path, "Add note")
    review_path = write(
        tmp_path / "reviews" / "example.prose-review.md",
        """=== PROSE REVIEW: example.md ===

Checks applied: 8

CLEAN:
- [Pseudo-formalism] Clean.

Overall: CLEAN
===
""",
    )
    review_commit = commit_all(tmp_path, "Add review")
    reviewed_blob_sha = review_metadata.blob_sha_at_commit(
        tmp_path,
        review_commit,
        Path("kb/notes/example.md"),
    )
    note(
        note_path,
        "Example",
        "\nSecond version.\n",
    )
    commit_all(tmp_path, "Update note after review")

    updated, reason = migrate_review_metadata.migrate_review_file(
        review_path,
        tmp_path / "kb" / "notes",
        tmp_path,
    )

    assert updated
    assert reason == "updated"
    migrated_text = review_path.read_text(encoding="utf-8")
    metadata = review_metadata.parse_review_metadata(migrated_text)
    assert metadata is not None
    assert metadata.note_path == "kb/notes/example.md"
    assert metadata.last_full_review_note_commit == review_commit
    assert metadata.last_full_review_note_sha == reviewed_blob_sha
    assert metadata.last_accepted_note_commit == review_commit
    assert metadata.last_accepted_note_sha == reviewed_blob_sha
    assert metadata.last_acceptance_kind == "full-review"
    assert metadata.last_accepted_note_sha != review_metadata.git_blob_sha(note_path)


def test_migrate_review_file_handles_untracked_review_file(tmp_path: Path) -> None:
    init_repo(tmp_path)
    note_path = note(
        tmp_path / "kb" / "notes" / "untracked.md",
        "Untracked",
        "\nCurrent version.\n",
    )
    note_commit = commit_all(tmp_path, "Add tracked note")
    review_path = write(
        tmp_path / "reviews" / "untracked.prose-review.md",
        """=== PROSE REVIEW: untracked.md ===

Checks applied: 8

CLEAN:
- [Pseudo-formalism] Clean.

Overall: CLEAN
===
""",
    )

    updated, reason = migrate_review_metadata.migrate_review_file(
        review_path,
        tmp_path / "kb" / "notes",
        tmp_path,
    )

    assert updated
    assert reason == "updated-untracked-review"
    metadata = review_metadata.parse_review_metadata(
        review_path.read_text(encoding="utf-8")
    )
    assert metadata is not None
    assert metadata.note_path == "kb/notes/untracked.md"
    assert metadata.last_full_review_note_sha == review_metadata.git_blob_sha(note_path)
    assert metadata.last_accepted_note_sha == review_metadata.git_blob_sha(note_path)
    assert metadata.last_full_review_note_commit == note_commit
    assert metadata.last_accepted_note_commit == note_commit
    assert metadata.last_acceptance_kind == "full-review"


def test_render_change_record_emits_compact_truncated_json() -> None:
    change = notes_selector.ReviewChange(
        note_path="kb/notes/example.md",
        review_path="reviews/example.prose-review.md",
        review_type="prose-review",
        status="changed",
        reason="content-changed",
        current_blob_sha="a" * 40,
        accepted_note_sha="b" * 40,
        accepted_note_commit="c" * 40,
        accepted_at="2026-03-23T10:00:00+01:00",
        diff="x" * 250,
    )

    rendered = notes_selector.render_change_record(change)

    assert rendered == {
        "note_path": "kb/notes/example.md",
        "review_path": "reviews/example.prose-review.md",
        "reason": "content-changed",
        "diff": "x" * 250,
    }


def test_render_change_record_can_include_status_for_unchanged_entries() -> None:
    change = notes_selector.ReviewChange(
        note_path="kb/notes/example.md",
        review_path="reviews/example.prose-review.md",
        review_type="prose-review",
        status="unchanged",
        reason="blob-match",
        current_blob_sha="a" * 40,
        accepted_note_sha="a" * 40,
        accepted_note_commit=None,
        accepted_at=None,
    )

    rendered = notes_selector.render_change_record(change, include_status=True)

    assert rendered == {
        "note_path": "kb/notes/example.md",
        "review_path": "reviews/example.prose-review.md",
        "reason": "blob-match",
        "status": "unchanged",
    }


def test_main_requires_review_type_or_all(capsys: pytest.CaptureFixture[str]) -> None:
    old_argv = sys.argv
    sys.argv = ["notes_selector.py"]
    try:
        with pytest.raises(SystemExit) as excinfo:
            notes_selector.main()
    finally:
        sys.argv = old_argv

    captured = capsys.readouterr()
    assert excinfo.value.code == 2
    assert "provide a review type or pass --all" in captured.err


def test_ack_review_advances_only_accepted_revision(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    init_repo(tmp_path)
    note_path = note(
        tmp_path / "kb" / "notes" / "ackable.md",
        "Ackable",
        "\nFirst version.\n",
    )
    first_commit = commit_all(tmp_path, "Add ackable note")
    first_blob_sha = review_metadata.git_blob_sha(note_path)
    review_text = review_metadata.inject_review_metadata(
        """=== PROSE REVIEW: ackable.md ===

Checks applied: 8

CLEAN:
- [Pseudo-formalism] Clean.

Overall: CLEAN
===
""",
        review_metadata.ReviewMetadata(
            note_path="kb/notes/ackable.md",
            last_full_review_note_sha=first_blob_sha,
            last_full_review_note_commit=first_commit,
            last_full_review_at="2026-03-23T10:00:00+01:00",
            last_accepted_note_sha=first_blob_sha,
            last_accepted_note_commit=first_commit,
            last_accepted_at="2026-03-23T10:00:00+01:00",
            last_acceptance_kind="full-review",
            review_type="prose-review",
        ),
    )
    review_file = tmp_path / "kb" / "reports" / "reviews" / "ackable.prose-review.md"
    write(review_file, review_text)
    note(
        note_path,
        "Ackable",
        "\nFirst version.\nTrivial extra line.\n",
    )
    second_commit = commit_all(tmp_path, "Trivial note change")

    monkeypatch.chdir(tmp_path)
    old_argv = sys.argv
    sys.argv = ["ack_review.py", "prose-review", "kb/notes/ackable.md"]
    try:
        ack_review.main()
    finally:
        sys.argv = old_argv

    metadata = review_metadata.parse_review_metadata(
        review_file.read_text(encoding="utf-8")
    )
    assert metadata is not None
    assert metadata.last_full_review_note_sha == first_blob_sha
    assert metadata.last_full_review_note_commit == first_commit
    assert metadata.last_accepted_note_sha == review_metadata.git_blob_sha(note_path)
    assert metadata.last_accepted_note_commit == second_commit
    assert metadata.last_acceptance_kind == "trivial-change-ack"
