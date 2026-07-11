#!/usr/bin/env python3
"""Show current WARN/FAIL/ERROR review findings for a note.

This is a temporary fixing aid around the review-store database.

Usage:
    python3 scripts/review-problems-for-note.py kb/agent-memory-systems/reviews/xMemory.md
    python3 scripts/review-problems-for-note.py --json kb/agent-memory-systems/reviews/xMemory.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path

from commonplace.review.review_db import ensure_db


PROBLEM_DECISIONS = {"warn", "fail", "error"}

SECTION_END_LOOKAHEAD = (
    r"(?=^###\s|"
    r"^##\s*(?:Result|Verdict|Outcome)\b|"
    r"^##\s+(?:pass|warn|fail|error|unknown|info|ok)\s*$|"
    r"^Verdict:|"
    r"^(?:[-*]\s*)?Outcome:|"
    r"\Z)"
)
SUMMARY_SECTION_RE = re.compile(
    rf"^###\s*Summary\s*$\s*(?P<body>.*?){SECTION_END_LOOKAHEAD}",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
FINDINGS_SECTION_RE = re.compile(
    rf"^###\s*Findings\s*$\s*(?P<body>.*?){SECTION_END_LOOKAHEAD}",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
SUGGESTED_REVISION_RE = re.compile(
    rf"^###\s*Suggested Revision\s*$\s*(?P<body>.*?){SECTION_END_LOOKAHEAD}",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
PROBLEM_FINDING_RE = re.compile(
    r"^\s*[-*]\s*(?P<severity>warn|fail|error)\s*:\s*(?P<body>.+?)"
    r"(?=^\s*[-*]\s*(?:pass|info|warn|fail|error|unknown)\s*:|^###\s|\Z)",
    re.IGNORECASE | re.MULTILINE | re.DOTALL,
)
RESULT_LINE_RE = re.compile(
    r"^\s*(?:##\s*)?(?:Result|Verdict|Outcome)\s*:\s*(?:PASS|WARN|FAIL|ERROR|UNKNOWN)\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def resolve_db_path(repo_root: Path, db_arg: str | None) -> Path:
    if db_arg:
        db_path = Path(db_arg)
    else:
        db_path = Path(os.environ.get("COMMONPLACE_REVIEW_DB", "kb/reports/review-store.sqlite"))
    if not db_path.is_absolute():
        db_path = repo_root / db_path
    return db_path


def normalize_note_path(repo_root: Path, raw_path: str) -> str:
    path = Path(raw_path)
    if path.is_absolute():
        try:
            return path.resolve().relative_to(repo_root).as_posix()
        except ValueError:
            return path.as_posix()
    return path.as_posix()


def extract_section(text: str, pattern: re.Pattern[str]) -> str | None:
    match = pattern.search(text)
    if match is None:
        return None
    body = match.group("body").strip()
    return body or None


def strip_result_lines(text: str) -> str:
    return RESULT_LINE_RE.sub("", text).strip()


def extract_problem_findings(review_text: str, decision: str) -> list[str]:
    findings = extract_section(review_text, FINDINGS_SECTION_RE)
    if findings:
        problem_findings = [
            f"{match.group('severity').upper()}: {match.group('body').strip()}"
            for match in PROBLEM_FINDING_RE.finditer(findings)
        ]
        if problem_findings:
            return problem_findings
        return [findings]

    summary = extract_section(review_text, SUMMARY_SECTION_RE)
    if summary:
        return [summary]

    if decision in PROBLEM_DECISIONS:
        body = strip_result_lines(review_text)
        if body:
            return [body]
    return []


def load_effective_problem_reviews(
    repo_root: Path,
    conn: sqlite3.Connection,
    *,
    note_paths: list[str],
    model_partition: str | None,
) -> list[dict[str, object]]:
    params: list[str] = []
    where: list[str] = []

    if note_paths:
        placeholders = ", ".join("?" for _ in note_paths)
        where.append(f"a.note_path IN ({placeholders})")
        params.extend(note_paths)
    if model_partition:
        where.append("a.model_partition = ?")
        params.append(model_partition)
    where.append("COALESCE(accepted.decision, latest.decision) IN ('warn', 'fail', 'error')")

    rows = conn.execute(
        f"""
        WITH latest_review_pairs AS (
            SELECT
                rp.*,
                ROW_NUMBER() OVER (
                    PARTITION BY rp.note_path, rp.criterion_path, rp.model_partition
                    ORDER BY rp.reviewed_at DESC, rp.review_pair_id DESC
                ) AS rn
            FROM review_pairs AS rp
            WHERE rp.pair_status = 'completed'
        )
        SELECT
            COALESCE(accepted.review_pair_id, latest.review_pair_id) AS review_pair_id,
            COALESCE(accepted.review_job_id, latest.review_job_id) AS review_job_id,
            COALESCE(accepted.note_path, latest.note_path) AS note_path,
            COALESCE(accepted.criterion_path, latest.criterion_path) AS criterion_path,
            COALESCE(accepted.model_partition, latest.model_partition) AS model_partition,
            COALESCE(accepted.decision, latest.decision) AS decision,
            COALESCE(accepted.result_path, latest.result_path) AS result_path,
            COALESCE(accepted.reviewed_at, latest.reviewed_at) AS reviewed_at
        FROM current_criterion_acceptances AS a
        LEFT JOIN review_pairs AS accepted
          ON accepted.review_pair_id = a.accepted_review_pair_id
        LEFT JOIN latest_review_pairs AS latest
          ON latest.note_path = a.note_path
         AND latest.criterion_path = a.criterion_path
         AND latest.model_partition = a.model_partition
         AND latest.rn = 1
        WHERE {" AND ".join(where)}
        ORDER BY note_path, criterion_path, model_partition
        """,
        params,
    ).fetchall()

    reviews: list[dict[str, object]] = []
    for row in rows:
        if row["review_pair_id"] is None:
            continue
        result_path = row["result_path"]
        if not result_path:
            continue
        try:
            review_text = (repo_root / result_path).read_text(encoding="utf-8")
        except OSError:
            continue
        reviews.append(
            {
                "note_path": row["note_path"],
                "criterion_path": row["criterion_path"],
                "decision": row["decision"],
                "model_partition": row["model_partition"],
                "review_pair_id": row["review_pair_id"],
                "review_job_id": row["review_job_id"],
                "result_path": result_path,
                "reviewed_at": row["reviewed_at"],
                "findings": extract_problem_findings(review_text, row["decision"]),
                "suggested_revision": extract_section(review_text, SUGGESTED_REVISION_RE),
                "review_text": review_text,
            }
        )
    return reviews


def render_grouped(reviews: list[dict[str, object]], *, include_full: bool) -> str:
    if not reviews:
        return "No WARN/FAIL/ERROR reviews found."

    lines: list[str] = []
    current_note: str | None = None
    for review in reviews:
        note_path = str(review["note_path"])
        if note_path != current_note:
            if lines:
                lines.append("")
            lines.append(note_path)
            current_note = note_path

        lines.append(
            f"- {review['criterion_path']} [{str(review['decision']).upper()}] "
            f"model={review['model_partition']} job={review['review_job_id']} pair={review['review_pair_id']}"
        )
        findings = review["findings"]
        if isinstance(findings, list) and findings:
            for finding in findings:
                lines.append(f"  Finding: {str(finding).replace(chr(10), chr(10) + '  ')}")
        suggested = review.get("suggested_revision")
        if suggested:
            lines.append(f"  Suggested revision: {str(suggested).replace(chr(10), chr(10) + '  ')}")
        if include_full:
            review_text = str(review["review_text"]).replace("\n", "\n  ")
            lines.append(f"  Review text:\n  {review_text}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show current WARN/FAIL/ERROR review findings for note(s).")
    parser.add_argument("note_paths", nargs="+", help="Note path(s), relative to the repository root.")
    parser.add_argument("--db", help="Review DB path. Defaults to COMMONPLACE_REVIEW_DB or kb/reports/review-store.sqlite.")
    parser.add_argument("--model", help="Optional model partition filter, e.g. gpt-5-4-high.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument("--full", action="store_true", help="Include full review text in grouped output.")
    args = parser.parse_args()

    repo_root = Path.cwd().resolve()
    db_path = resolve_db_path(repo_root, args.db)
    if not db_path.exists():
        print(f"Review DB not found: {db_path}", file=sys.stderr)
        return 1
    ensure_db(db_path)

    note_paths = [normalize_note_path(repo_root, raw) for raw in args.note_paths]
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        reviews = load_effective_problem_reviews(
            repo_root,
            conn,
            note_paths=note_paths,
            model_partition=args.model,
        )

    if args.json:
        print(json.dumps(reviews, indent=2))
    else:
        print(render_grouped(reviews, include_full=args.full))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
