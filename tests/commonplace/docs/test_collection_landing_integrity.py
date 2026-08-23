from pathlib import Path

from commonplace.cli import validate_notes
from commonplace.lib.validation import validate_collection_landings


def write(path: Path, content: str = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def add_collection(
    root: Path,
    name: str,
    *,
    readme: bool = True,
    index: bool = False,
) -> Path:
    collection = root / "kb" / name
    write(collection / "COLLECTION.md", f"# {name}\n")
    if readme:
        write(collection / "README.md", f"# {name}\n")
    if index:
        write(collection / "index.md", f"# {name} index\n")
    return collection


def test_collection_landings_accept_complete_top_level_inventory(tmp_path: Path) -> None:
    add_collection(tmp_path, "notes")
    add_collection(tmp_path, "types")

    results = validate_collection_landings(repo_root=tmp_path)

    assert results.fails == []
    assert (
        "[repository] collection landings: all 2 top-level collections have README.md"
        in results.passes
    )
    assert "[repository] collection landing collisions: none" in results.passes


def test_collection_landings_reject_missing_readme(tmp_path: Path) -> None:
    add_collection(tmp_path, "notes", readme=False)

    results = validate_collection_landings(repo_root=tmp_path)

    assert results.fails == [
        "[repository] collection landing does not exist: kb/notes/README.md"
    ]


def test_collection_landings_reject_readme_index_collision(tmp_path: Path) -> None:
    add_collection(tmp_path, "types", index=True)

    results = validate_collection_landings(repo_root=tmp_path)

    assert results.fails == [
        (
            "[repository] collection landing collision: "
            "kb/types contains both README.md and index.md"
        )
    ]


def test_collection_landings_ignore_nested_collection_boundaries(tmp_path: Path) -> None:
    work = add_collection(tmp_path, "work")
    write(work / "fixture" / "COLLECTION.md", "# Fixture\n")

    results = validate_collection_landings(repo_root=tmp_path)

    assert results.fails == []
    assert (
        "[repository] collection landings: all 1 top-level collections have README.md"
        in results.passes
    )


def test_landings_cli_target_reports_repository_validation(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    add_collection(tmp_path, "notes")
    monkeypatch.chdir(tmp_path)

    exit_code = validate_notes.main(["landings"])

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "Type: collection-landings" in output
    assert "Overall: PASS (clean)" in output
