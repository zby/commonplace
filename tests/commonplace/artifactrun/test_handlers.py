"""The standard apply handler's verification protocol, on the toy plan's verifier."""

from __future__ import annotations

from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import NO_BLOCKERS, Coordinator, blocking


def applied(c: Coordinator) -> dict[str, dict]:
    """The latest apply-verification attempt's judgments, by subject role."""
    run = Run(RunStore(c.run_dir))
    attempt = run.latest_completed("apply-verification")["id"]
    return {j["subject"]["role"]: j for j in run.judgments if j["attempt"] == attempt}


def test_one_blocker_refuses_its_subject_and_leaves_the_others_unsettled(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verify", blocking("report: r1"))
    judged = applied(c)
    assert judged["report"]["outcome"] == "refused"
    assert "## Blockers\n\n- report: r1\n" in judged["report"]["findings"]
    assert "other" not in judged and "summary" not in judged, "an unaddressed subject is not judged"
    assert judged["verification"]["outcome"] == "accepted", "a verdict with blockers is a valid document"
    assert not any(e["relation"].startswith("verification:verifies:") for e in judged["verification"]["scope"])


def test_a_blocker_free_verdict_accepts_every_subject(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verify", NO_BLOCKERS)
    judged = applied(c)
    for role in ("report", "other", "summary"):
        assert judged[role]["outcome"] == "accepted"
        assert [e["relation"] for e in judged[role]["scope"]] == [f"verification:verifies:{role}"]


def test_a_subject_failing_validation_is_refused_with_blockers_none(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    verifier = c.handout("verify")
    # The contract changes while the verifier holds report A.
    c.forbid("report A")
    c.advance()
    c.advance(c.result_for(verifier, NO_BLOCKERS))
    judged = applied(c)
    assert judged["report"]["outcome"] == "refused"
    findings = judged["report"]["findings"]
    assert "forbidden text 'report A'" in findings and "## Blockers\n\nnone\n" in findings
    assert judged["other"]["outcome"] == judged["summary"]["outcome"] == "accepted"


def test_a_verdict_breaking_the_protocol_judges_nothing_else(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verify", "## Blockers\n\n- the report is wrong\n\n## Limits\n\nnone\n")
    judged = applied(c)
    assert set(judged) == {"verification"}
    assert judged["verification"]["outcome"] == "refused"
    assert "blocker addresses none of report, other, summary" in judged["verification"]["findings"]


def test_a_verdict_without_limits_is_refused(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verify", "## Blockers\n\nnone\n")
    judged = applied(c)
    assert set(judged) == {"verification"} and judged["verification"]["outcome"] == "refused"
    assert "## Limits is missing" in judged["verification"]["findings"]


def set_checked(tmp_path, monkeypatch) -> Coordinator:
    """A toy run with a set check over the record roles, under the report's contract."""
    from tests.commonplace.artifactrun.support import CONTRACT, STANDARD, custom_run

    def add(jobs):
        jobs["set-check"] = {
            "name": "set-check", "kind": "code", "handler": f"{STANDARD}.set_check", "criteria": ["toy"],
            "outputs": ["findings"],
            "inputs": {"contract": {"address": "file", "source": CONTRACT},
                       **{role: {"address": "role", "source": role, "required": False}
                          for role in ("brief", "report", "other", "summary")}},
        }

    return custom_run(tmp_path, monkeypatch, add)


def test_the_set_check_writes_findings_over_the_members(tmp_path, tmp_library, monkeypatch) -> None:
    from commonplace.artifactrun import current_outputs
    from commonplace.artifactrun.handlers import set_check
    from commonplace.artifactrun.run import CodeAttempt, Resolved
    from tests.commonplace.artifactrun.support import as_member

    c = set_checked(tmp_path, monkeypatch)
    c.through_records()
    assert current_outputs(c.run_dir, "set-check") == {"findings": b"# Set check\n\nnone\n"}
    run = Run(RunStore(c.run_dir))
    attempt = run.latest_completed("set-check")["id"]
    assert not [j for j in run.judgments if j["attempt"] == attempt], "the set check judges nothing"

    # The engine runs the set check only on accepted members; a snapshot
    # holding a failing report shows what it writes.
    job = run.jobs.job("set-check")
    pins = {name: run.resolve(name, job.inputs) for name in job.inputs}
    pins["report"] = Resolved("v", as_member("report", "REFUSE\n").encode(), "report", "report")
    findings = set_check(CodeAttempt(run, job, pins))["findings"].decode()
    assert findings.startswith("# Set check\n\n- report.md: ") and "refused pattern REFUSE" in findings
