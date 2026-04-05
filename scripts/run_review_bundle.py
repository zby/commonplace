#!/usr/bin/env python3
"""Create, execute, and finalize one bundle review run."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

from review_db import (
    GATES_ROOT,
    complete_review_run,
    connect,
    ensure_db,
    fail_review_run,
    insert_gate_review,
    insert_review_run,
    insert_review_run_gates,
    load_review_run_gates,
    load_gate_reviews_for_run,
    load_review_run,
    parse_review_decision,
    rewrite_review_result_footer,
    resolve_db_path,
)
from review_metadata import git_blob_sha, iso_now, last_commit_for_path
from review_model import build_model_id, resolve_model
from review_runners import run_prompt
from resolve_gates import resolve_to_gate_ids, strip_frontmatter


MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)
BUNDLE_START_RE = re.compile(r"^=== GATE REVIEW START: (?P<gate_id>.+?) ===$")
BUNDLE_END_RE = re.compile(r"^=== GATE REVIEW END: (?P<gate_id>.+?) ===$")
BUNDLE_ARTIFACTS_ROOT = Path("kb/reports/bundle-reviews")


class BundleReviewRecordError(RuntimeError):
    def __init__(self, message: str, *, returncode: int = 1) -> None:
        super().__init__(message)
        self.returncode = returncode


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


def extract_bundle_reviews(
    bundle_markdown: str,
    *,
    expected_gate_ids: list[str],
) -> dict[str, str]:
    expected = set(expected_gate_ids)
    reviews: dict[str, str] = {}
    current_gate_id: str | None = None
    current_lines: list[str] = []

    for raw_line in bundle_markdown.splitlines():
        start_match = BUNDLE_START_RE.match(raw_line.strip())
        if start_match is not None:
            if current_gate_id is not None:
                raise ValueError(f"nested gate review start before closing {current_gate_id}")
            gate_id = start_match.group("gate_id")
            if gate_id not in expected:
                raise ValueError(f"unexpected gate in bundle output: {gate_id}")
            if gate_id in reviews:
                raise ValueError(f"duplicate gate in bundle output: {gate_id}")
            current_gate_id = gate_id
            current_lines = []
            continue

        end_match = BUNDLE_END_RE.match(raw_line.strip())
        if end_match is not None:
            gate_id = end_match.group("gate_id")
            if current_gate_id is None:
                raise ValueError(f"gate review end without start: {gate_id}")
            if gate_id != current_gate_id:
                raise ValueError(f"gate review end mismatch: expected {current_gate_id}, found {gate_id}")
            review_text = "\n".join(current_lines).strip()
            if not review_text:
                raise ValueError(f"empty review body for gate: {gate_id}")
            reviews[gate_id] = review_text + "\n"
            current_gate_id = None
            current_lines = []
            continue

        if current_gate_id is not None:
            current_lines.append(raw_line)

    if current_gate_id is not None:
        raise ValueError(f"unterminated gate review block: {current_gate_id}")

    missing = [gate_id for gate_id in expected_gate_ids if gate_id not in reviews]
    if missing:
        raise ValueError(f"missing gate reviews in bundle output: {', '.join(missing)}")

    return reviews


def rewrite_bundle_result_footers(
    bundle_markdown: str,
    *,
    parsed_reviews: dict[str, str],
) -> str:
    rewritten_lines: list[str] = []
    current_gate_id: str | None = None

    for raw_line in bundle_markdown.splitlines():
        start_match = BUNDLE_START_RE.match(raw_line.strip())
        if start_match is not None:
            current_gate_id = start_match.group("gate_id")
            rewritten_lines.append(raw_line)
            continue

        end_match = BUNDLE_END_RE.match(raw_line.strip())
        if end_match is not None:
            gate_id = end_match.group("gate_id")
            if current_gate_id == gate_id and gate_id in parsed_reviews:
                rewritten_lines.extend(parsed_reviews[gate_id].rstrip("\n").splitlines())
            rewritten_lines.append(raw_line)
            current_gate_id = None
            continue

        if current_gate_id is None:
            rewritten_lines.append(raw_line)

    rewritten = "\n".join(rewritten_lines)
    if bundle_markdown.endswith("\n"):
        return rewritten + "\n"
    return rewritten


def write_bundle_artifacts(
    *,
    artifact_dir: Path,
    raw_bundle_markdown: str,
    parsed_reviews: dict[str, str] | None = None,
) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "bundle-output.md").write_text(raw_bundle_markdown, encoding="utf-8")
    if parsed_reviews is None:
        return
    for gate_id, review_text in parsed_reviews.items():
        (artifact_dir / encode_stage_filename(gate_id)).write_text(review_text, encoding="utf-8")


def bundle_artifact_dir(repo_root: Path, review_run_id: int) -> Path:
    return repo_root / BUNDLE_ARTIFACTS_ROOT / f"review-run-{review_run_id}"


def record_bundle_reviews(
    conn,
    *,
    review_run_id: int,
    gate_ids: list[str],
    parsed_reviews: dict[str, str],
) -> None:
    review_run = load_review_run(conn, review_run_id=review_run_id)
    if review_run is None:
        raise ValueError(f"review run not found: {review_run_id}")
    if review_run.status != "running":
        raise ValueError(f"review run is not writable: {review_run.status}")

    run_gates = {row.gate_id: row for row in load_review_run_gates(conn, review_run_id=review_run_id)}
    for gate_id in gate_ids:
        run_gate = run_gates.get(gate_id)
        if run_gate is None:
            raise ValueError(f"gate {gate_id} is not part of review run {review_run_id}")
        review_text = parsed_reviews[gate_id]
        decision = parse_review_decision(review_text)
        canonical_review_text = rewrite_review_result_footer(review_text, decision=decision)
        insert_gate_review(
            conn,
            review_run_id=review_run_id,
            note_path=review_run.note_path,
            gate_id=gate_id,
            model_id=review_run.model_id,
            decision=decision,
            rationale_markdown=canonical_review_text,
            evidence_json=None,
            gate_sha=run_gate.gate_sha,
            reviewed_note_sha=review_run.reviewed_note_sha,
            reviewed_note_commit=review_run.reviewed_note_commit,
            reviewed_at=iso_now(),
            review_kind="full-review",
        )


def serialize_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if telemetry is None:
        return None
    return json.dumps(telemetry, ensure_ascii=True, sort_keys=True)


def model_id_from_telemetry(telemetry: dict[str, object] | None) -> str | None:
    if not isinstance(telemetry, dict):
        return None
    model = telemetry.get("model")
    if not isinstance(model, str) or not model.strip():
        return None
    reasoning_effort = telemetry.get("reasoning_effort")
    if reasoning_effort is not None and not isinstance(reasoning_effort, str):
        reasoning_effort = None
    return build_model_id(model, reasoning_effort)


def update_review_run_model_id(
    conn,
    *,
    review_run_id: int,
    model_id: str,
) -> None:
    conn.execute(
        """
        UPDATE review_runs
        SET model_id = ?
        WHERE id = ?
        """,
        (model_id, review_run_id),
    )


def persist_review_run_telemetry(
    conn,
    *,
    review_run_id: int,
    telemetry_json: str | None,
    raw_bundle_markdown: str | None = None,
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
            raw_bundle_markdown=raw_bundle_markdown,
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
            raw_bundle_markdown=raw_bundle_markdown,
            debug_log=debug_log,
            telemetry_json=telemetry_json,
        )


def finalize_review_run_subprocess(
    *,
    repo_root: Path,
    db_path: Path,
    review_run_id: int,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
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


def record_bundle_review_run(
    *,
    repo_root: Path,
    db_path: Path,
    review_run_id: int,
    raw_bundle_markdown: str,
    telemetry_json: str | None = None,
    debug_log: str | None = None,
) -> str:
    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    write_bundle_artifacts(artifact_dir=artifact_dir, raw_bundle_markdown=raw_bundle_markdown)

    with connect(db_path) as conn:
        review_run = load_review_run(conn, review_run_id=review_run_id)
        if review_run is None:
            raise BundleReviewRecordError(f"review run not found: {review_run_id}")
        if review_run.status != "running":
            raise BundleReviewRecordError(f"review run is not writable: {review_run.status}")

        gate_ids = [row.gate_id for row in load_review_run_gates(conn, review_run_id=review_run_id)]
        if not gate_ids:
            reason = f"review run has no gates: {review_run_id}"
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=reason,
                completed_at=iso_now(),
                raw_bundle_markdown=raw_bundle_markdown,
                debug_log=debug_log,
                telemetry_json=telemetry_json,
            )
            conn.commit()
            raise BundleReviewRecordError(reason)

        try:
            parsed_reviews = extract_bundle_reviews(raw_bundle_markdown, expected_gate_ids=gate_ids)
            canonical_reviews = {
                gate_id: rewrite_review_result_footer(
                    review_text,
                    decision=parse_review_decision(review_text),
                )
                for gate_id, review_text in parsed_reviews.items()
            }
            canonical_bundle_markdown = rewrite_bundle_result_footers(
                raw_bundle_markdown,
                parsed_reviews=canonical_reviews,
            )
            write_bundle_artifacts(
                artifact_dir=artifact_dir,
                raw_bundle_markdown=canonical_bundle_markdown,
                parsed_reviews=canonical_reviews,
            )
            record_bundle_reviews(
                conn,
                review_run_id=review_run_id,
                gate_ids=gate_ids,
                parsed_reviews=canonical_reviews,
            )
        except (ValueError, sqlite3.IntegrityError) as exc:
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=str(exc),
                completed_at=iso_now(),
                raw_bundle_markdown=raw_bundle_markdown,
                debug_log=debug_log,
                telemetry_json=telemetry_json,
            )
            conn.commit()
            raise BundleReviewRecordError(str(exc)) from exc

        conn.commit()

        written = load_gate_reviews_for_run(conn, review_run_id=review_run_id)
        if len(written) != len(gate_ids):
            reason = f"incomplete gate coverage: expected {len(gate_ids)}, found {len(written)}"
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=reason,
                completed_at=iso_now(),
                raw_bundle_markdown=raw_bundle_markdown,
                debug_log=debug_log,
                telemetry_json=telemetry_json,
            )
            conn.commit()
            raise BundleReviewRecordError(reason)

    finalize = finalize_review_run_subprocess(
        repo_root=repo_root,
        db_path=db_path,
        review_run_id=review_run_id,
    )
    finalize_debug_log = combine_logs(finalize.stdout, finalize.stderr)
    if finalize.returncode != 0:
        with connect(db_path) as conn:
            persist_review_run_telemetry(
                conn,
                review_run_id=review_run_id,
                telemetry_json=telemetry_json,
                raw_bundle_markdown=canonical_bundle_markdown,
                debug_log=finalize_debug_log,
                fallback_failure_reason=f"finalize_review_run.py exited {finalize.returncode}",
            )
            conn.commit()
        message = finalize_debug_log or f"finalize_review_run.py exited {finalize.returncode}"
        raise BundleReviewRecordError(message, returncode=finalize.returncode)

    if telemetry_json is not None or raw_bundle_markdown:
        with connect(db_path) as conn:
            persist_review_run_telemetry(
                conn,
                review_run_id=review_run_id,
                telemetry_json=telemetry_json,
                raw_bundle_markdown=canonical_bundle_markdown,
            )
            conn.commit()

    return finalize.stdout.rstrip()


def build_prompt(
    *,
    note_path: str,
    gate_ids: list[str],
    gate_texts: dict[str, str],
    resolved_links: list[tuple[str, str, str]],
    unresolved_links: list[tuple[str, str]],
    review_run_id: int,
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
        "Output contract for this run:",
        "- Do not write files or invoke review helper scripts.",
        "- Return exactly one markdown document in this process's stdout.",
        "- Use exactly one block per requested gate.",
        "- Use these exact sentinels for every block:",
        "  === GATE REVIEW START: <gate-id> ===",
        "  === GATE REVIEW END: <gate-id> ===",
        "- Inside each block, include a decision line in a parseable form such as `## Result: PASS` or `## Result: WARN`.",
        "- Make the decision line the last non-empty line inside each gate block.",
        "- End output after the final gate block.",
        "",
        f"Review run id: {review_run_id}",
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
            "Bundle template:",
            "# Review Bundle",
            "",
            f"Review run id: {review_run_id}",
            f"Target: {note_path}",
            "",
        ]
    )
    for gate_id in gate_ids:
        lines.extend(
            [
                f"=== GATE REVIEW START: {gate_id} ===",
                "### Summary",
                "<short paragraph>",
                "",
                "### Findings",
                "- <severity>: <finding>",
                "",
                "### Suggested Revision",
                "<optional; omit if not needed>",
                "",
                "## Result: PASS|WARN|FAIL|ERROR",
                f"=== GATE REVIEW END: {gate_id} ===",
                "",
            ]
        )

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

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run one review bundle and persist it into the review DB.")
    parser.add_argument("note_path", help="Repository-relative note path.")
    parser.add_argument("gate_or_bundle", nargs="+", help="Gate IDs and/or bundle names.")
    parser.add_argument("--runner", required=True, choices=["claude-code", "codex"])
    parser.add_argument("--db", help="Override COMMONPLACE_REVIEW_DB.")
    parser.add_argument("--model", help="Override runner model and review model.")
    parser.add_argument(
        "--keep-staging",
        action="store_true",
        help="Compatibility flag. Bundle artifacts are always kept; this prints the artifact directory.",
    )
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

    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    prompt = build_prompt(
        note_path=args.note_path,
        gate_ids=gate_ids,
        gate_texts=gate_texts,
        resolved_links=resolved_links,
        unresolved_links=unresolved_links,
        review_run_id=review_run_id,
    )

    if args.dry_run:
        print(prompt)
        return

    result = run_prompt(runner=args.runner, prompt=prompt, repo_root=repo_root, model=args.model)
    raw_bundle_markdown = result.stdout
    write_bundle_artifacts(artifact_dir=artifact_dir, raw_bundle_markdown=raw_bundle_markdown)
    actual_review_model = model_id_from_telemetry(result.telemetry)
    if actual_review_model is not None and actual_review_model != review_model:
        with connect(db_path) as conn:
            update_review_run_model_id(
                conn,
                review_run_id=review_run_id,
                model_id=actual_review_model,
            )
            conn.commit()
        print(
            (
                f"warning: requested model partition {review_model} "
                f"does not match runner telemetry {actual_review_model}; "
                "recording the actual partition"
            ),
            file=sys.stderr,
        )
        review_model = actual_review_model
    telemetry_json = serialize_telemetry(result.telemetry)
    runner_debug_log = combine_logs(result.stdout, result.stderr)
    if result.returncode != 0:
        with connect(db_path) as conn:
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=f"{args.runner} exited {result.returncode}",
                completed_at=iso_now(),
                raw_bundle_markdown=raw_bundle_markdown,
                debug_log=runner_debug_log,
                telemetry_json=telemetry_json,
            )
            conn.commit()
        raise SystemExit(result.returncode)

    try:
        finalize_output = record_bundle_review_run(
            repo_root=repo_root,
            db_path=db_path,
            review_run_id=review_run_id,
            raw_bundle_markdown=raw_bundle_markdown,
            telemetry_json=telemetry_json,
            debug_log=runner_debug_log,
        )
    except BundleReviewRecordError as exc:
        parser.exit(exc.returncode, f"{exc}\n")

    if args.keep_staging:
        print(f"artifacts: {artifact_dir}")
    print(finalize_output)


if __name__ == "__main__":
    main()
