"""Completed verdict application bypasses only its immutable model producer."""

from dataclasses import replace

import pytest
import yaml

from commonplace.workflow import start_run
from commonplace.workflow.declaration import Input
from commonplace.workflow.engine import _close
from commonplace.workflow.handouts import _open
from commonplace.workflow.state import Run
from commonplace.workflow.store import RunStore, digest
from tests.commonplace.workflow.conftest import Coordinator, toy_library
from tests.commonplace.workflow.handlers import LOG_ENV


def run_state(c):
    return Run(RunStore(c.run_dir))


def applications(c):
    return [r for r in run_state(c).attempts.values()
            if r["job"] == "apply-verification" and r["state"] == "completed"]


@pytest.fixture
def late_run(tmp_path, tmp_library, monkeypatch, request):
    declaration, method = toy_library(tmp_path)
    data = yaml.safe_load(declaration.read_text())
    verifier = next(j for j in data["jobs"] if j["name"] == "verify")
    verifier["max_attempts"] = getattr(request, "param", 3)
    # All verifier member inputs remain ordinary currency triggers.
    assert all(not i.get("order_only", False) for i in verifier["inputs"].values())
    declaration.write_text(yaml.safe_dump(data, sort_keys=False))
    log = tmp_path / "handlers.log"
    monkeypatch.setenv(LOG_ENV, str(log))
    directory = tmp_path / "run"
    start_run(directory, declaration, parameters={"subject": "toy"})
    c = Coordinator(directory, method, log)
    c.advance()
    c.through_records()
    old = c.handout("verify")
    c.edit_method("contract-report.md", "forbid: report A\n")
    c.advance()
    c.complete("report", "report B\n", answers="repair\n")
    c.complete("summary", "summary S2\n")
    assert c.member("report") == "report B\n"
    assert not applications(c)
    return c, old


@pytest.mark.parametrize("late_run", [1, 3], indirect=True)
@pytest.mark.parametrize("verdict", ["no blockers\n", "block report: late blocker\n"])
def test_late_completed_verdict_applies_before_ready_or_exhausted_rerun(late_run, verdict):
    c, old = late_run
    c.advance(c.result_for(old, verdict))
    run = run_state(c)
    assert len(applications(c)) == 1
    judgments = [j for j in run.judgments if j["job"] == "apply-verification"]
    subject = next(j for j in judgments if j["subject"]["role"] == "report")
    assert subject["subject"]["version"] == digest(b"report A\n")
    assert subject["outcome"] == ("refused" if "block report" in verdict else "accepted")
    assert not subject["installs"] and not subject["overrides"]
    assert c.member("report") == "report B\n"
    assert run.resolve("refusal", {"refusal": Input("refusal", "report")}).version is None
    assert not run.covered("verification:cites:report", "verification", "report")
    assert not c.status.publishable and "digest" not in c.handed()
    if run.jobs.job("verify").max_attempts == 1:
        assert c.stop("verify").reason == "max attempts (1) exhausted"
        assert not c.handed()
    else:
        assert c.handed() == {"verify"}
        new = run.open_attempt("verify")
        assert new["pins"]["report"]["version"] == digest(b"report B\n")
    c.advance()
    assert len(applications(c)) == 1, "an unchanged completed subject applies only once"


def test_completed_verdict_applies_while_subsequent_verifier_attempt_is_open(late_run):
    c, old = late_run
    # Close V and open its next ready attempt without the intervening code fixed
    # point. This constructs the same supported record state on a later invocation.
    result = c.result_for(old, "no blockers\n")
    run = run_state(c)
    with run.store.lock():
        assert _close(run, result) is None
        run.reload()
        verifier = run.jobs.job("verify")
        assert run.ready(verifier, run.permitted())
        new = _open(run, verifier)
    c.open.pop(old.attempt)
    c.open[new.attempt] = new
    c.advance()
    assert new.attempt in c.status.open_attempts
    assert len(applications(c)) == 1
    assert c.member("report") == "report B\n"
    assert not c.status.publishable and not c.handed()
    c.advance()
    assert len(applications(c)) == 1
    # Identical verdict bytes, but a new attempt record and handed B, apply again.
    c.complete("verify", "no blockers\n")
    assert len(applications(c)) == 2
    latest = [j for j in run_state(c).judgments
              if j["job"] == "apply-verification" and j["subject"]["role"] == "report"][-1]
    assert latest["subject"]["version"] == digest(b"report B\n")
    assert latest["installs"] and not latest["overrides"]
    assert "digest" in c.handed()


def test_report_separates_holding_historical_basis_from_canonical_currency(late_run):
    from commonplace.lib.agentic_engine_report import engine_run_report

    c, old = late_run
    c.advance(c.result_for(old, "no blockers\n"))
    view = engine_run_report(c.run_dir, status=c.status)
    report_drift = [entry for entry in view["canonical-peer-drift"] if entry["role"] == "report"]
    assert report_drift
    assert all(entry["handed"] == digest(b"report A\n") for entry in report_drift)
    assert all(entry["current"] == digest(b"report B\n") for entry in report_drift)
    assert any(entry["judgment"] not in view["stale-acceptances"] for entry in report_drift)
    assert not view["publishable"]


def test_own_answered_refusal_check_retains_scenario17_wait(coordinator):
    c = coordinator
    c.through_records()
    c.complete("verify", "block report: semantic blocker\n")
    run = run_state(c)
    check = run.jobs.job("check-report")
    assert "report" in run.producers(check)
    before = run.attempt_count("check-report")
    # A changed contract makes the check ready while R's correction is open.
    c.edit_method("contract-report.md", "# Changed contract\n")
    c.advance()
    run = run_state(c)
    assert run.ready(check, run.permitted())
    assert run.attempt_count("check-report") == before
    c.complete("report", "report B\n", answers="answer\n")
    assert run_state(c).attempt_count("check-report") == before + 1
    assert c.member("report") == "report B\n"
    c.complete("summary", "summary S2\n")
    c.complete("verify", "block report: second semantic blocker\n")
    run = run_state(c)
    # Even a consumer stripped down to only completed outputs, the attempt and
    # its now-present answered refusal must wait: the handed role is R's own.
    own_refusal_only = replace(check, inputs={
        name: check.inputs[name] for name in ("candidate", "report-attempt", "answered", "answers")
    })
    answered = run.resolve("answered", own_refusal_only.inputs)
    assert answered.version is not None and answered.role == "report"
    assert "report" in run.producers(own_refusal_only)
    assert run.open_attempt("report") is not None


@pytest.mark.parametrize("extra", [
    Input("member", "verification", required=False),
    Input("judgment", "report", required=False,
          relation="verification:cites:report", outcome="accepted"),
    Input("refusal", "verify", required=False),
    Input("handed", "verification-attempt:undeclared", required=False),
])
def test_live_or_undeclared_dependency_prevents_exemption(late_run, extra):
    c, old = late_run
    c.advance(c.result_for(old, "no blockers\n"))
    run = run_state(c)
    apply = run.jobs.job("apply-verification")
    assert "verify" not in run.producers(apply)
    guarded = replace(apply, inputs={**apply.inputs, "extra": extra})
    assert "verify" in run.producers(guarded)


def test_unpinned_output_and_model_consumers_keep_waiting(late_run):
    c, old = late_run
    run = run_state(c)
    apply = run.jobs.job("apply-verification")
    assert "verify" in run.producers(apply), "no completed record exists yet"
    c.advance(c.result_for(old, "no blockers\n"))
    run = run_state(c)
    output_only = replace(apply, inputs={"verdict": apply.inputs["verdict"]})
    assert "verify" in run.producers(output_only)
    order_only_record = replace(apply, inputs={
        **apply.inputs,
        "verification-attempt": replace(apply.inputs["verification-attempt"], order_only=True),
    })
    assert "verify" in run.producers(order_only_record)
    model_consumer = replace(run.jobs.job("digest"), inputs=apply.inputs)
    assert "verify" in run.producers(model_consumer)
    # Exemption is per producer, not a waiver for independent live dependencies.
    mixed = replace(apply, inputs={**apply.inputs, "report-now": Input("member", "report")})
    assert run.producers(mixed) == {"report"}
