"""Reset is a state transition, not an analytical correctness claim."""
import json
from pathlib import Path

import pytest

from commonplace.artifactrun import inspect
from commonplace.artifactrun.reset import affected_jobs, reset_run
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import CORRECTED, NO_BLOCKERS, blocking


def test_reset_preserves_upstream_and_resumes_correction(coordinator):
    c = coordinator
    c.through_publication()
    before = Run(RunStore(c.run_dir))
    upstream = {name: before.latest_completed(name) for name in ("brief", "report", "other", "summary")}
    seq = int((c.run_dir / "state/seq").read_text())
    report = reset_run(c.run_dir, "verification")
    assert set(report["jobs"]) == {"verification", "apply-verification", "digest", "check-digest", "assemble"}
    archive = Path(report["archive"])
    assert json.loads((archive / "reset.json").read_text())["state"] == "completed"
    assert Run(RunStore(archive / "before")).latest_completed("verification")
    after = Run(RunStore(c.run_dir))
    for name, record in upstream.items():
        assert after.latest_completed(name) == record
    assert after.latest_completed("verification") is None
    assert not inspect(c.run_dir)["publishable"]
    assert not (c.run_dir / "artifact/verification.md").exists()
    c.advance()
    assert c.handed() == {"verification"}
    assert int(c.handout("verification").attempt.partition("-")[0]) > seq
    # No audit feedback: the verifier independently writes an ordinary blocker.
    c.complete("verification", blocking("report: repair report"))
    assert "report" in c.handed()
    assert "repair report" in c.reachable(c.handout("report"))
    c.complete("report", "report repaired\n", answers=CORRECTED)
    # Normal downstream scheduling, rather than a separate re-entry loop.
    c.complete("summary", "summary repaired\n")
    c.complete("verification", NO_BLOCKERS)
    c.complete("digest", "digest repaired\n")
    assert c.status.publishable and not c.status.stops


def test_unknown_job_and_open_attempt_refuse_without_history(coordinator):
    c = coordinator
    with pytest.raises(KeyError):
        affected_jobs(Run(RunStore(c.run_dir)), "unknown")
    with pytest.raises(ValueError, match="idle"):
        reset_run(c.run_dir, "brief")
    assert not (c.run_dir.parent / ".reset-history").exists()


def test_interrupted_apply_is_fenced_and_repeatable(coordinator, monkeypatch):
    from commonplace.artifactrun import reset

    c = coordinator
    c.through_publication()
    original = reset._replace
    calls = 0

    def interrupt(source, destination):
        nonlocal calls
        calls += 1
        original(source, destination)
        if calls == 1:
            raise OSError("simulated interruption")

    monkeypatch.setattr(reset, "_replace", interrupt)
    with pytest.raises(OSError, match="simulated"):
        reset_run(c.run_dir, "verification")
    with pytest.raises(ValueError, match="incomplete"):
        c.advance()
    with pytest.raises(ValueError, match="finish pending"):
        reset_run(c.run_dir, "report")
    marker = json.loads((c.run_dir / reset.PENDING).read_text())
    monkeypatch.setattr(reset, "_replace", original)
    report = reset_run(c.run_dir, "verification")
    assert report["archive"] == marker["archive"]
    assert not (c.run_dir / reset.PENDING).exists()
    c.advance()
    assert c.handed() == {"verification"}


def test_second_reset_renews_budgets_and_never_reuses_old_verdict(coordinator):
    c = coordinator
    c.through_publication()
    first = reset_run(c.run_dir, "verification")
    c.advance()
    c.complete("verification", NO_BLOCKERS)
    c.complete("digest", "digest D2\n")
    assert c.status.publishable
    second = reset_run(c.run_dir, "verification")
    assert second["archive"] != first["archive"]
    c.advance()
    assert c.handed() == {"verification"}
    run = Run(RunStore(c.run_dir))
    assert run.attempt_count("report") == 0
    assert run.latest_completed("report") is not None


def test_cli_and_independent_later_completion(coordinator, capsys):
    import yaml

    from commonplace.cli.run import main

    c = coordinator
    c.through_publication()
    store = RunStore(c.run_dir)
    metadata = store.read_metadata()
    plan = yaml.safe_load(metadata["declaration"])
    # Deliberately place independent work after the reset point. Declaration
    # position and execution time must not alone cause invalidation.
    plan["jobs"].append({"name": "independent", "kind": "code", "handler": "unused.handler",
                         "inputs": {}, "outputs": ["notes"]})
    metadata["declaration"] = yaml.safe_dump(plan)
    store.write_json(store.metadata, metadata)
    seq = store.next_seq()
    record = {"id": f"{seq:06d}-independent", "seq": seq, "job": "independent", "kind": "code",
              "pins": {}, "outputs": {"notes": store.put(b"independent result")}}
    store.commit_attempt(record)
    capsys.readouterr()
    assert main(["reset", str(c.run_dir), "--from", "verification", "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert "independent" not in report["jobs"]
    assert Run(store).latest_completed("independent")["outputs"] == record["outputs"]
    assert main(["reset", str(c.run_dir), "--from", "verification"]) == 0
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 2
    assert lines[0].startswith("reset: ")
    assert lines[1].startswith("debug archive: ")
    assert not any(record["state"] == "open" for record in store.attempt_records())
    assert main(["reset", str(c.run_dir), "--from", "not-a-job"]) == 1
    assert "not-a-job" in capsys.readouterr().err
