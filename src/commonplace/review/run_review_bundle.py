"""Library functions for run_review_bundle.

Pure logic lives here; run_review_bundle.py is the thin CLI wrapper.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import find_markdown_links_with_text
from commonplace.review.protocol import parser as review_protocol_parser
from commonplace.review.protocol.prompt import OutputMode, render_bundle_prompt
from commonplace.review.review_db import (
    PendingGateReview,
    attach_execution_data,
    connect,
    create_run,
    ensure_db,
    fail_review_run,
)
from commonplace.review.review_metadata import iso_now, resolve_review_target
from commonplace.review.review_model import build_model_id, normalize_model_id
from commonplace.review.review_runners import run_prompt


URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)
BUNDLE_ARTIFACTS_ROOT = Path("kb/reports/bundle-reviews")
USAGE_EXHAUSTION_TEXT = "out of extra usage"


class UsageExhausted(Exception):
    """Raised when the runner reports that paid usage is exhausted.

    Callers running multiple bundles (e.g. review_sweep) should catch this
    and abort the whole batch rather than continuing.
    """


def encode_stage_filename(gate_id: str) -> str:
    return gate_id.replace("/", "__") + ".md"


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
    for link_text, raw_target in find_markdown_links_with_text(note_body):
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


def parse_bundle_gate_reviews(
    raw_bundle_markdown: str,
    *,
    expected_gate_ids: list[str],
) -> tuple[str, list[PendingGateReview], dict[str, str]]:
    canonical_bundle_markdown, parsed_reviews, canonical_reviews = review_protocol_parser.parse_bundle_output(
        raw_bundle_markdown,
        expected_gate_ids=expected_gate_ids,
    )
    gate_reviews: list[PendingGateReview] = []
    for gate_id in expected_gate_ids:
        parsed_review = parsed_reviews[gate_id]
        gate_reviews.append(
            PendingGateReview(
                gate_id=gate_id,
                decision=parsed_review.decision,
                rationale_markdown=parsed_review.rationale_markdown,
            )
        )

    return canonical_bundle_markdown, gate_reviews, canonical_reviews


def build_review_run_prompt(
    *,
    repo_root: Path,
    note_path: str,
    gate_ids: list[str],
    gate_texts: dict[str, str],
    review_run_id: int,
    output_mode: OutputMode = "stdout",
    bundle_output_path: str | None = None,
) -> str:
    note_abs = repo_root / note_path
    note_text = note_abs.read_text(encoding="utf-8")
    note_body = frontmatter.strip(note_text).lstrip("\n")
    resolved_links, unresolved_links = resolve_note_markdown_links(
        repo_root=repo_root,
        note_abs=note_abs,
        note_body=note_body,
    )
    return render_bundle_prompt(
        note_path=note_path,
        gate_ids=gate_ids,
        gate_texts=gate_texts,
        resolved_links=resolved_links,
        unresolved_links=unresolved_links,
        review_run_id=review_run_id,
        output_mode=output_mode,
        bundle_output_path=bundle_output_path,
    )


def run_bundle(
    *,
    repo_root: Path,
    db_path: Path,
    note_path: str,
    gate_or_bundle: list[str],
    runner: str,
    model: str,
    dry_run: bool,
) -> int:
    """Run one review bundle end-to-end. Returns a process exit code.

    Callers are responsible for validating note_path and model before calling;
    this function assumes both are well-formed.
    """
    runner_model = model
    model = normalize_model_id(model)

    note_sha, note_commit, started_at, run_gates, gate_texts = resolve_review_target(
        repo_root, note_path, gate_or_bundle,
    )
    gate_ids = [g[0] for g in run_gates]

    if dry_run:
        dry_run_prompt = build_review_run_prompt(
            repo_root=repo_root,
            note_path=note_path,
            gate_ids=gate_ids,
            gate_texts=gate_texts,
            review_run_id=0,
        )
        print(dry_run_prompt)
        return 0

    ensure_db(repo_root, db_path)

    with connect(db_path) as conn:
        review_run_id = create_run(
            conn,
            note_path=note_path,
            model_id=model,
            runner=runner,
            reviewed_note_sha=note_sha,
            reviewed_note_commit=note_commit,
            started_at=started_at,
            gates=run_gates,
        )
        conn.commit()

    prompt = build_review_run_prompt(
        repo_root=repo_root,
        note_path=note_path,
        gate_ids=gate_ids,
        gate_texts=gate_texts,
        review_run_id=review_run_id,
    )
    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)

    result = run_prompt(runner=runner, prompt=prompt, repo_root=repo_root, model=runner_model)
    raw_bundle_markdown = result.stdout
    write_bundle_artifacts(artifact_dir=artifact_dir, raw_bundle_markdown=raw_bundle_markdown)
    telemetry_json = serialize_telemetry(result.telemetry)
    runner_debug_log = combine_logs(result.stdout, result.stderr)
    actual_review_model = model_id_from_telemetry(result.telemetry)
    if actual_review_model is not None and actual_review_model != model:
        print(
            (
                f"warning: requested model partition {model} "
                f"does not match runner telemetry {actual_review_model}; "
                "recording the actual partition"
            ),
            file=sys.stderr,
        )

    usage_exhausted = USAGE_EXHAUSTION_TEXT in (result.stdout + result.stderr).lower()

    if result.returncode != 0 or usage_exhausted:
        failure_reason = (
            "runner reported usage exhausted"
            if usage_exhausted
            else f"{runner} exited {result.returncode}"
        )
        with connect(db_path) as conn:
            attach_execution_data(
                conn,
                review_run_id=review_run_id,
                telemetry_json=telemetry_json,
                raw_bundle_markdown=raw_bundle_markdown,
                debug_log=runner_debug_log,
            )
            fail_review_run(
                conn,
                review_run_id=review_run_id,
                failure_reason=failure_reason,
                completed_at=iso_now(),
            )
            conn.commit()
        if usage_exhausted:
            raise UsageExhausted()
        return result.returncode

    with connect(db_path) as conn:
        from commonplace.review.bundle_ingest import parse_and_finalize_bundle_output

        try:
            gate_count = parse_and_finalize_bundle_output(
                conn,
                repo_root=repo_root,
                review_run_id=review_run_id,
                raw_bundle_markdown=raw_bundle_markdown,
                expected_gate_ids=gate_ids,
                telemetry_json=telemetry_json,
                debug_log=runner_debug_log,
                actual_model_id=actual_review_model,
            )
        except ValueError as exc:
            conn.commit()
            print(str(exc), file=sys.stderr)
            return 1
        conn.commit()

    print(f"completed {review_run_id} {gate_count}")
    return 0
