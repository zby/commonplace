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
        / "kb/reports/types/agentic-system-analysis-run-state.md"
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


def test_complete_analysis_publishes_validated_candidates() -> None:
    orchestrator = instruction("analyse-agentic-system")
    memory_writer = instruction("write-agent-memory-system-review")
    collection = (REPO_ROOT / "kb/agentic-systems/COLLECTION.md").read_text(
        encoding="utf-8"
    )

    assert "Publish validated candidates" in orchestrator
    assert "temporary candidate" in orchestrator
    assert "commonplace-agentic-analysis-publication prepare" in orchestrator
    assert "commonplace-agentic-analysis-publication publish" in orchestrator
    assert "rolls back ordinary" in orchestrator
    assert "authorizes only the candidate" in memory_writer.lower()
    assert "incumbent untouched" in memory_writer
    assert "Do not run semantic review or publish" in memory_writer
    collection_text = collection.replace("\n", " ")
    assert "private candidate as its intended destination" in collection_text
    assert "complete run state is the sole declaration" in collection_text
    assert "Never stage or commit" in orchestrator


def test_exact_result_has_one_fixed_state_location() -> None:
    orchestrator = instruction("analyse-agentic-system")
    contract = (
        REPO_ROOT / "kb/types/agentic-system-analysis-result.md"
    ).read_text(encoding="utf-8")

    assert "exact result path is always `<run-id>/result.md`" in orchestrator
    assert "Every result is one typed Markdown file" in contract
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
    assert "full commit-relative path" in source_work
    assert "compact source allowlist" in source_work
    assert "recorded search boundary" in source_work


def test_runtime_checks_preflight_before_execution() -> None:
    orchestrator = instruction("analyse-agentic-system")
    runtime = orchestrator[
        orchestrator.index("### 4. Run and challenge the runtime baseline") :
        orchestrator.index("### 5. Run both lenses")
    ]

    assert "Before any dynamic" in runtime
    assert "execution-preflight" in runtime
    assert "never reaches the target remains `not run`" in runtime
    assert "probe evidence capsule" in runtime
    assert "actual intervention and comparison" in runtime
    assert "checks considered" in runtime


def test_both_lenses_share_one_canonical_register() -> None:
    orchestrator = instruction("analyse-agentic-system")
    epistemic = (
        REPO_ROOT
        / "kb/instructions/analyse-external-system-epistemic-architecture.md"
    ).read_text(encoding="utf-8")
    result_contract = (
        REPO_ROOT / "kb/types/agentic-system-analysis-result.md"
    ).read_text(encoding="utf-8")

    assert "Both lenses always run" in orchestrator
    assert "Maintain one canonical register" in orchestrator
    assert "Require a sparse overlay on canonical IDs" in orchestrator
    assert "it never mints a canonical ID" in epistemic
    assert "They do not reproduce the shared inventory" in result_contract


def test_memory_review_publication_closes_downstream_disposition() -> None:
    writer = instruction("write-agent-memory-system-review")
    orchestrator = instruction("analyse-agentic-system")

    assert "systems.csv" not in writer and "systems-table.md" not in writer
    assert "systems.csv" in orchestrator and "systems-table.md" in orchestrator
    assert "report a prior current landscape synthesis as historical" in orchestrator
    assert "publication of the legacy review happens only after" in orchestrator


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
    example = epistemic[
        epistemic.index("Example: observed-run evidence") :
        epistemic.index("Use this schema:")
    ]

    assert "persisted claim artifact" in example
    assert "does not establish that any particular production phase ran" in example
    assert "observed candidate state" in example
    assert "as `not determinable`, not `phase evidenced` or `accepted`" in example
