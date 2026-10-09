"""The standard apply handler's verification protocol, on the toy plan's verifier."""

from __future__ import annotations

from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import (
    NO_BLOCKERS,
    Coordinator,
    blocking,
    custom_run,
)


def applied(c: Coordinator) -> dict[str, dict]:
    """The latest apply-verification attempt's judgments, by subject role."""
    run = Run(RunStore(c.run_dir))
    attempt = run.latest_completed("apply-verification")["id"]
    return {j["subject"]["role"]: j for j in run.judgments if j["attempt"] == attempt}


def test_one_blocker_refuses_its_subject_and_leaves_the_others_unsettled(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verification", blocking("report: r1"))
    judged = applied(c)
    assert judged["report"]["outcome"] == "refused"
    assert "## Blockers\n\n- report: r1\n" in judged["report"]["findings"]
    assert "other" not in judged and "summary" not in judged, "an unaddressed subject is not judged"
    assert judged["verification"]["outcome"] == "accepted", "a verdict with blockers is a valid document"
    assert not any(e["relation"].startswith("verification:verifies:") for e in judged["verification"]["scope"])


def test_a_blocker_free_verdict_accepts_every_subject(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verification", NO_BLOCKERS)
    judged = applied(c)
    for role in ("report", "other", "summary"):
        assert judged[role]["outcome"] == "accepted"
        assert [e["relation"] for e in judged[role]["scope"]] == [f"verification:verifies:{role}"]


def test_a_verdict_dependent_finding_refuses_its_subject_with_blockers_none(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    # The toy type's rule: the summary repeats each Limit of the verification.
    c.complete("verification", blocking(limits=("the toy is small",)))
    judged = applied(c)
    assert judged["summary"]["outcome"] == "refused"
    findings = judged["summary"]["findings"]
    assert "limit not carried: the toy is small" in findings and "## Blockers\n\nnone\n" in findings
    assert "## Limits\n\n- the toy is small\n" in findings
    assert judged["report"]["outcome"] == judged["other"]["outcome"] == "accepted"


def test_a_finding_the_subject_shows_alone_is_left_to_its_check(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    verifier = c.handout("verification")
    # The contract changes while the verifier holds report A; check-report refuses A.
    c.forbid("report A")
    c.advance()
    c.advance(c.result_for(verifier, NO_BLOCKERS))
    judged = applied(c)
    assert judged["report"]["outcome"] == "accepted", "the verdict causes no finding at the report"
    refusals = [r for r in Run(RunStore(c.run_dir)).judgments
                if r["outcome"] == "refused" and r["subject"]["role"] == "report"]
    assert [r["job"] for r in refusals] == ["check-report"]


def test_a_verdict_breaking_the_protocol_judges_nothing_else(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verification", "## Blockers\n\n- the report is wrong\n\n## Limits\n\nnone\n")
    judged = applied(c)
    assert set(judged) == {"verification"}
    assert judged["verification"]["outcome"] == "refused"
    assert "blocker addresses none of report, other, summary" in judged["verification"]["findings"]


def test_a_verdict_without_limits_is_refused(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verification", "## Blockers\n\nnone\n")
    judged = applied(c)
    assert set(judged) == {"verification"} and judged["verification"]["outcome"] == "refused"
    assert "## Limits is missing" in judged["verification"]["findings"]


def set_checked(tmp_path, monkeypatch) -> Coordinator:
    """A toy run with a set check over the record roles, under the report's contract."""
    from tests.commonplace.artifactrun.support import CONTRACT, STANDARD

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


def vetoed(check) -> list[str]:
    """A declared check: refuse a candidate containing VETO."""
    return ["[declared] the candidate is vetoed"] if b"VETO" in check.data else []


def see_also(role, blockers, verdict) -> str:
    """A declared feedback function: one line naming the role and its blocker count."""
    return f"\n## See also\n\n{role}: {len(blockers)} blocker(s)\n"


def test_a_declared_check_refuses_through_the_standard_check(tmp_path, tmp_library, monkeypatch) -> None:
    c = custom_run(tmp_path, monkeypatch, lambda entries: entries["report"].update(checks=[f"{__name__}.vetoed"]),
                   compact=True)
    c.through_brief()
    c.advance(c.result("report", "report VETO\n", answers=""), c.result("other", "other O1\n"))
    assert "report" in c.handed()
    refusal = [j for j in Run(RunStore(c.run_dir)).judgments if j["job"] == "check-report"][-1]
    assert refusal["outcome"] == "refused" and "the candidate is vetoed" in refusal["findings"]


def test_declared_feedback_is_appended_to_a_subject_refusal(tmp_path, tmp_library, monkeypatch) -> None:
    c = custom_run(tmp_path, monkeypatch, lambda entries: entries["verification"].update(
        feedback=f"{__name__}.see_also"), compact=True)
    c.through_records()
    c.complete("verification", blocking("report: r1"))
    assert applied(c)["report"]["findings"].endswith("## See also\n\nreport: 1 blocker(s)\n")


def test_the_frozen_source_role_must_pin_a_source(tmp_path, tmp_library, monkeypatch) -> None:
    import yaml

    from commonplace.artifactrun import start_run
    from tests.commonplace.artifactrun.support import toy_library

    declaration, method = toy_library(tmp_path, compact=True)
    data = yaml.safe_load(declaration.read_text())
    data["frozen-source"] = "brief"  # The toy brief pins no source.
    declaration.write_text(yaml.safe_dump(data, sort_keys=False))
    start_run(tmp_path / "run", declaration, parameters={"subject": "toy"})
    c = Coordinator(tmp_path / "run", method, tmp_path / "handlers.log")
    c.advance()
    c.through_brief()
    c.advance(c.result("report", "report A\n", answers=""), c.result("other", "other O1\n"))
    assert "has no source field" in c.stop("check-report").reason
