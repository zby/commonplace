"""Start a code-scheduled run, advance it, or record an observation about it.

The shell is installed as the `commonplace-workflow` command. It parses
arguments and prints. Everything it does is a call on an
Orchestrator.

    start <package.module:ClassName> [--run <run>] [--param KEY=VALUE ...]
    step <run>
    report <run> <event> [--job NAME] [--text TEXT]
    resolve <run> <effect> completed|absent
    release <run> <subject>

`resolve` and `release` are for the operator: the first after an uncertain
outcome or an effect out of step with its inputs, the second after a block
that permits only stopping.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from commonplace.workflow_legacy.engine import (
    REPORT_EVENTS,
    Blocked,
    Done,
    Launch,
    Orchestrator,
    Recognition,
    RunBusy,
    StateError,
    StepResult,
    Uncertain,
)

STOP_TEXT = "stop and report to the operator"


def render(result: StepResult) -> str:
    """The text the agent orchestrator reads after a step.

    The first line is the outcome: `launch`, `done`, `blocked` or `uncertain`.
    A launch has one line per job, naming its prompt file between backticks,
    followed by the job's launch parameters. A blocked outcome names each
    record file and what is permitted; it points to the details and does not
    repeat them.
    """
    if isinstance(result, Done):
        return "done"
    if isinstance(result, Launch):
        lines = ["launch"]
        for job in result.jobs:
            line = f"- {job.name}: `{job.prompt_path}`"
            if job.launch:
                line += f" launch={json.dumps(dict(job.launch), sort_keys=True)}"
            lines.append(line)
        return "\n".join(lines)
    if isinstance(result, Blocked):
        lines = ["blocked"]
        for block in result.blocks:
            lines += [
                f"- {block.subject}: {block.reason}",
                f"  record: {block.record_path}",
            ]
            if block.permitted == "repair":
                lines.append(f"  permitted: repair within this scope: {block.scope}")
            else:
                lines.append(f"  permitted: {STOP_TEXT}")
        return "\n".join(lines)
    if isinstance(result, Uncertain):
        lines = [
            "uncertain",
            f"- effect {result.effect}: {result.detail}",
            f"  permitted: {STOP_TEXT}; the operator establishes what took place",
        ]
        for block in result.blocks:
            lines += [
                f"- also {block.subject}: {block.reason}",
                f"  record: {block.record_path}",
            ]
        return "\n".join(lines)
    raise TypeError(f"not a step result: {result!r}")


def _parameter(text: str) -> tuple[str, str]:
    key, equals, value = text.partition("=")
    if not equals or not key:
        raise argparse.ArgumentTypeError(f"{text!r} is not KEY=VALUE")
    return key, value


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="commonplace-workflow",
        description="Start, advance, or record an observation about a code-scheduled run.",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    start = commands.add_parser(
        "start",
        help=(
            "start a run and print its directory; without --run the definition "
            "names where it goes"
        ),
    )
    start.add_argument("definition", help="package.module:ClassName")
    start.add_argument("--run", type=Path)
    start.add_argument(
        "--param", type=_parameter, action="append", default=[], metavar="KEY=VALUE"
    )

    step = commands.add_parser("step", help="advance a run")
    step.add_argument("run", type=Path)

    report = commands.add_parser("report", help="record one observation")
    report.add_argument("run", type=Path)
    report.add_argument("event", help=", ".join(REPORT_EVENTS))
    report.add_argument("--job")
    report.add_argument("--text", default="")

    resolve = commands.add_parser("resolve", help="record the state of an effect")
    resolve.add_argument("run", type=Path)
    resolve.add_argument("effect")
    resolve.add_argument(
        "recognition",
        choices=[Recognition.COMPLETED.value, Recognition.ABSENT.value],
    )

    release = commands.add_parser(
        "release", help="let a stopped subject be tried again"
    )
    release.add_argument("run", type=Path)
    release.add_argument("subject")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run one command. Returns 0, or 1 with a message on standard error.

    Every outcome of `step`, including blocked and uncertain, returns 0: an
    outcome is not a failure of the command. A `step` refused because another
    is running returns 1 and says the run is busy. State that cannot be
    trusted (StateError) returns 1 and says so. Malformed arguments exit
    through SystemExit with status 2, as argparse does.
    """
    arguments = _parser().parse_args(argv)
    try:
        if arguments.command == "start":
            if arguments.run is None:
                orchestrator = Orchestrator.start(
                    arguments.definition, dict(arguments.param), base=Path.cwd()
                )
            else:
                orchestrator = Orchestrator.create(
                    arguments.run, arguments.definition, dict(arguments.param)
                )
            print(orchestrator.run_dir)
        elif arguments.command == "step":
            print(render(Orchestrator.open(arguments.run).step()))
        elif arguments.command == "report":
            report = Orchestrator.open(arguments.run).report(
                arguments.event, arguments.job, arguments.text
            )
            print(f"report {report.number} recorded")
        elif arguments.command == "resolve":
            Orchestrator.open(arguments.run).resolve(
                arguments.effect, Recognition(arguments.recognition)
            )
        elif arguments.command == "release":
            Orchestrator.open(arguments.run).release(arguments.subject)
    except RunBusy as error:
        print(f"the run is busy: {error}", file=sys.stderr)
        return 1
    except StateError as error:
        print(f"the run's state cannot be trusted: {error}", file=sys.stderr)
        return 1
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
