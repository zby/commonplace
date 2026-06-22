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
from commonplace.review.artifacts import write_manifest, write_pair_result_files
from commonplace.review.finalization import record_and_finalize_run
from commonplace.review.protocol.format import PAIR_END_TEMPLATE, PAIR_START_TEMPLATE
from commonplace.review.protocol.parser import ParsedPairBundle, parse_pair_bundle
from commonplace.review.protocol.prompt import NoteReviewTarget, render_pairs_prompt
from commonplace.review.review_db import (
    PendingReviewPair,
    attach_execution_data,
    connect,
    fail_review_run,
    load_review_pairs_for_run,
    load_review_run,
)
from commonplace.review.review_metadata import iso_now
from commonplace.review.review_model import build_model_id
from commonplace.review.runners import run_prompt


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


@dataclass(frozen=True)
class RunPairs:
    """One review run's identity and expected pair set, for finalization."""

    review_run_id: int
    pairs: tuple[tuple[str, str], ...]


def bundle_artifact_dir(repo_root: Path, review_run_id: int) -> Path:
    return repo_root / BUNDLE_ARTIFACTS_ROOT / f"review-run-{review_run_id}"


def write_run_artifacts(
    *,
    artifact_dir: Path,
    bundle_markdown: str,
) -> None:
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "bundle-output.md").write_text(bundle_markdown, encoding="utf-8")


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
    review_run_id: int,
    pairs: tuple[tuple[str, str], ...],
    canonical_texts: dict[tuple[str, str], str],
) -> tuple[str, dict[str, str]]:
    """Build the per-run canonical bundle document and pair result texts."""
    lines = [
        "# Review Bundle",
        "",
        f"Review run id: {review_run_id}",
        "",
    ]
    pair_reviews: dict[str, str] = {}
    for note_path, gate_id in pairs:
        review_text = canonical_texts[(note_path, gate_id)]
        pair_reviews[f"{note_path} :: {gate_id}"] = review_text
        lines.extend(
            [
                PAIR_START_TEMPLATE.format(note_path=note_path, gate_id=gate_id),
                review_text.rstrip("\n"),
                PAIR_END_TEMPLATE.format(note_path=note_path, gate_id=gate_id),
                "",
            ]
        )
    return "\n".join(lines), pair_reviews


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
            SELECT review_run_id, status
            FROM review_runs
            WHERE review_run_id IN ({", ".join("?" for _ in review_run_ids)})
            """,
            review_run_ids,
        ).fetchall()
        for row in rows:
            if row["status"] != "running":
                continue
            attach_execution_data(
                conn,
                review_run_id=int(row["review_run_id"]),
                telemetry_json=telemetry_json,
                raw_bundle_markdown=raw_bundle_markdown,
                debug_log=debug_log,
            )
            fail_review_run(
                conn,
                review_run_id=int(row["review_run_id"]),
                failure_reason=failure_reason,
                completed_at=completed_at,
            )
        conn.commit()


def finalize_run_from_pairs(
    conn,
    *,
    review_run_id: int,
    pairs: tuple[tuple[str, str], ...],
    parsed: ParsedPairBundle,
    raw_bundle_markdown: str | None = None,
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    actual_model_id: str | None = None,
) -> int:
    """Finalize one run from a parsed pair bundle. Raises ValueError on failure
    (the run is failed in the DB before raising)."""
    run_document, _ = assemble_run_document(
        review_run_id=review_run_id,
        pairs=pairs,
        canonical_texts=parsed.canonical_texts,
    )
    review_pairs = [
        PendingReviewPair(
            note_path=note_path,
            gate_id=gate_id,
            decision=parsed.reviews[(note_path, gate_id)].decision,
            rationale_markdown=parsed.reviews[(note_path, gate_id)].rationale_markdown,
        )
        for note_path, gate_id in pairs
    ]
    return record_and_finalize_run(
        conn,
        review_run_id=review_run_id,
        review_pairs=review_pairs,
        actual_model_id=actual_model_id,
        telemetry_json=telemetry_json,
        raw_bundle_markdown=raw_bundle_markdown or run_document,
        debug_log=debug_log,
    )


def write_artifacts_for_run(
    *,
    repo_root: Path,
    review_run_id: int,
    pairs: tuple[tuple[str, str], ...],
    parsed: ParsedPairBundle,
    packing: str,
) -> None:
    run_document, _ = assemble_run_document(
        review_run_id=review_run_id,
        pairs=pairs,
        canonical_texts=parsed.canonical_texts,
    )
    artifact_dir = bundle_artifact_dir(repo_root, review_run_id)
    write_run_artifacts(artifact_dir=artifact_dir, bundle_markdown=run_document)
    write_pair_result_files(
        artifact_dir=artifact_dir,
        packing=packing,
        pairs=pairs,
        canonical_texts=parsed.canonical_texts,
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
    run_ids = sorted({target.review_run_id for target in targets})
    if len(run_ids) != 1:
        raise ValueError("execute_batch expects one review_run_id per prompt")

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
    write_run_artifacts(
        artifact_dir=bundle_artifact_dir(repo_root, run_ids[0]),
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

    run_pairs = [RunPairs(review_run_id=run_ids[0], pairs=tuple(expected_pairs))]
    completed, failed = finalize_runs_from_parsed(
        repo_root=repo_root,
        db_path=db_path,
        run_pairs=run_pairs,
        parsed=parsed,
        raw_output=raw_output,
        telemetry_json=telemetry_json,
        debug_log=debug_log,
        actual_model_id=actual_model_id,
    )
    return BatchOutcome(completed=completed, failed=failed, runner_returncode=0)


def finalize_runs_from_parsed(
    *,
    repo_root: Path,
    db_path: Path,
    run_pairs: list[RunPairs],
    parsed: ParsedPairBundle,
    raw_output: str | None = None,
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    actual_model_id: str | None = None,
) -> tuple[list[int], list[tuple[int, str]]]:
    """Finalize parsed runs and write each run's canonical artifacts."""
    completed, failed = finalize_run_records_from_parsed(
        db_path=db_path,
        run_pairs=run_pairs,
        parsed=parsed,
        raw_output=raw_output,
        telemetry_json=telemetry_json,
        debug_log=debug_log,
        actual_model_id=actual_model_id,
    )
    with connect(db_path) as conn:
        rows_by_run = {
            run.review_run_id: (
                load_review_run(conn, review_run_id=run.review_run_id),
                load_review_pairs_for_run(conn, review_run_id=run.review_run_id),
            )
            for run in run_pairs
        }
    for run in run_pairs:
        review_run, updated_pairs = rows_by_run[run.review_run_id]
        if review_run is None:
            continue
        completed_pairs = tuple(
            (pair.note_path, pair.gate_id)
            for pair in updated_pairs
            if pair.pair_status == "completed"
        )
        write_artifacts_for_run(
            repo_root=repo_root,
            review_run_id=run.review_run_id,
            pairs=completed_pairs,
            parsed=parsed,
            packing=review_run.packing,
        )
        artifact_dir = bundle_artifact_dir(repo_root, run.review_run_id)
        artifact_dir_rel = artifact_dir.relative_to(repo_root).as_posix()
        write_manifest(
            repo_root=repo_root,
            artifact_dir=artifact_dir,
            review_run_id=run.review_run_id,
            packing=review_run.packing,
            prompt_path=f"{artifact_dir_rel}/prompt.md",
            bundle_output_path=f"{artifact_dir_rel}/bundle-output.md",
            pairs=updated_pairs,
            failure_reason=review_run.failure_reason,
        )
    return completed, failed


def missing_pairs_by_run(
    run_pairs: list[RunPairs],
    parsed: ParsedPairBundle,
) -> dict[int, list[tuple[str, str]]]:
    missing = set(parsed.missing)
    missing_by_run: dict[int, list[tuple[str, str]]] = {}
    for run in run_pairs:
        run_missing = [pair for pair in run.pairs if pair in missing]
        if run_missing:
            missing_by_run[run.review_run_id] = run_missing
    return missing_by_run


def finalize_run_records_from_parsed(
    *,
    db_path: Path,
    run_pairs: list[RunPairs],
    parsed: ParsedPairBundle,
    raw_output: str | None = None,
    telemetry_json: str | None = None,
    debug_log: str | None = None,
    actual_model_id: str | None = None,
) -> tuple[list[int], list[tuple[int, str]]]:
    """Finalize parsed run records without writing filesystem artifacts."""
    completed: list[int] = []
    failed: list[tuple[int, str]] = []
    for run in run_pairs:
        completed_pairs = tuple(pair for pair in run.pairs if pair not in set(parsed.missing))
        has_missing = len(completed_pairs) != len(run.pairs)
        with connect(db_path) as conn:
            try:
                finalize_run_from_pairs(
                    conn,
                    review_run_id=run.review_run_id,
                    pairs=completed_pairs,
                    parsed=parsed,
                    raw_bundle_markdown=raw_output if has_missing else None,
                    telemetry_json=telemetry_json,
                    debug_log=debug_log,
                    actual_model_id=actual_model_id,
                )
            except ValueError as exc:
                conn.commit()
                failed.append((run.review_run_id, str(exc)))
                continue
            conn.commit()
        completed.append(run.review_run_id)

    return completed, failed
