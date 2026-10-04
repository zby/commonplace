"""The analyst sees exactly what its real acceptance validator will refuse."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from commonplace.cli.analysis_check import check_draft, main
from commonplace.lib import agentic_publication
from commonplace.workflow import Done, Orchestrator
from tests.commonplace.lib.test_agentic_workflow import Fixture
from tests.commonplace.workflow.definitions import ScriptedAgent

pytestmark = pytest.mark.usefixtures("tmp_library")


def snapshot(root: Path):
    return {str(p.relative_to(root)): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in root.rglob("*") if p.is_file()}


@pytest.mark.parametrize("correction", ["none", "blockers", "returned"])
def test_each_scheduled_job_has_identical_read_only_checks(tmp_path, monkeypatch, capsys, correction):
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: tmp_path)
    fixture = Fixture(tmp_path)
    orchestrator = Orchestrator.create(
        fixture.run_dir,
        "tests.commonplace.lib.test_agentic_workflow:CountsPublication",
        fixture.params(),
    )
    definition = orchestrator.workflow
    jobs = {}
    original_job = definition.job

    def remember(*args, **kwargs):
        job = original_job(*args, **kwargs)
        jobs[job.name] = job
        return job

    monkeypatch.setattr(definition, "job", remember)
    originals = fixture.workers()
    if correction == "blockers":
        originals["verify-0"] = fixture.writes(lambda _: fixture.verification("- Recheck this fixture finding."))
    if correction == "returned":
        originals["reconcile-0"] = fixture.writes(lambda _: fixture.reconciliation(returned=True))
    observed = set()

    def wrap(worker):
        def run(handout):
            worker(handout)
            draft = handout.output_path
            correct = draft.read_bytes()
            draft.write_text("invalid draft\n")
            expected = list(jobs[handout.name].validator(draft))
            assert expected, handout.name
            before = snapshot(fixture.run_dir)
            assert check_draft(fixture.run_dir, handout.name)[1] == expected
            assert snapshot(fixture.run_dir) == before
            assert all("rule " in reason and "Repair:" in reason and draft.name in reason for reason in expected)
            assert main([str(fixture.run_dir / "run-state.md"), handout.name]) == 1
            assert capsys.readouterr().out.rstrip() == "\n".join(expected).rstrip()
            log = draft.parent / "scratch/acceptance-checks.jsonl"
            event = json.loads(log.read_text().splitlines()[-1])
            assert event["job"] == handout.name and event["refusals_by_rule"]
            # Only the scratch log may have changed.
            after = snapshot(fixture.run_dir)
            assert {k:v for k,v in after.items() if not k.endswith("acceptance-checks.jsonl")} == {k:v for k,v in before.items() if not k.endswith("acceptance-checks.jsonl")}
            draft.write_bytes(correct)
            before = snapshot(fixture.run_dir)
            assert check_draft(fixture.run_dir, handout.name)[1] == list(jobs[handout.name].validator(draft))
            assert snapshot(fixture.run_dir) == before
            observed.add(handout.name)
        return run

    scripted = ScriptedAgent(orchestrator, {name:wrap(worker) for name,worker in originals.items()})
    assert isinstance(scripted.run()[-1], Done)
    assert observed == set(scripted.launched)
    assert {"boundary", "runtime", "epistemic", "memory-0", "reconcile-0",
            "profile", "verify-profile", "synthesize", "verify-synthesis"} <= observed
    if correction != "returned":
        assert "verify-0" in observed
    if correction != "none":
        assert "reconcile-1" in observed and "verify-1" in observed
    if correction == "returned":
        assert "memory-1" in observed


def test_independent_member_failures_include_identity_and_quote(tmp_path, monkeypatch):
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: tmp_path)
    fixture = Fixture(tmp_path)
    orchestrator = Orchestrator.create(fixture.run_dir, "tests.commonplace.lib.test_agentic_workflow:CountsPublication", fixture.params())
    originals = fixture.workers()

    original_runtime = originals["runtime"]

    def runtime(handout):
        original_runtime(handout)
        draft = handout.output_path
        text = draft.read_text()
        text = text.replace(fixture.run_dir.name, "AAS-2026-09-04-wrong-system-01")
        text += '\nUnknown MEM-OBJ-missing.\n\n> absent passage\n> --- `README.md`\n'
        draft.write_text(text)
        _, reasons = check_draft(fixture.run_dir, "runtime")
        assert any("unresolved record MEM-OBJ-missing" in r for r in reasons)
        assert any("member identity: run-id" in r and fixture.run_dir.name in r for r in reasons)
        assert any("quotation not found" in r and "recheck the claim" in r for r in reasons)
        original_runtime(handout)

    originals["runtime"] = runtime
    scripted = ScriptedAgent(orchestrator, originals)
    assert isinstance(scripted.run()[-1], Done)
