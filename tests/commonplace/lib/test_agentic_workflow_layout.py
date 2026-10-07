"""Declared-slot acceptance and replay contracts of agentic_workflow."""

import json
from functools import partial
from hashlib import sha256
from pathlib import Path

import pytest

from commonplace.lib import agentic_set, validation
from commonplace.lib.agentic_finalize import start_manifest
from commonplace.lib.agentic_workflow import (
    MEASUREMENTS,
    AnalyseAgenticSystem,
    SetRefusal,
    actionable_refusals,
    compare_selfcheck,
    slot,
)
from commonplace.lib.directory_layout import Finding
from commonplace.workflow_legacy import Blocked, Done, Launch, Orchestrator, Workflow
from tests.commonplace.lib.test_agentic_workflow import (
    RUN_ID,
    ZERO,
    Fixture,
    epistemic_text,
    runtime_text,
)

pytestmark = pytest.mark.usefixtures("tmp_library")


@pytest.fixture
def fixture(tmp_path):
    return Fixture(tmp_path)


@pytest.mark.parametrize("role", [
    "boundary", "runtime", "memory", "epistemic", "reconciliation",
    "memory-profile", "record-verification", "profile-verification",
    "synthesis", "synthesis-verification",
])
def test_acceptance_is_same_role_findings_plus_labelled_job_residue(
    fixture: Fixture, role: str,
) -> None:
    start_manifest(fixture.run_dir)
    texts = {
        "boundary": fixture.boundary(),
        "runtime": runtime_text(fixture.revision),
        "memory": fixture.memory_report(),
        "epistemic": epistemic_text(fixture.revision),
        "reconciliation": fixture.reconciliation(),
        "memory-profile": fixture.memory_profile(),
        "record-verification": fixture.verification(),
        "profile-verification": fixture.verification(title="Profile verification"),
        "synthesis": fixture.synthesis(),
        "synthesis-verification": fixture.verification(title="Synthesis verification"),
    }
    for member, text in texts.items():
        (fixture.run_dir / slot(member)).write_text(text)
    # Another member's bad identity must not leak into this role's judgment.
    if role != "epistemic":
        path = fixture.run_dir / slot("epistemic")
        path.write_text(path.read_text().replace(f"run-id: {RUN_ID}", "run-id: wrong"))
    candidate = fixture.run_dir / "draft.md"
    candidate.write_text(texts[role].replace(f"run-id: {RUN_ID}", "run-id: wrong"))
    before = {path: (path.read_bytes(), path.stat().st_mtime_ns)
              for path in (fixture.run_dir / "output").iterdir()}
    definition = AnalyseAgenticSystem(fixture.params())
    definition.repo, definition.run_id = fixture.root, RUN_ID
    definition.jobs_dir = fixture.root / "kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs"
    if role == "boundary":
        job = definition.boundary_job(fixture.run_dir)
    elif role in ("runtime", "memory", "epistemic"):
        job = definition.analyst_job(fixture.run_dir, role, 0)
    elif role == "reconciliation":
        job = definition.reconcile_job(fixture.run_dir, 0, ZERO, ())
    elif role == "memory-profile":
        job = definition.profile_job(fixture.run_dir, 0)
    elif role == "record-verification":
        job = definition.verification_job(
            fixture.run_dir, 0, ZERO, (), validator=partial(
                definition.record_verification_refusals, fixture.run_dir, failures=["failed round"],
            ),
        )
    elif role == "profile-verification":
        job = definition.profile_verification_job(fixture.run_dir, 0)
    elif role == "synthesis":
        job = definition.synthesis_job(fixture.run_dir, 0)
    else:
        job = definition.synthesis_verification_job(fixture.run_dir, 0)
    findings = validation.validate_draft_at_slot(
        fixture.run_dir / "output", agentic_set.analysis_layout().path(role), candidate,
        repo_root=fixture.root,
    )
    assert all(finding.role == role for finding in findings)
    assert not any("set input cannot be checked" in finding.message for finding in findings)
    expected = ["[set] " + finding.render() for finding in findings
                if not finding.absent and not finding.warn]
    assert expected
    accepted = list(job.validator(candidate))
    assert [reason for reason in accepted if reason.startswith("[set] ")] == expected
    residue = [reason for reason in accepted if not reason.startswith("[set] ")]
    assert all(reason.startswith("[job residue] ") for reason in residue)
    assert bool(residue) == (role in ("boundary", "record-verification"))
    measurement = definition.job_measurements[job.name]
    assert measurement["set-findings"] == expected
    assert measurement["findings"] == accepted
    assert measurement["candidate-sha256"] == sha256(candidate.read_bytes()).hexdigest()
    assert measurement["another-member-count"] == 0
    assert measurement["unattributed-set-finding-count"] == 0
    assert measurement["set-finding-roles"] == [role] * len(expected)
    assert compare_selfcheck(
        measurement, candidate_sha256=measurement["candidate-sha256"],
        findings=[finding.render() for finding in findings if not finding.absent and not finding.warn],
    ) is False
    # Direct validator calls, like selfchecks, must not persist measurements.
    assert not (fixture.run_dir / MEASUREMENTS).exists()
    assert {path: (path.read_bytes(), path.stat().st_mtime_ns)
            for path in (fixture.run_dir / "output").iterdir()} == before


def test_job_residue_renderer_preserves_common_finding_text(tmp_path: Path) -> None:
    diagnostic = "[set] synthesis.md: identity field run-id does not match\nRepair: use the boundary run-id"
    reasons = actionable_refusals(lambda _: [diagnostic, diagnostic, "structural failures require explicit blockers"],
                                 tmp_path / "draft.md")
    assert reasons[0] == diagnostic
    assert reasons[1] == diagnostic
    assert reasons[2].startswith("[job residue] ")
    assert "Repair: write the supplied structural failures as explicit blockers" in reasons[2]


def test_coordinator_retains_refused_and_passing_judgments_without_replay_duplicates(
    fixture: Fixture,
) -> None:
    definition = AnalyseAgenticSystem(fixture.params())
    definition.jobs_dir = fixture.root / "kb/agentic-system-analyses/instructions/analyse-agentic-system/jobs"
    finding = SetRefusal(Finding("runtime", "runtime.md: invalid field"))
    reasons = [finding, finding, "record duplicate", "record duplicate"]
    job = definition.job(
        fixture.run_dir, "runtime-0", "runtime-report-0.md", role="runtime",
        reads={}, instruction="runtime", validator=lambda _: reasons,
    )

    class OneJob(Workflow):
        def run(self, ctx):
            definition.run_job(ctx, job)

    orchestrator = Orchestrator(fixture.run_dir, OneJob())
    assert isinstance(orchestrator.step(), Launch)
    assert not (fixture.run_dir / MEASUREMENTS).exists()
    candidate = job.output_path(fixture.run_dir)
    candidate.write_text("same candidate bytes\n")
    candidate_digest = sha256(candidate.read_bytes()).hexdigest()
    assert isinstance(orchestrator.step(), Launch)
    records = list((fixture.run_dir / MEASUREMENTS / job.name).glob("*.json"))
    assert len(records) == 1
    refused = json.loads(records[0].read_text())
    assert refused["run-id"] == RUN_ID
    assert refused["job"] == job.name
    assert refused["candidate-sha256"] == candidate_digest
    assert refused["set-findings"] == [finding, finding]
    assert refused["another-member-count"] == 0
    # Count raw refusals, not the coalesced feedback line.
    assert refused["residue-rule-counts"] == {"record contract": 2}
    assert "2 identical findings" in refused["findings"][-1]
    assert not candidate.exists()  # The engine preserved the rejected output.
    assert not (fixture.run_dir / "runtime-report-0.md").exists()
    original = (records[0].read_bytes(), records[0].stat().st_mtime_ns)
    candidate.write_text("same candidate bytes\n")
    assert isinstance(orchestrator.step(), Blocked)
    assert len(list(records[0].parent.glob("*.json"))) == 1
    assert (records[0].read_bytes(), records[0].stat().st_mtime_ns) == original
    # A changed judgment of identical bytes is retained separately.
    reasons.clear()
    assert isinstance(orchestrator.step(), Done)
    records = list(records[0].parent.glob("*.json"))
    assert len(records) == 2
    passing = next(json.loads(path.read_text()) for path in records
                   if not json.loads(path.read_text())["findings"])
    assert passing["candidate-sha256"] == candidate_digest
    assert passing["residue-rule-counts"] == {}
    assert (fixture.run_dir / "runtime-report-0.md").read_bytes() == candidate.read_bytes()
    before = {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in records}
    assert isinstance(orchestrator.step(), Done)
    assert {path: (path.read_bytes(), path.stat().st_mtime_ns)
            for path in records[0].parent.glob("*.json")} == before


def test_measurement_keeps_role_attribution_and_comparison_is_digest_gated(
    fixture: Fixture,
) -> None:
    definition = AnalyseAgenticSystem(fixture.params())
    own = SetRefusal(Finding("runtime", "own diagnostic"))
    foreign = SetRefusal(Finding("memory", "foreign diagnostic"))
    candidate = fixture.run_dir / "draft.md"
    candidate.write_text("draft\n")
    validator = definition.measured_validator(
        "runtime-0", "runtime", fixture.run_dir, lambda _: [own, foreign],
    )
    assert validator(candidate) == [own, foreign]
    measurement = definition.job_measurements["runtime-0"]
    assert measurement["another-member-count"] == 1
    assert measurement["set-finding-roles"] == ["runtime", "memory"]
    findings = [text.removeprefix("[set] ") for text in (own, foreign)]
    digest = measurement["candidate-sha256"]
    assert compare_selfcheck(measurement, candidate_sha256=digest, findings=findings) is False
    assert compare_selfcheck(measurement, candidate_sha256=digest, findings=findings[:1]) is True
    assert compare_selfcheck(measurement, candidate_sha256="different", findings=findings[:1]) is None
    assert not (fixture.run_dir / MEASUREMENTS).exists()


def test_measurement_counts_malformed_input_as_residue(fixture: Fixture) -> None:
    definition = AnalyseAgenticSystem(fixture.params())
    candidate = fixture.run_dir / "draft.md"
    candidate.write_text("draft\n")

    def broken(_):
        raise ValueError("malformed frontmatter")

    validator = definition.measured_validator("runtime-0", "runtime", fixture.run_dir, broken)
    delivered = validator(candidate)
    measurement = definition.job_measurements["runtime-0"]
    assert measurement["findings"] == delivered
    assert measurement["residue-rule-counts"] == {"frontmatter": 1}
    assert measurement["set-findings"] == []
    assert not (fixture.run_dir / MEASUREMENTS).exists()
