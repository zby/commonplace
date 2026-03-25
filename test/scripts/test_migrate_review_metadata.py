from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


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


review_metadata = load_module("review_metadata_migration", SCRIPTS_DIR / "review_metadata.py")
migrate_review_metadata = load_module(
    "migrate_review_metadata",
    SCRIPTS_DIR / "migrations" / "migrate_review_metadata.py",
)


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
