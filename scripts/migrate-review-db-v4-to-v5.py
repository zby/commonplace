#!/usr/bin/env python3
"""Migrate a populated Commonplace review store from schema v4 to v5."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


REVIEW_PAIRS_V5 = """
CREATE TABLE review_pairs_new (
    review_pair_id INTEGER PRIMARY KEY,
    review_job_id INTEGER NOT NULL REFERENCES review_jobs(review_job_id) ON DELETE CASCADE,
    note_path TEXT NOT NULL,
    gate_path TEXT NOT NULL,
    pair_ordinal INTEGER NOT NULL,
    result_kind TEXT NOT NULL CHECK (result_kind IN ('verdict', 'report')),
    decision TEXT CHECK (decision IN ('pass', 'warn', 'fail', 'error')),
    reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id),
    reviewed_at TEXT,
    CHECK (result_kind = 'verdict' OR decision IS NULL),
    UNIQUE (review_job_id, note_path, gate_path),
    UNIQUE (review_job_id, pair_ordinal)
)
"""

CURRENT_ACCEPTANCES_V5 = """
CREATE VIEW current_gate_acceptances AS
SELECT
    e.note_path,
    e.gate_path,
    e.model_partition,
    e.accepted_review_pair_id,
    e.accepted_note_snapshot_id,
    e.accepted_gate_snapshot_id,
    note_snapshot.content_sha256 AS accepted_note_hash,
    gate_snapshot.content_sha256 AS accepted_gate_hash,
    note_snapshot.content_text AS accepted_note_text,
    gate_snapshot.content_text AS accepted_gate_text,
    e.accepted_at,
    rp.result_kind,
    rp.decision
FROM acceptance AS e
JOIN review_pairs AS rp
  ON rp.review_pair_id = e.accepted_review_pair_id
 AND rp.note_path = e.note_path
 AND rp.gate_path = e.gate_path
JOIN review_jobs AS j
  ON j.review_job_id = rp.review_job_id
 AND j.model_partition = e.model_partition
LEFT JOIN review_file_snapshots AS note_snapshot
  ON e.accepted_note_snapshot_id = note_snapshot.snapshot_id
LEFT JOIN review_file_snapshots AS gate_snapshot
  ON e.accepted_gate_snapshot_id = gate_snapshot.snapshot_id
WHERE j.status = 'completed'
  AND rp.reviewed_at IS NOT NULL
  AND (rp.result_kind = 'report' OR rp.decision IS NOT NULL)
"""


def migrate(db_path: Path) -> None:
    conn = sqlite3.connect(db_path, isolation_level=None)
    try:
        conn.execute("PRAGMA foreign_keys = OFF")
        version = int(conn.execute("PRAGMA user_version").fetchone()[0])
        if version != 4:
            raise RuntimeError(f"expected review schema version 4, found {version}; migration refused")

        conn.execute("BEGIN IMMEDIATE")
        try:
            conn.execute("DROP VIEW IF EXISTS current_gate_acceptances")
            conn.execute(REVIEW_PAIRS_V5)
            conn.execute(
                """
                INSERT INTO review_pairs_new (
                    review_pair_id,
                    review_job_id,
                    note_path,
                    gate_path,
                    pair_ordinal,
                    result_kind,
                    decision,
                    reviewed_note_snapshot_id,
                    reviewed_gate_snapshot_id,
                    reviewed_at
                )
                SELECT
                    review_pair_id,
                    review_job_id,
                    note_path,
                    gate_path,
                    pair_ordinal,
                    'verdict',
                    decision,
                    reviewed_note_snapshot_id,
                    reviewed_gate_snapshot_id,
                    reviewed_at
                FROM review_pairs
                """
            )
            conn.execute("DROP TABLE review_pairs")
            conn.execute("ALTER TABLE review_pairs_new RENAME TO review_pairs")
            conn.execute(
                "CREATE INDEX idx_review_pairs_note_gate ON review_pairs(note_path, gate_path)"
            )
            conn.execute(
                "CREATE INDEX idx_review_pairs_review_job_id ON review_pairs(review_job_id)"
            )
            conn.execute(CURRENT_ACCEPTANCES_V5)
            violations = conn.execute("PRAGMA foreign_key_check").fetchall()
            if violations:
                raise RuntimeError(f"foreign key check failed: {violations}")
            conn.execute("PRAGMA user_version = 5")
            conn.execute("COMMIT")
        except Exception:
            conn.execute("ROLLBACK")
            raise
    finally:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "database",
        nargs="?",
        type=Path,
        default=Path("kb/reports/review-store.sqlite"),
        help="Review-store SQLite path (default: kb/reports/review-store.sqlite).",
    )
    args = parser.parse_args(argv)
    try:
        migrate(args.database)
    except (OSError, sqlite3.Error, RuntimeError) as exc:
        parser.error(str(exc))
    print(f"migrated {args.database} from review schema v4 to v5")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
