from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def instruction(name: str) -> str:
    return (REPO_ROOT / "kb" / "instructions" / name / "SKILL.md").read_text(
        encoding="utf-8"
    )


def job(name: str) -> str:
    return (
        REPO_ROOT / "kb/instructions/analyse-agentic-system/jobs" / f"{name}.md"
    ).read_text(encoding="utf-8")


def test_analysis_failure_is_rerun_instead_of_recovered() -> None:
    orchestrator = instruction("analyse-agentic-system")
    run_state = (
        REPO_ROOT
        / "kb/types/agentic-system-analysis-run-state.md"
    ).read_text(encoding="utf-8")

    assert "correctable pre-publication failure" in orchestrator
    assert "only when abandoning the run" in orchestrator
    assert "use a new run ID" in orchestrator
    assert "resume a failed run" in run_state


def contract(name: str) -> str:
    return (REPO_ROOT / "kb/types" / f"{name}.md").read_text(encoding="utf-8")


def test_set_has_one_fixed_state_location() -> None:
    from commonplace.lib.agentic_workflow import MANIFEST

    overview = contract("agentic-system-analysis-overview")

    assert MANIFEST == "output/ARTIFACT.yaml"
    assert "reading entry point" in overview
    assert "Run state and compact reviews pin `ARTIFACT.yaml`" in overview


def test_repository_sources_are_read_from_the_frozen_checkout() -> None:
    boundary = job("boundary")
    rules = job("worker-rules")

    assert "related-systems/<owner>--<repo>/" in boundary
    assert "git check-ignore -q" in boundary
    assert "verify an existing checkout's origin" in boundary
    assert "compact source allowlist" in boundary
    assert "git checkout --detach <commit>" in boundary
    # The boundary validator guarantees the checkout, so jobs read it directly.
    assert "read and grep the files of the checkout at `source.path`" in rules
    assert "do not extract another copy of the source" in rules
    # The anchor grammar is the overview type's, stated once under Status fields;
    # the searched boundary of an absence is a runtime-report record field.
    assert "one code span containing the full commit-relative path" in contract(
        "agentic-system-analysis-overview"
    )
    assert "searched boundary" in contract("agentic-system-runtime-report")


def test_runtime_checks_preflight_before_execution() -> None:
    runtime = job("runtime")

    assert "Before any dynamic" in runtime
    assert "execution-preflight" in runtime
    assert "probe evidence capsule" in runtime
    # Preflight and capsule semantics live in the runtime report type, not the job.
    runtime = contract("agentic-system-runtime-report")
    assert "leaves the target check `not run`" in runtime
    assert "supports no negative finding" in runtime
    assert "actual intervention and comparison" in runtime
    assert "checks considered" in runtime


def test_transfer_scan_runs_after_complete_state() -> None:
    orchestrator = instruction("analyse-agentic-system")

    assert "only after the complete run state validates" in orchestrator
    assert "scan-agentic-system-transfer" in orchestrator


def test_candidate_artifact_does_not_establish_phase_observation() -> None:
    epistemic = (
        REPO_ROOT
        / "kb/instructions/analyse-external-system-epistemic-architecture.md"
    ).read_text(encoding="utf-8")
    dispose = epistemic[
        epistemic.index("**Dispose every object.**") :
        epistemic.index("**Bound each check's licenses.**")
    ]

    assert "persisted candidate artifact" in dispose
    assert "no provenance or trace links it" in dispose
    assert "only that a candidate instance is available" in dispose
    assert "observed candidate state" in dispose
    assert "`not determinable`, not `phase evidenced` or `accepted`" in dispose
    assert "Observed candidate state is one of" in contract("agentic-system-epistemic-report")


def test_jobs_state_the_set_rules_they_depend_on() -> None:
    assert "Declare each record you establish under an `EPI-` ID" in job("epistemic")
    assert "no job rewrites it afterwards" in job("runtime")
    assert "(../../../types/agentic-system-runtime-report.md#shared-records)" in job(
        "judging-norms"
    )
    assert "`## Not reached`" in job("boundary")


def test_method_paths_exist_in_the_repository() -> None:
    from commonplace.lib.agentic_publication import METHOD_PATHS

    assert [path for path in METHOD_PATHS if not (REPO_ROOT / path).exists()] == []
