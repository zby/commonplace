#!/usr/bin/env python3
"""Create, execute, and finalize one bundle review run."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from gate_selector import GATES_ROOT, ensure_db, resolve_db_path
from review_db import (
    connect,
    fail_review_run,
    init_db,
    insert_review_run,
    insert_review_run_gates,
    load_gate_reviews_for_run,
)
from review_metadata import git_blob_sha, iso_now, last_commit_for_path
from review_model import resolve_model
from review_runners import run_prompt
from resolve_gates import resolve_to_gate_ids, strip_frontmatter

SCHEMA_PATH = Path("scripts/review-schema.sql")
SCRIPT_REPO_ROOT = Path(__file__).resolve().parents[1]


def ensure_review_db(repo_root: Path, db_path: Path) -> None:
    if db_path.exists():
        ensure_db(repo_root, db_path)
        return
    schema_path = repo_root / SCHEMA_PATH
    if not schema_path.is_file():
        schema_path = SCRIPT_REPO_ROOT / SCHEMA_PATH
    init_db(db_path, schema_path)


def encode_stage_filename(gate_id: str) -> str:
    return gate_id.replace("/", "__") + ".md"


def build_prompt(
    *,
    note_path: str,
    gate_ids: list[str],
    gate_texts: dict[str, str],
    review_run_id: int,
    staging_dir: Path,
) -> str:
    gates = " ".join(gate_ids)
    lines = [
        f"Write gate reviews for {note_path} for gates: {gates}",
        "",
        "This task prompt is self-contained. Do not open workflow instruction files unless a command errors and you need to debug the failure.",
        "",
        "Reading scope for this run:",
        "- Read the target note in full.",
        "- Read the requested gate definitions included below. Do not search for alternate copies.",
        "- For semantic grounding or consistency checks, follow only links that appear in the target note.",
        "- Do not do broad repo search or exploratory `rg` sweeps unless you need to resolve a specific linked path that is already referenced by the target note.",
        "- Do not widen the context beyond the target note's linked neighborhood unless the gate text explicitly requires it.",
        "- Treat the helper scripts in scripts/ as command interfaces, not reading material.",
        "- Only inspect script source if a command errors and you need to debug the failure.",
        "- Do not search for gate definitions by name.",
        "- Ignore review backups, workshop copies, and historical artifacts unless the target note links to them explicitly.",
        "",
        "Override only the output sink for this run:",
        "- Do not write to canonical review paths under kb/reports/reviews.",
        "- For each gate, write the full review markdown to the staging file listed below.",
        f"- Then run `python3 scripts/write_gate_review.py --review-run-id {review_run_id} --gate-id <gate-id> --input-file <staged-file>`.",
        "- Use exactly one staged file per gate.",
        "- After all gates have been recorded successfully, stop. Do not finalize the review run yourself.",
        "",
        f"Review run id: {review_run_id}",
        f"Staging directory: {staging_dir}",
        "Requested gate definition files:",
    ]
    for gate_id in gate_ids:
        gate_path = GATES_ROOT / f"{gate_id}.md"
        lines.append(f"- {gate_id} -> {gate_path}")

    lines.extend(
        [
        "",
        "Requested gate definitions (authoritative for this run):",
        ]
    )
    for gate_id in gate_ids:
        lines.append(f"=== gate: {gate_id} ===")
        lines.append(gate_texts[gate_id].rstrip())
        lines.append("")

    lines.extend(
        [
        "Gate staging files:",
        ]
    )
    for gate_id in gate_ids:
        stage_file = staging_dir / encode_stage_filename(gate_id)
        lines.append(f"- {gate_id} -> {stage_file}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one review bundle and persist it into the review DB.")
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, choices=["claude-code", "codex"])
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--model", help="Override runner model and review model.")
    parser.add_argument("--keep-staging", action="store_true", help="Keep temp staging directory after completion.")
    parser.add_argument("--dry-run", action="store_true", help="Print the prompt and staging plan without invoking the runner.")
    args = parser.parse_args()

    repo_root = Path.cwd()
    note_abs = repo_root / args.note_path
    if not note_abs.is_file():
        parser.error(f"note not found: {args.note_path}")

    gates_dir = repo_root / GATES_ROOT
    gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
    review_model = args.model or resolve_model()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_review_db(repo_root, db_path)

    note_sha = git_blob_sha(note_abs, write_object=True)
    note_commit = last_commit_for_path(repo_root, Path(args.note_path))
    started_at = iso_now()
    run_gates: list[tuple[str, str, int]] = []
    gate_texts: dict[str, str] = {}
    for ordinal, gate_id in enumerate(gate_ids):
        gate_abs = gates_dir / f"{gate_id}.md"
        if not gate_abs.is_file():
            parser.error(f"gate not found: {gate_id}")
        run_gates.append((gate_id, git_blob_sha(gate_abs), ordinal))
        gate_texts[gate_id] = strip_frontmatter(gate_abs.read_text(encoding="utf-8"))

    with connect(db_path) as conn:
        review_run_id = insert_review_run(
            conn,
            note_path=args.note_path,
            model_id=review_model,
            runner=args.runner,
            reviewed_note_sha=note_sha,
            reviewed_note_commit=note_commit,
            started_at=started_at,
            status="running",
        )
        insert_review_run_gates(conn, review_run_id=review_run_id, gates=run_gates)
        conn.commit()

    staging_dir = Path(tempfile.mkdtemp(prefix=f"review-run-{review_run_id}-"))
    prompt = build_prompt(
        note_path=args.note_path,
        gate_ids=gate_ids,
        gate_texts=gate_texts,
        review_run_id=review_run_id,
        staging_dir=staging_dir,
    )

    if args.dry_run:
        print(prompt)
        return

    result = run_prompt(runner=args.runner, prompt=prompt, repo_root=repo_root, model=args.model)
    if result.returncode != 0:
        with connect(db_path) as conn:
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=f"{args.runner} exited {result.returncode}",
                completed_at=iso_now(),
                debug_log=(result.stdout + ("\n" if result.stdout and result.stderr else "") + result.stderr).strip() or None,
            )
            conn.commit()
        if not args.keep_staging:
            shutil.rmtree(staging_dir, ignore_errors=True)
        raise SystemExit(result.returncode)

    # Finalize in-process to keep the transaction and error handling local.
    with connect(db_path) as conn:
        written = load_gate_reviews_for_run(conn, review_run_id=review_run_id)
        if len(written) != len(gate_ids):
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=f"incomplete gate coverage: expected {len(gate_ids)}, found {len(written)}",
                completed_at=iso_now(),
                debug_log=(result.stdout + ("\n" if result.stdout and result.stderr else "") + result.stderr).strip() or None,
            )
            conn.commit()
            if not args.keep_staging:
                shutil.rmtree(staging_dir, ignore_errors=True)
            raise SystemExit(1)

    # Reuse the standalone finalizer for the correctness checks and acceptance writes.
    finalize = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).with_name("finalize_review_run.py")),
            "--review-run-id",
            str(review_run_id),
            "--db",
            str(db_path),
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
    )
    if finalize.returncode != 0:
        if not args.keep_staging:
            shutil.rmtree(staging_dir, ignore_errors=True)
        raise SystemExit(finalize.returncode)

    if args.keep_staging:
        print(f"staging: {staging_dir}")
    else:
        shutil.rmtree(staging_dir, ignore_errors=True)
    print(finalize.stdout.rstrip())


if __name__ == "__main__":
    main()
