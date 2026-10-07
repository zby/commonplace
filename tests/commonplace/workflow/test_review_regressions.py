"""Regressions for the engine review: each test reproduces one reported failure."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from commonplace.workflow import DeclarationError, judge, load_job_set, start_run
from tests.commonplace.workflow.conftest import (
    BLOCKED_BRIEF,
    Coordinator,
    job_set,
    toy_library,
)
from tests.commonplace.workflow.handlers import INTERRUPT_ENV, LOG_ENV


def custom_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, edit) -> Coordinator:
    """A toy run whose declaration `edit` changes before the run starts."""
    declaration, method = toy_library(tmp_path)
    data = job_set(method)
    edit({job["name"]: job for job in data["jobs"]})
    declaration.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    log = tmp_path / "handlers.log"
    monkeypatch.setenv(LOG_ENV, str(log))
    monkeypatch.delenv(INTERRUPT_ENV, raising=False)
    run_dir = tmp_path / "runs" / "custom"
    start_run(run_dir, declaration, parameters={"subject": "toy"})
    coordinator = Coordinator(run_dir=run_dir, method=method, log=log)
    coordinator.advance()
    return coordinator


def test_a_file_input_edited_while_open_fails_the_attempt(coordinator: Coordinator) -> None:
    c = coordinator
    c.edit_method("brief.md", "# brief\n\nWrite a different brief.\n")
    c.complete("brief", "---\ndisposition: complete\n---\n# Brief\n")
    assert "file input instruction changed" in c.stop("brief").reason
    c.advance()
    assert c.handed() == {"brief"}, "the job is handed out again under the new instruction"


@pytest.mark.parametrize("edit", [
    lambda d: d["jobs"][0].update(name="group/brief"),
    lambda d: d["jobs"][0].update(name="operator"),
    lambda d: d["jobs"][0].update(outputs=["../brief"]),
    lambda d: d["jobs"][0]["inputs"].update({"a/b": {"address": "file", "source": "/x"}}),
])
def test_filesystem_names_are_checked(tmp_path: Path, edit) -> None:
    data = job_set(tmp_path)
    edit(data)
    with pytest.raises(DeclarationError):
        load_job_set(yaml.safe_dump(data))


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
    c.edit_method("verify.md", "# verify\n\nVerify again.\n")
    c.edit_method("digest.md", "# digest\n\nDigest again.\n")
    c.advance()
    assert "verify" in c.handed()
    assert "digest" not in c.handed(), "digest's gate is produced through the verifier"


def test_a_wait_cycle_stops_with_a_diagnosis(tmp_path: Path, tmp_library: None, monkeypatch: pytest.MonkeyPatch) -> None:
    def reciprocal(jobs):
        jobs["report"]["inputs"]["other"] = {"address": "member", "source": "other", "required": False}
        jobs["other"]["inputs"]["report"] = {"address": "member", "source": "report", "required": False}

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


def test_a_presence_only_input_orders_without_triggering(tmp_path: Path, tmp_library: None,
                                                         monkeypatch: pytest.MonkeyPatch) -> None:
    def after_report(jobs):
        jobs["other"]["inputs"]["report-context"] = {"address": "member", "source": "report", "trigger": False}

    c = custom_run(tmp_path, monkeypatch, after_report)
    c.through_brief()
    assert c.handed() == {"report"}, "other waits until the report is a member"
    c.complete("report", "report A\n", answers="")
    assert "other" in c.handed()
    c.complete("other", "other O1\n")
    c.complete("summary", "summary S1\n")
    c.complete("verify", "block report: r1\n")
    c.complete("report", "report B\n", answers="answered\n")
    assert c.member("report") == "report B\n"
    assert "other" not in c.handed(), "a changed presence-only input is not a rerun trigger"


def test_an_undeclared_relation_is_refused_at_start(tmp_path: Path, tmp_library: None,
                                                    monkeypatch: pytest.MonkeyPatch) -> None:
    def typo(jobs):
        jobs["digest"]["inputs"]["report-verified"]["relation"] = "verification:cites:reprot"

    with pytest.raises(DeclarationError, match="not declared by the type"):
        custom_run(tmp_path, monkeypatch, typo)
