from __future__ import annotations

import sqlite3
from pathlib import Path

from commonplace.review import review_db


TEST_MODEL = "claude-opus"
TEST_RUNNER_MODEL = "opus-4-6"
REVIEWED_AT = "2026-04-10T10:05:00+02:00"
ACCEPTED_AT = "2026-04-10T10:06:00+02:00"
GATE_ID = "prose/source-residue"
GATE_PATH = "kb/instructions/review-gates/prose/source-residue.md"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_reviewable_note(path: Path, title: str = "Old note") -> Path:
    return write(
        path,
        f"""---
description: Test note
type: kb/types/note.md
traits: []
status: current
---

# {title}

Body.
""",
    )


def make_gate(repo_root: Path) -> Path:
    return write(
        repo_root / GATE_PATH,
        """---
gate_id: prose/source-residue
name: Source Residue
lens: prose
watches: [body]
staleness: changed
---

## Failure mode

Fixture gate.
""",
    )


def table_rows(conn: sqlite3.Connection, table: str, order_by: str) -> list[dict[str, object]]:
    return [dict(row) for row in conn.execute(f"SELECT * FROM {table} ORDER BY {order_by}").fetchall()]


def review_state_rows(conn: sqlite3.Connection) -> dict[str, list[dict[str, object]]]:
    return {
        "review_jobs": table_rows(conn, "review_jobs", "review_job_id"),
        "review_pairs": table_rows(conn, "review_pairs", "review_pair_id"),
        "acceptance_events": table_rows(conn, "acceptance_events", "acceptance_event_id"),
    }


def seed_accepted_review(repo_root: Path, db_path: Path, *, note_path: str) -> int:
    review_db.ensure_db(db_path)
    with review_db.connect(db_path) as conn:
        note_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=note_path)
        gate_snapshot = review_db.snapshot_file(conn, repo_root=repo_root, path=GATE_PATH)
        review_job_id = review_db.create_job_with_pairs(
            conn,
            model_partition=TEST_MODEL,
            runner="test-runner",
            runner_model=TEST_RUNNER_MODEL,
            runner_effort="high",
            created_at=REVIEWED_AT,
            status="queued",
            packing="note",
            pairs=[
                review_db.ReviewPairRequest(
                    note_path=note_path,
                    gate_path=GATE_PATH,
                    pair_ordinal=0,
                    reviewed_note_snapshot_id=note_snapshot.snapshot_id,
                    reviewed_gate_snapshot_id=gate_snapshot.snapshot_id,
                )
            ],
        )
        review_db.complete_review_pairs(
            conn,
            review_job_id=review_job_id,
            review_pairs=[
                review_db.ReviewPairCompletion(
                    note_path=note_path,
                    gate_path=GATE_PATH,
                    decision="pass",
                    reviewed_at=REVIEWED_AT,
                )
            ],
            reviewed_at=REVIEWED_AT,
        )
        review_pair = review_db.load_review_pairs_for_job(conn, review_job_id=review_job_id)[0]
        review_db.complete_review_job(conn, review_job_id=review_job_id, completed_at=REVIEWED_AT)
        review_db.append_acceptance_event(
            conn,
            note_path=note_path,
            gate_path=GATE_PATH,
            model_partition=TEST_MODEL,
            accepted_review_pair_id=review_pair.review_pair_id,
            accepted_note_snapshot_id=note_snapshot.snapshot_id,
            accepted_gate_snapshot_id=gate_snapshot.snapshot_id,
            accepted_at=ACCEPTED_AT,
        )
        conn.commit()
        return review_pair.review_pair_id
