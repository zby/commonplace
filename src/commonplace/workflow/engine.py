"""The code orchestrator.

API definition only. Nothing here is implemented yet.

A workflow definition is ordinary synchronous code. It names jobs with
`agent()`, which returns a handle at once, and asks for results with `wait()`.
A wait on a job that is not yet accepted cannot be satisfied inside this
process, so it ends the path it is on. Nothing is resumed: the next `step`
runs the definition from the top, and accepted outputs let it pass the waits
it stopped at before. No asynchronous library is involved.

A definition has three kinds of step.

A job is executed by a worker, a sub-agent. Its result is a file in the run
directory, judged by code.

A mechanical step is executed by code and reads or changes only the run
directory. It is ordinary code in the definition, with no call into this
package. It runs again at every replay, so it must give the same result
whenever it runs on the same files.

An effect is executed by code and changes something outside the run
directory, such as publishing a result to its destination. The run directory
cannot show whether it took place, running it again is not harmless, and
what it produced stays outside when the run's files later change. It is
therefore declared with `Context.effect`, which runs it once.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from enum import Enum
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
    """The definition ran to its end, every job it named is accepted, and
    every effect recorded in the run was reached in this step or its state
    was recorded by the operator."""


@dataclass(frozen=True)
class Block:
    """Something code cannot get past.

    `subject` is a job name, `workflow` when a step that code executes
    failed, or `effect <name>` when a completed effect no longer matches its
    inputs or is no longer reached. No job can be named `workflow`, and a job
    name has no space, so the three kinds cannot be confused. `reason` is one short line. `record_path` is a file with the
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
    same validator. If it is still refused, the job is handed out again with
    a full set of attempts: the retry limit starts over after each blocked
    outcome. The repair limit does not. A block caused by a problem report
    leaves nothing in place to judge, because the report and any output
    beside it were moved into `workflow-state/` when the block was given.

    A block that permits only stopping ends what the agent orchestrator may
    do, not the run. Every `step` gives it again until the operator acts, with
    `Orchestrator.release` for a job or `workflow`, or by establishing the
    state of an effect. The run then continues with its accepted outputs.
    """

    blocks: tuple[Block, ...]


@dataclass(frozen=True)
class Uncertain:
    """An effect may or may not have taken place.

    Every later `step` gives the same outcome until the operator has
    established what took place and recorded it with `Orchestrator.resolve`.
    An uncertain step changes no job's state: it hands out nothing, moves
    nothing, and counts no attempt and no repair. `blocks` holds the blocks
    found in the same step, so that none is lost; they are counted when a
    later step gives them as Blocked.
    """

    effect: str
    detail: str
    blocks: tuple[Block, ...] = ()


StepResult = Launch | Done | Blocked | Uncertain


@dataclass(frozen=True)
class Report:
    """One observation recorded by the agent orchestrator."""

    number: int
    event: str
    job: str | None
    text: str
    recorded_at: str


class Recognition(Enum):
    """What can be established about an effect from the effect itself.

    COMPLETED: the effect took place in full. ABSENT: nothing of it took
    place, so running it is safe. UNKNOWN: neither can be established, for
    example because part of it took place.
    """

    COMPLETED = "completed"
    ABSENT = "absent"
    UNKNOWN = "unknown"


class RunBusy(Exception):
    """Another `step` is running on the same run."""


class StateError(Exception):
    """The run's state records cannot be trusted.

    Raised when a record the run requires is missing, does not parse, does
    not agree with the other records, or was written by a different format
    version. It is never read as an ordinary outcome such as a missing
    acceptance or an effect that never started, because that reading could
    repeat an effect. The run needs the operator.
    """


# The definition's side


class Workflow:
    """Base class of workflow definitions. A definition overrides `run`.

    retry_limit
        How many times code hands a job out again after a refused or missing
        output before it gives a blocked outcome. The count starts over when
        the job is accepted and after each blocked outcome.
    repair_limit
        How many blocked outcomes for one subject permit a repair. The next
        one permits only stopping. For a job, its acceptance resets the count.
        For `workflow`, failures are counted by the place in the definition
        where the error was raised: the innermost frame of the traceback that
        lies in the file defining the workflow class or one of its base
        classes. An error raised inside a shared helper or the standard
        library is therefore counted at the definition's line that called it,
        so two unrelated failing steps each get their repair. A step in which
        nothing that code executes fails resets these counts.
    repair_scope
        What the agent orchestrator may change during a repair.
    params
        The parameters the run was started with.
    """

    retry_limit = 1
    repair_limit = 1
    repair_scope = (
        "repair conditions (the environment, a missing input, a misnamed file) or "
        "remove a bad output; do not write or edit the content of a job's output, "
        "and do not change anything under workflow-state/"
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
    """What a definition may use while it runs.

    The run's parameters are on the definition itself, as `self.params`.
    """

    run_dir: Path

    def agent(self, job: Job) -> JobHandle:
        """Name a job and return its handle at once.

        The job is judged here. It is accepted when its output passes the
        job's current validator, the input state is the one recorded at
        hand-out, and the output's bytes are those accepted before, if it was
        accepted before. The input state
        is `Job.prompt`, the declared inputs' bytes and the launch parameters.
        It holds no absolute path of the run directory, so a run directory
        that is moved keeps its acceptances.

        An output that was never accepted, found when the input state differs
        from the one recorded at its hand-out, is refused. Such a refusal
        counts as a failed attempt, as a missing or invalid output does. An
        accepted output whose inputs change later, whose bytes someone
        changes, or that a changed validator now refuses, is not a failed
        attempt: the job is pending again with a full set of attempts.

        A job that is not accepted is handed out at the end of the step,
        whether or not the definition waits on it. At hand-out, whatever is at
        the job's output and problem report paths is moved into
        `workflow-state/` and kept there; nothing is deleted. This includes a
        refused output, an accepted output that someone changed, and one that
        a changed validator refuses.

        A job to be handed out whose declared inputs include the output of
        another job named in the same step and not accepted raises
        DefinitionError: the worker would read a result that does not exist
        yet. The definition waits on that job first. The check is made when
        the step ends, so it does not depend on the order of the two calls.

        The input state is compared at hand-out and when the output is
        judged, not in between. An input changed and changed back while the
        worker ran goes unseen, so an output made from the passing bytes can
        be accepted. The one-writer rule for a run covers inputs too.

        Naming the same job twice gives the same handle. Each job owns two
        paths, its output and its problem report. One name for two tasks that
        differ by `Job.same_task_as`, or a path owned by two jobs, raises
        DefinitionError. Paths are compared after normalization, so `a.md` and
        `./a.md` are the same path. A DefinitionError leaves the step without
        a result, so no job is handed out in a step that raises one.
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
        *,
        inputs: Sequence[str] = (),
        recognize: Callable[[], Recognition] | None = None,
    ) -> None:
        """Run an effect, once.

        An effect is a step that code executes and that changes something
        outside the run directory. `name` identifies it within the run. `do`
        performs it. `inputs` are the files the effect is made from, as a
        job's inputs are; their state is recorded before `do` runs.

        A step that changes only the run directory is not an effect and is
        not declared here.

        Code does not repeat or undo an effect. When it is completed and its
        inputs have changed since, what is outside no longer matches the run:
        the step gives a blocked outcome on `effect <name>` that permits only
        stopping, and the run does not report Done. The block is judged anew
        in every step and is not stored. It goes away when the inputs are back
        in the recorded state, or when the operator records the state of the
        effect with `Orchestrator.resolve`.

        A process can complete the effect and end before recording it. When a
        started effect has no completion record, `recognize` establishes from
        the effect itself what took place. COMPLETED: the effect is recorded
        and `do` does not run. ABSENT: `do` runs. UNKNOWN, an error raised by
        `recognize`, or no `recognize` at all: the step gives the Uncertain
        outcome and `do` does not run.

        An error raised by `do` leaves the effect started and not recorded,
        as a process that ended would. The step gives a block on `workflow`
        with the error. The next step asks `recognize` what took place.

        An effect stays owed after the definition stops calling it, for
        example because a later job's result changed a branch. When the
        definition runs to its end, every effect recorded in the run must have
        been reached in that step. One that was not is checked there: a
        completed effect gives a block on `effect <name>` that permits only
        stopping, and a started effect without a completion record gives the
        Uncertain outcome, because its `recognize` is supplied only at the
        call. A step that ends at a wait before reaching the end checks
        nothing, since the definition may still reach the call. The operator
        settles an effect that is no longer reached with
        `Orchestrator.resolve`.
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

    The state records carry a format version. Records that are missing where
    the run requires them, do not parse, disagree, or carry another version
    raise StateError from `step`, `resolve`, `release` and `open`; they are
    refused, not reshaped.

    The constructor takes a definition object and records nothing about it.
    A run driven only through the constructor cannot be opened with `open` or
    by the shell; `create` is what records the definition.
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

        A call of `step` consumes a round: it means every worker launched from
        the previous step has returned or failed to start. Attempts are
        counted per hand-out: each hand-out is one attempt, and its result is
        judged once. A job handed out before and still without an output
        counts as a failed attempt, so calling `step` again without worker
        activity uses up attempts and ends in a blocked outcome. A step that
        gives Uncertain counts nothing and moves nothing. Recovery in a fresh
        session therefore requires that the earlier session's workers have
        stopped.

        Repeating `step` gives the same outcome only where nothing is left to
        consume: on a finished run, on an uncertain effect, and on a run that
        may only be stopped.

        A step gives one outcome, the first of these that applies: Uncertain,
        Blocked, Launch, Done.

        Two kinds of record are written while the definition runs: an
        effect's start and completion, each at once and atomically, because
        the process can end inside the effect. Everything else the step
        records waits until the definition has finished running. The step
        then writes the prompt files of its hand-outs; replaces its other
        state records in one atomic rename; and after that moves
        files into `workflow-state/` as those records direct. The records
        name each file to be moved with its bytes' hash. A step that ends
        before the rename leaves those records as they were, and a prompt file it
        wrote is written again. A step that ends after the rename leaves
        moves undone; the next step first moves every such file that is
        still in place with the recorded hash, then judges. A hand-out whose
        Launch was never returned counts as a failed attempt, as any
        hand-out without an output does.

        One step runs on a run at a time. The lock is taken before the
        definition runs. It is an operating-system lock on a file under
        `workflow-state/`, so it ends with the process that holds it, and a
        crashed step leaves nothing to clear. A `step` in another process
        while one is running raises RunBusy. A second `step` within the same
        process is not a supported use, and its behaviour is not specified.
        """
        raise NotImplementedError

    def resolve(self, effect: str, recognition: Recognition) -> None:
        """Record what the operator established about an effect.

        This is the operator's act; the agent orchestrator may only stop and
        report. It applies to an effect that is uncertain, to a completed
        effect whose inputs have changed, and to an effect the definition no
        longer reaches.

        COMPLETED records the effect as completed for the inputs as they are
        now, so the next step goes past it; for an effect no longer reached,
        it means the effect stands and is no longer required to be reached.
        ABSENT clears the record: the next step runs the effect if the
        definition reaches it, and otherwise owes nothing. Raises ValueError
        for UNKNOWN, and for an effect in none of these states.
        """
        raise NotImplementedError

    def release(self, subject: str) -> None:
        """Let a stopped job, or the stopped `workflow`, be tried again.

        This is the operator's act; the agent orchestrator may only stop and
        report. The next `step` judges the subject again. If it is still not
        accepted, it is handed out with the retry limit and the repair limit
        starting over. Accepted outputs of other jobs are untouched.

        Raises ValueError for a subject that is not stopped, and for an
        effect, whose state is recorded with `resolve`.
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
