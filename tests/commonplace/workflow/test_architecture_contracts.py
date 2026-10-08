"""Contracts the architecture review asked the engine to state and enforce."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from commonplace.workflow import DeclarationError, load_job_set, open_handouts
from tests.commonplace.workflow.support import Coordinator, job_set


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
    (lambda d: d["jobs"][0].update(name="group/brief"), None),
    (lambda d: d["jobs"][0].update(name="operator"), None),
    (lambda d: d["jobs"][0].update(outputs=["../brief"]), None),
    (lambda d: d["jobs"][0]["inputs"].update({"a/b": {"address": "file", "source": "/x"}}), None),
])
def test_declaration_shape(tmp_path: Path, edit, message) -> None:
    data = job_set(tmp_path)
    edit(data)
    with pytest.raises(DeclarationError, match=message):
        load_job_set(yaml.safe_dump(data))


def test_an_interrupted_commit_leaves_its_judgments_invisible(coordinator: Coordinator, monkeypatch) -> None:
    c = coordinator
    c.through_brief()
    from commonplace.workflow import store as store_module

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
    from commonplace.workflow.declaration import CodeJob
    from commonplace.workflow.state import CodeAttempt, Run
    from commonplace.workflow.store import RunStore

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
    from commonplace.workflow.declaration import CodeJob, Input
    from commonplace.workflow.state import CodeAttempt, Resolved, Run
    from commonplace.workflow.store import RunStore

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
    from commonplace.lib.note_parser import parse_document
    from commonplace.workflow.store import digest

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

    from commonplace.workflow.declaration import Input
    from commonplace.workflow.state import Run
    from commonplace.workflow.store import RunStore, digest

    c = coordinator
    c.through_brief()
    c.complete("report", "report A\n", answers="")
    run = Run(RunStore(c.run_dir))
    record = json.loads(run.resolve("r", {"r": Input("attempt", "report")}).data)
    assert set(record) == {"id", "job", "kind", "outputs", "previous_outputs", "model", "effort"}
    assert record["job"] == "report" and record["kind"] == "model"
    assert record["outputs"]["report"] == digest(b"report A\n")
