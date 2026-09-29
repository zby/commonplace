"""Start a code-scheduled run, advance it, or record an observation about it.

API definition only. Nothing here is implemented yet.

The shell parses arguments and prints. Everything it does is a call on an
Orchestrator.

    start <run> <package.module:ClassName> [--param KEY=VALUE ...]
    step <run>
    report <run> <event> [--job NAME] [--text TEXT]
    resolve <run> <effect> completed|absent
    release <run> <subject>

`resolve` and `release` are for the operator: the first after an uncertain
outcome or an effect out of step with its inputs, the second after a block
that permits only stopping.
"""

from __future__ import annotations

from commonplace.workflow.engine import StepResult


def render(result: StepResult) -> str:
    """The text the agent orchestrator reads after a step.

    The first line is the outcome: `launch`, `done`, `blocked` or `uncertain`.
    A launch has one line per job, naming its prompt file between backticks,
    followed by the job's launch parameters. A blocked outcome names each
    record file and what is permitted; it points to the details and does not
    repeat them.
    """
    raise NotImplementedError


def main(argv: list[str] | None = None) -> int:
    """Run one command. Returns 0, or 1 with a message on standard error.

    Every outcome of `step`, including blocked and uncertain, returns 0: an
    outcome is not a failure of the command. A `step` refused because another
    is running returns 1 and says the run is busy. Malformed arguments exit
    through SystemExit with status 2, as argparse does.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
