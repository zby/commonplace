"""Regression tests for final closure, retries and bounded candidate priority."""

from dataclasses import replace

import pytest
import yaml

from commonplace.workflow import AttemptResult, advance, start_run
from commonplace.workflow.declaration import CodeJob, Input
from commonplace.workflow.engine import _close, _open_model_attempts, _run_code_jobs
from commonplace.workflow.state import Run
from commonplace.workflow.store import RunStore, digest
from tests.commonplace.workflow.conftest import COMPLETE_BRIEF, Coordinator, toy_library


def state(c):
    return Run(RunStore(c.run_dir))


@pytest.mark.parametrize("first_outcome", ["completed", "failed"])
@pytest.mark.parametrize("conflicting", [False, True])
@pytest.mark.parametrize("same_batch", [False, True])
def test_first_closure_is_final(coordinator, first_outcome, conflicting, same_batch):
    c = coordinator
    handout = c.handout("brief")
    c.write(handout, COMPLETE_BRIEF)
    first = AttemptResult(handout.attempt, first_outcome, reason="first", model="first-model")
    second = replace(first, outcome=("failed" if first_outcome == "completed" else "completed"),
                     reason="second", model="second-model") if conflicting else first
    if same_batch:
        c.advance(first, second)
    else:
        c.advance(first)
        before = state(c).attempts[handout.attempt]
        c.advance(second)
        assert state(c).attempts[handout.attempt] == before
    record = state(c).attempts[handout.attempt]
    assert record["state"] == first_outcome
    assert record["model"] == "first-model"
    if first_outcome == "completed":
        assert not c.status.stops
        assert record["outputs"]["brief"] == digest(COMPLETE_BRIEF.encode())
    else:
        assert record["reason"] == "first"
        if same_batch:
            assert len(c.status.stops) == 1
    assert not handout.prompt.parent.exists()


def test_failed_model_retries_after_inputs_revert_and_still_obeys_limits(coordinator):
    c = coordinator
    original = (c.method / "brief.md").read_text()
    c.through_brief()
    c.edit_method("brief.md", "changed")
    c.advance()
    failed = c.handout("brief")
    c.fail("brief", "temporary failure")
    c.edit_method("brief.md", original)
    run = state(c)
    job = run.jobs.job("brief")
    assert run.ready(job, run.permitted())
    assert not run.ready(job, set())
    (c.method / "brief.md").unlink()
    assert not run.ready(job, run.permitted())
    c.edit_method("brief.md", original)
    # The real declaration's two-attempt budget is still enforced.
    c.advance()
    assert c.stop("brief").reason == "max attempts (2) exhausted"
    assert state(c).attempts[failed.attempt]["state"] == "failed"


def test_failed_model_is_handed_out_again_after_inputs_revert(tmp_path, tmp_library):
    declaration, method = toy_library(tmp_path)
    data = yaml.safe_load(declaration.read_text())
    data["jobs"] = data["jobs"][:2]
    data["jobs"][0]["max_attempts"] = 3
    declaration.write_text(yaml.safe_dump(data))
    start_run(tmp_path / "run", declaration)
    c = Coordinator(tmp_path / "run", method, tmp_path / "log")
    c.advance()
    original = (method / "brief.md").read_text()
    c.through_brief()
    c.edit_method("brief.md", "changed")
    c.advance()
    c.fail("brief", "temporary")
    c.edit_method("brief.md", original)
    c.advance()
    assert c.handed() == {"brief"}
    c.complete("brief", COMPLETE_BRIEF)
    assert not c.handed() and not c.status.stops


def test_failed_code_retries_after_inputs_revert(coordinator, monkeypatch):
    c = coordinator
    c.through_brief()
    c.advance(c.result("report", "report A\n"), c.result("other", "other O1\n"))
    original = (c.method / "contract-report.md").read_text()
    resolve = CodeJob.resolve_handler
    calls = []

    def handler(job):
        if job.name != "check-report":
            return resolve(job)

        def check(attempt):
            calls.append(attempt.read("contract"))
            if len(calls) == 1:
                raise RuntimeError("temporary failure")
            return resolve(job)(attempt)

        return check

    monkeypatch.setattr(CodeJob, "resolve_handler", handler)
    c.edit_method("contract-report.md", "changed")
    c.advance()
    assert c.stop("check-report")
    c.edit_method("contract-report.md", original)
    c.advance()
    assert calls == [b"changed", original.encode()]
    assert not c.status.stops
    c.advance()
    assert len(calls) == 2


@pytest.fixture
def pending_candidate(tmp_path, tmp_library):
    """New runtime B is complete; downstream is ready but not yet handed out."""
    declaration, method = toy_library(tmp_path)
    data = yaml.safe_load(declaration.read_text())
    data["jobs"] = data["jobs"][:6]
    jobs = {job["name"]: job for job in data["jobs"]}
    jobs["check-report"]["inputs"]["other"] = {
        "address": "member", "source": "other", "required": False,
    }
    jobs["other"]["inputs"]["report"] = {
        "address": "member", "source": "report", "order_only": True,
    }
    declaration.write_text(yaml.safe_dump(data, sort_keys=False))
    start_run(tmp_path / "run", declaration, parameters={"subject": "toy"})
    c = Coordinator(tmp_path / "run", method, tmp_path / "log")
    c.advance()
    c.through_brief()
    c.complete("report", "runtime A\n")
    c.complete("other", "downstream A\n")
    c.edit_method("brief.md", "changed boundary instruction")
    c.advance()
    c.complete("brief", COMPLETE_BRIEF + "updated\n")
    assert c.handed() == {"report"}
    result = c.result("report", "runtime B\n")
    assert _close(state(c), result) is None
    c.open.pop(result.attempt)
    return c


def test_new_candidate_checked_before_optional_downstream(pending_candidate):
    c = pending_candidate
    c.advance()
    run = state(c)
    assert run.latest_output(run.jobs.job("report")) == digest(b"runtime B\n")
    assert not run.ready(run.jobs.job("check-report"), run.permitted())
    assert "other" in run.producers(run.jobs.job("check-report"))
    assert c.handed() == {"other"}
    assert run.open_attempt("other")["pins"]["report"]["version"] == digest(b"runtime B\n")
    assert c.member("report") == "runtime B\n"
    check = run.latest_completed("check-report")
    assert check["pins"]["other"]["version"] == digest(b"downstream A\n")
    judgment = next(j for j in run.judgments if j["attempt"] == check["id"])
    assert run.holds(judgment)
    c.complete("other", "downstream B\n")
    run = state(c)
    assert not run.holds(judgment)
    assert run.latest_completed("check-report")["pins"]["other"]["version"] == digest(b"downstream B\n")
    # This is not an immutable-handed-subject application: the peer is live.
    assert not run._consumes_completed_subjects(
        run.jobs.job("check-report"), run.jobs.job("other"),
    )
    assert not advance(c.run_dir).stops


@pytest.mark.parametrize("case", [
    "required-peer", "judgment-gate", "open-peer", "consumed-candidate",
    "auxiliary-output", "no-candidate", "ordinary-dependency", "optional-dependency",
    "unrelated-dependency",
])
def test_candidate_priority_has_narrow_boundaries(pending_candidate, case):
    c = pending_candidate
    run = state(c)
    check = run.jobs.job("check-report")
    peer = run.jobs.job("other")
    assert run.ready(check, run.permitted())
    assert run.ready(peer, run.permitted())
    assert run.checks_before_downstream(check, peer)
    inputs = dict(check.inputs)
    if case == "required-peer":
        inputs["other"] = Input("member", "other")
    elif case == "judgment-gate":
        # Even an optional gate must keep its live-producer wait.
        inputs["gate"] = Input("judgment", "other", required=False, outcome="accepted")
    elif case == "open-peer":
        run.attempts["open-peer"] = {"job": "other", "state": "open"}
    elif case == "consumed-candidate":
        last = run.latest_completed(check.name)
        last["pins"]["candidate"]["version"] = digest(b"runtime B\n")
        c.edit_method("contract-report.md", "new criterion only")
        assert run.ready(check, run.permitted())
    elif case == "auxiliary-output":
        inputs["candidate"] = Input("output", "report:answers", required=False)
    elif case == "no-candidate":
        inputs.pop("candidate")
    else:
        dependencies = dict(peer.inputs)
        dependencies["report"] = Input(
            "member", "brief" if case == "unrelated-dependency" else "report",
            required=case != "optional-dependency", order_only=case != "ordinary-dependency",
        )
        peer = replace(peer, inputs=dependencies)
    check = replace(check, inputs=inputs)
    assert "other" in run.producers(check)
    assert not run.checks_before_downstream(check, peer)
    if case not in {"open-peer", "consumed-candidate"}:
        replacements = {check.name: check, peer.name: peer}
        run.jobs = replace(run.jobs, jobs=tuple(
            replacements.get(job.name, job) for job in run.jobs.jobs
        ))
        previous = run.latest_completed(check.name)["id"]
        assert _run_code_jobs(run) is None
        assert run.latest_completed(check.name)["id"] == previous
        handouts, stops = _open_model_attempts(run)
        assert not stops
        assert {handout.job for handout in handouts} == {"other"}
        assert run.members()["report"] == digest(b"runtime A\n")
