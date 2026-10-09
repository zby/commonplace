"""Contracts the architecture review asked the engine to state and enforce."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import Input, PlanError, load_plan, open_handouts
from tests.commonplace.artifactrun.support import Coordinator, plan


@pytest.mark.parametrize("edit, message", [
    (lambda d: d["jobs"][0].update(outputs="brief"), "outputs must be a list"),
    (lambda d: d.update(jobs={"brief": {}}), "jobs must be a list"),
    (lambda d: d["jobs"][0]["inputs"].update({"output": {"address": "file", "source": "/x"}}), "hand-out field"),
    (lambda d: d["jobs"][0]["inputs"].update({"previous-brief": {"address": "file", "source": "/x"}}),
     "hand-out field"),
    (lambda d: d["jobs"][0].update(outputs=["brief", "brief"]), "unique"),
    (lambda d: d["jobs"][0].update(parameters={"where": "{nowhere}"}), "unknown placeholder"),
    (lambda d: d["jobs"][2]["inputs"].update({"self": {"address": "member", "source": "report"}}),
     "own role as input"),
    (lambda d: d["jobs"][1].update(max_attempts=3), "unknown keys"),
    (lambda d: d["jobs"][1]["inputs"].update({"c": {"address": "coverage", "source": "brief"}}), "derived"),
    (lambda d: d["jobs"][1].update(criteria=["absent"]), "no criteria group"),
    (lambda d: (d.update(criteria={"g": {"candidate": "contract.md"}}), d["jobs"][1].update(criteria=["g"])),
     "disagrees with criteria group"),
    (lambda d: d["jobs"][0].update(name="group/brief"), None),
    (lambda d: d["jobs"][0].update(name="operator"), None),
    (lambda d: d["jobs"][0].update(outputs=["../brief"]), None),
    (lambda d: d["jobs"][0]["inputs"].update({"a/b": {"address": "file", "source": "/x"}}), None),
])
def test_declaration_shape(tmp_path: Path, edit, message) -> None:
    data = plan(tmp_path)
    edit(data)
    with pytest.raises(PlanError, match=message):
        load_plan(yaml.safe_dump(data))


def test_an_interrupted_commit_leaves_its_judgments_invisible(coordinator: Coordinator, monkeypatch) -> None:
    c = coordinator
    c.through_brief()
    from commonplace.artifactrun import store as store_module

    real = store_module.RunStore._write_attempt

    def die_before_completion(self, record):
        if record["state"] == "completed" and record["job"] == "check-report":
            raise KeyboardInterrupt("killed between judgments and the attempt record")
        real(self, record)

    monkeypatch.setattr(store_module.RunStore, "_write_attempt", die_before_completion)
    with pytest.raises(KeyboardInterrupt):
        c.advance(c.result("report", "report A\n", answers=""))
    assert any((c.run_dir / "state" / "judgments").glob("*check-report*")), "the judgments were written"
    monkeypatch.setattr(store_module.RunStore, "_write_attempt", real)
    c.ran()
    c.advance()
    assert c.ran() == ["check-report"], "the uncommitted attempt does not count, so the check runs again"
    assert c.member("report") == "report A\n"


def test_open_handouts_survive_a_lost_response(coordinator: Coordinator) -> None:
    c = coordinator
    (lost,) = c.status.handouts
    recovered = open_handouts(c.run_dir)
    assert recovered == (lost,)


def test_code_attempt_exposes_fixed_read_only_run_metadata(coordinator: Coordinator, monkeypatch) -> None:
    from commonplace.artifactrun.plan import CodeJob
    from commonplace.artifactrun.run import CodeAttempt, Run
    from commonplace.artifactrun.store import RunStore

    c = coordinator
    run = Run(RunStore(c.run_dir))
    attempt = CodeAttempt(run, CodeJob("probe", {}, (), "x.y"), {})
    assert attempt.parameters == {"subject": "toy"}
    with pytest.raises(TypeError):
        attempt.parameters["subject"] = "changed"
    with pytest.raises(AttributeError):
        attempt.parameters = {}
    assert run.parameters == {"subject": "toy"}
    run.parameters["subject"] = "mutated internal view"
    assert attempt.parameters == {"subject": "toy"}
    assert attempt.run_dir == c.run_dir.resolve()
    type_file = c.method.parent.parent / "types" / "toy-set.md"
    type_file.write_text("not a type any more\n", encoding="utf-8")
    assert attempt.type_text != type_file.read_text(), "the type text is the copy fixed at start"
    assert "report" in attempt.layout.roles
    assert ("verification", "report", "verification:cites:report") in attempt.relations
    recorded_library = attempt.library
    monkeypatch.setenv("COMMONPLACE_LIBRARY_ROOT", "/not-the-recorded-library")
    assert attempt.library == recorded_library
    with pytest.raises(AttributeError):
        attempt.run_dir = c.run_dir.parent
    with pytest.raises(AttributeError):
        attempt.library = c.run_dir.parent
    with pytest.raises(KeyError, match="declares no input"):
        attempt.read("run.json")


def test_a_scope_with_two_partner_versions_is_refused(coordinator: Coordinator) -> None:
    from commonplace.artifactrun.plan import CodeJob, Input
    from commonplace.artifactrun.run import CodeAttempt, Resolved, Run
    from commonplace.artifactrun.store import RunStore

    c = coordinator
    c.through_records()
    run = Run(RunStore(c.run_dir))
    job = CodeJob("probe", {"a": Input("member", "report"), "b": Input("member", "report"),
                            "s": Input("member", "summary")}, (), "x.y")
    pins = {"a": Resolved("v1", b"", "report", "report"), "b": Resolved("v2", b"", "report", "report"),
            "s": Resolved("s1", b"", "summary", "summary")}
    attempt = CodeAttempt(run, job, pins)
    attempt.judge("s", outcome="accepted", scope=("summary:cites:report",))
    with pytest.raises(ValueError, match="2 versions of report"):
        attempt.judgments({}, 1, "probe")


def test_refusal_input_has_the_published_format(coordinator: Coordinator) -> None:
    from commonplace.artifactrun.store import digest
    from commonplace.lib.note_parser import parse_document

    c = coordinator
    c.through_records()
    c.complete("verify", "block report: r1\n")
    prompt = c.handout("report").prompt.read_text(encoding="utf-8").splitlines()
    path = Path(dict(line.split(" = ", 1) for line in prompt if " = " in line)["refusal"])
    document, error = parse_document(path.read_text(encoding="utf-8"))
    assert error is None and set(document.frontmatter) == {"refusal", "version", "scope"}
    assert document.frontmatter["version"] == digest(b"report A\n")
    assert document.frontmatter["scope"] == ["verification:cites:report"]
    assert document.body == "r1", "the findings, verbatim"


def test_attempt_record_input_has_only_the_published_fields(coordinator: Coordinator) -> None:
    import json

    from commonplace.artifactrun.plan import Input
    from commonplace.artifactrun.run import Run
    from commonplace.artifactrun.store import RunStore, digest

    c = coordinator
    c.through_brief()
    c.complete("report", "report A\n", answers="")
    run = Run(RunStore(c.run_dir))
    record = json.loads(run.resolve("r", {"r": Input("attempt", "report")}).data)
    assert set(record) == {"id", "job", "kind", "outputs", "previous_outputs", "model", "effort"}
    assert record["job"] == "report" and record["kind"] == "model"
    assert record["outputs"]["report"] == digest(b"report A\n")


def test_inspection_reports_the_run_condition_and_current_completions(coordinator: Coordinator) -> None:
    from commonplace.artifactrun import current_outputs, inspect, run_lock

    c = coordinator
    assert inspect(c.run_dir)["condition"] == "running", "the brief is handed out"
    c.through_publication()
    with run_lock(c.run_dir):  # Re-entered by inspect and current_outputs without deadlock.
        assert inspect(c.run_dir)["condition"] == "publishable"
        assert current_outputs(c.run_dir, "summary") == {"summary": b"summary S1\n"}
    c.edit_method("summary.md", "# summary\n\nWrite it again.\n")
    assert current_outputs(c.run_dir, "summary") is None, "a changed input makes the completion stale"
    assert inspect(c.run_dir)["condition"] == "publishable", "no member has changed yet"


def test_inspection_reports_a_run_stopped_by_exhausted_attempts(coordinator: Coordinator) -> None:
    from commonplace.artifactrun import inspect

    c = coordinator
    c.through_brief()
    c.complete("other", "other O1\n")
    for _ in range(3):
        c.handout("report").problem.write_text("unreadable\n", encoding="utf-8")
        c.fail("report", "worker reported a problem")
        c.advance()
    view = inspect(c.run_dir)
    assert view["exhausted_jobs"] == ["report"] and view["condition"] == "stopped"


def test_inspection_reports_a_run_stuck_on_an_uncovered_relation(
        tmp_path: Path, tmp_library: None, monkeypatch) -> None:
    from commonplace.artifactrun import inspect
    from tests.commonplace.artifactrun.support import custom_run

    # check-other never sees the report, so no check covers other:cites:report.
    c = custom_run(tmp_path, monkeypatch, lambda jobs: jobs["check-other"]["inputs"].pop("report"))
    c.through_records()
    c.complete("verify", "no blockers\n")
    c.complete("digest", "digest D1\n")
    view = inspect(c.run_dir)
    assert not c.handed() and not view["failed_attempts"] and not view["exhausted_jobs"]
    assert view["condition"] == "stuck"


def test_criteria_groups_expand_into_ordinary_file_inputs(tmp_path: Path) -> None:
    data = plan(tmp_path)
    data["criteria"] = {"contracts": {"contract": "contracts/report.md", "shared": "contracts/shared.md"}}
    data["jobs"][1]["criteria"] = ["contracts"]
    job = load_plan(yaml.safe_dump(data)).job(data["jobs"][1]["name"])
    assert job.inputs["contract"] == Input("file", "contracts/report.md")
    assert job.inputs["shared"] == Input("file", "contracts/shared.md")
