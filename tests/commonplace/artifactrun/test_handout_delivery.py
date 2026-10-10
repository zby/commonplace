"""Model judgment gates remain engine inputs, not worker-delivered evidence."""

import pytest
import yaml

from commonplace.artifactrun import PlanError, start_run
from commonplace.artifactrun.handouts import prompt_variable_names
from commonplace.artifactrun.run import Run
from commonplace.artifactrun.store import RunStore
from tests.commonplace.artifactrun.support import NO_BLOCKERS, toy_library
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


def test_prompt_section_cannot_reference_an_undelivered_gate(tmp_path):
    declaration, method = toy_library(tmp_path, compact=True)
    (method / "section.md").write_text(SECTION + "\n[report-verified]\nUse {report-verified}.\n")
    data = yaml.safe_load(declaration.read_text())
    data["prompt-section"] = "section.md"
    declaration.write_text(yaml.safe_dump(data, sort_keys=False))
    with pytest.raises(PlanError, match="binds no variable report-verified"):
        start_run(tmp_path / "run", declaration, parameters={"subject": "toy"})
