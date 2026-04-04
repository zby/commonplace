#!/usr/bin/env python3
"""Repair Codex review model partitions from persisted session logs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from review_db import connect, ensure_db, resolve_db_path
from review_model import build_model_id
from review_runners import load_codex_session_log_telemetry


REVIEW_RUN_ID_RE = re.compile(r"\bReview run id:\s*(\d+)\b")


def extract_review_run_id_from_session_log(session_log: Path) -> int | None:
    try:
        with session_log.open(encoding="utf-8") as handle:
            for line in handle:
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    event = None
                if isinstance(event, dict):
                    payload = event.get("payload")
                    if isinstance(payload, dict):
                        content = payload.get("content")
                        if isinstance(content, list):
                            for item in content:
                                if not isinstance(item, dict):
                                    continue
                                text = item.get("text")
                                if not isinstance(text, str):
                                    continue
                                match = REVIEW_RUN_ID_RE.search(text)
                                if match is not None:
                                    return int(match.group(1))
                match = REVIEW_RUN_ID_RE.search(line)
                if match is not None:
                    return int(match.group(1))
    except OSError:
        return None
    return None


def index_codex_session_logs(*, target_run_ids: set[int] | None = None) -> dict[int, Path]:
    sessions_root = Path.home() / ".codex" / "sessions"
    if not sessions_root.is_dir():
        return {}

    indexed: dict[int, Path] = {}
    for session_log in sessions_root.rglob("rollout-*.jsonl"):
        review_run_id = extract_review_run_id_from_session_log(session_log)
        if review_run_id is None:
            continue
        if target_run_ids is not None and review_run_id not in target_run_ids:
            continue
        indexed.setdefault(review_run_id, session_log)
    return indexed


def merge_telemetry(existing_json: str | None, refreshed: dict[str, object]) -> str:
    merged: dict[str, object] = {}
    if existing_json:
        try:
            existing = json.loads(existing_json)
        except json.JSONDecodeError:
            existing = None
        if isinstance(existing, dict):
            merged.update(existing)
    for key, value in refreshed.items():
        if value is not None:
            merged[key] = value
    return json.dumps(merged, ensure_ascii=True, sort_keys=True)


def model_id_from_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if not isinstance(telemetry, dict):
        return None
    model = telemetry.get("model")
    if not isinstance(model, str) or not model.strip():
        return None
    effort = telemetry.get("reasoning_effort")
    if effort is not None and not isinstance(effort, str):
        effort = None
    return build_model_id(model, effort)


def session_path_from_existing_telemetry(telemetry_json: str | None) -> Path | None:
    if not telemetry_json:
        return None
    try:
        payload = json.loads(telemetry_json)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict):
        return None
    session_path = payload.get("session_path")
    if not isinstance(session_path, str) or not session_path.strip():
        return None
    return Path(session_path)


def update_review_run_partition(
    conn,
    *,
    review_run_id: int,
    old_model_id: str,
    new_model_id: str,
    telemetry_json: str,
) -> tuple[int, int]:
    conn.execute(
        """
        UPDATE review_runs
        SET model_id = ?,
            telemetry_json = ?
        WHERE id = ?
        """,
        (new_model_id, telemetry_json, review_run_id),
    )

    gate_review_ids = [
        row[0]
        for row in conn.execute(
            "SELECT id FROM gate_reviews WHERE review_run_id = ? ORDER BY id",
            (review_run_id,),
        ).fetchall()
    ]

    conn.execute(
        """
        UPDATE gate_reviews
        SET model_id = ?
        WHERE review_run_id = ?
        """,
        (new_model_id, review_run_id),
    )

    acceptance_events_updated = 0
    if gate_review_ids:
        placeholders = ", ".join("?" for _ in gate_review_ids)
        params: list[object] = [new_model_id, *gate_review_ids]
        cursor = conn.execute(
            f"""
            UPDATE acceptance_events
            SET model_id = ?
            WHERE accepted_review_id IN ({placeholders})
            """,
            params,
        )
        acceptance_events_updated = cursor.rowcount

    gate_reviews_updated = conn.execute(
        "SELECT COUNT(*) FROM gate_reviews WHERE review_run_id = ? AND model_id = ?",
        (review_run_id, new_model_id),
    ).fetchone()[0]
    return gate_reviews_updated, acceptance_events_updated


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Repair Codex review model partitions using saved Codex session logs."
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument(
        "--review-run-id",
        type=int,
        action="append",
        dest="review_run_ids",
        help="Restrict to one or more review runs.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing them.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    params: list[object] = []
    where_sql = "WHERE runner = 'codex'"
    if args.review_run_ids:
        placeholders = ", ".join("?" for _ in args.review_run_ids)
        where_sql += f" AND id IN ({placeholders})"
        params.extend(args.review_run_ids)

    with connect(db_path) as conn:
        runs = conn.execute(
            f"""
            SELECT id, model_id, telemetry_json
            FROM review_runs
            {where_sql}
            ORDER BY id
            """,
            params,
        ).fetchall()

        target_run_ids = {int(row["id"]) for row in runs}
        indexed_session_logs = index_codex_session_logs(target_run_ids=target_run_ids)

        session_matched = 0
        missing_session_log = 0
        telemetry_updated = 0
        model_rekeyed = 0
        unresolved = 0

        for row in runs:
            review_run_id = int(row["id"])
            old_model_id = str(row["model_id"])
            existing_telemetry_json = row["telemetry_json"]

            session_path = session_path_from_existing_telemetry(existing_telemetry_json)
            if session_path is None or not session_path.is_file():
                session_path = indexed_session_logs.get(review_run_id)
            if session_path is None or not session_path.is_file():
                missing_session_log += 1
                continue

            telemetry = load_codex_session_log_telemetry(session_path)
            if telemetry is None:
                unresolved += 1
                continue

            session_matched += 1
            new_model_id = model_id_from_telemetry(telemetry)
            merged_telemetry_json = merge_telemetry(existing_telemetry_json, telemetry)
            telemetry_changed = merged_telemetry_json != (existing_telemetry_json or "")
            model_changed = new_model_id is not None and new_model_id != old_model_id

            if not telemetry_changed and not model_changed:
                continue

            if telemetry_changed:
                telemetry_updated += 1
            if model_changed:
                model_rekeyed += 1

            if args.dry_run:
                continue

            if model_changed and new_model_id is not None:
                update_review_run_partition(
                    conn,
                    review_run_id=review_run_id,
                    old_model_id=old_model_id,
                    new_model_id=new_model_id,
                    telemetry_json=merged_telemetry_json,
                )
                continue

            conn.execute(
                """
                UPDATE review_runs
                SET telemetry_json = ?
                WHERE id = ?
                """,
                (merged_telemetry_json, review_run_id),
            )

        if not args.dry_run:
            conn.commit()

    print(f"scanned: {len(runs)}")
    print(f"session_matched: {session_matched}")
    print(f"missing_session_log: {missing_session_log}")
    print(f"unresolved: {unresolved}")
    print(f"telemetry_updated: {telemetry_updated}")
    print(f"model_rekeyed: {model_rekeyed}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")


if __name__ == "__main__":
    main()
