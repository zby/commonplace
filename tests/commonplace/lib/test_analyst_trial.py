"""Trial preparation uses workflow invocations and records declared dependencies."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from commonplace.lib.agentic_workflow import AnalyseAgenticSystem
from scripts import analyst_trial
from tests.commonplace.lib.test_agentic_workflow import Fixture

pytestmark = pytest.mark.usefixtures("tmp_library")


def recorded_run(tmp_path: Path) -> Fixture:
    fixture = Fixture(tmp_path)
    run = fixture.run_dir
    (run / "output").mkdir()
    (run / "workflow-state").mkdir()
    (run / "workflow-state/run.json").write_text(
        json.dumps({"params": fixture.params()}), encoding="utf-8"
    )
    (run / "boundary.md").write_text(fixture.boundary(), encoding="utf-8")
    (run / "opening.json").write_text("{}\n", encoding="utf-8")
    (run / "output/runtime.md").write_text("# Frozen runtime\n", encoding="utf-8")
    (run / "run-state.md").write_text(
        "---\nrun-status: complete\nresult-disposition: complete\n"
        f"run-id: {run.name}\nsource:\n  path: {fixture.source_root}\n"
        "artifact:\n  path: original-manifest\n  sha256: old\n"
        "generated-review:\n  path: original-review\nfailure: null\n---\n# Recorded state\n",
        encoding="utf-8",
    )
    return fixture


@pytest.mark.parametrize("analyst", analyst_trial.ANALYSTS)
def test_trial_uses_the_workflow_constructor_and_hashes_every_dependency(tmp_path, analyst):
    fixture = recorded_run(tmp_path)
    prompt_path = analyst_trial.prepare(fixture.run_dir, analyst, "test")
    trial = prompt_path.parent
    definition = AnalyseAgenticSystem(fixture.params())
    definition.jobs_dir = fixture.root / analyst_trial.JOBS
    definition.repo = fixture.root
    if analyst == "memory":
        job = definition.memory_job(trial, 0, 0)
    else:
        job = getattr(definition, f"{analyst}_job")(trial)

    assert prompt_path.read_text(encoding="utf-8") == job.prompt
    record = json.loads((trial / "trial.json").read_text(encoding="utf-8"))
    assert record["inputs"] == {path: analyst_trial.sha256(Path(path)) for path in job.inputs}
    assert str(trial / "run-state.md") not in record["inputs"]
    assert (trial / "boundary.md").read_bytes() == (fixture.run_dir / "boundary.md").read_bytes()
    state = yaml.safe_load((trial / "run-state.md").read_text().split("---")[1])
    assert state["run-id"] == trial.name
    assert state["run-status"] == "running"
    assert state["source"]["path"] == str(fixture.source_root)
    assert state["artifact"] is None and state["generated-review"] is None


def test_trial_hash_discovery_does_not_parse_rendered_prompt(tmp_path, monkeypatch):
    fixture = recorded_run(tmp_path)
    monkeypatch.setattr(analyst_trial, "render_prompt", lambda *_: "An opaque message.\n")

    prompt_path = analyst_trial.prepare(fixture.run_dir, "memory", "opaque")
    record = json.loads((prompt_path.parent / "trial.json").read_text())

    assert prompt_path.read_text() == "An opaque message.\n"
    assert {Path(path).name for path in record["inputs"]} == {
        "boundary.md", "runtime.md", "memory.md", "worker-rules.md",
        "agentic-analysis-sources.md", "agentic-analysis-records.md",
        "agent-memory-analysis-report.md",
    }


@pytest.mark.parametrize("failure", ["missing", "unreadable"])
def test_unreadable_declared_dependency_fails_trial_preparation(tmp_path, monkeypatch, failure):
    fixture = recorded_run(tmp_path)
    method = fixture.root / analyst_trial.JOBS / "memory.md"
    if failure == "missing":
        method.unlink()
    else:
        original = analyst_trial.sha256

        def unreadable(path):
            if path == method:
                raise PermissionError("cannot read method")
            return original(path)

        monkeypatch.setattr(analyst_trial, "sha256", unreadable)

    with pytest.raises(ValueError, match="cannot read declared dependency .*memory.md"):
        analyst_trial.prepare(fixture.run_dir, "memory", failure)
    assert list(fixture.run_dir.parent.glob("*trial*/trial.json")) == []
    assert list(fixture.run_dir.parent.glob("*trial*/prompt.md")) == []
