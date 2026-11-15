"""Consumer regressions for frozen dispatch and retained-result publication recovery."""
import json
from pathlib import Path

from commonplace.cli.review_workflows import main
from commonplace.headless.jobs import Run
from commonplace.lib.review_workflows import observations, result_contract, results
from tests.commonplace.review_workflows.test_gates import (
    BODY_GATE,
    _project,
    note,
    review,
)


def test_dispatch_race_uses_captured_target_and_criterion(tmp_path, monkeypatch, capsys):
    repo = _project(tmp_path, monkeypatch, installed=False)
    root, harnesses, log = repo
    target = "kb/notes/alpha.md"
    anchor = "Original captured passage."
    original_target = note("Alpha", anchor).encode()
    (root / target).write_bytes(original_target)
    original_criterion = (root / BODY_GATE).read_bytes()
    fragment = result_contract.render(
        {"type": result_contract.TYPE, "findings": [
            {"scope": "passage", "quotes": [anchor], "reason": "A captured passage finding.", "level": "warn"}
        ], "outcome": "warn"},
        "# Review\n\n## Summary\n\nThe captured passage warrants a finding.\n",
    )
    # Check actual worker-side input files, not just the controller's request dict.
    script = tmp_path / "fake.py"
    worker = script.read_text().replace(
        'if "CANNOT" in note:',
        f'assert Path(listed("note.md")).read_bytes() == {original_target!r}\n'
        f'assert Path(listed("criterion.md")).read_bytes() == {original_criterion!r}\n'
        'if "CANNOT" in note:',
    ).replace('result = review_text("fail" if "FAILME" in note else "pass")', f"result = {fragment!r}")
    script.write_text(worker)
    original_ask = Run.ask
    mutations = []

    def mutate_before_dispatch(run, *args, **kwargs):
        assert not mutations, "the valid captured answer must require only one launch"
        assert log.read_text() == ""
        snapshot = json.loads((run.root / "review-request.json").read_text())
        assert snapshot["targets"][target].encode() == original_target
        assert snapshot["criteria"][BODY_GATE].encode() == original_criterion
        [record_path] = (run.root / "artifact/reviews").glob("*/observation.json")
        record = observations.load(record_path.parent)
        for role, expected in (("target", original_target), ("criterion", original_criterion)):
            capture = next(item for item in record["inputs"] if item["role"] == role)
            assert (record_path.parent / capture["path"]).read_bytes() == expected
        (root / target).write_text(note("Alpha", "FAILME changed live passage."))
        (root / BODY_GATE).write_bytes(original_criterion + b"\nChanged live criterion.\n")
        mutations.append(True)
        return original_ask(run, *args, **kwargs)

    monkeypatch.setattr(Run, "ask", mutate_before_dispatch)
    code, report, launches = review(repo, capsys, target, "--criteria", "prose/body-gate", "--max-workers", "1")
    assert code == 1, report  # Assessment succeeds, but concurrent edits fail the checkout guard.
    assert mutations == [True]
    assert launches == [f"{target}::{BODY_GATE}"]
    assert report["counts"] == {"reviewed": 1}
    assert report["guard"] == {"clean": False, "changed": sorted([target, BODY_GATE])}
    current = results.read_result(results.result_path(root, target, "prose/body-gate"))
    assert current.outcome == "warn"
    assert current.findings[0]["quotes"] == [anchor]
    assert anchor not in (root / target).read_text()
    assert (root / current.target_capture).read_bytes() == original_target
    record_path = root / current.observation
    record = observations.load(record_path.parent)
    [saved] = record["completed-results"]
    completed = record_path.parent / saved
    assert not result_contract.validate_saved(root, completed, completed.read_text()).fails
    assert main(["status", target, "--criteria", "prose/body-gate", "--json"], harnesses=harnesses) == 0
    [row] = json.loads(capsys.readouterr().out)["pairs"]
    assert row["freshness"] == "stale"
    assert row["changed"] == ["note", "criterion"]
    assert log.read_text().splitlines() == launches


def test_publication_crash_resumes_retained_result_without_new_launch(tmp_path, monkeypatch, capsys):
    repo = _project(tmp_path, monkeypatch, installed=False)
    root, harnesses, log = repo
    target = "kb/notes/alpha.md"
    current_path = results.result_path(root, target, "prose/body-gate")
    interrupted = []

    def crash_before_publication(repo_root, result):
        assert repo_root == root
        record_path = root / result.observation
        record = observations.load(record_path.parent)
        assert record["state"] == "completed"
        [saved] = record["completed-results"]
        retained = record_path.parent / saved
        assert observations.sha(retained.read_bytes()) == record["completed-result-sha256"][saved]
        assert not result_contract.validate_saved(root, retained, retained.read_text()).fails
        assert not current_path.exists(), "publication must not precede retained evidence"
        interrupted.append((result, retained, retained.read_bytes()))
        raise OSError("injected failure after retention, before current publication")

    with monkeypatch.context() as crash:
        crash.setattr(results, "write_result", crash_before_publication)
        assert main(["run", "gates", target, "--criteria", "prose/body-gate", "--max-workers", "1",
                     "--timeout", "30"], harnesses=harnesses) == 2
    assert "injected failure after retention, before current publication" in capsys.readouterr().err
    [(original, retained, completed_bytes)] = interrupted
    assert not current_path.exists()
    assert log.read_text().splitlines() == [f"{target}::{BODY_GATE}"]
    observation_path = root / original.observation
    record = observations.load(observation_path.parent)
    assert record["completed-results"] == [retained.relative_to(observation_path.parent).as_posix()]
    assert retained.read_bytes() == completed_bytes
    launch_root = root / original.run / "calls/launches"
    launch_bytes = {path.relative_to(launch_root): path.read_bytes()
                    for path in launch_root.rglob("*") if path.is_file()}
    log_before = log.read_bytes()

    code, resumed, launches = review(repo, capsys, target, "--criteria", "prose/body-gate",
                                    "--resume", original.run, "--max-workers", "1")
    assert code == 0 and resumed["ok"], resumed
    assert resumed["run-dir"] == original.run
    assert resumed["counts"] == {"reviewed": 1}
    assert launches == [] and log.read_bytes() == log_before
    assert retained.read_bytes() == completed_bytes
    assert {path.relative_to(launch_root): path.read_bytes()
            for path in launch_root.rglob("*") if path.is_file()} == launch_bytes
    assert results.read_result(current_path) == original
    current = results.read_result(current_path)
    for evidence in (current.observation, current.target_capture, current.raw_output):
        assert (root / evidence).is_file()
    final_record = observations.load(root / Path(current.observation).parent)
    assert final_record["state"] == "completed"
    assert final_record["completed-results"] == record["completed-results"]
    assert final_record["completed-result-sha256"] == record["completed-result-sha256"]
    assert results.freshness(root, target, BODY_GATE).state == "fresh"
