from __future__ import annotations

import sqlite3
import subprocess
import sys
from pathlib import Path

import pytest

from commonplace.review import review_db, review_target_selector, warn_selector
from commonplace.review.batch import prepare_grouped_review_job
from commonplace.review.finalization import finalize_review_job_from_owned_output
from commonplace.review.protocol.parser import parse_pair_bundle


NOTE_PATH = "kb/notes/sample.md"
CRITIQUE_PATH = "kb/instructions/critique-note.md"
MODEL = "test-model"
NOW = "2026-07-11T10:00:00+00:00"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_repo(root: Path) -> Path:
    write(
        root / NOTE_PATH,
        """---
description: Test note
type: kb/types/note.md
status: current
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
    db_path = root / "kb/reports/review-store.sqlite"
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
    parsed = parse_pair_bundle(
        report_bundle(),
        expected_pairs=[pair],
        result_kinds={pair: "report"},
    )
    assert parsed.reviews[pair].decision is None
    assert parsed.reviews[pair].result_kind == "report"
    assert parsed.canonical_texts[pair].endswith("## Result: REPORT\n")

    with pytest.raises(ValueError, match="result-kind contract mismatch"):
        parse_pair_bundle(report_bundle(), expected_pairs=[pair], result_kinds={})
    with pytest.raises(ValueError, match="verdict result is invalid"):
        parse_pair_bundle(
            report_bundle().replace("REPORT", "PASS"),
            expected_pairs=[pair],
            result_kinds={pair: "report"},
        )


def test_critique_report_flow_is_snapshot_anchored_and_writes_artifact(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    db_path = make_repo(repo)
    missing = review_target_selector.select_stale_gates(
        repo,
        model=MODEL,
        gate_ids=["critique"],
        note_filter=[NOTE_PATH],
    )
    assert [(record.reason, record.result_kind) for record in missing] == [
        ("missing-review", "report")
    ]
    records = review_target_selector.select_requested_gates(
        repo,
        gate_ids=["critique"],
        note_filter=[NOTE_PATH],
    )
    assert [(record.gate_path, record.result_kind) for record in records] == [
        (CRITIQUE_PATH, "report")
    ]

    prepared = prepare_grouped_review_job(
        repo_root=repo,
        db_path=db_path,
        pairs=[(NOTE_PATH, CRITIQUE_PATH, "report")],
        packing="note",
        runner=None,
        model_partition=MODEL,
    )
    original_prompt = (repo / prepared.prompt_path).read_text(encoding="utf-8")
    original_instruction = (repo / CRITIQUE_PATH).read_text(encoding="utf-8")
    assert "Attack the central commitment." in original_prompt
    assert "## Result: REPORT" in original_prompt
    assert "PASS, WARN, FAIL, or ERROR" in original_prompt

    write(repo / CRITIQUE_PATH, (repo / CRITIQUE_PATH).read_text() + "\nChanged live instruction.\n")
    assert (repo / prepared.prompt_path).read_text(encoding="utf-8") == original_prompt
    write(repo / prepared.bundle_output_path, report_bundle())
    outcome = finalize_review_job_from_owned_output(
        repo_root=repo,
        db_path=db_path,
        review_job_id=prepared.review_job_id,
    )
    assert outcome.completed

    with review_db.connect(db_path) as conn:
        pair = review_db.load_review_pairs_for_job(
            conn, review_job_id=prepared.review_job_id
        )[0]
        assert pair.result_kind == "report"
        assert pair.decision is None
        assert pair.reviewed_at is not None
        assert pair.result_path is not None
        acceptance = review_db.load_current_acceptances(conn)[(NOTE_PATH, CRITIQUE_PATH, "test-model")]
        assert acceptance.result_kind == "report"
        assert acceptance.decision is None
        latest = review_db.load_latest_completed_review_pair(
            conn,
            note_path=NOTE_PATH,
            gate_path=CRITIQUE_PATH,
            model_partition=MODEL,
        )
        assert latest is not None and latest.review_pair_id == pair.review_pair_id

    result_text = (repo / pair.result_path).read_text(encoding="utf-8")
    assert "result_kind: report" in result_text
    assert result_text.rstrip().endswith("## Result: REPORT")

    stale = review_target_selector.select_stale_gates(
        repo,
        model=MODEL,
        gate_ids=["critique"],
        note_filter=[NOTE_PATH],
    )
    assert [record.reason for record in stale] == ["gate-changed"]

    write(repo / CRITIQUE_PATH, original_instruction)
    write(repo / NOTE_PATH, (repo / NOTE_PATH).read_text(encoding="utf-8") + "\nFinal edit.\n")
    stale = review_target_selector.select_stale_gates(
        repo,
        model=MODEL,
        gate_ids=["critique"],
        note_filter=[NOTE_PATH],
    )
    assert [record.reason for record in stale] == ["note-changed"]

    write(repo / NOTE_PATH, (repo / NOTE_PATH).read_text(encoding="utf-8").removesuffix("\nFinal edit.\n"))
    notes, stale_gates = warn_selector.scan_reviews(repo, db_path=db_path)
    assert notes == []
    assert stale_gates == []


def test_report_pair_completion_and_job_homogeneity_invariants(tmp_path: Path) -> None:
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
            packing="note",
            runner=None,
            model_partition=MODEL,
        )

    with review_db.connect(db_path) as conn:
        job_id = review_db.create_job_with_pairs(
            conn,
            model_partition=MODEL,
            runner=None,
            created_at=NOW,
            status="queued",
            packing="note",
            pairs=[review_db.ReviewPairRequest(NOTE_PATH, CRITIQUE_PATH, 1, "report")],
        )
        pair = review_db.load_review_pairs_for_job(conn, review_job_id=job_id)[0]
        with pytest.raises(ValueError, match="incomplete"):
            review_db.upsert_acceptance(
                conn,
                note_path=NOTE_PATH,
                gate_path=CRITIQUE_PATH,
                model_partition=MODEL,
                accepted_review_pair_id=pair.review_pair_id,
                accepted_at=NOW,
            )
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                "UPDATE review_pairs SET decision = 'pass' WHERE review_pair_id = ?",
                (pair.review_pair_id,),
            )


V4_SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE review_jobs (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT,
    runner_model TEXT,
    runner_effort TEXT,
    created_at TEXT NOT NULL,
    completed_at TEXT,
    status TEXT NOT NULL,
    failure_reason TEXT,
    telemetry_json TEXT,
    packing TEXT NOT NULL
);
CREATE TABLE review_file_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    path TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    content_text TEXT,
    captured_at TEXT NOT NULL,
    UNIQUE(path, content_sha256)
);
CREATE TABLE review_pairs (
    review_pair_id INTEGER PRIMARY KEY,
    review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    decision TEXT,
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_at TEXT,
    UNIQUE(review_job_id, note_path, gate_path),
    UNIQUE(review_job_id, pair_ordinal)
);
CREATE INDEX idx_review_pairs_note_gate ON review_pairs(note_path, gate_path);
CREATE INDEX idx_review_pairs_review_job_id ON review_pairs(review_job_id);
CREATE TABLE acceptance (
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    model_partition TEXT NOT NULL,
    accepted_review_pair_id INTEGER NOT NULL REFERENCES review_pairs(review_pair_id),
    accepted_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    accepted_at TEXT NOT NULL
);
CREATE UNIQUE INDEX idx_acceptance_note_gate_model_partition
ON acceptance(note_path, gate_path, model_partition);
CREATE VIEW current_gate_acceptances AS SELECT * FROM acceptance;
PRAGMA user_version = 4;
"""


def test_migration_preserves_accepted_pair_identity_and_refuses_v5_rerun(tmp_path: Path) -> None:
    db_path = tmp_path / "review.sqlite"
    with sqlite3.connect(db_path) as conn:
        conn.executescript(V4_SCHEMA)
        conn.execute(
            "INSERT INTO review_jobs VALUES (7, 'test-model', NULL, NULL, NULL, ?, ?, 'completed', NULL, NULL, 'note')",
            (NOW, NOW),
        )
        conn.execute(
            "INSERT INTO review_pairs VALUES (42, 7, ?, ?, 1, 'warn', NULL, NULL, ?)",
            (NOTE_PATH, CRITIQUE_PATH, NOW),
        )
        conn.execute(
            "INSERT INTO acceptance VALUES (?, ?, 'test-model', 42, NULL, NULL, ?)",
            (NOTE_PATH, CRITIQUE_PATH, NOW),
        )
        conn.commit()

    script = Path(__file__).parents[3] / "scripts/migrate-review-db-v4-to-v5.py"
    first = subprocess.run(
        [sys.executable, str(script), str(db_path)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert first.returncode == 0, first.stderr
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            """
            SELECT rp.review_pair_id, rp.result_kind, a.accepted_review_pair_id
            FROM acceptance AS a
            JOIN review_pairs AS rp ON rp.review_pair_id = a.accepted_review_pair_id
            """
        ).fetchone()
        assert dict(row) == {
            "review_pair_id": 42,
            "result_kind": "verdict",
            "accepted_review_pair_id": 42,
        }
        assert conn.execute("PRAGMA user_version").fetchone()[0] == 5
        assert conn.execute("PRAGMA foreign_key_check").fetchall() == []

    second = subprocess.run(
        [sys.executable, str(script), str(db_path)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert second.returncode != 0
    assert "expected review schema version 4, found 5" in second.stderr
