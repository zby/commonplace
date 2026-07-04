from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import relocation
from commonplace.lib.naming import MAX_NOTE_SLUG_LENGTH, slugify_note_filename
from commonplace.review import review_db, review_target_selector
from tests.commonplace.cli.relocation_review_helpers import (
    GATE_ID,
    TEST_MODEL,
    make_gate,
    make_reviewable_note,
    review_state_rows,
    seed_accepted_review,
)


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


def test_relocate_note_apply_leaves_review_state_rows_unchanged_and_paths_derived(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    repo_root = tmp_path
    kb_root = repo_root / "kb"
    notes_root = kb_root / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    old_note = make_reviewable_note(notes_root / "old-note.md")
    make_gate(repo_root)
    write(repo_root / "mkdocs.yml", "plugins:\n  - redirects:\n      redirect_maps:\n")
    db_path = kb_root / "reports" / "review-store.sqlite"
    review_pair_id = seed_accepted_review(repo_root, db_path, note_path="kb/notes/old-note.md")
    with review_db.connect(db_path) as conn:
        rows_before = review_state_rows(conn)

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
    )

    new_note = notes_root / "archive" / "new-note-title.md"
    output = capsys.readouterr().out.lower()
    assert result == 0
    assert "review" not in output
    assert not old_note.exists()
    assert new_note.exists()

    with review_db.connect(db_path) as conn:
        rows_after = review_state_rows(conn)
        plan = review_db.load_review_job_plan(conn, review_job_id=1)
        old_pairs = review_db.load_review_pairs_for_note(
            conn,
            note_path="kb/notes/old-note.md",
            model_partition=TEST_MODEL,
        )
        new_pairs = review_db.load_review_pairs_for_note(
            conn,
            note_path="kb/notes/archive/new-note-title.md",
            model_partition=TEST_MODEL,
        )

    assert rows_after == rows_before
    assert plan is not None
    assert old_pairs[0].review_pair_id == review_pair_id
    assert new_pairs == []
    assert "prompt_path" not in rows_after["review_jobs"][0]
    assert "bundle_output_path" not in rows_after["review_jobs"][0]
    assert "result_path" not in rows_after["review_pairs"][0]
    assert plan.prompt_path == "kb/reports/bundle-reviews/review-job-1/prompt.md"
    assert plan.bundle_output_path == "kb/reports/bundle-reviews/review-job-1/bundle-output.md"
    assert old_pairs[0].result_path == "kb/reports/bundle-reviews/review-job-1/source-residue.md"

    stale = review_target_selector.select_stale_gates(
        repo_root,
        model=TEST_MODEL,
        gate_ids=[GATE_ID],
        note_filter=["kb/notes/archive/new-note-title.md"],
        db_path=db_path,
    )
    assert [(record.note_path, record.gate_id, record.reason) for record in stale] == [
        ("kb/notes/archive/new-note-title.md", GATE_ID, "missing-review")
    ]


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
