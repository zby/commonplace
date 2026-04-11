"""Library functions for run_gate_sweep.

Pure logic lives here; run_gate_sweep.py is the thin CLI wrapper.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.gate_sweep_format import (
    GateSweepNoteTarget,
    build_gate_sweep_prompt,
    extract_gate_sweep_reviews,
)
from commonplace.review.paths import GATES_ROOT
from commonplace.review.review_db import (
    attach_execution_data,
    connect,
    create_run,
    fail_review_run,
    record_and_finalize_run,
)
from commonplace.review.review_metadata import committed_file_provenance, iso_now, review_note_provenance
from commonplace.review.review_model import normalize_model_id
from commonplace.review.review_runners import run_prompt
from commonplace.review.review_target_selector import select_stale_gates
from commonplace.review.run_review_bundle import (
    bundle_artifact_dir,
    combine_logs,
    model_id_from_telemetry,
    parse_bundle_gate_reviews,
    resolve_note_markdown_links,
    serialize_telemetry,
    write_bundle_artifacts,
)


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
            note_body = frontmatter.strip(note_text).lstrip("\n")
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
            note_body = frontmatter.strip(note_text).lstrip("\n")
            resolved_links, unresolved_links = resolve_note_markdown_links(
                repo_root=repo_root,
                note_abs=note_abs,
                note_body=note_body,
            )
            note_sha, note_commit = review_note_provenance(repo_root, Path(note_path))
            review_run_id = create_run(
                conn,
                note_path=note_path,
                model_id=model_id,
                runner=runner,
                reviewed_note_sha=note_sha,
                reviewed_note_commit=note_commit,
                started_at=started_at,
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
            attach_execution_data(
                conn,
                review_run_id=int(row["id"]),
                telemetry_json=telemetry_json,
                debug_log=debug_log,
            )
            fail_review_run(
                conn,
                review_run_id=int(row["id"]),
                failure_reason=failure_reason,
                completed_at=completed_at,
            )
        conn.commit()


def run_gate_sweep(
    *,
    repo_root: Path,
    db_path: Path,
    gate_id: str,
    runner: str,
    model: str,
    note_paths: list[str] | None,
    current_only: bool,
    batch_size: int,
    dry_run: bool,
) -> int:
    """Run one gate across many notes in batched runner calls.

    Returns a process exit code. Raises ValueError on input/precondition
    errors so the caller can translate them to argparse-style failures.
    """
    runner_model = model
    model = normalize_model_id(model)
    gate_id = gate_id.removesuffix(".md")
    gate_abs = repo_root / GATES_ROOT / f"{gate_id}.md"
    if not gate_abs.is_file():
        raise ValueError(f"gate not found: {gate_id}")
    gate_text = frontmatter.strip(gate_abs.read_text(encoding="utf-8")).lstrip("\n")
    gate_sha, _ = committed_file_provenance(repo_root, gate_abs, kind="gate")

    stale_records = select_stale_gates(
        repo_root,
        model=model,
        gate_ids=[gate_id],
        note_filter=note_paths,
        current_only=current_only,
        include_diff=False,
        db_path=db_path,
    )

    sweep_note_paths = [record.note_path for record in stale_records]
    if not sweep_note_paths:
        print("Reviewed: 0 notes")
        return 0

    batches = chunked(sweep_note_paths, batch_size)
    print(f"Selected: {len(sweep_note_paths)} notes across {len(batches)} batches", file=sys.stderr)

    reviewed = 0
    for batch_index, batch_note_paths in enumerate(batches, start=1):
        prepared = prepare_gate_sweep_targets(
            repo_root=repo_root,
            db_path=db_path,
            note_paths=batch_note_paths,
            gate_id=gate_id,
            gate_sha=gate_sha,
            runner=runner,
            model_id=model,
            persist_runs=not dry_run,
        )
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
            f"{batch_label}: launching {runner} for {len(prepared)} notes",
            file=sys.stderr,
        )
        for item in prepared:
            print(f"  - {item.note_path} (review run id: {item.review_run_id})", file=sys.stderr)

        if dry_run:
            if batch_index > 1:
                print()
                print(f"=== BATCH {batch_index}/{len(batches)} ===")
            print(prompt)
            continue

        review_run_ids = [item.review_run_id for item in prepared]
        try:
            result = run_prompt(runner=runner, prompt=prompt, repo_root=repo_root, model=runner_model)
        except KeyboardInterrupt:
            fail_running_review_runs(
                db_path=db_path,
                review_run_ids=review_run_ids,
                failure_reason="gate sweep interrupted",
            )
            print("gate sweep interrupted", file=sys.stderr)
            return 130

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

        if result.returncode != 0:
            fail_running_review_runs(
                db_path=db_path,
                review_run_ids=review_run_ids,
                failure_reason=f"{runner} exited {result.returncode}",
                debug_log=runner_debug_log,
                telemetry_json=telemetry_json,
            )
            return result.returncode

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
            print(str(exc), file=sys.stderr)
            return 1

        completed_in_batch = 0
        for index, item in enumerate(prepared):
            note_bundle = build_note_local_bundle(
                note_path=item.note_path,
                gate_id=gate_id,
                review_run_id=item.review_run_id,
                review_text=parsed_reviews[item.note_path],
            )
            artifact_dir = bundle_artifact_dir(repo_root, item.review_run_id)
            write_bundle_artifacts(artifact_dir=artifact_dir, raw_bundle_markdown=note_bundle)
            try:
                canonical_bundle_markdown, gate_reviews, canonical_reviews = parse_bundle_gate_reviews(
                    note_bundle,
                    expected_gate_ids=[gate_id],
                )
            except ValueError as exc:
                with connect(db_path) as conn:
                    attach_execution_data(
                        conn,
                        review_run_id=item.review_run_id,
                        telemetry_json=telemetry_json,
                        raw_bundle_markdown=note_bundle,
                        debug_log=runner_debug_log,
                    )
                    fail_review_run(
                        conn,
                        review_run_id=item.review_run_id,
                        failure_reason=str(exc),
                        completed_at=iso_now(),
                    )
                    conn.commit()
                remaining_ids = [remaining.review_run_id for remaining in prepared[index + 1 :]]
                fail_running_review_runs(
                    db_path=db_path,
                    review_run_ids=remaining_ids,
                    failure_reason=f"gate sweep aborted after {item.note_path}: {exc}",
                    debug_log=runner_debug_log,
                    telemetry_json=telemetry_json,
                )
                print(str(exc), file=sys.stderr)
                return 1
            write_bundle_artifacts(
                artifact_dir=artifact_dir,
                raw_bundle_markdown=canonical_bundle_markdown,
                parsed_reviews=canonical_reviews,
            )
            with connect(db_path) as conn:
                attach_execution_data(
                    conn,
                    review_run_id=item.review_run_id,
                    telemetry_json=telemetry_json,
                    raw_bundle_markdown=canonical_bundle_markdown,
                    debug_log=runner_debug_log,
                )
                try:
                    record_and_finalize_run(
                        conn,
                        review_run_id=item.review_run_id,
                        gate_reviews=gate_reviews,
                        actual_model_id=actual_review_model,
                    )
                except ValueError as exc:
                    conn.commit()
                    remaining_ids = [remaining.review_run_id for remaining in prepared[index + 1 :]]
                    fail_running_review_runs(
                        db_path=db_path,
                        review_run_ids=remaining_ids,
                        failure_reason=f"gate sweep aborted after {item.note_path}: {exc}",
                        debug_log=runner_debug_log,
                        telemetry_json=telemetry_json,
                    )
                    print(str(exc), file=sys.stderr)
                    return 1
                conn.commit()
            completed_in_batch += 1

        reviewed += completed_in_batch
        print(f"Batch {batch_index}/{len(batches)}: reviewed {completed_in_batch} notes")

    if not dry_run:
        print(f"Reviewed: {reviewed} notes")
    return 0
