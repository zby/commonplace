"""Run note-local review bundles through a subprocess runner."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.review.batch import prepare_grouped_review_job
from commonplace.review.executor import UsageExhausted, prepare_note_target
from commonplace.review.gate_packing import GateBundleGroup, group_requested_gates_by_bundle
from commonplace.review.protocol.prompt import render_pairs_prompt
from commonplace.review.review_db import ensure_db
from commonplace.review.review_model import normalize_model_partition
from commonplace.review.run_review_jobs import run_review_jobs


@dataclass(frozen=True)
class RunBundlesOutcome:
    exit_code: int
    stdout: str = ""
    stderr: str = ""


def _dry_run_prompt(
    *,
    repo_root: Path,
    note_path: str,
    group: GateBundleGroup,
) -> str:
    target = prepare_note_target(
        repo_root=repo_root,
        note_path=note_path,
        review_job_id=0,
        gate_paths=tuple(group.gate_paths),
    )
    gate_texts = {
        gate_path: frontmatter.strip((repo_root / gate_path).read_text(encoding="utf-8")).lstrip("\n")
        for gate_path in group.gate_paths
    }
    return render_pairs_prompt(notes=[target], gate_texts=gate_texts)


def _append_line(text: str, line: str) -> str:
    return text + line + "\n"


def _run_group(
    *,
    repo_root: Path,
    db_path: Path,
    note_path: str,
    group: GateBundleGroup,
    runner: str,
    runner_model: str,
    model_partition: str,
    dry_run: bool,
) -> RunBundlesOutcome:
    if dry_run:
        prompt = _dry_run_prompt(repo_root=repo_root, note_path=note_path, group=group)
        return RunBundlesOutcome(
            exit_code=0,
            stdout=f"=== Bundle: {group.bundle} ===\n{prompt}\n\n",
        )

    prepared = prepare_grouped_review_job(
        repo_root=repo_root,
        db_path=db_path,
        pairs=[(note_path, gate_path) for gate_path in group.gate_paths],
        packing="note",
        runner=None,
        model_partition=model_partition,
    )
    payload, status = run_review_jobs(
        repo_root=repo_root,
        db_path=db_path,
        runner=runner,
        model=runner_model,
        review_job_id=prepared.review_job_id,
    )

    stderr = ""
    for job in payload.get("jobs", []):
        if not isinstance(job, dict):
            continue
        if job.get("failure_reason"):
            stderr = _append_line(stderr, str(job["failure_reason"]))
    if payload.get("usage_exhausted"):
        raise UsageExhausted()
    if status != 0:
        return RunBundlesOutcome(exit_code=status, stderr=stderr)
    return RunBundlesOutcome(
        exit_code=0,
        stdout=f"completed {prepared.review_job_id} {len(group.gate_paths)}\n",
        stderr=stderr,
    )


def run_bundles(
    *,
    repo_root: Path,
    db_path: Path,
    note_path: str,
    gate_or_bundle: list[str],
    runner: str,
    model: str,
    dry_run: bool,
) -> RunBundlesOutcome:
    """Run requested gates as one subprocess call per bundle/lens."""
    runner_model = model
    model_partition = normalize_model_partition(model)
    groups = group_requested_gates_by_bundle(
        repo_root=repo_root,
        note_path=note_path,
        gate_or_bundle=gate_or_bundle,
    )

    if not dry_run:
        ensure_db(db_path)

    stdout = ""
    stderr = ""
    for group in groups:
        outcome = _run_group(
            repo_root=repo_root,
            db_path=db_path,
            note_path=note_path,
            group=group,
            runner=runner,
            runner_model=runner_model,
            model_partition=model_partition,
            dry_run=dry_run,
        )
        stdout += outcome.stdout
        stderr += outcome.stderr
        if outcome.exit_code != 0:
            return RunBundlesOutcome(exit_code=outcome.exit_code, stdout=stdout, stderr=stderr)
    return RunBundlesOutcome(exit_code=0, stdout=stdout, stderr=stderr)
