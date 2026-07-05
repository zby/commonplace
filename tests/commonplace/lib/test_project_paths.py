from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import project_paths


def write(path: Path, content: str = "# Title\n") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def collection(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    write(path / "COLLECTION.md", "# Collection\n")
    return path


def test_collection_dirs_returns_content_collections_only(tmp_path: Path) -> None:
    collection(tmp_path / "kb" / "notes")
    collection(tmp_path / "kb" / "work")
    (tmp_path / "kb" / "types").mkdir()
    (tmp_path / "kb" / "reports").mkdir()
    (tmp_path / "kb" / ".cache").mkdir()

    assert project_paths.collection_dirs(tmp_path) == [
        tmp_path / "kb" / "notes",
        tmp_path / "kb" / "work",
    ]


def test_collection_dirs_allows_collections_inside_namespace(tmp_path: Path) -> None:
    collection(tmp_path / "kb" / "commonplace" / "notes")
    collection(tmp_path / "kb" / "commonplace" / "reference")

    assert project_paths.collection_dirs(tmp_path) == [
        tmp_path / "kb" / "commonplace" / "notes",
        tmp_path / "kb" / "commonplace" / "reference",
    ]


def test_collection_dirs_raises_when_kb_root_is_missing(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="KB root does not exist"):
        project_paths.collection_dirs(tmp_path)


def test_list_collection_note_paths_skips_nested_repos_and_type_dirs(tmp_path: Path) -> None:
    collection_root = collection(tmp_path / "kb" / "notes")
    kept = write(collection_root / "kept.md")
    nested = write(collection_root / "vendor" / "repo" / "ignored.md")
    (nested.parent / ".git").mkdir()
    template = write(collection_root / "types" / "note.template.md")
    nested_template = write(collection_root / "definitions" / "types" / "definition.template.md")

    discovered = project_paths.list_collection_note_paths(collection_root)

    assert kept in discovered
    assert nested not in discovered
    assert template not in discovered
    assert nested_template not in discovered


def test_list_kb_note_paths_spans_all_content_collections(tmp_path: Path) -> None:
    collection(tmp_path / "kb" / "notes")
    collection(tmp_path / "kb" / "sources")
    note = write(tmp_path / "kb" / "notes" / "note.md")
    source = write(tmp_path / "kb" / "sources" / "source.md")
    report = write(tmp_path / "kb" / "reports" / "report.md")
    type_doc = write(tmp_path / "kb" / "types" / "note.md")

    discovered = project_paths.list_kb_note_paths(tmp_path)

    assert note in discovered
    assert source in discovered
    assert report not in discovered
    assert type_doc not in discovered


def test_list_notes_collection_paths_scans_only_kb_notes(tmp_path: Path) -> None:
    collection(tmp_path / "kb" / "notes")
    collection(tmp_path / "kb" / "sources")
    note = write(tmp_path / "kb" / "notes" / "note.md")
    source = write(tmp_path / "kb" / "sources" / "source.md")

    discovered = project_paths.list_notes_collection_paths(tmp_path)

    assert note in discovered
    assert source not in discovered


def test_resolve_note_returns_unique_match_across_kb(tmp_path: Path) -> None:
    collection(tmp_path / "kb" / "sources")
    note = write(tmp_path / "kb" / "sources" / "sample.md")

    assert project_paths.resolve_note("sample", tmp_path) == note.resolve()


def test_resolve_note_raises_on_ambiguous_match(tmp_path: Path) -> None:
    collection(tmp_path / "kb" / "notes")
    collection(tmp_path / "kb" / "sources")
    write(tmp_path / "kb" / "notes" / "sample.md")
    write(tmp_path / "kb" / "sources" / "sample.md")

    with pytest.raises(FileNotFoundError, match="Multiple matching notes found"):
        project_paths.resolve_note("sample", tmp_path)
