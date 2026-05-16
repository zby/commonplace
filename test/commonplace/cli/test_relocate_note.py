from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import relocation
from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH, slugify_note_filename
from commonplace.review import review_db
from commonplace.review.relocation_hook import ReviewRelocationHook


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_rewrite_links_to_relocated_note_updates_real_links_only(tmp_path: Path) -> None:
    old_note = tmp_path / "kb" / "notes" / "old-note.md"
    new_note = tmp_path / "kb" / "notes" / "new-note.md"
    ref_file = tmp_path / "kb" / "sources" / "source.ingest.md"
    content = """Real: [old](../notes/old-note.md)
Anchored: [section](../notes/old-note.md#part)
External: [site](https://example.com/old-note.md)
Inline: `[skip](../notes/old-note.md)`

```md
[skip-fence](../notes/old-note.md)
```
"""

    updated, changes = relocation.rewrite_links_to_relocated_note(
        content,
        ref_file,
        old_note,
        new_note,
    )

    assert "[old](../notes/new-note.md)" in updated
    assert "[section](../notes/new-note.md#part)" in updated
    assert "https://example.com/old-note.md" in updated
    assert "`[skip](../notes/old-note.md)`" in updated
    assert "[skip-fence](../notes/old-note.md)" in updated
    assert changes == [
        "../notes/old-note.md -> ../notes/new-note.md",
        "../notes/old-note.md#part -> ../notes/new-note.md#part",
    ]


def test_rebase_relative_markdown_links_updates_outbound_links_for_moved_note(tmp_path: Path) -> None:
    old_note = tmp_path / "kb" / "notes" / "old-note.md"
    write(tmp_path / "kb" / "notes" / "definitions" / "concept.md", "# Concept\n")
    content = """Self: [self](./old-note.md)
Target: [concept](./definitions/concept.md)
"""

    updated, changes = relocation.rebase_relative_markdown_links(
        content,
        old_note,
        tmp_path / "kb" / "notes" / "archive" / "relocated-note.md",
    )

    assert "[self](./relocated-note.md)" in updated
    assert "[concept](../definitions/concept.md)" in updated
    assert changes == [
        "./old-note.md -> ./relocated-note.md",
        "./definitions/concept.md -> ../definitions/concept.md",
    ]


def test_update_mkdocs_config_adds_redirect_and_updates_targets() -> None:
    content = """site_name: Commonplace
plugins:
  - redirects:
      redirect_maps:
        'notes/older-name.md': 'notes/old-name.md'
nav:
  - Home: index.md
  - Example: notes/old-name.md
"""

    updated, changes = relocation.update_mkdocs_config(
        content,
        old_docs_path="notes/old-name.md",
        new_docs_path="notes/archive/new-name.md",
    )

    assert "'notes/old-name.md': 'notes/archive/new-name.md'" in updated
    assert "'notes/older-name.md': 'notes/archive/new-name.md'" in updated
    assert "- Example: notes/archive/new-name.md" in updated
    assert any("mkdocs redirect: notes/old-name.md -> notes/archive/new-name.md" == item for item in changes)
    assert any("mkdocs redirect target: notes/older-name.md -> notes/archive/new-name.md" == item for item in changes)


def test_slugify_rejects_overlong_note_slug() -> None:
    overlong_slug = "a" * (MAX_NOTE_SLUG_LENGTH + 1)
    message = (
        f"note filename slug exceeds {MAX_NOTE_SLUG_LENGTH} characters: "
        f"{MAX_NOTE_SLUG_LENGTH + 1}"
    )
    with pytest.raises(ValueError, match=message):
        slugify_note_filename(overlong_slug)


def test_resolve_destination_path_rejects_overlong_explicit_slug(tmp_path: Path) -> None:
    repo_root = tmp_path
    notes_root = repo_root / "kb" / "notes"
    source = write(notes_root / "old-note.md", "# Old note\n")

    overlong_slug = "a" * (MAX_NOTE_SLUG_LENGTH + 1)
    message = (
        f"note filename slug exceeds {MAX_NOTE_SLUG_LENGTH} characters: "
        f"{MAX_NOTE_SLUG_LENGTH + 1}"
    )
    with pytest.raises(ValueError, match=message):
        relocation.resolve_destination_path(
            source,
            None,
            f"kb/notes/{overlong_slug}.md",
            repo_root=repo_root,
            kb_root=repo_root / "kb",
        )


def test_resolve_destination_path_accepts_directory_target(tmp_path: Path) -> None:
    repo_root = tmp_path
    notes_root = repo_root / "kb" / "notes"
    source = write(notes_root / "old-note.md", "# Old note\n")

    destination = relocation.resolve_destination_path(
        source,
        None,
        "kb/notes/archive",
        repo_root=repo_root,
        kb_root=repo_root / "kb",
    )

    assert destination == notes_root / "archive" / "old-note.md"


def test_relocate_note_apply_runs_review_relocation_hook(tmp_path: Path, monkeypatch) -> None:
    """End-to-end coverage for ReviewRelocationHook: relocating a note must
    move its legacy review file and rekey its review-DB rows. Link rewriting,
    mkdocs redirect updates, and DB rekey mechanics are covered by dedicated
    unit tests; this test only verifies the hook is wired into relocate_note."""
    repo_root = tmp_path
    kb_root = repo_root / "kb"
    notes_root = kb_root / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    old_note = write(notes_root / "old-note.md", "# Old note\n")
    write(repo_root / "mkdocs.yml", "plugins:\n  - redirects:\n      redirect_maps:\n")
    legacy_review = write(
        kb_root / "reports" / "reviews" / "kb__notes__old-note" / "prose__source-residue.opus-4-6.md",
        """<!-- REVIEW-METADATA
note-path: kb/notes/old-note.md
gate-id: prose/source-residue
review-type: gate-review
-->
## Result: PASS
""",
    )
    db_path = kb_root / "reports" / "review-store.sqlite"
    review_db.ensure_db(repo_root, db_path)
    with review_db.connect(db_path) as conn:
        review_run_id = review_db.insert_review_run(
            conn,
            note_path="kb/notes/old-note.md",
            model_id="opus-4-6",
            runner="codex",
            reviewed_note_sha="note-sha",
            reviewed_note_commit="note-commit",
            started_at="2026-04-10T10:00:00+02:00",
        )
        review_db.insert_gate_review(
            conn,
            review_run_id=review_run_id,
            note_path="kb/notes/old-note.md",
            gate_id="prose/source-residue",
            model_id="opus-4-6",
            decision="pass",
            rationale_markdown="ok",
            evidence_json=None,
            gate_sha="gate-sha",
            reviewed_note_sha="note-sha",
            reviewed_note_commit="note-commit",
            reviewed_at="2026-04-10T10:05:00+02:00",
        )
        conn.commit()

    def fake_move(source: Path, destination: Path, *, repo_root: Path) -> str:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
        return "rename"

    monkeypatch.setattr(relocation, "move_note", fake_move)

    result = relocation.relocate_note(
        root=repo_root,
        note_arg="old-note",
        dest_path="kb/notes/archive/new-note-title.md",
        apply=True,
        hooks=[ReviewRelocationHook()],
    )

    new_note = notes_root / "archive" / "new-note-title.md"
    assert result == 0
    assert not old_note.exists()
    assert new_note.exists()

    moved_review = kb_root / "reports" / "reviews" / "kb__notes__archive__new-note-title" / legacy_review.name
    assert not legacy_review.exists()
    assert moved_review.exists()
    assert "note-path: kb/notes/archive/new-note-title.md" in moved_review.read_text(encoding="utf-8")

    with review_db.connect(db_path) as conn:
        counts = review_db.count_note_path_records(conn, note_path="kb/notes/archive/new-note-title.md")
        old_counts = review_db.count_note_path_records(conn, note_path="kb/notes/old-note.md")
    assert counts.review_runs == 1
    assert counts.gate_reviews == 1
    assert old_counts.total == 0


def test_relocate_note_apply_moves_file_with_to_directory(tmp_path: Path, monkeypatch) -> None:
    repo_root = tmp_path
    kb_root = repo_root / "kb"
    notes_root = kb_root / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    old_note = write(
        notes_root / "old-note.md",
        """# Old note

See [concept](./definitions/concept.md)
""",
    )
    write(notes_root / "definitions" / "concept.md", "# Concept\n")
    write(repo_root / "mkdocs.yml", "plugins:\n  - redirects:\n      redirect_maps:\n")

    def fake_move(source: Path, destination: Path, *, repo_root: Path) -> str:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
        return "rename"

    monkeypatch.setattr(relocation, "move_note", fake_move)

    result = relocation.relocate_note(
        root=repo_root,
        note_arg="old-note",
        dest_path="kb/notes/archive",
        apply=True,
    )

    new_note = notes_root / "archive" / "old-note.md"
    assert result == 0
    assert not old_note.exists()
    assert new_note.exists()
    relocated_text = new_note.read_text(encoding="utf-8")
    assert "[concept](../definitions/concept.md)" in relocated_text


def test_relocate_note_hook_plan_failure_aborts_before_core_writes(tmp_path: Path) -> None:
    repo_root = tmp_path
    notes_root = repo_root / "kb" / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    old_note = write(notes_root / "old-note.md", "# Old note\n")
    write(
        repo_root / "mkdocs.yml",
        """plugins:
  - redirects:
      redirect_maps:
""",
    )

    class FailingHook:
        def plan(self, *, root: Path, moves) -> object:
            raise RuntimeError("preflight failed")

        def describe(self, plan: object) -> list[str]:
            return []

        def execute(self, plan: object) -> None:
            raise AssertionError("execute should not run")

    result = relocation.relocate_note(
        root=repo_root,
        note_arg="old-note",
        dest_path="kb/notes/archive/old-note.md",
        apply=True,
        hooks=[FailingHook()],
    )

    assert result == 1
    assert old_note.exists()
    assert not (notes_root / "archive" / "old-note.md").exists()


def test_relocate_note_apply_moves_note_across_kb_collections(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo_root = tmp_path
    kb_root = repo_root / "kb"
    notes_root = kb_root / "notes"
    source = write(
        notes_root / "document-classification.md",
        """# Document classification

See [note](../types/note.md)
""",
    )
    write(kb_root / "types" / "note.md", "# Note\n")
    write(
        notes_root / "reader.md",
        """# Reader

See [doc](./document-classification.md).
""",
    )
    write(
        repo_root / "mkdocs.yml",
        """site_name: Commonplace
plugins:
  - redirects:
      redirect_maps:
        'notes/already-old.md': 'notes/document-classification.md'
nav:
  - Doc System: notes/document-classification.md
""",
    )

    def fake_move(source_path: Path, destination_path: Path, *, repo_root: Path) -> str:
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        source_path.rename(destination_path)
        return "rename"

    monkeypatch.setattr(relocation, "move_note", fake_move)

    result = relocation.relocate_note(
        root=repo_root,
        note_arg="kb/notes/document-classification.md",
        dest_path="kb/reference/type-system.md",
        apply=True,
    )

    destination = kb_root / "reference" / "type-system.md"
    assert result == 0
    assert not source.exists()
    assert destination.exists()
    relocated_text = destination.read_text(encoding="utf-8")
    assert "[note](../types/note.md)" in relocated_text
    assert "[doc](../reference/type-system.md)" in (notes_root / "reader.md").read_text(encoding="utf-8")
    mkdocs_content = (repo_root / "mkdocs.yml").read_text(encoding="utf-8")
    assert "'notes/document-classification.md': 'reference/type-system.md'" in mkdocs_content
    assert "'notes/already-old.md': 'reference/type-system.md'" in mkdocs_content
    assert "- Doc System: reference/type-system.md" in mkdocs_content
