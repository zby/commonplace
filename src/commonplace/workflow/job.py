"""The job record: one delegation to one sub-agent.

API definition only. Nothing here is implemented yet.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

Validator = Callable[[Path], Sequence[str]]
"""Judges one output file. It returns the reasons the output is refused; no
reasons means the output is valid."""


class DefinitionError(Exception):
    """The workflow definition misuses the core.

    Raised out of `step`, not turned into a blocked outcome: a run cannot
    repair its own definition.
    """


@dataclass(frozen=True, eq=False)
class Job:
    """What one worker is asked to do, and how its result is judged.

    A job is compared and hashed by identity. Whether two jobs are the same
    task is asked with `same_task_as`.

    name
        Identifies the job within a run. The definition chooses it, so it does
        not depend on the order in which paths run. Lower-case letters, digits
        and hyphens; anything else raises DefinitionError. `workflow` is
        reserved, because a block uses it for failures of steps that code
        executes, and raises DefinitionError too.
    prompt
        The task, in natural language, as the definition gives it. The core
        writes a prompt file from it, adding where to write the result, where
        to write a problem report, and on a retry the validator's messages.
        The input state uses this text, not the prompt file.
    output
        Where the result goes: a path inside the run directory. An absolute
        path, one that leaves the run directory, or one inside
        `workflow-state/` raises DefinitionError.
    inputs
        The files whose bytes the result depends on, relative to the run
        directory or absolute. Method files the job depends on are inputs too.
        The prompt is always part of the input state and is not listed here.
    validator
        Judges the output. Without one, an output is valid when it exists.
        It runs whenever the job is judged, which includes every step for an
        accepted output, so a changed validator applies to outputs accepted
        before the change. It is not part of the input state and is not
        compared between jobs, so a validator built anew each time the
        definition runs does not make two jobs differ. Within one step, the
        first declaration of a job supplies the validator; a later
        declaration of the same task is judged by it, not by its own.
    launch
        Passed to the agent orchestrator as data, for example a model or a
        tool scope. The core does not interpret it, but it is part of the
        input state: a result produced under one tool scope is not reused
        under another. It must be serializable as JSON; anything else raises
        DefinitionError.
    """

    name: str
    prompt: str
    output: str
    inputs: tuple[str, ...] = ()
    validator: Validator | None = None
    launch: Mapping[str, Any] = field(default_factory=dict)

    def output_path(self, run_dir: Path) -> Path:
        """The absolute path of the result."""
        raise NotImplementedError

    def problem_path(self, run_dir: Path) -> Path:
        """Where a worker that cannot finish writes why.

        Beside the output: the output's name without its last extension,
        followed by `.problem.md`. `lens-a.md` gives `lens-a.problem.md`,
        `result` gives `result.problem.md`, and `a.tar.gz` gives
        `a.tar.problem.md`.

        A problem report is not retried. The step that finds one gives a
        blocked outcome at once, whatever is at the output path. It moves the
        report, and any output beside it, into `workflow-state/`, where the
        failure record points to them. An output the worker flagged with a
        problem is therefore never accepted, and after the repair the next
        step finds nothing in place and hands the job out again.
        """
        raise NotImplementedError

    def same_task_as(self, other: Job) -> bool:
        """Whether both jobs ask for the same task.

        Decided by the fields a worker's result depends on: `prompt`,
        `output`, `inputs` and `launch`. `name` and `validator` are not
        compared, so a validator built anew each time the definition runs does
        not make two jobs differ.
        """
        raise NotImplementedError
