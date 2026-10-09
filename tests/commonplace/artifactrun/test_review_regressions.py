"""Regressions for the engine review: each test reproduces one reported failure."""

from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.artifactrun import PlanError, judge
from tests.commonplace.artifactrun.support import (
    BLOCKED_BRIEF,
    CORRECTED,
    Coordinator,
    blocking,
    custom_run,
)


def test_a_file_input_edited_while_open_fails_the_attempt(coordinator: Coordinator) -> None:
    c = coordinator
    c.edit_method("brief.md", "# brief\n\nWrite a different brief.\n")
    c.complete("brief", "---\ndisposition: complete\n---\n# Brief\n")
    assert "file input instruction changed" in c.stop("brief").reason
    c.advance()
    assert c.handed() == {"brief"}, "the job is handed out again under the new instruction"


def test_an_operator_refusal_reaches_a_job_that_declared_no_refusal_input(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    judge(c.run_dir, role="digest", outcome="refused", findings="redo the digest")
    c.advance()
    assert "digest" in c.handed()
    with pytest.raises(ValueError, match="filled by no model job"):
        judge(c.run_dir, role="overview", outcome="refused", findings="nothing can answer this")


def test_a_gate_waits_for_the_verifier_behind_its_judgment(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    c.edit_method("verification.md", "# verify\n\nVerify again.\n")
    c.edit_method("digest.md", "# digest\n\nDigest again.\n")
    c.advance()
    assert "verification" in c.handed()
    assert "digest" not in c.handed(), "digest's gate is produced through the verifier"


def test_a_wait_cycle_stops_with_a_diagnosis(tmp_path: Path, tmp_library: None, monkeypatch: pytest.MonkeyPatch) -> None:
    def reciprocal(jobs):
        jobs["report"]["inputs"]["other"] = {"address": "role", "source": "other", "required": False}
        jobs["other"]["inputs"]["report"] = {"address": "role", "source": "report", "required": False}

    c = custom_run(tmp_path, monkeypatch, reciprocal)
    c.through_brief()
    assert c.handed() == set()
    (stop,) = c.status.stops
    assert stop.reason.startswith("scheduling stalled")
    assert "report waits for other" in stop.reason and "other waits for report" in stop.reason


def test_a_disposition_change_retires_members_it_no_longer_permits(coordinator: Coordinator) -> None:
    c = coordinator
    c.through_publication()
    judge(c.run_dir, role="brief", outcome="refused", findings="the system is out of scope")
    c.advance()
    c.complete("brief", BLOCKED_BRIEF)
    assert c.member("report") is None, "a role the disposition does not permit has no member"
    assert c.member("overview") is not None
    assert c.status.publishable


def test_relative_file_inputs_resolve_against_the_library(tmp_path: Path, tmp_library: None,
                                                          monkeypatch: pytest.MonkeyPatch) -> None:
    def relative(jobs):
        jobs["brief"]["inputs"]["instruction"]["source"] = "instructions/toy/brief.md"

    c = custom_run(tmp_path, monkeypatch, relative)
    assert c.handed() == {"brief"}
    prompt = c.handout("brief").prompt.read_text(encoding="utf-8")
    assert prompt.splitlines()[0] == f"Follow {tmp_path / 'kb' / 'instructions/toy/brief.md'} with:"


def test_an_order_only_input_orders_without_triggering(tmp_path: Path, tmp_library: None,
                                                         monkeypatch: pytest.MonkeyPatch) -> None:
    def after_report(jobs):
        jobs["other"]["inputs"]["report-context"] = {"address": "role", "source": "report", "order_only": True}

    c = custom_run(tmp_path, monkeypatch, after_report)
    c.through_brief()
    assert c.handed() == {"report"}, "other waits until the report is a member"
    c.complete("report", "report A\n", answers="")
    assert "other" in c.handed()
    c.complete("other", "other O1\n")
    c.complete("summary", "summary S1\n")
    c.complete("verification", blocking("report: r1"))
    c.complete("report", "report B\n", answers=CORRECTED)
    assert c.member("report") == "report B\n"
    assert "other" not in c.handed(), "a changed order-only input is not a rerun trigger"


def test_an_undeclared_relation_is_refused_at_start(tmp_path: Path, tmp_library: None,
                                                    monkeypatch: pytest.MonkeyPatch) -> None:
    def typo(jobs):
        jobs["digest"]["inputs"]["report-verified"]["relation"] = "verification:verifies:reprot"

    with pytest.raises(PlanError, match="not declared by the type"):
        custom_run(tmp_path, monkeypatch, typo)


def test_a_judgment_does_not_lapse_on_an_order_only_input(tmp_path: Path, tmp_library: None,
                                                           monkeypatch: pytest.MonkeyPatch) -> None:
    def summary_record_order_only(jobs):
        jobs["check-summary"]["inputs"]["summary-attempt"] = {
            "address": "attempt", "source": "summary", "order_only": True}

    c = custom_run(tmp_path, monkeypatch, summary_record_order_only)
    c.through_publication()
    c.edit_method("summary.md", "# summary\n\nWrite it again.\n")
    c.advance()
    c.ran()
    c.complete("summary", "summary S1\n")
    assert c.ran() == [], "a new record of identical bytes is no signal"
    assert c.status.publishable, "so the check's acceptance keeps holding"


def test_a_check_reruns_when_an_optional_partner_disappears_for_good(tmp_path: Path, tmp_library: None,
                                                                     monkeypatch: pytest.MonkeyPatch) -> None:
    """A disposition that keeps the summary but retires what it cited.

    The summary's acceptance rested on the report and the other; once they are
    gone it stops holding, and nothing would renew it unless the check reran
    over the remaining snapshot.
    """
    import yaml

    from commonplace.artifactrun import start_run
    from tests.commonplace.artifactrun.handlers import INTERRUPT_ENV, LOG_ENV
    from tests.commonplace.artifactrun.support import (
        TOY_TYPE,
        record_calls,
        toy_library,
    )

    declaration, method = toy_library(tmp_path, compact=True)
    toy = yaml.safe_load(yaml.safe_dump(TOY_TYPE))
    toy["layout"]["required"]["by"]["values"]["partial"] = ["summary"]
    (tmp_path / "kb/types/toy-set.md").write_text(
        "---\n" + yaml.safe_dump(toy, sort_keys=False) + "---\n\n# Toy set\n", encoding="utf-8")
    log = tmp_path / "handlers.log"
    monkeypatch.setenv(LOG_ENV, str(log))
    monkeypatch.delenv(INTERRUPT_ENV, raising=False)
    record_calls(monkeypatch)
    start_run(tmp_path / "run", declaration, parameters={"subject": "toy"})
    c = Coordinator(run_dir=tmp_path / "run", method=method, log=log)
    c.advance()
    c.through_publication()
    c.ran()
    judge(c.run_dir, role="brief", outcome="refused", findings="narrow the scope")
    c.advance()
    c.complete("brief", "---\ndisposition: partial\n---\n# Brief\n")
    assert c.member("report") is None and c.member("summary") is not None
    assert "check-summary" in c.ran(), "the summary's acceptance lapsed with its partners; the check renews it"
    assert c.status.publishable
