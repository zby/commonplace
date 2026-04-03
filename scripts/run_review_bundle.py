#!/usr/bin/env python3
"""Create, execute, and finalize one bundle review run."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from review_db import (
    GATES_ROOT,
    complete_review_run,
    connect,
    ensure_db,
    fail_review_run,
    insert_review_run,
    insert_review_run_gates,
    load_gate_reviews_for_run,
    load_review_run,
    resolve_db_path,
)
from review_metadata import git_blob_sha, iso_now, last_commit_for_path
from review_model import resolve_model
from review_runners import run_prompt
from resolve_gates import resolve_to_gate_ids, strip_frontmatter


MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)


def encode_stage_filename(gate_id: str) -> str:
    return gate_id.replace("/", "__") + ".md"


def remove_code_regions(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


def find_markdown_links(text: str) -> list[tuple[str, str]]:
    cleaned = remove_code_regions(text)
    return [(match.group(1), match.group(2).strip()) for match in MARKDOWN_LINK_RE.finditer(cleaned)]


def resolve_note_markdown_links(
    *,
    repo_root: Path,
    note_abs: Path,
    note_body: str,
) -> tuple[list[tuple[str, str, str]], list[tuple[str, str]]]:
    resolved: list[tuple[str, str, str]] = []
    unresolved: list[tuple[str, str]] = []
    seen_resolved: set[tuple[str, str, str]] = set()
    seen_unresolved: set[tuple[str, str]] = set()

    repo_root_resolved = repo_root.resolve()
    for link_text, raw_target in find_markdown_links(note_body):
        if URL_SCHEME_RE.match(raw_target) or raw_target.startswith("#"):
            continue

        bare_target = raw_target.split("#", 1)[0]
        if not bare_target or not bare_target.endswith(".md"):
            continue

        candidate = (note_abs.parent / bare_target).resolve()
        try:
            repo_rel = candidate.relative_to(repo_root_resolved).as_posix()
        except ValueError:
            repo_rel = None

        if candidate.exists() and repo_rel is not None:
            entry = (link_text, raw_target, repo_rel)
            if entry not in seen_resolved:
                seen_resolved.add(entry)
                resolved.append(entry)
            continue

        missing = (link_text, raw_target)
        if missing not in seen_unresolved:
            seen_unresolved.add(missing)
            unresolved.append(missing)

    return resolved, unresolved


def combine_logs(stdout: str, stderr: str) -> str | None:
    return (stdout + ("\n" if stdout and stderr else "") + stderr).strip() or None


def serialize_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if telemetry is None:
        return None
    return json.dumps(telemetry, ensure_ascii=True, sort_keys=True)


def persist_review_run_telemetry(
    conn,
    *,
    review_run_id: int,
    telemetry_json: str | None,
    debug_log: str | None = None,
    fallback_failure_reason: str | None = None,
) -> None:
    review_run = load_review_run(conn, review_run_id=review_run_id)
    if review_run is None:
        return

    if review_run.status == "completed":
        complete_review_run(
            conn,
            review_run_id=review_run_id,
            completed_at=review_run.completed_at or iso_now(),
            debug_log=debug_log,
            telemetry_json=telemetry_json,
        )
        return

    if review_run.status == "failed" or fallback_failure_reason is not None:
        fail_review_run(
            conn,
            review_run_id=review_run_id,
            failure_reason=review_run.failure_reason or fallback_failure_reason or "review run failed",
            completed_at=review_run.completed_at or iso_now(),
            debug_log=debug_log,
            telemetry_json=telemetry_json,
        )


def build_prompt(
    *,
    note_path: str,
    gate_ids: list[str],
    gate_texts: dict[str, str],
    resolved_links: list[tuple[str, str, str]],
    unresolved_links: list[tuple[str, str]],
    review_run_id: int,
    staging_dir: Path,
) -> str:
    gates = " ".join(gate_ids)
    lines = [
        f"Write gate reviews for {note_path} for gates: {gates}",
        "",
        "Reading scope for this run:",
        "- Read the target note in full.",
        "- Read the requested gate definitions included below.",
        "- For semantic grounding or consistency checks, follow only links that appear in the target note.",
        "- When following a markdown link from the target note, use the pre-resolved path table below instead of searching for targets by name.",
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

    lines.append("")
    lines.append("Pre-resolved markdown links from the target note:")
    if resolved_links:
        for link_text, raw_target, repo_rel in resolved_links:
            lines.append(f"- [{link_text}]({raw_target}) -> {repo_rel}")
    else:
        lines.append("- none")

    if unresolved_links:
        lines.append("")
        lines.append("Unresolved markdown links in the target note:")
        lines.append("- Treat these as broken links if they become relevant; do not search for alternate targets.")
        for link_text, raw_target in unresolved_links:
            lines.append(f"- [{link_text}]({raw_target})")

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
    note_text = note_abs.read_text(encoding="utf-8")
    note_body = strip_frontmatter(note_text)
    resolved_links, unresolved_links = resolve_note_markdown_links(
        repo_root=repo_root,
        note_abs=note_abs,
        note_body=note_body,
    )

    gates_dir = repo_root / GATES_ROOT
    gate_ids = resolve_to_gate_ids(args.gate_or_bundle, gates_dir)
    review_model = args.model or resolve_model()
    db_path = Path(args.db).resolve() if args.db else resolve_db_path(repo_root)
    ensure_db(repo_root, db_path)

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
        resolved_links=resolved_links,
        unresolved_links=unresolved_links,
        review_run_id=review_run_id,
        staging_dir=staging_dir,
    )

    if args.dry_run:
        print(prompt)
        return

    result = run_prompt(runner=args.runner, prompt=prompt, repo_root=repo_root, model=args.model)
    telemetry_json = serialize_telemetry(result.telemetry)
    runner_debug_log = combine_logs(result.stdout, result.stderr)
    if result.returncode != 0:
        with connect(db_path) as conn:
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=f"{args.runner} exited {result.returncode}",
                completed_at=iso_now(),
                debug_log=runner_debug_log,
                telemetry_json=telemetry_json,
            )
            conn.commit()
        if not args.keep_staging:
            shutil.rmtree(staging_dir, ignore_errors=True)
        raise SystemExit(result.returncode)

    # Confirm the runner wrote one review per requested gate before finalizing acceptance.
    with connect(db_path) as conn:
        written = load_gate_reviews_for_run(conn, review_run_id=review_run_id)
        if len(written) != len(gate_ids):
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=f"incomplete gate coverage: expected {len(gate_ids)}, found {len(written)}",
                completed_at=iso_now(),
                debug_log=runner_debug_log,
                telemetry_json=telemetry_json,
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
    finalize_debug_log = combine_logs(finalize.stdout, finalize.stderr)
    if finalize.returncode != 0:
        with connect(db_path) as conn:
            persist_review_run_telemetry(
                conn,
                review_run_id=review_run_id,
                telemetry_json=telemetry_json,
                debug_log=finalize_debug_log,
                fallback_failure_reason=f"finalize_review_run.py exited {finalize.returncode}",
            )
            conn.commit()
        if not args.keep_staging:
            shutil.rmtree(staging_dir, ignore_errors=True)
        raise SystemExit(finalize.returncode)

    if telemetry_json is not None:
        with connect(db_path) as conn:
            persist_review_run_telemetry(
                conn,
                review_run_id=review_run_id,
                telemetry_json=telemetry_json,
            )
            conn.commit()

    if args.keep_staging:
        print(f"staging: {staging_dir}")
    else:
        shutil.rmtree(staging_dir, ignore_errors=True)
    print(finalize.stdout.rstrip())


if __name__ == "__main__":
    main()
