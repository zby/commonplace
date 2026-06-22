#!/usr/bin/env python3
"""Migrate the legacy review DB shape to review_runs + review_pairs.

This is a workshop script, not an installed Commonplace command. Run it against
the copied DB under kb/work/create-review-runs/db-scratch/ while iterating.
"""

from __future__ import annotations

import argparse
import shutil
import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


DEFAULT_DB = Path("kb/work/create-review-runs/db-scratch/review-store.sqlite")


@dataclass(frozen=True)
class MigrationPlan:
    legacy_review_runs: int
    legacy_review_run_gates: int
    legacy_gate_reviews: int
    legacy_manual_import_reviews: int
    legacy_acceptance_events: int
    legacy_null_acceptances: int
    note_packed_review_runs: int
    gate_packed_review_runs: int
    gate_packed_legacy_runs: int
    requested_review_pairs: int
    synthetic_review_runs: int
    migrated_review_runs: int
    migrated_review_pairs: int
    migrated_acceptance_events: int


def connect(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def _table_names(conn: sqlite3.Connection) -> set[str]:
    rows = conn.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        """
    ).fetchall()
    return {str(row["name"]) for row in rows}


def _column_names(conn: sqlite3.Connection, table: str) -> set[str]:
    rows = conn.execute(f"PRAGMA table_info({table})").fetchall()
    return {str(row["name"]) for row in rows}


def is_migrated(conn: sqlite3.Connection) -> bool:
    tables = _table_names(conn)
    return "review_pairs" in tables and "review_pair_id" in _column_names(conn, "review_pairs")


def _required_legacy_tables(conn: sqlite3.Connection) -> None:
    required = {"review_runs", "review_run_gates", "gate_reviews", "acceptance_events"}
    missing = sorted(required - _table_names(conn))
    if missing:
        raise RuntimeError(f"legacy review schema missing tables: {', '.join(missing)}")


def _int(conn: sqlite3.Connection, sql: str, params: tuple[object, ...] = ()) -> int:
    return int(conn.execute(sql, params).fetchone()[0])


def _exec_many(conn: sqlite3.Connection, statements: tuple[str, ...]) -> None:
    for statement in statements:
        conn.execute(statement)


def _current_gate_review_ids(conn: sqlite3.Connection) -> set[int]:
    rows = conn.execute(
        """
        WITH latest_acceptance AS (
            SELECT
                id,
                note_path,
                gate_id,
                model_id,
                accepted_review_id,
                ROW_NUMBER() OVER (
                    PARTITION BY note_path, gate_id, model_id
                    ORDER BY id DESC
                ) AS rn
            FROM acceptance_events
        ),
        latest_gate_review AS (
            SELECT
                id,
                note_path,
                gate_id,
                model_id,
                ROW_NUMBER() OVER (
                    PARTITION BY note_path, gate_id, model_id
                    ORDER BY reviewed_at DESC, id DESC
                ) AS rn
            FROM gate_reviews
        )
        SELECT COALESCE(a.accepted_review_id, gr.id) AS gate_review_id
        FROM latest_acceptance AS a
        LEFT JOIN latest_gate_review AS gr
          ON gr.note_path = a.note_path
         AND gr.gate_id = a.gate_id
         AND gr.model_id = a.model_id
         AND gr.rn = 1
        WHERE a.rn = 1
          AND COALESCE(a.accepted_review_id, gr.id) IS NOT NULL
        """
    ).fetchall()
    return {int(row["gate_review_id"]) for row in rows}


def validate_preconditions(conn: sqlite3.Connection) -> None:
    if is_migrated(conn):
        raise RuntimeError("database already has review_pairs; refusing to migrate again")

    _required_legacy_tables(conn)

    full_reviews_without_requested_pair = _int(
        conn,
        """
        SELECT COUNT(*)
        FROM gate_reviews AS gr
        LEFT JOIN review_run_gates AS rrg
          ON rrg.review_run_id = gr.review_run_id
         AND rrg.gate_id = gr.gate_id
        WHERE gr.review_run_id IS NOT NULL
          AND rrg.review_run_id IS NULL
        """,
    )
    if full_reviews_without_requested_pair:
        raise RuntimeError(
            "legacy gate_reviews contains full-review rows without matching review_run_gates: "
            f"{full_reviews_without_requested_pair}"
        )

    missing_acceptance_targets = _int(
        conn,
        """
        SELECT COUNT(*)
        FROM acceptance_events AS ae
        LEFT JOIN gate_reviews AS gr
          ON gr.id = ae.accepted_review_id
        WHERE ae.accepted_review_id IS NOT NULL
          AND gr.id IS NULL
        """,
    )
    if missing_acceptance_targets:
        raise RuntimeError(f"acceptance_events references missing gate_reviews: {missing_acceptance_targets}")

    current_gate_review_ids = _current_gate_review_ids(conn)
    all_gate_review_ids = {
        int(row["id"])
        for row in conn.execute(
            """
            SELECT id
            FROM gate_reviews
            """
        ).fetchall()
    }
    obsolete_ids = sorted(all_gate_review_ids - current_gate_review_ids)
    if obsolete_ids:
        raise RuntimeError(
            "legacy gate_reviews still contains superseded rows; run the prune script first "
            f"({len(obsolete_ids)} rows)"
        )

    current_acceptance_count = _int(conn, "SELECT COUNT(*) FROM current_gate_acceptances")
    acceptance_count = _int(conn, "SELECT COUNT(*) FROM acceptance_events")
    if current_acceptance_count != acceptance_count:
        raise RuntimeError(
            "legacy acceptance_events still contains superseded rows; run the prune script first "
            f"({acceptance_count - current_acceptance_count} rows)"
        )


def build_plan(conn: sqlite3.Connection) -> MigrationPlan:
    validate_preconditions(conn)
    legacy_review_run_gates = _int(conn, "SELECT COUNT(*) FROM review_run_gates")
    legacy_manual_import_reviews = _int(conn, "SELECT COUNT(*) FROM gate_reviews WHERE review_run_id IS NULL")
    gate_packed_review_runs = _int(
        conn,
        """
        WITH run_gate_counts AS (
            SELECT
                rr.id,
                rr.started_at,
                rr.runner,
                rr.model_id,
                COUNT(rrg.gate_id) AS gate_count,
                MIN(rrg.gate_id) AS gate_id
            FROM review_runs AS rr
            JOIN review_run_gates AS rrg
              ON rrg.review_run_id = rr.id
            GROUP BY rr.id
        )
        SELECT COUNT(*)
        FROM (
            SELECT started_at, runner, model_id, gate_id
            FROM run_gate_counts
            WHERE gate_count = 1
            GROUP BY started_at, runner, model_id, gate_id
            HAVING COUNT(*) > 1
        )
        """,
    )
    gate_packed_legacy_runs = _int(
        conn,
        """
        WITH run_gate_counts AS (
            SELECT
                rr.id,
                rr.started_at,
                rr.runner,
                rr.model_id,
                COUNT(rrg.gate_id) AS gate_count,
                MIN(rrg.gate_id) AS gate_id
            FROM review_runs AS rr
            JOIN review_run_gates AS rrg
              ON rrg.review_run_id = rr.id
            GROUP BY rr.id
        ),
        gate_packed_groups AS (
            SELECT started_at, runner, model_id, gate_id
            FROM run_gate_counts
            WHERE gate_count = 1
            GROUP BY started_at, runner, model_id, gate_id
            HAVING COUNT(*) > 1
        )
        SELECT COUNT(*)
        FROM run_gate_counts AS rgc
        JOIN gate_packed_groups AS g
          ON g.started_at = rgc.started_at
         AND g.runner = rgc.runner
         AND g.model_id = rgc.model_id
         AND g.gate_id = rgc.gate_id
        """,
    )
    legacy_review_runs = _int(conn, "SELECT COUNT(*) FROM review_runs")
    note_packed_review_runs = legacy_review_runs - gate_packed_legacy_runs
    synthetic_review_runs = legacy_manual_import_reviews
    return MigrationPlan(
        legacy_review_runs=legacy_review_runs,
        legacy_review_run_gates=legacy_review_run_gates,
        legacy_gate_reviews=_int(conn, "SELECT COUNT(*) FROM gate_reviews"),
        legacy_manual_import_reviews=legacy_manual_import_reviews,
        legacy_acceptance_events=_int(conn, "SELECT COUNT(*) FROM acceptance_events"),
        legacy_null_acceptances=_int(conn, "SELECT COUNT(*) FROM acceptance_events WHERE accepted_review_id IS NULL"),
        note_packed_review_runs=note_packed_review_runs,
        gate_packed_review_runs=gate_packed_review_runs,
        gate_packed_legacy_runs=gate_packed_legacy_runs,
        requested_review_pairs=legacy_review_run_gates,
        synthetic_review_runs=synthetic_review_runs,
        migrated_review_runs=note_packed_review_runs + gate_packed_review_runs + synthetic_review_runs,
        migrated_review_pairs=legacy_review_run_gates + legacy_manual_import_reviews,
        migrated_acceptance_events=_int(conn, "SELECT COUNT(*) FROM acceptance_events"),
    )


def _create_new_schema(conn: sqlite3.Connection) -> None:
    _exec_many(
        conn,
        (
            """
        CREATE TABLE review_runs (
            review_run_id INTEGER PRIMARY KEY,
            model_id TEXT NOT NULL,
            runner TEXT NOT NULL,
            started_at TEXT NOT NULL,
            completed_at TEXT,
            status TEXT NOT NULL CHECK (
                status IN ('running', 'completed', 'failed')
            ),
            failure_reason TEXT,
            telemetry_json TEXT,
            raw_bundle_markdown TEXT,
            debug_log TEXT,
            packing TEXT NOT NULL CHECK (
                packing IN ('note', 'gate', 'manual-import')
            )
        )
        """,
            """
        CREATE INDEX idx_review_runs_v1_model_started
        ON review_runs(model_id, started_at DESC);
        """,
            """
        CREATE INDEX idx_review_runs_v1_status
        ON review_runs(status);
        """,
            """
        CREATE TABLE review_pairs (
            review_pair_id INTEGER PRIMARY KEY,
            review_run_id INTEGER NOT NULL REFERENCES review_runs(review_run_id) ON DELETE CASCADE,
            note_path TEXT NOT NULL,
            gate_id TEXT NOT NULL,
            model_id TEXT NOT NULL,
            pair_ordinal INTEGER NOT NULL,
            pair_status TEXT NOT NULL CHECK (
                pair_status IN ('pending', 'completed', 'missing')
            ),
            decision TEXT CHECK (
                decision IN ('pass', 'warn', 'fail', 'error', 'unknown')
            ),
            rationale_markdown TEXT,
            evidence_json TEXT,
            gate_sha TEXT NOT NULL,
            reviewed_note_sha TEXT NOT NULL,
            reviewed_note_commit TEXT,
            reviewed_at TEXT,
            review_kind TEXT NOT NULL CHECK (
                review_kind IN ('full-review', 'manual-import')
            ),
            UNIQUE (review_run_id, note_path, gate_id),
            UNIQUE (review_run_id, pair_ordinal)
        )
        """,
            """
        CREATE INDEX idx_review_pairs_v1_note_gate_model
        ON review_pairs(note_path, gate_id, model_id);
        """,
            """
        CREATE INDEX idx_review_pairs_v1_review_run_id
        ON review_pairs(review_run_id);
        """,
            """
        CREATE INDEX idx_review_pairs_v1_status
        ON review_pairs(pair_status);
        """,
            """
        CREATE TABLE legacy_gate_review_map (
            legacy_gate_review_id INTEGER PRIMARY KEY,
            review_pair_id INTEGER NOT NULL UNIQUE REFERENCES review_pairs(review_pair_id) ON DELETE CASCADE
        )
        """,
            """
        CREATE TABLE legacy_review_run_map (
            legacy_review_run_id INTEGER PRIMARY KEY,
            review_run_id INTEGER NOT NULL REFERENCES review_runs(review_run_id) ON DELETE CASCADE,
            inferred_packing TEXT NOT NULL CHECK (
                inferred_packing IN ('note', 'gate')
            )
        )
        """,
            """
        CREATE TABLE acceptance_events (
            acceptance_event_id INTEGER PRIMARY KEY,
            note_path TEXT NOT NULL,
            gate_id TEXT NOT NULL,
            model_id TEXT NOT NULL,
            accepted_review_pair_id INTEGER REFERENCES review_pairs(review_pair_id) ON DELETE SET NULL,
            accepted_note_sha TEXT NOT NULL,
            accepted_note_commit TEXT,
            accepted_gate_sha TEXT NOT NULL,
            accepted_at TEXT NOT NULL,
            acceptance_kind TEXT NOT NULL CHECK (
                acceptance_kind IN (
                    'full-review',
                    'gate-migration',
                    'trivial-change-ack',
                    'migration-import',
                    'manual-override'
                )
            )
        )
        """,
            """
        CREATE INDEX idx_acceptance_events_v1_note_gate_model
        ON acceptance_events(note_path, gate_id, model_id, accepted_at DESC);
        """,
            """
        CREATE INDEX idx_acceptance_events_v1_latest_by_key
        ON acceptance_events(note_path, gate_id, model_id, acceptance_event_id DESC);
        """,
            """
        CREATE VIEW current_gate_acceptances AS
        SELECT
            e.note_path,
            e.gate_id,
            e.model_id,
            e.accepted_review_pair_id,
            e.accepted_note_sha,
            e.accepted_note_commit,
            e.accepted_gate_sha,
            e.accepted_at,
            e.acceptance_kind
        FROM acceptance_events AS e
        JOIN (
            SELECT
                note_path,
                gate_id,
                model_id,
                MAX(acceptance_event_id) AS max_id
            FROM acceptance_events
            GROUP BY note_path, gate_id, model_id
        ) AS latest
          ON e.acceptance_event_id = latest.max_id;
        """,
            """
        CREATE VIEW stale_gate_pairs AS
        SELECT
            a.note_path,
            a.gate_id,
            a.model_id,
            a.accepted_note_sha,
            a.accepted_gate_sha
        FROM current_gate_acceptances AS a;
        """,
            """
        CREATE TABLE review_schema_migrations (
            migration_name TEXT PRIMARY KEY,
            applied_at TEXT NOT NULL
        )
        """,
        ),
    )


def _rename_legacy_schema(conn: sqlite3.Connection) -> None:
    _exec_many(
        conn,
        (
            "DROP VIEW IF EXISTS stale_gate_pairs",
            "DROP VIEW IF EXISTS current_gate_acceptances",
            "ALTER TABLE review_runs RENAME TO legacy_review_runs",
            "ALTER TABLE review_run_gates RENAME TO legacy_review_run_gates",
            "ALTER TABLE gate_reviews RENAME TO legacy_gate_reviews",
            "ALTER TABLE acceptance_events RENAME TO legacy_acceptance_events",
        ),
    )


def _copy_inferred_review_runs(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        WITH run_gate_counts AS (
            SELECT
                rr.id,
                rr.started_at,
                rr.runner,
                rr.model_id,
                COUNT(rrg.gate_id) AS gate_count,
                MIN(rrg.gate_id) AS gate_id
            FROM legacy_review_runs AS rr
            JOIN legacy_review_run_gates AS rrg
              ON rrg.review_run_id = rr.id
            GROUP BY rr.id
        ),
        gate_packed_groups AS (
            SELECT started_at, runner, model_id, gate_id
            FROM run_gate_counts
            WHERE gate_count = 1
            GROUP BY started_at, runner, model_id, gate_id
            HAVING COUNT(*) > 1
        ),
        gate_packed_legacy_runs AS (
            SELECT rgc.id
            FROM run_gate_counts AS rgc
            JOIN gate_packed_groups AS g
              ON g.started_at = rgc.started_at
             AND g.runner = rgc.runner
             AND g.model_id = rgc.model_id
             AND g.gate_id = rgc.gate_id
        )
        INSERT INTO review_runs (
            review_run_id,
            model_id,
            runner,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log,
            packing
        )
        SELECT
            rr.id,
            rr.model_id,
            rr.runner,
            rr.started_at,
            rr.completed_at,
            rr.status,
            rr.failure_reason,
            rr.telemetry_json,
            rr.raw_bundle_markdown,
            rr.debug_log,
            'note'
        FROM legacy_review_runs AS rr
        LEFT JOIN gate_packed_legacy_runs AS packed
          ON packed.id = rr.id
        WHERE packed.id IS NULL
        ORDER BY rr.id
        """
    )
    conn.execute(
        """
        WITH run_gate_counts AS (
            SELECT
                rr.id,
                rr.started_at,
                rr.runner,
                rr.model_id,
                COUNT(rrg.gate_id) AS gate_count,
                MIN(rrg.gate_id) AS gate_id
            FROM legacy_review_runs AS rr
            JOIN legacy_review_run_gates AS rrg
              ON rrg.review_run_id = rr.id
            GROUP BY rr.id
        ),
        gate_packed_groups AS (
            SELECT
                started_at,
                runner,
                model_id,
                gate_id,
                MIN(id) AS review_run_id
            FROM run_gate_counts
            WHERE gate_count = 1
            GROUP BY started_at, runner, model_id, gate_id
            HAVING COUNT(*) > 1
        ),
        grouped_runs AS (
            SELECT
                g.review_run_id,
                rr.id AS legacy_review_run_id,
                rr.note_path,
                rr.model_id,
                rr.runner,
                rr.started_at,
                rr.completed_at,
                rr.status,
                rr.failure_reason,
                rr.telemetry_json,
                rr.raw_bundle_markdown,
                rr.debug_log
            FROM run_gate_counts AS rgc
            JOIN gate_packed_groups AS g
              ON g.started_at = rgc.started_at
             AND g.runner = rgc.runner
             AND g.model_id = rgc.model_id
             AND g.gate_id = rgc.gate_id
            JOIN legacy_review_runs AS rr
              ON rr.id = rgc.id
        )
        INSERT INTO review_runs (
            review_run_id,
            model_id,
            runner,
            started_at,
            completed_at,
            status,
            failure_reason,
            telemetry_json,
            raw_bundle_markdown,
            debug_log,
            packing
        )
        SELECT
            review_run_id,
            MIN(model_id),
            MIN(runner),
            MIN(started_at),
            CASE
                WHEN SUM(CASE WHEN status = 'running' THEN 1 ELSE 0 END) > 0 THEN NULL
                ELSE MAX(completed_at)
            END,
            CASE
                WHEN SUM(CASE WHEN status = 'running' THEN 1 ELSE 0 END) > 0 THEN 'running'
                WHEN SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) > 0 THEN 'failed'
                ELSE 'completed'
            END,
            CASE
                WHEN SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) > 0
                THEN GROUP_CONCAT(
                    CASE
                        WHEN status = 'failed'
                        THEN legacy_review_run_id || ': ' || COALESCE(failure_reason, 'failed')
                    END,
                    char(10)
                )
                ELSE NULL
            END,
            (
                CASE
                    WHEN COUNT(DISTINCT COALESCE(telemetry_json, '<NULL>')) <= 1 THEN MAX(telemetry_json)
                    ELSE json_object(
                        'legacy_gate_packed_telemetry_json_by_run',
                        json_group_array(
                            json_object(
                                'legacy_review_run_id',
                                legacy_review_run_id,
                                'note_path',
                                note_path,
                                'telemetry_json',
                                telemetry_json
                            )
                        )
                    )
                END
            ),
            (
                GROUP_CONCAT(
                    CASE
                        WHEN raw_bundle_markdown IS NOT NULL
                        THEN (
                            '--- legacy review_run '
                            || legacy_review_run_id
                            || ' note: '
                            || note_path
                            || ' ---'
                            || char(10)
                            || raw_bundle_markdown
                        )
                    END,
                    char(10) || char(10)
                )
            ),
            (
                GROUP_CONCAT(
                    CASE
                        WHEN debug_log IS NOT NULL
                        THEN (
                            '--- legacy review_run '
                            || legacy_review_run_id
                            || ' note: '
                            || note_path
                            || ' ---'
                            || char(10)
                            || debug_log
                        )
                    END,
                    char(10) || char(10)
                )
            ),
            'gate'
        FROM grouped_runs
        GROUP BY review_run_id
        ORDER BY review_run_id
        """
    )
    conn.execute(
        """
        WITH run_gate_counts AS (
            SELECT
                rr.id,
                rr.started_at,
                rr.runner,
                rr.model_id,
                COUNT(rrg.gate_id) AS gate_count,
                MIN(rrg.gate_id) AS gate_id
            FROM legacy_review_runs AS rr
            JOIN legacy_review_run_gates AS rrg
              ON rrg.review_run_id = rr.id
            GROUP BY rr.id
        ),
        gate_packed_groups AS (
            SELECT
                started_at,
                runner,
                model_id,
                gate_id,
                MIN(id) AS review_run_id
            FROM run_gate_counts
            WHERE gate_count = 1
            GROUP BY started_at, runner, model_id, gate_id
            HAVING COUNT(*) > 1
        ),
        gate_packed_legacy_runs AS (
            SELECT
                rgc.id AS legacy_review_run_id,
                g.review_run_id
            FROM run_gate_counts AS rgc
            JOIN gate_packed_groups AS g
              ON g.started_at = rgc.started_at
             AND g.runner = rgc.runner
             AND g.model_id = rgc.model_id
             AND g.gate_id = rgc.gate_id
        )
        INSERT INTO legacy_review_run_map (
            legacy_review_run_id,
            review_run_id,
            inferred_packing
        )
        SELECT
            rr.id,
            COALESCE(packed.review_run_id, rr.id),
            CASE WHEN packed.review_run_id IS NULL THEN 'note' ELSE 'gate' END
        FROM legacy_review_runs AS rr
        LEFT JOIN gate_packed_legacy_runs AS packed
          ON packed.legacy_review_run_id = rr.id
        ORDER BY rr.id
        """
    )


def _copy_requested_pairs(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        WITH requested_pairs AS (
            SELECT
                map.review_run_id,
                map.inferred_packing,
                rr.id AS legacy_review_run_id,
                rr.note_path,
                rrg.gate_id,
                rr.model_id,
                CASE
                    WHEN map.inferred_packing = 'gate'
                    THEN ROW_NUMBER() OVER (
                        PARTITION BY map.review_run_id
                        ORDER BY rr.id
                    ) - 1
                    ELSE rrg.ordinal
                END AS pair_ordinal,
                CASE
                    WHEN gr.id IS NOT NULL THEN 'completed'
                    WHEN rr.status = 'running' THEN 'pending'
                    ELSE 'missing'
                END AS pair_status,
                gr.decision,
                gr.rationale_markdown,
                gr.evidence_json,
                rrg.gate_sha,
                rr.reviewed_note_sha,
                rr.reviewed_note_commit,
                gr.reviewed_at,
                COALESCE(gr.review_kind, 'full-review') AS review_kind
            FROM legacy_review_run_gates AS rrg
            JOIN legacy_review_runs AS rr
              ON rr.id = rrg.review_run_id
            JOIN legacy_review_run_map AS map
              ON map.legacy_review_run_id = rr.id
            LEFT JOIN legacy_gate_reviews AS gr
              ON gr.review_run_id = rrg.review_run_id
             AND gr.gate_id = rrg.gate_id
        )
        INSERT INTO review_pairs (
            review_run_id,
            note_path,
            gate_id,
            model_id,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        )
        SELECT
            review_run_id,
            note_path,
            gate_id,
            model_id,
            pair_ordinal,
            pair_status,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM requested_pairs
        ORDER BY review_run_id, pair_ordinal
        """
    )
    conn.execute(
        """
        INSERT INTO legacy_gate_review_map (
            legacy_gate_review_id,
            review_pair_id
        )
        SELECT
            gr.id,
            rp.review_pair_id
        FROM legacy_gate_reviews AS gr
        JOIN legacy_review_run_map AS map
          ON map.legacy_review_run_id = gr.review_run_id
        JOIN review_pairs AS rp
          ON rp.review_run_id = map.review_run_id
         AND rp.gate_id = gr.gate_id
         AND rp.note_path = gr.note_path
        WHERE gr.review_run_id IS NOT NULL
        ORDER BY gr.id
        """
    )


def _copy_manual_imports(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        """
        SELECT
            id,
            note_path,
            gate_id,
            model_id,
            decision,
            rationale_markdown,
            evidence_json,
            gate_sha,
            reviewed_note_sha,
            reviewed_note_commit,
            reviewed_at,
            review_kind
        FROM legacy_gate_reviews
        WHERE review_run_id IS NULL
        ORDER BY id
        """
    ).fetchall()
    for row in rows:
        run_cursor = conn.execute(
            """
            INSERT INTO review_runs (
                model_id,
                runner,
                started_at,
                completed_at,
                status,
                failure_reason,
                telemetry_json,
                raw_bundle_markdown,
                debug_log,
                packing
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["model_id"],
                "manual-import",
                row["reviewed_at"],
                row["reviewed_at"],
                "completed",
                None,
                None,
                None,
                None,
                "manual-import",
            ),
        )
        review_run_id = int(run_cursor.lastrowid)
        pair_cursor = conn.execute(
            """
            INSERT INTO review_pairs (
                review_run_id,
                note_path,
                gate_id,
                model_id,
                pair_ordinal,
                pair_status,
                decision,
                rationale_markdown,
                evidence_json,
                gate_sha,
                reviewed_note_sha,
                reviewed_note_commit,
                reviewed_at,
                review_kind
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                review_run_id,
                row["note_path"],
                row["gate_id"],
                row["model_id"],
                0,
                "completed",
                row["decision"],
                row["rationale_markdown"],
                row["evidence_json"],
                row["gate_sha"],
                row["reviewed_note_sha"],
                row["reviewed_note_commit"],
                row["reviewed_at"],
                row["review_kind"],
            ),
        )
        conn.execute(
            """
            INSERT INTO legacy_gate_review_map (
                legacy_gate_review_id,
                review_pair_id
            ) VALUES (?, ?)
            """,
            (row["id"], int(pair_cursor.lastrowid)),
        )


def _copy_acceptance_events(conn: sqlite3.Connection) -> None:
    missing_mapped_acceptances = _int(
        conn,
        """
        SELECT COUNT(*)
        FROM legacy_acceptance_events AS ae
        LEFT JOIN legacy_gate_review_map AS map
          ON map.legacy_gate_review_id = ae.accepted_review_id
        WHERE ae.accepted_review_id IS NOT NULL
          AND map.review_pair_id IS NULL
        """,
    )
    if missing_mapped_acceptances:
        raise RuntimeError(f"acceptance_events could not be mapped to review_pairs: {missing_mapped_acceptances}")

    conn.execute(
        """
        INSERT INTO acceptance_events (
            acceptance_event_id,
            note_path,
            gate_id,
            model_id,
            accepted_review_pair_id,
            accepted_note_sha,
            accepted_note_commit,
            accepted_gate_sha,
            accepted_at,
            acceptance_kind
        )
        SELECT
            ae.id,
            ae.note_path,
            ae.gate_id,
            ae.model_id,
            map.review_pair_id,
            ae.accepted_note_sha,
            ae.accepted_note_commit,
            ae.accepted_gate_sha,
            ae.accepted_at,
            ae.acceptance_kind
        FROM legacy_acceptance_events AS ae
        LEFT JOIN legacy_gate_review_map AS map
          ON map.legacy_gate_review_id = ae.accepted_review_id
        ORDER BY ae.id
        """
    )


def _record_migration(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        INSERT INTO review_schema_migrations (
            migration_name,
            applied_at
        ) VALUES (?, ?)
        """,
        ("review-pairs-v1", datetime.now(UTC).isoformat()),
    )


def _validate_migrated(conn: sqlite3.Connection, expected: MigrationPlan) -> None:
    actual_runs = _int(conn, "SELECT COUNT(*) FROM review_runs")
    actual_pairs = _int(conn, "SELECT COUNT(*) FROM review_pairs")
    actual_acceptances = _int(conn, "SELECT COUNT(*) FROM acceptance_events")
    actual_run_map = _int(conn, "SELECT COUNT(*) FROM legacy_review_run_map")
    actual_map = _int(conn, "SELECT COUNT(*) FROM legacy_gate_review_map")

    expected_runs = expected.migrated_review_runs
    if actual_runs != expected_runs:
        raise RuntimeError(f"migrated review_runs count mismatch: expected {expected_runs}, got {actual_runs}")
    if actual_pairs != expected.migrated_review_pairs:
        raise RuntimeError(
            f"migrated review_pairs count mismatch: expected {expected.migrated_review_pairs}, got {actual_pairs}"
        )
    if actual_acceptances != expected.migrated_acceptance_events:
        raise RuntimeError(
            "migrated acceptance_events count mismatch: "
            f"expected {expected.migrated_acceptance_events}, got {actual_acceptances}"
        )
    if actual_map != expected.legacy_gate_reviews:
        raise RuntimeError(
            f"legacy_gate_review_map count mismatch: expected {expected.legacy_gate_reviews}, got {actual_map}"
        )
    if actual_run_map != expected.legacy_review_runs:
        raise RuntimeError(
            f"legacy_review_run_map count mismatch: expected {expected.legacy_review_runs}, got {actual_run_map}"
        )

    unmapped_current_acceptances = _int(
        conn,
        """
        SELECT COUNT(*)
        FROM acceptance_events
        WHERE accepted_review_pair_id IS NULL
          AND acceptance_kind IN ('full-review', 'manual-import')
        """,
    )
    if unmapped_current_acceptances:
        raise RuntimeError(f"accepted review events lost their review_pair mapping: {unmapped_current_acceptances}")

    fk_errors = conn.execute("PRAGMA foreign_key_check").fetchall()
    if fk_errors:
        raise RuntimeError(f"foreign key check failed: {fk_errors[:5]}")

    integrity_rows = conn.execute("PRAGMA integrity_check").fetchall()
    integrity_results = [str(row[0]) for row in integrity_rows]
    if integrity_results != ["ok"]:
        raise RuntimeError(f"integrity check failed: {integrity_results[:5]}")


def apply_migration(conn: sqlite3.Connection, expected: MigrationPlan) -> None:
    conn.isolation_level = None
    conn.execute("PRAGMA foreign_keys = OFF")
    conn.execute("BEGIN")
    try:
        _rename_legacy_schema(conn)
        _create_new_schema(conn)
        _copy_inferred_review_runs(conn)
        _copy_requested_pairs(conn)
        _copy_manual_imports(conn)
        _copy_acceptance_events(conn)
        _record_migration(conn)
        conn.execute("PRAGMA foreign_keys = ON")
        _validate_migrated(conn, expected)
    except Exception:
        conn.execute("ROLLBACK")
        raise
    else:
        conn.execute("COMMIT")


def print_plan(plan: MigrationPlan, *, mode: str) -> None:
    print(f"legacy_review_runs: {plan.legacy_review_runs}")
    print(f"legacy_review_run_gates: {plan.legacy_review_run_gates}")
    print(f"legacy_gate_reviews: {plan.legacy_gate_reviews}")
    print(f"legacy_manual_import_reviews: {plan.legacy_manual_import_reviews}")
    print(f"legacy_acceptance_events: {plan.legacy_acceptance_events}")
    print(f"legacy_null_acceptances: {plan.legacy_null_acceptances}")
    print(f"note_packed_review_runs: {plan.note_packed_review_runs}")
    print(f"gate_packed_review_runs: {plan.gate_packed_review_runs}")
    print(f"gate_packed_legacy_runs: {plan.gate_packed_legacy_runs}")
    print(f"requested_review_pairs: {plan.requested_review_pairs}")
    print(f"synthetic_review_runs: {plan.synthetic_review_runs}")
    print(f"migrated_review_runs: {plan.migrated_review_runs}")
    print(f"migrated_review_pairs: {plan.migrated_review_pairs}")
    print(f"migrated_acceptance_events: {plan.migrated_acceptance_events}")
    print(f"mode: {mode}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Migrate a copied review DB to review_pairs.")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help=f"DB to inspect or migrate. Default: {DEFAULT_DB}")
    parser.add_argument("--copy-to", type=Path, help="Copy --db to this path before migrating the copy.")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Validate and print the migration plan. This is the default.")
    mode.add_argument("--apply", action="store_true", help="Apply the migration to --db or --copy-to.")
    args = parser.parse_args(argv)

    db_path = args.db
    if args.copy_to is not None:
        args.copy_to.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(db_path, args.copy_to)
        db_path = args.copy_to

    with connect(db_path) as conn:
        plan = build_plan(conn)
        if args.apply:
            apply_migration(conn, plan)

    print(f"db: {db_path}")
    print_plan(plan, mode="apply" if args.apply else "dry-run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
