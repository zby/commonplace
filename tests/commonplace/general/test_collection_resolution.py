from pathlib import Path

import pytest

from commonplace.lib.project_paths import resolve_collection


@pytest.mark.parametrize("name", ["notes", "theory", "claims", "teams/claims"])
@pytest.mark.parametrize("typed", [False, True])
def test_resolve_collection_accepts_explicit_names_and_paths(tmp_path: Path, name: str, typed: bool):
    collection = tmp_path / "kb" / name
    collection.mkdir(parents=True)
    header = "---\ntype: types/collection-contract.md\n---\n" if typed else ""
    (collection / "COLLECTION.md").write_text(header + "# Contract\n")
    for arg in (name, f"kb/{name}", collection):
        assert resolve_collection(arg, tmp_path) == collection


def test_resolve_collection_rejects_missing_noncollection_and_external_targets(tmp_path: Path):
    (tmp_path / "kb/inbox").mkdir(parents=True)
    outside = tmp_path / "outside"
    outside.mkdir()
    (outside / "COLLECTION.md").write_text("# Contract\n")
    (tmp_path / "kb/alias").symlink_to(outside, target_is_directory=True)
    for arg in ("missing", "inbox", "kb", "../outside", outside, "alias"):
        with pytest.raises(ValueError, match="Not a collection under"):
            resolve_collection(arg, tmp_path)
