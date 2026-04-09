#!/usr/bin/env python3
"""Run one gate across multiple notes in batched runner calls."""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.gate_sweep_format import (
    GateSweepNoteTarget,
    build_gate_sweep_prompt,
    extract_gate_sweep_reviews,
)
from commonplace.review.review_db import (
    GATES_ROOT,
    connect,
    ensure_db,
    fail_review_run,
    insert_review_run,
    insert_review_run_gates,
    resolve_db_path,
)
from commonplace.review.review_metadata import committed_file_provenance, iso_now, review_note_provenance
from commonplace.review.review_runners import run_prompt
from commonplace.review.review_target_selector import select_stale_gates
from commonplace.review.resolve_gates import strip_frontmatter
from commonplace.review.run_review_bundle import (
    BundleReviewRecordError,
    bundle_artifact_dir,
    combine_logs,
    model_id_from_telemetry,
    record_bundle_review_run,
    resolve_note_markdown_links,
    serialize_telemetry,
    update_review_run_model_id,
)


DB_ENV_VAR = "COMMONPLACE_REVIEW_DB"


@dataclass(frozen=True)
class PreparedReviewRun:
    note_path: str
    review_run_id: int
    note_text: str
    resolved_links: list[tuple[str, str, str]]
    unresolved_links: list[tuple[str, str]]


def chunked(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def build_note_local_bundle(
    *,
    note_path: str,
    gate_id: str,
    review_run_id: int,
    review_text: str,
) -> str:
    review_body = review_text.rstrip("\n")
    return "\n".join(
        [
            "# Review Bundle",
            "",
            f"Review run id: {review_run_id}",
            f"Target: {note_path}",
            "",
            f"=== GATE REVIEW START: {gate_id} ===",
            review_body,
            f"=== GATE REVIEW END: {gate_id} ===",
            "",
        ]
    )


def prepare_gate_sweep_targets(
    *,
    repo_root: Path,
    db_path: Path,
    note_paths: list[str],
    gate_id: str,
    gate_sha: str,
    runner: str,
    model_id: str,
    persist_runs: bool,
) -> list[PreparedReviewRun]:
    prepared: list[PreparedReviewRun] = []
    started_at = iso_now()

    if not persist_runs:
        for ordinal, note_path in enumerate(note_paths, start=1):
            note_abs = repo_root / note_path
            note_text = note_abs.read_text(encoding="utf-8")
            note_body = strip_frontmatter(note_text)
            resolved_links, unresolved_links = resolve_note_markdown_links(
                repo_root=repo_root,
                note_abs=note_abs,
                note_body=note_body,
            )
            prepared.append(
                PreparedReviewRun(
                    note_path=note_path,
                    review_run_id=ordinal,
                    note_text=note_text,
                    resolved_links=resolved_links,
                    unresolved_links=unresolved_links,
                )
            )
        return prepared

    with connect(db_path) as conn:
        for note_path in note_paths:
            note_abs = repo_root / note_path
            note_text = note_abs.read_text(encoding="utf-8")
            note_body = strip_frontmatter(note_text)
            resolved_links, unresolved_links = resolve_note_markdown_links(
                repo_root=repo_root,
                note_abs=note_abs,
                note_body=note_body,
            )
            note_sha, note_commit = review_note_provenance(repo_root, Path(note_path))
            review_run_id = insert_review_run(
                conn,
                note_path=note_path,
                model_id=model_id,
                runner=runner,
                reviewed_note_sha=note_sha,
                reviewed_note_commit=note_commit,
                started_at=started_at,
                status="running",
            )
            insert_review_run_gates(
                conn,
                review_run_id=review_run_id,
                gates=[(gate_id, gate_sha, 0)],
            )
            bundle_artifact_dir(repo_root, review_run_id).mkdir(parents=True, exist_ok=True)
            prepared.append(
                PreparedReviewRun(
                    note_path=note_path,
                    review_run_id=review_run_id,
                    note_text=note_text,
                    resolved_links=resolved_links,
                    unresolved_links=unresolved_links,
                )
            )
        conn.commit()
    return prepared


def fail_running_review_runs(
    *,
    db_path: Path,
    review_run_ids: list[int],
    failure_reason: str,
    debug_log: str | None = None,
    telemetry_json: str | None = None,
) -> None:
    if not review_run_ids:
        return
    completed_at = iso_now()
    with connect(db_path) as conn:
        rows = conn.execute(
            f"""
            SELECT id, status
            FROM review_runs
            WHERE id IN ({", ".join("?" for _ in review_run_ids)})
            """,
            review_run_ids,
        ).fetchall()
        for row in rows:
            if row["status"] != "running":
                continue
            fail_review_run(
                conn,
                review_run_id=int(row["id"]),
                failure_reason=failure_reason,
                completed_at=completed_at,
                debug_log=debug_log,
                telemetry_json=telemetry_json,
            )
        conn.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one gate across many notes using batched prompts.")
    parser.add_argument("gate_id", help="Single gate id, e.g. accessibility/undefined-terms.")
    parser.add_argument("--runner", required=True, choices=["claude-code", "codex"])
    parser.add_argument("--model", required=True, help="Requested runner model and initial review model partition.")
    parser.add_argument("--current", action="store_true", help="Limit to notes whose frontmatter status is current.")
    parser.add_argument("--note", nargs="+", dest="note_paths", help="Filter to specific note paths.")
    parser.add_argument("--batch-size", type=int, default=5, help="Notes per runner invocation.")
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--dry-run", action="store_true", help="Print prompts without invoking the runner.")
    args = parser.parse_args()

    if args.batch_size < 1:
        parser.error("--batch-size must be a positive integer")
    if args.current and args.note_paths:
        parser.error("--current and --note are mutually exclusive")

    repo_root = Path.cwd()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    if args.db:
        os.environ[DB_ENV_VAR] = str(db_path)
    ensure_db(repo_root, db_path)

    gate_id = args.gate_id.removesuffix(".md")
    gate_abs = repo_root / GATES_ROOT / f"{gate_id}.md"
    if not gate_abs.is_file():
        parser.error(f"gate not found: {gate_id}")
    gate_text = strip_frontmatter(gate_abs.read_text(encoding="utf-8"))
    try:
        gate_sha, _ = committed_file_provenance(repo_root, gate_abs, kind="gate")
    except ValueError as exc:
        parser.error(str(exc))

    try:
        stale_records = select_stale_gates(
            repo_root,
            model=args.model,
            gate_ids=[gate_id],
            note_filter=args.note_paths,
            current_only=args.current,
            include_diff=False,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))

    note_paths = [record.note_path for record in stale_records]
    if not note_paths:
        print("Reviewed: 0 notes")
        return

    batches = chunked(note_paths, args.batch_size)
    reviewed = 0

    print(f"Selected: {len(note_paths)} notes across {len(batches)} batches", file=sys.stderr)

    for batch_index, batch_note_paths in enumerate(batches, start=1):
        try:
            prepared = prepare_gate_sweep_targets(
                repo_root=repo_root,
                db_path=db_path,
                note_paths=batch_note_paths,
                gate_id=gate_id,
                gate_sha=gate_sha,
                runner=args.runner,
                model_id=args.model,
                persist_runs=not args.dry_run,
            )
        except ValueError as exc:
            parser.error(str(exc))
        prompt = build_gate_sweep_prompt(
            gate_id=gate_id,
            gate_text=gate_text,
            gate_path=str((GATES_ROOT / f"{gate_id}.md").as_posix()),
            notes=[
                GateSweepNoteTarget(
                    note_path=item.note_path,
                    review_run_id=item.review_run_id,
                    note_text=item.note_text,
                    resolved_links=item.resolved_links,
                    unresolved_links=item.unresolved_links,
                )
                for item in prepared
            ],
        )
        batch_label = f"Batch {batch_index}/{len(batches)}"
        print(
            f"{batch_label}: launching {args.runner} for {len(prepared)} notes",
            file=sys.stderr,
        )
        for item in prepared:
            print(f"  - {item.note_path} (review run id: {item.review_run_id})", file=sys.stderr)

        if args.dry_run:
            if batch_index > 1:
                print()
                print(f"=== BATCH {batch_index}/{len(batches)} ===")
            print(prompt)
            continue

        review_run_ids = [item.review_run_id for item in prepared]
        try:
            result = run_prompt(runner=args.runner, prompt=prompt, repo_root=repo_root, model=args.model)
        except KeyboardInterrupt:
            fail_running_review_runs(
                db_path=db_path,
                review_run_ids=review_run_ids,
                failure_reason="gate sweep interrupted",
            )
            parser.exit(130, "gate sweep interrupted\n")

        telemetry_json = serialize_telemetry(result.telemetry)
        runner_debug_log = combine_logs(result.stdout, result.stderr)
        actual_review_model = model_id_from_telemetry(result.telemetry)

        if actual_review_model is not None and actual_review_model != args.model:
            with connect(db_path) as conn:
                for review_run_id in review_run_ids:
                    update_review_run_model_id(
                        conn,
                        review_run_id=review_run_id,
                        model_id=actual_review_model,
                    )
                conn.commit()
            print(
                (
                    f"warning: requested model partition {args.model} "
                    f"does not match runner telemetry {actual_review_model}; "
                    "recording the actual partition"
                ),
                file=sys.stderr,
            )

        if result.returncode != 0:
            fail_running_review_runs(
                db_path=db_path,
                review_run_ids=review_run_ids,
                failure_reason=f"{args.runner} exited {result.returncode}",
                debug_log=runner_debug_log,
                telemetry_json=telemetry_json,
            )
            raise SystemExit(result.returncode)

        try:
            parsed_reviews = extract_gate_sweep_reviews(
                result.stdout,
                gate_id=gate_id,
                expected_note_paths=batch_note_paths,
            )
        except ValueError as exc:
            fail_running_review_runs(
                db_path=db_path,
                review_run_ids=review_run_ids,
                failure_reason=str(exc),
                debug_log=runner_debug_log,
                telemetry_json=telemetry_json,
            )
            parser.exit(1, f"{exc}\n")

        completed_in_batch = 0
        for index, item in enumerate(prepared):
            note_bundle = build_note_local_bundle(
                note_path=item.note_path,
                gate_id=gate_id,
                review_run_id=item.review_run_id,
                review_text=parsed_reviews[item.note_path],
            )
            try:
                record_bundle_review_run(
                    repo_root=repo_root,
                    db_path=db_path,
                    review_run_id=item.review_run_id,
                    raw_bundle_markdown=note_bundle,
                    telemetry_json=telemetry_json,
                    debug_log=runner_debug_log,
                )
            except BundleReviewRecordError as exc:
                remaining_ids = [remaining.review_run_id for remaining in prepared[index + 1 :]]
                fail_running_review_runs(
                    db_path=db_path,
                    review_run_ids=remaining_ids,
                    failure_reason=f"gate sweep aborted after {item.note_path}: {exc}",
                    debug_log=runner_debug_log,
                    telemetry_json=telemetry_json,
                )
                parser.exit(exc.returncode, f"{exc}\n")
            completed_in_batch += 1

        reviewed += completed_in_batch
        print(f"Batch {batch_index}/{len(batches)}: reviewed {completed_in_batch} notes")

    if not args.dry_run:
        print(f"Reviewed: {reviewed} notes")


if __name__ == "__main__":
    main()
