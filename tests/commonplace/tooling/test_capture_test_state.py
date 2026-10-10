"""Check retained bytes, symlink boundaries, and deterministic change detection."""

import json
import tarfile

import pytest

from scripts.capture_test_state import capture, compare


def test_capture_preserves_before_state_and_reports_actual_changes(tmp_path):
    root = tmp_path / "project"
    root.mkdir()
    (root / "policy.md").write_text("48 hours")
    (root / "obsolete.md").write_text("history")
    (root / "unchanged.md").write_text("inspect before relending")
    first = capture(root, tmp_path / "before", archive=True)
    (root / "policy.md").write_text("72 hours")
    (root / "obsolete.md").unlink()
    (root / "new.md").write_text("new version")
    second = capture(root, tmp_path / "after")
    assert compare(first, second) == {
        "added": ["new.md"],
        "removed": ["obsolete.md"],
        "modified": ["policy.md"],
    }
    with tarfile.open(tmp_path / "before/files.tar.gz") as bundle:
        assert bundle.extractfile("project/policy.md").read() == b"48 hours"
    with pytest.raises(FileExistsError):
        capture(root, tmp_path / "before")
    assert json.loads((tmp_path / "before/inventory.json").read_text()) == first


def test_capture_does_not_follow_external_symlink(tmp_path):
    root = tmp_path / "project"
    root.mkdir()
    secret = tmp_path / "key.txt"
    secret.write_text("evaluator-only answer")
    try:
        (root / "escape").symlink_to(secret)
    except OSError:
        pytest.skip("Symlinks unavailable")
    state = capture(root, tmp_path / "record", archive=True)
    assert state == {"escape": {"symlink": str(secret)}}
    with tarfile.open(tmp_path / "record/files.tar.gz") as bundle:
        assert bundle.getmember("project/escape").issym()
        assert len(bundle.getmembers()) == 2


def test_capture_rejects_output_inside_input(tmp_path):
    with pytest.raises(ValueError, match="outside"):
        capture(tmp_path, tmp_path / "record", archive=True)
    assert not (tmp_path / "record").exists()
