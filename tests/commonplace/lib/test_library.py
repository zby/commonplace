from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import library, type_resolver


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_checkout(root: Path, *, name: str = library.PROJECT_NAME) -> Path:
    """A minimal Commonplace source checkout, as a batch worktree is."""
    write(root / "pyproject.toml", f'[project]\nname = "{name}"\n')
    (root / "src" / "commonplace").mkdir(parents=True)
    (root / "kb" / "instructions").mkdir(parents=True)
    write(root / "kb" / "types" / "note.md", "---\ndescription: Note type\n---\n\n# note\n")
    write(root / "kb" / "notes" / "COLLECTION.md", "# Notes\n")
    return root


def test_a_working_commonplace_checkout_is_its_own_library(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    checkout = make_checkout(tmp_path / "worktree")
    note = write(checkout / "kb" / "notes" / "sample.md", "---\ntype: types/note.md\n---\n")
    monkeypatch.delenv(library.LIBRARY_ENV, raising=False)
    monkeypatch.chdir(checkout / "kb" / "notes")

    assert library.library_root() == (checkout / "kb").resolve()
    rel, spec = type_resolver.validate_type_path(
        "types/note.md", repo_root=checkout, source_file=note
    )
    assert (rel, spec) == ("types/note.md", (checkout / "kb" / "types" / "note.md").resolve())


def test_the_library_override_wins_over_a_working_checkout(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    checkout = make_checkout(tmp_path / "worktree")
    override = tmp_path / "library"
    monkeypatch.setenv(library.LIBRARY_ENV, str(override))
    monkeypatch.chdir(checkout)

    assert library.library_root() == override.resolve()


def test_a_repository_of_another_project_is_not_a_library(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    other = make_checkout(tmp_path / "other", name="something-else")
    monkeypatch.delenv(library.LIBRARY_ENV, raising=False)
    monkeypatch.chdir(other)

    assert library.library_root() != (other / "kb").resolve()
