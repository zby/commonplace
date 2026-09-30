"""The job record: one delegation to one sub-agent."""

from __future__ import annotations

import json
import os
import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path, PurePath
from typing import Any

STATE_DIR = "workflow-state"
"""The directory, inside the run directory, that holds the run's state."""

RESERVED = "workflow"
"""The subject of a block on a step that code executes; no job may take it."""

_NAME = re.compile(r"[a-z0-9][a-z0-9-]*")

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
        writes a prompt file from it, normally adding the declared inputs' absolute
        paths, where to write the result, where to write a problem report, a
        request to reply in one line, and on a retry the validator's messages.
        The input state uses this text, not the prompt file, so a change to
        what the core adds, such as a new version of this package, reopens
        no job. Anything that should reopen a job when it changes belongs in
        this text or in a declared input.
    prompt_is_complete
        When true, `prompt` is the worker's whole message. The core writes
        it unchanged and appends only the refusal section on a retry.
    output
        Where the result goes: a path inside the run directory. An absolute
        path, one that leaves the run directory, or one inside
        `workflow-state/` raises DefinitionError.
    inputs
        The files whose bytes the result depends on, relative to the run
        directory or absolute. Method files the job depends on are inputs too.
        The prompt is always part of the input state and is not listed here.
        A job's own output or problem report path among its inputs raises
        DefinitionError: the worker's write would change the input state and
        refuse its own result.
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
    prompt_is_complete: bool = False

    def __post_init__(self) -> None:
        check_name(self.name, "job")
        if self.name == RESERVED:
            raise DefinitionError(f"`{RESERVED}` is reserved and cannot name a job")
        output = relative_inside(self.output)
        if output is None or output.split("/")[0] == STATE_DIR:
            raise DefinitionError(
                f"job {self.name}: output {self.output!r} must be a path inside "
                f"the run directory and outside {STATE_DIR}/"
            )
        object.__setattr__(self, "inputs", tuple(str(path) for path in self.inputs))
        owned = {self.owned_output, self.owned_problem}
        for path in self.inputs:
            if normalized(path) in owned:
                raise DefinitionError(
                    f"job {self.name} declares its own output or problem report "
                    f"{path!r} as an input"
                )
        try:
            json.dumps(dict(self.launch), sort_keys=True)
        except (TypeError, ValueError) as error:
            raise DefinitionError(
                f"job {self.name}: launch parameters are not serializable as JSON: {error}"
            ) from None

    @property
    def owned_output(self) -> str:
        """The output path relative to the run directory, normalized."""
        return normalized(self.output)

    @property
    def owned_problem(self) -> str:
        """The problem report path relative to the run directory, normalized."""
        output = PurePath(self.owned_output)
        return output.with_name(f"{output.stem}.problem.md").as_posix()

    def launch_data(self) -> Any:
        """The launch parameters as plain JSON data."""
        return json.loads(json.dumps(dict(self.launch), sort_keys=True))

    def output_path(self, run_dir: Path) -> Path:
        """The absolute path of the result."""
        return Path(run_dir) / self.owned_output

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
        return Path(run_dir) / self.owned_problem

    def same_task_as(self, other: Job) -> bool:
        """Whether both jobs ask for the same task.

        Decided by the fields a worker's result depends on: `prompt`,
        `prompt_is_complete`, `output`, `inputs` and `launch`. `name` and `validator` are not
        compared, so a validator built anew each time the definition runs does
        not make two jobs differ.
        """
        return (
            self.prompt == other.prompt
            and self.prompt_is_complete == other.prompt_is_complete
            and self.owned_output == other.owned_output
            and tuple(map(normalized, self.inputs))
            == tuple(map(normalized, other.inputs))
            and self.launch_data() == other.launch_data()
        )


def check_name(name: str, what: str) -> None:
    """Refuse a name that is not lower-case letters, digits and hyphens."""
    if not isinstance(name, str) or not _NAME.fullmatch(name):
        raise DefinitionError(
            f"{what} name {name!r} must be lower-case letters, digits and hyphens"
        )


def normalized(path: str) -> str:
    """A declared path in one spelling: `./a.md` and `a.md` are the same path."""
    return PurePath(os.path.normpath(path)).as_posix()


def relative_inside(path: str) -> str | None:
    """The normalized form of a relative path that stays inside the run
    directory, or None."""
    if not path or PurePath(path).is_absolute():
        return None
    result = normalized(path)
    if result == "." or result == ".." or result.startswith("../"):
        return None
    return result
