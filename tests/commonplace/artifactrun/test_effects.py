"""The journaled directory install: exact bytes, replay, rollback and uncertainty."""
from __future__ import annotations

import json
from hashlib import sha256

import pytest

from commonplace.artifactrun import UncertainEffectError, effects

ARCHIVED = "previous-run"


def effect(tmp_path, *, incumbent=False):
    destination = tmp_path / "retained" / "example"
    archive = tmp_path / "archive"
    old = {"overview.md": b"old overview\n", "ARTIFACT.yaml": b"old manifest\n", "memory.md": b"old memory\r\n"}
    if incumbent:
        destination.mkdir(parents=True)
        for name, data in old.items():
            (destination / name).write_bytes(data)
    new = {"ARTIFACT.yaml": b"new manifest\n", "overview.md": b"new overview\r\n", "memory.md": b"new memory\n"}
    args = {"journal": tmp_path / "run" / "effects" / "publish.json", "destination": destination,
            "archive_root": archive, "files": new, "anchor": "overview.md",
            "expected": sha256(old["overview.md"]).hexdigest() if incumbent else "absent",
            "identity": {"run-id": "this-run"}, "archive_name": lambda incumbent: ARCHIVED,
            "inspect_incumbent": lambda: None}
    return args, old


@pytest.mark.parametrize("incumbent", [False, True])
def test_exact_byte_effect_and_replay(tmp_path, incumbent):
    args, old = effect(tmp_path, incumbent=incumbent)
    first = effects.install_tree(**args)
    assert effects.tree(args["destination"]) == args["files"]
    if incumbent:
        assert effects.tree(args["archive_root"] / ARCHIVED) == old
    args["inspect_incumbent"] = lambda: pytest.fail("recognizable replay must not reinspect the new incumbent")
    assert effects.install_tree(**args) == first
    assert json.loads(args["journal"].read_bytes())["state"] == "completed"


def test_incumbent_guard_has_no_effect(tmp_path):
    args, old = effect(tmp_path, incumbent=True)
    args["expected"] = "f" * 64
    with pytest.raises(ValueError, match="changed since"):
        effects.install_tree(**args)
    assert effects.tree(args["destination"]) == old
    assert not args["journal"].exists()


def test_failed_write_rolls_back_exact_old_tree_and_retries(tmp_path, monkeypatch):
    args, old = effect(tmp_path, incumbent=True)
    original = effects.atomic_write

    def fail_member(path, data):
        if path.name == "memory.md":
            raise OSError("scripted member failure")
        original(path, data)

    monkeypatch.setattr(effects, "atomic_write", fail_member)
    with pytest.raises(OSError, match="scripted"):
        effects.install_tree(**args)
    assert effects.tree(args["destination"]) == old
    assert json.loads(args["journal"].read_bytes())["state"] == "rolled-back"
    monkeypatch.setattr(effects, "atomic_write", original)
    effects.install_tree(**args)
    assert effects.tree(args["destination"]) == args["files"]


@pytest.mark.parametrize("point", ["before-effect", "after-move", "after-install"])
def test_interrupted_effect_recognition(tmp_path, monkeypatch, point):
    args, old = effect(tmp_path, incumbent=True)
    original = effects.write_json
    write = effects.atomic_write

    def interrupt(path, record):
        if record["state"] == ("completed" if point == "after-install" else "started"):
            original(path, record) if point == "before-effect" else None
            if point != "after-move":
                raise KeyboardInterrupt("scripted interrupt")
        original(path, record)

    def interrupt_member(path, data):
        if point == "after-move" and path.name == "ARTIFACT.yaml":
            raise KeyboardInterrupt("scripted interrupt")
        write(path, data)

    monkeypatch.setattr(effects, "write_json", interrupt)
    monkeypatch.setattr(effects, "atomic_write", interrupt_member)
    with pytest.raises(KeyboardInterrupt):
        effects.install_tree(**args)
    monkeypatch.setattr(effects, "write_json", original)
    monkeypatch.setattr(effects, "atomic_write", write)
    if point == "after-move":
        with pytest.raises(UncertainEffectError, match="interrupted publication"):
            effects.install_tree(**args)
        assert effects.tree(args["destination"]) == {}
        assert effects.tree(args["archive_root"] / ARCHIVED) == old
    else:
        effects.install_tree(**args)
        assert effects.tree(args["destination"]) == args["files"]


def test_changed_journal_inputs_and_changed_completed_bytes_stop(tmp_path):
    args, _ = effect(tmp_path)
    effects.install_tree(**args)
    args["files"] = {**args["files"], "memory.md": b"different pin"}
    with pytest.raises(UncertainEffectError, match="identity"):
        effects.install_tree(**args)
    args["files"]["memory.md"] = b"new memory\n"
    (args["destination"] / "memory.md").write_bytes(b"unexpected mutation")
    with pytest.raises(UncertainEffectError, match="completed publication"):
        effects.install_tree(**args)


def test_rollback_failure_is_uncertain_and_preserves_evidence(tmp_path, monkeypatch):
    args, _ = effect(tmp_path, incumbent=True)
    original = effects.atomic_write

    def fail(path, data):
        if path.name == "memory.md":
            raise OSError("cannot write member")
        original(path, data)

    monkeypatch.setattr(effects, "atomic_write", fail)
    monkeypatch.setattr(effects.shutil, "rmtree", lambda path: (_ for _ in ()).throw(OSError("cannot rollback")))
    with pytest.raises(UncertainEffectError, match="rollback uncertain"):
        effects.install_tree(**args)
    assert args["journal"].exists()
    assert args["archive_root"].exists()


def test_effect_rejects_symlinked_destination_without_mutation(tmp_path):
    args, _ = effect(tmp_path)
    external = tmp_path / "external"
    external.mkdir()
    args["destination"].parent.mkdir()
    args["destination"].symlink_to(external, target_is_directory=True)
    with pytest.raises(UncertainEffectError, match="symlinks"):
        effects.install_tree(**args)
    assert list(external.iterdir()) == []


def test_an_incumbent_without_its_anchor_is_refused_before_mutation(tmp_path):
    args, old = effect(tmp_path, incumbent=True)
    (args["destination"] / "overview.md").unlink()
    args["expected"] = sha256(b"").hexdigest()
    with pytest.raises(ValueError, match="no overview.md"):
        effects.install_tree(**args)
    assert effects.tree(args["destination"]) == {k: v for k, v in old.items() if k != "overview.md"}
    assert not args["journal"].exists()
