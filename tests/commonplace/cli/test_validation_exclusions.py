from pathlib import Path

from commonplace.cli import validate_notes
from commonplace.lib import project_paths, validation


def write(path: Path, content: str = "# Title\n") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def configure_collection(tmp_path: Path) -> Path:
    notes = tmp_path / "kb" / "notes"
    write(notes / "COLLECTION.md", "# Notes collection\n")
    return notes


def test_collection_target_prunes_validation_ignored_subtree(
    tmp_path: Path,
) -> None:
    notes = configure_collection(tmp_path)
    kept = write(notes / "workshop" / "framing.md", "# Framing\n")
    ignored_dir = notes / "workshop" / "experiment"
    ignored = write(ignored_dir / "invalid.md", "---\nbroken: [\n---\n")
    write(ignored_dir / project_paths.VALIDATION_IGNORE_MARKER, "")

    target = validate_notes.resolve_validation_target("notes", repo_root=tmp_path)

    assert kept in target.paths
    assert ignored not in target.paths
    assert target.ignored_dirs == (ignored_dir,)
    assert validate_notes.resolve_validation_target(
        str(ignored), repo_root=tmp_path
    ).paths == (ignored.resolve(),)


def test_collection_structure_ignores_nested_collection_in_excluded_subtree(
    tmp_path: Path,
) -> None:
    notes = configure_collection(tmp_path)
    ignored_dir = notes / "experiment"
    write(ignored_dir / project_paths.VALIDATION_IGNORE_MARKER, "")
    write(ignored_dir / "COLLECTION.md", "# Experimental fixture\n")

    failures = validation.validate_collection_structure(notes, repo_root=tmp_path)

    assert failures == []
