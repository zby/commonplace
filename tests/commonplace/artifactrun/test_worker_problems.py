"""Worker evidence is independent of closure, content checks and current failures."""

import json
from dataclasses import replace

import pytest

from commonplace.artifactrun import AttemptResult, inspect
from commonplace.artifactrun.engine import _close
from commonplace.artifactrun.inspection import run_inspection
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from commonplace.cli.run import main
from tests.commonplace.artifactrun.support import COMPLETE_BRIEF

REPORT = "  Required worker check could not run.\n\nDetails remain unverified.  \n"


def problem_entry(handout, state="completed", text=REPORT):
    return {"id": handout.attempt, "job": handout.job, "state": state, "problem": text}


def test_completed_run_retains_problem_and_cli_exposes_it(coordinator, capsys):
    c = coordinator
    handout = c.handout("brief")
    handout.problem.write_text(REPORT, encoding="utf-8")
    c.through_publication()
    assert not handout.prompt.parent.exists()
    view = run_inspection(c.run_dir, final_job="assemble")
    assert view["state"] == "completed" and view["publishable"]
    assert view["worker-problems"] == [problem_entry(handout)]
    assert view["failed-attempts"] == []
    assert view["attempts"][0]["problem"] == REPORT
    assert any("every worker obligation" in text for text in view["limitations"])
    assert main(["status", str(c.run_dir), "--json"]) == 0
    cli = json.loads(capsys.readouterr().out)
    assert cli["worker_problems"] == view["worker-problems"]
    assert cli["attempts"][0]["problem"] == REPORT
    assert main(["status", str(c.run_dir)]) == 0
    text = capsys.readouterr().out
    assert f"worker problem {handout.attempt} brief (completed):\n{REPORT}" in text
    assert "every reported problem resolved" in text


def test_problem_without_output_survives_failure_and_correction(coordinator):
    c = coordinator
    handout = c.handout("brief")
    handout.problem.write_text(REPORT, encoding="utf-8")
    c.advance(AttemptResult(handout.attempt))
    assert c.stop("brief") and not handout.prompt.parent.exists()
    view = inspect(c.run_dir)
    assert view["worker_problems"] == [problem_entry(handout, "failed")]
    assert view["attempts"][0]["problem"] == REPORT
    c.advance()
    c.complete("brief", COMPLETE_BRIEF)
    view = run_inspection(c.run_dir, final_job="assemble")
    assert view["failed-attempts"] == []
    assert view["worker-problems"] == [problem_entry(handout, "failed")]


@pytest.mark.parametrize("refused", [False, True])
def test_problem_remains_visible_after_content_check(coordinator, refused):
    c = coordinator
    c.through_brief()
    handout = c.handout("report")
    handout.problem.write_text(REPORT, encoding="utf-8")
    c.complete("report", "REFUSE\n" if refused else "report A\n", answers="")
    view = run_inspection(c.run_dir, final_job="assemble")
    assert view["worker-problems"] == [problem_entry(handout)]
    assert bool(view["refusals"]) is refused
    if refused:
        assert any(item["job"] == "report" for item in view["refusals"])
    else:
        assert any(j["outcome"] == "accepted" and j["job"] == "check-report"
                   for j in RunStore(c.run_dir).judgment_records())
    assert set(view["worker-problems"][0]) == {"id", "job", "state", "problem"}, "no resolution claim"


@pytest.mark.parametrize("outcome", ["completed", "failed"])
@pytest.mark.parametrize("conflicting", [False, True])
def test_first_closure_preserves_report_without_another_event(coordinator, outcome, conflicting):
    c = coordinator
    handout = c.handout("brief")
    c.write(handout, COMPLETE_BRIEF)
    handout.problem.write_text(REPORT, encoding="utf-8")
    store = RunStore(c.run_dir)
    first = AttemptResult(handout.attempt, outcome, reason="first")
    _close(Run(store), first)
    records = store.attempt_records()
    judgments = store.judgment_records()
    assert records[0]["problem"] == REPORT
    second = replace(first, outcome="failed" if outcome == "completed" else "completed") if conflicting else first
    assert _close(Run(store), second) is None
    assert store.attempt_records() == records
    assert store.judgment_records() == judgments
    assert inspect(c.run_dir)["worker_problems"] == [problem_entry(handout, outcome)]


@pytest.mark.parametrize("outcome", ["completed", "failed"])
def test_persistence_failure_keeps_handout_evidence(coordinator, monkeypatch, outcome):
    c = coordinator
    handout = c.handout("brief")
    c.write(handout, COMPLETE_BRIEF)
    handout.problem.write_text(REPORT, encoding="utf-8")
    store = RunStore(c.run_dir)
    original = store.write_json

    def fail_record(path, record):
        if path.parent == store.attempts:
            raise OSError("attempt persistence failed")
        return original(path, record)

    monkeypatch.setattr(store, "write_json", fail_record)
    with pytest.raises(OSError, match="attempt persistence failed"):
        _close(Run(store), AttemptResult(handout.attempt, outcome))
    assert store.attempt_records()[0]["state"] == "open"
    assert handout.problem.read_text(encoding="utf-8") == REPORT
    assert handout.outputs["brief"].is_file()
    monkeypatch.setattr(store, "write_json", original)
    _close(Run(store), AttemptResult(handout.attempt, outcome))
    assert store.attempt_records()[0]["problem"] == REPORT
    assert not handout.prompt.parent.exists()


def test_older_record_without_problem_is_not_evidence_of_no_problem(coordinator):
    c = coordinator
    c.through_brief()
    store = RunStore(c.run_dir)
    record = store.attempt_records()[0]
    record.pop("problem")
    store.write_json(store.attempts / f"{record['id']}.json", record)
    view = run_inspection(c.run_dir, final_job="assemble")
    assert view["worker-problems"] == []
    assert view["attempts"][0]["problem"] is None
    assert any("not recorded" in text for text in view["limitations"])


def test_full_decoded_report_preserves_line_endings_and_replaces_bad_utf8(coordinator):
    c = coordinator
    handout = c.handout("brief")
    raw = b"  check failed\r\n\r\n\xff details\r\n  "
    handout.problem.write_bytes(raw)
    c.through_brief()
    view = inspect(c.run_dir)
    decoded = raw.decode("utf-8", errors="replace")
    assert view["attempts"][0]["problem"] == decoded
    assert view["worker_problems"] == [problem_entry(handout, text=decoded)]


def test_whitespace_report_is_retained_but_not_displayed_as_substantive(coordinator):
    c = coordinator
    handout = c.handout("brief")
    handout.problem.write_text(" \n\t\n", encoding="utf-8")
    c.through_brief()
    view = inspect(c.run_dir)
    assert view["attempts"][0]["problem"] == " \n\t\n"
    assert view["worker_problems"] == []
