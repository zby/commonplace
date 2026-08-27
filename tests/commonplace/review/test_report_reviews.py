"""Behavioral coverage for report-kind review jobs."""

from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.review import review_db, review_target_selector
from commonplace.review.batch import prepare_grouped_review_job
from commonplace.review.finalization import finalize_review_job_from_owned_output
from commonplace.review.protocol.parser import parse_job_output

NOTE_PATH = "kb/notes/sample.md"
CRITIQUE_PATH = "kb/instructions/critique-note.md"
MODEL = "test-model"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_repo(root: Path) -> Path:
    write(
        root / NOTE_PATH,
        """---
description: Test note
type: kb/types/note.md
---

# Sample

Initial body.
""",
    )
    write(
        root / CRITIQUE_PATH,
        """---
description: Critique a note
type: kb/types/instruction.md
---

# Critique a note

Attack the central commitment.
""",
    )
    db_path = root / "kb/reports/commonplace-store.sqlite"
    review_db.ensure_db(db_path)
    return db_path


def report_bundle(body: str = "A strong critique.") -> str:
    return f"""=== PAIR REVIEW START: {NOTE_PATH} :: {CRITIQUE_PATH} ===
{body}

## Result: REPORT
=== PAIR REVIEW END: {NOTE_PATH} :: {CRITIQUE_PATH} ===
"""


def test_result_kind_parser_enforces_pair_contract() -> None:
    pair = (NOTE_PATH, CRITIQUE_PATH)
    parsed = parse_job_output(
        report_bundle(),
        expected_pairs=[pair],
        result_kinds={pair: "report"},
    )
    assert parsed.reviews[pair].outcome is None
    assert parsed.canonical_texts[pair].endswith("## Result: REPORT\n")

    with pytest.raises(ValueError, match="result-kind contract mismatch"):
        parse_job_output(report_bundle(), expected_pairs=[pair], result_kinds={})
    with pytest.raises(ValueError, match="verdict result is invalid"):
        parse_job_output(
            report_bundle().replace("REPORT", "PASS"),
            expected_pairs=[pair],
            result_kinds={pair: "report"},
        )


def test_critique_report_flow_is_snapshot_anchored_and_writes_artifact(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    db_path = make_repo(repo)
    missing = review_target_selector.select_stale_criteria(
        repo,
        model=MODEL,
        criterion_ids=["critique"],
        note_filter=[NOTE_PATH],
    )
    assert [(record.reasons, record.result_kind) for record in missing] == [
        (("missing-baseline",), "report")
    ]

    prepared = prepare_grouped_review_job(
        repo_root=repo,
        db_path=db_path,
        pairs=[(NOTE_PATH, CRITIQUE_PATH, "report")],
        grouping="note",
        runner=None,
        model_partition=MODEL,
    )
    original_prompt = (repo / prepared.prompt_path).read_text(encoding="utf-8")
    original_instruction = (repo / CRITIQUE_PATH).read_text(encoding="utf-8")
    assert "Attack the central commitment." in original_prompt
    assert "## Result: REPORT" in original_prompt

    write(repo / CRITIQUE_PATH, (repo / CRITIQUE_PATH).read_text() + "\nChanged live instruction.\n")
    assert (repo / prepared.prompt_path).read_text(encoding="utf-8") == original_prompt
    write(repo / prepared.job_output_path, report_bundle())
    outcome = finalize_review_job_from_owned_output(
        repo_root=repo,
        db_path=db_path,
        review_job_id=prepared.review_job_id,
    )
    assert outcome.completed

    result_path = next(iter(prepared.result_paths.values()))
    assert outcome.to_payload()["pairs"] == [
        {
            "review_pair_id": prepared.pairs[0].review_pair_id,
            "note_path": NOTE_PATH,
            "criterion_path": CRITIQUE_PATH,
            "criterion_id": "critique",
            "pair_ordinal": 1,
            "result_kind": "report",
            "outcome": None,
            "result_path": result_path,
        }
    ]
    result_text = (repo / result_path).read_text(encoding="utf-8")
    assert "result_kind: report" in result_text
    assert result_text.rstrip().endswith("## Result: REPORT")

    stale = review_target_selector.select_stale_criteria(
        repo,
        model=MODEL,
        criterion_ids=["critique"],
        note_filter=[NOTE_PATH],
    )
    assert [record.reasons for record in stale] == [("criterion-changed",)]

    write(repo / CRITIQUE_PATH, original_instruction)
    write(repo / NOTE_PATH, (repo / NOTE_PATH).read_text(encoding="utf-8") + "\nFinal edit.\n")
    stale = review_target_selector.select_stale_criteria(
        repo,
        model=MODEL,
        criterion_ids=["critique"],
        note_filter=[NOTE_PATH],
    )
    assert [record.reasons for record in stale] == [("note-changed",)]


def test_review_job_rejects_mixed_result_kinds(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    db_path = make_repo(repo)

    with pytest.raises(ValueError, match="cannot mix result kinds"):
        prepare_grouped_review_job(
            repo_root=repo,
            db_path=db_path,
            pairs=[
                (NOTE_PATH, CRITIQUE_PATH, "report"),
                (NOTE_PATH, "kb/instructions/review-gates/semantic/test.md", "verdict"),
            ],
            grouping="note",
            runner=None,
            model_partition=MODEL,
        )
