"""Operator approval integrity and locking; no worker is launched."""

import sys

import pytest

from commonplace.headless.harness import Harness, Profile
from commonplace.headless.jobs import Run, RunLocked
from commonplace.headless.operator import answer, approve, waiting


@pytest.fixture
def run(tmp_path):
    harness = Harness(sys.executable, {"_subcommand": ["-c", "pass"]}, lambda profile: {})
    with Run(tmp_path / "run", tmp_path, Profile("fake", "m", "low"), harnesses={"fake": harness},
             sleep=lambda s: None) as run:
        yield run


def test_repeat_never_approves_even_an_existing_edited_file(run, tmp_path):
    run.artifact.mkdir(parents=True, exist_ok=True)
    (run.artifact / "plan.yaml").write_text("pre-existing\n")
    assert answer(run, "plan.yaml", "proposed\n", key="inputs") is None
    (run.artifact / "plan.yaml").write_text("edited\n")
    assert answer(run, "plan.yaml", "proposed\n", key="inputs") is None
    stop = waiting(run, tmp_path, "plan.yaml", "Edit the plan.", "repeat it")
    assert stop["file"] == "run/artifact/plan.yaml" and stop["command"] == "repeat it"
    assert "--key " + stop["key"] in stop["approve-command"]
    with pytest.raises(RunLocked):
        approve(run.root, "plan.yaml", stop["key"])
    run.close()
    approve(run.root, "plan.yaml", stop["key"])


def test_approval_captures_text_and_replacement_invalidates_old_command(run, tmp_path):
    assert answer(run, "plan.yaml", "proposed\n", key="inputs") is None
    stop = waiting(run, tmp_path, "plan.yaml", "Edit.", "repeat")
    root, cwd, profile, harnesses = run.root, run.cwd, run.profile, run.harnesses
    run.close()
    approve(root, "plan.yaml", stop["key"])
    (root / "artifact/plan.yaml").write_text("not approved\n")
    with Run(root, cwd, profile, harnesses=harnesses) as resumed:
        assert answer(resumed, "plan.yaml", "proposed\n", key="inputs") == "proposed\n"
        assert answer(resumed, "plan.yaml", "new proposal", key="changed inputs") is None
    with pytest.raises(ValueError, match="proposal changed"):
        approve(root, "plan.yaml", stop["key"])


@pytest.mark.parametrize("name", ["../escape", "/tmp/escape"])
def test_operator_paths_cannot_escape_artifact(run, name):
    with pytest.raises(ValueError, match="outside"):
        answer(run, name, "bad", key="inputs")


def test_symlink_cannot_redirect_an_approval_outside_artifact(run, tmp_path):
    answer(run, "plan.yaml", "plan", key="inputs")
    stop = waiting(run, tmp_path, "plan.yaml", "Edit.", "repeat")
    run.close()
    outside = tmp_path / "outside"
    outside.write_text("private")
    (run.artifact / "plan.yaml").unlink()
    try:
        (run.artifact / "plan.yaml").symlink_to(outside)
    except OSError as error:
        pytest.skip(f"file symlinks unavailable: {error}")
    with pytest.raises(ValueError, match="outside"):
        approve(run.root, "plan.yaml", stop["key"])
