#!/usr/bin/env python3
"""Move parseable gate-review result lines to the canonical footer position."""

from __future__ import annotations

import argparse
from pathlib import Path

from review_db import (
    connect,
    ensure_db,
    infer_manual_import_review_decision,
    resolve_db_path,
    rewrite_review_result_footer,
)
from run_review_bundle import bundle_artifact_dir, encode_stage_filename, rewrite_bundle_result_footers


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rewrite stored gate reviews so the parseable result line appears at the end."
    )
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing them.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

    gate_reviews_scanned = 0
    gate_reviews_updated = 0
    gate_review_decisions_updated = 0
    review_runs_scanned = 0
    review_runs_updated = 0
    bundle_artifacts_updated = 0
    stage_artifacts_updated = 0
    rewritten_reviews_by_run: dict[int, dict[str, str]] = {}

    with connect(db_path) as conn:
        gate_rows = conn.execute(
            """
            SELECT id, review_run_id, gate_id, decision, rationale_markdown, review_kind
            FROM gate_reviews
            ORDER BY id
            """
        ).fetchall()

        for row in gate_rows:
            gate_reviews_scanned += 1
            decision = row["decision"]
            if row["review_kind"] == "manual-import":
                decision = infer_manual_import_review_decision(row["rationale_markdown"])
            rewritten = rewrite_review_result_footer(
                row["rationale_markdown"],
                decision=decision,
            )
            review_run_id = row["review_run_id"]
            if review_run_id is not None:
                rewritten_reviews_by_run.setdefault(int(review_run_id), {})[str(row["gate_id"])] = rewritten
            if rewritten == row["rationale_markdown"] and decision == row["decision"]:
                continue
            gate_reviews_updated += 1
            if decision != row["decision"]:
                gate_review_decisions_updated += 1
            if args.dry_run:
                continue
            conn.execute(
                """
                UPDATE gate_reviews
                SET decision = ?, rationale_markdown = ?
                WHERE id = ?
                """,
                (decision, rewritten, row["id"]),
            )

        run_rows = conn.execute(
            """
            SELECT id, raw_bundle_markdown
            FROM review_runs
            WHERE raw_bundle_markdown IS NOT NULL AND raw_bundle_markdown != ''
            ORDER BY id
            """
        ).fetchall()

        for row in run_rows:
            review_runs_scanned += 1
            review_run_id = int(row["id"])
            rewritten_reviews = rewritten_reviews_by_run.get(review_run_id)
            if not rewritten_reviews:
                continue
            rewritten_bundle = rewrite_bundle_result_footers(
                row["raw_bundle_markdown"],
                parsed_reviews=rewritten_reviews,
            )
            if rewritten_bundle == row["raw_bundle_markdown"]:
                continue
            review_runs_updated += 1
            if args.dry_run:
                continue
            conn.execute(
                """
                UPDATE review_runs
                SET raw_bundle_markdown = ?
                WHERE id = ?
                """,
                (rewritten_bundle, review_run_id),
            )

        if not args.dry_run:
            conn.commit()

    if not args.dry_run:
        for review_run_id, rewritten_reviews in rewritten_reviews_by_run.items():
            artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
            if not artifact_dir.is_dir():
                continue

            bundle_path = artifact_dir / "bundle-output.md"
            if bundle_path.is_file():
                existing_bundle = bundle_path.read_text(encoding="utf-8")
                rewritten_bundle = rewrite_bundle_result_footers(
                    existing_bundle,
                    parsed_reviews=rewritten_reviews,
                )
                if rewritten_bundle != existing_bundle:
                    bundle_path.write_text(rewritten_bundle, encoding="utf-8")
                    bundle_artifacts_updated += 1

            for gate_id, rewritten_review in rewritten_reviews.items():
                stage_path = artifact_dir / encode_stage_filename(gate_id)
                if not stage_path.is_file():
                    continue
                existing_review = stage_path.read_text(encoding="utf-8")
                if existing_review == rewritten_review:
                    continue
                stage_path.write_text(rewritten_review, encoding="utf-8")
                stage_artifacts_updated += 1

    print(f"gate_reviews_scanned: {gate_reviews_scanned}")
    print(f"gate_reviews_updated: {gate_reviews_updated}")
    print(f"gate_review_decisions_updated: {gate_review_decisions_updated}")
    print(f"review_runs_scanned: {review_runs_scanned}")
    print(f"review_runs_updated: {review_runs_updated}")
    print(f"bundle_artifacts_updated: {bundle_artifacts_updated}")
    print(f"stage_artifacts_updated: {stage_artifacts_updated}")
    print(f"mode: {'dry-run' if args.dry_run else 'write'}")


if __name__ == "__main__":
    main()
