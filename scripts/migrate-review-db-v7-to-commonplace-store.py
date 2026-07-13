#!/usr/bin/env python3
"""Migrate a read-only review-store schema v7 database to commonplace-store.sqlite."""

from __future__ import annotations

import argparse
import hashlib
import sqlite3
from importlib import resources
from pathlib import Path

from commonplace.freshness.keys import review_pair_target_key
from commonplace.store import DEFAULT_DB_PATH, LEGACY_DB_PATH, STORE_SCHEMA_VERSION


REVIEW_PAIR_KIND = "review-pair"


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _count(conn: sqlite3.Connection, table: str) -> int:
    return int(conn.execute(f"SELECT count(*) FROM {table}").fetchone()[0])


def _connect_readonly(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def _connect_write(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _validate_source(conn: sqlite3.Connection) -> None:
    version = int(conn.execute("PRAGMA user_version").fetchone()[0])
    if version != 7:
        raise RuntimeError(f"expected review schema version 7, found {version}")
    journal_mode = str(conn.execute("PRAGMA journal_mode").fetchone()[0]).lower()
    if journal_mode == "wal":
        raise RuntimeError("source uses WAL; checkpoint before migration")
    if conn.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        raise RuntimeError("source integrity check failed")
    violations = conn.execute("PRAGMA foreign_key_check").fetchall()
    if violations:
        raise RuntimeError(f"source foreign key check failed: {violations}")


def _apply_destination_schema(conn: sqlite3.Connection) -> None:
    with resources.as_file(resources.files("commonplace") / "store-schema.sql") as schema_path:
        conn.executescript(schema_path.read_text(encoding="utf-8"))
    conn.execute(f"PRAGMA user_version = {STORE_SCHEMA_VERSION}")


def _path_exists(repo_root: Path, path: str) -> bool:
    return (repo_root / path).is_file()


def _compare_projections(
    source: sqlite3.Connection,
    dest: sqlite3.Connection,
    *,
    migrated_keys: set[tuple[str, str, str]],
) -> None:
    for note_path, criterion_path, model_partition in sorted(migrated_keys):
        old_row = source.execute(
            """
            SELECT *
            FROM current_freshness_baselines
            WHERE note_path = ? AND criterion_path = ? AND model_partition = ?
            """,
            (note_path, criterion_path, model_partition),
        ).fetchone()
        new_row = dest.execute(
            """
            SELECT *
            FROM current_review_freshness_baselines
            WHERE note_path = ? AND criterion_path = ? AND model_partition = ?
            """,
            (note_path, criterion_path, model_partition),
        ).fetchone()
        if old_row is None or new_row is None:
            raise RuntimeError(
                f"projection mismatch for {note_path} :: {criterion_path} :: {model_partition}"
            )
        for column in (
            "evidence_review_pair_id",
            "baseline_note_snapshot_id",
            "baseline_criterion_snapshot_id",
            "baseline_note_hash",
            "baseline_criterion_hash",
            "baseline_note_text",
            "baseline_criterion_text",
            "baseline_updated_at",
            "result_kind",
            "outcome",
        ):
            if old_row[column] != new_row[column]:
                raise RuntimeError(
                    f"projection field {column} mismatch for "
                    f"{note_path} :: {criterion_path} :: {model_partition}"
                )


def migrate(
    *,
    repo_root: Path,
    source_path: Path,
    destination_path: Path,
) -> dict[str, int]:
    if destination_path.exists():
        raise RuntimeError(f"destination already exists: {destination_path}")
    tmp_path = destination_path.with_suffix(destination_path.suffix + ".tmp")
    if tmp_path.exists():
        raise RuntimeError(f"temporary destination already exists: {tmp_path}")

    source_hash_before = _file_hash(source_path)
    with _connect_readonly(source_path) as source:
        _validate_source(source)
        source_counts = {
            "review_jobs": _count(source, "review_jobs"),
            "review_pairs": _count(source, "review_pairs"),
            "review_file_snapshots": _count(source, "review_file_snapshots"),
            "freshness_baselines": _count(source, "freshness_baselines"),
        }

        tmp_path.parent.mkdir(parents=True, exist_ok=True)
        with _connect_write(tmp_path) as dest:
            _apply_destination_schema(dest)
            dest.execute("ATTACH DATABASE ? AS source", (str(source_path),))
            dest.executescript(
                """
                INSERT INTO artifact_snapshots (
                    snapshot_id, artifact_path, version_kind,
                    content_sha256, content_text, captured_at
                )
                SELECT
                    snapshot_id, path, 'file-text',
                    content_sha256, content_text, captured_at
                FROM source.review_file_snapshots;

                INSERT INTO review_jobs (
                    review_job_id, model_partition, runner, runner_model,
                    runner_effort, created_at, completed_at, status,
                    failure_reason, telemetry_json, grouping
                )
                SELECT
                    review_job_id, model_partition, runner, runner_model,
                    runner_effort, created_at, completed_at, status,
                    failure_reason, telemetry_json, grouping
                FROM source.review_jobs;

                INSERT INTO review_pairs (
                    review_job_id, review_pair_id, note_path, criterion_path,
                    pair_ordinal, result_kind, outcome,
                    reviewed_note_snapshot_id, reviewed_criterion_snapshot_id,
                    expected_baseline_revision, completed_at
                )
                SELECT
                    review_job_id, review_pair_id, note_path, criterion_path,
                    pair_ordinal, result_kind, outcome,
                    reviewed_note_snapshot_id, reviewed_criterion_snapshot_id,
                    NULL, completed_at
                FROM source.review_pairs;
                """
            )

            migrated_keys: set[tuple[str, str, str]] = set()
            skipped_baselines = 0
            baseline_rows = source.execute(
                """
                SELECT
                    note_path, criterion_path, model_partition,
                    evidence_review_pair_id,
                    baseline_note_snapshot_id,
                    baseline_criterion_snapshot_id,
                    baseline_updated_at
                FROM freshness_baselines
                ORDER BY note_path, criterion_path, model_partition
                """
            ).fetchall()
            for row in baseline_rows:
                note_path = row["note_path"]
                criterion_path = row["criterion_path"]
                model_partition = row["model_partition"]
                if not _path_exists(repo_root, note_path) or not _path_exists(repo_root, criterion_path):
                    skipped_baselines += 1
                    continue
                target_key_json = review_pair_target_key(
                    note_path=note_path,
                    criterion_path=criterion_path,
                    model_partition=model_partition,
                )
                cursor = dest.execute(
                    """
                    INSERT INTO freshness_baselines (
                        target_kind, target_key_json, revision, accepted_at
                    ) VALUES (?, ?, 1, ?)
                    """,
                    (REVIEW_PAIR_KIND, target_key_json, row["baseline_updated_at"]),
                )
                target_id = int(cursor.lastrowid)
                for role, snapshot_id, artifact_path in (
                    ("note", row["baseline_note_snapshot_id"], note_path),
                    ("criterion", row["baseline_criterion_snapshot_id"], criterion_path),
                ):
                    dest.execute(
                        """
                        INSERT INTO freshness_inputs (
                            target_id, input_role, artifact_path, version_kind, accepted_snapshot_id
                        ) VALUES (?, ?, ?, 'file-text', ?)
                        """,
                        (target_id, role, artifact_path, snapshot_id),
                    )
                dest.execute(
                    """
                    INSERT INTO review_freshness_evidence (target_id, evidence_review_pair_id)
                    VALUES (?, ?)
                    """,
                    (target_id, row["evidence_review_pair_id"]),
                )
                migrated_keys.add((note_path, criterion_path, model_partition))

            failed_job_ids: set[int] = set()
            queued_pairs = dest.execute(
                """
                SELECT
                    rp.review_pair_id,
                    rp.review_job_id,
                    rp.note_path,
                    rp.criterion_path,
                    rp.reviewed_note_snapshot_id,
                    rp.reviewed_criterion_snapshot_id,
                    j.model_partition
                FROM review_pairs AS rp
                JOIN review_jobs AS j
                  ON j.review_job_id = rp.review_job_id
                WHERE j.status = 'queued'
                """
            ).fetchall()
            for pair in queued_pairs:
                key = (pair["note_path"], pair["criterion_path"], pair["model_partition"])
                baseline_row = dest.execute(
                    """
                    SELECT b.target_id, b.revision,
                           note_input.accepted_snapshot_id AS note_snapshot_id,
                           criterion_input.accepted_snapshot_id AS criterion_snapshot_id
                    FROM freshness_baselines AS b
                    JOIN freshness_inputs AS note_input
                      ON note_input.target_id = b.target_id
                     AND note_input.input_role = 'note'
                    JOIN freshness_inputs AS criterion_input
                      ON criterion_input.target_id = b.target_id
                     AND criterion_input.input_role = 'criterion'
                    WHERE b.target_kind = ?
                      AND b.target_key_json = ?
                    """,
                    (
                        REVIEW_PAIR_KIND,
                        review_pair_target_key(
                            note_path=pair["note_path"],
                            criterion_path=pair["criterion_path"],
                            model_partition=pair["model_partition"],
                        ),
                    ),
                ).fetchone()
                expected_revision = int(baseline_row["revision"]) if baseline_row is not None else None
                dest.execute(
                    """
                    UPDATE review_pairs
                    SET expected_baseline_revision = ?
                    WHERE review_pair_id = ?
                    """,
                    (expected_revision, pair["review_pair_id"]),
                )
                if baseline_row is None:
                    continue
                note_mismatch = (
                    pair["reviewed_note_snapshot_id"] is not None
                    and int(pair["reviewed_note_snapshot_id"]) != int(baseline_row["note_snapshot_id"])
                )
                criterion_mismatch = (
                    pair["reviewed_criterion_snapshot_id"] is not None
                    and int(pair["reviewed_criterion_snapshot_id"]) != int(baseline_row["criterion_snapshot_id"])
                )
                if note_mismatch or criterion_mismatch:
                    dest.execute(
                        """
                        UPDATE review_jobs
                        SET status = 'failed',
                            completed_at = created_at,
                            failure_reason = 'stale-queued-capture'
                        WHERE review_job_id = ?
                          AND status = 'queued'
                        """,
                        (pair["review_job_id"],),
                    )
                    failed_job_ids.add(int(pair["review_job_id"]))

            from commonplace.store import assert_store_integrity

            assert_store_integrity(dest)
            _compare_projections(source, dest, migrated_keys=migrated_keys)

            dest_counts = {
                "artifact_snapshots": _count(dest, "artifact_snapshots"),
                "freshness_baselines": _count(dest, "freshness_baselines"),
                "freshness_inputs": _count(dest, "freshness_inputs"),
                "review_freshness_evidence": _count(dest, "review_freshness_evidence"),
                "review_jobs": _count(dest, "review_jobs"),
                "review_pairs": _count(dest, "review_pairs"),
            }
            if dest_counts["artifact_snapshots"] != source_counts["review_file_snapshots"]:
                raise RuntimeError("snapshot count mismatch after migration")
            if dest_counts["review_jobs"] != source_counts["review_jobs"]:
                raise RuntimeError("review job count mismatch after migration")
            if dest_counts["review_pairs"] != source_counts["review_pairs"]:
                raise RuntimeError("review pair count mismatch after migration")
            if dest_counts["freshness_inputs"] != dest_counts["freshness_baselines"] * 2:
                raise RuntimeError("freshness input count mismatch after migration")
            dest.commit()

    tmp_path.replace(destination_path)
    source_hash_after = _file_hash(source_path)
    if source_hash_before != source_hash_after:
        destination_path.unlink(missing_ok=True)
        raise RuntimeError("source backup hash changed during migration; destination removed")

    return {
        "snapshots": dest_counts["artifact_snapshots"],
        "baselines": dest_counts["freshness_baselines"],
        "inputs": dest_counts["freshness_inputs"],
        "skipped_baselines": skipped_baselines,
        "failed_queued_jobs": len(failed_job_ids),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root for on-disk path checks (default: cwd).",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("kb/reports") / LEGACY_DB_PATH.name,
        help=f"Read-only review-store path (default: kb/reports/{LEGACY_DB_PATH.name}).",
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path("kb/reports") / DEFAULT_DB_PATH.name,
        help=f"Destination commonplace store path (default: kb/reports/{DEFAULT_DB_PATH.name}).",
    )
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()
    source_path = args.source if args.source.is_absolute() else (repo_root / args.source).resolve()
    destination_path = (
        args.destination if args.destination.is_absolute() else (repo_root / args.destination).resolve()
    )
    try:
        counts = migrate(repo_root=repo_root, source_path=source_path, destination_path=destination_path)
    except (OSError, sqlite3.Error, RuntimeError) as exc:
        parser.error(str(exc))
    print(
        "migrated "
        f"{source_path} -> {destination_path}: "
        f"{counts['baselines']} baselines, "
        f"{counts['inputs']} inputs, "
        f"{counts['skipped_baselines']} skipped, "
        f"{counts['failed_queued_jobs']} failed queued jobs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())