from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass
from pathlib import Path


GATES_DIR = Path("kb/instructions/review-gates")
USAGE_EXHAUSTION_TEXT = "out of extra usage"
USAGE_EXHAUSTED_EXIT_CODE = 99
DEFAULT_PARALLELISM = 4
SELECTOR_COMMAND = "commonplace-review-target-selector"
BUNDLE_COMMAND = "commonplace-run-review-bundle"


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
        choices=["claude-code", "codex"],
        default="claude-code",
        help="Runner to use for the review bundle command.",
    )
    parser.add_argument("--current", action="store_true", help="Review only notes with frontmatter status=current.")
    parser.add_argument("--all-gates", action="store_true", help="Review all gate bundles.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned review commands without executing them.")
    parser.add_argument(
        "bundle_or_note",
        nargs="*",
        help="Bundle name followed by optional note paths, unless --all-gates is used.",
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


def bundle_names(select_all_gates: bool, positional: list[str]) -> tuple[list[str], list[str]]:
    if select_all_gates:
        bundles = sorted(path.name for path in GATES_DIR.iterdir() if path.is_dir())
        return bundles, positional
    return [positional[0]], positional[1:]


def load_selector_output(
    *,
    model: str,
    bundle: str,
    current_only: bool,
    note_paths: list[str],
) -> list[dict[str, str]]:
    if current_only and note_paths:
        raise SystemExit("error: --current and explicit note paths are mutually exclusive")

    args = [SELECTOR_COMMAND, "--model", model, bundle, "--json"]
    if current_only:
        args.append("--current")
    elif note_paths:
        args.extend(["--note", *note_paths])

    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.stdout:
        print(result.stdout, end="")
    if result.returncode != 0:
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        raise SystemExit(result.returncode)
    return json.loads(result.stdout or "[]")


def group_selector_output(records: list[dict[str, str]]) -> list[SweepJob]:
    grouped: dict[str, list[str]] = {}
    for entry in records:
        grouped.setdefault(entry["note_path"], []).append(entry["gate_id"])
    return [
        SweepJob(note_path=note_path, gates=tuple(sorted(gates)))
        for note_path, gates in sorted(grouped.items())
    ]


def render_bundle_review_command(*, runner: str, model: str, job: SweepJob) -> str:
    args = [BUNDLE_COMMAND, "--runner", runner, "--model", model, job.note_path, *job.gates]
    return " ".join(args)


def run_bundle_review(*, runner: str, model: str, job: SweepJob) -> int:
    result = subprocess.run(
        [BUNDLE_COMMAND, "--runner", runner, "--model", model, job.note_path, *job.gates],
        capture_output=True,
        text=True,
        check=False,
    )
    output = f"{result.stdout}{result.stderr}"
    if output:
        print(output, end="")
    if USAGE_EXHAUSTION_TEXT in output.lower():
        print("error: claude reported extra usage exhaustion; aborting sweep immediately.", file=sys.stderr)
        return USAGE_EXHAUSTED_EXIT_CODE
    return result.returncode


def sweep_bundle(
    *,
    bundle: str,
    model: str,
    runner: str,
    current_only: bool,
    note_paths: list[str],
    dry_run: bool,
    parallelism: int,
) -> tuple[int, int]:
    jobs = group_selector_output(
        load_selector_output(model=model, bundle=bundle, current_only=current_only, note_paths=note_paths)
    )
    if not jobs:
        return 0, 0

    print(f"Bundle '{bundle}': {len(jobs)} notes to review")
    if dry_run:
        for job in jobs:
            print(f"--- Reviewing: {job.note_path} ({' '.join(job.gates)})")
            print(render_bundle_review_command(runner=runner, model=model, job=job))
            print()
        return len(jobs), 0

    reviewed = 0
    failed = 0
    pending = list(jobs)
    in_flight = {}
    with ThreadPoolExecutor(max_workers=parallelism) as executor:
        while pending and len(in_flight) < parallelism:
            job = pending.pop(0)
            print(f"--- Reviewing: {job.note_path} ({' '.join(job.gates)})")
            future = executor.submit(run_bundle_review, runner=runner, model=model, job=job)
            in_flight[future] = job
            print()

        while in_flight:
            done, _ = wait(in_flight, return_when=FIRST_COMPLETED)
            for future in done:
                job = in_flight.pop(future)
                status = future.result()
                if status == 0:
                    reviewed += 1
                elif status == USAGE_EXHAUSTED_EXIT_CODE:
                    for queued in in_flight:
                        queued.cancel()
                    return reviewed, USAGE_EXHAUSTED_EXIT_CODE
                else:
                    print(f"  FAILED: {job.note_path}", file=sys.stderr)
                    failed += 1

                if pending:
                    next_job = pending.pop(0)
                    print(f"--- Reviewing: {next_job.note_path} ({' '.join(next_job.gates)})")
                    future = executor.submit(run_bundle_review, runner=runner, model=model, job=next_job)
                    in_flight[future] = next_job
                    print()
    return reviewed, failed


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    parallelism = parallelism_from_env()
    bundles, note_paths = bundle_names(args.all_gates, args.bundle_or_note)

    reviewed_total = 0
    failed_total = 0
    for bundle in bundles:
        print(f"=== Bundle: {bundle} ===")
        reviewed, failed = sweep_bundle(
            bundle=bundle,
            model=args.model,
            runner=args.runner,
            current_only=args.current,
            note_paths=note_paths,
            dry_run=args.dry_run,
            parallelism=parallelism,
        )
        if failed == USAGE_EXHAUSTED_EXIT_CODE:
            return 1
        reviewed_total += reviewed
        failed_total += failed
        print()

    print("=== Sweep complete ===")
    print(f"Reviewed: {reviewed_total} notes")
    if failed_total > 0:
        print(f"Failed:   {failed_total} notes")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
