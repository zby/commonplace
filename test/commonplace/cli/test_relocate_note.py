from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.cli import relocate_note
from commonplace.lib.naming import slugify_note_filename


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

    updated, changes = relocate_note.rewrite_links_to_relocated_note(
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
    target = write(tmp_path / "kb" / "notes" / "definitions" / "concept.md", "# Concept\n")
    content = """Self: [self](./old-note.md)
Target: [concept](./definitions/concept.md)
"""

    updated, changes = relocate_note.rebase_relative_markdown_links(
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

    updated, changes = relocate_note.update_mkdocs_config(
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
    with pytest.raises(ValueError, match="note filename slug exceeds 100 characters: 101"):
        slugify_note_filename("a" * 101)


def test_resolve_destination_path_rejects_overlong_explicit_slug(tmp_path: Path, monkeypatch) -> None:
    repo_root = tmp_path
    kb_root = repo_root / "kb"
    notes_root = kb_root / "notes"
    source = write(notes_root / "old-note.md", "# Old note\n")

    monkeypatch.setattr(relocate_note, "REPO_ROOT", repo_root)
    monkeypatch.setattr(relocate_note, "KB_ROOT", kb_root)
    monkeypatch.setattr(relocate_note, "NOTES_ROOT", notes_root)

    overlong_slug = "a" * 101
    with pytest.raises(ValueError, match="note filename slug exceeds 100 characters: 101"):
        relocate_note.resolve_destination_path(
            source,
            None,
            None,
            f"kb/notes/{overlong_slug}.md",
        )


def test_relocate_note_apply_moves_file_and_updates_links(tmp_path: Path, monkeypatch) -> None:
    repo_root = tmp_path
    kb_root = repo_root / "kb"
    notes_root = kb_root / "notes"
    old_note = write(
        notes_root / "old-note.md",
        """# Old note

Self: [self](./old-note.md)
See [concept](./definitions/concept.md)
""",
    )
    write(notes_root / "definitions" / "concept.md", "# Concept\n")
    write(
        notes_root / "other.md",
        """# Other

See [old](./old-note.md).
""",
    )
    write(
        repo_root / "README.md",
        """[Old note](./kb/notes/old-note.md)
""",
    )
    write(
        repo_root / "mkdocs.yml",
        """site_name: Commonplace
plugins:
  - redirects:
      redirect_maps:
        'notes/already-old.md': 'notes/old-note.md'
nav:
  - Notes: notes/old-note.md
""",
    )

    monkeypatch.setattr(relocate_note, "REPO_ROOT", repo_root)
    monkeypatch.setattr(relocate_note, "KB_ROOT", kb_root)
    monkeypatch.setattr(relocate_note, "NOTES_ROOT", notes_root)
    monkeypatch.setattr(relocate_note, "MKDOCS_CONFIG", repo_root / "mkdocs.yml")

    def fake_move(source: Path, destination: Path) -> str:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.rename(destination)
        return "rename"

    monkeypatch.setattr(relocate_note, "move_note", fake_move)

    result = relocate_note.relocate_note(
        "old-note",
        "New note title",
        dest_dir="kb/notes/archive",
        apply=True,
    )

    new_note = notes_root / "archive" / "new-note-title.md"
    assert result == 0
    assert not old_note.exists()
    assert new_note.exists()
    relocated_text = new_note.read_text(encoding="utf-8")
    assert "[self](./new-note-title.md)" in relocated_text
    assert "[concept](../definitions/concept.md)" in relocated_text
    assert "[old](./archive/new-note-title.md)" in (notes_root / "other.md").read_text(encoding="utf-8")
    assert "./kb/notes/archive/new-note-title.md" in (repo_root / "README.md").read_text(encoding="utf-8")
    mkdocs_content = (repo_root / "mkdocs.yml").read_text(encoding="utf-8")
    assert "'notes/already-old.md': 'notes/archive/new-note-title.md'" in mkdocs_content
    assert "'notes/old-note.md': 'notes/archive/new-note-title.md'" in mkdocs_content
    assert "notes/archive/new-note-title.md" in mkdocs_content
