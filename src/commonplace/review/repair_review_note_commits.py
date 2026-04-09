#!/usr/bin/env python3
"""Backfill missing committed note versions for review records."""

from __future__ import annotations

import argparse
import subprocess
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.review_db import connect, ensure_db, resolve_db_path
from commonplace.review.review_metadata import blob_sha_at_commit


@dataclass(frozen=True)
class CandidateCommit:
    commit: str | None
    relation: str


def _git(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )


def commit_before(repo_root: Path, *, note_path: str, at: str) -> str | None:
    result = _git(repo_root, ["log", "-1", f"--before={at}", "--format=%H", "--", note_path])
    commit = result.stdout.strip()
    return commit or None


def commit_after(repo_root: Path, *, note_path: str, at: str) -> str | None:
    result = _git(repo_root, ["log", "--reverse", f"--after={at}", "--format=%H", "--", note_path])
    for line in result.stdout.splitlines():
        commit = line.strip()
        if commit:
            return commit
    return None


def infer_matching_commit(
    repo_root: Path,
    *,
    note_path: str,
    note_sha: str,
    at: str,
    surrounding_cache: dict[tuple[str, str], tuple[str | None, str | None]],
    blob_cache: dict[tuple[str, str], str | None],
) -> CandidateCommit:
    cache_key = (note_path, at)
    if cache_key not in surrounding_cache:
        surrounding_cache[cache_key] = (
            commit_before(repo_root, note_path=note_path, at=at),
            commit_after(repo_root, note_path=note_path, at=at),
        )
    before_commit, after_commit = surrounding_cache[cache_key]

    for relation, commit in (("before", before_commit), ("after", after_commit)):
        if not commit:
            continue
        blob_key = (note_path, commit)
        if blob_key not in blob_cache:
            blob_cache[blob_key] = blob_sha_at_commit(repo_root, commit, Path(note_path))
        if blob_cache[blob_key] == note_sha:
            return CandidateCommit(commit=commit, relation=relation)

    return CandidateCommit(commit=None, relation="unresolved")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Backfill missing note commit provenance for review_runs, gate_reviews, "
            "and acceptance_events by matching the stored note SHA against the "
            "nearest committed versions before and after the review timestamp."
        )
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing them.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    surrounding_cache: dict[tuple[str, str], tuple[str | None, str | None]] = {}
    blob_cache: dict[tuple[str, str], str | None] = {}

    review_runs_scanned = 0
    review_runs_updated = 0
    gate_reviews_scanned = 0
    gate_reviews_updated = 0
    acceptance_events_scanned = 0
    acceptance_events_updated = 0
    matched_before = 0
    matched_after = 0
    unresolved = 0

    with connect(db_path) as conn:
        run_rows = conn.execute(
            """
            SELECT id, note_path, reviewed_note_sha, reviewed_note_commit, started_at
            FROM review_runs
            WHERE reviewed_note_commit IS NULL
            ORDER BY id
            """
        ).fetchall()
        for row in run_rows:
            review_runs_scanned += 1
            candidate = infer_matching_commit(
                repo_root,
                note_path=row["note_path"],
                note_sha=row["reviewed_note_sha"],
                at=row["started_at"],
                surrounding_cache=surrounding_cache,
                blob_cache=blob_cache,
            )
            if candidate.commit is None:
                unresolved += 1
                continue
            if candidate.relation == "before":
                matched_before += 1
            else:
                matched_after += 1
            review_runs_updated += 1
            if args.dry_run:
                continue
            conn.execute(
                """
                UPDATE review_runs
                SET reviewed_note_commit = ?
                WHERE id = ?
                """,
                (candidate.commit, row["id"]),
            )

        gate_rows = conn.execute(
            """
            SELECT id, note_path, reviewed_note_sha, reviewed_note_commit, reviewed_at
            FROM gate_reviews
            WHERE reviewed_note_commit IS NULL
            ORDER BY id
            """
        ).fetchall()
        for row in gate_rows:
            gate_reviews_scanned += 1
            candidate = infer_matching_commit(
                repo_root,
                note_path=row["note_path"],
                note_sha=row["reviewed_note_sha"],
                at=row["reviewed_at"],
                surrounding_cache=surrounding_cache,
                blob_cache=blob_cache,
            )
            if candidate.commit is None:
                unresolved += 1
                continue
            if candidate.relation == "before":
                matched_before += 1
            else:
                matched_after += 1
            gate_reviews_updated += 1
            if args.dry_run:
                continue
            conn.execute(
                """
                UPDATE gate_reviews
                SET reviewed_note_commit = ?
                WHERE id = ?
                """,
                (candidate.commit, row["id"]),
            )

        acceptance_rows = conn.execute(
            """
            SELECT id, note_path, accepted_note_sha, accepted_note_commit, accepted_at
            FROM acceptance_events
            WHERE accepted_note_commit IS NULL
            ORDER BY id
            """
        ).fetchall()
        for row in acceptance_rows:
            acceptance_events_scanned += 1
            candidate = infer_matching_commit(
                repo_root,
                note_path=row["note_path"],
                note_sha=row["accepted_note_sha"],
                at=row["accepted_at"],
                surrounding_cache=surrounding_cache,
                blob_cache=blob_cache,
            )
            if candidate.commit is None:
                unresolved += 1
                continue
            if candidate.relation == "before":
                matched_before += 1
            else:
                matched_after += 1
            acceptance_events_updated += 1
            if args.dry_run:
                continue
            conn.execute(
                """
                UPDATE acceptance_events
                SET accepted_note_commit = ?
                WHERE id = ?
                """,
                (candidate.commit, row["id"]),
            )

        if not args.dry_run:
            conn.commit()

    print(f"review_runs_scanned: {review_runs_scanned}")
    print(f"review_runs_updated: {review_runs_updated}")
    print(f"gate_reviews_scanned: {gate_reviews_scanned}")
    print(f"gate_reviews_updated: {gate_reviews_updated}")
    print(f"acceptance_events_scanned: {acceptance_events_scanned}")
    print(f"acceptance_events_updated: {acceptance_events_updated}")
    print(f"matched_before: {matched_before}")
    print(f"matched_after: {matched_after}")
    print(f"unresolved: {unresolved}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")


if __name__ == "__main__":
    main()
