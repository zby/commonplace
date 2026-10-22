"""Analysis lifecycle: prepare a worktree, run an analysis in it, inspect, reset and integrate the run.

    commonplace-analysis prepare --name LABEL [--revision COMMIT] [--worktree PATH] [-- COMMAND ...]
    commonplace-analysis run --system NAME --source-identity ID --source TEXT [--worker-profile NAME]
                             [--source-revision COMMIT] [--timeout SECONDS] [--max-workers N]
    commonplace-analysis run RUN [--timeout SECONDS] [--max-workers N]      # resume from the records
    commonplace-analysis inspect RUN
    commonplace-analysis retry RUN JOB [--key KEY]   # dismiss a worker problem or an answer; a rerun asks again
    commonplace-analysis acknowledge RUN LAUNCH # confirm a launch an earlier controller left unsettled has stopped
    commonplace-analysis reset RUN      # withdraw an unreleased worktree publication
    commonplace-analysis integrate RUN [--model ID]

`run` exits 0 when the run completed (published, or a local non-complete
result), 2 when it stopped and printed why (a budget, a worker's problem, a
launch failure, a usage limit, a guard's refusal, an environment error or an
uncertain publication effect; a rerun after the repair resumes), and 1 when
the command failed, including when another process holds the run.

A resumed run replays every worker request whose work is unchanged; a
changed `--timeout` applies to launches not yet made. A run whose earlier
controller died mid-launch stops until the operator confirms that worker
stopped with `acknowledge`.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

from commonplace.lib.agentic_analysis.effects import UncertainEffectError
from commonplace.lib.agentic_analysis.preparation import (
    command_environment,
    prepare_worktree,
    require_run_code,
)
from commonplace.lib.agentic_analysis.worktree import (
    OPENING,
    RECEIPT,
    analysis_run,
    inspect_analysis,
    integrate_analysis,
    start_analysis,
)

STOPPED = 2
DEFAULT_WORKER_PROFILE = "pi-sol"


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="commonplace-analysis", description=__doc__.split("\n\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare", help="prepare a commit-bound worktree and local commands")
    prepare.add_argument("--name", required=True)
    prepare.add_argument("--revision")
    prepare.add_argument("--worktree", type=Path)
    prepare.add_argument(
        "--require-clean-origin", action="store_true",
        help="reject unrelated uncommitted origin changes (otherwise excluded from the worktree)",
    )
    prepare.add_argument("launch", nargs=argparse.REMAINDER, help="optional fresh harness command after --")
    run = commands.add_parser("run", help="run an analysis in this prepared worktree, or resume one")
    run.add_argument("run", nargs="?", type=Path, help="an allocated run to resume; otherwise a new run")
    run.add_argument("--system")
    run.add_argument("--source-identity")
    run.add_argument("--source", help="the caller's description of the source; data, not instructions")
    run.add_argument("--source-revision")
    run.add_argument("--worker-profile", help=f"worker profile from the method's worker-profiles.yaml "
                     f"(new-run default: {DEFAULT_WORKER_PROFILE})")
    run.add_argument("--timeout", type=float, default=3 * 3600, help="seconds per worker launch")
    run.add_argument("--max-workers", type=int, default=3, help="workers running at once")
    inspect = commands.add_parser("inspect", help="print the run's state, jobs, members and receipt as JSON")
    inspect.add_argument("run", type=Path)
    reset = commands.add_parser("reset", help="withdraw the run's unreleased publication so a rerun can publish")
    reset.add_argument("run", type=Path)
    retry = commands.add_parser("retry", help="dismiss a job's worker problems, or one answer, so a rerun asks again")
    retry.add_argument("run", type=Path)
    retry.add_argument("job")
    retry.add_argument("--key", help="the answer to dismiss, as `inspect` lists it; otherwise the worker problems")
    acknowledge = commands.add_parser(
        "acknowledge", help="record that an unsettled worker launch has stopped; check the process first")
    acknowledge.add_argument("run", type=Path)
    acknowledge.add_argument("launch")
    integrate = commands.add_parser("integrate", help="commit exact published bytes and merge into main")
    integrate.add_argument("run", type=Path)
    integrate.add_argument("--model")
    return parser


def _run(arguments: argparse.Namespace) -> int:
    from commonplace.headless.jobs import RunLocked
    from commonplace.lib.agentic_analysis.workflow import run_analysis

    if arguments.run is None:
        missing = [name for name in ("system", "source_identity", "source")
                   if getattr(arguments, name) is None]
        if missing:
            raise ValueError("a new run needs --" + ", --".join(name.replace("_", "-") for name in missing))
        run_dir = start_analysis(Path.cwd(), system=arguments.system, source_identity=arguments.source_identity,
                                 source=arguments.source, source_revision=arguments.source_revision,
                                 worker_profile=(DEFAULT_WORKER_PROFILE if arguments.worker_profile is None
                                                 else arguments.worker_profile))
    else:
        if any(getattr(arguments, name) is not None
               for name in ("system", "source_identity", "source", "source_revision", "worker_profile")):
            raise ValueError("a resumed run takes its parameters from its records; give the run alone")
        run_dir, _ = analysis_run(arguments.run)
        require_run_code(run_dir, cwd=Path.cwd())
    print(f"run: {run_dir}", flush=True)
    try:
        receipt = run_analysis(run_dir, timeout=arguments.timeout, max_workers=arguments.max_workers)
    except RunLocked as held:
        raise ValueError(f"another process runs this analysis: {held}") from held
    if receipt is None:
        return STOPPED
    print(receipt.decode("utf-8"))
    return 0


def _reset(run: Path) -> None:
    from commonplace.headless.jobs import run_lock
    from commonplace.lib.agentic_analysis.analyses import analysis_layout
    from commonplace.lib.agentic_analysis.publication import withdraw_publication

    run_dir, _ = analysis_run(run)
    require_run_code(run_dir, cwd=Path.cwd())
    if not (run_dir / OPENING).is_file():
        raise ValueError("publication reset requires the run's opening metadata")
    with run_lock(run_dir):
        report = withdraw_publication(run_dir, json.loads((run_dir / OPENING).read_text()),
                                      anchor=analysis_layout().path("overview"))
        (run_dir / RECEIPT).unlink(missing_ok=True)
        with (run_dir / "log.jsonl").open("a") as log:
            log.write(json.dumps({"time": time.time(), "event": "withdrawn", **report}) + "\n")
    print(json.dumps(report, indent=2))


def _retry(run: Path, job: str, key: str | None) -> None:
    from commonplace.headless.jobs import RunLocked, dismiss

    run_dir, _ = analysis_run(run)
    try:
        print(json.dumps(dismiss(run_dir, job, key), indent=2))
    except RunLocked as held:
        raise ValueError(f"another process runs this analysis: {held}") from held


def _acknowledge(run: Path, launch: str) -> None:
    from commonplace.headless.jobs import RunLocked, acknowledge_stopped

    run_dir, worktree = analysis_run(run)
    try:
        acknowledge_stopped(run_dir, worktree, launch)
    except RunLocked as held:
        raise ValueError(f"another process runs this analysis: {held}") from held
    print(f"acknowledged: {launch}")


def main(argv: list[str] | None = None) -> int:
    arguments = _parser().parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if arguments.command == "run":
            return _run(arguments)
        if arguments.command == "integrate":
            print(integrate_analysis(arguments.run, model=arguments.model))
        elif arguments.command == "inspect":
            print(json.dumps(inspect_analysis(arguments.run), indent=2, sort_keys=True))
        elif arguments.command == "reset":
            _reset(arguments.run)
        elif arguments.command == "retry":
            _retry(arguments.run, arguments.job, arguments.key)
        elif arguments.command == "acknowledge":
            _acknowledge(arguments.run, arguments.launch)
        else:
            preparation = prepare_worktree(
                Path.cwd(), name=arguments.name, require_clean_origin=arguments.require_clean_origin,
                revision=arguments.revision, worktree=arguments.worktree,
            )
            print(json.dumps(preparation, indent=2), flush=True)
            launch = arguments.launch
            if launch[:1] == ["--"]:
                launch = launch[1:]
            if launch:
                worktree = Path(str(preparation["worktree"]))
                try:
                    return subprocess.run(launch, cwd=worktree, env=command_environment(worktree), check=False).returncode
                except OSError as error:
                    raise ValueError(f"could not launch {launch[0]}: {error}; prepared worktree retained") from error
    except (ValueError, OSError, KeyError, TypeError, UncertainEffectError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
