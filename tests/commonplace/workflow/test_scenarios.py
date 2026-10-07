"""The scenarios of kb/work/workflow-requirements/scenarios.md, one test each.

`R` is the toy `report` job, `check-R` is `check-report`, `V` is `verify`
with `apply-verification`, `reconcile` is `summary` and `profile` is
`digest`; see conftest.py. Assertions use only the public surface: run
status, members in `set/`, hand-out files and the handlers' call log.
"""

from __future__ import annotations

import pytest

from commonplace.workflow import AttemptResult, judge, start_run
from tests.commonplace.workflow.conftest import BLOCKED_BRIEF, Coordinator
from tests.commonplace.workflow.handlers import INTERRUPT_ENV


def refuse_report(c: Coordinator, reason: str = "r1") -> None:
    """From a verification hand-out, have V block the report."""
    c.complete("verify", f"block report: {reason}\n")
    assert "report" in c.handed()


def correct_report(c: Coordinator, report: str, summary: str) -> None:
    """Answer the report's refusal and carry the change to the next verification."""
    c.complete("report", report, answers="answered\n")
    c.complete("summary", summary)
    assert "verify" in c.handed()


def test_start_run_refuses_an_existing_run(coordinator: Coordinator) -> None:
    with pytest.raises(FileExistsError):
        start_run(coordinator.run_dir, coordinator.method / "jobs.yaml")


def test_01_first_attempt_accepted(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_brief()
    c.ran()
    c.advance(c.result("report", "report A\n", answers=""))
    assert c.ran() == ["check-report"]
    assert c.member("report") == "report A\n"
    assert "report" not in c.handed()


def test_02_refuse_correct_accept(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    refuse_report(c)
    c.complete("report", "report B\n", answers="fixed r1\n")
    assert c.member("report") == "report B\n"
    assert "report" not in c.handed(), "a lapsed refusal input is not a change"
    assert "summary" in c.handed()
    c.complete("summary", "summary S2\n")
    c.complete("verify", "no blockers\n")
    assert "report" not in c.handed()
    assert "digest" in c.handed()


def test_03_verifier_waits_for_a_refused_producer(coordinator: Coordinator) -> None:
    # Scenario 3 as written cannot arise under the proposed upstream wait:
    # V reruns only after every refused producer of its inputs has answered.
    c = coordinator
    c.through_records()
    c.complete("verify", "block report: r1\nblock other: o1\n")
    c.complete("other", "other O2\n")
    assert "summary" not in c.handed(), "the report job, a producer of its input, is open"
    assert "verify" not in c.handed()
    c.complete("report", "report B\n", answers="answered\n")
    assert "summary" in c.handed()
    assert "verify" not in c.handed(), "the summary job is ready"


def test_04_second_refusal_and_the_bound(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    refuse_report(c, "r1")
    correct_report(c, "report B\n", "summary S2\n")
    refuse_report(c, "r2")
    correct_report(c, "report C\n", "summary S3\n")
    c.complete("verify", "block report: r3\n")
    assert "report" not in c.handed()
    c.stop("report")


def test_05_waiting_for_a_settled_stage(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    refuse_report(c)
    assert "digest" not in c.handed(), "the verification still has blockers"
    correct_report(c, "report B\n", "summary S2\n")
    c.complete("verify", "no blockers\n")
    assert "digest" in c.handed()
    c.complete("digest", "digest D1\n")

    c.edit_method("contract-report.md", "forbid: report B\n")
    c.advance()
    assert "report" in c.handed()
    c.complete("report", "report C\n", answers="answered\n")
    assert c.member("report") == "report C\n"
    assert "digest" not in c.handed(), "the acceptance of B no longer names the current member"
    c.complete("summary", "summary S3\n")
    c.complete("verify", "no blockers\n")
    assert "digest" in c.handed()


def test_06_upstream_replaced_downstream_rejudged(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    refuse_report(c)
    c.ran()
    c.complete("report", "report B\n", answers="answered\n")
    assert "check-other" in c.ran(), "check-other has the report as an input"
    assert "other" not in c.handed(), "other has the report only as untracked context"


def test_06_rejudged_downstream_refused(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records(other="other O1\nneeds report: report A\n")
    refuse_report(c)
    c.complete("report", "report B\n", answers="answered\n")
    assert "other" in c.handed(), "check-other refused the other report against B"


def test_07_identical_rerun(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    c.edit_method("summary.md", "# summary\n\nWrite the summary, carefully.\n")
    c.advance()
    assert "summary" in c.handed()
    c.ran()
    c.complete("summary", "summary S1\n")
    assert "verify" not in c.handed()
    assert c.ran() == []
    assert c.status.publishable


def test_08_criteria_change(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    c.ran()
    c.edit_method("contract-report.md", "forbid: report A\n")
    c.advance()
    assert "check-report" in c.ran()
    assert "report" in c.handed()
    assert c.member("report") == "report A\n"
    assert not c.status.publishable


def test_09_operator_refusal_makes_the_producer_ready(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    judge(c.run_dir, role="report", outcome="refused", findings="the operator wants a second look")
    c.advance()
    assert "report" in c.handed(), "an operator refusal is an ordinary refusal"
    assert "the operator wants a second look" in c.reachable(c.handout("report"))
    # Scenario 9's caveat: the refusal changed no acceptance's basis, so the set
    # still counts as publishable; the operator holds publication or waits.
    assert c.status.publishable


def test_09_operator_override_names_the_refusal(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    c.edit_method("contract-report.md", "forbid: report A\n")
    c.advance()
    assert "report" in c.handed(), "the check refused A under the new contract"
    from commonplace.workflow.engine import inspect

    refusal = next(r for r in inspect(c.run_dir)["refusals"] if r.job == "report")
    judge(c.run_dir, role="report", outcome="accepted", scope=("report:cites:brief",), basis=("brief",),
          overrides=(refusal.id,), findings="the operator accepts A as it stands")
    c.advance()
    assert c.member("report") == "report A\n"
    assert c.handout("report").attempt in c.status.open_attempts, "an open hand-out is not recalled"
    assert "report" not in c.handed(), "the superseded refusal does not make R ready again"


def test_09_judging_history_is_evidence_only(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    refuse_report(c)
    c.complete("report", "report B\n", answers="answered\n")
    from commonplace.workflow.store import digest

    judge(c.run_dir, role="report", outcome="accepted", version=digest(b"report A\n"))
    c.advance()
    assert c.member("report") == "report B\n", "an acceptance of an earlier version moves nothing"


def test_10_publication_blocked_by_an_acceptance_that_stopped_holding(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    c.edit_method("summary.md", "# summary\n\nWrite the summary again.\n")
    c.advance()
    c.complete("summary", "summary S2\n")
    assert c.member("summary") == "summary S2\n"
    assert "verify" in c.handed()
    assert not c.status.publishable
    c.complete("verify", "no blockers\n")
    assert c.status.publishable


def test_11_worker_reports_a_problem(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_brief()
    for _ in range(3):
        handout = c.handout("report")
        handout.problem.write_text("the source is unreadable\n", encoding="utf-8")
        c.fail("report", "worker reported a problem")
        assert "the source is unreadable" in c.stop("report").reason, "the problem text is the record"
        c.advance()
    assert "report" not in c.handed(), "three failed attempts exhaust the bound"
    c.stop("report")


def test_11_code_job_failure_stops_every_time(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_brief()
    c.ran()
    c.advance(c.result("report", "report CRASH\n", answers=""))
    c.stop("check-report")
    c.advance()
    c.stop("check-report")
    assert c.ran() == ["check-report", "check-report"]


def test_12_interrupted_invocation_resumes(coordinator: Coordinator, monkeypatch: pytest.MonkeyPatch) -> None:
    c = coordinator
    c.through_records()
    result = c.result("verify", "no blockers\n")
    monkeypatch.setenv(INTERRUPT_ENV, "apply-verification")
    with pytest.raises(KeyboardInterrupt):
        c.advance(result)
    monkeypatch.delenv(INTERRUPT_ENV)
    c.ran()
    c.advance(result)
    assert c.ran() == ["apply-verification"], "no job runs twice unless an input changed"
    assert "digest" in c.handed()


def test_12_tampered_member_is_rematerialized(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    (c.run_dir / "set" / "report.md").write_text("bytes with no record\n", encoding="utf-8")
    c.advance()
    assert c.member("report") == "report A\n"


def test_12_killed_worker_is_closed_by_a_report(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_brief()
    handout = c.handout("report")
    partial = handout.outputs["report"]
    partial.write_text("report part\n", encoding="utf-8")
    c.fail("report", "worker killed")
    c.stop("report")
    c.advance()
    assert "report" in c.handed(), "a failed attempt records no inputs"
    assert not (partial.exists() and partial.read_text(encoding="utf-8") == "report part\n")


@pytest.mark.skip(reason="a half-written publication is an external effect the consumer owns")
def test_12_partial_publication() -> None:
    ...


def test_13_parallel_handouts_one_at_a_time(coordinator: Coordinator) -> None:
    # Under the proposed upstream wait, summary waits for the second analyst
    # instead of running once per analyst, as scenario 13 still describes.
    c = coordinator
    c.through_records()
    c.complete("verify", "block report: r1\nblock other: o1\n")
    open_other = c.handout("other")
    c.complete("report", "report B\n", answers="answered\n")
    assert "summary" not in c.handed()
    assert "other" not in c.handed()
    assert open_other.attempt in c.status.open_attempts
    c.advance(c.result_for(open_other, "other O2\n"))
    assert "summary" in c.handed()


def test_13_parallel_handouts_together(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verify", "block report: r1\nblock other: o1\n")
    c.advance(c.result("report", "report B\n", answers="answered\n"), c.result("other", "other O2\n"))
    c.handout("summary")
    c.complete("summary", "summary S2\n")
    assert "summary" not in c.handed()
    assert "verify" in c.handed()


def test_14_non_complete_disposition(coordinator: Coordinator) -> None:
    c = coordinator
    c.ran()
    c.through_brief(BLOCKED_BRIEF)
    assert c.handed() == set()
    assert "assemble" in c.ran()
    assert c.member("overview") is not None
    assert c.status.publishable


def test_15_identical_bytes_after_a_refusal(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    refuse_report(c)
    c.complete("report", "report A\n", answers="answered\n")
    c.stop("report")
    c.advance()
    assert "report" in c.handed()


def test_16_structural_acceptance_does_not_replenish_the_bound(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    for version, summary in (("B", "S2"), ("C", "S3")):
        refuse_report(c)
        c.ran()
        correct_report(c, f"report {version}\n", f"summary {summary}\n")
        assert "check-report" in c.ran(), "each correction passed its structural check"
    c.complete("verify", "block report: r\n")
    assert "report" not in c.handed()
    c.stop("report")


def test_17_recheck_waits_for_the_refused_producer(coordinator: Coordinator) -> None:
    # Scenario 17's redundant re-acceptance of A no longer happens under the
    # proposed upstream wait: check-report waits while the report job is ready.
    c = coordinator
    c.through_records()
    c.ran()
    c.complete("verify", "block report: r1\n")
    assert "check-report" not in c.ran()
    assert "report" in c.handed()
    assert c.member("report") == "report A\n"
    c.complete("report", "report B\n", answers="answered r1\n")
    assert c.member("report") == "report B\n"


def test_18_input_versions_are_fixed_at_handout(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_brief()
    c.advance(c.result("report", "report A\n", answers=""), c.result("other", "other O1\n"))
    open_summary = c.handout("summary")
    assert "report A" in c.reachable(open_summary)
    c.edit_method("contract-report.md", "forbid: report A\n")
    c.advance()
    c.complete("report", "report B\n", answers="answered\n")
    assert "summary" not in c.handed()
    c.advance(c.result_for(open_summary, "summary S1\n"))
    assert "summary" in c.handed(), "the completed attempt recorded A, and B is current"


def test_19_cleanup_spares_an_open_attempt(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    c.complete("verify", "block report: r1\nblock other: o1\n")
    open_other = c.handout("other")
    partial = open_other.outputs["other"]
    partial.write_text("other half-written\n", encoding="utf-8")
    c.complete("report", "report B\n", answers="answered\n")
    assert partial.read_text(encoding="utf-8") == "other half-written\n"
    assert "other" not in c.handed()
    assert open_other.attempt in c.status.open_attempts
    c.advance(AttemptResult(open_other.attempt, outcome="failed", reason="worker killed"))
    c.advance()
    assert not (partial.exists() and partial.read_text(encoding="utf-8") == "other half-written\n")


def test_20_rerun_with_its_previous_output(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_records()
    refuse_report(c, "r1")
    c.complete("report", "report B\n", answers="answered\n")
    assert "summary S1" in c.reachable(c.handout("summary"))
    c.complete("summary", "summary S2\n")
    assert "block report: r1" in c.reachable(c.handout("verify"))


def test_21_late_verdict_about_a_replaced_version(coordinator: Coordinator) -> None:
    # The upstream wait keeps V from being handed out while R is pending, so
    # the race needs R to become ready after V opened: a criteria change.
    c = coordinator
    c.through_records()
    open_verify = c.handout("verify")
    c.edit_method("contract-report.md", "forbid: report A\n")
    c.advance()
    c.complete("report", "report B\n", answers="answered\n")
    assert c.member("report") == "report B\n"
    c.advance(c.result_for(open_verify, "no blockers\n"))
    assert c.member("report") == "report B\n", "a judgment of A is evidence only"
    assert "report" not in c.handed(), "A's refusal is not B's refusal input"
    assert "digest" not in c.handed(), "nothing accepted B against a verification"
    assert not c.status.publishable
    c.complete("summary", "summary S2\n")
    assert "verify" in c.handed(), "the verifier judged A; B is current"


def test_22_identical_verdict_text_about_different_inputs(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    c.edit_method("contract-report.md", "forbid: report A\n")
    c.advance()
    c.complete("report", "report B\n", answers="answered\n")
    c.complete("summary", "summary S1\n")
    c.ran()
    c.complete("verify", "no blockers\n")
    assert "apply-verification" in c.ran(), "the verifier's attempt record changed"
    assert "digest" in c.handed()
