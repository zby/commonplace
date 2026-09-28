from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def instruction(name: str) -> str:
    return (REPO_ROOT / "kb" / "instructions" / name / "SKILL.md").read_text(
        encoding="utf-8"
    )


def test_analysis_failure_is_rerun_instead_of_recovered() -> None:
    orchestrator = instruction("analyse-agentic-system")
    run_state = (
        REPO_ROOT
        / "kb/types/agentic-system-analysis-run-state.md"
    ).read_text(encoding="utf-8")

    assert "correctable pre-publication failure" in orchestrator
    assert "only when abandoning the run" in orchestrator
    assert "Use a new run ID" in orchestrator
    assert "resume a failed run" in run_state
    for obsolete in (
        "phase: handoff-ready",
        "reconciliation-seal",
        "accepted-lens-packets",
        "validation-receipt-path",
        "lens-return-byte-budget",
    ):
        assert obsolete not in orchestrator


def contract(name: str) -> str:
    return (REPO_ROOT / "kb/types" / f"{name}.md").read_text(encoding="utf-8")


def test_set_has_one_fixed_state_location() -> None:
    orchestrator = instruction("analyse-agentic-system")
    overview = contract("agentic-system-analysis-overview")

    assert "entry member is always\n   `<run-id>/overview.md`" in orchestrator
    assert "The entry member of one `analyse-agentic-system` run's retained set" in overview
    assert "the overview's manifest pins every other member" in overview
    assert "response-only" not in orchestrator
    assert "canonical carrier" not in orchestrator
    assert "package has exactly one" not in orchestrator.lower()


def test_repository_sources_remain_commit_addressed() -> None:
    orchestrator = instruction("analyse-agentic-system")
    source_work = orchestrator[
        orchestrator.index("### 2. Freeze and inspect sources once") :
        orchestrator.index("### 3. Use one vocabulary and one record set")
    ]

    assert "related-systems/<owner>--<repo>/" in source_work
    assert "git check-ignore -q" in source_work
    assert "verify an existing checkout's origin" in source_work
    assert "git --no-replace-objects -C" in source_work
    assert "never read evidence from the worktree" in source_work
    assert "compact source allowlist" in source_work
    # The anchor grammar is the overview type's, stated once under Status fields;
    # the searched boundary of an absence is a runtime-report record field.
    assert "one code span containing the full commit-relative path" in contract(
        "agentic-system-analysis-overview"
    )
    assert "searched boundary" in contract("agentic-system-runtime-report")


def test_runtime_checks_preflight_before_execution() -> None:
    orchestrator = instruction("analyse-agentic-system")
    runtime = orchestrator[
        orchestrator.index("### 4. Run and challenge the runtime baseline") :
        orchestrator.index("### 5. Run both lenses")
    ]

    assert "Before any dynamic" in runtime
    assert "execution-preflight" in runtime
    assert "probe evidence capsule" in runtime
    # Preflight and capsule semantics live in the runtime report type, not the skill.
    runtime = contract("agentic-system-runtime-report")
    assert "leaves the target check `not run`" in runtime
    assert "supports no negative finding" in runtime
    assert "actual intervention and comparison" in runtime
    assert "checks considered" in runtime


def test_transfer_scan_runs_after_complete_state() -> None:
    orchestrator = instruction("analyse-agentic-system")
    publication = orchestrator.index("### 8. Publish validated candidates")
    transfer = orchestrator.index("### 9. Run an optional transfer scan after completion")

    assert publication < transfer
    assert "only after the complete run state validates" in orchestrator[transfer:]
    assert "never edits the analysis" in orchestrator[transfer:]


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


def test_orchestrator_states_the_set_rules_it_depends_on() -> None:
    orchestrator = instruction("analyse-agentic-system")
    assert "write the overview only, with an empty\nmanifest" in orchestrator
    assert "commission a\nfresh specialist against the same frozen input" in orchestrator
    assert "cites only\ncanonical IDs" in orchestrator
    assert "(../../types/agentic-system-runtime-report.md#shared-records)" in orchestrator
    assert "`METHOD_PATHS` constant" in orchestrator
    assert "run bundle" not in orchestrator


def test_method_paths_exist_in_the_repository() -> None:
    from commonplace.lib.agentic_publication import METHOD_PATHS

    assert [path for path in METHOD_PATHS if not (REPO_ROOT / path).exists()] == []
