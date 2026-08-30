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


def test_response_fingerprint_contract_excludes_its_own_report() -> None:
    orchestrator = instruction("analyse-agentic-system")
    transfer = instruction("scan-agentic-system-transfer")
    contract = (
        REPO_ROOT
        / "kb"
        / "instructions"
        / "analyse-agentic-system"
        / "references"
        / "response-fingerprint.md"
    ).read_text(encoding="utf-8")

    assert "hash only its delimited stable block" in orchestrator
    assert "digest outside that block" in orchestrator
    assert "exact delimited stable response block" in transfer
    assert "Never hash the completed assistant message" in contract
    assert "AAS-STABLE-RESULT START" in contract
    assert "AAS-STABLE-RESULT END" in contract


def test_analysis_skill_uses_one_typed_result_shape_for_every_carrier() -> None:
    orchestrator = instruction("analyse-agentic-system")
    contract = (
        REPO_ROOT / "kb" / "types" / "agentic-system-analysis-result.md"
    ).read_text(encoding="utf-8")

    assert "single authority for the result's frontmatter" in orchestrator
    assert "A response's delimited stable block is the complete typed entry artifact" in orchestrator
    assert "copy those unchanged bytes to a temporary `.md` validation target" in orchestrator
    assert "The type fixes content shape, not lifecycle" in contract
    assert "A response-only result" in contract
    assert "A package has exactly one typed entry artifact" in orchestrator
    assert "wired; observed" in contract
    assert "implemented and observed" in contract
