"""Regression tests for final closure, retries and bounded candidate priority."""

from dataclasses import replace

import pytest
import yaml

from commonplace.artifactrun import AttemptResult, advance, start_run
from commonplace.artifactrun.engine import _close
from commonplace.artifactrun.plan import CodeJob
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import (
    COMPLETE_BRIEF,
    CONTRACT,
    Coordinator,
    toy_library,
    version,
)


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
        assert record["outputs"]["brief"] == version("brief", COMPLETE_BRIEF)
    else:
        assert record["reason"] == "first"
        if same_batch:
            assert len(c.status.stops) == 1
    assert not handout.prompt.parent.exists()




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
    c.edit_method("brief.md", "changed again")
    c.advance()
    assert c.stop("brief").reason == "max attempts (3) exhausted", "the failed attempt counted"


def test_failed_code_retries_after_inputs_revert(coordinator, monkeypatch):
    c = coordinator
    c.through_brief()
    c.advance(c.result("report", "report A\n"), c.result("other", "other O1\n"))
    original = c.contract.read_text()
    resolve = CodeJob.resolve_handler
    calls = []

    def handler(job):
        if job.name != "check-report":
            return resolve(job)

        def check(attempt):
            calls.append(next(attempt.read(name) for name, spec in attempt.inputs.items()
                              if spec.source == CONTRACT))
            if len(calls) == 1:
                raise RuntimeError("temporary failure")
            return resolve(job)(attempt)

        return check

    monkeypatch.setattr(CodeJob, "resolve_handler", handler)
    c.edit_contract()
    changed = c.contract.read_bytes()
    c.advance()
    assert c.stop("check-report")
    c.contract.write_text(original)
    c.advance()
    assert calls == [changed, original.encode()]
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
        "address": "role", "source": "other", "required": False,
    }
    jobs["other"]["inputs"]["report"] = {
        "address": "role", "source": "report", "order_only": True,
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
    assert run.latest_output(run.jobs.job("report")) == version("report", "runtime B\n")
    assert not run.ready(run.jobs.job("check-report"), run.permitted())
    assert "other" in run.producers(run.jobs.job("check-report"))
    assert c.handed() == {"other"}
    assert run.open_attempt("other")["pins"]["report"]["version"] == version("report", "runtime B\n")
    assert c.member("report") == "runtime B\n"
    check = run.latest_completed("check-report")
    assert check["pins"]["other"]["version"] == version("other", "downstream A\n")
    judgment = next(j for j in run.judgments if j["attempt"] == check["id"])
    assert run.holds(judgment)
    c.complete("other", "downstream B\n")
    run = state(c)
    assert not run.holds(judgment)
    assert run.latest_completed("check-report")["pins"]["other"]["version"] == version("other", "downstream B\n")
    # This is not an immutable-handed-subject application: the peer is live.
    assert not run._consumes_completed_subjects(
        run.jobs.job("check-report"), run.jobs.job("other"),
    )
    assert not advance(c.run_dir).stops
