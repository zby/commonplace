"""Batch review sweep using the direct-write review runner.

Selects stale (note, gate) pairs via review_target_selector.select_stale_gates
and runs each bundled note through run_review_bundle.run_bundle, in
parallel worker threads.
"""

from __future__ import annotations

import argparse
import os
import sys
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass
from pathlib import Path

from commonplace.review.paths import GATES_ROOT
from commonplace.review.resolve_gates import resolve_to_gate_ids
from commonplace.review.review_db import resolve_db_path
from commonplace.review.review_target_selector import StaleGate, select_stale_gates
from commonplace.review.executor import UsageExhausted
from commonplace.review.run_review_bundle import run_bundle
from commonplace.review.runners import runner_names


DEFAULT_PARALLELISM = 4


@dataclass(frozen=True)
class SweepJob:
    note_path: str
    gates: tuple[str, ...]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Batch review sweep using the direct-write review runner.",
    )
    parser.add_argument("--model", required=True, help="Model partition to review with.")
    parser.add_argument(
        "--runner",
        choices=runner_names(),
        default="claude-code",
        help="Runner to use for the review bundle command.",
    )
    parser.add_argument("--current", action="store_true", help="Review only notes with frontmatter status=current.")
    parser.add_argument("--all-gates", action="store_true", help="Review all gate bundles.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned review commands without executing them.")
    parser.add_argument(
        "bundle_or_note",
        nargs="*",
        help="Bundle name followed by note paths or directories, unless --all-gates is used.",
    )
    args = parser.parse_args(argv)

    if not args.all_gates and not args.bundle_or_note:
        parser.error("bundle name is required unless --all-gates is set")
    return args


def parallelism_from_env() -> int:
    raw = os.environ.get("REVIEW_SWEEP_JOBS", str(DEFAULT_PARALLELISM))
    if not raw.isdigit() or int(raw) < 1:
        raise SystemExit("error: REVIEW_SWEEP_JOBS must be a positive integer")
    return int(raw)


def bundle_names(select_all_gates: bool, positional: list[str], repo_root: Path) -> tuple[list[str], list[str]]:
    if select_all_gates:
        gates_dir = repo_root / GATES_ROOT
        bundles = sorted(path.name for path in gates_dir.iterdir() if path.is_dir())
        return bundles, positional
    return [positional[0]], positional[1:]


def group_stale_gates(records: list[StaleGate]) -> list[SweepJob]:
    grouped: dict[str, list[str]] = {}
    for record in records:
        grouped.setdefault(record.note_path, []).append(record.gate_id)
    return [
        SweepJob(note_path=note_path, gates=tuple(sorted(gates)))
        for note_path, gates in sorted(grouped.items())
    ]


def collect_sweep_jobs(
    *,
    repo_root: Path,
    model: str,
    bundle: str,
    current_only: bool,
    note_paths: list[str],
) -> list[SweepJob]:
    if current_only and note_paths:
        raise SystemExit("error: --current and explicit note paths are mutually exclusive")
    gates_dir = repo_root / GATES_ROOT
    gate_ids = resolve_to_gate_ids([bundle], gates_dir)
    stale = select_stale_gates(
        repo_root,
        model=model,
        gate_ids=gate_ids,
        note_filter=note_paths or None,
        current_only=current_only,
    )
    return group_stale_gates(stale)


def render_bundle_review_command(*, runner: str, model: str, job: SweepJob) -> str:
    args = ["commonplace-run-review-bundle", "--runner", runner, "--model", model, job.note_path, *job.gates]
    return " ".join(args)


def sweep_bundle(
    *,
    repo_root: Path,
    db_path: Path,
    bundle: str,
    model: str,
    runner: str,
    current_only: bool,
    note_paths: list[str],
    dry_run: bool,
    parallelism: int,
) -> tuple[int, int, bool]:
    """Run one bundle over all stale notes.

    Returns (reviewed_count, failed_count, usage_exhausted).
    """
    jobs = collect_sweep_jobs(
        repo_root=repo_root,
        model=model,
        bundle=bundle,
        current_only=current_only,
        note_paths=note_paths,
    )
    if not jobs:
        return 0, 0, False

    print(f"Bundle '{bundle}': {len(jobs)} notes to review")
    if dry_run:
        for job in jobs:
            print(f"--- Reviewing: {job.note_path} ({' '.join(job.gates)})")
            print(render_bundle_review_command(runner=runner, model=model, job=job))
            print()
        return len(jobs), 0, False

    reviewed = 0
    failed = 0
    pending = list(jobs)
    in_flight: dict = {}

    def _submit(executor: ThreadPoolExecutor, job: SweepJob) -> None:
        print(f"--- Reviewing: {job.note_path} ({' '.join(job.gates)})")
        future = executor.submit(
            run_bundle,
            repo_root=repo_root,
            db_path=db_path,
            note_path=job.note_path,
            gate_or_bundle=list(job.gates),
            runner=runner,
            model=model,
            dry_run=False,
        )
        in_flight[future] = job
        print()

    with ThreadPoolExecutor(max_workers=parallelism) as executor:
        while pending and len(in_flight) < parallelism:
            _submit(executor, pending.pop(0))

        while in_flight:
            done, _ = wait(in_flight, return_when=FIRST_COMPLETED)
            for future in done:
                job = in_flight.pop(future)
                try:
                    status = future.result()
                except UsageExhausted:
                    print(
                        "error: runner reported usage exhausted; aborting sweep immediately.",
                        file=sys.stderr,
                    )
                    for queued in list(in_flight):
                        queued.cancel()
                    return reviewed, failed, True
                if status == 0:
                    reviewed += 1
                else:
                    print(f"  FAILED: {job.note_path}", file=sys.stderr)
                    failed += 1

                if pending:
                    _submit(executor, pending.pop(0))
    return reviewed, failed, False


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    args = parse_args(argv)
    parallelism = parallelism_from_env()
    repo_root = (cwd if cwd is not None else Path.cwd()).resolve()
    db_path = resolve_db_path(repo_root)
    bundles, note_paths = bundle_names(args.all_gates, args.bundle_or_note, repo_root)

    reviewed_total = 0
    failed_total = 0
    for bundle in bundles:
        print(f"=== Bundle: {bundle} ===")
        reviewed, failed, usage_exhausted = sweep_bundle(
            repo_root=repo_root,
            db_path=db_path,
            bundle=bundle,
            model=args.model,
            runner=args.runner,
            current_only=args.current,
            note_paths=note_paths,
            dry_run=args.dry_run,
            parallelism=parallelism,
        )
        reviewed_total += reviewed
        failed_total += failed
        if usage_exhausted:
            return 1
        print()

    print("=== Sweep complete ===")
    print(f"Reviewed: {reviewed_total} notes")
    if failed_total > 0:
        print(f"Failed:   {failed_total} notes")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
