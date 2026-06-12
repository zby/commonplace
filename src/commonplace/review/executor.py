"""Execute batched pair reviews: one runner call, per-run salvage and finalize.

The executor owns the lifecycle shared by every packing shape: render one
prompt for a set of note targets, invoke the runner once, parse pair blocks,
then finalize each review run whose pairs all came back and fail the rest.
Failure policy lives here once: usage exhaustion, interrupts, runner errors,
structural parse errors, and per-run missing pairs.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import find_markdown_links_with_text
from commonplace.review.finalization import record_and_finalize_run
from commonplace.review.protocol.format import PAIR_END_TEMPLATE, PAIR_START_TEMPLATE
from commonplace.review.protocol.parser import ParsedPairBundle, parse_pair_bundle
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.review_db import (
    PendingGateReview,
    attach_execution_data,
    connect,
    fail_review_run,
)
from commonplace.review.review_metadata import iso_now
from commonplace.review.review_model import build_model_id
from commonplace.review.review_runners import run_prompt


URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)
BUNDLE_ARTIFACTS_ROOT = Path("kb/reports/bundle-reviews")
USAGE_EXHAUSTION_TEXT = "out of extra usage"


class UsageExhausted(Exception):
    """Raised when the runner reports that paid usage is exhausted.

    Callers running multiple batches (e.g. review_sweep) should catch this
    and abort the whole sweep rather than continuing.
    """


@dataclass(frozen=True)
class BatchOutcome:
    completed: list[int]
    failed: list[tuple[int, str]]
    runner_returncode: int

    @property
    def ok(self) -> bool:
        return self.runner_returncode == 0 and not self.failed


def encode_stage_filename(gate_id: str) -> str:
    return gate_id.replace("/", "__") + ".md"


def bundle_artifact_dir(repo_root: Path, review_run_id: int) -> Path:
    return repo_root / BUNDLE_ARTIFACTS_ROOT / f"review-run-{review_run_id}"


def write_run_artifacts(
    *,
    artifact_dir: Path,
    bundle_markdown: str,
    gate_texts: dict[str, str] | None = None,
) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "bundle-output.md").write_text(bundle_markdown, encoding="utf-8")
    if gate_texts is None:
        return
    for gate_id, review_text in gate_texts.items():
        (artifact_dir / encode_stage_filename(gate_id)).write_text(review_text, encoding="utf-8")


def combine_logs(stdout: str, stderr: str) -> str | None:
    return (stdout + ("\n" if stdout and stderr else "") + stderr).strip() or None


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


def prepare_note_target(
    *,
    repo_root: Path,
    note_path: str,
    review_run_id: int,
    gate_ids: tuple[str, ...],
) -> NoteReviewTarget:
    note_abs = repo_root / note_path
    note_text = note_abs.read_text(encoding="utf-8")
    note_body = frontmatter.strip(note_text).lstrip("\n")
    resolved_links, unresolved_links = resolve_note_markdown_links(
        repo_root=repo_root,
        note_abs=note_abs,
        note_body=note_body,
    )
    return NoteReviewTarget(
        note_path=note_path,
        review_run_id=review_run_id,
        gate_ids=gate_ids,
        note_text=note_text,
        resolved_links=resolved_links,
        unresolved_links=unresolved_links,
    )


def assemble_run_document(
    *,
    note_path: str,
    review_run_id: int,
    gate_ids: tuple[str, ...],
    canonical_texts: dict[tuple[str, str], str],
) -> tuple[str, dict[str, str]]:
    """Build the per-run canonical bundle document and its per-gate texts."""
    lines = [
        "# Review Bundle",
        "",
        f"Review run id: {review_run_id}",
        f"Target: {note_path}",
        "",
    ]
    gate_reviews: dict[str, str] = {}
    for gate_id in gate_ids:
        review_text = canonical_texts[(note_path, gate_id)]
        gate_reviews[gate_id] = review_text
        lines.extend(
            [
                PAIR_START_TEMPLATE.format(note_path=note_path, gate_id=gate_id),
                review_text.rstrip("\n"),
                PAIR_END_TEMPLATE.format(note_path=note_path, gate_id=gate_id),
                "",
            ]
        )
    return "\n".join(lines), gate_reviews


def fail_running_review_runs(
    *,
    db_path: Path,
    review_run_ids: list[int],
    failure_reason: str,
    debug_log: str | None = None,
    telemetry_json: str | None = None,
    raw_bundle_markdown: str | None = None,
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
            attach_execution_data(
                conn,
                review_run_id=int(row["id"]),
                telemetry_json=telemetry_json,
                raw_bundle_markdown=raw_bundle_markdown,
                debug_log=debug_log,
            )
            fail_review_run(
                conn,
                review_run_id=int(row["id"]),
                failure_reason=failure_reason,
                completed_at=completed_at,
            )
        conn.commit()


def finalize_run_from_pairs(
    conn,
    *,
    repo_root: Path,
    note_path: str,
    review_run_id: int,
    gate_ids: tuple[str, ...],
    parsed: ParsedPairBundle,
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    actual_model_id: str | None = None,
) -> int:
    """Finalize one run from a parsed pair bundle. Raises ValueError on failure
    (the run is failed in the DB before raising)."""
    run_document, gate_texts = assemble_run_document(
        note_path=note_path,
        review_run_id=review_run_id,
        gate_ids=gate_ids,
        canonical_texts=parsed.canonical_texts,
    )
    write_run_artifacts(
        artifact_dir=bundle_artifact_dir(repo_root, review_run_id),
        bundle_markdown=run_document,
        gate_texts=gate_texts,
    )
    gate_reviews = [
        PendingGateReview(
            gate_id=gate_id,
            decision=parsed.reviews[(note_path, gate_id)].decision,
            rationale_markdown=parsed.reviews[(note_path, gate_id)].rationale_markdown,
        )
        for gate_id in gate_ids
    ]
    return record_and_finalize_run(
        conn,
        review_run_id=review_run_id,
        gate_reviews=gate_reviews,
        actual_model_id=actual_model_id,
        telemetry_json=telemetry_json,
        raw_bundle_markdown=run_document,
        debug_log=debug_log,
    )


def execute_batch(
    *,
    repo_root: Path,
    db_path: Path,
    targets: list[NoteReviewTarget],
    gate_texts: dict[str, str],
    runner: str,
    runner_model: str,
    model_id: str,
) -> BatchOutcome:
    """Run one batched runner call over the given prepared targets.

    Every target must already have its review run created (status running).
    Returns a BatchOutcome; raises UsageExhausted after failing all runs if
    the runner reports exhausted usage, and re-raises KeyboardInterrupt after
    failing all runs.
    """
    run_ids = [target.review_run_id for target in targets]

    try:
        prompt = render_pairs_prompt(notes=targets, gate_texts=gate_texts)
    except ValueError as exc:
        fail_running_review_runs(db_path=db_path, review_run_ids=run_ids, failure_reason=str(exc))
        return BatchOutcome(completed=[], failed=[(rid, str(exc)) for rid in run_ids], runner_returncode=0)

    try:
        result = run_prompt(runner=runner, prompt=prompt, repo_root=repo_root, model=runner_model)
    except KeyboardInterrupt:
        fail_running_review_runs(
            db_path=db_path,
            review_run_ids=run_ids,
            failure_reason="review batch interrupted",
        )
        raise

    raw_output = result.stdout
    for target in targets:
        write_run_artifacts(
            artifact_dir=bundle_artifact_dir(repo_root, target.review_run_id),
            bundle_markdown=raw_output,
        )

    telemetry_json = serialize_telemetry(result.telemetry)
    debug_log = combine_logs(result.stdout, result.stderr)
    actual_model_id = model_id_from_telemetry(result.telemetry)
    if actual_model_id is not None and actual_model_id != model_id:
        print(
            (
                f"warning: requested model partition {model_id} "
                f"does not match runner telemetry {actual_model_id}; "
                "recording the actual partition"
            ),
            file=sys.stderr,
        )

    if USAGE_EXHAUSTION_TEXT in (result.stdout + result.stderr).lower():
        fail_running_review_runs(
            db_path=db_path,
            review_run_ids=run_ids,
            failure_reason="runner reported usage exhausted",
            debug_log=debug_log,
            telemetry_json=telemetry_json,
            raw_bundle_markdown=raw_output,
        )
        raise UsageExhausted()

    if result.returncode != 0:
        reason = f"{runner} exited {result.returncode}"
        fail_running_review_runs(
            db_path=db_path,
            review_run_ids=run_ids,
            failure_reason=reason,
            debug_log=debug_log,
            telemetry_json=telemetry_json,
            raw_bundle_markdown=raw_output,
        )
        return BatchOutcome(
            completed=[],
            failed=[(rid, reason) for rid in run_ids],
            runner_returncode=result.returncode,
        )

    expected_pairs = [(target.note_path, gate_id) for target in targets for gate_id in target.gate_ids]
    try:
        parsed = parse_pair_bundle(raw_output, expected_pairs=expected_pairs)
    except ValueError as exc:
        fail_running_review_runs(
            db_path=db_path,
            review_run_ids=run_ids,
            failure_reason=str(exc),
            debug_log=debug_log,
            telemetry_json=telemetry_json,
            raw_bundle_markdown=raw_output,
        )
        return BatchOutcome(completed=[], failed=[(rid, str(exc)) for rid in run_ids], runner_returncode=0)

    missing_by_note: dict[str, list[str]] = {}
    for note_path, gate_id in parsed.missing:
        missing_by_note.setdefault(note_path, []).append(gate_id)

    completed: list[int] = []
    failed: list[tuple[int, str]] = []
    for target in targets:
        missing_gates = missing_by_note.get(target.note_path)
        if missing_gates:
            reason = f"missing pair reviews: {', '.join(sorted(missing_gates))}"
            fail_running_review_runs(
                db_path=db_path,
                review_run_ids=[target.review_run_id],
                failure_reason=reason,
                debug_log=debug_log,
                telemetry_json=telemetry_json,
                raw_bundle_markdown=raw_output,
            )
            failed.append((target.review_run_id, reason))
            continue

        with connect(db_path) as conn:
            try:
                finalize_run_from_pairs(
                    conn,
                    repo_root=repo_root,
                    note_path=target.note_path,
                    review_run_id=target.review_run_id,
                    gate_ids=target.gate_ids,
                    parsed=parsed,
                    telemetry_json=telemetry_json,
                    debug_log=debug_log,
                    actual_model_id=actual_model_id,
                )
            except ValueError as exc:
                conn.commit()
                failed.append((target.review_run_id, str(exc)))
                continue
            conn.commit()
        completed.append(target.review_run_id)

    return BatchOutcome(completed=completed, failed=failed, runner_returncode=0)
