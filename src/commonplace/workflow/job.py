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


@dataclass(frozen=True)
class Job:
    """What one worker is asked to do, and how its result is judged.

    name
        Identifies the job within a run. The definition chooses it, so it does
        not depend on the order in which paths run. Lower-case letters, digits
        and hyphens; anything else raises DefinitionError.
    prompt
        The task, in natural language. The core adds where to write the result
        and where to write a problem report.
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

        Beside the output, named after it: `lens-a.md` gives
        `lens-a.problem.md`.
        """
        raise NotImplementedError
