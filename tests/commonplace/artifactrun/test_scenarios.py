"""The scenarios of kb/work/workflow-requirements/scenarios.md, one test each.

`R` is the toy `report` job, `check-R` is `check-report`, `V` is `verify`
with `apply-verification`, `reconcile` is `summary` and `profile` is
`digest`; see conftest.py. Assertions use only the public surface: run
status, members in `set/`, hand-out files and the handlers' call log.
"""

from __future__ import annotations

import pytest

from commonplace.workflow import AttemptResult, judge, start_run
from tests.commonplace.workflow.handlers import INTERRUPT_ENV
from tests.commonplace.workflow.support import BLOCKED_BRIEF, Coordinator


def refuse_report(c: Coordinator, reason: str = "r1") -> None:
    """From a verification hand-out, have V block the report."""
    c.complete("verify", f"block report: {reason}\n")
    assert "report" in c.handed()


def correct_report(c: Coordinator, report: str, summary: str) -> None:
    """Answer the report's refusal and carry the change to the next verification."""
    c.complete("report", report, answers="answered\n")
    c.complete("summary", summary)
    assert "verify" in c.handed()


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


@pytest.mark.parametrize(("other", "refused"), [
    ("other O1\n", False),
    ("other O1\nneeds report: report A\n", True),
])
def test_06_upstream_replaced_downstream_rejudged(coordinator: Coordinator, other: str, refused: bool) -> None:
    c = coordinator
    c.through_records(other=other)
    refuse_report(c)
    c.ran()
    c.complete("report", "report B\n", answers="answered\n")
    assert "check-other" in c.ran(), "check-other has the report as an input"
    # other has the report only as untracked context; it reruns only when
    # check-other refuses it against B.
    assert ("other" in c.handed()) == refused


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
    assert "report" not in c.handed(), "three failed attempts exhaust max attempts"
    c.stop("report")


def test_11_code_job_failure_stops_every_time(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_brief()
    c.ran()
    c.advance(c.result("report", "report CRASH\n", answers=""))
    c.stop("check-report")
    for _ in range(3):
        c.advance()
        c.stop("check-report")
    assert c.ran() == ["check-report"] * 4, "code jobs have no max attempts"




def test_code_jobs_run_to_a_fixed_point_within_one_invocation(coordinator: Coordinator) -> None:
    c = coordinator
    c.ran()
    c.through_brief(BLOCKED_BRIEF)
    assert c.ran() == ["check-brief", "assemble"], "assemble became ready from check-brief's acceptance"


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
    manifest = c.run_dir / "set" / "ARTIFACT.yaml"
    manifest.write_text("type: something/else.md\n", encoding="utf-8")
    c.advance()
    assert c.member("report") == "report A\n"
    assert manifest.read_text(encoding="utf-8") == "type: types/toy-set.md\n"


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


def test_14_complete_disposition_does_not_assemble_a_partial_set(coordinator: Coordinator) -> None:
    c = coordinator
    c.ran()
    c.through_brief()
    assert "assemble" not in c.ran(), "coverage of the set minus the overview does not hold yet"
    assert not c.status.stops, "assembly waits; it does not fail"
    c.advance(c.result("report", "report A\n", answers=""), c.result("other", "other O1\n"))
    c.complete("summary", "summary S1\n")
    c.complete("verify", "no blockers\n")
    assert "assemble" not in c.ran(), "the digest is still required"
    c.complete("digest", "digest D1\n")
    assert "assemble" in c.ran() and c.member("overview") is not None


def test_09_rerecording_an_unchanged_claim_does_not_reassemble(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    c.ran()
    judge(c.run_dir, role="report", outcome="accepted", scope=("verification:cites:report",),
          basis=("verification",), findings="the same claim again")
    c.advance()
    assert c.ran() == [], "coverage names claims, not records"
    assert c.status.publishable


def test_14_a_member_whose_acceptance_stopped_holding_blocks_publication(
        tmp_path, tmp_library, monkeypatch) -> None:
    from tests.commonplace.workflow.support import custom_run

    def edit(jobs):
        jobs["check-brief"]["inputs"]["contract"] = dict(jobs["check-report"]["inputs"]["contract"])

    c = custom_run(tmp_path, monkeypatch, edit)
    c.through_brief(BLOCKED_BRIEF)
    assert c.status.publishable
    (c.method / "contract-report.md").write_text("# Edited contract\n", encoding="utf-8")
    from commonplace.workflow.state import Run
    from commonplace.workflow.store import RunStore

    assert not Run(RunStore(c.run_dir)).publishable(), "the brief's only acceptance no longer holds"
    c.advance()
    assert c.status.publishable, "the check re-accepts the brief against the edited contract"


def test_16_structural_acceptance_does_not_replenish_max_attempts(coordinator: Coordinator) -> None:
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
    c = coordinator
    c.through_records()
    c.complete("verify", "block report: r1\n")
    assert "report" in c.handed()
    c.ran()
    c.edit_method("contract-report.md", "# Changed contract\n")
    c.advance()
    assert "check-report" not in c.ran(), "an input of check-report changed, but the report job is pending"
    assert c.member("report") == "report A\n"
    c.complete("report", "report B\n", answers="answered r1\n")
    assert c.ran().count("check-report") == 1, "one check of B, no redundant re-acceptance of A"
    assert c.member("report") == "report B\n"


@pytest.mark.parametrize(("scope", "basis", "supersedes"), [
    (("verification:cites:report",), ("verification",), True),
    (("report:cites:brief",), ("brief",), False),
])
def test_17_acceptance_supersedes_a_refusal_only_within_its_scope(
        coordinator: Coordinator, scope: tuple[str, ...], basis: tuple[str, ...], supersedes: bool) -> None:
    from commonplace.workflow.engine import inspect

    c = coordinator
    c.through_records()
    refuse_report(c)
    assert [r.job for r in inspect(c.run_dir)["refusals"]] == ["report"]
    judge(c.run_dir, role="report", outcome="accepted", scope=scope, basis=basis)
    in_force = [r.job for r in inspect(c.run_dir)["refusals"]]
    assert ("report" not in in_force) == supersedes


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


# Scenario 21 is test_late_completed_verdict_applies_before_ready_or_exhausted_rerun
# in test_completed_handed_scheduling.py, which also covers an exhausted verifier.


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


def test_type_is_fixed_for_the_run(coordinator: Coordinator) -> None:
    c = coordinator
    type_file = c.method.parent.parent / "types" / "toy-set.md"
    type_file.write_text("not a type any more\n", encoding="utf-8")
    c.through_brief()
    assert "report" in c.handed(), "the run kept the type it started with"


def test_check_job_refuses_to_run_on_a_moved_member(coordinator: Coordinator, monkeypatch) -> None:
    c = coordinator
    c.through_brief()
    from commonplace.workflow import engine

    real = engine._materialize
    calls = {"n": 0}

    def tamper_after_rebuild(run):
        real(run)
        calls["n"] += 1
        brief = run.store.set_dir / "brief.md"
        if brief.exists():
            brief.write_text("changed behind the engine's back\n", encoding="utf-8")

    monkeypatch.setattr(engine, "_materialize", tamper_after_rebuild)
    c.ran()
    c.advance(c.result("report", "report A\n", answers=""))
    assert "pinned version of brief" in c.stop("check-report").reason
    assert c.ran() == [], "the handler did not run"
    monkeypatch.setattr(engine, "_materialize", real)
    c.advance()
    assert c.ran() == ["check-report"], "the next invocation rebuilds the set and runs the job"
    assert c.member("report") == "report A\n"


def test_handout_prompt_keeps_the_legacy_shape(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_brief()
    handout = c.handout("report")
    prompt = handout.prompt.read_text(encoding="utf-8").splitlines()
    assert prompt[0] == f"Follow {c.method / 'report.md'} with:", "the instruction is handed at its own path"
    values = dict(line.split(" = ", 1) for line in prompt if " = " in line)
    assert values["system"] == "toy"
    assert values["validation-member"] == str(c.run_dir / "set" / "report.md")
    assert values["output"] == str(handout.outputs["report"])
    assert values["output-answers"] == str(handout.outputs["answers"])
    assert values["refusal"] == "absent"
    assert values["problem"] == str(handout.problem)
    assert values["scratch"].endswith("/scratch/")
    assert "## Input reading batches" in prompt
    assert any(line.startswith("1. ") and values["brief"] in line for line in prompt)


def test_start_refuses_missing_run_parameters(tmp_path, tmp_library) -> None:
    from tests.commonplace.workflow.support import toy_library

    declaration, _ = toy_library(tmp_path)
    with pytest.raises(ValueError, match="run parameters not given: subject"):
        start_run(tmp_path / "runs" / "bare", declaration)
