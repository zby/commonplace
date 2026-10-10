"""Mechanical calibration tests. These do not test model discrimination."""

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / "scripts/analysis_workflow_calibration.py"
spec = importlib.util.spec_from_file_location("calibration", SCRIPT)
calibration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calibration)


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    for command in (["init", "-q"], ["config", "user.name", "Calibration test"],
                    ["config", "user.email", "calibration@example.invalid"]):
        subprocess.run(["git", "-C", str(root), *command], check=True)
    for name in calibration.METHOD_FILES:
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("Committed method bytes\n")
    profiles = root / calibration.PROFILES_FILE
    profiles.write_text(
        "profiles:\n"
        "  pi-sol: {harness: pi, launch-model: gpt-6.1-sol, effort: medium}\n"
        "  pi-luna: {harness: pi, launch-model: gpt-6-luna, effort: medium}\n"
        "  pi-luna-low: {harness: pi, launch-model: gpt-6-luna, effort: low}\n"
    )
    subprocess.run(["git", "-C", str(root), "add", "kb"], check=True)
    subprocess.run(["git", "-C", str(root), "commit", "-qm", "Pin method"], check=True)
    workshop = root / calibration.WORKSHOP
    dump(workshop / "cases/packets.json", {f"c{i:02}": "Public evidence" for i in range(1, 9)})
    dump(workshop / "expected/judgments.json", {
        f"c{i:02}": {"blocker": i % 2 == 1, "reason": "SECRET answer key"}
        for i in range(1, 9)
    })
    (workshop / "protocol.md").write_text("Pilot protocol")
    return root


@pytest.fixture
def run(repo, tmp_path):
    target = tmp_path / "run"
    calibration.prepare(repo, "HEAD", target, "pi-sol")
    return target


def annotations(run, tmp_path):
    expected = calibration.load(run / "private/expected.json")
    data = {}
    for key, item in expected.items():
        (run / "packets" / key / "response.md").write_text("Raw model response")
        data[key] = {
            "status": "completed", "blocker": item["blocker"], "reason": "Annotated evidence",
            "launch": {"harness": "pi", "launch-model": "gpt-6.1-sol", "effort": "medium",
                       "resolved-model": "unknown", "isolation-evidence": "fixture boundary"},
        }
    target = tmp_path / "annotations.json"
    dump(target, data)
    return target


def test_pins_committed_method_and_profile_not_dirty_files(repo, tmp_path):
    (repo / calibration.METHOD_FILES[0]).write_text("Concurrent dirty implementation")
    (repo / calibration.PROFILES_FILE).write_text("profiles: {}")
    target = tmp_path / "run"
    manifest = calibration.prepare(repo, "HEAD", target, "pi-sol")
    assert (target / "packets/c01/method-1.md").read_text() == "Committed method bytes\n"
    assert manifest["worker-profile"]["launch-model"] == "gpt-6.1-sol"


@pytest.mark.parametrize("profile,effort", [("pi-luna", "medium"), ("pi-luna-low", "low")])
def test_luna_profiles_keep_distinct_effort(repo, tmp_path, profile, effort):
    manifest = calibration.prepare(repo, "HEAD", tmp_path / profile, profile)
    assert manifest["profile"] == profile
    assert manifest["worker-profile"] == {
        "harness": "pi", "launch-model": "gpt-6-luna", "effort": effort,
    }


def test_explicit_profile_override_is_pinned_separately(repo, tmp_path):
    override = tmp_path / "profiles.yaml"
    override.write_text(
        "profiles:\n  exploratory: {harness: pi, launch-model: gpt-6-luna, effort: low}\n"
    )
    target = tmp_path / "run"
    manifest = calibration.prepare(repo, "HEAD", target, "exploratory", override)
    assert manifest["profile-source"] == str(override)
    assert (target / "private/worker-profiles.yaml").read_bytes() == override.read_bytes()
    calibration.verify(target)


def test_answer_key_is_outside_all_packets(run):
    calibration.verify(run)
    for path in (run / "packets").rglob("*"):
        if path.is_file():
            assert "SECRET" not in path.read_text()
    assert (run / "private/expected.json").exists()


def test_rejects_repository_destination_and_reuse(repo, run):
    with pytest.raises(ValueError, match="outside"):
        calibration.prepare(repo, "HEAD", repo / "run", "pi-sol")
    with pytest.raises(FileExistsError):
        calibration.prepare(repo, "HEAD", run, "pi-sol")


def test_unknown_profile_does_not_create_run(repo, tmp_path):
    target = tmp_path / "bad"
    with pytest.raises(ValueError, match="Unknown worker profile"):
        calibration.prepare(repo, "HEAD", target, "replacement-model")
    assert not target.exists()


def test_detects_changed_pinned_inputs(run):
    (run / "packets/c01/input.md").write_text("Changed")
    with pytest.raises(ValueError, match="Pinned input"):
        calibration.verify(run)


def test_detects_extra_files_in_packet(run):
    (run / "packets/c01/answers.json").write_text("Leak")
    with pytest.raises(ValueError, match="Unexpected packet"):
        calibration.verify(run)


def test_scores_pairs_and_keeps_raw_response_hashes(run, tmp_path):
    path = annotations(run, tmp_path)
    result = calibration.score(run, path)
    assert result["counts"]["detected"] == 4
    assert result["counts"]["supported-control"] == 4
    assert result["profile"] == "pi-sol"
    assert result["cases"]["c01"]["response-sha256"]


def test_failures_and_unscorable_are_not_semantic_misses(run, tmp_path):
    path = annotations(run, tmp_path)
    data = calibration.load(path)
    data["c01"] = {"status": "failed", "reason": "Launch failed"}
    data["c02"] = {"status": "unscorable", "reason": "Malformed verdict"}
    data["c03"]["blocker"] = False
    data["c04"]["blocker"] = True
    dump(path, data)
    counts = calibration.score(run, path)["counts"]
    assert counts["execution-failure"] == counts["unscorable"] == 1
    assert counts["missed"] == counts["false-blocker"] == 1


def test_requires_all_annotations_and_raw_responses(run, tmp_path):
    path = annotations(run, tmp_path)
    (run / "packets/c01/response.md").unlink()
    with pytest.raises(ValueError, match="no raw response"):
        calibration.score(run, path)
    data = calibration.load(path)
    del data["c01"]
    dump(path, data)
    with pytest.raises(ValueError, match="every case"):
        calibration.score(run, path)


def test_rejects_substituted_launch_profile(run, tmp_path):
    path = annotations(run, tmp_path)
    data = calibration.load(path)
    data["c01"]["launch"]["effort"] = "high"
    dump(path, data)
    with pytest.raises(ValueError, match="pinned worker profile"):
        calibration.score(run, path)
