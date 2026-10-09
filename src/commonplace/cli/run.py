"""`commonplace-run`: start and advance a run directory, and judge from the command line.

    commonplace-run start RUN PLAN.yaml [--param key=value ...]
    commonplace-run advance RUN [--completed ATTEMPT ...] [--failed ATTEMPT=REASON ...]
                                [--model ID] [--effort LEVEL] [--json]
    commonplace-run status RUN [--json]          # also re-prints open hand-outs
    commonplace-run judge RUN --role ROLE --outcome accepted|refused
                          [--version V] [--scope RELATION ...] [--findings TEXT]
                          [--override JUDGMENT_ID ...] [--basis ROLE ...]

The engine behind these is `commonplace.artifactrun`; its design is in
kb/work/workflow-requirements/. `advance` prints the hand-outs a coordinator
must run and reports back with the next `advance`.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

from commonplace.artifactrun import (
    AttemptResult,
    PlanError,
    RunStatus,
    Stop,
    advance,
    inspect,
    judge,
    open_handouts,
    start_run,
)
from commonplace.artifactrun.worktree import require_run_code


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="commonplace-run", description=__doc__.split("\n\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)

    start = commands.add_parser("start", help="start a run from a plan")
    start.add_argument("run", type=Path)
    start.add_argument("plan", type=Path)
    start.add_argument("--param", action="append", default=[], metavar="KEY=VALUE")

    step = commands.add_parser("advance", help="close reported attempts, run code jobs, hand out model jobs")
    step.add_argument("run", type=Path)
    step.add_argument("--completed", action="append", default=[], metavar="ATTEMPT")
    step.add_argument("--failed", action="append", default=[], metavar="ATTEMPT=REASON")
    step.add_argument("--model", help="worker model identity for the reported attempts")
    step.add_argument("--effort", help="worker effort for the reported attempts")
    step.add_argument("--json", action="store_true")

    status = commands.add_parser("status", help="members, open attempts, refusals in force, publishability")
    status.add_argument("run", type=Path)
    status.add_argument("--json", action="store_true")

    verdict = commands.add_parser("judge", help="record an operator judgment of a role's member")
    verdict.add_argument("run", type=Path)
    verdict.add_argument("--role", required=True)
    verdict.add_argument("--outcome", required=True, choices=("accepted", "refused"))
    verdict.add_argument("--version", help="an earlier version to judge as evidence; default: the member")
    verdict.add_argument("--scope", action="append", default=[], metavar="ORIGIN:KIND:PARTNER")
    verdict.add_argument("--findings", default="")
    verdict.add_argument("--override", action="append", default=[], metavar="JUDGMENT_ID")
    verdict.add_argument("--basis", action="append", default=[], metavar="ROLE")
    return parser


def _pairs(items: list[str], what: str) -> dict[str, str]:
    pairs = {}
    for item in items:
        key, separator, value = item.partition("=")
        if not separator or not key:
            raise ValueError(f"{what} must read KEY=VALUE, not {item!r}")
        pairs[key] = value
    return pairs


def _print_stop(stop: Stop) -> None:
    where = " ".join(part for part in (stop.job, stop.attempt) if part)
    label = "uncertain effect" if stop.uncertain else "stop"
    print(f"{label} {where}: {stop.reason}")


def _print_status(status: RunStatus, as_json: bool) -> None:
    if as_json:
        print(json.dumps(asdict(status), default=str, indent=1))
        return
    for handout in status.handouts:
        print(f"hand-out {handout.attempt} {handout.job}")
        print(f"  prompt: {handout.prompt}")
        for name, path in handout.outputs.items():
            print(f"  output {name}: {path}")
        print(f"  problem: {handout.problem}")
        print(f"  worker-model: {handout.worker_model}")
    if status.open_attempts:
        print("open: " + " ".join(status.open_attempts))
    for stop in status.stops:
        _print_stop(stop)
    print(f"publishable: {'yes' if status.publishable else 'no'}")


def _print_inspection(view: dict, as_json: bool) -> None:
    if as_json:
        print(json.dumps({**view, "refusals": [asdict(r) for r in view["refusals"]],
                          "failed_attempts": [asdict(s) for s in view["failed_attempts"]],
                          "handouts": [asdict(h) for h in view["handouts"]]}, default=str, indent=1))
        return
    for role, version in view["members"].items():
        print(f"member {role}: {version[:12]}")
    for handout in view["handouts"]:
        print(f"open hand-out {handout.attempt} {handout.job}: {handout.prompt}")
    for stop in view["failed_attempts"]:
        _print_stop(stop)
    for refusal in view["refusals"]:
        first = refusal.findings.strip().splitlines()[:1]
        print(f"refusal {refusal.id} of {refusal.job} ({refusal.version[:12]}): {first[0] if first else ''}")
    print(f"publishable: {'yes' if view['publishable'] else 'no'}")


def main(argv: list[str] | None = None) -> int:
    arguments = _parser().parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if arguments.command != "status":
            require_run_code(arguments.run, cwd=Path.cwd())
        if arguments.command == "start":
            start_run(arguments.run, arguments.plan, parameters=_pairs(arguments.param, "--param"))
            print(f"started {arguments.run}")
        elif arguments.command == "advance":
            results = [AttemptResult(a, model=arguments.model, effort=arguments.effort) for a in arguments.completed]
            results += [AttemptResult(a, outcome="failed", reason=reason, model=arguments.model, effort=arguments.effort)
                        for a, reason in _pairs(arguments.failed, "--failed").items()]
            _print_status(advance(arguments.run, results=tuple(results)), arguments.json)
        elif arguments.command == "status":
            view = inspect(arguments.run)
            view["handouts"] = open_handouts(arguments.run)
            _print_inspection(view, arguments.json)
        else:
            identifier = judge(
                arguments.run, role=arguments.role, outcome=arguments.outcome, version=arguments.version,
                scope=tuple(arguments.scope), findings=arguments.findings,
                overrides=tuple(arguments.override), basis=tuple(arguments.basis),
            )
            print(f"recorded {identifier}")
    except (ValueError, OSError, PlanError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
