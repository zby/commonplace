"""Real collection context, controller stops and the production fixture adapter branch."""
import json

import pytest

from commonplace.cli.review_workflows import main
from commonplace.headless.harness import HARNESSES
from commonplace.lib.review_workflows import (
    fixtures,
    observations,
    result_contract,
    results,
)
from tests.commonplace.review_workflows.test_gates import _project, review


@pytest.mark.parametrize("installed", [False, True])
def test_all_kinds_validate_at_both_locations(tmp_path, monkeypatch, capsys, installed):
    repo = _project(tmp_path, monkeypatch, installed=installed)
    root = repo[0]
    hashes = []
    original = observations.library_files

    def counted(*args):
        hashes.append(args)
        return original(*args)

    monkeypatch.setattr(observations, "library_files", counted)
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria",
                                     "prose/body-gate", "type", "collection", "critique")
    assert code == 0 and len(launches) == 4, report
    assert len(hashes) == 1, "one library scan before parallel assessments"
    paths = list((root / report["run-dir"] / "artifact/reviews").glob("*/observation.json"))
    assert len(paths) == 4
    for path in paths:
        data = observations.load(path.parent)
        captured = observations.read_inputs(path.parent, data)
        contracts = {item["origin"]: captured[item["path"]]
                     for item in data["inputs"] if item["role"] == "contract"}
        assert contracts["workflow-state/COLLECTION.md"] == (root / "kb/workflow-state/COLLECTION.md").read_bytes()
        held = path.parent / data["completed-results"][0]
        text = held.read_text()
        current = results.result_path(root, data["request"]["note"], data["request"]["criterion-id"])
        assert not result_contract.validate_saved(root, held, text, contracts=contracts).fails
        assert not result_contract.validate_saved(root, current, text, contracts=contracts).fails
        del contracts["workflow-state/COLLECTION.md"]
        with pytest.raises(result_contract.ControllerError, match="missing pinned criterion"):
            result_contract.validate_saved(root, current, text, contracts=contracts)
    assert main(["show", report["run-dir"], "--json"], harnesses=repo[1]) == 0
    assert len(json.loads(capsys.readouterr().out)["observations"]) == 4


def test_missing_capture_stops_before_launch(tmp_path, monkeypatch, capsys):
    repo = _project(tmp_path, monkeypatch, installed=False)
    capture = result_contract.capture_contract

    def incomplete(root=None):
        return {k: v for k, v in capture(root).items() if k != "workflow-state/COLLECTION.md"}

    monkeypatch.setattr(result_contract, "capture_contract", incomplete)
    assert main(["kb/notes/alpha.md", "--criteria", "collection"], harnesses=repo[1]) == 2
    assert "missing pinned criterion" in capsys.readouterr().err
    assert repo[2].read_text() == ""


def test_evidence_corruption_is_not_a_worker_correction(tmp_path, monkeypatch, capsys):
    repo = _project(tmp_path, monkeypatch, installed=False)
    complete = result_contract.complete

    def corrupt(root, path, fragment, **kwargs):
        raw = root / kwargs["metadata"]["raw-output"]
        raw.write_bytes(raw.read_bytes() + b"tampered")
        return complete(root, path, fragment, **kwargs)

    monkeypatch.setattr(result_contract, "complete", corrupt)
    code, report, launches = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 1 and len(launches) == 1
    assert report["pairs"][0]["state"] == "controller-error"
    assert "hash mismatch" in report["stopped"]
    [path] = (repo[0] / report["run-dir"] / "artifact/reviews").glob("*/observation.json")
    record = observations.load(path.parent)
    assert record["state"] == "controller-error" and record["content-rejections"] == 0
    assert any(e["event"] == "controller-error" for e in record["diagnostics"])
    assert not list((repo[0] / "kb/workflow-state/data/current/review/results").rglob("*.md"))


def test_real_registry_fixture_selector_uses_claude_code(tmp_path, monkeypatch, capsys):
    root, fake, log = _project(tmp_path, monkeypatch, installed=False)
    # Keep the real registry identity and adapter name; replace only its process
    # implementation so this production-selection test cannot call a model.
    monkeypatch.setitem(HARNESSES, "claude-code", fake["fake"])
    profile = root / "kb/instructions/review-profiles.yaml"
    profile.write_text(profile.read_text().replace("harness: fake", "harness: claude-code"))
    repo = root, HARNESSES, log
    code, report, _ = review(repo, capsys, "kb/notes/alpha.md", "--criteria", "prose/body-gate")
    assert code == 0
    [path] = (root / report["run-dir"] / "artifact/reviews").glob("*/observation.json")
    fixture = fixtures.create(root, report["run-dir"], path.parent.name, substitute_executor=True)
    assert main(["--fixture", fixture.relative_to(root).as_posix()]) == 0
    trial = json.loads(capsys.readouterr().out)
    assert not trial["stopped"] and not trial["changed"]
