"""Start a code-scheduled run, advance it, or record an observation about it.

API definition only. Nothing here is implemented yet.

The shell parses arguments and prints. Everything it does is a call on an
Orchestrator.

    start <run> <package.module:ClassName> [--param KEY=VALUE ...]
    step <run>
    report <run> <event> [--job NAME] [--text TEXT]
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
    outcome is not a failure of the command.
    """
    raise NotImplementedError
