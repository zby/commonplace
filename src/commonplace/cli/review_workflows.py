"""Review notes against criteria with headless workers, keeping one result file per pair.

    commonplace-review status [NOTES... [--criteria C...]] [--outcome O...] [--fresh | --stale] [--json]
    commonplace-review run gates NOTES... (--criteria C... | --all-gates) [--profile NAME]
                                 [--max-workers N] [--timeout SECONDS] [--force] [--resume RUN_DIR]
    commonplace-review retry RUN JOB [--key KEY]   # dismiss a worker problem or an answer; a rerun asks again
    commonplace-review acknowledge RUN LAUNCH      # confirm a launch an earlier controller left unsettled has stopped

NOTES are files or directories (a directory means its reviewable notes, not
recursively). C are gate ids, bundle names or the lenses `type`, `collection`
and `critique`. `status` without `--criteria` covers all gates (critique stays
opt-in); `run gates` launches one worker per stale pair, so it takes all gates
only when asked with `--all-gates`.

`status` with NOTES shows each applicable pair, including pairs never
reviewed (`missing`); without NOTES it shows every stored result whose note
and criterion still exist. `--outcome` keeps the rows whose stored outcome is
one of those given, `--fresh` the rows with a fresh result, and `--stale` the
rows without one (stale or missing): `--fresh --outcome warn` lists the
current warnings, `--stale` what a sweep would ask. Orphaned results, whose
note or criterion is gone, are listed apart and are not filtered; removing
one is deleting its file. `--json` gives each row's result file, so a fixer
can read the finding.

`run gates` opens a new run under kb/reports/state/review/runs/<UTC stamp>/,
or continues RUN_DIR with `--resume`, which replays the calls whose work is
unchanged; give the same NOTES and criteria again. It prints a JSON report and
exits 0 only when every pair has a current result and the checkout guard saw
no change, 1 otherwise, and 2 when the command failed. A pair whose result
was written is fresh, so a rerun after `retry` of its answer needs `--force`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import asdict
from pathlib import Path

from commonplace.headless.harness import HARNESSES, Profile
from commonplace.headless.jobs import RunLocked, acknowledge_stopped, dismiss
from commonplace.lib.review_workflows import gates, results
from commonplace.lib.tasks import load_profile

SWEEP = "sweep.json"
"""The run's profile, recorded when it opens, so a resumed run asks the same worker."""


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="commonplace-review", description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    status = commands.add_parser("status", help="show each pair's freshness and stored outcome; launches nothing")
    status.add_argument("notes", nargs="*", help="notes or directories; without them, every stored result")
    status.add_argument("--criteria", nargs="+", help="with NOTES: gate ids, bundles or lenses (default: all gates)")
    status.add_argument("--outcome", nargs="+", action="extend", choices=results.OUTCOMES,
                        help="keep rows whose stored outcome is one of these")
    freshness = status.add_mutually_exclusive_group()
    freshness.add_argument("--fresh", action="store_true", help="keep rows with a fresh result")
    freshness.add_argument("--stale", action="store_true", help="keep rows without a fresh result (stale or missing)")
    status.add_argument("--json", action="store_true")
    run = commands.add_parser("run", help="run a review workflow")
    workflows = run.add_subparsers(dest="workflow", required=True)
    sweep = workflows.add_parser("gates", help="review each pair without a fresh result")
    sweep.add_argument("notes", nargs="+")
    chosen = sweep.add_mutually_exclusive_group(required=True)
    chosen.add_argument("--criteria", nargs="+")
    chosen.add_argument("--all-gates", action="store_true", help="every bundle plus `type` and `collection`")
    sweep.add_argument("--profile", help=f"worker profile from the library's {gates.PROFILES_REL} "
                       "(default: its `default`)")
    sweep.add_argument("--max-workers", type=int, default=4, help="workers running at once")
    sweep.add_argument("--timeout", type=float, help="seconds a launch may take")
    sweep.add_argument("--force", action="store_true", help="review fresh pairs too")
    sweep.add_argument("--resume", type=Path, help="continue this run directory instead of opening a new one")
    retry = commands.add_parser("retry", help="dismiss a job's worker problems, or one answer, so a rerun asks again")
    retry.add_argument("run", type=Path)
    retry.add_argument("job", help="the pair's job name, `<note>::<criterion-id>`")
    retry.add_argument("--key", help="the answer to dismiss; otherwise the worker problems")
    acknowledge = commands.add_parser(
        "acknowledge", help="record that an unsettled worker launch has stopped; check the process first")
    acknowledge.add_argument("run", type=Path)
    acknowledge.add_argument("launch")
    return parser


def _root() -> Path:
    return Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True,
                               text=True).stdout.strip())


def _pairs(root: Path, arguments: argparse.Namespace) -> list[gates.Pair]:
    return gates.pairs(root, gates.note_paths(root, arguments.notes), arguments.criteria)


def _keep(row: results.Row, arguments: argparse.Namespace) -> bool:
    fresh = row.freshness.state == "fresh"
    return ((not arguments.outcome or row.outcome in arguments.outcome)
            and not (arguments.fresh and not fresh) and not (arguments.stale and fresh))


def _status(root: Path, arguments: argparse.Namespace) -> int:
    if arguments.notes:
        rows = results.status(root, [(pair.note, pair.criterion) for pair in _pairs(root, arguments)])
        orphans = results.orphaned(root)
    elif arguments.criteria:
        raise ValueError("--criteria needs NOTES")
    else:
        rows, orphans = results.stored(root)
    rows = [row for row in rows if _keep(row, arguments)]
    orphans = [path.relative_to(root).as_posix() for path in orphans]
    if arguments.json:
        print(json.dumps({"pairs": [{"note": row.note, "criterion": row.criterion,
                                     "criterion-id": results.criterion_id(root, row.criterion),
                                     "freshness": row.freshness.state, "changed": list(row.freshness.changed),
                                     "outcome": row.outcome, "model": row.model,
                                     "result": row.path.relative_to(root).as_posix() if row.path else None}
                                    for row in rows],
                          "orphaned": orphans}, indent=2))
        return 0
    for row in rows:
        state = row.freshness.state + (f" ({', '.join(row.freshness.changed)})" if row.freshness.changed else "")
        print(f"{row.note}  {results.criterion_id(root, row.criterion)}  {state}  "
              f"{row.outcome or '-'}  {row.model or '-'}")
    for orphan in orphans:
        print(f"orphaned  {orphan}")
    return 0


def _run_dir(root: Path, resume: Path | None) -> Path:
    if resume is not None:
        run_dir = (root / resume).resolve()
        if not (run_dir / SWEEP).is_file():
            raise ValueError(f"not a review run: {resume}")
        return run_dir
    stamp = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime())
    for suffix in ("", *(f"-{n}" for n in range(2, 100))):
        run_dir = root / gates.RUNS / f"{stamp}{suffix}"
        try:
            run_dir.mkdir(parents=True)
        except FileExistsError:
            continue
        return run_dir
    raise ValueError(f"no free run directory for {stamp}")


def _profile(root: Path, run_dir: Path, name: str | None, resumed: bool) -> Profile:
    if resumed:
        recorded = Profile(**json.loads((run_dir / SWEEP).read_text(encoding="utf-8"))["profile"])
        if name is not None and load_profile(root, name, gates.profiles()) != recorded:
            raise ValueError(f"the run was opened with another profile: {recorded}")
        return recorded
    profile = load_profile(root, name, gates.profiles())
    (run_dir / SWEEP).write_text(json.dumps({"profile": asdict(profile)}, indent=2), encoding="utf-8")
    return profile


def _gates(root: Path, arguments: argparse.Namespace, harnesses) -> int:
    wanted = _pairs(root, arguments)
    run_dir = _run_dir(root, arguments.resume)
    profile = _profile(root, run_dir, arguments.profile, arguments.resume is not None)
    report = gates.sweep(root, wanted, profile, run_dir, max_workers=arguments.max_workers,
                         timeout=arguments.timeout, force=arguments.force, harnesses=harnesses)
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 1


def main(argv: list[str] | None = None, *, harnesses=HARNESSES) -> int:
    """Run the command; `harnesses` lets tests substitute a fake worker."""
    arguments = _parser().parse_args(sys.argv[1:] if argv is None else argv)
    try:
        root = _root().resolve()
        if arguments.command == "status":
            return _status(root, arguments)
        if arguments.command == "run":
            return _gates(root, arguments, harnesses)
        run_dir = (root / arguments.run).resolve()
        if arguments.command == "retry":
            print(json.dumps(dismiss(run_dir, arguments.job, arguments.key), indent=2))
        else:
            acknowledge_stopped(run_dir, root, arguments.launch)
            print(f"acknowledged: {arguments.launch}")
    except RunLocked as held:
        print(f"commonplace-review: another process runs this review: {held}", file=sys.stderr)
        return 2
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"commonplace-review: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
