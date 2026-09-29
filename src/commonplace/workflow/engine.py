"""The code orchestrator.

API definition only. Nothing here is implemented yet.

A workflow definition is ordinary synchronous code. It names jobs with
`agent()`, which returns a handle at once, and asks for results with `wait()`.
A wait on a job that is not yet accepted cannot be satisfied inside this
process, so it ends the path it is on. Nothing is resumed: the next `step`
runs the definition from the top, and accepted outputs let it pass the waits
it stopped at before. No asynchronous library is involved.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from commonplace.workflow.job import Job

REPORT_EVENTS = ("launch-failed", "repair", "stop")
"""The events the agent orchestrator reports. Any other event is refused."""


# Outcomes of a step


@dataclass(frozen=True)
class Handout:
    """One job for the agent orchestrator to launch.

    `prompt_path` holds the worker's whole task. `attempt` counts the times
    this job has been handed out in the run. `launch` is the job's launch
    parameters, unchanged.
    """

    name: str
    attempt: int
    prompt_path: Path
    output_path: Path
    problem_path: Path
    launch: Mapping[str, Any]


@dataclass(frozen=True)
class Launch:
    """Launch these jobs, wait for all of them, then run `step` again.

    The jobs are every job the definition has named and that is not accepted,
    ordered by name.
    """

    jobs: tuple[Handout, ...]


@dataclass(frozen=True)
class Done:
    """The definition ran to its end and every job it named is accepted."""


@dataclass(frozen=True)
class Block:
    """Something code cannot get past.

    `subject` is a job name, or `workflow` when a step that code executes
    failed. `reason` is one short line. `record_path` is a file with the
    details: attempts, validator messages, the worker's problem report, the
    error, and the agent orchestrator's reports. `permitted` is `repair` or
    `stop`. `scope` is what a repair may change, as the definition declares it.
    """

    subject: str
    reason: str
    record_path: Path
    permitted: str
    scope: str


@dataclass(frozen=True)
class Blocked:
    """Code cannot proceed. No job is handed out in a blocked step.

    After a repair, the next `step` judges the output in place again with the
    same validator, and hands the job out again if it is still refused.
    """

    blocks: tuple[Block, ...]


@dataclass(frozen=True)
class Uncertain:
    """An effect outside the run directory may or may not have happened.

    Every later `step` gives the same outcome until the operator resolves it.
    """

    effect: str
    detail: str


StepResult = Launch | Done | Blocked | Uncertain


@dataclass(frozen=True)
class Report:
    """One observation recorded by the agent orchestrator."""

    number: int
    event: str
    job: str | None
    text: str
    recorded_at: str


# The definition's side


class Workflow:
    """Base class of workflow definitions. A definition overrides `run`.

    retry_limit
        How many times code hands a job out again after a refused or missing
        output before it gives a blocked outcome.
    repair_limit
        How many blocked outcomes for one subject permit a repair. The next
        one permits only stopping. An acceptance resets the count.
    repair_scope
        What the agent orchestrator may change during a repair.
    params
        The parameters the run was started with.
    """

    retry_limit = 1
    repair_limit = 1
    repair_scope = (
        "repair conditions (the environment, a missing input, a misnamed file) or "
        "remove a bad output; do not write or edit the content of a job's output"
    )

    params: Mapping[str, Any]

    def __init__(self, params: Mapping[str, Any] | None = None) -> None:
        raise NotImplementedError

    def run(self, ctx: Context) -> None:
        """The workflow. It must give the same jobs when it is run again on the
        same run directory, and every step in it must be safe to meet again."""
        raise NotImplementedError


class JobHandle:
    """What `agent()` returns. Naming a job does not wait for it."""

    job: Job
    path: Path

    @property
    def accepted(self) -> bool:
        """Whether the job's output is accepted in this step."""
        raise NotImplementedError

    def wait(self) -> Path:
        """The path of the accepted output.

        When the job is not accepted, the path of the definition that called
        `wait` ends here for this step. A definition that catches `Exception`
        does not catch this.
        """
        raise NotImplementedError


class Context:
    """What a definition may use while it runs."""

    run_dir: Path
    params: Mapping[str, Any]

    def agent(self, job: Job) -> JobHandle:
        """Name a job and return its handle at once.

        The job is judged here. It is accepted when its output passed its
        validator for the input state recorded at hand-out, and neither the
        inputs nor the output's bytes have changed since.

        A job that is not accepted is handed out at the end of the step,
        whether or not the definition waits on it. Naming the same job twice
        gives the same handle. One name for two different tasks, or one output
        for two jobs, raises DefinitionError.
        """
        raise NotImplementedError

    def wait(self, *handles: JobHandle) -> list[Path]:
        """The accepted outputs, in the order asked.

        When any of the jobs is not accepted, the calling path ends here for
        this step.
        """
        raise NotImplementedError

    def parallel(self, *paths: Callable[[], Any]) -> list[Any]:
        """Run independent paths and return what each returned, in order.

        Each path is a function without arguments. Each runs to its end or to
        its first wait on a job that is not accepted; a path that ends at a
        wait does not keep the others from running. When any path ended at a
        wait, the calling path ends here too. An error on one path does not
        keep the others from running; it becomes a block on `workflow`.
        """
        raise NotImplementedError

    def effect(
        self,
        name: str,
        do: Callable[[], None],
        happened: Callable[[], bool] | None = None,
    ) -> None:
        """Run a step that has an effect outside the run directory, once.

        A process can complete the effect and end before recording it. When a
        started effect has no completion record, `happened` establishes from
        the effect itself whether it took place: if it did, the effect is
        recorded and not repeated; if it did not, `do` runs. Without
        `happened` the step gives the Uncertain outcome and does not run `do`.
        """
        raise NotImplementedError


# The orchestrator


def load_definition(reference: str) -> type[Workflow]:
    """Resolve `package.module:ClassName` to a workflow class.

    Raises ValueError when the reference cannot be loaded or does not name a
    workflow definition.
    """
    raise NotImplementedError


class Orchestrator:
    """Advances one run. It keeps nothing between two calls of `step`.

    All state is in the run directory, under `workflow-state/`. Two
    orchestrators made for the same run directory behave as one.
    """

    run_dir: Path
    workflow: Workflow

    def __init__(self, run_dir: Path, workflow: Workflow) -> None:
        raise NotImplementedError

    @classmethod
    def create(
        cls, run_dir: Path, definition: str, params: Mapping[str, Any] | None = None
    ) -> Orchestrator:
        """Start a run: record which definition it uses and with what parameters.

        `definition` is a reference as `load_definition` takes it. Raises
        ValueError when the directory already holds a started run.
        """
        raise NotImplementedError

    @classmethod
    def open(cls, run_dir: Path) -> Orchestrator:
        """The orchestrator of a started run. Raises ValueError when the
        directory is not a run."""
        raise NotImplementedError

    def step(self) -> StepResult:
        """Run the definition from the top until no path can continue.

        A call of `step` means the last round is over: every worker launched
        from the previous step has returned or failed to start. Recovery in a
        fresh session therefore requires that the earlier session's workers
        have stopped.
        """
        raise NotImplementedError

    def report(self, event: str, job: str | None = None, text: str = "") -> Report:
        """Record one observation of the agent orchestrator.

        The run does not advance, and no report causes an acceptance. Raises
        ValueError for an event that is not in REPORT_EVENTS.
        """
        raise NotImplementedError

    def reports(self) -> list[Report]:
        """Every report recorded for the run, oldest first."""
        raise NotImplementedError
