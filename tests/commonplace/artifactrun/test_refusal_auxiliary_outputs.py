"""An auxiliary answer can change while the refused subject stays identical.

Scripted toy jobs only: no workers, target execution or retained publication.
Consumer code, not the engine, decides whether a decline is valid.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import (
    NO_BLOCKERS,
    Coordinator,
    blocking,
    covered,
    custom_run,
)

ANSWER = "- declined: the frozen evidence supports the finding.\n"


def completed_reports(c):
    return [record for record in RunStore(c.run_dir).attempt_records()
            if record["job"] == "report" and record["state"] == "completed"]


def decline_run(tmp_path, monkeypatch, *, max_attempts=3, initial_answers=""):
    def edit(jobs):
        jobs["report"]["max-attempts"] = max_attempts
        # The analysis declaration already gives its verifiers these inputs.
        jobs["verification"]["inputs"]["answers"] = {
            "address": "output", "source": "report:answers", "required": False,
        }

    c = custom_run(tmp_path, monkeypatch, edit)
    c.through_brief()
    auxiliary = {} if initial_answers is None else {"answers": initial_answers}
    c.advance(c.result("report", "report A\n", **auxiliary), c.result("other", "other O1\n"))
    c.complete("summary", "summary S1\n")
    c.complete("verification", blocking("report: reconsider the finding"))
    assert c.handed() == {"report"}
    return c


def test_changed_answer_completes_rechecks_and_reverifies_same_subject(tmp_path, tmp_library, monkeypatch):
    c = decline_run(tmp_path, monkeypatch)
    original = completed_reports(c)[0]
    previous_summary = c.member("summary")
    c.ran()
    status = c.complete("report", "report A\n", answers=ANSWER)
    assert not status.stops and c.handed() == {"verification"}
    current = completed_reports(c)[-1]
    assert len(completed_reports(c)) == 2
    assert current["outputs"]["report"] == original["outputs"]["report"]
    assert current["outputs"]["answers"] != original["outputs"]["answers"]
    assert current["pins"]["refusal"]["version"] is not None
    assert "check-report" in c.ran()
    assert c.member("report") == "report A\n" and c.member("summary") == previous_summary
    run = Run(RunStore(c.run_dir))
    assert not covered(run, "verification:verifies:report", "verification", "report")
    report_job = run.jobs.job("report")
    assert not run.ready(report_job, set(run.layout.roles)), "the old refusal was answered, not overridden"
    prompt = c.handout("verification").prompt.read_text()
    answer_path = next(line.split(" = ", 1)[1] for line in prompt.splitlines() if line.startswith("answers = "))
    assert Path(answer_path).read_text() == ANSWER
    c.complete("verification", NO_BLOCKERS)
    assert c.handed() == {"digest"}
    assert covered(Run(RunStore(c.run_dir)), "verification:verifies:report", "verification", "report")


@pytest.mark.parametrize(("initial", "answer", "completes"), [
    (None, ANSWER, True),
    ("unchanged existing answer\n", None, False),
    ("unchanged existing answer\n", "unchanged existing answer\n", False),
])
def test_only_a_newly_present_or_changed_auxiliary_answer_completes(
        tmp_path, tmp_library, monkeypatch, initial, answer, completes):
    c = decline_run(tmp_path, monkeypatch, initial_answers=initial)
    auxiliary = {} if answer is None else {"answers": answer}
    c.complete("report", "report A\n", **auxiliary)
    if completes:
        assert not c.status.stops and c.handed() == {"verification"}
        assert "answers" in completed_reports(c)[-1]["outputs"]
        return
    assert "no new auxiliary version" in c.stop("report").reason
    assert len(completed_reports(c)) == 1
    failed = RunStore(c.run_dir).attempt_records()[-1]
    assert failed["state"] == "failed" and failed["pins"] == {}
    c.advance()
    assert c.handed() == {"report"}


def test_identical_decline_after_a_new_refusal_fails(tmp_path, tmp_library, monkeypatch):
    c = decline_run(tmp_path, monkeypatch)
    c.complete("report", "report A\n", answers=ANSWER)
    c.complete("verification", blocking("report: still not persuaded"))
    assert c.handed() == {"report"}
    c.complete("report", "report A\n", answers=ANSWER)
    assert "unchanged" in c.stop("report").reason
    assert len(completed_reports(c)) == 2
    c.advance()
    assert "max attempts" in c.stop("report").reason
    assert "report" not in c.handed(), "the counted decline attempts are not replenished"


def test_auxiliary_change_without_primary_output_still_fails(tmp_path, tmp_library, monkeypatch):
    c = decline_run(tmp_path, monkeypatch)
    h = c.handout("report")
    result = c.result("report", "report A\n", answers=ANSWER)
    h.outputs["report"].unlink()
    c.advance(result)
    assert "completed without its primary output" in c.stop("report").reason
    assert len(completed_reports(c)) == 1


def test_restoring_bytes_does_not_reanswer_a_historical_refusal(tmp_path, tmp_library, monkeypatch):
    c = decline_run(tmp_path, monkeypatch)
    original_refusal = RunStore(c.run_dir).judgment_records()[-1]
    c.complete("report", "REFUSE\n", answers=ANSWER)
    assert c.handed() == {"report"}
    c.ran()
    c.complete("report", "report A\n", answers=ANSWER + "Restored the structural fields.\n")
    assert not c.status.stops and c.handed() == {"verification"}
    assert "check-report" in c.ran()
    run = Run(RunStore(c.run_dir))
    assert not run.superseded(original_refusal), "completion is not an override"
    assert not covered(run, "verification:verifies:report", "verification", "report")
    assert len(completed_reports(c)) == 3


def test_changed_auxiliary_does_not_accept_a_structurally_refused_primary(coordinator: Coordinator):
    c = coordinator
    c.through_brief()
    c.complete("report", "REFUSE\n", answers="")
    assert c.handed() == {"report"}
    c.ran()
    c.complete("report", "REFUSE\n", answers=ANSWER)
    assert not c.status.stops and "check-report" in c.ran()
    assert c.member("report") is None
    judgments = [j for j in RunStore(c.run_dir).judgment_records() if j["job"] == "check-report"]
    assert [j["outcome"] for j in judgments] == ["refused", "refused"]
