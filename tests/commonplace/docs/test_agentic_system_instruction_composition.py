from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]


def instruction(name: str) -> str:
    return (REPO_ROOT / "kb" / "instructions" / name / "SKILL.md").read_text(
        encoding="utf-8"
    )


def test_memory_review_publication_closes_the_comparison_handoff() -> None:
    writer = instruction("write-agent-memory-system-review")
    orchestrator = instruction("analyse-agentic-system")

    assert "Close the downstream comparison handoff" in writer
    assert "systems.csv" in writer and "systems-table.md" in writer
    assert "report the pair as stale" in writer
    assert "synthesize-agent-memory-landscape/SKILL.md" in writer
    assert "matrix/table authority or stale disposition" in orchestrator


def test_transfer_scan_follows_stable_result_verification() -> None:
    orchestrator = instruction("analyse-agentic-system")

    verification = orchestrator.index("### 10. Verify and freeze the stable result")
    transfer = orchestrator.index(
        "### 11. Route a selective transfer scan only after stable verification"
    )

    assert verification < transfer
    assert "only after step 10 has frozen and fingerprinted" in orchestrator[transfer:]
