"""Model judgment gates remain engine inputs, not worker-delivered evidence."""

from pathlib import Path

import pytest
import yaml

from commonplace.artifactrun import PlanError, open_handouts, start_run
from commonplace.artifactrun.handouts import prompt_variable_names
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import (
    NO_BLOCKERS,
    Coordinator,
    blocking,
    record_calls,
    toy_library,
)
from tests.commonplace.artifactrun.test_prompt_section import SECTION, sectioned_run

pytestmark = pytest.mark.usefixtures("tmp_library")


def test_judgment_gates_are_required_and_pinned_but_not_delivered(tmp_path, monkeypatch):
    c = sectioned_run(tmp_path, monkeypatch)
    c.through_records()
    run = Run(RunStore(c.run_dir))
    job = run.jobs.job("digest")
    gates = {name for name, spec in job.inputs.items() if spec.address == "judgment"}
    assert gates == {"report-verified", "other-verified"}
    assert "digest" not in c.handed()
    assert not run.ready(job, run.permitted())
    assert gates.isdisjoint(prompt_variable_names(job, run.layout))

    c.complete("verification", NO_BLOCKERS)
    handout = c.handout("digest")
    text = handout.prompt.read_text()
    run = Run(RunStore(c.run_dir))
    pins = run.attempts[handout.attempt]["pins"]
    for gate in gates:
        assert gate not in text
        assert not (handout.prompt.parent / "inputs" / f"{gate}.md").exists()
        assert pins[gate]["version"] is not None
        assert run.store.get(pins[gate]["version"])
    # Actual reports and their types remain available to the model.
    assert "report = " in text and "report-type = " in text
    assert (handout.prompt.parent / "inputs" / "report.md").is_file()
    # The unchanged code path can still resolve every gate's bytes.
    for gate in gates:
        assert run.resolve(gate, job.inputs).data == run.store.get(pins[gate]["version"])


def test_relative_run_delivers_absolute_paths_on_open_retry_and_resume(tmp_path, monkeypatch):
    declaration, method = toy_library(tmp_path, compact=True)
    (method / "section.md").write_text(SECTION)
    data = yaml.safe_load(declaration.read_text())
    data["prompt-section"] = "section.md"
    report = next(job for job in data["jobs"] if job.get("role") == "report")
    report.setdefault("parameters", {}).update({
        "capture-directory": "{run}/sources",
        "source-anchor": "src/example.py",
    })
    declaration.write_text(yaml.safe_dump(data, sort_keys=False))
    record_calls(monkeypatch)
    monkeypatch.chdir(tmp_path)
    start_run(Path("run"), declaration, parameters={"subject": "toy"})
    c = Coordinator(Path("run"), method, tmp_path / "handlers.log")
    c.advance()

    def check(handout, *, retry=False):
        paths = [handout.prompt, *handout.outputs.values(), handout.problem,
                 handout.worker_identity]
        assert all(path.is_absolute() for path in paths)
        text = handout.prompt.read_text()
        head = text.split("\n\n", 1)[0]
        assert Path(head.splitlines()[0].removeprefix("Follow ").removesuffix(" with:")).is_absolute()
        values = dict(line.split(" = ", 1) for line in head.splitlines() if " = " in line)
        run = Run(RunStore(c.run_dir))
        job = run.jobs.job(handout.job)
        names = {name for name, spec in job.inputs.items()
                 if spec.address != "judgment" and name not in (job.instruction, "prompt-section")}
        names |= {"output", "problem", "worker-identity", "workspace", "artifact", "scratch"}
        names |= {name for name in values if name.startswith(("output-", "previous-"))}
        if "capture-directory" in values:
            names.add("capture-directory")
            assert values["source-anchor"] == "src/example.py"
            assert values["capture-directory"] == str(tmp_path / "run/sources")
        for name in names:
            if values[name] != "absent":
                assert Path(values[name]).is_absolute(), (name, values[name])
        assert values["artifact"] == str(tmp_path / "run/artifact")
        assert f"Validate it in {tmp_path / 'run/artifact'}." in text
        for line in text.split("## Input reading batches\n", 1)[1].splitlines():
            if line[:1].isdigit() and ". " in line:
                for path in line.split(". ", 1)[1].split(", "):
                    assert Path(path.removesuffix(" — read in bounded ranges")).is_absolute()
        if retry:
            assert values["refusal"] != "absent"
            assert Path(values["previous-report"]).read_text()
            assert Path(values["previous-answers"]).exists()
        return text

    check(c.handout("brief"))
    c.through_brief()
    check(c.handout("report"))
    c.complete("report", "report A\n", answers="")
    c.complete("other", "other O1\n")
    c.complete("summary", "summary S1\n")
    c.complete("verification", blocking("report: r1"))
    retry = c.handout("report")
    text = check(retry, retry=True)
    recovered = next(h for h in open_handouts(Path("run")) if h.job == "report")
    assert recovered == retry
    assert check(recovered, retry=True) == text
    # The printed destinations remain usable even after a worker changes cwd.
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    monkeypatch.chdir(elsewhere)
    assert recovered.prompt.read_text() == text
    recovered.worker_identity.write_text('{"model": "test-model", "effort": "medium"}\n')
    assert (tmp_path / "run/state/handouts" / recovered.attempt / "worker-identity.json").is_file()


def test_prompt_section_cannot_reference_an_undelivered_gate(tmp_path):
    declaration, method = toy_library(tmp_path, compact=True)
    (method / "section.md").write_text(SECTION + "\n[report-verified]\nUse {report-verified}.\n")
    data = yaml.safe_load(declaration.read_text())
    data["prompt-section"] = "section.md"
    declaration.write_text(yaml.safe_dump(data, sort_keys=False))
    with pytest.raises(PlanError, match="binds no variable report-verified"):
        start_run(tmp_path / "run", declaration, parameters={"subject": "toy"})
